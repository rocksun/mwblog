# Cutting 70% of Infra Costs with Go: A benchmark between Go, NextJS, Java and GraalVM
Source code for this article can be found [here](https://github.com/lucasbsimao/benchmark-apis).

[https://crl2020.imgix.net/img/cloud-report-footer.png](https://crl2020.imgix.net/img/cloud-report-footer.png?auto=format%2Ccompress&q=60&w=1185)
**TLDR:** The results are on the charts at the bottom of this article;
In the microsservices architecture, applying observability with metrics like saturation and latency is a key component to understand and improve application performance. While the choice of algorithms and code optimizations often have the most significant impact in these metrics — you can check algorithms comparison across languages on sites like [Vercel](https://programming-language-benchmarks.vercel.app/) — there are few references that explore efficiency of the language frameworks themselves.

This article aims to provide a broader benchmark perspective by evaluating a basic REST Api implemented in Java, Go, Kotlin and Node. To this end we will use [Benchmark API](https://github.com/lucasbsimao/benchmark-apis), which I developed to measure saturation and latency metrics and to explore possible performance optimizations in scenarios we will discuss here.

The code used on this benchmark is at this [Github repo](https://github.com/lucasbsimao/benchmark-node-java-kotlin/tree/include_docker), and if you are a TLDR person, full results can be found at the end of the article. This article was inspired by [another article on Toptal](https://www.toptal.com/back-end/server-side-io-performance-node-php-java-go) blog.

## Benchmark Setup
The benchmark was runned on top of Docker compose and you can see more instructions about it on the project’s [README file](https://github.com/lucasbsimao/benchmark-apis/blob/main/README.md). The PC setup is:

- AMD Ryzen 7 5800H with Radeon Graphics 3.20 GHz
- 16,0 GB DDR4 3200 MHz
- Runned in WSL2, Windows 11
[Artillery](https://www.artillery.io/docs)used to collect latency metrics
All benchmarks runned with following docker compose configuration:

`deploy:`
resources:
limits:
cpus: '6'
memory: 8g
## Bechmark languages and frameworks
- Java/Spring Boot
- Java/Micronauts
- Java/Quarkus
- Kotlin/SpringBoot
- Node/Nestjs
- Go/Gin
- Go/Chi
## Benchmark API definition
As the goal here is to collect requests latency, CPU and RAM usage, all APIs were developed following the definition below:

- Endpoint GET /benchmark with query parameter N
- 16kb file reading with the language standard lib
- A for loop interacting N times hashing the file content with SHA-256
Example request for the Api is:

`curl localhost:8080/benchmark?n=100`
## Artillery Configurations
The benchmark was runned with the following Artillery configurations:

— Case 1

Warm up: Arrival rate of 150 users per sec for 60 seconds with N=800
Spike: Arrival rate of 300 users per sec for 60 seconds with N=800

— Case 2

Warm up: Arrival rate of 400 users per sec for 60 seconds with N=1
Spike: Arrival rate of 550 users per sec for 60 seconds with N=1

— Case 3

Warm up: Arrival rate of 150 users per sec for 60 seconds with N=10
Spike: Arrival rate of 300 users per sec for 60 seconds with N=10

# RESULTS
Now that we placed the the definitions around the benchmark, we will start discussing some results per language/frameworks. At the end we will make a comparative review of the top performers among them.

## Node results
First, I chose NestJS as framework because it is widely used and offers some advantages like Convention over Configuration, Invertion of Control and built-in modularization. Here, we will compare two scenarios: one using NestJS with Express, without optimizations, and another NestJS using Fastify incorporating the [cluster](https://www.npmjs.com/package/cluster) library.

Let’s begin with the results from Artillery Case 1:

Considering that we blocked the event loop adopting N=800, it is expected that an application utilizing multi cluster would handle it better than one with single CPU core, although the CPU and RAM graphs indicate some concerning spikes. But what if we shift the scenario to Artillery Case 2, which involves more concurrency and less CPU usage. Even then, we would expect that the optimized app to outperform, right? Well:

And here we arrive at our first lesson. Due to the multiple spawned proccesses and the simple nature of our requests, the communication overhead between primary and worker proccesses leads to more CPU usage, which outweights the advantage of using multiples cores with cluster library. And given that Node is already optimized for I/O, the single-thread app outperforms in this one.

Considering this a borderline scenario, we can use Artillery Case 3 as an intermediary scenario to determine the more efficient approach. And here are the results:

The winner is then NestJS with clustered Fastify. And with that, we have our second lesson: a technology or framework will not be a solution if we don’t pay attention to its limitations and to the potential performance bottlenecks it may introduce.

And of course, Node gives us some optimization options through parameters like *--max-old-space-size* to define how much RAM long term objects can occupy.

## Java/Kotlin results
For Java, I selected some of most used frameworks: Spring Boot, Micronauts and Quarkus.

The results for Artillery Case 1 are:

As the results seem to differ only slightly from one another, let’s examine the results for Artillery Case 2:

And Quarkus is the winner here by a small margin. It’s important to note that Kotlin, even with coroutines, didn’t outperform others. This is likely because there’s no operation that actually suspends our coroutine during the request. As was mentioned earlier, the benefits of certain language features tends to be more perceptible in more complex applications where performatic algorithms would be applied. This applies for coroutines and other features that give Kotlin some advantage over Java.

Another point to consider is that this benchmark didn’t include Ktor framework, which could highlight some advantages Kotlin can bring to the API performance.

Finally, one always can improve RAM performance through parameters *-Xms* and *-Xmx*, or *-XX:+UseZGC* to change the application GC to a more performatic one. Although, it is not a requirement in such a simple API as ours.

## Go results
Go is recognized as one of the most performatic languages on the market. This might lead us to assume that it would outperform other languages in any scenario. Is it? In this section we will review the benchmark results of both Go using Chi and Gin, which are two of the most popular Go frameworks. Here are the graphs for Artillery Case 1:

Well, it looks like Chi has indeed outperformed other frameworks, but this scenario didn’t go well for Gin. Beyond the high CPU consumption, the latency reached 8 seconds. Things get even worse when we look at the Artillery report for Gin below:

`--------------------------------`
Summary report @ 11:57:36(-0300)
--------------------------------
errors.ETIMEDOUT: ................................................. 23558
http.codes.200: ................................................... 3442
http.downloaded_bytes: ............................................ 6884
http.request_rate: ................................................ 210/sec
http.requests: .................................................... 27000
Most of the requests actually resulted in a timeout. From this, we conclude that Gin can struggle in scenarios that require high CPU usage, even though it’s true that it’s unusual for an application to handle a loop of 800 repetitions.

Despite the results from the first case, the results from Artillery Case 2 appear to be somewhat better:

Gin achieved significantly better results, but the clear winner for this scenario is Chi. Besides, it seems like Gin is more capable of handling more moderated scenarios.

For further improvements in application performance, one can try changing the environment variable *GOMAXPROCS*, which has a default value that depends on the server settings.

# SUMMARY OF RESULTS
And here are the final results summarized. With Artillery Case 1:

And with Artillery Case 2:

# CONCLUSION
In summary, Go is clearly the most performatic framework on this benchmark. As you can see on the previous graphs, it uses 3 times less RAM, 4 times less CPU and, due to the latency percentiles we saw, we could even have less instances on the production environment, leading to significantly infra cost reduction. There are some reasons for this:

- Ahead of time compilation (AOT): Go is pre-compiled and optimized for machine code, what makes it very fast. But it’s important to notice that AOT implementation doesn’t guarantee superior performance over JIT. This can be observed by running this benchmark with Spring Native and comparing the results with those from Quarkus or Spring using JIT.
- Goroutines: coroutines have the same purpose to threads, but they are more lightweight and can be suspended and resumed with greater ease. Coroutines can be created more frequently than threads, and they operate on top of Go’s thread pool.
- Garbage Collection: GC in Go is designed to be as low latency as possible. Although Java has made significant improvements in garbage collection with the G1 and ZGC, Go’s GC is generally considered faster than its competitors.
But of course, the choice of language and framework for your projects should be based on your team’s proficiency, functional and performance requirements, and in how much community support does that language and framework have.