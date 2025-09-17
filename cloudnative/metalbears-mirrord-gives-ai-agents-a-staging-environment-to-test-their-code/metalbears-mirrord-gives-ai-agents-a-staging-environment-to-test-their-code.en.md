[Mirrord](https://metalbear.com/mirrord/) has long been a very popular tool for developers who want to test their Kubernetes-based application against a full-blown staging environment instead of a local simulacra of their company’s tech stack.

Instead of setting up a local environment, mirrord let’s developer code directly against the staging environment by having the tool intercept all of the local processes and re-route them directly to the staging cluster. This means developers can stay in the flow without having to go through packing up the code on a container and switching context to continuous integration platforms, for example.

With the rise of AI coding agents, there is now more code to be tested, and there’s also more of a need for the agents themselves to gain access to these staging environments.

Increasingly, testing is becoming the bottleneck, and unless developers want to rely on incomplete local tests, they need to go through an ever-increasing number of deployment cycles outside of the inner development loop.

[![](https://cdn.thenewstack.io/media/2025/09/737dc215-metalbear-productphoto.png)](https://cdn.thenewstack.io/media/2025/09/737dc215-metalbear-productphoto.png)

Image credit: MetalBear.

“AI has solved everything but what mirrord does,” [Aviram Hassan](https://metalbear.com/contributors/aviram-hassan/), the CEO and co-founder of MetalBear, the startup behind mirrord, told me. “You can generate code using AI. You can test it at a sort of local level — unit testing, component testing. You can review code. But once it comes to integration testing, you don’t really have a good solution. And so that bottleneck just becomes more dominant, because there’s more code that needs to be tested using those same limited resources.”

He argues that having to go through a new deployment cycle for every loop adds too much friction and slowing down businesses at a time when rapid iteration is increasingly a competitive advantage.

“The entire industry has accepted this as normal, but it’s actually the biggest hidden bottleneck in software development today,” he said.

With mirrord — and, if needed, Metalbear’s enterprise services on top of it — developers debug their code while it is interacting with the full staging environment and the microservices, databases, message queues and third-party services that run in it.

Agentic systems can use the same environment as needed as well. As MetalBear CTO and co-founder [Eyal Bukchin](https://metalbear.com/contributors/eyal-bukchin/) told me, the team started with building an MCP server. That’s the obvious thing to do, after all, to connect AI agents and tools. But as it turns out, by using an Agent.md file or similar instructions to tell the agent that it has access to this environment is enough.

“We realized that today, you can give a Markdown file to the agents that they read before they do any action, and then in the Markdown, you write: okay, Claude, to test, this is the command you run. You can read about mirrord and what it does — but to be honest, it just knows. Finally, run your service using mirrord to test the cluster,” Bukchin explained.

Bukchin and Hassan described the open source version of mirrord as feature-complete, with the team mostly focusing on bug fixes at this point. It is MetalBear’s commercial offering where the team is putting most of its emphasis at this point. There, the team, which just raised a $12.5 million seed round to commercialize the service, follows the well-worn playbook for building an open-source company by adding enterprise features on top of mirrord.

These include features like being able to better manage multiple clients accessing the same staging environment, support for deploying to multiple pods, as well as the usual admin and support feature like role-based access control and monitoring and auditing logs. MetalBear’s service starts at 50/seat/month. There is also an additional enterprise plan available that adds features like support for airgapped clusters and mirrord support in CI pipelines, among other things.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)