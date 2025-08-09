Microsoft’s [Azure Core Upstream](https://github.com/Azure/container-upstream) team this week released [Wassette](https://github.com/microsoft/wassette), a [Rust](https://thenewstack.io/rust-programming-language-guide/)-powered runtime that could fundamentally change how [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) acquire and execute new capabilities.

Built on the battle-tested, Rust-based [Wasmtime](https://thenewstack.io/webassemblys-wasmtime-1-0-revamps-security-performance/) [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) runtime and leveraging the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/), Wassette enables AI agents to autonomously download, vet and securely execute tools while maintaining browser-grade security isolation.

The runtime allows agents to autonomously fetch [WebAssembly Components](https://component-model.bytecodealliance.org/design/why-component-model.html) from [Open Container Initiative (OCI) registries](https://opensource.microsoft.com/blog/2024/09/25/distributing-webassembly-components-using-oci-registries/) and execute them as needed, Microsoft said.

Wassette acts as a bridge between two cutting-edge technologies: WebAssembly Components and MCP, which has emerged as a standard way for AI agents to interact with external tools and services. But until now, agents were limited to pre-configured tool sets.

Wassette “knows how to interpret a Wasm Component’s typed library interfaces and expose them as MCP tools,” [Yoshua Wuyts](https://www.linkedin.com/in/yoshuawuyts/?originalSubdomain=dk), senior developer advocate at Microsoft and [Rust Async Working Group](https://github.com/rust-lang/wg-async) member, explained in a [blog post](https://opensource.microsoft.com/blog/2025/08/06/introducing-wassette-webassembly-based-tools-for-ai-agents/).

This translation layer means that any WebAssembly component can instantly become available to MCP-compatible AI agents without requiring custom integration work.

MCP is rapidly becoming the standard protocol for AI agent tool integration, supported by major platforms like GitHub Copilot, Claude and others. By making WebAssembly components MCP-compatible, Wassette effectively opens up the entire WebAssembly ecosystem to AI agents.

“Allowing AI agents to use Wasm apps through MCP is exactly the kind of use case server-side WebAssembly was designed for,” [Torsten Volk](https://www.linkedin.com/in/torstenvolk/), principal analyst for application modernization at Enterprise Strategy Group, told The New Stack. “If you think about it further, AI agents could assemble applications by linking together Wasm apps via MCP. You might even give the agent a financial budget to purchase or subscribe to specific Wasm apps, and of course, the app owner can push updates to the registry for direct use by ‘paying’ AI agents.”

Getting started with Wassette is quick, easy and works with any AI agent that supports MCP, Wuyts wrote. The MCP integration means the tool works seamlessly with any MCP-compatible AI platform, including GitHub Copilot, [Claude Code](https://thenewstack.io/anthropic-adds-auto-security-reviews-to-claude-code/), [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) and [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/).

## Teaching Agents To Go on ‘Supply Runs’

“At the most basic level, the goal of an AI agent is to successfully complete any computer-based task you hand it, with minimal human intervention,” Wuyts wrote.

Yet, today’s agents are limited by their pre-installed tool sets. Wassette changes this.

“We can think of this as teaching agents how to go on supply runs: recognizing what is needed and figuring out how to get it,” Wuyts wrote.

This is about creating autonomous systems that can evolve their capabilities on demand. When an AI agent encounters a task requiring network requests, time calculations or file processing, it can now identify the missing tool, fetch it from a container registry and execute it securely, the post says.

## The Perfect Storm: Rust, WebAssembly and MCP

Rust provides the secure, performant runtime foundation. WebAssembly offers portable, sandboxed execution environments. And MCP provides the standardized interface that makes tools universally accessible to AI agents.

The choice of Rust for Wassette was no accident. The language’s emphasis on memory safety and zero-cost abstractions makes it ideal for security-critical infrastructure.

“Wassette is written in Rust and installable as a standalone binary with zero runtime dependencies,” Wuyts said.

The security foundation runs deeper than just the language choice. Wassette leverages Wasmtime, the WebAssembly runtime that “prioritizes security and correctness, and is conveniently available as a Rust library,” Wuyts wrote.

“Components provide workload isolation on par with modern browser engines, which is made possible by a deny-by-default capability system,” he said. This means that even if an agent loads a potentially malicious tool, it cannot access system resources without explicit user permission.

## Security Without Compromise

Moreover, rather than treating security as a bolt-on feature, it is built into the architecture from the ground up.

“This makes sure that, for example, the handy grammar plugin we installed doesn’t attempt to exfiltrate our server’s SSH keys behind our backs,” Wuyts said.

When an agent needs to make network requests, for instance, users are prompted to approve access to specific domains.

“Components loaded in Wasmtime can’t access system resources without explicit access permissions,” ensuring that users maintain control over their system’s security boundary, Wuyts noted.

This capability-based security model means that even compromised or malicious components have a limited blast radius. The Rust-powered sandbox provides multiple layers of protection, from memory safety guarantees to WebAssembly’s inherent isolation properties, he noted.

“Wassette’s use of Wasm and the Component Model is a great example of how these open standards can be used to build secure AI applications,” [David Mytton](https://www.linkedin.com/in/davidmytton), CEO of security platform provider [Arcjet](https://thenewstack.io/arcjet-launches-wasm-powered-security-for-modern-developers/), told The New Stack.

“This parallels our approach at Arcjet: We compile Rust-based security analyzers to Wasm Components and embed them directly in the application,” he said. “That lets us inspect untrusted requests — at native speed and in Wasm’s secure sandbox — providing developer-friendly, in-code protection. Wasm is secure by default because of the capability-based design, which is exactly how modern secure runtimes should work.”

## The Rust Advantage in Production

Wassette’s production-ready design reflects Rust’s maturity in systems programming and MCP’s growing adoption in enterprise AI deployments. The zero-dependency deployment model means operations teams can integrate Wassette into existing workflows without worrying about runtime conflicts or version management issues.

Also, Rust’s zero-cost abstractions ensure that the security sandboxing does not come at the expense of execution speed. The MCP protocol overhead is minimal, ensuring that tool invocations remain responsive even in complex agent workflows, the company said.

## Building the Component Ecosystem

Microsoft is not just releasing a runtime – the company is fostering an ecosystem. The team provides component examples across multiple languages, including [Python](https://github.com/microsoft/wassette/tree/main/examples/eval-py), [JavaScript](https://github.com/microsoft/wassette/tree/main/examples/get-weather-js), [Rust](https://github.com/microsoft/wassette/tree/main/examples/filesystem-rs) and [Go](https://github.com/microsoft/wassette/tree/main/examples/gomodule-go). This multilingual approach ensures developers can build components in their preferred languages while benefiting from Rust’s security guarantees at the runtime level and MCP’s universal agent compatibility.

The cryptographic signing capabilities, supporting both [Notation](https://github.com/notaryproject/notation) and [Cosign](https://github.com/sigstore/cosign), provide additional security layers for component distribution. This enterprise-grade approach to software supply chain security reflects the serious production intent behind Wassette.

## Looking Forward: Autonomous Tool Discovery

The current version of Wassette requires users to manually specify component locations, but the team has bigger ambitions.

“We believe that if an agent is missing the tools it needs to complete a task, it should be able to autonomously find those tools and load them,” Wuyts explained.

Future iterations will include intelligent component discovery, allowing agents to search container registries for appropriate tools automatically. This represents a significant step toward truly self-improving AI systems, Wuyts said.

Further, he said that the team is also working on simplified porting tools to convert existing applications into WebAssembly components, potentially unlocking vast libraries of existing software for agent use.

## The Rust Renaissance in AI Infrastructure

Moreover, Wassette represents a broader trend of Rust adoption in AI infrastructure, particularly in the context of standardized protocols like MCP.

In addition, as AI agents become more capable and autonomous, the infrastructure supporting them must be equally robust. Rust’s memory safety guarantees, combined with WebAssembly’s sandboxing capabilities, and MCP’s standardized interfaces provide the foundation needed for trustworthy autonomous systems, Microsoft notes.

For developers interested in exploring this technology, [Wassette is available on GitHub](https://github.com/microsoft/wassette) with comprehensive documentation and examples. And the [Microsoft Open Source Discord](https://discord.gg/microsoft-open-source) includes a dedicated Wassette channel for community discussions and support.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)