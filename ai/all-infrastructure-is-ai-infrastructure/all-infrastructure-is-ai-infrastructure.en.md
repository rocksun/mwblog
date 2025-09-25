In the very near future, all technology infrastructure will effectively be AI infrastructure. This is not hyperbole. As enterprises scale their use of generative AI models and autonomous agents, every layer of the technology stack — from silicon to orchestration — will be reshaped to support AI workloads.

This transition is another disruption following the move from physical data centers to [cloud computing](https://thenewstack.io/cloud-native/). Within a few years, large segments of conventional application space may disappear, replaced by AI-driven systems and workflows designed, and perhaps modified in real time, by [AI itself](https://thenewstack.io/ai-engineering/).

## **Why AI Infrastructure Breaks the Old Playbook**

The history of cloud computing was defined by abstraction. Virtualization, [containers](https://thenewstack.io/containers/), [APIs](https://thenewstack.io/api-management/) and [orchestration engines](https://thenewstack.io/orchestration-is-your-secret-weapon-for-smoother-workflows/) made lower layers — hardware, operating systems — progressively invisible.

AI workloads reverse this trend. Performance at scale depends directly on the hardware and fabrics underneath. Training and inference workloads are bound tightly to CPUs, GPUs, memory and the network. Instead of hiding complexity, AI brings it to the surface.

This creates a paradox: The faster AI adoption grows, the more enterprises must understand and optimize their hardware and infrastructure in meticulous detail. The promise of “serverless” simplicity vanishes when platform engineers must confront NUMA (non-uniform memory access ) nodes, PCI (peripheral component interconnect) lanes or GPU interconnects just to achieve usable throughput.

## **The New Stack Complexity**

At the heart of this transformation is the relationship between CPUs and GPUs. GPUs are the engines of AI, but they cannot operate in isolation. CPUs feed data pipelines, handle preprocessing and manage scheduling. In many cases, jobs run better on CPUs as part of a coordinated pipeline than on GPUs alone. Scaling models means orchestrating these resources holistically, not as independent silos.

Networking is equally critical. Four distinct fabrics shape AI infrastructure: data networks for east-west and north-south flows; wide-area networks to connect regions; PCI interconnects between devices; and RDMA (remote direct memory access) networks for ultra-low-latency GPU clusters. Each fabric must be accounted for when building out AI infrastructure, right down to the storage layer.

Scarcity compounds the challenge. GPUs are short in supply, but the real bottlenecks extend to data center power and physical space. One Mirantis partner consumes 100% of its available power budget while occupying only 20% of its facility’s floor space. The rules for designing data centers are being rewritten under AI’s demands — more power per rack, higher cooling requirements and longer lead times for equipment.

## **Governance and Sovereignty**

AI workloads introduce sovereignty concerns that traditional applications rarely encounter. Data locality requirements, legal and regulatory controls, and cross-border compliance frameworks such as the EU’s [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) or [Digital Operational Resilience Act (DORA)](https://en.wikipedia.org/wiki/Digital_Operational_Resilience_Act) place new constraints on where and how models run.

Enterprises must ensure not just availability and performance, but also provable governance of every agent, model and tool they deploy. Sovereignty is simultaneously geographic, legal and operational. Multitenancy adds another dimension, requiring strict isolation between workloads that may span teams, divisions or even partner organizations.

## **Developers and the Abstraction Gap**

The developers creating AI applications do not want to manage the minutiae of interconnects, fabrics and hardware pipelines.

The solution is not to push complexity onto developers, but to design platforms that hide infrastructure detail while ensuring control, security and performance at scale.

## **Building Blocks of AI Infrastructure**

AI infrastructure can be understood as four interdependent layers.

1. **Workloads**: The top layer is the workload itself — training, fine-tuning, inference or agent orchestration. While large-scale training evokes thousands of GPUs tied together, fine-tuning or small-model inference may require only a handful. Flexibility to handle both extremes is essential.
2. **Developer experience**: Next is the layer of usability. Developers require consistency: Models should run with predictable performance without excessive manual tuning. They need access to training resources, inference environments and GPU partitioning capabilities as older devices reach end of life. This layer is where self-service portals, APIs and catalogs make AI accessible across organizations.
3. **Infrastructure as a service**: Beneath workloads and experience is the raw infrastructure, whether on-premises, in the cloud or at the edge.
4. **Management and observability**: The foundation is the management plane, the layer that provisions, monitors, and optimizes everything above it. It must separate control from data so failures in management do not disrupt workloads. It must provide repeatability through templates, observability at every layer and flexibility to swap vendors, frameworks or fabrics as needed. This is where enterprises win or lose sovereignty.

## **Strategic Imperatives for Platforms**

What principles should guide the next generation of AI infrastructure platforms? Several imperatives stand out.

* **Manageability**: Platforms cannot be hand-built and brittle. They must support full life cycle upgrades and continuous improvement over time.
* **Observability**: Every layer — from GPU utilization to application response — must be instrumented. Performance is not optional; it is a hard requirement.
* **Flexibility**: Enterprises must retain the ability to change layers of the stack as vendors evolve, avoiding lock-in. Infrastructure should adapt without wholesale rewrites.
* **Repeatability**: Templates and declarative patterns capture known-good architectures, reducing complexity and eliminating wasted reinvention.
* **Borderless Computing**: Resources must be locatable and usable across data center, cloud and edge, secured and observable wherever they run.
* **Contracts for Resources**: Instead of abstracting hardware away, workloads should declare performance requirements and receive guaranteed contracts. This flips abstraction into assurance: Applications request what they need, and infrastructure responds predictably.

These imperatives collectively define what strategic, open infrastructure must become: composable, observable and responsive to the realities of AI workloads.

## **Open Source as the Path Forward**

Rapid time to value is a critical business requirement. Enterprises that invest in AI infrastructure cannot afford to wait months for return. Vendor stacks promise expedience by bundling everything into a closed ecosystem. But that expedience comes at a cost: Innovation is gated by the vendor’s roadmap, and flexibility is sacrificed.

An open source approach offers the alternative. Composable infrastructure, built on declarative patterns, ensures that platforms evolve with the ecosystem. Templates provide repeatability. Contracts provide guarantees. Borderless computing allows resources to be found and secured wherever they exist. Enterprises control their own destinies, rather than waiting for monolithic platforms to adapt.

This is the vision guiding Mirantis as we build [k0rdent](https://k0rdent.io/), an open source platform designed from the ground up to support AI workloads. K0rdent is multicloud, multicluster, and bare-metal aware. It uses a pattern-based solution to provide declarative AI infrastructure orchestration. And it positions enterprises to move from vague abstractions toward explicit contracts for performance. By doing so, it enables organizations to run workloads where they want, how they want, with full observability and sovereignty.

## **Conclusion**

All infrastructure is becoming AI infrastructure. The shift will be as dramatic as the rise of cloud, but more complex, more resource-constrained and more sovereignty-sensitive. Enterprises that succeed will embrace manageability, observability, flexibility and openness. They will design for scarcity and sovereignty. And they will adopt platforms that provide contracts for performance rather than illusions of abstraction.

AI will not wait for the industry to stabilize. Organizations must decide now whether to lock themselves into closed ecosystems or to embrace strategic, open infrastructure. We believe the choice is clear: The future belongs to those who can harness AI safely, at scale, on infrastructure they control.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/01/9a973c77-shaun-omeara-600x600.jpg)

Shaun O’Meara, global field CTO at Mirantis, has worked with customers designing and building enterprise IT infrastructure for 20 years.

Read more from Shaun O'Meara](https://thenewstack.io/author/shaun-omeara/)