**The migration to Kubernetes and cloud native infrastructure** has been one of the defining IT trends of the past decade. Adopting Kubernetes gives platform teams an immediate leap forward in agility and capability, but it also creates a dangerous security illusion. The declarative approach to infrastructure, sophistication, and dynamic flexibility make it seem like Kubernetes should also have built-in security, so that everything deployed will be magically secure.

Kubernetes is not a magic solution. It is more operationally complex than a VM environment, introducing a multifaceted environment with multiple layers that each require attention and additional work to secure properly, not less. Cloud-native security therefore requires a robust infrastructure that spans every container and every node, and underestimating the complexity is costing enterprises in real time.

The approach to access control precisely captures how this illusion creates risk. Amazon EKS has deprecated the legacy aws-auth ConfigMap for mapping IAM identities to cluster permissions, a manually edited and hard-to-audit method, in favor of a newer, API-driven alternative.

> “According to a 2025 Kubernetes Security Report, 81% of EKS clusters are still running on the older method, contrary to AWS’s own security guidance.”

According to a [2025 Kubernetes Security Report](https://www.wiz.io/reports/kubernetes-security-report-2025), 81% of EKS clusters are still running on the older method, contrary to AWS’s own security guidance. The consequences of such oversights show up downstream, and roughly two-thirds of organizations have delayed or slowed deployments due to Kubernetes-related security concerns.

The security gap between assumption and reality isn’t isolated to access control. It runs through nearly every layer of Kubernetes security, and it starts with a framework that predates most of the tools teams rely on today.

## **Why VM security protocols break down in Kubernetes**

The Kubernetes security community converged early on a framework for approaching the attack surface in cloud native environments: the “four Cs” – Code, Container, Cluster, and Cloud. Each layer is distinct and carries its own threat vectors, yet they are all tightly interconnected, and a weakness at any one layer can cascade across the others. A vulnerable container image (Container) can compromise workloads across a cluster (Cluster), while a misconfigured cloud IAM role (Cloud) can give an attacker access to the Kubernetes API.

The security model of Kubernetes is structurally different from that of traditional infrastructure, and the four Cs framework is designed to give engineering teams a means of reasoning across each dimension of the cloud-native model. In a VM environment, each VM has a known IP address, runs a single application, and uses a simple communication network. The model’s predictability makes security policies much simpler to create and enforce.

In contrast, everything is dynamic in a Kubernetes environment. Pods continuously start and stop, workloads move across nodes, and clusters themselves can scale up or down depending on demand. This dynamism is what makes Kubernetes powerful for running modern applications at scale. At the same time, it makes VM-era security practices structurally insufficient because they are not built to handle a constantly shifting set of running processes.

Mapping the four Cs to where teams actually struggle reveals a consistent pattern.

Code and Cloud security is well understood and reasonably well practiced. Teams carried this discipline over from traditional development workflows, and most organizations have existing governance processes at the infrastructure layer. The gaps are almost always at the Container and Cluster layers, which operate under very different rules than teams are used to with Code and Cloud.

At the Container layer, the challenge lies in the multifaceted image supply chain. Container images are the unit of deployment in Kubernetes. They carry all the dependencies and configurations of the applications they run, and they need to be repeatedly verified and monitored for any drift or misconfiguration, from the first stage of code sourcing through runtime.

At the Cluster layer, the challenge is configuration and lifecycle. Kubernetes provides significant flexibility in how clusters are configured, and that flexibility creates a large surface area for misconfiguration. The flexibility also adds a networking dimension that catches teams out.

In a traditional environment, the primary concern is North-South traffic in and out of the system, and teams are well-practiced at encapsulating and securing it. In Kubernetes, the East-West traffic between applications running within the cluster requires equal attention. By default, pods can communicate freely with any other pod in the cluster. Without explicit network policies restricting that traffic, a compromise in one workload has a clear path to every other workload sharing the cluster.

At Nutanix, we believe that security shouldn’t slow down development teams. Designing and implementing a secure cloud-native infrastructure platform in which security policies are enforced by default not only protects the enterprise from attacks but also makes developers more productive by reducing the time previously spent chasing down breaches and manually patching.

## **The challenges of cloud-native security**

Across the organizations we work with, five challenges come up most consistently.

### Inconsistent security policies across clusters

The most common root cause of policy inconsistency is the same building-as-you-go adoption pattern that creates operational complexity more broadly. Clusters are provisioned one at a time, and security policies are applied manually, without a central enforcement layer. The inconsistency and lack of oversight create small gaps that quickly add up when operating at scale.

Even a single cluster takes considerable effort to secure properly, including defining and enforcing RBAC roles, network policies, and admission rules, all of which take real expertise and time. Multiply that across a fleet, and there is not only greater manual effort required to implement security measures, but even a minor oversight in one cluster can become a systemic vulnerability once it’s replicated across dozens of clusters.

A common example is a developer pulling code from an open-source repository and deploying it without verifying the source. In a traditional environment, the security risk may be minimal, but across a fleet of clusters, it becomes a systemic vulnerability. The correct practice is to enforce that all images come from a trusted internal registry, which only works if the right mechanisms are consistently in place across every cluster, and automatically.

### Manual credential management and static secrets

One of the most persistent misconceptions in Kubernetes environments is that a Kubernetes Secret is secure by default. While it is base64-encoded, it is not encrypted and is therefore visible to anyone with the appropriate cluster access. Nutanix always advocates for encryption at rest for secrets as the default.

Similarly, reliance on long-lived service account tokens without regular rotation further increases credential security risk. A more sophisticated security policy is to use an external vault or secret store, combined with regular token rotation. In isolation, both are relatively simple to achieve, but for a distributed fleet, they become significant challenges for teams without a central platform to automate and monitor the entire lifecycle.

This is where the Nutanix Kubernetes Platform (NKP) solution helps. It simplifies fleet-wide credential management with a centralized management plane that automates the lifecycle of clusters, security policies, and RBAC across hybrid on-premises, public cloud, edge, and air-gapped environments alike. With the pre-integrated External Secrets Operator (ESO), platform teams can connect external vaults and secret stores directly to containerized workloads, eliminating the manual work of rotating tokens cluster by cluster.

### Multi-tenancy in Kubernetes

VM models provide multi-tenancy natively. When teams move to Kubernetes, they expect it to do the same. While Kubernetes can provide soft multi-tenancy through namespace-based isolation, it does not create genuine hard multi-tenancy. Further, namespace-based isolation still relies on a basic trust assumption among tenants sharing the same cluster, meaning that cluster-scoped resources may be visible across namespace boundaries if incorrect RBAC permissions are applied.

For genuine hard multi-tenancy, where tenant A has no visibility into tenant B’s environment whatsoever, teams need dedicated clusters per tenant, with fleet management automation handling consistent deployment and governance for each. Kubernetes’ soft isolation model is appropriate in some contexts, but it still carries a risk of “noisy-neighbor” scenarios, where a compromise or misconfiguration in one tenant’s namespace can affect others. With both soft multi-tenancy built into Kubernetes via concepts like Kubernetes Namespaces and hard multi-tenancy with Nutanix AHV, Nutanix offers the tools to meet nearly any company’s multi-tenancy needs.

### Secure image delivery

In Kubernetes, container images serve as the primary unit of deployment, and they pose a significant supply chain risk. [Sysdig’s 2025 Cloud-Native Security and Usage Report](https://www.sysdig.com/2025-cloud-native-security-and-usage-report) captures this gap in the data, showing that while enterprises have made real progress reducing critical and high vulnerabilities at runtime, package maintenance has slipped over the past year, and image bloat has roughly quintupled. The report attributes this pattern in part to the rush to build with AI because AI and ML packages are much larger than the traditional workloads Kubernetes was built to handle. Awareness of image security is rising, but the pipeline hygiene needed to back it up isn’t yet keeping pace.

The most robust image security posture is multifaceted and requires scanning and verification at multiple touchpoints, not just during sourcing. When code is sourced, it must be scanned before the image is built. The base image must then be verified as secure, and the resulting image signed and stored in a registry that enforces provenance. At deployment time, an admission controller should validate that every image comes from a trusted source. The final step, and one that is frequently overlooked, is to continue scanning at runtime to catch any unexpected process executions or anomalies. Most teams cover some of these steps, but few cover all of them, which is where the exposure risk creeps in.

### Compliance at scale

Some industries, such as government, defense, healthcare, and financial services, demand hard compliance requirements that the standard Kubernetes distribution does not accommodate. For example, FIPS 140-3 validated cryptography, CIS Kubernetes Benchmark hardening, and STIG-compliant OS images all require deliberate configuration and therefore pose an additional setup challenge to teams in these sectors. Further, the configurations need to be demonstrable across every cluster in the fleet, not just the most recently deployed ones. Meeting that standard manually, and at scale, is effectively impossible.

The majority of organizations reporting compliance audit failures are almost certainly operating in an environment where the compliance state was not consistently maintained and therefore could not be consistently evidenced.

> “Across these five common challenges, there is a recurring thread: they stem from a cluster-management approach and can all be resolved with a fleet-level approach.”

Across these five common challenges, there is a recurring thread: they stem from a cluster-management approach and can all be resolved with a fleet-level approach.

## **Fleet management as a security posture**

Nutanix’s core thesis is that Kubernetes demands a fleet management mindset. This is both an operational strategy and a security strategy. When security policies are defined at the fleet level and automatically enforced at deployment time, the security posture becomes more robust and easier to scale as the fleet grows.

At KubeCon + CloudNativeCon North America 2025 in Atlanta, the conversation around Kubernetes operational maturity consistently returned to the same theme: adoption is no longer the challenge. The [2025 CNCF survey](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/) reinforced this directly, finding that GitOps adoption, which is considered the practice most closely associated with fleet-level policy governance, is now the clearest single indicator of cloud native maturity. Among organizations categorized as “Innovators” in the survey, 58% use GitOps; among those still in the early stages, the figure is close to zero.

The shift-left security principle is closely aligned with our thesis. In a secure organization, platform engineers are responsible for providing Kubernetes infrastructure to application developers and ensuring that the environments in which those developers work are consistently secure and compliant. By defining and automating policy at the fleet level, enterprises can operate on a unified platform where both the dev environment and production share the same guardrails.

NKP is designed with fleet capabilities, not merely because this provides the best security policy, but also because it smooths the transition between build, deploy, and production. For cloud security, the fleet management approach provides a consistent policy layer with automated lifecycle management and enforcement.

## **Standardizing platform security across the fleet**

NKP’s security model is based on the principle that security should be a base framework, and not a bolt-on. NKP is structured to provide a full-stack security foundation from which teams can build up their unique security posture.

### The foundation: hardened by default

When you deploy a Kubernetes cluster with NKP, CIS Benchmark hardening is applied at both the OS and Kubernetes layers before the platform team has configured anything. This is the industry gold standard for Kubernetes configuration security, and NKP employs it to help enterprises meet this standard.

For the teams that require stricter compliance, NKP now also provides FIPS-validated and STIG-compatible OS images directly from the Nutanix portal. Developers can download an image, deploy it, and the cluster runs with FIPS-validated cryptographic modules from the ground up.

One practical and powerful benefit of this approach is the “proof layer.” NKP can produce a CIS benchmark report for every cluster in the fleet on demand. So, when a security team asks a platform team to demonstrate that their clusters meet a given compliance standard, the team has the evidence to hand, and the conversation shifts from “gate-and-audit” to collaboration.

Additionally, every NKP release is pre-scanned before distribution to continuously upgrade the stack to the newest available versions. Each upgrade deploys across the entire stack, with any manual intervention required from the platform team. Nutanix is alleviating the burden on engineers of keeping their environments current, enabling them to focus on their work.

### Policy as code: Gatekeeper and admission control

Manual policy enforcement is highly error-prone, especially over time and at scale. NKP includes Gatekeeper, the Kubernetes-native implementation of Open Policy Agent, as a built-in admission controller. Every policy is enforced at deployment, and a workload that violates a policy is rejected before it ever gets deployed.

For example, if a developer attempts to deploy a container image from an untrusted registry or tries to run a container with root privileges, Gatekeeper stops it at the gate. NKP also allows teams to configure it to either warn or block, depending on how they want to model enforcement in a given context.

> “An AI agent that can autonomously invoke external tools, query data sources, or take action without a human in the loop needs a clearly defined perimeter around what it’s allowed to touch and where its access ends.”

AI and agentic AI workloads further raise the stakes here. An AI agent that can autonomously invoke external tools, query data sources, or take action without a human in the loop needs a clearly defined perimeter around what it’s allowed to touch and where its access ends. The boundary needs to be enforced at the platform level, not left for individual application teams to interpret independently.

Gatekeeper’s admission controls are a strong starting point for that boundary because they can constrain what an agent-driven workload is permitted to request or deploy before it ever reaches production. However, Gatekeeper alone likely won’t be the full answer for agentic AI, especially as AI tools and usage are evolving as quickly as they are now. These workloads behave differently from traditional applications, and the guardrails the industry needs to contain them are still being defined in real time, alongside the technology itself.

In this instance, a flexible security base that allows for continued adaptation with every new development the industry produces is needed. As new guardrails for agentic workloads emerge, teams should be able to add or adjust controls as requirements shift, rather than being locked into a single model that supports security deployed around innovation rather than hindering it.

### Centralized authentication and RBAC via Dex

The difference between a purpose-built platform and a manually assembled stack becomes most visible in credential management. A lack of standardization and central management results in RBAC configurations gradually drifting apart, and no simple way to audit and maintain them

NKP is designed to allow teams to dictate authentication and configuration permissions at the fleet level, helping verify that the right people and systems have access to the right namespaces within the right cluster across the fleet, with the ability to customize individual clusters if necessary. Via Dex, NKP integrates with enterprise identity providers such as OIDC, LDAP, and SAML, giving customers choice of tools and preferred software.

### Service mesh and network security: Istio and mTLS

Network policies are the standard tool for controlling which pods can communicate with which other pods. They provide some basic guardrails, but they do not encrypt traffic between pods or cryptographically verify the identity of the communicating parties. Istio can fill this gap by inspecting application-layer headers and enforcing mutual TLS so that both sides of the connection authenticate each other cryptographically, transparently to the application.

Istio operates at Layer 7 and encrypts traffic flows between pods without changing the applications themselves. It is, in effect, an additional security layer that provides more application context than a network policy alone can. NKP ships with a default Istio configuration and deploys necessary upgrades consistently across all clusters without any input from the team, thereby reducing some of the operational complexity of running a service mesh.

### Observability, scanning, and continuous compliance: NKP Insights

It’s all very well to put security in place at the start, but teams need to be able to uphold that level. NKP Insights provides CIS benchmark scanning across the entire fleet, runtime container image scanning, and anomaly detection that flags unusual patterns. If a pod crashes frequently, resources approach capacity limits, or a configuration drifts from the expected baseline, Insights flags the issues for quick identification and remediation.

NKP Insights can operate simultaneously as a continuous security monitoring layer and a compliance reporting tool, making it useful for both day-to-day operations and the periodic compliance demonstrations required by regulated industries. Our design objective is to cover every direction, layer, and complexity of Kubernetes to help our customers succeed.

## **Looking Forward: The evolving threat surface**

Security is an ever-evolving landscape, growing more complex with each new technology. AI workloads, specifically running Agentic AI in a Kubernetes environment, introduce security considerations that traditional models were not designed to handle.

AI is now being used to exploit vulnerabilities at a speed and scale that would not have been possible a few years ago, combing through codebases and open-source repositories to find weaknesses that human researchers might take months to surface. That said, it also works in the opposite direction: AI-assisted detection is finding vulnerabilities in existing environments that have been present for years.

Just as new technologies may threaten enterprises’ security, they can also be used to enhance security posture. However, a solid structural foundation must be established first. NKP is designed to provide a full-stack foundation for robust security across the OS, Kubernetes, and application layers. It serves as the evidence layer that teams need to demonstrate their security posture at any moment.

Further, NKP is built to support a consistently secure fleet at scale. The design allows every cluster, workspace, and node to be accounted for and monitored. The automated updates across the NKP stack are designed to mitigate the risk of such incidents.

Across the ecosystem, developers are being asked to innovate faster than ever, using technologies such as AI and containers to ship more frequently and move quickly. Every new technology adds another layer of security risk, especially for AI and the connected nature of modern applications and distributed deployments, which create more attack surface than ever before.

If today’s enterprises want to continue to focus on innovation, they need a system in place that provides security by default. Nutanix is providing that default, delivering a gold standard base through NKP.

***To learn more about Nutanix Kubernetes Platform, visit*** [***Nutanix***](https://www.nutanix.com/products/kubernetes-management-platform)***.***

***To try NKP hands-on,*** [***launch a free test drive***](https://cloud.nutanixtestdrive.com/login?source=one-platform&marketo_id=df2715ab833d78c49a367de63a18b7b88e4e710b50fd687f3eb9fc18302b0059&type=nkp&ptk=&partnerid=)***.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/08/1c406aeb-cropped-ae07ec01-yannick-struyf_headshot.jpg)

Yannick Struyf is a Principal Product Manager at Nutanix, where he focuses on the cloud native ecosystem. Drawing on his extensive background in infrastructure automation and open-source technologies, he is dedicated to translating complex, real-world customer challenges into elegant and...

Read more from Yannick Struyf](https://thenewstack.io/author/yannick-struyf/)

[![](https://cdn.thenewstack.io/media/2025/11/e00a72d5-aarthi-mahesh.jpg)

Aarthi drives product and solutions marketing at Nutanix, specializing in the Nutanix Kubernetes Platform (NKP) and its full-stack cloud native solution. With a background in computer science and customer success engineering, she brings deep expertise in enterprise technology and Kubernetes...

Read more from Aarthi Mahesh](https://thenewstack.io/author/aarthi-mahesh/)