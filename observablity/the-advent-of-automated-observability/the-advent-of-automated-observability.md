
<!--
title: 自动化可观测性的出现
cover: https://cdn.thenewstack.io/media/2024/02/a7467d48-cat-3211011_1280.jpg
-->

AI 可能永远无法成为可观测性的万能疗法，但它肯定可以成为有价值的伴侣。

> 译自 [The Advent of Automated Observability](https://thenewstack.io/the-advent-of-automated-observability/)，作者 Ozan Unlu。

停机成本有据可查，会影响从收入到生产力、合规性再到品牌声誉的一切。在过去的一年中，有几家主要航空公司在其面向客户的登机和电子票务系统中遇到技术故障，导致数千次航班取消和延误。今年 4 月，在线折扣经纪公司 Robinhood 因 2020 年的宕机而被[猛烈抨击](https://www.financemagnates.com/forex/regulators-slam-10m-on-robinhood-for-technical-failures/)，被罚款 1000 万美元。

当我们关注头条新闻时，我们经常看到对大公司和宕机的报道。通常，他们的响应分为两个部分：增加监控和故障排除。

- `监控`意味着识别指标，这些指标表明你是否满足你的[服务级别目标](https://thenewstack.io/how-to-use-service-level-objectives-to-manage-external-services/)(SLO)，然后依靠人类定义的警报阈值，在指标超出预期行为时触发警报。
- `故障排除`意味着当警报触发时，你必须筛选日志，寻找“大海捞针”，以确定问题的根本原因。通常，这意味着依赖“机构知识”——谁最了解我们的系统，以前见过这个问题，并且知道如何解决它？

如上所述，监控和故障排除是反应性的。你将大量人力时间用于手动任务。此外，由于你只对已知行为发出警报，因此你的异常覆盖不完整。作为上述两者的副产品，你可能会遇到缓慢的解决，完全取决于 (a) 你是否发现了问题，以及 (b) 你是否可以找到相关的日志数据。

这种方法存在一个重大问题。在生产环境中可能发生的事件的罕见性使得以传统意义上的“预测”它们变得不切实际。在日常生活中，某些不可避免的伤亡和事件可能会对业务产生持久影响，而这些事件是无法预测的。例如，在 2020 年之前，谁能预见到一场百年不遇的流行病，会对美国经济造成重大打击？

应用程序开发中潜在错误的长尾与此类似，这就是为什么在 2024 年，仍然很难预见和防止生产中断的原因。在生产环境中，许多具体问题可能只发生一次，以至于你可能再也看不到它们再次发生，而其他类型的性能下降可能更频繁地发生，甚至每天都会发生。在应用程序开发上下文中，完全理解和预测所有可能出错的方式是不可能的。

建立了复杂的可观测性实践的大型组织可能能够在这些条件下蓬勃发展。但是，对于运营资源有限的中小型组织呢？可观测性只是他们众多职责之一呢？对于任何构建创收软件的人来说，卓越的性能（速度和可靠性）至关重要，无论规模大小。

## 人工智能作为可观测性“副驾驶”

如上所述，在生产环境中，许多导致生产中断的原因可能只发生一次。较小的团队可能没有资源或远见来预测可能导致系统故障的每种情况。这正是人工智能可以帮助最大化监控覆盖范围的情况。

更具体地说，人工智能可用于基准化[数据集和检测异常](https://thenewstack.io/anomaly-detection-glimpse-into-the-future-of-iot-data/)。在此用例中，[人工智能算法](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) 可以识别不同时间范围内的正常活动——从几个月到几周，甚至到个别天——并在异常情况出现时发出标记。通过这种方式，人工智能在问题可能正在酝酿时提供主动信号方面具有价值——而无需用户定义警报条件。它甚至可以检测“未知的未知”，因此工程师不必尝试以特定指标或阈值的形式预测未来。

人工智能可以提供帮助的另一个领域是作为故障排除副驾驶。人工智能可用于解释与警报相关的日志数据。然后，生成式人工智能可以总结行为并用对话文本推荐解决路径。当检测到异常时，人工智能可以：

- 分析导致异常的日志内容
- 传达问题的严重性及其影响
- 用对话文本总结负面行为
- 提供有关如何解决问题的建议

通过这种方式，人工智能可以帮助组织更快速地完成故障排除流程。这几乎就像一位同事已经为您调查了问题。当人工智能可以预测和推荐时，它非常强大，使专业人员能够决定补救措施。

如今，人工智能正在颠覆许多行业——从营销到零售再到法律等等。这些用例场景的共同主题是人工智能正在自动化许多“繁重的工作”，让人类能够专注于他们的核心任务。可观测性也不例外，因为 IT 和 [运营团队](https://thenewstack.io/building-and-running-a-successful-remote-saas-operations-team/)总是比“万一发生这种情况就构建这个东西”有更紧迫的问题。人工智能可能永远无法成为可观测性的万能药，但它肯定可以成为一个有价值的伴侣。它全天候“待命”，因此您不必如此；它可以代表您构建和优化警报，并且可以找到您[需要提供的数据](https://thenewstack.io/5-data-services-that-it-leaders-need-to-master-and-deliver/)，从而为您的客户提供更好的用户体验。
