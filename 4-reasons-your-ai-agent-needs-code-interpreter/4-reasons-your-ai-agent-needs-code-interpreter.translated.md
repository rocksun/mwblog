## 4 个原因说明你的 AI 代理需要代码解释器
![4 个原因说明你的 AI 代理需要代码解释器](https://cdn.thenewstack.io/media/2024/04/dfa23f6e-robot-1797548_1280-1024x576.png)

构建 AI 代理很难。你会遇到 [幻觉](https://thenewstack.io/the-security-risks-of-generative-ai-package-hallucinations/)、让代理保持正轨和 [引导它们](https://thenewstack.io/5-lessons-from-linkedins-first-foray-into-genai-development/) 使用正确工具的问题。

克服这些问题的一种方法是赋予代理代码执行能力。

以下是一些你的 AI 代理应该拥有代码解释器的原因：

**1. 额外技能**

拥有代码解释器的代理可以获得执行 CSV 文件统计分析或绘制图表等能力。

当你向不同的代理询问相同的事情时，就会明显看出那些具有底层代码解释器的代理有多大的不同。如果没有运行代码，几乎不可能完成以下任务：

- 分析 NVIDIA 股票并预测其发展。
- 与我玩扑克游戏。
- 为我预订航班。

看看 Perplexity（一个没有代码解释器的代理）如何处理数据分析任务。即使提供了数据文件，代理也无法完成任务——它能做的最好的事情就是提供有关我应该运行什么代码的建议。

以下是具有底层代码解释器的 ChatGPT 如何处理相同任务的示例……

……包括安装新包和生成图表。

请注意，最终用户不必 [意识到应用程序在后台执行编码](https://thenewstack.io/why-your-code-needs-abstraction-layers/) 任务，因为主要目标（如“为我预订航班”）通常不涉及编码。

**2. 复杂推理**

[大型语言模型](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) (LLM) 非常擅长生成文本 [但在推理和复杂思考方面存在困难](https://thenewstack.io/3-ways-llms-can-let-you-down/)。

谷歌团队

[从丹尼尔·卡尼曼的著名著作“思考，快与慢”中做了一个有趣的类比](https://blog.google/technology/ai/bard-improved-reasoning-google-sheets-export/)。执行代码的能力使代理具备慢思考（费力、合乎逻辑和计算）与快思考（直观和自动）的能力，并且由代理在没有代码解释器的情况下如何行动来表示。

在他们的类比中，纯粹依赖 LLM 的代理可以被认为在没有慢思考的情况下运行，快速生成文本而没有更深入的思考。以下是一个示例，说明即使是简单的任务也可能需要一些系统，而不能仅凭直觉来回答。

**3. 减少 LLM 幻觉**

最近的一篇 [论文](https://arxiv.org/abs/2305.13534) 证实，即使给出了推理提示，LLM 在多步骤任务中也会出现幻觉。作为对论文发现的后续，一位软件工程师 [演示](https://aditya-advani.medium.com/mitigate-gpt-4-hallucinations-using-code-interpreter-29fea4887eec) 了如何使用代码解释器风格的 LLM 引擎成功地将幻觉减少了一个数量级。他发现代码解释器可以将 GPT-4 幻觉率从 <10% 降低到 <1%。

代码解释器可以处理上传和下载，编写代码以从源文件中查找数据并得出结论，而不是像通常的简单代理那样自由推理。

[对抗 LLM 幻觉的其他方法](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/) 包括 RAG、微调和增加 LLM 上下文窗口的大小。

**4. 测试**

另一个重大挑战是 LLM 代码生成。当代理不仅可以 [生成还可以运行代码](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/) 时，它能够测试其自身输出的功能并对其进行迭代。

## 使用代码解释器构建

我认为我们将看到代码解释器为更多 AI 代理和应用程序提供支持，作为围绕 LLM 构建的新生态系统的一部分，其中代码解释器代表了代理大脑的关键部分。有关构建的灵感，请参阅流行的开源产品，如

[Open Interpreter](https://github.com/OpenInterpreter) 或 [AutoGen](https://github.com/microsoft/autogen)。

仍有一些挑战需要克服，例如找到一种安全且最佳的方式来运行 LLM 生成的代码，这可以通过在 [隔离的云环境](https://e2b.dev/docs) 中执行进程来解决。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、采访、演示等。