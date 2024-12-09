
<!--
title: 2025年该淘汰的5个JavaScript库
cover: https://cdn.thenewstack.io/media/2024/12/a80bcaae-getty-images-jpx9yr5rggw-unsplashb.jpg
-->

我们将重点介绍五个可能在2025年过时的JavaScript库，以及为什么现在是迁移的时候了。此外：我们还列出了替代方案！

> 译自 [5 JavaScript Libraries You Should Say Goodbye to in 2025](https://thenewstack.io/5-javascript-libraries-you-should-say-goodbye-to-in-2025/)，作者 Alexander T Williams。

随着[JavaScript](https://thenewstack.io/javascript/) 的发展，一些库不可避免地落后了，无法跟上开发者社区对最新特性、范式和性能的期望。

是时候做出一些艰难的决定，告别不再像以前那样满足我们需求的某些库了。下面，我们重点介绍五个在2025年可能过时的JavaScript库，以及为什么现在是迁移的时候。

## 为什么我们必须替换JS库？

我们都听说过JS的革命性突破，[例如18岁的Aiden Bai创建Million.js](https://arxiv.org/abs/2202.08409)来提高JS性能，或者有人找到了一种新的[在React中查看文档的方法](https://apryse.com/blog/react/how-to-embed-pdf-in-react)，但是那些被淘汰和不受欢迎的呢？

## 1. jQuery

jQuery是[现代JavaScript库的鼻祖](https://thenewstack.io/why-outdated-jquery-is-still-the-dominant-javascript-library/)，以其跨浏览器支持、[简单的DOM操作](https://api.jquery.com/category/manipulation/)和简洁的语法而闻名。然而，在2025年，是时候正式放弃它了。原生JavaScript API和现代框架（如React、Vue和Angular）已经使jQuery的核心实用程序过时了。

更不用说，原生JavaScript现在包含了诸如`querySelector`、addEventListener`和`fetch`之类的原生方法，这些方法更方便地提供了我们曾经依赖jQuery提供的功能。此外，现代浏览器已经标准化，使得像jQuery这样的跨浏览器解决方案的需求变得多余。更不用说，[如今将jQuery捆绑到应用程序中可能会增加不必要的膨胀](https://news.ycombinator.com/item?id=26319235)，在速度至上的时代减慢了加载时间。

如果您仍然依赖jQuery，请考虑迁移到模块化、特定于框架的解决方案，或重构代码以使用原生JS方法。这是一个巨大的飞跃，但这将使您的代码更精简、更快、更易于维护。

## 2. Moment.js

Moment.js长期以来都是默认的日期处理库，它因其解析、验证、操作和显示日期的能力而受到称赞。然而，与更新的替代方案相比，它现在变得笨重且缺乏灵活性，[更不用说它已被弃用](https://stackoverflow.com/questions/74682408/how-to-use-moment-js-instead-of-new-data#:~:text=The%20moment.,js.)。Moment.js的大小约为66 KB（压缩版），在追求更小包大小以实现更快性能和更好用户体验的时代，这是一个相当大的负载。

推荐的替代方案是`date-fns`或`luxon`。两者都提供模块化导入，这意味着您可以只使用所需的内容，从而大大减小包的大小。

更好的是，[JavaScript的Temporal API](https://refine.dev/blog/temporal-date-api/)一直在发展，可以直接处理日期和时间任务，[提供更有效的解决方案](https://thenewstack.io/javascript-due-for-new-time-date-and-set-features-next-year/)，而无需依赖第三方库。如果您仍在使用Moment.js，请将此视为开始迁移的通知。

## 3. Lodash

Lodash是一个多用途实用程序库，曾经是几乎每个JavaScript项目中的主打库。它提供了有用的实用程序来简化从深度对象克隆到数组操作的一切。然而，Lodash提供的许多功能现在要么[是JavaScript的原生功能](https://www.geeksforgeeks.org/common-javascript-functions-replacing-lodash/)，要么可以用简洁的代码轻松实现。

在ES6及以后版本中，`Object.assign()`、扩展运算符和`Array`方法等功能在很大程度上消除了对Lodash的需求。该库也很大，导入单个函数通常会将大量额外开销引入您的项目。

考虑通过使用ES6+等效项替换其函数来去除Lodash。对于Lodash确实提供独特便利性的少数几个极端情况，模块化导入`(import { cloneDeep } from 'lodash/cloneDeep')`可以最大限度地减少该库对包大小的影响。

## 4. Underscore.js

Underscore.js是Lodash的前身，尽管在很大程度上被其更年轻、功能更丰富的兄弟库所掩盖，但它已经存在多年了。是时候完全告别Underscore了。

与Lodash一样，Underscore的实用程序方法现在要么[在JavaScript中得到原生支持](https://www.specbee.com/blogs/javascripts-native-array-and-object-methods)，要么可以用更小的库或单个函数更有效地实现。如果您使用Underscore，您可能不会获得ES6+语法无法处理的任何实质性内容，并且它会为您的项目增加不必要的体积。

抛弃 Underscore 对性能和可维护性来说是一个简单的胜利，在 2025 年之后没有理由再继续使用它。

## 5. RequireJS
在 ES6 模块出现之前，RequireJS 在帮助 JavaScript 开发人员管理依赖项方面发挥了关键作用。它的[异步模块定义](https://requirejs.org/docs/whyamd.html) (AMD) 允许更有效的加载，帮助开发人员以模块化的方式组织他们的脚本，而这些功能在以前是不可用的。

然而，随着 ES6 模块的出现和[现代浏览器对它的广泛支持](https://stackoverflow.blog/2021/11/10/does-es6-make-javascript-frameworks-obsolete/)，RequireJS 现在已经多余了。ES6 提供了一种更简洁、标准化的导入和导出模块的方式，使得 RequireJS 的额外复杂性变得不必要。

像 Webpack、Vite 和 Rollup 这样的流行打包器也提供了简化依赖项管理的方法，使得使用 RequireJS 变得多余。此外，[云自动化工具通常会补充这些现代打包器](https://cast.ai/blog/cloud-automation-the-new-normal-in-the-tech-industry/)，提供无缝的部署和扩展能力。

如果您项目中仍然使用 RequireJS，现在是时候现代化了。将您的模块转换为 ES6 语法，并依赖 Webpack 或甚至原生模块加载工具来使您的代码库面向未来。

## 5 个旧库的 JavaScript 替代方案
随着上面提到的库即将淘汰，让我们来看看一些现代的替代方案，它们可以简化您的开发流程，并保持您的应用程序的性能和最新状态。

### 1. 原生 JavaScript (用于 jQuery)
[原生 JavaScript API](https://stackoverflow.com/questions/7022007/what-is-native-javascript) 已经得到了极大的改进，对于 jQuery 过去处理的大部分内容，原生 JavaScript 可以同样出色地完成。`querySelector`、`addEventListener` 和 `fetch` 等方法几乎涵盖了开发人员常用 jQuery 进行的 DOM 操作和 AJAX 请求，而不会给您的包增加不必要的体积。
### 2. Date-fns 或 Luxon (用于 Moment.js)
Date-fns 和 Luxon 是 Moment.js 的更轻量、更模块化的替代方案。它们允许您只导入所需的功能，从而显著减小包的大小。此外，JavaScript 正在发展的 Temporal API [提供了更强大的日期和时间处理能力](https://www.freecodecamp.org/news/how-javascripts-temporal-proposal-will-change-datetime-functions/)，直接在语言中使用。

### 3. ES6+ 原生特性 (用于 Lodash)
Lodash 的许多实用程序在 ES6+ 中都有原生替代方案。例如，您可以使用扩展运算符 (…)、`Object.assign()` 和大量的新的 `Array` 方法 (`map`、`reduce`、`filter`) 来处理 Lodash 曾简化的相同任务。对于更小众的用例，请考虑只导入所需的特定 Lodash 函数。

### 4. ES6+ 语法 (用于 Underscore.js)
Underscore 的实用程序方法也已被 ES6+ 语法大量取代。函数式编程、对象操作和数组迭代的方法都可以用更有效率和简洁的原生 JavaScript 来实现。将您的代码迁移到 ES6+ 将使其更清晰易于维护。

### 5. Webpack、Vite 或 ES6 模块 (用于 RequireJS)
现在 ES6 提供了标准化的模块系统，RequireJS 已不再需要。Webpack 和 [Vite](https://thenewstack.io/using-vite-and-vike-for-micro-frontends-plus-other-dev-news/) 等工具可以帮助您打包应用程序并以更简化的方式处理依赖项。此外，现代浏览器对原生模块的支持允许您加载模块而无需任何额外的依赖项。

## 结论

JavaScript 生态系统发展迅速，曾经不可或缺的东西很快就会过时。继续使用不再相关的库可能会给您的应用程序带来性能问题，增加维护成本，并使您的代码可读性降低。采用原生 JavaScript 功能、现代库或内置浏览器 API 可以使您的堆栈轻量化，应用程序高性能，并使您的开发实践保持最新。

是时候精简了：放弃 jQuery、Moment.js、Lodash、Underscore 和 RequireJS。现代替代方案不仅更快、更模块化，而且更符合当前 JavaScript 开发的最佳实践——确保您在 2025 年到来之际保持领先地位。
