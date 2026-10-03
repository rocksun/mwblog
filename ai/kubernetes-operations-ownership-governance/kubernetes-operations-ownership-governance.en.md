**Day 1 of a** [**Kubernetes**](https://kubernetes.io/) **deployment usually feels like a milestone to an IT department:** Clusters are provisioned, networking is routed, and initial application containers are running. But Day 2 exposes a harder reality: the cluster can be healthy while the application is not. So once Kubernetes goes live, who owns what happens next?

In an interview with *The New Stack*, [Karthik Subramanian](https://www.linkedin.com/in/karthik-subramanian-lnkd/), Principal Product Manager for [HPE Morpheus Software](https://www.hpe.com/us/en/products/software/morpheus-software.html) at [Hewlett Packard Enterprise (HPE)](https://www.hpe.com), describes how teams can divide responsibility for post-launch Kubernetes operations, including access, configuration drift, and cluster upgrades.

---

*This is the second in a four-part series. Read Part 1: [Developers and platform teams both want Kubernetes self-service. They disagree on who owns it.](https://thenewstack.io/kubernetes-self-service-platform-teams/)*

---

## **Dividing platform and application team responsibilities**

At the core of post-launch governance is a clear division between the teams building the platform and those consuming it. Subramanian says that responsibilities often break down between two groups that work closely together:

* **Platform teams:** Cloud architects, Kubernetes platform admins, security teams, and monitoring specialists. They oversee the overall Kubernetes environment, provision clusters, allocate namespaces, manage versioning policies, manage storage and Container Network Interface (CNI) plugins, enforce security policies, and manage infrastructure drift.
* **Application teams:** Comprised of core application developers, QA personnel, and production deployment engineers who act as tenant consumers. They deploy workloads within designated namespaces, manage application code releases, and use cluster capabilities without managing the underlying control plane.

Subramanian says these are functional responsibilities, even when one person handles several. As teams grow, assigning an owner for each function can clarify handoffs and access decisions.

## **Cloud-level and cluster-level standards**

Subramanian describes two levels at which a platform team can set standards: policies shared across a cloud environment and settings defined for an individual Kubernetes cluster.

**Cloud-level definitions**: A team can establish access and role-based access control (RBAC) policies, network and admission requirements, backup and recovery objectives, infrastructure-as-code standards such as [Terraform](https://www.hashicorp.com/en/solutions/accelerate-innovation), and service-level indicators for the environment.

**Cluster-level standardizations**: Individual clusters enforce localized settings tailored to specific environment constraints, such as Kubernetes version support cadences (e.g., maintaining support for two or three active minor versions); naming conventions, resource labeling, and multi-tenancy namespace models; and cluster-specific network policies for pod-to-pod communications.

## **Automating governance and upgrades with HPE Morpheus Software**

[HPE Morpheus Software—enterprise](https://www.hpe.com/us/en/products/software/morpheus-software.html) gives platform teams a way to connect cloud resources, Kubernetes provisioning, blueprints, workflows, and role-based access controls. Teams can configure catalog access, quotas, budgets, and approval policies, including integrations with IT service management systems. The platform team still decides which requests need approval and who can make changes.

For Kubernetes clusters managed through HPE Morpheus Software, supported versions can be delivered through cluster layouts that specify the software and dependencies used to provision a cluster. Subramanian says customers can review available upgrades through the HPE Morpheus Software interface or API, subject to the Kubernetes service, version, and support matrix for their environment.

### **Planning rolling upgrades to limit disruption**

Subramanian describes a staged upgrade process intended to limit application disruption. The steps he identified include:

* **Pre-validation checks:** Before initiating updates, the platform team reviews node health and compatibility warnings exposed by the supported Kubernetes environment, then remediates issues before applying changes.
* **Sequential control-plane and worker-node updates:** Subramanian says supported Kubernetes environments can update these components in stages rather than updating all nodes at once. The platform team monitors cluster health, while application teams validate workload availability and critical application paths throughout the process.
* **Canary and blue-green approaches:** For a production change, teams can run an existing cluster alongside one using a newer Kubernetes version, then use their application delivery and load-balancing tooling to send a small share of traffic to the new cluster. Subramanian gave 1% to 5% as an example, with traffic increased only after the application meets its agreed checks.

An upgrade is not complete when the nodes return to Ready. It is complete when the application’s critical path works, service objectives remain within tolerance, and the teams know what would trigger a pause or rollback.

## **Task-by-task responsibility matrix**

To eliminate ambiguity across operational lifecycle events, teams should map specific tasks to accountable owners and required approval gates:

| **Lifecycle domain** | **Specific task** | **Accountable team** | **Handoff or approval gate** |
| --- | --- | --- | --- |
| Architecture and sizing | Cluster topology, auto-scaling bounds | Cloud architect/platform admin | Approved based on workload requirements & quotas |
| Cluster and namespace provisioning | Namespace creation, version policy definition | Kubernetes platform admin | Platform team defines catalog access and any required approval |
| Workload provisioning and management | Application deployment, configuration, scaling, and lifecycle management | DevOps team | Platform team provides approved namespaces, policies, and cluster services |
| Security and secrets | User RBAC, secret and certificate rotation, mutual TLS (mTLS), optional Istio | Security and governance team | Security team defines rotation procedures and reviews policy changes |
| Upgrades and drift | Pre-validation, rolling updates, drift checks | Platform operations team | Platform team schedules the change and reviews pre-upgrade warnings |
| Monitoring and recovery | Capacity tracking, cluster health, state backups | Monitoring / SRE team | Monitoring team tracks alerts; recovery owners test restores against recovery objectives |

## **Testing resilience and measuring operational success**

Subramanian says teams should test their ownership models in lab environments before an incident. Those tests can include:

* **Upgrade failure testing:** In a lab, test failed upgrade scenarios, identify their causes, and confirm the team’s recovery procedure before changing production clusters.
* **Hardware and worker node failures:** Simulating node outages to confirm pod rescheduling and application continuity during node replacements.
* **RBAC boundary verification:** Validating tenant isolation to ensure that unauthorized users cannot access isolated namespaces.
* **Backup and restore verification:** Testing state backup restorations to confirm data integrity and recovery time objectives (RTOs).

To determine whether post-launch operations are succeeding, Subramanian recommended tracking specific operational metrics, such as:

* **Upgrade success rate:** The percentage of cluster upgrades completed without manual intervention or rollback and with minimal impact to running workloads.
* **MTTI and MTTR:** Mean time to identify (MTTI) and mean time to resolve (MTTR) operational incidents.
* **Backup and recovery rates:** The percentage of scheduled backups successfully created and validated for restore readiness.
* **Audit review:** Check whether records identify who or what performed a consequential action, what changed, and whether the required approval occurred.

Clear owners, tested recovery procedures, and carefully configured automation give teams a better basis for operating Kubernetes after launch. The practical test is whether they can identify who approves a change, who responds when it fails, and what evidence shows the application is still working.

---

***See how [HPE Morpheus Software](https://www.hpe.com/us/en/products/software/morpheus-software.html) helps platform teams deliver governed Kubernetes self-service without creating another operational silo. Meet HPE at KubeCon + CloudNativeCon North America 2026 in Salt Lake City, November 9–12.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)