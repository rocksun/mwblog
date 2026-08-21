**Not too long ago, edge computing was seen as a niche use case**, limited to telcos, manufacturing plants, and large retail stores. This is no longer true. With the rapid adoption of AI across every industry, edge has become mainstream and continues to grow at pace. According to the [CNCF’s 2025 Annual Survey](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/), 66% of organizations are now running generative AI workloads on Kubernetes. For most organizations, regardless of industry or scale, that makes edge worth a deliberate strategy now, rather than something addressed piecemeal as it comes up.

What do we mean by “edge” in this context? [CNCF’s IoT Edge Working Group](https://www.cncf.io/blog/2023/03/09/introducing-the-edge-native-whitepaper/) defines it as a computing environment shaped by constraints that don’t apply in the data center: compute, connectivity, storage, and power are all limited. Edge, then, is less a location than an operating condition. It is an infrastructure that has to keep running reliably without the assumptions of constant power, connectivity, and elastically available compute that the rest of cloud native takes for granted.

> “Edge is less a location than an operating condition.”

Kubernetes, along with the cloud native ecosystem, provides the ideal platform to run compute for anything from a tiny microservice to an enterprise GenAI application. The lightweight, containerized model provides the portability and orchestration required by the edge. It includes the cloud-native primitives needed to orchestrate GPU nodes, host large language models (LLMs), and run scalable Generative AI pipelines. By bringing a complete suite of integrated building blocks from networking and security to continuous delivery, it equips teams with a production-ready edge platform**.** However, there is a problem.

Every enterprise has followed its own path to the edge, and most are now running a dispersed web of clusters built up over years, each with its own configuration history, resulting in highly customized, homegrown automation or manually managed “snowflake” clusters. As organizations deploy more clusters and applications at the edge, piecemeal configuration is now creating a major operational bottleneck.

When an update or security patch needs to be rolled out, each cluster requires an individual audit and remediation. Further, there is typically no local admin to enforce uniform policy or stand by to fix things when something breaks. The result is that the very technology designed to empower platform teams is now holding them back, costing time, resources, and headspace because it struggles to handle modern-day edge operations for which it was never designed.

> “The goal isn’t only to reduce operational overhead, but to give teams back the bandwidth to do the work they’re actually there to do.”

Solving that problem starts with a different way of thinking about what’s actually being managed: fleet management. It means treating a group of clusters as a single, centrally governed unit, grouped by shared properties and governed by common policies, rather than as a collection of individual systems managed one by one. The goal isn’t only to reduce operational overhead, but to give teams back the bandwidth to do the work they’re actually there to do.

## **The challenges of edge**

Kubernetes wasn’t built with the edge specifically in mind, yet two of its core design features are a large part of why it has become the default starting point for edge deployments anyway. Its declarative API lets teams describe the end state they want, rather than scripting a sequence of steps that assumes someone is present to run and adapt them.

This means that a cluster doesn’t need an engineer standing in front of it to be built, rebuilt, or recovered. Secondly, its reconciliation loops continuously check a cluster’s actual state against its declared desired state, correcting drift automatically, with no human intervention required. Together, these let an edge site keep running and, crucially, keep correcting itself, without anyone on-site.

That’s necessary, but it isn’t sufficient on its own. Self-healing at the level of a single cluster is not the same as operating reliably at the level of a fleet, and getting real value from Kubernetes at the edge still requires a careful, deliberate approach.

Edge computing, almost by definition, means many remote Kubernetes clusters spread across many physical locations. These could be a factory floor, a retail store, or a cell tower, and they are usually remote locations without a platform engineer on-site. That absence of local expertise is precisely what makes snowflake clusters problematic. When something drifts or breaks, it must be resolved manually, but there’s no one on hand to fix it.

Three recurring challenges show up across nearly every edge deployment, regardless of industry: standardizing lifecycle management across dispersed clusters, maintaining synced configuration when connectivity is unreliable, and making observability work at fleet scale. The traditional approaches that made sense in an earlier era of Kubernetes are no longer sufficient, and teams face growing complexity as a result.

### **Standardizing lifecycle management: configuration and application drift**

The foundation of fleet management is the ability to create and manage clusters consistently across different environments. For years, the default approach was to script cluster provisioning with tools like Terraform and Ansible, cluster by cluster, which worked reasonably well when organizations ran a small number of long-lived clusters and the process was manageable and worth the manual investment.

At the scale at which most organizations are now operating, this is not merely untenable, but also creates a wider margin for human error. Every scripted, hand-tuned cluster requires an individual decision, slightly different from the last one, and creates the inconsistent fleets described above.

What’s increasingly expected today is a standardized, declarative approach to cluster lifecycle management, rather than one-off scripting. Cluster API (CAPI), a Kubernetes sub-project that provides a declarative API for cluster lifecycle management across any infrastructure, has become the closest thing the industry has to a standard for lifecycle management.

Alongside it, immutable “golden image” practices are becoming more common, whereby every cluster version is built from a pretested image, and an upgrade produces a new image rather than patching a running cluster in place. That removes much of the operational risk that accumulates when teams modify live clusters across dozens of slightly different environments. This model doesn’t fit every environment uniformly because some bare-metal edge deployments lack the hypervisor layer that image-based replacement depends on, and in-place upgrade paths remain the more practical option in those cases.

Where applicable, the consistency this model creates also supports stronger security. When every cluster is built from the same versioned specification, a security patch can move through the same declarative pipeline as any other update, rather than requiring individual audits and remediation at every site.

A patch that might previously have taken months to roll out across a fragmented fleet can, in a well-run declarative pipeline, be automated and deployed dramatically faster. However, the exact timeline depends on fleet size, rollout policy, and how much of the estate is on a consistent baseline to begin with. For highly regulated sectors such as defense, government, and finance, a smaller window of vulnerability is a meaningful reduction in security risk.

## **Keeping applications and configurations in sync**

### **Application and configuration drift**

Consistent cluster lifecycle management solves half the problem, but applications and configurations running inside those clusters still need to be monitored once they’re live. If left unmanaged, deployed workloads drift from their intended state just as easily as the clusters themselves do.

GitOps addresses this by making Git or an OCI registry the single source of truth for what should be running on a cluster. Any GitOps-compatible tooling, whether that’s ArgoCD, FluxCD, or a GitHub Actions-based pipeline, continuously reconciles a cluster’s actual state with the state declared in the repository and automatically corrects drift rather than waiting for someone to notice a discrepancy.

### **Handling connection loss**

The unreliable connectivity of edge environments creates additional challenges for reducing drift. Standard Kubernetes update models are push-based, which assumes a reliable connection, but this doesn’t hold up at the edge. When a site goes offline, or an operation fails mid-rollout, teams relying on a push-based model are left to manually reconcile what was deployed against what wasn’t.

For cluster lifecycle management, the Cluster API relies on Kubernetes controllers and operators that include an automatic retry mechanism. This means that when connectivity fails, the controller will retry once connectivity returns, rather than requiring manual intervention. However, the specifics of that retry behavior can vary somewhat by infrastructure provider.

For applications and workloads, GitOps tools such as FluxCD extend this approach using a pull-based model with local agents deployed on each cluster. In many configurations, those agents can continue operating from a local cache when the central management cluster is unreachable, rather than stalling outright. When this is in place, the reconciliation process pauses rather than fails and resumes once the connection returns, without requiring someone to manually diagnose what happened or restart a rollout from scratch.

## **Observability and Security at fleet scale**

### **Observability at scale**

The traditional model relied on a single dashboard and alerting stack per cluster, built for a small number of long-lived environments. The sheer volume of data generated by large fleets makes a manual approach untenable and meaningfully increases the risk of warning signs slipping through the cracks. Observability needs to be a proactive, fleet-wide process that catches issues before they escalate, rather than after. This pressure is pushing the industry toward an integrated observability stack with automated, increasingly AI-assisted anomaly detection able to flag CPU throttling, storage capacity warnings, configuration drift, vulnerabilities, and performance degradation as they emerge.

### **Centralized policy and security**

Policy enforcement is a related but distinct fleet-management function. Once visibility into the fleet is centralized, controlling it can become centralized too: capabilities like CIS Benchmark hardening, FIPS 140-2 support, and policy-as-code enforcement let policy be defined once and applied consistently across the fleet, rather than configured site by site. For the most sensitive deployments across defense, government, and other regulated industries, that same centralized approach can extend to air-gapped operation, where the OS binaries, container images, and Helm charts needed to stand up and run a cluster are packaged into a self-contained, disconnected bundle. This reduces, though doesn’t eliminate, dependence on internet connectivity throughout the cluster’s operational lifecycle.

## **Building the infrastructure for fleet management**

The fleet management approach is the shift that provides the framework for overcoming the challenges outlined above. The cluster-management mindset made sense in the early years of Kubernetes, when clusters were time-consuming to build, and so organizations ran as few as possible, each managed as an individual entity, and every configuration decision mattered. The speed and ease with which clusters can be spun up and torn down have eliminated their value as an operational unit. What matters most now are the definitions, policies, and standards that govern them, and a fleet management approach enables teams to enforce these from a single management layer.

Done properly, fleet management requires four things to work together: centralized control through single-pane-of-glass observability, standardization and automation of the cluster lifecycle and workload deployment processes, centralized policy management, and integration with the tooling a team already relies on. None of these four are new ideas individually, but they must now be performed simultaneously, from a central control point, with the view to create a uniform and standardized “fleet.”

> “The edge Kubernetes problem is as much a people and process problem as it is a technical one.”

The mindset shift is often where the barrier to achieving fleet management sits. The edge Kubernetes problem is as much a people and process problem as it is a technical one. Teams have built their workflows around specific tools and patterns over the years, which creates resistance when change arrives, even if the change will benefit them. In practice, the resistance tends to soften once a team starts to feel the benefits directly, even if that is only from a handful of initial pilot clusters, teams, or tools. The mindset shift follows quickly, and adoption moves quickly and, most importantly, lasts.

Executing on that operating model well depends on one more decision: how open the underlying tooling is to begin with.

## **Why open, upstream tooling matters for fleet management**

The fleet management model above only works if the underlying tooling can keep pace with how quickly the edge itself is changing. A platform wrapped in proprietary abstractions around the Kubernetes API creates a dependency on the abstraction layer to be updated before customers can use new tools or capabilities.

Staying upstream and unwrapped avoids that lag. It means new tooling can be adopted as fast as the ecosystem produces it, rather than being gated by a vendor’s own release cycle. It also means existing CNCF tooling and automation a team has already invested in continues to work without modification, rather than needing to be replaced or reconfigured to fit a proprietary model.

This matters even more now than it did a few years ago, as AI inference at the edge accelerates the pace at which the underlying requirements shift. An open foundation can keep adapting as those requirements change, rather than one that has to be rearchitected and replaced when they do.

It is clear across each of the four pillars of standardization, connectivity, security, and observability that cluster-by-cluster management is dead. The shift toward fleet management is now underway, even if many teams still lack the confidence to break away from the tools and habits that hold them back. This is where NKP comes in.

## **How NKP puts this into practice**

The Nutanix Kubernetes Platform (NKP) is built on a fleet-management approach. It is a comprehensive, CNCF-compliant stack designed for the operational reality of managing many clusters across distributed, heterogeneous, and often constrained environments. Every layer is left open and unwrapped, so the platform can absorb new tooling as fast as the ecosystem produces it, rather than waiting on a proprietary abstraction to catch up.

That principle extends to how NKP was built in the first place. Nutanix was one of the early adopters of Cluster API before it became the industry-wide standard. It was a deliberate bet on where the Kubernetes ecosystem was heading, rather than a reaction to where it had already arrived.

**Standardization and lifecycle management:** NKP pairs CAPI with golden images, so every cluster is immediately configured to the framework a team defines. If something breaks, a new cluster can be created quickly, with GitOps pipelines and backups pointed to it, and the fleet is back up and running, including the consistent, declarative patch path that keeps security updates from becoming a per-site manual task.

**Connectivity:** NKP uses FluxCD for GitOps-driven application and configuration delivery, with local caching so that clusters keep operating from their last known state when the central management cluster is unreachable. When the connection returns, clusters automatically resume from where they left off.

**Observability and policy:** NKP provides an integrated logging, monitoring, and alerting stack out of the box, configurable with a single UI checkbox. Its Insights engine and AI Navigator continuously monitor the fleet and flag anomalies before they escalate, while CIS Benchmark hardening, FIPS 140-2 support, and policy-as-code enforcement via Gatekeeper are applied centrally across the fleet by default. For the most sensitive deployments, NKP supports fully air-gapped operation, with no dependency on internet connectivity at any point in the cluster lifecycle.

Across all of this, the aim is the same: give platform teams back the time and headspace to focus on innovation, not integration.

## **Reclaiming the Platform Engineer’s Headspace**

At its core, transitioning to a fleet management mindset across standardization, connectivity, security, and observability comes down to a single goal: giving platform teams back the time and mental bandwidth to innovate, rather than constantly fighting fires.

Reaching this modern standard requires four key steps:

* **Standardize** cluster creation using declarative frameworks like Cluster API.
* **Integrate** automated GitOps pipelines to keep edge sites reconciled through spotty connectivity.
* **Automate** security and policy enforcement by default across all remote nodes.
* **Add** **intelligence** via fleet-wide, proactive observability to flag anomalies before outages happen.

Whether an organization migrates its infrastructure all at once or takes an incremental approach through pilot projects, moving away from cluster-by-cluster management is essential for operating at modern edge scale. By grounding fleet architecture in open, upstream standards, engineering teams can build an edge foundation that adapts as fast as the cloud-native ecosystem evolves.

***To learn more about the Nutanix Kubernetes Platform, visit*** [***Nutanix***](https://www.nutanix.com/solutions/cloud-native)***.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/08/3484e483-cropped-ba6bf87b-arvind-bhoj_headshot-600x600.jpeg)

Bio: Arvind is a Cloud Native Staff Solutions Architect at Nutanix with over 23 years of experience in the IT industry. A specialist in Kubernetes and the CNCF ecosystem, Arvind has spent over two decades evolving alongside the infrastructure landscape,...

Read more from Arvind Bhoj](https://thenewstack.io/author/arvind-bhoj/)

[![](https://cdn.thenewstack.io/media/2025/11/e00a72d5-aarthi-mahesh.jpg)

Aarthi drives product and solutions marketing at Nutanix, specializing in the Nutanix Kubernetes Platform (NKP) and its full-stack cloud native solution. With a background in computer science and customer success engineering, she brings deep expertise in enterprise technology and Kubernetes...

Read more from Aarthi Mahesh](https://thenewstack.io/author/aarthi-mahesh/)