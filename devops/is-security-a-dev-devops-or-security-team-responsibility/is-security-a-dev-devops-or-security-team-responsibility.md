# 安全是 Dev， DevOps 还是安全部门的职责

在“谁应该负责安全？”这个问题的答案不是“每个人”之前，你的系统永远不可能达到最安全的状态。

译自 [Is Security a Dev， DevOps or Security Team Responsibility?](https://thenewstack.io/is-security-a-dev-devops-or-security-team-responsibility/) 。

![](https://cdn.thenewstack.io/media/2023/09/be001be8-teamwork-1024x603.jpg)
*图片来自 Shutterstock 的 alphaspirit*

无论你从事什么角色——软件开发、DevOps、IT 运维、安全或任何其他技术职位——你可能都明白[强大的网络卫生](https://orca.security/resources/blog/making-modern-cloud-security-a-reality/)的重要性。

但是你可能不确定谁的工作是落实这一原则。尽管大多数组织传统的[网络安全](https://roadmap.sh/cyber-security)方法是期望安全团队来管理风险，但安全工程师经常指责其他团队，告诉他们确保应用程序的设计和部署的安全是他们的工作。

而开发人员可能会声称[安全](https://thenewstack.io/security/)主要是 [DevOps](https://orca.security/resources/blog/devops-security/) 或 IT 运维团队的责任，因为这些是在生产环境中必须管理应用程序的团队——攻击发生的地方，而开发人员只设计和构建软件。

与此同时，运维人员经常将责任指向开发人员，认为如果应用程序中存在攻击者在应用进入生产后利用的[漏洞](https://orca.security/resources/blog/two-critical-cloud-vulnerabilities/)，问题的根源在于开发人员的错误，而不是 DevOps 或 IT 运维工程师。

除此之外，工程师还可以认为其他利益相关者承担主要的安全责任。例如，他们可能会说，如果发生违规，那是因为云供应商没有强大的访问控制，或者因为最终用户做了一些不负责任的事情。

## 云安全是集体责任

谁是对的？事实上没有人。安全不是任何一个组或角色类型的工作。

相反，安全是每个人的工作。有前瞻性的组织必须摒弃某个团队“拥有”安全的思维方式，而是将安全视为一个真正的集体团队责任，贯穿整个 IT 组织乃至更广泛。

毕竟，云安全有很多利益相关者，包括：

- 安全团队，他们负责了解威胁并提供如何避免威胁的指导。
- 开发人员，他们必须确保应用程序在设计时就考虑到了安全性，并且不包含不安全的代码或依赖易受攻击的第三方软件运行。
- IT 运维工程师，他们的主要工作是管理软件一旦投入生产，因此在配置安全的应用程序托管环境和监控应用程序以检测潜在风险方面发挥着领导作用。
- DevOps 工程师，他们的责任跨越开发和 IT 运维工作，使他们能够在开发和生产阶段保护代码。
- 云服务提供商，他们负责确保基础云基础架构的安全性，并提供组织用于保护云工作负载的一些(尽管肯定不是全部)工具(如身份和访问管理框架)。
- 最终用户，他们需要通过教育云安全最佳实践，以抵制应用程序之间不安全共享业务数据和网络钓鱼攻击等风险。

如果这些组中只有一个可以管理网络安全的各个方面，那就太好了，但他们做不到。存在太多类型的风险，这些风险体现在太多不同的工作流程和资源上，因此云安全不可能是任何一组的责任。

## 每个组织和每个安全责任模型都是不同的

除此之外，挑战在于，根据您的组织，上述所有组可能甚至都不存在。也许你不再有开发和IT运维团队，因为你已经将它们合并成一个DevOps团队。也许你的规模不足以雇佣一个全职的安全团队。也许你不使用公有云，在这种情况下，没有云提供商帮助保护基础基础架构。

我在这里的观点是组织各不相同，它们可以实施的安全模型也各不相同。在团队或角色之间委派安全职责没有一刀切的策略。

## 实践 DevSecOps

这就是为什么在你的组织中实际执行 [DevSecOps](https://orca.security/resources/blog/devops-security/) 非常重要，DevSecOps 指开发人员、安全团队和运维团队共同对云安全负责。

现在，这看起来可能很明显。如今有大量关于 DevSecOps 的讨论，许多组织声称正在“执行” DevSecOps。

但是一个企业说它已经[接受了 DevSecOps](https://orca.security/resources/blog/3-essential-tips-for-adopting-devsecops/)，不一定意味着安全已经渗透到该企业的所有单位和流程中。有时 DevSecOps 只是高管为了让自己听起来很重视安全性而滥用的术语，即使他们实际上没有改变围绕安全的组织文化。其他时候， DevSecOps 基本上意味着您的安全团队与开发人员和 IT 运维进行交流，但您的企业仍将安全团队视为安全运营的主要利益相关者。

这些方法是不够的。在[网络攻击](https://orca.security/resources/blog/top-5-cloud-security-threats-2023/)的速度和范围每年都创记录的世界里，安全真的需要成为您整个组织的工作——不仅仅是技术团队，而且还有非技术利益相关者，如您的“业务”员工，甚至外部利益相关者，如云服务提供商和合作伙伴。只有在组织的每个层面和每个阶段落实安全性，您才能对风险产生影响。

## 结论：要改变安全状况，改变思维方式

因此，不要只谈 DevSecOps 或满足于指定某个工程师组作为“拥有”安全的团队。相反，力求使云安全成为帮助保护 IT 资产的组织内外每个利益相关者的优先事项。在“谁负责安全？”的问题答案不是“每个人”之前，您永远不可能达到最安全的状态。

想掌控云安全吗？ [Orca 云安全平台](https://orca.security/platform/)为您的整个云环境提供全面可视性，为您整个云帐户清单中的漏洞、配置错误、入侵和其他潜在威胁提供优先警报。 要开始，请[请求演示](https://orca.security/demo/) Orca 云安全平台，或者今天注册进行[免费的云风险评估](https://orca.security/lp/cloud-security-risk-assessment/)。

## 延伸阅读

- [启用 DevSecOps：满足 Orca GitHub 应用程序](https://orca.security/resources/blog/orca-github-app-enabling-devsecops/)
- [从想法到现实：实施云安全策略](https://orca.security/resources/blog/implementing-your-cloud-security-strategy/)
- [2023 年要关注的顶级云安全趋势](https://orca.security/resources/blog/top-cloud-security-trends-2023/)
