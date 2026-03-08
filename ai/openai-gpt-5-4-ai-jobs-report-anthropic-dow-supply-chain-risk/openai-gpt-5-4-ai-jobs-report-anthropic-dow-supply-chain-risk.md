<!--
title: GPT-5.4发布，AI就业报告出炉，Claude借“禁令”逆势崛起
cover: https://cdn.thenewstack.io/media/2026/03/5ddfa47f-screenshot-2026-03-06-at-9.59.12-am.png
summary: OpenAI推出GPT-5.4新模型，AI正在重塑工作模式，代理工具与编排层兴起。Anthropic因其对美国国防部的立场而声名鹊起，OpenAI则面临负面影响。
-->

OpenAI推出GPT-5.4新模型，AI正在重塑工作模式，代理工具与编排层兴起。Anthropic因其对美国国防部的立场而声名鹊起，OpenAI则面临负面影响。

> 译自：[OpenAI GPT-5.4 launches, AI gets its own jobs report, Claude surges after U.S. ban](https://thenewstack.io/openai-gpt-5-4-ai-jobs-report-anthropic-dow-supply-chain-risk/)
> 
> 作者：Matthew Burns

*我是 Matt Burns，Insight Media Group 的编辑总监。每周，我都会汇总最重要的 AI 发展动态。不只是新闻头条，还有它们对正在应用这项技术的人们和组织意味着什么。我的论点很简单：学会使用 AI 的工作者将定义他们行业的下一个时代，本通讯旨在帮助您成为其中一员。*

---

## **OpenAI 推出 GPT-5.4，Codex 用户达 160 万**

OpenAI 本周非常忙碌。周四，[它推出了 GPT-5.4](https://thenewstack.io/openai-launches-gpt-5-4/)，这是其前沿模型的下一版本。该公司称该模型是其“用于专业工作能力最强、效率最高的前沿模型”。它结合了 GPT-5.3-Codex 的编码能力，并改进了对电子表格、文档和演示文稿的支持。基准测试分数令人印象深刻，错误更少，虚假陈述更少，在 GDPval 测试中得分 83%，该测试通过 44 种职业的真实世界任务来评估模型。这意味着它在 83% 的比较中达到或超过了行业专业人士。Anthropic 的 Opus 4.6 在同一测试中得分 79.5%。

但 GPT-5.4 是 OpenAI 迄今为止每 token 成本最高的模型；该公司表示，它在每项任务中消耗的 token 少于其他模型。

本周早些时候，OpenAI [终于在 Windows 上推出了 Codex](https://thenewstack.io/openais-codex-is-now-on-windows/)。该应用程序专为 Windows 开发环境构建，支持 Windows 开发人员已经熟悉的本地沙盒和工作流。*The New Stack* 本周报道称，OpenAI 的 Codex 现在每周活跃用户达 160 万。

[@systemticls 发布了一篇好文](https://x.com/systematicls/status/2028814227004395561?s=20) 阐述“代理工程”在实践中究竟是什么样子，读起来更像一本软件架构手册，而非提示指南。任务分解、反馈循环、护栏和每一步的模型选择。那些从 Codex（和 Claude Code）中获得最多收益的人，并非在编写更好的提示词。他们正在设计更好的系统。

## **AI 正在以意想不到的方式重塑工作**

Anthropic 本周[发布了一项新研究](https://www.anthropic.com/research/labor-market-impacts)，引入了一项名为“可观测暴露度”的衡量标准。它将理论上的 LLM 能力与现实世界的使用数据相结合。研究发现？AI 远未达到其理论能力。实际任务覆盖率仍远低于可行范围。计算机程序员是暴露程度最高的职业，但在整个经济体中，研究报告称自 2022 年以来，其他高度暴露的工人的失业率没有系统性增加。该研究指出了一个警告信号：有证据表明，暴露职业中 22 至 25 岁工人的招聘速度有所放缓。这表明工作并未消失，但谁能获得这些工作可能正在改变。

[*Towards Data Science*](https://towardsdatascience.com/human-work-in-the-ai-world-how-to-remain-valuable/) 上的一篇新文章更详细地阐述了这一转变。Favio Vazquez 认为，递归技术不等于递归采用。AI 模型以软件速度改进，但现实世界受限于基础设施、法规和组织变革。Vazquez 认为工作并未消失。它们正在围绕系统设计、战略和判断进行重组。

[Kevin Rose 说得对](https://x.com/kevinrose/status/2029376563318305202?s=20)：如果代理可以编写代码，那么价值就会转向知道要构建什么。这才是现在的工作。

## **CLI 正在为代理重建**

Google 静悄悄地发布了 [gws](https://github.com/googleworkspace/cli)，这是一个适用于所有 Google Workspace 的统一 CLI：Gmail、Drive、Calendar、Docs、Sheets，应有尽有。它拥有 40 多种代理技能和 MCP 支持。但有趣的是它的设计：它是从 Google 的 Discovery Service 自动生成的，因此它总是与当前的 API 表面保持一致。每个命令都返回结构化的 JSON。每个模式都是可内省的。这不是一个供人类偶然自动化事务的工具。它是一个为代理设计的工具。

gws 的幕后推手 Justin Poehnelt [撰写了一篇文章](https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/)，完美地描述了这一转变：“代理 DX”与“人类 DX”。他认为，我们所了解的关于良好 CLI 设计的一切——可发现性、渐进式披露、有用的错误消息——对于代理来说都是错误的。代理需要可预测性、结构化输出、明确的故障和零交互式提示。他提出了七项原则，值得一读。Anthropic 的 Dickson Tsai 本周也[宣布了](https://x.com/dickson_tsai/status/2029235808235078095) Claude Code HTTP hooks。这再次表明，开发工具正在将代理视为第一级消费者而非事后补充来设计。

这里的模式对于任何构建内部工具的人都很重要。如果你的 CLI 仍然为人类输出漂亮的表格，那它就已经落后了。

## **代理编排正成为关键层**

单个代理可以完成工作。但总得有人来管理。本周发布了两个开源项目，正是为此而生。

[OpenAI 发布了 Symphony](https://github.com/openai/symphony)，它监控工作队列——从 Linear 看板开始——拾取任务，在隔离环境中生成代理来执行任务，运行测试并提交拉取请求。它是一个永不休眠的项目经理。其架构是模块化的：可以替换不同的 LLM 提供商、不同的项目管理工具、不同的 CI 流水线。[Paperclip](https://github.com/paperclipai/paperclip) 更进一步。它是一个用于管理整个代理组织的框架，包括组织结构图、预算、支出限额和治理规则。每个代理都有一个角色和一套工具。系统在整个操作过程中跟踪 token 成本。

两者都尚处于早期阶段。两者都有明显的不足。但它们正在展示未来更好的代理管理编排层的方向。这是一个值得关注的重要层面。那些能弄清楚如何构建代理团队、定义边界和维持质量控制的公司将迅速取得领先。

## **OpenAI 正在进行损害控制。Anthropic 正在打破记录。**

上周，[五角大楼将 Anthropic 踢出](https://thenewstack.io/perplexity-computer-vibe-coding-openai-anthropic-pentagon/)，并在数小时后与 OpenAI 签约。本周，OpenAI 首席执行官 Sam Altman 正在处理公共关系风波，而 Anthropic 则收到了正式的供应链风险文件。

周四，Anthropic 首席执行官 Dario Amodei 证实，美国国防部将 Anthropic 列为国家安全供应链风险。该公司表示，该指定范围狭窄——仅适用于 Claude 在国防部合同直接部分中的使用，而非所有承包商对 Claude 的使用。Amodei 表示，公司将在法庭上对该指定提出异议。他还就一份泄露的内部备忘录表示歉意，称其中的措辞生硬并未真正反映他的观点。他在发布的声明中语气和解，表示 Anthropic 将在过渡期间继续以象征性成本向国防部和国家安全界提供模型。他强调，Anthropic “与美国国防部的共同点远多于分歧”。

更广泛的余波对 OpenAI 造成了更大打击。在新宣布 OpenAI 与五角大楼的新协议之前，已有 300 多名 Google 员工和 60 名 OpenAI 员工[签署了一封公开信](https://techcrunch.com/2026/02/27/employees-at-google-and-openai-support-anthropics-pentagon-stand-in-open-letter/)，支持 Anthropic 的立场。协议公布后，OpenAI 旧金山办公室外出现了粉笔字信息：“你的红线在哪里？” [Altman 承认](https://www.cnbc.com/2026/03/03/openai-sam-altman-pentagon-deal-amended-surveillance-limits.html)该协议“看起来机会主义且草率”，并于 3 月 4 日告诉员工，他“为让他们遭受如此反弹感到非常抱歉”。几天之内，[OpenAI 修改了合同](https://www.nbcnews.com/tech/tech-news/openai-alters-deal-pentagon-critics-sound-alarm-surveillance-rcna261357)，增加了原始合同中没有的明确监控保护措施。

损害已经造成。大约 [250 万用户注册](https://quitgpt.org/)了“QuitGPT 运动”。很快，[Claude 跳升至第一名](https://techcrunch.com/2026/03/01/anthropics-claude-rises-to-no-2-in-the-app-store-following-pentagon-dispute/)，登上了 Apple App Store。据报道，本周每天的注册人数都打破了记录。自 1 月份以来，免费用户增长了 60% 以上。付费订阅者今年翻了一番。

收入数据也说明了同样的情况。[*Bloomberg* 报道](https://www.bloomberg.com/news/articles/2026-03-03/anthropic-nears-20-billion-revenue-run-rate-amid-pentagon-feud)称，Anthropic 的年化运行率达到 190 亿美元——高于 2025 年底的 90 亿美元。甚至在 Anthropic 失去政府合同之前，Claude Code 在九个月内的年化账单就从 0 美元增长到 25 亿美元。

Anthropic 将被美国政府列入黑名单变成了一场轰动一时的营销活动。