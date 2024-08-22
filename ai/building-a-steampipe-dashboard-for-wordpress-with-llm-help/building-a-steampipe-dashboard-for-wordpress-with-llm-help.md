
<!--
title: 使用LLM构建 WordPress 的 Steampipe 仪表板
cover: https://cdn.thenewstack.io/media/2024/08/5e54c3a6-francesco-ungaro-hqgfte2ri9s-unsplash.jpg
-->

我如何使用 LLM 帮助创建了一个 Steamipe 插件来用 SQL 查询 WordPress，然后构建仪表板来可视化查询结果。

> 译自 [Building a Steampipe Dashboard for WordPress, With LLM Help](https://thenewstack.io/building-a-steampipe-dashboard-for-wordpress-with-llm-help/)，作者 Jon Udell。

自从我[使用 LLM 构建了一个 Steampipe 插件](https://thenewstack.io/how-llms-helped-me-build-an-odbc-plugin-for-steampipe/)以来已经有一段时间了，LLM 自那以后已经发展了，所以我决定与我的助手们合作，解决我的愿望清单上的另一项内容：一个插件，用于启用[WordPress API 的 SQL 查询](https://github.com/judell/steampipe-plugin-wordpress)。当然，Steampipe 插件只有在它的外部表为一组 Powerpipe 仪表板提供支持时才会真正发挥作用。这里有一个，用于 The New Stack 的一位选定作者。

![](https://jonudell.info/newstack/wordpress-author-dashboard.png)

这就是最终结果，但让我们来分解一下我是如何实现的。

## 查找支持的 Go SDK

Steampipe 插件通常从这里开始，就像这个插件一样，从寻找一个[Go](https://thenewstack.io/go-the-programming-language-of-the-cloud/) SDK 开始，该 SDK 包装了目标 API。如果不存在，您将不得不自己包装 API，这可以直接在插件中完成，但理想情况下是在一个独立的模块中完成——就像[hypothes.is](https://github.com/turbot/steampipe-plugin-hypothesis) 插件的情况一样，我必须为它编写支持的[hypothesis-go](https://github.com/judell/hypothesis-go)。幸运的是，在很多情况下，您要针对的 API 都有现有的 Go SDK。

> 这是一种我很少做，因此做得不好的配置仪式，但 LLM 已经见过无数次，可以快速引导我走上正确的道路。

不过，通常可能不止一个，因此插件编写者的首要任务是确定要使用哪个 Go SDK。搜索 *pkg.go.dev* 通常会给出明显的答案，在这种情况下是[https://github.com/robbiet480/go-wordpress](https://github.com/robbiet480/go-wordpress)，尽管它最近没有活动，但它被比其他任何 Go 模块都多的 Go 模块导入。

![](https://jonudell.info/newstack/go-wordpress2.png)

但事情可能会变得有点复杂。*robbiet480/go-wordpress* 是一个比 *o1egl/go-wordpress* 超前 46 次提交的 fork，而 *o1egl/go-wordpress* 又比 *sogko/go-wordpress* 超前 1 次提交。作为 *robbiet480/go-wordpress* 的用户，插件的包实际上将通过其 *go.mod* 中的一些巧妙重定向导入 *sogko/go-wordpress*。

```go
module github.com/judell/steampipe-plugin-wordpress

go 1.21.4

require (
  github.com/sogko/go-wordpress v0.0.0-20190616154547-91556a5001c7
  github.com/turbot/steampipe-plugin-sdk/v5 v5.8.0
)

replace github.com/sogko/go-wordpress => github.com/robbiet480/go-wordpress v0.0.0-20180206201500-3b8369ffcef3

//replace github.com/sogko/go-wordpress => /home/jon/go-wordpress
```


正如我[上次](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/)提到的，这是一种我很少做，因此做得不好的配置仪式，但 LLM 已经见过无数次，可以快速引导我走上正确的道路。顺便说一下，这里注释掉的 *replace* 是拼图的另一部分。在某个时候，我需要调试 *go-wordpress*，这就是您可以让本地构建的插件使用具有自定义调试逻辑的本地 Go SDK 的方法。

即使找到了正确的魔法咒语，仍然有一些障碍。我的[助手](https://thenewstack.io/elevating-the-conversation-with-llm-assistants/)之一建议使用 *go get*，但我对 Go 生态系统的薄弱知识表明 *go mod tidy* 就足够了。然后另一个助手提醒我使用 *go clean -modcache*，这确实起作用了。像往常一样，我最终会找到解决方法，但人生苦短，没有时间浪费在剃牦牛上，因此我很感谢那些帮助我减少浪费时间的帮助。

## 实现第一个表

有了 SDK，我创建新插件的起点是[github.com/judell/steampipe-plugin-hello](https://github.com/judell/steampipe-plugin-hello)，它提供三个不调用任何 API 的表。为什么？它是一个可以复制、构建、使用，然后继续使用的可工作骨架，因为我添加了真正想要的表。随着我的进行，新的插件——最初使用 *hello* 替换 *wordpress* 进行修改——大部分时间都能正常工作；或者，如果它崩溃了，可以很容易地恢复到工作状态。

> 在我的助手团队中，有两个小队，一个只有世界知识（ChatGPT、Claude），另一个既有世界知识又有本地知识（Cody、Copilot、Unblocked）。

那么，首先应该使用哪个助手呢？最近真是令人眼花缭乱：ChatGPT、Claude、[Cody](https://sourcegraph.com/cody)、GitHub Copilot 和[Unblocked](https://getunblocked.com) 都已准备好提供帮助。在这种情况下，我有点随意地向 Claude 展示了 *hello* 表中的一个，并要求创建一个新的 *wordpress_post* 表。结果，就像往常一样，是一个不错的起点。

它做对了的事情：

- 核心表函数的结构，其中（大部分）从 Go SDK 的 *wordpress.Post* 类型到相应的 Steampipe 数据库类型进行了正确的映射。
- 使用对 Go SDK 的 *Posts.List* 的调用以及配套的 *wordpress.PostListOptions*。
- 使用 *wordpress.BasicAuthTransport* 对 WordPress API 进行身份验证。

它遗漏的事情：

- 分页以处理返回 100 个以上结果的查询。
- Transform 需要将 API 风格的日期转换为数据库风格的日期。
- 利用 KeyColumns 支持类似 where date > date('2024-08-01') 的 SQL 限定符。

如果一开始就用 Unblocked，我本可以获取更符合 Steampipe 习惯用法的结果。后来，我让它提供同一张表的初始版本，它确实包含了 KeyColumns 的声明以及适当地使用了它们来让 Steampipe 将 SQL 限定符“下推”到 WordPress API。

在我的助手团队中，有两个小队，一个小队只拥有世界知识（ChatGPT、Claude），而另一个小队则兼具世界知识和本地知识（Cody、Copilot、Unblocked）。理论上，后者始终会给出更好的结果，但实际上我发现自己为了完成任务而从这两个小队招募助手。

在这种情况下，我主要与 Claude 进行了反复的迭代，同时穿插了其他助手和自己以前经验的部分内容。在一次转动曲柄的过程中——而且是在没有被要求的情况下！——Claude 向插件的 listPosts 函数添加了分页功能。对于其他改进，包括正确处理 wordpress.spc 配置文件和日期列的适当转换，我主要借鉴了自己的经验。一旦将所有内容整理好，就可以继续处理下一张表：wordpress_author。













## 构建和测试

完成表后，我构建并测试了插件。我使用以下命令构建插件：

```
go build
```

我使用以下命令测试插件：

```
steampipe plugin test
```

测试通过后，我将插件发布到 Steampipe Hub。

## 使用插件

要使用插件，您需要在 Steampipe 中安装它。您可以使用以下命令安装插件：

```
steampipe plugin install wordpress
```

安装插件后，您就可以使用以下命令查询 WordPress 数据：

```
steampipe query "select * from wordpress_post"
```

## 结论

使用 LLM 构建 Steampipe 插件可以极大地提高效率。LLM 可以帮助您快速找到合适的 Go SDK，并生成表代码。您还可以使用 LLM 完善表代码，并添加其他功能。

希望这篇文章对您有所帮助。如果您有任何问题，请随时在评论区留言。
- 分页处理返回超过 100 个结果的查询。
- 将 API 风格的日期转换为数据库风格的日期所需的 *转换*。
- 使用 *KeyColumns* 来启用 SQL 限定符，例如 *where date > date('2024-08-01')*。
如果我一开始就使用 Unblocked，我会得到一个更符合 Steampipe 风格的结果。事后，我要求它提供相同表的初始版本，它确实包含了 *KeyColumns* 的声明，以及适当的使用方式，以使 Steampipe 能够将 SQL 限定符“下推”到 WordPress API 中。

在我的助手团队中，有两个小组，一个只有世界知识（ChatGPT、Claude），另一个既有世界知识又有本地知识（Cody、Copilot、Unblocked）。理论上，后者总是会给出更好的结果，但在实践中，我发现自己需要从这两个小组中招募助手才能完成工作。

在这种情况下，我主要与 Claude 迭代，同时加入其他助手和自己先前经验中的部分内容。在一次操作中，Claude 在没有被要求的情况下，为插件的 *listPosts* 函数添加了分页功能。对于其他改进，包括正确处理 *wordpress.spc* 配置文件和日期列的适当 *转换*，我主要依靠自己的经验。一旦我将所有内容都整理好，就该继续下一个表格：*wordpress_author*。

## 实现第二个表格
有了第一个表格作为模板，下一个表格自然就快得多。这里的主要关注点是分页。*wordpress_author* 表的分页逻辑是从 *wordpress_post* 表复制的。这需要重构，我之前已经谈到过这个话题。在 [当橡皮鸭说话](https://blog.jonudell.net/2023/05/24/when-the-rubber-duck-talks-back/) 中，我写了关于使用 ChatGPT 和 Cody 来完成 [Mastodon 插件](https://hub.steampipe.io/plugins/turbot/mastodon) 的类似重构。在 [与 AI 配对：高级开发人员构建插件的旅程](https://thenewstack.io/pairing-with-ai-a-senior-developers-journey-building-a-plugin/) 中，我们看到了 James Ramirez 如何为他的 [Kolide 插件](https://hub.steampipe.io/plugins/grendel-consulting/kolide) 找到了一种优雅的基于反射的技术。

LLM 继续吸收更多世界知识，也许包括我描述 James 方法的那一栏。

我知道我想做一些类似于 James 所做的事情，但我不想引导证人，所以我没有说任何关于反射的事情，我只是向 Claude 展示了这两个表格，并提示道：

“这里有两个表格。重构以使用通用分页。”

结果，它想出了一个与 James 在 Kolide 插件中使用的实现非常相似的实现。很难确切地知道这是如何发生的。一方面，大型模型（Claude、ChatGPT）一直在不断发展，并且关于它们改进的编码能力有很多讨论。另一方面，它们一直在吸收更多世界知识，也许包括我描述 James 方法的那一栏。也许这两个因素都影响了结果，但无论如何，这都是令人震惊的。

这种技术的最终版本仍然与 Claude 提出的相同，但我推动它并让它产生了一组注释，帮助我理解它是如何工作的。以下是核心分页函数。

以下是 *wordpress_post* 表如何使用它。

所有其他表格都以相同的方式使用 *paginate*。我永远不会自己想出这个方法，而且根据 Simon Willison 的 [个人 AI 道德](https://simonwillison.net/2023/Aug/27/wordcamp-llms/#personal-ai-ethics)（“如果我不能理解和解释每一行，就永远不要提交”），我不会对最初未加注释的版本感到满意。但在与 Claude 经过了一系列解释的迭代，并随着我们一起重写它们之后，我现在对这段代码感到满意。

## 尝试并发失败
有了两个表格，我将注意力转向了仪表板。我的测试用例是这个网站 *thenewstack.io*，它是数亿个由 WordPress 提供支持的网站之一。我知道 *wordpress_post* 表太大，无法显示在仪表板上。对于帖子，我需要依靠 *date KeyColumn* 来选择子集，例如：

```sql
select * from wordpress_post where date > now() - interval '1 month'
```
但我认为，拥有一个包含该网站 10 年任期内近 3000 位作者的仪表板是可行的，也是有用的。查询 *select * from authors* 是可行的，但速度很慢。因此，我与 ChatGPT 讨论了加速该查询的方法。一个建议是启用 HTTP [keep-alive](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive)，出于某种原因，它在 Go SDK 中被禁用。（这就是为什么注释掉的 *replace* 语句出现在插件的 *go.mod* 中。）这带来了一点变化，但不足以保证扩展 fork 链以依赖于 Go SDK 的另一个变体。

我对此持怀疑态度，但 ChatGPT 愿意尝试，所以我同意了这个实验。

下一个想法是实现并发。Steampipe 引擎在 [多个级别](https://steampipe.io/blog/release-0-10-0#better-concurrency--caching--faster-control-runs) 利用并发，特别是通过 [聚合器](https://steampipe.io/docs/managing/connections#querying-multiple-connections) 在多个连接之间并行化查询。例如，我可以这样设置我的 *wordpress.spc* 配置文件：

```
[connections]
  jon = {
    url = "https://jon.wordpress.com/wp-json/wp/v2"
  }
  newstack = {
    url = "https://newstack.wordpress.com/wp-json/wp/v2"
  }
  all_wordpress = {
    connections = ["jon", "newstack"]
  }
```

现在我可以编写以下查询：

*select title, date, link from jon.wordpress_post where date > now() – interval ‘1 month’* — 查询我的网站
*select title, date, link from newstack.wordpress_post where date > now() – interval ‘1 month’* — 查询 newstack
*select title, date, link from all_wordpress.wordpress_post where date > now() – interval ‘1 month’* — 查询两者

当我运行 *all_wordpress* 版本的查询时，Steampipe 会同时查询这两个网站。但通常没有办法并行化单个连接。这将如何运作？

当查询向 API 请求多个数据块时，分页逻辑就会启动，并将查询分成一系列 API 调用。这些调用可以并行化吗？我对此持怀疑态度，但 ChatGPT 愿意尝试，所以我同意了这个实验。我们尝试了几种策略的变体，这些策略会启动一批 goroutine 并将基于偏移量的 API 调用分配给每个 goroutine。因此，一个 goroutine 使用偏移量 0 进行 API 调用，另一个使用偏移量 100 进行 API 调用，依此类推。这些调用可以按任何顺序进行，因此这种方法的成功取决于 WordPress API 是否愿意容纳这种方式。

使用一批 10 个 goroutine，查询 *wordpress_author* 表所需的时间实际上加快了大约 10 倍。结果是否一致且准确？最初似乎有效，但更激进的测试表明，虽然它 *通常* 做对了，但查询有时会返回太多结果（因为有些是重复的），有时又太少。我们尝试了许多不同的方法来使这种技术可靠地工作，最终我将其搁置一旁，将其视为失败的实验。然而，这里的关键是尝试的成本很低。我不精通 goroutine 的机制，因此我会在这方面浪费很多时间。ChatGPT 对这些机制的熟练程度使我们能够快速迭代各种方法。顺便说一句，如果确实存在解决方案，我很想听听！

## 现在添加仪表板
由于 Steampipe 公开了 [Postgres](https://thenewstack.io/puzzling-over-the-postgres-query-planner-with-llms/) 端点，您可以从 [Metabase](https://turbot.com/pipes/docs/connect/metabase)、[Tableau](https://turbot.com/pipes/docs/connect/tableau) 或其他各种可视化工具连接到它。还有 [Powerpipe](https://powerpipe.io)，以前称为 *Steampipe 仪表板*，它提供了一种 [编写仪表板](https://powerpipe.io/docs/build/writing-dashboards) 的方法，该方法使用 SQL 获取数据，并使用 HCL 定义显示和交互该数据的仪表板小部件。[github.com/judell/steampipe-mod-wordpress](https://github.com/judell/steampipe-mod-wordpress) 提供了一组 Powerpipe 仪表板，这些仪表板显示使用 WordPress 插件获取的数据，包括上面显示的作者视图。

LLM 会很容易生成有效的查询，但会在这方面失败，我不想提交一个我无法完全解释的查询。

LLM 可以通过两种方式帮助构建这些仪表板。对于 SQL，大型模型非常出色。正如 [SQL 的未来：对话式动手解决问题](https://thenewstack.io/the-future-of-sql-conversational-hands-on-problem-solving/) 中所讨论的，我发现它们在迭代易于测试、调试和理解的查询时特别有用。Simon Willison 的格言也适用于此。LLM 会很容易生成有效的查询，但会在这方面失败，我不想提交一个我无法完全解释的查询。您必须推动 LLM 使它们吐出清晰且可维护的查询，但如果您扭转它们的胳膊，它们会照做的。
然后是 Powerpipe 仪表板的 HCL 方面。HCL（HashiCorp 配置语言）在 DevOps 人员中广为人知，他们是 Steampipe 和 Powerpipe 的主要用户，大型模型对 [Terraform](https://thenewstack.io/terraform-isnt-dead/) 导向的使用方式了解很多。但 Powerpipe 将 HCL 带向了不同的方向：仍然是一种声明资源配置的方式，但在这种情况下，资源不是虚拟机和网络接口，而是仪表板小部件。因此，Powerpipe 中使用的 HCL 是一个专门的编程语言的例子，大型模型对此还不太了解。

当世界知识匮乏时，你会转向本地知识。Cody、Copilot 和 Unblocked 是三种用特定代码知识增强大型模型的方法。由于它还索引了 Powerpipe 文档，因此 Unblocked 最有帮助。例如，有一次，我需要语法将作者仪表板中的作者姓名链接到所选作者相关仪表板中的作者页面。因为我很少做这件事，所以我总是需要在文档中查找它。但 Unblocked 为我省去了麻烦。

感谢 Unblocked！

## 查询 WordPress
这里有点讽刺。WordPress 使用 MySQL 数据库，如果您有权访问，可以直接查询它。WordPress API 在该数据库周围包装了一个 REST 接口，插件反过来在该 REST 接口周围包装了一个 SQL 接口。如果您可以直接查询 WordPress，并且在您的情况下这很合适，那么请务必这样做。如果您喜欢 Powerpipe 的 HCL+SQL 风格，您甚至可以将 Powerpipe 仪表板连接到 WordPress 的 MySQL 实例。该插件可以以补充方式使用。WordPress API 的用户可能会喜欢 SQL 接口提供的抽象——以及标准化。如果您需要查询多个 WordPress 网站，Steampipe 的连接聚合器将非常方便。如果您想将来自 WordPress 的数据与来自其他插件包装的其他 API 的数据集成到 [Steampipe 集线器](https://hub.steampipe.io) 中，跨不同 API 执行字面上的 SQL JOIN 是一种令人兴奋的体验。

对我来说，这是迄今为止最顺利的插件编写项目。

这个 WordPress 插件是全新的，尚未在 Steampipe 集线器或 [Pipes](https://turbot.com/pipes) 中提供。因此，您可能想等到它正式发布。但如果您迫不及待，构建和使用 Steampipe 插件实际上非常容易。如果您想尝试扩展插件，那也很容易。我已经实现了 *table_wordpress_post*、*table_wordpress_comment*、*table_wordpress_author*、*table_wordpress_category* 和 *table_wordpress_tag*。我向 Claude 征求建议，它建议：

- table_wordpress_user
- table_wordpress_media
- table_wordpress_plugin
- table_wordpress_theme
- table_wordpress_custom_post_type
- table_wordpress_revision
如果您尝试了其中任何一个，请告诉我结果！

对我来说，这是迄今为止最顺利的插件编写项目。我将此归因于难以区分的多种因素。LLM 更加强大，我作为插件编写者的经验也更加丰富，我还了解了如何更有效地驾驭 LLM。我们 Steampipe 社区中的许多人已经设想了一种从 API 规范完全自动生成插件的方法。我们还没有做到这一点，但与此同时，很明显，LLM 辅助使这种类型的项目比以往任何时候都更容易被那些（像我一样）只有中等编程技能的人所使用。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)