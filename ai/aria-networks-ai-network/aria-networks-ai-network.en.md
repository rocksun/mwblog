As the global race to provide AI infrastructure services accelerates, [Aria Networks](https://arianetworks.com/) claims it has engineered a “fundamentally different approach” to how networks operate and how to maximize token efficiency in the agentic era.

Called the “Network that Thinks” initiative and announced on Tuesday, the Palo Alto-based Aria Networks says there’s a combination of technologies and methodologies at work here, including tools to optimize [Model Flop Utilization](https://lmms-engine.readthedocs.io/en/latest/reference/mfu.html) (MFU), the company’s newly hardened Aria SONiC (an open-source network operating system for distribution-optimized data centers), end-to-end ultra-fine-grained [telemetry](https://thenewstack.io/data-telemetry-is-the-lifeline-of-modern-analytics-and-ai/), and intelligent agents that operate across the network stack.

## What is Model Flop Utilization?

Described by Aria Networks as the “defining metric” of the AI factory era, MPU measures datacenter hardware performance efficiency in relation to the theoretical peak throughput achievable. It can serve as a proxy for assessing whether an AI cluster is delivering on its investment.

MFU directly determines token efficiency and cost per token. As tokens become what Aria likes to call “the currency of intelligence”, the network’s infrastructure efficiency affects [how quickly gradients](https://www.grokmountain.com/p/understanding-gradients-in-ai-model) (mathematical signals that update a model’s weights) are synchronized, how efficiently [key-value caches](https://huggingface.co/blog/not-lain/kv-caching) are transferred (so that models don’t reprocess previous tokens), and how seamlessly jobs are scheduled across thousands of  GPUs, TPUs and NPUs etc.

> “Without the network performing at its best, the gains from every other optimization investment are left on the table.” — Mansour Karam, founder & CEO at Aria Networks

## The network inside the cluster

[Mansour Karam](https://www.linkedin.com/in/mansourkaram/), founder & CEO at Aria Networks, says that network operations teams and software engineers need to realize why their network expenditure (which he estimates to be just 10-15% of total cluster cost) is also the “highest-leverage” investment, i.e., the zone where the line between success and failure is most prominent.

He makes this assertion because network teams can optimize the job scheduler, the storage layer, or the KV cache transfer algorithm, but each of those optimizations depends on an optimized network to achieve the expected result.

“Without the network performing at its best, the gains from every other investment are left on the table,” Karam tells *The New Stack*. “The Aria solution distinguishes between updates that affect the data plane, control plane, and management plane. Updates that affect the data plane are treated very differently from upgrades that only affect the management plane.”

## Deliberately hybrid

He explains that his company has adopted a hybrid architecture, and deliberately so. The Aria agent layer spans multiple layers of the stack — from the switching ASIC layer (an Application Specific Integrated Circuit designed to route data packets in a specific way) up through the controller (where network traffic is configured and orchestrated), all the way to the cloud.

Throughout this hybrid architecture, different layers operate at different resolutions and with different methods and intelligence requirements. At the lowest levels, close to the hardware, Karam explains that agents are “simpler and faster” as they may need to react in microseconds or milliseconds to link events or anomalies.

So the era of automated infrastructure continues to grow. This tier of the technology stack now provides everything from serverless functions to automated provisioning and self-healing instances with autonomous load balancing. Does that mean developers should consider their years spent getting an MSc in cloud communications & networking somewhat redundant? Perhaps Aria’s hardened SONiC implementation could expose APIs for developers who want to build custom tooling or integrate their own networking constructs into existing infrastructure-as-code pipelines, right?

“While Aria Networks introduces a transformational operational model designed to maximize AI cluster utilization, it’s built to be open and drop into existing environments and toolsets,” says Karam.

He further explains that Aria’s SONiC distribution preserves the standard interfaces that developers already rely on, so existing tooling continues to work without modification. The Aria platform also exposes a [REST API](https://thenewstack.io/rest-still-outshines-graphql-for-many-api-use-cases/), CLI, and [MCP](https://thenewstack.io/when-is-mcp-actually-worth-it/) interfaces that developers can use to interact with the Aria Server to integrate “deep networking” (a branded term that Aria capitalizes to denote its work covering ultra-fine grain telemetry and deep network visibility) into existing infrastructure.

How fine-grained is fine-grained telemetry? In Aria’s case, it’s 10–10,000x finer resolution than traditional tools, collected across switches, transceivers, and hosts in a single unified view.

## Agents partner alongside network engineers

At the operator-facing layer (Aria Console), the agents include leading LLM models. Operators primarily interact in natural language: they can ask questions about the network state, request explanations of alerts, and collaborate with the system on remediation decisions.

The LLM has access to the full telemetry and system state. It uses a specialized networking context, meaning its responses and actions are grounded in the accuracy, safety, and reliability standards required by network operators. The agents partner with the operators to enable continuous network optimization.

“We champion an automated testing culture, whereby systems are continuously and thoroughly tested 24/7 before any new updates are pushed out. Updates go through automated validation in a staging environment before rolling out incrementally across the fabric,” says Karam.

> The bottom line on the use of networking agents working to devise strategies for resolving issues or optimizing performance is a simple pledge – this is not a black box; it is a partnership.

As with every AI advancement, this technology is not about putting network engineers and operators out of a job; instead, it’s about enabling capabilities such as intent-based configuration. Network operators specify their needs, and the platform configures the fabric accordingly for routing, load balancing, congestion management, and failover. This is intended to reduce (Aria would say eliminate) the manual, error-prone workflows that slow down traditional deployments.

Karam promises transparency and control; his company’s bottom line on the use of networking agents working to devise strategies for resolving issues or optimizing performance is a simple pledge. This is not a black box; it is a partnership.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)