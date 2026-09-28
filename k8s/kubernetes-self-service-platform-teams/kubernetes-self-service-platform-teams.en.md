**What do developers want?** Kubernetes environments when they need them.

**What do they *not* want?** Those environments after a week or more of tickets.

Platform teams, meanwhile, own what those environments cost, who can access them, and whether they meet company policy.

That tension is the core of Kubernetes self-service: What can safely be handed to developers, and what still belongs to the platform team?

In a recent interview with enterprise cloud specialists — [Marius Bogoevici](https://www.linkedin.com/in/marius-bogoevici/), Senior Principal Product Manager at Hewlett Packard Enterprise (HPE), and [Karthik Subramanian](https://www.linkedin.com/in/karthik-subramanian-lnkd/), Principal Product Manager for HPE Morpheus Software — *The New Stack* explored the core friction points of Kubernetes self-service. The conversation focused less on whether self-service is desirable than on where to draw the line.

HKS, HPE’s CNCF-certified Kubernetes distribution, is integrated with [HPE Morpheus Software](https://www.hpe.com/us/en/products/software/morpheus-software.html) to help platform teams deliver and lifecycle-manage Kubernetes environments as part of a broader operating model spanning Kubernetes, VMs, infrastructure, and clouds. [HPE Morpheus Advanced Software](https://www.hpe.com/us/en/products/software/morpheus-software/features.html) supports the on-premises private-cloud use case with HKS, while HPE Morpheus Enterprise Software extends Kubernetes and application operations across hybrid and public-cloud environments.

Together, HKS and HPE Morpheus Software extend that operating model beyond infrastructure provisioning. Through service and application catalogs, platform teams can connect approved Kubernetes environments with the CI/CD pipelines, container registries, automation tools, and other services developers already use. Developers receive a governed, ready-to-use path from code to deployment instead of manually assembling the toolchain for each project.

## **The self-service paradox**

Open-source Kubernetes provides orchestration and declarative APIs, but not a complete operating model.

Subramanian says teams building their own self-service layer usually run into two recurring problems:

1. **Tool and package sprawl:** To make upstream Kubernetes production-ready, platform teams must curate and maintain an ever-evolving ecosystem of third-party CNCF tooling for networking (CNI), storage (CSI), ingress, identity, and policy enforcement. Navigating and supporting this fragmented stack creates immense maintenance overhead for internal platform teams.
2. **Day-2 lifecycle and hybrid footprint complexity:** Spinning up a Kubernetes cluster is the easy part, but keeping it current — across development, QA, staging, and production — is where the work piles up. That is why HPE says every Kubernetes upgrade must be checked against the networking, storage, ingress, identity, and policy components around it. The problem gets harder when clusters span bare metal, private clouds, edge sites, and public clouds, because one-off scripts and environment-specific configurations can quickly create drift. That maintenance burden belongs with the platform team, not with developers trying to ship applications.

Giving developers direct access to raw Kubernetes APIs just shifts the operational work — it’s far from gone for good. In fact, developers will wind up debugging manifests and storage drivers instead of writing code.

Meanwhile, operations teams have to deal with overprovisioning, idle clusters, and configurations that reach production without review.

## **What developers control — and what the platform supplies**

The practical answer is not unrestricted access. It is a paved path: approved Kubernetes services that developers can request themselves, with access, configuration, placement, approvals, and lifecycle controls defined by the platform team.

“The best candidates for self-service are requests that are repeatable, low-risk, and well-understood,” Bogoevici tells *The New Stack*. “For example, a developer should be able to request a development cluster, deploy an approved application, create a namespace, or select resources from pre-approved configurations without opening a ticket. The platform team decides what a safe configuration looks like, and the developer chooses from a supporting menu.”

> “The platform team decides what a safe configuration looks like, and the developer chooses from a supporting menu.”

Rather than asking developers to write YAML for ingress, storage classes, and RBAC, HPE Morpheus exposes those choices through service catalogs, reusable layouts and blueprints, workflows, role-based access control, approvals, APIs, and automation. Developers do not lose Kubernetes. They retain direct access through standard Kubernetes interfaces and tools where permitted, while the platform team standardizes the request, governance, and lifecycle processes around them.

Those catalog items can package more than infrastructure settings. They can also integrate the approved services and application components that support the development workflow – including CI/CD tooling, source and artifact repositories, container registries, and runtime dependencies – while the platform team controls how those components are configured and governed.

Developers choose the parameters that matter to the application:

* **Approved Kubernetes versions and cluster sizes:** Select from pre-tested Kubernetes runtime releases and node count templates.
* **Resource quotas:** Specify required CPU, RAM, and persistent storage capacity tailored to the workload.
* **Integrated toolsets and IDE environments:** Select required developer toolchains, container registries, and runtime dependencies.
* **Lease and duration limits:** Define explicit operational lifetimes for temporary development or sandbox clusters to prevent abandoned infrastructure sprawl.

Network isolation, identity-provider integration, security policy, and cost allocation stay with the platform team and are applied automatically through the approved service configuration.

The same division of responsibility applies to the delivery toolchain: Developers choose from approved services, while the platform team manages the integrations, credentials, policies, and automation behind them. This gives developers a consistent experience without shifting toolchain maintenance and governance onto individual application teams.

The division of responsibility looks like this:

| **Service area** | **Developer chooses or requests** | **Platform team defines and supplies** | **Review or exception path** |
| --- | --- | --- | --- |
| Development cluster provisioning | Approved Kubernetes service, version, size, target environment, and duration. | Reusable layout or blueprint, access controls, placement rules, storage and network defaults, and lifecycle policy. | Nonstandard versions, placements, configurations, or requests outside quota. |
| Production deployment | Application artifacts, target namespace, and deployment request through the approved path. | RBAC, tenancy, policy, audit, backup, and release controls appropriate to the environment. | Formal review for production changes and exceptions. |
| Resource allocation and quotas | CPU, memory, storage, and other approved capacity parameters within project limits. | Project quotas, upper bounds, placement constraints, and supported resource profiles. | Requests above quota or for specialized resources. |
| Networking and security | Application endpoints and permitted connectivity within approved patterns. | Identity integration, RBAC, tenant isolation, network policy, secrets, and audit controls. | Cross-tenant access, elevated privileges, or changes to baseline security policy. |
| Lifecycle and cost governance | Service lifetime and approved operational actions. | Visibility, policy, approvals, retirement workflows, and applicable cost controls for the licensed variant. | Long-running exceptions, nonstandard lifecycle actions, or budget exceptions. |

## From ticket queues to a repeatable paved path

In conventional IT environments, provisioning a dedicated Kubernetes environment for a new project often involves cross-departmental ticket handoffs spanning infrastructure, networking, security, and storage teams. This friction frequently stretches provisioning timelines from days to weeks.

By unifying infrastructure orchestration, role-based access controls, and multi-tenancy into a single operational experience, HPE Morpheus Software can compress these provisioning workflows down to minutes or hours, according to HPE. “Developers get a usable environment that complies with the organization’s defined controls and policies, without needing to understand all the complex infrastructure steps sitting underneath,” Bogoevici says. “When you reduce provisioning time from weeks to hours, that is super meaningful and tangible.”

> “When you reduce provisioning time from weeks to hours, that is super meaningful and tangible.”

The result is not only faster cluster provisioning. HPE Morpheus Software can also automate the handoff into the developer’s established delivery process by making approved CI/CD and application services available with the environment. Instead of waiting for separate teams to connect pipelines, registries, credentials, and runtime dependencies, developers receive a ready-to-use path from development through deployment.

Faster provisioning can create a different problem, too: The speed can and will cause teams to lose track of what was provisioned and why. HPE Morpheus Software gives administrators visibility into utilization and cost, while lease controls can shut down temporary development clusters when their time expires.

Bogoevici says ticket volume is a poor measure of success, particularly early on, when more developers may be trying the catalog. He recommends watching deployment success, exception rates, resource utilization, and the day-to-day effort required to keep the service running.

## Security belongs in the service design

Security is another boundary that must be designed into the self-service path. If identity, access, tenancy, and policy are added only after a cluster is created, every request produces more work and more room for inconsistency.

“Security must be a core design consideration built directly into the service, not an afterthought during deployment,” Bogoevici says. “HPE Morpheus Software brings identity integration, role-based access, tenant isolation, approvals, and policy into the operational workflow.”

A newly provisioned environment should arrive through an approved configuration with the applicable identity, RBAC, tenant, policy, and audit controls attached. Platform teams can validate the paved path by testing an allowed request, a request that should be rejected, and the resulting audit record.

## The operating-model test

The strongest Kubernetes self-service model does not hide Kubernetes or make it the control plane for every workload. It gives developers useful, approved choices and direct access to the Kubernetes workflows they need, while the platform team standardizes the enterprise processes around those workflows.

That matters because the enterprise still runs VMs, clouds, and existing infrastructure alongside Kubernetes. HPE Morpheus Software helps platform teams use common request, governance, automation, and lifecycle processes across these environments without forcing every workload onto one runtime or creating another operational silo.

In practice, that means self-service should deliver more than a Kubernetes cluster. With HPE Morpheus Software, a catalog request can bring together the approved environment, application services, and DevOps toolchain integrations developers need, while preserving the governance and lifecycle controls the platform team requires. Developers spend less time assembling and troubleshooting delivery infrastructure – and more time building and releasing applications.

Looking toward 2027, the goal is not unrestricted control. It is faster access, predictable results, transparent guardrails, and a clear exception path when the standard service does not fit.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)