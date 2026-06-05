When the conversation turns to AI infrastructure, it almost always lands on GPUs and TPUs. *The New Stack* sat down with [Bhumik Patel](http://linkedin.com/in/bhumikpatel) of Arm and [Mo Farhat](https://www.linkedin.com/in/mofarhat0/) of Google to talk about the chip that rarely makes the headlines anymore: the CPU, and why it’s getting more important, not less, as AI shifts from chatbots to agents.

VIDEO

[Farhat,](https://www.linkedin.com/in/mfarhat/) who leads product management for Axion and Arm-based virtual machines at Google Compute Engine, tells *The New Stack*, “The role, more or less, is of a CPU as an air traffic controller.”

In this episode, we discuss how the shift from conversational chatbots to autonomous agents is quietly turning into a CPU story.

## The workload shifted from answering to acting

Early chatbots returned a response, but agents can act on them. They perform tasks by calling tools and, when needed, create environments to execute the code they write. “All of these are CPU workloads,” Farhat says.

While large language models typically run on accelerators, the CPU sits next to them, doing the work that makes an agent function.

[Patel](https://www.linkedin.com/in/bhumikpatel), who drives Arm’s software ecosystem efforts for cloud and AI, walked us through what that work actually looks like. The components of an agent’s tasks “are traditionally what CPUs are good at: orchestrating, talking to APIs, and doing some memory management,” he says. And that’s the kind of concurrent, distributed work these chips were built for.

There’s a role for actually running models here, too, but we’re talking about very small ones, including summarizers, classifiers, and targeted evaluators. Farhat says CPUs are already delivering good performance for models in the 8-billion-parameter range, and he believes the workloads they can handle will continue to expand.

## Why agents need sandboxes, and lots of them

For those agents to run code, though, they need an environment that lets them do so in a secure way that doesn’t endanger any production systems.

Patel says, “These agents are executing code on your behalf, and not all code might be secure, so you need this isolation layer.”

Google’s pitch for this is gVisor, an open-source project that sits between the application and the host operating system, offered as an option in GKE Agent Sandbox, the managed environment Google offers for running agents at scale. “You don’t really have to trust the agents, you can just sandbox them,” Patel says.

GKE Agent Sandbox, Google argues, can also handle the scale necessary in this agentic era. It can start as many as 300 sandboxes per second per cluster, Farhat says, with less than a second to first instruction. Agent workloads are also spiky, since an agent calling sub-agents often sits idle waiting for responses. So the platform relies on pod snapshots and warm pools to keep those idle agents cheap, rather than paying for pods that sit idle.

## The efficiency pitch

At Google Cloud Next, Google said customers running its Arm-based Axion processors in GKE Agent Sandbox can get “30 percent better price performance than the next leading cloud provider,” Farhat says, and notes that this is an advantage that is built on the efficiency of the latest Axion chips thanks to Arm’s latest cores.

There, Google now offers Axion N4A machines optimized for cost and efficiency, which work well for sandboxes. The other SKU, C4A machines, are tuned for high single-threaded performance, which can include stateful orchestration and control-flow logic that agentic workflows depend on.

“The good news is for a lot of the cloud native developers and broad set of cloud users, these tools are very familiar, and it kind of extends to this agentic approach,” Patel added.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)