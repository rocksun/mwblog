<!--
title: 未来应用形态：Web、原生，抑或两者合璧？
cover: https://cdn.thenewstack.io/media/2025/08/f3a590c2-web_app_getty_images.jpg
summary: 开发者对App和PWA的争论激烈，调查显示用户更喜欢移动网站(PWA)。PWA易于更新，无需应用商店审核，且分析功能更强。专家建议App用于保留用户，PWA用于发现和吸引新用户。
-->

开发者对App和PWA的争论激烈，调查显示用户更喜欢移动网站(PWA)。PWA易于更新，无需应用商店审核，且分析功能更强。专家建议App用于保留用户，PWA用于发现和吸引新用户。

> 译自：[Your Next App: Web-Based App, Native or … Both?](https://thenewstack.io/your-next-app-web-based-app-native-or-both/)
> 
> 作者：Loraine Lawson

软件开发者 Ibrahim Diallo 有一个想法：不要下载 App，使用网站。

他发布了这条评论，并附上了[指向他的博客的链接](https://idiallo.com/blog/dont-download-apps)，在博客中他为自己的立场辩护，该评论在 [Hacker News](https://news.ycombinator.com/item?id=44689059) 上吸引了 700 多条评论，这表明这仍然是开发者们热议的话题。

但对于用户来说，这场争论可能没有意义：根据一家为托管、IT 和开发者社区提供教育和新闻内容的 Hosting Advice 公司所做的一项[调查](https://www.hostingadvice.com/studies/survey-mandatory-app-downloads/)，四分之三的用户更喜欢移动网站而不是专用 App。该调查询问了 1000 名 18 岁以上的美国成年人。

[![图表显示了用户为什么会下载移动 App 而不是使用网站。](https://cdn.thenewstack.io/media/2025/08/2c7d596f-chart_hosting_advice.png)](https://cdn.thenewstack.io/media/2025/08/2c7d596f-chart_hosting_advice.png)

图片由 Hosting Advice 提供。

原生 App 是专门为移动平台构建的，无论是 [Android](https://thenewstack.io/implement-behavior-driven-development-in-android-with-cucumber/) 还是 [iOS](https://thenewstack.io/new-small-ai-model-lets-developers-experiment-on-ios/)。 因此，原生 App 可以访问手机的工具，例如日历。 它们通常也通过平台商店分发，在那里它们会经过一个可能需要数周的审查过程。

相比之下，[PWA](https://thenewstack.io/its-time-to-build-a-progressive-web-app-heres-how/) 基本上是一个网站——有时会打包一个浏览器，以便[用户体验](https://thenewstack.io/measuring-user-experience-in-modern-applications-and-infrastructure/) 基本上像一个应用程序，但没有原生 App 的成本，例如开发时间和用户手机内存。 *（有关原生和 PWA 之间差异的更多信息，请参阅 Alexander T. Williams 5 月份的文章[何时使用渐进式 Web App，何时使用原生 App](https://thenewstack.io/when-to-use-progressive-web-apps-and-when-to-go-native/)。）*

渐进式 Web App (PWA) 不通过 Google Play 或 Apple App Store 分发，尽管 Apple 和 Google 最近已经可以 PWA 包装在原生外壳中，并将这些 App 提交到他们的商店。 如果你不需要进入 App Store，那么不进入 App Store 也有好处。 例如，开发者可以更轻松、更快速地进行更新，而无需经过耗时的 App 审查过程。

这就提出了一个问题：开发者应该在什么时候构建具有所有相关花里胡哨功能和占用手机空间的原生 App，又应该在什么时候选择 PWA？ 或者，正如一位分析师建议的那样，开发者是否应该两者都选择？

## PWA：简史

使用 Web 标准进行移动开发的想法已经存在一段时间了：早在 2007 年，Steve Jobs 就表示 iPhone 将运行[基于 Web 标准的应用程序](https://www.apple.com/newsroom/2007/06/11iPhone-to-Support-Third-Party-Web-2-0-Applications/)。 术语 [PWA 由设计师 Frances Berriman 和 Google Chrome 工程师 Alex Russell 在 2015 年创造](https://infrequently.org/2015/06/progressive-apps-escaping-tabs-without-losing-our-soul/)。 然后，Google 的 Chrome 团队开始推广 Android 开发的这个概念。

Chrome 的产品组经理 [Rob Kochman](https://www.linkedin.com/in/rkochman/) 告诉 *The New Stack*，Google 继续看到 Web App 的采用率不断提高，因为开发者和用户都意识到 Web 作为应用程序平台的优势：

*   跨操作系统的广泛覆盖
*   易于发现
*   即时更新
*   强大的安全性

“Web App 让用户可以选择在浏览器选项卡中或通过完全安装的体验进行交互，”Kochman 说道。 “虽然 Web 没有提供原生平台的每项功能，但对于许多 App 来说，它是一个绝佳的选择。”

## 重新审视 PWA

Kochman 说，如果你已经有几年没有考虑过 PWA，那么值得重新审视一下。

“最近没有关注过 [Web App](https://thenewstack.io/web-app-development-sans-javascript-with-microsoft-blazor/) 的开发者应该考虑一下强大的新 API，例如文件系统访问——更丰富的操作系统集成和性能改进，”他指出。

[![图表显示了选择原生的理由与选择 PWA 的理由。](https://cdn.thenewstack.io/media/2025/08/e77905a0-should_you_build_native_app_or_pwa.png)](https://cdn.thenewstack.io/media/2025/08/e77905a0-should_you_build_native_app_or_pwa.png)

图片由 Loraine Lawson 提供

Hosting Advice 的高级分析师 [Joe Warnimont](https://www.linkedin.com/in/joewarnimont/) 表示，公司经常推广 App，但大多数人喜欢 PWA 的便利性。

“我认为这是品牌与客户建立联系的理想选择，尤其是在第一次接触时，”Warnimont 说。 “如果客户只想查看你的菜单，但在看到任何内容、看到价格或菜单之类的东西之前，就遇到了‘下载我们的 App’这堵墙，那么这对任何人来说都是一个艰难的推销。”

尤其是因为 PWA 在模仿 App 的功能方面做得如此出色，他说。 例如，用户可以下载 PWA 并在他们的屏幕上获得一个图标，这使得区分两者变得更加困难（尽管这在 iOS 上仍然有些限制）。 PWA 通常在浏览器内部运行，但安装后，它可以在没有浏览器 UI 的独立窗口中启动。 开发者还可以将 Web 引擎（[Blink](https://www.chromium.org/blink/)、[Gecko](https://firefox-source-docs.mozilla.org/overview/gecko.html) 和 [WebKit](https://webkit.org/)) 嵌入到原生包装器中，以提供相同的体验，尽管这更接近于混合 App 而不是纯 PWA。

PWA 的另一个令人惊讶的好处是更好的分析。

“与网站或 App 相比，PWA 通常可以在用户行为方面为你提供更丰富的分析，因此你可以在不必浏览我们讨论过的复杂 App 世界的情况下，获得可能更多的用户参与度，并且不必依赖 Apple App Store 和 Google App Store 提供的分析，”Warnimont 说。

当然，你也可以采用混合方法并[同时构建两者](https://thenewstack.io/one-lets-frontend-devs-build-once-deploy-web-and-native-apps/)，因为 PWA 和原生 App 可以解决不同的业务用例。

“我认为 App 更适合用于保留，而 PWA 更适合用于发现、吸引客户并建立第一次接触点，”他说。