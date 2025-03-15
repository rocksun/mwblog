# Kubernetes Fleets: Beyond the IoT Edge
![Featued image for: Kubernetes Fleets: Beyond the IoT Edge](https://cdn.thenewstack.io/media/2025/03/57a97849-chip-1024x576.jpg)
With the breakneck speed of technology, 10 years is an eternity. Ten years ago, IoT was taking off thanks to the proliferation of mobile devices. Companies were looking for [ways to process the data](https://thenewstack.io/5-ways-data-protection-for-kubernetes-is-different/) from their web of devices, and public clouds were ready to provide solutions.

For those looking for local processing, [Kubernetes](https://thenewstack.io/kubernetes/) — just over a year old itself — was a natural choice. Kubernetes allowed these companies to [deploy myriad applications locally](https://thenewstack.io/a-look-at-kubernetes-deployment/) that mimicked and integrated with the services available in the cloud, giving them incredible flexibility in deployment location. Borrowing a term from networking, this was colloquially referred to as “the edge.”

## From Edge to Fleet
Ten years later, Kubernetes is going stronger than ever. Not only are new applications built cloud native by default, but existing applications have been refactored, and cloud native versions of third-party tools are now available. Taking advantage of the same deployment flexibility and development velocity that IoT thrived on, companies have replaced existing compute stacks and extended into unique new locations with Kubernetes. For example:

- Replacing a VM stack in each store branch with a centrally managed Kubernetes stack
- Running a stack of Kubernetes on each cruise ship to provide on-ship services
- Fighter jets running Kubernetes on missions to process data and respond in real time
These haven’t traditionally been thought of as the edge, but it is fundamentally the same construct. Put another way, Kubernetes doesn’t just allow us to run machine learning workloads at the edge — any workload can be at your edge. This is the new edge: the Kubernetes fleet.

So what are some of the [key considerations when planning and building your Kubernetes fleet](https://thenewstack.io/the-state-of-kubernetes-key-challenges-and-the-role-of-ai/)?

## Building the Stack
Deploying a base Kubernetes cluster is easy; adding all the functionality is where it gets difficult. With so many tools going into an enterprise-ready Kubernetes stack — such as networking, ingress gateways, policy management and service meshes — you must ensure that whatever you choose to deploy, you can manage at scale. And don’t forget about supportability.

Look for projects that are well established and well adopted. The Cloud Native Computing Foundation has a whole list of projects you can use. Your current workloads can tell you what kinds of features you’ll need, but it’s also important to not lock yourself in. You may choose one networking stack, but down the line realize that a different one provides a unique feature or a more compatible stack, and you don’t want to be stuck. Look for solutions that are flexible enough to adapt to swapping out components or running components alongside each other to ensure that, no matter what, you can use the right tool for the job.

## Deployment and Future Expansion
One of the natural consequences of many smaller stacks is that new deployments happen far more often. No longer is deployment something that occurs once every few years. When comparing Kubernetes fleet-management solutions, it’s important to consider both how long it will take you to deploy the base solution as well as how long it takes to add additional clusters. The quicker you get started with the base solution, the quicker you can challenge and update your expectations and adapt to the growing needs of your applications. The quicker you can deploy a new cluster, the quicker you can expand.

## Migration and Split Stacks
While many companies are deploying pure Kubernetes stacks, that doesn’t work for everyone. Operators will often discover that they have a need for a small number of other VMs in addition to their Kubernetes clusters. This can happen for a limited period of time. For instance, there might be a migration period or cutover where both need to run alongside each other, or perhaps there are a couple of applications that can’t be containerized. Rarely, operators will fully adopt Kubernetes on remote sites only to discover a new use case that can’t be easily containerized.

When building your Kubernetes fleet, it’s important to consider how to manage these split workloads. How closely should the two systems work together, or should Kubernetes and VMs be treated as completely separate stacks? What will you do when you need to move workloads between the two environments?

## Handling State and Storage
As Kubernetes expands to new workloads, the number of containers requiring state and storage has skyrocketed. Storage should not be an afterthought; it needs to be a first-class citizen when planning your fleet.

Of course, this isn’t just the physical storage itself. Backups need to be considered as well. Just like with any enterprise workload, be sure to consider your recovery time objective (RTO) and recovery point objective (RPO) targets. Just because a cluster isn’t in the data center doesn’t mean that these considerations change.

## Life Cycle Management of Hardware
Naturally, any [Kubernetes fleet management](https://thenewstack.io/kubernetes-will-revolutionize-enterprise-database-management/) solution will handle upgrades of Kubernetes itself as well as core services, but that’s not the only piece to worry about here. The hardware needs updates too.

When planning your solution, think through how you’ll handle firmware updates, such as the basic input/output systems (BIOS). What level of exposure is the company willing to take between the release of a new CVE and mitigation of the issue? How will you audit to make sure that updates are applied as expected?

## An Ounce of Prevention Is Worth a Pound of Cure
Spending the time in the beginning on what to consider in your Kubernetes fleet will save you plenty of heartache down the line. Early decisions can easily create dreaded tech debt that will take far longer to fix later than if properly planned out.

Nutanix is excited to sponsor KubeCon this year in London. Come check out our booth and talk to us about your Kubernetes plans, and see how we can help with virtualization, Kubernetes and storage anywhere.

*To learn more about Kubernetes and the cloud native ecosystem, join us at* *KubeCon + CloudNativeCon Europe** in London on April 1-4.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)