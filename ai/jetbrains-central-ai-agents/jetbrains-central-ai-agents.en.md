Deploying [AI coding agents](https://thenewstack.io/crafting-ai-agents-platform/) is no longer hard, but knowing whether they’re working and keeping them from becoming another unmanaged layer of enterprise sprawl is.

[JetBrains Central](https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/), announced last week by the Prague-based developer tools maker, is the company’s answer to that problem. It’s a governance and execution platform for [AI agent workflows](https://thenewstack.io/github-agentic-workflows-overview/).

[Oleg Koverznev](https://www.linkedin.com/in/oleg-koverznev/), a vice president and head of Agentic Platform at JetBrains, stated bluntly in a briefing with *The New Stack* that the industry is about to replay the cloud ROI crisis.

“Everyone knows AI is a game changer,” he said. “But it’s very hard to prove that implementing these systems is making a difference in what the return is for the business.”

When enterprises moved to the cloud, the first wave of investment was followed quickly by pressure to show ROI, and an entire category of cost management and observability tooling grew up around that pressure. JetBrains is making a similar bet on [agentic AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/), earlier than most.

JetBrains’ own AI Pulse survey of 11,000 developers in January 2026 found 90% already use AI at work, and 66% of companies plan to adopt coding agents within 12 months. But only 13% report using AI across the full software development lifecycle. “[Code generation](https://thenewstack.io/the-ai-code-generation-problem-nobodys-talking-about/) is cheap and no longer a bottleneck,” Koverznev writes in the launch post. “The real challenge is aligning outcomes with intent, along with managing the growing operational and economic complexity of [agent-driven](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/) work.”

## The coordination problem nobody’s talking about yet

Koverznev’s more pointed argument isn’t about ROI measurement — it’s about what happens when agent counts scale past the point where anyone has a clear picture of what’s running.

“We envision that in the future there will be teams of humans and agent co-workers,” he said. “The coordination across agents and humans is a big aspect — and this problem is emerging.”

Most organizations are still running agents in isolated pockets. But Gartner predicts 40% of enterprise applications will feature AI agents by the end of 2026, up from less than 5% today. At that scale, tracking what’s running, what it costs, and whether it did what anyone intended becomes a real operational problem.

JetBrains Central’s answer is a semantic layer that aggregates context from codebases, architecture, runtime behavior, and delivery infrastructure — giving agents system-level understanding rather than just prompt-level instructions.

“To get predictable results, we need to give agents the necessary context and the ability to understand the code,” Koverznev said.

That feeds into [Air](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/) Team, a collaborative workspace for delegating tasks to agents and tracking multi-step workflows, integrated with Slack, Atlassian products, and Linear. The argument is that agent workflows that don’t connect to existing team systems create a parallel coordination layer on top of the existing one.

## An open platform plays in a market moving toward lock-in

Most AI platform vendors are building closed ecosystems. JetBrains is going in the other direction, and Koverznev didn’t dress it up.

“We don’t want to own the stack,” he said. “We want to provide the system so that customers choose which tools, which agents — and we give them the ability to control it.”

Organizations can connect any IDE or CLI, bring their own API keys for OpenAI or other providers, and plug in external agents — such as Claude, Codex, or the Gemini CLI — via the Agent Communication Protocol without custom integration work. An on-premises option is planned.

“We’re standing on the shoulders of giants,” Koverznev said. “LLMs provide great intelligence — we don’t compete with that. We bring it all together into a controllable system.”

A no-lock-in pitch is only as strong as the integrations holding it together, and this market is not slowing down. Yet, JetBrains is at least eating its own cooking. “We’re increasingly leaning into agents and AI-driven workflows, which is creating a need for better visibility into costs and governance,” said [Hadi Hariri](https://www.linkedin.com/in/hadi-hariri/), SVP of Operations, in a statement. “That’s why we’ve started piloting JetBrains Central internally.”

## Pricing: Fixed governance, variable execution

Pricing is two-part: a fixed per-seat subscription for governance, covering JetBrains and third-party seats, and pay-as-you-go for agentic execution. Koverznev offered a range of pricing scenarios.

“One developer can spend $100 a month,” he said. “Another can orchestrate thousands of agents and spend $100,000. It’s really possible.” The platform’s job is to make that spending legible and to connect it to outcomes such as time-to-market and cost of delivery.

The Early Access Program launches Q2 2026 with a limited group of design partners to test JetBrains Central in real-world agentic workflows. Meanwhile. The open-platform bet only works if JetBrains reaches general availability before the market consolidates around someone else’s governance layer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)