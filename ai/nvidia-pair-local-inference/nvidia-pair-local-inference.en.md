Nvidia’s bet on open models and local AI has been taking shape for a while now. Its [acquisition of Hugging Face](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/) will only accelerate that, but on the product level, too, the company is making some headway in getting more potential users to run AI models on their machines.

On Thursday, Nvidia [launched](https://blogs.nvidia.com/local-ai%E2%80%93ifa-next-gen-agents-nv-pair-rtx-spark) the [Nvidia Personal AI Router (PAIR), an open-source](https://www.nvidia.com/en-us/ai-on-rtx/personal-ai-router/) software router for your home network that lets you use idle Macs and PCs in your house to run small models on demand and speed up agentic workflows with the help of subagents.

PAIR is very much meant to speed up agents like NemoClaw, OpenClaw or Hermes by allowing them to use more subagents in parallel. The idea is for a lead agent to split up tasks across subagents, whose model requests can then run on these idle machines.

![](https://cdn.thenewstack.io/media/2026/09/7d121da0-pair-demo.gif)

Credit: Nvidia.

Nvidia calls it a “virtual inference router” and is very clear that this is not a new inference engine. Instead, it uses the Ollama or LM Studio installs already running on a given machine and lets them run the models. Once installed on every machine, PAIR can then discover the different systems on your local network (using mDNS) and check if they are able to run a request.

The caveat here is that this does not split up a single inference request across different machines. Nvidia stresses that this doesn’t merge GPUs or pool VRAM into a single accelerator and can’t split a single inference request across machines.

“Agents can send a request through the familiar local interface it expects,” Nvidia explains. “PAIR receives the request through its proxy, identifies its engine and model requirements, and selects one eligible node. That node executes the request from start to finish and sends the response back through PAIR. The agent continues to see one connection while PAIR handles placement behind it.”

![](https://cdn.thenewstack.io/media/2026/09/aebeca77-screenshot-2026-09-03-at-7.56.11-am-1024x587.png)

Credit: Nvidia.

PAIR supports Windows, macOS, and Linux machines with compatible GPUs. In practical terms, that’s Nvidia GeForce RTX 20 series GPUs and newer (which Nvidia says is the baseline), a Mac with M4 silicon or newer, or an Nvidia DGX Spark (and then, once they are available later this year, RTX Spark PCs and laptops).

It’s nice to see Nvidia supporting Macs here, which have obviously become quite popular for running local models and agents like OpenClaw, even though they don’t use Nvidia GPUs.

Each system can host different models, but PAIR will only route a request to a machine with the required engine enabled and the exact requested model available. Installing the same model on several machines gives the router more options for distributing concurrent requests.

![](https://cdn.thenewstack.io/media/2026/09/f960beda-screenshot-2026-09-03-at-8.17.23-am-1024x578.png)

Credit: Nvidia.

PAIR keeps an eye on which computers are available and once a user gets back to work (or gaming) on a given machine and reclaims the GPU, the local inference engine is stopped.

In Nvidia’s example, using PAIR with two PCs running high-end RTX 5090 GPUs with 32 GB of RAM (and a $5,000 price tag right now, despite their initial $2,000 MSRP) and the Qwen3.6 35B A3B model sped up work with five subagents by about 1.6x.

Few people have a bunch of RTX 5090 cards at home (and maybe a few DGX Spark desktops, too), so it remains to be seen what this will look like in a scenario with maybe a Mac Studio, a few Mac minis and maybe a gaming PC, but even that should speed up a local agent workflow as well.

## Availability

Nvidia PAIR is now available as a beta. To get started, you just need to install it on every machine you want to be part of the network, have it discover and pair those systems, and make sure you have Ollama or LM Studio installed on them (and the models downloaded).

PAIR can also help with setup by installing Ollama or LM Studio and initiating model downloads on paired machines.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)