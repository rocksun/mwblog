**Choosing a coding agent may soon no longer** mean having to pick a new editor or terminal, too. That scenario came a step closer to reality this week, when AWS explained how [Kiro](https://thenewstack.io/aws-kiro-mobile-ios-agentic-coding/) replaced three separate agent harnesses with a single architecture built around the Agent Client Protocol. The move lets Kiro’s clients communicate with its agent through a shared protocol. It could eventually let developers choose their coding tools and AI agents independently.

The IDE relied on a TypeScript harness, the CLI used Rust, and the web experience depended on Python. These have now been [consolidated](https://kiro.dev/blog/one-agent/) into a single standalone agent harness that runs as a separate process alongside the workspace.

The engineering simplification is noteworthy, but the architectural decision is more consequential: AWS chose the [Agent Client Protocol](https://agentclientprotocol.org/) (ACP) as the interface between Kiro’s clients and Kiro’s own agent. ACP originated at [Zed](https://thenewstack.io/fast-rust-based-zed-code-editor-finally-arrives-on-windows/) and is now jointly developed with [JetBrains](https://thenewstack.io/jetbrains-independent-ai-coding/). By adopting an ecosystem protocol even for its first-party components, AWS is treating the client-agent boundary as a standardized interface rather than a proprietary implementation detail.

## The protocol became the architectural boundary

Kiro’s engineers describe an evolution familiar to anyone who has built extensible software. Earlier attempts using shared libraries failed to maintain separation. Client applications gradually accumulated agent-specific logic by reaching into internal APIs, making the boundary increasingly porous.

Moving the agent into a standalone process solved that problem. The client now communicates exclusively through ACP, while the execution environment becomes an implementation detail. Whether the agent runs locally on a developer workstation or inside a cloud sandbox, the client interacts with the same protocol.

> The protocol remains standard; differentiation happens through extensions.

AWS deliberately extended ACP instead of creating a proprietary variant. The team introduced more than 20 agent-callable methods, 15 client-callable methods, and 20 notification types, all namespaced under `_kiro/`. It also implemented a WebSocket transport for web and iOS clients while continuing to use ACP’s standard stdio transport for local execution. Extensions such as custom agents and lifecycle hooks now share a common configuration model across every Kiro surface, while each client remains free to deliver native user experiences and platform-specific tools.

The protocol remains standard; differentiation happens through extensions.

## AWS is not alone in arriving at this conclusion.

Multiple vendors are arriving on the same idea.

[Microsoft introduced Intelligent Terminal 0.1](https://thenewstack.io/microsoft-intelligent-terminal-ai-agents/) at Build in June as an experimental ACP client that can discover locally installed agent CLIs. GitHub Copilot CLI serves as the default agent, but the architecture is intentionally designed to support multiple implementations.

JetBrains followed in July by bringing [Junie](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/) into [ReSharper](https://blog.jetbrains.com/dotnet/2026/07/22/resharper-2026-2-release/) 2026.2 through ACP. The company describes the integration as an early step toward broader protocol support rather than a finished implementation.

Although these announcements differ significantly in maturity, they converge on the same architectural principle. Microsoft uses ACP to decouple the terminal from agent implementations. JetBrains is introducing the protocol into its IDE stack. AWS has standardized the boundary inside its own product.

The pattern closely resembles what the Language Server Protocol accomplished for programming language tooling. LSP separated editors from language intelligence. ACP is beginning to separate developer experiences from agent implementations. Instead of requiring every editor to build bespoke integrations for every agent, both sides can target a common protocol, reducing integration complexity from N **×** M relationships toward N **+** M.

> The protocol establishes interoperability without eliminating product differentiation.

Vendor-specific capabilities inevitably reintroduce some specialization. Kiro’s namespaced extensions illustrate this trade-off. Third-party ACP clients receive a standardized experience, while Kiro’s own clients benefit from richer capabilities, including live steering, specifications, and advanced permission management.

The protocol establishes interoperability without eliminating product differentiation.

## Governance becomes the new competitive layer

Standardizing communication shifts innovation elsewhere.

Kiro’s most significant differentiation lies in policy management rather than transport. The platform replaces two incompatible permission systems with a unified capability model backed by [Cedar](https://thenewstack.io/aws-kubernetes-invisible-simplicity/), AWS’s authorization language designed with formal verification techniques.

Previously, the CLI relied on regular-expression allow and deny lists, while the IDE implemented prefix-based matching. The new capability model abstracts permissions around functional intent. Capabilities such as `fs_read`, `fs_write`, `shell`, `web_fetch`, `mcp`, and `subagent` represent classes of operations rather than individual tools. Denying `fs_read`, for example, blocks all file-reading operations, regardless of which tool performs them.

Policies are evaluated across multiple scopes, including MDM, user, workspace, agent profile, and session, with explicit deny rules taking precedence.

ACP itself provides only basic tool approval semantics. AWS has built a considerably richer governance model on top of that foundation. As enterprise adoption accelerates, this layer is likely to become a primary point of differentiation. Identity integration, auditing, authorization, policy inheritance, and sandboxing will matter at least as much as protocol compatibility.

It is also important to distinguish ACP from MCP. MCP standardizes how agents communicate with external tools and services. ACP standardizes how clients communicate with agents. They address complementary layers of the stack rather than competing with each other.

## An ecosystem standard without the default distribution

One notable aspect of ACP’s adoption is where it has appeared and where it has not.

As of August 2026, [Visual Studio Code](https://thenewstack.io/vs-code-becomes-multi-agent-command-center-for-developers/) has not adopted ACP as the native boundary between its editor and agent architecture. Microsoft’s ACP implementation currently appears in Intelligent Terminal rather than the editor itself.

> Once the client-agent boundary is standardized, agents become replaceable components rather than tightly coupled features embedded within individual developer tools.

Despite the absence of the industry’s largest editor platform, ACP continues to gain momentum across independent implementations. That suggests the protocol is succeeding on architectural merit rather than distribution alone.

For developers, this points toward a fundamental shift. The editor or terminal they use no longer has to determine which coding agent they run. Those decisions are gradually becoming independent. Once the client-agent boundary is standardized, agents become replaceable components rather than tightly coupled features embedded within individual developer tools.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)