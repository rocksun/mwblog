# Mirantis Tackles Container Sprawl With Open Source k0rdent
![Featued image for: Mirantis Tackles Container Sprawl With Open Source k0rdent](https://cdn.thenewstack.io/media/2025/02/717e87c6-kordent-1024x768.png)
We all use cloud native applications, but no one finds managing them easy. True, [Kubernetes](https://thenewstack.io/kubernetes/) enables us to orchestrate them, but it’s still a lot of work. To address this, [Mirantis](https://www.mirantis.com/about/), a leading provider of open source cloud native programs, has launched [k0rdent](https://github.com/Mirantis/project-2a-docs), the first of what it calls an open source Distributed Container Management Environment (DCME).

K0rdent’s designed to address the growing challenge of [container sprawl](https://thenewstack.io/containers/). It does this by providing a single control point for managing cloud native applications across various environments, including on-premises, public clouds, and edge locations.

## Single Pane of Glass
Well, I’d call it a single pane of glass, myself, but that term’s no longer fashionable. Call it what you will, k0rdent offers several advantages for organizations grappling with Kubernetes complexity. These are:

- Unified Management: The platform enables easy creation of customized internal developer platforms (IDPs), simplifying the management of Kubernetes clusters across diverse infrastructures.
- Composable Architecture: Platform engineers can tailor k0rdent to their specific requirements, leveraging standardized deployment templates for rapid implementation.
- Multicloud Support: k0rdent has been tested on major cloud platforms, including AWS EC2, AWS EKS, Azure Compute, Azure AKS, and on-premises solutions like vSphere and OpenStack.
- Declarative Automation: The platform streamlines maintenance through declarative automation, centralized policy enforcement, and production-ready templates optimized for modern workloads.
- Open Source Advantage: By leveraging the open source Cluster API, k0rdent allows for creating and deploying Kubernetes clusters anywhere, promoting flexibility and avoiding vendor lock-in.
Put it all together, and you get, according to [Shaun O’Meara](https://www.linkedin.com/in/shaun-omeara/) Miranti’s CTO in a blog post, not just a program to help you manage infrastructure and services but “about pr[oviding a unified, scalable, and policy-driven platform that can handle modern distributed workloads](https://www.mirantis.com/blog/announcing-k0rdent-a-new-era-of-kubernetes-native-distributed-container-management/) — without forcing teams into vendor lock-in or operational bottlenecks.”

That’s a win in my book.

[Randy Bias](https://ph.linkedin.com/in/randybias), Mirantis’s VP of open source strategy and technology, explained in a statement, “[k0rdent is designed for creating customized internal developer platforms, powered by Kubernetes](https://www.businesswire.com/news/home/20250206532790/en/Mirantis-Launches-Open-Source-Project-for-Platform-Engineering-that-Accelerates-Innovation-for-Modern-Distributed-Workloads), that assist in large-scale application management across any infrastructure anywhere while providing choice, accelerating innovation, and enforcing compliance.”
## Multicloud Environments
So, why is Mirantis doing this as an open source project? The story behind k0rdent started with the broader trends we see in the technology landscape — the increasing complexity of deploying and managing modern, distributed workloads across multicloud environments and the rise of AI. As an open source company with deep roots in the cloud native ecosystem, Mirantis had a front-row seat to these shifts.

Earlier, Mirantis had built a robust Kubernetes multicluster management program, [Kubeadm-dind-cluster (KDC)](https://github.com/kubernetes-retired/kubeadm-dind-cluster), that handled everything from bare metal to the public cloud. However, it took a very opinionated approach that didn’t easily provide the flexibility and composability modern platform engineers need to build IDPs for demanding, cloud native workloads. Recognizing these limitations, Mirantis took a fresh approach.

## Container Control Plane
That’s where Mirantis’s idea for k0rdent was born. Mirantis wanted to create an open source, distributed container management environment that would remove barriers to deploying diverse, distributed applications across complex, multicloud environments.

Built on Kubernetes as a multicloud control plane, Mirantis claims k0rdent goes beyond infrastructure — it provides the higher-level abstractions, templated workflows, and automation necessary for platform engineers to deliver scalable, repeatable, and secure environments.

As Kubernetes adoption continues to grow, solutions like k0rdent are poised to play a crucial role in helping enterprises manage the complexity of distributed container environments. With its focus on simplification, customization, and open source principles, k0rdent represents a significant step forward in addressing the massive challenges of managing Kubernetes-driven, cloud native deployments.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)