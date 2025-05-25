# Cloud Realities Are Slowing AI Ambitions
![Featued image for: Cloud Realities Are Slowing AI Ambitions](https://cdn.thenewstack.io/media/2025/05/d0770791-firosnv-photography-z2c6ounf-ie-unsplash-1024x683.jpg)
[Firosnv. Photography](https://unsplash.com/@firosnv?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/black-laptop-computer-turned-on-near-black-and-white-electronic-devices-Z2c6ounF-iE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
Cloud operations today are, for the most part, mature. Enterprises are comfortable with cloud: it has a defined operational role, and there’s enough support available, through architectural best practices, community, knowledge, visibility, and automation, to optimally run most digital applications and workloads in public, private, or hybrid cloud environments.

Moreover, cloud technology has become a key to widespread access to AI. In years past, only a select few private companies would have had access to the high-performance compute capacity required to run generative AI workloads. Cloud is proving to be the great leveler, making this level of compute accessible—and the AI services that use it available—to all who wish to use it.

But it’s coming at a cost. Not necessarily a financial one, although it’s a factor in decision-making. The bigger cost is to cloud optimization approaches. Put simply, widespread and intensive AI adoption is starting to push organizations outside of their comfort zones when it comes to cloud configurations. Targeted action is required to get comfortable with cloud again.

**Understanding AI characteristics**
To understand why established norms in cloud [operations are being tested](https://thenewstack.io/who-should-run-tests-on-the-future-of-qa/), one must first understand the nature of the AI workloads that cloud is now being asked to drive.

AI workloads are powerful, both in terms of the value they can bring to enterprises and the compute resources required to run them at scale.

This will only increase as Agentic AI becomes the dominant type of AI encountered in enterprise environments. [Agentic AI signifies a tighter integration of AI technology](https://thenewstack.io/agentic-ai-and-a2a-in-2025-from-prompts-to-processes/) into business processes, with autonomous or semi-autonomous software agents handling key processes or parts of those processes to meet specific goals. These systems can make rapid decisions, manage complex tasks, and adapt to changing conditions, assuming underlying systems are performant, but we’ll get to that.

What enterprises need to know is that [Agentic AI](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/) is more interactive than other forms of AI – “talking” constantly to source systems, data repositories, external tools, databases, and APIs, which makes it a more latency-sensitive evolution of artificial intelligence technology. A cloud or connectivity disruption or failure could lead to an agent-led process failing to kick off or achieve what it intended.

The main thing to understand about AI workloads is that they have different characteristics from those used to [define cloud operational](https://thenewstack.io/defining-low-data-loss-downtime-tolerances-in-kubernetes/) parameters today. That means past decisions to make a [digital application or workload perform optimally in the cloud](https://thenewstack.io/driving-digital-experiences-via-cloud-native-applications/) are not always cross-applicable to AI. Today’s cloud setups are not designed to meet a very different set of requirements, nor were they intended to.

For enterprises, it’s clear that the same effort that went into optimizing cloud setups for a digital context must now be repeated to optimize cloud setups for AI.

The onus is on enterprises to understand and capture the characteristics of their different AI workloads, such that [supporting cloud infrastructure](https://thenewstack.io/terraform-beta-supports-multicloud-complex-environments/) can be architected and configured to meet evolving performance needs.

**What this will look like in the cloud**
For most enterprises, AI and the source systems it taps into run in multiple clouds, data centers, and across a complex network of owned and unowned connectivity links.

Not all AI services will be available in a local region or zone, which may be an overriding factor in an enterprise’s choice of AI model.

From an operational excellence perspective, enterprises need to determine where the infrastructure underpinning an AI service and its users are based to understand whether a cloud environment can support those requirements or if changes need to be made.

This includes understanding the extent of the AI’s exposure to “common” infrastructure, such as having a large amount of traffic being funneled over a single fiber link, or through a single aggregation point such as a point-of-presence in a high-density data center that has a high concentration of AI service providers present. Such concentration risk and [single points of failure](https://thenewstack.io/james-webb-space-telescope-and-344-single-points-of-failure/) may exceed internal risk tolerances, given AI’s increasingly critical role.

Enterprises must understand how every provider or part of their AI [service delivery chain operates](https://thenewstack.io/top-costly-cloud-mistakes-and-how-to-sidestep-them/). How does a provider prioritise traffic at certain transit or hand-off points? Do they perform their own load balancing? How will this impact AI service delivery? The answers to these questions may give enterprises cause to re-architect their cloud setups to diversify traffic routes and improve redundancy options.

These decisions will impact performance efficiency. A roundtrip response time of 50ms might be acceptable for a basic generative AI application, such as a user asking a question and expecting a contextual response. But for a [busy Agentic AI system](https://thenewstack.io/system-two-ai-the-dawn-of-reasoning-agents-in-business/), if every query response takes 50ms, that will quickly add up. Users may experience excessive transaction times, timeouts, or other congestion and latency-related issues as a result.

Enterprises can improve [performance efficiency](https://thenewstack.io/3-legs-of-cloud-efficiency-cost-performance-and-velocity/) by proactively identifying optimization opportunities for traffic and cloud resource usage.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)