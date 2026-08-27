**OpenAI’s unreleased foundation model**, codenamed Astra, is already working directly inside the company’s internal codebase, taking on experimental work that previously required as much as a week from a human researcher.

As part of a series of interviews with *[Time,](/https://time.com/article/2026/08/26/openai-sam-altman-interview/)* OpenAI chief scientist [Jakub Pachocki](https://www.linkedin.com/in/jakub-pachocki/) said Astra can take an idea for an experiment, turn it into code, run it, and return the results. A step beyond asking AI to fix a bug or write a function, OpenAI is essentially testing what happens when you hand the agent the experiment itself and let it figure out the steps in between.

For developers, Astra offers a glimpse into the future of coding agents. But giving an agent that much freedom creates another problem. Astra may already be powerful enough to trigger OpenAI’s highest-level cybersecurity safeguards.

> OpenAI is essentially testing what happens when you hand the agent the experiment itself and let it figure out the steps in between.

## Persistent agents change everything

OpenAI CEO Sam Altman described what the company is building as “persistent agents,” or systems that can keep working without needing a person to prompt them through every step.

Coding agents can already dig through a repository, change files, run tests, and try again when something breaks. Persistent agents are meant to keep going without a developer guiding them through each step.

That also changes what developers need from the tools around the agent. An IDE gives it somewhere to work, but a long-running agent needs infrastructure that can keep it running safely without constant oversight.

## Multi-agent coordination at scale

In one demonstration witnessed by *Time*, 16 Astra agents worked together on a research-level math problem, splitting it into smaller pieces and then bringing their work together into a proposed solution.

For developers, it’s not hard to imagine that same setup applied to a large software project, with different agents working on different pieces at the same time. OpenAI is already experimenting with that kind of coordination, along with agents that can stay on a job for much longer.

Running several agents at once also complicates the infrastructure behind them. Developers need a way to keep the whole operation under control. Giving agents that much freedom, though, has created another problem for OpenAI: keeping them under control.

## When agents escape containment

OpenAI said this month that preliminary evaluations indicate Astra may have reached the “Critical” cybersecurity capability threshold in the company’s [Preparedness Framework](https://openai.com/index/pacing-model-development-cyber-capabilities/), a finding the company [disclosed alongside a pause on some frontier workloads](https://thenewstack.io/openai-astra-cybersecurity-delay/).

Under the company’s framework, hitting that threshold brings stricter safeguards for how the model can be used.

OpenAI had already seen what could go wrong with agents that have access to tools. During a cybersecurity test, one of its internal AI agents escaped its sandbox and accessed Hugging Face systems without authorization. Astra was not the model involved, but the incident led OpenAI to pause some frontier-model research workloads while it tightened the infrastructure used to run them.

And OpenAI isn’t the only company running into this problem. Google’s AI coding agent [recently broke out of the boundaries of its IDE](https://thenewstack.io/google-antigravity-ide-extensions/). The circumstances were different, and the incident was less serious, but both point to the same problem that happens when giving an agent more freedom to act; you also have to make sure it stays where you put it.

Astra is now running under OpenAI’s strictest security controls. Some training and evaluation workloads have resumed, but OpenAI says a “significant number” are still paused while it upgrades the infrastructure behind them.

> Astra is now running under OpenAI’s strictest security controls.

## Monitoring costs real compute

The company also says it is monitoring Astra more closely when it uses tools, watching for behavior that could signal it is going beyond what it’s allowed to do. OpenAI estimates that monitoring adds about 20% to the inference compute for those workloads.

*Time* reports that OpenAI still plans to release Astra, although there’s no launch date yet. Until then, OpenAI is working through the same challenge developers could eventually face as agents work for longer stretches without human supervision and begin coordinating with other agents.

As agents take on more work, the IDE is only part of the picture. Developers also need a way to see what those agents are doing and keep them from going where they shouldn’t. OpenAI is already seeing the cost, with monitoring alone adding about 20% to Astra’s inference compute.

That kind of overhead could become another cost developers have to account for, along with the [governance around autonomous agents](https://thenewstack.io/enterprise-ai-agent-governance/) that sets boundaries on what they can do.

> OpenAI is already seeing what that costs, with monitoring alone adding about 20% to Astra’s inference compute.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)