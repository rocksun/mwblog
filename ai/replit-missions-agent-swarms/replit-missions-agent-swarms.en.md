![Illustration depicting a swarm of agents.](https://cdn.thenewstack.io/media/2026/11/2530ee0a-getty-images-0gfedlukaji-unsplash-1024x683.jpg)

Agent swarms are all the rage, as companies set about finding ways to coordinate multiple AI agents to tackle complex tasks in parallel.

In the past week alone, [Google and Cursor unveiled](https://thenewstack.io/cursor-google-multiplayer-swarm/) competing approaches to multi-agent coding, building on existing efforts from companies including Anthropic, whose [experimental Claude Code Agent Teams](https://code.claude.com/docs/en/agent-teams) feature lets multiple agents collaborate on development tasks. OpenAI has also explored [shared workspaces for agents](https://thenewstack.io/openai-shared-workspace-agents/).

On Tuesday, Replit revealed that it’s tapping deeper into the trend with [Missions](https://replit.com/missions), a new product that lets users set objectives, establish budgets and approval requirements, and deploy swarms of AI agents to pursue them over hours, days, or even weeks.

## How Replit Missions works

At its core, Missions is a way to delegate complex projects to AI agents, leaving them to determine how best to achieve a specified goal. Users establish the parameters through what Replit calls a Mission Agreement, which sets out success criteria, spending limits and actions requiring human approval.

To get started, users can type `/mission` in a conversation and describe their objective in plain English, such as getting every page on a website to load in under 500 milliseconds.

![Starting a Mission](https://cdn.thenewstack.io/media/2026/11/9a01b3db-gif4.gif)

*Starting a Mission*

Crucially, users aren’t expected to devise a detailed plan upfront, giving agents the freedom to determine how best to approach a problem and adapt their methods as work progresses.

Replit president [Michele Catasta](https://www.linkedin.com/in/pirroh/) says this is a very deliberate design choice, as requiring users to map out every step in advance could constrain the agents’ ability to find effective solutions.

> “That would force the human to worry about implementation details, and not afford the flexibility the AI system might need to accomplish complex objectives.”

“That would force the human to worry about implementation details, and not afford the flexibility the AI system might need to accomplish complex objectives,” Catasta tells *The New Stack*.

A separate AI agent then evaluates the work against the agreed success criteria, sending it back for revisions if necessary before the user reviews the results.

![Missions dashboard and setup interface](https://cdn.thenewstack.io/media/2026/11/2b62ce61-missions-dash-1024x668.png)

*Missions dashboard and setup interface*

The concept has parallels with other multi-agent tools, including Factory, which launched its own product [called Missions earlier this year](https://factory.com/news/missions). Catasta argues that Replit’s approach differs in how it establishes user intent upfront, alongside the controls and infrastructure available to its agents.

For example, each agent operates in its own isolated cloud environment, with access to development tools, integrations and infrastructure such as databases, authentication and deployment.

Moreover, users must set a spending limit before a mission begins. Replit checks spending against that budget at every step, blocking further use of paid services once the limit is reached. Catasta argues that such controls are particularly important when multiple agents are operating autonomously.

> “Most autonomous or multi-agent products lead to runaway token costs.”

“Most autonomous or multi-agent products lead to runaway token costs,” Catasta says.

## Missions accomplished

Ahead of the launch, Replit says it used Missions to build Radar, its own application monitoring platform. According to the company, agents developed the system with direction from Replit engineers, completing it in two days with a $3,000 budget and producing dashboards, alerts and application tracing capabilities.

Replit then deliberately introduced a database fault to test the system, with Radar identifying the problem and raising an alert in 38 seconds, beating a 60-second target. In a separate three-hour test, the company says, it processed 26 million activity records and 4.4 million log entries without losing data.

![Radar application monitoring dashboard](https://cdn.thenewstack.io/media/2026/11/37e5e756-radar-application-dashboard-view-1024x640.png)

*Radar application monitoring dashboard (supplied by Replit)*

While Radar was developed for Replit’s own use, the company eventually plans to release it to the public under an open-source license, following further reliability improvements and a code audit.

Additionally, Replit has tested Missions on software optimization, reporting speedups of up to 19 times across selected workloads in [NumPy](https://numpy.org/), the widely used open-source Python library for numerical computing, using 32-agent swarms.

![NumPy performance comparison chart](https://cdn.thenewstack.io/media/2026/11/2243869b-numpy-workload-speedups-achieved-by-a-single-agent-a-16-agent-swarm-and-a-32-agent-swarm-using-auto-max-and-auto-power-1024x576.jpeg)

*NumPy performance comparison chart (supplied by Replit)*

Another internal example involved deploying 32 agents to improve [Replit Slides](https://replit.com/slides), the company’s AI-powered presentation creation tool, with workers assigned different aspects of visual design and storytelling.

The company envisages broader applications, too, including researching potential enterprise customers, preparing tailored demonstrations, and refining sales outreach.

![Replit Slides agent swarm interface](https://cdn.thenewstack.io/media/2026/11/08541ec1-figure-shows-agent-swarms-working-on-improving-replit-slides-1024x596.jpeg)

*Replit Slides agent swarm interface (supplied by Replit)*

## Keeping the swarm in check

While having multiple agents working in parallel sounds great in theory, it might raise concerns around the potential for duplicated work, conflicting code changes, spiralling costs, and the sheer difficulty of keeping autonomous systems under control.

To prevent agents from interfering with one another’s code, Replit draws on some of its existing technology, [such as parallel Tasks](https://docs.replit.com/learn/build-in-parallel). Its sandbox infrastructure allows agents to work on separate copies of a project before merging their changes, while a dedicated AI agent handles conflicts when those changes overlap. The same system, originally developed for collaboration between human developers, now supports agent swarms.

Moreover, improvements in the underlying AI models have also made this kind of coordination easier to execute.

“We’ve found that frontier models have gotten progressively better at splitting up work, and collaborating in parallel,” Catasta says. “Swarms have only started to be useful over the last few months as this behavior has been post-trained into the models.”

![Agent swarm coordination](https://cdn.thenewstack.io/media/2026/11/67805bb7-gif2.gif)

*Agent swarm coordination*

The appeal of this approach, ultimately, is that different agents can tackle different parts of a complex problem simultaneously, potentially completing work much faster than a single agent working sequentially. Catasta points to [OpenAI’s recent work](https://openai.com/index/navier-stokes-solution/) on the [Navier–Stokes](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness) Millennium Prize Problem, a longstanding mathematical challenge involving equations that describe fluid motion. OpenAI reported using approximately 10,000 coordinated agents to develop a proposed solution.

Catasta suggests that tackling such a problem could take centuries of human effort or years for a single agent, compared with weeks for a coordinated swarm. Those timelines are speculative, but they illustrate a broader argument for running many agents simultaneously.

“That’s because you can pack more compute and reasoning into a smaller amount of time by working in parallel in isolated environments, so long as you can have agents collaborate efficiently,” Catasta explains.

Replit also sees value in assigning different responsibilities to individual agents, much as a company brings together employees with different areas of expertise.

“This allows agents to focus their context on a particular part of the problem, rather than trying to make a single Agent manage context about many different subproblems simultaneously,” Catasta continues.

Of course, some tasks have inherent time constraints that additional workers cannot overcome — you can put ten cooks in a kitchen, but an egg still takes the same amount of time to boil. The same principle applies when a project has too few independent tasks to keep a large swarm occupied.

> “There is a point of diminishing returns, both for time speedups and the benefit of specialization — you don’t want 500 agents making a 5 slide deck.”

“There is a point of diminishing returns, both for time speedups and the benefit of specialization — you don’t want 500 agents making a 5 slide deck,” Catasta says.

As such, the appropriate swarm size varies according to the complexity and nature of the assignment. “Replit is tuned to suggest an appropriate number of Agents for each job,” Catasta says.

There are also questions about how reliably autonomous agents respect the restrictions placed on them. In July 2025, a Replit coding agent [deleted](https://www.theregister.com/software/2025/07/21/vibe-coding-service-replit-deleted-production-database/719783) a customer’s production database despite instructions restricting its actions, prompting concerns about the risks of delegating consequential operations to AI.

Catasta maintains that incident “is still misunderstood,” noting that the affected Replit-managed database could be restored through the platform’s recovery tools. He says the company has since introduced more explicit controls governing which integrations agents can access and which actions require permission, with restrictions enforced at the infrastructure level.

“Anything not allowed is hard blocked by our proxy service,” Catasta says. “Replit is uniquely positioned to handle configurable agent security settings and isolate risk exposure by being in the cloud and being so mature within the enterprise.”

The post [Replit’s agent swarms built an app monitoring platform in 2 days on a $3K budget. Now, it’s offering them to customers.](https://thenewstack.io/replit-missions-agent-swarms/) appeared first on [The New Stack](https://thenewstack.io).