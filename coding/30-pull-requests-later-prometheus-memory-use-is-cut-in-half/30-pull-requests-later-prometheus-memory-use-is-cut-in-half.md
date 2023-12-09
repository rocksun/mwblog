<!--
title: 30次PR实现Prometheus内存使用减半
cover: https://cdn.thenewstack.io/media/2023/12/139fdbb3-kubecon-bboreham-1024x782.jpg
-->

Grafana实验室杰出工程师Bryan Boreham在KubeCon大会上，详细讲解了他是如何对Prometheus进行优化，将其内存使用量减少了一半

> 译自 [30 Pull Requests Later， Prometheus Memory Use Is Cut in Half](https://thenewstack.io/30-pull-requests-later-prometheus-memory-use-is-cut-in-half/)，作者 B. Cameron Gain 是 ReveCom Media 的创始人和首席分析师。他对计算机的痴迷始于在20世纪80年代初在当地的视频游戏厅里修改《太空侵略者》控制台，可以一天花费25美分玩一整天。然后...

Prometheus的内存消耗是观测监控系统可能导致系统崩溃的众多方式之一。

Grafana Labs的杰出工程师[Bryan Boreham](https://www.linkedin.com/in/bryanboreham/?originalSubdomain=uk)在KubeCon+CloudNativeCon的演讲中详细介绍了他在尝试各种方法的过程中最终减少[Prometheus](https://thenewstack.io/know-the-hidden-costs-of-diy-prometheus/)内存使用的经验。他的演讲标题是“Prometheus如何将内存使用减半”，主要探讨了Prometheus的研究，特别是标签的内存消耗，揭示了减少内存使用的方法。

根据[Prometheus的文档](https://prometheus.io/docs/practices/naming/#:~:text=queue%20is%20not.-,Labels,%22extract%7Ctransform%7Cload%22)，标签用于区分正在测量的事物的特征：

- **api_http_requests_total** – 区分请求类型：operation=”create|update|delete”
- **api_request_duration_seconds** – 区分请求阶段：stage=”extract|transform|load”

Boreham的工作也体现了开源精神，展示了贡献如何带来实质性的结果。在两年的时间里，他向[监控系统项目](https://prometheus.io/)提交了30个拉取请求，涉及超过2500行代码更改，Boreham的工作帮助最新版本的Prometheus使用了之前版本一半的内存。

“这是一条漫长的道路，但最终非常令人满足，”Boreham在[KubeCon+CloudNativeCon](https://thenewstack.io/kubecon-2023-managing-pets-cattle-and-starfish/)之后告诉The New Stack。“有数十万个Prometheus服务器在运行，通过降低内存需求，我们降低了运行它们和它们的碳足迹的成本。”

## Go的内存分析器

![](https://cdn.thenewstack.io/media/2023/12/7be735d2-capture-decran-2023-12-05-164204.png)

[Go编程语言](https://thenewstack.io/how-golang-evolves-without-breaking-programs/)在其运行时中内置了一个性能分析器，可以提供 Prometheus 内存消耗（以及 CPU 使用）的内存分解，Boreham 在他的演讲中解释道。它提供了一种被称为 flame graph 视图的可视化方式。方块的宽度表示正在使用的内存比例。图表顶部显示了100%，总计6.7 GB 的内存消耗，Boreham 表示。

在图表中，出现了所谓的锯齿效应。这是垃圾随时间积累，然后被收集，因此内存急剧下降，然后再次积累的过程，Boreham 告诉 The New Stack。“这就是锯齿效应，” Boreham 说。

“Go内存分析器报告的是在上一次垃圾收集时的内存使用情况，所以在这个图中你永远看不到垃圾。很多人认为，‘哦，它可能主要是垃圾，我不需要考虑它，’” Boreham 说。“但是在Go的分析中，这永远不是垃圾。这是锯齿底部，是无法丢弃的内容。”

减小内存消耗的过程“始于问，‘那是什么让它这么大？’” Boreham 说。“但总的来说，当时的赢家几乎占据了 Prometheus 内部所有内存的三分之一（在这个图表中为31%），” 他说。

## Prometheus标签的问题

![](https://cdn.thenewstack.io/media/2023/12/227c0cd0-capture-decran-2023-12-05-164529.png)

在Prometheus中，每个series都通过这个名称-值对集合进行唯一标识，Boreham解释道。“如果你有另一个与之相关的series，而它们之间唯一的区别就是方法，实际上你就会得到一个全新的字符串集，层层叠叠，”Boreham说。“所以，你看着这个并说，‘哦，这很愚蠢。我只有一个字符串的拷贝，’但事情并没有那么简单。”

![](https://cdn.thenewstack.io/media/2023/12/0bb427da-capture-decran-2023-12-05-164845.png)

上面的图表显示了其中的数据结构。指向所有标签的切片头部占用24字节，每个字符串都有一个字符串头部，占用16字节。“它是内容的指针和一个长度，”Boreham说。“如果你把它们都加起来，结果会发现在数据结构中所有这些指针的大小要比字符串本身大得多。”

通过[Prometheus PR 10991](https://github.com/prometheus/prometheus/issues/12230)，Boreham将所有字符串放入单个字符串中，并使用长度进行编码：

![](https://cdn.thenewstack.io/media/2023/12/dd0350b1-capture-decran-2023-12-05-165241.png)

![](https://cdn.thenewstack.io/media/2023/12/ca99eadc-capture-decran-2023-12-05-165506.png)

![](https://cdn.thenewstack.io/media/2023/12/c6d4866d-capture-decran-2023-12-05-165652.png)

“这花了一年的时间和2500行代码的更改，因为有很多代码只是假设自己知道那个数据结构是什么样的，”Boreham说。

在Prometheus 2.74.2中，而以前的版本在内存消耗达到17GB时会崩溃，Boreham运行了2.47.2，内存消耗为13.1GB，没有发生事故：

![](https://cdn.thenewstack.io/media/2023/12/7f74d607-capture-decran-2023-12-05-165921.png)

![](https://cdn.thenewstack.io/media/2023/12/58f63e6e-capture-decran-2023-12-05-170223.png)

虽然在2.47.2中添加了对样本和本地直方图特性的处理，“它们并没有真正使用掉所有的内存，”Boreham说，尽管内存消耗大幅减少，但还没有达到50%的标志。

Boreham随后在2.39版本中找到并修复了一个bug：事务隔离环，Boreham表示在某些条件下，“在过去会变得异常庞大。”“但我做了计算，内存消耗仍然没有完全减半”：

![](https://cdn.thenewstack.io/media/2023/12/a9c2cb21-capture-decran-2023-12-05-170527.png)

![](https://cdn.thenewstack.io/media/2023/12/11b9ccaf-capture-decran-2023-12-05-170654.png)

Bug修复将内存消耗降至10GB：

![](https://cdn.thenewstack.io/media/2023/12/0d84eae9-capture-decran-2023-12-05-171021.png)

Boreham继续研究Go分析器，以定位最大的内存消耗元凶。

“你选取最大的数字，处理它，如果可以找到其中的一些低效性，然后再做一次。现在原来的第二大数字现在变成了最大的数字，”Boreham说。“一开始并不是那么大的数字现在变成了大数字。所以这是一个不错的自我强化的过程。”

这是2.47版本加上上面图表中的所有PR的总和，共8.6GB的内存消耗，几乎达到了50%的减少标志：

![](https://cdn.thenewstack.io/media/2023/12/990922c5-capture-decran-2023-12-05-171204.png)

![](https://cdn.thenewstack.io/media/2023/12/e7635e96-capture-decran-2023-12-05-171248.png)

如Boreham解释的那样，Go运行时有一个称为GoGC的参数，默认值是100。锯齿的大小增长到锯齿底部的大小的100%，即7GB。“对于那些有100GB Prometheus的人，它增长了50GB，但出于维护的目的，你不需要50GB的垃圾来运行一个有效的堆，”Boreham说。“你可以调整这个数字 — 它是一个环境变量，你可以设置它，它将增长到你设置的百分比，超过它降到的最小值，然后进行垃圾收集，速度会稍微加快。”

自此以后，Prometheus运行时的内存为8GB — 内存消耗已经达到了50%的标志。Boreham达到了他的目标：

![](https://cdn.thenewstack.io/media/2023/12/db19ee80-capture-decran-2023-12-05-171335.png)

![](https://cdn.thenewstack.io/media/2023/12/78f8d446-capture-decran-2023-12-05-171510.png)

Prometheus 用户们必然会欣赏更低的内存消耗，而大多数人可能对如何实现这一点不太感兴趣。

但对于那些喜欢为开源社区贡献的人来说，Boreham 的努力展示了如何通过大量的工作和耐心，制作可以产生实质影响的拉取请求（PR）。尽管事后看起来 Boreham 的工作似乎很简单，但显然并非如此 — 这在数学和科学研究中经常发生。Prometheus，以及一般的开源项目，为用户和对计算感兴趣的人提供了一个产生影响的机会。

“真的是出于热爱的努力，” Boreham 告诉 The New Stack。“让计算机程序变得更小更快对我来说有点痴迷，所以能够在这样一个受欢迎且广泛使用的项目中付诸实践真是太棒了。而且，在 Grafana Labs，‘开源就在我们的基因中。’”

