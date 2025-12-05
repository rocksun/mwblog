In November 2024, Anthropic published a seemingly innocuous blog post entitled [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol). In it, they promised that Model Context Protocol (MCP) would provide “a universal, open standard for connecting AI systems with data sources, replacing fragmented integrations with a single protocol.”

Tech companies say lots of lofty things, but in its first year, it’s hard to build a case that says Anthropic overpromised. MCP still has room to improve, but the protocol filled a need and has found its audience fast. Let’s dig into why, and where it might be headed in 2026 and beyond.

## A Little History

We leaned in on [building an MCP server](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/) at Sentry very early, and in the past 30 days alone it’s served over 278m requests, across more than 5,000 organizations. Those numbers ***sound*** great — but getting here was… rough.

For anyone building in the earliest days of MCP there were [A LOT of bumps](https://cra.mr/mcp-is-not-good-yet). Because of the [scale our company operates](https://thenewstack.io/can-companies-really-self-host-at-scale/) at, we ran into a lot of them early.

Like most technologies, MCP saw a lot of shifts early on — across the protocol itself and the platforms that ended up supporting it. The first days of MCP were full of hacked-together things like locally running with chained-together commands, or CLIs to help duct-tape together remote support. Outside of Anthropic’s products — which makes sense, given they built it — most LLMs’ support for MCP was pretty sketchy.

A year later? It’s still not perfect, but it’s definitely on much more solid ground. It’s also clearly not going away any time soon.

Cloudflare jumped in headfirst here and became a “go-to” for platforms to build a full-featured MCP server on. They shipped [framework helpers](https://developers.cloudflare.com/agents/guides/remote-mcp-server/), [OAuth support packages](https://developers.cloudflare.com/agents/model-context-protocol/authorization/#2-third-party-oauth-provider), made [durable objects](https://developers.cloudflare.com/durable-objects/get-started/) more approachable, all through the Cloudflare Workers platform. Vercel followed suit, introducing [mcp-handler](https://github.com/vercel/mcp-handler) as an easy way to create MCP servers as API routes in Next.js, and shipped their own authentication support and functionality along with it.

Over the past twelve months, MCP has grown from a curious, complex spec to a pretty much mandatory feature of any LLM client — whether it’s the terminal-heavy TUIs currently on the rise, or more fully featured editors like Cursor.

We hit our share of challenges and lessons learned building around MCP, and we’ve got a lot of hopes for where it’s going next.

## Lessons Learned: Building MCP Servers at Scale

Do we know everything there is to know about building the perfect MCP? Nope! No one does. This stuff is new-new. But here’s some stuff we’ve picked up along the way:

### **You’ll Need To Figure out What’s Breaking, Where, and for Whom**

[![](https://cdn.thenewstack.io/media/2025/12/10e4a3ed-image1-1024x586.png)](https://cdn.thenewstack.io/media/2025/12/10e4a3ed-image1-1024x586.png)

Being so new, MCP broke… a lot, in the early days.

We needed better ways to understand exactly where that was happening in the code, which tool calls were flaking the most, which users things were breaking for, and most importantly: which combinations of clients/protocols were running into these various issues.

Sentry has a lot of tooling that helps with similar use cases, but there were absolutely gaps due to the combination of MCP being such a different approach to software, and running on top of Cloudflare workers.

Realizing we probably weren’t the only ones who needed this, we folded the functionality we built for monitoring MCP into Sentry for everyone to use.

Looking back, more standardization at a spec level would’ve gone a long way in ensuring an easier path forward for monitoring the way MCP interacts with both clients and the actions it takes.

A lot of this observability falls back on the LLMs today, but we’re absolutely seeing a rise in people wanting a clearer understanding of what’s happening under the hood with their MCP servers. MCP feels like magic until it breaks and you’re digging for why.

Complexities are going to continue to pop up as different platforms approach the problem in slightly different ways. For our part, we’re staying as close to the application code as possible — and choosing to wrap Sentry around the MCP server layer itself.

### **Remote First… but Also… Local?**

Running the first generation of MCP servers largely involved cloning down a repo, dropping them into specific directories, and then battling with node path issues until you got a green connection indicator. Layer on challenges like local dependencies, or creating/storing API tokens… It was a high-friction experience, not to mention being error-prone. Day-2 updates were annoying to try and manage.

Remote servers sidestepped many of these challenges, and in the early days were supported largely by using [mcp-remote](https://github.com/geelen/mcp-remote) to connect standard MCP servers as remote. There were a few other proxy solutions, but none of them really took off. This created a really spotty support ecosystem in common editors and tooling.

Reading the room on where all this was going, and how we could keep fiction low for users as well as enable them to just “consume” the service, we opted for a primary path of remotely hosting our MCP. Hosting remotely had a lot of benefits – it lets you continually add new functionality without the user having to install a new package or clone anything down, you’re able to centrally monitor the service and optimize around the standard user paths, and if you do it right, you also get to simplify the way you manage user access through things like OAuth.

[Remote MCP servers](https://thenewstack.io/remote-mcp-servers-inevitable-not-easy/) are pretty easy to implement (especially using the Cloudflare / Vercel tooling I talked about earlier) these days — and you gain a lot from a maintenance standpoint on running them remotely (namely, no worrying about if users are updating their local code.)

It’s still a good idea to have local options also. Keeping a local STDIO version handy gives you the ability to test locally, and also gives you some flexibility around the few clients that don’t support OAuth in remote MCP yet (there are a few out there).

Over time, OpenAI embraced the spec, and started [including it in their own tooling](https://openai.com/index/new-tools-and-features-in-the-responses-api/). We’ve watched the shift from STDIO servers that were cloned from GitHub and run locally, into remotely hosted MCP servers that bundle auth. Now we’re watching as the different client platforms race to support and leverage each revision.

### **MCP Goes Wider, and Then, Narrower**

With MCP servers it’s really easy to fall into the trap of building a tool for everything, and trying to just replicate what you’re doing in APIs inside MCP tool calls. But it turns out having dozens of bloated token-heavy MCP tool calls is a good way to blast through token limits *fast.*

The problem with this approach is that with MCP, every time you make a call, the full tool list is sent with every prompt. Every call, you’re eating away at that precious context window. On top of the tool calls, any resources you create or prompts you attach are also sent.

Context windows are getting bigger, but the wasted space from context bloat adds up very quickly, and it gets exponentially worse the more complex calls you make or tool calls you chain together.. We’re coming into a time where the MCP builders are pulling back on the tools they expose by default, either by scrapping unnecessary tool calls entirely, or by giving users options to let them reduce which tool calls are exposed to the client.

[![](https://cdn.thenewstack.io/media/2025/12/f553617c-image3-1024x668.png)](https://cdn.thenewstack.io/media/2025/12/f553617c-image3-1024x668.png)

We opted for this route in our own MCP, mostly so we could still keep some of the useful functionality but also give our users a choice in how much they wanted to expose. We removed several tool calls that weren’t being used at all, reduced the available resources, and removed the additional prompts. We also added an enhancement at the OAuth consent screen that lets you configure which tool groups you want to expose in the MCP, allowing a finer level of control. Give developers the tools they need, but don’t eat their precious context window with what they don’t.

### **SSE Is Fading out, HTTP-Streamable Is in**

In the early MCP ecosystem, Server-Sent Events (SSE) were the default [way to stream data](https://thenewstack.io/how-to-build-applications-over-streaming-data-the-right-way/) from a server to a client. SSE is simple and worked well enough early on, so it made sense to use it when we were first prototyping things. But it’s built on top of a long-lived HTTP connection that can be, well, finicky. Among the challenges: SSE’s long-lived connection required specific infrastructure decisions to support, and in the event of failure, there was no clean way to resume sessions.

Eventually, OpenAI introduced HTTP Streamable, a more robust streaming format designed specifically to fix the pain points that people were starting to have. Pretty quickly thereafter, we made the call to move away from SSE to HTTP Streamable.

SSE had a lot of limitations — and even though it took several months to get here, the major clients all support HTTP Streamable now. We’re finding connections to be much more stable overall after the move.

[![](https://cdn.thenewstack.io/media/2025/12/167d5d3b-image2-1024x423.png)](https://cdn.thenewstack.io/media/2025/12/167d5d3b-image2-1024x423.png)

We’re still in the transition time; many servers are still leveraging SSE as their default protocol, but I anticipate this is going to quickly shift. HTTP-Streamable ends up giving a far simpler implementation experience overall, and a better user experience for consuming it.

### **MCP as a Workflow**

The most successful MCP servers at this point I see are ones that are designed to fit right into users’ existing workflows. As much as possible, these tools need to meet users where they are.

A great example of this is the recently released [Chrome Dev Tools MCP server](https://developer.chrome.com/blog/chrome-devtools-mcp). This MCP makes it easier for developers to have MCP fire up a browser; to see beyond the code, and get a view of what a running app actually works/looks like. The [Resend MCP server](https://resend.com/docs/knowledge-base/mcp-server) lets you take the context of things you are building, and easily email it out to users alongside your generated templates. If you’re an iOS developer, the [Xcode MCP server](https://github.com/cameroncooke/XcodeBuildMCP) makes it easy to give models more visibility into your Xcode environment.

We’ve even started working on a new MCP server that is designed to be used with [Spotlight](https://spotlightjs.com/), to help with local debugging as opposed to the standard Sentry’s hosted model. This gives us a clear separation of functionality where the standard Sentry MCP is designed for the core of Sentry’s platform functionality – but we can now enable some specific local debugging workflows as well, and create scenarios where the MCP servers can work together across tool calls.

## **What’s Next for MCP?**

So what lies ahead for MCP? As someone that’s been building here for a while now, here’s what I see coming:

* **Protocol is set — HTTP Streamable is so in**. There’s a bit of noise around adding deeper [Websocket support](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/493?utm_source=chatgpt.com) overall, but ultimately, HTTP Streamable is likely to be the primary path for a long while — with fallback to SSE as needed.
* **OAuth 2.1 will require some work, but building for it now will pay off in the long run** — The move from OAuth 2.0 to 2.1 has some sharp edges in it, no doubt, but the ecosystem is quickly converting to 2.1 as the standard path forward. Put the work in now and it’ll pay off later. For servers that the use case fits, no one wants to tell users to pull manual tokens for authentication.
* **MCP Tool consolidation is very much the vibe** — Developers will continue to look for ways to reduce the total tool sprawl within their MCP environments, as a mechanism to control token utilization. Expect more customization options around tool exposure, and ways to introduce more dynamic tool usage (like the natural language search in the Sentry MCP)
* **Agent loops powered by MCP** — With the major providers all adding MCP support directly into their agent SDKs, it’s a pretty strong signal that these are first-class tooling for agents to consume. I expect MCP to become more and more a first-class citizen in these workflows, as [ways to](https://thenewstack.io/3-ways-intelligent-automation-can-break-down-devsecops-silos/)extend the functionality of systems intelligently. We’re seeing people expose [more agentic flows with MCP,](https://cra.mr/subagents-with-mcp) which is creating some new and interesting ways to leverage it. It’s creating a balancing act between context conservation and making these tools actually useful

Over the past year we watched the MCP shift around on unsteady ground — both as the protocol itself evolved, and as people figured out some best practices. It’s still the earliest of days — and MCP will certainly have plenty of more evolution points over the next year — but many of these areas are starting to firm up now; if you’ve been waiting for things to be a bit more stable before diving in, now might be the time.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/01/ccbba06f-cropped-05c5e023-cody-dearkland-e1675186947773.jpg)

Cody De Arkland is the head of developer experience at Sentry, where his team focuses on helping developers build and ship software more safely. He's an engineer, product leader and marketer but mostly loves helping teams figure out how they...

Read more from Cody De Arkland](https://thenewstack.io/author/cody-de-arkland/)