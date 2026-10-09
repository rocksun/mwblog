This week, OpenAI opened its Decisions API to public beta and added image inputs to make fast decisions from visual content.

First [announced](https://thenewstack.io/openai-decision-api-luna/) last week as a likely response to [TypeSafe’s Jev](https://thenewstack.io/typesafe-jev-system-one/), OpenAI is now billing its decision model at $0.10 per 1M input tokens. There are no output-token charges, nor charges for cache reads or writes.

Running on GPT-6 Luna, the public beta version gives all developers the ability to turn text or images into three types of structured outputs: predicates (i.e., how likely something is to be true), choices (i.e., which predefined option is the best fit), and scores (i.e., where an input falls on a numeric range).

But OpenAI’s Decisions API may be but one fish in a sea of decision models. Perplexity, Cloudflare, and Amazon also dropped their own versions this month, opting for open-weight models that developers can download and run on their own infrastructure.

## What Decisions API can do with image input

In a new [video](https://www.youtube.com/watch?v=FB6oCmrIj-Y&t=21s), OpenAI shows how image inputs can help applications take quick action based on visual understanding.

![](https://cdn.thenewstack.io/media/2026/10/b60c58e9-decisions-api-game-1024x574.png)

Source: [OpenAI YouTube](https://www.youtube.com/watch?v=FB6oCmrIj-Y&t=21s)

It offers the example of a video game with a car moving through traffic. Using frames of the road and obstacles, Decisions API can choose whether the car should switch lanes or keep driving.

OpenAI claims its API can make those decisions in a fraction of the time a reasoning model would take to do the same.

Zooming out, the AI company hints at what this visual understanding could enable if developers pair the API with basic computer-use tasks, like taking screenshots and quickly choosing the next action.

![](https://cdn.thenewstack.io/media/2026/10/e91abc84-decisions-api-hugging-face-robot-1024x570.png)

Source: [OpenAI YouTube](https://www.youtube.com/watch?v=FB6oCmrIj-Y&t=21s)

The same video also shows OpenAI received a preview unit of [Hugging Face’s upcoming programmable Microduck robot](https://thenewstack.io/hugging-face-microduck-robot), an open-source bipedal developer robot.

By integrating the robot with [GPT-Live](https://developers.openai.com/api/docs/models/gpt-live-1), OpenAI’s real-time voice model, and the Decisions API, OpenAI says its decision model can analyze the robot’s camera frames to make fast decisions about where it should look.

In the given example, the Decisions API responds to a request to “follow the apple” by first identifying the fruit and then directing the robot to turn toward it. OpenAI adds that the GPT-Live and Decisions API pairing can go further and respond to more ambiguous commands, like “follow the fruit.”

![](https://cdn.thenewstack.io/media/2026/10/902912a9-decisions-api-animated-character-1024x571.png)

Source: [OpenAI YouTube](https://www.youtube.com/watch?v=FB6oCmrIj-Y&t=21s)

OpenAI also promises its new API can bring more dimension to voice conversations.

It shows GPT-Live and Decisions API paired with an animated character; the former handles the voice and the latter steps in to choose which expression the character should use.

## Decision models are suddenly everywhere. How do you decide which one to use?

TypeSafe kicked up quite a storm when it released Jev last month. But its time in the spotlight seems to be coming to a quick end. In addition to OpenAI’s foray into decision models, Perplexity, Cloudflare, and Amazon have all stepped onto the scene — but they’re letting developers download the model weights and run them themselves.

> Perplexity, Cloudflare, and Amazon have all stepped onto the scene — but they’re letting developers download the model weights and run them themselves.

[Released on Hugging Face](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b) this month, Perplexity’s pplx-decider-v1-27b is an open-weight decision model fine-tuned from Qwen3.8-27B, released under Apache 2.0. Per its model card, it supports a similar decision pattern to TypeSafe and OpenAI: selecting among predefined choices and returning yes/no probabilities.

Unlike OpenAI, Perplexity showed its benchmark results, reporting its decision model beats Jev overall across 11 benchmarks at 85.71% to TypeSafe’s 84.51%. But that overall score comes from a mixed bag; Jev takes the cake on six out of 11 benchmarks, including WinoGrande, BBH, and TruthfulQA binary.

[Amazon’s local answer to Jev](https://thenewstack.io/aws-strands-decider-model/), Strands Decider 2B, is also a downloadable model — this time, built on Qwen3.5-2B. Amazon says it ranks second among public models with roughly 2 billion parameters on JevBench’s public set.

> Like OpenAI’s and Perplexity’s models, Clef has a vision encoder to accept images as well as text. Jev and Strands Decider are currently text only.

Cloudflare, meanwhile, has given developers [two decision models](https://blog.cloudflare.com/clef-decision-models), Clef and Clef-flash, both available as Apache 2.0 open weights, as well as through its own hosted Workers AI service. Like OpenAI’s and Perplexity’s models, Clef has a vision encoder to accept images as well as text. Jev and Strands Decider are currently text-only.

More consequential than image or text inputs is OpenAI’s decision to keep its model behind a hosted API, even as many contemporaries are opening up their versions so developers can download and run them themselves. As decision models become the new norm, where and how they can be deployed may become the deciding factor in which model developers let decide.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)