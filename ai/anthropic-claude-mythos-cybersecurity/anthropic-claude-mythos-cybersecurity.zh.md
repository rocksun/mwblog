3月下旬，Anthropic的内容管理系统出现了一次[配置错误](https://fortune.com/2026/03/26/anthropic-leaked-unreleased-model-exclusive-event-security-issues-cybersecurity-unsecured-data-store/)，揭示了该公司正在开发 **Claude Mythos**。这是一个比其当前的旗舰模型 Opus 规模更大、能力更强的新层级模型。那份未发布的公告还提到，Anthropic 将采取更加审慎的方式来发布该模型，以减轻“网络安全领域的潜在近期风险”。这正是 Anthropic 目前正在做的事情。

Claude Mythos Preview 被该公司在周二描述为“通用的、未发布的尖端模型”，它将不会公开发布——至少目前不会，也不会以现在的形式发布。相反，Anthropic 将通过其所谓的“玻璃翼计划”（Project Glasswing）将其提供给少数选定的合作伙伴。

> Claude Mythos Preview 不会公开——只有选定的合作伙伴可以访问。

Amazon、Apple、Broadcom、Cisco、CrowdStrike、Linux Foundation、Microsoft 和 Palo Alto Networks 是该项目的启动合作伙伴。他们以及大约 40 个额外的组织将获得 Claude Mythos 预览版的访问权限，用于防御性安全工作，以便他们可以使用它来扫描和保护自己的系统及开源工具。

虽然 Mythos 并非专门为网络安全任务设计，但 Anthropic 指出，该模型在智能体编码和推理方面表现强劲。在 [CyberGym 基准测试](https://www.cybergym.io)（该测试评估 AI 智能体在漏洞分析任务上的表现）中，Claude Mythos 获得了 83.1% 的分数。此前在该基准测试中排名第一的 Opus 4.6 得分为 66.6%。

![](https://cdn.thenewstack.io/media/2026/04/37a60f92-project-glasswing-logos-1024x576.png)

图片来源：Anthropic。

Anthropic 最初作为 OpenAI 的替代方案成立，专注于 AI 安全。它似乎认为，发布具有此类能力的模型应当谨慎行事，以便在攻击者也获得访问权限之前，给防御者留出时间来“未雨绸缪”。

愤世嫉俗的人可能会争辩说，夸大这些危险也有助于将这些模型定位为特别强大、从而在公众眼中更具吸引力。但正如 CrowdStrike 的 CTO Elia Zaitsev 所指出的，这里确实存在真正的危险。

他在一份声明中表示：“漏洞被发现与被对手利用之间的时间窗口已经塌缩——以前需要几个月的时间，现在利用 AI 几分钟内就能发生。Claude Mythos Preview 展示了防御者现在可以实现的大规模防御能力，而对手不可避免地也会寻求利用同样的能力。这不是减速的理由，而是我们应该团结起来、行动更快的理由。如果你想部署 AI，你就需要安全。”

> “Claude Mythos Preview 展示了防御者现在可以实现的大规模防御能力”

Anthropic 已经使用 Mythos Preview 发现了它所描述的“数千个零日漏洞，其中许多是关键漏洞”。通常，这些漏洞非常陈旧，其中最古老的是 OpenBSD 中的一个漏洞，它保持未知且未修复状态长达 27 年。

该模型还成功地利用 Linux 内核中的多个漏洞实现了链式攻击，从而获得了超级用户访问权限。

这类安全研究对于开源项目尤为重要。Linux Foundation 执行董事 Jim Zemlin 表示，安全专业知识在历史上是大型企业才能负担得起的，但对于小型公司和开源项目来说一直是遥不可及的。

> “这就是 AI 增强安全如何成为每个维护者的得力助手。”

他说：“开源维护者——他们的软件支撑着世界上大部分的关键基础设施——在历史上一直只能靠自己来解决安全问题。通过让这些关键开源代码库的维护者接触到能够主动大规模识别和修复漏洞的新一代 AI 模型，Project Glasswing 提供了一条改变这一现状的可靠路径。这就是 AI 增强安全如何成为每个维护者的得力助手，而不仅仅是那些负担得起昂贵安全团队的人的专利。”

最终，Anthropic 计划向其用户推出 Mythos 级别的模型，但目前，它仅限于 Project Glasswing 的参与者。Anthropic 将向参与公司提供 1 亿美元的试用额度，并向开源安全组织直接捐赠 400 百万美元。