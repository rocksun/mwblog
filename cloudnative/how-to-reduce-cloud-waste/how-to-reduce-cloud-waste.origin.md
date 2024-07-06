# How To Reduce Cloud Waste
![Featued image for: How To Reduce Cloud Waste](https://cdn.thenewstack.io/media/2024/07/ed26b8eb-clouds-1024x576.jpg)
For most applications today, saying you host them in your own data center will be like saying you generate your own electricity. Why pay all that capex to provision enough hardware to cover your peak loads, which may only happen once a year, and then spend the opex to power and cool those machines as well as maintain them? Just let someone like [Amazon](https://aws.amazon.com/?utm_content=inline+mention), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) or [Google ](https://cloud.google.com/?utm_content=inline+mention)do that for you, and only pay for what you use as you do with your electricity bill.

This is the promise of cloud computing: a utility-based pricing model with lower bills to run your mission-critical enterprise applications.

Unfortunately, the reality often turns out to be different, and people find that moving to the cloud costs them more than hosting on-premises. How can this be and how can we address this?

Let’s look specifically at JVM-based applications [using Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/). However, many other languages, like [Kotlin](https://thenewstack.io/angular-18-kotlins-new-compiler-astro-adds-react-19-support/), [Scala](https://thenewstack.io/scala-creator-proposes-lean-scala-for-simpler-code/) and [Clojure](https://thenewstack.io/the-new-stack-makers-adrian-cockcroft-on-sun-netflix-clojure-go-docker-and-more/), can also be compiled for the JVM.

The modern approach to architecting cloud-based applications is to [use microservices](https://thenewstack.io/microservices/). Rather than developing a single, monolithic application, we break the application into discrete services that can be loosely coupled yet highly cohesive. In doing this, when one service becomes a bottleneck to performance, we can spin up new instances of that service, load balance usage and eliminate the bottleneck without needing to change other parts of the system.

This is where one of the core pieces of functionality of the JVM can lead to wasted cloud resources.

To deliver on the promise of “write once, run anywhere*,”* Java applications compile to bytecodes*,* the instructions of a virtual machine, rather than a specific processor. When a Java application starts, the JVM will profile it and identify frequently used code hot spots that can be compiled into native code. This just-in-time (JIT) compilation delivers excellent performance as the JVM knows precisely how the code is being used and can optimize it accordingly.

However, the time it takes for all the frequently used sections of code to be identified and compiled, which is actually a more complex, multistage process, can be longer than desired. This warmup time, as it is referred to, is not generally an issue for long-running processes like web or application servers. Microservices can start and stop frequently to dynamically respond to load variation. Waiting for a microservice to warm up before it can deliver full carrying capacity reduces the benefits of this approach.

A frequently used solution is to start multiple instances of a service and leave them running so that they are ready to deliver full performance immediately when required. This is obviously very wasteful and incurs unnecessary cloud infrastructure costs.

How can we solve this problem?

One approach is to use ahead-of-time (AOT) compilation. Rather than using JIT compilation, all code is compiled directly to native instructions. This eliminates warmup entirely, and the application starts with the full level of performance available.

Although this sounds like the ideal solution, it does not come without cost and limitations.

AOT compiles code without knowing how it will actually be used, limiting the potential for optimization. JIT compilation has profiling information that enables optimizations tailored precisely to the way the application is being used. Typically, this results insignificantly better overall performance.

For ephemeral microservices, so-called serverless computing, AOT delivers definite benefits. For any service that will run for at least a few minutes, JIT will result in better performance and, therefore, lower cloud computing costs.

An alternative solution is one that Azul has implemented as part of its Platform Prime high-performance Java runtime. This includes ReadyNow warmup-elimination technology.

The problem, as we have seen, is that each time we start an instance of a microservice, the JVM must perform the same analysis to identify hot spots, gather profiling information and compile them to native code. This happens even when we have used that microservice in the same way many times before. With ReadyNow, the service is started and allowed to warm up in production using real-world requests, not simulated ones. When the service is fully warmed up ( has reached its optimum level of performance), a profile is collected. This profile includes all the information required to obtain that level of performance: a list of hot spots, profiling data and even compiled code.

When the service needs to be started again, the profile is provided as part of the execution parameters. The JVM uses the profile to ensure that when it is ready to handle the first transaction, performance will be almost at the level it was when the profile was taken (it’s around 98% as some technical limitations on how the JVM works prevent the delivery of 100%).

The result is almost all warmup time is eliminated, while retaining all the performance benefits of JIT compilation. This system provides complete flexibility since different profiles can be used for the same service, depending on when and where the service is in use. For example, the workload profile may be very different on a Monday morning to a Friday afternoon. Multiple profiles can be stored, and the appropriate one can be selected when required.

Now that JVM-based microservices can have minimal warmup time, there is no need to maintain a pool of services sitting idly in the background. This can significantly reduce cloud waste.

A performance-optimized JVM that also includes an alternative memory management system, eliminating the latency for transactions typically associated with this is a great option. The JIT compilation system has also been improved to deliver higher throughput. Rather than reducing cloud waste, these simply reduce the cloud resources required to provide the same carrying capacity. The effect is to lower cloud costs even further.

Let’s look at an example of how this worked for a real customer. [Supercell](https://supercell.com/en/) is a company that runs some of the biggest online multiplayer games in the world. For the recent release of Brawl Stars, it was experiencing delays when spinning up new servers as the JVMs were compiling the required code. By switching to Azul Platform Prime, and exploiting ReadyNow, it was able to deliver much more consistent load-carrying capacity, reducing game lag, and reducing CPU usage by 20 to 25% for the same workload.

Clearly, a JVM that runs faster code means fewer cloud resources are needed.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)