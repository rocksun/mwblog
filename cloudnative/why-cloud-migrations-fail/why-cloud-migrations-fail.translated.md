# 云迁移失败的原因

![云迁移失败的特色图片](https://cdn.thenewstack.io/media/2024/01/9347d1ba-ai-iot-cloud-to-edge-1024x576.jpg)

[近 60% 的 IT 领导者](https://thenewstack.io/cloud-migrations-pick-up-the-pace-in-2024/) 计划今年将更多工作负载迁移到云。可以理解的是，[可扩展性的承诺](https://thenewstack.io/how-to-build-a-scalable-platform-architecture-for-real-time-data/)、成本节约和增强的协作使这成为一个引人注目的提议。然而，这是一个细致入微且规模庞大的任务，需要时间、关注和对安全有效使用的承诺。

有时，[云迁移](https://thenewstack.io/cloud-migrations-pick-up-the-pace-in-2024/) 会变得非常复杂或难以驾驭，以至于[无法实现预期的效益](https://thenewstack.io/cloud-migration-regrets-should-you-repatriate/)，导致成本超支和延误，或者过度依赖第三方。最终，复制和粘贴从少数几个善意但可能被过度炒作的案例研究中得出的路线图根本行不通。

在这里，我将回顾云迁移失败的三大主要原因，并提供一些关键指导，这些指导可能有助于企业安全团队和决策者纠正航向。

**共享责任模型**

云之旅中的一个绊脚石是对[共享责任模型](https://www.techtarget.com/searchcloudcomputing/definition/shared-responsibility-model) 的误解或混淆。此框架界定了云服务提供商 (CSP) 的安全义务（归结为保护底层基础设施）和客户（即保护数据、访问、应用程序和配置）。该模型需要对最终用户义务有清晰的理解，并强调协作和勤勉的必要性。

对 CSP 提供的安全监督水平的广泛假设会导致安全/数据泄露，美国国家安全局 (NSA) [指出](https://media.defense.gov/2024/Mar/07/2003407863/-1/-1/0/CSI-CloudTop10-Shared-Responsibility-Model.PDF)，“发生的频率可能比报告的要高”。值得注意的是，82% 的泄露事件[在 2023 年](https://www.wsj.com/tech/cybersecurity/why-are-cybersecurity-data-breaches-still-rising-2f08866c) 涉及云数据。

在云“迁移”的情况下，这种混淆往往会加剧，在这种情况下，照常运营、架构和实践只是被推送到云中，而没有适应其新的环境。在这些情况下，组织可能难以及时实施适当的程序、监控和人员，以匹配其新的云环境的安全限制。

虽然嵌入式安全级别*可以*根据所选的云模型（软件即服务、基础设施即服务、平台即服务）而有所不同，但客户通常必须实施严格的安全和[身份和访问管理 (IAM)](https://thenewstack.io/getting-started-with-identity-and-access-management/) 控制来保护其环境。如今，后者变得越来越重要，考虑到[近 40%](https://www.cybersecuritydive.com/news/exploits-credentials-fuel-ransomware-surge/717943/) 的勒索软件事件在 2023 年始于被盗的合法凭据。

[NSA](https://media.defense.gov/2024/Mar/07/2003407863/-1/-1/0/CSI-CloudTop10-Shared-Responsibility-Model.PDF) 在其指南中还警告说：“客户通常认为 CSP 保护客户数据的责任范围比实际范围更广，导致客户未能采取必要的措施。”

因此，云用户必须开发和压力测试事件响应手册，积极寻找入侵，部署[多因素身份验证](https://thenewstack.io/73-of-organizations-dont-enforce-multifactor-authentication/)，也许最重要的是，仔细审查“细则”，即他们与提供商的[服务级别协议 (SLA)](https://thenewstack.io/ignoring-slas-doesnt-pay/)。

**数据主权障碍**

我不能不提另一个房间里的大象：合规性。根据 2024 年云安全联盟报告，61% 的 IT 和安全领导者最近将合规性标准一致性列为 SaaS 环境中的主要挑战。法规增加了复杂性，尤其是在“数据主权”等及时考虑因素方面，即数据受其存储或处理所在国家/地区的法律和法规约束。
全球范围内，数据本地化法律的执行力度不断加强，部分原因是欧盟的《通用数据保护条例 (GDPR)》和《加州消费者隐私法 (CCPA)》等更广泛法规中的规定。这两项法规都对数据隐私和保护提出了严格的指导方针，包括对数据处理、存储和传输方式的强制性要求。

这可能给企业团队带来新的挑战，他们必须制定全面的治理框架，其中包括：

- 加密实践
- 严格的 CSP 选择标准（包括选择拥有本地数据中心的 CSP）
- 强制性、持续的审计等等
总而言之，在未考虑监管影响的情况下进行云迁移可能会增加成本、减缓进度，并可能需要在后期进行完全重新设计以补救控制措施。

**迁移后监督**
数据和应用程序迁移后，云之旅仍在继续。有效的管理需要一支高效的云运营团队来提供重要的支持功能，包括：

- 性能监控，以检测和解决问题
- 持续的安全评估，以防范已知和零日漏洞
- 身份控制，以管理对云应用程序的访问
- 成本管理，以防止预算超支
- 资源退役流程，以降低云蔓延或成本螺旋式上升的风险
正如科技培训平台 [InfoSec Institute 警告](https://www.infosecinstitute.com/resources/cloud/the-rise-of-cloud-computing-trends-and-predictions/) 那样，“[云] 比本地部署更复杂，需要了解……基本原理和原则。” 它补充道：“忽视新的范式……会带来巨大的风险。” 我完全同意。

组织必须规划永久性监督，并在项目启动时就提出这个问题。

**确保顺利迁移**
尽管存在挑战，但云计算拥有巨大的潜力，并能为团队节省大量前期投资于物理基础设施的成本。

通过定制设计、经过验证的控制措施和有效的管理，企业可以确保更顺利的云迁移之旅，并充分发挥其优势。经验丰富或思想开放的领导层和核心技术人员也将有助于顺利过渡。

每个组织都会有独特的路径。但是，在适当的指导下，团队可以避免笨拙、昂贵或有风险的流程，并在云中蓬勃发展。

[
YOUTUBE.COM/THENEWSTACK
科技发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)