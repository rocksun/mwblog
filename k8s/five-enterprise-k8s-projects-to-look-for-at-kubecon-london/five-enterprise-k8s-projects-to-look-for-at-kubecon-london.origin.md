# Five Enterprise K8s Projects To Look For at KubeCon London
![Featued image for: Five Enterprise K8s Projects To Look For at KubeCon London](https://cdn.thenewstack.io/media/2025/02/32396366-kubecon123-1024x563.png)
If you’re heading to [KubeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) in London this April, chances are you’re not paying to sample the food. You’re going for the sessions and specifically to get your fingers on the pulse of the latest innovations in the cloud native ecosystem.

When you visit the schedule page to build your itinerary, it’s easy to get overwhelmed. There are more than 300 talks to choose from (selected through a grueling process from more than 2,500 submissions).

Despite the huge number of talks, there are still many awesome, vital, game-changing open source projects that have [thriving communities of contributors and users](https://www.cncf.io/blog/2025/01/29/2024-year-in-review-of-cncf-and-top-30-open-source-project-velocity/), but minimal or zero coverage on the event agenda.

Some are relatively mature; some are newer, but they don’t have a significant role on the the Cloud Native Computing Foundation’s ([CNCF](https://cncf.io/?utm_content=inline+mention)) KubeCon EU schedule this year.

- For every OpenTelemetry or Prometheus talk (35+ talks between them), there’s a
[vCluster](https://thenewstack.io/kubernetes-gets-back-to-scaling-with-virtual-clusters/)talk (one). - For every eBPF or Kubeflow session (22 talks between them), there’s a
[Kairos](https://thenewstack.io/livin-kubernetes-on-the-immutable-edge-with-kairos-project/)session (one). - You’ll also find nothing at all about backup tool
[Velero](https://thenewstack.io/how-to-make-up-for-kubernetes-disaster-recovery-shortfalls/), sustainability tool[kube-green](https://thenewstack.io/an-open-source-journey-to-greener-cloud-native-environments/), networking supertool[Multus](https://thenewstack.io/how-to-navigate-multiple-networks-for-kubernetes-workloads/), data store Kine or bare metal provisioner[MAAS](https://thenewstack.io/provision-bare-metal-kubernetes-with-the-cluster-api/). Not a thing.
So let’s take a minute and shine a light on a few projects that, as an enterprise adopter of Kubernetes, you need to know about.

## 1. Cluster API
Cluster API, or CAPI to its friends, definitely falls into the “mature” camp; it started back in 2018. It’s the power behind multicluster Kubernetes, enabling you to declaratively provision and manage clusters, just as Kubernetes declaratively provisions and manages its own resources. Cluster API is extensible; a host of CAPI providers exist, enabling you to manage clusters in different clouds and other infrastructure environments.

CAPI matters because we live in a multicluster, multi-environment world — of course, we need a way to lift ourselves up and orchestrate across clusters. And CAPI does that in an open source way that’s completely in line with K8s and its API-driven, declarative, extensible approach.

You’ll find CAPI today inside Spectro Cloud’s Palette, [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) OpenShift, [VMware Tanzu](https://tanzu.vmware.com?utm_content=inline+mention) and many other products. It’s definitely making an impact on enterprise Kubernetes. And it’s actively maintained, with new releases in just the past few weeks. But with just 3,700 GitHub stars, it’s not exactly in the limelight.

For the lowdown on Cluster API, [read our blog post](https://www.spectrocloud.com/blog/cluster-api-and-kubernetes-cluster-management).

And at KubeCon, you’ll find just a couple of talks mentioning CAPI. We’d put [this one from New Relic](https://sched.co/1txDE) on our schedule.

## 2. KubeVirt
KubeVirt is the most popular solution for bringing VM workloads into your Kubernetes clusters. As a project, it’s been going for more than eight years, but recently development and adoption have increased as enterprises look for an exit strategy from proprietary vendors’ price increases.

While KubeVirt may not yet be a household name, it’s racked up more than 5,000 GitHub stars and is used by Nvidia, Cloudflare and some big enterprises that we’re not allowed to tell you about. On the contributor side, it has some pretty big guns too, including Red Hat, and you’ll find it baked into various K8s management platforms in some way.

If you’re committed to cloud native and you’re looking for a home for your VMs — like thousands of businesses, large and small — you need to be aware of KubeVirt.

At KubeCon you’ll find just three talks that mention it. We’d recommend [this one from Red Hat and Nvidia](https://sched.co/1td18). In the meantime, we recommend [reading this blog post](https://www.spectrocloud.com/blog/production-ready-kubevirt-architecture-for-vms-on-kubernetes).

## 3. vCluster
vCluster enables you to create “virtual clusters” — environments that look and feel like a full-fledged Kubernetes cluster but run within a single host cluster. vClusters can be stood up and torn down in seconds, and have very little overhead. They also are truly isolated from each other.

These qualities solve some real-world Kubernetes pains. vClusters are ideal for ephemeral dev environments because they don’t leave your engineers waiting half an hour for a cluster to get to a ready state, and you aren’t therefore tempted to leave the vCluster up and running after the testing is done. The isolation features address the frustrating weaknesses of namespaces such as resource names spanning all namespaces.

Some vendors have gone so far as to say that you no longer need multiple clusters, you can just run one big cluster and use virtual clusters to segment. We’re not totally convinced by that argument (and our research shows that [the number of clusters is trending up](https://info.spectrocloud.com/2024-state-of-production-kubernetes)) but we certainly believe that vCluster is a great tool for certain use cases, particularly when you’re providing Kubernetes as a service (KaaS) to dev teams.

Since Loft Labs created vCluster, it’s racked up 8,000 GitHub stars, but you’ll only find [one talk at KubeCon](https://sched.co/1tx9S), from Loft.

In the meantime, read up on this [classic blog post from our archives](https://www.spectrocloud.com/blog/virtual-kubernetes-clusters-with-palette-virtual-clusters) to get started.

## 4. Kairos
Kairos is a software factory for building customizable bootable images, primarily intended for use in edge computing environments. You put your preferred OS and Kubernetes distribution in and get secure, immutable images out — making it a vital foundation for success in many edge use cases.

While it only has 1,200 GitHub stars, the contributors are building advanced capabilities like Trusted Boot, and Kairos is already in use in demanding environments like European railways.

In 2024 Kairos became a CNCF Sandbox project, putting it in the spotlight. But if you head to KubeCon, you’ll have to head to the Project Pavilion to meet the team or catch the [five-minute Lightning Talk](https://sched.co/1tcuw) on Tuesday.

You might want to [check out this blog post to get the background](https://www.spectrocloud.com/blog/livin-kubernetes-on-the-immutable-edge-with-kairos-project).

## 5. LocalAI
At the past couple of KubeCons, you couldn’t move for talks about AI, and in London there are 25 talks on the AI/machine learning (ML) track.

We know that K8s folks are embracing AI in all kinds of ways, including with cluster ops assistants like [K8SGPT, ](https://sched.co/1tx86)but we also know that this is a community that understands security and privacy and loves a little #selfhosted and #homelab action.

So it’s a surprise not to see any talks (from a read of the titles) focusing on how to run AI models for local inference in the cluster. Whether for privacy reasons or far-edge deployments, there are lots of use cases where you can’t have data shipped off to the cloud or central DC for analysis.

This is the use case that LocalAI targets, a trending project with over 30,000 GitHub stars. It provides a drop-in replacement REST API that’s compatible with OpenAI API specifications. You can see how it [unlocks value for tools like K8SGPT in this blog post](https://www.spectrocloud.com/blog/k8sgpt-localai-unlock-kubernetes-superpowers-for-free).

## Embracing the Variety
The breadth of the cloud native ecosystem has always been both its killer advantage and its Achilles heel. Our [2024 State of Production Kubernetes research](https://info.spectrocloud.com/2024-state-of-production-kubernetes) found that navigating the ecosystem was the No. 1 challenge for enterprise adopters.

So let’s use this opportunity at KubeCon to step away from the crowded keynotes discussing the usual projects and turn our attention back to the challenges we’re trying to address and the innovative projects being built to solve them.

And let’s do what we can to support those projects, not only through the usual routes of contributing code or funding but also through choosing platforms that are non-opinionated and make it easy to adopt innovations. This idea of choice is one of the guiding principles behind our Palette platform. [Take a look.](https://www.spectrocloud.com/integrations-and-environments)

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)