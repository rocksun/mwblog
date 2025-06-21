Web平台总是在不断发展和改进；对于Web开发者来说，不利之处在于需要了解哪些新功能可用以及何时可以使用它们。

[Interop](https://thenewstack.io/browser-vendors-aim-to-heal-developer-pain-with-interop-2022/) 是一个合理的指南，可以了解在未来几年内，哪些Web功能有望成熟到可以使用，但它只涵盖了浏览器领域中*每个人*都同意努力的方向。 新的[Safari 26 beta](https://developer.apple.com/videos/play/wwdc2025/233/) 增加了对锚点定位的支持：这是[Interop 2025](https://thenewstack.io/interop-unites-browser-makers-to-smooth-web-inconsistencies/) 列表中非常受欢迎的功能，也是[2024 State of CSS survey](https://2024.stateofcss.com/en-US/) 中“你还不能使用的CSS功能”问题中最常被要求的选项（相关的Popover API是[State of HTML 2024](https://2024.stateofhtml.com/en-US) 调查中的热门需求）。 但是，Safari 26 beta 还包括跨文档的视图转换：Interop 2025 中 View Transitions API 的工作重点是同一文档中的转换。

像这些调查这样的研究也表明，Web开发者往往[在使用新的CSS功能时非常保守](https://patrickbrosset.com/articles/2024-11-08-state-of-css-and-state-of-html-2024/)，可能是因为他们的用户使用多种浏览器，或者因为他们过去遇到过新功能的跨浏览器兼容性问题；但也因为当新功能不仅仅是发布，而且值得尝试时，不容易注意到。 同样，假设您使用框架或polyfill来采用浏览器中未广泛支持的新功能。 您如何知道何时可以删除通常是大量代码的内容，或者跳过转译器构建步骤，因为该功能现在可以原生使用了？

> 当新的Web功能不仅仅是发布，而且值得尝试时，不容易注意到。

Igalia 开发者倡导者 [Brian Kardell](https://www.linkedin.com/in/brian-kardell-08a4264/) 指出：“很久以前，你有一个浏览器策略：我们支持最新的浏览器两年，或者两个版本。 好吧，现在 Chrome 大概是四周一次，所以这已经不可能了！ 过去，这对于开发者来说是一件很好、很简单的事情，你可以说‘这是我需要学习的’。”

您可以查看 [CanIUse](https://caniuse.com/) 和 [CanIWebView](https://caniwebview.com/)，但您必须知道某个功能存在才能查找它。 始终可以查看发布说明、博客、来源试用、实验性功能测试、说明、路线图、计划的功能列表以及来自浏览器创建者的关于即将到来的标准的立场（Microsoft Edge 高级产品经理兼 [W3C Web Developer Experience (WebDX) Community Group](https://www.w3.org/community/webdx/) 联合主席 [Patrick Brosset](https://www.linkedin.com/in/patrickbrosset/) 维护着[这些和其他资源的便捷列表](https://patrickbrosset.com/lab/navigating-the-web-platform/)），但这需要了解很多。

Igalia 推出的便捷的 [BCD Watch](https://bcd-watch.igalia.com/) 每周都会更新 Browser Compatibility Data 项目中的更改，该项目是 MDN 的基础，但详细信息可能有点难以理解。

[Baseline project](https://thenewstack.io/what-does-it-mean-for-web-browsers-to-have-a-baseline/) 由 Google 启动，对开发者更加友好，它使用 WebDX CG 的定义——该定义创建了[Web平台功能的综合列表](https://web-platform-dx.github.io/web-features-explorer/features/)，其中包括规范、浏览器支持、使用情况和供应商意见——尝试对这些功能在核心浏览器集中是否可用且完整进行分类，从而更容易决定是否使用它们。

> “Baseline 项目旨在简化关于 Web 平台上存在哪些功能以及它们的可使用程度的相当复杂的信息。”
> **— James Graham, Mozilla Web 兼容性工程师**

Mozilla Web 兼容性工程师 [James Graham](https://hacks.mozilla.org/author/jgrahammozilla-com/) 解释说：“Baseline 项目旨在将关于 Web 平台上存在哪些功能以及它们的可使用程度的相当复杂的信息简化为一种更简单的形式，这样，如果你非常保守——比如你正在编写一个库——你可以问一个非常简单的‘是/否’问题，该问题涵盖了大多数用例。” “在大多数情况下，它消除了计算‘这是否可用？’的认知负担。”

以相对容易理解的格式提供关于谁在实现哪些 Web 标准的信息，也可能减少一些谨慎，因为它清楚地表明哪些功能得到广泛支持，并且可以安全使用。

Graham 说：“我们看到的一件事是，Web 开发者有时一直不愿使用在平台上运行良好的东西，而且在运行良好之后很长一段时间才使用，因为他们仍然认为这是一件新事物，所以它可能仍然很糟糕，或者它可能还没有真正普及。”

## 准备好使用

最初，[Baseline](https://web-platform-dx.github.io/web-features/) 是一个年度列表，其中列出了所有主要桌面浏览器（Chrome、Edge、Firefox 和 Safari）的最后两个版本中可用的所有功能，并且在 MDN 页面上标记了广泛支持的功能。

“开发者最关心的是 [浏览器] 引擎中的内容以及用户手中的内容，”Google 从事 Web 平台工作（包括 Interop 和 Baseline）的 [Kadir Topal](https://www.linkedin.com/in/kadirtopal/) 指出。

“我们希望使 Web 平台更加稳定，我们希望拥有一个更具互操作性的平台，与此同时，我们希望确保开发者实际上了解它：这就是 Baseline 所做的。 对于那些实际上在浏览器中可用的东西，它向开发者清楚地表明了这些东西是什么以及它们每年如何变化。 由于 Web 实际上没有任何版本发布，因此很难说从去年到今年发生了什么变化。 借助 Baseline，你可以说‘23 年与 24 年的 Baseline 有什么不同’，它可以告诉你发生了什么变化。 人们可以每年关注一次，并了解最近一年中发布的内容，就像某个时间点一样。”

但是开发者不仅关心某个功能是否具有互操作性，即它在所有主要浏览器中是否可用（这很容易跟踪），他们还想知道何时可以安全地在自己的网站上实现某个功能，而不必担心支持问题；这会因每个网站的地理位置和用户群而异。

> Safari 更新与底层操作系统的最新版本相关联，因此它们需要更长的时间才能达到与其他浏览器相同的使用率。

某些国家/地区的某些设备上的某些用户会在有新版本时立即更新其浏览器：Chrome、Edge 和 Firefox 更新通常会在[三个月内覆盖 95% 的用户](https://web.dev/case-studies/rumvision#browser_adoption_across_the_web)。 但是，Safari 更新与底层操作系统的最新版本相关联，因此它们需要大约 19 个月才能达到相同的使用率，并且某些更新甚至可能需要新设备。 有些开发者也愿意使用polyfill和回退，以便他们可以更快地使用新功能，而另一些开发者则希望等到他们的用户升级。

有时，一旦您听说某个新功能，它就会在至少一个浏览器中可用，但有时可能需要很长时间——就像新的JavaScript日期和时间支持[Temporal](https://thenewstack.io/the-new-javascript-features-coming-in-ecmascript-2023/)一样，它最终出现在Firefox nightly版本中。 如果Web开发者要充分利用浏览器中的所有新Web功能，他们需要一种方法来了解即将发生的事情，以及完全成熟并可以依赖的事情。

现在，Baseline 具有更高的粒度，Kardell 将其视为与“你需要加多少勺糖”相对应的“真实程度”。

## 增加更多粒度

Baseline Widely Available 会告诉您，Web平台功能何时成熟，可以在所有主流浏览器（包括移动版本）中使用，因为它已经存在了 30 个月，这有时间让用户更新到最新版本。

Kardell 说：“30 个月是基于对几年操作系统更新和周转以及事物发展方向的数据进行观察得出的。 两年半后，可能只有不到 5% 的人使用的东西比这更旧”——尽管他鼓励开发者继续为这些用户polyfill功能，因为他们可能最负担不起新设备或损坏的网站。

> “Baseline Widely Available 是开发者可以用来了解某个功能是否适用于其所有流量的最强大、最简单的信号。”
> **– Patrick Brosset, Microsoft Edge 高级产品经理**

开始试验的时间有点晚了：理想情况下，当大多数用户更新以获取该新功能时，开发者希望准备好重构其代码以使用它，而不仅仅是开始学习它。 Microsoft Edge 的 Brosset 指出：“Baseline Widely Available 是开发者可以用来了解某个功能是否适用于其所有流量的最强大、最简单的信号，但等待 Widely Available 也是最保守的选择。”

Mozilla 的 Graham 鼓励 Web 开发者对使用新功能更有信心，因为标准和测试使 Web 平台更加可靠。

Graham 解释说：“我们希望，一旦浏览器发布某个功能，那么限制因素就不是该功能不应该存在错误；限制因素是用户开始使用该浏览器的速度有多快。” “在所有浏览器中最初可用的东西到被认为是 Baseline Widely Available 之间的时间是关于注意用户获取最新版本。 十年前，这是一个截然不同的世界：那是 CSS hack 的世界，你必须了解所有这些用于解决不同浏览器错误的神秘解决方法。 现在这种情况少了很多！”

Baseline 现在可以帮助您做好准备。 尚未在所有四个核心浏览器（桌面和移动）中实现的功能都标记为 Limited Availability——这并不是一个不使用它们的信号，只是表明需要[更多工作](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)，无论是 polyfill 和转译器，还是渐进增强和对不受支持用户的回退。

一旦某个功能至少在所有 Baseline 浏览器的最新稳定版本中，它就被认为是 Baseline Newly Available；Brosset 称其为“Web 功能生命中的一件大事”。

> “一旦它在所有地方都实现了，您就应该意识到 [它] 发生了：这值得了解，值得在 Web 的晚间新闻中播出。”
> **– Brian Kardell, Igalia 开发者倡导者**

“这是某个功能真正成为 Web 平台一部分的时间点。 现在，该功能已在 Baseline 考虑的所有引擎中实现。 这一刻代表了开发者开始自信地使用新功能的绝佳时机，因为它们具有互操作性。 并非所有用户都使用每个浏览器的最新版本，因此 Widely Available 旨在提供更有力的保证，即某个功能几乎适用于网站的所有流量。”

Kardell 建议说：“您可以将其想象成一个具有不同准备程度的温度计”，因为实现某个功能的最后一个浏览器是一个有用的信号。 “一旦它在所有地方都实现了，您就应该意识到 [它] 发生了：这值得了解，值得在 Web 的晚间新闻中播出。 何时使用它取决于您，但即使它只是浏览器中的实验性功能，它也会到来，它是真实的。”

至少，这是开始了解新功能的好时机，因为您还可以清楚地了解达到 Baseline Widely Available 需要多长时间（假设没有发现任何实现问题）。 Widely Available 更多的是一个移动的目标，而不是年度总结：它承认网站需要时间来构建和更新，因此开发者会随着时间的推移重新评估哪些功能是合适的。

Kardell 建议每年二月发布的 Interop 公告标志着一个检查新功能的好时机。 “您应该将其视为一名开发者，因为它具有很高的信噪比：即使您之前尝试过 [某个功能] 并且效果不佳，现在也应该花点时间认真地看一下它。”

> “如果某个功能在 Interop 中，那么可以合理地预期它将在年底之前成为 Baseline Newly Available。”
> **— Graham, Mozilla**

Graham 也同意：“如果某个功能在 Interop 中，那么可以合理地预期它将在年底之前成为 Baseline Newly Available。”

Igalia Web 标准倡导者 [Eric Meyer](https://www.linkedin.com/in/meyerweb/) 预测：“希望到今年年底，锚点定位将成为 Baseline Newly Available，然后在 2028 年年中，它将只是 Baseline。”

从任何浏览器中的首次实现到覆盖所有四个核心浏览器的进展变化更大。 WebDX CG 联合主席 [Francois Daoust](https://www.linkedin.com/in/francois-daoust-66668b41/) 创建了 [Web平台基线的时间表](https://web-platform-dx.github.io/web-features-explorer/timeline/)（时间比 Baseline 项目存在的时间长得多，但使用相同的原则），有些功能花费了长达 240 个月的时间。 有趣的是，在 2023 年和 2024 年需要最长时间才能达到 Baseline Newly Available 的功能证明了 Interop 正在改善互操作性的方式。

HTML [summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary) element 细节元素最初于 2010 年实现：WebKit 实现于 2019 年推出，Edge 直到 2020 年切换到 Chromium 引擎才支持它。 同样，Kardell 描述为“可能需要十年才能完成”的 [ariaDetailsElements](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaDetailsElements) 属性最近已成为 Baseline Newly Available。 “有很多方法可以达到 Baseline。 这是一个连续的过程：很多事情需要更长的时间，但最终仍然会达到。 很多事情都在到达，爬行和气喘吁吁，但它们仍然会到达。”

## 广泛引用

Baseline 并非旨在成为您应该和不应该使用哪些功能的最终答案：但它的目的是让开发者更容易自己回答这个问题。

Brosset 指出：“早期采用通过在实施者和用户之间创建健康的反馈循环来帮助推动 Web 的发展，而公开 Newly Available 的功能有助于开发者在功能进入广泛采用阶段时接受这些功能。” “开发者最清楚访问其网站的设备、浏览器和版本的组合，并且在许多情况下，他们可能希望在早期阶段开始部署或试验功能，例如在将它们用作渐进增强时。 我们正在看到证据表明，Baseline Newly Available 正在帮助填补社区中的一个空白，即开发者难以跟上快速的变化步伐。”

有帮助的是，现在可以在更多地方获得信息：它位于 MDN 开发者文档、[CSS-Tricks](https://css-tricks.com/)、CanIUse 和 CanIWebView 中，以及在 WebDX [Web 平台功能资源管理器](https://web-platform-dx.github.io/web-features-explorer/)、Google 的 [Web Platform Status](https://webstatus.dev/)（其中包含自 2020 年以来年度 Baseline 功能的列表）、Microsoft 编译的 [Edge 2024 Top Developer Needs](https://microsoftedge.github.io/TopDeveloperNeeds/) 以及 [Web Platform Features](https://web-features.lttr.cz/) 等独立网站上。 [State of HTML survey](https://2024.stateofhtml.com/en-US) 现在包含每个问题中提到的功能的 Baseline 状态，这应该是一种提高意识的好方法。

> “我们正在看到证据表明，Baseline Newly Available 正在帮助填补社区中的一个空白，即开发者难以跟上快速的变化步伐。”
> **– Brosset, Microsoft Edge**

有很多方法可以跟踪正在成为基线一部分的内容。 Google 的 Web.Dev 上有关于 Baseline 功能和新闻的[每月更新](https://web.dev/baseline#the-baseline-monthly-digest)，WebDX 功能资源管理器允许您查看[Limited Availability](https://web-platform-dx.github.io/web-features-explorer/limited-availability/)、[Newly Available](https://web-platform-dx.github.io/web-features-explorer/newly-available/) 或 [Widely Available](https://web-platform-dx.github.io/web-features-explorer/widely-available/) 的功能；[每月发布说明](https://web-platform-dx.github.io/web-features-explorer/release-notes/march-2025/) 涵盖了哪些功能达到了新的基线状态。 Google Web 性能开发团队的 [Rick Viscomi](https://www.linkedin.com/in/rviscomi/) 提供了一个[更简洁的时间表](https://rviscomi.github.io/timebase/)，其中列出了每个月获得 Baseline 状态的功能。

但也许更有用的是，Baseline 详细信息直接显示在工具中。 将鼠标悬停在 VS Code 中的 Web 功能（CSS 或 HTML）上，[悬停卡片会显示 Baseline 状态](https://web.dev/blog/baseline-vscode)；JetBrains 计划向 [WebStorm](https://www.jetbrains.com/webstorm/nextversion/) 添加类似的功能。

真正有用的是了解您的网站用户可以使用哪些 Baseline 功能。 您可以查看 Akamai 的 [RUM Insights](https://rumarchive.com/insights/#baseline)，以查看按国家/地区划分的实际用户测量结果，显示其浏览器支持哪些 Baseline 级别——或者，如果您有足够关于其浏览器使用情况的详细信息以了解哪个年度 Baseline 适合，您可以使用 [browserslist-config-baseline 包](https://www.npmjs.com/package/browserslist-config-baseline) 或 [bl2bl Baseline browserslist 模块](https://github.com/web-platform-dx/bl2bl) 在 Autoprefixer、Babel、PostCSS、webpack 和 Vite 等工具中[定位](https://web.dev/articles/use-baseline-with-browserslist)该 Baseline。 [向 ESLint 提供您的基线目标](https://github.com/GoogleChromeLabs/baseline-demos/tree/main/tooling/eslint)，如果您使用的功能比该基线新，它将发出警告（如果您需要比 CSS 更多的功能，则有一个 [html-eslint](https://github.com/yeonjuan/html-eslint) 插件）。 Stylelint 也有一个 [Baseline 插件](https://www.npmjs.com/package/stylelint-plugin-use-baseline)。

如果您使用 [Google Analytics](https://chrome.dev/google-analytics-baseline-checker/)、[Netlify](https://app.netlify.com/extensions/baseline) 或 [RUMvision](https://www.rumvision.com/help-center/monitoring/dashboard/baseline/)，您可以获得关于哪个 Baseline 目标最适合您的访问者的建议，因此您可以决定是否需要等待功能达到 Widely Available，或者更快地采用容器查询和弹出窗口等功能。

> 尽管 Baseline 很有用，但它并不能替代您自己判断要采用哪些功能。

尽管 Baseline 很有用，但它并不能替代您自己判断要采用哪些功能：仅仅因为您的 linter [警告](https://github.com/eslint/css/blob/main/docs/rules/use-baseline.md)您的代码中的某个功能不在您定位的 Baseline 中，并不意味着您不能使用它。 这只是意味着您可以更容易地判断您的用户可以使用哪些功能，以及哪些功能需要更多的工作和测试才能支持。

Brosset 同意：“我们看到开发者对 Baseline 的认知度增长非常迅速。 这个词本身正在填补开发者一直在谈论平台的方式上的一个空白。 这是一个令人放心的标志，可以帮助他们更快地做出决定。 我们在博客、社交媒体和会议演讲中越来越多地看到对 Baseline 的提及。 Baseline 正在为开发者提供一种谈论 Web 平台的新方式，这似乎与他们产生了很好的共鸣。”