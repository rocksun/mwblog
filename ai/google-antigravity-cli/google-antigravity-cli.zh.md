**在上周的 Google I/O 大会上**，该公司宣布 Gemini CLI 的终结拉开帷幕——也就是说，除了企业用户和拥有 API 密钥的用户外，所有人都是如此。从 6 月 18 日开始，许多用户将失去对 Gemini CLI、Gemini Code Assist IDE 插件以及 GitHub 版 Gemini Code Assist 的访问权限。

取而代之的是，开发者可以转向 Antigravity CLI，这是一个闭源平台，不仅缺少一些功能，而且其使用限制已经让部分开发者感到沮丧。

## 为什么会这样？

在其[发布声明博客](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)中，Google 表示，推出 Antigravity CLI 是为了应对社区不断变化的需求：“听取你们的反馈让我们明白了一件事：将精力倾注在为当今多智能体（multi-agent）现实而构建的单一产品上，才能最好地为你们服务。”

该产品 Antigravity CLI 是一个“首创的智能体优先开发平台”，包含一个服务端框架和全新的终端体验。Google 表示，Antigravity 仍能让用户快速获得解答、构建和搭建新项目，以及配置云基础设施，但它会更加敏捷。此外，得益于全新的统一架构，Antigravity 可以在后台协调多个智能体以处理复杂任务，并确保对核心智能体的改进能普遍应用。

但从 Gemini CLI 用户的首波反馈来看，许多人似乎认为自己吃亏了。

## 至少在目前，它的功能较少

“它不会一上来就实现 1:1 的功能对等，”Google 表示。它没有说的是，这种对等何时才会实现，甚至是否会实现。

> “它不会一上来就实现 1:1 的功能对等。”

与此同时，开发者可以通过 Antigravity 插件使用 Google 所谓的 Gemini“最关键功能”：智能体技能（Agent Skills）、钩子（Hooks）、子智能体（Subagents）和扩展（Extensions）。

## 它不是开源的

与 Gemini 不同，Antigravity 不是开源的。虽然 [Gemini GitHub 页面](https://github.com/google-gemini/gemini-cli)上代码密集且有数百名贡献者列表，但相比之下，[Antigravity 的 GitHub 页面](https://github.com/google-antigravity/antigravity-cli)却显得空空如也。

开发者们似乎并不买账。正如一位 [Reddit 用户](https://www.reddit.com/r/GeminiCLI/comments/1thweon/comment/omq0tt5/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)所指出的：“我没看到任何迹象表明 Antigravity CLI 会开源，我在 Gemini CLI 之上构建了各种自定义层，失去它们我会很伤心。而且我对使用限制感到非常焦虑。”

## 它的实际使用成本可能更高

其他开发者不仅对使用限制感到焦虑，他们甚至已经遇到了问题。[GeminiCLI Reddit 社区](https://www.reddit.com/r/GeminiCLI/)里充满了 Antigravity 用户的沮丧评论，他们表示新平台让他们更快地达到了使用上限，这实际上可能使新平台比 Gemini 更加昂贵。

“我可以告诉你，Antigravity CLI 的配额非常低，刚刚尝试用 Kotlin 设计几个屏幕，Token 就用完了，”一位 Reddit 用户说道。另一位补充道，“即使是 Pro 用户，也只用了 6 到 7 次提示词（prompts）就达到了使用限制，这太疯狂了。以前我用 Gemini CLI 制作整个项目也才消耗 13% 的配额。”

还有更多人加入了吐槽，有人质疑 Antigravity 是否已经准备好推出：“限制设置有问题；即使订阅了，配额也低得灾难性。文档非常糟糕。他们不应该在处于这种状态时发布它。”

使用限制的问题似乎是普遍现象，最终可能会迫使一些用户放弃使用。“如果他们不每天刷新，我就会取消我的 Google 订阅，转而使用 Codex 或 Claude Code。如果 CLI 配额没了，Pro 订阅就是一个笑话，”另一位 Reddit 用户写道。

“刚刚切换到 Antigravity CLI，但在还能用的时候我要换回 Gemini CLI，我的 Token 消耗得太快了，”还有人说。

但换回来的时间窗口正在迅速关闭。

## 除了企业用户和拥有 API 密钥的用户，其他人都要倒霉了

6 月 18 日，Google AI Pro、Ultra 和免费用户将失去对 Gemini CLI、Gemini Code Assist IDE 插件以及 GitHub 版 Gemini Code Assist 的访问权限——但企业用户和拥有 API 密钥的用户是安全的。

对于拥有付费 Gemini 和 Gemini Enterprise Agent Platform API 密钥的用户，仍可访问 Gemini CLI。同样，对于通过 Gemini Code Assist Standard 或 Enterprise 许可证使用 Gemini CLI 或 IDE 插件的用户，以及通过 Google Cloud 使用 GitHub 版 Gemini Code Assist 的用户，其访问权限将保持不变。

## 这就是现在的趋势吗？

“不久前我还渴望听到一些关于 AI 的新闻，因为我期待着一些新的突破。现在，每一次发布基本上都是‘我们要让 AI 变得更贵了’，”一位 Reddit 用户感叹道。

> “现在，每一次发布基本上都是‘我们要让 AI 变得更贵了’。”

如果说这些用户因为许多 Reddit 网友反映在 Antigravity 上消耗配额比 Gemini 更快而感到不悦，那么对于 [Anthropic 拆分计费并将 Agent SDK 推入独立的信用额度池](https://thenewstack.io/anthropic-agent-sdk-credits/?utm_source=chatgpt.com) 以及 [GitHub 将 Copilot 转向基于使用量的计费模式](https://thenewstack.io/github-copilot-usage-billing/?utm_source=chatgpt.com)，他们可能也会同样感到郁闷。这些举措正是 AI 成本不断攀升这一增长趋势的一部分。