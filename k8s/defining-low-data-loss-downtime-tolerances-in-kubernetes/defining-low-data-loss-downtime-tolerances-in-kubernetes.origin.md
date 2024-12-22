# Defining Low Data Loss, Downtime Tolerances in Kubernetes
![Featued image for: Defining Low Data Loss, Downtime Tolerances in Kubernetes](https://cdn.thenewstack.io/media/2024/12/25d22b1d-dr-1024x576.jpg)
More than ever, customers both want and expect a seamless experience. They expect a frictionless experience where their applications are highly performant and always available. This is no simple feat, especially with the rise of Kubernetes applications not only just becoming the norm, but becoming the orchestrator of choice to run mission-critical applications.

As the types of applications built on Kubernetes grow, so does the importance of maintaining business continuity to ensure that users — whether internal development teams or external customers — do not encounter disruptions.

Disaster recovery and business continuity policies help provide these critical applications with the availability and recovery procedures that prevent extended downtime or data loss, both of which can be disastrous for large enterprises.

**Defining Recovery Point and Recovery Time ****Objectives **
IT teams need to determine recovery point objective (RPO) and recovery time objective (RTO) tolerances for their applications. RPO defines the amount of acceptable data loss in the event of a disaster. For mission-critical applications, like [video streaming](https://portworx.com/customers/large-service-provider-case-study/) for example, zero data loss is acceptable. For less critical applications, RPO can be anywhere from a couple minutes, to a couple hours, to a couple of days. RTO defines the acceptable amount of time that an application can experience downtime.

RPO and RTO are determined by a number of factors, including application criticality, service-level agreements (SLAs) or regulatory requirements. With the growing footprint of Kubernetes applications, and the growing footprint of mission-critical Kubernetes applications, keeping RPO and RTO low has become increasingly vital. In the Portworx “[Voice of Kubernetes Experts Report 2024,” ](https://portworx.com/resources/voice-of-kubernetes-expert-report/)over 50% of respondents say that their cloud native platforms would benefit from added high availability and disaster recovery functionality.

**Supporting Low RPO in Complex Kubernetes Environments**
When developing critical Kubernetes applications, it is important to support them with an environment that can meet low RPO and RTO requirements. Losing critical application data or experiencing extended downtime can result in lost revenue, loss of brand equity or even regulatory penalties. An organization must be able to maintain business continuity and remain in operation even through an unexpected disaster. However, Kubernetes environments can introduce a number of complexities.

In the same survey, 86% of respondents said they were building their applications in hybrid and multicloud environments, taking advantage of the dynamic infrastructure of Kubernetes by deploying their applications across a range of environments like public and private cloud. This gives developers the freedom to flexibly deploy their applications in environments of choice, optimizing performance and cost.

Before Kubernetes, all you needed was the same storage hardware between two sites to provide synchronous and asynchronous replication. However, deploying Kubernetes applications across multiple environments makes replication much more difficult. You may not not have access to the same hardware in all your environments.

Some organizations may turn to data protection solutions that provide Kubernetes-native backup and recovery, but mere backup operations are not enough to provide low enough RPO or RTO to meet the needs of critical applications. To meet strict RPO requirements that demand little to no data loss you need a common storage layer that can replicate your data no matter where it’s located.

**Disaster Recovery for Kubernetes**
Beyond just replicating data, the storage management layer must also be able to replicate Kubernetes data to maintain business continuity. Containerized applications are not built the same as virtual machines. A Kubernetes disaster recovery solution must be able to recover application data as well as the underlying metadata, like application configuration and objects, in order to recover quickly. Otherwise, engineering teams waste precious time restoring application components separately or referencing documentation to walk them through recovery steps.

Achieving low RPO for Kubernetes applications requires automation. You want to be able to recover applications and all their associated components quickly and efficiently, especially for those mission-critical applications that can tolerate little data loss and downtime.

You will want to look for — or build — a solution that offers flexible disaster recovery policies that can support:

**Synchronous disaster recovery (DR)**provides an exact replica from the primary copy to the secondary copy, so that any changes made to the primary copy are reflected in the secondary copy. Synchronous DR solutions often require that clusters remain in the same metro region to limit latency.**Asynchronous DR**replicates data between copies based on a set schedule generally determined by RPO requirements. Since the data is not being copied automatically, there will be a delta between the primary and secondary copies.
In summary, when building applications on Kubernetes, it is important not only to define RTO and RPO tolerances across all tiers of application, but to also build an environment that can support your strictest SLAs. Kubernetes environments can introduce a host of complexities, including diverse infrastructure that spans on-premises and public cloud environments, as well as application structure. Disaster recovery solutions must be prepared to provide synchronous and asynchronous recovery to relevant applications.

To learn more about the “Voice of Kubernetes Experts 2024 Report,” [download a copy today](https://portworx.com/resources/voice-of-kubernetes-expert-report/). To learn more about Portworx and how we can provide flexible disaster recovery policies for any of your Kubernetes applications,[ learn more at our website](https://portworx.com/) or [read more about disaster recovery](https://portworx.com/kubernetes-disaster-recovery/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)