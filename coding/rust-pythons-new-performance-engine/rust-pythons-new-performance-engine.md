<!--
title: Rust：Python的性能新引擎
cover: https://cdn.thenewstack.io/media/2025/08/ff731826-andreas-brun-fjddh6iobqa-unsplash-1.jpg
summary: Rust正成为Python的性能助手。越来越多的Python项目使用Rust编写高性能组件，例如Polars、Pydantic V2和FastAPI。Rust不仅提升了性能，还提供了内存安全和更好的开发者体验。Python开发者应学习阅读Rust代码，并考虑使用Rust构建扩展。
-->

Rust正成为Python的性能助手。越来越多的Python项目使用Rust编写高性能组件，例如Polars、Pydantic V2和FastAPI。Rust不仅提升了性能，还提供了内存安全和更好的开发者体验。Python开发者应学习阅读Rust代码，并考虑使用Rust构建扩展。

> 译自：[Rust: Python's New Performance Engine](https://thenewstack.io/rust-pythons-new-performance-engine/)
> 
> 作者：Darryl K. Taft

[Python](https://thenewstack.io/what-is-python/) 开发者一直面临着一个权衡：编写优雅、可读的代码，还是追求高性能。长期以来，这意味着在速度至关重要时，需要借助 [C](https://thenewstack.io/code-wars-rust-vs-c-in-the-battle-for-billion-device-safety/) 扩展。但 [Rust](https://thenewstack.io/rust-programming-language-guide/) 已经成为 [Python 的性能](https://thenewstack.io/why-python-is-so-slow-and-what-is-being-done-about-it/) 助手。

## Rust 在 Python 中的变革

根据 [JetBrains](https://www.jetbrains.com/) 的 [State of Python 2025](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/) 报告，Rust 在 Python 二进制扩展中的使用率从 27% 跃升至 33%，仅一年就增长了 22%。这代表着 Python 生态系统在 [性能优化](https://thenewstack.io/how-to-master-javascript-performance-optimization/) 方面的一个关键转变。

在关于该研究的 [博客文章](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/) 中（该研究基于对 30,000 名开发者的调查），[Talk Python](https://talkpython.fm/) 的创始人兼 [Python Software Foundation](https://www.python.org/psf-landing/) 研究员 Michael Kennedy 写道：“在 [2025 Python Language Summit](https://us.pycon.org/2025/events/language-summit/) 上，核心开发者分享了一个令人大开眼界的统计数据：‘上传到 [PyPI](https://thenewstack.io/the-top-5-python-packages-and-what-they-do/) 的新项目的所有原生代码中，有四分之一到三分之一使用了 Rust。’ 这意味着，当今开发者启动新的对性能要求高的 Python 项目时，他们越来越多地选择 Rust 而不是传统的 C 扩展。”

## 为什么 Rust 胜过 C

Rust 在 Python 生态系统中迅速普及的关键原因之一是性能。Rust 在保持 Python 易于集成的同时，提供了 C 级别的性能。Rust 的 [零成本抽象](https://stackoverflow.com/questions/69178380/what-does-zero-cost-abstraction-mean) 和高效的内存管理使其成为对性能要求高的组件的理想选择。

Rust 还提供内存安全。与 C 不同，Rust 在编译时可以防止常见的编程错误，如 [缓冲区溢出和内存泄漏](https://thenewstack.io/secure-coding-in-c-avoid-buffer-overflows-and-memory-leaks/)。这使得扩展 Python 更加安全，而不会引入安全漏洞或崩溃。

此外，Rust 凭借其现代化的工具链、出色的错误消息和包管理器 ([Cargo](https://doc.rust-lang.org/cargo/))，提供了高质量的开发者体验。与编写和调试 C 扩展的痛苦过程相比，它提供了更好的开发体验。

## 真实世界的成功案例

Python 生态系统已经展示了几个引人注目的 Rust 成功案例：

* **Polars** 通过 DataFrame 操作彻底改变了数据科学，其性能通常比 [Pandas](https://thenewstack.io/python-pandas-ditches-numpy-for-speedier-pyarrow/) 高出几个数量级。它使用 Rust 构建，提供了一个感觉自然的 Python API，同时为数据处理任务提供了前所未有的速度。
* **Pydantic V2** 在 Rust 中重写了其核心验证引擎，从而为几乎所有 Python 学科（从 Web API 到机器学习管道）的数据验证和序列化带来了显著的性能提升。
* **FastAPI 的生态系统** 越来越依赖于基于 Rust 的组件。调查显示，[FastAPI](https://thenewstack.io/jetbrains-developer-survey-tracks-rapid-adoption-of-ai-chatgpt/) 的使用率从 29% 跃升至 38%（增长了 30%），部分原因是其异步友好的架构，可以与基于 Rust 的服务器组件很好地配合使用。

## 基础设施的变革

Rust 的影响超出了单个软件包，扩展到 Python 的核心基础设施。传统的 Web Server Gateway Interface (WSGI) 服务器正在让位于与 Asynchronous Server Gateway Interface (ASGI) 兼容的替代方案，其中许多是使用 Rust 构建的。Kennedy 提到了 [Granian](https://github.com/emmett-framework/granian)，这是一个新的基于 Rust 的应用服务器，正在获得显著的关注。他还特别提到了 [Uvicorn](https://www.uvicorn.org/)，它虽然是基于 Python 的，但越来越多地与 Rust 组件集成。

## 下一代工具

Kennedy 还指出，出现了两个新的 Python 类型检查器，都是用 Rust 编写的。一个是来自 [Astral](https://astral.sh/) 的 [ty](https://github.com/astral-sh/ty)，它被描述为“一个非常快速的 Python 类型检查器和语言服务器”。另一个是来自 Meta 的 [Pyrefly](https://pyrefly.org/)，它是传统类型检查器（如 [mypy](https://mypy-lang.org/)）的高性能替代品。

“它们都在争夺成为下一代类型检查工具。此外，这两种工具都提供了非常快速的语言服务器协议 (LSP)，” Kennedy 写道。

“注意到什么相似之处了吗？它们都是用 Rust 编写的，这印证了之前的说法，即‘Rust 已经成为 Python 的性能助手，’” 他补充道。

## 商业案例

与此同时，对于企业而言，Rust 增强的 Python 带来了切实的利益。仅性能改进就可以转化为成本节约，包括降低云计算成本和降低内存使用率。此外，更快的响应时间可以提高客户满意度，更高效的代码可以降低能源消耗，Kennedy 说。

## 给 Python 开发者的建议

Kennedy 建议 Python 开发者学习阅读 Rust。

Python 开发者应该考虑学习 Rust 的基础知识，不是为了取代 Python，而是为了补充它。

“正如我在我们的分析中讨论的那样，Rust 在 Python 生态系统最重要的部分中变得越来越重要，” Kennedy 写道。“我绝对不建议你成为 Rust 开发者而不是 Pythonista，但能够阅读基本的 Rust，以便你了解你正在使用的库在做什么，将是一项有用的技能。”

Kennedy 还建议 Python 开发者拥抱 Rust 增强的库。在选择类似的软件包时，请考虑那些具有 Rust 内核的软件包——它们通常提供卓越的性能，而不会牺牲 Python 的易用性，他说。

Kennedy 建议，Python 开发人员还应该考虑使用 Rust 进行扩展。构建对性能要求高的 Python 扩展的 Python 开发者应该评估 Rust 作为他们的实现语言，而不是默认使用 C，他指出。

## 未来是混合的

总的来说，Rust 并没有取代 Python，而是增强了它。报告表示，这种混合方法为开发者提供了两全其美的优势：Python 的表达能力和生态系统用于应用逻辑，而 Rust 的性能用于计算密集型组件。