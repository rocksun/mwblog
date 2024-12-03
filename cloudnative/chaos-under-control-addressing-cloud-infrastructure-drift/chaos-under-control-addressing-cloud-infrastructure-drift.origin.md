# How to Control Cloud Infrastructure Drift
![Featued image for: How to Control Cloud Infrastructure Drift](https://cdn.thenewstack.io/media/2024/11/a387581e-infrastructure-drift-chaos-control-1024x576.jpg)
Infrastructure drift is a pervasive challenge for organizations managing cloud resources at scale. While [Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code/) offers a structured approach to deploying and maintaining infrastructure, drift still occurs when changes happen outside IaC workflows. And this isn’t necessarily anomalous behavior — this can happen at any given time due to an external contractor, during a high-pressure situation (such as an incident) that requires quick resolution, or due to a lapse in judgment or an overly privileged tool.

**While we always aspire to maintain perfect IaC hygiene with flawless GitOps processes, unfortunately this is pretty much wishful thinking and impossible to enforce.** In practice, we see an overreliance on
[ClickOps](https://thenewstack.io/beyond-orchestration-a-comprehensive-approach-to-iac-strategy/)(or the manual execution of tasks by clicking through various options within software tools, which can be more accessible for users who may not be familiar with coding or scripting). And that manual process can often be the cause of infrastructure drift.
Infrastructure drift refers to the divergence between the actual state of infrastructure in the cloud and the desired state defined in IaC tools like [Terraform](https://thenewstack.io/is-terraform-dead-revive-your-infrastructure-as-code-strategy). This discrepancy can lead to security vulnerabilities, reliability issues and operational inefficiencies.

At Firefly, we scan and process more than 55,000 cloud accounts through our system daily. In that, we process almost 320,000 drifts per month, so we really understand the sheer magnitude and implications of the infrastructure drift problem. We’ve also seen that 90% of large-scale deployments using IaC experience drift, and about half of those cases go unnoticed. For those organizations, there’s a 100% chance of negative impact, whether it’s on reliability, security or toil.

**Common Causes of Infrastructure Drift**
There are many reasons infrastructure drift is so common, despite growing understanding that it needs to be mitigated. Many of the causes result from everyday maintenance of large-scale cloud infrastructure and high-velocity and high-pressure delivery cycles.

Common reasons infrastructure drift occurs include:

**Manual emergency fixes**: During incidents or emergencies, engineers often make direct changes to infrastructure through cloud consoles or APIs. These changes can address immediate issues but may bypass IaC pipelines, leading to drift.**Legacy resources**: Organizations that adopt IaC midstream may have existing resources that were created manually or with different tools. These unmanaged resources are prone to drift as they fall outside IaC governance.**Automated tools with permissions**: Tools like[cloud security posture management (CSPM)](https://thenewstack.io/why-you-no-longer-need-cloud-security-posture-management)may have permissions to modify configurations, such as security groups. When these tools make changes outside of IaC workflows, drift is introduced.**Partial IaC adoption**: Some organizations implement IaC selectively, managing only new or specific projects with IaC while older or different resources are managed manually. This inconsistency can result in drift across environments.**Environment misalignment**: Although production environments are often tightly controlled, staging and development environments may allow more flexibility for developers. Manual changes in these environments can create discrepancies, especially if configurations don’t match across environments.**IaC and cloud API misalignment**: Cloud providers frequently update their APIs and services, which can lead to drift if IaC tools aren’t updated to match. This misalignment can cause IaC deployments to diverge from the current cloud state.
Manual emergency fixes are unavoidable for even the most evolved engineering organizations. Yet, while these changes may address immediate issues, they bypass IaC pipelines, leading to discrepancies. Additionally, organizations that adopt IaC partway through their cloud journey may have legacy resources created outside IaC governance, making them prone to drift. Automated tools, such as CSPM systems, may have permissions to modify configurations such as security groups; changes made by these tools outside of IaC workflows can introduce further discrepancies.

**What Infrastructure Drift Looks Like**
Infrastructure drift can take many forms, often beginning with minor changes that snowball into significant discrepancies.

For instance, consider an [AWS](https://aws.amazon.com/?utm_content=inline+mention) identity and access management (IAM) policy managed through Terraform, where a drift occurs when someone adds something as simple as an asterisk (*) to a policy, which expands permissions from read-only to full access. Similarly, in a [Kubernetes](https://roadmap.sh/kubernetes) environment, a role with read-only permissions in IaC might be modified to include write and delete permissions in the actual cluster — which can potentially cause a lot of production damage. These seemingly small adjustments can compromise security and lead to unintended access.

When drift goes unchecked, it can pose risks beyond minor inconveniences.

Data from our [2024 State of Infrastructure as Code Report](https://www.firefly.ai/state-of-iac-2024) shows that it is often going unchecked. Not only is infrastructure drift frequently flying under the radar undetected, even when it is detected, it’s not getting remediated right away. Worryingly, 13% of the time, infrastructure drift isn’t fixed at all.

Beyond just the major risk of downtime, unaddressed drift can impact the stability and security of your infrastructure. For example, when permissions or configurations change outside IaC, it can open vulnerabilities that attackers might exploit. Drift can also affect service reliability if the infrastructure’s actual state doesn’t match the desired configurations tested in staging. All in all, drift is more than a just technical nuisance, and it can compromise your organization as a whole.

**First: Practical Approaches to Proactive Drift Detection**
Managing drift effectively requires robust monitoring and detection, as well as tried-and-true methods to mitigate it as quickly as possible.

Below are some handy tips for detecting and managing drift:

**Drift monitoring**:[Terraform](https://roadmap.sh/terraform)’s`plan`
or[Pulumi](https://www.pulumi.com?utm_content=inline+mention)’s`preview`
command can be used to detect drift, as can running AWS CloudFormation’s`drift detection`
command via the command-line interface (CLI). By scheduling regular checks, teams can compare the current infrastructure state with the desired configuration. If drift is detected, an exit code will indicate a discrepancy, enabling teams to respond accordingly.**GitOps for Kubernetes**: For Kubernetes environments, GitOps tools like Argo CD and Flux continuously reconcile the cluster state with the configuration stored in Git. These tools help ensure that any unauthorized changes are quickly reverted, maintaining alignment with the source of truth in Git.**Drift detection tools**: Open source tools like Driftctl and KubeDiff provide targeted drift detection capabilities. Driftctl works well with IaC tools like Terraform, while KubeDiff is optimized for Kubernetes configurations.**Real-time alerts and routing**: Establishing alerting mechanisms is crucial for effective drift management. By integrating IaC tools with Slack or[PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention), teams can receive real-time notifications of drift, enabling prompt resolution.
These are good ways to detect drift, but the goal must be remediating the drift.

**Next: Strategies for Drift Remediation**
Remediating drift can take two main forms: aligning the cloud environment with IaC or updating IaC to reflect the actual state. In cases where manual changes are temporary fixes, reapplying IaC configurations can restore the desired state. However, if manual changes represent necessary adjustments, it’s best to update the IaC templates to align with the actual state, preventing recurring drift.

If you’re just starting out with drift detection, a simple monitoring script using Terraform can provide valuable insights into discrepancies. Although this basic approach may not scale for large deployments, it can be effective for smaller setups or as a proof of concept. For larger environments, tools like Firefly, driftctl or GitOps frameworks provide a more robust solution for handling the complexity of enterprise-scale infrastructures.

**Getting Infrastructure Drift Under Control**
Infrastructure drift is an ongoing challenge in cloud environments, but with the right tools and practices, organizations can maintain control over their infrastructure.

By leveraging IaC, monitoring drift proactively and implementing strategies like GitOps, teams can minimize the impact of drift, ensuring infrastructure remains consistent and aligned with organizational needs. Regular drift detection and timely remediation ultimately improve the security, reliability and efficiency of cloud operations, empowering teams to deliver with confidence at the velocity modern companies require.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)