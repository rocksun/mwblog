Anthropic 在周二于伦敦举行的首届美国境外开发者大会上，宣布了 [Claude 托管智能体](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/) 的新功能，这是该公司为运行 AI 智能体提供的托管且安全的基础设施层。

在 [使用 Claude 编码](https://claude.com/code-with-claude) 活动中，Anthropic 展示了自托管沙箱的公开测试版以及 MCP 隧道的科研预览版。作为解决当今 AI 软件工程师迫切需求的更新，团队解释了这些功能背后的机制以及现在将其推向台前的理由。

## Anthropic 沙箱：智能体的执行之地

传统上，沙箱用于隔离测试和代码实验，在 AI 模型领域也起着类似的隔离作用；它们存在于此层级，是为了保护公司内部网络免受智能体生成的恶意脚本攻击，并防止这些脚本泄露到第三方连接。

通过将 [数据隐私](https://thenewstack.io/llms-and-data-privacy-navigating-the-new-frontiers-of-ai/) 合规性、安全性和运行时控制权交给使用它的组织，该沙箱成为智能体执行工具并在客户自己的基础设施或由 Cloudflare、Daytona、Modal 或 Vercel 等托管服务提供商提供的基础设施上运行的地方。

在这种情况下，虽然工具执行移至客户环境，但智能体循环（AI 服务感知输入、推理并参与编排、上下文管理和错误恢复的持续执行周期）仍保留在 Anthropic 一侧。

## MCP 隧道：轻量级网关

随着 MCP 成为当前代理式软件开发时代（考虑到其已被 [Linux 基金会采用](https://thenewstack.io/agentic-ai-foundation-launch/)）几乎事实上的互连协议，它在 MCP 隧道中的托管功能使智能体能够连接到私有网络内的 MCP 服务器，而无需将其暴露给公共互联网。

Anthropic 对 MCP 隧道的科研预览版被描述为由客户部署的轻量级网关，可以建立“单一出站连接”，该连接由系统管理员按照 Claude 控制台中的工作空间设置进行管理。

自托管沙箱和 MCP 隧道都不需要更改现有的 Claude 托管智能体集成。在 Anthropic 的基础设施和客户自己的基础设施层之间移动是通过配置更改完成的，通常涉及将云托管的 API 令牌更换为本地身份验证密钥，并更新网络路由参数。

> “Claude 托管智能体让我们能够复制本地智能体的能力，同时具备云端智能体的可靠性、版本控制和后台执行能力……在我们的沙箱（如 Daytona）中运行它，让我们获得了对文件系统的控制权，因此我们可以即时挂载外部文件存储并安装软件包。”
> ——Ryan Chang，Clay 的 AI 工程构建者。

## 客户明确 Claude 托管智能体的使用场景

B2B 数据平台和编排层公司 [Clay](https://www.clay.com/) 正在使用 Claude 托管智能体来驱动其工程智能体 [Sculptor](https://www.clay.com/sculptor)，这是一个 AI 驱动的对话式副驾驶。Sculptor 在托管智能体和 Daytona 上自主构建、测试和监控进入市场（GTM）的工作流。

其核心理念是：兼具本地智能体的威力和云端的可靠性。

Clay 的 AI 工程构建者 [Ryan Chang](https://www.linkedin.com/in/ryancwc/?skipRedirect=true) 解释说，在构建 Sculptor 时，Clay 团队希望为它提供一种比仅在循环中使用工具更灵活、更强大的行动方式。

“Claude 托管智能体让我们能够复制本地智能体的能力，同时具备云端智能体的可靠性、版本控制和后台执行能力，”Chang 说道。“在我们的沙箱（如 Daytona）中运行它，让我们获得了对文件系统的控制权，因此我们可以即时挂载外部文件存储并安装软件包。”

## Rogo 寄希望于 Claude 托管智能体

金融领域企业 AI 公司 [Rogo](https://rogo.ai/) 目前正在为投资者和银行家开发机构金融分析师服务。该组织使用 Claude 托管智能体作为推理层，并使用 Vercel 作为其专有数据的安全执行层。

Rogo 的产品负责人 [Strib Walker](https://www.linkedin.com/in/strib-walker-560b56145/) 解释说，Claude 托管智能体满足了他公司对智能体循环功能的要求。随后，该公司还使用 Vercel 的沙箱来提供一个可以为其工作负载配置的环境。

“这让我们在专注于金融 AI 平台的核心竞争力——工具和数据的深度与广度，以及为投资者和银行家的实际工作方式构建的产品界面时，能够利用一流的基础设施，”Walker 说道。

> “我们的目标很明确：一条通往生产的高效路径，具备完整的控制、规模化和可靠性……我们很高兴能评估 Claude 托管智能体以迈出下一步，并在 Modal 的基础上构建我们的 AI 基础设施。”
> ——Andy Fang，DoorDash 联合创始人。

## DoorDash 订购 Modal 的自定义容器运行时

在线外卖公司 [DoorDash](https://www.doordash.com/?ignore_splash_experience=true&gclsrc=aw.ds&&utm_source=Google&utm_medium=SEMb&utm_campaign=CX_US_SE_SB_GO_ACQ_TETXXX_9256288225_RSTRNT_+BR_ACQ_INMKT_GenDeliveryxx_EVG_CPAx_EPX_COUSA_EN_EN_X_DOOR_GO_SE_TXT_XXXXXXXXXX&utm_term=doordash&utm_content=176836934629&kclickid=_k_CjwKCAjw8arQBhB9EiwAfIKdQnLFlpG-lJTq0XT7oIC7trMbOug6jXwwejknPXvrqHQDOGYihmH7jBoCX98QAvD_BwE_k_&utm_adgroup_id=176836934629&utm_creative_id=742508394378&utm_keyword_id=kwd-63454401416&gad_source=1&gad_campaignid=9256288225&gbraid=0AAAAADemgEtX2nNJRM1VODeqYeP0FACNl&gclid=CjwKCAjw8arQBhB9EiwAfIKdQnLFlpG-lJTq0XT7oIC7trMbOug6jXwwejknPXvrqHQDOGYihmH7jBoCX98QAvD_BwE) 正在基于 Claude 托管智能体构建内部生产力智能体，并由 [Modal](https://modal.com/) 处理执行。

Modal 是一个专为 AI 工作负载构建的云平台，其中的沙箱与 Modal 的函数、存储和网络原语共享相同的基础，为开发者提供了构建生产级 AI 系统所需的一切。Modal 的自定义容器运行时可在任何镜像上实现亚秒级启动，可扩展至数十万个并发沙箱，并按需提供 CPU 和 GPU 资源。

DoorDash 的联合创始人 [Andy Fang](https://www.linkedin.com/in/fangsterr/) 表示，他的公司正寻求以单一使命助力下一代智能体。

“我们的目标很明确：一条通往生产的高效路径，具备完整的控制、规模化和可靠性，”Fang 说道。“我们很高兴能评估 Claude 托管智能体以迈出下一步，并在 Modal 的基础上构建我们的 AI 基础设施。”

## 核心原语保持不变

自托管沙箱和 MCP 隧道都在 Claude 托管智能体支持的相同核心原语（基础 AI 模型架构构建块，包括令牌、权重和层）内工作。这些更新可能被视为重大进展，特别是考虑到 Claude 托管智能体在今年 [4 月 8 日才刚刚推出](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/)。

结合内置记忆功能的添加以及 AWS 上的 Claude 平台现已正式可用，Anthropic 表示，这些发布将智能体循环、跨会话记忆以及现在的执行和连接模型“融合在一起”，以适应企业基础设施。