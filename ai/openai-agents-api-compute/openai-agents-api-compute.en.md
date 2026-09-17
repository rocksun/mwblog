**OpenAI rolled out its Agents API** in public beta Thursday, opening the backend behind Codex to developers looking to run agents unattended for days.  
  
Now, developers don’t have to build their own system to keep an agent going because the API tracks the job as it progresses and gives the agent somewhere to execute its work, even when a task stretches well beyond a single context window.

That makes long-running agents easier to try, but it also gives developers more ways to burn through compute. Interestingly enough, on the same day Agents API launched, OpenAI paused new sign-ups for its $200-a-month Pro plan after demand for GPT-6 Astra strained capacity.

[Thibault Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/), engineering lead for Codex, writes on X that Pro subscriptions “put the most strain on our systems,” adding that OpenAI was working to add capacity “as fast as we can.”

The Agents API and ChatGPT Pro are separate products, so there’s no reason to assume one is taking capacity from the other. Still, the timing stands out: the company is making it easier for developers to run agents for hours or days while [pulling back access to its heaviest-use consumer plan](https://x.com/thsottiaux/status/2098113585683808624) and working to add more capacity.

## Agent inference adds up fast

As a task gets longer, the API can compress earlier context, so the agent doesn’t just stop when it reaches the model’s context limit. It can also bring in tools only when they’re needed or send parts of a larger job to subagents working in parallel. The actual work can run in OpenAI’s sandbox or on infrastructure the developer controls.

> The actual work can run in OpenAI’s sandbox or on infrastructure the developer controls.

As agents make progress, they go back to the model for the next step, and a job that takes hours can rack up far more inference than a typical API call. The usage climbs even faster when agents work in parallel.

OpenAI has already seen this inside its own shop. In a [research report published September 6](https://openai.com/index/research-acceleration-view-inside-openai/), OpenAI said its research organization was logging 3.1 agent-workdays for every human workday by mid-August, measured in standard eight-hour equivalents. The median researcher, ranked by agent usage, was spending more than $600 per day on inference at API prices, while [the 90th percentile exceeded $7,000](https://thenewstack.io/openai-agent-research-bottleneck/).

Before June, OpenAI’s researchers were still putting in more hours than their agent, but by mid-August, the agents were doing three times as much work.

Arguably, OpenAI’s researchers are an extreme case, but the numbers show what happens when agent use starts to scale. One person can suddenly generate far more inference than their headcount would suggest.

> One person can suddenly generate far more inference than their headcount would suggest.

## Friction limited compute demand

The Agents API lowers the cost of that experimentation by leaving the orchestration layer out of the bill. Developers pay for the models, tools, and hosted compute their agents actually use.

The flip side is that it’s now easier to consume more inference. Context compaction is a good example. A full context window used to force developers to decide what to discard or how to summarize the work so far. Now the API handles that automatically and the agent keeps going. That’s useful for developers, but it also means the workload doesn’t stop when the context window fills up.

## Astra demand hit the ceiling

The Astra rollout offers a preview of what that could look like. OpenAI stopped accepting new Pro subscribers less than two weeks after [the model launched on September 3](https://thenewstack.io/gpt6-astra-developer-access-delayed/), saying those accounts put the most strain on its systems. The Agents API has its own rate limits and usage tiers, so the Pro pause doesn’t directly affect developers using it. Still, the company is already having to manage capacity around its newest model.

## Infrastructure outweighs benchmarks now

The more agents developers run, and the longer they run them, the faster that usage adds up. One developer might have several agents working at once, each going back to the model throughout the task. So headcount alone doesn’t tell you much about how much compute you’re using.

For long-running agents, the challenge is keeping the work moving without wasting tokens or losing track of the task. [Cloudflare made a similar bet this summer](https://thenewstack.io/cloudflare-ai-web-economics/), arguing that the infrastructure around AI workloads would eventually matter as much as the models themselves.

> For long-running agents, the challenge is keeping the work moving without wasting tokens or losing track of the task.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)