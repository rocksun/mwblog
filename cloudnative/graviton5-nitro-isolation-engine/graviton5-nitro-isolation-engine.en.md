On Wednesday, AWS announced that its Graviton5 processor is now generally available and powers two new Amazon EC2 instances: M9g for general-purpose workloads and M9gd for workloads that require high-speed local storage. These are the first Graviton5 instances since AWS [previewed the chips at re:Invent 2025](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2).

The new chips double Graviton4’s core count from 96 to 192, and AWS says the new instances will deliver up to 25% better compute performance than the previous generation.

> AWS says the new instances will deliver up to 25% better compute performance than the previous generation.

What’s maybe more interesting, however, is that these new instances also run on the sixth-generation Nitro System, which now includes the Nitro Isolation Engine, a new, formally verified security component that AWS describes as “a separation kernel whose sole job is isolating virtual machines from each other.”

## A kernel whose only job is isolation

The idea of a [separation kernel](https://en.wikipedia.org/wiki/Separation_kernel) has been around for a while. [John Rushby coined the term in 1981](https://dl.acm.org/doi/10.1145/800216.806586). His core idea was that a standard OS kernel, even at the time, had become far too large to formally verify. A smaller, specialized separation kernel, however, would still allow formal verification due to its relatively limited complexity.

AWS launched its [Nitro system and hypervisor](https://aws.amazon.com/ec2/nitro/) in 2017, and it has enforced isolation in EC2 ever since. But Nitro also handles substantial business logic and manages device drivers and other AWS-specific features, meaning it was not designed for formal verification from the start.

With this new system, the Nitro hypervisor still handles policy, including VM creation, resource allocation, migration, and scheduling, but it is now somewhat deprivileged and must ask the Nitro Isolation Engine (NIE) to perform any operation that touches guest state, and the Isolation Engine checks every request before acting.

“Distilling the hypervisor’s security-critical isolation logic into a minimal component, the NIE, makes it small enough to verify and audit, giving customers unprecedented visibility into how isolation is enforced,” AWS’s Dominic Mulligan and Nathan Chong write. “We also wrote NIE in Rust, a language that lends itself more naturally to formal verification.”

## How we got here

Some of the earlier work in this area includes Columbia’s [SeKVM project](https://www.cs.columbia.edu/~rgu/publications/oakland21-li.pdf), which was the first formally verified commercial-grade hypervisor in 2021. But it looks like this was mostly a research project that never ran in a commercial cloud.

AWS itself credits [seL4](https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf), a project that demonstrated that OS verification was feasible.

To prove the kernel behaves correctly, AWS used the [Isabelle/HOL proof assistant](https://www.amazon.science/blog/isabelle-hol-the-proof-assistant-behind-the-nitro-isolation-engine). AWS says the model and proof “comprise 330,000 lines of machine-checked mathematics,” making it comparable to the seL4 project. “However, unlike seL4, NIE is designed for a commercial cloud environment and ships on production hardware as an always-on feature for Graviton5 users,” AWS writes in its announcement.

## 192 cores: a substantial redesign

The chip itself got a substantial redesign. Graviton5 moves from TSMC’s 4nm process to 3nm, and while Graviton4 put all 96 cores on a single chiplet with PCIe and DDR controllers on their own chiplets, Graviton5 divides its 192 cores across four chiplets, each with its own controllers, which puts the memory controllers closer to the cores.

AWS claims that, together with faster memory chips, this will allow web applications to run up to 35% faster and ML inference up to 35% faster than on Graviton4.

## Graviton and agentic AI

AWS positions Graviton5 as purpose-built for agentic AI. That pitch, which isn’t all that different from Google’s pitch for its ARM processors, seems to be working. Meta signed a [multibillion-dollar agreement](https://www.aboutamazon.com/news/aws/meta-aws-graviton-ai-partnership) in April to deploy tens of millions of Graviton cores for its agentic AI work, and Snowflake [committed $6 billion](https://www.snowflake.com/en/news/press-releases/snowflake-expands-aws-collaboration-with-6b-commitment-to-accelerate-enterprise-agentic-ai-adoption/) over five years in May. AWS says Uber is also deploying Graviton for agentic workloads.

In total, AWS says, more than 120,000 customers currently use Graviton, and that more than half of new CPU capacity added to AWS has been Graviton for the third year running.

AWS may have a bit of an early mover advantage here. Microsoft’s [Cobalt 200](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/announcing-cobalt-200-azure%E2%80%99s-next-cloud-native-cpu/4469807) is still in preview, Google’s latest [Axion](https://cloud.google.com/blog/products/compute/axion-based-n4a-vms-now-in-preview) chips only went GA in January, and Nvidia’s [Vera](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/) — maybe the most hyped of all of these chips — will arrive in the second half of the year.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)