The biggest update to the Model Context Protocol (MCP) since its launch is almost here. Lead maintainers [froze](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) the release candidate on May 21, with the final specification set to arrive July 28.

At first glance, the [changelog](https://modelcontextprotocol.io/specification/draft/changelog) sounds drastic: Sessions and the initialization handshake are will disappear, and three core features are being deprecated. Look closer, though, and the revision is really about simplifying MCP by handing familiar jobs back to the infrastructure already built to handle them. For operators, that addresses a long-running frustration: Running a remote MCP server shouldn’t require specialized machinery that an ordinary stateless service doesn’t need.

## The tax MCP was charging its own users

To understand the removals, you have to examine the gap between MCP’s original design and its actual deployment. Its earliest and most recognizable form was a desktop app communicating with a local process via standard input and output, where a startup handshake was inexpensive to perform over a long-lasting connection.

> A team shipping an MCP server was paying to solve a distributed-systems problem the protocol had created for them.

As more servers moved into remote, horizontally scaled deployments, those sessions became the problem. A server minted an `Mcp-Session-Id`, which pinned the client to the issuing instance. To scale out, this often requires session affinity, an externally shared session store, or MCP-aware gateway logic that parses JSON bodies to determine call routing. A team shipping an MCP server was paying to solve a distributed-systems problem the protocol had created for them.

Capability negotiation added a second cost. Because capabilities were exchanged once at connect time, list results could vary by connection, which made caching across sessions or in a shared intermediary hard to reason about.

## What the maintainers optimized for

Six Specification Enhancement Proposals converge on a single goal: making every request stand on its own. Protocol version and client capabilities now travel in `_meta` on each call. Clients are expected to include their identity there too, and a new `server/discover` method makes server capabilities independently queryable either up front or when needed. The release post calls this the underlying principle of pay-as-you-go complexity: The core stays lean, and statefulness shows up only where a feature genuinely needs it.

> The release post calls the underlying principle pay-as-you-go complexity, where the core stays lean, and statefulness shows up only where a feature genuinely needs it.

The obvious objection is that plenty of servers do need to remember things. One principal answer is the explicit handle, which is the pattern every shopping cart built over HTTP has used for twenty years. A tool mints a `basket_id`, returns it in the result, and the model passes it back as an ordinary argument on the next call. Account state, resource URIs, task handles, and ordinary database identifiers all remain available for anything that should not travel that route.

What makes the handle more than a workaround is that it is visible to the model. Session state hidden in transport metadata was something the model could never reason about, whereas a handle in a tool result can be composed across tools and handed between workflow steps. The trade-off is that it also appears in prompts, transcripts, and logs, so bind it to the authenticated principal and verify permissions with each use instead of considering it as proof of authorization.

## What developers actually get

For server authors, a remote MCP server can now be operated much more like a conventional stateless HTTP service. Three replicas behind round-robin, no affinity configuration, and no protocol session store to run or recover. Rolling deploys no longer invalidate sessions or strand a client on a removed instance, though they can still interrupt in-flight requests and subscription streams, and since resumability is gone, the client reissues that work under a new request ID.

For platform teams, the required `Mcp-Method` header, plus `Mcp-Name` for the named tool, resource, and prompt operations, means a gateway can rate-limit or authorize by operation without inspecting a request body. That only holds under the [transport validation rules](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http), where the backend rejects any header that disagrees with the body and a policy-enforcing intermediary refuses protocol versions that do not guarantee the check. Skip that and a benign header can front a different call underneath.

The caching change deserves more attention than it has received. Affected list and read results must now include `ttlMs` and `cacheScope`, modeled on HTTP `Cache-Control`, so a client can hold a catalog for a stated interval rather than refetching it. The draft treats `ttlMs` as a freshness hint rather than a promise that the data still holds. Servers are also asked to return tools in deterministic order, which the draft ties to better prompt cache hit rates, and at volume that can mean lower latency or token cost wherever the provider prices prompt caching.

One caveat belongs here rather than in a footnote. Statelessness at the protocol layer buys routability, not determinism. Two replicas will accept the same request without consulting protocol state, and they will still return different answers if they run different versions or read different downstream data.

## Why care about extensions

The ecosystem argument is stronger than any single feature. [Extensions](https://modelcontextprotocol.io/extensions/overview) now get namespaced identifiers, official ones under `io.modelcontextprotocol` and third-party ones under a reversed domain the author owns, plus their own `ext-` repositories and release cadences. Anyone who has written a Kubernetes custom resource definition will recognize the shape, where a capability ships and matures outside the core release train.

Tasks is the proof of why that matters. It shipped as an experimental core feature in 2025-11-25, real production use exposed design problems, and it has been redesigned as an extension. Moving it out of core is itself a breaking specification change, but the next iteration is not, because extensions evolve through capability flags or settings-level versioning, with a fresh identifier only when a break is unavoidable. MCP Apps, already available as an extension, now sits inside a formally governed negotiation framework rather than a process that did not exist.

## What the deprecation policy buys

The [feature lifecycle policy](https://modelcontextprotocol.io/community/feature-lifecycle) gives every feature an Active, Deprecated, and Removed state, with a minimum twelve-month window measured from the revision in which the feature first becomes Deprecated. The floor can be shortened only for an active security risk carrying a published advisory or documented exploitation, and even then ninety days is the hard minimum. A public registry lists what is on the way out and by when, and a Standards Track proposal cannot reach Final until a matching scenario lands in the conformance suite.

For a developer, that reads like housekeeping. For anyone who has to justify an MCP integration to a platform review board, a written deprecation guarantee is worth more than any capability in the release.

## What it costs

None of this arrives free of charge. Anyone who built against the experimental Tasks API migrates to the new lifecycle, and any server that issued its own requests to the client moves onto the [Multi Round-Trip Requests](https://modelcontextprotocol.io/specification/draft/basic/patterns/mrtr) pattern, where the server returns what it still needs, and the client retries with the answers. That server also has to authenticate any echoed `requestState` that can influence authorization or business logic, and one-time workflows still need their own replay tracking.

The deprecations are migration directions rather than drop-in replacements, and Sampling is the sharpest case. A server using client-mediated Sampling needed no provider credentials and generally did not carry the model bill, whereas calling a provider API directly turns it into a credential holder, a billing party, and a separate processor of user data. Logging tells a similar story, since `stderr` and OpenTelemetry answer operator observability without giving a remote client any equivalent of the structured log stream it used to receive.

> The protocol stopped managing state, which is not the same as the state going away.

Application state does not disappear either. Handles, carts, task records, and idempotency keys still need somewhere to live. The protocol stopped managing state, which is not the same as the state going away.

## The road ahead

Removing a foundational abstraction less than two years into a protocol’s life is a calculated risk, and the maintainers hedged it sensibly with a ten-week validation window and beta SDKs for Python, TypeScript, Go, and C#.

They also defined a migration path where clients probe with `server/discover` first and fall back to `initialize` — only when they encounter a legacy-only server. It’s a wire-level break with a negotiated path across it rather than an ecosystem flag day.

The release-candidate window is the right time to inventory session dependencies and test them, with production rollout following ratification and stable SDKs. From individual server authors to platform teams to the vendors building gateways and registries around it, the payoff is a protocol layer that fits far more naturally onto infrastructure the industry already knows how to operate.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)