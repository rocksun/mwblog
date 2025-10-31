Cloud native was once about packaging applications into containers and deploying them fast. Today, it’s about supporting everything from microservices to Software as a Service platforms to AI inferencing on infrastructure that must be performant, scalable and cost-efficient.

But here lies the challenge: Developers don’t have the luxury of choosing the [infrastructure](https://thenewstack.io/all-infrastructure-is-ai-infrastructure/) where their apps will run. They need to code once and trust the underlying deployment platform to run workloads wherever it makes sense. The answer comes in the form of best practices around multi-architecture support in [Kubernetes](https://thenewstack.io/kubernetes/) and the availability of [cloud native software ecosystem](https://thenewstack.io/cloud-native/) across all major cloud providers.

## Why Multiple Clouds and Architectures Matter

For years, containerization promised “build once, run anywhere” portability. In practice, most teams defaulted to a single processor architecture hosted by a single cloud provider. That’s changing quickly.

Multi-architecture builds are now becoming the golden standard across the industry. Containers, registries and orchestration platforms all support them natively, meaning developers can produce a single image that runs across x86 and Arm-based processors. For their part, IT organizations are increasingly running these apps in multicloud setups, balancing workloads across providers to reduce risk, comply with regulations and optimize costs.

This shift matters because it gives developers freedom to tap into new classes of infrastructure without rewriting code or maintaining multiple pipelines, and for IT practitioners, it means application portability with better operational efficiency, improved total cost of ownership (TCO) and vendor choice.

[![](https://cdn.thenewstack.io/media/2025/10/12cd536d-image1-1024x575.png)](https://cdn.thenewstack.io/media/2025/10/12cd536d-image1-1024x575.png)

Today, [cloud native isn’t just about speed](https://thenewstack.io/why-its-next-challenge-isnt-in-the-cloud/); it’s also about the flexibility and predictability of application deployments in a rapidly evolving infrastructure landscape. Kubernetes is a great platform for deploying portable applications as it can schedule containers onto nodes that match the architecture, hiding infrastructure complexities and efficiently landing an application on the best node, whether it is x86 or Arm.

## Preparing for Cloud Native and AI Convergence

Cloud native principles — portability, elasticity, automation — were built for [microservices and web apps](https://thenewstack.io/how-to-build-a-roadmap-to-app-modernization/). But as AI becomes central to nearly every product, those same principles are now being applied to machine learning (ML) pipelines and inference workloads.

Developers are already seeing this convergence, and the intersection of cloud native and AI creates some of the most compelling use cases for multi-architecture:

* **Retrieval-Augmented Generation (RAG):** Arm-based CPUs efficiently handle vector search and preprocessing tasks compared to legacy architectures.
* **Embedded inference in microservices:** Smaller models run natively on Arm-based CPUs, cutting costs and reducing energy use.
* **Elastic scaling:** Kubernetes lets workloads burst onto GPUs when needed, then settle back on Arm-based CPUs for ongoing tasks.

For many developers, multicloud and multi-architecture are no longer abstract concepts. They’re the day-to-day reality shaping how applications are built, deployed, and scaled. This is how they future-proof their efforts:

* **Ensure every build supports multiple architectures and cloud providers.**
* **Build apps using interpreted languages:** Python, Java and R are good choices.
* **Lean on abstraction:** Let Kubernetes and managed services handle complexity while you focus on application logic. Workloads need to be matched to the right compute and cloud provider to reduce costs, making sustainability a built-in outcome.
* **Prioritize efficiency:** Recognize that price-performance and energy-per-task are as critical as speed.

These straightforward concepts are natural extensions of cloud native principles, and as AI and cloud native continue to converge, they could help developers to be more productive and simplify app delivery in the years ahead.

## Future-Proofing Your Applications

Arm is helping developers and infrastructure teams adapt to this new paradigm by ensuring that the entire ecosystem is ready for multicloud and multi-architecture deployments.

Take Google Cloud’s Axion processors, powered by Arm Neoverse technology, as an example. Axion is designed for the workloads developers care about most, such as cloud native services, data-intensive pipelines and small-to-medium-scale AI inference.

But the key to success isn’t just performance; it’s the sum of all ingredients. From Axion being a first-class option in Google Kubernetes Engine and Compute Engine to seamless support across container tooling, observability platforms, and CI/CD pipelines, developers can run workloads on Axion-backed instances using the same Kubernetes manifests and cloud APIs they already use. No new tooling, no separate pipelines, no forks or separate code paths are needed. Just more efficient compute available through familiar Kubernetes APIs. Developers stay focused on implementing services and adding new features, while the platform and runtime optimize execution under the hood.

The future of cloud native and AI application development is no longer just about bigger or faster compute; it’s about offering developers infrastructure choice while ensuring longevity for their applications.

With Kubernetes, multi-architecture builds and processors like Google Cloud’s Axion, developers can deliver applications that are portable, performant and sustainable.

*The* [*Arm Cloud Migration*](https://www.arm.com/markets/computing-infrastructure/arm-cloud-migration) *program provides a clear, low-risk path to adopt and optimize workloads on Arm-based infrastructure in the cloud.**If you’re attending KubeCon + CloudNativeCon North America 2025, stop by the Arm booth #231 to learn more. And don’t miss the “*[*Building Multi-Architecture Cloud-Native Applications and Scalable AI Inference on Google Axion with Kubernetes*](https://events.arm.com/kubecon25northamerica)*” workshop jointly hosted by Arm and Google Cloud, noon-5 p.m. on Nov.10.*

*KubeCon + CloudNativeCon North America 2025 is taking place Nov. 10-13 in Atlanta, Georgia. [Register now](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/10/a56c0a66-cropped-fbad4227-yan-fisher.jpeg)

Yan Fisher is a director of software ecosystem at Arm, with 25 years of experience in the computer industry and a deep background in systems design and architecture. Having honed his expertise at companies like Sun Microsystems, Oracle and Red...

Read more from Yan Fisher](https://thenewstack.io/author/yan-fisher/)