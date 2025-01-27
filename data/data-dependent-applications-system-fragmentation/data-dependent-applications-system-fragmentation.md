
<!--
title: 探索数据依赖型应用的必然未来
cover: https://cdn.thenewstack.io/media/2025/01/55ee1a46-pankaj-patel-byiw48klbmw-unsplash-scaled.jpg
-->

何不跳过系统碎片化，而使用单一技术平台？

> 译自 [Exploring the Inevitable Future of Data-Dependent Applications](https://thenewstack.io/data-dependent-applications-system-fragmentation/)，作者 Stephen Goldberg。

数据是现代应用的生命线。查看天气、玩在线游戏或规划旅行路线——这些流行的应用程序都依赖于数据。

最简单的形式，天气应用程序只是一个设计用于获取、处理和存储数据以供不同位置的各种用户快速、高吞吐量检索的[数据应用程序](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)。

在线游戏尽可能多地使用本地数据存储，但仍然依赖于与其他玩家实时共享游戏中的位置、动作和统计数据。这使得游戏数据比天气数据更具动态性，因为它可能需要每秒 20 多次更新才能以快速读/写方式分发，但仅限于相对较少数量的玩家。同时，路线规划需要[数据和大量的服务器端计算](https://thenewstack.io/cloud-native-computing-now-has-its-own-file-system-cubefs/)。

数据需求（位置、所需速度和所需计算量等因素）会影响数据应用程序的设计和基础设施决策。

内容分发网络 (CDN) 是否足够，或者此应用程序是否需要超大规模计算的计算能力？

如果延迟很重要——通常情况下是这样——则需要靠近边缘的地理分布式部署，并且使用消息总线技术复制数据变得至关重要。

由于完全的数据复制不切实际，数据库通常在原始数据库和边缘的缓存版本之间进行拆分。所有这些[数据随后通过来自 Web 服务器的 HTTP API 查询交付](https://thenewstack.io/openais-chatgpt-now-formats-output-to-developer-queries/)——选择您的供应商。

## 系统碎片化之愚

支撑现代应用程序的技术堆栈需要仔细协调各种组件以实现最佳性能和成本效率。由于许多地方都有这么多部分，因此通常以可维护性换取性能。

随着应用程序需求的变化，复杂的技术堆栈会逐渐衰退，导致底层架构不适合其用途——无法满足应用程序不断变化的需求。

开发人员通常专注于优化堆栈的某一部分以克服碎片化系统的性能挑战。这可能涉及替换数据库或添加 Redis 层。但是，这种熟悉的做法忽略了一个巨大的问题并助长了它。连接多种技术以创建复杂、笨重的系统效率低下。

## 复杂性导致低效率

当今企业技术堆栈面临的主要挑战是复杂性。

为了提供用户体验，[应用程序提供商在服务器和区域之间部署](https://thenewstack.io/security-considerations-for-api-driven-apps-deployed-to-cloud/) API、数据库、缓存和消息传递系统，从而增加了技术堆栈的复杂性，并随之带来了更多问题：

- 需要管理的内容很多——增加了延迟和成本，同时限制了吞吐量。
- 它需要序列化和网络连接等中间过程，这些过程会消耗大量资源。
- 它创建了一个生态系统，云提供商有动力保持系统的复杂性。

## 统一方法开启 Web 性能新时代

与其组合 MongoDB、Redis、Kafka 和应用程序服务器等技术，为什么不跳过[系统碎片化并使用单一](https://thenewstack.io/nvm-manage-multiple-versions-of-node-js-on-a-single-system/)技术平台？只有代码才能使这些系统运行，那么为什么不只为一个系统编写代码呢？

想象一下，将 API、缓存和数据库功能组合到服务器上的单个进程中。这将消除每种技术之间各层资源消耗的逻辑、序列化和网络进程，从而导致极低的响应时间。此类高性能应用程序将获得更高的参与度、用户满意度和收入。

但是规模呢？像上述平台这样的统一系统如何管理 PlayStation 或 AccuWeather 的沉重负载？高效的消息总线还需要同步[地理分布式节点之间的](https://thenewstack.io/analytics-in-2022-means-mastery-of-distributed-data-politics/)数据。

现状——单独的缓存、计算、数据库和同步——对于全球规模的应用程序交付不再有意义。它过于复杂、低效且成本高昂。
具有几乎无限水平扩展能力、高冗余性和低网络延迟的单一系统是未来。它将促进更流畅的开发、更少的错误和缓存，以及轻松的维护——即使应用程序需求发生变化。

听起来不错，对吧？
