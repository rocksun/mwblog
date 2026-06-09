Securing Kubernetes has always been complex — spanning access control, image vulnerabilities, secrets management, and networking. AI workloads make it harder. They expand the attack surface with new behaviors, new traffic patterns, and new risks.

Two years ago, your cluster ran microservices. Now it runs agents. So, instead of persistent apps with predictable CPU usage, you have dynamic, ephemeral processes on GPU nodes generating bursty, unpredictable traffic that frequently needs egress — and Kubernetes NetworkPolicy doesn’t have the granularity or visibility to handle it.

> Two years ago, your cluster ran microservices. Now it runs agents.

Agents copy or generate untrusted code, discover and invoke tools you haven’t assessed, let alone whitelisted from new registries, spin up sub-agents, skills and MCP clients, chain together unexpected calls to unfamiliar APIs and generally make unpredictable demands on your infrastructure and data sources.

Plus that infrastructure now includes scarce, expensive GPU resources that are almost certainly shared with other users in ways few teams are used to securing. Tackling that requires far more than traditional cluster hardening: you need an architecture that delivers security across four key control planes, starting with the network.

## Zero trust networking from bootstrap to agent hops

Even on a managed service like **[Azure Kubernetes Service](https://azure.microsoft.com/en-us/products/kubernetes-service)**, standard clusters have unrestricted outbound network access by default. Instead of leaving users to lock that down with cumbersome firewall rules, AKS is moving towards a more secure default: [Network-isolated clusters](https://learn.microsoft.com/en-us/azure/aks/concepts-network-isolated) let you bootstrap with no outbound dependencies on the public internet unless you explicitly enable them.

[Shashank Barsin](https://www.linkedin.com/in/shashank-barsin-1898643b/), who leads security experiences for AKS, explains it this way to *The New Stack*.

“Bootstrapping the cluster itself requires no egress: you can use private endpoints to pull all your images from a private Azure Container Registry,” Barsin says. “That’s us designing the platform so there’s no unexpected data exfiltration. In the AI era, you’re always concerned about what agents do and what data they could extract out.”

[Toddy Mladenov](https://www.linkedin.com/in/toddysm/), who leads the cloud-native security and registries team, tells *The New Stack* that if the cluster can’t see public registries and APIs beyond your cluster, agents running there have fewer opportunities to surprise you with unwanted behavior or connections.

“Network routes you establish on the cluster control where agents can go to get tools, get packages, or get knowledge to operate on,” Mladenov says.

For fully air-gapped environments, improvements in network acceleration make Private Link more suitable for connecting to Azure Key Vault or sending metrics and logs to Azure Monitor, keeping telemetry and secrets off the public network.

Zero trust applies to cluster operations too; AKS is adopting Gateway API along with the rest of the Kubernetes ecosystem, and [Azure Kubernetes Application Network](https://learn.microsoft.com/en-us/azure/application-network/) (currently in preview) simplifies [ambient service mesh](https://istio.io/latest/docs/ambient/) with a managed Istio service, giving platform teams a consistent way to control and monitor east‑west and north‑south traffic.

## **Policy-as-code for guardrails and governance**

You can’t try to predict every AI behavior, but you can enforce [declarative policies](https://learn.microsoft.com/en-us/azure/aks/use-azure-policy) governing agent-to-agent, agent-to-tool, and agent-to-LLM communications.

Set up guardrails with admission policies and engines like [OPA](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes) and [Kyverno](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/eks-to-aks/governance) to handle the granularity of which agent, in which transaction, using which identity, is allowed to deploy which workload, call which tool, which data sources count as sensitive, and when to involve a human.

“We’re dealing with situations where an agent calls another agent, that agent calls another agent, that agent calls a set of tools; and there’s authorization that needs to be done in the context of the transaction rather than a static, one-time authorization,” explains Barsin. “It’s becoming more important to be able to stitch through the entire transaction of what an agent does with sub-agents and tools and how they interact.”

> “New projects like transaction tokens and AAuth emerging in the zero-trust space cover the whole lifecycle, not just the cluster but the workloads on top and their communication as well.”

The Istio community is exploring using the project as the control plane for [AgentGateway](https://github.com/agentgateway/agentgateway) to provide a routing layer for connections that need to stay open while agents generate irregular, bursty traffic with multiple requests, thereby maintaining state. AKS will align with that as it matures; meanwhile, the team is experimenting with agent identity approaches that make the entire path — from end user through agents and tools — visible to that control plane, so policies can act on the whole context.

“New projects like [transaction tokens](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/) and [AAuth](https://datatracker.ietf.org/doc/draft-rosenberg-oauth-aauth/) emerging in the zero-trust space cover the whole lifecycle, not just the cluster but the workloads on top and their communication as well.” On his own time, Barsin is collaborating on [kontxt, an open-source implementation of the IETF Agentic Authorization proposals for OAuth and Transaction Tokens,](https://github.com/aramase/kontxt) to provide a zero-trust environment for agent-to-agent communication with declarative authorization policies that cover the entire identity chain.

These approaches hold out the promise of higher-level controls, such as requiring a certain level of policy compliance from agents and tools participating in transactions tagged as handling regulated data.

## Image scanning and provenance validation

Policies should cover which registries agents can pull images, libraries, and tools from, how new tools are approved for use, and which APIs and data sources are considered sensitive, confidential, or suitable for any agent to use. “If you don’t restrict the perimeter, agents can decide to go pull a tool from any registry they find convenient,” Mladenov warns. “That’s the point of agents: they’re looking for the way to solve problems. Without any restrictions, they’ll go find the solution anywhere on the internet.”

> “That’s the point of agents: they’re looking for the way to solve problems. Without any restrictions, they’ll go find the solution anywhere on the internet.”

To get the flexibility of agents with less risk from what they run, you can restrict them to using a single approved, curated registry within the VNet. That limits the tools they have access to and allows you to apply appropriate security policies, such as [continuously scanning](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-containers-introduction?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json) for vulnerabilities, missing patches, outdated dependencies, malware, and exposed secrets. That way, any images pulled from public registries can be quarantined, scanned, [signed](https://learn.microsoft.com/en-us/azure/container-registry/overview-sign-verify-artifacts), verified, and (if necessary) [updated](https://opensource.microsoft.com/blog/2024/09/18/project-copacetic-quick-and-efficient-container-image-patching/) before reaching production. To simplify that, Azure Container Registry supports RBAC, and you can now [lock its artifact cache to using another ACR registry](https://techcommunity.microsoft.com/blog/AzureCompute/use-azure-container-registry-as-an-upstream-source-for-artifact-cache/4517102).

Lifecycle metadata helps you tackle image lineage: machine-readable provenance and vulnerability reports enable automated patching and updating, as well as auditing or even blocking unsuitable images at the admission controller.

Sandboxes offer an additional layer of protection. Cloud Hypervisor improves [Kata containers](https://katacontainers.io/) performance, but if you’re spinning up a sandbox to run a Python script, that doesn’t scale to thousands of agents. The [Hyperlight](https://opensource.microsoft.com/blog/2024/11/07/introducing-hyperlight-virtual-machine-based-security-for-functions-at-scale/) runtime executes single-purpose applications in hardware-isolated VMs and has such minimal memory footprint and startup latency (just 1-2 milliseconds) that there’s no reason not to make a sandbox environment mandatory, especially for agents. That’s where you most want the protection of a sandbox, so you can treat all the code an agent wants to run as untrusted by default.

## **Runtime anomaly detection tuned for agentic behavior**

Even with these layers of policy and guardrails, agents will behave in unexpected ways: after all, if you knew how everything should get done, you wouldn’t need agents in the first place.

AKS integrates with Microsoft Defender for Containers for run-time protection using eBPF and other low‑level probes, [raising alerts](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-containers?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json) to flag [binary drift](https://learn.microsoft.com/en-us/azure/defender-for-cloud/binary-drift-detection?toc=%2Fazure%2Faks%2Ftoc.json&bc=%2Fazure%2Faks%2Fbreadcrumb%2Ftoc.json&tabs=edit-rule) — increasingly common as agents try to run code not in the original container — and suspicious network access or process behavior.

Monitoring network and file system covers known traffic patterns and application behavior for long-lived workloads, but ephemeral agent workloads spin up pods dynamically. Anomaly detection will need to work at a higher level when it’s not misbehaving pods but agents repeatedly creating short‑lived pods that immediately attempt sandbox escapes or brute‑force databases. Shutting that down doesn’t help if another pod shows the same behavior; the agent needs to be contained.

## **Protection in production**

Today most customers worry more about GPU capacity than security, Mladenov suggests. But balancing isolation and utilization as you make the most of these scarce and expensive resources is complex.

> “I have one cluster that hosts multi-tenant applications: some are agentic, Some are not, but they all follow very good security practices because the platform enforces them.”

If you don’t know [how to securely partition a GPU](https://docs.nvidia.com/datacenter/cloud-native/kubernetes/latest/index.html) into multiple instances, the direct connections between GPU nodes that enable high-speed data transfer and the efficient communication models they require can degrade performance for other workloads or even lead to data leakage. The [confidential GPUs](https://github.com/Azure/az-cgpu-onboarding/blob/main/docs/Confidential-GPU-H100-AKS-Onboarding.md) that let you use your most sensitive data for AI are still a [preview feature](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-confidential-containers.html) for Kata and also require you to handle key management.

To move successfully from proof of concept to production, you’re going to need to deal with observability, high-performance sandboxes, [secure GPU multi-tenancy](https://learn.microsoft.com/en-us/azure/aks/gpu-multi-instance?tabs=azure-cli), and securing how agents communicate – or pick a platform like AKS that handles it for you.

“A new stack is needed for inferencing and for agents, which brings with it new security challenges and the need for new security controls,” agrees Barsin.

The work being done in AKS to address agent security will also pay dividends for more traditional workloads, Mladenov maintains. “I have one cluster that hosts multi-tenant applications: Some are agentic, some are not, but they all follow very good security practices because the platform enforces them.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/e2700739-maryb.jpg)

After completing an MSc in Intelligent Knowledge Based Systems in 1990, Mary Branscombe was convinced that promising as the AI techniques she’d been studying were, they weren’t even close to being ready. Since then, she’s been a technology journalist for...

Read more from Mary Branscombe](https://thenewstack.io/author/marybranscombe/)