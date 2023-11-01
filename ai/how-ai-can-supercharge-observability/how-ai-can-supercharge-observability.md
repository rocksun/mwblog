<!-- 
# 人工智能如何增强可观测性
https://cdn.thenewstack.io/media/2023/10/0d5d3fb2-smash-5515411_1280-1024x682.jpg
 -->

当前的时代背景下，理解怀念过去是可以理解的，但我们正处在这样的环境里，因此，可观测性永远不会和从前一样了。

译自 [How AI Can Supercharge Observability](https://thenewstack.io/how-ai-can-supercharge-observability/) 。

最近，可观测性变得越来越复杂，肯定比IT监控的早期阶段要复杂得多，那时所有的事物都是在大型主机上运行，日志和所有可用的监控数据都可以轻松地收集和可视化。

即使在更近期应用成为大多数组织的核心之后，情况也简单得多。然而，在我们当前的Kubernetes、微服务和无服务器的世界，情况看起来大不相同。想象一下用锤子击碎过去那可以轻松观测的流动，看着它分解成上百块碎片；但是，所有这些小碎片仍必须保持紧密相连并持续交流。

本质上，这种情况是由初期引入的抽象化和虚拟化所造成的。然后Kubernetes出现了，它的短暂、快速变化和分布式特性增加了许多复杂度。在这里，一切都变得更加难以管理，也更难监控和故障排除；许多人感到不知所措，纳闷自己陷入了什么状况。我们可能会问自己——是否一切真的需要这么复杂？

理解怀念过去是可以理解的，但我们正处在这样的环境里，因此，可观测性永远不会和从前一样了。

## 重新审视“现代”可观测性的界限

首先，让我们退一步，介绍一些基本原则，从定义开始。在我们的云基础设施和应用程序的背景下，可观测性是检查软件并做出基于数据的决策来监控和修复生产系统的艺术。关键是要注意，这些决策应该专注于特定的结果和服务级别目标，而不仅仅是持续的监控、报警和故障排除。

然后，让我们考虑在当今世界设计一个可靠的可观测性系统的艺术——在编码或基础设施问题已经发展成[大数据](https://thenewstack.io/unravel-data-tackles-application-performance-management-big-data-stack/)问题的地方——这现在还需要找到方法来提高这些现代可观测性系统的计算、网络和存储需求的效率。更多的数据不意味着更好的洞见。

事实证明，抽象化、虚拟化和微服务只是冰山一角。随着人工智能工具的出现和持续采用，比[如Copilot、Code Whisperer等，人类处理、分析和关联数十亿个不同的事件来理解他们编写的代码是否按预期运行](https://thenewstack.io/developers-put-ai-bots-to-the-test-of-writing-code/)，这实际上成为一个无法解决的问题。再次，可观测性成为一个迫在眉睫的[大数据](https://thenewstack.io/mitylytics-provides-insight-big-data-deployment-scaling/)难题。

即使工程师具有理解可观测性信号以及如何分析[遥测数据](https://thenewstack.io/lightsteps-opentelemetry-extension-helps-make-lambda-telemetry-data-more-accessible/)的技能——这是难以获取的人才——要分类的海量数据也是不现实的，甚至是惊人的。事实是，大量数据中绝大部分对洞察关键业务系统的性能没有特别大的用处。

更多不等于更好。与此同时，大多数流行的可观测性解决方案表明，需要通过使用大量复杂的功能和额外的工具来解决庞大的数据流和复杂性这个[大数据问题](https://thenewstack.io/data-dignity-developers-must-solve-the-ai-attribution-problem/)——所有这些都需要一个高昂的价格标签，与数据膨胀相匹配。但还是有希望的。

## 迎接人工智能可观测性时代

在微服务和人工智能生成代码的现代[可观测性时代](https://thenewstack.io/modern-observability-is-a-single-braid-of-data/)，可观测性不必过于复杂或昂贵，是的——日益增长的人工智能应用提供了巨大的希望。[驱动人工智能驱动代码的大语言模型(LLM)为可观测性提供了一种新的方法](https://thenewstack.io/how-porsche-informatiks-cloud-migration-hinged-on-ai-powered-observability/)。

这是如何工作的？LLM正在变得善于处理、学习和识别大规模重复文本数据中的模式——这正是高度分布式和动态系统中的日志数据和其他遥测的[本质特征](https://thenewstack.io/art-data-logging/)。LLM知道如何回答基本问题并得出有用的推断、假设和预测。

这种方法并不完美，因为LLM模型还不是为实时设计的，在确定完整的[上下文范围以解决所有可观测性](https://thenewstack.io/the-new-stack-context-observability-in-the-time-of-covid/)难题方面也不够准确。然而，与人类在合理的时间内理解和建立大量机器生成的数据的上下文相比，首先用LLM建立一个基线，了解发生了什么并获得有益的建议要容易得多。

因此，LLM对解决可观测性问题非常相关。它们旨在用于基于文本的系统，以及分析和提供见解。这可以通过[集成](https://thenewstack.io/continuous-integration-observability-explained/)轻松地应用于可观测性，以提供有意义的建议。

我们认为，在这方面LLM的最大价值之一是更好地支持可能没有很高技术熟练度的从业者，并使他们能够处理必须解决的大量复杂数据。大多数需要恢复的生产问题都有足够的时间让LLM根据历史上下文数据提供帮助。通过这种方式，LLM能够使可观测性更简单、更经济高效。

与此同时，尽管人工智能在可观测性方面正在变得[日益强大](https://thenewstack.io/growing-adoption-of-observability-powers-business-transformation/)，但未来还有更有趣、更具颠覆性的机会。接下来的是可以用自然语言书写和调查的LLM，而不是[晦涩难懂的查询语言](https://thenewstack.io/grafana-now-offers-flux-as-a-native-query-language/)——这对所有级别的用户来说都是巨大的福音，但对那些比较缺乏实践经验的人尤其如此，包括业务部门的管理人员。

用户不再需要掌握所有相关信息的专家，现在人们能够编写与常见参数相关的查询，最重要的是业务部门主管使用的自然语言，而不仅仅是生产工程师。这为广泛的新流程和利益相关者解锁了可观测性，不仅仅是生产工程师。

在Logz.io，我们已经开始与LLM集成，现在正在平台上努力开发令人兴奋的新功能，目的是利用这些新兴的人工智能能力。我们相信，这是为面临大数据挑战的寻求必要可观测性的组织提供[下一波](https://thenewstack.io/unlock-the-next-wave-of-machine-learning-with-the-hybrid-cloud/)关键创新的手段。虽然成本和复杂性的紧迫问题在市场上仍然存在，但我们相信这给了每个人许多保持乐观的理由。
