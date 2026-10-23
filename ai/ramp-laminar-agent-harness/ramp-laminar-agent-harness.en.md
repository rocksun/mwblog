Ramp spent months testing managed agent APIs, open-source frameworks, and third-party platforms before concluding it would be better off building its own. The result is Laminar, an internal agent harness that took six weeks to reach a first version and now powers every agentic product at the fintech company.

> “We studied the other offerings on the market and decided that we could do better, move faster, and have stronger alignment to where we want to go by building in house.”

“We studied the other offerings on the market and decided that we could do better, move faster, and have stronger alignment to where we want to go by building in house,” [Sam Kronick](https://www.linkedin.com/in/sam-kronick-534075117/), the Ramp engineer behind the platform, writes in the company’s [engineering blog](https://builders.ramp.com/post/building-laminar).

In Tuesday’s post, Ramp detailed how Laminar brings agent execution, sandboxing, observability, and asynchronous workflows under a single platform. The architecture caught the attention of LangChain CEO [Harrison Chase](https://www.linkedin.com/in/harrison-chase-961287118/), who praised several design choices in his [X post](https://x.com/hwchase17/status/2112650555852275951), while pointing to similar work underway in [LangChain’s Deep Agents](https://github.com/langchain-ai/deepagents).

Ramp and LangChain are approaching the problem from different directions, but both point to a bigger shift in [agent infrastructure](https://thenewstack.io/kubecon-agent-harness-koordinator/). As harnesses take on more responsibility, enterprises have to decide how much of that infrastructure they want to build and maintain themselves.

## Why Ramp built in-house

Ramp didn’t want to be locked into one model provider. It needed the flexibility to switch models based on cost, speed, and performance, along with better visibility into how its agents behaved. Engineers were already digging through traces to find unnecessary tool calls, bloated context, and errors, but existing observability tools made that harder than it needed to be. So Ramp built its own debugging interface into Laminar. Keeping development in-house also meant the harness team could work directly with product engineers instead of waiting on vendors to make changes.

Chase agreed with Ramp’s priorities, particularly model independence and observability, both of which LangChain has emphasized in its own work. And, there were other parts of Laminar’s architecture that caught his attention.

> Keeping development in-house also meant the harness team could work directly with product engineers instead of waiting on vendors to make changes.

## Sessions split from sandboxes

Laminar runs everything from customer service agents to [Ramp Inspect](https://builders.ramp.com/post/why-we-built-our-background-agent), the company’s cloud coding agent, and Glass, which handles longer-running, collaborative work. Supporting these products requires a harness that can manage persistent sessions, human approvals, and work across environments.

Chase highlights Kronick’s observation that a production harness does far more than run a simple execution loop. “[+100 to this](https://x.com/hwchase17/status/2112650555852275951),” he writes, pointing to LangChain’s investment in Deep Agents.

Ramp keeps agent sessions separate from the sandboxes where code runs. Conversation history and execution state are stored independently, allowing sandboxes to spin up and shut down without disrupting a session.

Chase sees the [sandbox-as-a-tool approach](https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes) as a growing trend, noting that Deep Agents uses a similar design. It also keeps credentials and orchestration outside the sandbox, an important consideration as developers work to [isolate agents running untrusted code](https://thenewstack.io/webassembly-sandboxing-ai-agents/).

## Async agents by default

Laminar lets agents keep working without waiting for every step to finish. Chase describes non-blocking asynchronous agents as the future and says LangChain is developing similar functionality for Deep Agents.

Ramp’s Connectors Service also caught his attention. It centralizes authentication, credentials, access controls, and tool execution behind a shared API.

Chase says LangChain is exploring comparable features for managed Deep Agents. Centralizing those functions also gives platform teams a consistent place to manage access and credential handling rather than implementing them separately for every agent.

The harness is also where teams can trim inference costs, and LangChain has made that case directly. In an [October 1 engineering post](https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness), it describes moving model selection into the harness of [Open SWE](https://github.com/langchain-ai/open-swe), its open-source coding agent. A router examines the initial request and assigns one of three models based on expected task complexity, sending the simplest work to GLM-5.3-Flash, intermediate tasks to GPT-5.6 Sol, and the most demanding requests to GPT-6 Astra.

## Routing trims inference costs

Across 973 agent threads, the router cut median LLM costs from $2.61 to $0.94 per thread, a 64 percent drop compared with using GPT-6 Astra for every task. The savings didn’t come with a measurable hit to performance. Merged pull request rates were 29.2 percent for routed threads and 27.3 percent for the control group, a difference that wasn’t statistically significant. Ninety percent of requests went to the two less expensive model tiers.

> LangChain argues that routing works better inside the harness than at a generic LLM gateway, where there’s less context about what an agent is doing.

LangChain argues that routing works better inside the harness than at a [generic LLM gateway](https://thenewstack.io/respan-rust-ai-gateway/), where there’s less context about what an agent is doing. The harness already knows which prompts, tools, and domain context are involved, giving it more information to make that choice. LangChain uses [model-selection middleware](https://docs.langchain.com/oss/python/langchain/agents) to pick a model at the start of each thread.

The results don’t tell us whether building a custom harness is cheaper than using an existing framework. Ramp wasn’t part of the experiment. But they do show how much companies can save by making smarter model choices at the harness level, especially when their agents handle tasks with very different demands.

## The harness ownership dilemma

Ramp’s decision also shows how coding agents have changed infrastructure costs. Kronick says agents generated all of Laminar’s initial code, with experienced engineers guiding the architecture and implementation.

But building the first version in six weeks is one thing. Maintaining it is another. Ramp still needs engineers to handle incidents, update the platform, and support its product teams. The company also hasn’t published operating-cost comparisons or benchmarks against competing platforms, which makes it difficult to judge whether building in-house is cheaper.

LangChain offers another option. Rather than building a harness from scratch, companies can use frameworks that handle much of the underlying infrastructure, an approach other vendors are also taking as they [open-source their own harnesses](https://thenewstack.io/aws-strands-harness-agent/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)