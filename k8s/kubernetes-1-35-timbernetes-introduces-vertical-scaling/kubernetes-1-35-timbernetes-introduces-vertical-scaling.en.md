As any good home gardener knows, a healthy plant can outgrow its planter.

And so it is with Kubernetes jobs, some have found. They are growing too big for the nodes that they run on.

The latest release of the Kubernetes open source orchestration platform introduces in-place updates for pod resources.

This feature (described in [KEP #1287](https://kep.k8s.io/1287) ) allows users to adjust CPU and memory resources on the fly, without having to restart pods or containers.

Overall, the release of Kubernetes v1.35 (working name “Timbernetes”)  introduces 60 enhancements.

Of those enhancements, 17 have graduated to stable status (including vertical scaling), meaning they are fully production-ready.

Another 19 have entered Beta as features worth testing, and 22 are brand new technologies that have entered Alpha testing stage.

There are also some notable [deprecations and removals](https://deploy-preview-53498--kubernetes-io-main-staging.netlify.app/blog/2025/12/17/kubernetes-v1-35-release/#deprecations-and-removals) in this release.

## A New Feature: Vertical Scaling

Kubernetes workloads have always been horizontally scalable, as long as they are stateless (don’t hold any unique data).

More nodes can be spun up and additional identical copies of the containerized app can be added, assuming that the application is designed such that more copies can be easily added for additional capacity.

In recent years, however, K8s operators have been calling for in-place upgrades, to boost the memory and/or CPU capacities of the existing node the application is running upon — while keeping the application running.

This sort of scaling is a bit trickier for stateful workloads, in which some data or unique business logic resides in the node being upgraded.

Previously, upgrading in place required creating a new pod and then moving the workload over, which could cause service disruptions.

This new feature allows users to adjust cpu and memory resources without restarting pods or containers.

## What Other New Features Are in Kubernetes 1.35

Some of the other notable new features in this release include:

* **KYAML** (Beta): Kubernetes has always been configurable through the YAML human-readable format, often to the consternation of operators [who would prefer](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/) a less fussy and easier-to-understand language to work with. KYAML is a subset of YAML optimized for Kubernetes, making it easier to use not only for operators but also more expressive for Kubernetes tools such as kubectl. ([KEP #5295](https://kep.k8s.io/5295)).
* **Gang scheduling** (Alpha): Large, interdependent AI workloads will benefit from this one: An “all-or-nothing” scheduling strategy that will ensure that a defined group of pods is scheduled only if the cluster has sufficient resources to accommodate the entire group simultaneously. ([KEP #4671](https://kep.k8s.io/4671)).
* **Mutable container resources when a job is suspended** (Alpha): Until now, if a job fails due to an out-of-memory error or insufficient CPU, the user must delete the Job and create a new one, losing the execution history and status. Kubernetes v1.35 introduces the capability to update resource requests and limits for Jobs that are in a suspended state. ([KEP #5440](https://kep.k8s.io/5440)).

This release also includes some notable depreciations. One major one is the long-used Ingress NGINX retirement in favor of the  [Gateway API](https://gateway-api.sigs.k8s.io/), which has had operators [scrambling](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/) for an update.

Also support for the Linux control groups (cgroup v1) will be coming to an end, as permissions are [now being managed](https://thenewstack.io/linux-cgroups-v2-brings-rootless-containers-superior-memory-management/) by cgroup v2.

For full details of all the new features and deprecations, check out the Kubernetes v1.35 [release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md).

## Plant a Tree

Each release of Kubernetes gets a fresh logo, which is usually done by the tea release lead. In this case, it was done by [Drew Hagen](https://www.linkedin.com/in/drew-hagen/), a Kubernetes engineer who was the team release manager for v 1.35.

“The bar is really high on the logos, I wanted to come up with something that was both fun, but also symbolic,” he told TNS.

He chose a tree as the main image in order “to demonstrate the resilience of the Kubernetes community.”

“The maintainers and contributors have day jobs, have families, and some of them are volunteering for this. But they are coming together from all around the world to contribute to one of the [biggest open source projects](https://thenewstack.io/kubernetes/),” he said.

Kubernetes v1.35 is available for download on [GitHub](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.0) or on the [Kubernetes download page](https://deploy-preview-53498--kubernetes-io-main-staging.netlify.app/releases/download/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)