# 加快现代 Web 应用程序速度的复古技术

![Featued image for: The Vintage Technology That Speeds Up Modern Web Apps](https://cdn.thenewstack.io/media/2025/01/86f71230-old-school-technology-for-web-development-1024x683.jpg)

Isaac Hagoel 处理过[商业应用程序中的诸多问题](https://dev.to/isaachagoel/are-sync-engines-the-future-of-web-applications-1bbi)，其中许多问题直到 Web 应用程序开始获得关注时才会显现出来。

他写道：“我注意到，开始开发新产品的开发团队通常会完全忽略这些问题，即使团队意识到了这些问题。“理由通常是’当我们真正开始遇到这些问题时，我们会处理它。’”

他继续说，忽略这些问题会使以后难以修复。

Hagoel 写道：“然后，团队会选择一些成熟的框架（选择你最喜欢的），认为这些工具肯定会为可能出现的任何常见问题提供解决方案。“几个月后，当应用程序达到一万活跃用户时，现实就会显现出来：团队必须引入局部的、零碎的解决方案，这些解决方案会增加复杂性，并使系统更加缓慢和充满错误，或者重写核心部分（在发布后没有人会这样做）。哎呦。”

Hagoel 写道，同步引擎可能是避免这些性能问题的关键。

他并不是唯一一个这么认为的人。The New Stack 越来越多地看到[同步引擎被提及为现代 Web 开发的工具](https://medium.com/@nile.bits/why-sync-engines-might-be-the-future-of-web-applications-41fdab1d650c)。

## 同步引擎：具有新应用的老技术

同步引擎并不新鲜。相反，根据 [Aaron Boodman](https://www.linkedin.com/in/aaron-boodman/) 的说法，同步引擎是一种古老的解决方案，他是一位软件工程师，曾帮助构建 [Google Chrome](https://thenewstack.io/google-genai-comes-to-chrome/)。他的整个职业生涯都在研究同步引擎。

他解释说，同步引擎是一种旨在同步多个设备或服务之间的数据的软件。Hagoel 称其为“前端和后端之间的持久缓冲区”。根据 Boodman 的说法，同步引擎可以用任何语言编写。

他说：“我通常以 Microsoft Outlook 为例，它使用同步编写，谁知道它有多老，像泥土一样古老，但实际上它甚至早于泥土。“计算机历史上最著名的 GUI 程序之一 Lotus Notes 也是一个基于同步的产品。”

“人们不断回归它的原因是，它可以制作真正高质量的用户界面。”

– Aaron Boodman, Rocicorp 首席执行官兼同步引擎开发人员

Boodman 现在是 [Rocicorp](https://rocicorp.dev/) 的首席执行官、创始人和合伙人，Rocicorp 是一个小型合伙企业，致力于构建高质量的开发者工具，包括 [Replicache](https://replicache.dev/) 和 [Zero](https://zero.rocicorp.dev/)，两者都是开源同步引擎。

Hagoel 表示，最近，[Linear](https://www.youtube.com/live/WxK11RsLqp4?t=2175s)、[Figma](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/) 和 [Trello](https://www.atlassian.com/blog/atlassian-engineering/sync-architecture) 都在使用同步引擎。

Boodman 说，[UI 开发人员](https://thenewstack.io/non-browser-ui-platform-for-ai-offers-grants-to-developers/) 多年来一直在摆弄同步引擎。
他说：“人们不断回归它的原因是，它可以制作真正高质量的用户界面。“当你从技术角度来看谁对同步感兴趣时，他们都是 [UI 人员](https://roadmap.sh/ux-design)。原因是 UI 开发人员的动力是让事情变得非常快。”

## 同步实现的 UX 改进

同步实现的 UX 改进包括：

- 它允许在用户点击 UI 中的内容时立即发生读取。当用户在 UI 中触发某些内容时，同步引擎会将数据移动到客户端，以便客户端可以立即显示数据；
- 它允许立即写入，因为您正在更改的数据是本地的；
- 这意味着没有进度条，因为同步一直在后台发生。

他说：“同步引擎非常有前途，而且长期以来一直很有前途，因为从核心上讲，它们可以使交互立即发生。”

对于使用同步引擎的 UI 开发人员来说，很多机制都消失了，因为同步引擎将其抽象化了。他补充说，这使 UI 开发更加有趣和令人满意，这就是开发人员经常回到同步引擎的原因。

## Web 应用程序同步：为什么是现在

Boodman 确定了同步引擎正成为加速前端的热门选择的几个原因，首先是大多数软件现在都是基于 Web 的。长期以来，Web 没有良好的存储原语，因此无法在 Web 客户端本地存储大量数据，这是同步所需要的，他补充说。
“实际上，这种情况在 10 多年前就开始发生变化，但当时可用的原语非常糟糕，开发人员花了很长时间才弄清楚如何使用它们并对其进行迭代，”他说。

另一个因素是，许多备受瞩目的应用程序因其高质量而受到开发人员的尊重，而这些应用程序是由同步引擎实现的，他说。

“其他开发人员也希望获得同样高质量的 UI，并且他们知道这是由同步引擎实现的，因此他们正在寻找某种方法来自己获得这些好处，”他说。

最后，Boodman 说，现在正在构建[新一代的同步引擎](https://gist.github.com/pesterhazy/3e039677f2e314cb77ffe3497ebca07b)。他的公司正在开发一种名为 [Zero](https://zero.rocicorp.dev/) 的新同步引擎，但还有其他新产品，包括 [Power Sync](https://www.powersync.com/)、[Electric SQL](https://electric-sql.com/)、[Convex](https://www.convex.dev/sync) 和 [Jazz Tools](https://jazz.tools/)。

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。