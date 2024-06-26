
<!--
title: TypeScript 5.5：更快、更智能、更强大
cover: https://cdn.thenewstack.io/media/2024/06/8465ea7a-hotwheels.png
-->

TypeScript 5.5 为 JavaScript 开发带来了新的功能和性能增强，提升了标准。

> 译自 [TypeScript 5.5: Faster, Smarter and More Powerful](https://thenewstack.io/typescript-5-5-faster-smarter-and-more-powerful/)，作者 Darryl K Taft。

[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 最近发布了 [TypeScript](https://thenewstack.io/what-is-typescript/) 5.5，提供了一系列功能和优化，以增强该公司 [JavaScript](https://thenewstack.io/outer-excuses-why-javascript-developers-should-learn-sql/) 超集。

此更新包括推断类型条件、改进的表达式验证和单独声明，以及显着的性能提升和对编辑器可靠性的增强。

## 更好的开发人员体验

此版本侧重于改善开发人员的体验。TypeScript 5.5 旨在提供更快的构建流程和更强大的工具辅助。

“在我们的代码中编写类型使我们能够解释意图并让其他工具检查我们的代码以捕获错误，例如拼写错误、`null` 和 `undefined` 的问题等等，”Microsoft TypeScript 首席产品经理 [Daniel Rosenwasser](https://www.linkedin.com/in/daniel-rosenwasser-b56b7837/) 在一篇 [博客文章](https://devblogs.microsoft.com/typescript/author/danielrosenwasser) 中写道。“类型还为 TypeScript 的编辑器工具提供支持，例如您可能在 [Visual Studio](https://thenewstack.io/microsoft-visual-studio-2017-devops-five-star-app/) 和 [VS Code](https://thenewstack.io/this-week-in-programming-all-hail-visual-studio-code/) 等编辑器中看到的自动完成、代码导航和重构。事实上，如果您在这两个编辑器中的任何一个中编写 JavaScript，那么这种体验是由 TypeScript 提供支持的！”

自 TypeScript 5.5 的 beta 版和候选发布版以来，Microsoft 对该语言进行了一些更改。

例如，“自 beta 版以来，我们 [添加了对 ECMAScript 新 Set 方法的支持](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/#support-for-new-set-methods)。此外，我们调整了 [TypeScript 新正则表达式检查](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/#regular-expression-syntax-checking) 的行为，使其稍微宽松一些，同时仍然对仅根据 [ECMAScript](https://thenewstack.io/the-new-javascript-features-coming-in-ecmascript-2023/) 的附录 B 允许的 questionable 转义进行错误处理，”该帖子说。

Microsoft 还添加并记录了更多 [性能优化](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/#performance-and-size-optimizations)：值得注意的是，在 `transpileModule` 中跳过检查以及 TypeScript 过滤上下文类型的优化方式。该公司表示，这些优化可以缩短构建和迭代时间。

## 主要新功能摘要

TypeScript 5.5 中主要新功能和改进的总结亮点包括：

- 推断类型谓词：在某些情况下改进类型推断，尤其是在数组和过滤方面。
- 针对常量索引访问的控制流缩小：增强对对象属性访问的类型缩小。
- JSDoc `@import` 标签：用于在 JavaScript 文件中导入类型的新标签，不会影响运行时。
- 正则表达式语法检查：对正则表达式进行基本语法检查，以捕获常见错误。
- 支持新的 ECMAScript `Set` 方法：为提议的新 `Set` 方法添加声明。
- 独立声明：新的编译器选项，有助于更快地生成声明文件。
- `${configDir}` 模板变量：有助于编写更便携的配置文件。
- 咨询 `package.json` 依赖项：通过考虑包依赖项来改进声明文件生成。
- 编辑器和监视模式可靠性改进：各种修复以改善编辑器体验和监视模式。
- 性能和大小优化：对编译器速度和包大小的多个改进。
- 更轻松地从 ECMAScript 模块中使用 API：更好地支持在 ESM（ECMAScript 模块）环境中使用 TypeScript 的 API。
- `transpileDeclaration` API：用于为单个文件生成声明文件的新 API。

## 持续交付

Constellation Research 分析师 [Holger Mueller](https://www.linkedin.com/in/holgermueller/) 回顾了 TypeScript 的首次发布，他说：“Microsoft 继续投资 TypeScript 5.5 版本。——即使第一个 .5 版本的发布可能表明速度放缓。但从本质上讲，TypeScript 已经交付并继续交付其发明目的：使基于 JavaScript 的应用程序扩展到企业级规模。此版本在各个方面都提供了新功能，没有哪一项特别突出，使其成为 TypeScript 开发人员的“无聊”但有效的版本。”

此版本还包括一些行为更改，例如禁用 TypeScript 5.0 中弃用的功能。下一个版本 TypeScript 5.6 计划于 9 月初发布。

与此同时，Omdia 分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 指出：“简而言之，我认为 5.5 更新展示了这种相对较新的语言在解决软件稳定性和可扩展性方面的重要需求方面取得了多大的进步；它也展示了 TypeScript 从其 JavaScript 根源中走了多远。我认为可以公平地说，随着正则表达式语法检查等新功能的出现（这些功能以前在编译时被忽略），TypeScript 在支持企业级部署方面越来越像 Java 了。”

