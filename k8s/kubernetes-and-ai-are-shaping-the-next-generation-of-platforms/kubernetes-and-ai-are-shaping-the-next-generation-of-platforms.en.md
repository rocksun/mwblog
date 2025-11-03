Platform engineering has emerged as one of the most significant shifts in the cloud native ecosystem. Teams everywhere are adopting [internal developer platforms](https://thenewstack.io/platform-engineering-face-off-to-idp-or-not-to-idp/) (IDPs) to reduce complexity, accelerate delivery and give developers a consistent “[golden path](https://thenewstack.io/heres-one-golden-path-to-build-an-mvp-enterprise-idp/)” to production.

But IDPs are only part of the story. Kubernetes has become the standard control plane for running applications. [Crossplane](https://www.crossplane.io/) builds on that foundation to extend control outward, from cloud resources to anything with an API, making the idea of a universal control plane possible.

Alongside projects like [Backstage](https://backstage.io/), [Argo CD](https://argoproj.github.io/cd/) and [Kyverno](https://kyverno.io/), this shift is shaping a new generation of platforms that unify infrastructure, developer experience, delivery and policy. This is becoming the foundation for the next phase of [platform engineering](https://thenewstack.io/platform-engineering/), one where AI is not just writing code, but also helping operate infrastructure.

## **Kubernetes: The API for Platforms**

[Kubernetes](https://thenewstack.io/kubernetes-complexity-realigns-platform-engineering-strategy/) started as a way to orchestrate containers, but its true innovation lies in its API model. The declarative resource pattern, with its desired state, actual state and continuous reconciliation, has proven to be a universal abstraction. It works for workloads, infrastructure, policies and more.

That universality is why Kubernetes has become the foundation for IDPs. It provides a consistent way to define, extend and enforce platform building blocks. Whether you’re provisioning a cloud database, managing a network policy or applying compliance rules, Kubernetes APIs make platforms programmable, predictable and composable.

This API-first foundation also makes Kubernetes uniquely ready for the AI era. Agents and large language models (LLMs) don’t navigate dashboards or tribal knowledge; they interact with APIs. And Kubernetes offers a consistent, structured interface designed from Day 1 for machine-to-machine communication.

## **The Evolution of Platform APIs**

As AI moves into operations, we’re starting to see platform APIs evolve. Instead of rigid, predefined interfaces, APIs are becoming more dynamic and discoverable. Think of them less like static contracts and more like models that can be explored, queried and guided.

This shift could radically simplify the way developers consume platforms. Instead of memorizing YAML schemas or reading through long docs, they could interact conversationally with an agent that understands both the platform’s APIs and the organization’s rules.

## **Beyond IDPs: Toward Adaptive Platforms**

So, where does this leave platform engineering?

* **IDPs** are the here and now: Consolidating best practices, enforcing consistency and improving developer experience.
* **Kubernetes** is the bedrock: A universal control plane that standardizes how platforms are expressed and consumed.
* **AI-driven APIs** point to what’s next: Platforms that can guide, adapt and even learn from their own operations.

These trends suggest a future where platforms are not just tools for automation, but active partners for both humans and agents. A recent paper on [Intelligent Control Planes](https://mkto.upbound.io/rs/975-TPU-636/images/The%20Intelligent%20Control%20Plane%20-%20Towards%20Autonomous%20Infrastructure.pdf?version=0&utm_campaign=2025_Q3_8.5_GBL_FEV_UXP2-Launch&utm_medium=blog&utm_source=corporate-event) explores this vision further, outlining how unifying state, policy, knowledge and intelligence could enable platforms that learn and adapt over time. Instead of developers stitching together scripts and runbooks, the platform itself could provide context, recommend solutions and continuously optimize.

That doesn’t mean replacing engineers. It means freeing them from repetitive toil so they can focus on higher-value work.

IDPs give us the golden paths we need today. But in the era of AI, platforms will also need to become adaptive, context-aware and capable of serving both humans and machines. The future of platform engineering isn’t just about automation — it’s about intelligence.

## **Join the Conversation**

At KubeCon + CloudNativeCon North America 2025, we invite you to attend our sessions to explore both the present and the future of platform engineering:

*KubeCon + CloudNativeCon North America 2025 is taking place Nov. 10-13 in Atlanta, Georgia.* [*Register now*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/02/b08c2c68-cropped-94595a98-ana-margarita-medina2.jpg)

Ana Margarita Medina is a staff developer advocate at Upbound where she speaks on all things site reliability engineering, DevOps and reliability. She is a self-taught engineer with over 14 years of experience, focusing on cloud infrastructure and reliability in...

Read more from Ana Margarita Medina](https://thenewstack.io/author/ana-margarita-medina/)

[![](https://cdn.thenewstack.io/media/2023/06/9ffa2925-cropped-e0bb2067-viktor-farcic.jpg)

Viktor Farcic is a developer advocate at Upbound, a member of the Google Developer Experts, CDF Ambassadors, and GitHub Stars groups, and a published author. He is a host of the YouTube channel "DevOps Toolkit" and a co-host of “DevOps...

Read more from Viktor Farcic](https://thenewstack.io/author/viktor-farcic/)