# AI 应用：为什么企业难以从开发转向生产

![特色图片：AI 应用：为什么企业难以从开发转向生产](https://cdn.thenewstack.io/media/2025/03/f27f912d-mike-kononov-lfv0v3_2h6s-unsplash-1024x576.jpg)

[Mike Kononov](https://unsplash.com/@mikofilm?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/architectural-photography-of-building-with-people-in-it-during-nighttime-lFv0V3_2H6s?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 上发布。

人工智能已不再是未来；它就是现在。然而，随着企业争先恐后地将人工智能整合到其工作流程中，他们发现应用绝非易事。更复杂的是一场高风险的拉锯战：OpenAI 和 Anthropic 等供应商希望企业将日常工作转移到他们的人工智能优先平台上。另一方面，[软件开发人员的目标是将人工智能作为一项功能嵌入](https://thenewstack.io/using-apis-with-low-code-tools-9-best-practices/)，以增强其现有产品并留住用户。

这种紧张关系突显了一个关键事实：人工智能可能无处不在，并且是任何规模较大的企业的优先事项，但成功并非必然。[Bain 最近的一项研究强调了这一悖论](https://www.bain.com/insights/ai-survey-four-themes-emerging/)，报告称，尽管开发活动激增，但生产中的人工智能解决方案却比上一季度*更少*。与此同时，领先者正在扩大其领先优势。是什么导致了这种瓶颈？将人工智能投入生产非常复杂，需要重新思考策略、调整流程以及谨慎的数据管理、安全和扩展选择。

**新的人工智能开发范式**

构建人工智能应用程序是一种平衡行为。人工智能是概率性的，这与传统软件不同，在传统软件中，输入和输出是可预测的。它就像一个非常聪明的幼儿，有时会按照你的要求去做，有时会决定用手指在你的墙上涂鸦。警戒线，以监视流程的形式，可以跟踪并缩短对话，这是你[保持系统](https://thenewstack.io/werner-vogels-6-lessons-for-keeping-systems-simple/)按计划进行并避免麻烦的方式。

这种不可预测性也改变了我们对人工智能应用程序工程的思考方式。对人工智能系统进行迭代更改是很棘手的，因为整体准确性很容易倒退。为了避免这种情况，你需要预先考虑你希望[大型语言模型](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) (LLM) 处理什么，以及你希望自己管理什么。这不仅仅是关于模型，而是关于整个系统和用例。

要有足够大的想法，才能产生真正的影响，并尽早获得高管的支持。即使是最好的想法，如果没有它，也可能会在离开起跑线之前停滞不前。

**构建基础**

任何人工智能集成的起点是选择一个基础模型。值得庆幸的是，大多数模型都是 API 兼容的，因此可以根据你的需求相对容易地进行更换。无论是 GPT-4o 还是 -o1、Claude 还是 Gemini，每个提供商还以不同的复杂程度和价格提供其模型。[Meta 正在遵循不同的策略，并将其 Llama 模型作为“开放权重”发布](https://thenewstack.io/metas-llama-2-is-not-open-source-and-thats-ok/)：你可以下载并在你自己的（强大的）硬件上运行的模型。

这种互换性意味着真正的差异化因素在于其他方面：你如何集成你的公司数据、设计安全和警戒线以及调整你的开发流程。

**是时候引入你的公司数据了**

人工智能的真正力量[在于它与你的公司数据协同工作的能力](https://thenewstack.io/starbursts-ceo-decries-big-data-lies-touts-data-truths/)。实现此目的有两种主要策略：微调和向量嵌入。微调有点像人工智能的健身会员资格：每个人都在谈论它，但只有少数人真正使用它。它需要大量的资源、专业知识和持续的维护，这使得它对许多公司来说是不切实际的。

相反，大多数成功的实现都利用了向量嵌入。文档或文本被预处理成向量，这些向量就像地图上的坐标，指示其单词的含义。坐标不仅仅是经度和纬度，而是由数千个维度组成。彼此靠近的项目具有相似的含义。

大型文档包含许多思想和含义，必须将其分成块，这些块要足够小，以便有效地查询，但又不能太小以至于失去上下文。可以采用各种分块策略，包括具有重叠块的滑动窗口方法。有很多方法可以选择在对话中哪些块是相关的，并将它们传递给人工智能进行分析。
随着您的业务数据不断发展，扩展向量数据库并保持其更新是一个具有挑战性的问题。为了最大限度地提高人工智能投资的影响，请寻找提供这些服务的专业IT供应商。

**人工智能在生产中：值得付出努力**

一个强大的[数据管理计划是成功](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/)的人工智能集成的基础。第一步是捕获与人工智能的所有交互，包括对话和隐式或显式反馈。这种持续的[数据流](https://thenewstack.io/why-we-use-apache-kafka-for-real-time-data-at-scale/)提供了构建训练数据集并随着时间的推移提高性能的原始材料。在生产中监控人工智能同样至关重要。实时跟踪输出可确保系统按预期运行，识别异常情况，并提供纠正措施的机会。这些实践共同构成了自适应、弹性人工智能战略的支柱。

将人工智能引入生产环境是困难的，但这是值得的。基础模型可能会成为头条新闻，但[真正的魔力在于企业如何](https://thenewstack.io/the-real-business-value-of-platform-engineering/)使用他们的数据，设计安全和合乎道德的系统，并使工作流程适应人工智能的独特需求。

通过周密的计划和执行，人工智能可以超越炒作，成为它注定要成为的变革力量。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube
频道，以流式传输我们所有的播客、访谈、演示等。