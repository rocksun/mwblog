<!--
title: 可组合代理
cover: https://hashnode.com/utility/r?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1754066340300%2F28af3dcf-9f58-4299-b182-9be5216337bc.jpeg%3Fw%3D1200%26auto%3Dcompress%2Cformat%26format%3Dwebp%26fm%3Dpng
summary: 本文介绍了如何使用 Golang 和 Rust 构建一个轻量级命令行 AI 代理，并使用 Hayride 将其部署。文章涵盖了 Hayride 的安装、CLI 代理的构建、项目设置、依赖管理以及 WAC 组合和部署。重点是利用 WebAssembly 的组件模型和现有 AI morphs 来快速构建可组合和可重用的 AI 工具。
-->

本文介绍了如何使用 Golang 和 Rust 构建一个轻量级命令行 AI 代理，并使用 Hayride 将其部署。文章涵盖了 Hayride 的安装、CLI 代理的构建、项目设置、依赖管理以及 WAC 组合和部署。重点是利用 WebAssembly 的组件模型和现有 AI morphs 来快速构建可组合和可重用的 AI 工具。

> 译自：[Composable Agents](https://blog.hayride.dev/composable-agents)
> 
> 作者：Ethan Lewis

## 概述

[在我们的上一篇文章中](https://blog.hayride.dev/sandboxing-ai)，我们宣布推出 Hayride，这是一个用于 LLM、沙盒代码执行和编排代理工作流程的开源安全 AI 运行时。

Hayride 利用 WebAssembly 提供的[安全性](https://webassembly.org/docs/security/)和[可移植性](https://webassembly.org/docs/portability/)优势，使其成为专注于构建可组合和可重用 AI 工具的开发人员的理想平台。

在一系列的帖子中，本文将启动一个使用 **Golang** 构建的轻量级命令行 (CLI) AI 代理，并带有一点 **Rust**，以演示如何使用 Hayride 快速地将使用多种语言编写的 AI 代理组合在一起。

如果您不熟悉 WebAssembly 以及 WebAssembly 接口类型、WebAssembly 系统接口或组件模型等概念，我们建议您现在了解这些主题。但是，本文将引导您了解出现的各种概念。

以下是一些帮助您快速了解 WebAssembly 的资源：

让我们开始吧！

## 前提条件

在我们开始实施我们的应用程序之前，需要一些工具。值得注意的是，Hayride 利用 [WASI Preview 2](https://wasi.dev/interfaces#wasi-02)，它正在获得各种语言的支持。

我们将在本文中使用以下工具：

- [Hayride](https://github.com/hayride-dev/releases)
- [Wit-bindgen-go](https://github.com/bytecodealliance/go-modules?tab=readme-ov-file#wit-bindgen-go)
- [Wit-deps](https://github.com/bytecodealliance/wit-deps)
- [Wac](https://github.com/bytecodealliance/wac)
- [Go](https://go.dev/doc/install) version 1.23.0+
- [TinyGo](https://tinygo.org/) version 0.33.0+
- [Rust +nightly](https://www.rust-lang.org/tools/install)
- [Cargo component](https://github.com/bytecodealliance/cargo-component)

请参阅工具的安装指南以开始使用。

### 安装 Hayride

安装 Hayride 的最简单方法是通过我们的安装脚本。Linux 和 macOS 用户可以执行以下操作：

`curl https://raw.githubusercontent.com/hayride-dev/releases/refs/heads/main/install.sh -sSf | bash`

这将下载预编译版本的 wasmtime，将其放置在 $HOME/.hayride 中，并更新您的 shell 配置以在 PATH 中设置正确的目录。

Windows 用户可以访问我们的发布页面以下载 [MSI 安装程序](https://github.com/hayride-dev/releases/releases/download/v0.0.3-alpha/hayride-v0.0.3-alpha-x86_64-windows.msi) 并使用它来安装 Hayride。

安装完成后，hayride 二进制文件应位于您的路径中。您可以通过从终端运行 `hayride help` 来验证安装。

现在 Hayride 已经安装完毕，我们可以开始开发可以部署到 Hayride 的代理了！

## 构建 CLI 代理

Hayride 使用 WebAssembly 接口类型 (WIT) 定义了一组 AI 接口。

**接口**描述了一个以单一为中心、可组合的合约，组件可以通过该合约相互交互以及与主机交互。

接口是定向的。使用接口时，您可以指示该接口是否可用于外部代码调用（即，**导出**），或者外部代码是否必须满足该接口才能让组件调用（即，**导入**）。

接口严格绑定到组件。组件无法与自身之外的任何事物进行交互，除非通过调用其导出或调用其导入。这些约束提供了严格的沙盒。

以下是 Hayride 如何使用 WIT 定义代理运行器接口的示例：

```
package hayride:ai@0.0.61;

interface runner {
    use types.{message};
    use agents.{agent};
    use wasi:io/streams@0.2.0.{output-stream};

    enum error-code {
        invoke-error,
        unknown
    }

    resource error {
        code: func() -> error-code;
        data: func() -> string;
    }

    invoke: func(message: message, agent: borrow<agent>) -> result<list<message>, error>;
    invoke-stream: func(message: message, writer: borrow<output-stream>, agent: borrow<agent>) -> result<_,error>;
}

```

(<https://github.com/hayride-dev/coven/blob/main/ai/wit/runner.wit>)

运行器接口负责调用代理并提供提示或消息。

**运行器**将代理循环定义为一个描述代理如何执行的函数。

**代理**被定义为一个与 AI 模型交互、可以使用工具并且可以存储任何交互的上下文的组件。

我们在 WIT 中的代理接口定义如下：

```
package hayride:ai@0.0.61;

interface agents {
    use types.{message};
    use context.{context};
    use model.{format};
    use hayride:mcp/tools@0.0.61.{tools};
    use hayride:mcp/types@0.0.61.{tool, call-tool-params, call-tool-result};
    use graph-stream.{graph-stream};
    use inference-stream.{graph-execution-context-stream};
    use wasi:io/streams@0.2.0.{output-stream};

    enum error-code {
        capabilities-error,
        context-error,
        compute-error,
        execute-error,
        unknown
    }

    resource error {
        code: func() -> error-code;
        data: func() -> string;
    }

    resource agent {
        constructor(name: string, instruction: string, format: format, graph: graph-execution-context-stream, tools: option<tools>, context: option<context>);
        name: func() -> string;
        instruction: func() -> string;
        capabilities: func() -> result<list<tool>, error>;
        context: func() -> result<list<message>, error>;
        compute: func(message: message) -> result<message, error>;
        execute: func(params: call-tool-params) -> result<call-tool-result, error>;
    }
}

```

(<https://github.com/hayride-dev/coven/blob/main/ai/wit/agents.wit>)

按照组件模型，这些接口可以由外部代码实现，并由我们的组件导入。

对于这篇文章，我们使用 Hayride 打包的默认运行器和代理实现。这使我们可以只关注代理的 CLI 部分，并使用外部可用的运行器和代理组件来满足我们的接口合约。这些组件的实现可以在我们的 [morphs 仓库](https://github.com/hayride-dev/morphs/tree/main/components) 中找到。

在以后的文章中，我们将介绍每个组件如何工作，以及如何实现您自己的组件来满足 Hayride 提供的各种 AI 接口。

### 定义我们的 Morph

Hayride Morphs 是应用程序的基本构建块。它们可以**导入**函数来访问外部功能，也可以**导出**它们的功能到其他 morphs。

术语 **morph** 只是指一种 WebAssembly 组件，它被设计为可在不同环境中组合和移植。

我们的 CLI 代理 Morph 可以使用 **worlds** 在 WIT 中进行描述。

WIT world 是一个更高级别的合约，描述了组件的功能和需求。一个 world 由接口组成。为了使组件运行，它的导入必须由主机或其他组件满足。

将组件的一些或全部导入连接到其他组件的匹配导出称为**组合**。

鉴于此，我们可以将我们的组件 world 定义如下：

```
package hayride:example@0.0.1;

world cli {
    include hayride:wasip2/imports@0.0.61;
    include hayride:wasip2/exports@0.0.61;

    import hayride:ai/runner@0.0.61;
    import hayride:ai/model-repository@0.0.61;
}

```

(<https://github.com/hayride-dev/morphs/blob/main/components/examples/agents/wit/world.wit#L3C1-L9C2>)

现在我们对我们的 world 和接口的样子有了一个大概的了解，我们可以创建我们的项目，看看我们如何使用前面的 WIT 定义。

### 项目设置

首先，我们创建项目的目录布局：

`mkdir hayride-example-agent`

由于我们正在用 Go 构建我们的代理，并使用 TinyGo 编译为 WebAssembly，我们可以使用 **go mod** 来初始化我们的应用程序和依赖项：

`go mod init`

接下来，我们创建一个名为 wit 的目录：

`mkdir wit`

我们使用上面定义的 world 并将其复制到我们的 wit 目录中的一个文件中：

`touch ./wit/world.wit`

要使用这个 world，我们需要拉取我们的依赖项。使用 Hayride 的 WIT 仓库，我们可以使用 **wit-deps** 添加两个依赖项。

Wit-deps 需要一个 `deps.toml` 来跟踪依赖项。我们可以使用以下命令将其添加到我们的 wit 目录：

`Touch ./wit/deps.toml`

在 `deps.toml` 文件中，添加以下依赖项：

```
wasip2 = "https://github.com/hayride-dev/coven/releases/download/v0.0.61/hayride_wasip2_v0.0.61.tar.gz"
ai = "https://github.com/hayride-dev/coven/releases/download/v0.0.61/hayride_ai_v0.0.61.tar.gz"
mcp = "https://github.com/hayride-dev/coven/releases/download/v0.0.61/hayride_mcp_v0.0.61.tar.gz"

```

要将这些依赖项拉入我们的项目，我们使用一个名为 **wit-deps** 的工具。

从项目的根目录，运行以下命令：

`wit-deps update`

接下来，我们创建一个 `main.go` 文件并开始实现我们的 CLI 应用程序：

`touch main.go`

现在我们已经下载了基本的项目布局和依赖项，我们可以继续实现我们的 CLI。

### CLI 应用程序

我们的 CLI 负责从 STDIN 读取用户的消息，并返回代理的响应。

首先，让我们开始使用 Hayride 的 [bindings 仓库](https://github.com/hayride-dev/bindings) 创建必要的对象。

在 `main.go` 文件中，添加以下代码行：

```
package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strings"

    "github.com/hayride-dev/bindings/go/hayride/ai/agents"
    "github.com/hayride-dev/bindings/go/hayride/ai/ctx"
    "github.com/hayride-dev/bindings/go/hayride/ai/graph"
    "github.com/hayride-dev/bindings/go/hayride/ai/models"
    "github.com/hayride-dev/bindings/go/hayride/ai/models/repository"
    "github.com/hayride-dev/bindings/go/hayride/ai/runner"
    "github.com/hayride-dev/bindings/go/hayride/mcp/tools"
    "github.com/hayride-dev/bindings/go/hayride/types"
    "github.com/hayride-dev/bindings/go/wasi/cli"
    "go.bytecodealliance.org/cm"
)

func main() {
    repo := repository.New()
    path, err := repo.DownloadModel("bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf")
    if err != nil {
        log.Fatal("failed to download model:", err)
    }

    
    ctx, err := ctx.New()
    if err != nil {
        log.Fatal("failed to create context:", err)
    }

    tools, err := tools.New()
    if err != nil {
        log.Fatal("failed to create tools:", err)
    }

    format, err := models.New()
    if err != nil {
        log.Fatal("failed to create model format:", err)
    }

    
    inferenceStream, err := graph.LoadByName(path)
    if err != nil {
        log.Fatal("failed to load graph:", err)
    }

    graphExecutionCtxStream, err := inferenceStream.InitExecutionContextStream()
    if err != nil {
        log.Fatal("failed to initialize graph execution context stream:", err)
    }

    a, err := agents.New(
        format, graphExecutionCtxStream,
        agents.WithName("Helpful Agent"),
        agents.WithInstruction("You are a helpful assistant. Answer the user's questions to the best of your ability."),
        agents.WithContext(ctx),
        agents.WithTools(tools),
    )
    if err != nil {
        log.Fatal("failed to create agent:", err)
    }

    runner := runner.New()
}

```

这段代码只是简单地创建了我们的运行器和代理执行所需的各种对象：

* **Repository:** 仓库包提供了从远程仓库下载模型的功能。Hayride 的主机环境为模型仓库提供了一个 Hugging Face 实现。
* **Context**: 上下文对象是代理的消息存储。代理决定何时存储上下文以及何时拉取过去的消息。在这个例子中，我们使用的是 Hayride 的内存上下文存储。
* **Tools**: 工具对象用于向代理公开可调用的工具。由于我们的代理不需要工具，我们将附加一个空的工具组件。
* **Format**: 格式对象用于在将用户的消息发送到 LLM 之前对其进行编码。我们还使用格式对象来解码 LLM 的响应。每个模型通常需要某种形式的自定义编码或解码。
* **GraphExecutionCtxStream**: GraphExecutionCtxStream 提供了对我们的主机环境和加载的 LLM 的访问。这是 [wasi-nn](https://github.com/WebAssembly/wasi-nn/releases) 的一个扩展，允许流式响应。

接下来，我们添加从 **STDIN** 读取和创建 **STDOUT** 写入器的代码。

由于我们正在使用 WebAssembly，我们利用 WASI 在我们的应用程序中管道传输终端的 **STDIN/STDOUT**。

虽然 TinyGo 支持 wasip2，但在组合多个组件时会出现一些限制。其中一个限制是当使用标准库时，无法访问主机运行时为 `io.Writer` 提供的 Wasm 资源。简而言之，这意味着我们无法将这个资源传递给使用这个资源的组件。

为了避免这个限制，我们在 [bindings 仓库](https://github.com/hayride-dev/bindings/tree/main/go/wasi) 中实现了一些 WASI 助手。要利用的主要助手是我们的 [**wasi-cli**](https://github.com/WebAssembly/wasi-cli/blob/main/wit/stdio.wit) 接口的实现。

使用我们的 bindings，我们可以创建一个可以转换为 WASI 输出流并在组件之间传递的 `io.Writer`，在我们的例子中，将 CLI 应用程序中创建的写入器传递给 AI 运行器：

```
writer := cli.GetStdout(true)
reader := bufio.NewReader(os.Stdin)

```

最后，我们添加一个基本的循环，允许用户输入提示，使用我们的运行器将提示发送给代理，并显示结果：

```
fmt.Println("What can I help with?")
for {
    input, _ := reader.ReadString('\n')
    prompt := strings.TrimSpace(input)
    if strings.ToLower(prompt) == "exit" {
        fmt.Println("Goodbye!")
        break
    }

    msg := types.Message{
        Role: types.RoleUser,
        Content: cm.ToList([]types.MessageContent{
            types.NewMessageContent(types.Text(input)),
        }),
    }

    err := runner.InvokeStream(msg, writer, a)
    if err != nil {
        fmt.Println("error invoking agent:", err)
        os.Exit(1)
    }

    fmt.Println("\nWhat else can I help with? (type 'exit' to quit)")
}

```

运行器的 **InvokeStream** 函数被调用，其中包含用户的提示、输出流和一个代理。代理的结果会自动写回给用户。我们只是在一个循环中调用我们的代理，其中包含用户发送的消息。

WebAssembly 的异步功能存在一些限制，这要求我们将写入器转发到我们的组件，以便尽快开始写入结果。但是，关于异步函数的讨论正在 wasip3 中进行。更多信息可以在 [wasi 路线图](https://wasi.dev/roadmap?utm_source=chatgpt.com) 上找到。

完整的代码如下所示：

```
package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strings"

    "github.com/hayride-dev/bindings/go/hayride/ai/agents"
    "github.com/hayride-dev/bindings/go/hayride/ai/ctx"
    "github.com/hayride-dev/bindings/go/hayride/ai/graph"
    "github.com/hayride-dev/bindings/go/hayride/ai/models"
    "github.com/hayride-dev/bindings/go/hayride/ai/models/repository"
    "github.com/hayride-dev/bindings/go/hayride/ai/runner"
    "github.com/hayride-dev/bindings/go/hayride/mcp/tools"
    "github.com/hayride-dev/bindings/go/hayride/types"
    "github.com/hayride-dev/bindings/go/wasi/cli"
    "go.bytecodealliance.org/cm"
)

func main() {
    repo := repository.New()
    path, err := repo.DownloadModel("bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf")
    if err != nil {
        log.Fatal("failed to download model:", err)
    }

    
    ctx, err := ctx.New()
    if err != nil {
        log.Fatal("failed to create context:", err)
    }

    tools, err := tools.New()
    if err != nil {
        log.Fatal("failed to create tools:", err)
    }

    format, err := models.New()
    if err != nil {
        log.Fatal("failed to create model format:", err)
    }

    
    inferenceStream, err := graph.LoadByName(path)
    if err != nil {
        log.Fatal("failed to load graph:", err)
    }

    graphExecutionCtxStream, err := inferenceStream.InitExecutionContextStream()
    if err != nil {
        log.Fatal("failed to initialize graph execution context stream:", err)
    }

    a, err := agents.New(
        format, graphExecutionCtxStream,
        agents.WithName("Helpful Agent"),
        agents.WithInstruction("You are a helpful assistant. Answer the user's questions to the best of your ability."),
        agents.WithContext(ctx),
        agents.WithTools(tools),
    )
    if err != nil {
        log.Fatal("failed to create agent:", err)
    }

    runner := runner.New()

    writer := cli.GetStdout(true)
    reader := bufio.NewReader(os.Stdin)

    fmt.Println("What can I help with?")
    for {
        input, _ := reader.ReadString('\n')
        prompt := strings.TrimSpace(input)
        if strings.ToLower(prompt) == "exit" {
            fmt.Println("Goodbye!")
            break
        }

        msg := types.Message{
            Role: types.RoleUser,
            Content: cm.ToList([]types.MessageContent{
                types.NewMessageContent(types.Text(input)),
            }),
        }

        err := runner.InvokeStream(msg, writer, a)
        if err != nil {
            fmt.Println("error invoking agent:", err)
            os.Exit(1)
        }

        fmt.Println("\nWhat else can I help with? (type 'exit' to quit)")
    }
}

```

(<https://github.com/hayride-dev/morphs/blob/main/components/examples/agents/cli.go>)

剩下的就是构建我们的代理并将其部署到 Hayride 上！

我们将编译我们的应用程序，将其与 Hayride 现有的 morphs 组合，并将我们组合的 morph 部署到 Hayride。

### 构建组合和部署

为了将我们的 CLI 与 Hayride 提供的现有 Wasm 组件组合在一起，我们使用 **WAC**，这是一个用于将 WebAssembly 组件组合在一起的工具。这些组件的源代码可以在我们的 [morphs 仓库](https://github.com/hayride-dev/morphs/tree/main/components) 中找到。

WAC 的完整语言指南可以在[这里](https://github.com/bytecodealliance/wac/blob/main/LANGUAGE.md)找到。

我们首先创建一个 `cli.wac`，其中包含以下内容：

```
package hayride:example;

let context = new hayride:inmemory@0.0.1 {...}; 
let llama = new hayride:llama31@0.0.1 {...};
let tools = new hayride:default-tools@0.0.1 {...};

let agent = new hayride:default-agent@0.0.1 {
  context: context.context,
  model: llama.model,
  tools: tools.tools,
  ...
};

let runner = new hayride:default-runner@0.0.1 {
  agents: agent.agents,
  ...
};

let cli = new hayride:cli@0.0.1 {
  context: context.context,
  model: llama.model,
  tools: tools.tools,
  agents: agent.agents,
  runner: runner.runner,
  ...
};

export cli...;

```

这个文件负责组合满足我们的运行器和代理期望的接口的 Wasm 组件。

在上面的文件中，我们使用了以下 Hayride Morphs：

使用这些组件，我们可以组合我们的 CLI。最终结果是一个可以在 Hayride 上部署的单个 Wasm 模块。

Hayride 内置了对 WAC 文件的支持，我们可以使用以下命令执行我们的组合：

`hayride wac compose --path ./cli.wac --out ./composed-cli-agent.wasm`

一旦我们有了 `composed-cli-agent.wasm` 文件，我们就可以将其注册到 Hayride。这使得 morph 可用于未来的组合和直接执行。

`hayride register --bin ./cli-agent.wasm --package hayride:composed-cli-agent@0.0.1`

剩下的就是执行我们的 morph：
`hayride cast --package hayride:composed-cli-agent@0.0.1 -it`

此命令启动我们的 CLI：

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcnunFoEQ-rmBxnonyKtdkK2dhB4ZIw_VnxxzpGwFRQVqoGet5Yi9Xxt9JnC1BxmYJ8cVUklDceFXLq8ELxc7zDErb1Ft3T_FbJyXzwz1t9EQa3L09z13qc5pdApF42VzqEFVV-?key=HJZoXeiqMu56XW0ZbuwWHuiK)

## 结论

在这篇文章中，我们演示了如何使用 Hayride 现有的 AI morphs 构建一个 CLI 应用程序。使用 WebAssembly 的组件模型和各种社区工具，我们将多个组件组合在一起，以在 Hayride 上构建和部署我们的 CLI 应用程序。

在我们的下一篇文章中，我们将深入研究 Hayride 代理和运行器，探索每个组件如何工作。

要了解未来发展的最新信息，请在 [X](https://x.com/HayrideDev) 和 [GitHub](https://github.com/hayride-dev) 上关注我们。