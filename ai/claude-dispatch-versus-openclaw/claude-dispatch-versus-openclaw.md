<!--
title: Anthropic回应深圳排队爆火的AI工具
cover: https://cdn.thenewstack.io/media/2026/03/d3029841-darmau-byphnnewj3m-unsplash-scaled.jpg
summary: 文章探讨了开源AI代理OpenClaw的流行，尤其是在中国市场。Anthropic试图通过推出更安全的Claude Dispatch for Cowork来回应，该产品允许AI代理通过移动设备访问本地驱动器。然而，作者认为Anthropic的方案虽然更安全，但在用户体验上不如OpenClaw直观，并质疑其竞争力，强调需进一步提升集成度和用户友好性。
-->

文章探讨了开源AI代理OpenClaw的流行，尤其是在中国市场。Anthropic试图通过推出更安全的Claude Dispatch for Cowork来回应，该产品允许AI代理通过移动设备访问本地驱动器。然而，作者认为Anthropic的方案虽然更安全，但在用户体验上不如OpenClaw直观，并质疑其竞争力，强调需进一步提升集成度和用户友好性。

> 译自：[Anthropic's response to the AI tool that caused lines around the block in Shenzhen](https://thenewstack.io/claude-dispatch-versus-openclaw/)
> 
> 作者：David Eastman

OpenClaw在全球的受欢迎程度有时难以衡量。然后，最近《福布斯》上的一篇报道就是例证。

《[福布斯](https://fortune.com/2026/03/14/openclaw-china-ai-agent-boom-open-source-lobster-craze-minimax-qwen/)》的一篇文章援引路透社的报道称：“3月的一个周五下午，近1000人排队等候在深圳腾讯总部外，只为在他们的笔记本电脑上安装一款软件。”

为什么一家市值6500亿美元的中国公司的工程师会把一位奥地利人开发的开源AI代理部署到普通人的笔记本电脑上？但似乎许多中国AI初创公司都在政府的鼓励下试图“养一只龙虾”（raise a lobster）。

两周前我研究了[NanoClaw](https://thenewstack.io/nanoclaw-containerized-ai-agents/)，它是其更大的甲壳类兄弟的一个更安全的版本，但像Anthropic这样敏锐的公司很快就会卷入一场源于其自身工作的热潮。

我们现在在多个地方看到了OpenClaw的三个基本基础：一个LLM代理，能够访问本地驱动器，并通过移动消息控制。就像破产一样，这项技术的用户群逐渐扩大，然后突然爆发。用户现在可以通过他们已经非常熟悉的软件，利用AI来完成实际工作。这就是其他公司试图达到的目标。

我想迅速回应[Azeem Azhar](https://www.linkedin.com/in/azhar/)的一个观点——尽管Apple在AI软件领域没有做出任何值得注意的成就，但他们的硬件非常适合运行代理式（即实际计算）任务。他们取代Intel芯片的Apple Silicon系列芯片非常适合本地设备上的推理。这就是为什么Mac Mini——一个可能一整代人从未听说过的电脑——在商店里卖断货的原因。

OpenClaw的关键弱点（缺乏安全边界和防护措施）也正是它的优势——你可以尝试任何事情，它可能就会奏效。当然，任何可能被起诉的公司都不会走这条“易燃”路线。

Anthropic在移动通信方面的首次尝试是上个月发布的[Claude Remote Control](https://code.claude.com/docs/en/remote-control)。它与Claude Code配合使用，[Simon Willison](https://simonwillison.net/2026/Feb/25/claude-code-remote-control/)将其描述为“不稳定”。

## Claude Dispatch for Cowork登场

但现在有了[Claude Dispatch for Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork)。通过Cowork，你已经获得了三合一中的两部分——AI代理可以与你的本地驱动器协同工作，而无需理解MCP。

如果你是Pro计划用户，可以尝试这个研究预览版。

首先，确保你的Claude Desktop是最新的。如果你还记得，你可以从其中的一个标签页启动[Cowork](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/)。

查看我的桌面应用程序文件菜单，我立刻看到需要更新

![](https://cdn.thenewstack.io/media/2026/03/4a243a62-image.png)

更新后，当我重启Claude Desktop时，我看到了这个：

![](https://cdn.thenewstack.io/media/2026/03/2d5aa649-image-1-1024x430.png)

因此，点击Dispatch，我们看到所需的步骤非常简单：

![](https://cdn.thenewstack.io/media/2026/03/4524a5a8-image-2-845x1024.png)

新增的部分是我们还需要一个手机应用。现在，我不会说这是一个失误，但这不像使用WhatsApp。我们需要安装一个新的应用才能与Claude对话。然而，这当然更安全，很可能是Anthropic正确的第一个举措。我之前没有Claude应用（因为我根本不需要），但我把它安装在了我的Android手机上，以完成整个链条。

最终的设置向我们揭示了正在发生的事情

![](https://cdn.thenewstack.io/media/2026/03/b5a74737-image-3-821x1024.png)

（我不太确定“Claude in Chrome”是什么，但它似乎是另一个测试版插件。你可能已经看过我本周关于[WebMCP](https://thenewstack.io/webmcp-chrome-ai-agents/)的文章。）

使用Claude Dispatch，你无需为每个任务启动一个新会话，而是有一个单一的持久线程。这个线程不会重置——Claude会保留之前任务的上下文，因此你可以在笔记本电脑或手机上从上次中断的地方继续。实际上，即使你想重启，也相当困难。

登录并摆弄我的手机后，我看到了Dispatch线程的链接，然后我们开始了。

我想尝试查找护照扫描件——这实际上是Claude Cowork提示中建议的功能。我首先在笔记本电脑上进行了尝试：

![](https://cdn.thenewstack.io/media/2026/03/a56d3982-image-4-1024x523.png)

我需要与Google Drive对话。尽管Claude不知道它可以这样做，但幸运的是，网络知道——我只需添加一个连接器：

![](https://cdn.thenewstack.io/media/2026/03/1d3409fd-image-5-1024x493.png)

我意识到它访问的是网络上的Drive，而不是实际的文件夹，这很奇怪。不过，我还是授予了访问权限并继续。

正如所料，它像对讲机一样工作——我在手机上输入的任何请求都会“调度”到笔记本电脑上：

![](https://cdn.thenewstack.io/media/2026/03/1d0fca00-image-6-1024x444.png)

不幸的是，在多次权限请求后，它放弃了查询并停止工作。

我本打算继续尝试，也许通过告诉它一个特定的文件夹，但我意识到我不知道问题出在Cowork还是Dispatch，而且我可能会忽略重点。我可以清楚地看到远程控制方面工作正常。然而，我不确定这是否能促使人们放弃OpenClaw，转而等待Anthropic迎头赶上。

## 养一只龙虾

我在想，这种方法——尽管是一个好的开始——是否会让Anthropic落后于OpenClaw太多。即使这变得不那么麻烦，一个由应用控制的单一连续线程，给你一个对讲机，也只是更多Anthropic特有的机制。用户并不是想要一个会话的对讲机——他们只是想找到那个护照扫描件。

感觉还需要做更多工作，才能找到正确的框架，既能保持安全，又能足够灵活地缩短好奇心和实际采用之间的距离。