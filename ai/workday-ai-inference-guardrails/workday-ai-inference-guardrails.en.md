**Workday, the payroll and HR data platform,** has been pursuing AI and agents for a while, but while other businesses may allow a little room for error, getting a payroll run in Workday 99% right is not exactly good enough.

[Gabe Monroy](https://www.linkedin.com/in/gabemonroy), Workday’s chief technology officer, tells *The New Stack* that enterprise AI has to clear this bar before anyone will let it near their HR and finance data.

“There aren’t many systems that are more critical — or less forgiving — than ones that are dealing with people and money,” he says. There’s no tolerance for “well, it works most of the time,” Monroy says in an interview.

At its [DevCon developer conference](https://blog.workday.com/en-us/workday-devcon-2026-going-agentic-building-future.html) in early June, Workday laid out its plans to clear this correctness bar. The company introduced [Agent-Ready Tools](https://newsroom.workday.com/2026-06-02-Workday-Launches-New-Tools-for-Developers-to-Build,-Connect,-and-Verify-AI-Agents-For-HR,-Finance,-and-IT), a set of connectors that let agents act across the platform over the Model Context Protocol (MCP), a Developer Agent that lets people build apps and agents on Workday in plain language, and [Agent Passport](https://newsroom.workday.com/2026-06-02-Workday-Launches-Agent-Passport-to-Test,-Verify,-and-Continuously-Monitor-Every-AI-Agent-in-the-Enterprise), which tests and verifies agents before they go into production and keeps monitoring them after, with Cisco as the first attestation partner.

## Guardrails belong in the inference engine

Monroy spent most of his career in infrastructure and the developer space: at Deis, Microsoft, DigitalOcean, and, most recently, Google. At Google, he focused on building infrastructure for large AI labs to run inference at scale. For someone so focused on infrastructure, coming to Workday might seem a bit like an odd move, but Monroy argues that, at this point, LLM safety is — or at least should be — part of the core infrastructure for enterprises.

> “The stakes are higher … in the world of people and money”

“The stakes are higher in the world of Workday and in the world of people and money, and that’s something that I was really excited about tackling at Workday specifically — and I do look at it as a core infrastructure,” he says. “A lot of what I’ve been doing in my recent past has been building infrastructure for large AI labs to do inferencing at scale, and what you pick up pretty quickly is that inferencing is probabilistic.

“[Inferencing] involves prefill and decode, and a whole bunch of really technical machinery in place to stream tokens out to end users, but what is nowhere in that stack today is the concept of native LLM-level enforced guardrails — guardrails that are part of the core inference.”

In his view, making it safe for enterprises to operate inference at scale has to be done at the inference engine layer. Agent gateways and similar add-ons that wrap the model from the outside sit at the wrong layer, he argues.

![](https://cdn.thenewstack.io/media/2026/06/6858d517-1634663536418.jpeg)

Workday CTO Gabe Monroy

For a system of record like Workday, the system must strictly enforce guardrails on who the user is, what their budget authority is, and where they sit in the org chart. Those constraints, Monroy says, can be wired deep into the inference rather than checked after the fact. “These are things that we have the opportunity to wire deeply into the inferences at a very, very low level, in a way that produces much safer outcomes,” he says.

Workday’s recent [acquisition of Pipedream](https://newsroom.workday.com/2025-11-19-Workday-Signs-Definitive-Agreement-to-Acquire-Pipedream) partially plays into this. With Pipedream, an agent can reach out to third-party systems outside Workday to, for example, pull a policy document from Google Drive, and the platform can then verify that this specific agent has all necessary access rights to do so.

## “Bring it to our shop”

All of those agents need to be managed, of course, and while many SaaS companies are currently [building out their own agent platforms and agent orchestration services](https://thenewstack.io/sap-ai-agent-hub/), seemingly all offering the same services, Monroy argues that orchestration should happen close to the data sources.

“If you’re trying to run an agent interaction that is integrating with people and money, that orchestration loop should probably happen closer to Workday, ideally on the Workday,” he says. “I do think there is something to be said for inference engines having proximity to the underlying system, because when it comes to a low-level inference engine and runtime perspective, there are some differentiated things you can do at the inference engine level that are only possible due to proximity to.”

> “I do think there is something to be said for inference engines having proximity to the underlying system…”

He likened it to car repair. If somebody hands you a toolbox, you may or may not be able to fix your car’s problem. “Maybe you’ll get the outcome, but I tell you what, if you really want your car repair done right, bring it to our shop. We got the hydraulic lift, we got the trained engineers who know how to do this stuff, and we got the tools — but our tools are the best in the industry.”

For the part of an agent’s orchestration loop that has to run next to HR and finance data, “you really should be running that in our shop.”

For more general-purpose workflows, though, he believes there is room for general-purpose platforms. Not everything needs to run on Workday, after all, and Workday does offer MCP servers that third-party tools can tap into to access its data and tools as well.

To some degree, every system-of-record vendor is making some version of the [proximity-and-context case](https://thenewstack.io/sap-sapphire-ai-context/) right now. Owning the context for AI agents to work with is a [major moat](https://thenewstack.io/hyland-enterprise-context-engine-agents/) for these companies, after all, even as APIs and MCP servers allow agents to pull in data across vendors.

Meanwhile, there is also a group of other companies positioning themselves as neutral parties benefiting from the fact that these other vendors are now opening their platforms to third-party agents. It seems unlikely that, in the long run, enterprises will want to manage multiple agent platforms, but at this point, it is still far from clear in which direction this pendulum will swing.

If proximity is where Workday thinks it can win, there is one area where the company doesn’t want to compete: developer tools.

“We’re not going to differentiate Workday on building better tools for developers,” Monroy says. “We’re going to differentiate on safety, on trust, on the inference engine.” It’s telling that the demos at DevCon ran on Claude Code, Cursor, OpenAI’s Codex, and Google’s Antigravity rather than on anything Workday-branded. “On the tooling front, I’m happy to have Claude Code and Codex and others,” he says.

It’s no secret that [developer loyalty to AI tools doesn’t really exist](https://thenewstack.io/github-wants-developers-back/) at this point. Developers definitely don’t want a one-off tool from a single vendor, and Monroy notes that he isn’t going to ask them to adopt one. Instead, Workday wants to own skills, which he calls “the underlying lingua franca that we’re using to converge across the system.”

Workday is happy to be the system of record for its vertical and to let others fight over the tools.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)