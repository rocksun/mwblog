
<!--
title: JavaScript三十年：重塑Web的10大里程碑
cover: https://cdn.thenewstack.io/media/2025/07/3921dc37-javascript-1995-computerb.jpg
summary: 文章回顾了 JavaScript 30 年发展历程中的十个里程碑，包括其诞生、ECMAScript 标准化、Ajax 的出现、Node.js 的引入、npm 的扩展、ES6 的现代化、React 的组件革命、TypeScript 的突破以及 WebAssembly 和边缘计算的应用。文章也提到了 JavaScript 生态系统复杂性以及未来发展趋势。
-->

文章回顾了 JavaScript 30 年发展历程中的十个里程碑，包括其诞生、ECMAScript 标准化、Ajax 的出现、Node.js 的引入、npm 的扩展、ES6 的现代化、React 的组件革命、TypeScript 的突破以及 WebAssembly 和边缘计算的应用。文章也提到了 JavaScript 生态系统复杂性以及未来发展趋势。

> 译自：[30 Years of JavaScript: 10 Milestones That Changed the Web](https://thenewstack.io/30-years-of-javascript-10-milestones-that-changed-the-web/)
> 
> 作者：Richard MacManus

三十年前，Netscape 工程师 Brendan Eich 在[短短十天内](https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/)创造了一种新的客户端脚本语言，这已成为一段佳话。它最初被称为 Mocha，但在当年年底被重命名为 JavaScript。1995 年，没有人能够预测到 JavaScript 会成为[世界上最流行的编程语言](https://survey.stackoverflow.co/2024/technology#most-popular-technologies)。但事实正是如此。

JavaScript 是如何成为现代 Web 的定义性技术的？在本文中，我们将回顾 JavaScript 30 年历史中的十个里程碑时刻。令人惊叹的是，在这段时间内，JavaScript 生态系统（以及 Web 生态系统）的扩展和转变程度。

## **1. 1995：为 Web 增加互动性**

第一个关键时刻当然是 1995 年 5 月的那十天。当时的设想是创建一个与 Microsoft 的 Visual Basic 相对应的 Netscape 产品——一种对初级开发人员、网页设计师和 DIY 人士来说都很容易使用的 Web 语言。或者正如 Brendan Eich 后来自己所说的那样，“需要一种平易近人的语言，你可以直接将其放入网页中。”

从实际意义上讲，放入网页意味着使用脚本语言创建在 Netscape 浏览器中运行的客户端程序。JavaScript 这个名称在很大程度上是 Netscape 和 Sun Microsystem 的高管们提出的营销术语。但它也有一定的道理：JavaScript 将用于设计小的互动效果——例如表单验证或动画按钮——而 Java 将用于开发更复杂的 Web 组件。

[JavaScript 于 1995 年底公开发布](https://cybercultural.com/p/1995-the-birth-of-javascript/)，作为 Netscape Navigator 2.0 浏览器的 Beta 版本的一部分。

## **2. 1997：ECMAScript 1.0**

在 1996 年，早期的开发人员和网站管理员开始试验 JavaScript。起初，JavaScript 被用于相当琐碎的方式——滚动文本、愚蠢的动画、颜色技巧（渐变、彩虹效果等等）。Eich 后来自己将[这些类型的 JS 功能](https://cybercultural.com/p/1996-javascript-annoyances-and-meeting-the-dom/)称为“烦恼”。

但是到 1997 年，[JavaScript 已经成为一种复杂的语言](https://cybercultural.com/p/1997-javascript-apps-dynamic-web/)——Netscape 的 layers 等新功能为其功能增加了进一步的动态维度。此时，Microsoft 拥有[自己的 JS 版本](https://cybercultural.com/p/1996-microsoft-activates-the-internet-with-activex-jscript/)，称为 JScript；由于 JavaScript 是开源的，Microsoft 可以自由地复制和调整 JS 以适应其 Internet Explorer 浏览器。Netscape、Microsoft 和其他公司随后同意通过一个名为 Ecma International 的标准机构制定一个公正的规范。第一个 [ECMA-262 规范](https://ecma-international.org/wp-content/uploads/ECMA-262_1st_edition_june_1997.pdf)（昵称为 ECMAScript）于 1997 年 6 月发布，为 JavaScript 提供了一个中立的路线图。

## **3. 1999：XMLHttpRequest 首次亮相**

这是 JavaScript 真正开始变得有趣的地方——但奇怪的是，提供巨大技术飞跃的是 Microsoft，而不是 Netscape。

Internet Explorer 5 悄然引入了一种称为 XMLHttpRequest 的技术，允许脚本[在后台获取数据](https://medium.com/@mohamedtayee3/make-an-http-request-in-javascript-with-xmlhttprequest-xhr-e08f8c79a9d1)。它是一种 JavaScript 对象形式的 API，使用异步调用来使页面能够在不完全刷新的情况下进行更新。它是后来被称为 Ajax 的技术的种子。

负责这项技术的 Microsoft 工程师之一 Alex Hopmann [后来解释说](https://web.archive.org/web/20090130092236/http://www.alexhopmann.com/xmlhttp.htm)，他们创建该技术是为了在 Web 版本的 Outlook 中使用。当需要将 XMLHttpRequest 包含在 IE5 中时，它被作为 MSXML 库（Microsoft XML Core Services）的一部分添加。Hopmman 说，这就是名称中“XML”部分的由来——“实际上，它主要与 HTTP 有关，并且除了这是发布它的最简单的借口之外，与 XML 没有任何特定的联系，所以我需要将 XML 塞入名称中，”他写道。

与当时之前在 [JavaScript 编程](https://thenewstack.io/javascript/ "JavaScript programming") 中看到的任何其他技术相比，XMLHttpRequest 推动了 Web 浏览器从文档查看器发展到应用程序平台。

## **4. 2005：Web 2.0 中的 Ajax 和 jQuery**

在互联网泡沫破裂之后，浏览器创新萎缩了——这也意味着 JavaScript 方面也没有发生太多的创新（尽管要感谢 JSON——JavaScript 对象表示法——它是由 Douglas Crockford 在 2001 年发明的）。然而，[当 Web 2.0 在 2004 年左右开始时](https://cybercultural.com/p/003-the-first-web-20-conference-2004/)，情况再次好转。

值得注意的是，XMLHttpRequest 进行了品牌重塑。用户体验架构师 Jesse James Garrett 在 [2005 年 2 月 18 日](https://designftw.mit.edu/lectures/apis/ajax_adaptive_path.pdf) 创造了 Ajax 这个术语（它代表“异步 JavaScript 和 XML”）。一个月后，Google 地图展示了它的潜力。Ajax 可能成为最时髦的 Web 2.0 功能——尽管[闪亮的圆角](https://jonathannicol.com/blog/2006/10/21/the-visual-design-of-web-20/)也与它不相上下。

[2005 年 8 月](https://www.slideshare.net/slideshow/history-of-jquery/151586#4)，开发人员 John Resig 开始开发后来成为最流行的——[也是最持久的](https://thenewstack.io/why-outdated-jquery-is-still-the-dominant-javascript-library/)——JavaScript 库：[jQuery](https://en.wikipedia.org/wiki/JQuery)。当他在 2006 年 1 月发布它时，他将其宣传为“新浪潮 JavaScript”。基本上，它消除了 DOM 的怪癖，为开发人员提供了一个单一的、可链式调用的 API。

## **5. 2009：Node.js 逃离浏览器**

在 2009 年 5 月 27 日的 JSConf EU 大会上，Ryan Dahl [推出了 Node.js](https://www.youtube.com/watch?v=ztspvPYybIY)，将 Chrome 的 V8 引擎与事件循环服务器模型结合在一起。突然，JavaScript 可以处理后端以及 UI。

由于 Node.js，"JavaScript 无处不在 "的口号变得很普遍。分析公司 Redmonk 在 [2010 年 7 月的一篇博客文章](https://redmonk.com/cote/2010/07/29/makeall007/) 中使用了这个术语，并补充说 JavaScript 现在是 "云的通用语言"。当然，初创企业喜欢单一语言堆栈的概念；企业也很快采用了它。

这句话流行起来——"Run JavaScript Everywhere "目前醒目地印在 [该项目的首页](https://nodejs.org/en) 上。

## **6. 2014：npm 扩展**

随着 JavaScript 生态系统扩展到包括后端和前端，库和 JS 包的数量也随之增加。

Npm 创建于 2010 年，是 JavaScript 项目的注册表。到 2014 年 npm, Inc. 成立时，该注册表已实现商业化，模块数量从 2012 年初的 6,000 个猛增[到 50,000 个包](https://blog.npmjs.org/post/156076312840/search-update.html)。这得益于 npm 易于安装的命令，该命令鼓励超小型模块的文化。

npm 的兴起意味着开发人员从复制粘贴脚本转变为使用许多小型 JS 包来组成应用程序。这使得代码重用更容易，尽管它也增加了依赖链中的安全性和可靠性风险。

## **7. 2015：ES6 使语言现代化**

期待已久的 [ECMAScript 2015 (ES6)](https://ecma-international.org/wp-content/uploads/ECMA-262_6th_edition_june_2015.pdf) 使 JavaScript 与现代编程品味保持一致。事实上，[官方规范](https://262.ecma-international.org/6.0/index.html#sec-scope) 承认 JavaScript 现在是一种 "功能齐全的通用编程语言"。规范是这样描述的：

"ECMAScript 的使用已经超越了简单的脚本编写，现在它被用于许多不同环境和规模的全方位编程任务。随着 ECMAScript 的使用范围扩大，它提供的特性和功能也随之增加。"

正如 The New Stack 的 Mary Branscombe [去年所说的那样](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/)，ECMAScript 2015 不仅是对该语言有史以来最大的更新，而且还增加了 "一个可靠的年度更新流程，带来了一系列或大或小的改进"。

## **8. 2016：React 和组件革命**

在 Stack Overflow 的 [2016 年开发者调查](https://survey.stackoverflow.co/2016) 中，React 被列为当年最 "热门的技术"（前一年，报告中甚至没有提到 React）。

毫无疑问，[React 是 JavaScript 开发的一场革命性变革](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)。当它最初在 2013 年由 Facebook 发布时，它为开发人员提供了两个 DOM 的 "虚拟" 副本（每次交互的前后副本），然后你可以从中运行一个 "差异" 过程来确定到底发生了什么变化。然后，React 将这些更改应用于实际的 DOM——这意味着只更改了 DOM 的一部分，其余部分保持不变。反过来，这意味着只需要为最终用户重新渲染网页的一部分。Facebook 开发人员 Christopher Chedeau 将 React 比作 "DOM 的版本控制"。

React 背后的另一个重要概念是，它不是基于模板的，就像以前流行的框架（如 Ruby on Rails 和 Django）一样。正如 Facebook 的 Pete Hunt 在 2013 年所说的那样，"React 通过将用户界面分解为组件，以不同的方式构建用户界面 [这意味着 React 使用一种真正的、功能齐全的编程语言来渲染视图]。"

到 2016 年，React 已经全面展开，但也开始吸引批评者——他们的主要抱怨是 React 应用程序或页面因 JavaScript 代码而臃肿、速度太慢以及过于复杂（尤其是在状态管理方面）。

## **9. 2019：TypeScript 突破**

RedMonk 的 [2019 年 6 月语言排名](https://redmonk.com/sogrady/2019/07/18/language-rankings-6-19/) 将 TypeScript 排在第十位——这是五年来首次有新语言进入前 10 名，也是 TypeScript 首次进入前 10 名。

[TypeScript](https://thenewstack.io/what-is-typescript/)（JavaScript 的超集）带来了静态类型、IDE 自动完成、重构友好的工具等等。这些特性帮助大型企业团队相信 JavaScript 可以扩展到数百万行代码。

从 2019 年开始，TypeScript 越来越受欢迎的部分原因是它得到了主要 JavaScript 框架的支持。TypeScript 与 React 无缝集成，它是 Angular 的主要语言，并且与 [Vue.js](http://vue.js) 集成。此外，它还受到服务器端 JS 平台（如 Deno（一直支持 TypeScript））和 [Node.js](http://node.js)（今年 [3 月份添加了对它的支持](https://thenewstack.io/denos-response-to-nodes-recent-support-for-typescript/)）的支持。

在 Redmonk 最新的 [2025 年 1 月排名](https://redmonk.com/sogrady/2025/06/18/language-rankings-1-25/) 中，TypeScript 排名第 6 位。因此，它在 JS 生态系统中继续获得影响力。

## **10. 2022：WebAssembly 和边缘计算**

WebAssembly 在 [2019 年 12 月](https://www.w3.org/2019/12/pressrelease-wasm-rec.html.en) 成为 W3C 推荐标准，但开发人员的转折点发生在 Cloudflare 在 2022 年 9 月开源其 [workerd](https://blog.cloudflare.com/workerd-open-source-workers-runtime/) JavaScript/Wasm 运行时。现在，JavaScript 通常在全球各地的数据中心中与 Wasm 模块并行运行。

实际上，这意味着 JavaScript 现在正在网络边缘使用，并且通常与 WebAssembly 结合用于计算密集型任务——这或许是编程多语言未来的一个缩影（在单个项目中使用多种编程语言）。

你可能会问，WebAssembly 最初的目的是编译其他语言，以便开发人员可以通过 JavaScript 在浏览器中使用它们吗？确实如此，但这种情况正在发生变化。正如 Fastly 的 Guy Bedford 在 [2023 年 4 月](https://thenewstack.io/webassembly/will-javascript-become-the-most-popular-webassembly-language/) 告诉 Mary Branscombe 的那样，"WebAssembly 具有所有这些优势，这些优势适用于它可以部署的所有不同环境，因为它具有安全性、性能和可移植性。" 换句话说，Wasm 本身具有许多优势——尤其是在边缘计算方面——因此将 JavaScript 引入其生态系统对于某些项目来说是有价值的。

## **接下来是什么？**

在人工智能[可能使编程本身过时](https://thenewstack.io/coding-sucks-anyway-matt-welsh-on-the-end-of-programming/)的时代，JavaScript 还能持续 30 年吗？现在没有人可以回答这个问题，但我们确实知道，Web 开发社区开始反对[现代 JavaScript 生态系统的复杂性](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/)。正如我的同事 Alex T. Williams 在今天早些时候发表的一篇文章中所写的那样，React 尤其[受到了挑战](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/)。"现代浏览器功能更强大，开发人员更挑剔，而且这种把戏快要结束了，" 他指出。

因此，也许现在是 JavaScript 世界回归简单的时候了。无论如何，让我们庆祝 Web 的首要编程语言的三十年广泛创新。感谢 Brendan Eich 在 1995 年的 10 个忙碌的日子，并祝愿未来 30 年更美好！