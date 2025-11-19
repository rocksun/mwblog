Once upon a time, major banks built their own Linux kernels because there were no [distros](https://thenewstack.io/best-linux-distros-for-development/) yet. They were pioneers who knew they wanted Linux but had to figure everything out themselves. Now, though, it’s just the way the world works.

“Everybody’s got a commercial Linux distro. That’s what we all run on,” mused [Jesse Butler](https://www.linkedin.com/in/jesse-butler/), principal project manager for Amazon EKS, at [KubeCon + CloudNativeCon North America](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) in Atlanta. “I think Kubernetes is now there as well. We’ve gone from building our own bespoke cluster API servers and our own control planes to looking for standards to build at scale for our enterprises.”

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Butler’s point: There’s no longer a market segment or a certain type of organization using Kubernetes — everyone is using it. And that universality changes how companies like [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) approach open source contributions.

In this episode of The New Stack Makers, Butler sat down with TNS Founder and Publisher [Alex Williams](https://thenewstack.io/author/alex/) to discuss two open source projects that AWS EKS has donated via different SIGs within the Kubernetes community: [Kubernetes Resource Orchestrator (Kro)](https://thenewstack.io/the-kro-project-giving-kubernetes-users-what-they-want/) and [Karpenter](https://thenewstack.io/migrating-from-cluster-autoscaler-to-karpenter-v0-32/). But more importantly, they talked about why AWS is building these as Kubernetes features rather than standalone products — and what that shift means for the ecosystem.

## When Your Glue Code Becomes Technical Debt

The catalyst for Kro came from watching customers struggle with controller proliferation. As Butler explained, once custom resource definitions (CRDs) made it easy to represent everything from cloud infrastructure to network switches as Kubernetes resources, organizations started building custom controllers just to glue other resources together.

“Some of our customers, even four or five years ago, had 20 or 30 custom resources,” Butler noted. “So you have some small team inside of a much larger organization that has to own just this code, and it isn’t even really business logic.”

Kro was built to automatically generate both the CRD and a microcontroller to manage it. Platform engineers define what they want in YAML using Kro’s Simple Schema, specify the constituent resources, and Kro infers dependencies, creates a directed acyclic graph and handles the orchestration. It’s Controller as a Service, but without leaving the Kubernetes ecosystem.

## The Node Provisioning Problem Nobody Wanted To Solve

Karpenter emerged from a different pain point: The cluster autoscaler couldn’t keep up with cloud native workloads. “Cloud native workloads in general are spiky, they’re dynamic,” Butler said. The traditional approach of predicting capacity needs quickly broke down.

Karpenter’s solution? Just-in-time node provisioning that not only scales based on demand but also optimizes for cost.

What’s caught on isn’t just the automation — it’s the API design. “The Karpenter API lets you just be as simple as you want – ‘Hey, just give me a node’ – or go all the way to really fine-grained detail for that node configuration,” Butler said. That elegance, combined with real cost savings, drove rapid adoption and ultimately led to Karpenter being donated to the Kubernetes SIG Autoscaling.

Both projects reflect a philosophical shift at AWS: building solutions that work for the entire Kubernetes ecosystem, not just AWS customers.

“In the context of Kubernetes and cloud native software, this is a community and we are all the customer,” Butler said. “We can’t very well build something just for our product and say it’s Kubernetes.”

The full conversation dives deeper into Kro’s Resource Graph Definitions, Karpenter’s evolution from prototype to stable API and why AWS is increasingly donating projects to Kubernetes SIGs rather than creating competing [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) projects. For anyone watching Kubernetes mature from scrappy orchestrator to enterprise standard, it’s a revealing look at how the most successful open source projects grow up.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/05/5bc05c60-cropped-bb29d761-michelle_gienow.jpeg)

Michelle Gienow is a former journalist turned software developer. She draws from both professions to write about in-depth technical topics ranging from K8s to Kotlin. Michelle is co-author of "Cloud Native Transformation: Practical Patterns for Innovation" from O'Reilly Media and...

Read more from Michelle Gienow](https://thenewstack.io/author/michelle_gienow/)