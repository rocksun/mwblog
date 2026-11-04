**Replit CEO Amjad Masad 警告称，在员工设备上运行的 AI 编程智能体**正成为企业和政府的安全风险，因为金融机构开始限制对 Claude Code 等工具的访问。

“在员工终端上运行的 AI 智能体正成为企业和政府的系统性安全风险，”[Masad](https://www.linkedin.com/in/amjadmasad/) 周二[在 X 上](https://x.com/amasad/status/2117481616943820843)写道。“一些机构正在通过限制 Claude Code 等工具来应对，据报道高盛就是其中之一。”

> “一些机构正在通过限制 Claude Code 等工具来应对，据报道高盛就是其中之一。”

## 为什么金融业要限制编程智能体

在此之前，彭博社[报道称](https://news.bloomberglaw.com/capital-markets/goldman-restricts-traders-and-bankers-from-using-some-ai-tools)，高盛已将 Anthropic 的 Claude Code 和微软的 GitHub 编程工具的访问权限限制在工程师范围内。这些限制适用于银行家和交易员，但被称为 strats 的某些量化员工可以豁免。

高盛发言人 [Nick Carcaterra](https://www.linkedin.com/in/nick-carcaterra-a2119212/) 告诉彭博社，该行在决定哪些员工可以继续使用 AI 工具时，会在生产力提升与潜在风险之间进行权衡。

Masad 暗示高盛并非个例。

> “这在金融界很普遍。禁令重锤正在落下，”

他在回应一则关于该行限制措施的帖子时写道：“这在金融界很普遍。禁令重锤正在落下。”

当被问及是什么推动了这场打击行动时，Masad 指向了“供应链攻击等”。

## 凭证暴露问题

直接在员工机器上运行编程智能体会引发对凭证暴露、恶意指令和受损依赖项的担忧，这些问题中的每一个都已在金融行业之外显现。

几个月来，凭证问题一直在推动供应商转向短效 Token，Vercel 最近[通过设定放弃长效密钥的期限，强迫其自身供应商](https://thenewstack.io/vercel-oidc-static-credentials/)做出这一转变，终端上运行的智能体可以悄悄读取并重复使用这些长效密钥。

当在 X 上被问及银行更担心代码离开其环境还是缺乏审计追踪时，Masad 表示：“有太多事情了。”

他没有提供促成高盛限制措施或其他金融机构采用类似政策的安全事件的具体例子。

## 在云端隔离智能体

在发表上述评论的同时，Masad 分享了 Replit 于周一[发布的安全公告](https://frontier.replit.com/managed-cloud-environments-for-ai-agents/)。该公告由 Replit 的首席技术官 [Luis Héctor Chávez](https://www.linkedin.com/in/lhchavez/) 以及 Replit 的工程负责人 [Manish Mehta](https://www.linkedin.com/in/manishmehta/) 共同撰写，建议让 AI 智能体远离员工设备，改为在公司控制的云环境中运行。

> “AI 智能体应该在专用的、组织控制的环境中运行，并对每个任务所需的资源进行有限访问，”

Masad 写道：“AI 智能体应该在专用的、组织控制的环境中运行，并对每个任务所需的资源进行有限访问。”

Replit 建议在隔离环境中运行智能体，并单独管理凭证、审计日志和审批。

该公告指出了近期的安全事件，包括通过 Cursor 市场分发的受损 Claude Code 扩展，作为攻击者如何利用开发者工具的例子。

今年整个生态系统一再上演这种模式，包括一次攻击中入侵者[劫持了大约 19,000 个 GitHub 账户，然后将目标转向了大约 30,000 个代码库](https://thenewstack.io/hackers-hijacked-1900-github-accounts-then-they-went-after-30000-repos/)，这提醒人们，链条中的单个受污染链接可以延伸到它开始的机器之外。

## 控制智能体可以访问的内容

但将 AI 编程智能体限制给工程师并不能完全解决问题。即使是经验丰富的开发人员也可能会运行[遵循恶意指令](https://thenewstack.io/coding-agents-overstep-scope/)或引入受损软件的智能体，并且研究表明，将智能体带偏是多么容易，一个团队发现从 Claude Code 的指令中删掉单行代码就会导致其超出范围的操作激增。Replit 认为，公司需要控制智能体能做什么，而不仅仅是谁能使用它们。

## 这对企业 AI 采用意味着什么

高盛的限制表明，企业可能在重新思考允许员工使用 AI 编程工具的广泛程度。赋予非开发人员构建软件的能力一直是主要的卖点，但当智能体能够访问敏感的企业系统时，这就变得更难以合理解释。

Masad 认为，企业并不需要停止使用智能体。他们需要让智能体远离员工设备，并围绕它们可以访问的内容实施更严格的控制。

金融机构是否会广泛采用这种模式仍有待观察。Masad 将这些限制描述为普遍存在的，但并未提供公开证据来确立有多少组织已经引入了这些限制。

*The New Stack* 已联系 Replit，希望其就报道中的限制、驱动这些限制的安全担忧以及金融机构是否在改变其对待 AI 编程智能体的方法发表更多评论。

[Claude Code
2026 年成为 Claude Code 专家的分步指南

引言
使用 Claude 的方法
理解基础知识
使用 Claude Code
Claude 工作流
使用最佳实践
CLAUDE.md
技能
钩子
管理上下文](https://roadmap.sh/claude-code?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=ai-coding-agents-security)