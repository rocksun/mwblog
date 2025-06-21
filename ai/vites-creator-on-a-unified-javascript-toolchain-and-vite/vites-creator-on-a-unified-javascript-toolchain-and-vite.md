<!--
title: Vite作者谈统一JavaScript工具链与Vite+
cover: https://cdn.thenewstack.io/media/2025/06/11d0d7fe-ethanyoupresentation.jpg
summary: Vite 和 Vue 的创建者 Ethan You 正在构建 Vite+，旨在为 JavaScript 提供一个统一的工具链，类似于 Rust 的 Cargo。该项目包括 Vite、Vitest、Rolldown 和 OXC 等工具，涵盖打包、测试、代码检查和格式化等功能。Vite+ 旨在简化 JavaScript 开发流程，解决生态系统碎片化问题。
-->

Vite 和 Vue 的创建者 Ethan You 正在构建 Vite+，旨在为 JavaScript 提供一个统一的工具链，类似于 Rust 的 Cargo。该项目包括 Vite、Vitest、Rolldown 和 OXC 等工具，涵盖打包、测试、代码检查和格式化等功能。Vite+ 旨在简化 JavaScript 开发流程，解决生态系统碎片化问题。

> 译自：[Vite’s Creator on a Unified JavaScript Toolchain and Vite+](https://thenewstack.io/vites-creator-on-a-unified-javascript-toolchain-and-vite/)
> 
> 作者：Loraine Lawson

作为 Vite 插件推出的框架将具有优势，例如 [Remix React Router](https://thenewstack.io/remix-react-router-merge-jetbrains-ide-for-test-automation/)、TanStack 和 Redmond 已经实现的，[Ethan You](https://github.com/yyx990803)（[Vite](https://thenewstack.io/how-to-build-a-server-side-react-app-using-vite-and-express/) 和 JavaScript 框架 [Vue](https://thenewstack.io/a-peek-at-whats-next-for-vue/) 的创建者）表示。

You 现在正在为 JavaScript 生态系统创建一个新的统一工具链，并且在 [JSNation 2025 会议](https://gitnation.com/events/jsnation-2025) 期间提供了 [该项目的最新信息](https://gitnation.com/contents/vite-and-the-future-of-javascript-tooling)，该会议在阿姆斯特丹举行，并在 GitNation 平台上进行了部分虚拟展示。

他还介绍了仍在开发中的 Vite+ 的概念。它的目标是像 Cargo 对 [Rust](https://thenewstack.io/rust-programming-language-guide/) 所做的那样，对 JavaScript 工具进行改造——[Cargo](https://doc.rust-lang.org/rust-by-example/cargo.html) 是 Rust 的包管理器和构建系统。

“Remix React Router、[TanStack Start](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/)、[Redwood SDK](https://rwsdk.com/) 都在朝着这个方向发展，这是一种非常聪明的方式来利用 [Vite](https://thenewstack.io/development-server-vite-gets-independent-team-and-rust-ifies/)，以及 Vite+ 的未来特性，因为将来，当你将你的框架作为 Vite+ 插件发布时，你还可以挂钩到这些额外的命令，”You 说。“当你可以通过插件接口访问完整的工具链时，可能性是无限的。”

越来越多的前端框架建立在开发服务器 Vite 之上或已迁移到该服务器，包括 Angular、Astro Qwik、Redwood、Remix、Solid 和 SvelteKit。最终，他在 Vite 上的工作使 You 相信 JavaScript 需要更好的工具链。

“我们一直在思考我们可以做些什么来使 Vite 更好地发挥这个作用，我们得出的结论是，Vite 在目前的状态下远非完美，”他说。

> “如果我们研究打包器，并查看打包器需要的所有较低级别的依赖项，（我们）意识到 JS 生态系统实际上在每一层都存在碎片化。”
> **– Ethan You, Vite 和 Vue 的创建者**

具体来说，You 发现 Vite 依赖于具有重叠职责的第三方依赖项。

“问题在于，这些工具中的许多工具都有重叠的职责。它们是用不同的语言编写的，”他说。“在这些工具之间来回传递数据时，存在许多效率问题，并且它们在打包或转换时都有稍微不同的行为。”

该团队决定构建一个名为 Rolldown 的打包器，目标是用一个统一的构建工具替换 esbuild 和 Rollup（目前在 Vite 中用作依赖项）。

但这有点像那些“[如果你给老鼠一块饼干](https://en.wikipedia.org/wiki/If_You_Give_a_Mouse_a_Cookie)”的书，构建打包器意味着他们还需要挑选和选择使用哪个 linter，使用哪个转换器等等。

“当你深入研究时，你会意识到 Vite 面临的挑战实际上反映了整个 JavaScript 生态系统，”他说。“如果我们研究打包器，并查看打包器需要的所有较低级别的依赖项，（我们）意识到 JS 生态系统实际上在每一层都存在碎片化。”

这导致了决策疲劳，并且对于刚开始从事 JavaScript 开发的普通用户来说，这是压倒性的。虽然蓬勃发展的 JavaScript 生态系统使开发人员能够创建更雄心勃勃的应用程序，但随着该语言的成熟，它导致了“每个人的复杂性税”，You 说。

“我认为现在是 JavaScript 应该拥有统一工具链的时候了，”他说。为此，他创立了 [void(0)](https://voidzero.dev/team)，发音为“Void Zero”。

## Void(0) 的重点

Void(0) 团队正在研究四个主要部分：

*   **[Vite](https://github.com/vitejs/vite)**
*   **[Vitest](https://vitest.dev/guide/why)**，一个测试运行器，可以单独在任何 JavaScript 项目中使用。
*   [**Rolldown**](https://github.com/rolldown/rolldown)，一个用于 JavaScript/TypeScript 的 Rust 打包器，具有与 Rollup 兼容的 API。它在内部支持 Vite 和 Vitest。它最初由 Yinan Long 创建，但现在由 You 领导。据 You 称，它目前处于 1.0 beta 状态。“你已经可以将其用作 Rollup 的几乎直接的替代品，并且你将看到性能的显着提高，”You 说。它带有内置的 Node 兼容解析，因此开发人员不需要为此使用插件，他补充说。它还支持 90% 的 Rollup 插件接口兼容性，因此虽然它是一个 Rust 打包器，但它确实支持 JavaScript 插件，他补充说。
*   **[OXC](https://oxc.rs/)**，JavaScript Oxidation Compiler，是一组工具，包括 linter、解析器、解析器、压缩器（目前处于 alpha 状态）和格式化程序（仍在建设中）。[Oxlint 的第一个稳定版本](https://voidzero.dev/posts/announcing-oxlint-1-stable) 于 2025 年 6 月 9 日发布。

许多工具已经完成，包括 OXC 的解析器、linter、解析器和转换器。

“我们构建的大多数这些东西都是同类产品中最快的，即使与其他也用本机语言编写的解决方案相比，”他说。“解析器、链接器、解析器、转换器都是同类产品中最快的。压缩器是第二快的，但它也比最快的解决方案具有更好的压缩率，因此它仍然是一个非常不错的选择。”

他补充说，未来有计划提高压缩器的压缩率。

## OXC 工具集更新

了解所有工具的功能有助于理解 You 正在构建的内容。

解析器采用原始 JavaScript 代码，并将其转换为称为 [抽象语法树 (AST)](https://daily.dev/blog/js-parser-essentials-for-developers#:~:text=So%2C%20to%20sum%20it%20up,them%20into%20a%20tree%20diagram) 的结构化、分层表示。AST 是一种树状数据结构，其中每个节点代表代码中的一个 [构造](https://nearform.com/insights/what-is-an-abstract-syntax-tree/)，例如，变量声明、函数调用或 if 语句。它是程序的语法结构和内容，没有“表面”细节，例如空格或注释。

解析器已完全完成，并且 Void(0) [基准测试](https://github.com/oxc-project/bench-javascript-parser-written-in-rust) 发现它比基于 Rust 的编译器 Speedy Web Compiler (SWC) 快三倍，后者包括一个解析器。

[![](https://cdn.thenewstack.io/media/2025/06/adb6cb51-oxc_toolit.png)](https://cdn.thenewstack.io/media/2025/06/adb6cb51-oxc_toolit.png)

Evan You 团队创建的 OXC 工具集。

AST 是几乎所有其他 JavaScript 工具完成其工作所需的基本输入。

压缩器使用 AST 来安全地重命名变量、删除死代码并优化代码结构，而不会改变其功能。它基本上 [从源代码中删除所有不必要的字符](https://wysiwyg-editor.froala.help/hc/en-us/articles/360000185869-What-is-the-difference-between-minified-and-unminified-source-code)，而不会改变其功能。Webpack、Rollup、Vite、Terser（一种流行的 JavaScript 压缩器）和 Esbuild 等工具都将压缩作为其优化管道的一部分。

[Linter](https://owasp.org/www-project-devsecops-guideline/latest/01b-Linting-Code) 强制执行编码风格，识别潜在的错误或突出显示可疑的模式。

[打包器](https://career.comarch.com/blog/javascript-bundlers-is-it-worth-switching-from-webpack-to-vite/)（例如 Webpack、SWC 和 Rollup）将各个模块解析为 AST，以了解它们的依赖关系并有效地组合它们。对于生产构建，Vite 充当打包器，使用 Rollup 将应用程序的代码编译和优化为高效、可用于生产环境的包。Vite 也可以与 Speedy Web Compiler (SWC) 一起使用，后者是用 Rust 编写的 JavaScript 和 TypeScript 编译器，也可用于打包。Vite 正在开发自己的打包器，称为 [Rolldown](https://rolldown.rs/)。

代码格式化程序将代码解析为 AST，然后以一致的样式将其打印出来。Void(o) 已经完成了一个原型格式化程序，但它尚未可用。

转换编译器获取 AST（例如，现代 JavaScript），并将其转换为另一个 AST（例如，旧 JavaScript），然后再将其转换回代码。Void(o) 构建了一个与 [Babel](https://babeljs.io/) 兼容的转换器，该转换器将 TypeScript 转换为 ESNext，并将 React JSX 转换为 ESNext。转换器是更广泛的工具类别，它们以各种方式修改代码，因此包括转换编译器。

## 即将推出：Vite+

Vite+ 仍处于早期开发阶段，但其理念来自 Cargo，Cargo 是 Rust 的包管理器和构建系统。

“如果你使用过 Rust，你可能知道 Cargo 是一个集所有功能于一体的工具包、工具链，可以满足 Rust 开发期间的大部分开发工作流程需求，”You 说。“JavaScript 中没有类似的东西，而 Vite+ 正是我们试图构建以满足这一角色的东西。”

开发人员可以将他们的包管理器指向 Vite+，就可以开始了，他说。

“今天在 Vite 中工作的所有内容将继续以完全相同的方式工作，但 Vite 命令行变得更加强大，”他说。“现在它配备了额外的命令，例如 Vite lib，它专用于库打包、Vite 测试和基准测试 Vite 链接以进行格式化、Vite 新建用于项目脚手架、Vite 任务用于 monorepo 任务编排和构建缓存。”

它将具有 GUI 开发工具、工作区审核和企业用户的策略执行。该团队还可能通过内置的 MCP 服务器提供与 AI 集成的 Vite+，他补充说。他还补充说，还额外支持 [monorepos](https://thenewstack.io/the-case-for-and-against-monorepos-on-the-frontend/)。

“Vite+ 将能够识别 monorepo，这意味着我们将拥有管道、构建、编排、缓存——类似于 Turborepo 的功能——并且我们将拥有头等概念工作区和策略执行，”You 说。