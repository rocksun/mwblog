# Why FinOps Belongs in Your CI/CD Workflow
![Featued image for: Why FinOps Belongs in Your CI/CD Workflow](https://cdn.thenewstack.io/media/2025/03/bb187a6b-shift-left-finops-ci-ci-1024x674.jpg)
[Infrastructure as Code (IaC)](https://thenewstack.io/introduction-to-infrastructure-as-code/) has transformed cloud provisioning, but without governance, cost awareness and proactive enforcement, organizations risk spiraling cloud expenses or increased security and compliance risks. The evolution of IaC has given rise to [Policy as Code (PaC) and Governance as Code (GaC)](https://thenewstack.io/for-infrastructure-as-code-ci-cd-can-beat-terraform/), enabling organizations to apply structured, automated policies across domains beyond security.
This practice is now extending into [FinOps](https://thenewstack.io/finops/) to enable cost governance to be codified, ensuring that financial guardrails are enforced as part of infrastructure automation, much like compliance and security policies.

The shift-left approach originated in software security, emphasizing early-stage vulnerability detection within development workflows to minimize risks and remediation costs. Traditionally, security testing occurred late in the development lifecycle, often leading to expensive fixes and compliance gaps. By shifting security left — integrating automated security checks, compliance policies and best practices into [CI/CD pipelines](https://thenewstack.io/ci-cd/) — organizations can proactively mitigate threats before code reaches production.

Now the same principles are being applied to FinOps, embedding cost awareness, forecasting and governance earlier in the software delivery process. Instead of waiting for monthly cloud bills to assess expenses, shift-left FinOps integrates cost estimation, tagging enforcement and budget constraints directly into infrastructure provisioning to codify financial accountability as early as possible.

Let’s explore the application of [shift-left principles](https://thenewstack.io/its-time-to-start-shifting-left/) to FinOps and examine how integrating cost visibility into CI/CD workflows, enforcing tagging through governance policies and leveraging cloud waste reduction strategies can provide financial accountability without restricting developer autonomy.

**GaC and PaC for FinOps**
GaC and PaC are now fundamental in enforcing GitOps guardrails, ensuring consistency, compliance and security across infrastructure and application deployments. By codifying governance policies, organizations can automate access controls, enforce security baselines and standardize resource configurations across environments. These practices help prevent misconfigurations, enforce cost constraints and maintain auditability by embedding rules directly into Git workflows.

As GitOps becomes a central practice in modern DevOps, GaC and PaC serve as critical enforcement layers, enabling automated drift detection, continuous compliance monitoring and proactive remediation so that infrastructure and operational policies remain intact without manual intervention. GaC and PaC are becoming more essential than ever before in enforcing financial best practices within IaC workflows.

By codifying FinOps governance policies, teams can put guardrails in place while still granting developers autonomy to create resources. Guardrails don’t stifle innovation — they’re simply there to prevent costly mistakes. Every engineer makes mistakes, but guardrails ensure that those mistakes don’t lead to $10K-per-day cloud bills due to an overlooked database instance in a Terraform template taken off of GitHub.

Additionally, policy enforcement must be dynamic and flexible, allowing organizations to adjust tagging, cost constraints and security requirements as they evolve. AI-driven governance can scale policy enforcement by identifying repeatable patterns and automating compliance checks across environments.

**FinOps and Shift-Left: Cost Forecasting Before Deployment**
Traditional cost management tools focus on retrospective analysis — looking at what has already been spent. However, shift-left FinOps means integrating cost forecasting directly into the development lifecycle. Tools like InfraCost and Firefly enable teams to estimate infrastructure expenses directly from Terraform plans, preventing budget overruns before deployment:

- Developers can see the projected cost of their infrastructure before deploying.
- Cost guardrails ensure resources that exceed budget thresholds fail at deployment time.
- Teams can compare architectural options — e.g., using multiple availability zones (multi-AZ) vs. single-AZ — before committing to provisioning.
- Architects can generate cost estimates for new services before infrastructure is even provisioned, avoiding surprises.
- Product teams can design and optimize features with cost efficiency in mind, leveraging
[Terraform Plan](https://developer.hashicorp.com/terraform/tutorials/cli/plan)insights to make informed decisions on infrastructure trade-offs. - Automated workflows can block deployments that exceed preset cost limits and provide alternative lower-cost recommendations.
![Terraform Plan UI shows "plan completed"](https://cdn.thenewstack.io/media/2025/03/4582e719-terraform-plan.png)
Source: Firefly.

By leveraging Terraform Plan, cost estimation tools analyze the infrastructure configuration before deployment and provide a financial projection based on the resources defined in the plan.

When a developer runs a Terraform Plan, FinOps platforms can extract key parameters, such as instance types, storage sizes and networking costs, then map them to real-time cloud pricing data. This allows teams to assess the financial impact of their infrastructure choices before provisioning, ensuring budget constraints are met and preventing unexpected expenses.

**Tagging: The Backbone of FinOps Governance**
Tagging plays a critical role in modern FinOps by providing a structured way to track, allocate and optimize cloud costs. Most FinOps platforms depend on well-defined tags to associate cloud spending with specific teams, environments and services.

By enforcing tagging policies through GaC and PaC, organizations can ensure that every deployed resource includes metadata for accurate cost attribution. This allows for real-time budgeting, forecasting and waste reduction by identifying underutilized resources or untagged deployments. Without proper tagging enforcement, cloud cost management becomes significantly more challenging, making it difficult to allocate expenses, apply budget controls or generate meaningful financial insights:

- Tagging coverage and enforcement in CI/CD ensure all resources are properly labeled.
[Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention)cost allocation tags and Cost Explorer require structured tagging for meaningful cost tracking.- Key tags such as
`env_owner`
,`environment`
,`service`
and`version`
enable teams to correlate resources with services, tenants and owners. - Multitenant Software as a Service (SaaS) environments require strong tagging policies to properly allocate costs across customers, whereas single-tenant setups make cost tracking more straightforward.
Without robust tagging, understanding cloud costs — especially in multitenant SaaS environments — becomes significantly more complex. Enforcing tagging through CI/CD ensures that no resources are provisioned without the necessary metadata, preventing costly gaps in cost tracking.

**Enforcing Cost and Compliance Guardrails**
Cost enforcement and compliance go hand in hand. The same policy frameworks that prevent security misconfigurations, such as publicly accessible Relational Database Service (RDS) instances, can also enforce cost controls.

By integrating cost guardrails at the infrastructure level, you can gain the following:

- Developers are notified when their deployments exceed budget thresholds.
- Security and cost policies can be enforced together (e.g., EKS clusters requiring private nodes while also adhering to budget limits).
- Built-in templates aligned with SOC 2, ISO 27001 and HIPAA help ensure compliance while allowing for flexible, dynamic policies based on organizational needs.
- Developers receive clear feedback on deployment failures — whether due to budget constraints or security risks — so they can remediate issues before deployment.
Production environments have different requirements and cost considerations than development environments. Unlike production, development environments don’t always need the same level of availability, performance or compliance guarantees. These differences have significant cost implications; while production might require multi-AZ deployments and larger compute resources, development environments can often use lower-cost configurations. By being cost-aware before provisioning, organizations can empower developers with greater autonomy while keeping cloud expenses within allocated budgets.

**Platform Engineering and FinOps**
[Internal developer platforms (IDPs)](https://thenewstack.io/internal-developer-platforms-are-for-devops-too/) like Backstage play a critical role in providing real-time cost transparency by integrating FinOps data directly into developer workflows. By exposing cloud waste insights through APIs, teams can visualize cost allocation, identify underutilized resources and automate remediation within their platform engineering ecosystem.
This integration gives developers full visibility into infrastructure costs without needing to leave their existing workflows, helping to drive accountability and better cost decisions. With FinOps principles embedded into IDPs, teams can proactively manage budgets, optimize resource allocation and reduce cloud waste through automated governance policies.

**A Word on Cloud Waste and Actionable Remediation**
Legacy cost analysis tools tell you what you’re spending but rarely offer actionable cleanup recommendations. True FinOps governance requires actionable policies for cloud waste reduction, alongside proactive FinOps measures.

Shifting left in FinOps isn’t just about cost visibility — it’s about ensuring cost efficiency is enforced as code, and continuously on your production systems. Legacy cost analysis tools provide visibility into cloud spending but rarely offer actionable cleanup recommendations. This includes actionable insights for cloud waste reduction, ensuring that predefined cost-saving policies highlight underutilized or orphaned resources while automated cleanup workflows help reclaim unused infrastructure.

![UI shows insights for cloud waste reduction](https://cdn.thenewstack.io/media/2025/03/b33302f9-manage-cloud-waste.png)
Source: Firefly.

Proactively managing cloud waste is possible by providing deep visibility into infrastructure sprawl, enforcing tagging policies and automating remediation. Beyond identifying orphaned or underutilized resources, actionable insights help teams make smarter infrastructure decisions. Analyzing deployment patterns or surfacing redundant workloads enables you to make data-driven decisions to minimize waste and identify optimizations — whether it’s downsizing overprovisioned instances, consolidating redundant workloads or refining autoscaling configurations. These recommendations empower engineering teams to balance performance and cost efficiency while maintaining compliance.

**Shift Left FinOps: The Key to Greater Cloud Efficiencies**
Shifting FinOps left is a natural progression in cloud management, building on GaC principles that enable automation and unified enforcement across systems. As organizations scale, shifting FinOps left becomes essential for balancing developer autonomy with financial responsibility, ensuring cost guardrails are integrated into the earliest stages of as-code provisioning and CI/CD processes.

Embedding financial guardrails into PaC and GaC ensures cost transparency at every stage of development, so teams can prevent budget overruns while maintaining agility. Firefly plays a key role in this transformation by providing the visibility and actionable insights needed to manage cloud spending.

By enabling organizations to have the visibility, automation capabilities and governance needed to scale cloud environments efficiently, engineering teams remain cost-conscious through a shift-left FinOps approach. They can accomplish this by proactively managing cloud waste, enforcing compliance guardrails and seamlessly integrating cost governance into IDPs to natively integrate with platform engineering practices, developer tools and workflows.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)