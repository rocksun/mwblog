As AI agents take over more application logic, such as reading files, fetching web pages, and processing queue messages, the security tools built around HTTP boundaries are no longer effective. [Arcjet](https://arcjet.com/) wants to fix that with its latest offering.

The San Francisco-based runtime security company recently announced [Guards](https://docs.arcjet.com/guards), a capability that [enforces security policy](https://thenewstack.io/the-impact-of-regular-training-and-timely-security-policy-changes-on-dev-teams/) inside [AI agent tool handlers](https://thenewstack.io/how-to-choose-the-right-tool-for-your-google-adk-agent/), queue consumers, and workflow steps, as these are code paths that never touch an HTTP request and are therefore invisible to traditional web application firewalls (WAFs), proxies, and middleware, [David Mytton](https://www.linkedin.com/in/davidmytton/), the company’s CEO, tells *The New Stack*.

## The gap Guards is targeting

The premise is straightforward. Traditional application security, such as WAFs, AI gateways, and proxies, assumes a request boundary exists. An HTTP request comes in, hits middleware, is inspected, and reaches the application code. That model worked when applications had a front door.

Agentic systems don’t. “An agent tool handler receives untrusted input as a function argument, not a request body,” Mytton wrote in a [blog post](https://blog.arcjet.com/introducing-arcjet-guards-security-inside-the-agent-loop/) accompanying the announcement. “A queue consumer pulls a message off a broker, never touching a router. A [multi-agent pipeline](https://thenewstack.io/vs-code-becomes-multi-agent-command-center-for-developers/) passes state from one step to the next through shared memory or a workflow engine.” None of that crosses a network boundary a proxy can see.

The consequences are concrete.

Indeed, Mytton cited a real incident in which an agent pulled down a maliciously crafted website that instructed it to send content to an external attacker, and the WAF protecting the chat interface upstream never saw it.

“You’ve got all your permission set up correctly on the chat interface,” he said in a briefing with *The New Stack*, “but by prompt injecting agents right behind the scenes, you can get it to take actions that it wasn’t expecting.” Text instructions hidden inside an image the agent loads is another vector he pointed out.

There’s also a context problem that goes beyond visibility. “A proxy sitting in front of the application can see the request,” Mytton wrote in the blog post. “It can’t see the identity, the session, the business logic, or the budget.” Guards runs inside the application, where that context lives. Inside an agentic system, he notes, the reduction is worse still — a proxy can’t see a tool call at all, because a tool call isn’t a request.

## What Guards does

Guards integrates into [Arcjet’s existing SDK model](https://thenewstack.io/arcjet-reaches-v10-promises-stable-security-for-javascript-apps/), where developers define rules in the same codebase as the feature itself, so protection ships with the code and gets reviewed in the same pull request. The enforcement point moves to wherever untrusted input arrives.

“Security has to live where the code lives,” Mytton said in a [press release](https://www.prnewswire.com/news-releases/arcjet-introduces-guards-bringing-application-security-inside-ai-agent-workflows-302758796.html) on the news. “For [agentic systems](https://thenewstack.io/why-agentic-llm-systems-fail-control-cost-and-reliability/), that means inside the tool calls and workflow steps where untrusted input actually arrives, not at a perimeter that no longer exists. Guards give developers a way to enforce policy inside the code paths agents use every day — the same place the threat model now lives.”

The initial use cases cover three scenarios Arcjet sees as most pressing in production agentic systems: prompt injection detection on tool results — catching malicious instructions embedded in fetched content before it re-enters model context; PII blocking on tool inputs and queue messages before data reaches third-party models; and per-user token budget enforcement inside agent loops.

On that last point, Mytton was blunt in the briefing: a runaway agent loop can burn through budget fast. “Controlling budgets,” he says, means it “doesn’t go off and read thousands and thousands of pages and cost loads of money.”

Guards also handles multi-agent scenarios. Rather than inspecting individual tool calls in isolation, it carries session context across the entire pipeline. “If you’ve got multiple agents going off doing different things, the idea is you wrap your tool call in, protect what goes in, and then it will analyze what comes out — so you get two attempts at the analysis,” Mytton tells The New Stack.

## Agent-first, not just agent-friendly

Arcjet’s pitch goes beyond the technical capability. Mytton draws a line between products that are “agent-friendly” and products built around how agents actually work.

“Being agent-friendly isn’t the same thing as being agent-first,” he wrote in the blog post. “Shipping a [CLI](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) or an [MCP server](https://thenewstack.io/build-mcp-server-tutorial/) on top of an existing control plane or dashboard makes that control plane accessible to an agent, but that’s only half of the work.”

The other half, in Arcjet’s positioning, is meeting agents where they operate — inside a repo, writing code, and producing diffs.

“The agent writing your chat handler can see the prompt injection rule protecting it when that code is three lines above in the same file,” Mytton wrote in the post. “The code review covers both. The pull request that adds the feature adds the protection.”

Arcjet ships Guards with a prompt-based installation path: rather than walking developers through manual SDK integration, the install command drops instructions that a coding agent, such as Claude Code, Codex, Gemini Code Assist, executes directly. As Mytton puts it in the briefing, instead of telling developers to install the SDK and figure it out themselves, “we just give you a prompt, and the prompt tells your coding agent how to use Arcjet Guards.”

## Competitive landscape

The traditional web approach is well-covered. Cloudflare’s AI Gateway and Salesforce’s AI Gateway handle rate limiting, billing, and request inspection, but both operate on the assumption that a web request is in progress.

“These are all proxies, and they always assume a web request is happening,” Mytton tells *The New Stack*.

Arcjet’s argument is that the proxy model hits a structural wall when the agent calls a function rather than makes a request.

“Just like when you run something in the terminal — that’s not going through a proxy first. That’s where Arcjet fits,” he says.

Mytton looks at the shift in terms of where the perimeter has gone.

“Proxies and WAFs exist because, for a long time, they were the only way to put enforcement between the internet and an application without involving the developers,” Mytton wrote in the blog post. “That worked because the perimeter was real. It’s now dissolving.”

Guards is available now through Arcjet’s JavaScript and [Python SDKs](https://thenewstack.io/arcjets-python-sdk-embeds-security-in-code/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)