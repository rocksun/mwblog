**For roughly $825, Anthropic’s Frontier Red Team built a cluster of 15 off-brand Android TV boxes** that runs an AI model at 0.39 tokens per second, painfully slow for a chatbot but fine for software with nowhere to be and nobody waiting on it.

That experiment anchors [new research](https://www.anthropic.com/research/self-replicating-ai) from Anthropic researchers [William Zhou](https://www.linkedin.com/in/williamchou/) and [Daniel Freeman](https://www.linkedin.com/in/daniel-freeman-6952136/), published Monday, suggesting small open-weight models may be only months away from copying themselves across cheap, internet-connected hardware without relying on a datacenter.

The researchers haven’t built an AI worm that can spread across the public internet on its own, and their experiments took place inside controlled environments with shortcuts that made replication easier. But the results suggest several of the remaining technical barriers may be temporary.

> The researchers haven’t built an AI worm that can spread across the public internet on its own, and their experiments took place inside controlled environments with shortcuts that made replication easier.

## Inference is the real hurdle

Zhou and Freeman identify four steps an AI needs to take to replicate itself, which are finding a target, gaining access, getting inference running, and moving on to the next machine.

Previous benchmarks such as [CyberGym](https://arxiv.org/abs/2506.02548) and [ExploitBench](https://arxiv.org/abs/2605.14153) suggest smaller models can already handle some of the exploitation work, and frontier agents [escaped their test sandboxes using basic exploits](https://thenewstack.io/securing-ai-agent-sandboxes/) earlier this year. The bigger challenge may be getting a model running on unfamiliar hardware, where it has to sort out whatever operating system, dependencies, and installation problems it runs into.

In Anthropic’s tests, Qwen3.5-9B deployed a working Llama3.1-8B inference server on eight of nine hardware types, including Jetson Nanos, Macs, and RTX 4090 machines, while the larger GLM-5.2 handled the same work more reliably and with higher throughput.

The team then built a firewalled Google Cloud environment with eight nodes running Android emulators, and starting from a single worm instance, the system had to reach the other nodes and establish a working inference server on each one. A fresh copy of the worm was spawned whenever a node’s server passed correctness and anti-cheating checks, and GLM-5.2 reached all eight nodes in four of five trials and seven nodes in the fifth.

GLM-5.2 ran on a separate inference server because the target machines couldn’t hold it, so the worm installed a smaller 8B model in its place, and the researchers made exploitation easy by leaving an unauthenticated Android Debug Bridge port open.

> A fresh copy of the worm was spawned whenever a node’s server passed correctness and anti-cheating checks, and GLM-5.2 reached all eight nodes in four of five trials and seven nodes in the fifth.

## Worms that take notes

The agents got better at setting up inference on unfamiliar hardware when they could read notes left by earlier attempts. The researchers ran Qwen3.5-9B through 20 separate lineages, each lasting six generations, and success climbed from 45% in the first generation to between 61% and 84% in later ones.

The researchers call this Lamarckian inheritance, where one agent passes what it learned to the next without any retraining of the model. It’s a mechanism familiar to developers using persistent agent runtimes such as [OpenClaw and Hermes Agent](https://thenewstack.io/persistent-ai-agents-compared/), but here that memory helps successive copies work through installation failures on hardware they’ve never seen.

> The researchers call this Lamarckian inheritance, where one agent passes what it learned to the next without any retraining of the model

The team also tried giving Qwen3.5-9B access to the much more capable Opus 4.8 model for advice, and it produced no statistically significant improvement because the small model tended not to know the right questions to ask.

## The end-of-2026 trend line

The paper identifies two constraints that have kept this scenario theoretical. A model needs to be capable enough to replicate reliably and small enough to run on compromised hardware, and right now those requirements don’t overlap. GLM-5.2 showed the necessary competence in the simplified test but is too large for the cheap devices the researchers have in mind, while smaller models can fit on those devices, particularly when inference is distributed across several machines, but can’t yet complete the entire process consistently.

Using the [Epoch Capabilities Index](https://epoch.ai/eci), the researchers tracked open-weight models with 30 billion parameters or fewer and found that, by the end of 2026, the trend line puts the strongest of them at GLM-5.2’s general capability level. It’s a rough estimate, since general capability scores don’t necessarily predict replication performance, and the team’s end-to-end experiment used favorable conditions.

By the researchers’ calculations, typical 4GB TV boxes running 4-bit weights can host a 9B model across four or more devices, and a 26B model across ten or more, which is how their own 15-box cluster runs Gemma4-26B-A4B.

A single inference setup on this class of hardware could take roughly 28 to 150 hours depending on the model, and the researchers argue that lightweight agents may be far more willing than human attackers to grind through that kind of effort across huge numbers of devices. They compare the possibility to a digital slime mold, spreading slowly through whatever resources it can reach.

## Cheap boxes, borrowed compute

The [Kimwolf botnet](https://synthient.com/blog/a-broken-system-fueling-botnets) infected more than two million devices, most of them cheap Android TV boxes, and the researchers used that figure to calculate what an AI replicator could do with a network of equivalent size. Dividing those devices into clusters of 15 running Gemma4-26B-A4B would yield roughly 133,000 copies of the model generating a combined 80,000 tokens per second.

That’s equivalent to no more than about 40 Nvidia H100 GPUs, which is modest by datacenter standards, but the hardware and operating costs would belong to someone else.

The researchers also examined edge accelerators such as Nvidia Jetsons, which are used in everything from security cameras and conference room equipment to robots and drones. Those devices are generally harder to reach because they communicate through outbound cloud-management connections.

## Stopping software that copies itself

The researchers aren’t suggesting there’s no way to stop a self-replicating AI worm, and some of its traits could make it easier to detect. Moving multi-gigabyte models between devices creates network traffic that ISPs can monitor, and a worm that spreads aggressively won’t go unnoticed.

During the Mirai botnet cleanup, one ISP’s quarantine of infected subscribers [cleared 92% of infections within 14 days](https://www.ndss-symposium.org/ndss-paper/cleaning-up-the-internet-of-evil-things-real-world-evidence-on-isp-and-consumer-efforts-to-remove-mirai/), and the researchers expect a similar approach to work as a first line of defense. Eliminating a replicator completely, however, would mean coordinating every ISP with infected customers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)