# AI自主性评估工具帮助开发者对抗幻觉

![AI自主性评估工具帮助开发者对抗幻觉的特色图片](https://cdn.thenewstack.io/media/2025/02/3abd7127-jr-korpa-quxyfcoa4qm-unsplashb-1024x576.jpg)

自主性指的是系统自主行动并独立实现目标的能力。因此，AI自主性评估工具是评估生成式AI和[AI智能体](https://thenewstack.io/ai-agents-are-about-to-blow-up-the-business-process-layer/)是否存在幻觉和其他问题的解决方案。

该领域非常新兴，解决方案提供商和研究人员仍在确定使用哪些指标。为了了解更多信息，我们采访了[Atin Sanyal](https://www.linkedin.com/in/atinsanyal/)，他是新兴AI自主性评估领域的专家。Sanyal是[Galileo](https://www.galileo.ai/)的首席技术官和联合创始人，Galileo是一家AI评估平台初创公司，大约五年前从斯坦福实验室发展而来。此前，他曾在Uber、Apple、LinkedIn、UCLA和[Oracle](https://developer.oracle.com/?utm_content=inline+mention)等机构担任工程师和研究员。

## 评估幻觉

Sanyal确定了两种类型的[幻觉](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/)。开放域幻觉是指AI模型在没有特定上下文或输入的情况下生成虚假信息。封闭域幻觉是指AI模型仅基于有限的上下文数据编造不正确的信息。

在构建AI智能体时，封闭域幻觉尤其令人担忧。封闭域幻觉的两个关键指标是上下文一致性——衡量输出中上下文出现的程度——和指令一致性，它衡量AI遵循用户提示的程度。

## 超越LLM作为评判者

当组织最初开始解决幻觉问题时，他们部署了一个大型语言模型(LLM)作为评判者的模型，该模型基本上使用一个LLM来检查生成式AI模型。然而，这种方法有其局限性，例如[位置偏差](https://eugeneyan.com/writing/position-bias/)、[冗余偏差](https://arxiv.org/abs/2310.10076)、[自我增强偏差](https://arxiv.org/abs/2402.11436)和[有限的推理能力](https://news.mit.edu/2024/reasoning-skills-large-language-models-often-overestimated-0711)，根据一篇[2023年的研究论文](https://arxiv.org/abs/2306.05685)。

Sanyal补充说，另一个大问题是大型企业已经达到了这种方法的极限。

“它们根本无法扩展，因为存在[速率限制](https://thenewstack.io/how-nuanced-rate-limiting-transforms-your-api-and-business/)以及第三方API会施加的各种限制，这实际上会降低源应用程序的质量，”他说。

在评估AI智能体时，还有一个更复杂的因素：即使是AI系统的一个部分的输出中出现的一个问题，也会加剧并导致“输出失衡”，Sanyal说。他说，挑战在于将输出中的错误追溯到导致该错误的AI系统部分。

## 评估AI智能体：开源

这就是AI自主性评估发挥作用的地方。

“这实际上是关于我们如何帮助AI工程师使这些不可预测的系统更可预测，并为它们提供正确的防护措施，并帮助我们所说的评估，”Sanyal说。

有一些[开源](https://thenewstack.io/the-metamorphosis-of-open-source-an-industry-in-transition/)库和框架可以评估AI智能体，包括[RAGAS](https://docs.ragas.io/en/stable/)和[TruLens](https://www.trulens.org/)，后者去年被云数据仓库平台Snowflake收购。Sanyal说，这些工具在过去12-15个月中获得了关注。

他认为，开源解决方案往往“不足和短视”，开源工具通常侧重于生成数字的*定量*测量，而不是更详细的*定性*信息。

“许多开源解决方案仍然专注于对[RAG](https://thenewstack.io/tutorial-build-a-rag-agent-with-azure-ai-agent-service-sdk/)幻觉或开放域幻觉以及LLM系统犯下的各种其他常见形式错误进行统计量化的方法，但我们发现这真的不够，不足，”他说。“他们错过了定制部分，即根据用例定义自己的指标和评分器。”

## AI智能体副驾驶

他说，Galileo充当AI智能体副驾驶，并通过两行代码集成到开发人员的工作流程中。它提供具有通用定性和定量度量的默认防护措施。
开发者还有一个“核心需求”，即创建他们自己的指标并修改其他指标。因此，基于代码的指标至关重要，但由于并非所有大型语言模型创建者都是程序员，因此还需要基于定性自然语言定义的指标。

“我们构建了这个自动[ML（机器学习）](https://thenewstack.io/use-these-tools-to-build-accurate-machine-learning-models/)管道，它不仅允许你为你的应用程序创建你想要的自定义指标，还允许你通过人工反馈以及不同形式的反馈随着时间推移改进它们，”他说。“它们几乎就像我们内部构建的小型自主评估系统，能够使你的指标适应你的数据。”

实际上，要使用哪些指标取决于开发者正在构建的[自主系统类型](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/)。目前，有数十种[自主构建系统的设计模式](https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/)，这也影响了应该使用哪些指标，他指出。

## Galileo的双重方法
Galileo的评估智能平台采用双重方法来评估AI代理。

首先，它开发了[ChainPoll](https://arxiv.org/abs/2310.18344)，这是一种类似于基于裁判的自主框架的自主AI，但它比基本的LLM作为裁判的技术提供了阶跃函数式的改进，并且旨在检测各种类型的LLM幻觉。它在幕后使用LLM，并且设计为可定制的，以便用户可以提供他们自己对幻觉的定义，并且系统以此为基础工作。

Luna是一套低延迟评估模型，具有开放权重，运行在Galileo内部开发的可扩展LLM推理基础设施上。它专注于用户请求量大且需要数据隐私的情况。

“我们为开发者提供了工具，让他们可以选择将其反馈给用户，或者重新表述生成结果，或者如果出现幻觉则重试端到端请求。”

– Galileo首席技术官兼联合创始人 Atin Sanyal
Sanyal说，Luna创建于2024年，代表着一年来重返绘图板，尝试使用更小的生成模型。它是一个DeBERTA-large（440M）编码器——这是一种花哨的说法，即拥有4.4亿个参数的Luna比其他LLM更小。相比之下，GPT-3.5拥有1750亿个参数。这使得Luna运行效率更高，计算成本更低。该[模型还针对RAG中的幻觉检测进行了微调](https://thenewstack.io/rag-vs-fine-tuning-models-whats-the-right-approach/)。

Sanyal说，像Luna这样更小的评估模型有望在未来更好地进行幻觉评估。例如，根据Galileo的[关于Luna的研究论文](https://arxiv.org/abs/2406.00975)，Luna的表现优于RAGAS和Trulens，以及Galileo自己的ChainPoll。

“这是一套较小的模型，通常在20亿到100亿个参数之间，它们经过专门微调和训练以检测幻觉，我们最终将它们托管在我们这边的商品化GPU上，”他说。

Sanyal将Galileo描述为一个“评估副驾驶”，它在[Web开发者构建应用程序](https://thenewstack.io/web-app-development-sans-javascript-with-microsoft-blazor/)的同时运行。它只需要在应用程序中插入两行Galileo代码。Galileo提供[Typescript](https://docs.galileo.ai/client-reference/evaluate/typescript)和[Python SDK](https://galileo-sdk.readthedocs.io/en/latest/index.html)，他补充道。该平台可以在本地或Galileo的SOC 2合规云中运行。

“我们为开发者提供了工具，让他们可以选择将其反馈给用户，或者重新表述生成结果，或者如果出现幻觉则重试端到端请求，”他说。“接下来该做什么取决于开发者，而不是直接呈现在用户面前。”

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)