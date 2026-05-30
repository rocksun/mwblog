<!--
title: Claude Opus 4.8 正式发布：支持投入度控制与动态工作流，快速模式更便宜，且更诚实少欺骗
cover: https://cdn.thenewstack.io/media/2026/05/84f82f64-introducing-claude-opus-4.8-scaled.webp
summary: Anthropic发布了Claude Opus 4.8，新增投入度控制、动态工作流，降低了快速模式价格，并提升了诚实度与安全性，但在终端编程上略逊于GPT-5.5。
-->

Anthropic发布了Claude Opus 4.8，新增投入度控制、动态工作流，降低了快速模式价格，并提升了诚实度与安全性，但在终端编程上略逊于GPT-5.5。

> 译自：[Claude Opus 4.8 is here: effort controls, dynamic workflows, cheaper fast mode, better honesty, less deception](https://thenewstack.io/claude-opus-48-release/)
> 
> 作者：Meredith Shubel

周四，Anthropic 发布了其旗舰模型的最新版本 Opus 4.8，允许用户控制 Claude 的工作投入度、应对更大规模的编程任务，并能以更低的成本运行快速模式。Anthropic 还表示，该模型更加诚实、欺骗性更低，并且能更好地支持用户的自主性和切身利益。

基准测试显示，Opus 4.8 领先于其前代产品，以及 GPT-5.5 和 Gemini 3.1 Pro，但在智能体终端编程（agentic terminal coding）方面除外，OpenAI 的模型在该领域依然处于领先地位。

它已于周四上线，价格与 Opus 4.7 相同。

## 传言属实：Opus 4.8 作为 4.7 的升级版正式落地

5 月 28 日，X 上关于 Opus 4.8 即将发布的传言传得沸沸扬扬。一位[用户](https://x.com/hysteresis_x/status/2059997797420540338)发布传言称：“在桌面应用的 Claude Code 模型选择器中发现了已经就绪的 Opus 4.8。它应该在今天发布！”

街头巷尾的推文确实没说错，但 Opus 4.8 在 Opus 的历史中将如何被人们铭记？

### 新变化：用户可以控制 Claude 的工作投入度

一项全新的控制功能意味着用户可以调大或调小 Claude 在任务中付出的努力。Anthropic 在其发布博客中解释道，当全力以赴时，Claude 将“进行更频繁、更深入的思考，以给出更好的回答”。相反，在较低投入度下，Claude 的响应速度会更快，并且消耗用户速率限制（rate limit）的速度也会更慢。

对于那些感受到 AI“变相降级”（shrinkflation）影响、并担心比预期更快达到速率限制的用户来说，这可能是一个好消息。

### 新变化：Claude 可以承担更大规模的编程任务

现已在研究预览版中提供、被 Anthropic 称为“动态工作流”的功能，应该允许用户使用 Claude Code 解决更大规模的问题。具体来说，Anthropic 表示，用户现在可以要求 Claude “规划工作，然后在单个会话中运行数百个并行的子智能体（subagents）”。随后，它会在将输出返回给用户之前对其进行验证。

对于普通用户来说，这会是什么样子？Anthropic 举了代码库规模迁移的例子，称搭载了 Opus 4.8 的 Claude Code 可以“在数十万行代码中，从启动到合并全程搞定”。

### 新变化：快速模式更便宜

对 Claude 用户的钱包来说，还有更多好消息：Anthropic 表示，Opus 4.8 的快速模式（即模型以 2.5 倍于正常速度运行的速度）“现在的价格比以前的模型便宜了三倍”。

### 新变化：Opus 4.8 更多地支持用户，更少地欺骗用户

也就是说，该模型“在我们的亲社会特质衡量中达到了新高”，Anthropic 的对齐（Alignment）团队在发布博客中表示。具体来说，这家 AI 公司报告称，Opus 4.8 改进了对用户自主性的支持，并能更好地为用户的最大利益服务。

根据 *The New Stack* 的[报道](https://thenewstack.io/claude-opus-47-launch/)，另一个好消息是，Anthropic 表示 Opus 4.8 的欺骗率以及协助滥用的比例“大幅低于”其前代产品，显然已经赶上了 Claude Mythos Preview（这家 AI 公司曾称其为“我们训练过的对齐度最好的模型”）。

### 新变化：它更诚实了

该模型的另一个重大改进是其诚实度的提升。据 Anthropic 称，Opus 4.8 “在允许其编写的代码中存在缺陷而默不作声的可能性上，比其前代低了大约四倍”。该公司声称，早期的测试人员已经证实了这一说法，并形容 Opus 4.8 在“执行智能体任务时更加可靠，判断也更加敏锐”。

## 基准测试对比：Opus 4.8 对决其他所有模型

Anthropic 表示，Opus 4.8 在所有基准测试中都比其前代有所提升。虽然发布当天的基准测试并不总能反映真实世界中的使用情况，但这些数据确实展现出了希望。

> 虽然发布当天的基准测试并不总能反映真实世界中的使用情况，但这些数据确实展现出了希望。

最值得注意的是：Opus 4.8 在智能体编程方面达到了 69.2%，相比 Opus 4.7（64.3%）有了显著提升，更不用说 GPT-5.5（58.6%）和 Gemini 3.1 Pro（54.2%）了。其在智能体计算资源使用上的得分（83.4%）与 GPT-5.5（78.7%）和 Gemini 3.1 Pro（76.2%）相比也毫不逊色。但在智能体终端编程方面，它输给了 GPT-5.5，比 OpenAI 的模型低了 3.6%。

![](https://cdn.thenewstack.io/media/2026/05/f3b74731-image-1024x548.png)

来源：[Anthropic](https://www.anthropic.com/news/claude-opus-4-8)

## 回顾 Opus 的发展历程：从“全球最佳编程模型”到一年内的 AI 变相降级

2025 年 5 月，Anthropic 在其首届开发者大会“Code with Claude”上[发布了](https://www.anthropic.com/news/claude-4) Opus 4，并称其为“全球最佳编程模型”。当时，这家 AI 公司承诺要为编程、高级推理和 AI 智能体设定新标准。该模型在编程和长上下文推理方面带来了[重大进展](https://thenewstack.io/anthropic-launches-claude-opus-4-and-sonnet-4/)，因其处理长期任务和保持上下文的能力而脱颖而出，Anthropic 当时称其可保持“数千个步骤”的上下文。

紧接着在 2025 年 8 月，Opus 4.1 问世，该模型在智能体任务、编程和推理方面的性能有了适度提升。但这只是一个微小的更新；当时，Anthropic [预告](https://www.anthropic.com/news/claude-opus-4-1)称“在接下来的几周内，我们的模型将迎来大幅度的改进”。

2025 年 11 月，Opus 4.5 伴随着巨大的声势[发布了](https://www.anthropic.com/news/claude-opus-4-5)。Anthropic 再次吹捧它是“世界上最适合编程、智能体和计算机使用的模型”。而且，他们再次吊起了我们的胃口，指出 Opus 4.5 只是“对工作方式将发生更大改变的一次预览”。就其本身而言，该预览版带来的改进使模型能够更好地处理模糊性，并解决涉及多系统 Bug 的问题。在许多方面，Opus 4.5 让 Anthropic 在 OpenAI 的 GPT-5.1-Codex-Max 和谷歌的 Gemini 3模型赢得青睐后，得以[夺回编程皇冠](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/?utm_source=chatgpt.com)。

正如他们所暗示的那样，三个月后，Anthropic 为我们带来了 Opus 4.6。*The New Stack* [报道](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/?utm_source=chatgpt.com)称，由于它能够处理更复杂的任务并提供更好的结果，这是“在大企业工作流中使用大型语言模型（LLM）的一次阶段性飞跃”。Opus 4.6 凭借更好的规划、编程和调试能力进行了升级，成为 Anthropic 首个使用自适应思维的模型，并获得了优异的基准测试分数。特别值得注意的是其 100 万（1M）Token 的上下文窗口。Anthropic 的发言人告诉 *The New Stack*：“与我们在任何模型中看到的相比，它在第一次尝试时就更接近生产级质量——文档、电子表格和演示文稿将需要更少的来回迭代。”

但闪光的不一定都是金子。在 Opus 4.6 发布后不久，Anthropic 因价格调整而饱受批评：根据 *The New Stack* 的[报道](https://thenewstack.io/claude-million-token-pricing/?utm_source=chatgpt.com)，“虽然这些模型在技术上支持接近 100 万 Token 限制的提示词，但超过大约 20 万 Token 的请求会按照更高的‘长上下文’计费标准收费，从而将整个请求推入了高额收费档位。”

Opus 4.7 也面临一些复杂情况。在 2026 年 4 月[发布](https://www.anthropic.com/news/claude-opus-4-7)（这是对 Opus 4.6 的直接升级，带来了更好的视觉、更好的记忆和更好的指令遵循能力）之后，*The New Stack* [报道](https://thenewstack.io/claude-opus-47-flaky-performance/?utm_source=chatgpt.com)称：“Claude Opus 4.7 用户反映其回答自相矛盾且性能下降，这引发了人们对 AI 模型质量、安全性折中以及变相降级的质疑。”同样尴尬的是：Anthropic 自己也称 Opus 4.7 的能力不如当时备受关注的 [Claude Mythos Preview](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/)。正如 *The New Stack* [报道](https://thenewstack.io/claude-opus-47-launch/)的那样，Opus 4.7 似乎在某种程度上成为了 Mythos 新网络安全保护措施的试验场。

## Anthropic 接下来的秘密武器是什么？

有关 5 月 28 日发布 Opus 4.8 的传言被证明完全准确，因此互联网上的其他八卦或许也值得关注：爆料还[表明](https://www.geeky-gadgets.com/three-new-anthropic-ai-models-leaked/)，Anthropic 很快将宣布 Sonnet 4.8 和 Mythos 1。

退一步讲，对于这家最近一直让用户感到失望的 AI 公司来说，这无疑将是一个大新闻。

本月早些时候，它推出的 [Claude Code 智能体视图](https://thenewstack.io/claude-code-agent-view/)让开发者大失所望。正如 [Neurometric AI](https://www.neurometric.ai/) 的首席执行官兼联合创始人 [Rob May](https://www.linkedin.com/in/robmay/) 告诉 *The New Stack* 的那样：“它减少了一些摩擦，但并没有改变底层问题。”就在同一周，Anthropic 还宣布将从 6 月 15 日起对 [Agent SDK 使用进行拆分计费](https://thenewstack.io/anthropic-agent-sdk-credits/)，这对于已经习惯了从同一个订阅限制中扣除编程使用额和交互使用额的用户来说，显然不是什么受欢迎的消息。

也许 Mythos 1 和 Sonnet 4.8 会带来更多胜利。