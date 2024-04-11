
<!--
title: 采用WebAssembly：缓慢而稳定是否能赢得比赛？
cover: https://cdn.thenewstack.io/media/2024/04/4d56f40d-jude-infantini-4tlnf0mztvk-unsplash.jpg
-->

我们与 WebAssembly 联合创建者和其他行业专家探讨了其采用状态、Java 用例、WASI 的重要性等。

> 译自 [WebAssembly Adoption: Is Slow and Steady Winning the Race?](https://thenewstack.io/webassembly-adoption-is-slow-and-steady-winning-the-race/)，作者 Richard Gall。

我们目前处于 [WebAssembly](https://thenewstack.io/webassembly/) 采用阶段？十八个月前，The New Stack 发布了一篇文章，[询问是什么阻碍了 Wasm](https://thenewstack.io/whats-stopping-webassembly-from-widespread-adoption/)；就在上个月，51% 的 The New Stack 民意调查受访者表示，他们仍然没有使用 WebAssembly 的个人经验。两个月前，[我们的另一项民意调查](https://www.datawrapper.de/_/emwOK/?v=2) 发现，虽然 23% 的人在工作中使用过 WebAssembly，但 42% 的人表示，虽然他们不使用 WebAssembly，但计划在它成熟时使用。

对于一项已经存在七年的技术来说——在软件行业中这是一段相当长的时间——如此多的人仍然在等待开始使用它，这很奇怪。

那么，发生了什么事？WebAssembly 是否陷入停滞不前的状态，注定永远处于青春期？还是仅仅是一个期望和观点的问题，是我们所有人学习标准炒作周期过程的症状。

## WebAssembly 目前的现状

“采用率很低，但仍呈缓慢而稳定的上升趋势，”

Suborbital 的工程总监 [Oscar Spencer](https://www.linkedin.com/in/oscarspen/) 告诉 The New Stack。Oscar 也是 [Grain 编程语言](https://grain-lang.org/) 的合著者，并为上述文章接受了 The New Stack 的采访。在文章中，他表达了对 AssemblyScript 项目撤销对 WASI（WebAssembly 系统接口）的支持感到失望，这被广泛认为不利于采用，并且会导致 Wasm 生态系统进一步碎片化。

然而，Spencer 现在确信 WebAssembly 已经克服了 2022 年的问题。“工具正在慢慢变得更好，开发人员的信心也在慢慢建立，”他说。

在某种程度上，Spencer 在 2022 年预测的碎片化 *已经* 成为现实——但它不是一个挑战，而是可以说 WebAssembly 的优势之一。

WebAssembly 的联合创始人之一 [Ben Titzer](https://www.linkedin.com/in/ben-l-titzer-6b78584/) 提出这一观点。“看到它被如此多不同的人在如此多的上下文中使用，真是太棒了，”他说。“我曾预计采用轨迹会更加集中……实际上，它通过口碑和独立实验传播了很多。”

Dylibso 的联合创始人兼首席执行官 [Steve Manuel](https://www.linkedin.com/in/stevemanuel/) 是一家构建工具以帮助团队利用 Wasm 的软件公司，他说“我们仍处于早期阶段”。他认为当前的现状主要是“系统工程师和编译器开发人员致力于针对 Wasm”。然而，他将“大公司的重要实施”——比如 Shopify，[它为其 Functions 产品使用了 Wasm](https://shopify.engineering/javascript-in-webassembly-for-shopify-functions)——视为“即将迎来采用浪潮”的标志。

“现在，每个 Shopify 应用程序开发人员都在重新调整工具以使用这个新产品，”他补充说。“无论他们是否知道 [他们] 都在将 WebAssembly 模块部署到 Shopify，伪装成平台上的应用程序。”

## 采用成功与挑战

Titzer 说，除了惊讶于该项目并没有真正受到中央管理的推动之外，他还惊讶于“现有语言针对它的渐进性”。

“虽然 C/C++ 和 Rust 显然很早就进入生态系统，但其他语言似乎慢慢地‘试水’，首先提供有限的支持，然后随着使用量的增加逐渐投入更多。”

作为一家专门开发工具来帮助工程师利用 WebAssembly 的公司的创始人，Manuel 非常适合跟踪和关注特定的采用趋势。“一个有趣的增长领域是采用用 Java 编写的业务关键型企业应用程序。”他说。这听起来可能令人惊讶，但他解释说，“许多经历过 Java 早期浪潮的人基本上将 Wasm 视为 JVM 2.0。”实际上，这意味着“Wasm 被嵌入到 Java 应用程序中，主要使用 Chicory 运行时，主要由 Dylibso 和 Red Hat 为 Java 用户构建。”

Manuel 看到 WebAssembly 取得成功的另一个领域是帮助开发人员“将插件系统整合到软件应用程序中”。换句话说，“使最终用户能够使用程序（插件）编写软件的自定义，该程序编译为 WebAssembly。”

## 对无服务器的疑问？

一种被吹捧为特别适合 Wasm 的用例是无服务器。去年，一位行业分析师[告诉 The New Stack](https://thenewstack.io/can-webassembly-solve-serverless-problems/)，他认为 WebAssembly 有潜力解决供应商锁定问题，这是无服务器的主要弱点之一。同时，[我们的分析](https://thenewstack.io/whos-leading-webassembly-adoption-so-far-vendors/)表明，Scott Logic 的 [2023 年 WebAssembly 状态报告](https://blog.scottlogic.com/2023/10/18/the-state-of-webassembly-2023) 发现无服务器 WebAssembly 的用例正在下降，从 2022 年的 36% 受访者下降到 2023 年的 13%（可能是因为较新的调查问题区分了后端服务和其他无服务器产品，例如以供应商为中心的函数即服务）。

Manuel 认为这个领域存在一些挑战。

“采用周期可能需要更长的时间，因为团队在最近可能已经为采用容器和 Kubernetes 而重新调整和重新学习技能后，被迫再次进行调整和学习，”他说。“有人在努力以更简化的方式将 Wasm 引入 Kubernetes，但这些都是最近才有的。”

## 什么将推动 Wasm 的未来？

Wasm 最终几乎可以应用于任何领域。事实上，Manuel 指出，他相信它将在 [LLM 的未来](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) 和人工智能中发挥作用，因为它能够作为此类工作负载的“安全且可移植的运行时”。

在未来几个月和几年里，有一些关键因素将推动 WebAssembly 的采用。

WASI 无疑很重要。WebAssembly 社区中的人们普遍认为 0.2 版是一个里程碑，它稳定了 WebAssembly 的设计和生态系统的基本部分，为开发人员提供了一种更简单的方法来使用该技术。

“
[WASI 预览版 2](https://thenewstack.io/wasi-0-2-unlocking-webassemblys-promise-outside-the-browser/) 是稳定接口的检查点，”Spencer 说。“预览版 1 的不稳定性 [可能] 让您害怕或无法在生产中使用 Wasm，现在已经成为过去。”

Titzer 也承认 WASI 对 WebAssembly 生态系统的重要性。“它代表了一个从一开始就拥有经过深思熟虑的平台的机会，该平台具有出色的安全属性，并且部署广泛。”然而，他指出这并不简单。“设计跨语言和跨平台的高级 API 是软件中‘[邪恶问题](https://blog.codinghorror.com/development-is-inherently-wicked/)’的一个示例。WebAssembly 社区必须努力坚持适当的分层，以避免他人陷入的陷阱。”

有趣的是，Titzer 和 Spencer 都认为 WASI 之下更令人兴奋。鉴于他们与 WebAssembly 的关系，这可能并不令人惊讶，但它仍然强调，WebAssembly 的重要性不在于达到一个每个人最终都会理解的平台，而在于它对新排列和不断重新构想的容量。

“核心 WebAssembly——指令集设计——是 WASI 之下的一个层，它将在我们尚未想到的上下文中得到采用，”Titzer 说。与此同时，对于 Spencer 来说，尽管 WASI 可能对开发人员有“直接影响”，但 [组件模型](https://thenewstack.io/webassembly-in-2024-components-are-and-are-not-the-big-story/)——支撑 Wasm 互操作性的架构指令——才是真正有价值的地方：“从长远来看，组件模型带来的便利性将使 Wasm 腾飞。”

在考虑 Wasm 采用时，另一个需要考虑的重要方面是支持与之兼容的新语言。正如 Titzer 所说，这可能是“渐进的”，但 Manuel 指出，在支持 WebAssembly 方面，语言正在赶上 [Rust](https://thenewstack.io/rust-is-surging-ahead-in-webassembly-for-now/)。例如，他指出 Go 最近增加了对 WASI 的支持，并且它“可以编译为 Wasm 以针对几乎任何 Wasm 运行时”，还提到了 [Zig](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/) 等较新的语言。“Zig 的显式内存管理 […] 非常出色，因为它提供了一个专门针对 Wasm 内存模型调整的非常方便的分配器，”他说。“用 Zig 编写的程序编译为 Wasm 后性能非常好。”

## Wasm 是否在讲述一个清晰的故事？

WebAssembly 的一个问题可能是它讲述自己清晰故事的能力。例如，对于 Docker 之类的东西，它很简单：它使在容器内构建和运行系统或应用程序的小组件变得容易。

这并不是说 WebAssembly 没有一个好故事；更确切地说，要讲述一个每个人都理解的故事很棘手。

“WebAssembly 的核心思想的传播既因其当今可以做到的热门新事物而变得更容易，也变得更困难，”Titzer 说。“外部价值故事总是依赖于上下文，因为内部价值向用例的转换是外部价值出现的地方。”

他提供了一些示例：“对于智能合约，故事是‘确定性、可验证的正确性和高效的执行，可从主流语言中定位’……对于嵌入式系统，则是‘奇怪的 CPU 现在看起来几乎相同，并且您无法意外地损坏设备’。”

Manuel 对 Titzer 有着类似的看法：“Wasm 讲述了许多引人注目的故事——既是其弱点，也是其优势。”他认为这可能解释了它为何没有按部就班地发展。“[WebAssembly] 的广泛受众意味着它具有交叉影响，但由于影响目前分散在这些领域，因此它可能是一个缓慢的消耗品。”

换句话说，WebAssembly 的采用并不像我们预期的那样引人注目，因为它被广泛分布，并跨越许多领域和用例。

## 这仅仅是期望的问题吗？

那么，也许这实际上是一个期望的问题。“我听到很多人谈论 Wasm 是什么或不是什么，但对我来说，Wasm 是一个编译器目标，”Spencer 说。“是的，它是一个具有良好安全性和可移植性特征的编译器目标，但它仍然只是一个编译器目标。用 x86 或 ARM 替换您每次说 WebAssembly 的地方，看看它是否仍然有意义。”

换句话说，当我们谈论 WebAssembly 的采用时，我们期望看到一些东西，而实际上，它的真正价值不一定可见。“作为一项基础技术，Wasm 在幕后被使用通常是不可见的——甚至可能不重要，”Titzer 建议。

考虑到这一点，也许 Wasm *是* 主流。例如，Spencer 指出，任何浏览网络的人每天都可能与 WebAssembly 互动。但话又说回来，也许没有：“当我们不再过多地谈论它时，Wasm 就已成为主流，”他补充说。

抛开行业闲聊，我们可能只需要意识到缓慢而稳定地赢得比赛。“正如我告诉 Luke [Wagner，WebAssembly 联合创始人] 的那样，”Titzer 讲述道，“‘接管世界是一个缓慢的过程，就像霉菌在物体上生长一样。成为霉菌。’”
