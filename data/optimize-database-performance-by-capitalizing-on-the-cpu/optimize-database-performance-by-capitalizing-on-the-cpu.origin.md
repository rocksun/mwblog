# Optimize Database Performance by Capitalizing on the CPU
![Featued image for: Optimize Database Performance by Capitalizing on the CPU](https://cdn.thenewstack.io/media/2024/10/88d35569-optimizedatabaseperformancecpu-1024x576.jpg)
A database’s internal architecture makes a tremendous impact on its latency and how much throughput it can handle. Being an extremely complex piece of software, a [database](https://thenewstack.io/databases/) doesn’t exist in a vacuum, rather it interacts with its environment, including the operating system and hardware.

While it’s one thing to get massive terabyte-to-petabyte scale systems up and running, it’s a whole other thing to make sure they are operating at peak efficiency. In fact, it’s usually more than just “one other thing.” Performance optimization of large distributed systems is usually a multivariate problem combining aspects of the underlying hardware, networking, tuning operating systems, or finagling with layers of virtualization and [application architectures](https://roadmap.sh/software-design-architecture).

Such a complex problem warrants exploration from multiple perspectives. Let’s look at ways databases can optimize performance by taking advantage of modern hardware [CPUs](https://thenewstack.io/the-hobbyists-who-build-their-own-cpus/).

When programming books say CPUs can run processes or threads, “runs” means there’s some simple sequential instruction execution. But then there’s a footnote explaining that with multiple threads you might need to consider doing some synchronization.

In reality, the way things are executed inside CPU cores is something completely different — and much more complicated. It would be very difficult to program these machines if we didn’t have those abstractions mentioned in books, but they are a lie to some degree — and how you can efficiently take advantage of CPU capabilities is still very important.

## Share Nothing Across Cores
Individual CPU cores aren’t getting any faster. Their clock speeds reached a performance plateau long ago. Now, the ongoing increase of CPU performance is horizontal: by increasing the number of processing units. In turn, increasing the number of cores means performance now depends on coordination across multiple cores (versus the throughput of a single core).

On modern hardware, the performance of standard workloads depends more on the locking and coordination across cores than on the performance of an individual core. Software architects face two unattractive alternatives:

- Coarse-grained locking, where application threads contend for control of the data and wait instead of producing useful work.
- Fine-grained locking, which, in addition to being hard to program and debug, sees significant overhead even without any contention due to the locking primitives.
Consider an SSD drive. The typical time needed to communicate with an SSD on a modern NVMe device is quite lengthy — it’s about 20 µseconds. That’s enough time for the CPU to execute tens of thousands of instructions. Developers should consider it a networked device but generally do not program in that way. Instead, they often use an API that is synchronous, which produces a thread that can be blocked.

Looking at the image of the logical layout of an [Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention) Xeon Processor, it’s clear that this is a networked device.

The cores are all connected by what is essentially a network — a dual ring interconnected architecture. There are two such rings, and they are bidirectional. Why should developers use a synchronous API for that? Since sharing information across cores requires costly locking, a shared-nothing model is perfectly worth considering. In such a model, all requests are sharded onto individual cores, one application thread is run per core, and communication depends on explicit message passing, not shared memory between threads. This design avoids slow, unscalable lock primitives and cache bounces.

Any sharing of resources across cores in modern processors must be handled explicitly. For example, when two requests are part of the same session and two CPUs each get a request that depends on the same session state, one CPU must explicitly forward the request to the other. Either CPU may handle either response.

Ideally, your database provides facilities that limit the need for cross-core communication, but when communication is inevitable, it provides high-performance non-blocking communication primitives to prevent degrading performance.

## Optimize Future-Promise Design
There are many solutions for coordinating work across multiple cores. Some are highly programmer-friendly and enable development of software that works exactly as if it were running on a single core. For example, the classic Unix process model is designed to keep each process in total isolation and relies on kernel code to maintain a separate virtual memory space per process. Unfortunately, this increases the overhead at the operating system level.

There’s a model known as “futures and promises.” A **future** is a data structure that represents some yet-undetermined result. A **promise** is the provider of this result. It can be helpful to think of a promise/future pair as a first-in, first-out (FIFO) queue with a maximum length of one item, which may be used only once. The promise is the producing end of the queue, while the future is the consuming end. Like FIFOs, futures and promises are used to decouple the data producer and the data consumer.

However, there are several considerations for optimizing implementations of futures and promises. While the standard implementation targets coarse-grained tasks that may block and take a long time to complete, optimized futures and promises are used to manage fine-grained, non-blocking tasks. In order to meet this requirement efficiently, they should:

- Require no locking
- Not allocate memory
- Support continuations
Future-promise design eliminates the costs associated with maintaining individual threads by the operating system and allows near-complete utilization of the CPU. On the other hand, it calls for user space CPU scheduling and very likely limits the developer with voluntary preemption scheduling. The latter, in turn, is prone to generating phantom jams in popular producer-consumer programming templates. To learn more, watch [Exploring Phantom Traffic Jams in Your Data Flows](https://www.youtube.com/watch?v=IXS_Afb6Y4o) or read the [corresponding article](https://www.scylladb.com/2022/04/19/exploring-phantom-jams-in-your-data-flow/).

Applying future-promise design to database internals has obvious benefits. First, database workloads can naturally be CPU-bound. That’s typically the case with in-memory database engines, and aggregates’ evaluations also involve pretty intensive CPU work. Even for huge on-disk data sets, when the query time is typically dominated by I/O, CPU should be considered. Parsing a query is a CPU-intensive task regardless of whether the workload is CPU-bound or storage-bound, and collecting, converting and sending the data back to the user also calls for careful CPU utilization.

And last but not least: Processing data always involves a lot of high-level operations and low-level instructions. Maintaining them in an optimal manner requires a good low-level programming paradigm, and future-promises is one of the best choices. However, large instruction sets need even more care; which leads us to execution stages.

## Execution Stages
Let’s dive deeper into CPU microarchitecture because database engine CPUs typically need to deal with millions and billions of instructions, and it’s essential to help the poor things with that.

In a very simplified way, the microarchitecture of a modern x86 CPU — from the [top-down analysis](https://perf.wiki.kernel.org/index.php/Top-Down_Analysis) point of view — consists of four major components: frontend, backend, branch speculation and retiring.

### Frontend
The processor’s frontend is responsible for fetching and decoding instructions that are going to be executed. It may become a bottleneck when there is either a latency problem or insufficient bandwidth. The former can be caused, for example, by instruction cache misses. The latter happens when the instruction decoders cannot keep up. In the latter case, the solution may be to attempt to make the [hotpath](https://en.wiktionary.org/wiki/hotpath) (or at least significant portions of it) fit in the decoded micro-operation (µop) cache (DSB) or be recognizable by the loop detector (LSD).

### Branch Speculation
Pipeline slots that the top-down analysis classifies as “bad speculation” are not stalled, but wasted. This happens when a branch is mispredicted and the rest of the CPU executes a µop that eventually cannot be committed. The branch predictor is generally considered to be a part of the frontend. However, its problems can affect the whole pipeline in ways beyond just causing the backend to be undersupplied by the instruction fetch and decode.

### Backend
The backend receives decoded µops and executes them. A stall may happen either because of an execution port being busy or a cache miss. At the lower level, a pipeline slot may be core bound, either due to data dependency or an insufficient number of available execution units. Stalls caused by memory can be caused by cache misses at different levels of data cache, external memory latency or bandwidth.

### Retiring
Finally, some pipeline slots are classified as “retiring.” They are the lucky ones that were able to execute and commit their µop without any problems. When 100% of the pipeline slots are able to retire without a stall, then the program has achieved the maximum number of instructions per cycle for that model of the CPU. Although this is very desirable, it doesn’t mean that there’s no opportunity for improvement. Rather, it means that the CPU is fully utilized and the only way to improve the performance is to reduce the number of instructions.

## Implications for Databases
The way CPUs are architected has direct implications on database design. Individual requests may involve a lot of logic and relatively little data, which is a scenario that stresses the CPU significantly. This kind of workload will be completely dominated by the frontend — instruction cache misses in particular. If you think about this for a moment, it isn’t very surprising. The pipeline each request goes through is quite long. For example, write requests may need to go through transport protocol logic, query parsing code, lookup in the caching layer or be applied to the in-memory structure where it will be waiting to be flushed on disk.

The most obvious way to solve this is to attempt to reduce the amount of logic in the hotpath. Unfortunately, this approach does not offer a huge potential for significant performance improvement. Reducing the number of instructions needed to perform a certain activity is a popular optimization practice, but a developer cannot make any code shorter infinitely. At some point, the code “freezes” — literally. A minimal amount of instructions is needed even to compare two strings and return the result. It’s impossible to perform that with a single instruction.

A higher-level way of dealing with instruction cache problems is called staged event-driven architecture ([SEDA](https://en.wikipedia.org/wiki/Staged_event-driven_architecture)). It splits the request-processing pipeline into a graph of stages, thereby decoupling the logic from the event and thread scheduling. This tends to yield greater performance improvements than the previous approach.

## What Else?
As a database user, it can be interesting to explore the database engineering decisions that help your database squeeze more power out of modern infrastructure.

But it’s not all about the CPU. How the database interacts with the operating system plus memory, storage and networking also matters, but those are outside the scope of this article.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)