# Rust, Linux, SLOs and All Things Performance at P99 CONF
![Featued image for: Rust, Linux, SLOs and All Things Performance at P99 CONF](https://cdn.thenewstack.io/media/2024/09/4c9cc0de-p99conf-1024x576.png)
P99 CONF is a free virtual conference that’s all about performance. Thousands of latency-obsessed engineers from around the world come together for P99 CONF each year. It’s purely technical, intentionally virtual, highly interactive and open source-focused.

[ScyllaDB](https://www.scylladb.com/) launched P99 CONF in 2021 to connect and foster the community of technologists who obsess over low-latency engineering, and it’s really caught on, thanks to many knowledgeable speakers sharing their optimization strategies, lessons learned and insights on what’s next for performance.
As we ramp up for P99 CONF 24 (more on that later), we thought it was a good time to share some of the most talked-about sessions from past P99 CONFs. You can also binge-watch more than 150 tech talks (free, ungated) in the [on-demand library](https://www.p99conf.io/on-demand/).

[Get a complimentary P99 CONF 24 conference pass](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000F15eY&campaign_status=Registered&utm_campaign=mp%20newstack%202024-10-23%20p99%20conf&utm_medium=the%20new%20stack&utm_source=marketing%20partner&lead_source_type=the%20new%20stack).
## Rust and Low-Latency Systems’ Future – Bryan Cantrill
No recap can do justice to the information-packed and impassioned keynote by [Bryan Cantrill](https://www.linkedin.com/in/bryan-cantrill-b6a1/), co-founder and chief technology officer at Oxide Computer Company.

In just 20 minutes, he took the audience on a history of computing to date, provided a blazing critique of where we are today, and gave the audience a glimpse of where the industry is heading next. We wrote it up in article format in “[Bryan Cantrill on Rust and the Future of Low-Latency Systems](https://thenewstack.io/bryan-cantrill-on-rust-and-the-future-of-low-latency-systems/),” but trust us — you want to watch the video for this one.

Here’s a tease: Cantrill’s conclusion, in his own words:

“Rust is actually the first language since C to meaningfully exist at the boundary of hardware and software. And this is what points us to the future.

“Wright’s Law means we’re going to have compute in more places. We are already seeing that. Those compute elements are going to be special-purpose. Don’t wait for your general-purpose CPU to be shoved down to a SmartNIC. It’s going to draw too much power. We can’t have memory that fast down there.

“But what we can put down there is Rust. Rust can fit into these places. We are going to see many more exciting de novo hardware-facing Rust systems that — thanks to no_std — will be able to build on one another.

“It’s a very exciting time to be developing high-performance low-latency systems, and the Rust revolution is very much here.”

## Whoops! I Rewrote It in Rust – Brian Martin
The scalability and efficiency of Twitter (now X) services relies heavily on high-quality cache offerings. The team there developed Pelikan as a caching system when Memcached and Redis didn’t fully meet their needs. Their No. 1 priority for Pelikan was “best-in-class efficiency and predictability through latency-oriented design and lean implementation.” This was initially achieved with a C implementation. However, two subsequent projects introduced Rust into the framework with rather impressive development speed.

When they decided to add TLS support to Pelikan, Twitter software engineer Brian Martin suspected it could be done faster and more efficiently in Rust than in C. But to gain approval, the Rust implementation had to match (or beat) the performance of the C implementation.

Initial prototypes with the existing Rust-based Twemcache didn’t look promising from the performance perspective; they yielded 25% to 50% higher P999 latency as well as 10% to 15% slower throughputs. Even when Martin doubled down on optimizing the Rust prototype’s performance, he saw minimal impact. After yet more frustrating performance test results, he considered several different implementation approaches. Fortunately, just as he was weighing potential compromises, he came across a new storage design that made it easier to port the entire storage library over to Rust.

Martin went all in on Rust at that point, with a simplified single-threaded application and all memory allocations managed in Rust. The result? The 100% Rust implementation not only delivered performance equal to — or exceeding — both the C implementation and memcached: It also improved the overall design and enabled coding with confidence thanks to “awesome language features and tools,” which Martin then dove into.

## Keeping Latency Low and Throughput High – Avi Kivity
Throughput and latency are in constant tension. ScyllaDB CTO and co-founder [Avi Kivity](https://x.com/AviKivity) focused his keynote on discussing how high throughput and low latency can both be achieved in a single application by using application-level priority scheduling.

Kivity began by outlining the stark contrast between throughput computing (OLAP) and latency computing (OLTP) and explaining the scenarios where it makes sense to mix these two types of jobs in a single application. When mixing is desired, two core actions are essential:

- Isolate different tasks for latency jobs and throughput jobs so you can measure and control them.
- Schedule them in a way that allows the latency jobs to be completed quickly, without interference from the throughput jobs.
But the devil is in the details. Do you take the common approach of isolating the tasks in threads and letting the kernel schedule them? It’s generally easier, but it doesn’t yield sufficient control or efficiency to achieve the optimal results.

The alternative is application-level task isolation. Here, every operation is a normal object and tasks are multiplexed on a small number of threads (ideally, one thread per logical core, with both throughput- and latency-sensitive tasks on the same thread). A concurrency framework assigns tasks to threads and controls the order in which tasks are executed. This means you can fine-tune everything to your heart’s content, but all that fine-tuning can be addictive, drawing your attention away from other critical tasks. More advantages: low overhead, simpler locking, good CPU affinity and fewer surprises from the kernel. It’s a less mature (though improving) ecosystem, but Kivity feels strongly that the extra effort required pays off immensely.

After visualizing what the execution timeline looks like, Kivity went into the finer details of switching queues, preemption techniques and using a stall detector. To wrap up, he explained how it all plays out in a real-world example: the ScyllaDB database.

## Misery Metrics and Consequences – Gil Tene
[Gil Tene](https://x.com/giltene)’s legendary “[oh sh*t](https://www.youtube.com/watch?v=nP1aK4DLu-k)” talk has prompted many engineers to rethink their approach to measuring P99 and similar latencies. But after obsessing over how to improve performance measurement for over a decade and seeing how distributed systems are evolving, Gil’s own approach to the topic has also evolved.
From “Dr. Strangelove” to “The Matrix” to sacrificial goats, Tene, co-founder and CTO of [Azul Systems](https://www.azul.com/?utm_content=inline+mention), took the audience on a journey that ranged from high latency peaks to a trough of measurement despair. He deconstructed what we’re really looking at with “all the pretty charts,” and, more importantly, what we’re missing. This talk will leave you wondering what’s really going on behind the charts you see across our event logos — and probably thinking quite a bit about the very idea of P99. At what seems to be the bottom of the trough of despair, Tene shows a rather terrifying example of how actions that improve performance on a chart can seriously undermine the end-user experience. Misery indeed.

But Tene remains confident that it is, in fact, possible to overcome the shortcomings of our accepted performance measurement methodologies, just not in the way he originally believed we could. There’s hope in misery. A light at the end of the tunnel. Rainbows, even (perhaps because Tene was joining us from Hawaii). As it turns out, engineers can prevent misery by learning to love misery. And if that doesn’t yet make sense to you, it’s time to grab the red pill and watch his session.

Bonus: Read more in “[If P99 Latency Is BS, What’s the Alternative?](https://thenewstack.io/if-p99-latency-is-bs-whats-the-alternative/)”

## From SLOs to ‘Game of the Year’ – Charity Majors
[Charity Majors](https://x.com/mipsytipsy) is known for her brutally incisive insights — and her P99 CONF keynote on service-level objectives (SLOs) was no exception. There’s a lot that latency-minded engineers can learn from gaming — where anything short of a flawless experience will undermine even the most imaginative design. That’s where tools and telemetry come into play. As Majors puts it, “It’s impossible to not have issues. But it is possible to find and fix issues before users notice. You really want this to be taken for granted by users.”
But how do you measure this experience? Following on the ugly P99 reality first introduced by Tene, then also probed by [Alex Hidalgo](https://www.p99conf.io/session/throw-away-your-nines/) and [Brian Taylor](https://www.p99conf.io/session/properly-understanding-latency-is-hard-what-we-learned-when-we-did-it-correctly/), Majors declares, “Aggregates are bullsh*t. Every individual experience counts. Any one player who can log in can start a sh*tstorm on the forums.” Your system might have four nines, but still…

- Everyone who logged in today might have had their state saved on an unresponsive shard — and think you are 100% down.
- Latency for logins might be timing out for everybody in certain regions.
- Upserts to payment might be failing upon registration.
- Effective observability is the hidden link between engineering experience and user experience.
According to Majors, “Without observability, you are really driving blind. You are careening down the freeway without your glasses on.” Observability should help you see what’s happening under the hood — to the point where you can debug your code, reconstruct any user’s experience and even understand new scenarios without shipping new code. It should help you move beyond “Is this broken?” to “How does this work and what is my user experiencing?” The better you get at that, the less you will experience breakages.

But how do you achieve this unicorn-like level of observability with games or other complex highly distributed systems that are:

- Deployed across multiple clouds, data centers and regions
- Designed and developed by a multitude of teams around the world
- Used across thousands of device types
- Prone to enormous concurrency issues and “thundering herds”
That’s something Majors has been tackling for years, leading to her latest adventure as “accidental startup founder” at [Honeycomb.io](https://www.honeycomb.io/?utm_content=inline+mention). Watch her keynote for a clear path forward, sharing her hard-fought lessons learned so you can deliver a user experience that’s all unicorns and rainbows.

## Using eBPF for High-Performance Networking – Liz Rice
[Liz Rice](https://x.com/lizrice), chief open source officer, Isovalent at [Cisco](http://cisco.com/?utm_content=inline+mention), walked attendees through how [Cilium](https://cilium.io/) (part of the Cloud Native Computing Foundation) improves throughput, frees up CPU usage and makes Kubernetes networking more efficient by using eBPF to bypass parts of the network stack.
Using XDP (eXpress Data Path), Cilium can run eBPF programs on the network interface card, enabling you to take advantage of eBPF as soon as a network packet arrives. For example, as Rice demonstrates, you could use eBPF as a very fast and efficient way to identify and discard “packets of death.” Notably, such a mitigation can be loaded dynamically, without installing a kernel patch or rebooting machines. And that’s just one case of how you can use eBPF to dynamically change the behavior of networking in a system.

eBPF can also be used for manipulating packets — for example, to change the source and destination addresses contained in the packets for load balancing. As a packet arrives, an eBPF XDP program can determine where to send it — on that host or to a different machine – without the packet being processed by the kernel’s networking stack. This enables impressive performance gains. (Exhibit A: Read how Seznam.cz achieved over two times better throughput and saved an “unbelievable amount of CPU usage” by [running an XDP-based load balancer vs. IPVS one](https://cilium.io/blog/2022/04/12/cilium-standalone-L4LB-XDP/).)

Looking beyond XDP, eBPF programs can be attached to a variety of different points in the network stack, and this is especially helpful when working with the complex networking stack of Kubernetes. As Rice’s demos, flame graphs and benchmarks show, this yields yet more opportunities for throughput and CPU gains. Watch the video and see the performance impact for yourself.

## Extreme HTTP Performance Tuning – Marc Richards
With over a decade of high-level performance tuning under his belt, [ Marc Richards](https://x.com/TalawahTech) recently tackled a low-level systems performance tuning project for an API server written in C. Reflecting on that adventure, his talk begins with three tips for anyone who’s curious about getting started with low-level performance tuning:

- You don’t need to be a kernel developer or wizard sysadmin; it requires curiosity and persistence, but you can absolutely learn as you go along.
- FlameGraph and
[bpftrace](https://opensource.com/article/19/8/introduction-bpftrace)have really changed the game, making the discipline much more approachable. - There are a number of new eBPF-based tools on the horizon that will make things even easier.
Shifting to the nuts and bolts of tuning, Richards outlined the nine optimization categories that he focused on for this system, which was already rather high performing from the start (1.32ms P999 and 224k requests per second).

In the “application optimization” category alone, he achieved a staggering 55% gain (to 347k requests per second). By fixing a simple coding mistake, he was able to get the application running on all available cores, delivering a 25% improvement. Using the right combination of GCC flags in compiling the framework and application resulted in a 15% boost. Updating the framework to use SEND/RECV calls instead of the more generic WRITE and READ added another 5%. Finally, he achieved an additional 3% increase by removing pthread overhead.

Richards continued to explain the various other optimizations he applied, carefully detailing why he decided to make each change and the performance improvement it delivered. The video covers the full range of optimizations, from perfect locality and interrupt optimizations to “the case of the nosy neighbor.” For an even deeper dive than Richards could provide in his 20-minute session, see his blog “[Extreme HTTP Performance Tuning: 1.2M API req/s on a 4 vCPU EC2 Instance](https://talawah.io/blog/extreme-http-performance-tuning-one-point-two-million/).”

## Join the Community for P99 CONF 2024
Just like the P99 CONF community, we’re obsessed with continually optimizing. And that brings us to P99 CONF 2024. Here’s a peek at what’s on the agenda:

**Gunnar Morling**: “1BRC – Nerd Sniping the Java Community”**Andy Pavlo**: “The Next Chapter in the Sordid Love/Hate Relationship Between DBs and OSes”**Amos Wenger (fasterthanlime)**: “Rust + io_uring + ktls: How Fast Can We Make HTTP?”**Michael Stonebraker**: “You’re Doing It All Wrong”**Jose Fernandez**: “Noisy Neighbor Detection with eBPF at Netflix”**Carl Lerche**: “Rust: A Productive Language for Writing Database Applications”**Tanel Poder**: “Using eBPF Off-CPU Sampling to See What Your Databases are Really Waiting For”**Bryan Cantrill**: To Be Announced**Avi Kivity**: “Designing a Query Queue for ScyllaDB”**Liz Rice**: “Zero-overhead Container Networking with eBPF and Netkit”
[Get a free pass for P99 CONF 24](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000F15eY&campaign_status=Registered&utm_campaign=mp%20newstack%202024-10-23%20p99%20conf&utm_medium=the%20new%20stack&utm_source=marketing%20partner&lead_source_type=the%20new%20stack).
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)