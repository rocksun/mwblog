**Put several AI bots to work**, and a mistake by one may not stay within its assigned task. For example, that error could reach another bot’s files and login credentials, or even the computer running them all. Two releases this month offered companies very different ways of containing that risk.

On August 17, [Nous Research](https://nousresearch.com/) announced that its [Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) would ship bundled and enabled by default in [Hermes Agent v0.20.3](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.16.2), turning agent profiles into a roster of named bots that hand off work to one another. About a week earlier, SpaceXAI launched [Grok Bot](https://x.ai/news/introducing-grok-bot) with almost the same interface: a sidebar of named teammates who sign in to your tools and keep working long after you close your laptop.

The interface converged within a week, but the answer to the question every platform team has to ask did not: *When one bot goes wrong, what can it reach?*

Four projects have now come to their own answer, and no two of them agree.

1. Grok Bot draws the line around the user account.
2. Hermes draws it around the profile.
3. [OpenClaw](https://docs.openclaw.ai/gateway/sandboxing) draws it around an optional runtime sandbox.
4. [ClawFleet](https://github.com/clawfleet/ClawFleet) draws it around a container.

Taken together, the documentation shows an industry converging on the persistent coworker interface far faster than it is converging on what constitutes an identity or a security boundary for it.

## Four projects, four written answers

Every one of these products now offers the same surface. You create several named agents, assign them different jobs, and have them pass work among themselves. The naming convention alone suggests separation, since a bot called Expense Manager and a bot called Talent Scout sound like they occupy different rooms in a shared office.

The documentation says otherwise, and it says something different in each case. The unit of isolation is the account in one product, the profile directory in another, an opt-in container in a third, and the deployment topology in the fourth. Those four units are not interchangeable, and an operator who assumes the roster itself is the boundary will be right in exactly one of the four cases.

## Is Grok Bot confused about what it wants to be?

SpaceXAI’s [launch post](https://x.ai/news/introducing-grok-bot) leads with the promise that bots have their own computer. The [documentation](https://docs.x.ai/grok-bot/computer-and-apps), last updated the same day, describes a single persistent cloud computer assigned to the user account rather than to any individual bot. Browser cookies and signed-in sessions are shared across the roster, files are visible to every bot, and command-line credentials are shared. One bot can pick up work that another bot saved.

Each bot gets its own screen on that machine, which allows several of them to run browser and desktop tools in parallel. SpaceXAI is direct about what those screens are not. The documentation calls them “separate work surfaces, not separate security boundaries.” It then instructs operators to keep a credential or file off the machine entirely if another bot on the account cannot use it.

The consequences run further than credentials. Signing in for one bot makes that session available to the others because the browser is shared. Installed [connectors](https://docs.x.ai/grok-bot/computer-and-apps) are account-wide, and their availability is not isolated to a single bot. The shared workspace sits at `/workspace` and is designed to survive computer updates and recovery, so the durable state is shared across the whole roster.

None of this is an implementation accident. It is what makes handoffs between bots cheap, and cheap handoffs are the product. But an operator reading only the launch page would build a mental model that the documentation contradicts, and that gap is where the risk sits.

## Hermes gives each bot its own profile

Nous took the opposite architectural position. In [Hermes](https://github.com/NousResearch/hermes-agent), a bot is a profile, and each profile has its own configuration, memory, skills, credentials, and chat history stored in its own directory on disk. Handoffs between bots run as real invocations against the named profile, rather than as a shared context blob passed around within a single process.

Nous shipped the teammate protocol as part of [v0.20.3](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.16.2), alongside the [MCP](https://modelcontextprotocol.io/) 2.x SDK migration and a set of runtime hardening changes. The company archived the [standalone plugin repository](https://github.com/NousResearch/Hermes-Bot-Mode) once the merge was completed. Bot Mode is on by default, so a Hermes user who updates gets the roster without opting in.

Two qualifications matter before anyone reads that as containment. A separate credential store does not guarantee different credentials, since what ends up in a new profile depends on how the operator created it and what they edited afterward. And every profile still shares the host machine, its operating system user, and its filesystem permissions. What Hermes documents is workstation-level separation of agent state, a meaningfully stronger default than a shared cloud account, but not the same as isolation.

## OpenClaw’s sandbox is off by default

OpenClaw documents the most complete boundary of the four. When the [sandbox](https://docs.openclaw.ai/gateway/sandboxing) is enabled with the Docker backend, agent tool execution runs inside isolated containers. At the same time, the gateway remains on the host, and the scope can be selected per session, per agent, or shared across agents. Each scope gets its own [workspace](https://docs.openclaw.ai/concepts/agent-workspace). Auth material lives per agent under an [agent-scoped auth profiles file](https://docs.openclaw.ai/concepts/multi-agent). Operators can configure network isolation, resource limits, and allow-or-deny tool policies on top of it.

The [documented default](https://docs.openclaw.ai/install/docker) for that sandbox mode is off. That is a defensible choice for a project most people run on a laptop, where the container overhead buys little against a single-user threat model. The underlying setup behavior deserves more attention. If sandbox prerequisites fail during setup, the script resets sandbox mode to off rather than refusing to start, so an operator who intended isolation and encountered a Docker socket issue ends up running without sandbox isolation. The documentation also warns against mounting the host Docker socket into agent sandbox containers and flags the CLI container’s shared network namespace with the gateway as a trust boundary in its own right.

ClawFleet answers the same question by moving it into the deployment topology. The project documents a [wrapper](https://github.com/clawfleet/ClawFleet) that puts each OpenClaw or Hermes agent in its own Docker container with an isolated filesystem and network. It lists roughly 500 MB of memory per OpenClaw instance and 150 MB per Hermes instance. That cost is why the other three projects make the boundary optional or skip it, and naming the number makes the trade-off legible.

## How to choose which bot is right for you

| Scenario | Documented fit | Rationale |
| --- | --- | --- |
| Persistent work that must continue with the laptop closed | Grok Bot | The only one of the four with a vendor-run always-on cloud computer, at the cost of one shared credential surface for the whole roster |
| Several agents with genuinely different credential sets on one workstation | Hermes | Per-profile stores are the documented default, and Bot Mode ships on |
| Untrusted or multi-tenant agent sessions | OpenClaw with sandbox enabled | Per-agent or per-session container scope with configurable network and tool policy, provided the operator turns it on and verifies it |
| Isolation as the deployment model rather than a runtime setting | ClawFleet | Container per agent with separate filesystem and networking, at a documented memory cost per instance |

## Each project gives operators different advice

The operational guidance diverges as sharply as the architecture. OpenClaw’s docs read like infrastructure documentation, naming specific hazards such as the Docker socket and the shared network namespace, and telling the operator what not to do. Hermes documents the profile layout and the protocol, then leaves policy to the operator. Grok Bot’s guidance is largely the warning itself, an instruction to treat the account as the boundary and to keep sensitive credentials off the shared machine entirely.

Grok Bot carries a second disclaimer worth reading alongside the first. Sensitive actions route through an [approval mechanism](https://docs.x.ai/grok-bot/approvals-security-and-privacy). SpaceXAI documents the categories that trigger it, including sending messages, publishing content, purchases and transfers, deleting data, and touching production. Enforcement runs through an LLM classifier. [Cursor](https://cursor.com/)‘s documentation for that same engine states plainly that the classifier is not a security boundary and can make mistakes. A buyer evaluating the product therefore finds the phrase twice, attached to the two mechanisms they would most reasonably assume protect them.

## AI agents still lack identities of their own

Enterprises can adopt any of these four products today and get real work done, and the honest reading is that all four are engineering their boundaries in good faith against different threat models. What none of them provides is an identity for the agent. In every case, the bot borrows the operator’s credentials, whether from a shared cloud browser, a profile directory, or a container volume, and the entire security conversation boils down to how far those borrowed credentials travel.

> “There is no primitive to standardize on, so each project has invented a boundary at whatever layer it already controlled, the account, the profile, the runtime, or the container.”

That is why the four answers differ so much. There is no primitive to standardize on, so each project has invented a boundary at whatever layer it already controlled: the account, the profile, the runtime, or the container. Expect to see that gap close on the identity side rather than the agent side, through scoped delegation and per-agent credentials issued by the identity provider, rather than being copied from the human. Until then, the useful move for platform teams is unglamorous and specific. Read the security page before the launch page, because for this class of product, they describe different things.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)