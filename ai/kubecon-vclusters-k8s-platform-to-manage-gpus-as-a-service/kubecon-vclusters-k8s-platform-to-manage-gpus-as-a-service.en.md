ATLANTA — [VCluster Labs](https://www.vcluster.com/) (formerly Loft Labs) has released an augmented version of its [namesake Kubernetes distribution](https://thenewstack.io/vcluster-to-the-rescue/), one customized for running NVIDIA GPUs, the [preferred platform](https://thenewstack.io/nvidias-ai-factories-and-agentic-software-development/) for running [large, compute-intensive AI workloads](https://thenewstack.io/nvidias-ai-factories-and-agentic-software-development/).

The company will be demonstrating the software at [KubeCon+CloudNativeCon North America 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event), being held this week in Atlanta, at booth #421.

The platform is officially called the Infrastructure Tenancy Platform for AI to Maximize GPU Efficiency on NVIDIA Kubernetes Environments. It combines advanced isolation, dynamic scaling, and hybrid networking to provide a platform for organizations to run GPU services in a cloud-like fashion for their internal users.

## Flexible Tenancy for GPUs

“Our story is about flexible tenancy,” explained vCluster CEO [Lukas Gentele](https://github.com/LukasGentele), in an interview with TNS. “Sometimes you need separate clusters for individual tenants. A tenant can be one of your customers or one of your developer teams. It can be for an individual developer, or an application.”

Two groups of users would find this technology potentially valuable, Gentele said. One would be large organizations that have many potential users vying for a limited set of GPUs. Another would be for a public cloud service that would want to offer GPU-based services for its own clientele.

Flexibility is extremely important in both cases, given the dynamic nature of AI work, Gentele said. The ability to dynamically allocate and deallocate them quickly would be a premium feature for such an environment.

Using vCluster’s ability to carve multiple individually-secured “virtual clusters” from one large cluster, companies can provision clusters more quickly, use more of their GPUs and manage [Day 2 operations](https://thenewstack.io/learn-to-love-day-2-operations-with-gitops-driven-api-management/) more effectively, according to the company.

The Tenancy Platform enables “dynamic, multitenant GPU orchestration with the same elasticity and control enterprises expect from the public cloud,” but for private NVIDIA-powered AI systems,” further explained Paul Nashawaty, practice lead and principal analyst at [theCUBE Research](https://thecuberesearch.com/analysts/), in a statement. He noted that theCUBE Research found that 71% of organizations have reported GPU utilization inefficiency as a major challenge.

VCluster has also published a [reference architecture](https://www.vcluster.com/ebooks/reference-architecture-vcluster-on-nvidia-dgx) for running the Infrastructure Tenancy Platform on [NVIDIA DGX line of turnkey GPU servers](https://www.nvidia.com/en-us/products/workstations/dgx-spark/).

## The Infrastructure Tenancy Platform

The distribution is built on a number of Kubernetes technologies, some recently introduced by vCluster, including:

It is directly integrated with the NVIDIA [Base Command Manager](https://docs.nvidia.com/base-command-manager/index.html) (BCM) cluster management software. This is the software that NVIDIA provides to launch bare-metal GPU servers and hook them into the network.

VCluster provides all the supporting software and an ease-of-use experience, Gentele said. The virtual GPUs can be provisioned through the [Kubernetes Cluster API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/), or by Terraform, Helm charts, or kubectl.

The new vCluster Reference Architecture for NVIDIA DGX systems provides a set of best practices for deploying virtual clusters on GPU-centric systems, enabling enterprises to deliver in-house a cloud-like Kubernetes experience.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)