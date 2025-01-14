
<!--
title: 想用Rust而不是 JavaScript编写Web框架？试试 Leptos
cover: https://cdn.thenewstack.io/media/2025/01/1d76744b-getty-images-ybl2fiz32qo-unsplashb.jpg
-->

随着 WebAssembly 在 Web 开发中越来越受欢迎，像 Leptos 这样的框架允许您构建由 Rust 驱动的 Web 应用程序。

> 译自 [Want a Web Framework for Rust, Not JavaScript? Try Leptos](https://thenewstack.io/want-a-web-framework-for-rust-not-javascript-try-leptos/)，作者 Richard MacManus。

[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 在 Web 开发中的应用越来越广泛。特别是 Leptos 和 Sycamore 等 [Rust 框架](https://thenewstack.io/what-rust-brings-to-frontend-and-web-development/)，它们利用 Wasm 将 Rust 编译成快速、交互式的 Web 应用。

[Leptos](https://leptos.dev/) 将自己描述为“现代 Web 的前沿 Rust 框架”。该项目声称其 Web 性能仅次于原生 [JavaScript](https://thenewstack.io/javascript/)——它表示其性能优于 Vue、Svelte 和 React（根据引用的基准测试，性能是 React 的三倍；见下文）。

![](https://cdn.thenewstack.io/media/2025/01/0e050975-leptos-perf-jan25.jpg)

在 [其文档](https://book.leptos.dev/) 中，Leptos 表示它“最类似于 Solid（JavaScript）和 Sycamore（Rust）等框架”。这主要是因为它具有细粒度的反应式系统来进行更新和状态管理。“这意味着只有 UI 中发生变化的部分才会重新渲染，从而导致应用程序更高效且性能更好（没有虚拟 DOM！）”，[Leptos 指出](https://github.com/leptos-rs)。它也是基于组件的，并支持客户端渲染 (CSR) 和服务器端渲染 (SSR)。

在 [2024 年 1 月的 YouTube 视频](https://www.youtube.com/watch?v=xOVx4bM4t9U) 中，Leptos 创建者解释了该项目的起源。他受到了 Ruby on Rails 创建者 David Heinemeier Hansson (DHH) 曾说过的一句话的启发，大意是：Web 的魅力在于，只要它向最终用户提供 HTML，你就可以在服务器上运行任何你想要的东西。他表示，曾在创建 Leptos 之前“构建了许多 JavaScript 应用程序”，但这给他带来了问题。“当我学习 Rust 时，”他继续说道，“我只是觉得……这种语言给了我很多方法来避免我[用 JS]给自己带来的那些问题，而且我真的很想能够构建 Web 应用，这就是我想用它[Rust]做的事情。”

他补充说，正是 WebAssembly 的出现促使他创建了一个 Rust Web 框架。借助 Wasm，他使用 Leptos 的目标是“提供大致与 JavaScript 框架平行的体验，但在 Rust 中”。

![](https://cdn.thenewstack.io/media/2025/01/0048d371-leptos-playground.png)

*Leptos playground*

## Leptos 入门

开始使用 Leptos 有两种途径。如果你只需要一个简单的 CSR 网站，可以使用 [Trunk](https://trunkrs.dev/)，这是一个用于 Rust 的开源 Wasm Web 应用程序捆绑器。但如果你想要一个更复杂、全栈的 SSR 网站，那么 Leptos 通过其构建工具 [Cargo](https://github.com/leptos-rs/cargo-leptos) 支持这一点。

该项目表示：“如果想要 Rust 同时为你的前端和后端提供动力，SSR 是构建 CRUD 风格的网站和自定义 Web 应用的一个绝佳选择。”

> “……如果你愿意在过程中贡献一些缺失的部分，这个框架绝对可以使用。”
>
> – Leptos 创建者

Leptos 当前版本为 0.7.3，并且它自己也承认，它还不完全准备好用于生产环境。但是，维护者补充道：“如果你愿意在过程中贡献一些缺失的部分，这个框架绝对可以使用，特别是考虑到围绕它出现的库生态系统。”

因此，虽然该框架功能齐全，但需要注意的是，“生产就绪”取决于你愿意应对其当前限制的意愿。

## 性能和正确性

该项目每月在 YouTube 上举行一次虚拟聚会，在 [12 月底](https://www.youtube.com/watch?v=6-luPDoxAHo)，加入了主持人 Luke Skinner 进行了一次 AMA。在某个时刻，Skinner 观察到“想要用 Rust 进行开发的人”。一句话，这归结为对性能的热情。

Skinner 说：“对我来说，这就像一个原则问题——是的，我想榨取性能，是的，我希望它是完美的……或者尽可能完美。”

他表示同意，并补充说 Leptos 社区也痴迷于“正确性”——他解释说这意味着“以正确的方式做事，而不是以最简单的方式”。他给出了一个有趣的例子，将 Rust 与 Go 进行比较，解释了这两种语言如何处理包含无效 Unicode 字符的 Windows 文件名。

关于有问题的字符，他说：“Go 只会删除它们”，而“Rust 会返回一个结果。而且，有时候你……希望看到瑕疵和复杂性，然后被问到：你想如何处理这个问题？”

## Leptos 技术栈及其未来

在聊天的后期，被问到：“如果 Leptos 不存在，你会使用什么来构建个人项目的反应式 Web 应用？”

Johnston 在回应中提到了Angular、React、Solid、Svelte 5和Vue（都是JavaScript框架）。他表示Solid可能是他会选择的。他还提到他对React有疑虑。

“我不太喜欢React，”他说，“前端有很多很好的函数式编程语言，比如ReScript……或者之前的ReasonML，它就像是OCaml的另一种语法。但它们都只是用React作为后端，而我不喜欢React的模式。” 

Skinner 接着问 Johnston，除了Leptos和Rust之外，他2025年首选的技术栈会是什么？他表示如果他开始一个新项目，他会使用axum——一个Rust的Web应用框架——以及“某种客户端路由的岛屿模式”。

> “我认为我们正朝着一个我可以欣然称之为1.0的方向前进——这感觉像是正确的范式。”—— Johnston  

最后，一位观众询问Leptos 0.7是否处于“某种最终形态”，或者未来是否还会有重大变化。

“我认为这是最终形态，我不认为未来版本会有重大变化。”Johnston 回答道。在他的回答稍后部分，他又补充说：“我认为我们正朝着一个我可以欣然称之为1.0的方向前进——这感觉像是正确的范式。”


## 结论

无论是 Leptos 还是其竞争的基于 Rust 的 Web 框架 Sycamore（v0.9.1），都还没有达到 1.0 版本——因此，以 Rust 和 Wasm 为基础构建 Web 应用显然还不完全成熟。但如果你对性能和“正确性”有着执着的追求，那么你可能会对尝试使用这两个框架中的一个或两个感兴趣。

Wasm 这一方面尤其引人注目。随着 WebAssembly 在 Web 开发中的不断流行，像 Leptos 这样的框架让我们得以窥见高性能、由 Rust 驱动的 Web 应用的可能未来。尽管仍在不断发展，Leptos 已经证明了无需依赖 JavaScript 重度生态，也能构建响应式 Web 应用。

毕竟，Wasm 的一项承诺就是能够将几乎任何编程语言都转变为 Web 语言。