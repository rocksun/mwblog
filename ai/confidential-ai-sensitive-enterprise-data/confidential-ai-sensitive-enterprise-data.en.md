**Most people already understand what generative AI can do.** But enterprises run into problems when they need to give a model access to information that cannot leave their own environment, such as a patient record, a customer’s financial details, or a company’s most valuable intellectual property.

Sending that data to a cloud or SaaS service means it crosses external networks and is processed on infrastructure run by another organization, creating additional concerns about control, accountability, and exposure. That’s where AI enthusiasm collides with production realities. Despite its productivity potential, enterprise AI still faces a fundamental gap in trust and control.

Organizations need to know whether a system will expose information it should protect, act as intended, meet security and performance requirements, and behave safely at machine speed.

[**Alon Horev**](http://linkedin.com/in/alonhorev?originalSubdomain=il), CTO and co-founder of AI operating system company [**VAST Data**](https://www.vastdata.com/?utm_medium=paiddigital&utm_source=tns&utm_campaign=Q327-Global-ADOP-MUC-UnboundedLaunch), tells *The New Stack* that the challenge is particularly acute when AI systems handle sensitive customer information. “Even if you ask the model today to obfuscate a conversation or redact PII from a conversation, it’s hard to have 100% confidence that’s the case, and that it worked.”

> “Even if you ask the model today to obfuscate a conversation or redact PII from a conversation, it’s hard to have 100% confidence that’s the case, and that it worked.”

Consider a customer support agent that needs access to an individual’s profile to provide a useful, personalized answer. The organization must ensure that information isn’t exposed to another customer, while also considering whether those conversations can be used for training or system improvement. They might contain personally identifiable information (PII) or other protected details, and the consequences of mishandling them ultimately fall on the organization and the people whose information it holds.

Confidential AI architectures: solving a two-sided trust problem

Enterprise AI has two parties to satisfy: organizations must keep sensitive data under their control, while model builders need to protect the weights and software that represent substantial investments in research, engineering, and IP. They’re understandably reluctant to place those assets in environments where customers, infrastructure operators, or attackers might gain access. That mutual need for control has created a stalemate. How can organizations bring advanced models to sensitive data without asking either side to surrender control?

Horev has seen that the most capable models are increasingly delivered as SaaS services, because that’s the simplest way for their creators to distribute and protect them. Even when a provider offers compliance controls, the enterprise might still shoulder the consequences of a breach, misuse, or regulatory violation. Sending information across the WAN also places it in the hands of more systems, connections, and operators, increasing the number of points that must be trusted and governed. Organizations may also be unwilling, or legally unable, to rely on a provider’s assurances that it will not retain, reuse, or expose their data beyond the intended service.

For organizations in regulated or data sovereignty-sensitive sectors, that could be an unacceptable trade-off. “Naturally, many organizations are adopting a hybrid strategy,” Horev tells *The New Stack*. “Some applications and datasets can go to the cloud, while others must remain on-premises, sometimes even in the building, or in the country.”  
  
This is where confidential AI comes in. Encryption at rest and in transit protects data while it’s stored or moving between systems. Confidential computing extends that protection into the processing environment, using hardware-isolated execution to create a protected enclave in which the data and model weights can remain encrypted until they’re released to an approved workload.

Cryptographic attestation verifies the hardware, virtual machine (VM), software, and configuration requesting access before releasing keys. The model builder can encrypt its model using the public key of a specific confidential VM. Only that VM’s corresponding private key can decrypt it within protected memory, enabling the customer to use the model without accessing its weights.

Independent key control preserves the separation between the two sides. The enterprise retains control of the keys governing its data, while the model builder retains control of the keys governing its model. While the workload is running, the infrastructure operator doesn’t control either set of keys.

As AI becomes more agentic, those controls will matter more. Agents will need to access more data, systems and tools, and might act on that information with far less human intervention.

> “This world of agentic AI is moving extremely fast, and we need to limit what an agent can see and do.”

Those that can’t establish strong privacy and governance assurances for today’s models will find it even harder to deploy agents safely in the future. “This world of agentic AI is moving extremely fast, and we need to limit what an agent can see and do,” Horev tells *The New Stack*.

## From architecture to ecosystem

Many businesses simply cannot manage the integration, security, and maintenance of the entire AI stack, because it requires working separately with each model provider to engineer something that suits both parties. Turning confidential AI architecture into something organizations can deploy is the challenge [VAST DataEnclave](https://www.vastdata.com/platform/dataengine?utm_medium=paiddigital&utm_source=tns&utm_campaign=Q327-Global-ADOP-MUC-UnboundedLaunch), which was [launched on September 22](https://www.vastdata.com/press-releases/vast-data-introduces-dataenclave-to-bring-leading-ai-models-and-enterprise-data-together-on-trusted-infrastructure?utm_medium=paiddigital&utm_source=tns&utm_campaign=Q327-Global-ADOP-MUC-UnboundedLaunch), intends to address.

As a capability of the **VAST** [**AI Operating System**](https://www.vastdata.com/platform/ai-os?utm_medium=paiddigital&utm_source=tns&utm_campaign=Q327-Global-ADOP-MUC-UnboundedLaunch), the goal is to bring the model, application layer, and data platform together under customer-controlled operating conditions. The architecture is designed to protect both sides of the equation: the enterprise’s data and the model builder’s weights. The customer retains control of its infrastructure and data keys, while the model provider can make its software available without handing over the underlying intellectual property.

“We’re trying to close the trust and control gap by working with world-class model builders such as Cohere, Deepgram, Factory, Fundamental and TwelveLabs, who continue to innovate and build their expertise,” says Horev. The ecosystem also includes infrastructure and security providers such as Nvidia, CrowdStrike, Fortanix, Nscale, Cisco, and Supermicro. The range reflects the practical challenge: confidential AI needs more than a protected GPU. It requires models, applications, accelerated hardware, data infrastructure, and operational support to work together.

That control also changes the cost conversation, without automatically making AI cheaper. Hosted models can make budgets harder to predict as token consumption varies with usage patterns, agent loops, model architecture, and workload volume. Customer-controlled infrastructure gives enterprises a more defined capacity and cost base: they can plan around GPU clusters they own or have already budgeted for, instead of allowing inefficient model choices or uncontrolled agent activity to generate an open-ended token bill.

> “…instead of allowing inefficient model choices or uncontrolled agent activity to generate an open-ended token bill.”

The cluster also imposes a natural ceiling on throughput, which helps organizations understand how much work their infrastructure can handle within a given period. Model providers can then price access by token, task, or license, while the enterprise retains greater visibility into its total operating cost.

## Why the data platform is paramount

Confidential AI protects data and model weights during inference, but it’s only part of the production challenge. Real-world AI systems are living environments in which data moves between storage, databases, GPUs, networks, applications, and agents.

That’s why confidential AI can’t be bolted onto a fragmented stack. Businesses need to protect the model, the data, and the infrastructure connecting them as one system. As Horev says: “You need to build security in multiple layers of the platform,” with someone accountable for rapidly updating compromised components.

Confidentiality is only useful if the resulting system can also be operated, monitored, and improved. As AI infrastructure becomes more distributed, it becomes harder to tell what’s happening when something goes wrong and where the fault lies.

Horev recommends a “single pane of glass” across storage, networking, and compute, so teams can see what’s happening and keep resolution times low. If a network port is intermittently failing in a data center, for example, an agent could help identify the root cause, provided it has access to the right operational data and tightly controlled permissions. Those permissions should govern the infrastructure it can inspect, the data it can retrieve, and the actions it can take.

The same applies to monitoring AI workloads. Teams need visibility into performance, failures, and access patterns without exposing the customer data or model weights. Agent sandboxes can limit the systems and tools an agent can reach, while data platform observability can log which data it accessed, what it did with that data, and how it interacted with downstream systems.

Evaluation, therefore, becomes part of production discipline. Teams must observe systems, measure behavior, govern access, and manage change in ways that demonstrate progress. Confidentiality, data-level policy, observability and correctness have to work together.

The emerging ecosystem suggests demand for models that can run securely under customer control, wherever sensitive data resides. These are “living systems,” says Horev. “It’s not just leveraging a feature inside of a wider platform.”

***Visit the*** [***VAST Data Confidential AI solution page***](https://www.vastdata.com/lp/confidential-ai?utm_medium=paiddigital&utm_source=tns&utm_campaign=Q327-Global-ADOP-MUC-UnboundedLaunch) ***to learn more about the architecture, ecosystem, and availability.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/e36dae7b-cropped-6c610b3e-megan-carnegie-square-sizing-600x600.jpg)

Megan is a London-based independent technology journalist with over a decade of experience writing analytical features for publications like WIRED, Fast Company, and the BBC. She specializes in the world of work, covering Big Tech, startups, AI, recruitment trends, and...

Read more from Megan Carnegie](https://thenewstack.io/author/megan-carnegie/)