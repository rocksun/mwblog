
<!--
title: 使用Claude 3.7 Sonnet让联邦宇宙更易于访问
cover: https://cdn.thenewstack.io/media/2025/03/86acb995-joshua-earle-jypu1ftddwk-unsplashb.jpg
-->

Claude 的 Sonnet LLM 和 ChatGPT 如何帮助简化去中心化和中心化社交网络之间的连接。

> 译自：[Making the Fediverse More Accessible With Claude 3.7 Sonnet](https://thenewstack.io/making-the-fediverse-more-accessible-with-claude-3-7-sonnet/)
> 
> 作者：Jon Udell

几年前，我放弃了 Twitter，转而使用 Mastodon。最近发生的事件验证了我的选择，并强调了[一个去中心化的联邦宇宙](https://thenewstack.io/the-fediverse-points-to-our-social-media-future-post-musk/)的战略重要性，它不能被单一的公司或国家行为者所拥有。虽然 Mastodon 满足了我的需求，但 Twitter 的大部分用户已经转向 Bluesky。目前这很好，但可能不会永远如此。在一篇题为“[科学必须远离国家管理的](https://www.thetransmitter.org/policy/science-must-step-away-from-nationally-managed-infrastructure/)”的文章中，Dan Goodman 写道：

我们如何为未来从 Bluesky 迁移到 Mastodon 做准备？[Bridgy Fed](https://fed.brid.gy/)——一项使您能够[将您的网站、fediverse 帐户和 Bluesky 帐户连接在一起](https://thenewstack.io/bridge-building-the-state-of-the-open-web-heading-into-2025/)的服务——将会有所帮助。但 Bridgy Fed 需要更容易使用。所以我招募了 Claude 的新 Sonnet 7 模型来做到这一点。

## Fediverse/Bluesky 桥

这座桥由 [Ryan Barrett](https://snarfed.org/) 发明和运营，它使 Bluesky 用户能够关注 Mastodon 用户并与之互动——反之亦然——通过一对代理，可以在两端创建虚拟帐户。原则上，使用这座桥很容易。这是来自 [Kilian Evang](https://kilian.evang.name/) 的一份方便的备忘单：

![](https://jonudell.info/newstack/cheatsheet-kilian.png)

典型的开发人员可以轻松且自动地进行这种心理替换，他们往往没有意识到其他人通常不会这样做，并且许多人需要帮助才能进行转换。这是开发人员编写的文档通常不如他们可能提供的帮助的原因之一。这并不是说作者不关心有效地沟通，而是他们没有意识到他们默认理解的事情必须明确地展示出来，才能使其他人达到相同的理解水平。

在这种情况下，我和可能许多其他人希望看到的是：

![](https://jonudell.info/newstack/fedi-bsky-cheatsheat2.gif)

所以我向 Claude 展示了 Kilian 的屏幕截图，并要求提供该剪辑中显示的[交互式版本](https://jonudell.info/fedi-bsky-interactive-cheatsheet/)。

## 创建初稿

这是最初的提示：

> Turn this into an interactive web page where I can enter the respective handles and see the transformation.

Claude 以一个托管的构件作为回应，您可以在此处实时看到。好的开始！这确实是我想要的本质;我本可以分享这个链接并收工。但是，当然，当事情发生得如此迅速和容易时，你不能不想修饰。对于初学者来说，Claude 工件是基于 React 的，除非必要，否则我从不希望这样做。

> No React, no dependencies, just vanilla JS.

这一次，生成的工件在 Claude 提供的托管环境中失败，并且 crank 转了几圈并没有解决问题。但这没关系，我现在有一个独立的 HTML/CSS/JS 结构，我可以在本地保存、测试和改进它，并轻松发布到任何普通的 Web 主机。我为它创建了一个 repo 并收工了。

## 增强初稿

几天后，当我带着增强的想法回来时，我想首先要求 Claude 记录现有代码。正当我争论是上传 HTML 文件还是复制/粘贴它时，我注意到了新的 GitHub 集成。

![](https://jonudell.info/newstack/claude-github.png)

现在，您可以授权 Claude 查看您的存储库，然后将其指向要包含在聊天会话中的文件。好！

以下是我心目中的增强功能：

- **动态验证**。键入 handle 时，您应该会看到翻译的形成。当它生效时，它应该从灰色变为绿色
- **Copy （复制） 按钮**。当它变为绿色时，应出现一个复制按钮。
- **TLD 验证**。Mastodon 句柄以域名结尾，除非这些是在此列表中找到的有效顶级 TLD，否则不应变为绿色。
- **Bridgy 用户页面**。当您桥接 Mastodon 或 Bluesky 帐户时，该桥会创建一个页面，您可以在其中监控相应的 ghost 帐户。指向该页面的链接也应该动态形成，并且只有在有效时才会变为绿色。

在进行这些增强功能时，我要求 Claude 证明它们有效，它通过实时生成可交互的工件来隔离这些更改，并使每个更改都可用于交互式测试。这让我对这些更改有了很大的信心，但现在我必须将它们集成到不断发展的工具中。

## 集成更改

受到 Claude 新获得的 GitHub 能力的鼓舞，这是我的下一个提示：

> Can you file a PR that proposes those changes and adds tests for them?

目前，这有点遥不可及。但是，问问总是没错的，对吧？我降低了我的期望，转而问：

> Can you provide the changes in a patch file?

Claude 立即提供了一个看起来完全合理的补丁文件，但实际上却完全坏掉了。这令人惊讶，因为这似乎是 [LLM 倾向于做得非常好的](https://thenewstack.io/choosing-when-to-use-or-not-use-llms-as-a-developer/)那种机械的、面向模式的转换。我们来回折腾了一段时间，但我始终无法让它生成一个可用的补丁。当我意识到它可能需要一个带有行号的源文件版本时，我提供了它——但仍然没有帮助。我将 ChatGPT 也加入了进来，但它也束手无策。我不确定为什么这个特殊的任务似乎难倒了最聪明的 LLM。是我提问的方式不对吗？这个任务有什么与常理相悖的地方吗？如果有人能解释它们失败的原因，我将洗耳恭听。

## 最后的清理和重构

抱怨这个限制感觉很荒谬。我想起了 Louis C.K. 关于飞机 WiFi 出问题的经典段子。（“这太糟糕了。”“伙计，你正坐在天空中的椅子上！”）尽管如此，将这些更改集成起来确实比最初生成它们花费了更多的时间。

一旦该工具的功能完善，就需要进行通常的重构和整合。我很清楚需要做什么，但是当我要求 Claude 和 ChatGPT 审查代码时，他们提出了一些我没有想到的改进，其中包括事件处理程序从两个不同的地方被冗余地调用。

同样，实际上集成这些改进比最初生成它们要困难得多。不过，一旦完成，Claude 就能够编写一个不错的[变更日志](https://github.com/judell/fedi-bsky-bridge-interactive-cheatsheet/blob/main/CHANGELOG.md)。

## 坐在天空中的椅子上

正如 Dan Goodin 指出的那样，我们需要为不可避免的平台转变做好准备。值得注意的是，这些工具使我能够构建和完善这个小而有用的工具，比其他任何方式都更快更容易。使 fediverse/Bluesky 更容易访问是朝着使我们自己免受企业所有者的突发奇想，并在我们的在线社区中建立更多韧性的方向迈出的一步。

这并不是一个完全顺利的体验，但我很感激 AI 的帮助，它简化了任务并丰富了结果。毕竟，我们正坐在天空中的椅子上。偶尔出现的补丁文件小故障似乎是微不足道的代价。
