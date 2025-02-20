# AI 开发工具：如何使用 Dagger 容器化 Agent

![AI 开发工具：如何使用 Dagger 容器化 Agent 的特色图片](https://cdn.thenewstack.io/media/2025/02/f8b4d45f-agents-1024x667.jpg)

我们需要标准化构建[AI Agent](https://thenewstack.io/ai-agents/) 的流程，那么为什么不从[容器生态系统](https://thenewstack.io/introduction-to-containers/) 中寻找灵感呢？

这是 Docker 创建者兼 Dagger 首席执行官在 Sourcegraph 的[AI 工具之夜聚会](https://lu.ma/aidevfeb)（上周在旧金山 Cloudflare 总部举行）上的演讲中得出的结论。

“应该有一个软件生态系统，让我们可以重用彼此的东西，”他说。“我们建议 Dagger 作为这样一个生态系统。”

[Dagger](https://dagger.io/blog/public-launch-announcement) 是一个用于软件构建的[开源引擎运行时](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/)。DevOps 工程师们已经[创建](https://docs.dagger.io/quickstart/)了数千个模块，或[DAG](https://dagger.io/blog/introducing-the-daggerverse)，用于[他们自己的容器构建流程](https://dagger.dev/dev-guide/)。Dagger 构建一个包含大量专用逻辑的不可变容器，并且该设计可以很容易地应用于构建基于大型语言模型的 Agent，他认为。

“所有这些向你出售高级基础设施的初创公司……基本上，现在都是开源的，”他说。

为了演示容器如何轻松地使事情变得简单，他构建了一个简单的 AI Agent，并反过来，只使用三个函数调用就构建了一个[cURL 克隆](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/)。

## 我们以前见过这样的场景

Docker 容器之所以成功[取得成功](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)，很大程度上是因为它驯服了构建 Web 应用程序日益增长的复杂性，他回忆道。将应用程序分解成可重用的组件，并将它们容器化以方便复制。Docker[带来了](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/)可重用性和可扩展性。

“我建议我们对 Agent 做同样的事情，”他建议道。“把这些大脑装进罐子里，然后控制它们连接的内容。”

将外部系统调用添加到[LLM](https://thenewstack.io/in-2025-llms-will-be-the-secret-sauce-in-software-development/) 中是一个[重大的突破](https://thenewstack.io/ai-agents-are-about-to-blow-up-the-business-process-layer/)，并且已迅速成为[构建 AI Agent](https://www.anthropic.com/research/building-effective-agents) 的一个重要元素。它们为 LLM 提供了一个协议，如果需要完成任务，则可以调用附加函数。

随着 Agent 数量的激增以及它们执行的任务变得越来越复杂，管理这些 Agent 将很快变得难以控制。

## DAG 贯穿始终

他观察到，LLM 的工作方式就像一个良好的不可变软件构建系统一样。它们与不可变状态绑定。你将数据添加到上下文窗口，然后执行一个函数。

Dagger 有一个名为 LLM 的新谓词，它基本上是一个空状态，其中加载了[GPT-4o](https://openai.com/index/hello-gpt-4o/)（尽管它可以使用其他模型）。

使用 Dagger shell 或以编程方式，你可以将多个操作链接在一起。第一个操作可能是初始提示。

整个 Dagger API 是一组对象，每个对象都有自己的一组函数调用、模式和状态。因此，在 Dagger Shell 中，你可以创建一个容器对象：

```
LLM | with-container (Container | from alpine | with-new-file yay.txt 'my favorite language is PHP')
```

在执行上述创建容器对象的示例时，他添加了一个文件 yay.txt，以证明他的现场演示的真实性。

他指出，除了创建容器之外，该命令还将其连接到 LLM 本身。

从那里，你可以将多个对象链接在一起。

运行“构建”时，[OpenTelemetry](https://thenewstack.io/how-to-make-sense-of-ios-user-activity-with-opentelemetry/) 检测可以列出它已采取的所有步骤，包括 LLM 如何从 LLM 需要经历的各种错误（例如调用错误的安装包）中恢复以完成其目标（这对于问责制也很重要）。

他还展示了如何在第一次尝试中，创建容器的命令将 PHP 安装到容器本身中，以便后续使用。

太酷了！

## 三个函数的 cURL 克隆

他建议，LLM 工作区的最低要求至少应包括一个容器和一个状态、用于读写文件的函数以及一个构建函数（理想情况下没有参数）。
Hykes 用这些东西编写了一个 DAG，名为 [toy-workspace](https://daggerverse.dev/mod/github.com/shykes/melvin/toy-workspace@efce73bff57b24f54fcdfc387fb987dd99146f05)。

在演示中，他将 toy-workspace 安装到一个 LLM 容器中。他为 LLM 添加了一个基本的提示：

* 你是一位专家级的 Go 程序员。
* 你可以访问一个工作区。
* 使用读、写和构建工具来完成以下任务：

用户命令被分配给一个 `@assignment` 变量。

然后他给出了一些最终指示：

* 不要使用容器工具。
* 在你的代码构建之前不要构建。
* 函数是循环的。

Hykes 随后展示了他的演示技巧，运行了这个程序，只添加了指令：“为我编写一个 cURL 克隆”。一分钟后，他得到了一个运行良好的 cURL 克隆。

Hykes 说：“这就是 agent 开发的魔力。”


## Agent 调试

组织这次聚会的 Sourcegraph 高级 AI 开发倡导者 [YK Sugi](https://www.linkedin.com/in/ykdojo/) 对 Dagger 的方法表示赞赏，尤其是在调试方面。
他在 LinkedIn 消息中写道：“作为一名自己构建过 agent 的人，我知道构建 AI agent 可能是一项挑战。”

他写道：“你的错误可能来自你正在使用的 LLM API 或你为 LLM 设置的任何内容。” 它们可能是速率限制问题，或者语法与当前可用的版本不匹配。找到问题的根源可能很痛苦。

“对于 agent，你可能在它尝试遵循的路径上存在特定问题，或者 LLM 输出的工具用法的语法不正确。即使 LLM 的行为符合你的预期，你仍然可能在后端服务方面遇到问题。”

Dagger 能够检查所有日志，不仅是来自 LLM 的日志，还包括来自后端服务的日志，在这方面可能会有很大帮助。

他写道：“这似乎不仅简化了调试，而且简化了整体开发，从而更容易开发更可靠的系统。”

[Sourcegraph](https://sourcegraph.com/about) 的 AI 开发工具之夜的[整个晚上](https://lu.ma/sourcegraph) [可以在这里找到](https://www.youtube.com/watch?v=1HA9h1MnUy0)。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)