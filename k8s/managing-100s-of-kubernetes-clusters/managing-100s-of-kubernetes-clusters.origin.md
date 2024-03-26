# Managing 100s of Kubernetes Clusters using Cluster API
### Automating every step from cluster creation to workload-ready. Turtles all the way down.
*Written by Zain Malik and Nibir Bora, members of the engineering teams that work on core infrastructure.*
At City Storage Systems, our Core Infrastructure team navigates the complexities of managing over 100 multi-tenant Kubernetes clusters, each hosting up to tens of thousands of daily active pods. Our entire software stack runs on Kubernetes from mission critical microservices to stateful databases and observability solutions.
This blog delves into our journey of achieving complete automation in cluster provisioning, lifecycle management, and upgrades. With the new toolset, we slashed the time required to provision and prepare a workload-ready cluster from 1.5 weeks to under 1 day, all while maintaining a lean team of engineers. This transformation was catalyzed by our strategic decision to migrate to Microsoft Azure within a deadline of a few months. During the transition the number of clusters we operate more than doubled.
We present a set of Kubernetes
[custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) and [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) that models our infrastructure and associated operations. The flexibility of the Kubernetes operator pattern makes this approach extremely powerful and we are confident it can be used to manage clusters on any public cloud provider.
Figure 1: Hierarchy of all custom resources used to manage a Kubernetes cluster and node pools.
# Adopting Cluster API
We initially created clusters using Terraform and thereon managed node pools using a custom homegrown Kubernetes operator. Changes, including Kubernetes version upgrades, were handled via GitOps. However, the cognitive overhead and manual intervention required made this approach unsustainable, specially to migrate 80+ clusters from one cloud provider to another.
This led us to explore
[Cluster API](https://cluster-api.sigs.k8s.io/), which offers declarative APIs for simplifying provisioning, upgrading, and managing multiple Kubernetes clusters. Two key factors made Cluster API particularly attractive:
Extensibility: Cluster API's custom resources are extended by
[provider](https://cluster-api.sigs.k8s.io/reference/providers.html)custom resources, which can then be extended by higher level custom resources that capture organizational needs. Since our clusters are multi-tenant, this allowed us to abstract away any details about node pools from workload developers.
Operator Pattern: Any extension of Cluster API and its providers are Kubernetes Operators, aligning with our Kubernetes-centric approach to infrastructure management. Leveraging our team's experience with building operators, the learning curve was minimal.
To create a cluster using Cluster API and the Cluster API provider for Azure (CAPZ) we simply need to create objects of the following custom resources:
Cluster(from Cluster API)
AzureManagedClusterand
AzureManagedControlPlane(from CAPZ)
Similarly, to create a node pool we need to create objects of the following custom resources:
MachinePool(from Cluster API)
AzureManagedMachinePool(from CAPZ)
We were able to seamlessly integrate these processes into our existing CI pipelines, relying fully on GitOps for cluster management. We do not use the
clusterctl CLI provided by Cluster API.
However, there were three major roadblocks to adopting Cluster API immediately:
Limited support for managed Kubernetes distributions in Cluster API. Although this was part of Cluster API’s roadmap, most of the work done was focused on self-managed Kubernetes.
CAPZ’s support for Azure Kubernetes Service (AKS), the managed Kubernetes distribution, was still in an experimental phase, lacking essential features required for our use case.
No major engineering organization was using Cluster API for AKS (not that we knew of at the time).
We leaned on our partnership with Microsoft Azure to find a path forward. They suggested we collaborate on the CAPZ project in open source to achieve feature completeness. Several engineers from the Microsoft AKS team along with engineers from our Core Infrastructure team contributed to the CAPZ project prioritizing features aligned with our production use cases. This collaboration was a huge success. It enabled us to launch our first Kubernetes cluster using Cluster API and CAPZ within three months.
# Automating Workload-Ready Clusters
While Cluster API and CAPZ simplified cluster creation, these clusters weren’t ready for workloads yet.
The new cluster does not have permission to access container images from Azure Container Registry (ACR). It is a reasonable design choice to leave such dependencies out of Cluster API to keep the interface generic.
An AKS cluster comes configured with a default cluster autoscaler profile. Configuring anything other than default can be done by manually running a Azure CLI command. We tune Cluster Autoscaler to achieve resource optimization and bin-packing on all of our production clusters.
Using Terraform and running Azure CLI commands to configure these for every cluster wasn’t aligned with our principle of minimizing human intervention. So, we decided to write a companion Kubernetes operator instead. This introduces a
AzureClusterAdditionalConfig, an extensible custom resource intended for any additional Azure managed service configurations necessary for a cluster. For ACR permissions this resolves to a
AzureRoleAssignment object, and a
AzureClusterAutoscaler object for custom cluster autoscaler configuration.
Introducing the companion operator enabled us to fully automate cluster creation and prepare them to be workload-ready by installing a single kubernetes resource using GitOps. This streamlined approach facilitated the migration of over 80 production clusters between different cloud providers.
# Automating Node Pools
After running production workloads on a new cloud provider for a few months, we identified two major operational pain points.
We didn’t nail the node types (instance family, disk type, etc. settings) at the first attempt. Some of these fields like machineType, diskSize, diskType, maxPod, type (spot vs regular) are immutable fields on AKS. This meant we had to replace node pools running production workloads a handful of times. Each replacement involved creating a new node pool, draining the old one, then deleting it. This process required human coordination and multiple steps in our GitOps workflow.
While updating Kubernetes version we learned that AKS’s in-place node pool upgrade tends to enter an endless retry loop when it encounters an application with 0 disruptions allowed (PodDisruptionBudget setting). Since AKS only
[permits](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/operationnotallowed)one concurrent node pool update operation per cluster, this block operations on other node pools including manual scale up. Consequently, we had to fall back to the multi-step node pool replacement process for upgrades as well.
We implemented a node pool Kubernetes operator, which introduces a single
Nodepool resource encapsulating the multi-step process for replacing a node pool. Under the hood, the operator creates a new node pool, drains the old one, then deletes it in a process completely opaque from the users. From the user’s perspective all node pool manipulations are done in-place with a single GitOps change. This end-to-end automation is especially powerful during Kubernetes version upgrades.
The only limitation was that we couldn’t link the new
Nodepool resource to the existing hierarchy of Cluster API’s
MachinePool or CAPZ’s
AzureManagedMachinePool resource using
ownerReference. Instead, these resources exist side by side and are linked using
objectReference. This drawback becomes apparent when deleting a node pool entirely, as the resource hierarchy is removed using
[finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/).
# Conclusion
Figure 2: Complete cluster management stack.
Evolving our cluster management toolchain empowered us to manage twice as many clusters and applications, while sustaining the same handful of engineers on our Core Infrastructure team. This achievement marks a significant boost in operational efficiency, made possible by our steadfast commitment to GitOps principles and the elimination of human-in-the-loop processes. Along the same lines, self-healing, drift detection, etc. are first class ideas on our platform. This mindset allows us to always
*prioritize organizational needs* leveraging the extensible nature of Kubernetes, while balancing efficiency, reliability and agility.
Reflecting on our journey, we've had some key learnings and missteps:
**Big Bold Bets**: When we explored the industry state-of-the-art for cluster management we couldn’t find anything that meets the level of automation we were striving for. At such times, we leaned on our company’s core value - Big Bold Bets. The bet on Cluster API was fruitful in the long run. **Hidden cost of Open Source**: Strategic partnership and driving appropriate community engagement was vital to making our open source collaboration a success. We did learn that a long term commitment is necessary to be able to effectively steer an open source project to continue to meet our needs. We remain committed to contributing to Cluster API for the foreseeable future. **First Adopter Risks**: We experienced a Sev1 incident lasting several hours where 60% of our nodes on production clusters were wiped out. We traced it to a bug in CAPZ where just the sequence number suffix was used to identify nodes instead of the full
spec.providerID. This caused Cluster API to reference nodes from different node pools within a cluster using the same ID and in turn deleting them.
**Automation Enhances Reliability**: Despite not being the primary focus, our automation efforts significantly improved systems reliability. We’ve successfully completed 4 incident-free Kubernetes version upgrades. Previously, there used to be at least one incident per version upgrade. **Kubernetes Operator Pattern**: We leverage Kubernetes operators extensively in our infrastructure organization. Adhering to standard design patterns like goal state reconciliation enables us to sidestep design debates, mitigate concerns about corner cases, and minimize the learning curve. This along with using managed Kubernetes distributions exclusively was the right tradeoff for us. We remain committed to this approach even today.
So, what lies ahead for us? We've already kicked off a strategic plan to get us to the next level of scale. This involves automatically partitioning workload clusters, considering factors such as API Server pressure and node size. We've also started provisioning more single-tenant clusters. Furthermore, efforts are underway to streamline the time it takes to prepare workload-ready clusters, including steps like IP address allocation and installing cluster addons. All these initiatives are guided by our commitment to minimizing human intervention and achieving full automation. With this roadmap, we aim to adeptly manage over 500 Kubernetes clusters efficiently.
*We would like to acknowledge Cécile Robert-Michon, David Tesar, and Jack Francis at Microsoft. Each contributed during various phases of the project.*