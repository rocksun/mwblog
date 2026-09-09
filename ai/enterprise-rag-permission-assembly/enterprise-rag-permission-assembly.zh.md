**周一上午 9 点，某位员工调离了财务团队。** 您的系统同步任务在凌晨 2 点运行。在接下来的十七个小时里，该员工依然可以从您的检索索引中拉取财务文档，而系统对此一无所知。我借用了 [Truto 的案例](https://truto.one/blog/how-to-maintain-document-level-rbac-in-enterprise-rag-pipelines/)，但我交流过的每个团队都遇到过类似问题。

这就是“有时效性”的版本。而在安全审查中，人们提出的质疑则不同。检索原型运行成功、演示效果很好、高管赞助商也很满意，然后有人问：你如何保证这个系统永远不会把 CEO 的薪酬评估报告总结给一个问及薪资范围的实习生？

大多数团队都没有答案。他们有的只是一个过滤器。

我认为答案必须是结构性的。权限不是在组装完语境后才应用的过滤器，而是针对特定身份如何组装语境的一种属性，因为组装是拒绝包含某项信息的最后时机，此后模型便从未接触过该数据。

> 权限不是在组装完语境后才应用的过滤器，而是针对特定身份如何组装语境的一种属性。

赛道上的主要平台厂商都在构建这一步骤的不同版本，但没人给它起个统一的名字。我经营着一家名为 Modus 的公司，正是构建于这一领域，所以请权衡我的论点。在我们的产品中，我们称之为语境组合（context composition）。在本文中，我称之为**语境组装（context assembly）**。这是系统决定在特定时刻、针对特定问题、为特定人员向模型提供哪些企业知识的环节。上游的一切都是存储，下游的一切都是推理。组装环节决定了身份的存在与否。

## **宣布并不等于出货**

之所以要在九月而不是六月讨论这个问题，是因为平台厂商已经停止在“该步骤位于何处”这一问题上产生分歧，但大多数公司运行的软件还没有跟上他们的步伐。

AWS 在六月份表现得最为明确，在纽约峰会上[宣布了 AWS Context](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/)，[当时的报道在此](https://thenewstack.io/aws-context-knowledge-graph-agents/)。其底层设计决策才是最有趣的部分。该图谱受与湖泊相同的权限治理，即通过 [Glue Data Catalog、SageMaker Unified Studio 和 Lake Formation](https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/) 进行管理，并且在有人查询时会再次核查身份。管理它的人就是已经在管理其他一切的人，他们拥有 S3 对象权限无法提供的[列级、行级和单元格级策略](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)。

准确把握时态很有必要，因为转述已经模糊了它。每一次调用都“[旨在继承调用用户的 IAM 和 Lake Formation 权限，因此代理只能查看和遍历其身份授权访问的关系。](https://aws.amazon.com/blogs/machine-learning/context-intelligence-for-your-data-and-ai-agents-at-scale/)” 重点是“旨在”。这是路线图语言，近三个月过去了，AWS Context 仍然被列为“即将推出”，没有 GA 日期、没有区域列表，也没有定价。而 [Amazon Bedrock Managed Knowledge Base](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-managed-knowledge-base/) 在当天确实实现了普遍可用（GA），这正是两者被混淆的主要原因。

> 微软于 6 月 16 日发布了具备身份意识的检索功能。AWS 在 6 月 17 日宣布了该功能，但你至今无法购买。

在 AWS 宣布 Context 的前一天，微软的 [Work IQ API 已普遍可用](https://www.microsoft.com/en-us/licensing/news/work-iq-general-availability)。它[在登录用户的上下文中运行，遵循 Microsoft 365 权限](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/work-iq)，可通过 Copilot Credits 计费，管理员今天就可以开启。两项公告仅相隔一天，架构定位相同，但只有一项可以投入生产。

Databricks 从另一个方向达到了同样的位置，[将 Unity Catalog 扩展到了代理](https://www.databricks.com/blog/whats-new-unity-catalog-data-ai-summit-2026)。然而，该生态系统中的合作伙伴指出，这种保护锚定在 Databricks Runtime 而非数据本身，因此当 BI 工具或 MCP 服务器直接访问同一源时，保护就不再适用。

团队并没有等待这一切。他们在身份感知版本仍停留在演示稿上时，就已经上线了扁平索引版本。

方向是一致的，局限性也是。每一个控制措施在发出它的系统内最为有效。有趣的问题在于当代理需要同时跨越多个系统获取语境时，这正是组装环节必须解决的任务。

## **数据湖不是业务本身**

Lake Formation 在其管控的湖内执行细粒度权限，并且做得很好。但这些权限并不会自动成为 Salesforce、Slack、Google Drive 或 Confluence 中的共享规则。

AWS 记录了其边界所在。其八月份关于[通过 AgentCore 传播用户授权上下文的指导](https://aws.amazon.com/blogs/security/propagate-user-authorization-context-in-ai-agents-with-amazon-bedrock-agentcore/)中，阐述了将作用于实际用户的令牌传递给 Salesforce，以便 Salesforce 应用其自身的共享规则。用 AWS 的话说，“代理充当协调者，而不是守门人”，“下游服务强制执行授权”。

这是一个合理的决定。这也是一个重要的产品边界。Lake Formation 并未与 Salesforce、GitHub、Jira、Slack、Confluence 或 Google Drive 进行集成。这些系统各自根据自己的条款决定谁能看到什么，否则就没人能做到。

最有用的一句话是关于过滤器本身的。在同一篇安全文章中，AWS 明确指出“[元数据过滤是应用层面的强制执行。Bedrock:Retrieve API 不会将元数据过滤内容作为 IAM 条件键公开。](https://aws.amazon.com/blogs/security/propagate-user-authorization-context-in-ai-agents-with-amazon-bedrock-agentcore/)” 我一直回想起这句话，因为这是供应商在冷静地告诉您他们的保证在哪里结束，而您的责任从哪里开始。

您的技术栈也是如此。分块（chunks）上的标签并不是身份边界，它们只是您的应用程序代码被信任去遵守的提示。

## **授权滞后时会发生什么**

故障是结构性的，这也是为什么我总是遇到这几种相同的情况。

我想在这里小心一点。“过滤器是坏的”并不是我的论点。问题在于顺序。检索系统可以搜索混合索引、检索不透明 ID、授权它们，并仅提取用户允许阅读的文档。这是一种过滤器，它是没问题的，因为没有任何未经授权的内容离开了检索边界。

我更经常看到的是在文档被提取后才进行检查的版本。一旦受限文本被提取、重排序、总结或缓存到边界之外，授权就是在追赶问题，而不是预防问题。AWS 自己的指导意见称这种使用宽泛凭据的版本为“单点故障”，因为提示词注入或过滤逻辑中的错误可能会暴露整个数据集。如果它到达了模型，模型就已经读取了该用户本无权检索的内容，窗口期的任何错误或注入指令都可以利用这一点。

大多数团队首先采取的防御措施可能会让情况变得更糟。宾夕法尼亚州立大学的 Jiale Liu、Jiahao Zhang 和 Suhang Wang 对[基于图谱的检索进行了红队测试](https://aclanthology.org/2026.findings-acl.899/)，发现总结可以减少非目标攻击中的泄露，但在目标攻击中却会增加泄露。我的解读是，总结保留了显著细节，而显著细节通常是敏感信息。另一项 [2026 年的预印本](https://arxiv.org/abs/2602.08668)发现，在从向量搜索切换到图谱的管道中存在跨租户泄露，通过在每一跳重新检查授权消除了这一问题。当没有人在组件之间的转换处重新检查授权时，两个各自安全的组件仍然可以组成一个不安全的系统。

> 当没有人在组件之间的转换处重新检查授权时，两个各自安全的组件仍然可以组成一个不安全的系统。

本文开头提到的十七小时窗口是同样故障的慢动作重现。直接共享、嵌套组和公共链接都会独立变化，这就是 Google 构建 [Zanzibar](https://www.usenix.org/conference/atc19/presentation/pang) 作为关系模型而不是列表的原因。在每个块上加盖的允许用户列表只是一个图谱的快照，它在变动时并不会通知您。

这已经不再是边缘问题了。 [OWASP LLM 应用十大风险](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)在其 2025 年修订版中将“敏感信息泄露”从第六位移至第二位，并增加了 [LLM08：向量与嵌入漏洞](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/)，指出了在共享向量数据库的用户之间存在语境泄露的风险，并建议使用具备权限感知能力的存储作为修复方案。

企业级版本的代表是 Copilot。在企业版发布的第一年，Gartner 对 132 位 IT 领导者的调查发现，过度共享[导致 40% 的企业推迟了 Microsoft 365 Copilot 的部署](https://www.computerworld.com/article/3542000/microsoft-365-copilot-rollouts-slowed-by-data-security-roi-concerns.html)达 3 个月或更久。这个案例之所以有用，是因为 Copilot 本身并没有做错什么。微软在查询时检查用户的权限，其文档称结果被“[修剪为登录用户有权访问的内容](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-apis-security-authentication)”。Copilot 展示的是这些人本来就有权打开的东西。

> 相当大一部分企业数据保持私密，仅仅是因为它们很难找到，而检索技术非常擅长发现事物。

这种暴露一直存在。相当大一部分企业数据保持私密，仅仅是因为它们很难找到，而检索技术非常擅长发现事物。

## **身份必须在何处介入**

所以从 Copilot 中得到的教训是，在组装环节解决身份问题是必要的，但还不够。组装环节继承了权限图谱实际所反映的内容。如果图谱是错误的、陈旧的或范围太广的，检索系统就会忠实地执行错误的答案。自研的检索系统可能会继承同样的问题，而且往往治理工具更少。

但这并不会削弱“组装”的重要性。它定位了它。组装并不能让您的权限变正确。它是正确权限仍然有效的最后关口，因为在此之后，模型已经读取了文档。

我并不是说这是我的发明。AWS 通过用湖泊已有的权限来管理图谱，也支持了这一观点。OWASP 从安全角度也得出了同样的结论，其对 LLM08 的建议修复方案是一个“知道是谁在提问的存储”，而不是事后运行的检查。

我想要补充的部分来自观察企业产品从试点走向生产的过程。团队可以在演示过程中推迟许多架构决策。但他们无法长时间推迟这一个。最终有人会问谁能看到什么、谁来担保、权限变更传播有多快，以及当三个不同的系统意见不一致时谁来负责。这通常是一个令人印象深刻的 AI 试点项目转变为安全项目的时刻，而它通常始于类似“实习生的问题”这类事件。

所以，对于任何构建此类系统的团队，我有四个问题：

1. 身份是在组装环节解决，还是在检索之后解决？
2. 在 IAM 无法覆盖的聊天记录、工单和文档中，有多少语境位于湖泊之外？
3. 当某人更换团队时，您的最坏情况下的陈旧窗口是多长？
4. 您是否能在流程的每一步重新检查授权，还是只在门口检查一次？

如果这些答案让人感到不安，那是有意义的。我参与的讨论中，大多都是如此。