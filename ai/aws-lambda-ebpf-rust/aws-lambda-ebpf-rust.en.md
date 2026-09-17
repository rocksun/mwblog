**On any compute platform, when a security alert fires,** the question is always the same. Which workload talked to that endpoint, when, and how much? So, you dig through logs and hope they hold up. The hard part is knowing what to look for and where to find it. On a single server, thousands of microVMs run for a few hundred milliseconds, then shut down.

Each one belongs to a different customer running a different function. Within milliseconds, the workload is done, and the logs captured during those few milliseconds are the only witness left.

> “Within milliseconds, the workload is done, and the logs captured during those few milliseconds are the only witness left.”

That was our situation at AWS Lambda. We needed a complete network ledger for every tenant workload, no matter how short its life or how much traffic it generates. This is the story of how we replaced an aging capture system with a purpose-built pipeline written in eBPF and Rust: why the old architecture ran out of road, and the decisions that let the new one hold up at Lambda’s scale.

## The job: a record you’re not allowed to touch

Every Lambda worker is a bare-metal EC2 instance packed with microVMs, each an isolated Firecracker guest. They all talk over the network to S3, other AWS services, the public internet, and back into a customer’s VPC. Something has to keep an honest, complete account of it all.

That is where a network flow log comes in. A network flow log helps with investigation, incident response, audit, and reconstructing what happened with a workload. Imagine it as the system of record for what happened to a network packet flowing across the system. The same records also feed into network usage and metering services that demand accuracy above all else. Lastly, all records must be persisted for [audit and compliance](https://thenewstack.io/agentic-cicd-audit-compliance-gap/) purposes.

Two properties matter more than the rest. The record must be complete and correctly attributed, and capturing it must add almost no overhead to both the network flow and the platform.

Correct attribution means every packet/flow is associated with the microVM where it landed and the tenant that produced it. Completeness means no missed packets. A missing or misattributed record can cause billing, observability, and monitoring problems at scale. Imagine this happening for every microVM when Lambda serves millions of requests per second. Overhead matters for a reason that isn’t readily visible to customers but plays a major role in how you run a service at Lambda’s scale. Every extra megabyte of RAM and every microsecond of CPU consumed adds up at Lambda’s density, lowering utilization, operating margin, and the ability to serve requests under load.

## Why the old way ran out of road

While building the new multi-tenant, Firecracker microVM-powered Lambda, we started with a system borrowed from the older, less-dense single-tenant EC2-era design. It had two parts: a kernel-side extension that counted packets and matched them to tenants and sandboxes per flow, and a userspace daemon that read those counters, batched them into records, serialized them, and frequently uploaded the files. This solution worked well for a small number of VMs. However, the solution broke at Lambda’s density for two mutually exclusive reasons.

First, rule explosion. iptables walks its rules more or less linearly for every packet, and each new microVM piled more rules onto the chain. One worker running a couple of thousand [microVMs](https://thenewstack.io/nanoclaw-docker-sandboxes-ai-agents/) needed well over a hundred thousand iptables rules just to keep the record. Every packet paid a tax proportional to how crowded the host was and what slot it received. So a packet’s bookkeeping slowed as the host got busier, which is exactly the wrong direction, since the whole plan was to pack more microVMs onto a host, not fewer.

> “A record that can’t see half the address space isn’t one you can trust, and the moment dual-stack IPv6 support was proposed for Lambda, the old approach was finished.”

The second reason was harder: the borrowed kernel module did not speak IPv6. A record that can’t see half the address space isn’t one you can trust, and the moment dual-stack IPv6 support was proposed for Lambda, the old approach was finished, no matter the performance improvements.

## Design considerations

As we embarked on the rewrite, we had a few non-negotiable design considerations: correct attribution, meaningful overhead reduction, and support for IPv6 as a first-class citizen. Dozens of internal systems already knew how to read the Amazon Ion records the old daemon produced. If we could emit byte-for-byte identical records, we could rip out the whole capture engine and no consumer, flow-log, or metering would notice the swap.

To solve for correct attribution, we implemented isolation at the microVM level. Each microVM already had its own network: a namespace with its own virtual devices. That network is the unit everything else organizes around.

## The shape of the new system

The replacement is three cooperating pieces. We’ll give each a plain name based on their role.

```

 ONE WORKER HOST

   control plane
       |
       |  gRPC over a Unix domain socket
       v
   orchestrator ....... one privileged process per host
       |                (loads eBPF, configures TC,
       |                 spawns one tagger per network)
       v
   --- per network (one microVM) ------------------------------

   eBPF capture  -->  ring buffer  -->  tagger  -->  Ion records
   TC hooks on        one per           Rust,
   the network's      network           userspace
   devices

   ------------------------------------------------------------
       |
       v
   same billing + flow-log pipeline as before

```

At the bottom sits the [kernel capture layer](https://thenewstack.io/groundcover-ai-observability-agents/). It’s a set of small eBPF programs attached to the traffic-control(tc) hook on each network’s relevant virtual Linux devices. They intercept packets and emit one compact event per packet into a ring buffer. They just watch. Nothing in these programs can copy, block, drop, or rewrite a packet; there’s literally no code path for it.

In the middle is the tagger: an unprivileged userspace process written in Rust, one per network. It drains its own dedicated ring buffer, rolls the raw per-packet events up into per-flow records, and writes them to disk in the legacy Amazon Ion format. On top is the orchestrator, one privileged process per host. It owns everything that needs elevated permissions: loading the eBPF programs, wiring up traffic control, spawning and supervising the fleet of taggers. It exposes a small lifecycle API over a Unix domain socket so the control plane can create, assign, recycle, and tear down tagging as microVMs come and go.

The decoupled design lets capture happen in the kernel, aggregation in userspace, and one process per host orchestrates it all. The captured records go to the existing downstream consumers unchanged.

## Capturing in the kernel, without getting in the way

The capture programs attach to the clsact qdisc in traffic control(tc), on both the ingress and egress side of each of a network’s devices. A network spans two devices, so that’s four attach points per network. Traffic control is a good place to stand. It sees every packet early, before anything downstream has touched it. Every eBPF program reads the packet and returns the “keep going” action. We never drop or modify a customer’s packet, and nothing we do adds meaningful latency.

For each packet, the program walks the headers- Ethernet, then IPv4 or IPv6, then TCP, UDP, or ICMP and writes one fixed-size event into that network’s BPF ring buffer. The event is small on purpose, about two dozen bytes for IPv4. A simplified version looks like this:

```

/* one event per packet, ~24 bytes for IPv4 */
 struct flow_event {
     u8  ip_version;       /* 4 or 6 */
     u8  protocol;         /* TCP / UDP / ICMP */
     u8  direction;        /* ingress or egress */
     u8  device_id;        /* which of the network's devices */
     u16 local_port;       /* "local" is always the sandbox side */
     u16 remote_port;
     u32 flags_and_bytes;  /* TCP flags in bits [31:24], byte count in [23:0] */
     u32 local_addr;       /* 16 bytes for IPv6 */
     u32 remote_addr;
     u32 received_time_ms;
 };

```

One packet, one event, one byte count. We don’t count packets in the kernel. The flags and the byte count share a single 32-bit word: eight bits of TCP flags on top, a 24-bit byte count underneath. Doing less work per packet in the kernel is the entire point, so aggregation is somebody else’s job.

The local and remote fields get normalized by direction before the event ever leaves the kernel. Arriving or departing, local always means the sandbox side and remote means the outside world. That one small normalization means userspace never has to reason about direction when it groups flows, and the record reads the same way regardless of which way the packet was headed.

> “Doing less work per packet in the kernel is the entire point, so aggregation is somebody else’s job.”

Let’s look at how eBPF plays a key role in simplifying the architecture. The eBPF program here works in a reserve-then-commit order. Each eBPF program maintains a dedicated ring buffer to record packet metadata. You ask the ring buffer for space, add the event in place, and submit. This avoids copying data through a syscall, consumes minimal CPU, and needs no per-CPU bookkeeping. Just a single consumer that drains it in order.

However, all this complex logic for parsing and event submission past the eBPF verifier took work. The eBPF verifier has a critical job: proving a program is safe before the kernel can load it, and that requires strict memory bounds checks and instruction limits. We had to make sure it could verify and load programs quickly, so we did the following: First, we made the header parser a shared subroutine, so the verifier proves it once instead of re-proving it inline at every attach point in the eBPF program. Then, we bounded the IPv6 extension-header walk to a fixed number of hops so the verifier can ensure it terminates. We also had to make sure packet fragments past the first IPv4 fragment report zero ports and flags rather than vending garbage into the ring-buffer events. We also had to make sure any coalesced super-packets from segmentation and receive offload (GSO/GRO) have their byte counts handled correctly. A garbage port or an over-counted byte would create a false log entry, so we keep the record honest at the source and byte-identical with the old system.

However, we don’t trust the verifier as the sole source of correctness, because this code produces a record critical to billing, compliance, and auditing systems; each eBPF program is written in C and runs through a formal model checker (CBMC) during every build. Its harnesses assert, among other things, that the event struct’s byte layout stays compatible with what every attached program expects. A struct that silently shifts by a byte is the kind of bug that quietly corrupts every record it touches, and nobody notices until the day they need the log.

## Sizing the ring buffer from first principles

The ring buffer is the one thing the kernel producer and the userspace consumer share, and its size is a real tradeoff. Too small and you drop events under a burst, which means missing records, which is a hole in the log right when traffic matters. Too large and you waste memory, and you pay for that waste on every ring buffer on the host.

So we didn’t guess. We derived the floor from each microVM’s packet rate; for example, if the ceiling is 100,000 packets per second per direction. We drain the ring roughly every 100 milliseconds. Multiply the peak rate by the drain interval, by the event size, and by two directions:

```

ring bytes =~ 62,500 pps x 0.1 s x ~24 bytes x 2 directions
            =~ 300 KB

```

The ring buffer API requires a power of two, so the design defaults to 512 KiB. That’s the smallest buffer that can’t overflow between drains at the guest’s own maximum packet rate. Put another way, the floor ensures a guest can’t outrun the recorder, even when it’s trying to. The size is configurable per network. In the running deployment, we currently provision it more generously than that floor, on the order of a couple of megabytes, while we finish tuning the right per-workload value. The number to defend is the floor, and the floor comes from a hard system limit, not a guess.

The drain cadence has another nice property: waking a userspace process isn’t free, and a fleet of thousands of processes all waking constantly would thrash the CPU. So the kernel decides when to bother. It checks how full the ring is and only forces a wakeup once the ring crosses about one percent full. Below that, it stays quiet and lets events pile up. Userspace, on its end, won’t come back to read more than once every 100 milliseconds. A quiet flow just sits there until the next drain, basically free. A busy one trips that one-percent threshold and gets read almost right away. Nothing’s on a fixed timer, so neither case gets the timing wrong.

## Draining and aggregating in Rust

The tagger turns raw per-packet events into the per-flow records the pipeline stores. One tagger per network, running unprivileged.

We picked Rust for boring, practical reasons. At this density, thousands of these processes run on a host, each holding a small amount of state that has to be correct. A garbage-collected runtime would give us pause times and memory that balloon under load, and a pause in the wrong place could create a gap in the record. Rust gives us predictable memory and no collector, plus a compiler that flat-out refuses to build whole categories of bugs that turn into misattribution. Each tagger runs in a few hundred kilobytes of RAM against a budget of about a megabyte. That’s what makes thousands of them per host affordable.

Inside, it’s a small set of cooperating tasks on a single-threaded async runtime. One task reads the ring, another owns the flow state, and a third writes parcels. The only work we fence off onto a blocking pool is the couple of operations that genuinely block: receiving the ring descriptor and serializing Ion, since the Ion writer isn’t async. It reads the ring through epoll, so it sleeps when there’s nothing to do and wakes when there is.

As events arrive, the tagger drops them into a flow map keyed by device, the five-tuple, and a tenant attribution handle. That handle comes from the metadata the control plane handed over when the flow was activated. Matching events accumulate bytes, packet counts, and OR’d TCP flags. Grouping happens as the events are read, so the hot path stays a lookup and an add.

Where does attribution actually come from? That’s because mapping is the most important property for the record. The kernel event carries no identity, and it doesn’t need to. Every network has its own dedicated ring and devices, so packets are separated long before the tagger sees them. The tagger isn’t pulling one tenant’s packets out of some shared firehose. The stream it reads was only ever that one tenant’s, because the ring and the devices feeding it belong to that tenant alone.

Once a minute, on a fixed interval lined up to the top of the second to match the old system it replaced, the tagger serializes the completed flows into Amazon Ion records in exactly the schema the old daemon produced. Each file gets written to a temporary name, flushed to disk, and renamed into place. A reader sees a complete record or nothing, never a torn one. A separate flush loop, with a little random jitter at startup so thousands of processes don’t all write at the same instant, drains completed flows even after a microVM has gone quiet. A workload that goes silent still leaves a finished record behind it.

Because the records are byte-compatible with the old format, the entire downstream world kept working untouched. And when we ran the two systems side by side, we could compare their output record for record and confirm they agreed. That’s about as direct a completeness check as you can get.

## Least privilege, enforced by a file descriptor

This is the part of the design I’m most fond of, because it uses an old Unix trick to get a strong security property for almost nothing.

The processes that do the actual packet work, the thousands of taggers, hold no elevated privileges. They can’t load eBPF or touch traffic control. They can’t even open the ring buffer map on their own. All of that power lives in one place: the per-host orchestrator, and even it runs with just the two capabilities it needs rather than as root.

> “Passing a file descriptor over a socket is a decades-old Unix feature, and it lets us keep thousands of processes powerless while concentrating privilege in one small place.”

So how does an unprivileged tagger read a ring buffer it isn’t allowed to open? The orchestrator opens it and hands the open file descriptor to the tagger over a Unix domain socket, using the kernel’s SCM\_RIGHTS mechanism to pass descriptors between processes. The tagger gets a ready-to-use handle to the ring and nothing else. It never had, and never needs, permission to create one. The privileged surface of the whole system is one small process per host. The thousands of processes touching customer traffic are about as powerless as we can make them.

## A lifecycle API, and why it has two doors

MicroVMs come and go constantly, so the control plane needs a way to tell the orchestrator when to start and stop recording a network. It does that through gRPC APIs over a Unix domain socket, with a handful of methods: create a set of flows, activate a flow, recycle one, tear one down, plus a health check.

Starting to record is split into two calls, a heavy one and a light one, and the split is deliberate. Create is a heavy call, the expensive path: it loads and attaches the eBPF programs, configures traffic control, and spawns the tagger. Attaching to network devices takes a kernel lock that every such operation on the host contends for, so when a host is standing up many networks at once, we batch these to keep everyone from serializing behind that one lock. Activate is the lighter call. By the time it runs, the machinery already exists, so it just hands over the customer metadata and flips the flow into steady-state recording. Its latency budget is tight: under 2 milliseconds at p90, under 10 milliseconds at p99.9, matching the baseline of the system it replaced.

## An honest tradeoff: kill it, or reuse it

Not every decision came out clean. These are lessons for anyone building something similar.

The original design had a strict rule for recycling a network: always destroy the tagger and spawn a fresh one. From a correctness standpoint, the reasoning was airtight. A brand-new process can’t carry stale metadata from a previous tenant, so a flow from one tenant landing in another’s record across a recycle becomes structurally impossible. Kill it, don’t try to clean it. We were sure that was the right call.

Reality under Production workloads showed us that forking and exec’ing a new process thousands of times as networks churned turned into a real source of CPU spikes at scale. The safest choice showed up as a flame graph. So the shipped system needed a new knob. A workload that reuses its networks can reuse the tagger after a recycle, trading off a little of that structural guarantee for a lot less CPU churn. A workload that wants the strict, cross-tenant-proof behavior leaves the knob off. I still think the strict version is the more correct design, but the fleet’s CPU budget just didn’t allow it.

## What it bought us

Start with the number that killed the old design. One host needed more than a hundred thousand firewall rules to keep the record for two thousand microVMs, and each additional microVM piled on more, taxing every packet a little further. The eBPF version swaps that linear rule walk for constant-time map lookups whose cost doesn’t climb as the host fills up. The linear tax is gone. That puts the density target, roughly double the microVMs per host, within reach, and without the burst-time gap a per-packet tax invites.

The rest of the payoff falls out of the constraints we started with:

1. IPv6 flows, invisible to the old tool, get recorded like anything else, so the log covers the whole address space instead of half.
2. Each tagger lives in a few hundred kilobytes of RAM against a roughly one-megabyte budget, small enough that thousands per host is practical.
3. Activating a flow into steady-state recording stays under 2 milliseconds at p90 and under 10 milliseconds at p99.9.
4. The capture layer is observe-only and formally checked, and the processes touching customer traffic hold no privileges. We added significant visibility while shrinking the trusted, privileged surface that could corrupt the record.
5. The output records are byte-for-byte identical to the old format, so every downstream flow-log and metering consumer kept working with no change

## Lessons worth carrying to other systems

A few of these travel well beyond Lambda. Kubernetes pods, edge runtimes, the sandboxes people are spinning up now to [run AI agents](https://thenewstack.io/perplexity-portable-computer-nvidia/). Anywhere you’ve got many tenants sharing a host and need a trustworthy record of their traffic, the same shapes hold.

First: observe from outside the hot path. The moment your recording logic sits inline in packet forwarding, its cost becomes a tax on every packet, and that tax is heaviest right when the record matters most. That same pressure pushes teams to drop or sample data, and an audit trail can’t survive sampling. eBPF lets you watch from the side and emit a compact event, while everything expensive happens elsewhere.

Second: size buffers from something real. A buffer sized by an actual rate limit times an actual drain interval is a number you can defend in a review, and it’s what lets you promise no dropped events under a burst. We could’ve picked 512 KB because it felt about right, and it probably would’ve held most of the time, right up until some burst it wasn’t sized for.

Third: keeping tenants apart at the point of capture is the part I’d argue hardest for. Give each tenant its own ring and its own devices, and the streams never touch, so you’re labeling clean traffic instead of guessing after the fact.

Fourth: old primitives are underrated. Passing a file descriptor over a socket is a decades-old Unix feature, and it lets us keep thousands of processes powerless while concentrating privilege in one small place.

Last one, and it’s the cheapest to get wrong: when you swap out an engine, keep the bolt pattern. Byte-for-byte identical output let us replace the entire capture path with zero downstream migration, and it handed us a record-for-record way to prove the new system saw everything the old one did.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/09/4981deeb-prsi-hs.png)

Prashant Kumar Singh is a Principal Engineer at Amazon Web Services, where he works on the AWS Lambda networking stack. He holds multiple U.S. patents in serverless networking and focuses on network telemetry and flow logging, eBPF-based data planes, multi-tenant...

Read more from Prashant Kumar Singh](https://thenewstack.io/author/prashant-kumar-singh/)

[![](https://cdn.thenewstack.io/media/2026/09/0cf65bfa-kg-hs.jpg)

Kshitij Gupta is a Senior Engineer at AWS Lambda, where he has spent the past eight years building and scaling the VM data plane that supports millions of invocations. During his more than 10 years at AWS, he has focused...

Read more from Kshitij Gupta](https://thenewstack.io/author/kshitij-gupta/)

[![](https://thenewstack.io/wp-content/uploads/2026/09/0e0f0202-shivendra_srivastava-hs2-600x600.jpg)

Shivendra Srivastava is an Engineering Leader at AWS Lambda. He manages a team of engineers working on challenging problems in serverless computing. Before joining AWS, he worked at Microsoft, Wayfair, and Walgreens. He holds a master’s degree in computer science,...

Read more from Shivendra Srivastava](https://thenewstack.io/author/shivendra-srivastava/)