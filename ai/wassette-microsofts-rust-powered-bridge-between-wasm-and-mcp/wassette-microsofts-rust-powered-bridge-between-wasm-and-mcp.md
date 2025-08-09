
<!--
title: Wassette：微软 Rust 技术打造 Wasm 与 MCP 的桥梁
cover: https://cdn.thenewstack.io/media/2025/08/47004f38-planet-volumes-tvwelcgs1w-unsplash.jpg
summary: 微软发布了 Rust 驱动的 Wassette 运行时，它使 AI 代理能够安全地获取和执行新功能。Wassette 利用 WebAssembly 和模型上下文协议 (MCP)，允许代理从开放容器注册表中下载和执行工具，扩展了代理的能力并提高了安全性。
-->

微软发布了 Rust 驱动的 Wassette 运行时，它使 AI 代理能够安全地获取和执行新功能。Wassette 利用 WebAssembly 和模型上下文协议 (MCP)，允许代理从开放容器注册表中下载和执行工具，扩展了代理的能力并提高了安全性。

> 译自：[Wassette: Microsoft’s Rust-Powered Bridge Between Wasm and MCP](https://thenewstack.io/wassette-microsofts-rust-powered-bridge-between-wasm-and-mcp/)
> 
> 作者：Darryl K. Taft

微软的 [Azure Core Upstream](https://github.com/Azure/container-upstream) 团队本周发布了 [Wassette](https://github.com/microsoft/wassette)，这是一个由 [Rust](https://thenewstack.io/rust-programming-language-guide/) 驱动的运行时，它可能会从根本上改变 [AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 获取和执行新功能的方式。

Wassette 构建在经过实战检验的、基于 Rust 的 [Wasmtime](https://thenewstack.io/webassemblys-wasmtime-1-0-revamps-security-performance/) [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 运行时之上，并利用了 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)，使 AI 代理能够自主下载、审查和安全地执行工具，同时保持浏览器级别的安全隔离。

微软表示，该运行时允许代理自主地从 [开放容器倡议 (OCI) 注册表](https://opensource.microsoft.com/blog/2024/09/25/distributing-webassembly-components-using-oci-registries/) 中获取 [WebAssembly 组件](https://component-model.bytecodealliance.org/design/why-component-model.html)，并根据需要执行它们。

Wassette 充当了两种前沿技术之间的桥梁：WebAssembly 组件和 MCP，后者已成为 AI 代理与外部工具和服务交互的标准方式。但到目前为止，代理仅限于预配置的工具集。

微软高级开发者倡导者和 [Rust Async Working Group](https://github.com/rust-lang/wg-async) 成员 [Yoshua Wuyts](https://www.linkedin.com/in/yoshuawuyts/?originalSubdomain=dk) 在一篇 [博客文章](https://opensource.microsoft.com/blog/2025/08/06/introducing-wassette-webassembly-based-tools-for-ai-agents/) 中解释说，Wassette “知道如何解释 Wasm 组件的类型化库接口，并将它们作为 MCP 工具公开”。

这种转换层意味着任何 WebAssembly 组件都可以立即提供给 MCP 兼容的 AI 代理，而无需自定义集成工作。

MCP 正在迅速成为 AI 代理工具集成的标准协议，并得到了 GitHub Copilot、Claude 等主要平台的支持。通过使 WebAssembly 组件与 MCP 兼容，Wassette 有效地向 AI 代理开放了整个 WebAssembly 生态系统。

Enterprise Strategy Group 的应用程序现代化首席分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk/) 告诉 The New Stack：“允许 AI 代理通过 MCP 使用 Wasm 应用程序，正是服务器端 WebAssembly 的设计初衷。如果进一步考虑，AI 代理可以通过 MCP 将 Wasm 应用程序链接在一起来组装应用程序。您甚至可以给代理一个财务预算来购买或订阅特定的 Wasm 应用程序，当然，应用程序所有者可以将更新推送到注册表，供‘付费’AI 代理直接使用。”

Wuyts 写道，Wassette 的入门非常快速、简单，并且适用于任何支持 MCP 的 AI 代理。MCP 集成意味着该工具可以与任何 MCP 兼容的 AI 平台无缝协作，包括 GitHub Copilot、[Claude Code](https://thenewstack.io/anthropic-adds-auto-security-reviews-to-claude-code/)、[Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) 和 [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/)。

## 教会代理进行“补给”

Wuyts 写道：“在最基本的层面上，AI 代理的目标是成功完成您交给它的任何基于计算机的任务，而无需太多人工干预。”

然而，今天的代理受到其预安装的工具集的限制。Wassette 改变了这一点。

Wuyts 写道：“我们可以将其视为教代理如何进行补给：识别需要什么，并弄清楚如何获得它。”

这是关于创建能够按需发展其能力的自主系统。当 AI 代理遇到需要网络请求、时间计算或文件处理的任务时，它现在可以识别缺少的工具，从容器注册表中获取它并安全地执行它，该文章称。

## 完美风暴：Rust、WebAssembly 和 MCP

Rust 提供了安全、高性能的运行时基础。WebAssembly 提供了可移植的沙盒执行环境。MCP 提供了标准化接口，使工具可以普遍访问 AI 代理。

选择 Rust 用于 Wassette 并非偶然。该语言对内存安全和零成本抽象的强调使其成为安全关键型基础设施的理想选择。

Wuyts 说：“Wassette 是用 Rust 编写的，可以作为独立的二进制文件安装，而无需任何运行时依赖项。”

安全基础不仅仅在于语言的选择。Wuyts 写道，Wassette 利用了 Wasmtime，这是一种 WebAssembly 运行时，“优先考虑安全性和正确性，并且可以方便地作为 Rust 库使用”。

他说：“组件提供的负载隔离与现代浏览器引擎相当，这得益于默认拒绝功能的系统。” 这意味着即使代理加载了潜在的恶意工具，它也无法在没有明确用户许可的情况下访问系统资源。

## 安全性，无需妥协

此外，安全性不是被视为附加功能，而是从一开始就构建到架构中。

Wuyts 说：“这确保了，例如，我们安装的方便的语法插件不会试图在我们背后渗透我们服务器的 SSH 密钥。”

例如，当代理需要发出网络请求时，系统会提示用户批准访问特定域。

Wuyts 指出：“在 Wasmtime 中加载的组件未经明确的访问权限就无法访问系统资源”，从而确保用户保持对其系统安全边界的控制。

这种基于能力的安全模型意味着即使是受损或恶意的组件也具有有限的影响范围。他指出，由 Rust 驱动的沙箱提供了多层保护，从内存安全保证到 WebAssembly 固有的隔离属性。

安全平台提供商 [Arcjet](https://thenewstack.io/arcjet-launches-wasm-powered-security-for-modern-developers/) 的 CEO [David Mytton](https://www.linkedin.com/in/davidmytton) 告诉 The New Stack：“Wassette 使用 Wasm 和组件模型是这些开放标准如何用于构建安全 AI 应用程序的一个很好的例子。”

他说：“这与我们在 Arcjet 的方法类似：我们将基于 Rust 的安全分析器编译为 Wasm 组件，并将它们直接嵌入到应用程序中。这使我们能够以本机速度和在 Wasm 的安全沙箱中检查不受信任的请求，从而提供对开发者友好的、代码内的保护。由于基于能力的设计，Wasm 默认是安全的，这正是现代安全运行时应该工作的方式。”

## Rust 在生产中的优势

Wassette 的生产就绪设计反映了 Rust 在系统编程中的成熟度以及 MCP 在企业 AI 部署中日益普及。零依赖部署模型意味着运营团队可以将 Wassette 集成到现有工作流程中，而无需担心运行时冲突或版本管理问题。

此外，Rust 的零成本抽象确保了安全沙箱不会以执行速度为代价。该公司表示，MCP 协议开销很小，可确保即使在复杂的代理工作流程中，工具调用也能保持响应。

## 构建组件生态系统

微软不仅仅是发布一个运行时，该公司还在培育一个生态系统。该团队提供了跨多种语言的组件示例，包括 [Python](https://github.com/microsoft/wassette/tree/main/examples/eval-py)、[JavaScript](https://github.com/microsoft/wassette/tree/main/examples/get-weather-js)、[Rust](https://github.com/microsoft/wassette/tree/main/examples/filesystem-rs) 和 [Go](https://github.com/microsoft/wassette/tree/main/examples/gomodule-go)。这种多语言方法可确保开发者可以使用他们喜欢的语言构建组件，同时受益于 Rust 在运行时级别的安全保证和 MCP 的通用代理兼容性。

支持 [Notation](https://github.com/notaryproject/notation) 和 [Cosign](https://github.com/sigstore/cosign) 的加密签名功能为组件分发提供了额外的安全层。这种企业级软件供应链安全方法反映了 Wassette 背后的严肃生产意图。

## 展望未来：自主工具发现

当前版本的 Wassette 要求用户手动指定组件位置，但该团队有更大的雄心。

Wuyts 解释说：“我们认为，如果代理缺少完成任务所需的工具，它应该能够自主地找到这些工具并加载它们。”

未来的迭代将包括智能组件发现，允许代理自动搜索容器注册表以查找合适的工具。Wuyts 说，这代表着朝着真正自我改进的 AI 系统迈出了重要一步。

此外，他说该团队还在致力于简化的移植工具，以将现有应用程序转换为 WebAssembly 组件，从而有可能为代理使用解锁大量的现有软件库。

## Rust 在 AI 基础设施中的复兴

此外，Wassette 代表了 Rust 在 AI 基础设施中更广泛的采用趋势，尤其是在 MCP 等标准化协议的背景下。

此外，随着 AI 代理变得越来越强大和自主，支持它们的基础设施必须同样强大。微软指出，Rust 的内存安全保证，结合 WebAssembly 的沙箱功能和 MCP 的标准化接口，为可信赖的自主系统提供了必要的基础。

对于有兴趣探索这项技术的开发者，[Wassette 在 GitHub 上可用](https://github.com/microsoft/wassette)，其中包含全面的文档和示例。[Microsoft Open Source Discord](https://discord.gg/microsoft-open-source) 包含一个专门的 Wassette 频道，用于社区讨论和支持。