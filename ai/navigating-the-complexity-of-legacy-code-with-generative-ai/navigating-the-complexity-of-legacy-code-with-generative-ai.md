
<!--
title: 利用生成式AI应对遗留代码的复杂性
cover: https://cdn.thenewstack.io/media/2024/12/f91d08d3-legacy.jpg
-->

生成式AI的引入提供了一种实用且可扩展的方法来弥合知识差距并保持开发势头。

> 译自 [Navigating the Complexity of Legacy Code with Generative AI](https://thenewstack.io/navigating-the-complexity-of-legacy-code-with-generative-ai/)，作者 Sid Misra。

软件行业员工流动率高于其他行业已不是秘密。LinkedIn 2022年对其全球用户数据的[分析](https://www.linkedin.com/business/talent/blog/talent-strategy/industries-with-the-highest-turnover-rates)显示，科技公司员工流动率为12.9%，而所有行业的平均流动率为10.6%。

虽然这在外人看来可能波动很大，但业内人士认为这是该行业不断变化和适应的自然产物。员工往往优先考虑接触尖端技术或提供更大灵活性的角色的机会。与此同时，公司调整员工队伍战略，以保持敏捷、竞争力和对不断变化的业务优先级的响应能力。

这种人员流动往往使团队难以应对遗留代码：[开发人员离开后仍未完成或文档不足的工作](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/)。负责在几个月甚至一年后继续其同事未完成工作的软件开发人员面临着最艰巨的挑战。

当继承遗留代码时，开发人员依靠文档和内联注释来理解其预期用途。当这些注释缺失或不完整时，他们可能会花费大量时间来解读甚至反向工程代码。随着时间的推移，影响会加剧。机构知识会消散。积压工作会不成比例地偏向于[偿还技术债务](https://thenewstack.io/how-to-persuade-your-organization-to-pay-down-technical-debt/)，而不是开发新功能。挫败感油然而生。

SAP对此现象的经验提供了独特的国际视角。该公司的一些核心业务逻辑编写于20世纪后期，当时其开发组织集中在其德国总部。当时，用德语命名业务对象和技术结构是很常见的：BUKRS代表*Buchungskreis*（公司代码），GJAHR代表*Geschäftsjahr*（财政年度），EKPO代表*Einkaufspositionsdaten*（采购单项）。

随着公司[将其员工队伍发展到国际化](https://www.sap.com/canada/about/company.html)，员工人数超过107,000人，遍布157多个国家，这成为许多例子中的一个，突显了遗留系统如何无意中使现代工作流程复杂化。

## 人工智能作为游戏规则改变者

最近，SAP与许多其他科技公司一样，将生成式AI视为管理遗留代码的有力潜在补救措施。这种信心源于[大型语言模型（LLM）](https://thenewstack.io/llm/)的架构、设计原则和训练方法。虽然最初设计用于处理人类语言，但这些模型在理解代码语法和结构以及推断底层意图和上下文方面非常有效。

LLM在海量代码、技术文档和自然语言数据集上进行训练，可以识别遗留代码库中通常隐含的模式和约定。它们擅长分析单个代码行和更广泛的系统交互。这有助于它们映射依赖关系并揭示关键关系。它们进行情境化分析的能力超越了语法，使它们能够推断特定领域的业务逻辑和意图，即使是在文档匮乏的系统中也是如此。

对于开发人员而言，这意味着生成式AI可以为模糊的功能提供自然语言解释，甚至可以[建议优化重构代码的方法](https://thenewstack.io/how-to-use-self-healing-code-to-reduce-technical-debt/)。通过弥合机构知识的差距，它可以减少更新遗留代码所需的时间和精力。更重要的是，它有助于[开发团队快速超越维护旧系统](https://thenewstack.io/ai-code-assistants-are-moving-beyond-auto-complete-heres-whats-next/)，从而加速创新并创造更大的价值。

SAP在其云开发模型和专有编程语言ABAP上训练了其生成式AI副驾驶[Joule](https://thenewstack.io/ai-agents-and-co-pilots-sap-introduces-deeper-integrations/)。2025年，Joule的开发人员功能将无缝集成到Eclipse集成开发环境中的ABAP开发工具插件中。同样，通过Joule提供的生成式AI功能已添加到SAP Build中，SAP Build是一个统一的应用程序开发和自动化解决方案，它结合了低代码和专业代码工具。
从开发人员的角度来看，新的模块化窗口将使他们能够在工作的过程中直接与Joule聊天。代码解释可以像直接询问特定函数、方法或业务对象的功用一样轻松地生成。或者，[开发人员可以请求对粘贴到Joule聊天窗口中的一段遗留代码的详细解释](placeholder)。开发人员还可以为类和视图生成RESTful业务对象、服务和单元测试。

人员流动和遗留代码的挑战长期以来一直严重困扰着软件行业，耗费了本可用于创新的时间和资源。生成式AI的引入标志着一个转折点，它提供了一种实用且可扩展的方法来弥合知识差距并保持开发势头。随着SAP Build等解决方案不断发展，它们不仅有望解决当前的[挑战](placeholder)，而且还将重新定义软件团队的构建方式，在不断变化的环境中创新和蓬勃发展。

访问我们的[网站](placeholder)开始您自己的SAP Build免费试用。
