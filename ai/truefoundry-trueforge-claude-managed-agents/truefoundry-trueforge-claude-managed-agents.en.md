AI infrastructure platform company [TrueFoundry](https://90908956.streak-link.com/C_zjgFh2tnFZYzDI_gQtpMy5/https%3A%2F%2Fwww.truefoundry.com%2F) has launched its open source agent harness TrueForge. The technology is directly billed as an alternative to [Claude Managed Agents](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/), Anthropic’s hosted infrastructure service that runs, sandboxes, and orchestrates autonomous Claude agents.

TrueForge promises to allow software engineers to build, deploy, [debug](https://thenewstack.io/5-steps-to-debug-development-and-operations-teams/), and [govern](https://thenewstack.io/five-pillars-ai-governance/) production AI agents on any model (and the company means *any* model) or [MCP server](https://thenewstack.io/when-is-mcp-actually-worth-it/), while reducing total agent operating costs by an estimated 50%.

While open models such as [GLM-5.2](https://z.ai/blog/glm-5.2) from Chinese frontier model maverick [Z.ai](https://z.ai) are [challenging proprietary frontier models](https://thenewstack.io/open-weight-models-frontier-costs/) at lower costs, most managed agent platforms still lock enterprises into a single vendor’s models, infrastructure, and pricing.

## Challenging the pervading narrative of managed agent platform lock-in

Ex-machine learning tech lead at Meta and now co-founder and CEO of TrueFoundry, [Nikunj Bajaj](https://www.linkedin.com/in/nikunj-bajaj-10476824/), tells *The New Stack* that this pervading managed agent platform lock-in is precisely the logic behind his firm’s neutral approach to model vendor choice.

“A provider selling you a million tokens for $50 has zero incentive to tell you the same task could be done using a model that charges 50 cents for a million tokens,” Bajaj says. “Traditionally, one vendor provides the models, builds your agents and decides your token usage, in what order, and with what tools and under governance that the managed agent provider stipulates – and they’re selling the exact same setup to your competitor.”

Fundamentally, he insists, this means “the incentives are misaligned” here and so the “players in this game don’t get a voice to talk to the referee” in managed agent deployment scenarios where there’s always a tradeoff.

“Why should building powerful agents mean giving up control of your AI stack? We give developers the managed-agent experience without forcing them into one vendor forever,” adds Bajaj.

> **“A provider selling you a million tokens for $50 has zero incentive to tell you the same task could be done using a model that charges 50 cents for a million tokens. The incentives are misaligned, so the players in this game don’t get a voice to talk to the referee.”**

## The harness underneath becomes the strategic control point

Although Claude Managed Agents only [arrived as a beta release](https://claude.com/blog/claude-managed-agents?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) in April of this year, Bajaj and team think they can track an evolutionary curve being etched out here. This arc sees the first wave of AI agents existing on developers’ laptops, inside coding tools and prototypes. But the next wave is moving into customer-facing products typified by hosted infrastructure services with the ability to use shared workflows.

Crucially, that’s a shift that turns the harness underneath those products into a strategic control point, working as an execution layer in an operational loop between the user, the model and the systems it interacts with.

“This is indeed the reality: the harness is the critical layer between the user, LLM, and everything else,” clarifies Bajaj. “Say a developer is building an agent. They bring their own models, but the harness still decides when to call an MCP server, when to use an agent someone has already built, what context to keep, and which model handles which part of the plan.”

This means there are security implications, too. Bajaj specifies that “some actions” still need to run in a completely isolated sandbox, and some data should never be sent to a closed-source model.

“All of that logic sits in the harness. If software engineers don’t use one, then the developer team has to build all of that logic from scratch,” he adds.

## Enterprises will want to own key agent layers

In an open vendor-neutral approach to managed agent platform provision, organizations must manage persistent sessions, tool credentials, execution sandboxes, context, human approvals, debugging, access policies, and spending across every agent they operate. TrueFoundry is betting enterprises will want to own that layer rather than inherit it from a single model provider, but with enterprise governance built in at lower cost.

TrueForge routes every model call and MCP interaction through TrueFoundry’s AI Gateway, so budget enforcement, rate limits, and guardrails can be applied to deliver a governed and secure managed agent experience for enterprises.

## Headless chickens, when foo and bar are behind the wheel

When organizations don’t have the same hold on the steering wheel, Bajaj says that he has personally witnessed operations where [“foo” and “bar”](https://en.wikipedia.org/wiki/Foobar) (standard placeholder names used in computer programming for as yet-unnamed known metasyntactic variable values, rather like John Doe) end up becoming the doers of everything.

“Every action in the system came from a generic shared account, not a person you could actually identify. So when something changed or broke, you had no idea who to talk to. Once, when we were halfway through a migration from shared access to individual access, some keys were rotated. Half the company was still on the old account, and the system broke for half the company,” he explains.

Teams can run TrueForge on their own infrastructure, bring their own models, MCP servers, and API keys, and route each task to whichever model fits the cost, latency, or quality needs of that job. But does that mean workloads might become too fragmented that way?

“On the contrary, workloads become more uniform,” enthuses Bajaj. “Most teams already bring their own models by default. What changes is that organizations get to define what it takes for a model, agent, or MCP to belong in their registry. I call it the agent development life cycle, or ADLC. Once you own that, you can enforce the same operating principles across everything.”

In practice, the TrueFoundry team confirms it has seen most AI-centric software engineering operations converge on “roughly a dozen models” for typical tasks, plus a few specialized models for niche work.

## Is Anthropic doing something wrong?

TrueForge ships with support for OpenAI, Anthropic, and 20+ additional models, along with 40+ built-in tools, sandboxed execution, human-approval workflows, large-context handling, generative UI, and web search powered by Tavily. But despite offering a Claude Managed Agents alternative, Bajaj goes to pains to point out he doesn’t hold Anthropic up as some kind of pariah.

**“**This isn’t about Anthropic doing something wrong,” confirms Bajaj. “It’s that it doesn’t own every model in the world. Claude Managed Agents can only choose from the finite set of models Anthropic offers. There are open models that are terrific at certain tasks at a fraction of the cost, or simply more capable for that particular job. An open harness has a much wider set of choices.”

## When you own the harness, you can get rid of the parts that don’t apply to you

He underlines his point by pointing out that Anthropic also has to build one harness for a very broad set of customers; a truth that means its system prompt has to account for all kinds of instructions, guardrails, and corner cases.

“Many of those elements may have nothing to do with a developer’s own use case, but they still go into every call and add cost and latency. When you own the harness, you can get rid of the parts that don’t apply to you and make it extremely specialized,” he adds.

> “To be clear, we support Anthropic as a first-class provider because its models are great. There will be many cases where our users want to use them. The point is not to limit that choice to Anthropic alone.”

To validate its statements here, TrueFoundry has tested the above claim on a total of 14 level-one and level-two tasks from DevRev’s public Enterprise-Bench. The company says TrueForge “came in 50% cheaper at similar accuracy”, so the savings came from using fewer tokens and having access to models outside Anthropic’s set that were better suited to specific tasks.

“To be clear, we support Anthropic as a first-class provider because its models are great. There will be many cases where our users want to use them. The point is not to limit that choice to Anthropic alone,” Bajaj concludes.

TrueFoundry is also launching a hosted, pay-per-usage version of TrueForge for teams that want the same experience without managing the infrastructure themselves.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)