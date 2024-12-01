
<!--
title: Deno申请撤销Oracle的JavaScript商标
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
-->

在其他开发者新闻方面，了解Vite团队为何将Vite 6称为重大版本发布，并了解Tailwind CSS 4.0 beta 1。

> 译自 [Deno Petitions to Cancel Oracle’s JavaScript Trademark](https://thenewstack.io/deno-petitions-to-cancel-oracles-javascript-trademark/)，作者 Loraine Lawson。

Deno正在向美国专利商标局（USPTO）请愿，要求取消甲骨文公司对JavaScript的商标权，Deno的创造者Ryan Dahl在周一宣布。

“这标志着将‘JavaScript’从法律纠纷中解放出来，并承认其为共享公共产品的关键一步，”Dahl写道。

Deno是一个用于JavaScript、TypeScript和WebAssembly的开源运行时环境。Dahl因其创建Node.js而在前端社区享有盛名。他指出，如果这一努力成功，社区可以宣称JavaScript，将其作为会议和规范推广，而不是目前的“ECMAScript”。

请愿书声称JavaScript是一个通用的、普遍的编程语言名称，甲骨文既不控制也从未控制过该语言的规范或使用。它还声称甲骨文在2019年续签JavaScript商标时向美国专利商标局提交了欺诈性证据。

“这包括Node.js的截图——这个项目是由我自己创立的，与甲骨文完全无关，”达尔写道。“将Node.js作为甲骨文‘商业使用’的证据违反了商标法的完整性。” 

最后，达尔声称甲骨文通过2009年收购Sun Microsystems获得了商标，但由于不使用而有效地放弃了它。

“请愿书表明甲骨文多年来没有在‘JavaScript’这个名字下提供重要的产品或服务，”他说。“像JavaScript扩展工具包或GraalVM这样的鲜为人知的产品，并不构成真正的商业使用。美国法律认为连续三年未使用的商标为废弃，甲骨文的不作为显然达到了这个门槛。”

## Vite 6 发布

其他新闻中，Vite 6于周二发布，Vite团队称其为“自Vite 2以来最重要的主要版本”。快速查看GitHub变更日志就明白了——它包含了大量的破坏性变更、特性、修复和杂项。

团队报告称，采用率持续增长——自Vite 5发布以来，每周npm下载量从750万跃升至1700万。他们还向新加入Vite生态系统的框架表示致敬，包括TanStack Start、One和Ember。

Vite 6支持Node.js 18、20和22+，但已放弃对Node.js 21的支持（Vite在Node.js版本生命周期结束后放弃对其的支持）。

团队还介绍了新的环境API，这是实验性的，主要针对框架作者。

博客文章指出：“这些新API将允许框架作者提供更接近生产的开发体验，并让生态系统共享新的构建块。”“如果你是在构建SPA；当你使用Vite与单一客户端环境时，一切如旧。即使是自定义SSR应用，Vite 6也是向后兼容的。”

有一个迁移指南，但列出的Vite 6的主要变更包括：

* [Default value for `resolve.conditions`](https://vite.dev/guide/migration.html#default-value-for-resolve-conditions)
* [JSON stringify](https://vite.dev/guide/migration.html#json-stringify)
* [postcss-load-config](https://vite.dev/guide/migration.html#postcss-load-config)
* [Extended support of asset references in HTML elements](https://vite.dev/guide/migration.html#extended-support-of-asset-references-in-html-elements)
* [Sass now uses modern API by default](https://vite.dev/guide/migration.html#sass-now-uses-modern-api-by-default)
* [Customize CSS output file name in library mode](https://vite.dev/guide/migration.html#customize-css-output-file-name-in-library-mode)

## Tailwind CSS Releases V4.0 Beta 1
上周晚些时候，Tailwind 发布了 4.0 Beta 1 版本。大约八个月前，Tailwind CSS 团队开源了他们的进展，此次发布紧随其后，此外，Tailwind 开发者描述了“数百小时的 bug 修复、令人沮丧的向后兼容性工作以及 Windows CI 故障排除”。

结果，他写道，这是一个“为性能而构建，专为现代网络设计的全新引擎”。据说完整构建速度提高了 5 倍，增量构建速度提高了 100 多倍，以微秒为单位测量。

它还有一个统一的工具链和 CSS 优先配置。它专为现代网络而设计，因为它“建立在原生级联层、广色域颜色之上，并包括对现代 CSS 特性（如容器查询、`@starting-style`、弹出窗口等）的一流支持”。

团队还发布了 beta 文档，以帮助开发者入门。
