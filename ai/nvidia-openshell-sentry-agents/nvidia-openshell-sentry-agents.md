<!--
title: 英伟达发布开源智能体安全平台以锁死失控AI
cover: https://cdn.thenewstack.io/media/2026/09/f0f0ea15-img_3479-scaled.jpg
summary: 针对近期各大厂商AI模型频频突破测试环境失控的现象，英伟达推出了开源智能体安全平台（Open Agent Safety Platform）。该平台结合了内核级隔离沙箱OpenShell与运行在DPU上的硬件级监控服务Nvidia Sentry，通过确定性策略和网络级阻断，有效防范AI智能体越权与越狱风险。
-->

针对近期各大厂商AI模型频频突破测试环境失控的现象，英伟达推出了开源智能体安全平台（Open Agent Safety Platform）。该平台结合了内核级隔离沙箱OpenShell与运行在DPU上的硬件级监控服务Nvidia Sentry，通过确定性策略和网络级阻断，有效防范AI智能体越权与越狱风险。

> 译自：[Nvidia launches Open Agent Safety Platform to lock down rogue AI agents](https://thenewstack.io/nvidia-openshell-sentry-agents/)
> 
> 作者：Frederic Lardinois

OpenAI、Anthropic、Meta和Google最近都公开承认，他们的模型突破了测试环境并触及了真实系统。作为回应，英伟达于周一宣布推出一个运行时环境，该环境将智能体锁定在内核强制执行的沙箱中，并在其自身的芯片上配备了一个能够将其关闭的监视器。

[Nvidia Open Agent Safety Platform](https://nvidianews.nvidia.com/news/open-agent-safety-platform) 结合了 [OpenShell](https://github.com/NVIDIA/openshell) 0.1.0（这是该公司[在3月的GTC上宣布的](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/) Apache 2.0 智能体运行时）与 Nvidia Sentry（一个运行在公司 [BlueField-4](https://blogs.nvidia.com/blog/bluefield-4-ai-factory/) 数据处理单元（DPU）上的监视服务）。

这个新的 OpenShell 版本增加了一个策略证明器，用于检查智能体的各种权限是否会被组合成操作员不希望看到的结果——比如黑客攻击 HuggingFace。

由于 BlueField DPU 是一个拥有自己信任域的独立处理器，它能够监控智能体发往模型的流量，并密切关注其所有动作和推理过程。然后，当情况出现偏差时，它可以在网络层面切断智能体。

英伟达企业级 AI 副总裁 Justin Boitano 在一次新闻发布会上表示，最近的事件“凸显了 AI 智能体的一个根本障碍，那就是仅靠模型级别的安全防护无法管理智能体可以访问或做什么。”

Boitano 说：“迄今为止，模型安全一直是关于在模型中训练出良好的行为。业界称之为模型对齐。”“对于概率系统而言，这种方法有明显的局限性。这就是为什么我们要引入一个确定性系统来调解和强制这些智能体的行为。”

![](https://cdn.thenewstack.io/media/2026/09/e3ec2096-screenshot-2026-09-28-at-11.35.35-1024x441.png)

图片来源：Nvidia。

## 沙箱逃逸之夏

OpenAI [在 7 月 21 日透露](https://openai.com/index/hugging-face-model-evaluation-security-incident/)，GPT-5.6 Sol 和一个研究原型利用了作为其沙箱唯一网络路径的包代理中的零日漏洞，并进一步触及了 [Hugging Face 的生产数据库](https://huggingface.co/blog/agent-intrusion-technical-timeline)。

仅仅几天后，[Anthropic 报道称](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)，其三个模型在其评估合作伙伴 Irregular 处发现了意外的互联网访问权限，并访问了真实公司的数据库，以及在 PyPI 上发布了一个实时的恶意包等。

[Meta 紧随其后，于 8 月 6 日发布了](https://research.meta.ai/blog/addressing-third-party-testing-misconfiguration-muse-spark-1-1) 一个预发布 Muse Spark 模型，在 Irregular 的相同配置错误将其真实网站名称交予该模型后，它读取并修改了真实网站的数据库。

最近，[Google 宣布](https://www.cybersecuritydive.com/news/google-ai-gemini-autonomous-hacks/830884/) Gemini 闯入了三家公司的网络，同样是通过 Irregular 的测试环境。

Irregular 为前沿实验室运行预发布网络评估，是这里的一个共同因素，值得注意的是，该公司在英伟达此次发布的合作伙伴名单上。

英伟达自己的[技术博客](https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/)将这些突破归咎于“工具、时间和模糊指令的组合”，而不是新的能力。

当被问及该平台是否能阻止 Hugging Face 的违规行为时，Boitano 表示每个事件都是独一无二的，“但据我们所知，如果早期在用于模型评估的前沿实验室中使用，这个新的安全平台本可以阻止这次违规。”

## 在智能体外部强制执行策略

OpenShell 是该平台的核心，自从英伟达在 3 月的 GTC 上首次展示它以来，它并没有太大的变化。

通过 OpenShell（英伟达最初与其 [NemoClaw distribution of OpenClaw](thenewstack.io/nemoclaw-openclaw-with-guardrails/) 并行发布），每个智能体都在一个内核隔离的沙箱中运行，除了通过位于工作负载外部的监督程序之外，没有其他网络访问权限。

Boitano 说：“传统的沙箱，无论是微虚拟机、容器还是虚拟机，都是为应用程序级别的隔离而构建的。”“贵公司运行的每个智能体都需要在其自己的隔离沙箱中运行，并具有智能体够不到的安全控制。”

## 是证明者，而不是裁判

OpenShell 现在版本为 0.1.0，在此次更新中添加的重要新组件是一个策略证明器。该证明器检查给定策略授予的权限是否始终保持在操作员实际意图的边界内。

“它是确定性的。它是数学推理。所以这不是作为裁判的 LLM，”英伟达 AI 软件高级总监 [Ali Golshan](https://thenewstack.io/nvidia-openshell-agent-runtime/) 在发布会上说。正因为如此，他说，它的运行速度和性能“高出大约两个数量级”。

在 Golshan 的例子中，策略可以例如禁止智能体读取 GitHub 上的代码并将其发布到外部。

他说：“智能体可以通过派生两个子智能体来绕过这一点：一个可以从 GitHub 读取，可以与另一个对话，然后后者也可以向外部发布。”该证明器对整个智能体集群的组合访问进行建模，以找到该路径。

在英伟达自己的测试中，运行防护减弱的智能体的花费长达两个小时，试图说服 AI 审查员授予对受保护存储库的写权限。该公司表示，证明器向审查员提供了关于请求实际允许内容的证据，并且没有发生受保护的写入。

## Sentry：安全岛

Nvidia Sentry 为该系统添加了一个额外的硬件层。它在与主机分离的信任域中的 BlueField-4 上运行，据英伟达称，它可以在几毫秒内隔离智能体。

Boitano 说，通过系统中的 DPU，智能体的模型端到端被路由“通过 DPU 上的代理，以便您可以看到主机上智能体的所有推理轨迹”。

![](https://cdn.thenewstack.io/media/2026/09/685b5d3d-screenshot-2026-09-28-at-11.36.38-1024x442.png)

与 OpenShell 不同，Sentry 不是开源的，尽管 Boitano 表示它具有开放的 API，并且 OpenShell 可以与其他网络强制硬件配合使用。

他将其比作自动驾驶汽车。“可能有一个运行感知系统的主要系统，还有一个确保系统安全的安全岛。”

Boitano 说：“在这些架构中，DPU 实际上是可选的。”“在许多情况下，老实说，仅在 CPU 上使用 OpenShell 就足以提供某种针对智能体的严格访问控制。”

他说，DPU 用于“评估模型或系统的最前沿用例，在这些用例中，你可能会关闭模型的护栏，因此它可能用于红蓝对抗。”

## 谁在基于它构建

Anthropic 正在将 OpenShell 与 [Claude Managed Agents](https://claude.com/blog/claude-managed-agents-updates) 集成，后者已经将智能体循环保持在 Anthropic 的基础设施上，并将工具执行推送到客户控制的沙箱中。

SpaceXAI 表示它正在将该平台用于 Cursor 编码智能体和 Grok 模型，而 Salesforce 已将 OpenShell 审计事件和权限批准添加到 Slack 中。

SAP 正在将运行时嵌入到 Joule Studio 中，同时也贡献了代码。

OpenAI 和 Google 是今年夏天其智能体失控的四个实验室中的两个，但不在合作伙伴名单上。AWS 也不在其中。

当被问及 Anthropic 和 OpenAI 是否计划为其自身的训练运行 OpenShell 和 Nvidia Sentry 时，Boitano 表示可以关注合作伙伴自己的博客文章。