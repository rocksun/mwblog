
<!--
title: JavaScript 预计明年将推出新的时间、日期和集合功能
cover: https://cdn.thenewstack.io/media/2024/10/f9227aec-allison-saeng-zo9fjlfuokm-unsplash_1280.jpg
-->

我们预计将在 ECMAScript 2025 中看到的重大 JavaScript 新功能，以及导致它们延迟的讨论。

> 译自 [JavaScript Due for New Time, Date and Set Features Next Year](https://thenewstack.io/javascript-due-for-new-time-date-and-set-features-next-year/)，作者 Mary Branscombe。

JavaScript 下一个[年度更新](https://thenewstack.io/whats-new-for-javascript-developers-in-ecmascript-2024/) 将在新年初确定其包含的功能，包括在 2025 年 3 月前达到最终第四阶段里程碑的项目（其中一些功能已经达到了这一阶段）。

还有一些功能有望在截止日期前准备就绪，其中包括一项备受期待的、长期以来一直被人们热切期盼的功能，它似乎终于走到了最后阶段。在 ECMAScript 2024 截止日期之后，有两个新功能达到了第四阶段：用于处理正则表达式的重复命名捕获组和用于处理集合的方法。

## 为 JavaScript 效率奠定基础

能够[在正则表达式不同分支中使用相同的名称](https://github.com/tc39/proposal-duplicate-named-capturing-groups) 虽然是一个很小的功能，但它可以简化表达式编写，因为你可能需要匹配可以用不同方式表达但只匹配一次的内容（例如，日期中的年份可以是 2025 或 25）。目前，如果你将这两个模式都命名为“year”，就会出现[错误](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_duplicate_capture_group_name)，因此你必须想出不同的名称。现在，只要这些名称位于表达式中由 | 分隔的不同分支中，你就可以使用相同的名称。

> “当所有浏览器都非常迅速地生成这些[实现]时，这表明了强烈的支持，这也是我们在推动任何提案时尽可能追求的目标。”
>
> – Rob Palmer，TC39 联合主席

多年来，人们一直在讨论 JavaScript Set 类的新方法：在这个方面，JavaScript 落后于许多其他语言（如 Python、Ruby、Swift、Rust 和 C#），导致开发者不得不编写自己的集合方法或[使用 Core.js 等 polyfill](https://github.com/zloirock/core-js?tab=readme-ov-file#set)。TC39 联合主席[Rob Palmer](https://www.linkedin.com/in/robpalmer2) 将此描述为“另一个典型的例子，人们从 ES 2015 开始，也就是九年前，就一直在编写自己的三到四行实用程序函数来处理集合并提供基本的集合操作。”

“这个提案之所以花费了这么长时间，是因为它在语言中开辟了新的领域，”彭博社软件工程师[Ashley Claymore](https://www.linkedin.com/in/ashleycutmore/) 解释道，他参与了多个 TC39 提案。

在这些新的集合方法出现之前，JavaScript 没有一种复杂类型可以与另一个相同类型的实例组合并返回一个实例，因此没有示例说明新功能应该如何工作。

“我们花了大量时间讨论什么是集合，”Claymore 说。“如果我将一个集合与另一个集合进行交集，另一个集合是什么？另一个集合是可迭代的吗？它必须是使用 new Set 创建的实际官方集合实例吗？如果将一个映射传递给集合方法会发生什么？”

> “……实际上，我们花了大量时间讨论什么是集合，现在我们有了答案。”
>
> – Ashley Claymore，彭博社软件工程师

以不会产生意外后果的方式正确解决这些技术问题非常重要。

“每个人都同意这很有用，”他继续说道。“集合应该做这些事情，这些是我们应该拥有的方法。但实际上，我们花了大量时间讨论什么是集合，现在我们有了答案。”

所有这些讨论确保了看似基本的功能以一种适合语言的方式实现。

集合类似于数组，但每个值都是唯一的，因此你只能添加集合中不存在的新值。这意味着你可能对处理一个集合中存在而另一个集合中不存在的所有值（差集）、两个集合中存在但不在两个集合中都存在的值（对称差集）、或仅存在于两个集合中的值（交集）或其他各种组合感兴趣。七种新方法涵盖了开发者在处理集合时所需的标准范围：并集、交集、差集、对称差集、是否是子集、是否是超集、是否是互斥的。

> “我经常使用集合，但你很少在不需要其中一个或多个方法的情况下使用它们，你可能会认为它们应该一开始就包含在标准库中，但事实并非如此。”
>
> – Brian Kardell，Igalia 开发者倡导者

“我经常使用集合，但你很少会不想要其中一个或多个而使用它们，你会认为它们应该一开始就出现在标准库中，但它们就是没有，”Igalia 开发者倡导者 [Brian Kardell](https://www.linkedin.com/in/brian-kardell-08a4264/) 告诉 The New Stack**。**“作为一名开发者（以及开发者*倡导者*），我对这一点感到非常兴奋，因为我知道我会永远使用它们——就像我最喜欢的几个数组方法一样。”

尽管开发者可以通过编写自己的函数在 JavaScript 中实现这一点，但将这些功能添加到语言中可以节省时间并提高一致性。

“集合和数组方法很有价值，因为它们被广泛使用，”Kardell 继续说道，“你不需要重写它们，也不需要担心你的大型程序最终会包含五个相同功能的实现。”

因为达到第四阶段意味着至少有两个主要实现，开发者可以考虑立即使用这两个功能。新的 Set 功能现在已在所有主流浏览器中得到支持：它于 2024 年 6 月在 Firefox 和 [TypeScript 5.5](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5) 中发布，使其 [广泛可用](https://thenewstack.io/what-does-it-mean-for-web-browsers-to-have-a-baseline/#:~:text=A%20new%20project%20called%20Baseline%20aims%20to%20clarify%20what%20developers) 成为 [Baseline 2024](https://web.dev/blog/set-methods?hl=en) 的一部分，Kardell 将其概括为“当我们发布某个功能的最后一个实现时”。

Palmer 将 Set 方法进入基线的速度视为从标准到广泛可用性的管道的一个很好的例子，[ECMAScript 标准化过程](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/) 旨在实现这一目标：“当所有浏览器都非常迅速地生成这些 [实现] 时，这是一个强有力的支持表现，这也是我们在推动任何这些提案时尽可能追求的目标。你不想让人们因为它们在一个浏览器中不可用而犹豫使用它们，尽管，显然，始终可以使用 Babel 或 TypeScript 等编译器作为解决方案。”

重复捕获组还没有那么先进：它在所有主要桌面浏览器和大多数移动浏览器中得到支持（它仍在三星移动浏览器中处于预览阶段），但在 Node.js 或 Deno 中还没有。

## 下一阶段：装饰器、JSON 模块和 Promise

最有可能在 ECMAScript 2025 中及时准备好的其他功能是已经达到第三阶段的提案：装饰器、JSON 模块、Promise.try 和（最终）Temporal。

### 装饰器

装饰器通过将现有代码包装在另一段代码中来添加额外的功能（就像在房间里添加窗帘或新涂层以使其更实用一样）。这可以像简单地更改代码的外观以使其更易读而不更改底层代码一样简单，也可以通过使代码更模块化来提供更灵活的代码结构方式。

使用装饰器，你可以将处理数据存储和模板的逻辑放在你正在编写的类之外，而不是将它们放在一起，这会降低灵活性，并且难以在其他项目中重用。装饰器允许开发者为常见任务（如日志记录、动态类型检查和其他安全检查（如验证参数））创建抽象，并在需要时将它们添加到类中。

> “我们发现从现有装饰器使用方式过渡的路径很重要，我们希望能够逐步采用并良好地处理现有生态系统：我们不是在真空中设计它。”
> 
> – Daniel Ehrenberg，Ecma 副总裁

这是一种在 React 和 Angular 等框架中广泛使用的模式，并且在 TypeScript 和 Babel 中已经支持了很多年——尽管与 ECMAScript 提案经过多年讨论后发展成的形式并不完全相同（这允许装饰器与私有字段和方法一起使用）。

尽管装饰器的更广泛概念已通过在转译器中的广泛使用得到广泛验证，但在 JavaScript 语言本身中就正确的方法达成一致却花费了相当长的时间。

“我们经历了装饰器提案的许多迭代，最终我们找到了一个我们都同意满足用例和从先前装饰器过渡的路径以及浏览器可实现性问题的提案，”Ecma 副总裁 [Daniel Ehrenberg](https://www.linkedin.com/in/danielehrenberg/) 解释道。“我们终于能够将所有这些三角化。这确实意味着存在一些差异，但同时，我们确实努力确保过渡顺利。”
其中一部分是允许代码使用 TypeScript 实验性装饰器的现有语法或提案中的新语法。您必须为单个函数选择其中一个，但他解释说：“在一个特定的导出类声明中，装饰器可以在导出关键字之前或之后出现。” 这是一件小事，但它避免了开发人员需要重写现有代码。

Ehrenberg 指出：“我们发现从现有装饰器使用的过渡路径很重要，我们希望能够逐步采用并很好地对待现有生态系统：我们不是在真空中设计这个。”

作为将装饰器引入 JavaScript 的一部分，一些关于将装饰器应用于对象、变量和参数的更雄心勃勃的想法已从提案中删除——但这些仍然作为 [可能的扩展](https://github.com/tc39/proposal-decorators/blob/master/EXTENSIONS.md) 使用相同的语法。

### JSON 模块

在另一个简化中，[JSON 模块](https://github.com/tc39/proposal-json-modules) 最初是导入属性提案的一部分，是大型 [模块和谐工作](https://thenewstack.io/5-ways-javascript-is-improving-modules-for-developers/) 的一部分，旨在填补 [ECMAScript 模块功能](https://thenewstack.io/how-javascript-is-finally-improving-the-module-experience/) 在 JavaScript 中的空白。它被移到一个单独的提案中，以避免阻碍更普遍的概念，即能够包含用于处理导入内容的说明，以及处理 JSON 文件的具体细节。

> 导入属性和 JSON 模块的实现正在进行中，并且可能都将在今年晚些时候同时进入第四阶段。

能够将 JSON 或 CSS 文件标记为要读取的文本而不是要执行的代码对安全性有好处，因为它意味着该文件不会执行开发人员没有预料到的操作。虽然这看起来很简单，但 HTML 和浏览器社区以及 ECMAScript 委员会花了些时间来研究将此集成到浏览器的正确语法。Chrome 已经使用早期版本的语法（由 Microsoft 贡献）发布了该功能，但现在已被删除，并且导入属性和 JSON 模块的实现正在进行中，并且可能都将在今年晚些时候同时进入第四阶段。这并不意味着将提案分开是毫无意义的；它允许它们以自己的速度前进，即使它们看起来会同时到达。

### Promises.try

另一个已经开发了一段时间的特性填补了使用 promises 的一个小空白。

> Promises.try 在 6 月份进入第三阶段，并且已经在各种浏览器中实现了。

JavaScript 中的 promises 以结构化的方式处理异步操作的最终成功或失败：promises 链末尾的 catch 方法应该捕获所有错误，而 then 方法告诉你的代码如何处理错误。但是，如果您正在调用一个函数或使用一个接受回调的 API，该回调可能是异步的，也可能不是异步的，[Promise.try](https://github.com/tc39/proposal-promise-try) 将回调的结果包装在一个 promise 中，因此如果它抛出错误，该错误将被捕获并转换为一个被拒绝的 promise。这样，您可以确保可以在单个 promises 链中处理同步和异步错误。这是另一个在 Core.js 中被 polyfill 的流行特性（以及早于 JavaScript 实现的第三方 promise 库，例如 [Bluebird](http://bluebirdjs.com/docs/why-bluebird.html)）。

Promises.try 在 6 月份进入第三阶段，并且已经在各种浏览器中实现了（它在 Edge 和 Chrome 中，已添加到 WebKit，在当前 Firefox 开发人员版本的标志后面，并且很可能包含在 2024 年 11 月或 2025 年 1 月的 Firefox 版本中）以及 Bun 和 Cloudflare worker 等运行时。这足以在 ECMAScript 委员会达成一致后进入第四阶段，这应该在 ECMAScript 2025 年之前完成。

## Temporal 即将到来

Temporal（当时 TC39 编辑 [Brian Terlson](https://www.linkedin.com/in/brian-terlson-6822aa61/) 在 2021 年首次进入第三阶段时，令人难忘地 [向我们描述](https://thenewstack.io/javascript-forecast-whats-ahead-for-ecmascript-2022/#:~:text=Temporal,%20for%20Date-Related%20Javascript.%20Temporal,%20which%20Terlson%20refers%20to%20as) 为“我们破损的 Date 对象的替代品”）似乎越来越有可能在 ECMAScript 2025 年准备好，因为最近在 [处理阻碍其进展的问题](https://github.com/tc39/proposal-temporal/issues/2628) 上取得了很大进展。

当 JavaScript 在 1995 年创建时，它 [复制了 Java 的日期对象](https://maggiepint.com/2017/04/09/fixing-javascript-date-getting-started/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)：一个相当简单的实现，Java 在 1997 年就替换了它，但它在 JavaScript 中却仍在挣扎（或者更常见的是，它被 Moment.js 等库所取代）。用 Temporal 替换它一直被认为是一项艰巨的任务，因为日期、时间、时区和日历的复杂性，但也相对没有争议。

Temporal 显然是人们需要的：作为 [Interop 2023](https://thenewstack.io/how-interop-2023-will-move-the-web-forward/#:~:text=Interop%20progress%20as%20of%20August%202023.%20Government%20regulation%20on%20competition) 中将包含哪些内容的讨论的一部分，Ehrenberg 告诉我们，“他们对开发者希望使用哪些 API 进行了调查，Temporal 获得了大量投票”。那么，为什么一个受欢迎的提案在五年内一直处于即将进入 JavaScript 语言的边缘呢？

> “......专门用于 Temporal 的规范页面数量与整个 ES6 的大小大致相同。”
>
> – Palmer

该提案一直在等待的一件事是互联网工程任务组 (IETF) 的工作，即 [标准化用于日历和时区](https://www.rfc-editor.org/rfc/rfc9557.html) 注释的 ISO 字符串格式。这项工作在一定程度上因疫情而推迟，于 2024 年 4 月作为新的 RFC 完成，但即使在它完成之前，也很明显，它并不是唯一阻碍 Temporal 的因素。

日期和时间是一个庞大而复杂的主题，有着错综复杂的规则（例如英国历史上缺失的 11 天，或者多伦多曾经出现过 23 小时 30 分钟的一天）。Temporal 最初是一个非常全面的解决这个问题的方法：如此全面，以至于当各种浏览器开始实现它时，很明显，将所有必需的代码放入 JavaScript 引擎将需要大量工作，并且可能需要比目前在例如 Apple Watch 或低端 Android 手机上可用的磁盘和可执行内存空间更多。

找出如何节省空间是一项艰巨的任务，需要查看 Temporal 中的每个参数和函数，以了解其重要性以及没有它会损失什么，而不会重新设计一个已经开发了七年的提案，或者让开发者更难学习。

虽然 Temporal 规范中有一些地方可以优化，但它也必须缩减范围——主要是通过删除用于允许开发者构建自定义日历和时区的日历和时区对象。这两者都是提案中最复杂的部分，也是 Web 浏览器在实现过程中发现最多错误的地方。

> “我们真的想专注于确保我们仍然满足重要的用例。”
>
> – Ehrenberg

Ehrenberg 解释说，从规范中删除它们是为了“减少实现和维护负担”。“我们真的想专注于确保我们仍然满足重要的用例。”

“这只是考虑到专门用于 Temporal 的规范页面数量与整个 ES6 的大小大致相同，什么是更合理的规模和范围，”Palmer 同意道。“它变得越来越庞大，我们以后可能会得到这些东西。”

部分原因是，新设备将拥有更多存储空间和内存，为 JavaScript 中的更多功能腾出空间。而开发 Temporal 的经验让我们更清楚地了解哪些自定义时区和日历将有效，哪些将无效，因此，针对这些内容的新设计（可能基于 [jsCalendar](https://www.rfc-editor.org/rfc/rfc8984.html)，旨在取代无处不在的 iCal 格式）很可能比最初的方法有所改进。

与此同时，SpiderMonkey、V8、LibJS、JavaScriptCore 和 Boa 中的实现正在进行，以及 [来自 Fullcalendar 的 polyfill](https://github.com/fullcalendar/temporal-polyfill)。当其中两个可用时，Temporal 终于可以进入第四阶段，成为 JavaScript 的正式组成部分。如果幸运的话，这将在 ECMAScript 2025 中实现。

## 让 Web 真正国际化

像 Temporal 这样雄心勃勃的提案往往需要这种迭代设计（尽管这对领导提案通过委员会的人来说很困难；Temporal 已经有多位“冠军”带头冲锋）。
另一个重大且重要的提案，即[通过在 JavaScript 中用标准替换专有消息格式，使网站和应用程序更容易在多种语言中本地化](https://thenewstack.io/whats-next-for-javascript-new-features-to-look-forward-to/#:~:text=Intl%20MessageFormat%20is%20another%20stage%201%20TC39%20proposal,%20in%20conjunction)，也进展缓慢。同样，[它相关的外部 ICU 标准已经取得了重大进展](https://www.unicode.org/reports/tr35/tr35-messageFormat.html#introduction)，但 ECMAScript 委员会[仍在讨论该提案在 JavaScript 中的范围应该是什么](https://github.com/tc39/notes/blob/main/meetings/2024-04/april-10.md)，这使得一些参与者对进展缓慢感到沮丧。

同样，这也是开发人员想要的东西：几乎三分之一的 Web 本地化使用与[Intl.MessageFormat](https://github.com/tc39/proposal-intl-messageformat) 提案非常相似的 API 的 polyfill（实际上它基于 2013 年提出的类似提案，该提案使用了之前的 ICU MessageFormat）。

> “…他们[像 Intl.MessageFormat 这样的重大提案]解决了更难的问题，而且它们也是真正的公共利益——改进这些东西有助于鼓励我们构建一个更国际化的网络。”
>
> – Kardell

尽管新的 ICU 工作是为了响应 ECMAScript 提案，但 TC39 委员会希望确保这种方法对尚未参与 MessageFormat 2 的组织有用：这将看起来像大约十几个新组织在生产中使用新的语法。彭博社已经在开发原型，但看起来它需要更多示例才能使该提案达到我们可以推测它何时会成为语言一部分的阶段。

但 Kardell 认为，即使进展缓慢，这些重大提案仍然令人兴奋。“[那些]更难甚至不可能的事情——比如[Temporal](https://github.com/tc39/proposal-temporal) 或[Intl.MessageFormat](https://github.com/tc39/proposal-intl-messageformat)——甚至[模块捆绑/内联模块想法](https://github.com/tc39/proposal-module-expressions)，这些可能需要巨大的复杂性，需要构建步骤，或者可能有一些事情在现实中根本不可能做到。我因为其他原因对这些感到兴奋。如果我们能得到它们，它们将是巨大的。它们不会仅仅稍微提高性能，它们会解决更难的问题，而且它们也是真正的公共利益——改进这些东西有助于*鼓励*我们构建一个更国际化的网络。”
