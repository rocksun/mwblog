*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 进展，并解释它们对那些将这项技术投入使用的人员和组织意味着什么。核心论点很简单：学习使用 AI 的员工将定义他们行业的下一个时代，而本通讯旨在帮助您成为其中一员。*

---

***周五晚上更新**：[Anthropic 已禁止所有人访问 Fable 5 和 Mythos 5](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)，以遵守美国政府的出口管制指令。这发生在我写完专栏后、周六早上发布前的几个小时内。政府称其获悉了一种破解 Fable 的方法；Anthropic 审查了该技术，称其为轻微漏洞，并指出包括 OpenAI 的 GPT-5.5 在内的其他公开模型在没有绕过手段的情况下也会出现同样的问题。Anthropic 称该指令是一个误解，并表示正努力恢复访问。当您在周六早上读到这篇文章时，Fable 可能已经恢复，也可能没有。无论如何，原文的重点因这则新闻而变得更加尖锐：您所依赖的模型可能会在一夜之间消失，而知道接下来该使用哪个模型才是整场博弈的关键。*

Anthropic 周二发布了 Claude Fable 5，我所见过的最有用的反应是路由图，而不是基准测试。

Fable 的能力及其价格加在一起，使得模型选择成为了区分高效 AI 用户与“昂贵”用户的技能。那些能从现有最佳模型中获得最大价值的人，是那些有纪律地不去默认使用它的人。他们使用 Fable 进行规划、编排和审查，然后将实际工作交给成本仅为其十分之一的模型。

随着 Fable 在 6 月 23 日退出订阅计划，且其下方正在形成价格战，这项技能将对每个人（不仅仅是开发者）都变得重要。

## 最聪明的 Fable 用户只“兼职”使用 Fable

本周，我的书签中排在最前面的是这两条推文。Dan McAteer [分享了一个工作流](https://x.com/daniel_mac8/status/2065066247448821841)，用于在 Claude Code 中使用 Fable，而不会立即达到计划限制：将 Fable 设置为编排器，让 Opus 处理繁重的推理短语。他的解释一语道破：“Fable 太过强大，你不需要在每一步都动用它的智能。” CJ Zafir [更进一步](https://x.com/cjzafir/status/2065104422762684745)，称他通过使用 Fable 进行规划、OpenAI 的 Codex 5.5 进行执行、再次使用 Fable 进行审查，将每周的 Claude Code 额度消耗减半。

Mitchell Hashimoto 用数据解释了原因。经过数天的对比测试，[他报告说](https://x.com/mitchellh/status/2064773611647574429)，对于普通的“实现此功能”工作，Fable、GPT-5.5 和 Zhipus 的经济型 GLM-5.1 产生的效果同样令人满意——但 GLM 成本不到一美元且在几分钟内完成，GPT-5.5 耗费约 1.50 美元，而 Fable 搅动了 40 分钟并花费了 9 美元。然后，他给了 Fable 一个其他模型无法触及的问题：优化他用 Go 编写的 SwiftUI 布局解析器。两小时后，耗资 40 美元，它达到了他自认为无法达到的性能水平。他的结论是：将 Fable 保留用于“有针对性的、外科手术式的分析和工作”，而不是日常驾驶。

（我要说这没意思。只要 Fable 还在订阅服务中，我就要尽可能多地使用它。）

看看 [Morgan Linton 的推文](https://x.com/morganlinton/status/2064874883298013467)关于此基准测试的看法：“Fable 低配版比 Opus 和 GPT 高配版更好。试试看。” 不要将其视为模型评论。这是一种路由指令。

以下是 Hashimoto 的发现。

![](https://cdn.thenewstack.io/media/2026/06/7af563e1-model_triage_hashimoto_share_graphic_rounded-1024x576.png)

## 经济因素使分流成为常态，而非发布时的巧合

Fable 的 API 定价为每百万输入 Token 10 美元，每百万输出 Token 50 美元——正好是 Opus 4.8 的两倍。在订阅计划中，它在您的限额内大约相当于 Opus 使用量的两倍。而且它仅在 6 月 22 日之前包含在 Pro、Max、Team 和 Enterprise 计划中。从 6 月 23 日开始，Fable 需要按完整 API 费率计费的积分。Anthropic 表示这与能力有关，并打算在可能时将 Fable 恢复到订阅中。也许吧。但订阅窗口看起来不像是一种发布福利，而更像是 Anthropic 暂时无法将其作为默认模型的两周补贴。Frederic Lardinois 在 *The New Stack* 上报道了这次发布及其异常短暂的窗口期——[他的文章](https://thenewstack.io/anthropic-claude-mythos-fable-5/)很好地总结了 Fable 是什么以及其中的陷阱。

这就是 Citadel Securities 预见到的部分。其新的 [Tokenomics 报告](https://www.citadelsecurities.com/news-and-insights/global-macro-strategy/tokenomics/)认为，对代理型 AI 的期望建立在“对无摩擦部署成本的不切实际预期”之上，并指出了一种已经开始的分歧：前沿推理正集中在能够证明其支出合理性的组织中，而其他人则转向更便宜的模型。

Silicon Data 的 LLM 支出指数最近的下降可能反映了这种转变。Silicon Data 指出，当模型价格下跌、用户选择更高效的模型，或市场从昂贵的集中化中撤出时，该指数可能会下降。[一项新的 arXiv 研究](https://arxiv.org/abs/2604.22750)在任务层面也提出了同样的观点：代理型编码消耗的 Token 可能是普通代码聊天的 1,000 倍，相同的运行结果可能会有 30 倍的差异，而更多的 Token 并不能可靠地带来更高的准确性。这就是模型分流在数据中的体现，无论是微观还是宏观层面。

顺便提一下：我不相信 Token 的定价与其创造的价值相符。Hashimoto 耗资 40 美元的优化运行在工程时间上本应花费数倍于此；从这个角度衡量，Fable 是被低估了，而不是被高估了。我没有数据来定论，但我注意到市场目前正在争论相反的观点。但如果前沿 Token 在两个方向上都被错误定价——对于日常工作太贵，对于手术级工作太便宜——那么选择就变得更有价值，而不是更少。

## 价格战使路由变得艰难，而非可有可无

周三，《华尔街日报》报道称，[OpenAI 正在考虑大幅削减 Token 价格](https://www.wsj.com/tech/ai/openai-considers-drastic-price-cuts-anticipating-war-for-users-with-anthropic-9b8c178e)——只是讨论，尚未决策——以预见与 Anthropic 在用户争夺战中的对抗，因为两家公司都在迈向 IPO。Sam Altman 本月告诉企业受众，Token 成本已成为一个“巨大的问题”，公司在第一季度烧掉年度 AI 预算几乎成了一个梗；Uber 的 CTO 说确实发生了这种情况。Chris J. Preimesberger 在我们的网站上写到了这种支出焦虑已经带来的[清理业务](https://thenewstack.io/revenium-ai-cost-observability/)。

更便宜的 Token 听起来像是救济，但它们并没有消除选择问题；它们使问题成倍增加。每一次降价都会改变现在唯一重要问题的答案：哪个模型应该运行这个？而这些决策的数量正在激增，因为工作正在循环中进行。Janakiram MSV 本周在我们的网站上发表了我读过的关于这种转变的最好的文章：“[循环工程](https://thenewstack.io/loop-engineering/)”，这是一种设计自动化代理工作流而不是直接提示的实践。Anthropic 负责 Claude Code 的 Boris Cherny 是这样说的：“我不再提示 Claude 了。我编写循环，循环来完成工作。” 阅读 Janakiram 的文章，注意循环内部有多少决策是模型选择——哪个模型编排，哪个执行，哪个认证。McAteer 和 Zafir 的工作流就是带有成本函数的循环工程。

Matt Shumer [提供了监督层](https://x.com/mattshumer_/status/2065102622604787857)：进行为期数天的 Fable 运行，并将带时间戳的更新附加到持久的 HTML 页面上，以便您可以跟踪进度。我本周在一个个人项目上尝试了一个版本。它有效，并改变了对过程的感觉。工作已悄然从编写提示词转变为监督一个小团队，其中每个模型成本不同，必须有人决定谁来完成工作。