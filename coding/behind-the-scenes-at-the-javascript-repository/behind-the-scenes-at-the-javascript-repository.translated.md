# JavaScript 注册中心幕后

![Featued image for: Behind the Scenes at the JavaScript Registry](https://cdn.thenewstack.io/media/2024/10/80113a3b-jsr-1024x683-1.jpg)

今天，我发现如果你将 JSR 徽标倒置（见上图）——它看起来完全一样

自 3 月份公开测试版发布以来，[JavaScript 注册中心](https://jsr.io/) (JSR) 一直在播客、博客文章和网络评论中为其好奇的开发者社区分享技巧、见解和普遍的善意。

“在 JSR 上发布的包作者很喜欢这种体验，”[Deno](https://thenewstack.io/deno-2-arrives-with-long-term-support-node-js-compatibility/) 的产品营销经理 [Andy Jiang](https://theorg.com/org/deno/org-chart/andy-jiang) 在接受 The New Stack 的电子邮件采访时表示。“JSR 在幕后处理了很多事情，因此作者可以发布 TypeScript 源代码，而无需进行转译或构建步骤。”

这个开源网站是雄心勃勃计划的一部分，旨在为 [JavaScript](https://thenewstack.io/JavaScript/)（以及 [TypeScript](https://thenewstack.io/TypeScript/)）构建一个更好的包存储库，支持类型声明文件等功能，并提供一种简单的方法来为包提供加密签名。是的，虽然它专注于 JavaScript（和 TypeScript），但 JSR 仅支持 ES 模块。在与 Stack Overflow 的 [春季采访](https://the-stack-overflow-podcast.simplecast.com/episodes/why-the-creator-of-nodejs-created-a-new-javascript-runtime/) 中，[Ryan Dahl](https://thenewstack.io/denos-ryan-dahl-is-an-asynchronous-guy/) 指出 [ECMAScript](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/) “现在已嵌入到所有 Web 浏览器中，是模块的真正方式。”或者，正如存储库的 [常见问题解答](https://jsr.io/docs/why) 所解释的那样，“ECMAScript 模块已成为标准。

## 现代注册中心

“现代注册中心应该以 TypeScript 为设计理念。”

但现代 JavaScript 仍然受欢迎。“虽然我们确实希望从一开始就为 TypeScript 设计，但你绝对可以愉快地在 JSR 上编写和发布纯 JavaScript 代码，”Deno 的开发者关系主管 [Kevin Whinnery](https://www.linkedin.com/in/kevinwhinnery/) 在 3 月份 [在 Hacker News 上](https://news.ycombinator.com/item?id=39563688) 发布。（Whinnery 当时补充说，“我们可能需要更好地解释和展示这一点”，而 JSR 的主页现在自豪地宣布它是一个“用于现代 JavaScript 和 TypeScript”的包注册中心。）

这一切都是持续推广工作的一部分，旨在让开发者熟悉有关新注册中心的许多细节——并希望鼓励他们尝试一下

## 默认安全

在 Deno 的博客上，一篇 [4 月份的文章](https://deno.com/blog/how-we-built-jsr) 题为“我们如何构建 JSR”，解释了该网站的一些内部细节，包括它“默认安全，支持来自 GitHub Actions 的无令牌发布以及使用 Sigstore 的包来源”。

一篇早期的 [3 月份博客文章](https://deno.com/blog/jsr_open_beta) 包含将 GitHub 存储库链接到 JSR 的说明。“以这种方式发布还可以让你的用户放心，他们项目中包含的工件确实是从 CI 上传的，并且有一个可供查看的来源透明度日志。”

正如 Dahl [在 Stack Overflow 的播客](https://thenewstack.io/ryan-dahl-from-node-js-and-deno-to-the-modern-jsr-registry/) 上在 3 月份所说，“归根结底，你将使用许多依赖项来构建你的微服务，然后将其作为 Docker 容器在某个 Kubernetes 基础设施中运行。而且能够说这个 Docker 容器中运行的所有软件都有证明，可以追溯到某个经过验证的用户，并且这里没有运行的代码是我们不知道来源的，这将非常棒。我们正在构建这个基础设施。”

4 月份的博客文章解释了他们不仅必须构建一种强大的方式来托管包，而且还必须接受和分析新的包以查找无效的依赖项或语法错误（并计算一个分数以显示包——并生成文档）。

## 云端

但这篇博客文章还包含了一些关于他们如何构建基础设施的有趣细节。大多数数据存储在 Postgres 集群中，通过 HTTP REST API 使用 JSON 访问。

API 服务器是用 [Rust](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/) 编写的，它与数据库并排位于 [Google Cloud Run](https://cloud.google.com/?utm_content=inline+mention) 上，在那里它还“执行身份验证和授权策略”，与 GitHub API 和 Sigstore 交谈。
在 Stack Overflow 的播客中，Ryan Dahl 強調 JSR “旨在能够在商品云软件上非常便宜地运行”。正如 [FAQ](https://jsr.io/docs/faq) 所说，“目前 JSR 的托管费用由 Deno 公司支付。未来，JSR 可能通过其他方式获得资金，例如赞助、捐赠或基金会。”

“我们预计 Deno 公司能够在可预见的未来继续支付 JSR 的托管费用——JSR 的设计非常便宜。”

正如 Dahl 在播客中所说，“我们正在努力为 JavaScript 的未来建立一个机构。”

“[T]here is no magic，”博客文章承认。“我们使用非常无聊、非常容易理解且非常可靠的云基础设施。”一个 Google Cloud L7 负载均衡器会将请求适当地路由到前端、API 服务器或托管源代码和 npm tarball 的 Google Cloud CDN 后端。“那么我们如何使模块服务变得可靠呢？我们将整个问题委托给 Google Cloud。与为 google.com 和 YouTube 提供服务的相同基础设施用于在 JSR 上托管模块……”

“只有当 Google 本身宕机时，JSR 才会宕机。但到那时——可能互联网的一半都宕机了，所以你甚至不会注意到。”

那篇 4 月份的博客文章还详细介绍了他们 Web 前端的具体细节。（因为“如果你正在编写一项供人类使用的服务，你会很快发现大多数人类实际上并不想使用 curl 手动调用 API。”）他们使用 Fresh（他们将其描述为“一个现代的‘服务器端渲染优先’ Web 框架）构建了它，通过“并行化”许多 API 调用以同时运行来仔细优化它以实现快速响应。

## 包是如何发布的
最终结果令人惊讶地高效。发布脚本将文件捆绑到一个 .tar.gz 文件中，触发 API 服务器执行自己的验证（例如检查 tarball 是否 [小于 20 兆字节](https://jsr.io/docs/quotas-and-limits#other-limits)）。根据博客文章，后台工作者在 99% 的这些 tarball 上不到 30 毫秒内开始运行，验证是否存在“name”、“version”和“exports”字段。对于大多数包，所有导入模块的存在也将在 10 毫秒内得到验证（以及 TypeScript 或 JavaScript 代码的有效性）。

然后使用自动生成的模块图使用 Rust 中的 TypeScript 语法分析来创建文档。

在服务的公开测试版期间，一篇 [3 月份的博客文章](https://deno.com/blog/jsr_open_beta) 向潜在用户解释说，“一旦你找到了合适的模块，安装和使用说明可以在每个页面顶部的模块自动生成的 API 参考文档中找到。”

在某个时刻，该服务甚至为 JSR 的 npm 兼容层生成一个 tarball，创建“node_modules/ 解析理解的导入”（通过将 TypeScript 源代码转换为 .js 文件和 .d.ts 声明文件），“以及一个 package.json”。

根据 Deno 开发者关系主管 [Kevin Whinnery](https://www.linkedin.com/in/kevinwhinnery/) 在 3 月份 [在 Hacker News](https://news.ycombinator.com/item?id=39561988) 上发表的评论，未来可能会有更多功能。“我们也一直在探索如何围绕同时将 JSR 模块发布到 npm 创建良好的开发者体验，以便发布者也可以控制他们在那里的命名空间。我们当然知道这是人们感兴趣的使用模式。”

然后，当然，Postgres 数据库会更新……

## 关于那个前端
一篇新的 [上周的博客文章](https://deno.com/blog/designing-jsr) 回顾了这一切的起源。在这篇文章中，产品设计主管 [John Donmoyer](http://linkedin.com/in/johndonmoyer) 指出，除了其他一切之外，JSR 是开源的。因此，除了注册表中添加的“数万个”包之外，“我们很高兴看到社区拥抱 JSR，来自 Deno 之外的 35 多位贡献者贡献了 240 多个额外贡献。”

5 月份，Deno 的标准库问世，为其提供了“自动生成的文档和 SemVer 重复数据消除”，根据 [另一篇博客文章](https://deno.com/blog/std-on-jsr)，“同时增强了全球开发者的可访问性和多功能性”。（虽然它在 deno.land/std 的原始位置“将无限期地可用。所有依赖 deno.land/std 的程序将继续工作。不用担心！”）

Deno 标准库包含 44 个模块，涵盖数据解析/操作、使用 Web 协议以及通用辅助函数，可能包含你所需的一切。

[https://t.co/9inNA4dMXe][https://t.co/CZybUAhr9a][pic.twitter.com/BFCeQbrsU0]— JSR (@jsr_io)

[2024 年 8 月 21 日]
Donmoyer 还讲述了 JSRF 标识设计的幕后故事——从他们采用 Chris Williams 的 [非官方 JavaScript 标识](https://github.com/voodootikigod/logo.js) 的黄色色调开始。但随后设计团队“开始玩弄‘块’的概念，以唤起一个由许多较小部分组成的系统”，最终形成了 JSR 的镜像文字——也就是说，一个旋转 180 度后仍然相同的标识。

博客文章中的图片还展示了他们考虑过的其他几个版本……“最终成为 JSR 官方标识的概念最初只是一个匆忙的草图，”Deno 前端工程师 [Josh Collinsworth](https://www.linkedin.com/in/joshcollinsworth/) 回忆道。“我当时尝试了很多想法，从我在设计学校期间完成的项目中汲取灵感……”

好奇 JSR 标识和网站设计是如何融合在一起的吗？🤔️

这里有一窥我们的设计过程。

[https://t.co/NoIeaOUFRn]— JSR (@jsr_io)

[2024 年 9 月 4 日]
但工程师开始将其用作占位符——最终，开始为其代言。“我最初不愿将其定为赢家，因为我仍然认为它只是一个快速的概念草图。但我们越是用它，它直截了当的简洁性就越让人感觉恰如其分。”

有趣的是，一件事是如何导致另一件事的。下一步是将网站其余部分的调色板与标识相匹配。最终，经常访问的访客意识到，他们的光标可以从页面背景中始终向上漂浮的小方块中画出线条（这要归功于令人愉快的开源库 [particles.js](https://vincentgarreau.com/particles.js/)）。最终结果“是一种有趣的视觉效果，它将 JSR 品牌和盒子主题联系在一起，并融入了有趣的小互动。”（它也具有很高的性能——加载不到 10 千字节，这将在页面其余部分加载后延迟加载。）

## 超越 npm
早在 JSR 处于公开测试阶段时，一篇 [3 月份的博客文章](https://deno.com/blog/jsr_open_beta) 承认了 npm 的 250 万个包“以及仅在过去 30 天内约 2500 亿次下载”，并表示这样的数字使其“可以说是世界上最成功的包注册中心。如果没有 JavaScript 社区共同构建的这个令人难以置信的生态系统，JavaScript 可能不会享有今天的这种地位。”

但随后它继续谈论 JSR 的价值主张。“我们认为，现在是重新构想包注册中心在 2024 年应该如何运作的时候了。”

因此，想法是创建一个 npm 的扩展——但具有更大的雄心。
在 [4 月份的一篇博客文章](https://deno.com/blog/jsr-is-not-another-package-manager) 中，Dahl 认为 JSR“不仅仅是生态系统中的另一个工具，而是我们如何看待 JavaScript 和 TypeScript 分发方式的根本转变……”

“JavaScript 是许多程序员的通用语言，使其既通用又易于访问。这种语言值得一个中心枢纽——一个城镇广场——让开发人员可以在没有过分复杂的情况下分享他们的工作。

“我们相信 JavaScript 将在未来几年内继续成为软件开发的核心，而 JSR 的目标是支持这种持久的重要性。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)