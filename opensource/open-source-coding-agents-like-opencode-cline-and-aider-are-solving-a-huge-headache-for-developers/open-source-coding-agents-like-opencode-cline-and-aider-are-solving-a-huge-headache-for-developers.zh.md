AI 编码代理正在激增，但由于开发者需要应对多个 API 和严重不可预测的 token 费用，运行大型语言模型 (LLM) 的经济模式正在崩溃。当代理为了完成单个请求而进行数十次模型调用时，这尤其成问题。

开发者社区的响应是开源编码代理，它们在模型之上运行一层。它们保持成本一致，因为它们独立于许多 LLM，并且可以跨许多 LLM 工作。

[OpenCode](https://opencode.ai/) 就是其中之一，它上周推出了 [OpenCode Go](https://opencode.ai/go)，一项每月 10 美元的订阅服务，旨在让这些工作负载更易于管理。

## 代理层成为焦点

OpenCode 等编码代理的兴起也预示着人工智能软件堆栈中价值定位的转变。生成式 AI 的早期关注点主要集中在 LLM 本身的能力上。像 OpenCode 这样的工具可以扫描仓库，解释开发者指令，将任务分解成多个步骤，运行命令，并在整个项目中应用更改。实际上，它们将模型的通用推理能力转化为代码库中的具体行动。

越来越多的类似开源项目正在探索这个领域。除了 OpenCode，[Kilo Code](https://kilo.ai/)（截至撰写时在 GitHub 上有 1.63 万颗星）等工具正在尝试类似的开放代理架构，同时[引入自己的付费层级](https://www.forkable.io/p/kilo-an-open-source-coding-agent)来覆盖基础设施成本。[Cline](https://github.com/cline/cline) 是一款开源的 VS Code 扩展，它诞生于 2024 年 Anthropic 的“Build with Claude”黑客马拉松，拥有 5.87 万颗 GitHub 星。与此同时，[Aider](https://aider.chat/)（目前有 4.16 万颗 GitHub 星）多年来不断发展，是知名度最高的开源编码代理之一。

这些项目标志着围绕 LLM 构建的新一层开发者工具的出现。代理是开发者交互的界面：它是一款解释任务、导航仓库并协调模型调用以生成最终输出的软件。

与更广泛的软件领域一样，订阅已成为打包它们（代理）的标准方式。诸如 [Anthropic 的 Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/)、[OpenAI 的 Codex](https://thenewstack.io/openais-codex-is-now-on-windows/) 和 [Cursor](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/) 等工具将模型访问与一个助手结合起来，该助手可以读取仓库、提出编辑建议并在整个项目中执行任务。订阅层通常将模型使用量捆绑到一个单一的月度计划中，这反映了这些系统产生的巨大提示流量。

OpenCode 从一个略有不同的角度解决这个问题。它是一个开源编码代理，在终端中运行（[桌面应用程序](https://opencode.ai/download)也提供测试版），并连接到开发者想要使用的任何模型。OpenCode 作为开发者和模型之间的中立层，允许同一个代理与来自 OpenAI、Anthropic、Google 或其他地方托管的开放模型系统一起操作。

## 开源代理正在领先

OpenCode 于 2024 年悄然出现，由 Serverless Stack ([SST](https://sst.dev/)) 团队开发，SST 是一个用于在 Amazon Web Services (AWS) 上构建应用程序的开源框架。包括 [Dax Raad](https://x.com/thdxr)、[Jay V](https://www.linkedin.com/in/jayair/) 和 [Frank Wang](https://www.linkedin.com/in/fanjiewang/) 在内的多位开发者参与其中，他们共同经营着开发者工具公司 [Anomaly](https://anoma.ly/)。

在整个 2025 年，该项目获得了显著的关注度。根据 [Runa Capital 的 ROSS 指数](https://www.forkable.io/p/the-20-hottest-open-source-startups-2e9)（快速增长的商业开源初创公司榜单），[OpenCode 仓库](https://github.com/anomalyco/opencode)在去年年底达到了 4.46 万颗 GitHub 星，使其跻身增长最快的项目之列。截至 2026 年 3 月撰写本文时，该仓库仍在持续增长，已突破 11.7 万颗星。

部分吸引力在于 OpenCode 的灵活性。许多主要的编码代理都与特定的模型提供商紧密结合——例如 Anthropic 的 Claude Code 或 OpenAI 的 Codex。而 Cursor 则在其编辑器环境中提供了一组精选模型。然而，OpenCode 允许开发者连接自己的提供商和 API 密钥，支持数十个模型提供商甚至本地托管系统。

随着模型提供商收紧对其系统访问的控制，这种灵活性变得更加重要。例如，Anthropic [最近收紧了 Claude 限制](https://venturebeat.com/technology/anthropic-cracks-down-on-unauthorized-claude-usage-by-third-party-harnesses)，此前发现一些第三方工具——[包括 OpenCode](https://github.com/anomalyco/opencode/issues/6930)——通过外部代理路由 Claude Code 订阅访问。这项更改阻止了 Claude Code 订阅凭据在 Anthropic 自己的工具之外使用，尽管开发者仍然可以通过 OpenCode 等工具内的标准 API [访问 Claude 模型](https://thenewstack.io/anthropic-agent-sdk-confusion/)。

此举似乎旨在针对一些开发者采用的模式：通过固定费率订阅运行密集的代理循环，而如果按使用量计费的 API 定价，费用会高得多。相比之下，[OpenAI 模型仍然可用](https://x.com/thdxr/status/2009803906461905202)于 OpenCode 等第三方代理中，这反映了模型提供商之间争夺开发者社区的日益激烈的竞争。

OpenCode Go 通过提供捆绑选项，进一步增强了这种模型灵活性。该每月 10 美元的计划无需开发者自行连接外部提供商，而是直接在工具内部提供对多种模型的访问，包括来自 Zhipu 的 [GLM-5](https://z.ai/blog/glm-5)、来自 Moonshot AI 的 [Kimi K2.5](https://www.kimi.com/ai-models/kimi-k2-5) 和来自 MiniMax 的 [MiniMax M2.5](https://www.minimax.io/news/minimax-m25)。这三个模型均来自中国的 AI 实验室，被普遍认为比许多西方前沿系统运行成本更低，这有助于使一个可能产生大量模型调用的工具实现低成本订阅。

当然，编码代理倾向于产生突发性的模型活动，而非持续性活动。单个请求可以触发数十次模型调用，因为代理会扫描仓库、提出更改、运行命令并修改其输出。这种模式可以在短时间内产生大量 token。

开源使这个新的代理层具有可塑性，允许开发者检查、修改和替换影响这些代理行为的组件。这种 token 密集型行为也使得 OpenCode Go 的定价值得关注：相对较低的每月 10 美元开源订阅表明运行这些模型的成本已大幅下降，足以使低利润订阅模式可行，这对于底层经济走向来说是一个有意义的信号。