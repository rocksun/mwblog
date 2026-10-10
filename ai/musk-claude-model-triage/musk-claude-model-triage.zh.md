*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 发展，并解释它们对于将这项技术投入实际工作的个人和组织意味着什么。核心理念很简单：学会使用 AI 的工作者将定义其行业的下一个时代，而本期通讯旨在帮助您成为其中之一。*

---

埃隆·马斯克周三在 X 上发布了一则“[重要通知](https://x.com/elonmusk/status/2107724314451878104)”，谈到了 SpaceX 于 8 月推出测试版的 AI 智能体 Grok Bot：“关于 Grok @Bot 的重要通知：展望未来，@SpaceX 将为任何给定任务使用最佳的后端模型，包括 Claude Opus 5.5、MidJourney、Suno 以及其他领先的 API。无论哪种最有可能为您带来最佳结果。”

Grok Bot 是 SpaceXAI（马斯克的 AI 实验室，现已并入 SpaceX）与 Cursor 的联合产品。SpaceX 在 6 月[同意以 60 亿美元股票收购 Cursor](https://thenewstack.io/spacex-cursor-ai-coding/)，该交易已于 8 月完成。

今年 8 月，[我曾写过](https://thenewstack.io/grok-4-6-matched-fable-5-max/)，当不同模型的价格趋于收敛时，资金将流向决定哪个模型来承担工作的人。这种趋势正在越来越依赖 AI 并在尝试平衡不断上升成本的各种组织中发生。

本周我对此有了切身体会。在我们本周于某[AI 活动](https://scaleup.events/)上采访的 22 位公司高管中，至少有 10 位描述了相同的习惯：根据任务选择模型，并将昂贵的模型留给确实需要它的工作。

## 模型分诊是公司控制 AI 成本的方式

本周我和 [Cautious Optimism 通讯](https://www.cautiousoptimism.news/)的 Alex Wilhelm 以及 [*The New Stack*](https://thenewstack.io/) 的 Nick Lucchesi 一起在纽约市，我们在周一和周二参加了 Insight Partners 的 ScaleUp:AI 会议，采访了 Insight 旗下 22 家投资组合公司的运营者。请注意，Insight Partners 拥有 *The New Stack*，我们拍摄这些采访是为了 Insight 正在制作的一个视频系列。我在这里不点名任何人，也不推销他们的任何产品。这些是由经验丰富的运营人员运营的真实公司，他们告诉我们关于运行 AI 的情况与市场其余部分正在做的事情相吻合，正如下面的 OpenRouter 数据所示。

我们听到的最常见的模型分诊设置是漏斗。一家安全公司首先对所有内容运行规则引擎，并将幸存的内容传递给小型模型。大型模型只看到剩下的部分。其高管之一告诉我们，通过任何模型（甚至小型模型）运行一拍字节（petabyte）的数据将花费数百万美元。另一家公司在昂贵模型做任何事情之前，通过廉价模型向其智能体发送请求，以弄清楚用户想要什么。

成本是大多数人给出的原因。一位高管表示，他的公司最初拥有无限的 AI 预算，现在却在询问所有这些 Token 实际上买到了什么。另一位高管表示，即使在大材小用时，他的员工也一直在寻找最先进的模型，因此该公司现在向员工传授哪种模型适合哪种工作。第三位高管直言不讳地指出了激励机制：当你花费更多 Token 时，实验室的表现会更好。当然，我们交谈过的一些人靠出售小型模型为生，因此我正在相应地权衡他们的热情。

切换有其自身的风险。一位工程负责人告诉我们，他的团队在向重要潜在客户进行演示前三天换入了一个更新的模型，因为基准测试表明它更便宜且同样好。工作流崩溃了，他的团队在一个周末进行了回滚。他的教训是进行评估（evals），这是一套测试，可以在团队不得不手动发现问题之前捕捉到问题。*The New Stack* 的 Amanda Caswell 上个月[发现了该故事的供应商版本](https://thenewstack.io/claude-opus-agent-migration/)，当时 Anthropic 将 Opus 5.5 的价格比 Opus 5 降低了 20%，并破坏了智能体依赖的四项功能。

简而言之，切换前先进行测试，并遵循 ABS 规则：始终在切换（Always Be Switching）。

## OpenRouter 的排行榜显示廉价模型承担了大量业务

OpenRouter 是开发人员通过一个连接访问数百个模型的服务，它会发布流经它的数据。截至 10 月 7 日的一周内，其十个最常用的模型中有四个是“Flash”模型，这是实验室在其旗舰产品旁边推出的廉价、快速版本。Anthropic 刚刚将其廉价层级变得更便宜。[Haiku 5.5 于周三推出](https://thenewstack.io/anthropic-claude-haiku-5-5/)，每百万输入 Token 仅售 0.10 美元，对于 100,000 Token 以下的请求降价 90%，而类似的小型模型通常处理高容量任务，如分类和路由。

廉价模型承担了大部分业务。前沿模型增长最快。

截至 2026 年 10 月 7 日的一周内，按处理的 Token 计算，OpenRouter 前 10 名中的精选模型以及与前一周相比的变化。

| 模型 | 制造商 | Token | 变化 |
| --- | --- | --- | --- |
| DeepSeek V4.1 Flash | DeepSeek | 33.6T | +48% |
| GLM 5.3 Flash | Z.ai | 10.5T | -1% |
| MiMo-V2.6-Flash | Xiaomi | 10.1T | +11% |
| GPT-6 Luna | OpenAI | 6.46T | +28% |
| Claude Opus 5.5 | Anthropic | 3.37T | +74% |
| Jev 1.13 | TypeSafe | 3.32T | +12% |

前沿模型也在增长。Claude Opus 5.5 按业务量排名第九，一周内增长了 74%，是前 10 名中增长最快的模型。它在 OpenRouter 的人工分析智能指数上也排名第一。这就是从外部看到的模型分诊：昂贵模型每周承担更多的工作，而没有接近榜首。

对于 TNS 来说，Jessica Wachtel 本周对此进行了两次测试：Claude Sonnet 5.5 [通过了她所有的 15 次编码运行](https://thenewstack.io/claude-sonnet-5-5-vs-opus-5-5/)，成本比 Opus 5.5 低 42%（后者通过了 13 次，尽管有四次 Sonnet 运行是在她提高了输出 Token 限制后才通过的）。前一天，她发现 [GPT-6.1 Sol 以 18% 的成本匹配了 GPT-6 Astra 的准确度](https://thenewstack.io/gpt-6-1-sol-vs-gpt-6-astra/)。更便宜的模型两次都经受住了考验。

目前模型更迭迅速。DeepSeek V4.1 Flash 一个月前还不存在，现在已经是 OpenRouter 的顶级模型。决策模型（从一组选项中选择答案而不是编写答案的模型）也开始出现。[TypeSafe 的 Jev](https://thenewstack.io/typesafe-jev-system-one/) 排在第 10 位，而[OpenAI 的 GPT-6 Luna Decisions](https://thenewstack.io/openai-decision-api-luna/) 是趋势列表上的新面孔。

显而易见的反对意见是，OpenRouter 的客户是选择了路由器的开发人员，因此他们会切换。这很公平。它自己的页面指出，Token 数量并不衡量用户或支出，企业合同更具粘性。

但我们采访的至少有 10 家公司以同样的方式运行他们的 AI，截至周三，埃隆·马斯克也是如此。