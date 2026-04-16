OpenAI [announced](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) a major update to its [Agents SDK](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/) on Wednesday, one that takes the model-agnostic SDK from being a relatively bare-bones, unopinionated way to build agents and turns it into a fully-fledged toolbox for moving agents into production.

When the original SDK launched just over a year ago, OpenAI made a bet that models would get better at having a trajectory, planning, and staying on task for a reasonable amount of time.

As OpenAI’s [Steve Coffey](https://www.linkedin.com/in/stevendcoffey/), who is the tech lead for the company’s Responses API, tells *The New Stack*, the original SDK was essentially built for chatbot use cases.

> “Now we have models that can kind of work for hours at a time or days or weeks.”

“The models that were out at the time, you could expect them to take five, six, seven steps maybe in a workflow, but not really go beyond that. And now we have models that can kind of work for hours at a time or days or weeks,” he says.

Over the past year, OpenAI added a number of features to the SDK, including support for MCP, Temporal’s tools for durable execution, and other third-party tools and services. But as Coffey notes, it remained a pre-1.0 product — and that’s still the case today (“We plan to evolve it a bit further,” Coffey says.)

## Sanboxes for agents

The marquee feature of this launch is that developers can now give their agents controlled workspaces in which to operate. The core idea here is to separate the agent harness from the compute to ensure security and durability, while also enabling these systems to scale when needed.

> The marquee feature of this launch is that developers can now give their agents controlled workspaces in which to operate.

Those sandboxes can be virtually any kind of container or virtual machine. Developers can bring their own container infrastructure or use tools from Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, and Vercel to create a sandbox for their agents. Agents can use a single sandbox or start up additional ones when needed — or start up sub-agents that run in their own sandboxed environments, too.

Because of this, the SDK could run as a Temporal job, Coffey explains, and the agent would then run in a Model sandbox or Docker container. “And then these things are very separated from each other. So tool calls run in an unprivileged environment, and all the code that Modal writes runs in a privileged environment,” he notes.

## Separating the harness from compute

As Coffey notes, the team wanted to ensure that businesses could use their existing infrastructure to run these workspaces.

There is a security aspect to this as well, especially for large enterprises. As Coffey notes, an individual developer working on a one-off task may not worry too much about security, but “on the other end of the spectrum are these big enterprise deployments, where you care a ton about the agent running in a totally de-approved environment.

“So no API keys, no secrets in that sandbox. You want it to be totally isolated — probably isolated from the network in a lot of cases and not able to do any sort of egress.”

![](https://cdn.thenewstack.io/media/2026/04/48a70f8a-codex-harness-compute-1024x563.png)

*Credit: OpenAI.*

Inside this sandbox, the sandbox agent, which is now quite a bit more opinionated than its predecessors, can use the shell and the file system to work with text files, images, or PDFs, for example. Developers, of course, can also define which other tools the agent can work with.

Those agents need access to data, too. Developers can mount local files, AWS S3 buckets, Google Cloud Storage, Azure Blob Storage, and Cloudflare R2. This also allows the sandbox to be somewhat stateful.

“If you want to be able to snapshot a container and spin down that container and then spin it back up later with the same file system, we’re adding support for that,” Coffey says.

Even without using the sandboxes, agents built on the Agent SDK now have configurable memory and support for files and documents, though it seems OpenAI expects most production systems to use sandboxed environments.

Like before, there is no additional pricing for the Agents SDK. Users pay for the tokens and tool use they consume through the API, based on OpenAI’s [standard pricing](https://openai.com/api/pricing/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)