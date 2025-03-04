
<!--
title: Curl的Daniel Stenberg关于保护18万行C代码
cover: https://cdn.thenewstack.io/media/2025/02/c5fdc519-screenshot-from-fosdem-2025-talk-by-curl-maintainer-daniel-stenberg-laughing-1.png
-->

> 译自：[Curl's Daniel Stenberg on Securing 180,000 Lines of C Code](https://thenewstack.io/curls-daniel-stenberg-on-securing-180000-lines-of-c-code/)
> 
> 作者：David Cassel

志愿者团队已裁剪不必要的函数，开发了一套CI折磨测试套件，并获得了CVE编号权限。但他们拒绝用Rust重写项目。

在今年的年度开源会议 [FOSDEM](https://fosdem.org/2025/) 上的 [演讲](https://www.youtube.com/watch?v=Yr5fPxZvhOw)中，Curl 创建者 [Daniel Stenberg](https://daniel.haxx.se) 向听众承诺将展示“在拥有 200 亿次安装量的 C 代码的同时，如何安心入睡的方法”。

Stenberg 认为 200 亿实际上是对 [Curl 安装数量](https://thenewstack.io/the-creator-of-curl-remembers-23-wildly-successful-years/) 的 [低估](https://thenewstack.io/youre-addicted-to-curl-you-just-didnt-know-it/)。但这无疑给他创建的 [开源数据传输工具](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/) 带来了“一些责任”。

“但当然，我们是用最安全的语言编写的，”他笑着说——因为 Curl 是用 [C 编程语言](https://thenewstack.io/introduction-to-c-programming-language/) 编写的……

他的演讲引人入胜，内容丰富，最终令人放心。

但它也提供了一个鼓舞人心的例子，说明一个项目如何致力于更高的安全级别，以及当风险异常高时，这种承诺如何转化为执行……

## 不仅仅是周末项目

在演讲结束时，Stenberg 放出了一张滑稽的幻灯片，模仿 O’Reilly 书籍封面，“用 Rust 重写 Curl。一个周末项目。”（书籍封面上方添加了标语“告诉别人而不是自己动手”。）

“这是一本非常受欢迎的书，”Stenberg 说，同时尖锐地补充道，“没有人真正完成它。”

Curl 包含 18 万行 C 代码。Stenberg 告诉他的听众，这相当于小说《战争与和平》长度的 1.14 倍，并将其描述为“实际上相当多的代码……就其本身而言。它传输数据。”所以他强调说：“我们 [不会用 Rust](https://thenewstack.io/rust-integration-in-linux-kernel-faces-challenges-but-shows-progress/) 重写 Curl。任何语言都不行——我们根本不会重写它。它已经存在了。”Stenberg 承认 Rust “可能是一种很棒的语言”，并表示第三方依赖项仍然可以用 Rust 编写，他预测 Curl 项目未来会有更多这样的依赖项。

但 Curl 的当前代码库仍然是用 C 编写的，“我们只是耐心地迭代和改进。不会有任何重写。”

因此，演讲提供了他们为保持 [Curl](https://curl.se/) 安全所做的其他一切工作的示例……

首先，虽然他们使用 C 编码，但 Stenberg 说他们已经禁止了一堆“不受欢迎的函数”，这些函数很容易被错误使用。有人在演讲结束时要求举例——Stenberg 从 `gets()` 开始（一位 Stack Overflow 的评论者将其称为 [“创建缓冲区溢出的魔鬼工具”](https://stackoverflow.com/questions/4344776/student-info-file-handling#comment4725926_4345431)），以及 `scanf()`、`strcpy()` 和 `sprintf()`。

“你的经验有多丰富其实并不重要——C 标准中的一些函数真的不建议在代码中使用。我们使用工具检查它们，禁止它们，这样你就不会因为疏忽而偷偷使用它们。”

## 测试，测试……

还有一个特殊的“折磨测试”，它在一个自定义调试版本中进行，其中每个可能导致内存分配失败的函数（如 `malloc` 或 `calloc`）都有一个包装器，允许他们调用该函数——并不断调用它直到它失败。“它应该很好地失败——没有内存泄漏，没有崩溃，只是以错误代码退出，”Stenberg 解释道。“这真的是测试退出路径的一种很棒的方法，并确保我们在退出时始终释放和清理资源。”

开发团队并不总是测试所有这些。他笑着说，“这不是一个快速的过程，”——所以他们有一个系统可以随机测试较小的子集。Stenberg 说他们还在使用 [持续集成](https://thenewstack.io/ci-cd/)——这最终会为每个拉取请求和提交运行超过 40 万次测试。“就在一年前，我认为这需要几个小时，”他回忆道——但他们后来对其进行了优化，现在可以在 30 分钟内运行。“让它们快速完成真的很方便，这样我们就能立即知道最新更改的状态。”

你可能听说过“CPU 秒”这个词——服务器级 CPU 全功率使用一秒钟——86400 个 CPU 秒加起来就是一个完整的 CPU 天。Stenberg 说，平均而言，“我们现在每天只在 CI 上花费大约 10 个 CPU 天。”

为维护整个项目的安全性，Stenberg 说还有各种各样的其他测试——甚至还有一个测试“代码风格是否正确，以及代码中的缩进和拼写”。还有一个 CI 作业来确保他们没有任何二进制 Blob。（尽管 Stenberg 说：“无论如何，都不应该有任何方法可以在我们的存储库中隐藏任何加密的有效负载，”因为他们的大多数提交者已经在使用数字加密签名。）

有单元测试、库测试、工具测试，“当然，我们还有分析器一直在检查代码”——静态和动态分析器。Curl 也是 Google 的 [OSS-Fuzz](https://github.com/google/oss-fuzz) 项目的一部分。（正如 Stenberg 所描述的，“他们不断地在 Google 的硬件上对 Curl 进行模糊测试……”）

“我们想要确保所有这 200 亿个安装都能正常运行。”

## 修复——并发现——漏洞

在漏洞方面，“我们尽快修复它们，我们应该向发行版发出警报，并且我们非常非常彻底地记录所有内容，”Stenberg 说，包括一个 JSON 格式的 Curl 受影响版本的列表。该信息也在 Curl 的网站上提供。Curl 程序现在也是官方的 CVE 编号机构，“这样我们就可以更好地管理我们自己的 CVE”。

Stenberg 说，他们非常重视发现漏洞，并补充道：“我们进行了多次审计。”

Stenberg 回忆说，他们 2016 年的第一次审计“导致了七个 CVE”，而 2022 年的一次审计又导致了两个 CVE。但他为 2024 年一次范围更窄的审计没有发现任何 CVE 而感到自豪——这是一个令人鼓舞的趋势。审计是一项庞大而昂贵的任务。“有人将花费大量时间查看代码……对于小型开源项目来说，这并非易事。你必须有人拥有雄厚的财力，突然想要这件事发生。”

然而，他还指出，审计的成本仍然“多年来远远超过我们的整个[漏洞赏金计划](https://curl.se/docs/bugbounty.html)”——即使漏洞赏金计划最终发现了更多 CVE。

该漏洞赏金计划是与[HackerOne](https://www.hackerone.com/) 和[Internet Bug Bounty](https://www.hackerone.com/internet-bug-bounty) 计划联合运行的。Stenberg 说，自从他们近六年前（2019 年 4 月）启动该计划以来，他们已经支付了超过 85,000 美元——并且 500 个报告中的 76% 导致了 CVE（超过 15%——而另外 19% 导致了非 CVE 级别的错误修复）。“并非所有其他内容都是垃圾，”Stenberg 说，“但也有一些……我们总是事后披露所有内容，以便您可以关注讨论……”

尽管“漏洞赏金”幻灯片的最后要点只是说“AI 垃圾正在增加”。

Stenberg 说：“实际上，现在我们有效的报告数量与‘AI 垃圾’报告的数量大致相同”——大约 10% 到 15% 的提交！

## 一切皆安全
该项目致力于顶级安全性，并且这种承诺似乎渗透到各个层面。

- 所有提交都经过仔细审查——由人和机器审查。Stenberg 说：“我们现在有非常严格的代码风格，”这使得整个 180,000 行代码库看起来像是由单个作者编写的（这种一致性使其更易于阅读和调试）。
- “我们有很多关于源代码和内部 API 等方面的文档。”稍后 Stenberg 解释说，甚至还有文档检查工具，而不仅仅是拼写和语法。“例如，我们试图避免在我们编写的文档的英语中使用缩写。因此，‘isn’t’ 在文档中是不允许的……诸如此类……”
- 项目的开发团队都使用双因素身份验证来访问其 GitHub 托管的源代码……
GitHub 为他们提供了额外的测试资源，这最终引发了关于其他开源项目是否应该从一开始就采用最严格的安全性的[Mastodon 上的有趣讨论](https://mastodon.social/@bagder/113910838011988132)。

Stenberg 回复说：“我认为大多数开源项目都是从小而‘简单’开始的，”并补充说，“在甚至不知道项目是否成功的情况下，从一开始就将所有事情都做好并严格执行可能不是最佳优先级。我认为很少有项目这样做……在 Curl 项目中，我们开始时几乎每个螺栓都很松……”

在随后的讨论中，Curl 开发者 [Stefan Eissing](https://eissing.org/) 开玩笑说，有时候风险感觉非常高。“我们有‘如果你搞砸了，几个星球上的文明都将终结’的 FOSS 项目。这不是运行文明的方式。”

Stenberg 似乎很感谢他们从 GitHub 获得的帮助——也许希望同样的支持能够惠及更多正在努力解决自身松动螺栓的开源软件存储库。
“环顾世界，许多项目仍然有一些地方需要改进……”
