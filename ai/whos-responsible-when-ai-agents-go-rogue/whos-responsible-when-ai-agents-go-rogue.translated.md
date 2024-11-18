# AI代理失控时，谁来负责？

![AI代理失控时，谁来负责？的特色图片](https://cdn.thenewstack.io/media/2024/11/ad6f6fc8-alessio-ferretti-upwjvq8cjry-unsplash-1024x604.jpg)

[Alessio Ferretti](https://unsplash.com/@ilferrets?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-strange-looking-object-with-eyes-and-a-nose-upwjVq8cJRY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

无论您身处科技界还是与家人共进晚餐，如今都无法逃脱AI的影响。我们许多人都经历了AI发展的几个周期，每一个新的增长阶段都会引发许多关于我们如何走到这里以及我们将走向何方的疑问。几年前，在ARM构建机器学习产品时，我们也面临着许多这样的问题，创新和AI的独立性是紧密交织的概念这一点非常清楚。

快进到今天的AI时代，虽然我们还没有被天网接管，但人们、企业和社会越来越担心最新阶段的广泛生成式AI应用带来的新的攻击面。无论您是担心[深度伪造驱动的社会工程攻击](https://thenewstack.io/why-ai-cant-protect-you-from-ai-generated-attacks/)、[AI驱动的网络钓鱼攻击](https://hbr.org/2024/05/ai-will-increase-the-quantity-and-quality-of-phishing-scams)还是[提示注入攻击](https://thenewstack.io/top-9-api-security-vulnerabilities-how-to-defend-against-them/)，都有充分的理由担心AI应用堆栈中潜伏的新风险；毕竟，AI并非存在于真空中——它集成在应用堆栈的每个层级的核心，处理海量数据，包括高度敏感的数据，并与各种第三方交换这些数据，无论是OpenAI这样的AI API还是来自Hugging Face的内部模型。

尽管AI有缺陷，但不可否认的是，它在生产力和创新方面具有巨大的潜力。虽然并不完美，但AI代理即将变得更加普遍。根据[Capgemini的一项调查](https://www.capgemini.com/insights/research-library/generative-ai-in-organizations-2024/)，82%的科技高管“打算在未来三年内在其组织中整合基于AI的代理——高于目前拥有功能性代理的10%”。

随着AI代理的日益普及，在其使用它们的重点行业中，潜在的危险也在增加。鉴于此，C级高管面临着一个关键问题：当AI失控时，谁来负责？

**AI问责制：不断变化的格局**

AI的激增正在扰乱现代企业的组织结构。[Pearl Meyer的一份报告](https://pearlmeyer.com/press-releases/pearl-meyer-survey-shows-companies-are-taking-steps-to-introduce-ai-in-the-workforce)显示，30%的公司选择将AI相关的责任纳入现有的高管角色。与此同时，“32%的公司正在采取去中心化的AI监督方法，并期望AI工作由多个职能部门的各种领导者负责”。

在当今大多数组织中，CISO、CIO和CTO承担着AI行为和安全的主要责任。这可能会在不同的领导角色之间造成紧张关系，因为CISO无法控制AI系统，但他们却负责维护安全。

由于AI是共享责任，组织必须采用能够明确定义问责制并弥合不同领导领域之间差距的策略和工具。

**为AI的“黑箱”带来透明度**

透明度是实现问责制的重要第一步。作为一名工程师，当我解构系统的工作原理时，我天生就感到快乐。在操作系统和加密领域之间架起桥梁，我了解了如何在这些复杂的软件系统之间建立透明度和信任。

但这对于那些在AI开发前沿的人来说并非易事。传统的软件工程倾向于依赖于可以编写和审核的预定义规则的确定性系统。相比之下，现代概率生成式AI系统根据其对可能性的复杂和多维计算做出（通常是不可预测的）预测。概率系统，就其本质而言，是不透明的。

因此，如果AI代理失控并且无法解释其决策，那么确定出了什么问题可能具有挑战性（如果不是不可能的话）。那么，负责AI系统的领导者如何在这样一个不完美的世界中获得尽可能多的透明度和控制权呢？
AI 的好坏取决于驱动它的数据——正如谚语所说，“垃圾进，垃圾出”——因此，清晰记录哪些训练数据正在为模型提供支持至关重要。尽可能频繁地擦除和删除可能有意或无意地被纳入其建模中的私人信息，也至关重要。

当通过 AI API 部署 AI 时，团队必须完整了解其数据和应用程序行为如何与外部实体（例如 Open AI）交互。他们需要了解哪些数据预期会流经模型（以及哪些数据不会），并实时访问其 AI 代理的运行方式，以便能够立即捕获和阻止意外行为，防止它们窃取数据或使整个系统瘫痪。

**利用技术增强人工监督**

一些人认为，人类需要与 AI 交互才能使其保持问责制，但我们如何才能避免人工监督成为创新的障碍呢？

设计 AI 与人类专家互动以增强其能力而不是取代他们是一个良好的开端。然后，团队必须利用技术主动限制对 AI 代理的访问，以减少或消除恶意破坏的后果。

就像我们在网络安全环境中强制执行零信任一样，访问控制和权限是根据安全的“[最小权限](https://www.cisa.gov/zero-trust-maturity-model)”模型分配给特定个人的，同样也应该将“最小权限”逻辑应用于 AI 代理。这样，AI 代理的任务就可以被限制，攻击面也将减小。同时，在关键时刻进行人工监督为最终负责其行为的团队和领导者提供了至关重要的透明度和控制。

AI 革命正在蓬勃发展，但我们仍处于起步阶段。组织必须确定谁应对 AI 的行为负责，这可能意味着弥合 CISO、CIO 和 CTO 之间的差距，或聘用一位完全专注于 AI 的高管。通过建立问责制，提高透明度，并利用技术增强人工监督，公司将能够很好地利用 AI 的优势，安全可靠地推动创新。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。