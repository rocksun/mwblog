We’re now several years into the adoption of platform engineering, which has been widely accepted as the best way for organizations to accelerate software development and transition to modern software methods. Gartner expects that by 2026, around [80% of organizations will have a dedicated platform engineering team](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering).

However, despite significant attention and some notable successes, many organizations have found that their initial platform engineering efforts aren’t meeting their expectations. This is happening not because [platform engineering is the wrong](https://thenewstack.io/youre-doing-platform-engineering-wrong-probably/) approach, but because platform teams have been too narrowly focused.

## Why Platform Engineering Teams Are Missing the Infrastructure Foundation

For most organizations, platform engineering is a significant undertaking. You’d like to start with a clean slate, but your organization may have multiple development teams with widely differing concerns plus significant investments in hardware, software, and tools. Here are four common areas where platform teams go astray.

**Insufficient Attention to Infrastructure**: Many teams focus their efforts on internal developer platforms (IDPs). This makes sense since that’s where [developers spend all their time](https://thenewstack.io/why-traditional-logging-and-observability-waste-developer-time/), but with so much focus on the IDP, the underlying infrastructure becomes an afterthought. When the foundation is weak, the whole building is shaky.

**Failure to Balance Developer Experience (DX) vs Cost:** For platform teams getting started, DX and developer productivity tend to take priority. However, if your costs are unsustainable, your platform will eventually be compromised, especially if you’re growing fast.

For example, Ada initially tried to have [everyone share two development clusters](https://www.vcluster.com/case-studies/ada-cx), but found that the developers were overwriting each other’s work. The company initially contemplated giving each developer their own cluster, but realized that this would be too expensive and too difficult for developers to manage.

**Security, Compliance, and Governance are an Afterthought**: Given today’s regulatory environment and growing cyberthreats, security, compliance, and governance are so critical that they need to be built into your platform from the outset. Layer them on after the fact, and you’ll always be playing catch-up and incurring greater risk.

**Failure to Align Platform Architecture with Future Needs**: Often, through no fault of their own, platform [teams end up creating general-purpose platforms to support](https://thenewstack.io/how-team-topologies-supports-platform-engineering/) a variety of architectures, including both legacy and modern ones. As more and more workloads [migrate to Kubernetes](https://thenewstack.io/how-to-jump-start-your-stalled-kubernetes-migration/), these platforms become increasingly inefficient.

## Infrastructure Platform Engineering: The Evolution Beyond Developer Tools

Like any new discipline, [platform engineering is evolving](https://thenewstack.io/platform-engineering-is-devops-evolved-new-report-shows/). Organizations are extending the concept [platform engineering to explicitly encompass infrastructure](https://thenewstack.io/the-pillars-of-platform-engineering-part-5-orchestration/) platform engineering (IPE), shifting away from an exclusive focus on DX and IDEs.

IPE focuses on building self-service, scalable, and cost-efficient infrastructure platforms tailored to cloud native environments. Unlike approaches that primarily aim to streamline developer workflows and abstract infrastructure complexity, IPE is concerned explicitly with providing scalable, policy-driven, and cost-aware [Kubernetes infrastructure that empowers your teams to operate](https://thenewstack.io/understanding-the-kubernetes-operator-pattern/) efficiently at scale. IPE addresses the concerns outlined above.

**Infrastructure as a First-Class Concern:** With IPE, you prioritize the underlying infrastructure, ensuring that multitenancy, isolation, cost efficiency, and governance are built in from the start.

**Efficiency and Productivity:** IPE optimizes for infrastructure efficiency, reducing waste, and ensuring cost-aware scaling.

**Policy-Driven and Secure by Design:** Security, compliance, and governance are integrated into the platform, enabling a secure, shared infrastructure that eliminates [operational bottlenecks while controlling](https://thenewstack.io/chaos-to-control-3-steps-for-automating-incident-management/) costs.

**Built for Kubernetes-Native Workloads:** IPE is tailored for the dynamic environments, ephemeral workloads, and multi-cloud strategies of organizations transitioning to Kubernetes.

## Getting Started With Infrastructure Platform Engineering Implementation

The good news is that many organizations can migrate to IPE from where they are today without having to start from scratch. It’s like lifting up a house to build a new, solid foundation underneath.

If your team has embraced [Kubernetes and has reasonable visibility into existing costs](https://thenewstack.io/how-to-gain-visibility-into-kubernetes-cost-allocation/), workloads, and failures, you should be a candidate to get started. The key is to identify the structural weaknesses in your current platform(s) to determine where to apply IPE principles. The following roadmap provides a useful starting point.

| Getting Started with IPE: A Practical Roadmap | |
| --- | --- |
| STEP 1: | Audit your platform(s) for cost, governance, and infrastructure failure points. |
| STEP 2: | Shift platform design to treat infrastructure as a product. |
| STEP 3: | Define policy-as-code and cost metrics from Day 1. |
| STEP 4: | Adopt Kubernetes-native tooling  (virtual Kubernetes, hierarchical multi-tenancy, etc.) |

If your organization would benefit from IPE, ask yourself whether your current platform team is equipped to execute against this roadmap, and consider adding or bringing in infrastructure specialists to help.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/03/5d566d7a-lukas-gentele.jpg)

Lukas Gentele is the CEO and Co-founder of Loft Labs, the leading provider of building blocks for platform teams that enable companies to operate their cloud infrastructure more efficiently using virtual Kubernetes clusters. Gentele has deep expertise in enterprise architecture,...

Read more from Lukas Gentele](https://thenewstack.io/author/lukasgentele/)