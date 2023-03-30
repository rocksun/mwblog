# 使用 fluentbit、go 和 graphs 填充并保持最新的 CMDB

翻译自 [Populating and keeping up-to-date a CMDB using fluentbit, go, and graphs](https://itnext.io/populating-and-keeping-up-to-date-a-cmdb-using-fluentbit-go-and-graphs-ddf486b0cfdf) 。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*Vj4vrw6son51-x2ypPogQg.png)

假设你经营一项服务，我们称其为“My Service”。你可能对 My Service 直接调用的其他服务的依赖关系有一个相当好的了解。在上面的图表中，这些将是“ Nearby Service ”和“ Well-known Service ” 。但是你可能不清楚这些服务的依赖关系，而这些服务的依赖关系也是你的依赖关系。

好了，现在你的 My Service 已经平稳地运行了一段时间。其中一个开发小组实现了一个很棒的新功能……却没有告诉任何人它引入了一个新的依赖关系。看起来这应该是需要知道的信息，对吗？

## 映射服务依赖关系——通用方法

### 注册授权

也许你以前见过这种情况。你的 IT 组织要求每个人在某个集中工具中注册他们的服务及其依赖关系。也许这个工具是机器可查询的……也可能不是。也许每个人一开始都热情地输入他们的直接依赖关系。但是，根据我的经验，我还没有见过以下两件事情中的任何一件在此之后发生。第一，通常很少或根本没有努力建立一个强大的依赖关系图——一个显示所有相互依赖关系的模型，让你看到跨越图的多个边缘的依赖关系。第二，我很少或几乎没有看到服务所有者像最初注册它们那样勤奋地更新他们的文档依赖关系。我并不认为这两个问题都是普遍存在的（我真的不知道），但我走过一些路，我看到它们发生了很多次。这很令人沮丧，因为缺乏关于企业全面依赖关系的完整信息会以多种不同的方式妨碍组织。

### 自动发现

另一种方法是使用自动化——要么是一个专门构建的工具，要么是包括发现、持久化和呈现依赖关系功能的工具（例如 ServiceNow 、 DataDog APM 、 Dynatrace ）。我曾经使用过其中一些，如果你使用其中一个并喜欢它，那太好了。我对它们唯一的问题是，它们很少便宜，通常需要配置访问服务和/或服务托管基础架构本身。它们与您现有工具的互操作性肯定会有所不同。如果您还没有使用这些产品之一，也许您不想花费资金或时间来部署和支持其中之一。

## 发现便宜的服务依赖

尽管标题有点误导（我的过失），但本文并不是关于将 CMDB（配置管理数据库）完全填充有关服务 CI 的信息，这些信息可能包括基础操作系统和/或中间件、使用的编程语言等等。但我将要概述的方法在某些情况下可能适用，并且我们可能会在最后讨论其中的一些情况。

我想要的是更基本的东西——我只想开始构建一个服务依赖关系图，显示服务/应用程序之间的相互依赖关系，无论是直接还是间接的。而且我想在对服务和应用程序所有者（或者实际上是任何其他人）造成尽可能少的负担的情况下完成这项工作。这意味着要问一下，我们今天可以访问哪些信息，可以用来构建这个图形？

## 每个人都有日志

我们有日志，您也有日志。每个人都有日志（我希望如此）。在许多组织和/或企业中，这些日志通过共享的传输/路由架构进行处理。那么，如果我们可以仅基于已经写入日志事件中的信息构建（并保持更新）服务依赖关系图呢？

我从经验中知道，我们大多数服务在调用另一个服务时已经写了日志事件。而这些日志事件通常包括目标服务的地址或 URL……由于主机名/URL 标准的原因，大多数主机名包括服务的名称，遵循像 `api.service.mycompany.com` 这样的标准格式。这是很重要的，因为它有助于在事件中提取服务名称，而不需要额外的元数据（从而避免需要应用程序开发人员额外的工作）。

### 那些不编写这些类型事件的应用程序/服务呢？

好吧...通常来说，除非有明确的理由（最好包括对被要求遵守规定的人产生具体利益），否则强制性的要求通常不会受到好评。所以我们不会一开始就说：“听好了，你们这些原始人，按这种格式编写事件，否则就完了。”相反，我们希望证明这样做确实有真正的价值，并且展示这个价值是本文的一个重要部分。因此，个人认为，除非我能证明遵守规定会产生某些超出...遵守规定的好处，否则我喜欢把这些讨论留到后面。

## 规范化日志事件

第一步是将日志事件标准化为一些通用的结构，以便我们可以尽可能轻松地从中提取所需信息。正如我之前所说，我想在不要求其他人做任何事情的情况下完成这项工作。所以我在想...让我们在日志传输/路由层中完成这项工作。

对于这个示例，我使用的是 Fluent Bit 。当然，您可以使用其他技术/平台来完成以下操作，但我喜欢 Fluent Bit 的一个特点（除了它非常小、轻巧和快速外），就是它具有高度可定制的数据管道。该管道基于可配置插件的模型。插件的数量和范围不如 Fluent Bit 的老兄弟 Fluentd 多，但我发现它的插件已经非常强大了，而且它比 Fluentd 更快且占用更少的资源。但如果您使用的不是 Fluent Bit ，则请专注于我们正在实施的概念，而不是细粒度的机制——这可能在日志平台上差异很大。


### Fluent Bit 配置

在这种情况下，我们充当多个服务的集中日志处理器。我们需要模拟从每个服务接收日志，为此，我们需要像这样的 INPUT 小节：

```
[INPUT]
    Name    dummy
    Dummy   {"service":"ui", "request":"GET https://api.mycompany.com/resources"}
```


This uses Fluent Bit’s dummy input plugin to generate fake log lines at a default rate of one per second, each of which is a JSON record whose contents are the value of the Dummy field. We will need one of these stanzas for each direct dependency we want to simulate. Alternatively, we could write some simple code to write the lines to a file and then configure Fluent Bit to read that file using its tail plugin, but we’re going the dummy route here.
这使用 Fluent Bit 的 dummy 输入插件以每秒一条的默认速率生成假日志行，每行都是一个 JSON 记录，其内容是 Dummy 字段的值。对于我们想要模拟的每个直接依赖项，我们将需要这些节之一。或者，我们可以编写一些简单的代码来将这些行写入文件，然后配置 Fluent Bit 以使用它的 tail 插件读取该文件，但我们在这里采用 dummy 路线。

We also need to configure Fluent Bit to send the log events to our event processor, which is the application we’ll build to generate the actual dependency graph. For that we use an output stanza like this:
我们还需要配置 Fluent Bit 以将日志事件发送到我们的事件处理器，这是我们将构建的用于生成实际依赖关系图的应用程序。为此，我们使用这样的输出节：

[OUTPUT]
    Name    http
    Match   *
    Host    localhost
    Port    9000
    URI     /event
    Format  json
This tells Fluent Bit to send all log events via http to localhost:9000/event in JSON format.
这告诉 Fluent Bit 通过 http 以 JSON 格式将所有日志事件发送到 localhost:9000/event 。

But we’re still missing a piece — we need to extract the name of the target service from that request field in the record. For this we can use a filter plugin of type parser — these are commonly used to allow flexibility in log formats, and here we’ll use one to pull out the piece of that request field that we actually need.
但我们仍然遗漏了一块——我们需要从记录中的 request 字段中提取目标服务的名称。为此，我们可以使用 parser 类型的过滤器插件——这些通常用于允许日志格式的灵活性，在这里我们将使用一个来提取我们实际需要的 request 字段。

For this, we need a parsers file (you can actually configure parsers in the main configuration file, but the documented convention is to use a separate file for parser stanzas, and that’s what we’re doing here), let’s suppose we store it at /var/fluentbit/config/parsers.conf. In that file we add a stanza like this:
为此，我们需要一个解析器文件（您实际上可以在主配置文件中配置解析器，但记录的约定是为解析器节使用一个单独的文件，这就是我们在这里所做的），假设我们将它存储在 /var/fluentbit/config/parsers.conf 。在该文件中，我们添加这样的节：

[PARSER]
    Name            extract_target
    Format          regex
    Regex           ^\S+\s+\w+\W+(?<target>[\w\-]+).*$
This creates a named parser called extract_target, which uses a regular expression (Fluent Bit uses the Onigmo regex library — the regex documentation for it is here) to discard everything but the first word (or hyphenated string) of the hostname and add it to the event as a field named target.
这将创建一个名为 extract_target 的命名解析器，它使用正则表达式（Fluent Bit 使用 Onigmo 正则表达式库——它的正则表达式文档在这里 ）来丢弃主机名的第一个单词（或带连字符的字符串）以外的所有内容，将其作为名为 target 的字段添加到事件中。

To link this back to our main Fluent Bit configuration file, we add to the main file this piece:
为了将其链接回我们的主 Fluent Bit 配置文件，我们将以下部分添加到主文件：

[SERVICE]
    Parsers_File    /var/fluentbit/config/parsers.conf

[FILTER]
    Name        parser
    Match       *
    Key_Name    request
    Parser      extract_target
    Reserve_Data    true
The Reserve_Data true line is important here, because it tells the parser to keep the other (non-parsed) fields in the event — without it, our event would contain only the parsed target field.
Reserve_Data true 行在这里很重要，因为它告诉解析器将其他（未解析的）字段保留在事件中 — 没有它，我们的事件将只包含已解析的 target 字段。

When we’re ready, we can start Fluent Bit with fluent-bit -c /var/fluentbit/config/fb.conf (replace the path with wherever you’re storing your main config file).
准备就绪后，我们可以使用 fluent-bit -c /var/fluentbit/config/fb.conf 启动 Fluent Bit（将路径替换为您存储主配置文件的位置）。