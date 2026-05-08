Kubernetes is complicated; everybody knows it. Logically enough, Kubernetes deployed as a cluster of collected and coalesced instances at “fleet scale” is unquestionably complicated.

Synchronizing the configurations of thousands of clusters across massively distributed environments that span on-premises, cloud, and edge is a big ask, so how is it done?

VIDEO

## Small is beautiful, big is brutal

In a more standard (smaller) environment, automated controllers in Git repositories sync the desired state of a cluster held in Git with the actual state in a given Kubernetes cluster.

[Stephane Erbrech](https://www.linkedin.com/in/serbrech/), principal software engineer at Microsoft, tells *The New Stack* that although GitOps is the dominant declarative management pattern in the Kubernetes ecosystem, its single-cluster assumptions are a real constraint as fleet size grows.

“In a standard GitOps setup, cloud-native software engineering teams might manage one or two clusters,” Erbrech says. “At fleet scale, the complexity shifts from how you deploy… to how you govern a massive, distributed environment without manual intervention.”

> “Since the customer base and community have grown around Kubernetes…teams now start with one cluster, but then grow to two, then ten… and then subsequently to hundreds or even thousands.”

He notes that GitOps typically assumes a 1:1 relationship between a repository and a cluster. It often overlooks multi-cluster complexities like global traffic routing, cross-cluster secret synchronization, and unified observability across environments.

“Since the customer base and community have grown around Kubernetes (and it has been cemented as the platform of choice), we’ve seen teams start with one cluster, but then grow to two, then ten… and then subsequently to hundreds or even thousands,” Erbrech explains. “On this journey, they all end up with the same problems that they used to have with VMs and how to manage them and stay compliant and secure.”

The need for massively distributed Kubernetes stems from many reasons (straightforward popularity being one), but a key driver is that AI is being deployed everywhere, i.e., on every edge device, from wind turbines to bakery ovens. This means unified cluster management had better scale the same way. As inference workloads become distributed by default, cluster management needs to move beyond the reconciliation lag that GitOps will suffer from at scale.

## All the cluster’s a stage

Offering this backdrop as contextual validation for [Microsoft Azure Kubernetes Fleet Manager](https://azure.microsoft.com/en-gb/products/kubernetes-fleet-manager), Erbrech says that this management-layer technology allows teams to define reusable strategies for orchestrating cluster updates across a fleet.

Engineers can group clusters into stages to enable a more controlled rollout. This means cluster updates can be applied sequentially, potentially with validation in lower-risk environments (such as test environments) before being applied to critical live production cluster areas within the fleet.

“This control enables developers to deploy applications safely, environment by environment, cluster by cluster, at the pace the team chooses, all while continuously checking metrics and ensuring nothing breaks across the deployed environment,” Erbrech explains.

> “Cilium Cluster Mesh is the technology we use to ‘underneath’ to enable the cross-cluster connectivity that Microsoft Azure Kubernetes Fleet Manager delivers and enable the network work in a seamless manner.”

## Cilium Cluster Mesh

Cilium is also an important part of this story. The open-source networking, security, and observability service for cloud-native environments was extended with the arrival of [Cilium Cluster Mesh](https://cilium.io/use-cases/cluster-mesh/).

“Cilium Cluster Mesh is the technology we use to ‘underneath’ to enable the cross-cluster connectivity that Microsoft Azure Kubernetes Fleet Manager delivers and enable the network to work in a seamless manner,” Erbrech clarifies. “The [Cilium] community has put in so much work to enable smart network policies and control mechanisms; because of the eBPF layer in Cilium, teams can manage certificates in just a couple of clicks.”

The aggregation of control that this technology brings is clearly appealing to cloud-native engineers, many of whom will be painfully aware of just how multifarious and unwieldy the total Kubernetes toolkit can be. The elevated control that Erbrech talks of in Microsoft Azure Kubernetes Fleet Manager means teams can now enable clusters to “talk to each other” as workloads can be moved from cluster to cluster

“All that happens seamlessly, and the end user is none the wiser, because the workload remains eminently accessible, and everything works fine,” Erbrech surmises.

> Because GPU resources are expensive and occasionally scarce, cross-cluster workload journeys help ensure teams take advantage of provisioned resources and do not leave them idle and wasted.

We mentioned the wider transept of AI inference at the start in relation to the edge, and there’s a second vector that impacts the workload trajectory to accommodate here. Because GPU resources are expensive and occasionally scarce, cross-cluster workload journeys help ensure teams make efficient use of provisioned resources and do not leave them idle or wasted.

## Cluster lifecycle management

All of which brings us full circle to cluster lifecycle management and the ability to use Microsoft Azure Kubernetes Fleet Manager as a route not just for sequenced Kubernetes version upgrades, but also for end-of-life actions as clusters are periodically retired.

As platform engineering now intersects with cloud-native management layers across increasingly distributed and complex environments, we will need to manage the fleet to keep it afloat amid a veritable armada of misconfiguration skews. Batten down the hatches, everyone.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)