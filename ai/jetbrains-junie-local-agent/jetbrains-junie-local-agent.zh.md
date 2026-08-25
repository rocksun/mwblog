**虽然大多数AI编程工具默认使用云端托管模型**，但对于那些希望将代码保留在自己机器上、避免按请求支付API费用或必须在无网络连接环境下工作的开发者来说，本地模型运行时[已成为一种可行的替代方案](https://thenewstack.io/how-to-run-a-local-llm-via-localai-an-open-source-project/)。

[诸如 Cline](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/)、[Continue](https://thenewstack.io/cursor-acquires-continue-coding/) 和 [Aider](https://thenewstack.io/developer-walk-through-of-aider-an-open-source-agentic-cli/) 等工具已经可以指向 [Ollama](https://ollama.com/) 或 [LM Studio](https://lmstudio.ai/) 等运行时。与此同时，GitHub 在[四月份](https://github.blog/changelog/2026-04-07-copilot-cli-now-supports-byok-and-local-models/)为 Copilot CLI 增加了对本地模型的支持，包括针对完全物理隔离环境的离线模式。

问题在于，“本地”方案通常仍需要开发者进行大量的组装工作。你必须选择模型并为你的硬件配置合适的量化版本，设置运行时和上下文参数，并找出哪种组合最适合该智能体。

而最后一部分确实至关重要：能在笔记本电脑上流畅运行的小型模型，在处理编码智能体所需的工具调用、推理和长时间运行的任务时，往往会显得吃力。

这就是为什么 JetBrains 现在构建了 [Junie Local](https://junie.jetbrains.com/local)，这是其编码智能体的一个免费版本，旨在完全在开发者的机器上运行。

## 本地市场

简要回顾一下，[JetBrains](https://www.jetbrains.com/)（IntelliJ IDEA、PyCharm 和 WebStorm 背后的开发者工具公司）于 [2025年1月](https://blog.jetbrains.com/junie/2025/01/meet-junie-your-coding-agent-by-jetbrains/) 推出了 Junie，这是一个嵌入在其 IDE 中的 AI 编码智能体，能够规划任务、修改代码、运行测试和检查，并利用开发者项目的上下文进行工作。此后，它[扩展为一个独立的 CLI](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/)。

Junie 本身对于本地模型并不陌生。在周一发布的一篇[博客文章](https://blog.jetbrains.com/junie/2026/08/junie-local-launch/)中，JetBrains 市场营销主管 Dmitry Savelev 指出，开发者早就可以将该智能体连接到 Ollama 和 LM Studio 等运行时，加载他们想要的任何模型，并让 Junie 在本地运行。

然而，通过 Junie Local，JetBrains 亲自挑选了模型、进行了量化，并围绕这一特定组合调整了其推理引擎和智能体框架。设置过程在 Junie 内部即可完成：运行 */local* 命令即可下载模型和推理引擎，启动本地服务器，并自动切换智能体。无需安装单独的 Ollama 或 LM Studio，无需配置端点，也无需编写模型配置文件。

第一步仅仅是从模型选择器中选择 Junie Local，它会与通常的云端托管模型列表一起显示。

![Junie的模型选择器在云端托管模型旁边提供了Junie Local选项](https://cdn.thenewstack.io/media/2026/08/d6db6ef4-gif1.gif)

*Junie的模型选择器在云端托管模型旁边提供了Junie Local选项*

一旦下载和设置完成，Junie 就会切换到本地的 Qwen 模型，该模型随后会像其他任何模型选项一样出现在 CLI 中。

![Junie在本地运行Qwen3.6](https://cdn.thenewstack.io/media/2026/08/684ace87-gif2.gif)

*Junie在本地运行Qwen3.6*

从那时起，推理完全在开发者的机器上进行。

## 幕后：为什么选择 Qwen3.6 以及为什么需要 M5 Mac

值得注意的是，JetBrains 对其模型选择非常明确，并没有选择最新、最引人注目的开源权重版本。Junie Local 使用的是 Qwen3.6-27B，这是一个在[四月份发布](https://qwen.ai/blog?id=qwen3.6-27b)的 270 亿参数开源权重模型，尽管更新的 [Qwen3.8-27B](https://thenewstack.io/qwen38-27b-local-inference/) 早在八月就已经发布并进行了改进。

> “在当前的 Mac 上，[Qwen] 3.6 胜出。”

Savelev 指出，这一选择归结为两个模型在当前 Mac 上的 Junie 中表现如何，Qwen3.8 需要启用推理模式才能与智能体可靠地工作；而开启推理模式后，任务所需时间大约延长了四倍。对于目前的 Junie Local 而言，Qwen 3.6 在可靠性和速度之间提供了更好的平衡。

“在当前的 Mac 上，3.6 胜出，” Savelev 写道。

JetBrains 在基于 mlx-vlm 的推理引擎上以 4-bit 运行 Qwen3.6-27B，而该引擎又使用了苹果的机器学习框架 [MLX](https://opensource.apple.com/projects/mlx/)。这与 [Ollama 在三月份采用的方法](https://thenewstack.io/ollama-taps-apples-mlx/)类似，当时它将其 Apple Silicon 引擎迁移到 MLX 上，以利用芯片的统一内存架构。

不过，这里有一个相当高的硬件门槛：JetBrains 证实 Junie Local 涉及约 20 GB 的下载量，并且需要 macOS 26、至少 64 GB 的统一内存以及 Apple M5 芯片或更新版本。实际上，这 64 GB 的要求使 MacBook Pro 用户处于 M5 Pro 或 M5 Max 的范畴——换句话说，这绝对是一个高端 Mac 的配置。

JetBrains 承认，这些要求将使许多可能感兴趣的开发者无法使用 Junie Local。

“我们知道配备 64 GB 内存的 M5 Mac 是一个很高的要求，” Savelev 写道。“我们不会假装不是这样。这仅仅是目前良好运行 27B 模型所需的成本，也是我们最努力想要降低的数字。”

> “我们知道配备 64 GB 内存的 M5 Mac 是一个很高的要求。我们不会假装不是这样。”

他们的目标是降低内存需求、支持更广泛的硬件，并继续优化底层堆栈。

“如果是因为过高的要求导致你无法尝试 Junie Local，请放心，我们正在努力降低它们，” Savelev 补充道。

## 本地化的回报

归根结底，硬件要求与 JetBrains 认为的本地编码智能体的真正性能瓶颈密切相关。每秒令牌数（tokens-per-second）指标衡量的是模型生成输出的速度，但智能体在开始生成答案之前，大部分时间可能花在摄取源文件、提示词和其他上下文上——即预填充（prefill）阶段。

“每个人都在对生成速度进行基准测试，” Savelev 写道。“对于编码智能体来说，事实证明这是错误的追踪数字，因为大部分时间都花在预填充上，即模型在读取文件以弄清楚发生了什么。优化预填充才是真正的增长点。”

免费且无限制的使用也改变了开发者愿意交付的工作类型。JetBrains 将 Junie Local 定位为特别适合长期、重复性和机械性的工作——例如多文件重构和重命名、填补测试覆盖率空白、依赖项升级和框架迁移——智能体可以在不让开发者担心消耗多少令牌的情况下持续工作和迭代。

“长期、重复、机械的工作正是智能体的用武之地，也是当你关注账单时你会停止使用的功能，” Savelev 写道。

> “长期、重复、机械的工作正是智能体的用武之地，也是当你关注账单时你会停止使用的功能。”

对于日常开发工作，Savelev 认为用户不太可能注意到与更强大的云端模型之间的巨大差距。不过，他也承认更复杂的架构推理仍然更适合云端模型。

当然，这也是开发者最初对本地模型感兴趣的最大原因：隐私。在本地运行整个智能体意味着没有任何外部模型提供商置于开发者和他们的代码之间，没有任何源代码、提示词或生成的更改需要离开机器。对于处理专有代码、受客户保密协议（NDA）约束或在禁止将源代码发送给第三方的环境中工作的开发者来说，这是吸引力的重要组成部分。

“下载之后的一切都在你的硬件上发生，所以你的提示词、源代码和差异对比（diffs）都保留在本地，” Savelev 写道。