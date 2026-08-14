Nvidia on Tuesday launched Nemotron 3.5 Lightning, the newest member of its Nemotron 3 family of open models. In addition, the company also launched NeMo Switchyard, a new open-source library that can power model routers.

Nemotron 3.5 Lightning is a 30-billion-parameter mixture-of-experts model that was developed with contributions from the Nemotron coalition and that has reasoning capabilities that come close to the much larger Nemotron 3 Super model. Both Nvidia models, however, do trail the similarly sized Gemma 4 31B from Google on Artificial Analysis’ Intelligence Index.

![](https://cdn.thenewstack.io/media/2026/08/78b8abe3-artificial-analysis-intelligence-index-chart-1-nvidia-nemotron-3.5-lightning-1024x576.png)

Credit: Nvidia.

## Built for speed

But the focus here, Nvidia argues, isn’t on the benchmarks so much as on speed and the ability to easily customize the model. As with similar small models, the core use case is for a frontier model to plan and orchestrate the work, and for the smaller — and potentially fine-tuned — model to handle execution.

As Nvidia Senior Director Joey Conway told *The New Stack* recently, the company believes that it’s these [systems of models](https://www.youtube.com/watch?v=F96DvTrijdI) that are the future of AI, after all.

As for speed, Nvidia argues that 3.5 Lightning can deliver up to 4x faster output speeds but as Nvidia’s Kari Briski noted during a press briefing ahead of the announcement, it’s the ability to modify and optimize the model for specific workflows that Nvidia hopes will set it apart from the competition.

![](https://cdn.thenewstack.io/media/2026/08/914bf7c9-announcing-nvidia-nemotron-3.5-lightning-1024x576.png)

Credit: Nvidia.

## Post-training for specialized tasks

“General agentic benchmarks are just the starting point, but in production, what matters is accuracy on your task — and that’s where post-training makes the biggest difference,” she says. “We gave customers early access to Lightning to customize it for specialized workflows. Post-training significantly improved accuracy. Lightning outperformed the open or proprietary models partners use today.”

Working with partners like CrowdStrike, CodeRabbit, and others, Nvidia found that a fine-tuned open model like 3.5 Lightning could perform as well (and sometimes better) and larger proprietary models when working on a specialized task it was post-trained on.

And since enterprises are becoming hyper-aware of the cost of running frontier models, that’s when open models are able to shine, even as the work to post-train them isn’t always trivial.

![](https://cdn.thenewstack.io/media/2026/08/259da000-customization-chart-nvidia-nemotron-3.5-lightning-1024x576.png)

Credit: Nvidia.

Nvidia, however, argues that its NeMo ecosystem offers all of the tools necessary to make that easier and, in an additional launch today, the company is making a [full dataset for agentic reinforcement learning to train coding agents](https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Terminal-Pivot-v1-nano35-release) available as well.

At the core of any system of models is a router that decides which model to use for which task. The actual routing itself is pretty straightforward, but it’s the decision-making that is complicated. With NeMo Switchyard, Nvidia is now offering a new open-source routing library that existing routers and AI gateways like Kong, OpenRouter, and LiteLLM are building into their offerings already.

“We work with the ecosystem,” Briski says. “We are an ecosystem lover, and we want to make sure that we are integrated. Our libraries are integrated into tools that developers already use.”

Switchyard itself is written in Rust, but since developers interact with it through APIs, it’s meant to slot into existing stacks without much extra work. Developers define their own pool of models and then set the routing criteria and policies — with algorithms they can tune for quality, latency, and cost, depending on what a given workflow needs.

In Nvidia’s internal benchmarks, a Switchyard-routed system that mixed a few open models with Anthropic’s Opus 4.8 maintained frontier-level accuracy while cutting task-completion costs to roughly a third of running Opus alone.

Early partner numbers show similar results. LangChain saw 74% lower costs across 145 multi-turn Deep Agents tasks by routing only 7% of calls to a frontier model (though at a 6% accuracy tradeoff), and Ramp says it matched a frontier model’s performance on its internal SWE-Bench while cutting costs by 58% and runtime by 33%.

Nemotron 3.5 Lightning is now available on Hugging Face, ModelScope, OpenRouter, and build.nvidia.com as an Nvidia NIM microservice. NeMo Switchyard is available on GitHub, with more partner integrations coming soon.

If Nvidia is right and agents do become ensembles of many models, then the router becomes the layer where the cost and quality decisions actually get made — and Nvidia clearly hopes that its open, easily customized models will be the ones those routers pick for the high-volume work.


[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)