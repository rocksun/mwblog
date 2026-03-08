AI coding agents are proliferating, but the economics of running large language models (LLMs) are breaking down as developers juggle multiple APIs and seriously unpredictable token bills. This is particularly problematic when agents start making dozens of model calls just to complete a single request.

The response from the developer community has been open-source coding agents, which operate one layer above the models. They keep costs consistent because they’re independent of — and work across — many LLMs.

[OpenCode](https://opencode.ai/) is one such player, which last week introduced [OpenCode Go](https://opencode.ai/go), a $10-per-month subscription designed to make those workloads easier to manage.

## The agent layer takes center stage

The rise of coding agents such as OpenCode also points to a shift in where value may sit in the AI software stack. Much of the early attention in generative AI centred on the capabilities of LLMs themselves. Tools like OpenCode scan repositories, interpret developer instructions, break tasks into multiple steps, run commands, and apply changes across a project. In effect, they translate a model’s general reasoning ability into concrete actions inside a codebase.

A growing number of similar open projects are exploring this space. Alongside OpenCode, tools such as [Kilo Code](https://kilo.ai/) (16.3k stars on GitHub as of writing) are experimenting with similar open-agent architectures while [introducing their own paid tiers](https://www.forkable.io/p/kilo-an-open-source-coding-agent) to cover infrastructure costs. [Cline](https://github.com/cline/cline), an open-source VS Code extension that emerged from an Anthropic “Build with Claude” Hackathon in 2024, has 58.7k GitHub stars. Meanwhile, [Aider](https://aider.chat/) (currently at 41.6k GitHub stars) has evolved over the years and is one of the most established open-source coding agents.

Projects like these mark the emergence of a new layer of developer tooling built around LLMs. The agent is the interface that developers interact with: software that interprets tasks, navigates repositories, and coordinates the model calls that produce the final output.

And much like the broader software sphere, subscriptions have become the standard way to package them. Tools such as [Anthropic’s Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/), [OpenAI’s Codex](https://thenewstack.io/openais-codex-is-now-on-windows/), and [Cursor](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/) combine model access with an assistant that can read repositories, propose edits, and execute tasks across a project. The subscription layer typically bundles model usage into a single monthly plan, reflecting the heavy prompt traffic these systems generate.

OpenCode approaches the problem from a slightly different angle. It’s an open-source coding agent that runs in the terminal (a [desktop app](https://opencode.ai/download) is also available in beta) and connects to whichever models developers want to use. OpenCode acts as a neutral layer between a developer and the models, allowing the same agent to operate with systems from OpenAI, Anthropic, Google, or open models hosted elsewhere.

## Open source agents are pulling ahead

OpenCode quietly emerged in 2024 from the team behind Serverless Stack ([SST](https://sst.dev/)), an open source framework for building applications on Amazon Web Services (AWS). Several of the same developers are involved, including [Dax Raad](https://x.com/thdxr), alongside [Jay V](https://www.linkedin.com/in/jayair/) and [Frank Wang](https://www.linkedin.com/in/fanjiewang/), who run developer tools company [Anomaly](https://anoma.ly/).

Throughout 2025, the project gained significant traction. According to [Runa Capital’s ROSS Index](https://www.forkable.io/p/the-20-hottest-open-source-startups-2e9) of fast-growing commercial open source startups, the [OpenCode repository](https://github.com/anomalyco/opencode) reached 44.6K GitHub stars by the end of last year, placing it among the fastest-rising projects. The repo has continued to grow, too, passing 117K stars as of this writing in March 2026.

Part of the appeal lies in OpenCode’s flexibility. Many of the major coding agents are tightly aligned with a particular model provider — for example, Anthropic’s Claude Code or OpenAI’s Codex. Cursor, for its part, exposes a curated set of models inside its editor environment. OpenCode, however, allows developers to connect their own providers and API keys, supporting dozens of model providers and even locally hosted systems.

That flexibility becomes more relevant as model providers tighten control over how their systems are accessed. Anthropic, for example, [recently tightened Claude restrictions](https://venturebeat.com/technology/anthropic-cracks-down-on-unauthorized-claude-usage-by-third-party-harnesses) after discovering that some third-party tools — [including OpenCode](https://github.com/anomalyco/opencode/issues/6930) — were routing Claude Code subscription access through external agents. The change prevents Claude Code subscription credentials from being used outside Anthropic’s own tooling, although developers [can still access Claude models](https://thenewstack.io/anthropic-agent-sdk-confusion/) through the standard API inside tools such as OpenCode.

The move appears aimed at a pattern some developers had adopted: running intensive agent loops through flat-rate subscriptions that would otherwise cost far more under usage-based API pricing. By contrast, [OpenAI models remain usable](https://x.com/thdxr/status/2009803906461905202) inside third-party agents such as OpenCode, reflecting growing competition between model providers seeking to win over the developer community.

OpenCode Go builds on that model flexibility by offering a bundled option. Instead of requiring developers to connect external providers themselves, the $10-per-month plan includes access to several models directly inside the tool, including [GLM-5](https://z.ai/blog/glm-5) from Zhipu, [Kimi K2.5](https://www.kimi.com/ai-models/kimi-k2-5) from Moonshot AI, and [MiniMax M2.5](https://www.minimax.io/news/minimax-m25). All three models come from Chinese AI labs and are widely considered cheaper to run than many Western frontier systems, helping make a low-cost subscription feasible for a tool that may generate large volumes of model calls.

Coding agents, of course, tend to generate bursts of model activity rather than sustained activity. A single request can trigger dozens of model calls as the agent scans a repository, proposes changes, runs commands, and revises its output. That pattern can produce large volumes of tokens in a short period.

Open source keeps this new agent layer malleable, allowing developers to inspect, modify, and swap the components that shape how those agents behave. That token-intensive behavior is also what makes OpenCode Go’s pricing noteworthy: A relatively low $10/month open-source subscription signals that the cost of running these models has dropped enough to make a low-margin subscription viable, which is a meaningful signal about where the underlying economics are heading.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)