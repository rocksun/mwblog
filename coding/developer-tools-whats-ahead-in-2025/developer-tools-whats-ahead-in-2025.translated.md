# 开发者工具：2025 年的展望

![开发者工具：2025 年的展望特色图片](https://cdn.thenewstack.io/media/2023/12/95c34a5e-year-forecast-1-1024x576.png)

随着一场革命的临近，首先显而易见的变化是态度的转变。

开发者工具通常不是快速革命性变化的领域。但是，将[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms)添加到工具链中正在颠覆一切。问题是LLM提供的变化是否真正符合人们真正想要的变化。以下是我在2025年看到的开发者工具的趋势：

## 大型语言模型和生成式 AI

我们开始意识到，大型LLM供应商不仅使用他们不拥有的数据来训练他们的模型，而且基于云的AI能够看到许多他们也可以从中受益的私人信息。

就像[谷歌](https://cloud.google.com/?utm_content=inline+mention)知道每个人都在搜索什么，因为我们告诉他们一样，LLM供应商希望你的查询始于他们的云端，仅仅出于这个原因，开发将保持快速但狭窄。

业务查询不会直接发送给[Sam Altman](https://thenewstack.io/what-openai-ceo-sam-altman-really-expects-in-ais-future/)的解决方案显然会继续存在，但总是落后于其他一切。我立即看到像[CodeGate](https://thenewstack.io/codegate-open-source-tool-secures-ai-coding-assistants/)这样的解决方案，试图在你的AI工作流程和供应商之间设置防火墙，既突出了也可能减轻了这个问题。当然，公司认为其本地机密（密码等）是敏感的，但各种信息泄露都比这更敏感。

一旦人们开始考虑并限制他们的查询明确告诉供应商的内容，他们可能会在使用托管[LLM](https://thenewstack.io/llm/)的方式上变得更加保守。这将在来年持续僵持。

现在，[自主系统](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/)可能只代表一系列并非完全可靠的查询，并且相乘在一起，微小的错误可能会使端到端查询无法使用。在任务已知、简化且将以高精度成功完成的未来环境中，自主系统将蓬勃发展。但不是今年。

如果你学会了风帆冲浪，你可能会记得不会逆风逆流航行的难题，这意味着所有初学者都会被吹到海滩的同一部分。越来越多的偶然开发者会发现自己搁浅了，因为他们借助LLM的帮助取得了超出他们理解能力的进展——然后卡住了。

这可能是一个教学机会，我希望一些道场式的教学网站会转向那些平静的风帆冲浪者，并说服他们回去学习一些开发基础知识。

生成式AI，特别是艺术资产，将继续提高质量，并将成为互联网上的祸害，直到可以内置水印解决方案。然而，随着生成输出质量的提高，以及潜在成本的提高，我认为情况可能会发生逆转，生成式AI可能会寻求保护以防止水印。进行更深入查询的代币成本正在迅速上升。

## WebAssembly

[WebAssembly (Wasm)](https://thenewstack.io/webassembly/) 将继续为开发者提供选择，尽管现在你仍然需要复杂的[Javascript](https://thenewstack.io/webassembly/will-javascript-become-the-most-popular-webassembly-language/)粘合代码来与之交互。然而，浏览器中的接近原生性能是一个不容忽视的选择。

向网络简化回归的趋势似乎与客户端的Wasm相矛盾。但随着时间的推移，Wasm可能会逐渐被接受为网络的自然（即使是新的）组成部分。无论开发者使用它来只保存一次内部代码，还是为了可移植性或前端速度来加快一组操作，它都将继续出现在项目中和项目周围。[Moonbit](https://thenewstack.io/moonbit-wasm-optimized-language-creates-less-code-than-rust/)就是一个我看到的例子，它提供了一种新的语言，用于创建比传统语言管理的更小的Wasm可执行文件。

## Fediverse
基于ActivityPub的[fediverse](https://thenewstack.io/the-fediverse-what-it-is-why-its-promising-whats-next/)平台仍有待进一步发展。目前，它仍处于等待被大众发现的阶段。但作为一个开放平台，它拥有成为其他应用通信基础的最佳起点。fediverse中已经不仅仅只有[Mastodon](https://thenewstack.io/developers-mastodon-and-bluesky-want-your-twitter-bots/)。但尚未出现其他“杀手级应用”，尽管它们可能在2025年出现。（我清楚地知道，fediverse中感到满意的人并不寻求名利。）

Bluesky的成功并非归功于[AT协议](https://thenewstack.io/blueskys-at-protocol-pros-and-cons-for-developers/)，但我们都知道，鉴于没有“单一”的Mastodon服务器，劝说新用户尝试Mastodon证明了它的致命弱点——而Bluesky今年从中获益。但这仅仅意味着其他项目可能更符合人们的心理模型。

有人会尝试创建一个新的基于AT协议的服务器系统，这将增加对该系统的工具开发兴趣。相反，在出现[bluesky.social](https://bsky.social/about)的替代品之前，人们会一直议论这个庞然大物看起来有点熟悉。

## 小型团队的更多新项目

启动小型新项目的成本持续下降。虽然代码辅助无法提供创新，但它可以帮助忙碌的开发者尝试更多超出他们知识范围的事情，而这通常是维护开发软件所需做的。

另一方面，一旦某个库或系统获得关注，那么LLM可能会将其作为示例推荐给其他开发者（我们假设如此）。可发现性仍然良好，正如我一年来所展示的，有很多优秀的案例说明如何启动、展示并帮助新用户加入你的新项目。

网络[playground](https://thenewstack.io/playgrounds-for-developers-uses-and-design-patterns/)仍然是让人们体验你的新工具的最有效方式。因此，我预测启动新的开发语言和基于开发者的项目的趋势将持续下去。一个已经沉寂一段时间了的项目，[darklang](https://darklang.com/)，应该会在2025年重新出现。

如果你的新项目在新的一年推出，我有机会会报道它。在此之前，祝一切顺利。

[YOUTUBE.COM/THENEWSTACK 科技发展日新月异，不要错过任何一期节目。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)