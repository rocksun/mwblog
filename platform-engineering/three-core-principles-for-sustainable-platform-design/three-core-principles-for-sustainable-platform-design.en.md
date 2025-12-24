Platform as a product extends platform engineering beyond a narrow technology solution. Platforms require a shift in the way organizations deliver value. An effective platform gives software teams more time for revenue-focused work by providing highly contextualized tooling in a scalable and sustainable way.

Technology-focused platform designs often solve only part of the wider challenge. To reach the full promise of platforms, organizations must think not only about technology components but also about how they package the experience of providing and consuming managed services that reflect the organization’s standards and constraints.

## **Tests to Apply When Evaluating Platform Design**

Applying [product thinking](https://uxplanet.org/product-thinking-101-1d71a0784f60) makes it clear that a platform should not attempt to solve every use case, nor should it force a single narrow path. Instead, [platform products](https://thenewstack.io/5-lessons-for-building-a-platform-as-a-product/) are a curated set of solutions that encode what is unique to the business but common enough across application teams to be worth sharing.

A practical way to assess platform value is to test how well it can support three essential outcomes:

* **How long does it take a platform consumer to access what they need when they need it?** A platform must enable on-demand access to services and resources. When developers are faced with high numbers of handovers, long waits and other friction, they end up wasting a lot of time and energy or eventually resort to shadow IT.
* **How many people, and how much time, are required to roll out an organization-wide change to a platform capability?** Central owners should be able to upgrade and control every instance through a single action. Without this, environments drift and maintenance creeps toward unmanageable levels.
* **How many people and how much time are required to add a new capability to the platform?** A sustainable platform architecture lets specialists contribute their own capabilities. Platform teams alone cannot maintain all services in areas such as CI, data, AI or networking. Specialists must be able to publish capabilities that pass the first three tests without delay. The platform team’s role is to make this contribution model possible.

## **Technical Principles That Underpin Effective Platforms**

A common mistake in platform design is relying too heavily on current infrastructure and configuration tools. These tools are helpful but not enough to manage complex transitions, diverse systems and the organization’s own processes.

The following three principles repeatedly build platforms that pass the value tests while adapting to changing needs over time.

### Composition Over Simple Abstraction

Abstraction is important because it gives developers a single interface that hides the specifics of underlying tools. When those abstractions are offered as APIs, they decouple the user experience from the implementation. A developer should not need to care whether a capability is implemented with Ansible, Terraform or a mainframe script.

Once consistent API abstractions exist, composition becomes possible. Composition lets capability creators depend on APIs published by others and reuse them without being experts in each domain. Without composition, platforms either duplicate work or centralize too aggressively, slowing the organization’s ability to deliver value to its end customers.

### Encapsulation of Process and Configuration

The choice to “build” within platform engineering, given the options of build, buy or blend, is expensive. This means you should only invest in building what is unique to the organization and valuable across many teams. What makes a company unique is a combination of not only custom infrastructure, configuration and policy, but also any related processes.

Declarative languages such as [Crossplane](https://www.crossplane.io/), [Terraform](https://developer.hashicorp.com/terraform)/[OpenTofu](https://opentofu.org/), Open Policy Agent ([OPA](https://www.openpolicyagent.org/)) and [Kyverno](https://kyverno.io/) have advanced infrastructure, configuration and policy management. Yet imperative actions remain common, especially across cloud provider CLIs, internal systems or environments that lack suitable declarative interfaces. And none of these languages includes processes such as managing longer workflows, offline activities and manual steps, such as approvals, which are core requirements.

A platform must encapsulate infrastructure, configuration, policy and process into a coherent unit. Without this, you cannot safely compose services or rely on them as building blocks. This is because any non-trivial service’s behavior spans multiple tools that cannot be coordinated in lockstep.

It has been said that organizations create processes as the scar tissue of their past pains. This makes any processes particularly unique to an organization and difficult to change and modernize. Systems that do not account for the need to incorporate these business-critical requirements end up adding more complexity than they remove.

Platforms are the one place in your organization where you should fully realise what it means to support a business-compliant solution.

### Decoupled Delivery Optimized for Each Environment

Architecture choices in software shift between central orchestration and distributed choreography. Platforms benefit from both as they need control over when and how a capability is provided, but also need to scale across many clusters and non-Kubernetes locations.

Centralized planning gives control. Decentralized delivery allows scale. A platform should enable the definition of rules and enforcement in a central orchestrator, then rely on distributed deployment engines to deliver the capability in the correct places and form. This avoids the limits of tightly coupled orchestration and reduces the operational burden of scale.

## **Putting Principles Into Practice**

While these principles can be met through many architectures, Kubernetes has emerged as the default control plane for building platforms. A number of cloud native projects have emerged to create a Kubernetes native architecture that supports platforms at scale.

### Composition Behind Custom Resource Definitions (CRDs)

Several tools help manage infrastructure from within Kubernetes. [Crossplane](https://thenewstack.io/cloud-control-planes-for-all-implement-internal-platforms-with-crossplane/) and cloud provider operators have shown how declarative reconciliation can solve drift and scale challenges that earlier Infrastructure as Code (IaC) approaches struggled with.

As more Kubernetes resources appear, the need to compose them grows. Packaging tools such as Helm and Kustomize help, and controller-based solutions extend this further. [Crossplane v2 Compositions](https://docs.crossplane.io/latest/composition/compositions/), [kro ResourceGroupDefinitions](https://kro.run/docs/concepts/rgd/overview) and [Kratix Compound Promises](https://docs.kratix.io/blog/compound-promises) all gather sets of Kubernetes resources behind a single [CRD](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). This forms a clean abstraction for developers.

### Business-Critical Requirement Management Through Custom Controllers

Encapsulation gives capability creators a way to make a single change across configuration, policy and process that can be verified. Declarative tools solve much of the configuration challenge. But enterprise platforms must also support imperative logic due to legacy systems, compliance steps and complex workflows. Intentional packaging can expose a stable API, encode workflow logic and output a deployable unit that downstream systems can manage.

Controller frameworks like [Kubebuilder](https://thenewstack.io/how-to-build-a-kubernetes-operator-from-scratch/) and [Crossplane Providers](https://docs.crossplane.io/latest/packages/providers/) build on low-level [controller runtime](https://github.com/kubernetes-sigs/controller-runtime?tab=readme-ov-file#kubernetes-controller-runtime-project) tools, which let developers embed imperative logic inside operators. Kratix Promises achieve the same outcomes with the often simpler and more accessible interface of Open Container Initiative (OCI)-compliant containers.

### Two-Level GitOps as a Model for Decoupled Delivery

Few real capabilities are deployed using only a single cluster. Platforms need to coordinate deployments across clusters, cloud providers and SaaS systems. Tools such as [KCP](https://www.kcp.io/) and [Karmada](https://karmada.io/) help schedule resources to multiple control planes. Kratix uses a two-tier [GitOps](https://glossary.cncf.io/gitops/) model to route declarative workloads to the correct destination.

## **Achievement Unlocked: Democratized Platform Building**

A Kubernetes-centric architecture built on these principles can meet the tests of on-demand APIs, context-aware solutions and fleet-managed resources. Yet platform sustainability demands that we also consider the cost of maintaining the catalogue of offerings on the platform. This gets to the heart of the third platform test: How many people and how much time are required to add a new capability to the platform?

If all additions must go through a centralized team, either because they are the only ones with permissions or because they are the only ones with the skills to extend the platform, then platform growth is not sustainable. While most can see the issue with a centralized team being the only ones allowed to contribute, the bigger risk is the second blocker: People do not realise they are creating implicit blockers due to the challenge of contributing.

If contributors need to understand too many operator frameworks, workflow engines or domain-specific languages, the platform becomes harder to extend and slows down — often requiring a single centralized team to deliver all new platform capabilities and be a part of updating and extending existing capabilities, even if the architecture allows for independent plugins.

A coherent packaging model that adheres to composability, encapsulation and decoupled delivery allows experts to focus on codifying their expertise rather than on the wiring to make it work with other parts of the ecosystem. [Kratix Promises](https://thenewstack.io/how-cover-whale-scaled-its-developer-platform-beyond-an-mvp/), for example, encapsulate the logic as OCI-compliant containers that can be written in any language when defining a capability, thereby reducing the barrier for specialists.

Three simple quality tests for a platform can uncover a deeper need for a platform design that makes contributions safe and easy, thereby unlocking scale and supporting long-term sustainability.

## **Delivering Lasting Value Over Short-Term Fixes**

When teams can access what they need on demand, when central owners can guide behavior without wrestling with every environment by hand, and when specialists can extend the platform without learning a plethora of tools, the whole system becomes easier to run and easier to evolve.

Strong platforms give engineers time back, reduce operational drag, and turn organizational complexity into something you can manage with confidence rather than fear. A platform built on these principles does more than clear today’s hurdles. It creates the conditions for scale, safe change, and steady contribution across the organization.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/10/3894494a-headshotcncf_square-600x600.jpg)

Abby is a principal engineer at Syntasso delivering Kratix, an open source cloud native framework for building internal platforms on Kubernetes. Her keen interest in supporting internal development comes from over a decade of experience in consulting and product delivery...

Read more from Abby Bangser](https://thenewstack.io/author/abbybangser/)