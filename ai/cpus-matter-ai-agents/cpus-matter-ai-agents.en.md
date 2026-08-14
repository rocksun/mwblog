When the conversation turns to AI infrastructure, it almost always lands on GPUs and TPUs. *The New Stack* sat down with [Bhumik Patel](http://linkedin.com/in/bhumikpatel) of Arm and [Mo Farhat](https://www.linkedin.com/in/mofarhat0/) of Google to talk about the chip that rarely makes the headlines anymore: the CPU, and why it’s getting more important, not less, as AI shifts from chatbots to agents.

[Farhat,](https://www.linkedin.com/in/mfarhat/) who leads product management for Axion and Arm-based virtual machines at Google Compute Engine, tells *The New Stack*, “The role, more or less, is of a CPU as an air traffic controller.”

VIDEO

In this episode, we discuss how the shift from conversational chatbots to autonomous agents is quietly turning into a CPU story.

“Today’s six- to eight-billion-parameter models are performing much better than they have in the past,” Farhat says. For some specialized workloads, he says, CPUs can deliver roughly 25 tokens per second, which can be enough for agentic workloads.

## The workload shifted from answering to acting

Early chatbots returned a response, but agents can act on them. They perform tasks by calling tools and, when needed, create environments to execute the code they write.

“The orchestration harnesses themselves for agentic workloads are these always-on branching kind of control-flow logic that CPUs are great at,” Farhat says.

While large language models typically run on accelerators, CPUs also handle orchestration, data preparation, semantic search, and vector databases, Farhat says.

[Patel](https://www.linkedin.com/in/bhumikpatel), who drives Arm’s software ecosystem efforts for cloud and AI, says the company is focused on the software and infrastructure layers needed to run these workloads at scale. Different types of agents, he notes, are doing “different type[s] of code execution and API calling and the typical CPU work.”

There’s a role for actually running models here, too, but we’re talking about very small ones, including summarizers, recommenders, and evaluators.

“Today’s six- to eight-billion-parameter models are performing much better than they have in the past,” Farhat says. For some specialized workloads, he says, CPUs can deliver roughly 25 tokens per second, which can be enough for agentic workloads.

## Why agents need sandboxes, and lots of them

For those agents to run code, though, they need an environment that lets them do so securely without endangering production systems.

“The agents are doing code execution, so you want to make sure that the LLM-generated code is trusted,” Patel says. “Or if it’s not trusted, then you kind of sandbox the environment.”

Google’s pitch for this is gVisor, an open-source project that acts as an isolation layer between the application and the host operating system. As Farhat puts it, “We operate in a zero-trust environment. This is exactly why you need the isolation technologies that agents run in.”

As Farhat puts it: “We operate in a zero-trust environment. This is exactly why you need the isolation technologies that agents run in.”

GKE Agent Sandbox, Google argues, can also handle the scale necessary in this agentic era.

“GKE Agent Sandbox will allow customers to spin up 300 sandboxes per second per cluster,” Farhat says. Patel says the platform uses pod snapshots and warm pools of suspended environments to help customers scale more quickly without keeping all of those environments fully provisioned.

## The efficiency pitch

Google says Axion can offer advantages in both cost and energy use.

“Axion today will give you up to 2x the price performance of comparable current-generation virtual machines,” Farhat says, “and we’ll do that at over 60% better energy efficiency as well.”

Google offers Axion C4A machines for consistently high performance and N4A machines for a balance of performance and cost-optimized workloads. For a compute-bound, long-running engineering job where completion time is critical, Farhat says C4A offers the needed performance. For smaller code-execution tasks where density and cost matter more, he points to N4A.

“The good thing about the options in Google Cloud is, like Mo offered earlier, you have the C4A for high-performance workloads, and then the N4A,” Patel says. “You want to scale a large number of agents, and different types of agents are doing different types of code executions and API calling and the typical CPU work. The N4A is a great fit.”

Farhat’s broader point is also that CPU, GPU, and TPU resources will continue to work together as agents scale.

“We’re in a fluid compute world,” he says. “We do recommend that customers look at all the options, CPU-based, TPU, GPU-based, and ensure that their application is built to scale going forward.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)