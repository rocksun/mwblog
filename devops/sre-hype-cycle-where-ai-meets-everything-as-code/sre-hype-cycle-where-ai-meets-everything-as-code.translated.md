# SRE Hype Cycle: Where AI Meets ‘Everything as Code’

![Featued image for: SRE Hype Cycle: Where AI Meets ‘Everything as Code’](https://cdn.thenewstack.io/media/2024/07/cee8226b-sre-hype-cycle-ai-everything-as-code-firefly.jpg)

In June, Gartner released its [2024 Site Reliability Engineering (SRE) Hype Cycle](https://www.gartner.com/en/documents/5522895), predicting trends—rising, declining, and peaking—that companies can leverage when making site reliability decisions. Companies including [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), and Firefly are pushing the boundaries of what’s possible in SRE and [platform engineering](https://thenewstack.io/platform-engineering/) across many areas and categories—including AI, which is at the peak.

SRE industry leaders are pouring significant effort and engineering into [AI](https://thenewstack.io/ai/), believing that the next wave will be embedding AI capabilities into [DevOps](https://roadmap.sh/devops) tools and platforms. But this isn’t just about providing out-of-context code snippets; it’s about truly understanding the nuances and complexities of modern cloud-native environments and leveraging AI’s unique capabilities to take our systems to the next level. This is why I believe the future of SRE will focus on delivering cloud-aware and contextually intelligent solutions.

AI needs to understand everything from Git to GitOps, microservice environments and cloud complexities, and CI/CD processes and workflows to provide truly valuable assistance and insights.

While AI is one of Gartner’s top SRE trends this year, here are some of the other most interesting areas I found in Gartner’s 2024 SRE Hype Cycle.

## Unified Policy as Code

One of the most exciting developments is the growing momentum behind [Policy as Code](https://www.youtube.com/watch?v=JR7RqoEIEEU) (PaC). While many companies claim to be doing PaC, the actual implementation varies greatly.

It’s important to consider PaC from both a CI/CD and runtime environment perspective. Focusing on only one area—such as scanning code only, enforcing CI/CD policies only at deployment and GitOps, or implementing runtime security only after deployment or remediation—won’t provide comprehensive coverage. Combining PaC and AI automation to generate these policies and guardrails is where the real innovation lies in applying automation at scale.

Strong PaC is also a pillar of Governance as Code (GaC), an emerging category also known as DevOps continuous compliance automation. The difference between policy and governance is management and hygiene. Common tasks such as proper tagging, eliminating waste, and implementing liveness probes in every [Kubernetes](https://thenewstack.io/kubernetes/) deployment are important aspects of governance. When governance can be managed as code, it can be automated and enforced more consistently, leading to better compliance with regulatory requirements and internally defined policies.

## Codifying Entire SaaS into Code

Codifying your entire cloud footprint—“[cloud to code](https://www.firefly.ai/use-cases/everything-as-code)”—enables engineering organizations to apply the same coding practices across all clouds. This allows you to treat all platforms as infrastructure, including monitoring, application performance management, version control systems, content delivery networks, and everything else.

There are many benefits to managing the diversity of software-as-a-service (SaaS) platforms as code. It’s no surprise then that Gartner included [Monitoring as Code](https://www.youtube.com/watch?v=LeRgHihHTcE) (MaC) in its 2024 report. MaC, like all things related to code management, enables you to manage your monitoring systems the same way you manage all your infrastructure as code.

## Infrastructure Orchestration Through Workflows

Infrastructure orchestration needs better automation, CI pipeline management, and portability, repeatability, and visualization to deliver at the speed today’s businesses require on one platform. Traditional [CI/CD](https://thenewstack.io/ci-cd/) management approaches are fragmented and painful between software and infrastructure.

Repeatability requires understanding the entire cloud environment and implementing guardrails in the form of drift and misconfiguration detection from deployment to runtime. Implementing guardrails to enforce policies—whether security, cost considerations, or code quality—empowers platform engineers to give developers more autonomy.

## Immutable Infrastructure and Cloud Resilience

### EDITOR'S RESPONSE
不可变基础设施是确保环境在部署后保持一致性和可靠性的关键。实现这一目标的一种方法是通过自动化将弹性融入云管理，能够检测和自动修复漂移和错误配置，并防止生产错误。自动修复有助于快速解决云问题，维护生产环境的完整性和性能。

许多云配置尚未准备好应对复杂场景。例如，考虑[UniSuper](https://www.informationweek.com/cyber-resilience/lessons-learned-from-the-unisuper-cloud-outage)最近发生的灾难性云中断。尽管UniSuper的基础设施经理拥有独立的备份（他应该为此获得荣誉勋章），但UniSuper仍然花费了一整周的时间才从中断中恢复过来。

这是因为从这种严重的中断中恢复不仅是备份系统和数据的问题——还需要备份配置。云弹性和自动化事件恢复和响应方面的创新将包括对云中所有系统配置进行编码备份。这有助于使恢复快速而全面，并最大程度地减少停机时间——即使在巨大的灾难中也是如此。

## 真正的创新带来真正的影响

如果SRE炒作周期无法兑现其承诺，那么它就只是炒作。Firefly非常自豪地被列入[Gartner的用于基础设施即代码的AI助手](https://www.linkedin.com/posts/fireflyai_sre-sitereliabilityengineering-sitereliabilityengineer-activity-7211361139136372736-mqQo?utm_source=share&utm_medium=member_desktop)类别，处于炒作周期的顶峰。很高兴看到像Firefly这样的行业巨头和新兴公司因致力于为SRE和平台工程师提供真正有用的创新而获得认可。

Gartner 2024年SRE炒作周期突出了行业发展趋势和方向。SRE和平台工程的未来一片光明，Firefly很高兴能够走在这些新兴趋势的前沿。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。