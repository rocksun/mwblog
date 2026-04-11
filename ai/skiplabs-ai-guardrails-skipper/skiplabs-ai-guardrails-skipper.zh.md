每个人都说 AI 需要护栏。[Julien Verlaguet](https://www.linkedin.com/in/julien-verlaguet-b5710a20/) 想知道究竟是谁在真正构建它们。

[SkipLabs](https://skiplabs.io/) 的创始人 Verlaguet 在过去的一年里一直在追问这个问题，但他并不喜欢他所发现的答案。“每当我仔细观察那些声称要[为 AI 带来护栏](https://thenewstack.io/galileo-agent-control-open-source/)的人时，我看到的都是老一套，”他告诉 *The New Stack*。“我看到了更多的提示词工程——但我没有看到有人试图从头开始构建真正的护栏和真正的工具。”

他解释其原因为：“这需要大量的工作，所以做出这些宏大的承诺要容易得多，但到头来你却什么也没做。”

Verlaguet 已经开始着手实现这一目标。SkipLabs 构建了 Skipper，这是一个用于生成和维护后端服务的专用编码智能体——它不是 [Copilot](https://thenewstack.io/microsofts-copilot-llm-team/) 那种模式的代码生成器，而是[AI 辅助开发](https://thenewstack.io/three-ai-assisted-development-skills-you-can-start-using-today/)底层的结构层，旨在让 AI 的输出具有可读性、可维护性并能快速部署。

“首先要注意的是，Skipper 不是一个模型，” Verlaguet 说。“所以，我们在这里不做任何 AI。我们将模型视为一种商品。我们使用不同的模型，大部分是 [Anthropic](https://thenewstack.io/pentagon-anthropic-model-orchestration/)，但不限于此。对我们来说，模型只是一个我们带着上下文调用的 API，它返回结果。”

Verlaguet 的论点始于延迟问题，他说道。

“在未来几年里，让 [CircleCI](https://thenewstack.io/circleci-extends-ci-cd-platform-beyond-the-cloud/) 花半小时到一小时来验证一个 diff（代码差异）是不可接受的，”他说。“AI 变得越来越快，因此你需要工具来为 AI 设置护栏，而且这些工具需要是增量的。”

## 增量优势

Verlaguet 的职业生涯建立在增量开发的想法之上。在 Facebook，他创建了 [Hack](https://hacklang.org/)，这是一种渐进类型的 [PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/) 方言，在 [TypeScript](https://thenewstack.io/typescript-6-0-rc-arrives-as-a-bridge-to-a-faster-future/) 引领潮流之前就为动态语言引入了类型系统。

“当 Julien Verlaguet 和 Facebook 团队创建 Hack 时，他们正在解决一个特定的问题：PHP，即驱动整个 Facebook 代码库的语言，从根本上说是类型不安全的，” SkipLabs 的软件工程师 [Hugo Venturini](https://www.linkedin.com/in/venturini/) 在一篇[博文](https://skiplabs.io/blog/future_of_tools_for_ai)中写道。

然而，Venturini 补充道：“在 Facebook 的运作规模下，这不仅是一个审美问题，更是一个工程隐患。”

“所以，Julien 构建了 Hack：一个渐进类型、经过严格标注的替代品，写起来肯定不如 PHP 愉快，” Venturini 写道。“它更冗长，要求精确，需要你确切地表达你的意图。然后，他们让 Facebook 的每一位工程师都切换到了 Hack。”

随后，Verlaguet 构建了 Skip，这是一个围绕“当输入改变时，你不必从头重新计算所有内容”这一原则组织的完整响应式编程环境。SkipLabs 公司表示，由于看到在 Meta 之外没有类似的框架，Julien 和团队创立了 SkipLabs，旨在将响应性带给下一百万名软件工程师。

SkipLabs 的软件工程师 [Lucas Hosseini](https://www.linkedin.com/in/lucas-hosseini-73126a41/?locale=en) 在一篇博文中提供了他对响应式编程的定义：“从实际意义上讲，[响应式编程](https://www.baeldung.com/cs/reactive-programming)是一种表达计算的声明式方式：与其手动处理状态转换，你只需将状态描述为多个输入的函数。”

Verlaguet 于 2020 年离开 Meta，围绕响应式技术创办了他的初创公司；Skipper 正是这项工作的结晶。

## 两个部分，一个栈

Skipper 有两个组件。第一个是建立在新的、完备且增量的 TypeScript 实现之上的开发环境。Verlaguet 刻意选择了 TypeScript。

“AI 非常擅长 TypeScript 和 [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/)，”他说。“我认为从这两者之一开始，可能会得到最好的结果。”完备性在技术上至关重要：带有漏洞的类型系统无法支持[可达性分析](https://help.sonatype.com/en/reachability-analysis.html)——即代码更改会影响哪些程序状态的[调用图](https://en.wikipedia.org/wiki/Call_graph)映射——而这正是 Skipper 的核心。

“如果类型系统不完备，你就不知道类型是什么，不知道你在调用什么，也就无法构建调用图，” Verlaguet 说。一个响应式运行时位于其上，在代码更改时更新实时状态，这样程序就永远不必从头开始重启。

第二个组件是安全带（harness）——智能体编排层。Verlaguet 表示，虽然结构上很经典（计划、生成测试、生成代码），但它建立在相同的增量框架之上，因此生成和修复是在独立的部分上并行进行的，而不是在整个代码库中顺序进行的。这种组合意味着 Skipper 可以快速摄取 diff，仅运行受更改影响的测试，并在不关停的情况下更新实时服务。

## 在其擅长的领域击败 Claude Code

在内部基准测试中，Verlaguet 声称 Skipper 在其后端服务提示语料库上的测试通过率超过 90%，而 Claude Code 在同一语料库上的通过率为 20%。但他对这种比较的范围很谨慎。

“Claude Code 做的事情更多，”他说。“但在我们所做的领域，我们做得更好。”他们所做的是生成后端服务——通用的后端服务，而不是预定义模板的目录。“所有的代码都是从头开始生成的，”他说。

Verlaguet 表示，他相信 AI 将推动越来越多的软件进入服务架构，这不是因为当今的构建方式如此，而是因为有状态的服务使迭代式 AI 开发变得可行。他用编译器作为例子。

“五年后，我很确定你会希望这个编译器由 AI 构建。这意味着什么？”他问道。“这意味着每次 AI 想要对该编译器进行迭代时，它都必须等待半小时。这没有任何意义。”将编译器转变为具有状态的服务，向其发送请求，AI 就可以在没有这些开销的情况下进行迭代。

不过，Skipper 仍处于早期阶段，Verlaguet 表示公司有望在下个月发布公告。他将目前的用户群描述为“我们和我们的朋友”。

Verlaguet 将 SkipLabs 定位为一个专业的编码智能体商店，并预计这一领域将变得拥挤。“我认为我们将看到拥有不同工具、工具链的不同智能体，它们在处理某些事情上表现更好，”他说。

他认为，护栏问题将把真正的强者与喧嚣区分开来。

“这里有一家公司，真正为你 AI 生成的代码构建了你一直在寻找的护栏，” Verlaguet 说。

这种技术雄心并没有被行业观察者忽视。

Futurum Group 的分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 评价 SkipLabs 的技术成果为：“非常令人着迷，反映了在我们当前的非确定性世界中软件是如何变化的。该框架和后端服务不再使用传统但有时网络负担较重的声明式框架来实现实时响应，而是基本使用声明式机制来推理代码块应该做什么，并在计算图中跟踪任何依赖关系。”

与此同时，AI 安全平台提供商 [Arcjet](https://arcjet.com/) 的 CEO [David Mytton](https://www.linkedin.com/in/davidmytton/) 告诉 *The New Stack*，Skipper 确实在解决一个新出现的问题。

“我最近与多位技术负责人进行了多次对话，行业仍在努力接受代码审查的消亡，”他说。“我们处于一个新世界，旧的安全模型正在崩溃，因为它假设代码是人写的。当智能体处理实现时，审查无法跟上进度——而且它们很快就会管理从计划到部署的全周期。安全必须融入整个过程，从开发环境到运行时。”

## 可读性时代的终结

Venturini 在他的文章中说：“智能体从冗长中获益。冗长、精确、明确的工具输出比简短、巧妙、针对人类优化的输出更容易解析。”

他认为，大声、具体的失败比为了开发者体验而掩盖的错误更有用。他说，强大的类型系统之所以重要，不在于作为护栏，而在于作为描述代码预期行为的最信息密集型手段。

此外，Venturini 在博客中指出，这预示着工具领域的某种分裂。为人类作者构建的语言和环境将继续存在，因为“人类哪儿也不会去”。但与此同时，新一代工具正在出现，以智能体为主要消费者：严格、形式化说明、不容忍歧义，他指出。

SkipLabs 将 Skipper 置于这第二个阵营中。其兼容 TypeScript 的类型检查器 SKJS 在标准 TypeScript 不完备的地方做到了完备。这种权衡让它对人类来说更难使用，但对智能体来说更有用。Venturini 指出，响应式运行时强制执行显式的依赖契约，这对于手写代码的开发者来说可能觉得多余，但正是智能体推理代码库中因果关系所需要的。

底层的论点是：如果智能体生成了大部分代码，而这些智能体使用的工具是围绕人类可读性设计的，那么一个显著的能力上限就被留在了那里。他说，你是在要求智能体在别人的媒介中工作。

“我们让工具更具可读性是为了吸引更多开发者，” Venturini 写道。“我们将让它们变得不那么可读——更精确、更形式化、更机器原生——从而获得更好的智能体。编程语言的可读性时代漫长而多产，而现在它正走向终结。”

## 时间线

以下是 Verlaguet 在创建 Skipper 及其潜在产品发布之前取得的成就的时间线：

* 2012 年，Verlaguet 创建了 Hack，为 PHP 用户社区提供静态类型、异步和泛型。
* 2014 年，Facebook 在 MIT 许可下开源了 Hack 和 HHVM。
* 2017 年，他创建了 Skiplang，这是一种专为响应式编程设计的编程语言。
* 2018 年，Facebook 在 MIT 许可下开源了 Skip。
* 2019 年，Facebook 开发了 SKAI (Skip for AI)，将响应性应用于 AI 应用。
* 2020 年，Skip 增加了一种语言——一个独立的运行时，替代了 Facebook 使用的其他基础设施。
* 2024 年，Skip Framework 发布：一个原生支持 TypeScript 的框架，用于编写和运行基于 Skip Runtime 的响应式函数和服务。
* 2025 年，SkipLabs 宣布获得来自 Amplify Partners 的 800 万美元种子轮融资。