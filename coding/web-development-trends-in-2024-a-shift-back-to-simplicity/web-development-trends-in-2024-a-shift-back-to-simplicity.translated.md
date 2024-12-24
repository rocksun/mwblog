# 2024年Web开发趋势：回归简洁

![2024年Web开发趋势：回归简洁的特色图片](https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1-1024x576.png)

过去一年，Web开发的特点是回归构建网站或Web应用程序的更简单方法。部分原因是对JavaScript框架（尤其是基于React的框架）日益增长的复杂性的反应。像Astro和Eleventy这样的更简单的选项在2024年变得越来越流行，导致一些人（好吧，至少是我）认为我们正在接近后React时代。

当然，并非每个Web开发者都愿意放弃React——而2024年关于Web组件的大讨论充分证明了这一点。

简化开发也是AI集成到开发工具的副产品，这使得即使是经验不足的开发者也能轻松应对复杂的编码问题。也就是说，AI也有其自身的问题——特别是Web发布者和运营商在今年遭受了AI接管的困扰。

因此，让我们深入探讨一下2024年的五个Web开发趋势。

## 1. 更简洁的Web框架兴起

1月份，Netlify首席执行官在TheJam.dev大会上告诉与会者，Jamstack需要[减少复杂性，再次变得简单](https://thenewstack.io/keep-it-simple-frameworks-netlify-ceo-praises-astro-remix/)。他表示，Jamstack工具和流程在过去几年变得更加复杂。他指出，当混合架构开始渗透到Jamstack时，这一点变得显而易见——当存在客户端和服务器端编程的混合时。

谈到了“走向简洁的两条路径”。第一条路径是他所谓的“预烘焙Jamstack”，这意味着使用构建工具将内容发送到CDN（内容分发网络）。这基本上是Jamstack最初的愿景，在混合方法接管之前。根据的说法，第二条走向简洁的路径是“拥抱服务器端渲染”（SSR）。他推荐Astro和[Remix](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/)作为简化开发的两个优秀框架。

Astro无疑是今年最流行的Web框架之一。[其最突出的特点之一](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/)是它不像其他流行框架那样使用大量的JavaScript。它具有“默认情况下零JS”——这意味着Astro组件不会在客户端渲染，而是“在构建时或按需使用服务器端渲染（SSR）渲染到HTML”。

Astro提供了一种[“回归基础”的Web开发方法](https://thenewstack.io/how-astro-and-its-server-islands-compare-to-react-frameworks/)，让人想起早期的Web 2.0框架，如Ruby on Rails和Django，它们也是服务器端渲染的。

需要注意的是，Astro最初是一个静态网站生成器（SSG），但现在已经超越了这一点。但是对于大多数网站或Web应用程序来说，一个SSG——例如[Eleventy](https://thenewstack.io/static-sites-do-scale-eleventy-vs-next-js-at-11ty-event/)或[Nue](https://thenewstack.io/nue-a-new-static-site-generator-taking-on-next-js/)——已经足够了。

还值得一提的是[Vue作为另一个不错的选择](https://thenewstack.io/want-out-of-react-complexity-try-vues-progressive-framework/)。与Astro一样，它并没有试图将所有内容都塞进JavaScript——尽管如果您需要，高级JavaScript也是可用的。这种[简单优先的Web开发方法](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/)正在获得越来越多的关注，我预计这种趋势将在2025年继续下去。

## 2. 后React时代

2024年恰逢React十周年。在7月份的一篇文章中，我回顾了React的传承及其在Web开发领域中的现状。我得出结论，尽管它有巧妙的创新——特别是它的“虚拟DOM”方法——但它已经变得过于复杂。

我使用术语“[后React](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)”多少有些戏谑的意味，因为React——以及Next.js等相关框架——仍然非常流行。但是，有一种感觉是，开发人员现在可以选择可行的替代方法。上面提到的Astro和Svelte都没有使用虚拟DOM方法，因此开发人员现在可以选择不依赖React的Web框架（尽管Astro仍然可以选择React）。
此外，较新的React特性，例如React服务器组件，已[在Web社区中引发大量争论](https://thenewstack.io/frontend-schism-will-react-server-components-destroy-react/)。Angular框架的创建者之一，现任Cloudflare工程高级总监的Igor Minar甚至断言：“对我来说很清楚的一点是，React服务器组件将会摧毁React。”


## 3. Web组件的爱与恨
一些工程团队正在放弃React，并开始使用更多原生Web方法。“HTML优先”方法就是Microsoft Edge浏览器团队正在采用的方法，微软工程师Alex Russell将其描述为“现代Web组件+HTML优先架构”。

五月底，[微软发布了WebUI 2.0](https://thenewstack.io/from-react-to-html-first-microsoft-edge-debuts-webui-2-0/)，“这是一种全新的标记优先架构，它最大限度地减少了代码包的大小以及UI初始化路径中运行的JavaScript代码量。”

更少的JavaScript意味着更小的占用空间，这转化为用户更快的Web体验。其他[规模较小的开发团队也采用了类似的方法](https://thenewstack.io/pivoting-from-react-to-native-dom-apis-a-real-world-example/)。六月，我采访了一家名为Eukleia的瑞士IT公司的高级开发人员，该公司正在构建一个名为Mindsapp的定制开发工具。该公司通过从React迁移到现代Web技术（包括Web组件）简化了其应用程序，从而大大缩短了用户的加载时间。

这一切都很好，但是[许多开发人员不喜欢使用Web组件](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/)。十月，SolidJS JavaScript框架的创建者Ryan Carniato发表了一篇博文，标题具有挑衅性，[《Web组件并非未来》](https://dev.to/ryansolid/web-components-are-not-the-future-48bh) 。基本上，他的论点是，像SolidJS这样的框架在某些情况下能够比Web组件做得更多，并且更容易实现。他将Web组件斥为“彻头彻尾的妥协”。

针对Carniato的观点，[Shoelace](https://thenewstack.io/shoelace-web-components-library-that-works-with-any-framework/)的创建者Cory LaViska认为[Web组件提供了稳定性和互操作性](https://www.abeautifulsite.net/posts/web-components-are-not-the-future-they-re-the-present/)。LaViska还指出，Web组件并非执行框架组件的所有功能，“因为它们是互操作元素的较低级别实现”。

像往常一样，社交媒体战场上并没有改变任何人的想法。


## 4. 无处不在的AI
如果不提及生成式AI几乎压倒一切的影响，那么对2024年科技的回顾就不完整。

今年对于开发人员来说，AI被集成到开发人员的核心工具（IDE）中，而创建“AI代理”的新技术则出现在LangChain和LlamaIndex等辅助工具中。可用的大型语言模型类型也变得更加多样化，小型模型和本地开发能力尤其受到开发人员的关注。

AI辅助编码今年对开发人员的影响最大。“这是我在软件工程整个职业生涯中看到发展速度最快的领域之一，”SingleStore的[Madhukar Kumar](https://www.linkedin.com/in/madhukarkumar/)最近告诉The New Stack。“我们看到新的工具、IDE和全栈开发平台取代了几个月前很流行的IDE（例如GitHub Copilot）。对于开发人员来说，最大的挑战将是如何跟上这些变化，并不断调整他们的工作流程以适应他们的经验水平和他们正在构建的内容，而不会产生‘新IDE疲劳症’。”

请参阅我上周的年度总结，以[更深入地了解2024年的AI工程趋势](https://thenewstack.io/top-5-ai-engineering-trends-of-2024/)。


## 5. Web发布的虚无主义
对于Web发布者和运营商来说，这是特别压力重重的一年，他们不仅要应对AI的侵蚀，还要应对全球最大的开源Web发布社区的一场重大风波。当WordPress的共同创建者Matt Mullenweg和WordPress供应商WP Engine[发生法律纠纷](https://thenewstack.io/the-wordpress-saga-does-matt-mullenwegg-wants-a-fork-or-not/)时，这促使许多运营商[寻找WordPress的替代方案](https://thenewstack.io/wordpress-alternatives-stick-with-php-or-pivot-to-javascript/)。
到年底，谷歌AI概述（AIO）——谷歌的AI引擎试图在搜索结果页面顶部回答您的查询——已在100多个国家/地区上线。然而，评估其影响仍然很困难。您的网站在AIO中出现的频率如何？您的引用链接在AIO中被点击了多少次？SEO公司BrightEdge的Jim Yu告诉我们[AIO就像“增强版的零点击快速答案”]——这意味着人们并不一定会点击引用链接。他说，AIO可能会降低点击率，因为它的AI摘要旨在直接回答查询。


Drupal创建者Dries Buytaert在另一个TNS采访中[为出版商提供了一些希望]。“你必须提供超越ChatGPT所能提供的价值，这样人们仍然有动力访问你的网站，”他在二月份说道。“那么你该如何做到呢？通过提供更好的内容——更好的内容可能是个性化内容，或者……也可能是更多内容放在……不一定是付费墙后面，而是门槛后面。你知道，也许你需要注册才能获得内容。”


## 结论

网络开发中事情从来都不简单，但至少已经开始摆脱React的复杂性。让我们希望这种情况在2025年继续下去。与此同时，人工智能的进步和网络出版软件持续的动荡，预示着新的一年对许多网络从业者来说将是一个动荡的开始。

[YOUTUBE.COM/THENEWSTACK 科技发展日新月异，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)