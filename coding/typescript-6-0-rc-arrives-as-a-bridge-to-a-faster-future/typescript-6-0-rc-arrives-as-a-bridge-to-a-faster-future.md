<!--
title: TypeScript 6.0 RC：通往更快未来的过渡桥梁
cover: https://cdn.thenewstack.io/media/2026/03/4263f83c-compagnons-lyna7tjmork-unsplash-1.jpg
summary: TypeScript 6.0 RC发布，作为通向7.0 Go重写版本的桥梁。它带来了Temporal API等新功能，并弃用旧特性、默认开启严格模式，同时更改了`types`字段默认行为，为开发者平稳过渡到更快版本做准备。
-->

TypeScript 6.0 RC发布，作为通向7.0 Go重写版本的桥梁。它带来了Temporal API等新功能，并弃用旧特性、默认开启严格模式，同时更改了`types`字段默认行为，为开发者平稳过渡到更快版本做准备。

> 译自：[TypeScript 6.0 RC arrives as a bridge to a faster future](https://thenewstack.io/typescript-6-0-rc-arrives-as-a-bridge-to-a-faster-future/)
> 
> 作者：Darryl K. Taft

TypeScript 6.0 发布候选版本 (RC) 来了，从某些方面来看，它是自该项目在 2014 年发布 1.0 版本以来最具影响力的版本。并非因为它充满了华丽的新功能——尽管确实有一些——而是因为它所奠定的基础。

微软的 [TypeScript](https://thenewstack.io/what-is-typescript/) 团队一直在并行开发 [用 Go 重写编译器](https://thenewstack.io/go-power-microsofts-bold-bet-on-faster-typescript-tools/)，Go 是一种为速度而构建的系统编程语言。这次重写将作为 TypeScript 7.0 发布。6.0 版本是过渡版本：[旧引擎的最后一个版本](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)，在切换之前进行了优化并指向了正确的方向。团队表示 7.0 将很快推出——可能在几个月内。

## 实际新功能

最实用的新增功能是支持 [**Temporal API**](https://www.w3schools.com/js/js_temporal.asp)，它是 JavaScript `Date` 对象的迟来替代品。Temporal 为开发人员提供了处理日期、时间和时区的适当工具，而无需依赖 `date-fns` 或 `Luxon` 等第三方库。TypeScript 现已内置到类型定义中，因此开发人员可以立即开始尝试。

此外，新增了 **Map.getOrInsert** 和 **RegExp.escape** 的类型，这两个 ECMAScript 提案刚刚达到第 4 阶段——实际上已定稿。前者消除了在设置默认值之前检查 Map 键是否存在的一种常见模式。后者处理在字符串用于正则表达式之前转义特殊字符的问题，这是开发人员几十年来一直手动进行的工作。

在开发体验方面，`dom.iterable` 现已合并到核心 `dom` 库中，因此迭代 DOM 集合不再需要单独的配置条目。它现在开箱即用。

## 移除或弃用内容

6.0 版本更重要的部分是清理工作。此版本弃用或移除了大量在 2014 年有意义但在 2026 年看起来像古老遗物的选项。

**ES5 输出已移除。** Internet Explorer 已死，TypeScript 承认了这一点。仍然需要 ES5 输出的开发人员被引导至使用外部工具。

**AMD、UMD 和 SystemJS 模块格式已弃用。** 这些是打包器出现之前的模块系统。Webpack、Vite 和 esbuild 等现代工具已使它们过时。ESM 是标准。

`strict` **现在默认为 true。** TypeScript 的严格模式可以捕获大量常见错误，但以前是可选的。从 6.0 RC 开始，它默认开启。依赖旧的宽松默认值的项目需要显式设置 `"strict": false`——尽管团队更希望你解决潜在问题。

`--baseUrl` **已弃用。** 许多配置使用它来设置路径别名并避免深度嵌套的相对导入。该选项在 6.0 中已弃用，在 7.0 中将被移除。解决方案是将映射移至 `paths` 设置中，该设置长期以来一直独立处理此问题。

## 最可能导致破坏性更改

一个配置更改值得单独说明。TypeScript 配置中的 `types` 字段以前默认加载 `node_modules/@types` 中找到的每个包——这可能是数百个声明文件，其中大部分与当前项目无关。

在 TypeScript 6.0 中，默认值现在是一个空数组。没有东西会自动加载。依赖 `@types/node`、`@types/jest` 或类似包的全局类型的项目需要明确声明它们：

`"types": ["node", "jest"]`

团队表示，仅此更改就可以将构建时间缩短 20% 到 50%。但如果开发人员在不了解背景的情况下遇到此问题，将会看到一连串“无法找到名称”的错误，并想知道哪里出了问题。

## 总结

TypeScript 6.0 是一个开发人员主要会在其配置中而不是代码中感受到的版本。真正的重头戏——原生 [Go](https://thenewstack.io/introduction-to-go-programming-language/) 编译器、并行类型检查、显著更快的构建——将在 7.0 中到来。

目前，需要升级到 6.0，解决弃用警告，并明确设置 `types` 数组。微软表示，现在完成这些工作的团队将在 7.0 到来时获得更平稳的过渡。

TypeScript 6.0 RC 可通过 npm 获取：`npm install -D typescript@rc`。