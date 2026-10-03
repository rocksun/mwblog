*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 发展趋势，并解释它们对于将这项技术投入实际应用的人员和组织意味着什么。核心论点很简单：学会使用 AI 的工作者将定义其行业的下一个时代，而本期通讯旨在帮助你成为其中一员。*

---

OpenAI 在周二的开发者日（DevDay）上推出了 [Dots](https://thenewstack.io/openai-dots-gpt6-agents/)。每个 Dot 都是一个全天候运行的智能体，拥有自己的云端计算机和浏览器，并接入了已经连接到 ChatGPT 的 4,000 多个应用程序。在 OpenAI 的示例中，Dot 看到 Slack 中弹出的漏洞警报后，便开始自行深入排查。很酷。

在 Dots 推出之前，Meta 推出了 Muse，其移动端安装量打破了此前由 ChatGPT 创下的纪录。而在 Muse 之前，xAI 在 8 月推出了其版本 Grok Bot。

Anthropic 的版本虽然在几个方面有所不同，但[在两周前作为 Claude 的更新推出，](https://thenewstack.io/claude-cowork-vs-chatgpt-work-benchmark/)并且没有可爱的主角名字或毛绒吉祥物。此次更新将 Cowork（自 7 月起就已上线，[能够在用户合上笔记本电脑后无需提示地运行预定任务](https://thenewstack.io/claude-cowork-cloud-mobile/)）整合进了主 Claude 应用中。

无论 Cowork 的下载量是否能赶上 Muse，Anthropic 的这一决策都是正确的。全天候运行的智能体还处于萌芽期，谈论赢家为时尚早，且技术护城河很浅。一个实验室发布的功能往往会在几周或几个月内出现在竞争对手的产品中。Meta 需要 Muse 成为轰动一时的爆款，而 Anthropic 则需要已经在用 Claude 构建应用的开发者交出真实、重复的工作任务，并持续回访。重复使用和完成任务比一场华丽的发布会更重要。

## 全天候运行的智能体还处于难以决出赢家的早期阶段

这波全天候个人智能体浪潮是在不到一年前兴起的。去年 11 月，Peter Steinberger 在 GitHub 上发布了一个名为 Clawdbot 的周末项目。它运行在一台闲置电脑上，通过 WhatsApp 或 Telegram 接受提示词，主要依赖 Claude。Anthropic [在 1 月派出了律师团队](https://laravel-news.com/clawdbot-rebrands-to-moltbot-after-trademark-request-from-anthropic)，于是[它改名为 Moltbot](https://thenewstack.io/moltbook-the-singularity-or-hype/)，几天后又变成 OpenClaw。这演变成了一个安全隐患，2 月份 Steinberger 加入了 OpenAI。周二，运营该项目的基金会[发布了 OpenClaw Enterprise 的早期 Pre-1.0 版本](https://thenewstack.io/openclaw-enterprise-kubernetes-agents/)供企业内部试用。

十个月，三个名字，一次 OpenAI 挖角和一个企业版。创意在这些产品之间流转的速度比以往任何时候都要快。Meta 的 Nat Friedman [表示 Muse 很大程度上受了 OpenClaw 的启发](https://thenextweb.com/news/meta-muse-openclaw-friedman-soul-md)，深入研究 Muse 的用户发现了一个与 OpenClaw 几乎完全相同的 SOUL.md 个性文件。

一个实验室发布的新功能，会在几个月内出现在其竞争对手的产品中。

每个 AI 助手和智能体功能的早期版本在哪里发布，以及现在由谁提供。

| 功能 | 早期发布示例 | 现在也提供于 |
| --- | --- | --- |
| 深度研究报告 | Google Gemini (2024年12月) | OpenAI, Anthropic, Perplexity |
| 终端编程智能体 | Claude Code (2025年2月) | OpenAI Codex, Gemini CLI, Meta Muse Code |
| 智能体个性文件 | OpenClaw (SOUL.md) | Meta Muse |
| 具有工作身份的智能体 | Anthropic Claude Tag (2026年6月) | OpenAI 专员 Dots (预览版) |
| 聊天与智能体工作在同一窗口 | OpenAI Work 模式 (2026年7月) | Claude (2026年9月) |

Anthropic 的 9 月合并被列在了上面“抄袭者”的行列中，比 OpenAI 的 Work 模式晚了两个月——尽管 Cowork 的云端和定时任务功能是在 7 月 7 日发布的，比 Work 模式早了两天。Jessica Wachtel [在我们的网站上针对三个开发者任务对两者进行了测试](https://thenewstack.io/claude-cowork-vs-chatgpt-work-benchmark/)，发现它们的准确率不相上下，其中 ChatGPT 速度更快，而 Claude 更彻底。当产品如此年轻时，“跟风式”发布正是实验室吸引自己的用户进场，以观察他们如何使用该产品的方式。

Muse 是一个巨大的成功。仅计算 iOS 端，[Apptopia 估计在 Muse 推出的前 12 天内，美国日活用户达到了 359,000 人](https://techcrunch.com/2026/09/21/metas-muse-is-outpacing-chatgpts-early-mobile-launch/)，而在同一时期 ChatGPT 的 iOS 应用为 231,000 人。Sensor Tower [估计](https://techcrunch.com/2026/09/25/meta-is-putting-its-muscle-behind-muse-as-the-ai-app-takes-off/)截至 9 月 24 日下载量超过 340 万次，尽管其他机构的数据有所不同。

Meta 需要这个。其 Reality Labs 部门在元宇宙上花费了数百亿美元，却没有拿出一个主流产品来证明自己。Llama 4 去年反响平平，以至于扎克伯格围绕一个新的超级智能实验室重建了他的 AI 部门，特别是收购了 Scale AI 49% 的股份并聘用了其创始人亚历山大·王（Alexandr Wang）。

Muse 是这次重组中首个取得突破的产品，它借助了 Meta 的用户基础取得了成功：Apptopia 发现超过 95% 的 Muse 用户同时也使用 Facebook。Muse 提供免费层、每月 20 美元和 100 美元的付费计划，并连接到 Shopify 和 Stripe 结算系统，使智能体能够购买商品。Meta 的路线是通过规模取胜。规模也有其缺点。Janakiram MSV 在 TNS 上解释了[为什么亚马逊在发布两周后开始阻止 Muse](https://thenewstack.io/amazon-meta-muse-block/)，这篇文章非常值得一读，因为这是电子商务领域的一个新切入点。

OpenAI 和 xAI 从付费端切入。Dots 的入场券是什么？每月 100 到 500 美元的 ChatGPT Pro 计划，或者 Business Premium 或 Enterprise 账户。萨姆·阿尔特曼（Sam Altman）将 Dots 称为高端产品，因为每个 Dots 都需要大量的算力。据 [Bloomberg 报道](https://www.bloomberg.com/news/articles/2026-09-22/spacexai-s-grok-bot-agent-tops-400-000-users-after-first-month)，Grok Bot 在 9 月中旬达到了每周 418,000 名用户，而 xAI 刚刚在周一推出了 Team Bots。

这两家公司都不需要 Meta 的用户基础来学习有价值的东西。付费客户已经在 AI 上花钱，用户留存率将证明他们在新鲜感消退后是否会继续使用该智能体。

## Anthropic 将其版本推出了给那些已经在用 Claude 构建应用的群体

Anthropic 做了我目前对各大实验室所期望的事情：快速发布，面向付费订阅用户发布，并将智能体置于这些人已经在使用的应用程序中。合并后的 Claude 触达了 Pro 和 Max 客户，Team 和 Free 计划也将很快推出。团队们[自 6 月以来就在 Slack 中使用了 Claude Tag](https://thenewstack.io/anthropic-claude-tag-slack/)，这是一个具有自身身份和审计追踪功能的积极主动的团队成员。Cat Wu 表示，内部版本约占[产品团队代码更改的 65%](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive)。自 4 月以来，开发者们就有了用于托管、长期运行智能体的托管智能体（Managed Agents）。

Anthropic 尚未做的是将 Claude 放在 Muse 所在的地方。Muse 在 Meta 旗下的 WhatsApp 内部工作，但 Claude 仍然要求你打开 Claude 应用或在 Slack 中对其进行@提及。这种工作流对主流消费者可能很重要。但将智能体接入其代码的团队更关心它能触及什么。Jani [在我们的网站上阐述了这一区别](https://thenewstack.io/persistent-ai-agent-identities/)：Grok Bots 在整个名册中共享一台云计算机和一组登录信息，而 Claude Tag 以其自身的服务身份和频道限定的访问权限加入 Slack 工作区。在将登录信息交托给智能体之前，请先了解你要面对的是什么。

这些正是 Anthropic 应该争取的幕后用户。《Towards Data Science》上的撰稿人今年一直在展示构建者如何使用全天候运行的智能体。[Samir Saci 将一组 OpenClaw 智能体](https://towardsdatascience.com/i-simulated-an-international-supply-chain-and-let-openclaw-monitor-it/)部署到供应链模拟中以追查延迟发货。Eivind Kjosbakken 的[运行 OpenClaw 机器人集群指南](https://towardsdatascience.com/how-to-orchestrate-a-fleet-of-openclaw-bots/)介绍了测试应用程序并报告错误的夜间 QA 机器人，以及检查发票的智能体。两者都在 OpenAI 的 Codex 上运行了他们的智能体。据 [*VentureBeat* 报道](https://venturebeat.com/orchestration/openclaw-launches-free-enterprise-control-plane-for-persistent-ai-agents-backed-ai-openai-red-hat-and-nvidia)，OpenAI 运行着自己的 OpenClaw 智能体 Androidclaw，用于追踪损坏的构建并在某些情况下合并修复。Anthropic 需要这种类型的工作在 Claude 上运行。

今年春天我在一台旧 Mac Mini 上设置了 OpenClaw，我遇到了很多问题（也有许多突破）。这就是为什么构建者、编码员和开发者对产品开发至关重要：他们在 GitHub 问题和 Discord 线程中大声提出这些问题，而答案最终会落实在产品中。

显而易见的反对意见是信任问题。这很公平。全天候运行的智能体掌握着凭据，并在无人看管的情况下采取行动。xAI 自己的文档告诉用户不要将 Grok Bots 视为安全边界，OpenClaw 基金会表示大多数 IT 部门直接禁止智能体平台。Anthropic 的默认设置倾向于谨慎：除非你另行告知，否则 Claude 在行动前会征求意见，并且 Tag 会保留其自己的审计追踪。如果构建者不再回来，或者每个完成的任务比自己动手需要更多的监督，那么这个实验就没有成功。但如果他们不断发现有用的工作可以委派，他们的问题和突破就会成为路线图。

这才是对 Claude、Dots 和 Muse 而言最重要的竞赛：成为人们愿意将下一个工作托付信任的智能体。