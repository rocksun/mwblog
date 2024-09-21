# Deno 2 发布，提供长期支持和 npm 兼容性

![Deno 2 发布，提供长期支持和 npm 兼容性的特色图片](https://cdn.thenewstack.io/media/2022/08/caa9cb24-deno.jpg)

Ryan Dahl 在创建 Node.js 运行时时将 JavaScript 从 Web 浏览器中解放出来，然后又通过 Node 的包管理器 npm 进一步扩展了生态系统。之后出现了针对 JavaScript 和 TypeScript 的改进版 [Deno 运行时](https://thenewstack.io/denos-ryan-dahl-is-an-asynchronous-guy/)，随后将发布一个主要版本升级——Deno 2.0。

Deno 的产品营销经理 [Andy Jiang](https://www.linkedin.com/in/andyjiang/) 告诉我们，“我们计划在 10 月初发布”Deno 2 的正式版（希望如此）。Deno 的创建者 Ryan Dahl 一直在 [四个](https://topenddevs.com/podcasts/javascript-jabber/episodes/unpacking-deno-2-code-stability-free-speech-and-more-jsj-648#player1?catid=0&trackid=0) [不同](https://stackoverflow.blog/2024/08/20/ryan-dahl-deno-20-scale-improve-npm-nodejs/) [播客](https://podrocket.logrocket.com/deno-2-ryan-dahl)（以及一部简短的 [Honeypot 纪录片](https://www.youtube.com/watch?v=zxitJn9MwYs)）中预告即将到来的里程碑。
但 Dahl 不仅谈论了 Deno 运行时即将发生的重大变化，还谈论了它在 JavaScript 和 Web 本身更宏大的故事中的位置。

在 [“JavaScript Jabber” 播客](https://topenddevs.com/podcasts/javascript-jabber/episodes/unpacking-deno-2-code-stability-free-speech-and-more-jsj-648#player1?catid=0&trackid=0) 上，Dahl 強调，Deno 2 计划在 10 月初发布，旨在“确保它能够扩展到拥有 10 万行 JavaScript 代码的项目”。然后他列举了主要的新功能。“这包括 npm 支持、JavaScript 注册表、长期支持和工作区——所有这些都与 Deno 的扩展有关。”

Deno 2 的候选版本于 8 月底开始发布，大约在同一时间，Deno 的 CLI 团队负责人 Bartek Iwanczuk [发布](https://www.twitter.com/biwanczuk/status/1829311165001789538) 消息称，Deno 已经发布了最后一个 2.0 版本之前的版本。

## 导入 npm 模块

“在过去几年中，越来越明显的是，人们需要使用很多 npm 包，”Dahl 在 [Syntax 播客上的采访](https://www.youtube.com/watch?v=tZBCq8Ijkgw) 中说道。

因此，Deno 2 将支持导入 [npm 包](https://thenewstack.io/npm-to-adopt-sigstore-for-software-supply-chain-security/)。

Dahl 将其称为“一项非常庞大的任务……我们已经为此工作了大约两年了”。

但他还表示，他们已经达到了“大多数 npm 包在 Deno 中开箱即用。特别是框架……包括像 [Next.js](https://en.wikipedia.org/wiki/Next.js) 这样具有构建过程和各种功能的复杂框架。所以是的，一旦我们发布 Deno 2，你就可以在下一个项目中直接运行这些东西。”

虽然 Deno 使用 [基于 HTTP 的导入语句](https://deno.com/blog/http-imports)，但 Deno 2 带来了“能够使用指向 npm 模块的 URL 并将其拉取进来……”Dahl 在 [Stack Overflow 播客](https://stackoverflow.blog/2024/08/20/ryan-dahl-deno-20-scale-improve-npm-nodejs/) 上说道。

“因为事实证明，很多 JavaScript 生态系统严重依赖它，”他说。

![Arsenii Gorushkin 在 YouTube 评论中嘲笑 Deno 2](https://cdn.thenewstack.io/media/2024/09/93c15fe4-arsenii-gorushkin-mocks-deno-2-in-youtube-comment.png)

在 Deno 2 发布公告视频的评论中，后端 Web 开发人员 [Arsenii Gorushkin](https://github.com/agorushkin)（也是 Deno 的狂热爱好者）表达了一些怀疑。

在“JavaScript Jabber” 播客上，Dahl 強调，“npm 和 Deno 之间的兼容性水平非常出色”。

“总会有‘长尾’的不兼容性，我们认为任何无法运行的模块都是一个 bug，我们会修复它。但现在它真的非常棒。”

例如，Deno 甚至可以导入具有自己编译的扩展模块的 Node 模块。“它非常深入……基本上，你导入的任何东西都应该在 Deno 中开箱即用……

“我鼓励大家尝试一下。你会感到震惊的。”

6 月，Deno 还开始复制 npm 流行的 [工作区功能](https://docs.deno.com/runtime/fundamentals/workspaces/)，该功能允许开发人员在一个存储库中管理和同步多个相互依赖的包。“我们支持 npm 工作区以及我们自己的 npm 工作区形式，”Dahl 在 Syntax 播客上说道。
这也有助于开发人员更轻松地从 Node 转向 Deno。Dahl 在 [PodRocket 播客](https://podrocket.logrocket.com/deno-2-ryan-dahl) 中提到了工作区，以及 Deno 的整体性能。“如果你尝试一下，我保证你会对它的好用程度感到震惊。”

## 长期支持
Dahl 一再强调 Deno 已经成熟。

在 PodRocket 播客中，Dahl 还提到了 Deno 的长期支持，包括向后移植的安全修复和 API 稳定性承诺，称之为“帮助人们采用 Deno 并将其用于更多场景的另一种方式。因为如果没有稳定性保证，你就无法在某些企业环境中使用它。”

“我们一直在开发 Deno，”Dahl 在 Syntax 播客中说。“它现在很稳定，基本上，Deno 2 是我们 Deno 准备好投入生产、准备好用于各种用例的标志。”

## JavaScript 的未来
Dahl 承认 JavaScript 社区有一个 [长期提案](https://blog.logrocket.com/types-as-comments-strong-types-weakly-held/)，即使类型注释被 JavaScript 引擎忽略（有时称为“类型作为注释”），也要使其成为有效的 JavaScript 语法。Dahl 说，虽然该提案尚未完全形成，但他认为这是“JavaScript 将要发展的方向”——最终可能会在 Google 的 V8 JavaScript 引擎中得到支持。

“所以我认为五年后，Chrome 将原生执行 TypeScript，因为它可以在 V8 本身内部进行类型剥离。这将非常棒。”

但也许 Dahl 最简洁的声明是在 Syntax 播客中。“我只是有一个理论，认为 JavaScript 将长期存在，这不像是一件两年的事情，而是一件 20 年的事情，因为软件基础设施严重依赖于浏览器。所以我认为，我们必须从长远角度考虑我们在这个领域的发展方向……

“我们正在为未来构建 Deno。”

[YOUTUBE.COM/THENEWSTACK 科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)