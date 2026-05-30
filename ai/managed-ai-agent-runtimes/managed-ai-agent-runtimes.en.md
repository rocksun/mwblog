When Google announced last week at its I/O conference that it was [repositioning Antigravity as a platform for developing and managing teams of autonomous AI agents](https://thenewstack.io/google-io-antigravity-codemender-ai-agentic/), the pitch quickly took on a familiar arc.

For anyone paying attention to the space for the previous two months, the following felt a bit like *déjà vu:* One API call to the Antigravity agent spins up a remote Linux sandbox where the agent reasons, calls tools, runs code, and browses the web. You extend it by writing an `AGENTS.md` file and a `SKILL.md` file, register it as a named agent, and write no orchestration code.

I have watched this product ship twice already in the last two months, from two other vendors, and this trend says everything about how important managed agent runtime has become — it has become so important that it has become unimportant, a non-factor, because many labs are adding the service.

## The same runtime shipped three times in six weeks

Anthropic shipped [Claude Managed Agents](http://anthropic-wants-to-run-your-ai-agents-for-you/) into public beta on April 8. The pitch was that infrastructure — not intelligence — had become the bottleneck for production agents, so Anthropic would handle the agent loop, the sandbox, the state, and the credential scoping.

AWS followed on April 22 with a preview of a managed harness within [Bedrock AgentCore](https://thenewstack.io/openai-bedrock-trainium-silicon/). The runtime itself predates that release, [having shipped in 2025](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/), but the April update added the piece that matters here, a configuration-first harness that declares the model, tools, and instructions and runs the loop without bespoke orchestration code.

Then, Google at I/O, with Managed Agents in the Gemini API, did the same thing again.

Three vendors landed nearly the same runtime shape inside six weeks. Each launch post tells the same story: Building a production agent used to mean stitching together a model API, a sandbox, an orchestration layer, and hosting, and that the managed version collapses all of that into configuration and a handful of API calls.

When three companies independently converge on the same product within six weeks, the runtime has become table stakes rather than a reason to pick one platform over another.

## The Markdown file is becoming the config standard nobody voted on

Google’s Managed Agents are defined by `AGENTS.md` and `SKILL.md`. [Anthropic shipped Agent Skills](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/) as Markdown directories last year, and `SKILL.md` is now load-bearing across Claude Code and Managed Agents. [`AGENTS.md`](https://agents.md/) is an open format that grew out of work across OpenAI Codex, Cursor, Amp, Jules, and Factory, now sits in more than 60,000 open-source repositories, and is stewarded by the Linux Foundation. AWS leaned the same way, shipping prebuilt skills for Claude Code, Codex, Cursor, and Kiro alongside its harness.

So the agent is defined in a plain-text file that a developer can read, diff, and check into Git, with no proprietary DSL and no visual builder holding the definition hostage. The same file describes a Claude agent, a Gemini agent, or an AgentCore agent with very little edited between them. Models will keep leapfrogging each other on benchmarks, but the Markdown config is quietly becoming the portable layer beneath them all, the way a Dockerfile became the unit of a container long before anyone agreed it should.

## What it means for the developer choosing now

For a developer picking an agent platform today, whether a lab has a managed agent runtime is no longer the deciding factor because Google, Anthropic, and AWS all offer it. The decision moves to the boring questions: where your data sits, what a session-hour costs, which model runs underneath, and how hard it is to leave when the next model is better elsewhere.

The honest counterargument is that Markdown portability is shallow today. An `AGENTS.md` written for Gemini still assumes Gemini tool semantics, and moving it to Claude is not a non-starter. If the labs deliberately fork the format to make migration painful, the standard fractures before it sets. But the incentive runs the other way, because the vendor that makes its agents easiest to define also makes them easiest to leave, and right now, every one of them wants the developers more than it wants the lock-in.

The config file is where the next standards fight gets decided, so that is the thing to watch.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)