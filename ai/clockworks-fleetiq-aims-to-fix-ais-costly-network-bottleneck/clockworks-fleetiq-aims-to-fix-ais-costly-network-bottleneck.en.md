GPUs are steadily getting faster, but as enterprises, neoclouds and the entrenched hyperscalers look to get more efficiency out of them, the bottleneck is often the network — to the point where NVIDIA, for example, is now [investing](https://www.nvidia.com/en-us/networking/products/silicon-photonics/) in silicon photonics to improve networking speed and resiliency. One key to improving existing networks is improved visibility into the state of these GPU clusters and the networks that connect the different systems.

[Clockwork](https://www.clockwork.io/) started out as a tool and service for synchronizing clocks across compute clusters. But as it turns out, once you know when a package was sent and received with sub-microsecond accuracy, you’ve also built the basis for a monitoring solution that can keep track of where exactly there are bottlenecks in a large cluster, no matter whether you’re looking at CPUs or GPUs. Once you have that information and added additional monitoring features, you can start shaping this between machines, too.

Meanwhile, AI workloads — and especially training workloads — put a high demand on these clusters, with networking often becoming both a bottleneck and a source of errors for these highly distributed workloads, which can then necessitate restarting the training process from a recent checkpoint.

[![](https://cdn.thenewstack.io/media/2025/09/65196db3-clockwork-fleetiq.png)](https://cdn.thenewstack.io/media/2025/09/65196db3-clockwork-fleetiq.png)

Image credit: Clockwork.

This, said Clockwork’s VP of Products and Solutions, Dan Zheng, can often lead to hours of work lost and days of time added to training runs.

“Today, what happens is that you may have really good siloed information for GPUs, for networking, for storage, but when a job is running slow — this could be a training job or could be a distributed inferencing job — you’re trying to pinpoint where the problems are, and oftentimes, it takes a lot of effort to figure out. … We’re able to provide cross-stack visibility so that you can quickly identify where the problem is,” Zheng said.

FleetIQ, which the company is launching today, gives operations teams this visibility, combined with stateful fault-tolerance (so that jobs can continue without disruptions, even in the face of infrastructure failures) and automatic performance optimizations to help avoid network congestion, contention and other bottlenecks.

[![](https://cdn.thenewstack.io/media/2025/09/e0815da9-clockwork-jitter.png)](https://cdn.thenewstack.io/media/2025/09/e0815da9-clockwork-jitter.png)

Image credit: Clockwork.

“If you look at the availability or uptime of GPU clusters, you’re really looking at maybe, at best, in the low 90s,” Zhen explained. Individual GPUs can fail, just like networking equipment or storage pods. “Because we’re sitting at the edge and have a unique point of view, we can do interesting things in the software layer. Collectively, we call this software-driven fabrics, because we believe that the bottleneck shifted from raw GPU compute to communication.”

The Clockwork team, which recently brought on former Sysdig and Nimble Storage CEO [Suresh Vasudevan](https://www.linkedin.com/in/suvasudevan/) as the company’s CEO, argues that its system provides full visibility into the entire stack, all while being mostly agnostic to the hardware, though the team does have to dig deep into how the different hardware components interact with a variety of networking APIs, transport protocols and communication libraries, for example.

[![](https://cdn.thenewstack.io/media/2025/09/a578dccb-clockwork-recover.png)](https://cdn.thenewstack.io/media/2025/09/a578dccb-clockwork-recover.png)

Image credit: Clockwork.

Among others, the service can work with GPUs and accelerators from NVIDIA, AMD and others, and supports networking libraries like NVIDIA’s [NCCL](https://developer.nvidia.com/nccl) and the open source [RCCL](https://github.com/ROCm/rccl) library, as well as InfiniBand and Ethernet/[RoCE](https://www.roceinitiative.org/roce-introduction/). (Networking engineers love acronyms even more than most tech disciplines.)

Looking ahead, Clockwork also plans to go a bit further up the stack and bring application-level monitoring to its service. Currently, a tool like FleetIQ doesn’t know a lot about the actual applications that are sending data across the network.

[Nebius](https://nebius.com/), which just signed a major AI infrastructure deal with Microsoft, NScale, Uber and several other large public and private cloud operators, is already using FleetIQ.

“We are in the process of rolling out Clockwork across Uber infrastructure, and look forward to experiencing their full capabilities at Uber’s scale. Clockwork’s software-driven fabric provides foundational observability for the hybrid, multicloud environment, helping us deliver what matters most: improved infrastructure utilization, enhanced resiliency, and ultimately, a better experience for the millions of people who rely on our platform every day,” said [Albert Greenberg](https://www.linkedin.com/in/albert-greenberg-376a39/), the chief architect officer at Uber.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)