# SRE Hype Cycle: Where AI Meets ‘Everything as Code’
![Featued image for: SRE Hype Cycle: Where AI Meets ‘Everything as Code’](https://cdn.thenewstack.io/media/2024/07/cee8226b-sre-hype-cycle-ai-everything-as-code-firefly.jpg)
In June, Gartner released its [Site Reliability Engineering (SRE) Hype Cycle for 2024](https://www.gartner.com/en/documents/5522895), forecasting trends — rising, falling and peaking — companies can use when making site reliability decisions. Companies including [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) and Firefly are pushing the boundaries of what’s possible in the realm of SRE and [platform engineering](https://thenewstack.io/platform-engineering/) across many domains and categories — including AI, which is sitting at its peak.

SRE industry leaders are investing significant effort and engineering in [AI](https://thenewstack.io/ai/), believing that the next exciting wave will be embedded AI capabilities in [DevOps](https://roadmap.sh/devops) tooling and platforms. It’s not just about providing out-of-context code snippets though; it’s about truly understanding the nuances and complexities of modern cloud native environments and leveraging AI’s unique capabilities to take our systems to the next level. This is why I believe SRE’s future will be focused on delivering solutions that are cloud-aware and contextually intelligent.

AI needs to understand everything from Git to GitOps, microservices environments and cloud complexities, and CI/CD processes and workflows to provide truly valuable assistance and insights.

While AI is one of Gartner’s top SRE trends this year, here are some of the other areas I found most interesting in Gartner’s SRE Hype Cycle for 2024.

## Unified Policy as Code
One of the most exciting developments is the growing momentum behind [Policy as Code ](https://www.youtube.com/watch?v=JR7RqoEIEEU)(PaC). While many companies claim to be doing PaC, there is a wide spectrum of what that implementation actually looks like.

It’s important to think about PaC in the context of CI/CD and runtime environments. Focusing on only one area — such as only scanning code, enforcing CI/CD policy only on deployment and GitOps, or implementing runtime security only after deployment or remediation — won’t provide full coverage. Combining PaC and AI automation to generate these policies and guardrails is where the real innovation lies in applying automation at scale.

Robust PaC is also the backbone of Governance as Code (GaC), an emerging category that is also known as DevOps continuous compliance automation. Where policy and governance differ is around management and hygiene. Common tasks like proper tagging, eliminating waste and implementing liveness probes in every [Kubernetes](https://thenewstack.io/kubernetes/) deployment are essential aspects of governance. When governance can be managed as code, it can be automated and enforced more consistently, enabling greater compliance with regulatory requirements and internally defined policies.

## Codifying Your Entire SaaS
Codifying your entire cloud footprint — “[from code to cloud](https://www.firefly.ai/use-cases/everything-as-code)” — enables engineering organizations to apply the same coding practices across all clouds. This allows you to treat all platforms like infrastructure, including monitoring, application performance management, version control systems, content delivery networks and everything else.

There are many benefits to managing the diversity of your software as a service (SaaS) platforms as code. Therefore, it is no surprise that Gartner included [Monitoring as Code](https://www.youtube.com/watch?v=LeRgHihHTcE) (MaC) in the 2024 report. MaC, like everything related to as-code management, enables you to manage your monitoring systems like you would manage all infrastructure as code.

## Infrastructure Orchestration Through Workflows
Infrastructure orchestration requires better automation, CI pipeline management, and portability, reproducibility and visualization in a single platform to deliver at the pace business requires today. Traditional approaches to [CI/CD](https://thenewstack.io/ci-cd/) management are fragmented and painful across software and infrastructure.

Repeatability requires an understanding of the entire cloud environment and implementation of guardrails in the form of drift and misconfiguration detection from deployment to runtime. Putting guardrails in place to enforce policy — whether it’s security, cost considerations or code quality — enables platform engineers to provide greater autonomy to developers.

## Immutable Infrastructure and Cloud Resilience
[Immutable infrastructure](https://thenewstack.io/a-brief-look-at-immutable-infrastructure-and-why-it-is-such-a-quest/) is key to ensuring that environments remain consistent and reliable once they have been deployed. One way to achieve this is by automating resilience into cloud management by being able to detect and automatically fix drifts and misconfigurations and prevent production errors. Auto-remediation helps quickly address cloud issues, maintaining the integrity and performance of production environments.
Many cloud configurations are not yet ready for complex scenarios. For example, consider [UniSuper](https://www.informationweek.com/cyber-resilience/lessons-learned-from-the-unisuper-cloud-outage)’s recent catastrophic cloud outage. Even though the infrastructure manager at UniSuper had a separate backup (for which he deserves a medal of honor), it still took UniSuper an entire week to recover from the outage.

This is because recovering from a serious outage like this is not only a matter of backing up your systems and data — your configurations also need to be backed up. Innovations in cloud resilience and automated incident recovery and response will include having codified backups of all of your systems configurations in the cloud. This helps make recovery swift and comprehensive with minimal downtime — even in an enormous catastrophe.

## Real Innovation for Real Impact
The SRE Hype Cycle is only hype if it fails to deliver on its promises. Firefly is very proud that we were named in [Gartner’s AI Assistants for Infrastructure as Code](https://www.linkedin.com/posts/fireflyai_sre-sitereliabilityengineering-sitereliabilityengineer-activity-7211361139136372736-mqQo?utm_source=share&utm_medium=member_desktop) category at the peak of the hype cycle. It’s great to see that industry giants and emerging companies like Firefly are recognized for our dedication to providing real, useful innovations for SREs and platform engineers.

The Gartner SRE Hype Cycle for 2024 highlights the trends and directions where the industry is headed. The future of SRE and platform engineering is bright, and Firefly is thrilled to be at the forefront of these emerging trends.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)