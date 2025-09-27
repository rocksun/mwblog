[David Cramer](https://www.linkedin.com/in/dmcramer/) 是对生成式人工智能 (GenAI) 当前取代人类开发者和工程师工作的能力持怀疑态度的人之一。

他在本期 The New Stack Agents 直播中表示，GenAI 工具在编写可用于生产环境的软件方面，可靠性还不足够。

视频

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，别错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等。

订阅](https://youtube.com/thenewstack?sub_confirmation=1)

但 Sentry（一家应用程序监控软件制造商）的创始人兼首席产品官 Cramer 也愿意暂时放下这种怀疑，推出基于人工智能的产品。

6 月，[Sentry 的 Seer](https://blog.sentry.io/seer-sentrys-ai-debugger-is-generally-available/) 正式发布，它利用 GenAI 能力进行调试和识别 bug 的根本原因。公司通过思考其核心使命，决定开始探索[大型语言模型](https://thenewstack.io/introduction-to-llms/) (LLMs) 能为其客户做些什么。

“Sentry 在帮助你调试生产环境中软件出现的问题方面做得非常好，”Cramer 告诉本期节目的联合主持人，TNS 创始人兼发行人 [Alex Williams](https://thenewstack.io/author/alex/) 和 TNS 人工智能高级编辑 [Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)。“因为我们捕捉了所有这些信息，我们能否让调试变得更好？我们能否做到超越调试问题？”

## 人工智能模仿资深工程专业知识的潜力

Cramer 说，通过利用 LLMs 增强 Sentry 的解决方案，用户可以受益于 LLMs 的大规模模式匹配能力。“我们发现这项技术对我们的业务非常有益。首先，Sentry 的核心部分是聚合。我有一个错误。我又有另一个错误。它们是同一个错误吗？”

而且，由于 Sentry 收集的跟踪信息，LLMs“实际上能够总结系统中的大量数据，并且能够惊人地 [识别] 根本原因问题，其方式就像人类一样。”

他打了一个比方，提到了他多年来认识的一些在大公司担任高级或首席工程师的朋友。“他们似乎没做什么，却拿着巨额薪水，而且普遍讨厌自己的工作，”他指出。“很长一段时间里，我不明白为什么，为什么他们存在，为什么公司会如此看重他们。”

“然后我意识到原因：对于工程领域真正的资深人士而言。关键在于能够理论化系统是如何工作的。而做到这一点的唯一方法是，你对这些系统拥有领域经验。很多这些大公司的领域经验实际上就是那家公司。它对那家公司来说非常具体。”

他说，他用这个比喻来强调一个人工智能最终可能证明有益的领域：能够非常迅速地总结系统中正在发生的一切。“你现在可以用 LLMs 做很多这样的事情。”

## 为什么人工智能仍然需要“人在回路”

然而，Cramer 承认，这并非意味着人工智能已准备好取代[血肉之躯的工程师](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/)。他再次表达了这种怀疑。

“我们现在正处于这个阶段，我认为我们将在很长一段时间内都处于这个阶段，那就是真正地、不间断地[人在回路](https://thenewstack.io/human-on-the-loop-the-new-ai-control-model-that-actually-works/)，”他说。“但它是一个极好的推动者，可以加速一些代码审查工作。”

“包括我们在内，有数十家公司在这个领域进行了投资，而且它实际上不一定要完全正确，因为那里仍然有人。如果它能发现一些你可能没有发现，或者自己没有发现的 bug，那这就是一个净胜利——对生产力的净积极影响。”

## 人工智能驱动的补丁生成的现状

Cramer 认为，利用人工智能技术的创新将像创新常有的那样，逐步改进。他说，到目前为止，Sentry 在人工智能方面的实验产品结果“并非为完全自主而设计。我们确实可以自主完成一些很酷的事情。”

例如，尽管人工智能驱动的**可观测性**通常可以识别 bug 的根本原因，“补丁生成效果很差。我将率先告诉你，它并不那么好，而且所有人的补丁生成效果都很差。但这没关系。这就是这项技术的现状。”

但他补充说，“我们今天能做的就是我们今天能做的。好吧，也许我们可以更有效地让你找到那个 [根本] 原因，这样你就能更快地调试。”

## Sentry 转向公平源代码许可

Cramer 还就公司在保持创新开源方面持续存在的争议发表了看法。他指出，Sentry 已经有 15 年历史，很久以前就从[开源许可](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)转向了公平源代码。

[2023 年，该公司根据[功能源代码许可](https://fsl.software/)重新许可了 Sentry](https://blog.sentry.io/introducing-the-functional-source-license-freedom-without-free-riding/)。FSL 在两年后转换为 Apache 2.0。“事实上，我们大部分软件目前都是 Apache 许可，”Cramer 说。

Cramer 说：“开源这件事不一定[是融入商业模式的正确选择](https://thenewstack.io/whats-next-for-companies-built-on-open-source/)。” “它让一切都变得复杂。它使市场商品化。”

他说，做出这个决定是因为“我被那些试图获取 Sentry 并将其商业化的人困扰，他们不属于我们的组织，老实说，也不属于开源社区，作为其他纯商业实体，他们试图从中获利。”

他说，这让他很生气。“我就想，‘听着，我们就是要阻止他们。’ 我们将把许可改为我们深信能实现我们目标的模式。我们希望每个人都使用我们的软件。我们不希望人们免费搭便车，尤其是其他风险投资支持的公司，只是拿走我们的软件并将其商业化。”

他说，目标是避免出现 Sentry 产品多个版本的情况——“开源免费版本，然后是每个人都真正想要的，价格高昂的版本。因此我们提出了这个叫做公平源代码（fair source）的概念，它的简而言之就是：一个附加条件很少的许可。”

观看 The New Stack Agents 的完整剧集，了解 Cramer 关于公平源代码许可、Sentry 如何以怀疑和好奇心对待人工智能、人工智能可能创造的新技术工作等更多内容。