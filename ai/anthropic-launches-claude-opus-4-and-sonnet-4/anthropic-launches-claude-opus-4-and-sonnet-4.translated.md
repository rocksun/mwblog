# Anthropic 发布其最强大的编码模型

![Featued image for: Anthropic 发布其最强大的编码模型](https://cdn.thenewstack.io/media/2025/05/45c94973-img_0980-1024x768.jpg)

旧金山 — 在其首次开发者大会 [Code with Claude](https://www.anthropic.com/news/Introducing-code-with-claude) 上，人工智能公司 Anthropic 今天[发布](https://www.anthropic.com/news/claude-4)了其大型语言模型 (LLM) 的最新版本：Claude Opus 4 和 Claude Sonnet 4。

这些更新承诺为开发者和工程团队带来重大进步，尤其是在编码和长上下文推理方面。在所有与编码相关的基准测试中，这两种模型都轻松超越了其前代产品，尽管在视觉推理等其他领域，旧的 Sonnet 模型实际上优于新的模型。

虽然 Sonnet 3.7 已经提供了一种混合方法，既有快速响应，又有用于更深入推理的扩展思考模式，但 Opus 4 之前缺乏这种可调节的能力。此更新将相同的双模式功能带到 Opus 4。

![Anthropic 首席执行官 Dario Amodei](https://cdn.thenewstack.io/media/2025/05/12f6fe38-anthropic-amodei.jpeg)

Anthropic 首席执行官 Dario Amodei 在该公司的 Code with Claude 会议上。图片来源：The New Stack。

这些新模型可立即在 Anthropic 自己的 API、Amazon Bedrock 和 Google 的 Vertex AI 等平台上使用。Claude Sonnet 4 在 Claude.ai 上免费提供，而 Opus 4 则供付费用户使用。

“Claude 4 标志着人工智能协作的新时代，”该公司表示。“我们正在构建 Claude，使其成为您值得信赖的合作伙伴——以完整的上下文运行，持续关注更长的项目，并在每一步都推动变革性影响。”

![Anthropic benchmarks for Opus 4 and Sonnet 4](https://cdn.thenewstack.io/media/2025/05/ec51a21a-claude-4-benchmarks.png)

图片来源：Anthropic。

## Opus 4

Opus 是 Anthropic 旗舰模型的名称。当 Opus 3 在一年多前[发布](https://www.anthropic.com/news/claude-3-family)时，它巩固了 Anthropic 作为提供一些最佳编码用例模型的声誉。该公司将 Opus 4 描述为其迄今为止最强大的模型，也是“世界上最好的编码模型”。该公司表示，它还擅长解决问题和为代理产品提供动力。

与此同时，GitHub 使用 Claude 作为其新的软件工程 (SWE) 代理的基础，表示使用 Opus 4 实现了 9% 的更好结果，同时减少了 30% 的 tokens。

![Claude 玩口袋妖怪](https://cdn.thenewstack.io/media/2025/05/87caa1cc-claude-plays-pokemon.gif)

Claude 玩口袋妖怪。图片来源：Anthropic。

在某种程度上，Opus 4 的突出之处在于它可以处理长时间运行的任务，并在 Anthropic 描述的“数千个步骤”中保持其上下文。该模型的一些测试人员已经能够

这种新功能。“Opus 4 为编码提供了真正先进的推理能力，”Rakuten 人工智能总经理 Yusuke Kaji 说。“当我们的团队在一个复杂的开源项目上部署 Opus 4 时，它自主编码了近七个小时——这是人工智能能力的一次巨大飞跃，让团队感到惊讶。”

Anthropic 保持了使用 Opus 4 的价格与之前的版本相同，API 使用费为每百万个输入 tokens 15 美元，模型输出为每百万个 tokens 75 美元。

![SWE-bench](https://cdn.thenewstack.io/media/2025/05/c1332f04-4_swe-bench.png)

图片来源：Anthropic。

## Sonnet 4

像包括 OpenAI 和 Google 在内的大多数其他 LLM 公司一样，

以不同的价格点提供各种模型（Haiku 今天没有更新，是该公司最快、最便宜的模型，但也是最不智能的模型。）对于 Sonnet 4，Anthropic 表示，这个新版本改进了 Sonnet 3.7，后者长期以来一直领先于 [SWE-bench](https://www.swebench.com/) 基准测试，用于评估软件工程任务的模型。它现在的得分为 72.7%，而之前的版本为 62.3%。

Anthropic 声称：“该模型在性能与内部和外部用例的实用性之间取得了平衡，同时提供了增强的可操纵性，使您可以更好地控制它如何实施更改。”

在今天于旧金山举行的公司发布会上，Anthropic 首席执行官 Dario Amodei 还指出，Sonnet 4 不像其前代产品那样过于热切，这是使用之前版本的开发人员的常见抱怨，他们经常认为它与 Sonnet 3.5 相比有点令人失望。

Anthropic 改进的不仅仅是模型本身。它还为用户如何使用这些模型添加了一些新功能。Opus 4 和 Sonnet 4 现在都可以使用工具，包括网络搜索，同时思考问题。这里最有趣的是，他们可以在工具使用和推理之间来回切换，因为他们试图改进他们的响应。他们甚至可以并行使用多个工具。
此外，在允许的情况下，这些模型现在可以访问本地文件。Anthropic表示，这使它们能够“展示显著提高的记忆能力，提取和保存关键事实，以保持连续性并随着时间的推移建立隐性知识”。

Anthropic还保持了Sonnet 4的价格稳定。仍然是每百万token 3美元/15美元（输入/输出）。

## Claude Code

除了新的模型之外，Anthropic还在今天正式发布其代理式编码工具Claude Code。Claude Code可以存在于终端中，现在也可以存在于开发者的IDE中。Anthropic正在为VS Code和JetBrains提供扩展。这使其直接与GitHub Copilot以及Cursor和Windsurf等工具展开竞争（为了使事情更有趣，后者也在其工具中向开发者提供Anthropic的模型）。

Anthropic还在发布一个新的Claude Code SDK，以便开发者可以使用Claude Code代理作为核心来构建自己的代理和应用程序。

SDK的示例代码非常有趣：它是GitHub上的Claude Code。有了这个，开发者现在可以在pull request上标记Claude，以“响应审查者的反馈、修复CI错误或修改代码”。Anthropic和GitHub长期以来一直是密切的合作伙伴。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。