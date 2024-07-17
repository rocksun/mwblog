# 2024 年软件工程师的 AI 工具：现实检验（第一部分）

### 软件工程师如何在软件开发工作流程中使用 GenAI 工具？我们避开炒作，看看技术专业人士使用 LLM 进行编码和其他任务的现实情况。

去年 4 月，我们发布了[AI 编码工具的生产力影响](https://newsletter.pragmaticengineer.com/p/ai-coding-tools)，该文章基于对本通讯订阅者的调查，内容是关于新的 AI 工具如何帮助开发人员进行编码。当时，ChatGPT 和 GitHub Copilot 是主要的工具，并且在那个实验时期，[更多工具正在路上](https://blog.pragmaticengineer.com/github-copilot-alternatives/)。

根据当时读者的反馈，文章建议尝试使用 AI 编码工具，找出哪些有效，哪些无效，并预测：“AI 编码工具将推动行业发展。”

快进到 2024 年，AI 编码工具比以往任何时候都更加普及。GitHub Copilot 已经拥有超过 100 万付费用户（可以安全地假设大多数是开发人员），并且涌现出一批初创公司构建 AI 软件工程工具，同时也不乏炒作。

AI 炒作周期最近达到顶峰，一些初创公司筹集资金以[“用 AI 工程师取代开发人员](https://newsletter.pragmaticengineer.com/i/142616988/is-the-ai-developera-threat-to-jobs-or-a-marketing-stunt)”。*本出版物对该“使命”和类似使命的看法是，它们是针对 GitHub Copilot 的流行而产生的过热的营销口号，并非现实。*

**但是，工程师在 2024 年** **真的** **如何使用这些工具？**

为了避开炒作并解决这个问题，我们最近发起了一项新的调查，询问软件工程师和工程经理您使用 AI 工具的实际经验；今年使用哪些工具，哪些开发工作流程部分是 AI 增强的，哪些有效，哪些无效？

据我们所知，这是迄今为止关于技术专业人士如何使用 AI 工具的最大规模调查，本出版物的商业模式意味着我们在该主题上不受偏见。响应的数量之多，以至于整理数据花了几个月时间，但今天我们将其呈现出来！

我们分析了来自本通讯订阅者的意见，并力求提供一个平衡、务实和详细的视角，了解 LLM 驱动的开发工具的现状。

本文涵盖：

**调查概述**。本调查中的大多数数据来自软件工程师，在使用 AI 工具不到 6 个月、6-12 个月或超过一年的人员之间大致平均分配。**流行的软件工程 AI 工具**。ChatGPT 和 GitHub Copilot 仍然是最受欢迎的工具。谷歌的 Gemini、Anthropic 的 Claude、Jetbrains AI、Codeium 以及其他工具紧随其后。**AI 辅助软件工程工作流程**。一些最常见的工作流程是在 IDE 中使用 Copilot，与 AI 机器人聊天而不是谷歌搜索，AI 辅助调试，以及学习不熟悉的语言和框架。还有许多有用的、创新的用例。**优点**。当 AI 工具运行良好时，它们在完成项目、提高测试覆盖率和简化实验方面有很大帮助。**缺点**。输出质量差、幻觉以及开发人员过度信任这些工具，是投诉最多的问题。**自去年以来发生了什么变化？**令人惊讶的是，变化并不大！交互式橡皮鸭调试更加普遍，团队正在更多地尝试使用 AI 代理。

*本文底部可能在某些电子邮件客户端中被截断。在线阅读完整文章，不受干扰。*

## 1. 概述

共有 211 名技术专业人士参与了调查，比[去年的 AI 工具问卷调查](https://newsletter.pragmaticengineer.com/p/ai-coding-tools)的 175 份响应有所增加。

**职位：**大多数受访者是个人贡献者（约 62%）。其余人员担任各种工程管理职位：

我们向工程领导者提出了额外的问题，因为这些人处于有利位置，可以了解 AI 工具对团队的影响。*我们将在后续文章中介绍工程领导层的观点。*

**经验：**受访者的职业生涯长度被细分为五年期，最高可达 20 多年的技术行业经验（YOE）：

有趣的事实：一位受访者拥有 60 年的专业开发经验（！！）这位开发人员现在半退休了。他对这些工具的看法（他计划在未来使用这些工具）是积极的，他写道：

“在过去的 60 年里，我见过许多其他被吹捧为软件开发人员终结者的技术。它们都没有达到炒作的水平。这是一个新时代，AI 看起来可能是一个很有希望的机会，可以推动软件设计和开发的边界。这是一个激动人心的时代，让我们见证未来的繁荣。”
**使用 AI 工具花费的时间：**同样，在使用 AI 工具的新手（6 个月或更短时间）、使用 AI 工具 6-12 个月的人以及使用 AI 工具超过一年的人之间，比例相当均衡。
来自不使用 AI 工具的人的回复在关于这些工具的调查中可能显得有些格格不入，但我们希望接触到这些开发者并提出具体问题，以了解为什么有些人不会、不愿或不能使用它们。*我们将在以后的文章中深入探讨这个问题。*

**公司规模：**从小型企业到大型企业，规模大致相当。拥有 1-50 人的公司占多数。
## 2. 流行的软件工程 AI 工具
ChatGPT 和 GitHub Copilot 作为软件工程领域的市场领导者，几乎不需要介绍。但它们到底有多受欢迎，开发者还使用哪些其他工具？

#### 工具
正如刚才提到的，ChatGPT 和 GitHub Copilot 在调查中占有很大比例。令人惊讶的是它们的受欢迎程度：

回复显示，使用 *ChatGPT 和 GitHub Copilot* 的专业人士数量与所有其他工具的总和一样多！以下是“其他”类别的细分；请注意，下一个最受欢迎的工具 Google 的 Gemini 仅获得了 GitHub Copilot 提及次数的 14%：

受访者对不同工具的关注度差异很大，从将所有提及一起可视化后可以清楚地看出：

此图表列出了调查中至少被提及两次的所有工具。仅被提及一次的工具包括 Microsoft Teams AI、Amazon Q、Meta AI、Vercel 的 v0.dev（从提示生成 UI）、Databricks AI 助手、Replit Ghostwriter、Ellipsis.dev（AI 代码审查和错误修复）、Mutable.ai（创建动态文档）、CodeRabbit AI（AI 驱动的代码审查）、StartCoder（代码补全）和 Aider（终端中的 AI 配对编程）。这么多工具被尝试真是太好了！

#### 最喜欢的 AI 编码工具
我们询问了开发者他们最喜欢的工具。

**GitHub Copilot 和 ChatGPT。**正如图表所示，它们获得了最多的提及。以下是一些示例：
“Github Copilot 聊天是真正的交易。” - 开发工具初创公司的工程师

“我使用 GitHub Copilot，因为它还内置了聊天功能。” - 质量控制软件供应商的 Ruby on Rails 开发者

“我每天使用 GitHub Coliplot 进行编码，使用 ChatGPT 4 进行复杂、开放式设计讨论。” - 数据工程师

“GitHub Copilot 的自动补全功能很好 [但] 我发现它的聊天功能毫无用处。它与“从描述生成代码”功能一样。当我需要一个 leetcode 函数，例如“根据 Y 分区数组 X”时，我喜欢使用 chatGPT，因为它运行良好。但 ChatGPT 在更难的问题上会卡住。例如，构建复杂的 typescript 泛型超出了它的处理能力。” - 规模化公司的工程师

“我目前只使用 Copilot。我曾经使用过免费的 ChatGPT，偶尔我会回来使用它来做一些特定的事情。” - 网络安全初创公司的软件工程师

GitHub Copilot Chat 被提及了很多次，大多是积极的。一个很大的优势是它提供了一种替代方案，可以避免打开浏览器使用 ChatGTP。尽管如此，并非所有人都对市场领先的 AI 的功能感到震惊，包括一位资深软件工程师，他的不满情绪很难忽视：

“我最喜欢的是 GitHub Copilot。在我可以使用的所有 AI 工具中，它是最好的。”

另一位受访者分享说，他们的公司评估了 8 种 AI 编码工具，最终选择了 GitHub Copilot，这似乎在公司购买部门级许可证以及开发者从其他工具迁移到 GitHub Copilot 方面具有优势：

“我最初使用的是 Tab9。之后，我的公司为我提供了免费的 GitHub Copilot 选项，所以我开始使用 Copilot！” - 质量控制软件供应商的 Ruby on Rails 开发者

几位受访者表示，ChatGPT 是他们唯一使用的工具，并且他们很喜欢它。一家电子竞技公司的软件工程师分享道：

“如果我想对某件事进行推理，而身边没有同事可以咨询，我会使用 ChatGPT。”

**其他工具**也获得了荣誉提名，成为一些开发者最喜欢的工具：
– Opus 模型 – 被多次提及为最佳编码模型。这发生在 Claude 3.5 Sonnet 模型发布之前，该模型在编码任务方面更加熟练，[Claude](https://claude.ai/) [根据](https://www.anthropic.com/news/claude-3-5-sonnet)Anthropic 团队的说法，他们使用该模型来开发自己的产品；这意味着我们可以预期 Claude 的受欢迎程度会提高。在 ChatGPT 和 Copilot 之后被提及最多。一些受访者认为 Gemini 在编码任务方面比 ChatGPT 更好，并且更喜欢使用它而不是 OpenAI 的聊天机器人。一位受访者表示，他们在 Gemini 和 Claude 之间交替使用，以衡量哪一个更适合每个用例。[Gemini](https://gemini.google.com/)。多次被提及为最喜欢的 IDE，这得益于其代码感知的自动完成功能。[Codieum](https://codeium.com/) 也被多次提及，一位受访者称其为“游戏规则改变者”。[Cursor](https://www.cursor.com/) 和 [Perplexity](https://www.perplexity.ai/?__cf_chl_tk=APpQg437C4fCJZbe8j8GXHNAuOXSZV7maVZal8F3Dfw-1720786519-0.0.1.1-8062) [Phind](https://www.phind.com/) **其他工具：**[Aider](https://aider.chat/)(终端中的结对编程)，[JetBrains AI](https://www.jetbrains.com/ai/)，[AWS CodeWhisperer](https://aws.amazon.com/blogs/aws/amazon-codewhisperer-free-for-individual-use-is-now-generally-available/) 和 [Rewatch](https://rewatch.com/)(会议记录) 每个都有一次提及

## 3. AI 辅助软件工程工作流程

我们询问了使用 AI 工具超过六个月的受访者，他们或其团队的 AI 辅助工作流程是什么样的。可以观察到一些趋势：