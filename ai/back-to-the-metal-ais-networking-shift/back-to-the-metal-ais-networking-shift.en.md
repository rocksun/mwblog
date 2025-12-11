For the past decade, [networking](https://thenewstack.io/networking/) has followed the same trajectory as much of IT: abstracting intelligence away from individual devices, centralizing control into software and treating the underlying hardware as largely interchangeable. Software‑defined wide area network (WAN), software‑defined local area network (LAN) and centralized orchestration tools became the norm.

In many ways, this shift delivered exactly what enterprises needed: greater agility, centralized policy control, automation at scale and simplified network operations. The speed of provisioning and the consistency of [policy enforcement across wide geographies](https://thenewstack.io/the-impact-of-regular-training-and-timely-security-policy-changes-on-dev-teams/) changed the way IT teams worked.

But AI is now rewriting those rules. The demands [AI workloads](https://thenewstack.io/how-agentic-ai-is-redefining-campus-and-branch-network-needs/) place on the network — in scale, in latency sensitivity, in security — are more akin to high‑performance computing than traditional business applications. That’s putting the spotlight back on the physical network underlay in ways we haven’t seen in years.

And it’s a change that feels familiar when you look at what’s happening in cloud computing.

## **From Cloud-First to Workload-Right**

When the public cloud first surged in adoption, its benefits were transformative: instant scalability, rapid provisioning, operational freedom from maintaining extensive data center infrastructure and pay‑as‑you‑go economics. Enterprises embraced it as a way to innovate faster and respond to shifting market needs.

But as AI workloads enter the mix, their unique characteristics are influencing [where they run best](https://thenewstack.io/ai-in-network-observability-the-dawn-of-network-intelligence/). Large‑scale model training can generate massive volumes of data, often petabytes, which are more efficiently processed closer to where that data is created or aggregated. Real‑time AI services, such as computer vision in manufacturing or natural‑language assistants in customer service, may benefit from ultra‑low‑latency execution that’s easier to achieve in on‑premises or edge locations. For organizations working with sensitive or regulated data, localizing parts of the workflow can simplify [compliance and governance](https://thenewstack.io/3-steps-cloud-governance-steps-to-avoid-the-next-hack/).

This evolution, often called “cloud repatriation,” isn’t about moving away from cloud, but about intelligently placing workloads where they perform, scale, and comply best. The public cloud remains essential for many AI applications, but it’s now part of a more deliberate hybrid ecosystem, one where some AI workloads or stages of the AI life cycle come closer to purpose‑built [infrastructure to meet performance and efficiency goals](https://thenewstack.io/cios-heed-on-premises-app-and-infrastructure-performance/).

## **Why AI Workloads Break Virtual Comfort Zones**

In traditional enterprise environments, even demanding applications could function well with best‑effort internet bandwidth and latency measured in tens of milliseconds. Under those conditions, software‑defined overlays running on generic forwarding hardware performed admirably.

AI workloads change that equation. Training large models involves sustained, high‑volume data movement between GPU clusters and storage, something that can quickly push virtualized forwarding planes to their throughput limits. While training is typically done in the data center at the core, inference is now starting to move out to the edge and branch locations, bringing new requirements to distributed infrastructure.

Latency becomes mission‑critical, too. AI inference for real‑time analytics, autonomous vehicle coordination or industrial automation may require packet delivery in microseconds, not milliseconds. Deterministic latency — consistent and guaranteed delivery times — must be enforced in hardware.

Security is no less vital. AI data often contains sensitive intellectual property or regulated personal information. Encrypting those high‑throughput streams without cutting performance requires specialized silicon capable of line‑rate processing. And in rugged or industrial environments where AI is often deployed, the hardware itself must be built to endure challenging conditions and sometimes run legacy protocols alongside modern workloads.

## **The Case For AI****‑****Optimized Networking Hardware**

These demands don’t negate the value of software‑defined networking, quite the opposite. Controllers, orchestrators, and overlays have never been more important for shaping policies, automating provisioning, and routing traffic intelligently. But without an AI‑optimized hardware underlay, these systems can become constrained.

Think of it like running an advanced AI model: The orchestration layer might schedule and manage training tasks, but the execution performance comes from GPUs and specialized accelerators that are built for the workload. In networking, that execution muscle comes from AI‑ready physical routers, switches and wireless devices.

These platforms offer ASIC (application-specific integrated circuit)‑based packet forwarding capable of sustaining terabit‑class throughput. They use hardware‑implemented quality‑of‑service and traffic shaping to deliver microsecond latency control. They’re post-quantum ready and handle encryption and inline threat protection without sacrificing speed. And they incorporate telemetry directly into the forwarding plane, enabling operators to monitor and optimize AI data flows in real time.

## **When Software Agility Meets Hardware Muscle**

The goal isn’t to replace software‑defined solutions with hardware‑centric networking, it’s to ensure the underlay can support the complexity and intensity of AI traffic. This is the natural extension of the software‑defined network promise: decoupling control from hardware while still aligning the physical infrastructure with the workload’s performance requirements.

Imagine an SD‑WAN deployment selecting the best path for an AI application, but the path leads to a physical router that can forward encrypted 400‑Gbps flows with no performance drop. Or a software‑defined campus fabric that segments and prioritizes AI inference traffic, enforced by switch silicon that guarantees those microsecond service-level agreements.

The software orchestrates and adapts; the hardware executes at full AI demand.

## **Architecting for AI: A Hybrid Approach to Networking**

As AI moves from pilots to production, networking strategies will follow the pattern cloud infrastructure has taken, becoming more deliberate and workload‑aware. Hardware refresh cycles will shorten to keep pace with advances in routing and switching silicon, and next-generation security including quantum-resistant algorithms will ensure verified access, starting at the device level. Network design decisions will explicitly consider AI workload placement, just as cloud architects now choose whether code runs in cloud, edge or on‑premises.

The industry direction is clear: The most robust AI networks will integrate software‑defined agility with AI‑optimized hardware performance. That combination will enable the infrastructure to match the unprecedented scale, security and latency requirements of AI, from the cloud core, through the WAN, to the ruggedized edge.

AI is triggering networking’s own form of “repatriation thinking,” not a return to the past, but a recalibration for the future. Just as cloud strategies have evolved to place workloads where they run best, AI demands a balance between the flexibility of software‑defined networking and the raw, predictable capability of purpose‑built hardware. Getting this balance right will be what allows enterprises to fully realize the potential of AI.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/ddf14f4b-cropped-8e141faf-lee-peterson.jpeg)

As the vice president of Product Management for the Secure WAN product portfolio at Cisco, Lee Peterson leads product strategy, development and roadmap for the company’s multibillion-dollar enterprise routing portfolio. With more than 20 years of experience in telecommunications and...

Read more from Lee Peterson](https://thenewstack.io/author/lee-peterson/)