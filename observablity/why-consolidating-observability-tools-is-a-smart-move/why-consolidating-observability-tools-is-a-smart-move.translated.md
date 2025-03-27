# 为什么整合可观测性工具是明智之举

![Featued image for: Why Consolidating Observability Tools Is a Smart Move](https://cdn.thenewstack.io/media/2025/03/efa4644e-gamze-senturk-xgj_gnpcpoi-unsplash-1024x683.jpg)

[Gamze Şentürk](https://unsplash.com/@delikosesi?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/grayscale-photo-of-binoculars-on-the-ground-Xgj_GNPcPOI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

随着业务的更多方面变得数字化和复杂化，可观测性已经从锦上添花变成了绝对必需品。它保持系统平稳运行，用户满意，并推动业务前进。但说实话 - 如果您依赖各种工具来监控指标、事件、日志和追踪（MELT），您可能会感到有些压力。

企业[组织正在集中可观测性](https://thenewstack.io/what-observability-should-do-for-your-organization/)工作，并意识到最初看起来易于管理的分散的可观测性工具正在出现裂缝。数据孤岛、运营难题、缺乏标准、集成复杂性和成本膨胀只是可观测性工具增长带来的一些挑战。这就像试图用胶带修理漏水的管道一样 - 效率低下、成本越来越高，而且并不完全万无一失。

**可观测性成本：房间里的大象**

可观测性不仅复杂，而且成本高昂。2022 年，Datadog 在一次财报电话会议中透露，单个客户每年在可观测性工具上花费 6500 万美元。这个数字引发了关于成本上升和当前方法的可持续性的[讨论](https://thenewstack.io/real-talk-why-is-datadog-so-expensive/)。

一位观察员[指出](https://www.rtinsights.com/why-legacy-observability-tools-are-so-expensive/)，一些供应商建议将高达 30% 的总基础设施成本分配给可观测性工具。对于许多组织来说，这是一个不可持续的成本。虽然确保系统弹性至关重要，但分散的可观测性工具的财务压力限制了对其他领域的投资，迫使团队做出可能损害整体性能的权衡。

在 2025 年，更多的组织将通过更加谨慎地对待哪些应用程序需要可观测性平台的全部功能、探索开源和低成本的商业替代方案、改进其成本估算和预算流程以及与现有供应商谈判有利的条款来寻找降低成本的方法。

**简化、精简、成功**

[2024 年 SRE 报告](https://www.catchpoint.com/asset/2024-sre-report)发现，许多大型企业使用超过五种应用程序性能管理 (APM) 工具来监控其 IT 基础设施。

分散的工具使故障排除更加困难，减慢了团队的速度并增加了成本。[整合提供了一条明确的前进道路](https://thenewstack.io/duplication-not-consolidation-the-path-forward-for-apps/)，使组织能够集中其可观测性工作并优化工作流程。统一的可观测性平台不仅简化了流程，还打破了孤岛，加快了解决时间并加强了协作。

像 Open Telemetry 这样的开放标准进一步放大了这些好处，使团队能够集成不同的系统而不会被锁定在单个供应商中。这种灵活性确保了[可观测性策略在基础设施发展过程中保持面向未来](https://thenewstack.io/pulumi-templates-for-genai-stacks-pinecone-langchain-first/)。

考虑一下[航空公司基准报告](https://resources.catchpoint.com/hubfs/Website%20Assets%20-%20Briefs%2c%20EBooks%2c%20etc/Catchpoint%20Airline%20Website%20Performance%20Benchmark%20Report%20-%20July%202024.pdf?_gl=1*1hbn9rs*_gcl_au*MTI1MzMzMTM5MC4xNzI5NjMxMDkz)中的发现：采用整合的、现代化的可观测性解决方案的公司经历了更少的服务中断和更快的恢复时间。这些组织不仅仅是监控性能，他们还在积极地设计弹性。

**过度依赖 MELT 的挑战**

但问题是：传统的可观测性模型只能为您提供部分信息。他们一直在使用专注于 MELT 的 APM 平台，因为这是过去 30 年来该行业一直在做的事情。IT 运维团队经常淹没在数据中，但仍然视而不见。我们似乎相信，如果我们能获得更多的数据、更多的日志、更多的指标，我们就能找到答案。但是，如果[问题不是数据的数量](https://thenewstack.io/why-supply-chain-disruptions-are-a-data-problem/)，而是我们正在寻找错误的答案呢？
当然，MELT 非常适合跟踪内部应用程序指标，但在当今世界，大多数应用程序都是混合的、面向服务的和分布式的，这需要了解它们的依赖关系，包括连接性、ISP、云服务、第三方 API、CDN 等。这些外部因素在确保流畅的用户体验方面都起着至关重要的作用，但通常不属于[传统可观测性](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/)堆栈的范围。

现代可观测性团队将其传统的 APM 工具与互联网性能监控 (IPM) 相结合，以获得必要的由外而内的视角，从而了解真实世界的客户体验并有效地管理外部依赖关系。当与 APM 结合使用时，IPM 使团队能够获得完整的可见性，从而主动检测和解决问题。

**集中式可观测性治理的趋势**

大型企业中日益增长的趋势是创建一个中央监控团队，为多个公司部门提供服务，或者至少为分布式[监控和可观测性](https://thenewstack.io/whats-the-difference-between-observability-and-monitoring/)团队提供指导、最佳实践和治理。

** आगे बढ़ो **

从战术性的 MELT 驱动方法转变为更广泛的[现代可观测性战略需要思维方式的转变](https://thenewstack.io/modernizing-observability-the-shift-from-diy-elk-to-saas/)。通过关注整合、集中治理以及[跨应用程序和互联网堆栈](https://thenewstack.io/devops-embraces-observability-across-stacks-for-llm-era/)的完全可见性，您将提高系统可靠性并为您的团队的长期成功做好准备。毕竟，可观测性不仅仅是发现问题，而是每次都提供卓越的数字体验。

这是我们想在本文中讨论的最后一个趋势：体验级别目标 (XLO) 的出现，它不关注系统级别的 SLI 或供应商 SLA，而是关注 IT 负责的[应用程序和服务给用户带来的体验](https://thenewstack.io/measuring-user-experience-in-modern-applications-and-infrastructure/)。采用 XLO 可以帮助弥合 IT 和业务之间的差距，并以一种更切实的方式展示 IT 运营团队带来的价值。

现在是放弃零散的工具并采用更智能、更统一的可观测性方法的时候了。回报是什么？更快乐的用户、更高效的团队以及您的系统可以处理接下来发生的事情的信心。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)