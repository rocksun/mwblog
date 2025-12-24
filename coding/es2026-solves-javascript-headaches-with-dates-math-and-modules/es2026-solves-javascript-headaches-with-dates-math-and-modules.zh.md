对于 [2026](https://tc39.es/ecma262/) 年的 JavaScript 语言新特性来说，这可能是一个丰收年，一些非常大的提案终于成熟，同时还混合了常规的技术改进和新选项，使开发人员的工作更加轻松。

最终进入该语言的特性列表将包括所有在 2026 年 3 月前达到 [Stage 4 里程碑](https://tc39.es/process-document/) 的 ECMAScript 项目。

目前已有多个项目完全进入 Stage 4，另有两个项目也已接近尾声，只待最终批准（这意味着它们已在某些浏览器、JavaScript 运行时或工具中可用）。此外，还有一些非常有前景的提案处于 Stage 3，它们势头强劲，看起来很有可能及时获得批准。

## ECMAScript 2026 已批准哪些特性？

在 JavaScript 中进行除简单数学运算之外的任何操作都出了名的复杂。`Math` 对象目前甚至没有一个用于求和的常见方法（而不是一次只加两个数）。如果您编写一个循环来对那些无法用 JavaScript 64 位浮点数精确表示的数字求和，那么由于中间结果的浮点精度问题，[结果可能与您预期不符](https://github.com/tc39/proposal-math-sum)。

[Math.sumPrecise](https://github.com/tc39/proposal-math-sum) 使用一种更好（但更慢）的算法，为浮点数提供更精确的结果。虽然它没有解决 JavaScript 无法正确添加 0.1 和 0.2 的奇怪现象，但那是因为这些数的浮点表示本身就不是精确的 0.1 和 0.2。Igalia Web 标准倡导者 [Eric Meyer](https://www.linkedin.com/in/meyerweb/) 表示，新算法“使许多事情比自己编写函数更容易完成”。

> “作为一名时不时使用 base64 数据的人，并且可能希望将其移入和移出其他值格式，我期待着尝试这个 [Math.sumPrecise]。”
> **– Eric Meyer，Igalia Web 标准倡导者**

同样，JavaScript 目前有用于处理二进制数据的 `Uint8Array`，但没有内置的方法可以将二进制数据编码为 [Base64](https://github.com/tc39/proposal-arraybuffer-base64/blob/main/base64.md)（例如用于处理 SSH 密钥或在页面中嵌入小图片），或者从 Base64 数据（或从十六进制字符串）创建数组。[Uint8Array 转 Base64 提案](https://github.com/tc39/proposal-arraybuffer-base64) 增加了实现这两种功能的方法。

Meyer 说：“作为一名时不时使用 base64 数据，并且可能希望将其移入和移出其他值格式的人，我期待着尝试这个特性。”

JavaScript 已经有一个将 JSON 转换为可操作数据对象的方法 [JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)，但如果您处理数字和日期，转换会造成信息损失——因为 JSON 具有任意精度而 JavaScript 没有。

如果您解析一个千亿亿（1 后面跟 18 个零），您会得到 1000000000000000000——但如果您解析 999999999999999999（比千亿亿少一），您也会得到相同的结果。解析日期和时间时，JavaScript 会在格式中添加一个空的秒数。JavaScript 甚至不允许您将 `BigInt` 转换为 JSON，因为当您将其从 JSON 解析回来时，您将得不到相同的数字。

[JSON.parse 源文本](https://github.com/tc39/proposal-json-parse-with-source) 提案允许您检索原始 JSON 源文本，并根据需要将其精确转换——无论是转换为 `BigInt`，还是您可以查看哪些字符被转义，以便您能够以您想要的方式准确地组合字符串。这最早在 2018 年被提出，当时有很多关于添加额外功能的讨论，例如能够以同样的方式将 JavaScript 对象序列化为 JSON（解析的逆向操作）；不过，进入 Stage 4 的提案中不包含这些功能。

另一个存在已久（自 2015 年以来）的提案是 [Error.isError](https://github.com/tc39/proposal-is-error)。它用于检查 JavaScript 值是否确实是一个错误对象，因为您可以在 JavaScript 中使用 `throw` 抛出几乎任何东西，包括数字。它比使用 `instanceof Error` 更可靠，因为它在不同的执行上下文（如浏览器扩展和 iframe）中也能工作，并且不会被看起来像错误的对象所迷惑。这对于调试非常有用，对于编写 polyfill 和库也极其有用；此外，它已在浏览器中广泛可用。

许多其他语言已经内置了将一系列迭代器链接在一起的方法，这样您可以一个接一个地调用它们，并一次性按正确顺序获取所有值；目前，您必须在 JavaScript 中使用生成器来完成此操作。新的 [迭代器排序](https://github.com/tc39/proposal-iterator-sequencing) 提案通过一个新的 `Iterator.concat` 函数使其更简单；它已在 Firefox 和 Safari 中可用。

## 改进国际化和本地化

一周的第一天是哪一天？在某些地方是周日而不是周一。在某些国家，周末是周五和周日（周六是工作日），或者周四和周五。在其他国家，只有一天——但那一天在不同地区是周五、周六或周日。如果您正在编写日历应用程序，您需要了解这些信息（以及哪些国家最近更改了官方周末是哪些天）。[Intl Locale](https://github.com/tc39/proposal-intl-locale-info/blob/main/README.md) 会从 [Unicode 区域设置数据](https://unicode.org/reports/tr35/tr35-dates.html#Calendar_Preference_Data) 中获取所有这些信息，以及其他细节，例如该地区的语言是否需要从右到左或从左到右渲染，这样开发人员就不需要自己去解决。

> ECMAScript 2026 还将包含 Intl.Locale 的变体 API。

这不是一个具体的提案，但 ECMAScript 2026 还将包含 `Intl.Locale` 的变体 API，允许开发人员使用 Unicode 区域设置细节，例如特定地点使用的地区、语言、脚本和数字——这些可能对日期和时间有自己的样式，而无需为确切的组合提供 ISO 代码。

因此，“ca-Latn-ES-fonipa-valencia-u-nu-roman”代表在西班牙使用的拉丁文 `Catalan language`，其中瓦伦西亚变体以音标 IPA 捕获，并使用罗马数字编号系统（子标签的顺序始终是字母顺序）。这提供了大量的细节——这正是您需要使网页在全球任何地方都能正常工作所需的精确信息。

## 最终确定异步代码和资源管理

最常用的 `Array` 方法之一是 `Array.from`，当您想要一个 map、set 或类似数组的副本时使用；但它只适用于立即生成值的同步可迭代对象，不适用于将值包装在 Promise 中（因此您可以使用它们来处理网络请求、文件流或来自事件和 API 的数据等异步请求）的异步可迭代对象。为此，您需要一个非常流行的库或 [Array.fromAsync](https://github.com/tc39/proposal-array-from-async)，这使得代码更容易阅读（和编写），并且 [已可用](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fromAsync#browser_compatibility) 于所有浏览器以及 Node 和 Deno 等 JavaScript 运行时。事实上，它已经存在足够长的时间，成为 [Baseline 2024](https://thenewstack.io/baseline-newly-available-stay-on-top-of-new-web-features/) 的一部分。

但到目前为止，它的工作细节尚未添加到 ECMAScript 标准中，主要是因为有一个小 bug 在实现中很快得到修复，但实际上并未写入规范中，并且为了匹配 JavaScript 其他地方的行为而进行了一项更改，增加了一个新的 WPT 测试，几乎所有浏览器都已通过。目前已达成一致，只要 TC39 编辑批准规范更改，它就会达到 Stage 4，这应该会赶上 ECMAScript 2026。

同样，[显式资源管理](https://github.com/tc39/proposal-explicit-resource-management) 需要审查最后几个测试并批准规范文本才能达到 Stage 4，但它已在 Chrome、Node、Deno、用于嵌入式设备的 [Moddable XS 引擎](https://www.moddable.com/faq#what-is-xs) 中发布，并在 Firefox（通过标志）中提供；同时还支持 Babel、TypeScript 和其他工具。

彭博社软件工程师 [Ashley Claymore](https://www.linkedin.com/in/ashleycutmore/)（他参与了多个 TC39 提案）解释说，以前，检查是否明确清理了内存等资源意味着在代码中大量上下滚动。

“你在 `try` 块中获取资源，并且知道无论发生什么，无论它返回还是抛出异常，你都必须清理它，但你必须把它一直放到 `finally` 块中。”但对于很长的代码块，开发人员可能无法同时在屏幕上看到两者。“你看到需要一个资源，你希望它会被清理，然后你滚动又滚动，直到找到最终块并看到，是的，它正在被清理，所以你滚动回到顶部，然后继续。现在，使用 `using` 块，你可以免费获得它。”

> “…这个 [显式资源管理] 现在使其更符合人体工程学，并标准化了如何完成此操作。”
> **– Ashley Claymore，彭博社软件工程师**

您不是使用 `const`，而是创建了一个 `using` 块，对象可以定义 `Symbol.dispose` 或 `Symbol.asyncDispose`，这些方法在代码块结束时自动调用。这更像是使用 C++、C# 或 Python 进行开发。

“即使您的代码抛出异常，或者它只是返回，您也能保证清理工作会发生。这是您以前可以做的事情，但现在这使得它更符合人体工程学，并标准化了如何完成此操作。”

Claymore 建议，Babel、TypeScript 和 esbuild 等工具已经支持这一点，可以帮助开发人员养成确定性清理资源的好习惯。

“过去，人们可能会使用终结器注册表并依赖垃圾回收器来清理事物。虽然它在代码中看起来很棒，但这有问题，因为垃圾回收器非常不可预测。你不知道它何时运行。假设你有一个数据库句柄，你的数据库连接硬性限制是 256 个：你的垃圾回收器不知道。你的垃圾回收器只知道你正在使用多少内存。等待垃圾回收器决定‘你正在使用太多内存，我将开始清理事物，我可能会也可能不会调用你的终结器注册表处理程序’这太冒险了。”

## 期待已久的 Temporal API：修复 JavaScript 的 Date 对象

其他原定于 2025 年进入 ECMAScript 的项目，例如 [装饰器](https://github.com/tc39/proposal-decorators)（已通过转译器广泛可用），仍在进行最后阶段的工作。但是 [Temporal](https://github.com/tc39/proposal-temporal)，这个长期以来备受期待的“[JavaScript 的损坏 Date 对象](https://thenewstack.io/javascript-forecast-whats-ahead-for-ecmascript-2022/#:~:text=Temporal,%20for%20Date-Related%20Javascript.%20Temporal,%20which%20Terlson%20refers%20to%20as)”的替代品，已经达到了一个重要的里程碑：它现在是一个 Stage 3 草案，并且第一个实现正在进行中。

“`Date` 对象没有很好地老化。它相当糟糕，开发人员要么错误地使用它并出现 bug，要么就完全避免使用它，”[Boa](https://github.com/boa-dev/boa)（一个用 Rust 编写的可嵌入 JavaScript 引擎）的创建者、TC39 `Temporal` 倡导者之一 [Jason Williams](https://www.linkedin.com/in/jason-williams10/) 解释道。

开发人员为解决这些问题而采用的日期库为项目增加了大量额外代码，特别是当您需要时区支持或国际化时。

> “Temporal 在帮助您避免错误和力求更明确方面做得更好。”
> **– Jason Williams，Boa 创建者**

Williams 指出：“如果你拿任何 Web 应用放到打包分析器中，有时最大的方块通常是 [Moment.js](https://momentjs.com/) 或类似的库。”“当浏览器通常无论如何都拥有这些数据时，我们继续通过网络发送它就没有意义了。”

新的规范设计也更好：“Temporal 在帮助你避免错误和力求更明确方面做得更好。”它处理时区，包含内置日历，并正确解析和格式化日期和时间，创建易于人类阅读的时间和日期字符串版本。这是 `Date` 对象非常糟糕的一点，以至于 Budibase 开发者 [Sam Rose](https://github.com/samwho) [发现它对 0 和“0”的处理方式不同](https://bsky.app/profile/samwho.dev/post/3ltpdkr3bmk2o) 后，受到启发创建了 [一个令人恼火的有趣测验](https://jsdate.wtf/) 来嘲笑它的特性。（实际上，由于 `Date` 的许多行为都依赖于实现，因此该测验的答案在 Firefox 和 Chrome 中会有所不同。）

Temporal 在影响力和代码量方面都很大。典型的 JavaScript 功能可能只有几百个测试；Temporal 有 4000 个测试，一度几乎是这个数字的两倍。

“它实际上比整个 ES6 的测试还要大；这就是它覆盖的面积有多广，”Williams 说。“我们确实把它缩小了，因为我们试图降低复杂性。”

就规范达成一致需要时间（Williams 补充说：“我们现在处于收尾阶段，一些小错误正在被整理”），实现它也需要时间。尽管 Firefox 已经发布了实现。

V8 团队正在与 Boa 合作开发一个名为 [temporal_rs](https://lib.rs/crates/temporal_rs) 的 Rust crate，其中包含 Temporal 的大部分逻辑，其他 JavaScript 引擎也可以使用——这种开源社区合作模式通常可以降低浏览器采用新 JavaScript 功能的成本。[Kiesel](https://kiesel.dev/) 和 [Yavashark](https://github.com/Sharktheone/yavashark) JavaScript 引擎也正在采用它。

> “它 [Temporal] 使围绕日期和时间的许多事情变得更容易，并且程序员出错的可能性更小。”
> **– Meyer**

该 [库](https://github.com/boa-dev/temporal) 目前已推出 v0.1 版本，以便在最后一刻进行规范更改——尽管它通过了所有当前测试并可供使用。它在 V8 中已 [取消标志](https://issues.chromium.org/issues/401065166#comment106)，预计将在 [Chromium 144](https://chromestatus.com/feature/5668291307634688) 中落地（该版本将于 2026 年 1 月 7 日稳定），而 WebKit 存储库中的 Safari 实现已完成近一半，[两个](https://www.npmjs.com/package/@js-temporal/polyfill)[polyfill](https://www.npmjs.com/package/temporal-polyfill) 也已可用于生产环境。Ladybird 和 Graal 引擎也已完成大部分实现。

这使得 Temporal 很有可能在 ECMAScript 2026 中实现——Williams [预测](https://boajs.dev/blog/2025/09/24/temporal-release) 它将在 2026 年第一季度达到 [Stage 4](https://github.com/tc39/proposal-temporal/milestone/2)，这可能赶上二月份的截止日期。Igalia 开发者倡导者 [Brian Kardell](https://www.linkedin.com/in/brian-kardell-08a4264/) 对此充满热情：“这是一项多么巨大的努力，它能从我们的应用程序中消除多么大量的代码啊！太棒了。”

“它使围绕日期和时间的许多事情变得更容易，并且程序员出错的可能性更小，”Meyer 同意。“我能够在一个上午写出一个基本的‘告诉我今天与给定日期之间的一半日期，以及与给定日期距离今天相同的日期’的工具，而且我在写代码的过程中学习了 Temporal 方法。”

## 使用延迟模块导入优化性能

另一个可能在 ECMAScript 2026 中实现的 Stage 3 提案是“`module harmony`”改进之一，旨在提高性能：[Import defer](https://github.com/tc39/proposal-defer-import-eval)。

TC39 联席主席 [Rob Palmer](https://www.linkedin.com/in/robpalmer2)（他也在彭博社工作）解释说：“与通常的急切加载不同，急切加载会导致模块在当前模块中的任何内容之前进行评估，而你得到的是对命名空间的句柄。”“当你触摸命名空间的那一刻，当你拉取一个属性的那一刻——这可能在很久以后才发生——当你第一次使用该模块命名空间时，模块就会被加载。这在大型代码库中非常有用，其中模块图可能需要数百毫秒才能加载，因为你可以确保你只为使用的部分付费。”

> “这个 [import defer] 在大型代码库中非常有用，其中模块图可能需要数百毫秒才能加载……”
> **– Rob Palmer，TC39 联席主席**

彭博社终端（用 C++ 和 JavaScript 编写）已经使用了这种模式。“我们有一些庞大而复杂的应用程序，即使有编译器也很难知道最佳加载顺序是什么，因此能够说‘让代码运行，无论它碰到什么，我们都即时加载’被证明是一种非常高效的工作方式。”

JavaScript 已经有动态导入，但这意味着需要回头进行网络调用来加载模块——这可能太慢了。

Palmer 建议：“如果你能进行动态导入，你就应该这么做。”但现有代码并非总能转换为使用动态导入。“你需要确保你的调用者和你的调用都是异步的，并且能够容忍异步加载，而当你使用 `defer` 关键字时，所有内容仍然是同步的，因此当你发现需要时，将其作为优化手段会容易得多。”

使用 `import defer` 推迟模块评估已经得到 [各种工具](https://github.com/tc39/proposal-defer-import-eval/issues/73) 的支持，例如 [TypeScript](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-9.html#support-for-import-defer)、Prettier、Babel 和 [webpack](https://webpack.js.org/guides/lazy-loading/)。随着 [V8](https://issues.chromium.org/issues/398218423) 和 WebKit [JavaScriptCore](https://github.com/WebKit/WebKit/pull/40453) 引擎的实现正在进行中（并且 [SpiderMonkey](https://bugzilla.mozilla.org/show_bug.cgi?id=1952263) 也在待办事项中），Palmer 预测它将在 2026 年在浏览器中得到支持，并加速大型 Web 应用程序的启动时间。

大多数其他语言已经允许您在不编写条件测试的情况下检查值是否存在或如果不存在则插入，因为这是一种非常常见的数据库操作；现在 JavaScript 将通过 `Upsert`（`update` 和 `insert` 的合成词）为 `map` 和 `weak map` 提供此功能。Palmer 指出，该功能将于 2026 年 1 月在 Chrome 145 中发布，很可能在 3 月份达到 Stage 4。这是一个相对简单的功能，因此它被用来让更多人参与到浏览器贡献中——目前有 [卑尔根大学的学生](https://webengineshackfest.org/slides/cross-engine_contributions_at_scale:_how_newcomers_accelerated_temporal_and_upsert_in_spidermonkey,_v8,_and_boa_by_jonas_haukenes,_mikhail_barash_&_shane_carr.pdf) 正在从事相关代码工作。