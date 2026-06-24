Inference is now the dominant force in enterprise AI — and with it has come an inconvenient reality: Data is almost always transported to compute. Every inference call moves sensitive enterprise information out of the systems where it lives and into external environments optimized for GPU throughput rather than data governance. This creates friction that compounds at scale: rising costs, expanding security exposure, and a growing tangle of data copies that drift out of sync with operational reality.

What enterprises actually want is different: to keep data and IP intact within the database rather than creating multiple copies and managing the resulting inconsistencies.

[Research](https://www.enterprisedb.com/sovereignty-matters) across more than 2,050 senior executives from major enterprises worldwide suggests that 95% of organizations intend to become their own AI and data platforms within the next 780 working days. Yet only 13% have successfully reached that goal. The organizations that have succeeded are achieving almost five times the return on investment of those still struggling to operationalize AI.

**What separates the leaders from the followers is not model quality. It is infrastructure strategy.**

The most successful organizations have adopted a sovereign-by-design approach. More than 75% are operating across multiple clouds and on-premises environments rather than relying on a single hyperscale provider. They are building AI around their own business, regulatory, and operational requirements rather than adapting those requirements to fit a cloud vendor’s architecture.

As AI moves from experimentation into production, CIOs are discovering that training models is relatively easy. Running them efficiently, securely and compliantly across thousands of operational workloads is where the real challenge begins.

## The shift from training to inference

Training is a discrete event. Inference is an ongoing business process.

A model may be trained once, but it could be called millions of times each day. Every fraud assessment, insurance claim review, customer service interaction, medical recommendation, sanctions check, or predictive maintenance event relies on inference occurring against live operational data.

> “What separates the leaders from the followers is not model quality. It is infrastructure strategy.”

This distinction fundamentally changes enterprise infrastructure requirements.

Training workloads prioritize compute density and GPU availability. Inference workloads prioritize latency, governance, reliability and cost control. They must operate where business data resides and where compliance requirements can be enforced.

For heavily regulated industries such as financial services, healthcare, telecommunications, energy and the public sector, inference cannot simply occur in whichever region offers the lowest compute cost. Data sovereignty requirements, audit obligations and security mandates often dictate exactly where workloads must execute.

The challenge therefore becomes much larger than AI itself. Organizations need an operating model capable of bringing together compute, data and governance without sacrificing flexibility.

## Why neoclouds are emerging as a critical layer to cross the chasm to production

This is where neoclouds have become increasingly important.

Unlike traditional hyperscalers, [neoclouds are purpose-built](https://thenewstack.io/why-neoclouds-are-the-answer-to-ai-storage-lock-in/) around AI infrastructure. Their focus is not delivering hundreds of generic cloud services but rather optimizing for GPU access, AI performance, and flexible consumption models.

For many enterprises, neoclouds offer a compelling answer to the growing demand for specialized AI compute. They provide access to the latest accelerator technologies while enabling organizations to scale workloads without the complexity often associated with large cloud environments.

> “The future of AI architecture therefore depends on bringing models closer to data rather than moving data closer to models.”

However, neoclouds solve only one part of the enterprise AI equation.

AI does not create value in isolation. Models require context. They need access to customer records, transaction histories, operational workflows, policy documents, supply chain information and enterprise knowledge. Moving these assets into separate AI environments creates duplication, latency and governance challenges.

The future of AI architecture therefore depends on bringing models closer to data rather than moving data closer to models.

## Why Postgres has become the enterprise AI foundation

As organizations look for a common platform that supports both operational and AI workloads, [Postgres](https://www.enterprisedb.com/company/postgres-vitality-index) has emerged as a natural foundation.

Postgres already serves as the operational backbone for many of the world’s most important applications. It combines transactional reliability, extensibility, and scalability with the openness that enterprises increasingly demand. 70%+ of AI-related application development is happening on Postgres.

What makes Postgres particularly relevant in the AI era is [its ability to become more than a database](https://thenewstack.io/postgres-ai-ground-truth/). It can serve as a governed memory layer for AI systems, integrating operational data, application context, permissions, observability, and retrieval capabilities into a single architecture.

This dramatically reduces complexity.

Instead of maintaining separate infrastructures for transactional systems, vector stores, AI memory layers, and governance frameworks, organizations can consolidate around a trusted operational platform that already supports their mission-critical workloads.

For CIOs seeking to balance innovation with control, this architectural simplification represents a significant strategic advantage.

## Why sovereignty matters more than ever

[Sovereignty](https://www.enterprisedb.com/what-is-sovereign-ai-data-sovereignty) has become one of the defining themes of enterprise technology.

For banks, sovereignty means maintaining control over financial data and regulatory obligations. For healthcare organizations, it means protecting patient information while enabling innovation. For governments, it means ensuring national and citizen data remains under appropriate jurisdictional control.

**The rise of AI has amplified these concerns.**

Organizations increasingly need assurance that models, data, policies and operational controls can remain within designated environments while still benefiting from advances in AI technology.

This requirement is driving demand for [sovereign AI](https://www.enterprisedb.com/use-case/sovereign-ai) architectures capable of operating across clouds, private infrastructure and on-premises environments.

The challenge is creating consistency across these environments without introducing operational complexity.

## EDB Postgres AI: connecting sovereign data and sovereign AI

[EDB Postgres AI](https://www.enterprisedb.com/products/edb-postgres-ai) addresses this challenge by bringing together operational Postgres, AI capabilities and hybrid infrastructure management into a unified platform.

Rather than forcing enterprises to choose between innovation and control, EDB Postgres AI enables organizations to deploy AI where their data already resides. Through capabilities spanning operational databases, analytics, agentic AI workloads and hybrid management, organizations can create a consistent operating model across sovereign environments.

This approach is particularly relevant for regulated industries where moving sensitive information into external AI services may introduce compliance, security or governance concerns.

By enabling inference close to operational data, organizations reduce data movement, improve performance, and strengthen their compliance posture. At the same time, they maintain the flexibility required to leverage emerging AI technologies and modern infrastructure models.

> “By enabling inference close to operational data, organizations reduce data movement, improve performance, and strengthen their compliance posture.”

The result is a platform that aligns with the realities of enterprise AI rather than the assumptions of consumer AI.

*“The reality is that the new AI at scale world needs a new infrastructure. That isn’t just the compute; it’s the governance, heuristic data access and level of observational and orchestration control that are absolute, governed, agile and work for humans and agents.”*  Nancy Hensley, CPO, EDB

## The new enterprise AI stack

The emerging enterprise AI architecture is increasingly built around complementary rather than competing technologies.

| Infrastructure layer | Primary role | Strategic value |
| --- | --- | --- |
| Neoclouds | Specialized AI compute and GPU infrastructure | Access to cutting-edge AI acceleration and flexible scaling |
| Public Hyperscalers | Broad cloud services and global reach | Ecosystem breadth and service diversity |
| Postgres | Operational data foundation | Trusted, governed and scalable enterprise data platform |
| EDB Postgres AI | Sovereign AI and hybrid management layer | Enables AI, analytics and operational workloads to run consistently across sovereign environments |
| Enterprise Governance | Security, compliance and [policy controls](https://thenewstack.io/how-to-create-an-effective-ai-usage-policy/) | Ensures AI aligns with regulatory and business requirements |

Together, these layers create an architecture capable of supporting the complete AI lifecycle—from experimentation and model training through production inference and continuous optimization.

## The CIO imperative

The organizations realizing the greatest value from AI are no longer asking how to train better models. They are asking how to operationalize AI across the enterprise while maintaining control over cost, governance, and risk.

Their answer is increasingly consistent.

They are adopting multi-cloud and hybrid strategies rather than relying on a single cloud. They are prioritizing sovereign architectures rather than centralized data movement. They are building around open operational foundations rather than proprietary lock-in. Most importantly, they are recognizing that AI success depends on bringing intelligence to data, not data to intelligence.

Neoclouds provide the compute layer required for modern AI. Postgres provides the operational foundation required for trusted enterprise systems. EDB Postgres AI connects these worlds through a sovereign architecture designed for the realities of regulated industries.

As AI transitions from experimentation to operational necessity, the winning enterprises will be those that can make inference secure, governed, low-latency, and economically sustainable at scale.

**In the next era of enterprise AI, the greatest business value will not come from model selection or raw GPU access. It will come from infrastructure strategy built around data — keeping intelligence close to where data already lives, governed, trusted, and ready to act.**

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/06/5eca8c28-maxromanenko.png)

Max Romanenko is Chief Engineering Officer at EDB with deep expertise across cloud infrastructure, AI, and enterprise SaaS. Previously, he built and scaled large global engineering organizations, launching major public cloud services and modernizing healthcare platforms for organizations across the...

Read more from Max Romanenko](https://thenewstack.io/author/max-romanenko/)