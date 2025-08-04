# Overview

[In our last post](https://blog.hayride.dev/sandboxing-ai), we announced Hayride, an open-source secure AI runtime for LLMs, sandboxed code execution, and orchestrating agentic workflows.

Hayride leverages the [security](https://webassembly.org/docs/security/) and [por](https://webassembly.org/docs/security/)[tability](https://webassembly.org/docs/portability/) benefits offered by WebAssembly, making it an ideal platform for developers focused on building composable and reusable AI tooling.

In a series of posts this one kicks off, we will explore building a lightweight command-line (CLI) AI agent using **Golang**, with a sprinkle of **Rust**, to demonstrate how quickly AI agents leveraging tools written in multiple languages can be composed together using Hayride.

If you are new to WebAssembly and concepts such as WebAssembly Interface Types, WebAssembly System Interfaces, or the component model, we recommend learning about these topics now. However, this post will guide you through the various concepts as they come up.

Here are some resources to get you up to speed on WebAssembly:

Let’s dive in!

## Prerequisites

Before we can start implementing our application, several tools are required. Of note, Hayride leverages [WASI Preview 2](https://wasi.dev/interfaces#wasi-02), which is gaining support across various languages.

We’ll use the following tools in this post:

Please refer to the tools’ installation guides to get started.

### Installing Hayride

The easiest way to install Hayride is through our installation script. Linux and macOS users can execute the following:

`curl https://raw.githubusercontent.com/hayride-dev/releases/refs/heads/main/install.sh -sSf | bash`

This downloads a precompiled version of wasmtime, places it in $HOME/.hayride, and updates your shell configuration to set the right directory in PATH.

Windows users can visit our releases page to download the [MSI installer](https://github.com/hayride-dev/releases/releases/download/v0.0.3-alpha/hayride-v0.0.3-alpha-x86_64-windows.msi) and use it to install Hayride.

After the installation completes, the hayride binary should be located in your path. You can verify the installation by running `hayride help` from your terminal.

Now that Hayride is installed, we can start developing an agent that can be deployed to Hayride!

## Building a CLI Agent

Hayride has defined a set of AI interfaces using WebAssembly Interface Types (WIT).

An **interface** describes a single-focused, composable contract through which components can interact with each other and with hosts.

Interfaces are directional. When using an interface, you can indicate whether the interface is available for external code to call (i.e., **export**) or whether external code must fulfill the interface for the component to call (i.e., **import**).

Interfaces are strictly bound to a component. A component cannot interact with anything outside itself except by having its exports called or by calling its imports. These constraints provide rigorous sandboxing.

Here is an example of how Hayride defines an agent runner interface using WIT:

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

The runner interface is responsible for invoking an agent and supplying a prompt or message.

**Runners** define the agent loop as a function that describes how the agent executes.

**Agents** are defined as a component that interacts with an AI model, can use tools, and can store the context of any interactions.

Our agent interface in WIT is defined as follows:

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

Following the component model, these interfaces can be implemented externally by outside code and imported by our component.

For this post, we use a default runner and agent implementation packaged with Hayride. This allows us to focus solely on the CLI portion of our agent and uses an externally available runner and agent component that satisfy our interface contracts. The implementations of these components can be found in our [morphs repository](https://github.com/hayride-dev/morphs/tree/main/components).

In a future post, we will unpack how each of these components works and how you can implement your own component that satisfies the various AI interfaces Hayride supplies.

### Defining Our Morph

Hayride Morphs are the fundamental building blocks of applications. They can **import** functions to access external capabilities and can also **export** their capabilities to other morphs.

The term **morph** simply refers to a WebAssembly component that is designed to be composable and portable across different environments.

Our CLI Agent Morph can be described in WIT using **worlds**.

A WIT world is a higher-level contract that describes a component’s capabilities and needs. A world is composed of interfaces. For a component to run, its imports must be fulfilled by a host or by other components.

Connecting up some or all of a component’s imports to other components’ matching exports is called **composition**.

Given this, we can define our component world as follows:

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

Now that we have a rough idea of what our world and interfaces look like, we can create our project and see how we use the preceding WIT definitions.

### Project Setup

First, we create our project’s directory layout:

`mkdir hayride-example-agent`

Since we are building our agent in Go and compiling to WebAssembly using TinyGo, we can use **go mod** to initialize our application and dependencies:

`go mod init`

Next, we create a directory called wit:

`mkdir wit`

We use the world defined above and copy it to a file in our wit directory:

`touch ./wit/world.wit`

To use this world, we need to pull down our dependencies. Using Hayride’s WIT repository, we can add two dependencies using **wit-deps**.

Wit-deps requires a `deps.toml` to track dependencies. We can add it to our wit directory using the following command:

`Touch ./wit/deps.toml`

In the `deps.toml` file, add the following dependencies:

```
wasip2 = "https://github.com/hayride-dev/coven/releases/download/v0.0.61/hayride_wasip2_v0.0.61.tar.gz"
ai = "https://github.com/hayride-dev/coven/releases/download/v0.0.61/hayride_ai_v0.0.61.tar.gz"
mcp = "https://github.com/hayride-dev/coven/releases/download/v0.0.61/hayride_mcp_v0.0.61.tar.gz"

```

To pull these dependencies into our project, we use a tool called **wit-deps.**

From the project’s root, run the following command:

`wit-deps update`

Next, we create a `main.go` file and start implementing our CLI application:

`touch main.go`

Now that we have the basic project layout and dependencies downloaded, we can move on to implementing our CLI.

### CLI Application

Our CLI is responsible for reading in a user’s message from STDIN and returning the response from the agent.

First, let’s start by creating the necessary objects using Hayride’s [bindings repository](https://github.com/hayride-dev/bindings).

In the `main.go` file, add the following lines of code:

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

This code simply creates the various objects that our runner and agent require to execute:

* **Repository:** The repository package provides the ability to download models from a remote repository. Hayride’s host environment provides a Hugging Face implementation for model repositories.
* **Context**: The context object is a message store for the agent. The agent determines when to store context and when to pull past messages. We’re using Hayride’s in-memory context store for this example.
* **Tools**: The tools object is used to expose callable tools to the agent. Since our agent doesn’t require tools, we’ll attach an empty tools component.
* **Format**: The format object is used to encode the user’s message before sending it to the LLM. We also use the format object to decode the response from the LLM. Each model typically requires some form of custom encoding or decoding.
* **GraphExecutionCtxStream**: The GraphExecutionCtxStream provides access to our host environment and the LLM loaded. This is an extension of [wasi-nn](https://github.com/WebAssembly/wasi-nn/releases) to allow for streaming responses.

Next, we add the code to read from **STDIN** and create a **STDOUT** writer.

Since we are working with WebAssembly, we leverage WASI to pipe the terminal’s **STDIN/STDOUT** in our application.

While TinyGo supports wasip2, a few limitations come up when composing multiple components. One of these limitations is the inability to access the Wasm resource provisioned by the host runtime for an `io.Writer` when using the Standard library. In short, this means that we are unable to pass this resource to a component that uses this resource.

To avoid this limitation, we have implemented a few WASI helpers in the [bindings repository](https://github.com/hayride-dev/bindings/tree/main/go/wasi). The main helper to leverage is our implementation of the [**wasi-cli**](https://github.com/WebAssembly/wasi-cli/blob/main/wit/stdio.wit) interface.

Using our bindings, we can create an `io.Writer` that can be converted into a WASI output stream and passed between components, in our case, passing the writer created in our CLI application to an AI runner:

```
writer := cli.GetStdout(true)
reader := bufio.NewReader(os.Stdin)

```

Lastly, we add a basic loop that allows the user to type a prompt, send the prompt to the agent using our runner, and display the result:

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

The runner’s **InvokeStream** function is called with the user’s prompt, an output stream, and an agent. The result of the agent is automatically written back to the user. We simply invoke our agent in a loop with the message the user has sent.

There are limitations with WebAssembly’s async capabilities that require us to pass the writer forward to our component in order to start writing the result as fast as possible. However, discussions around async functions are taking place in wasip3. More information can be found on the [wasi roadmap](https://wasi.dev/roadmap?utm_source=chatgpt.com).

The full code looks like this:

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

All that’s left is to build and deploy our agent onto Hayride!

We’ll compile our application, compose it with Hayride’s existing morphs, and deploy our composed morph to Hayride.

### Build Composition and Deployment

To compose our CLI with the existing Wasm components supplied by Hayride, we use **WAC,** a tool for composing WebAssembly Components together. The source code for these components can be found in our [morphs repository](https://github.com/hayride-dev/morphs/tree/main/components).

The full language guide for WAC can be found [here](https://github.com/bytecodealliance/wac/blob/main/LANGUAGE.md).

We start by creating a `cli.wac` with the following content:

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

This file is responsible for composing the Wasm components that satisfy the interfaces our runner and agent expect.

In the above file, we are using the following Hayride Morphs:

Using these components, we can compose our CLI. The final result is a single Wasm module that can be deployed on Hayride.

Hayride has built-in support for WAC files, and we can execute our composition with the following command:

`hayride wac compose --path ./cli.wac --out ./composed-cli-agent.wasm`

Once we have the `composed-cli-agent.wasm` file, we can register it with Hayride. This makes the morph available for future composition and direct execution.

`hayride register --bin ./cli-agent.wasm --package hayride:composed-cli-agent@0.0.1`

All that’s left is to execute our morph:  
`hayride cast --package hayride:composed-cli-agent@0.0.1 -it`

This command launches our CLI:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcnunFoEQ-rmBxnonyKtdkK2dhB4ZIw_VnxxzpGwFRQVqoGet5Yi9Xxt9JnC1BxmYJ8cVUklDceFXLq8ELxc7zDErb1Ft3T_FbJyXzwz1t9EQa3L09z13qc5pdApF42VzqEFVV-?key=HJZoXeiqMu56XW0ZbuwWHuiK)

## Conclusion

In this post, we have demonstrated how to build a CLI application using Hayride’s existing AI morphs. Using WebAssembly’s Component model and various community tools, we composed multiple components together to build and deploy our CLI application on Hayride.

In our next post, we will delve into the Hayride Agent and Runner, exploring how each of these components works.

To stay informed about future developments, follow us on [X](https://x.com/HayrideDev) and [GitHub](https://github.com/hayride-dev).