ATLANTA — When systems grow large enough, even very small optimizations can lead to very large savings.

This was the lesson that OpenAI Technical Staff Member [Fabian Ponce](https://x.com/fabianmponce) imparted before the keynote crowd at [KubeCon+CloudNativeCon North America 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event), being held this week in Atlanta.

## OpenAI’s Observability Challenge at Scale

Each iteration of OpenAI’s ChatGPT have brought big improvements, along with more Kubernetes clusters and greater volumes of traffic — “And orders of magnitude more telemetry to keep it all running,” Ponce said.

In order to make it all run smoothly, OpenAI requires “an absolutely massive amount of telemetry and making it fast, queryable and actionable at scale,” he said.

## Fluent Bit’s Critical Role in Data Telemetry

[OpenAI](https://thenewstack.io/openais-sam-altman-sees-a-future-with-a-collective-superintelligence/) runs [Fluent Bit](https://thenewstack.io/how-to-deploy-fluent-bit-in-a-kubernetes-native-way/), an observability platform stewarded by the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention), on every Kubernetes node. It digests log files and enriches them with samples of network streams, formats the results and sends them to the appropriate data stores.

With architecture, Fluent Bit generates 10PBs of data a day, stored on [Clickhouse](https://thenewstack.io/moving-from-c-to-rust-clickhouse-has-some-advice/).

## The Drive for Resource Efficiency Amidst Massive Growth

OpenAI, Ponce admitted, has an “absolutely insatiable appetite” for GPUs. OpenAI CEO [Sam Altman](https://thenewstack.io/openais-sam-altman-ai-is-now-ready-for-the-enterprise/) has plans for the company to use of over 1 million GPUs by the end of the year, and [promises to increase that number 100x](https://x.com/sama/status/1947057625780396512).

And all those GPUs will also need CPUs to run.

So despite these [gargantuan purchase orders](https://techcrunch.com/2025/11/06/sam-altman-says-openai-has-20b-arr-and-about-1-4-trillion-in-data-center-commitments/), the company’s observability engineers, anyway, are still mindful of using resources efficiently. So one mission is to make [Fluent Bit](https://fluentbit.io/) as “lean as possible.”

Using [perf](https://www.brendangregg.com/perf.html), a Linux tool for gathering performance data, the observability team looked at the CPU cycles Fluent Bit was using. Ponce hypothesized that most of the work Fluent D was doing would be in preparing and formatting the incoming data.

## Uncovering a Surprising CPU Bottleneck With perf

But what surprised Ponce, was that this wasn’t the case at all. Instead, at least 35% of the data was chewed up by a single function (`fstatat64`) whose purpose was to figure out how large log files were before reading them.

So the team turned off this capability — and the results were immediately apparent:

[![](https://cdn.thenewstack.io/media/2025/11/b23f50ff-openai-02.jpg)](https://cdn.thenewstack.io/media/2025/11/b23f50ff-openai-02.jpg)

“The results speak for themselves,” Fabian Ponce told the crowd. “We have a new load pattern here that uses about half as much CPU while doing exactly the same work.”

Every time a new file is written, Fluent Bit executes the `fstatat64` to read the size of the file.

“If the process is continually emitting new logs, line by line, then Fluent Bit is going to race that, and continue to run `fstatat64` every time that happens,” Ponce explained. “That is going to burn a ton of extra compute.”

And it turns out the company didn’t really need that information, at least not at that level of nuance.

## The Impact of Disabling a Hungry Function

While the maintenance team knew the change would reduce CPU usage, perhaps they would be forgiven for not realizing how much savings would accrue.

In fact, when Fluent Bit [was modified system-wise](https://x.com/Joab_Jackson/status/1988618222376034488), it ended up “returning about 30,000 CPU cores to our Kubernetes clusters,” Ponce said.

[![](https://cdn.thenewstack.io/media/2025/11/4d62533a-openai-03.jpg)](https://cdn.thenewstack.io/media/2025/11/4d62533a-openai-03.jpg)

“If we can return a CPU to every node, then maybe that’s one more microservice that we can fit into a given host,” he said.

The team went on to optimize Fluent Bit in other ways as well, though this one tweak had the biggest overall impact. The company’s engineers are preparing for Fluent Bit a patch that would allow users to specify a lower threshold of notifications.

## Key Takeaways for Performance Optimization

The takeaway for Ponce was clear: There is always value in breaking out your “profiler of choice, and seeing what is happening under the hood. ”

As famed Golang programmer [Rob Pike](https://github.com/robpike) once advised in his [Five Rules of Programming](https://users.ece.utexas.edu/~adnan/pike.html): “You can’t tell where a program will spend its time. Bottlenecks occur in surprising places.”

And in large distributed systems, those little bottlenecks can be expensive unless they are uncorked.

You can enjoy the entire talk here:

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)