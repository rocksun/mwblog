<!-- 
# 如何防止 AI 系统给 Kubernetes 部署带来风险
https://cdn.thenewstack.io/media/2023/10/0e694464-kubernetes1a-1024x683.jpg
 -->


将 AI 系统引入 Kubernetes 环境可能会带来许多挑战。让我们来看四个主要问题，以及如何应对这些风险。

译自 [How to Prevent AI from Hurting Your Kubernetes Deployments](https://thenewstack.io/how-to-prevent-ai-from-hurting-your-kubernetes-deployments/) 。

全球各地，AI技术正在爆炸式增长，但并非所有应用这项快速进步技术的人都怀着良好意图。

当今动荡的[网络安全](https://thenewstack.io/security/)局势意味着IT领导者必须注意AI技术给他们的运营带来的各种风险，例如生成复杂的钓鱼攻击、为恶意目的合成数据、用对抗样本欺骗AI系统，以及通过污染数据破坏AI模型。

从[云原生](https://thenewstack.io/cloud-native/)的视角来看，我们目睹了AI技术被利用来绕过传统安全措施的例子。例如[最近出现的WormGPT](https://protect-us.mimecast.com/s/1rA3CDkx22TB8AkkHAszhG?domain=thehackernews.com)，一种被用来发动精密网络钓鱼和商业电子邮件威胁的生成式AI工具。加上肆虐的勒索软件，这为IT领导者带来一个日新月异的风险环境。仅过去一年，据[Veeam的2023年勒索软件报告](https://protect-us.mimecast.com/s/f1pUCERy22cWZxNNIPzTzM?domain=veeam.com)，85%的组织遭受过至少一次勒索软件攻击。

## 将AI引入Kubernetes环境

AI技术为人机交互引入了自然语言，自动化[Kubernetes](https://roadmap.sh/kubernetes)工具链的各个方面，并在大数据集上综合信息，这有望极大提升云原生应用和运维的价值。但同时，将AI引入Kubernetes环境也会带来许多挑战。让我们考虑四个这样的挑战及如何应对。

## 这是个瞬息万变的环境

AI对安全部队来说还太新，他们还无法充分理解AI带来的风险。例如，一个新兴的威胁是利用AI生成的合成数据来制造假身份、文件或证书，以绕过安全措施或冒充授权用户。同样，许多部署Kubernetes的组织对这个系统的来龙去脉并不熟悉，一旦把AI引入，组织就会面临未知威胁的固有风险。生成式AI的进化意味着新的攻击面不可避免。跟所有的勒索软件攻击一样，问题不再是是否，而是何时。

AI有一个学习曲线，我们正在边干边制定和修改规则，继续尝试和测试它的功能。对想部署AI的Kubernetes领导者来说，拥有一个积极的行动指南非常有帮助，以确保满足一些基本和关键的条件，比如修订网络治理策略。

这个不断发展的领域有几个框架可以帮助快速启动，包括MITRE[机器学习威胁矩阵](https://attack.mitre.org/)和NIST [AI风险管理框架](https://airc.nist.gov/docs/AI_RMF_Playbook.pdf)。由于环境持续变化，该指南应及时演进和更新。这不仅有助于满足基本条件，还可以跟踪AI在Kubernetes环境中的进展、反应和影响。

## 找到使用案例

发现使用案例是采用AI的第一步。这引出一个问题和挑战，即判断你的用例属于低风险/低影响还是高风险/高影响。你现有的技术历史上已经证明了各自的风险和影响级别，但AI不能简单类比。

你需要在增加AI视角的情况下重新评估风险。例如，对抗样本可以向图像或声音添加细微的噪声或畸变，导致AI系统错误分类或提供不正确信息。这可能给依赖AI决策的应用带来严重后果，如自动驾驶汽车、医学诊断或人脸识别。

与任何光鲜亮丽的新事物一样，AI需要谨慎对待，但仍应积极推进。正如每日新闻所提醒我们的，在云原生领域没有缺乏创新和活跃的AI项目，从声称[提升55%效率](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)的GitHub Copilot，到支持Nvidia GPU增强性能的Kubernetes。

组织应该亲自动手，在自己的环境中评估各种开发工具，试验AI以识别其优劣。最好起初在安全可控的环境下进行这些试验，同时密切关注行业的版权问题和不断[演变的法规](https://www.europarl.europa.eu/news/en/press-room/20230505IPR84904/ai-act-a-step-closer-to-the-first-rules-on-artificial-intelligence)，这是明智的启蒙之路。

## 在DevSecOps基础上改进

安全是组织中的共同责任，需要开发到部署的各方协作配合。为保持高效率，关注点分离可以让每个团队专注核心能力和任务。然而，这也产生数据孤岛和安全漏洞，可能危害组织的安全态势。已经实施了DevSecOps实践和自动化工具以弥合鸿沟，确保安全成为优先事项而不是事后考量。

举一个潜在缺陷的例子，你当前的政策和实践是否可以防止数据污染？再加上sig-security审计发现，Kubernetes审计日志并未捕获所有相关信息进行安全分析，如API请求的源IP地址、用户代理和请求体。增强审计日志以包含更多信息，这可以帮助识别API请求的来源和意图，并支持不同的日志格式和目标，这对提供共享上下文很有帮助。

集成AI的应用往往更复杂和动态，需要在整个生命周期内持续测试、监控和验证，利益相关方也在增多。增强DevSecOps工具和实践可以通过在持续集成和交付流水线中自动化这些活动来促进它们，实现更快的反馈和错误纠正。

例如，纳入数据治理策略以维护对容器镜像以及训练和生产数据的加密、审计和受控访问非常重要。合规性即代码构造需要在开发环境中扩展，以纳入[NIST](https://www.nist.gov/itl/ai-risk-management-framework)等针对AI的各种监管标准。

## 重新审视红蓝队

红队是一群模拟真实网络攻击的道德黑客，目的是测试安全态势并识别漏洞。

AI技术现在可以为红队提供“增强剂”，使他们能够更好地模拟真实对手的战术、技术和程序。然而，鉴于AI为组织带来的不断增多的攻击面，你也需要重新培训或聘请第三方以保护你免受日益增多的威胁，包括模型和数据提取或篡改、数据污染以及对抗输入。请参考[Microsoft的AI红队](https://www.microsoft.com/en-us/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/)报告和指南。

蓝队通常专注于积极的防御策略、威胁检测、事件响应和漏洞管理。AI技术可以成为这种团队的效率增强器，因为AI解决方案可以综合和分析不同来源的大量数据，以及分析异常行为。请参考[谷歌的安全AI框架](https://services.google.com/fh/files/blogs/google_secure_ai_framework_approach.pdf)或[保护AI流水线](https://www.mandiant.com/resources/blog/securing-ai-pipeline)的指南。这些升级和新工具值得投资。

## 加强最后一道防线

作为一个关键的临别思考，请记住你的安全措施可能无法阻止所有攻击。所以你需要为Kubernetes环境提供最后一道防线，以防范像勒索软件这样的攻击。一个与任何环境(存储、云或分布式)兼容、能及时跟上最新进展的数据保护解决方案就是你需要的。

你还需要全面保护Kubernetes应用程序，包括可能使用向量数据库以及SQL/NoSQL数据服务的AI应用程序。通过准备好可以在这个快节奏的云原生环境中恢复、检测和预防攻击的主动工具和流程，你将获得长期利益。
