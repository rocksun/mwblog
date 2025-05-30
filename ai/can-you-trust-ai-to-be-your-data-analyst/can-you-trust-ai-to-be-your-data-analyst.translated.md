# 你能信任 AI 成为你的数据分析师吗？

![Featued image for: Can You Trust AI To Be Your Data Analyst?](https://cdn.thenewstack.io/media/2025/03/8e34160a-igor-omilaev-9xtksci9crg-unsplash-1024x576.jpg)

[Igor Omilaev](https://unsplash.com/@omilaev?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/a-neon-neon-sign-that-is-on-the-side-of-a-wall-9XtKSci9crg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)上。

好消息是，部署 AI 代理并将它们连接到你的数据比以往任何时候都容易。但仅仅这样做并不能使 AI 代理在数据驱动的决策中发挥作用。像 DeepSeek 这样的模型——或任何其他大型 LLM——如果底层数据不一致，就无法产生有意义的见解。这是经典的 **garbage in, garbage out** 问题。

在大多数公司中，都存在一个显而易见的问题：组织通常拥有同一指标的多个版本，每个版本的计算方式都不同。以“利润率”为例——财务、销售和运营部门可能会对其进行不同的定义。在这种不一致的情况下，AI 无法提供*正确*的答案，因为实际上，组织尚未就正确的答案达成一致。

许多人认为清理[数据并消除错误就足够了](https://thenewstack.io/observability-isnt-enough-its-time-to-federate-log-data/)，从而获得 AI 驱动的见解。然而，即使是完美无瑕的数据，如果没有一致的定义，也可能导致相互冲突的答案。

**一个真实世界的场景**

假设要求 AI 代理找到公司有流失风险的客户——最有可能流失的客户。它搜索 CRM，并看到一个标记为 **“at-risk”** 的字段附加到客户帐户列表。AI 提取数据，生成报告并呈现结果。

*那是正确的吗？*

不完全是。客户支持团队在几个月前的一次临时服务问题期间应用了 **“at-risk”** 标签。应该使用长期参与度、产品使用情况和历史流失率等指标来评估风险，而不是使用过时的标签。更糟糕的是，管理层正式接受的实际流失模型位于 BI 工具中其他探索性仪表板中的一个工作簿中。

那么接下来会发生什么？AI 代理提供不完整或误导性的分析，团队基于错误的数字做出决策，并且对 AI 驱动的见解的信任度下降。

**为 AI 就绪的数据资产构建基础**

传统上，团队[首先构建受监管的语义模型来处理 AI 驱动的分析](https://thenewstack.io/building-ai-driven-applications-with-a-multimodal-approach/)。为业务指标创建受监管的基础对于长期成功至关重要。它可以确保一致的[数据解释并将业务](https://thenewstack.io/ai-adoption-why-businesses-struggle-to-move-from-development-to-production/)意图准确地映射到数据。语义模型对于启用 text-to-SQL 至关重要，并确保 AI 代理可以准确地解释和回答自然语言查询，例如：*我们上个季度的 CAC（客户获取成本）是多少？*

但是，如果你还希望 AI 代理提取正确的仪表板和报告，则它们需要区分临时工作和受信任的数据产品。大多数组织都有数千个仪表板，其中许多是为快速分析或一次性报告而创建的。如果用户问：*“按区域显示我们的销售业绩”*，AI 不应仅仅显示它找到的第一个仪表板。

为了确保 AI 显示正确的报告，我们建议**将可靠的仪表板标记为已认证**，以便 AI 代理可以放心地共享它们。这将防止过时或探索性报告被误认为是受信任的数据。

**从小处着手并扩展**

构建语义模型和认证数据产品不必采取全有或全无的方法。与其试图一次性管理所有内容，不如从一组有限的表（例如公司范围内的 KPI 或与特定领域相关的表）开始，然后再扩展到整个数据生态系统。

**建立受监管的语义模型**

[语义模型](https://euno.ai/blog/semantic-layers/)充当组织关键指标的统一事实来源。它使用[标准化](https://thenewstack.io/why-we-need-an-inter-cloud-data-standard/)定义将业务意图映射到数据，使 AI 工具能够准确地解释自然语言查询，从而实现经典的 text-to-SQL 场景。
但这里有个挑战：分析师们总是在他们的 BI 工具中随时创建新的指标定义。如果无法了解这些指标是如何定义和使用的，以及它们是否与现有定义冲突，组织就有可能构建一个与实际业务需求不符的语义模型。为了确保你的语义[模型反映数据的使用方式](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)，你需要深入了解已存在的内容、如何使用以及不一致之处。

**如何建立你的语义模型：**

*   **从高利用率的指标开始**：从跨团队频繁引用或查询的指标开始。这些指标在受到治理时将提供最大的价值。
*   **优先考虑复杂的计算**：具有自定义逻辑的指标是包含在语义模型中的良好候选对象。管理这些指标可确保准确性并最大限度地减少下游报告中的错误。
*   **保持一致性和清洁**：投入精力解决冲突、识别重复项并清理未使用的指标。
*   **持续监控**：语义模型不是静态的。密切关注哪些指标受到关注，并评估它们是否应纳入语义模型或替换过时的定义。

目标不仅仅是构建模型，而是保持其清洁、相关并与业务发展保持一致。

![](https://cdn.thenewstack.io/media/2025/03/12fa9433-conflict-analysis-1024x512.png)

查找冲突的度量、追踪其数据源、比较计算并评估其利用率和所有者以解决不一致问题。

**认证数据产品**

即使有了受治理的语义模型，AI 代理仍然需要知道哪些仪表板和报告是可信的。认证计划有助于区分基于经过验证、受治理的[数据构建的报告与为探索性或一次性分析创建的报告](https://thenewstack.io/the-rise-of-community-driven-data-analysis-in-the-age-of-ai/)。实施认证计划可以帮助 AI 代理浏览仪表板的蔓延。

运作方式：

*   **设置认证标准**：定义什么使仪表板或报告可认证。例如：

    *   [数据应来自生产级表](https://thenewstack.io/a-react-based-open-source-tool-for-creating-data-tables/)(例如，带有生产标签的债务市场)。
    *   所有权和文档应清晰且最新。
    *   不包括自定义逻辑（例如，以自定义 SQL 语句的形式）。
*   **向仪表板添加“已认证”标签**：可以标记仪表板为“已认证”，以表明它们符合治理标准。你可以手动管理此过程，也可以使用 Euno 等工具自动执行认证。这些工具可以识别哪些仪表板符合认证标准，突出显示未认证仪表板中的差距，并提供明确的补救步骤。
*   **持续监控**：如果仪表板的数据源或逻辑发生变化，则应重新评估其认证状态。定期更新认证，以确保 AI 代理始终使用[可靠的数据以获得可信赖的](https://thenewstack.io/aws-brings-trusted-extension-support-to-managed-postgres/)结果。
*   **通过 API 将 AI 代理连接到治理数据**

AI 代理并非天生就理解治理，它们需要关于数据资产可信度的明确标签。通过 [API 将它们连接到治理数据](https://thenewstack.io/make-data-governance-automation-suck-less-with-a-supergraph/)可确保它们仅显示可靠、经过认证的见解。

**用于显示仪表板：**

*   当用户问“按区域显示我们的销售业绩”时，AI 代理应：

    *   查询治理 API 以识别经过认证的仪表板。
    *   显示最相关、可信的仪表板，避免过时或未经认证的版本。
*   **用于回答临时问题：**

    *   对于诸如“企业客户的流失率是多少？”之类的查询，AI 代理应：

        *   从语义模型中提取定义以确保一致性。
        *   仅使用受治理的数据源来计算并返回准确的结果。

通过将治理元数据集成到其工作流程中，AI 代理可以自信地区分高质量、可靠的资产与探索性或过时的资产。

**结果：AI 按预期工作**

组织可以通过建立受治理的语义模型和强大的认证计划来转变其 AI 驱动的分析。AI 代理将不再猜测或依赖不完整的数据，而是提供准确、可操作的[与业务保持一致的见解](https://thenewstack.io/data-unleashed-unlocking-powerful-business-insights/)。

当你的数据准备好用于 AI 时：

*   **决策发生得更快**：用户可以立即访问可靠的见解。
*   **信任提高采用率**：业务团队可以放心地依赖 AI 工具。
*   **数据保持清洁**：治理流程减少了混乱和错误。

**结论**
只有在数据资产受到治理的情况下，AI 驱动的分析才能改变游戏规则。如果没有治理，AI 工具可能会放大混乱，而不是提供清晰度。标准化关键指标、认证可信的仪表板以及将 AI 代理连接到治理元数据将确保您的 AI 计划带来真实、可靠的影响。生成式 AI 可以彻底改变分析。只需确保您的组织已准备好兑现承诺。

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)