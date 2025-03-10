# 使用 Claude 3.7 Sonnet 让 Fediverse 更易于访问

![Featued image for: Making the Fediverse More Accessible With Claude 3.7 Sonnet](https://cdn.thenewstack.io/media/2025/03/86acb995-joshua-earle-jypu1ftddwk-unsplashb-1024x576.jpg)

几年前，我放弃了 Twitter，转而使用 Mastodon。最近发生的事件验证了我的选择，并强调了[一个去中心化的 fediverse](https://thenewstack.io/the-fediverse-points-to-our-social-media-future-post-musk/) 的战略重要性，它不能被单一的公司或国家行为者所拥有。虽然 Mastodon 满足了我的需求，但 Twitter 的大部分用户已经转向 Bluesky。目前这很好，但可能不会永远如此。在一篇题为“[科学必须远离国家管理的 инфраструктура](https://www.thetransmitter.org/policy/science-must-step-away-from-nationally-managed-infrastructure/)”的文章中，Dan Goodman 写道：

我们如何为未来从 Bluesky 迁移到 Mastodon 做准备？[Bridgy Fed](https://fed.brid.gy/)——一项使您能够[将您的网站、fediverse 帐户和 Bluesky 帐户连接在一起](https://thenewstack.io/bridge-building-the-state-of-the-open-web-heading-into-2025/)的服务——将会有所帮助。但 Bridgy Fed 需要更容易使用。所以我招募了 Claude 的新 Sonnet 7 模型来做到这一点。

## Fediverse/Bluesky 桥

这座桥由 [Ryan Barrett](https://snarfed.org/) 发明和运营，它使 Bluesky 用户能够关注 Mastodon 用户并与之互动——反之亦然——通过一对代理，可以在两端创建虚拟帐户。原则上，使用这座桥很容易。这是来自 [Kilian Evang](https://kilian.evang.name/) 的一份方便的备忘单：

Easy, right? Well, for most developers’ brains it is, but not for mine and certainly not for many non-devs. To follow the Bluesky handle *jonudell.bsky.social* from the fediverse, you have to translate *@username.app.tld@bsky.brid.gy* to *@jonudell.bsky.social@bsky.brid.gy*. To follow the Mastodon handle *judell@social.coop* from Bluesky, you have to translate *@username.app.tld.ap.brid.gy* to *@judell.social.coop.ap.brid.gy*.

典型的开发人员可以轻松且自动地进行这种心理替换，他们往往没有意识到其他人通常不会这样做，并且许多人需要帮助才能进行转换。这是开发人员编写的文档通常不如他们可能提供的帮助的原因之一。这并不是说作者不关心有效地沟通，而是他们没有意识到他们默认理解的事情必须明确地展示出来，才能使其他人达到相同的理解水平。

在这种情况下，我和可能许多其他人希望看到的是：

所以我向 Claude 展示了 Kilian 的屏幕截图，并要求提供该剪辑中显示的[交互式版本](https://jonudell.info/fedi-bsky-interactive-cheatsheet/)。

## 创建初稿

这是最初的提示：

Claude responded with a hosted artifact you can see live [here](https://claude.site/artifacts/a6e31cb1-ce17-4042-b79c-6b6afa27a0c7). Great start! This was indeed the essence of what I wanted; I could have shared the link and called it day. But of course when things happen this quickly and easily you can’t *not* want to embellish. For starters, the Claude artifact is React-based and I never want that unless necessary.

This time the generated artifact failed in the hosting environment provided by Claude, and a couple of turns of the crank didn’t resolve the problem. But that was OK, I now had a stand-alone HTML/CSS/JS construct that I could save, test and evolve locally, and easily publish to any vanilla web host. I created a [repo](https://github.com/judell/fedi-bsky-bridge-interactive-cheatsheet) for it and called it a day.

## 增强初稿

几天后，当我带着增强的想法回来时，我想首先要求 Claude 记录现有代码。正当我争论是上传 HTML 文件还是复制/粘贴它时，我注意到了新的 GitHub 集成。

You can now authorize Claude to see your repos, and then point it at the files you want to include in a chat session. Nice!

Here were the enhancements I had in mind:

**Dynamic validation.** As you type a handle, you should see the translation forming. When it becomes valid it should turn from gray to green.

**Copy button.** When it goes green, a copy button should appear.

**TLD validation.** Mastodon handles end with domains and shouldn’t go green unless those are valid top-level TLDs found on [this list](https://data.iana.org/TLD/tlds-alpha-by-domain.txt).

**Bridgy user page.** When you bridge a Mastodon or Bluesky account, the bridge creates a page where you can monitor the corresponding ghost account. The link to that page should form dynamically too and go green only when valid.
在进行这些增强功能时，我要求 Claude 证明它们有效，它通过实时生成可交互的工件来隔离这些更改，并使每个更改都可用于交互式测试。这让我对这些更改有了很大的信心，但现在我必须将它们集成到不断发展的工具中。

## 集成更改

受到 Claude 新获得的 GitHub 能力的鼓舞，这是我的下一个提示：

目前，这有点遥不可及。但是，问问总是没错的，对吧？我降低了我的期望，转而问：

Claude 立即提供了一个看起来完全合理的补丁文件，但实际上却完全坏掉了。这令人惊讶，因为这似乎是 [LLM 倾向于做得非常好的](https://thenewstack.io/choosing-when-to-use-or-not-use-llms-as-a-developer/)那种机械的、面向模式的转换。我们来回折腾了一段时间，但我始终无法让它生成一个可用的补丁。当我意识到它可能需要一个带有行号的源文件版本时，我提供了它——但仍然没有帮助。我将 ChatGPT 也加入了进来，但它也束手无策。我不确定为什么这个特殊的任务似乎难倒了最聪明的 LLM。是我提问的方式不对吗？这个任务有什么与常理相悖的地方吗？如果有人能解释它们失败的原因，我将洗耳恭听。

## 最后的清理和重构

抱怨这个限制感觉很荒谬。我想起了 Louis C.K. 关于飞机 WiFi 出问题的经典段子。（“这太糟糕了。”“伙计，你正坐在天空中的椅子上！”）尽管如此，将这些更改集成起来确实比最初生成它们花费了更多的时间。

一旦该工具的功能完善，就需要进行通常的重构和整合。我很清楚需要做什么，但是当我要求 Claude 和 ChatGPT 审查代码时，他们提出了一些我没有想到的改进，其中包括事件处理程序从两个不同的地方被冗余地调用。

同样，实际上集成这些改进比最初生成它们要困难得多。不过，一旦完成，Claude 就能够编写一个不错的[变更日志](https://github.com/judell/fedi-bsky-bridge-interactive-cheatsheet/blob/main/CHANGELOG.md)。

## 坐在天空中的椅子上

正如 Dan Goodin 指出的那样，我们需要为不可避免的平台转变做好准备。值得注意的是，这些工具使我能够构建和完善这个小而有用的工具，比其他任何方式都更快更容易。使 fediverse/Bluesky 更容易访问是朝着使我们自己免受企业所有者的突发奇想，并在我们的在线社区中建立更多韧性的方向迈出的一步。

这并不是一个完全顺利的体验，但我很感激 AI 的帮助，它简化了任务并丰富了结果。毕竟，我们正坐在天空中的椅子上。偶尔出现的补丁文件小故障似乎是微不足道的代价。

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)