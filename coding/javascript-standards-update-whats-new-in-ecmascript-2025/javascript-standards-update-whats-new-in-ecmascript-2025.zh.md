既然 ECMAScript 2025 的[年度更新已经获得批准](https://ecma-international.org/publications-and-standards/standards/ecma-262/)，我们就确切地知道哪些特性已纳入官方 JavaScript 语言规范，以及我们仍在等待哪些特性。它包括[我们希望的部分特性，但并非全部](https://thenewstack.io/javascript-due-for-new-time-date-and-set-features-next-year/)，以及一些快速通过批准阶段的其他新提案。

顺便说一句，年度更新被称为 ECMAScript 的原因不仅仅是因为负责它的 TC39 委员会是 Ecma International 的一部分；而是因为 [Oracle 仍然持有 JavaScript 商标](https://thenewstack.io/oracle-wont-release-javascript-without-a-fight/)。Oracle 对 [Deno 的诉求](https://deno.com/blog/deno-v-oracle4)（即它应该将其作为通用术语和废弃商标交给社区，因为它没有相关产品）的法律回应将于本月到期。

与此同时，自大型 ECMAScript 2015 发布以来，该语言本身继续以我们过去十年所看到的相同势头改进。

> “这是另一个规模健康的发布版本：不太大也不太小。”
> **— Rob Palmer, TC39 联合主席**

TC39 联合主席 [Rob Palmer](https://www.linkedin.com/in/robpalmer2) 告诉 The New Stack：“这是另一个规模健康的发布版本：不太大也不太小。它有很多符合人体工程学的特性，我们真的希望这些特性能够被广泛使用。”

它们与其说是根本性的新功能，不如说是让 Web 开发人员的生活更轻松——正如 Palmer 所说，“这些特性允许开发人员简洁地表达自己”。

## 更优雅的集合

JavaScript 长期以来都有迭代器的概念，但除了循环遍历值集合中的所有内容之外，它们无法做太多事情。如果开发人员想要转换甚至只是过滤值，他们会使用第三方库或将值复制到数组中进行处理，从而立即增加代码所需的内存量。有了[新的迭代器助手](https://github.com/tc39/proposal-iterator-helpers)，就不再需要这样做了。

[Ashley Claymore](https://www.linkedin.com/in/ashleycutmore/)（一位在多个 TC39 提案中工作过的彭博软件工程师）表示：“现在你可以留在迭代器的世界里”，这将更具表现力，而且通常更有效，因为“迭代器会尽量减少工作量”。

如果你想将迭代器过滤到只有前三个值，你现在可以在控制循环中直接这样做（新方法包括 map、filter、reduce、flatMap、some、find 和 every——这些方法在使用数组时会很熟悉——以及新的 drop 和 take 操作）。

Claymore 解释说，在迭代器中进行过滤需要的工作量要少得多。“如果我把所有的东西都放到一个数组中，我就创建了一个大数组，然后我正在处理该数组中的每一件事，但我只取前三个。如果我告诉这个迭代器，我只需要前三个东西，一旦我们有了三个，它就会停止工作，停止要求更多的值。”

> “这就是我喜欢 JavaScript 的地方。我们不会回避这些事情。JavaScript 确实试图说这就是你将得到的。”
> **— Ashley Claymore, 彭博软件工程师**

这仅适用于同步迭代器。最初，迭代器助手提案包括另一个用于处理包含 promise 的迭代器的特性；该特性被分离到 [Sync 迭代器](https://github.com/tc39/proposal-async-iterator-helpers)（一个第 2 阶段提案）中，“因为一旦你将异步操作引入到其中，设计空间就会爆炸”。另一个第 2 阶段迭代器提案 [Iterator Chunking](https://github.com/tc39/proposal-iterator-chunking) 将允许开发人员从迭代器中检索多个值以一起处理（无论是数据块还是滑动窗口）。

[正如预期的那样](https://thenewstack.io/javascript-due-for-new-time-date-and-set-features-next-year/)，[用于组合和比较集合](https://github.com/tc39/proposal-set-methods) 的新方法（在支持集合的语言中很常见，而 JavaScript 长期以来一直缺乏这些方法）现在是该语言的一部分，填补了一个对于库来说太小，并且对于每个开发人员来说每次都难以做对的空白。到目前为止，你所能做的就是向集合中添加值或检查集合中是否存在某个值。“每个人都在一遍又一遍地编写这些小代码片段，” Palmer 指出。

看起来很简单但很棘手是该特性需要一段时间才能出现的原因之一，但正如集合方法的结果一样明确（它们只需要以数学和所有其他语言中的方式工作），重要的是要获得正确的执行顺序。

Claymore 解释说：“从抽象意义上讲，集合没有顺序，它只是一袋东西；你不知道哪个是第一个东西，哪个是最后一个东西。但是在 JavaScript 中，你可以使用迭代器循环遍历集合，因此存在可观测的顺序，如果你遍历所有内容并记录它，你将看到首先记录的是什么，最后记录的是什么。”

重要的是不要让它成为在不同实现中可能给出不同结果的东西。Claymore 补充说：“这就是我喜欢 JavaScript 的地方。我们不会回避这些事情。JavaScript 确实试图说这就是你将得到的。”

例如，虽然很容易说出两个集合的交集应该是什么，但计算效率取决于你如何处理不同大小的集合。

Claymore 说：“你真的只想循环遍历较小的两个集合中的一个。如果我有一个集合中只有一个项目，而另一个集合中有一百万个项目，那么交集将永远是零或一个项目，因此最有效的方法是基于较小的集合进行排序——但这意味着排序取决于哪个集合较小。我们必须讨论这个问题：这可以吗？开发人员是否会感到惊讶，有时你可能会得到 123，有时你可能会得到 231，这取决于哪个集合较小？”

> 与一致性相比，“显著”的性能差异胜出。

与一致性相比，“显著”的性能差异胜出，但对于几乎所有方法，关于排序应该是直观的还是高效的，都出现了相同的决定；挖掘细节以做出这些决定需要时间。

此外，由于 JavaScript 的大部分吸引力在于它是一种具有很大灵活性的动态语言，因此委员会需要严格定义哪些算作可以使用这些方法的有效集合。正如 Claymore 指出的那样，“拥有集合与数组或集合与映射的交集是否可以，因为它们具有非常相似的方法？”

最后，这归结为使有效集合的三个关键属性。

Claymore 说：“我们必须能够知道它的大小。你必须能够对它执行 .size，并且它必须返回一个我们可以转换为整数的数字，然后它必须有两个方法：has，以便我们可以立即询问它，你是否有这个东西？然后是一个 keys 方法，它为我们提供一个迭代器，以便我们可以循环遍历所有内容。”

这意味着你可以将新方法与具有所有这三个属性的映射一起使用，但不能与数组或字符串一起使用，因为它们没有这些属性。

## 在模块方面取得进展

[将使 JavaScript 模块具有 CommonJS 模块的完整特性](https://thenewstack.io/how-javascript-is-finally-improving-the-module-experience/)的 [整套提案](https://thenewstack.io/5-ways-javascript-is-improving-modules-for-developers/) 的工作仍在继续。Palmer 说：“我要说的是，至少其中一些基础现在已经落地。”

使用 with（不要与 [已弃用的 with 语句](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with) 混淆，该语句会更改 JavaScript 中的作用域）的 [导入属性](https://github.com/tc39/proposal-import-attributes/) 语法导入（例如）JSON 代码，并确信你得到的是 JSON 代码，这可以解决潜在的安全问题。

Palmer 解释说：“你可能认为你正在导入无害的数据，常规 JSON，但在 Web 上，文件名只是一个文件名；它不能保证其中的内容，并且它可能正在传递 JavaScript。”

最初的提案只是检查内容是否可以加载，但是因为你可能正在使用此选项从 CSS 导入样式，而这需要修改标头（以添加“Accept: text/css”），所以导入属性现在可以更改内容的加载方式；Palmer 建议这对于构建工具特别有用。

> “我们吸取了教训 [...] 特别是关于确保 JavaScript 委员会和其他 Web 组织在流程的早期进行对话。”
> **— Palmer**

因为 Chrome 已经发布了使用原始 assert 关键字的该功能的早期版本，并且因为 Node 嵌入了 V8 引擎，所以工具生态系统已经采用了它。取消发布意味着使用遥测来查看有多少网站会受到影响——因为虽然其他浏览器没有添加该功能，但 Chrome 足够大，其功能可以很快被采用。虽然当采用发生在工具而不是网站代码中时，迁移更容易，但对于工具作者来说，这仍然需要更多的工作。

Palmer 说：“就像印第安纳·琼斯电影一样，他用一袋沙子代替了宝藏，我们侥幸逃脱了，但是很明显，工具生态系统经历了与需要让人们转移相关的迁移痛苦。我们从中吸取了教训，特别是关于确保 JavaScript 委员会和其他 Web 组织在流程的早期进行对话；第 2 阶段是我们将来应该抓住这些东西的地方，因为一旦我们进入第 3 阶段，浏览器就有权发布。”

人们已经在导入属性之上进行构建。有一个 [JSON 模块提案](https://github.com/tc39/proposal-json-modules/)，其中包含如何导入 JSON 并确保你得到的是 JSON 的具体细节（最初是导入属性的一部分，并在同一时间达到第 4 阶段）。但还有一个名为 [导入字节](https://github.com/tc39/proposal-import-bytes) 的新提案，用于从任何类型的文件导入任意字节——例如你想要 [转换为 SVG](https://github.com/vercel/satori) 的照片或 Web 字体，这依赖于它。

> “这是一个运行时已经说我们想要使用此功能的情况……”
> **— Claymore**

导入字节在最新的 TC39 会议上展示时，直接从第 0 阶段跳到第 2 阶段，因为这是多个工具和运行时已经开始添加的功能。它位于 Deno、Bun、webpack、esbuild、Parcel 和 Moddable 中——但它们都使用不同的语法，因此开发人员必须检测他们的代码正在哪个平台上运行，并选择正确的语法。

Claymore 解释说：“这是一个运行时已经说我们想要使用此功能的情况。如果我们要这样做，让我们将其放入规范中并说明会发生什么。”

如此多的兴趣意味着该功能也可能快速通过其他阶段。

## **规范化正则表达式**

[重复名称捕获组](https://github.com/tc39/proposal-duplicate-named-capturing-groups) 允许你在正则表达式的两个部分中使用相同的名称，前提是其中只有一个可以匹配（因此你不需要仅仅因为你想匹配 2025 或 25 而想出“year”的巧妙同义词），[仅差一点就错过了 ECMAScript 2024](https://thenewstack.io/javascript-due-for-new-time-date-and-set-features-next-year/)，因此它很容易达到今年的截止日期。但这并不是对正则表达式的唯一改进。

JavaScript [长期以来一直需要](https://simonwillison.net/2006/Jan/20/escape/) 一种用于匹配和转义字符串中在正则表达式中具有特定含义的字符（如 $ 或“.”）的方法；[Regex Escaping](https://github.com/tc39/proposal-regex-escaping) 为开发人员提供了“你通常会导入一个库或尝试自己编写它并且可能出错的东西，” Claymore 说。

> “有时你希望正则表达式的一部分区分大小写，但另一部分不区分大小写。”
> **— Claymore**

JavaScript 还获得了与其他语言和正则表达式引擎相同的语法，用于使用 [模式修饰符](https://github.com/tc39/proposal-regexp-modifiers) 更改表达式内的大小写或多行标志。

Claymore 解释说：“有时你希望正则表达式的一部分区分大小写，但另一部分不区分大小写。过去，区分大小写与否是整个正则表达式的标志。现在你可以说：我希望整个事物都不区分大小写，除了这个部分，我希望这个部分区分大小写。”

## 更简洁的捕获

另一个已经摆在桌面上的提案通过添加 [Promise.try](https://github.com/tc39/proposal-promise-try) 而被推过了终点线，用于将函数包装在 promise 中，而无需提前知道该函数（可能在库中）是异步的并已经返回 promise，还是只是一个值。

Palmer 解释说：“当你调用函数时，我们有这些不同的可能性。你想要获得 promise 的结果，而不是抛出异常，这是非常非常常见的，因为这几乎是事情可能发生的第三种方式。promise 可以以积极的方式实现，[但]它可能会被拒绝：然后以第三种控制路径抛出异常是很奇怪的。”

Promise.try 意味着如果函数是同步的，它可以安全地立即运行。这节省了时间，但你不需要编写额外的代码（或从 npm 中提取库）来做到这一点。使用新语法，TypeScript 也可以更容易地推断 JavaScript 中发生的事情。

Claymore 补充说：“这样做更简单，代码在 TypeScript 中也运行得更好，因此你可以获得另一个不错的人体工程学优势。”

一种可能不会被广泛使用的底层功能——他建议，ECMAScript 2025 中的其他功能将在几乎每个代码库中使用——但对于任何使用 [高级图形](https://github.com/w3c/ColorWeb-CG/blob/main/canvas_float.md)、WebGPU 和 WebGL 或机器学习的人来说，都非常受欢迎，那就是新的半精度 Float16 TypedArray。它不会向 JavaScript 添加新的数字类型，但这意味着你可以选择只存储 16 位而不是 64 位，并节省一些内存。

> “开发人员只需表达他们想要做什么，它就会尽可能快。”
> **— Claymore**

Claymore 说：“JavaScript 已经有 8 位整数、16 位整数、64 位整数、64 位浮点数、32 位浮点数，但它没有 16 位浮点数，并且在过去几年中，16 位浮点数的价值确实得到了证明。在机器学习中，如果你可以拥有两倍数量的数字，即使这些数字的精度只有一半，那也是一件非常好的事情。即使这些权重本身包含的信息较少，机器学习模型在拥有更多权重时也能表现得更好。”

更多的 CPU 对更多的 API 想要使用的 16 位浮点数提供硬件支持，并且 WebGPU 可以使用它们，但没有一种从 JavaScript 与这些 API 交互的好方法。Claymore 说：“如果你尝试自己实现它，你必须非常低效地执行操作才能获取和操作这些位。”

此外，你自己的代码不会自动利用添加支持的新 CPU，因此即使在新硬件上它也会保持缓慢。

Claymore 说：“现在你有一个 Float16 数组，因此你可以以本机方式将你的 16 位浮点数降至 16 位。开发人员只需表达他们想要做什么，它就会尽可能快。”