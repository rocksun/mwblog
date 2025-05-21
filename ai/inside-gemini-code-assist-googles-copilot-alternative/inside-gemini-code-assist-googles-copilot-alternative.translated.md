# Gemini Code Assist vs. Copilot：AI 编码代理的崛起

![Gemini Code Assist vs. Copilot：AI 编码代理的崛起 的特色图片](https://cdn.thenewstack.io/media/2025/05/0d27859d-google-io-gemini-1024x576.jpg)

在今天的 Google I/O 大会上，面向个人的 [Gemini Code Assist](https://codeassist.google/) 正式发布。在大会之前，我与 Google Cloud 的产品管理高级总监 Ryan J. Salva 进行了交谈，讨论了 Gemini Code Assist 的最新迭代版本，即 Google 的 AI 编码工具。我们特别关注了该产品对 Agentic AI 的应用，以及它与 Microsoft 的 GitHub Copilot 之间持续的竞争。

我不知道你是否了解，但 AI 代理是今年开发者们追逐的新热点。当然，我是在开玩笑：如果现在的开发者工具发布没有提到 “代理” 这个词，那才是不正常的！昨天我们已经看到了这方面的证据，Microsoft Build 大会上 [GitHub Copilot 编码代理发布了](https://thenewstack.io/github-launches-its-coding-agent/)。

Gemini Code Assist 代理在上个月的 Google Cloud Next 大会上以 “私有预览” 的形式 [发布](https://techcrunch.com/2025/04/09/gemini-code-assist-googles-ai-coding-assistant-gets-agentic-upgrades/)。当时，Google 邀请开发者 [申请](https://developers.google.com/profile/badges/community/sdlcagents/gca-agents) 使用 “通过 VS Code 和 Firebase Studio 中的 Gemini Code Assist 获得的一套 SDLC 代理”。

同样在今天，Google 宣布开放访问 [Jules](https://jules.google.com/home)，这是一个 AI 编码代理，“可以完成你不想做的编码任务”。（但是，Jules 不是 Code Assist 的一部分。）

## “代理的混合”

自 2 月下旬以来，Google 显然一直在瞄准 GitHub Copilot 用户，当时它宣布了一个免费版本的 Gemini Code Assist，该版本 [提供的代码补全数量是其主要竞争对手的 90 倍](https://thenewstack.io/google-ai-coding-tool-now-free-with-90x-copilots-output/)。所以我问 Salva，Google 在 Gemini Code Assist 中使用代理技术的方式与 GitHub Copilot 使用代理的方式有什么不同。

Salva 回答说，Copilot 的 “代理模式”（他还提到了 Cursor 的 Yolo Mode）类似于一个开发者独自完成一个计划，而 Gemini 使用的是 “代理的混合” 方法。这涉及到多个专门的代理——例如，开发者、测试人员和安全分析师的角色——一起工作。正如 Salva 所说，这些代理本质上是 “相互对抗的合作者，以便检查彼此的工作”。他将此比作共享聊天室中的虚拟团队。

> Gemini Code Assist 代理是 “相互对抗的合作者，以便检查彼此的工作”。
>
> – Ryan J. Salva, Google Cloud

我问开发者是否能够创建自己的代理——例如，创建一个 “电子商务专家” 代理？

他回答说，自定义代理是 Google 对 Gemini Code Assist 的愿景，但目前他们只提供预定义的代理。

他说：“我们目前还没有让开发者去定义他们自己的专家和代理的能力，但随着我们走向全面可用性，这肯定是我们的目标。”

虽然今天的 I/O 大会上没有关于 Code Assist 代理的具体更新，但 Google 宣布了 Gemini Code Assist 中 “更多的自定义选项”——包括 “更多的方式来定制工作流程以适应不同的项目需求，更容易地从你上次离开的地方继续完成任务，以及新的工具来执行团队的编码标准、风格指南和架构模式。”

## 学习信任 AI 代理

Salva 进一步深入地介绍了 Google 的编码代理方法，他认为开发者与 AI 工具的交互方式正在发生转变。开发者正在从低信任、高监督的 AI 工作模式，转向 “自主性越来越高、信任度越来越高的地位”，他说。

根据 Salva 的说法，开发者与 AI 之间有四种交互模式——每一种都比上一种更复杂。

- 预测文本，用于简单的代码补全。
- 聊天：AI 辅助的编码任务对话。
- 协作式 “氛围编码”：使用 AI 进行广泛、协调的代码更改。
- 代理模式：AI 在后台自主运行，可能会在没有直接监督的情况下进行更改。

显然，第四种——代理模式——是编码工具炒作周期中所处的阶段。Google 似乎正在通过强调 SDLC（软件开发生命周期）中的代理来定位自己。或者正如 Salva 所说，“我们如何引入越来越多的这些代理来帮助开发者有效地完成他们的工作——不仅是编写代码，还要提高代码质量。”
相关新闻方面，谷歌今天还宣布 Gemini 2.5 现在为 Gemini Code Assist 提供支持，并且 Code Assist 的付费客户将在“Vertex AI 上可用时”获得 200 万个 token 的上下文窗口。

Gemini 2.5 于 3 月底发布，谷歌[称其为](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/)“我们最智能的 AI 模型”，并补充说它“擅长创建具有视觉吸引力的 Web 应用程序和代理代码应用程序，以及代码转换和编辑。”

这引出了与 GitHub Copilot 的另一个不同之处。顾名思义，Gemini Code Assist 仅使用一种 LLM（Gemini）。但 GitHub Copilot 提供了一系列模型，例如 Claude 3.7 Sonnet、OpenAI o1 和 Google Gemini 2.0 Flash。我问 Salva 为什么 Code Assist 仅限于 Gemini。

“我们使用 Gemini 模型的原因，首先也是最重要的原因是它们实际上是非常好的编码模型——因此我们从中获得了良好的结果。而且，我们同时制造工具和模型的一个真正好处——在非常、非常紧密的组织合作中——是当我们与工具本身紧密结合时，我们可以更快地改进模型。”

他在这里暗示的是，Code Assist 与 Google Cloud 生态系统紧密集成——就像 Google 的其他 AI 产品一样。在[四月份的 Cloud Next 公告](https://cloud.google.com/blog/products/application-development/an-application-centric-ai-powered-cloud)中，Google 宣布了 Gemini Cloud Assist，它“在 Google Cloud 环境中的整个应用程序生命周期中提供 AI 驱动的帮助”。Code Assist 略有不同，因为它也可以供个人免费使用，但同时它也正在成为 Google 企业云平台的重要组成部分。

## AI 代理语义

谷歌或微软的 AI 代理哪个对开发者更有效，还有待观察。尽管 GitHub 的产品似乎更进一步——现在已提供给他们付费最高的客户。Gemini Code Assist 代理仍在私有预览中。

我还注意到，谷歌在描述编码代理方面更加谨慎。GitHub 最近一直将其代理技术称为“[peer programming](https://thenewstack.io/github-copilot-wants-to-become-your-peer-programmer/)”（对“[pair programming](https://thenewstack.io/advance-your-devops-with-pair-programming-even-remotely/)”一词的戏仿，后者是一种更传统的 IT 技术）。另一方面，谷歌将 Code Assist 称为“开发人员的编码助手”。也许我对此解读过多，但“peer”意味着地位相等的人或事物，而“companion”一词可以像应用于人类（或 AI 代理）一样应用于狗。

我们将看到 AI 代理最终会更接近人类同伴还是犬类同伴。无论如何，我们已经真正进入了 AI 编码代理的时代。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)