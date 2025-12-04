LAS VEGAS — Yesterday, AWS [announced Nova Forge](https://thenewstack.io/with-nova-forge-aws-makes-building-custom-ai-models-easy/), a new way for enterprises to customize [Amazon](https://aws.amazon.com/?utm_content=inline+mention)‘s family of Nova large language models (LLMs) with their own data. Today, it’s addressing a very similar need by adding model customization options to its Amazon Bedrock and SageMaker AI services.

As Swami Sivasubramanian, AWS’s VP of Agentic AI, told me in an interview ahead of today’s announcement, serverless model customization in SageMaker takes a different approach from what the company is doing with Nova Forge.

## SageMaker AI Model Customization

At its core, SageMaker had always been about building machine learning models — with foundation models only recently added to the mix — based on a company’s own data, and then helping them deploy and manage those models over their lifecycle.

“This is different from the Nova Forge, where you can actually, as an engineer who doesn’t know anything about [supervised fine-tuning], RL [Reinforcement Learning] or any of it, you can chat with the agent and say: ‘Here is my use case. Here is the data set I have. How should I customize it?’ And it will guide you through, all the way from supervised fine-tuning to RL to how to go about it. And then it’ll kickstart all of it end-to-end.”

As part of this process, the tool will even generate its own synthetic data.

For developers who want more control, there is also a second agentic experience (AWS describes this one as the “self-guided” approach). Developers get more control over every step of the process, but as AWS notes, they still won’t have to manage any of the infrastructure that runs these processes and instead get to focus on finding the right customization techniques and tweaking those.

Sivasubramanian stressed that this capability was previously only available to specialized AI scientists and out of reach for most developers.  He also noted that this is a fully serverless product — like the rest of SageMaker.

## Reinforcement Fine-Tuning on Bedrock

As for Bedrock, which is AWS’s fully-managed service for accessing foundation models from Amazon itself, Anthropic, Mistral and others, the focus is on Reinforcement Fine Tuning (RFT). As with Nova Forge, AWS argues that it remains too hard for developers to set up the training pipelines and infrastructure to effectively use this technique to tune models for their specific use cases.

Reinforcement Fine-Tuning essentially involves tuning a model to perform well on a given task by having another model grade every answer, with those answers then being incorporated into the model’s weights. As with other RL techniques, this is a reward-based system, with the grading model providing those scores and rewards.

For this service, developers can choose different reward functions — AI-based, rule-based or a ready-to-use template — and Bedrock will handle the fine-tuning process from there.

“No Ph.D. in machine learning required — only a clear sense of what good results look like for the business,” AWS notes in its press release.

AWS argues that it is seeing an average of 66% accuracy gains over base models for its customers who use this technique — all while also making the models easier and faster to run.

## Competition

It’s worth noting that AWS isn’t the first to market with many of these features. Google’s Vertex AI [offers](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-use-supervised-tuning) a model customization suite that offers quite a few reinforcement learning options. Similarly, Microsoft’s AI Foundry also [offers fine-tuning services](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/fine-tuning-considerations?view=foundry-classic).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)