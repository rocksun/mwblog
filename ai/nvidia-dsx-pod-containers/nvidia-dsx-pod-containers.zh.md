英伟达希望全新的AI算力能够以完全内置的形式出现在数据中心中。周三在柏林举行的GTC大会上，该公司推出了 DSX POD，这是一个集装箱参考设计，合作伙伴可以在集装箱离开工厂前，将 [Vera Rubin racks](https://thenewstack.io/future-proof-ai-infrastructure/)、网络和液冷系统填充进去。

英伟达表示，在传统数据中心中安装和连接机架可能需要几个月的时间。但是，只要场地已经具备必要的电力、冷却和网络连接（公平地说，这些往往也是瓶颈），DSX POD 最快可在 14 天内准备好分发 Token。

这里的理念是让数据中心运营商更快地实现价值，因为正如英伟达创始人兼首席执行官黄仁勋在一份声明中所说：“AI工厂在开始产生 Token 时创造价值——而不是在建设完成时。”

## 箱子里有什么

每个容器容纳七个 [Vera Rubin NVL72 racks](https://thenewstack.io/spacex-nvidia-orbital-ai/)，即 504 个 Rubin GPU。英伟达超大规模和高性能计算副总裁 Ian Buck 在发布会前的吹风会上表示，单个单元包含约 1000 万个组件，重约 28 公吨。

这些集装箱还预先安装并测试了大约 20 公里长的铜缆和 17 公里长的横向扩展网络。Buck 说，一旦集装箱运达，施工人员就会将其固定到位，将其与邻近设备连接起来，并运行最后的预热老化测试。

## 水资源利用

Buck 还指出，英伟达将该系统设计为不使用水进行冷却。英伟达表示，Vera Rubin 可以使用高达 45 摄氏度的冷却液运行，因此干式冷却器（其工作原理与汽车散热器非常相似）可以替代蒸发冷却塔，而蒸发冷却塔[至今仍是许多数据中心的标准配置](https://eenews.net/articles/ais-no-win-choice-using-huge-amounts-of-water-or-energy)。

在另一项 DSX 宣布中，英伟达解释说，在最热的日子里，某些气候条件下的运营商可能仍然需要冷水机组。对于 2 吉瓦的部署，该公司估计，与冷却塔相比，干式冷却每天可以节省约 5400 万升水。

## 箱中的数据中心

这种容器中的服务器可能会让人感觉有点熟悉，确实，科技公司喜欢使用容器，即使有时这更多是一种宣传噱头，而不是解决实际问题的方案。

例如，早在 2006 年，Sun Microsystems 就推出了 [Project Blackbox](https://en.wikipedia.org/wiki/Sun_Modular_Datacenter)，这是一个 20 英尺集装箱中的数据中心。十年后，时任 AWS 首席执行官 Andy Jassy 在 re:Invent 2016 主题演讲的最后，让一辆 18 个轮子的卡车将 [Snowmobile](https://www.cnbc.com/2024/04/17/aws-stops-selling-snowmobile-truck-for-cloud-migrations.html)（一个可以运输 100 PB 数据的 45 英尺集装箱）开到了舞台上。

此后，微软和 AWS 为[灾区](https://www.infoq.com/news/2020/11/azure-modular-datacenter/)和[军事任务](https://aws.amazon.com/about-aws/whats-new/2023/02/aws-modular-data-center-mdc-us-department-defense-customers)构建了集装箱式数据中心。

然而，所有这些都与英伟达在这里所做的不一样。DSX POD 基本上是可以插入数据中心的预制部件。Buck 将其描述为构建新AI工厂的积木。

[Armada](https://armada.ai/product/galleon) 已经销售集装箱式边缘数据中心，它是构建这些系统的 17 个合作伙伴之一，其他合作伙伴还包括 Bull、Dell、HPE、Schneider Electric 和 Vertiv。

英伟达表示，合作伙伴将从 2027 年初开始在全球范围内交付 DSX POD 系统。