**AWS on Thursday launched Strands Decider 2B**, its take on decision models like [Jev](https://thenewstack.io/typesafe-jev-system-one/), [Kev](https://github.com/jaredpalmer/kev), [imajev](https://huggingface.co/mohit67890/imajev-4b), [Laya](https://huggingface.co/convaiinnovations/laya), and others.

TypeSafe’s Jev kicked off the current wave of decision models a few weeks ago, and the major AI vendors are now bringing out their own versions.

OpenAI on Tuesday, for example, launched its [Decisions API](https://thenewstack.io/openai-decision-api-luna/) as a limited preview. But that’s a hosted API that focuses its Luna model on questions with predefined answers, while AWS is releasing a [downloadable model](https://github.com/strands-labs/strands-decider) along with the data and scripts used to train it.

## How Strands Decider works

Decision models trade free-form text generation for selecting from developer-supplied options or returning numerical scores. That makes them useful for routing natural language requests, selecting tools, evaluating outputs, and checking proposed actions, while leaving conversation and more complex work to generative models.

Strands Decider uses [Qwen3.5-2B](https://huggingface.co/Qwen) as its language-understanding base model, which AWS calls the “torso.” The team then removed the language-model head that generates text and replaced it with a pointer head that scores the supplied answer options.

![](https://cdn.thenewstack.io/media/2026/10/a2b83828-image-3.png)

*Credit: AWS*

That head has just over a million parameters, and the backbone uses a rank-16 [LoRA](https://arxiv.org/abs/2106.09685) (low-rank adaptation) adapter.

Restricting the answer space prevents the model from inventing an option that wasn’t supplied, but that still doesn’t mean it will always answer correctly. That’s a minor tradeoff, though, since LLMs aren’t always right either. In return, developers get faster decisions and confidence scores they can use to make decisions.

## Checking an agent before it acts

In AWS’s example, built with the company’s open-source [Strands agent framework](https://thenewstack.io/aws-launches-its-take-on-an-open-source-ai-agents-sdk/), a user asks for the weather without saying where, and the agent guesses a city and proposes calling a weather tool.

Before that tool runs, Decider checks whether the argument values are grounded in the conversation and whether the agent has enough information to proceed. The application then sends the agent back to ask which city the user meant.

The check then runs through Strands’ intervention system, which lets developers choose whether they want to proceed with a tool call, deny it, request human confirmation, or return feedback to the agent.

In this demo, Decider runs locally while the agent calls its generative model through [Amazon Bedrock](https://aws.amazon.com/bedrock/). AWS says it’s also working on decision-model integration libraries.

## Built on an open Qwen model

Like Kev, Strands Decider builds on an open Qwen model, showing how much of this experimentation now depends on open weights. Kev already supports local deployment and fine-tuning, and with the [training data and scripts](https://huggingface.co/StrandsAgents) included, AWS’s release lets developers inspect the recipe and adapt it to their own tasks.

> Like Kev, Strands Decider builds on an open Qwen model, showing how much of this experimentation now depends on open weights.

AWS says it focused on balancing accuracy, calibration, and latency. Calibration here means how closely the model’s confidence scores track how often it’s actually right.

On [JevBench](https://github.com/fstandhartinger/jevbench)‘s public set, AWS says Strands Decider ranks second among public models with roughly 2 billion parameters, and first among public models with a full training recipe available.

![](https://cdn.thenewstack.io/media/2026/10/ad1ad06a-image-2.png)

*Credit: AWS*

AWS also notes that Strands Decider 2B answers every question in JevBench’s easy tier correctly, which is the kind of routine agent decision it’s built for.

AWS reports decisions in under 100 milliseconds on an Nvidia RTX 3090, with response times going up as tasks grow. On an M3 MacBook, the median for small tasks is around 150 milliseconds, the company says.

The model AWS is releasing now is the second major iteration of the architecture. The company says an earlier head design performed significantly worse. AWS also left every earlier iteration in the [repository](https://github.com/strands-labs/strands-decider), so developers can trace how the model evolved.

![](https://cdn.thenewstack.io/media/2026/10/17940bf8-image.png)

*Credit: AWS*

Strands Decider was incubated at Strands Labs, AWS’s home for experimental approaches to agentic AI, which launched earlier this year. It also follows the company’s recent release of [Strands Harness](https://thenewstack.io/aws-strands-harness-agent/), which packages the tools and supporting machinery needed to run longer-lived agents.

## Hosted Decider?

One thing that remains to be seen is if AWS will also offer a hosted version of this model — or a future version of it — in its cloud. Hybrid scenarios are great for experiments and running on localhost, but to put an app built on this model in production, developers will want to see a hosted version as well.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)