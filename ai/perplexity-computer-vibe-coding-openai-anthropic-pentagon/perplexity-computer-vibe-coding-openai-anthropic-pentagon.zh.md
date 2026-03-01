我是 Matt Burns，Insight Media Group 的编辑总监。每周，我都会汇总最重要的 AI 发展。不仅是头条新闻，还有它们对那些将这项技术投入工作的人和组织意味着什么。核心论点很简单：学会使用 AI 的员工将定义他们行业的下一个时代，而这份通讯旨在帮助你成为其中之一。

---

**小炫耀一下**：[Roadmap](https://roadmap.sh/dashboard) 本周达到了一个重要的里程碑。它现在是 [GitHub 上星标排名第六的项目](https://github.com/kamranahmedse/developer-roadmap?tab=readme-ov-file)，其创始人 Kamran Ahmed 现已成为 GitHub 上星标排名第二的用户。我拥有出色的同事。

## **多智能体桌面走进大众**

工作人员需要开始适应智能体。它们正在超越软件内部功能，成为界面本身。

本周，AI 智能体不再仅仅是开发者的工具，而是开始为非技术用户服务。[Perplexity 推出了 Computer](https://www.perplexity.ai/products/computer)——它不是聊天机器人，也不是更智能的研究引擎，而是该公司所称的“通用数字工作者”。你只需描述结果，Computer 就会在后台自动部署子智能体进行浏览、研究、创建并连接你的工具。它连接到 Gmail、Slack、Notion、日历以及数百种其他应用程序，可以运行数小时甚至数月（[根据发布说明](https://www.perplexity.ai/hub/blog/introducing-perplexity-computer#:~:text=Perplexity%20Computer%20is%20a%20system%20that%20creates%20and%20executes%20entire%20workflows%2C%20capable%20of%20running%20for%20hours%20or%20even%20months.%C2%A0)）。其标语清晰地阐明了价值主张：“聊天回答。智能体执行任务。Computer 工作。” 产品页面上 [有数十个示例](https://www.perplexity.ai/computer/live/) 可供查看其工作原理。

Perplexity Computer 类似于 OpenClaw，但适用于普通用户。OpenClaw 在本地机器上运行，需要大量设置。Computer 在浏览器中运行，即插即用。

与此同时，Anthropic 扩展了 [Claude Cowork，增加了 13 个新的企业插件](https://thenewstack.io/anthropic-accelerates-its-cowork-enterprise-play/)，涵盖 Google Workspace、DocuSign、FactSet、LegalZoom 等。该公司还发布了 [Claude Code 的远程控制功能](https://code.claude.com/docs/en/remote-control)，最终实现了桌面应用程序的移动访问，以及一个 [调度工具](https://x.com/claudeai/status/2026720870631354429?s=20)，使 Claude 更接近 OpenClaw。Notion 发布了自定义智能体，这些智能体可以在工作区中按计划运行工作流或响应特定请求。为了支持此产品，Notion 在 GitHub 上悄悄发布了一个用于构建自定义工具调用的早期 Alpha 版工具包。Notion 的 Eric Goldman [将其宣布](https://x.com/goldmanem/status/2026392066222354785) 为自定义智能体的可编程合作伙伴：“为您的智能体构建它们在整个业务中完成工作所需的精确工具。”

## **智能体标准竞争白热化**

The New Stack 一直密切关注 [智能体框架之战](https://thenewstack.io/agent-framework-container-wars/)，其与容器之战的相似之处不容忽视——不同的角色，更高的 stakes，几乎相同的 plot。本周，Anthropic 通过 [在 GitHub 上发布其 Skills 存储库](https://github.com/anthropics/skills) 进一步推动了这一进展，使所有智能体技能的完整集合对任何人开放。这包括教导 AI 智能体可重复工作流的指令、脚本和资源文件夹。该存储库已经拥有超过 76,000 个星标。正如 TNS 在其深度报道中所述，智能体技能是 [Anthropic 定义 AI 标准的下一个尝试](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/)，遵循了将 MCP 变为智能体使用工具事实协议的相同策略。

这一举动很重要，因为其采用范围已经远远超出了 Anthropic。Microsoft 在 VS Code 和 GitHub 中采用了智能体技能。Cursor、Goose、Amp 和 OpenCode 也都采用了。OpenAI 在 ChatGPT 和 Codex 中悄然采用了结构相同的架构。该规范目前处于 v0.9 版本，由新成立的 Agentic AI Foundation（一个由 Linux 基金会支持的联盟）管理。无论你是构建智能体还是仅仅使用它们，这都是一个值得关注的底层结构。

## **氛围编程已是过去时，智能体工程才是现在。**

一年前的这个月，Andrej Karpathy 创造了“氛围编程”一词。而 [他现在称其已过时](https://thenewstack.io/vibe-coding-agentic-engineering/)。他的替代术语更合我意：“[智能体工程](https://thenewstack.io/vibe-coding-is-passe/)”。他在 [X 上的帖子](https://x.com/karpathy/status/2026731645169185220?s=20) 疯传（300 万次浏览并持续增长），Karpathy 描述了通过给智能体一个简单的英文提示来设置家庭视频分析仪表板——“登录我的 DGX Spark，设置 vLLM，下载并基准测试 Qwen3-VL，构建一个 Web UI，测试所有内容，配置 systemd 服务，并给我写一份报告。他说智能体运行了 30 分钟，遇到了多个问题，在线研究解决方案，调试，并最终完成了产品。”

他的工作流程正是我现在的工作方式，过去几周，我看到了无数其他人也这样做，与过去模型上的类似尝试相比，产生了显著改善的结果。

Karpathy 更广泛的说法呼应了 [Matt Shumer](https://x.com/mattshumer_/status/2021256989876109403) 的观点：2025 年 12 月之前，编码智能体不起作用，但现在可以了。这些模型跨越了连贯性和韧性的门槛，使得旧的工作流程——在编辑器中输入代码——感觉像是一个遗迹。产品策略师 Aakash Gupta [在一个相关的 Karpathy 讨论串中](https://x.com/aakashgupta/status/2026367615602667784) 指出，软件的新分发渠道是智能体。“智能体不会浏览你的营销网站或观看你的演示视频。它们会调用你的 CLI，访问你的 MCP 服务器，并以编程方式读取你的文档。如果这些界面都不存在，你的产品对它们来说就是隐形的……MCP 在十二个月内从零增长到每月 9700 万次 SDK 下载。”

Benjamin Lee [在 TDS 上发表了一篇文章](https://towardsdatascience.com/the-missing-curriculum-essential-concepts-for-data-scientists-in-the-age-of-ai-coding-agents/)，阐述了 AI 编码智能体时代数据科学家缺失的课程。他认为，当智能体编写代码时，代码异味（code smells）、架构直觉和系统思维比以往任何时候都重要，但你仍需承担后果。这是一篇很棒的实用读物，如果你正在应对这一转变，值得一读。在智能体工程时代蓬勃发展的人将不会是打字最快的人。他们将是那些知道好代码是什么样子并能引导智能体实现它的人。

## **Cloudflare 为智能体友好型网站构建底层设施**

本月早些时候，[Cloudflare 推出了 Markdown for Agents](https://thenewstack.io/cloudflares-markdown-for-agents-automatically-make-websites-more-aifriendly/)。这个概念很简单：当 AI 智能体请求网页时，Cloudflare 的边缘会将 HTML 转换为干净的 Markdown，然后再返回。token 节省效果显著。当在 Cloudflare 自己的博客文章上使用时，它显示 token 数量从 HTML 的 16,180 减少到 Markdown 的 3,150，减少了 80%。

像 Claude Code 和 OpenCode 这样的智能体已经发送了触发此转换的 Accept 标头。该功能处于 Beta 阶段，Pro、Business 和 Enterprise 级别的 Cloudflare 客户无需额外付费即可使用。它是基础设施层面的底层结构，使 Cloudflare 背后的每个网站都能立即更易于 AI 智能体访问（无需修改任何代码）。

## **五角大楼弃用 Anthropic，OpenAI 取而代之**

President Trump 周五 [指示所有联邦机构立即停止使用](https://truthsocial.com/@realDonaldTrump/posts/116144552969293195) Anthropic 的产品，称其为一家“激进左翼、觉醒主义公司”。Secretary Hegseth 随后 [在一条推文中宣布](https://x.com/SecWar/status/2027507717469049070?s=20) Anthropic 是供应链风险——这个标签通常用于外国对手。如果这项指定成为官方决定，将产生严重影响，可能会限制 Anthropic 与其他 DoW 供应商（如 AWS、Nvidia 和 Microsoft）开展业务。[Anthropic 作出回应](https://www.anthropic.com/news/statement-comments-secretary-war)，质疑 Hegseth 命令的含义，并表示将在法庭上挑战这项指定。

数小时后，[Sam Altman 在 X 上宣布](https://x.com/sama/status/2027578652477821175?s=20) OpenAI 已达成协议，将在五角大楼的机密网络上部署其模型。细节很重要。Altman 表示，该协议包括禁止国内大规模监控和“人类对武力使用的责任，包括自主武器系统”。表面上看，这听起来像是 Anthropic 所要求的。但措辞不同。Anthropic 想要在扣动扳机前的人工监督——在 AI 动力武器的杀伤链序列中有人类参与。OpenAI 的协议要求人类责任——这可能意味着事后问责。Anthropic 希望获得超越现有法律的监控保护，因为 Dario Amodei 认为现有法律尚未跟上 AI 可能实现的功能。OpenAI 的协议似乎遵循现有法律和政策，而这正是 Anthropic 认为不足的框架。

这还没结束。五角大楼自己的立场是，大规模监控和自主武器在现有法律下已经是非法的——这引发了一个显而易见的问题：如果你反正都不会做，为什么不把它写下来呢？Anthropic 迫使五角大楼回答这个问题，并因此被列入黑名单。OpenAI 达成了一项协议，其措辞看似相似，但承诺更少。这一事件为所有与政府开展业务的 AI 公司设定的先例值得密切关注。

---

## 往期回顾

> [Claude Code 登陆 Roadmap，OpenClaw 失去控制，以及 AI 工作流程](https://thenewstack.io/claude-code-comes-to-roadmap-openclaw-loses-its-head-and-ai-workslop/)

YOUTUBE.COM/THENEWSTACK

科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、采访、演示等。

订阅

组
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns 是 Insight Media Group 的编辑总监，负责 The New Stack、Roadmap.sh 和 Towards Data Science——这三个平台共同帮助数百万开发者了解接下来要学习什么。此前，他曾花费 16 年……

阅读 Matthew Burns 的更多文章](https://thenewstack.io/author/matthew-burns/)