# Eclipse Theia：AI工具的“DeepSeek”时刻？

![Featued image for: Eclipse Theia: The ‘DeepSeek’ of AI Tooling?](https://cdn.thenewstack.io/media/2025/03/2ba92d47-planet-volumes-w1hqljythcm-unsplash-1024x644.jpg)

[Eclipse 基金会](https://thenewstack.io/alternative-to-visual-studio-marketplace-gains-momentum/)最近发布的 [Theia AI](https://theia-ide.org/docs/theia_ai/) 平台能否成为 [AI 工具](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/)领域的“[DeepSeek](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/)”？

嗯，基金会执行董事 [Mike Milinkovich](https://www.linkedin.com/in/mikemilinkovich/?originalSubdomain=ca) 的愿景有可能会实现。

Eclipse 上周发布了其用于构建 AI 工具的平台 Theia AI 的生产版本，以及一个 AI 驱动的 IDE ([Theia IDE](https://theia-ide.org/)) 的 alpha 版本，该版本展示了该平台的功能。

## DeepSeek 时刻

在一次采访中，Milinkovich 和 [Jonas Helming](https://www.linkedin.com/in/jonas-helming-76303b28/)（[EclipseSource](https://eclipsesource.com/) 的 CEO，负责 Theia AI 项目）将 Theia 定位为 AI 工具领域潜在的“DeepSeek 时刻”，指的是 DeepSeek 如何挑战了传统观念，即前沿 AI 模型需要大量的资本投资。Milinkovich 说，类似地，Theia 旨在表明可以使用开源而不是专有解决方案来构建高质量的 AI 开发者工具。

“我们并不是说 Theia 是 AI 工具领域的 DeepSeek，但从某种意义上说，它可能需要社区和希望在其之上构建产品的公司的投资和参与，才能使其达到并保持与功能对等的水平，”他说。

EclipseSource 是一家 IT 服务公司，也是 Eclipse 基金会的创始成员，它将 Theia 技术贡献给了该基金会。

Milinkovich 和 Helming 认为，目前是一个关键时刻，行业必须决定 AI 工具将主要采用开源还是专有模式。他们将 Theia 与资金雄厚的竞争对手进行对比，例如广受欢迎的 AI 驱动的代码编辑器 [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)（由 [Anysphere](https://anysphere.inc/) 创建，估值 [接近 100 亿美元](https://www.bloomberg.com/news/articles/2025-03-07/ai-startup-anysphere-in-talks-for-close-to-10-billion-valuation)）和 [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/)。

Helming 称 Anysphere（及其 Cursor）是“该领域的宠儿”，并表示大多数工具初创项目“基本上都是从 fork VS code 开始，并以这种方式工作，但他们实际上可以使用 Theia 框架，并降低构建这些工具的成本，因为它更好、更快、更智能，而不是从你自己的 VS code fork 开始，”他说。

其次，他补充说，“与其购买一个未来由单一供应商提供 AI 工具的世界，不如选择一个替代解决方案，该解决方案将对 Theia 这样的协作项目进行一定量的投资，以在功能上与这些资金雄厚的初创公司相匹配，但成本大大降低，并且围绕协作项目建立一种不同的商业模式，而不是将其作为单一供应商解决方案来做。”

## 看起来像一个 Fork

[David Mytton](https://www.linkedin.com/in/davidmytton/)，Arcjet 的 CEO 告诉 The New Stack，Theia IDE 看起来像一个 VS Code fork，但实际上并非如此。

“它有一个独立的代码库，在组件（如 [Monaco editor](https://microsoft.github.io/monaco-editor/)）和 VS Code 扩展兼容性方面有一些交叉，”Mytton 说。“他们对 Theia AI 采取了类似的方法，Theia AI 是他们用于构建 AI 功能的框架，在该框架中，模型和 UX 可以互换。”

事实上，Theia AI 为开发者提供了灵活性、透明性和选择自由，这与专有解决方案不同。它还允许开发者使用任何 LLM，包括本地模型，为透明性和灵活性提供了显著优势。工具构建者可以将他们选择的 LLM（基于云、自托管或本地）集成到自定义工具和 IDE 中。
Eclipse 使用 Theia AI 框架将 AI 构建到 Theia IDE 中，这样“它实际上是专家代理的集合——代码完成、架构助手、终端命令助手——以及创建你自己的能力。这对开发者来说是有意义的，因为他们想看到幕后的细节并自定义东西，”Mytton 说。“例如，看看人们花多少时间自定义 Vim。为 AI 工具提供支持的模型是一种商品，因此差异化必须来自构建在其之上的东西。我认为这类似于大多数 IT 基础设施都是开源的，因此商业价值来自构建在其之上的应用程序。”

## 一项值得注意的创新

与此同时，“自从 ChatGPT 首次问世以来，围绕 AI 和 LLM 的故事情节主要围绕着‘你需要巨额资本投资才能生产出前沿模型……’而 DeepSeek——顺便说一句，它声称自己是一个开源 LLM，并且它的代码在 MIT 许可下可用——通过证明以更低的成本构建一个非常高性能的 LLM 是可能的，真正非常戏剧性地改变了传统的观念，”Milinkovich 说。

[Arnal Dayaratna](https://www.idc.com/getdoc.jsp?containerId=PRF004946) 是 IDC 的一位分析师，他对此深有体会。
他认为 Eclipse Theia AI 标志着开发者工具领域的一项值得注意的创新，因为它认识到大型语言模型在现代软件开发中的变革性作用。

“[通过提供灵活的 LLM 集成和可定制的 AI 驱动的工作流程，Theia 使开发者能够在他们的 IDE 中无缝地利用 AI 功能，”Dayaratna 告诉 The New Stack。“这种能力至关重要，因为开发堆栈在不断发展，特别是 AI 和生成式 AI 是当代编码和测试工作流的核心。Theia 的开放框架允许开发者选择和配置他们首选的 LLM，确保 AI 辅助与特定项目的需求以及他们工作的组织的相关监管和合规要求相一致。”

此外，Theia IDE 还包括以下功能：

*   **与外部工具和上下文数据集成**：通过[模型上下文协议 (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)集成，开发者可以将 AI 驱动的工作流程与外部工具、服务和上下文数据连接起来，从而增强开发环境中的自动化和互操作性。
*   **确保开源许可证合规性**：[SCANOSS](https://www.scanoss.com/)集成分析 AI 生成的代码的开源许可合规性，帮助开发者在合并 AI 生成的代码时降低法律和运营风险。

“[很高兴看到 Eclipse 基金会团队专注于 MCP，它基本上充当了支持性数据源的插件协议。请注意，Eclipse 并不是第一个将 MCP 引入其工具中的，”The Futurum Group 的分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 说。

Shimmin 指出，在整个软件行业中，AI 辅助开发已迅速成为常态，AI 增强和自动化范围从基本的提前输入工具到完全无需动手的 [“氛围”编码](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/) 工具（如 Cursor）。

“基本上，市场上每个 IDE 都已全力投入到这个机会中，由主要的 IDE 开发者 Microsoft 和 JetBrains 以及新来者 Zed 和开源主力 Vim（好吧，Neovim）、EMACS 和 Eclipse 领导，”他告诉 The New Stack。

## 构建 Agentic AI 解决方案

此外，Shimmin 表示，Eclipse 基金会新发布的 IDE 在将 AI 引入前台方面做得非常出色。

“但这个版本有趣的地方不仅仅在于该工具使用 AI（特别是 GenAI）来生成任何旧代码。相反，Eclipse 基金会开源社区已决定着手解决构建 agentic AI 解决方案的难题，”他说。“这意味着帮助开发者处理模型、工具、上下文和支持性数据资产。后者最为重要。如果没有数据，GenAI 模型和 agentic AI 流程就什么都不是。但是，及时访问高质量数据仍然是企业希望构建 GenAI 成果（agentic 或其他）的最大挑战。”

## Eclipse 历史重演

Helming 表示，Theia AI 和 Theia IDE 的举动“在某种程度上是历史的重演，从某种意义上说，如果你回想 24 年前，最初的 Eclipse IDE 是一个非常成功的构建工具的平台，”他说。“然后他们构建了团队在其之上构建了一个 IDE，以证明该平台可用于构建该专业质量的 IDE。”

事实上，Constellation Research 的分析师 Holger Mueller 认为，很高兴看到 Eclipse 基金会没有让开发者陷入困境。
“AI 正在改变代码的编写、管理和审查方式。为了保持并提高开发者的速度，开发者希望并且需要使用他们选择的 AI 工具，特别是模型，”他说。“能够选择他们喜欢的工具是 IDE 的一项关键能力，Eclipse 基金会通过 Theia 提供了这种能力，这很好。”

## 激烈的竞争

然而，Arcjet 的 Mytton 表示，问题在于现在有很多编辑器。

“它已经从 VS Code 成为唯一受关注的编辑器，转变为突然爆发的竞争。这是一个很难参与的领域，”他说。

尽管如此，可以肯定的是，“现在判断它 [Theia] 是否有能力取代知名的代码编辑器和 IDE 还为时过早，但由于它认识到基础模型对于当代开发的核心地位，因此它在方向上代表了开发者工具的未来，”Dayaratna 总结道。

然而，Theia 拥有宽松的许可证，允许公司在选择的情况下在其之上构建专有解决方案。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。