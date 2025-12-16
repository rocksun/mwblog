<!--
title: 始源实验室：大模型极速提效，成本锐减！
cover: https://cdn.thenewstack.io/media/2025/12/97f308b5-mercury-speed-2.jpg
summary: Karpathy 赞誉 Inception 扩散模型。它并行生成词元，比传统 LLM 快 5-10 倍。尤其适用于编码和语音等实时应用，Inception 提供 API 且具成本效益。
-->

Karpathy 赞誉 Inception 扩散模型。它并行生成词元，比传统 LLM 快 5-10 倍。尤其适用于编码和语音等实时应用，Inception 提供 API 且具成本效益。

> 译自：[Inception Labs: Making LLMs Faster and More Cost-Efficient](https://thenewstack.io/inception-labs-making-llms-faster-and-more-cost-efficient/)
> 
> 作者：Alex Williams

AI 领军人物 [Andrej Karpathy](https://karpathy.ai/) 表示，[Inception Labs](https://www.inceptionlabs.ai/) 的扩散方法有可能与目前领先的 Claude 和 ChatGPT 等所有其他大型语言模型有所不同。

这意味着非同寻常。当 Karpathy 鼓励人们尝试时？那可真是件大事。

Karpathy 创造了“氛围编程”（vibe coding）一词，他于二月份在 X 上发帖称，大多数大型语言模型（LLM）都是自回归训练的，这意味着它们从左到右预测词元。扩散模型并非从左到右，而是同时进行。用他的话说，你从噪声开始，然后逐渐将其去噪为词元流。

[他](https://x.com/karpathy/status/1894923254864978091?s=20) 在 X 上写道：“所有这些都表明，这个模型有可能与众不同，并可能展现出新的、独特的‘心理’，或新的优势和劣势。我鼓励大家尝试一下！”

Inception Labs 是一家成立 18 个月的初创公司，其创始人开创了扩散技术，并声称已开发出比传统自回归大型语言模型更快、更具成本效益地构建语言模型的能力。[Kimberly Mok](https://thenewstack.io/author/kimberleymok/) 今年早些时候为 The New Stack [撰文介绍了 Inception](https://thenewstack.io/get-ready-for-faster-text-generation-with-diffusion-llms/)。

该公司在市场上有少数同行，包括 [Dream7B](https://thenewstack.io/dream-7b-a-powerful-and-open-diffusion-language-model/)、[LLaDA](https://thenewstack.io/how-diffusion-based-llm-ai-speeds-up-reasoning/) 和 [Google](https://deepmind.google/models/gemini-diffusion/) 通过 Gemini 提供的实验性扩散模型。但 Inception 是唯一提供自有 API 的商业可用模型。

## 扩散模型与自回归大型语言模型有何不同？

Inception 的产品副总裁 [Burzin Patel](https://www.linkedin.com/in/burzinpatel/) 在 [AWS re:Invent](https://thenewstack.io/aws-updates-its-nova-models-to-compete-with-google-anthropic-and-openai/) 期间接受 The New Stack 采访时表示，Inception 的模型 [Mercury](https://www.inceptionlabs.ai/blog/mercury-refreshed) 并行生成词元。自回归模型则顺序生成词元。

Patel 谈到 Mercury 时说：“每次通过选择过程，你都会弹出多个词元，正因为如此，它的速度快了 5 到 10 倍。”“一次通过”意味着神经网络进行一次前向查找，以评估和做出预测。

Patel 表示，对于需要多次顺序调用大型语言模型的应用程序来说，速度优势会累积。“越来越多的应用程序会多次与大型语言模型交互——这是智能代理应用的一个非常大的趋势，”他说，“如果一个应用程序进行 30 次大型语言模型调用，每次都快两秒，那么每次请求就能节省整整一分钟。”

自回归架构具有优势，尤其是在用户界面方面。例如，使用 Claude 等服务时，您在第一次通过后就能看到词元输出。自回归模型的输出是实时的，而扩散模型的初始输出会有一些延迟，尽管最终响应可能更快。

## 扩散模型的速度和效率优势

但对于代理工作流来说，扩散模型的速度可以带来真正的改变。

Patel 说，使用 Mercury，作为块的一部分，你实际上可以改变词元。如果你看到更好的第五个词元，你可以去改变第二个词元。

扩散模型通常同时预测所有被遮蔽的词元。Patel 说，Mercury 以不同的置信水平生成词元块。（这是他对内部工作原理的唯一解释：他说，公司不披露详细的架构选择。）

在 Mercury 中，关键在于对词元具有高置信度。如果一个块有 1000 个词元，其中 300 个可能具有高置信度。Mercury 可以继续分解并持续显示具有高置信度的词元。

Patel 说：“假设你的答案需要 1000 个词元。使用自回归模型，你需要进行一千次前向传递。使用扩散模型，每次前向传递可以生成 5 到 10 个词元——1000 除以 5 或 1000 除以 10。这并不比那复杂多少。”

## Inception 对编码和语音用例的关注

扩散方法起源于斯坦福大学的人工智能实验室。Patel 指出 Inception 联合创始人的参与以及他们之间的联系：“[Stefano [Ermon]](https://www.linkedin.com/in/ermon/) 是斯坦福大学人工智能实验室的负责人。[Aditya Grover](https://www.linkedin.com/in/aditya-grover/) 是加州大学洛杉矶分校的博士教授，而 [Volodymyr Kuleshov](https://www.linkedin.com/in/volodymyr-kuleshov-6aa83294/) 来自康奈尔大学。Aditya 和 Volodymyr 是 Stefano 的学生，他们共同开发了这种基于扩散的算法。”

Patel 补充道：“所有 [扩散算法] 都来自斯坦福实验室。没有人想出如何将这种算法用于文本模态。这是 Stefano 的突破，他从斯坦福休假并创办了这家公司。”

他说，Inception 是一家小公司，正在通过专注于两个垂直领域来充分利用其资源：编码和语音。

Patel 说：“我们实际上可以涵盖所有用例，但我们是一家只有 25 人的初创公司，所以这不是我们进入市场的方式。”

它为什么决定专注于编码和语音呢？“因为这两个领域对速度最敏感。当你进行编码并做像自动补全这样的事情时，如果我打字比自动补全还快，那它就没什么用了。”

语音代理需要速度以避免因其实时性而产生的延迟。

Patel 说：“我们是文本到文本的模态，所以我们不是语音到语音的。”“你使用 ASR，获得文本，然后使用模型——它的核心是我们的 Inception Mercury 扩散模型引擎——然后你进行文本到语音的转换。我们有一些客户正在大规模地这样做。”

他说，Inception 已开始与编码集成开发环境（IDE）合作，这些 IDE 依赖于“模型专家，那些来自斯坦福等地方，花费多年时间研究博士学位的人。”

Patel 说：“我们是许多 IDE 插件的默认大型语言模型。如果你看看整个编码和 IDE 领域，这些人非常擅长构建 IDE。他们了解程序员环境。他们不是模型专家。模型专家来自斯坦福并拥有博士学位。我们就是模型。”

Inception 与开源编码代理 [Continue](https://www.continue.dev/) 合作。这家初创公司还与 [Proxy AI](https://www.codegpt.ee/)、[JetBrains](https://www.jetbrains.com/)、[Kilo Code](https://kilo.ai/) 和 [Cline](https://cline.bot/) 等公司合作。

## Mercury 模型如何整合到现有系统

Mercury 与 OpenAI 和标准模型兼容 API。集成只需要单行或两位数的代码，API 轻量级且遵循相同的协议。

在当今时代，对于使用生成式 AI 的公司来说，算法效率比以往任何时候都更加重要。

Patel 说：“我们的模型价格是每百万输入词元 25 美分，每百万输出词元 1 美元。我们更具成本效益。我们可以更高效地提供这些模型，这就是我们保持低成本的原因。”

Patel 表示，Inception 的部署模型各不相同。例如，用户在创建账户时会获得 1000 万个词元。API 文档帮助他们开始构建程序和开发模型。

一些公司有数据主权要求，在这种情况下，他们可以通过 Amazon Bedrock 或 Azure Foundry 自行托管模型。

[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 拉丁美洲初创公司总监 [Alvaro Echeverria](https://www.linkedin.com/in/echeverriaalvaro/) 在 AWS re:Invent 的一次讨论中说：“如果你看看 Bedrock，有超过 20 种不同的模型选择可供你使用，包括开源模型。”

Echeverria 说：“我们不相信有一种模型可以解决所有用例，你可以选择最适合你的模型。像 Bedrock 这样的平台将允许你进行微调。”

Patel 说，目前，Inception 仅与 Nvidia 合作提供 GPU。

扩散模型具有相当大的上涨潜力。Inception 处于游戏的早期阶段，这带来了其自身的优势。尽管如此，扩散模型在文本领域的能力在历史上无法与它们的自回归对应物相提并论。

有关比较自回归和扩散技术的详细技术分析，请查阅 [Greg Robison 在 Medium 上发布的文章](https://gregrobison.medium.com/a-comparative-analysis-of-diffusion-and-autoregressive-models-for-text-generation-architectures-99fb24fa390c)。