大多数[AI编程工具](https://thenewstack.io/ai-coding-tools-create-more-bugs-than-they-fix/)的卖点是速度。编写提示词、获取草稿、迭代。理论上，模型越快，软件开发就越快。

[Julien Verlaguet](https://www.linkedin.com/in/julien-verlaguet-b5710a20/) 告诉 *The New Stack*，他并不认同这一观点。

这位总部位于巴黎的 [SkipLabs](https://skiplabs.io/) 的创始人兼 CEO，曾是 [Hack](https://hacklang.org/) 语言的创造者——这是一种渐进类型编程语言，支撑着 Facebook 超过 1 亿行生产代码的核心业务逻辑。他认为，整个行业一直在解决错误的问题。

> “构建正确的软件一直是一个伪装成编码问题的架构问题。”

“构建正确的软件一直是一个伪装成编码问题的架构问题，”Verlaguet 在一份声明中表示。“AI 并没有改变这一点；它只是让这个问题变得更加紧迫。”

周一，SkipLabs 推出了 [Skipper](https://thenewstack.io/skiplabs-ai-guardrails-skipper/)，这是一个闭环编程智能体，旨在接收自然语言描述或 [OpenAPI](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) 规范，并返回一个完整的、运行中的、经过验证的后端服务。没有评审周期，没有迭代，无需开发者来回沟通。该公司将其描述为介于基础模型和交付软件之间的底层基质。

## 闭环

![](https://cdn.thenewstack.io/media/2026/06/1830214e-1537985926303.jpg)

总部位于巴黎的 SkipLabs 创始人兼 CEO Julien Verlaguet。

SkipLabs 定位中的关键短语是“闭环”，Verlaguet 对其含义有着精确的界定。像 [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/)、Cursor 或 Codex 这样的工具将开发者保留在迭代循环中——提示、评审、改进、重复。他指出，Skipper 则将这一循环放在内部运行。评审和改进的过程发生在智能体内部，而不是智能体与人类之间。

“闭环不是一个功能，”Verlaguet 在声明中补充道。“它是关于 AI 编程工具应该做什么的另一种理论。当前这一代工具让开发者变得更快。下一代工具则让开发者的参与成为可选。描述你想要什么，Skipper 就会把它构建出来。”

在实践中，这意味着 Skipper 接收一个提示词，从中生成 OpenAPI 规范，构建出完整的服务——包括路由、数据映射器、验证器、TypeScript 类型、单元测试——并在 Docker 容器中运行整个服务。如果生成的代码未能通过类型检查，Skipper 会进行修复，在返回结果前最多尝试八次。整个过程无需开发者在旁监督即可运行。

Skipper 附带的常见问题解答（FAQ）做了一个类比：“你定义一个输入，运行 Skipper，然后获得一个可工作的服务——而无需担心生成的代码长什么样。”

## 状态是 AI 崩溃的地方

Skipper 背后的架构赌注是，状态管理和并发是 AI 生成代码最容易频繁失败的地方，而正确的解决方案是结构性的，而不是基于提示词的。

Verlaguet 提出这个论点已经有一段时间了。在发布前与 *The New Stack* 的一次早期交流中，他这样说道：“每次我仔细观察那些声称为 AI 带来护栏的人时，我看到的都是老一套。我看到的是更多的提示词——而看不到有人试图从头开始构建真正的护栏和真正的工具。”

他的解决方案是支撑 Skipper 的响应式运行时——源自 Verlaguet 于 2017 年在 Facebook 开发的编程语言 [Skip](https://github.com/skiplang/skip/blob/master/docs/overview/getting_started.md)。在响应式模型中，程序被定义为从输入到输出的声明式计算图。运行时会自动处理状态管理、缓存失效和并发。生成服务的 AI 模型永远不需要去推理当状态图的一部分发生变化而另一部分依赖它时会发生什么。

“我认为这是因为这是一项繁重的工作，”Verlaguet 说之所有竞争对手没有采用相同的方法，“所以做出那些宏伟的承诺要容易得多，但最终你并没有真正付诸行动。”

他将其与 [React](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/) 进行了对比——将同样的概念应用到后端服务，而不是 UI 上。[JavaScript](https://thenewstack.io/introduction-to-javascript/) 处理图节点之间的计算链接；Skip 运行时则管理其下的所有内容。

## **周一发布的内容**

周一的发布交付了核心的闭环体验：单个提示词即可转化为一个运行中的服务。Skipper 是多模型的：它根据适用性将任务路由到不同的基础模型，默认使用 Claude Opus，同时也混合使用了 Sonnet 和 Haiku。它并没有绑定到 Anthropic；模型的选择是一种架构层面的抉择，而非产品依赖。

“我们在这里不进行任何 AI 研发，”Verlaguet 在早期的讨论中告诉 *The New Stack*。“我们将模型视为一种商品。对我们来说，模型只是一个我们用上下文调用的 API；它返回结果即可。”

周一同时发布的还有：外部服务集成。Skipper 生成的服务可以调用外部 API、获取实时数据并推送到其他系统，这意味着它生产的软件不是沙盒化在本地环境中，而是从一开始就接入了真实的堆栈。

此外，两项功能将在发布后不久推出，但目前尚未准备好交付：一个是 Verlaguet 称为 SKJS 的健全、增量的 [TypeScript](https://thenewstack.io/typescript-6-0-rc-arrives-as-a-bridge-to-a-faster-future/) 实现，另一个是增量更新模式，该模式允许构建者修改规范，并让 Skipper 直接修改运行中的服务而无需重新构建。这两项功能都已经非常接近实用，因此出现在了产品路线图中，但还不足以让 SkipLabs 默认交付它们。

“我们还不会将其作为默认设置，因为我们需要解决几个细节问题，”Verlaguet 在发布前的简报中表示，“但我们应该能够在[发布后迅速]推出该类型系统。”

## 基础设施论点

与此同时，Verlaguet 通过 Skipper 提出的长远论点在于，AI 辅助开发的瓶颈究竟在哪里。他认为，模型改进的速度已经超越了用于验证输出的工具。

“在接下来的几年里，等待持续集成（CI）花费半小时到一个小时来验证代码差异（diff）将变得不可接受，”Verlaguet 告诉 *The New Stack*。“AI 正在变得越来越快，因此你需要工具来为 AI 提供护栏，而这些工具必须是增量的。”

他说，这就是健全的 TypeScript 重新实现的原理所在，它在设计上就是增量式的——当发生变化时，它可以重新检查代码，而无需从头开始重启，从而在生成过程中（而非结束时）向 AI 提供快速、可靠的反馈。

在财务方面，SkipLabs 筹集了由 Amplify Partners 领投的 8000 万美元种子轮融资，该机构在其投资备忘录中将 Verlaguet 描述为“全球最顶尖的两到三位编程语言设计师之一”。天使投资人包括图灵奖获得者、前 Meta 首席 AI 科学家 [Yann LeCun](https://www.linkedin.com/in/yann-lecun/)，以及 Cockroach Labs 的联合创始人兼 CEO Spencer Kimball。

Skipper 即日起可在 skipperai.dev 上使用。