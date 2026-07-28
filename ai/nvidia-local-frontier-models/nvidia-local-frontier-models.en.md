The models small enough to run on the box on your desk are getting good enough that the interesting question is no longer whether you can run them, but what you can do with them, and how organizations can get the most out of them.

[Joey Conway](https://blogs.nvidia.com/blog/author/joeyconway/), Nvidia’s senior director of generative AI software, spoke to *The New Stack* about how local and open models are increasingly working alongside frontier models, often with a [router](https://thenewstack.io/cursor-ramp-meta-model-router/) in between deciding which one to use, and how organizations can adapt these open models for their own needs.

> “We love the world where we can use both frontier and open models together.” — Joey Conway, Nvidia

## A system of models

Tasks vary in complexity, so the models handling them should vary too, Conway tells *The New Stack*. He points to the early open reasoning models, which would reason their way through trivial problems, mulling number lines and memory to work out what two plus two is. “I just say four,” he says.

“Being able to route those easy things to local models that are quick, and route the hard things to more sophisticated models,” Conway says, lets you “get a better outcome at a lower cost and lower time to completion.”

It’s a different picture from the one large model most people imagine doing everything. In his version, you build a bench of specialists. “You’ll have specialized agents that are really good at focused tasks because that’s what they do every day,” he says, “and they just get better and better at that task.”

To the user, none of that shows. “It’ll feel like one interface,” Conway says, “but behind that interface, there’ll be a variety of models handling a variety of tasks.”

Getting there is largely a routing problem, and one Conway says is still in its early days. Nvidia’s own contribution, for now, sits lower in the stack, in inference-serving software like its open-source Dynamo, which steers each query to the GPU that handled it most recently. Which model is best for which job, Nvidia leaves to a wider field of routers, some of them models in their own right that weigh budget, latency, and modality. But Conway also leaves the door open for Nvidia to build more of that routing itself before long.

Nvidia points to its collaboration with LangChain, whose Deep Agents harness ran on [Nemotron 3 Ultra](https://thenewstack.io/nvidias-best-model-is-now-live/), Nvidia’s 550-billion-parameter open model, and matched top closed models on business tasks at [up to a 10x lower cost](https://thenewstack.io/open-weight-models-frontier-costs/), as Conway notes. It required no retraining; the gains came entirely from tuning the harness around it: its prompts, tool descriptions, and middleware.

You’re not going to run a 550-billion-parameter model on your desktop anytime soon, but running relatively large models locally is now a real possibility, as long as you have some beefy hardware at your disposal. For enterprises, setting up a fleet of accelerators in a data center isn’t exactly cheap either, but it does mean full control and no surprise token bills.

## Bringing AI to where the data lives

Running models yourself can save money, but Conway thinks control matters more. Enterprises already decide where their data lives and what they hand to outside vendors, and open models give them even more control. “Move AI to where your data lives,” he says, “or move AI to where your employees are.”

Companies want to keep their data — and especially their intellectual property — in-house, and Conway argues a fine-tuned open model is the place to put it. “It’s like an employee,” he says. “You hire them, and they’re part of your company.”

The local half runs on hardware like Nvidia’s [DGX Spark](https://thenewstack.io/nvidia-dgx-spark-the-new-stack-developers-guide/), a $4,699 Grace Blackwell machine with 128GB of unified memory that handles models up to roughly 200 billion parameters without anything leaving your desk. (There is also the [DGX Station](https://www.nvidia.com/en-us/products/workstations/dgx-station/), its bigger, pricier sibling with 748 GB of RAM for running even larger models.)

“It’s like a system sitting right there next to you,” Conway says, one where “you don’t think about network latencies.” To run those agents securely, Nvidia offers [NemoClaw](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/), a reference stack that wraps an open agent harness like [OpenClaw](https://thenewstack.io/openclaw-hermes-agent-harness/) in a sandbox called OpenShell, with policy controls and local Nemotron inference.

When you need more power for a broader problem, you reach for a frontier model in the cloud. For Nvidia, that’s all good news: a system of models runs on its silicon one way or another, on your desk or in the cloud.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)