<!--
title: Arcjet Python SDK：安全防护，代码原生集成！
cover: https://cdn.thenewstack.io/media/2026/01/3b66e0dd-anastasiya-romanova-ruj7cpp204a-unsplash-1.jpg
summary: Arcjet推出Python SDK，将应用层安全嵌入代码，支持速率限制和机器人检测。它利用WebAssembly进行本地分析，兼容FastAPI和Flask，以满足AI驱动下Python生态的安全需求。
-->

Arcjet推出Python SDK，将应用层安全嵌入代码，支持速率限制和机器人检测。它利用WebAssembly进行本地分析，兼容FastAPI和Flask，以满足AI驱动下Python生态的安全需求。

> 译自：[Arcjet's Python SDK Embeds Security in Code](https://thenewstack.io/arcjets-python-sdk-embeds-security-in-code/)
> 
> 作者：Darryl K. Taft

安全平台提供商 [Arcjet](https://arcjet.com/) 推出了 [Python](https://thenewstack.io/what-is-python/) SDK，旨在将应用层安全直接嵌入到代码中。

Arcjet 创始人兼首席执行官 [David Mytton](https://www.linkedin.com/in/davidmytton/) 表示，该 SDK（目前处于测试阶段）将 Arcjet 的安全平台扩展到基于 Python 的服务和 API，以满足客户需求和 AI 驱动的 Python 增长。

他告诉 The New Stack：“我们从 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 生态系统开始，因为大多数新应用都是通过全栈开发在那里构建的。”该公司最初支持 JavaScript 和 [TypeScript](https://thenewstack.io/what-is-typescript/) 应用。

然而，Mytton 在一份声明中说：“借助 Python SDK，我们将 Arcjet 的应用层方法扩展到全球最大的开发者生态系统之一。团队依赖 Python 来提供关键服务，从公共 API 到内部系统。此次发布为开发人员提供了一种清晰的方式，可以直接在代码中应用有意义的安全控制，而不会增加运营开销。”

Arcjet 收到了大量关于支持其他语言的请求，其中 Python 最受欢迎。

Mytton 写道：“[Django](https://thenewstack.io/what-is-pythons-django/) Python 框架是这方面的一个特殊推动因素，因为它在 Web 应用和 API 中广受欢迎，但 AI 用例加速了 Python 的普及。”

## Python 安全需求

事实上，随着 AI 开发推动 Python 采用，Python 安全变得越来越重要。

本周早些时候，领先的 AI 研究和产品公司 [Anthropic](https://www.anthropic.com/) 向 [Python 软件基金会](https://www.python.org/psf-landing/) (PSF) 投资了 150 万美元。这项投资将全面支持该基金会，特别是专注于 [Python 生态系统安全](https://thenewstack.io/whos-keeping-the-python-ecosystem-safe/)。

基金会表示，Anthropic 的资金将使 PSF 能够在其安全路线图上取得进展，包括旨在保护数百万 [PyPI](https://thenewstack.io/compiled-python-code-used-in-a-new-pypi-attack/) 用户免受供应链攻击的努力。

Mytton 说，Python 广泛用于后端服务和 API——特别是 AI 应用——但大多数安全工具在网络或边缘层运行。他解释说，Arcjet 将安全决策引入应用程序代码中，开发人员可以完全访问请求上下文和业务逻辑，从而使保护更准确、更易于管理。

Mytton 在博客中表示，总的来说，Arcjet Python SDK 支持应用层保护，包括速率限制、机器人检测、电子邮件验证和注册垃圾邮件预防。这些保护通过 Arcjet 的上下文决策引擎进行评估，并作为正常请求处理的一部分应用，允许团队根据用户活动、请求模式和特定于应用程序的信号来调整行为。

Arcjet SDK 提供构建块，使安全成为一项普通功能，无论部署环境如何。

## WebAssembly 组件

Arcjet 的方法涉及在其 SDK 中嵌入 [WebAssembly (Wasm)](https://thenewstack.io/webassembly/) 模块，从而能够以接近原生速度对传入请求进行本地分析。

Mytton 说，Wasm 模块由 [Rust](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/) 编译而来，为分析提供了一个安全沙箱，它是跨平台的，现在已扩展到 [JavaScript](https://thenewstack.io/web-app-development-sans-javascript-with-microsoft-blazor/) 之外的另一种语言。

他说：“Python SDK 的第一个版本已经为我们准备好框架，可以将 WebAssembly 位插入其中，这样我们就可以进行我们在 JavaScript 方面一直在进行的所有本地分析。”

此外，Mytton 解释说：“Wasmtime 允许我们在 Python 中执行 WebAssembly。” Wasmtime 是一个由 [Bytecode Alliance](https://thenewstack.io/webassembly-to-let-developers-combine-languages/) 托管的开源 WebAssembly 运行时，旨在作为大型堆栈的一部分或作为独立运行时使用。

正如 Arcjet 的 JavaScript SDK 一样，Python SDK 也使用 WebAssembly 进行本地安全分析。这目前处于测试/beta 阶段，但它使他们能够本地运行安全分析，而不仅仅是使用 API 客户端。

此外，Python SDK 同时支持 [FastAPI](https://github.com/arcjet/example-fastapi?ref=blog.arcjet.com) 风格（异步）和 [Flask](https://github.com/arcjet/example-flask?ref=blog.arcjet.com) 风格（同步）的 API。Arcjet 为 FastAPI 和 Flask 都提供了示例应用程序。