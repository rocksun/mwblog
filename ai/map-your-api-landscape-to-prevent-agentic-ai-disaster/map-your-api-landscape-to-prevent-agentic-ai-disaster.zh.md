超过15年来，开源API基金会 [Naftiko](https://naftiko.io) 的联合创始人兼首席社区官 (CCO) [Kin Lane](https://www.linkedin.com/in/kinlane/) 一直致力于积累其在API方面的专业知识——不仅包括技术细节，还包括业务视角。他认为，企业中越来越多地使用副驾驶（copilots）和[代理AI系统](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/)意味着我们必须围绕业务能力而非资源来设计和[构建API](https://thenewstack.io/api-management/)。他说，API应该代表核心业务功能，例如“管理库存”或“处理支付”。

[他并非唯一持有此观点的人](https://apievangelist.com/2025/10/07/what-is-a-capability/)。包括 [Christian Posta](https://blog.christianposta.com/from-apis-to-capabilities-what-ai-agents-mean-for-application-architecture/)、[Mike Amundsen](https://mamund.substack.com/p/focusing-on-capabilities-is-a-win) 和 [Daniel Kocot](https://architecturalbytes.substack.com/p/from-apis-to-capabilities) 在内的多位知名API专家也得出了相似的结论。

DORA的[《AI辅助软件开发现状报告》](https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report?hl=en)中记载的最新研究为此观点提供了支持，该报告总结称生成式AI（GenAI）是一个放大器。报告指出：“它放大了高绩效组织的优势，也凸显了困境组织的弊端。” Lane在组织构建和使用API的方式中看到了这种放大效应。

他在一次采访中告诉我：“公司在AI实施方面的成败将取决于其现有的API投入以及在API发展路径上的进展。例如，他们是否有API目录？他们是否有开放API？他们是否在进行测试/模拟？他们的API是否得到适当的文档记录？他们是否投资了开源？”

Lane认为，对API采取不成熟方法的组织的AI项目将是一场灾难。考虑到这一点，Lane概述了一个四步流程，以帮助组织更好地掌握其API全景，从而实现更成功的AI实施。

## 1. 绘制您的API全景图

Lane表示，API潜在失败的原因是，不够成熟的组织在“企业所知与企业所能”之间存在巨大差距。普通企业的软件即服务（SaaS）产品组合大约有250到500项服务，所有这些服务都拥有API。但Lane认为，由于发现手段有限，许多API最终几乎未被使用。

将AI代理引入此环境将产生两种结果之一：要么代理无法发现可用的API，因此几乎无用。要么它能够访问这些API，但最终[过度共享](https://leaddev.com/technical-direction/if-95-of-generative-ai-pilots-fail-whats-going-wrong)，暴露了应该保密的数据。因此，首要任务是绘制组织API全景图，以了解内部和外部资源。

绘制这张地图需要查看可用的信号。如果你要从外部绘制一个组织的API地图，你会查看公开的GitHub仓库、博客文章、新闻稿、招聘信息以及任何已发布API的技术文档。同样的流程也可以在内部使用，Lane在彭博社领导API治理一年期间就熟悉了这一点。

Lane说：“我爬取了GitHub和Confluence，寻找任何API的存在。我绘制了那个全景图，找出了其背后的团队，并将数据组织成一个组织结构图，这就像我的棋盘一样。”

## 2. 建立通用语言

有了这张地图，Lane的第二个重点是审视API组件中使用的语言，例如端点URL、方法名称和参数。

网景首席开发者[Phil Karlton曾有名言](https://martinfowler.com/bliki/TwoHardThings.html)：“计算机科学中只有两件难事：缓存失效和命名事物。” 命名事物之所以具有挑战性，是因为我们做出的语言选择确实很重要。尽管[语言主要是一种交流工具而非思维工具](https://gwern.net/doc/psychology/linguistics/2024-fedorenko.pdf)，但它会影响注意力、记忆和分类，使某些认知区分变得更容易或更困难，并可能模糊预期的含义。

彭博社的API主要是REST API。Lane说：“我审查的API名称中都包含‘database’或‘ERP’这样的词。这不是一个好的设计。”

Lane发现，在绝大多数情况下，彭博社的开发者在错误的抽象层次上构建API，它们反映的是后端系统而非业务流程。这表现为[API蔓延](https://thenewstack.io/heres-how-to-tame-your-api-sprawl-and-why-you-should/)和许多没有实际用途的API。

这并非REST的局限性，但使用REST确实会影响我们的思维：它鼓励我们关注资源的表述性状态转移，因为这正是REST的设计初衷。

Lane说：“我认为90%的人都没有做好REST API设计。他们不考虑或不关心REST，也没有采取以消费者或产品为导向的设计方法。”

REST影响我们思维的方式是语言选择重要性的一个例子。REST的动词——GET、PUT、PATCH、DELETE——指定了对特定资源（或资源集合）执行的操作。对于任何API，其词汇都会影响使用它的开发者的思维。API实际上是一种小型语言，其使用者必须学习。正如SoftIron首席科学家[Harry Richardson](https://www.linkedin.com/in/harry-richardson-007a69/)在2024年告诉我的，我们选择的名称[塑造了我们的心智模型](https://thenewstack.io/what-are-the-core-principles-of-good-api-design/)。

结果是，分类法很重要。借鉴Eric Evans的著作[《领域驱动设计》](https://learning.oreilly.com/library/view/domain-driven-design-tackling/0321125215/)，Lane建议开发者需要从构建IT部门与业务其他部门共享的通用或“无处不在”的语言开始。这是一个好主意，但很少被付诸实践。

Lane说：“企业发展如此之快，以至于你最终会得到一堆杂乱无章的、上下文不一致或无法协同工作的发票、支付和消息。”

此外，当领域专家和开发者不共享通用语言时，沟通就会以高昂的代价崩溃。专家使用其领域的专业术语，而开发者则以技术抽象思维，从而产生语言鸿沟，双方只能模糊地理解对方。即使有少数团队成员弥合了这一分歧，他们也会成为信息瓶颈，并且他们的翻译会失去精确性——导致概念混乱，团队之间持续误解，最终代码以破坏原始设计的方式进行重构。

## 3. 从API转向业务能力

拥有通用语言是定义面向业务的API的先决条件。

Lane说：“做得最好的公司以对业务重要的方式将API整合在一起。下一个迭代是从资源转向‘能力’或‘体验’。”

Lane[将能力定义为](https://naftiko.io/blog/reframing-how-we-integrate-software-with-capabilities)“与特定领域内的业务成果对齐的开源、声明式、基于标准的集成。它们提供了在无数内部、合作伙伴和第三方系统之间交付和自动化集成所需的构建块。能力有助于重新平衡我们如何思考和执行对我们所依赖的庞大生态系统中的集成。”

Lane关于能力的思想源于许多不同的学科，但与“聚合体”（“聚合体”在《领域驱动设计》中被定义为“为数据变更目的而作为一个单元处理的关联对象集群”）有所重叠。良好的能力应是与业务对齐的、人机可读的、可组合的、声明式的、受治理的，并且可以在多个系统上执行。

Daniel Kocot将[“能力思维”](https://architecturalbytes.substack.com/p/from-apis-to-capabilities)定义为“强调平台或系统实际能为其消费者做什么，以及这些操作如何被文档化、标准化并在不同用例中可重用……能力思维重新定义了设计单元。平台不再暴露细粒度资源，而是描述离散的业务功能，例如‘发货订单’、‘处理支付’或‘批准贷款’。”

“能力”一词在描述AI代理可以做什么方面焕发了新的生机，但它也揭示了企业认为自己能做什么与其实际架构所支持的之间存在的差距。代理需要发现系统具备哪些能力，并根据目标和上下文决定使用哪些能力。正如[Mike Amundsen所说](https://mamund.substack.com/p/focusing-on-capabilities-is-a-win)，自主客户端需要的是“可能性菜单”，而不仅仅是端点列表。

## 4. 为AI建立清晰的边界

Lane认为，拥有地图、建立通用语言并进行领域驱动设计工作，意味着您的AI工作将有更好的范围界定。“您的MCP [模型上下文协议] 服务器将拥有针对特定产品、客户或业务线的适量工具。” 相反，如果您没有明确定义的边界，就会增加安全暴露和风险。

具备这些条件后，接下来的步骤将取决于业务上下文。Lane说，风险规避程度较低的公司“正在公开MCP服务器，并鼓励人们在其上构建有趣的东西”。在受监管更严格的行业中，重点将放在运营和开发者平台上，目标是提高开发者的速度。

## 成功AI实施，从API基础开始

Lane的方法要求企业从基础开始：在急于追求AI明天可能实现的目标之前，先建立通用词汇、绘制API全景图并了解他们今天的能力。正如他所强调的，这项工作不仅仅是关于技术架构。它是关于让工程师、产品经理和业务利益相关者围绕相同的语言和有界上下文达成一致。

对于那些想知道从何开始的高管来说，答案出奇地简单：从打标签和编目开始。定义特定领域的词汇，绘制其中的服务和资源，并为您要实现的目标建立清晰的边界。

与启动最新的AI代理相比，这项基础工作可能看起来不那么光鲜亮丽。但正是这种放慢速度、仔细思考语言、设计和业务对齐的意愿，将那些AI投资能放大自身优势的企业，与那些AI投资只会加剧自身功能障碍的企业区分开来。