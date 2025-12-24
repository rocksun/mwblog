“As a low-level systems engineer, if you do your job right, no one knows you exist — but the minute you do your job wrong, everybody knows you exist.”

That observation from Nvidia Distinguished Engineer [Kevin Klues](https://www.linkedin.com/in/klueska) underlines why the Kubernetes open source community has been quietly building foundational features and abstractions that will shape how organizations run AI workloads for the next decade.

VIDEO

At [KubeCon + CloudNativeCon North America 2025](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) in Atlanta, New Stack Founder and Publisher [Alex Williams](https://thenewstack.io/author/alex/) led a panel discussion with Klues and [Jesse Butler](https://thenewstack.io/how-kubernetes-became-the-new-linux/), principal product manager at [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), about two developments that deserve more attention: dynamic resource allocation (DRA) and an upcoming workload abstraction that could transform multinode AI deployments.

## DRA: GPUs That Work Like Storage

[Dynamic resource allocation (DRA)](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/), which reached general availability in [Kubernetes 1.34](https://thenewstack.io/kubernetes-v1-34-introduces-benefits-but-also-new-blind-spots/), solves the long-standing frustration around requesting GPU resources in Kubernetes.

“The only knob you had in the old way of requesting access to resources was a simple count,” Klues said. “You could say, ‘I want two GPUs,’ but you couldn’t say what type of GPU. You couldn’t say how you might want that GPU to be configured once it’s given to you.”

DRA, which Butler called “one of the most elegant things I’ve ever seen,” borrows its conceptual model from persistent volumes and persistent volume claims — familiar abstractions that storage teams have used for years. The difference is that DRA works with any specialized hardware, not just storage, meaning that third-party vendors can now bring their own device drivers and make hardware accessible to Kubernetes users in standardized ways.

## A New Workload Abstraction for Smart Scheduling

But DRA alone isn’t enough for complex AI deployments. Sometimes you need multiple pods across multiple nodes to all come online simultaneously or, conversely, not at all. That’s the problem a new Kubernetes abstraction (called, simply, “the workload abstraction”) aims to solve.

“You want to be able to express things like, I can have some subset of these pods come up, but if I can’t get all of them, I don’t want any of them to come up,” Klues said. “And, at least today, you can’t really express that in the Kubernetes world.”

A basic implementation is slated for the [Kubernetes 1.35](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)  release on Dec. 17, though Klues emphasized there’s significant work ahead. The abstraction will let users define pod groupings with scheduling constraints and topology requirements, kind of like node selectors on steroids.

“It’s going to shape the future of how all of this works for the next 10 years of Kubernetes,” Klues said, stressing that the [Device Management Working Group](https://github.com/kubernetes-sigs/wg-device-management), where these features take shape, strongly invites community participation.

For the full conversation — including discussion of agentic AI architectures, small language models, and why Unix philosophy still matters in the age of large language models — check out the complete interview.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/05/5bc05c60-cropped-bb29d761-michelle_gienow.jpeg)

Michelle Gienow is a former journalist turned software developer. She draws from both professions to write about in-depth technical topics ranging from K8s to Kotlin. Michelle is co-author of "Cloud Native Transformation: Practical Patterns for Innovation" from O'Reilly Media and...

Read more from Michelle Gienow](https://thenewstack.io/author/michelle_gienow/)