<!--
title: Kepler：OpenAI内部智能体平台，驱动数据合成未来
cover: https://cdn.thenewstack.io/media/2026/01/7e9ed590-qcon-openai-bonnie_xu.jpg
summary: OpenAI数据分散查询难。Kepler是AI代理，简化内部数据检索，自动分析，高效准确。已提升数据生产力。
-->

OpenAI数据分散查询难。Kepler是AI代理，简化内部数据检索，自动分析，高效准确。已提升数据生产力。

> 译自：[Kepler: OpenAI's Internal Agent Platform for Synthesizing Data](https://thenewstack.io/kepler-openais-internal-agent-platform-for-synthesizing-data/)
> 
> 作者：Joab Jackson

对于 [OpenAI](https://thenewstack.io/openai-recovers-30000-cpu-cores-with-fluent-bit-tweak/) 的员工来说，即使是像“某个特定国家有多少 ChatGPT Pro 用户”这样看似简单的问题，也可能出奇地难以回答。原因在于所需数据可能分散在多个数据源中，并且每个数据源的访问方式都略有不同。

总的来说，OpenAI 拥有 7 万个不同的数据集，每天新增 600 PB 的数据。大约 3500 名员工可以使用 15 种工具中的任意一种来访问这些数据。该公司一直密切关注其用户数量，但随着区域、计划和功能的增加，统计数字变得越来越困难。

然而，每个新的查询都带来了自身的挑战。因此，分析师们常常发现自己不得不与同事进行长时间的 Slack 对话甚至会议，只为弄清楚如何访问数据。

“简单的问题不应该如此困难或耗时，”OpenAI 数据生产力团队的技术人员 [Bonnie Xu](https://www.linkedin.com/in/xubonnie/) 上个月在纽约举行的 [QCON AI 大会](https://ai.qconferences.com/schedule/newyork2025)上的一次 [演讲](https://ai.qconferences.com/presentation/newyork2025/ai-agents-make-sense-data-openai)中说道。

Xu 在会上讨论了该公司为简化这一过程而创建的工具——Kepler。

Kepler 是一款有用的代理，旨在回答 OpenAI 员工的问题，它隐藏了为找到答案有时必须执行的诸多任务。

最初，Kepler 主要为公司的数据科学家设计，但自发布以来，其用户群已扩展到财务、人力资源和其他部门的员工。

据 Xu 称，一位 Kepler 用户表示，这是他们体验过的 AI 系统最接近 AGI（通用人工智能）的一次。

## OpenAI 内部数据检索面临的挑战

对于业务分析师来说，许多数据库表可能看起来非常相似。一个数据库可能包含未登录用户，而另一个则不包含。有些表包含加密用户，而另一些则不包含，并且必须将这些数据连接到结果数据集中。那么应该使用哪一个呢？

编写正确的 SQL 代码来提取数据也可能很困难，特别是当它们涉及跨不同表的连接时。

“遗漏一个细微之处可能导致答案偏差一个数量级，这在做出重要的业务决策时可能是灾难性的，”Xu 说。

![SQL 查询](https://cdn.thenewstack.io/media/2026/01/e6807422-qcon-xu-01-1024x768.jpg)

这个 SQL 查询正确吗？许多经理都无法判断。

## Kepler 的实际应用

Kepler 是内部构建的数据分析师，它可以利用 OpenAI 所有的内部数据存储来回答问题。OpenAI 员工可以通过 Slack、[Cursor](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/) 等集成开发环境 (IDE)，或通过与特定工作流集成，或通过移动设备及其他远程客户端与 Kepler 交互。在后台，Kepler 使用 GPT-5 来解析请求。

为了演示 Kepler 的工作原理，Xu 举了一个关于纽约出租车出行时间的问题。她想知道一天中哪些时段的出行时间差异最大，以及哪些行程是“最不可靠的”，这意味着起点和终点位置对之间最短和最长出行时间的差异最大。

演示展示了 Kepler 为回答这个问题而执行的“思维链”，即一系列评估和操作。

首先，它进行内部知识搜索，识别出两个潜在相关的数据库，包括 2016 年 NYC 出租车出行时间数据集合，其中包含了上下车时间以及目的地和出发地的邮政编码。

然后，代理计算每个邮政编码的中位数时间，并识别出第 95 和 99 百分位数。代理通过有根据的猜测来编写适当的查询以获取所需信息，逐一测试，并很快找到一个有效的查询。

“你可以想象，自己手动完成这些需要大量时间，但代理只是代表你完成了这些查询和结果步骤，”Xu 说。当查询看起来正确时，它会对结果进行排序，然后进行一些简单的格式化，甚至准备一个图表来向用户展示数据。（答案显示，高峰时段和深夜是最不可靠的时间。）

Xu 提供的另一个演示展示了 Kepler 如何处理一个关于 ChatGPT 用户在 2025 年 3 月出现大幅增长原因的问题。它查阅了一个仪表板和一份任务文档，找到了显示这些数据的表。Kepler 编写了不同的查询，试图查明使用量的突然增加，例如按区域查询。它还查找了错误，例如日志数据重复。

该思维链确定了一个可能的原因，即一项新的生成式图像功能的发布。他们进行网络搜索以交叉验证这一假设，找到了关于该发布版本的发布说明和新闻文章。

Kepler 会存储所有问题，因此您可以在以后继续讨论后续话题。当被问及 2 月 14 日情人节的出租车乘车情况的后续问题时，Kepler 显示出该代理知道要使用哪些表格和查询。

如果您从 Kepler 的思维链中发现它走向了错误的方向，您也可以打断它。

由于分析师倾向于提出相同类型的问题，例如产品分析和数据验证，Kepler 为这些类型的问题保留了一系列自定义工作流。

## Kepler 的工作原理

Kepler 的核心是一组直接与 ChatGPT（目前是版本 5）通信的 API。Kepler 还直接连接到一组预处理信息，包括内部数据知识库和内部文档服务。它还可以调用数据仓库以及运行在 [Apache Spark](https://thenewstack.io/enhancing-the-flexibility-of-sparks-physical-plan-to-enable-execution-on-various-native-engines/)、[Airflow](https://thenewstack.io/apache-airflow-3-0-from-data-pipelines-to-ai-inference/) 和其他平台上的数据服务。

Xu 表示，使用 Anthropic 发明的 [模型控制协议](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/) (MCP) 对 Kepler 来说“非常有帮助”。Kepler 利用内部文档来理解如何查询数据库或在 MCP 上执行其他任务。如果结果不如预期，它可以稍作修改后重新运行查询。实际上，Kepler 代理正在自主推理。

“所以，不是你提供反馈，而是 Kepler 运行工具，然后根据获得的任何反馈，使用正确的工具采取下一步行动，”Xu 说。

通常，独立运行的代理可能会返回极其不准确的结果，但如果手头有额外的上下文，它们就能理解何时出现错误并尝试改变其方法。

“所以，真正美妙之处在于 Kepler 可以交互式地探索数据本身，而且上下文始终贯穿整个过程，”她说。

## 元数据的重要性

帮助构建上下文的还有元数据。

“仅仅查看表格本身是不够的，你需要了解表格是如何创建的以及它来自何处，”Xu 说。这是代理真正理解表格之间差异的秘密。

一个离线作业会运行以编译每个表格的这些信息。

公司已经编译了大部分数据。关于每个数据库表的丰富元数据已被捕获，例如它为何被创建、其用途，甚至其主键是什么。

![OpenAI 元数据生成。](https://cdn.thenewstack.io/media/2026/01/983e792d-kepler-04-1024x768.jpg)

OpenAI 如何从其自身文档中生成额外元数据。

它还使用 [codex 生成](https://thenewstack.io/openai-says-its-new-codex-max-model-is-better-faster-and-cheaper/) 功能，从代码本身构建元数据。

“由于这一切都由离线作业定期刷新，因此上下文保持新鲜，无需任何人工干预。”

如果 Kepler 或用户发现错误，它会将其更正保存在内存中。

“对我们来说，内存是帮助代理持续学习和改进的真正机制，”Xu 说。“上下文可能会让你完成 80% 到 90% 的工作。但有时你需要那些最终的小修正，这些修正很难仅仅通过推断获得。”

![Kepler 代码](https://cdn.thenewstack.io/media/2026/01/daff4413-qcon-kepler-03-1024x768.jpg)

Kepler 如何将更正保存在内存中。

为了评估答案的质量，OpenAI 运行了一个 Eval Grader，它为每个测试的答案提供一个分数。它会查看交付结果与预期或正确结果的差异。

在许多情况下，正确答案的 SQL 查询可能与预期略有不同，但开发团队对此有所计划。

“当我们比较解决测试时，我们实际上会为那些对答案没有实质性影响的地方留出一点余地，”Xu 说。

用户将自己的凭据带到 Kepler，从而确保他们不会看到任何未经授权的数据。

## Kepler 的未来发展方向

Xu 表示，目前 OpenAI 尚无开源 Kepler 或将其作为企业产品提供的计划，并指出她无权做出这些决定。

尽管如此，运行基于代理的内部数据分析工具似乎为公司带来了巨大价值。

“我认为，至少从我们用户那里听到的反馈来看，直接使用 Kepler 会快得多。它更高效，因为当你查看不同来源时，有很多事情你需要做，而且你需要连接这些点，”Xu 说。“Kepler 实际上就是最顶层的那个抽象层，它为你完成了所有这些工作。”