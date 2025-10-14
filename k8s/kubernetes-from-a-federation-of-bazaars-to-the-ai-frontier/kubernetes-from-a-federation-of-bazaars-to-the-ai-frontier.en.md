Looking back, it’s hard to believe the Kubernetes project has been around for over a decade. It makes me think of [Eric S. Raymond](https://en.wikipedia.org/wiki/Eric_S._Raymond)’s old essay, “[The Cathedral and the Bazaar](https://www.oreilly.com/library/view/the-cathedral/0596001088/),” and how we used to see open source. You either had the “cathedral,” built from a master plan by a select group of developers, or the “bazaar,” a chaotic but vibrant marketplace of ideas.

So, which one is Kubernetes? After years of working deep on its codebase and community, I can tell you it’s neither. [Kubernetes](https://thenewstack.io/kubernetes-an-overview/) is something new: a federation of bazaars. It’s a place where the work of thousands of passionate people is guided not by a top-down architect, but by a shared vision and a structure that trusts experts to do their best work. That’s our secret sauce. It’s why we move so fast, and it’s why we’re now ready for our next big challenge: becoming the go-to platform for [AI](https://thenewstack.io/ai-for-developers-how-can-programmers-use-artificial-intelligence/).

## **The Federation of Bazaars**

You might assume a project of this scale relies on a rigid, top-down plan, but the real magic happens within our [Special Interest Groups (SIGs)](https://github.com/kubernetes/community/blob/master/committee-steering/governance/sig-governance.md). Think of SIG-Network, SIG-Node and SIG-API-Machinery — focused groups where experts from across the industry roll up their sleeves to tackle tough challenges in their specific domains.

Of course, these SIGs don’t work in isolation; they are constantly communicating. [SIG Architecture](https://github.com/kubernetes/community/tree/master/sig-architecture) serves as the natural forum where cross-SIG technical matters are discussed to ensure the project remains a cohesive whole. For particularly complex and ambiguous problems that span multiple SIGs, we form [Working Groups](https://github.com/kubernetes/community/blob/master/committee-steering/governance/wg-governance.md). These temporary groups bring together experts from different SIGs to focus on solving a specific, challenging issue and then disband once their mission is complete.

All of this technical work thrives on a stable, supportive foundation. That’s where the project’s governance comes in. The [Steering Committee’s](https://github.com/kubernetes/community/tree/master/committee-steering) role isn’t to issue technical commands; it’s to ensure the project’s overall health, mediate disputes and protect our community values. While the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF) provides a neutral home for our work, the true innovation comes from this collaborative, interconnected network of SIGs and Working Groups.

## **A Decade of Evolution**

All this collaboration has really paid off over the last ten years. Our first job was just to make container orchestration work reliably at scale. Today, we have a platform that’s been battle-hardened by solving the real-world problems of thousands of users and billions of containers.

That solid foundation is exactly why Kubernetes is a great fit for AI. Running large-scale AI and machine learning (ML) workloads pushes every part of the infrastructure to its limit. Our community model was perfectly suited to evolve the platform for this challenge:

## **Portability and Vendor Neutrality**

As Kubernetes becomes the standard for AI, we face the risk of fragmentation, breaking the “run anywhere” promise that makes Kubernetes so great. That would take us right back to the vendor lock-in we all worked so hard to escape.

This is where our community’s immune system kicks in. The [K8s AI Conformance Program](https://github.com/cncf/ai-conformance) is a proactive, community-led initiative to prevent this. It’s our federation of bazaars coming together to create a common set of standards. The goal is to define a certified baseline for what it means to be an “AI-ready” Kubernetes cluster. This ensures that an AI application you build today will run on any conformant Kubernetes distribution tomorrow, whether it’s on premises or in any cloud. It’s our way of ensuring the platform remains a common good, not a collection of walled gardens.

## **The Next Decade**

[Kubernetes’ readiness for the AI era](https://thenewstack.io/kubecon-europe-how-google-will-evolve-kubernetes-in-ai-era/) is no accident. It’s the direct result of a decade of open collaboration, spirited debate and shared ownership. It’s a testament to a model that successfully blends the passion of individual contributors with the strategic investment of companies across the industry.

At [Google](https://cloud.google.com/?utm_content=inline+mention), we are incredibly proud to have been part of this journey from the beginning and to continue to be a major contributor to the upstream project. But Kubernetes’ strength comes from its diversity. It is the sum of all our efforts.

**Top 5 Corporate Contributors to Kubernetes/Kubernetes (All Time)**

|  |  |  |
| --- | --- | --- |
| **Rank** | **Company** | **Total Contributions (Last Decade)** |
| 1 | Google | 1,334,974 |
| 2 | [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) | 527,045 |
| 3 | [VMware](https://tanzu.vmware.com?utm_content=inline+mention) | 361,508 |
| 4 | Microsoft | 246,836 |
| 5 | IBM | 114,501 |

*Source: CNCF DevStats, Kubernetes Project, as of September 2025.*

The platform we have all built together is more than just code. It is a robust, open and ever-evolving foundation for the [next generation of intelligent applications](https://thenewstack.io/whats-next-in-building-better-generative-ai-applications/). I can’t wait to see what we build on it in the next 10 years.

*KubeCon + CloudNativeCon North America 2025 is taking place Nov. 10-13 in Atlanta, Georgia. Register now.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/03/37f09d75-cropped-ab1219c7-antonio-ojea.jpeg)

Antonio Ojea is a software engineer at Google, where he works on Kubernetes. He is one of the top contributors of the Kubernetes project, tech lead in Kubernetes SIG Network & Testing and is an elected member of the Kubernetes...

Read more from Antonio Ojea](https://thenewstack.io/author/antonio-ojea/)