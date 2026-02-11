<!--
title: GSD如何让Claude成为一个“自主开发”的程序员
cover: https://cdn.thenewstack.io/media/2026/02/cc56e694-sara-oliveira-s0y4m1x8a3u-unsplash-scaled.jpg
summary: 本文记录了作者使用 Claude 扩展 GSD 开发 JSON 查看器的过程。文中介绍了 OpenClaw 作为本地 AI 助手的潜力与安全问题。作者详细描述了 GSD 迭代开发、checkpoint 审批以及遇到 token 限制等情况。尽管面临挑战，GSD 成功引导项目，展示了其引导开发并帮助学习新技术的强大能力，如 SwiftUI。
-->

本文记录了作者使用 Claude 扩展 GSD 开发 JSON 查看器的过程。文中介绍了 OpenClaw 作为本地 AI 助手的潜力与安全问题。作者详细描述了 GSD 迭代开发、checkpoint 审批以及遇到 token 限制等情况。尽管面临挑战，GSD 成功引导项目，展示了其引导开发并帮助学习新技术的强大能力，如 SwiftUI。

> 译自：[How GSD turns Claude into a self-steering developer](https://thenewstack.io/openclaw-gsd/)
> 
> 作者：David Eastman

OpenClaw 的普及速度相当惊人，这是有充分理由的：它的受众超越了开发者领域，尤其是那些只想尝试数字助理的人。今天的文章继续我与 GSD 的旅程，但 LLM 代理格局正在迅速变化，这颗“流星”吸引了所有人的目光。

OpenClaw 的核心是一个本地托管的开源 AI 助理，可在你的计算机或服务器上运行。你可以通过你可能已在使用的应用程序与它交流，例如 WhatsApp、Telegram、Discord、Slack、Signal 甚至是 iMessage。而且它确实“能做事”——有时甚至做得*太*好。它是一个网关服务，维护 WebSocket 连接，并包含一个智能编排层，用于处理 LLM 代理。

OpenClaw 在 LLM 代理方面展现出强大的技术专注；然而，[其显著且多样的安全问题](https://thenewstack.io/openclaw-moltbot-security-concerns/)意味着我们在试验代理之前必须更仔细地考虑代理漏洞。但请继续关注，即使是[AI 教会](https://thenewstack.io/moltbook-the-singularity-or-hype/)的这种奇特旁路也确实引人入胜。OpenClaw 可能有缺陷，但它确实表明，与代理能够做的事情相比，现有且根深蒂固的数字助理是多么可笑地有限。现在回到我们预定的节目。

> OpenClaw 可能有缺陷，但它确实表明，与代理能够做的事情相比，现有且根深蒂固的数字助理是多么可笑地有限。

在我[关于流行的 Claude 扩展 GSD 的第一篇文章](https://thenewstack.io/beating-the-rot-and-getting-stuff-done/)中，我设置了一个项目来创建一个 JSON 查看器。GSD 随后提出了许多问题来制定具体计划，最后在其选择的平台 SwiftUI 上完成了第一个版本。

当我们停下来时，它刚刚展示了它的工作：

![](https://cdn.thenewstack.io/media/2026/02/f84309c7-image.png)

所以首先，让我们运行实际的东西。我仔细遵循建议，因为我不是 SwiftUI 开发者，也不使用 Xcode。事实上，我不得不更新到 26.2 才能使用它。我运行它，它确实做到了所描述的事情：

![](https://cdn.thenewstack.io/media/2026/02/ba988d48-image-1-1024x743.png)

所以我批准了检查点。是的，这只是一个带标题的窗口，但它告诉我所有的假设都是正确的。它花了一些时间更新路线图和需求。

然后我们准备进行第二阶段的规划：

![](https://cdn.thenewstack.io/media/2026/02/b4e83275-image-2-1024x290.png)

嗯，那个百分比进度条正在慢慢上升。当时，我以为它代表项目离完成还有多远。

我正在 [Warp](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/) shell 中运行 GSD，但在单个连续会话中运行的一个缺点是，我无法使用 Warp 独特的命令和响应块，这些块可以告诉我所有响应的时间。

阶段目标和成功标准现在转向 SwiftUI 的具体细节，这我很喜欢。虽然我不是 Mac 开发者，但我可以看到它正在引入运行所需的通用组件：

![](https://cdn.thenewstack.io/media/2026/02/a264ff24-image-3-1024x360.png)

尽管我在此过程中扮演着管理者的角色，但我的开发者思维能够理解它正在执行的步骤。创建计划后，它会执行该计划。

现在再次需要人类（也就是我）进行验证——这次是为了检查我能否通过应用程序加载 JSON 文件：

![](https://cdn.thenewstack.io/media/2026/02/2f987125-image-4-1024x414.png)

我确实从我的项目中加载了一个带有预期 Mac 用户界面的 JSON 文件，并且它确实统计了文件中的所有对象——仅此而已。我批准它的进度以继续。在我批准之前，我快速问了一个关于 token 使用的问题：

![](https://cdn.thenewstack.io/media/2026/02/60a07c42-image-5-1024x120.png)

同样，GSD 在继续之前需要我的批准。我给了。

最后，我们达到了我的计划限制：

![](https://cdn.thenewstack.io/media/2026/02/60bb061e-image-6-1024x199.png)

所以我清除了上下文窗口，再次尝试第三阶段。注意当进度条变红时出现的恐怖骷髅。

![](https://cdn.thenewstack.io/media/2026/02/05da7359-image-7.png)

无论如何，现在我知道那个进度条意味着什么了！当窗口被清除时它会重置。我还检查了网站上的账单。我还被警告说，我正在接近我的限制，直到定期重置：

![](https://cdn.thenewstack.io/media/2026/02/e1fb1424-image-8.png)

顺便说一句，这是在专业版计划上。所以我执行了第三阶段。作为记录，这是规划部分：

![](https://cdn.thenewstack.io/media/2026/02/e5fb1424-image-9-1024x350.png)

在等待我的 token 从专业版计划的使用中重新补充后，我们继续前进。现在，GSD 正在研究如何实现一个可浏览列表，并将其绑定到我的 JSON 数据。

最后，GSD 完成了一个更重要的版本，其中大部分查看功能似乎都已到位：

![](https://cdn.thenewstack.io/media/2026/02/0fcb2f10-image-10-1024x365.png)

在 Xcode 中启动应用程序后，我可以随意从我选择的 JSON 文件中选择对象：

![](https://cdn.thenewstack.io/media/2026/02/8a309f39-image-11-1024x683.png)

为了完整起见，这是 Xcode 中生成项目的功能布局。结构看起来不错——我继续这个项目没有问题。但我们已经走得足够远，足以证明 GSD 具备引导开发项目而不会出现问题的能力。

![](https://cdn.thenewstack.io/media/2026/02/9784efff-image-12-1024x356.png)

### 结论

尽管 GSD 工作流使用了大量组织术语——计划、需求、阶段、波次、检查点（他们确实没有留下任何敏捷行话）——我明白这是为了将所有内容联系在一起，保持“专注”，并减轻上下文窗口的压力。

![](https://cdn.thenewstack.io/media/2026/02/e3124752-image-13.png)

即使在窗口耗尽、token 耗尽以及 Mac 必须重启之后，我也能够继续。正如我在之前的文章中提到的，这些限制是时代的产物——考虑到目前投入到 AI 基础设施的全球资源量，我预计 token 成本会下降，并且平均上下文窗口会扩展，直到不再存在限制。如果我想避免 token 重新填充之间的中断，那么我就需要升级我的计划。

对于开发者来说，看到项目需求逐一发展是完全自然的——但这可能比有些人想象的要慢。对我而言，价值在于追求一个项目，其语言（SwiftUI）我可以在看到工作原型*之后*再学习。我觉得 GSD 是一条明智的前进道路，我预计 Anthropic 将悄然吸收它。