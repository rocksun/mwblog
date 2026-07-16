周二，AWS [宣布](https://aws.amazon.com/blogs/security/security-hub-adds-ai-workload-protection-and-multicloud-support-for-microsoft-azure/) 扩展了其安全运营服务 [Security Hub](https://aws.amazon.com/security-hub/)，除现有的 AI 工作负载保护工具外，该服务现在还能监控 Microsoft Azure 资源。这是该服务首次实现对 AWS 以外资源的本地监控。

此次发布共包含四项重大更新：[Azure 资源监控](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-hub-supports-monitoring-microsoft-azure/)、Amazon GuardDuty AI 保护、[GuardDuty AI 驱动的调查](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-guardduty/)以及 Security Hub AI 清单。除了尚处于预览阶段（在 10 个 AWS 区域）的调查功能外，其余功能现已全面可用。这些功能共同实现了 AWS 在 RSA 大会前夕于 3 月份[承诺](https://aws.amazon.com/blogs/security/aws-security-hub-is-expanding-to-unify-security-operations-across-multicloud-environments/)的多云扩展计划。

## AWS 助力 Azure 安全保障

此次最引人注目的更新是支持对 Azure 资源的监控。Security Hub 可以自动发现客户的 Azure 虚拟机、容器镜像、无服务器 Function Apps 和身份信息。随后，它会使用 [CIS Azure Foundations Benchmark](https://www.cisecurity.org/benchmark/azure) 检查这些资源是否存在配置错误、暴露于互联网的情况以及脆弱的软件。所有来自 Azure 的调查结果都会与 AWS 的调查结果并列显示在同一个排名队列中，并可以触发团队现有的自动化工作流程。

正如 AWS 安全服务总监 Michael Fuller 在发布这些功能的博文中写道：“你的工作负载会迁移到新的云环境，你的安全保障也应该同步到位。”

监控 Azure 资源的成本与监控同等 AWS 资源的成本相同，且不收取额外的平台费用，并提供独立的 30 天免费试用。

## 保护 AI 工作负载

相比之下，[GuardDuty AI 保护](https://docs.aws.amazon.com/guardduty/latest/ug/ai-protection.html)则是一个非常以 AWS 为中心的产品。它的目标是检测 Amazon Bedrock 和 SageMaker 工作负载特有的威胁，包括异常模型调用、提示注入尝试（通过与 Bedrock Guardrails 集成），以及 AWS 所称的“成本窃取”——即攻击者利用窃取的凭据在他人的账户上累积高额的推理费用。

Fuller 指出，这是一种他经常见到的模式。“我最近与一位安全主管交谈，”他写道，“他们的团队发现一个被入侵的服务账户调用了数千次基础模型，仅仅是因为财务部门标记了账单。”

AI 驱动的调查功能目前处于预览阶段，它会对 GuardDuty 的调查结果进行自动化的初步筛选，以区分真实威胁与噪音。每次调查都会根据 90 天的相关活动返回包含置信度评分、[MITRE ATT&CK 分类](https://attack.mitre.org/)以及补救建议的处置方案。AWS 声称，该分析能在“几分钟内完成以前需要数小时的工作”。

AI 清单功能现已包含在 Security Hub 的基础计划中，无需额外费用。它会对组织内的 AI 资产进行编目，包括 Bedrock、SageMaker 和 AgentCore 等托管服务、客户在 EC2、ECS 或 EKS 上自行运行的模型，以及内部工作负载调用的外部模型 API。该清单还将每个资产与其底层基础设施关联起来，并将资产与任何相关的 GuardDuty 调查结果连接。

## 竞争激烈的领域

AWS 并非首家监控竞争对手云平台的超大规模云厂商。Microsoft Defender for Cloud 自 2021 年底以来一直提供针对 AWS 的态势管理，并自 2022 年初以来提供针对 Google Cloud 的管理服务。Google 在 3 月份完成了对 Wiz 的 320 亿美元收购——Wiz 的平台涵盖了所有三大主要云平台。目前，Security Hub 的覆盖范围仅限于 Azure，AWS 尚未透露是否会跟进支持 Google Cloud。

AI 保护功能也进入了一个竞争同样激烈的市场。Wiz、Palo Alto Networks 和 CrowdStrike 目前都在销售 AI 安全态势管理产品。

AWS 押注于那些寻求多云部署的客户，希望 Security Hub 能成为他们跨云使用的统一控制台和统一账单来源。“多云”在未来多长时间内仅意味着 Azure，将是 AWS 这项赌注是否认真的首个考验。