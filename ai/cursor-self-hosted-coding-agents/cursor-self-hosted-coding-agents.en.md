For AI coding agents to work effectively, they need access to a broad range of systems — from private repositories and dependencies to internal tools and build pipelines. However, many companies are reluctant to grant that level of access to external services due to security, legal, and compliance restrictions governing how code and data are handled.

And that is why [Cursor](https://cursor.com/) is now letting companies run its [cloud agents](https://cursor.com/docs/cloud-agent) inside their own infrastructure. The coding platform, last [valued at $29.3 billion](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) following a $2.3 billion funding round in November, says this allows its agents to run code, tests, and development tasks locally while keeping source code and build data within a company’s own environment.

“Self-hosted agents offer all the benefits of cloud agents with tighter security control: your codebase, tool execution, and build artifacts never leave your environment,” Cursor engineer [Katia Baza](https://www.linkedin.com/in/katiabazzi/) writes in a [blog post](https://cursor.com/blog/self-hosted-cloud-agents). “For teams with complex development environments, self-hosted agents have access to your caches, dependencies, and network endpoints – just like an engineer or service account would.”

## **Bringing agents closer to the code**

Cursor [is an AI code editor](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/) developed by [Anysphere](https://anysphere.inc/), a startup founded by students out of Massachusetts Institute of Technology (MIT) in 2022. Its core product centers on autonomous coding agents that can handle long-running software tasks, including writing code, running tests, and preparing changes for review.

Those agents are designed to work with a high degree of autonomy. To do that, they need a full development environment to operate in. Cursor’s cloud agents handle this by spinning up isolated virtual machines, where they clone a repository, install dependencies, make changes, and run tests as part of a given task.

However, this depends on running those environments on Cursor’s own infrastructure, effectively bringing the code to the agent. Self-hosting reverses that, bringing those same agents closer to where a company’s code and systems already sit.

They can interact directly with internal services, dependencies, and network-restricted resources as part of a task. This removes the need to route those interactions through external systems or expose internal infrastructure, while Cursor continues to coordinate how the agents operate.

## In high demand

Requests to self-host Cursor’s cloud agents [have been](https://forum.cursor.com/t/running-agents-in-company-managed-cloud-environments/150016) surfacing among users [for months](https://forum.cursor.com/t/self-hosted-cloud-agents/151880). In forum threads and [community discussions](https://www.reddit.com/r/cursor/comments/1psie9e/can_you_self_host_cloud_agents/), developers have asked about running these agents inside their own environments, often to avoid exposing code externally or to connect more easily to internal systems.

Some of those discussions also highlight the limits of what “self-hosting” can mean in this context. Running the core agent logic locally is one thing; managing orchestration, lifecycle, and user interfaces is another. Cursor’s cloud agents bundle those components together, making a fully independent setup difficult.

Still, Cursor’s update addresses at least part of that gap. Many companies, particularly in regulated industries, are restricted from sharing source code or build environments with third-party services. Even when technically possible, internal policies can limit what tools are allowed to access.

Self-hosting doesn’t remove every challenge. Companies still need to deploy and manage the infrastructure these agents run on, and the agents’ planning and coordination still take place in Cursor’s cloud, with only execution handled locally.

While the clearest use case is for companies that need to keep code and systems inside their own networks, Cursor is also tapping into a growing appetite for running coding agents locally on individual machines, something reflected in the [recent hype around projects such as OpenClaw](https://thenewstack.io/openclaw-github-stars-security/).

Cursor, in fact, makes this use case explicit in its [official documentation](https://cursor.com/docs/cloud-agent/self-hosted):

> > “Run Cursor anywhere — spin up a worker on your laptop, a devbox, or a remote VM. You get a Cloud Agent that uses your local environment, your dependencies, and your network access.”

So, in effect, Cursor is giving users greater flexibility to run its agents across different environments, expanding where the product can be deployed — and removing a key barrier to adoption.

Cursor says self-hosted cloud agents currently support up to 10 workers per user and 50 per team, with larger company-wide deployments available on request. Self-hosted agents can be enabled through the Cursor dashboard, once a worker is set up in the target environment.

![Choosing "self-hosted" in the Cursor dashboard](https://cdn.thenewstack.io/media/2026/03/9e1115c8-self-hosted-og-image.png)

***Choosing “self-hosted” in the Cursor dashboard***

## Frontier territory

Cursor’s move toward self-hosted agents sits within a broader effort to make its tools usable in environments that have so far been difficult to reach.

The company has been expanding its agentic capabilities, including [“always-on” agents](https://thenewstack.io/cursor-agents-developer-workflows/) that can handle code reviews, bug triage, and other routine tasks across a codebase. It has also [open-sourced security-focused agent templates](https://thenewstack.io/cursor-open-sources-security-agents/), which allow teams to define how agents interact with sensitive code and systems.

These moves come as competition intensifies from both standalone coding tools and the major model providers — including OpenAI, Anthropic, and Google — which are building their own agent systems on top of models they develop and control.

That dynamic helps explain why Cursor is also moving to control more of its own stack. That includes [Composer 2](https://cursor.com/blog/composer-2), a recently released model designed to [handle longer coding tasks at lower cost](https://thenewstack.io/cursors-composer-2-beats-opus/). It reduces reliance on third-party frontier models, but it has [drawn scrutiny after Cursor acknowledged](https://venturebeat.com/technology/cursors-composer-2-was-secretly-built-on-a-chinese-ai-model-and-it-exposes-a) it is built on top of Moonshot AI’s Kimi K2.5 (a Chinese open-weights model) that wasn’t disclosed at launch.

So for Cursor, the challenge, perhaps, lies in both differentiating its product and removing barriers that limit how and where it can be used. The company says its broader platform is currently used by more than two-thirds of the Fortune 500, while the likes of Notion and Brex are already early adopters of its self-hosted cloud agents, suggesting demand among teams with more complex infrastructure and security requirements.

“Self-hosted cloud agents are a meaningful step toward making coding agents enterprise ready,” [Ben Kraft](https://www.benkraft.org/about/), a software engineer at Notion, writes in the blog post. “In large codebases like Notion’s, running agent workloads in our own cloud environment allows agents to access more tools more securely and saves our team from needing to maintain multiple stacks.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)