<!--
title: 2小时内，研究员轻松劫持OpenClaw
cover: https://cdn.thenewstack.io/media/2026/02/564ec44f-getty-images-t3grnwa0cdy-unsplash-scaled.jpg
summary: OpenClaw AI代理及Moltbook社交网络存在严重安全漏洞，研究员仅用不到2小时即成功劫持，导致数据泄露、远程代码执行及恶意插件泛滥。AI代理的安全风险已迫在眉睫，需立即防范。
-->

OpenClaw AI代理及Moltbook社交网络存在严重安全漏洞，研究员仅用不到2小时即成功劫持，导致数据泄露、远程代码执行及恶意插件泛滥。AI代理的安全风险已迫在眉睫，需立即防范。

> 译自：[It took a researcher fewer than 2 hours to hijack OpenClaw](https://thenewstack.io/openclaw-moltbot-security-concerns/)
> 
> 作者：Steven J. Vaughan-Nichols

安全研究人员一直在编目和报告漏洞，他们表示，所有关于OpenClaw AI代理及其社交网络，[Moltbook](https://thenewstack.io/moltbook-the-singularity-or-hype/)的安全担忧已经得到证实。

OpenClaw，这个热门的新型个人AI代理，可能运行在你的本地机器上。然而，默认情况下，它拥有完整的系统访问权限，可以读取文件、执行命令、管理凭据，并通过Discord、Slack和Telegram等消息平台与外部服务协作。对于有安全意识的人来说，仅仅这一点就令人深感不安。

但现在，这已成为整个“个人AI代理”概念的一次实战安全演练。研究人员正在迅速编目具体的漏洞，从远程代码执行错误到完全开放的社交图谱数据库，再到充斥着恶意软件的插件生态系统。

我们从一开始就知道，OpenClaw（当时称为Clawdbot）发布时就带有一个巨大的攻击面、强大的本地权限、一个可网络访问的控制接口，以及其[模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/?mailpoet_page=subscriptions)管道中薄弱或缺失的身份验证。实际上，这意味着用户机器上的任何进程都可以触及代理的“方向盘”，并像遥控汽车一样驾驶它。

例如，安全公司[Guardz](https://guardz.com/)的一份技术深度分析描述了默认部署中Clawdbot网关绑定到0.0.0.0端口18789并[暴露了完整的管理API](https://guardz.com/blog/when-ai-agents-go-wrong-clawdbots-security-failures-active-campaigns-and-defense-playbook/)，Shodan上索引了数百或数千个带有“Clawdbot Control”签名的此类实例。

他们还指出，MCP发布时“缺乏安全性”，使得攻击者和信息窃取者很容易针对Clawdbot的配置目录，并窃取明文凭据和聊天记录。

MCP授予对工具、凭据和操作例程的直接访问。因此，暴露的端点让攻击者能够读取配置文件、获取存储的API密钥和OAuth令牌、浏览私人对话日志，甚至像所有者一样向代理发出命令。

但是，等等！还有更多！一个单独的高严重性缺陷，现在追踪为[CVE‑2026‑25253](https://nvd.nist.gov/vuln/detail/CVE-2026-25253)，影响了OpenClaw。这个漏洞允许攻击者制作一个恶意链接，当用户在先前已验证登录OpenClaw控制UI的浏览器中打开该链接时，会窃取令牌并交出对网关API的“操作员级别”访问权限。

> 他“在大约1小时40分钟内发现了从一键账户接管到远程代码执行（RCE）的漏洞。”

正如Ethiack（一家道德黑客安全初创公司）的AI工程师[Henrique Branquinho](https://www.linkedin.com/in/henrique-branquinho-5495a7123/)所写，他“在大约1小时40分钟内发现了从[一键账户接管到远程代码执行 (RCE)](https://ethiack.com/news/blog/one-click-rce-moltbot)的漏洞。”

“受害者只需访问一个由攻击者控制的网站，该网站通过WebSocket通道泄露网关控制UI的身份验证令牌（该功能默认启用）。然后，即使受害者在本地托管，任意命令也会运行。” 哇！

他警告说，由于受害者的浏览器发起出站WebSocket连接，即使网关配置为仅在环回接口上监听，此漏洞也有效，从而有效地绕过了通常“localhost是安全的”这一假设。通过被盗令牌，攻击者可以更改配置，在主机上执行任意代码，并指示代理对任何连接的服务或数据集采取行动。

至于为OpenClaw代理构建的类似Reddit的社交网络[Moltbook](https://www.moltbook.com/)，它已经遭受了一次关键的后端配置错误，暴露了其主数据库。云安全公司[Wiz](https://www.wiz.io/)的研究人员表示，网站代码中嵌入的一个密钥足以解锁对Moltbook内部数据存储的完整读取访问权限。这让我感觉不太好。

此漏洞暴露了数万个电子邮件地址，并且，根据Wiz威胁暴露负责人[Gal Nagli](https://www.linkedin.com/in/galnagli/)的说法，还暴露了大约150万个API密钥和代理之间的私人消息，同时还允许攻击者冒充平台上的任何机器人。手持有效身份验证令牌，恶意行为者可以代表代理身份发布、编辑或删除内容，可能毒害下游模型或发起大规模的虚假信息和垃圾邮件活动。作恶的可能性是无穷无尽的。

雪上加霜的是，Moltbook依赖于OpenClaw。大多数Moltbook账户都是由其所有者编写脚本的OpenClaw代理，用于角色扮演、协作或试验自主代理间的交互。因此，Moltbook也容易受到OpenClaw安全问题的影响。

安全巨头[Palo Alto Networks](https://www.paloaltonetworks.com/)警告说，[OpenClaw“记住”数周交互的能力意味着](https://www.paloaltonetworks.com/blog/network-security/why-moltbot-may-signal-ai-crisis/)网站、PDF或Moltbook帖子中的隐藏指令可以保持休眠状态，直到未来的任务触发代理执行它。换句话说，“有了持久记忆，攻击不再仅仅是即时漏洞利用。它们变成了有状态的、延迟执行的攻击。”

不过，正如安全公司[Dvuln](https://dvuln.com/)的创始人[Jamieson O’Reilly](https://www.linkedin.com/in/theonejvo/)在LinkedIn上观察到的，尽管“数百人[已将他们的Clawdbot控制服务器暴露给公众](https://www.linkedin.com/pulse/hacking-clawdbot-eating-lobster-souls-jamieson-o-reilly-whhlc/)……但这并不是世界末日。这甚至不是一次特别复杂的攻击——它是一个任何安全审查都应该发现的配置错误/漏洞。” 啊，但他们没有发现，对吗？哦，他还发现代理本身无法帮助用户保护它。讽刺吧？

假设最明显的漏洞都已修补，那又如何？Moltbot/OpenClaw生态系统已经成为商品恶意软件的一个有吸引力的分发渠道。OpenClaw的“技能”，即扩展助手功能的插件，已经遭到攻击者的滥用。他们使用常见的伎俩，例如发布拼写错误或伪装成加密交易工具、金融工具或社交媒体助手的虚假软件包。

根据社区安全网站[OpenSourceMalware](https://opensourcemalware.com/)的数据，OpenClaw现在有[386个受恶意软件感染的技能](https://opensourcemalware.com/blog/clawdbot-skills-ganked-your-crypto/)。这在[3016个已知的OpenClaw技能](https://blog.virustotal.com/2026/02/from-automation-to-infection-how.html)中占了一部分。我不喜欢这样的几率。

O’Reilly在随后的帖子中总结得很好：“就在6个月前，我仍然对AI在攻击能力方面的实用性和威胁持怀疑态度。” 他改变了主意。“如果你的工作与组织中的数据/隐私/安全责任有关，请不要像我一样一直告诉自己‘也许有一天，但不是今天’。现在就投资AI防御。” 如果你不这样做，你会后悔的。

与此同时，明智的做法可能是远离Moltbot和OpenClaw。缺乏有意义的安全性可能会让粗心的开发者和用户吃亏。