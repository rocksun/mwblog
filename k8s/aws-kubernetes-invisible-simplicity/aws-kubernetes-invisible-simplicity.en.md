For this edition of *The New Stack Makers*, we sit down with [Jesse Butler](https://www.linkedin.com/in/jesse-butler/?skipRedirect=true), principal product manager at [AWS Elastic Kubernetes Service](https://aws.amazon.com/eks/).

With his involvement in several key Cloud Native Computing Foundation (CNCF) projects, including Karpenter, Kro, and Cedar, Butler explained his vision for more effective cloud-native computing at KubeCon + CloudNativeCon Europe 2026 in Amsterdam.

VIDEO

Having joined AWS in 2020, Butler says his mission during his tenure has been to make Kubernetes easier to use. Drawing on his background in Unix, he is a firm believer in open-source software development and in its ability to democratize technology.

In terms of the state of the nation in open source, Butler agrees that the “commercial aspect is appropriate” within open platforms, but that essentially it all comes down to community-driven activities and the work of maintainers and committers.

## Formulation for the nation

“That’s really one of the things that the CNCF does so well, it helps formulate, standardize, and assemble this community and make it like a formal, governed thing. But companies can play a really important role too; just because one team is solving something in [GitHub](https://thenewstack.io/github-launches-its-coding-agent/), that doesn’t mean that it’s workable for everybody, so there needs to be a fluid mix where we see a synthesis of open source technologies and proprietary core foundational innovation too,” says Butler.

Acknowledging the value of software engineers and vendors coming together on unfinished software products, Butler reminds us that it’s often CNCF member organizations that finish off a project with the requisite polish and make it ready for use.

“But just think about the scope here, I mean, the CNCF is pretty much the biggest software engineering project that has ever existed on the planet, and it’s part of the wider Linux Foundation, too,” says Butler. “I get the vibe that not every single organization wants to contribute in the same way, but that’s the central ethos of open source, i.e., freedom to choose. It’s the right methodology to embrace if we’re going to get out of these pillared, proprietary stacks in the long run.”

> The CNCF is pretty much the biggest software engineering project that has ever existed on the planet and it’s part of the wider Linux Foundation too.

## Containers, no brainers

Talking about the industry’s progression in recent years, Butler says his team at AWS welcomed Kubernetes’s ability to enable developers to orchestrate at scale. With somewhere around [80% of enterprises now using Kubernetes](https://www.cncf.io/reports/cncf-annual-survey-2024/) meaningfully in production, the open ecosystem is firmly sold on the technology, but complexity still pervades.

This reality clearly drove Butler to title his keynote “From complexity to clarity, making Kubernetes invisible” at KubeCon Europe 2026. His intention was to draw parallels with Linux, which (he says) has “mostly faded away into the background” and become an accepted utility. He thinks there are many ways we can solve the complexity challenge, ranging from abstracting services to coalescing or consolidating functions into more easily consumable blocks.

## Karpenter, Kro, and Cedar

Covering off his work on the Karpenter, Kro, and Cedar projects, Butler explained how Karpenter works to manage node lifecycle management. He says the revelation this project revealed was that the best auto-scaling approach is to provision nodes in real time. This means engineers don’t have to worry about auto-scaling, and that’s how [Karpenter](https://github.com/aws/karpenter-provider-aws) works. The technology works based on workload pressure: when a developer schedules work, and there’s no node available, it checks the specified configuration, creates a node, and then joins it to the cluster.

Looking at project [Kro](https://github.com/kubernetes-sigs/kro) (Kubernetes Resource Orchestator), Butler describes himself as a self-confessed “cranky old man in an airport lounge,” complaining that he had to write custom controllers to glue resources together in a cluster.

“During that flight, I wrote the first instance of what is now Kro and took a couple of really novel approaches to composition and resource orchestration in the cluster and knew immediately this was something that the whole ecosystem could benefit from,” Butler says.

Finally, to [Cedar, an open source policy language](https://www.cedarpolicy.com/en) and evaluation engine that AWS donated to the CNCF. This technology handles fine-grained authorization controls and is not Kubernetes-specific, making it suitable for a range of cloud-native policy tasks.

## Open source is everywhere

“Overall, I have to say that maintainers need more love. None of these guys are trying to get rich when they fix a container debug, right? Open source is everywhere today, from your laptop to your smartphone to your aircraft seat, but the people behind so much of this technology are not doing it for glory, so we do have to take care of this ecosystem,” added an upbeat Butler.

As the drive to simplify Kubernetes and to continue upholding project openness throughout the CNCF pervades, Butler’s closing words carry plenty of weight. Looking ahead, he hopes that a combination of agentic automation and human ingenuity will come together to make open source software better for users everywhere.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)