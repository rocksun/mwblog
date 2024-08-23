# Beyond Orchestration: A Comprehensive Approach to IaC Strategy
![Featued image for: Beyond Orchestration: A Comprehensive Approach to IaC Strategy](https://cdn.thenewstack.io/media/2024/08/196d3b2f-iac-1024x574.png)
In the past decade since the large-scale adoption of cloud (native) technologies, [Infrastructure as Code (IaC)](https://thenewstack.io/the-pros-and-cons-of-iac-what-you-need-to-know/) has been the core of enabling the unprecedented growth and manageability of very complex systems. However, much like other domains with their evolutions and intrigues, the IaC landscape has also undergone quite a bit of change.

In this year alone [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) replaced its open source [license for Terraform](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/) with a more restrictive one, and [the community forked](https://thenewstack.io/new-opentofu-release-challenges-terraforms-dominance/) this most ubiquitous tool. (I spoke about this recently at a panel at KubeCon Paris called “[The Evolution of IaC: On Open Source and Everything Else](https://kccnceu2024.sched.com/event/1YeOi)”).

This leaves us, as platform engineers and DevOps professionals, grappling with two primary dilemmas when crafting our IaC strategy:

- Which IaC tool should we use? Terraform, OpenTofu, cloud-specific solutions like
[AWS](https://aws.amazon.com/?utm_content=inline+mention)CloudFormation or Kubernetes controllers like Crossplane? - How should we handle orchestration? Should we build our own IaC provisioning pipeline in our
[CI/CD](https://thenewstack.io/ci-cd/)tools or invest in IaC automation products like Terraform Cloud?
While these questions are undoubtedly crucial, they only scratch the surface of what a comprehensive IaC strategy should encompass. With IaC now serving as the backbone to the way we deliver software and the critical systems they run on — the [CrowdStrike outage](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/) is just one example of how this can go very wrong — our IaC strategy will have a direct impact on our business operations. To truly channel the power of IaC, organizations need to look beyond just tool selection and orchestration. These are honestly just implementation details. Let’s explore the often-overlooked aspects that can make or break your IaC operations and systems engineering.

**The Missing Pieces in Your IaC Strategy**
**1. IaC Coverage: The Critical KPI You’re Not Measuring**
IaC coverage represents the percentage of your cloud resources managed through IaC. This crucial metric provides insight into the health and maturity of your cloud infrastructure management.

Why is IaC coverage so important?

- It indicates how much of your infrastructure is consistently managed and version-controlled.
- It helps identify areas of potential risk (unmanaged resources are not DR-Compliant).
- It serves as a benchmark for continuous improvement in your cloud governance.
Despite its significance, most cloud providers don’t offer visibility into this metric. Without understanding your IaC coverage, you’re essentially flying blind in your cloud management efforts.

We’ve learned over many years of writing infrastructure code that all of these combined lead to greater system health and stability over time through better guardrails, governance and maintainability. When systems aren’t codified — and much of this leads to the next point — which at times is a byproduct of older and legacy systems, it is much harder to visualize, manage and maintain systems, and even recover from failure.

**2. Dealing with Existing Resources: The Legacy Challenge**
Lambda is celebrating its 10th anniversary this year, so let’s not talk about Amazon Elastic Compute Cloud (EC2) which will be celebrating two decades in 2026. For young engineers now entering the trade, the cloud has been around forever — there was no time before the cloud. However, for more seasoned engineers, we know what came before (and it ain’t pretty).

We’ve found that when adopting IaC, organizations often focus on new deployments while neglecting existing infrastructure — some pre-cloud or early cloud days when everything was managed through the console. This oversight can lead to a hybrid state where some resources are managed via IaC while others remain as “ClickOps” console creations (unmanaged by IaC, and not deriving the benefits of IaC noted above).

The ClickOps challenge lies in:

- Identifying which resources are not currently managed by IaC
- Determining the effort required to “codify” these existing resources
- Prioritizing which resources to bring under IaC management first
Without a strategy for addressing existing resources, organizations risk perpetuating a divided infrastructure, undermining the benefits of IaC adoption. In addition, we’ve all learned that sometimes our most legacy systems are our business “cash cows” and mission-critical systems. It’s not just a matter of letting them remain uncodified and unmanaged. These are usually the primary systems that will hurt the most when they go down and cause the most pain when not rapidly recovered.

**3. Multi-IaC Reality: One Tool Doesn’t Fit All**
In large organizations, enforcing a single IaC tool across all departments is often impractical. Today, there are a diversity of tools that cater to different stacks, strengths and collaboration with developers — from those that are native to a specific platform (CloudFormation or ARM for Azure), and those for multicloud or cloud native, from Terraform and OpenTofu, to Helm and Crossplane, and those that cater to developers like Pulumi or AWS Cloud Development Kit (CDK). Different teams may prefer different tools based on their expertise, use cases or specific project requirements.

A robust IaC strategy must account for:

- The coexistence of multiple IaC tools within the organization
- Visibility across various IaC implementations
- Governance and compliance across diverse IaC ecosystems
Ignoring this multi-IaC reality can lead to silos, reduced visibility and governance challenges. In the same way that many teams today select their clouds, programming languages and stacks based upon a diversity of criteria from performance to complexity, overhead maintenance and more, the same goes for IaC. With different tools optimized for different stacks and use cases, understanding how to manage the many tools in this landscape is part and parcel to a robust IaC strategy.

**Comprehensive IaC Management**
As DevOps and platform engineers, we’ve developed a platform that we ourselves have needed over many years of managing cloud fleets at scale. A platform that addresses not just tooling and orchestration, but all aspects of a comprehensive IaC strategy can be the difference between 2 a.m. downtime and a good night’s sleep.

Such a single platform can transform the engineering team’s approach to IaC and evolve with a continuously changing cloud landscape:

**Complete visibility —**automatically discovers all assets across your multicloud accounts, providing a clear inventory of managed and unmanaged resources in a single dashboard, no matter what cloud your resources and assets are running on.**IaC coverage insights —**offers real-time metrics on your IaC coverage, helping you understand which resources are managed by IaC and which aren’t, and the risk severity helping to optimize planning for codification of critical resources and assets.**Multi-IaC support —**recognizes and supports various IaC tools, giving you a unified view of your infrastructure regardless of the IaC solution used. In this way, the tool selection is decoupled from the management and maintenance, and teams are able to choose the right tool for the workload.**Automated codification (such as reverse IaC) —**can automatically “codify” existing resources into your preferred IaC format, significantly reducing the manual effort required to bring legacy resources under IaC management, and migrate between IaC tools.**Drift detection —**identifies resources that have deviated from their IaC-defined state, helping maintain consistency and security. Drift is a growing problem in large-scale systems, where cloud assets are still changed via console and ClickOps.**Governance and compliance —**ensure that all resources, regardless of how they were created, adhere to your organization’s standards without hindering real-time incident response.**Orchestration and beyond —**Beyond robust orchestration, it offers a comprehensive suite of tools for managing your entire IaC life cycle.
**Elevate Your IaC Strategy**
As the cloud continues to grow in complexity and evolve, so too must our approach to managing it. By looking beyond just tool selection and orchestration, and ensuring your IaC strategy focuses on additional and critical aspects that include IaC coverage, legacy resource management and multi-IaC support, organizations can unlock the full potential of their cloud infrastructure.

Ready to take your IaC strategy to the next level? [Book a demo](https://www.firefly.ai/demo) or [start using Firefly for free](https://try.firefly.ai/dashboard) today and experience the future of cloud asset management.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)