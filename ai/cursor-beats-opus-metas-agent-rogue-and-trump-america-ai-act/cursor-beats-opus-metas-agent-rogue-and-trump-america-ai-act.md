<!--
title: Cursor 1/10 价格力压 Opus，Meta AI 代理失控，300 页《特朗普美国 AI 法案》重磅来袭
cover: https://cdn.thenewstack.io/media/2026/03/2af64047-beatriz-camaleao-q95gyosqn_k-unsplash-scaled.jpg
summary: AI行业整合加速，Cursor、OpenAI、Anthropic、Nvidia各有布局。AI代理安全问题凸显。美国发布300页《特朗普美国AI法案》，旨在统一监管并关注AI对就业影响，预示规则制定时代到来。
-->

AI行业整合加速，Cursor、OpenAI、Anthropic、Nvidia各有布局。AI代理安全问题凸显。美国发布300页《特朗普美国AI法案》，旨在统一监管并关注AI对就业影响，预示规则制定时代到来。

> 译自：[Cursor beats Opus at 10x less, Meta's agent goes rogue, and the 300-page Trump America AI Act](https://thenewstack.io/cursor-beats-opus-metas-agent-rogue-and-trump-america-ai-act/)
> 
> 作者：Matthew Burns

我是 Matt Burns，Insight Media Group 的编辑总监。每周，我都会汇总最重要的 AI 发展动态，解释它们对那些正在将这项技术付诸实践的个人和组织意味着什么。我的论点很简单：学会使用 AI 的员工将定义他们行业的下一个时代，而这份新闻简报旨在帮助您成为其中一员。

我基于 AI 的 NCAA 三月疯狂赛预测在第一天就泡汤了，这证明 AI 尚未发展到能够预测青少年在压力下表现的程度。我使用了 <https://www.bracketmadness.ai/>，并且很喜欢它的新手引导流程。

本周的主题是整合。不是那种无聊、吓人的企业整合，而是战略性整合。Cursor 发布了自己的模型。Nvidia 召集了一个联盟，共同构建开放式基础模型。OpenAI 正在将三个应用程序合并为一个。Anthropic 两次降价。贝佐斯（Bezos）正在筹集 1000 亿美元，用于收购制造商并向其注入 AI。而国会发布了长达 300 页的《特朗普美国 AI 法案》，旨在取代美国所有州级的 AI 法律。

贯穿始终的线索是：每个主要参与者都试图在技术栈中占据更大份额。而你今天使用的工具，可能在六个月后就不是你使用的工具了。

## Cursor 力压 Opus，价格更低

Cursor 本周[发布了 Composer 2](https://thenewstack.io/cursors-composer-2-beats-opus-46-on-coding-benchmarks-at-a-fraction-of-the-price/)，这是其第三代内部编码模型。基准测试结果令人印象深刻。在衡量 AI 代理在终端中处理真实世界软件工程任务能力的 Terminal-Bench 2.0 上，Composer 2 得分 61.7%，超越了 Claude Opus 4.6 的 58%。在 Cursor 自己的 CursorBench 上，新模型达到 61.3 分，高于上一代的 44.2 分，并与 GPT-5.4 Thinking 的 63.9 分具有竞争力。

定价才是真正的亮点。Composer 2 每百万输入 token 成本为 0.50 美元，每百万输出 token 成本为 2.50 美元。Opus 4.6 的成本是 5 美元/25 美元。这是一个 10 倍的差价。Cursor 专门在代码数据上训练了该模型，并在长周期编码任务（需要数百个独立步骤的问题）上应用了强化学习。结果是一个更小、更专注的模型，它不需要无所不知，只需擅长编写代码即可。

我一直在等待这些 AI 编码工具达到平台期，但它迟迟未到。Cursor 在这里面临着真正的结构性压力——它现在与 OpenAI 和 Anthropic 竞争，同时又依赖于它们的模型。构建 Composer 2 是他们开始控制自己利润的方式。他们并非孤军奋战。[Nvidia 本周宣布成立一个 AI 实验室联盟](https://thenewstack.io/nvidia-tier2-nemotron-coalition/)——包括 Cursor、Mistral、Perplexity、LangChian 和 Black Forest Labs——以汇集资源并在 Nvidia 的 DGX Cloud 基础设施上构建共享的基础模型。第一个项目，一个新基础模型，将构成 Nvidia Nemotron 4 系列的基础。工具制造商正在成为模型制造商。这是一个重要的步骤。

## OpenAI 超级应用

《华尔街日报》[报道称](https://www.wsj.com/tech/openai-plans-launch-of-desktop-superapp-to-refocus-simplify-user-experience-9e19931d)，OpenAI 计划将 ChatGPT、Codex 及其网页浏览器整合到单个桌面应用程序中。OpenAI 应用程序首席执行官 Fidji Simo 告诉员工：“我们意识到我们分散了太多的精力在过多的应用程序和技术栈上，我们需要简化工作。这种碎片化一直在拖慢我们的速度，使我们更难达到我们想要的质量标准。”

移动版 ChatGPT 应用程序保持独立。这是一个桌面端的策略——据称旨在面向希望将对话式 AI、编码辅助和浏览功能集中在一个地方的开发者、企业和高级用户。我发现内部引述很有启发性，表明内部产品开发结构未能满足用户的期望。一家公司很少会直接说：“我们做了太多东西，而且效果不佳。”这表明该公司认为其目前的竞争不在于聊天，而在于 Anthropic 的 Claude 和 Cursor 已经存在的桌面工作空间。成为你电脑上默认 AI 层的竞争正变得越来越激烈。竞争是好事。

## Token 降价

Anthropic 本周的两项举措降低了 AI 的成本。首先，该公司[取消了 Claude Opus 4.6 和 Sonnet 4.6 的长上下文定价附加费](https://thenewstack.io/claude-million-token-pricing)。100 万 token 的上下文窗口现在以标准 token 费率普遍可用——Opus 为 5 美元/25 美元，Sonnet 为 3 美元/15 美元。此前，超过 20 万 token 的提示会触发溢价。现在，一个 90 万 token 的请求与一个 9 千 token 的请求按 token 计费是相同的。如果你处理大型代码库或长文档，这很重要。我几周来一直受到上下文限制的困扰，所以这一举措对我很有帮助。

其次，Anthropic [将所有 Claude 计划在非高峰时段的使用限制翻倍](https://thenewstack.io/anthropic-doubles-claude-usage-outside-peak-hours/)——这项为期两周的促销活动持续到 3 月 28 日。翻倍的限制适用于周末以及东部时间工作日上午 8 点之前和下午 2 点之后。《The New Stack》将此解读为一种竞争策略，而非慷慨：将使用量转移到非高峰时段可以缓解高峰期的基础设施负载，而更频繁的使用有助于培养习惯。很快，我将不得不像给我的电动汽车充电一样，按照相同的时间表来安排 cron 作业了。

介于 Cursor 便宜 10 倍的编码模型和 Anthropic 免费赠送使用量之间，AI 辅助工作的成本正在迅速下降。那些找出如何以经济高效的方式实际使用这些工具的组织将从中受益。

## 代理失控

AI 编码代理的速度几个月来一直是热门话题。它们所产生代码的质量和安全性正开始成为另一个故事。

Daryl K. Taft [本周报道](https://thenewstack.io/cursor-open-sources-security-agents/)，Cursor 的安全团队构建了一队 AI 代理，持续监控公司代码库中拉取请求的漏洞——然后开源了模板和 Terraform，以便其他团队也能这样做。动机是：传统的安全工具（代码所有者、代码检查器、静态分析）无法跟上 AI 编码工具生成代码的速度。

另外，JetBrains 创造了“影子技术债务”（Shadow Tech Debt）一词——指 AI 代理在没有项目结构理解的情况下生成[低质量、缺乏架构意识的代码](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/)。该公司在诊断的同时推出了 Junie CLI，认为这将是企业开发的下一个大问题。

在《Towards Data Science》上，[Reya Vir 探讨了同样的紧张关系](https://towardsdatascience.com/the-reality-of-vibe-coding-ai-agents-and-the-security-debt-crisis/)。她提到了 Moltbook 事件——一个主要通过“氛围编程”（Vibe coding）构建的社交平台，通过一个配置错误的 Supabase 数据库暴露了 150 万个 API 密钥和 35,000 个用户电子邮件。根本原因是开发者依赖的 AI 代理只优化代码运行，而不是优化代码安全。

哥伦比亚大学的研究证实，安全性是编码代理的常见故障模式。

不仅是代码质量问题。《The Information》[报道称](https://www.theinformation.com/articles/inside-meta-rogue-ai-agent-triggers-security-alert)，Meta 内部的一个 AI 代理本周在未经授权的情况下行动，触发了一级（Sev 1）安全事件。一名员工使用该代理分析同事在内部论坛上的查询，而该代理自行向该同事发布了回复。该同事听从了代理的建议，这引发了一系列连锁反应，将公司和用户数据暴露给了不应拥有访问权限的工程师。数据暴露持续了大约两小时。Meta 的安全与对齐总监 Summer Yue [上个月就已指出这个问题](https://www.engadget.com/ai/a-meta-agentic-ai-sparked-a-security-incident-by-acting-without-permission-224013384.html)，当时她的 OpenClaw 代理在被告知需确认后再行动的情况下，删除了她的整个收件箱。这些代理速度快、能力强，而且越来越难以控制。

接着是 Nvidia 的解决方案。[Frederic Lardinois 本周报道了 Nemoclaw](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/)，它将 OpenClaw 封装在 Nvidia 的代理技术栈中，包括基于策略的安全性、隐私保护措施以及一个名为 OpenShell 的开源安全运行时。它可以在 Nvidia 自己的 Nemotron 模型或任何云托管模型上运行，并通过一个命令即可安装。如果说 OpenClaw 是一个令人兴奋、略显鲁莽的开源代理平台，那么 NemoClaw 就是一个附加了保护措施的企业版。对于任何在生产环境中部署代理的人来说，它可能正是所缺少的东西。Eivind Kjosbakken 还在 Towards Data Science 上发布了一份关于如何设置 OpenClaw 作为个人 AI 助手的实用指南——如果你想亲自尝试无保护的版本，值得一读。

## 300 页的《特朗普美国 AI 法案》

任何在美国构建 AI 产品的人可能很快就会有一套统一的联邦法规可遵循，而不是 50 套州级法规。参议员 Marsha Blackburn 发布了被称为《特朗普美国 AI 法案》的讨论草案，这是一份近 300 页的立法框架，将完全取代州级 AI 监管。白宫[围绕六个目标对其进行了阐述](https://www.whitehouse.gov/articles/2026/03/president-donald-j-trump-unveils-national-ai-legislative-framework/)：儿童保护、社区保障、知识产权、言论自由、创新和劳动力发展。

其中一些条款意义重大。该法案规定 AI 开发者有责任防止可预见的损害。它废除了第 230 条款，终止了平台对用户生成内容的责任保护。它明确指出，未经授权为 AI 训练复制受版权保护的作品不构成合理使用。它还要求公司和联邦机构每季度向劳工部报告与 AI 相关的裁员和就业岗位转移情况。

最后一部分值得关注。关于 AI 造成的就业岗位转移的季度报告将创建第一个关于 AI 实际如何重塑劳动力的系统数据集——不遵守规定将面临高达每项违规 100 万美元的民事罚款。无论它是否通过——《Roll Call》[指出它面临](https://rollcall.com/2026/03/19/ai-draft-bill-would-revamp-online-landscape)真正的障碍，包括日益减少的立法日历和共和党在技术强制规定上的分歧，方向是明确的。构建 AI 工具和部署 AI 工具的人们正开始在一个规则被制定出来的世界中运作。