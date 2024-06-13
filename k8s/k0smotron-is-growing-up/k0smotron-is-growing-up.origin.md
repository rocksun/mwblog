[< BLOG HOME](/blog)
# k0smotron is Growing Up
[Jussi Nummelin](/blog/authors/jussi-nummelin)- June 11, 2024 ![image](https://a.storyblok.com/f/153547/1080x608/a3934909cf/k0smotron_1-0_announcement_blog.png/m/)
## k0smotron 1.0 announces general availability with new enterprise capabilities, including enabling remote deployment of whole clusters on any infrastructure, improving control plane high availability, and enabling updates-in-place. Making things more seamless and simple for Kubernetes multi-cluster deployments.
Organizations using Kubernetes face the challenge of defining, provisioning, scaling, and lifecycle-managing clusters. Many need to do this on more than one kind of infrastructure — private cloud, public cloud, bare metal, etc.
Platform teams need ways to define k8s clusters and related services, so that operators and developers can deploy them on demand. Platform teams and architects need ways to specify deployments with novel footprints – conventional or hosted control planes, local or remote workers – to suit requirements of modern hybrid, edge, and other use cases.
k0smotron – introduced last year and announced in November – offers an open source, Kubernetes-native solution to these multi-cluster/hybrid challenges. It works hand-in-hand with Kubernetes ClusterAPI to enable declarative infrastructure provisioning on your choice of public clouds, private clouds, managed or unmanaged bare metal, or any combination thereof. k0smotron helps you configure, deploy, and lifecycle manage k0s Kubernetes child clusters across all these infrastructures: as many as you’ve installed CAPI providers to support. (
[.) Learn more about ClusterAPI](https://www.mirantis.com/blog/how-to-use-cluster-api)
But there’s more. By leveraging the unique advantages of k0s Kubernetes (like control plane/worker network separation), k0smotron 1.0 makes it easier to configure exotic cluster footprints for hybrid, edge, and even wilder use cases:
Control planes in the cloud with high-powered worker nodes on customer premises
Containerized control planes on a public cloud ‘mothership’ cluster, with remote workers at the far edge, behind a firewall
IoT with fully-mobile workers
k0smotron can do all this – and k0s helps keep the networking fairly simple.
### Pave the World with Kubernetes
By putting everything you need for platform management behind the Kubernetes API and declarative configuration, k0smotron provides what you need for Kubernetes-native multi-cluster GitOps, and gets you a big step closer to using Kubernetes to ‘pave the world’ of infrastructures under a Kubernetes substrate.
With k0smotron 1.0 (combined with Helm for efficiently installing applications and services on child clusters), platform engineers can package up full solution-stacks in a single set of version-controlled YAML files: composing everything a software development team needs (i.e., infra(s), cluster(s), installed services and applications) to cover a broad range of use cases, such as:
Entire SaaS point-of-presence configurations
Complete edge applications with endpoint architectures
Multi-service mobile network platforms and services
All now easily-deployed and self-maintaining.
One obvious benefit for platform engineers: simplicity. With k0smotron, you don’t need to install, maintain, update, manage a ton of different deployment tools (and their own collections of YAML or other configuration codebases).
k0smotron also makes sense in terms of macro trends:
First, Kubernetes is beyond a doubt the future platform for everything. It’s currently the best tool we have for running complex modern applications. And it provides the core platform for all the higher-order services we need (like serverless and PaaS and functions-as-a-service, etc). So using it to pave over infrastructure simplifies our lives, and even lets us think about infrastructure in new ways — we can even think about public clouds as commodity utilities. (Remember when we all thought about ‘cloud’ that way and imagined a future in which compute/storage/network providers would compete for our workloads without locking us in and charging us a ton of money? This was the original goal.)
Second, Kubernetes is good at this. It’s a standardized machine for looking at declarative files describing a desired state, and then (either directly or through standard middleware) converging reality on that state. That’s why modern configuration-automation tools all work basically this way.
Having <everything> behind the Kubernetes API (and making sure this is entirely open source and standardized) gives us superpowers:
One way to describe and implement deep solution-stacks
One way to inject and implement observability
One point of integration for DevSecOps
Maybe most importantly, one point of integration for AIOps.
### Tested by Actual Customers
k0smotron has been in the hands of key Mirantis customers for a while now, and we’re so grateful for their help and enthusiasm. Today we’re announcing general availability of k0smotron 1.0, along with enterprise support. k0smotron 1.0 has some exciting new features that make it an even more complete solution. No longer primarily a “hosted control plane manager,” k0smotron 1.0 is now a true multi-cluster/hybrid management solution.
New features in k0smotron 1.0 include:
### Remote Machine Support
**k0smotron RemoteMachine is now a full-fledged infrastructure provider for Kubernetes ClusterAPI (see the ** __Providers list__ **), enabling provisioning of remote machines via SSH.** k0smotron can now use RemoteMachine to (for example) build and lifecycle-manage distributed or monolithic k0s clusters with hosted or conventional control planes.
Benefit: Convenient operations on unmanaged bare metal, opening up use cases in data centers and at the edge. For example, you can build a cluster with a k0s hosted control plane on a mothership cluster in a public cloud, with remote workers on bare metal Linux machines at an edge location or on a customer’s premises.
k0smotron + CAPI providers (including RemoteMachine) can also work as a high-level infrastructure provider with non-k0s control plane providers. So in principle, you can now use k0smotron RemoteMachine to deploy k3s or MicroK8s (or many other) cluster flavors, as well. k0smotron RemoteMachine can also support custom SSH connectors, so if your infrastructure requires you to use Teleport, for example, you can
[ to run provisioning with Teleport-required infrastructure authorization. customize the provider](https://docs.k0smotron.io/stable/capi-remotemachine-teleport/)
### Control Plane Scaling and Updates
Conventional k0s clusters can automatically and non-disruptively update themselves (controllers and workers) by leveraging the Autopilot operator. Previous versions of k0smotron, however, didn’t fully support this paradigm, since k0smotron had no means for signaling the in-cluster Autopilot to update hosted child cluster control planes.
**Now, for child clusters running in virtual machines, k0smotron 1.0 integrates with the child cluster’s Autopilot to update the full cluster (controllers and workers) – using a node-by-node strategy that keeps clusters available.**
Benefit: Easy scaling of child clusters on multiple infrastructure platforms, in a standardized way.
### External etcd Support for Control Plane HA
To enhance high availability (HA) for hosted control planes (running a k0s control plane in pods),
**k0smotron 1.0 will now deploy etcd in a separate pod (and statefulset) from the hosted control plane component.** Previously, running a highly available hosted control plane (i.e., multiple containerized controllers, deployed to different fault domains) was challenging, due to potential split-brain scenarios as etcd (effectively part of each control plane) got scaled up and down. With the new update, etcd is managed independently of other HCP components (in a separate set of pods), letting it scale independently. etcd can also be snapshotted and restored, enabling robust full cluster upgrades and restoration of state. *Note: this involves a breaking change with regard to versions of k0smotron prior to 0.9.5 – see * __this note__ * for more information and a simple workaround.*
Benefit: Freely-scalable hosted control planes – so you can balance redundant availability with utilization.
### Clusterctl Support
Finally,
**k0smotron 1.0 adds support for installing k0smotron through ClusterAPI’s clusterctl CLI.** Users can install and manage k0smotron directly through clusterctl instead of separately – making it easier to, in effect, turn a ClusterAPI setup for infrastructure management into a complete multi-cluster solution. Simple:
clusterctl init --bootstrap k0sproject-k0smotron \ --control-plane k0sproject-k0smotron \ --infrastructure k0sproject-k0smotron
Benefit: Simpler setup. From zero to ‘complete multi-cluster manager’ in one command.
### ClusterClass Support
Defining a complete Kubernetes cluster plus its infrastructure for ClusterAPI previously required pretty long and complicated YAML files – sometimes in excess of 500 lines.
**ClusterClass – now an alpha feature in ClusterAPI – lets you standardize an infrastructure definition, then reference it (with variations) in just a few lines of code.** This is supported in k0smotron 1.0 – streamlining files, making them more readable and manageable, enabling development of reusable configurations, and simplifying automation.
Benefit: Improved reusability and easier-to-read code. Less chance of errors creeping in.
### Try k0smotron today!
k0smotron 1.0 is now a full multi-cluster manager – hosted control planes are no longer the whole story (though they are extremely cool and useful).
Also exciting, k0smotron will now be fully supported globally by Mirantis – so enterprises wishing to explore solutions or bring use cases to life with k0smotron at scale can do so with the backing of Mirantis’ deep Customer Success engineering bench, as well as the particular expertise of Team k0s itself. Support will be available in three tiers:
LabCare - 8 x 5 (M-F) business hours support. For non-production workloads
Opscare - 24/7 support, with 30-minute response time SLA on critical issues. For enterprise production environments
Opscare Plus - Fully managed, proactive support, with >99.9% availability
Please note that support for k0smotron includes support for k0s – the zero friction, zero dependencies, CNCF-validated Kubernetes.
Try k0smotron 1.0 today and experience the future of Kubernetes cluster management. For more information, visit
[ – our GitHub for releases, community, or contributing – or schedule a k0smotron.io](http://k0smotron.io) [with Mirantis.](https://mirantis.com/contact) __live demo__