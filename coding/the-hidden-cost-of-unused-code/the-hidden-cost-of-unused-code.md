
<!--
title: 未使用的代码的隐藏成本
cover: https://cdn.thenewstack.io/media/2024/11/ed293088-xray.jpg
-->

移除冗余或废弃代码的阻塞，可以提高开发人员的生产力，缩短部署时间，降低维护成本和安全风险。

> 译自 [The Hidden Cost of Unused Code](https://thenewstack.io/the-hidden-cost-of-unused-code/)，作者 Frank Delporte。

想象一下，你的医生在年度体检时给你看了你的动脉扫描图。它显示，斑块多年来一直在积聚，你正走向中风，而你却从未感觉到即将到来的危险。你的心脏功能正在下降……你会因为还有很多其他事情要做而继续忽视这个问题吗？或者你会通过立即采取行动来调整你的生活方式并慢慢恢复来防止坏事的发生？

这正是你的应用程序中的代码可能发生的情况。

## 无声的积累

就像胆固醇会在我们的动脉中逐渐积累一样，未使用的代码也会随着时间的推移在我们的应用程序中悄无声息地积累。一个方法被另一个方法取代；一个功能不再使用；注释掉的代码被签入；还有一小段代码，没有人敢去碰……所有这些未使用的代码限制了构建、运行和维护应用程序所需的[开发人员时间和资源](https://thenewstack.io/its-time-to-build-some-empathy-for-developers/)：

- 需要为从未使用过的方法执行[单元测试](https://thenewstack.io/expedia-3-tips-for-more-effective-unit-testing/)。由于测试会检查未使用的代码，反馈循环会变得更长。当库发生变化或测试出现问题时，您需要调查问题并修复它。但最终，修复后的代码从未在生产中使用过。
- 开发人员经常发现，当他们不得不翻阅大量的遗留代码来实现一个简单的功能或追踪一个错误时，他们的热情会减退。他们在浏览不需要的代码时会分心。这会导致开发时间延长，因为您的团队需要绕过这些混乱的代码。
- 部署包变得更大，占用内存、磁盘空间和网络流量。
- 未使用的代码可能依赖于过时的库，从而引入安全风险。其中一些风险的严重性评分很高，急需解决方案。这样的修复需要优先于带来新功能的工作，而实际上并不需要修复，因为代码和 [依赖项](https://thenewstack.io/to-reduce-tech-debt-eliminate-dependencies-and-refactoring/) 根本没有被使用。


## 代码健康检查的时间

就像你的身体应该（并且需要）定期进行健康检查一样，你的代码库也应该（并且需要）进行同样的检查。使用正确的工具，您可以发现项目中最终可能导致“生产力阻塞”的“斑块积聚”。

有几个方面与未使用的代码积聚相关。一般来说，应用程序越大、越旧，参与其中的人就越多，闲置的代码也就越多。在监控了许多应用程序之后，大概的数字是接近 20% 的代码，在一些较大的应用程序中接近 66%。这不仅仅是外部依赖项；这些数字过滤了公司自己的软件包。通过删减这些未使用的代码，开发人员可以节省大量时间，不必在混乱的代码中导航，从而缩短 CI/CD 反馈循环。

## 采取小行动

处理未使用的代码不需要采取激烈的行动或进行重大的重构。相反，有一些方法可以在每个 sprint 中处理它，以降低问题并对清除代码阻塞产生很大的影响。

首先监控代码，以确定在短时间内哪些方法被使用，哪些方法未使用。在短暂的时间之后，您通常会确认对代码某些部分的怀疑；对于其他部分，您可能需要监控更长时间。

较小的团队不需要正式的弃用流程。首先选择未使用的包、类或方法。通过 Slack、午餐或任何你喜欢的方式告诉你的同事，这些代码将被删除。然后删除代码：红色差异是最好的差异。

不能与每个人交谈的大型团队可以使用更正式但仍然简单的流程。首先将代码标记为 `@Deprecated`，向团队成员和工具指示某个方法或类不打算使用。团队可以在方法中添加一个额外的日志记录语句，作为一种双重安慰。在你喜欢的时候应用额外的标志 `@Deprecated(forRemoval=true)`，然后在未来的更新中删除代码。在那之后不久，就该正式告别并删除代码了。

你的团队中大多数熟悉代码的成员都会对未使用的或不需要的代码有所了解。按照以下步骤，可以稳定地改进代码：

- **监控代码：** 找到监控代码的方法以发现未使用的部分，或者让你的团队审查它。
- **弃用：** 使用 `@Deprecated` 注解，我们可以标记候选移除的方法。
- **继续监控：** 构建工具会在仍然使用弃用方法时发出警报。
- **调整测试：** 重构报告使用了弃用代码的单元测试。
- **移除弃用代码：** 当监控没有发现任何问题时，你可以安全地移除它。
- **循环：** 不断重复此过程。清理具有悠久历史的大型项目需要一些时间。但是，此过程最终将使代码库更易于维护且更高效。

[Azul Intelligence Cloud 的代码清单](https://www.azul.com/products/intelligence-cloud/) 可以在监控步骤中为你提供帮助，它提供洞察信息来帮助你做出有关代码健康的明智决策。代码清单提供有关代码使用模式的详细洞察信息。你可以将其比作代码库的持续监控器，它可以准确地显示生产环境中正在使用的类和方法——对正在运行的应用程序的性能零影响。

通过这样一个良好的健康计划，你将实现更快的部署时间、更低的维护成本、更高的开发人员生产力、更低的风险以及更好的应用程序性能。

## 结论

就像你可能与健康专家合作来改善你的身体健康一样，Azul 也在这里帮助你改善代码健康。联系我们的销售团队，开始使用 Intelligence Cloud 并找到代码中未使用的部分。

立即开始。你的代码库的健康状况不容等待。
