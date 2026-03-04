<!--
title: OpenClaw GitHub登顶，安全吗？
cover: https://cdn.thenewstack.io/media/2026/03/82d193e2-beatriz-camaleao-h52hez3-3vu-unsplash-scaled.jpg
summary: OpenClaw迅速崛起为GitHub上星标最多的非聚合项目，但其代理系统特性和分布式部署引发了严重安全担忧，专家呼吁加强治理和控制。
-->

OpenClaw迅速崛起为GitHub上星标最多的非聚合项目，但其代理系统特性和分布式部署引发了严重安全担忧，专家呼吁加强治理和控制。

> 译自：[OpenClaw rocks to GitHub's most-starred status, but is it safe?](https://thenewstack.io/openclaw-github-stars-security/)
> 
> 作者：Adrian Bridgwater

OpenClaw 正在崛起。

这个开源的自主AI代理今年在GitHub历史星标排行榜上超越了Linux。该项目现在积累的星标数量已超过React，一个用于构建网页应用用户界面（UI）的开源JavaScript库。

在短短四个月内积累了超过25万颗星标，OpenClaw是GitHub上获得星标最多的非聚合型软件项目（即一个生成原创价值和内容的工具，而非过滤和显示现有信息），[star-history.com](https://www.star-history.com/blog/openclaw-surpasses-react-most-starred-software)最先报道了这一消息。

但开发者的喜爱并不总是能转化为长期的企业部署成功。微内核背后的概念从未根除庞大的Windows系统，一些人认为Lisp语言有点像Edsel或DeLorean。

那么现在的问题是，OpenClaw是昙花一现（无意使用龙虾炒饭双关语），[一个即将发生的安全性风险](https://thenewstack.io/openclaw-moltbot-security-concerns/)，还是一个正在形成的*事实*标准。

## OpenClaw 定义

OpenClaw 使用大型语言模型作为个人AI助手，充当在用户机器上本地运行的代理网关。

OpenClaw 有时被称为个人AI助手，在WhatsApp、Slack、Telegram、Google Chat、Signal、Discord、iMessage、Microsoft Teams和WebChat中提供代理答案服务。兼容Mac OS X、iOS和Android，建议Windows用户通过WSL2（适用于Linux的Windows子系统）使用OpenClaw，而不是原生运行，以确保最佳兼容性和稳定性。

为什么是龙虾标志和主题？因为OpenClaw在用户机器上执行任务时“夹走了繁重工作”。

## 眼中是星光？

根据一份引用微信公众号“新智元”的报告，GitHub上的星标有点像“低成本的声明”，与书签或点赞相差不远。从其原文中文翻译过来，该博客指出，在开发者粉丝榜单顶部看到资源汇总、教程和书单是很常见的。

“当你移除这些资源库和事件型项目，真正审视那些可以安装和运行的基础软件时，OpenClaw的崛起是极具颠覆性的。与此同时，核心开发者正忙着将其变成一台24/7自动代码编写机器。伴随狂热而来的是对现实世界控制的丧失，”作者写道。

> “OpenClaw之所以人气爆棚，原因只有一个——无论是技术人员还是非技术人员，都想要一个免费的个人AI助手。”

今年一月和二月，OpenClaw的第三方技能市场ClawHub在一次精心策划的网络安全攻击中被黑客入侵，那么这里的风险会传播多远呢？

[Michael Levan](https://www.linkedin.com/in/michaellevan/)，[Solo.io](https://www.solo.io/)的AI架构师，告诉《The New Stack》，OpenClaw的成功归结于一个看似普遍的愿望：一个个人助手。

“OpenClaw之所以人气爆棚，原因只有一个——无论是技术人员还是非技术人员，都想要一个免费的个人AI助手。尽管它本身令人印象深刻，但它也带来了一系列复杂的安全挑战，从集中式访问控制（谁可以使用标准RBAC或更复杂的协议如ReBAC和ABAC做什么）到LLM、代理技能和MCP服务器，”Levan说道。

Levan表示：“OpenClaw在企业中成功采用将需要多层控制，包括用于集中认证的企业级ExtAuth服务器，增强对代理流量的可观测性以及运行时防护措施，包括速率限制和提示防护。”

## 超越模型

显然这里正在发生真正的转变。OpenClaw的快速普及反映了向执行工作流并更像自主服务（在某些情况下更像员工）而非传统应用的系统转变。

推动这种兴趣的不仅仅是模型本身，更是自动化跨工具和系统实际任务的能力，这正是开发者多年来一直努力实现的操作化。

[Yossi Atlevet](https://www.linkedin.com/in/yossi-altevet-538340/?originalSubdomain=il)，[DeepKeep](https://www.deepkeep.ai/)的CTO和联合创始人，告诉《The New Stack》，OpenClaw的普及已经超出了常规。

Atlevet说：“届时，与OpenClaw合作的开发者不再是整合一个模型；他们实际上是在部署一个分布式系统，可以在API、文件和内部基础设施之间自动采取行动。这从根本上改变了安全模型。”

“传统的应用程序安全性假设确定性行为和明确定义的权限。然而，代理系统在运行时做出决策，将工具串联起来，并跨多个信任边界运行。”

Atlevet表示，因此，像提示注入、不安全工具调用、数据暴露和意外操作等风险不再是随机事件。它们是这些系统运作方式固有的，并且超出了大多数现有安全控制设计用于处理的范围。

对Atlevet来说，开发者现在需要弥合差距，将安全性融入执行层，不仅要监控和验证模型生成的内容，还要监控和验证代理实际尝试做的事情。

## 另一个Napster时刻？

[Alexander Feick](https://www.linkedin.com/in/alexanderfeick/) 在[eSentire](https://www.esentire.com/) 认为OpenClaw的受欢迎程度感觉就像AI代理的Napster时刻，但他同意他的行业同行关于风险的看法。

Feick告诉《The New Stack》：“用户正在接受风险，因为其效用是实实在在和立竿见影的，这暴露了在任何人构建治理之前，治理应该是什么样子。市场会将OpenClaw之类的工具推到治理框架之前，除非我们首先嵌入控制平面，而不是作为事后诸葛亮。”

Feick说：“根本的差距不仅仅是缺少一个复选框——它是一个能够表达细粒度信任边界的控制平面的缺失。人们希望说‘使用我的信用卡’，但当前的代理无法强制执行消费上限或商家安全列表等限制；它们可以广泛读取电子邮件，但不能限定到特定的收件箱或联系人。没有这些控制，风险的扩大速度将快于普及速度。”

## OpenClaw 比 Linux 更伟大吗？

OpenClaw现在是否会被视为下一个Twitter并被认为比Linux更伟大，这一点尚不确定。

Linux在全球的安装基础、其作为互联网基础的根本作用，以及它在以前专有领域的广泛接受，无疑保证了它在可预见的未来保持其全明星地位。

请递上龙虾卷。