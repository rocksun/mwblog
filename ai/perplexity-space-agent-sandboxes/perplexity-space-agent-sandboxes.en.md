Sandboxes for AI agents may feel like a solved problem. After all, projects like Firecracker, the open-source microVM technology AWS built to power its own Lambda service, provide strong isolation off the shelf, and a growing roster of startups sells [managed sandboxes for agent workloads](https://thenewstack.io/agent-runtime-application-server/).

Still, Perplexity decided to go back to the drawing board because the team there was convinced that isolation isn’t actually where the hard problems are.

On July 15, the company launched SPACE, the sandbox platform that now runs underneath Computer, its [agent platform for knowledge work](https://thenewstack.io/ai-agents-knowledge-workers/).

![](https://cdn.thenewstack.io/media/2026/07/a3e666ae-1516431438094.jpeg)

*Nate Kupp of Perplexity*

In an interview with *The New Stack*, [Nate Kupp](https://www.linkedin.com/in/natekupp/), Perplexity’s vice president of infrastructure, says the real engineering went into managing state — that is, pausing, resuming, and forking agent sessions that can sometimes run for days or weeks — across the millions of sandboxes that Perplexity’s users spin up to use its [Computer](https://www.perplexity.ai/products/computer) AI assistant.

“What we kept coming back to was recognizing our needs and the needs of an agent system at our scale were pretty different than what you see from the existing players,” Kupp says.

The team wanted agents “to pause and resume and run tasks for not just hours but then days and weeks,” he says, with those sessions living on as persistent, durable artifacts.

## State is the hard part

It’s important to note that SPACE doesn’t try to reinvent the lowest layers of the stack. Kupp says the team uses Firecracker as its core building block and Kubernetes for its cloud deployments, with portability across environments, from the cloud to on-premises data centers to the laptop, as a design goal from the start.

Most of the work actually sat in the control plane above these microVMs. As Computer’s agent harness brings context into a sandbox, Kupp says, the system has to pause and resume sessions quickly, bring them back up on other clusters, and keep them “portable, forkable, so that we can branch off and run different threads in different directions.”

The foundation for that turned out to be [Btrfs](https://wiki.archlinux.org/title/Btrfs), the Linux copy-on-write filesystem, which makes snapshots and forks cheap metadata operations rather than full copies. “That’s been pretty key to a lot of the performance wins there,” Kupp says, and “was a very natural fit” for the pause, resume, snapshot, and fork operations SPACE is built around. “We did some early prototypes, very quickly found this was just a great fit, and have run with it,” he says.

On top of that sits what the company’s launch post describes as rolling snapshots of full session state, live memory included. Those snapshots happen as often as every minute, and a session can rewind up to a week.

Compared with the incumbent providers, Kupp says, “we’ve seen 3x or more speedups on all of the metrics that we care about for performance, and then pretty significant cost improvements too.” The team also spent heavily on tail latencies, he says, tuning P95 and P99 guarantees because sandbox performance sits directly in the user’s critical path.

“Stateful systems are incredibly hard to build,” Kupp says, pointing to the durability and uptime guarantees Perplexity has to hit while running millions of sandboxes.

## Knobs, not trade-offs

When it comes to the trade-offs between security versus performance, Kupp argues that “it’s less trade-offs and more where we’ve had to think about putting the knobs in the right places for our customers to control.” Since every customer plugs Computer into a different mix of Salesforce, Slack, Snowflake, and other data sources, each with its own risk profile.

Beyond what he calls the “table stakes” work of RBAC and other core enterprise features, Kupp says the team is focused on [agentic security](https://thenewstack.io/ai-agents-are-creating-a-new-security-nightmare-for-enterprises-and-startups/), including provisioning just-in-time access to downstream systems and setting controls at the level of individual tool calls.

An admin can disallow any write access, so an agent can’t write into a business system at all, he says, a hard, platform-level restriction rather than something left to model behavior. Computer will also flag sensitive actions and raise them to the user for approval. One thing SPACE doesn’t use yet is hardware-backed confidential computing, though Kupp notes the company works closely with Nvidia across its stack.

## Sandboxes everywhere

SPACE’s sandboxes today are largely homogeneous, one standard size tuned for Computer’s workloads. That will change, Kupp says, because “we will be offering this as an [API product](https://thenewstack.io/perplexity-agent-api/),” with flexibility over sandbox sizing for more heterogeneous external workloads.

Perplexity already announced a narrower [Sandbox API](https://www.perplexity.ai/hub/blog/sandbox-api-isolated-code-execution-for-ai-agents) in March, a code execution service for agents built on Kubernetes pods rather than microVMs, with a private beta to follow. The company also says Computer will soon work across third-party sandboxes, not just SPACE. “We’ve thought about these extension points at every level of the stack, from the sandbox layer to the APIs and MCPs,” Kupp says.

Kupp is also looking down the stack, at local and hybrid deployments. Perplexity has been partnering with Nvidia on the chipmaker’s RTX Spark platform for local AI workloads, he says, to bring orchestration down to the laptop.

The company recently released a research preview of a new orchestrator model for Computer: a version of GLM 5.2, the [open-source Chinese model](https://thenewstack.io/china-leads-open-ai-models/), post-trained for its harness.

Kupp says it delivered results at “a third of the cost of some frontier models.” The end state here, he explains, is an orchestrator that routes work wherever the economics make sense. “You can run it locally. You can run it remote in the cloud.”

That routing question is about to collide with a bigger one. As agents take on more of the work, Kupp says, “we’re really going to see a constraint on not just GPUs but CPUs too,” shifting a conversation that so far has been almost entirely about GPU scarcity. If agent sessions keep stretching from hours to weeks, the [fleets of CPUs that host them](https://thenewstack.io/cpu-agentic-ai-axion/), and the state machinery that keeps those sessions alive, start to look less like plumbing and more like the industry’s next capacity fight.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)