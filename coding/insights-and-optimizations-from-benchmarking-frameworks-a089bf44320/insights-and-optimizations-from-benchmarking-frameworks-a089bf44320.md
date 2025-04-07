
<!--
title: 使用Go降低70%的基础设施成本
cover: https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997792/dr36gwmldhcgv0u1uycr.png
summary: Go性能炸裂！实测对比Go/Gin、Java/SpringBoot、Node/Nestjs等框架，Go在CPU、RAM占用上大幅领先，基础设施成本狂降70%！AOT编译、`Goroutines`、GC优化是关键。选型需综合考虑团队技术栈、功能需求和社区支持。
-->

Go性能炸裂！实测对比Go/Gin、Java/SpringBoot、Node/Nestjs等框架，Go在CPU、RAM占用上大幅领先，基础设施成本狂降70%！AOT编译、`Goroutines`、GC优化是关键。选型需综合考虑团队技术栈、功能需求和社区支持。

> 译自：[Insights and Optimizations from Benchmarking Frameworks](https://medium.com/@lucas01/insights-and-optimizations-from-benchmarking-frameworks-a089bf44320)
> 
> 作者：Lucas Borsatto

**总结:** 结果在本文底部的图表中；

在微服务架构中，应用具有饱和度和延迟等指标的可观测性是理解和提高应用程序性能的关键组成部分。虽然算法的选择和代码优化通常对这些指标有最显著的影响——你可以在 [Vercel](https://programming-language-benchmarks.vercel.app/) 等网站上查看跨语言的算法比较——但很少有参考文献探讨语言框架本身的效率。

本文旨在通过评估用 Java、Go、Kotlin 和 Node 实现的基本 REST Api，提供更广泛的基准测试视角。为此，我们将使用 [Benchmark API](https://github.com/lucasbsimao/benchmark-apis)，我开发它是为了测量饱和度和延迟指标，并探索我们将在本文中讨论的场景中可能的性能优化。

此基准测试中使用的代码位于此 [Github repo](https://github.com/lucasbsimao/benchmark-node-java-kotlin/tree/include_docker)，如果您是只想看结果的人，可以在文章末尾找到完整的结果。 这篇文章的灵感来自 [Toptal 上的另一篇文章](https://www.toptal.com/back-end/server-side-io-performance-node-php-java-go) 博客。

## 基准测试设置

该基准测试在 Docker compose 之上运行，您可以在项目的 [README 文件](https://github.com/lucasbsimao/benchmark-apis/blob/main/README.md)中看到更多相关说明。 PC 设置为：

- AMD Ryzen 7 5800H with Radeon Graphics 3.20 GHz
- 16,0 GB DDR4 3200 MHz
- 在 WSL2, Windows 11 中运行
- [Artillery](https://www.artillery.io/docs) 用于收集延迟指标

所有基准测试均使用以下 docker compose 配置运行：

```yaml
deploy:
  resources:
    limits:
      cpus: '6'
      memory: 8g
```

## 基准测试语言和框架

- Java/Spring Boot
- Java/Micronauts
- Java/Quarkus
- Kotlin/SpringBoot
- Node/Nestjs
- Go/Gin
- Go/Chi

## 基准测试 API 定义

由于这里的目标是收集请求延迟、CPU 和 RAM 使用情况，因此所有 API 的开发都遵循以下定义：

- 具有查询参数 N 的 Endpoint GET /benchmark
- 使用语言标准库读取 16kb 文件
- 一个 for 循环，交互 N 次，使用 SHA-256 哈希文件内容

Api 的示例请求是：

```bash
curl localhost:8080/benchmark?n=100
```

## Artillery 配置

该基准测试使用以下 Artillery 配置运行：

— Case 1

Warm up: Arrival rate of 150 users per sec for 60 seconds with N=800
Spike: Arrival rate of 300 users per sec for 60 seconds with N=800

— Case 2

Warm up: Arrival rate of 400 users per sec for 60 seconds with N=1
Spike: Arrival rate of 550 users per sec for 60 seconds with N=1

— Case 3

Warm up: Arrival rate of 150 users per sec for 60 seconds with N=10
Spike: Arrival rate of 300 users per sec for 60 seconds with N=10

# 结果

现在我们已经确定了基准测试的定义，我们将开始讨论每种语言/框架的一些结果。 最后，我们将对其中的佼佼者进行比较回顾。

## Node 结果

首先，我选择 NestJS 作为框架，因为它被广泛使用，并提供了一些优势，例如约定优于配置、控制反转和内置模块化。 在这里，我们将比较两种情况：一种是使用没有优化的带有 Express 的 NestJS，另一种是使用 Fastify 并入 [cluster](https://www.npmjs.com/package/cluster) 库的 NestJS。

让我们从 Artillery Case 1 的结果开始：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997813/nnshkr5zq6mydlxrlnvn.png)

考虑到我们通过采用 N=800 阻止了事件循环，因此可以预期利用多集群的应用程序会比具有单 CPU 核心的应用程序更好地处理它，尽管 CPU 和 RAM 图表表明了一些令人担忧的峰值。 但是，如果我们将场景转移到 Artillery Case 2，其中涉及更多的并发和更少的 CPU 使用率，该怎么办。 即使那样，我们也会期望优化的应用程序表现更好，对吗？ 好吧：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997831/ftmr2gc7kbjftqplkw3h.png)

在这里我们得到了第一个教训。 由于多个产生的进程以及我们请求的简单性质，主进程和工作进程之间的通信开销导致更多的 CPU 使用率，这超过了使用带有集群库的多个内核的优势。 鉴于 Node 已经针对 I/O 进行了优化，因此单线程应用程序在这方面表现更好。

考虑到这是一个临界情况，我们可以使用 Artillery Case 3 作为中间情况来确定更有效的方法。 这是结果：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997861/pwpdwqrmolmvvzgupu8w.png)

获胜者是使用集群 Fastify 的 NestJS。由此，我们得到了第二个教训：如果我们不关注技术或框架的局限性以及它可能引入的潜在性能瓶颈，那么技术或框架就无法成为解决方案。

当然，Node 通过 `--max-old-space-size` 等参数为我们提供了一些优化选项，以定义长期对象可以占用多少 RAM。

## Java/Kotlin 结果

对于 Java，我选择了一些最常用的框架：SpringBoot、Micronauts 和 Quarkus。

Artillery Case 1 的结果是：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997872/nrjwmlnzswqqzwsdtiy1.png)

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997881/p1bp3vwrrlnw2s9jcofa.png)

由于结果看起来彼此之间只有细微的差异，让我们检查一下 Artillery Case 2 的结果：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997894/sscvqscfn1xgrkxenhb9.png)

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997924/xo24gbvat1ekglmy15vs.png)

Quarkus 以微弱优势获胜。重要的是要注意，即使使用协程，Kotlin 也没有胜过其他语言。这可能是因为在请求期间实际上没有挂起协程的操作。正如前面提到的，某些语言特性的好处在更复杂的应用程序中往往更明显，在这些应用程序中会应用高性能算法。这适用于协程和其他使 Kotlin 比 Java 具有优势的特性。

另一个需要考虑的点是，此基准测试不包括 Ktor 框架，该框架可以突出显示 Kotlin 可以为 API 性能带来的一些优势。

最后，人们总是可以通过参数 `-Xms` 和 `-Xmx` 来提高 RAM 性能，或者使用 `-XX:+UseZGC` 将应用程序 GC 更改为性能更高的 GC。虽然，这在我们这样简单的 API 中不是必需的。

## Go 结果

Go 被认为是市场上性能最高的语言之一。这可能会让我们认为它在任何情况下都会胜过其他语言。是这样吗？在本节中，我们将回顾使用 Chi 和 Gin 的 Go 的基准测试结果，它们是两个最流行的 Go 框架。以下是 Artillery Case 1 的图表：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997936/jyauxykaq3l7yqq5iwo4.png)

好吧，看起来 Chi 确实胜过了其他框架，但这种情况对 Gin 不利。除了高 CPU 消耗外，延迟达到了 8 秒。当我们查看下面 Gin 的 Artillery 报告时，情况会变得更糟：

```
--------------------------------
Summary report @ 11:57:36(-0300)
--------------------------------
errors.ETIMEDOUT: ................................................. 23558
http.codes.200: ................................................... 3442
http.downloaded_bytes: ............................................ 6884
http.request_rate: ................................................ 210/sec
http.requests: .................................................... 27000
```

实际上，大多数请求都导致超时。由此，我们得出结论，Gin 在需要高 CPU 使用率的场景中可能会遇到困难，即使应用程序处理 800 次重复循环的情况确实不常见。

尽管第一个案例的结果如此，但 Artillery Case 2 的结果似乎更好一些：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997948/tpaq5ioaookbspx9x2fn.png)

Gin 取得了明显更好的结果，但此场景的明显赢家是 Chi。此外，Gin 似乎更能够处理更温和的场景。

为了进一步提高应用程序性能，可以尝试更改环境变量 `GOMAXPROCS`，该变量具有取决于服务器设置的默认值。

# 结果总结

以下是总结的最终结果。使用 Artillery Case 1：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997958/vq1z4fpwjjfrtnfodczx.png)

使用 Artillery Case 2：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1743997970/rkjduqakatubsjxleami.png)

# 结论

总而言之，Go 显然是此基准测试中性能最高的框架。正如您在之前的图表中看到的那样，它使用的 RAM 少 3 倍，CPU 少 4 倍，并且由于我们看到的延迟百分位数，我们甚至可以在生产环境中减少实例数量，从而显着降低基础设施成本。这有一些原因：

- 提前编译 (AOT)：Go 经过预编译并针对机器代码进行了优化，这使其速度非常快。但重要的是要注意，AOT 实现并不能保证优于 JIT 的性能。可以通过使用 Spring Native 运行此基准测试，并将结果与使用 JIT 的 Quarkus 或 Spring 的结果进行比较来观察到这一点。
- Goroutines：协程与线程具有相同的目的，但它们更轻量级，并且可以更轻松地挂起和恢复。可以比线程更频繁地创建协程，并且它们在 Go 的线程池之上运行。
- 垃圾回收：Go 中的 GC 旨在尽可能降低延迟。尽管 Java 在使用 G1 和 ZGC 的垃圾回收方面取得了重大改进，但 Go 的 GC 通常被认为比其竞争对手更快。

当然，为您的项目选择语言和框架应基于您团队的熟练程度、功能和性能要求，以及该语言和框架拥有的社区支持程度。