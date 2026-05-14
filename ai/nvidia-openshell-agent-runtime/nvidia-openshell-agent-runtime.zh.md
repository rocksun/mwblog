驱动企业应用的软件栈是为人类构建的。它假设了人速交互、人为管理凭证以及人类对每一个关键动作的监督。自主 AI 智能体打破了这三个假设——[Nvidia](https://www.nvidia.com/en-us/) 认为，整个技术栈需要从头开始重建以适应它们。

这一论点的核心是 [OpenShell](https://github.com/NVIDIA/OpenShell)，这是一个 Apache 2.0 开源的自主智能体安全运行时，由 Nvidia AI 软件高级总监 Ali Golshan 及其团队在过去六个月中开发。

该项目是 Nvidia 更广泛的 [智能体工具包 (Agent Toolkit)](https://nvidianews.nvidia.com/news/ai-agents) 的一部分，旨在为企业提供一个受信任的环境，使智能体能够以机器速度运行，而不会暴露主机基础设施、泄露凭证或绕过治理控制。

> “如果你想赋予智能体越来越多的自主权，技术栈的最底层确实应该是一个沙箱……该智能体不应直接与你的操作系统、主机、网络或基础设施进行交互。”

“当我们回到‘智能体原生软件栈是什么样子’的原则时——如果你想赋予智能体越来越多的自主权，技术栈的最底层确实应该是一个沙箱，”Ali Golshan 告诉 *The New Stack*。“该智能体不应直接与你的操作系统、主机、网络或基础设施进行交互。”

OpenShell 解决的是架构问题。Ali Golshan 表示，目前的大多数工具都是围绕人类用户作为受信任主体而设计的——即以人类的速度在环境中控制、监控和移动的人。但智能体的运行方式截然不同。

它们速度更快，可以无限期运行，且无法完全契合为人类构建的身份和访问模型。将传统技术栈直接应用到自主智能体身上不仅会产生低效，还会造成安全漏洞。

## 沙箱第一，网关第二

OpenShell 通过分层方法解决这一问题。每个智能体（包括其套件和模型）都会获得自己的沙箱。在每个沙箱外部都有一个维护凭证和会话状态的网关。当智能体需要与外部服务（如 [ServiceNow](https://thenewstack.io/servicenow-ai-governance-agents/)、[Salesforce](https://thenewstack.io/snowflake-salesforce-launch-new-standard-to-unify-data-for-ai/) 或 [Workday](https://www.workday.com/en-us/homepage.html)）交互时，网关负责处理身份验证并将会话传递到沙箱中。

智能体本身永远不会直接持有密钥或凭证。如果发生意外，例如提示注入或执行任意命令的企图，爆炸半径会被限制在沙箱内。

## 应用层之下的策略

策略执行发生在应用层之下，使用 [Linux 内核原语](https://thenewstack.io/linux-kernel-cve-system/)，如 [seccomp](https://thenewstack.io/4-ways-to-use-kernel-security-features-for-process-monitoring/)、[eBPF](https://thenewstack.io/research-ebpf-not-always-a-silver-bullet-for-network-apps/) 和 Landlock。这就是 Ali Golshan 所描述的“内置安全”与“外挂安全”的区别。

在外挂模型中，技术栈中的每个产品都带有自己的执行机制，从而产生冲突和可靠性风险。在 OpenShell 的模型中，策略在智能体无法触及或绕过的单一水平层执行。

“在应用层之下执行策略的能力——与此同时，你并不希望每个用户都能做到这一点，因为那个层级的操作很复杂，”Ali Golshan 说。“所以，你需要合适的抽象层次和合适的执行层次。”

OpenShell 可以在任何环境上运行——桌面、[Kubernetes](https://thenewstack.io/kubernetes/)、微型虚拟机、云基础设施——并且设计为与模型、[套件 (harness)](https://thenewstack.io/ai-agent-harness-pricing-split/) 和智能体框架无关。包括 [Claude Code](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/) 和 [Codex](https://thenewstack.io/openai-codex-claude-code/) 在内的工具都可以在其中运行。

## 企业采用与开源贡献

该项目正获得 Nvidia 内部团队之外的关注。[LangChain](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) 是一家开发工具公司，其框架支撑了很大一部分企业智能体开发，该公司宣布将公开向 OpenShell GitHub 仓库提交贡献——这一进展最近将该项目推向了公众视野。

**上周在拉斯维加斯举行的 [ServiceNow Knowledge 2026](https://www.servicenow.com/events/knowledge.html) 大会上**，企业采用案例变得更加具体。Nvidia 创始人兼首席执行官黄仁勋与 ServiceNow 董事长兼首席执行官 Bill McDermott 同台宣布扩大两家公司的合作，并将 OpenShell 作为安全架构的核心。

## Project Arc 与 Action Fabric

ServiceNow 正在推出 [Project Arc](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-extends-agentic-AI-governance-from-desktops-to-data-centers-with-NVIDIA/default.aspx)，这是一个为知识工作者（包括开发人员、IT 团队和管理员）设计的长期运行自主桌面智能体。Project Arc 使用 OpenShell 作为其安全运行时，ServiceNow 为该项目做出了贡献，并将其作为企业级智能体执行的共同基础。该智能体连接到 [ServiceNow 的 Action Fabric](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) 进行治理和审计，并连接到 [ServiceNow AI Control Tower](https://www.servicenow.com/products/ai-control-tower.html) 对智能体生命周期进行监督。

ServiceNow AI 平台执行副总裁兼总经理 Jon Sigler 在一份声明中表示：“Project Arc 代表了我们与 Nvidia 持续合作的下一步，将自主执行带到了桌面。通过将 OpenShell 的运行时层与 ServiceNow AI Control Tower 相结合，并由 ServiceNow Action Fabric 提供支持，我们正在提供企业 AI 所需的治理和安全性。”

ServiceNow 的合作伙伴关系还推进了 [NOWAI-Bench](https://github.com/ServiceNow/NOWAI-Bench)，这是一个使用 Nvidia 的 [NeMo Gym 库](https://docs.nvidia.com/nemo/gym/latest/index.html) 构建的企业 AI 智能体开源基准测试套件。该套件包括 [EnterpriseOps-Gym](https://enterpriseops-gym.github.io/)，这是目前可用的要求最高的企业智能体基准测试之一，[Nemotron 3 Super](https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/) 目前在开源模型中排名第一。

## 智能体原生栈

Nvidia 通过 OpenShell 提出的更深层次论点超出了任何单一产品。Ali Golshan 将其解释为一套需要为智能体原生世界重建的原语——不仅是沙箱，还包括身份、凭证管理和策略执行，所有这些都围绕“智能体并非受信任用户”这一假设进行了重新设计。

> “你可以拥有一个智能体，然后拥有一大堆了解你业务的专业智能体，从身份或访问的角度来看，你不能像对待传统的人类团队那样对待它们……所有这些原语和构造都需要重建。”

“你可以拥有一个智能体，然后拥有一大堆了解你业务的专业智能体，从身份或访问的角度来看，你不能像对待传统的人类团队那样对待它们，”Ali Golshan 告诉 *The New Stack*。“所有这些原语和构造都需要重建。”

在 Ali Golshan 看来，自主智能体已经到来了。问题不再是它们何时到来，而是企业能否在受监管行业和敏感垂直领域（医疗、金融、联邦政府）部署它们，并具备这些环境所需的控制。他认为，OpenShell 和更广泛的智能体工具包正是为了弥合这一差距而构建的工具。

“开发者们正试图理解：如果我在一个受监管的行业工作，我需要构建什么样的技术栈，既能适用于自主智能体，又是值得信赖的？”Ali Golshan 说。“他们试图回答的最大问题是，什么东西是不会变的？有什么我可以依靠的、位于底层且稳定的东西？”

OpenShell 现在已在 GitHub 上根据 Apache 2.0 许可发布。