**Nvidia has reportedly agreed to buy Hugging Face** for $12.9 billion, putting one of the biggest names in AI hardware in charge of a platform developers rely on to find and run open models.

[*The Information*](https://www.theinformation.com/articles/nvidia-agrees-buy-open-source-model-repository-hugging-face-12-9-billion) first reported the deal Wednesday, citing a person familiar with the agreement. Nvidia and Hugging Face had not publicly confirmed it as of publication.

Hugging Face doesn’t push developers toward one chipmaker, which is what makes the acquisition interesting. Its Optimum libraries work with Nvidia’s TensorRT-LLM and also support hardware from AMD, Intel, and AWS. Projects such as Optimum AMD and Optimum Intel let developers run Transformers and Diffusers models on non-Nvidia hardware.

The company also plays a role in what happens after a developer chooses a model, including how easily they can get it running on the hardware they want to use. The problem for Nvidia might be this: It is buying a platform whose value depends on openness and hardware neutrality, but if the purchase means Nvidia hardware is favored, that value might diminish.

> The company also plays a role in what happens after a developer chooses a model, including how easily they can get it running on the hardware they want to use.

## Hugging Face already sits between the model and the chip

Hugging Face has expanded well beyond file hosting. With Inference Endpoints, developers can deploy a model from the Hub while Hugging Face handles the underlying infrastructure.

Those hosted deployments can run on AWS, Microsoft Azure or Google Cloud, but most of the GPU options Hugging Face lists are Nvidia chips, including the T4, L4 and A100. That gives developers a wider choice of hardware through Hugging Face’s open-source libraries than through its hosted services.

If the deal goes through, Nvidia would own both sides of that experience.

## Deployment defaults favor Nvidia

NIM (Nvidia Inference Microservices) already works with models hosted on Hugging Face. Developers can point NIM to an hf:// repository path and pull the model directly from the Hub.

Owning Hugging Face would give Nvidia more room to bring NIM and CUDA-optimized containers directly into the deployment experience. Nvidia hasn’t announced plans to make NIM the default, and support for AMD and Intel could remain exactly where it is.

> Owning Hugging Face would give Nvidia more room to bring NIM and CUDA-optimized containers directly into the deployment experience.

The bigger question is what happens over time. Nvidia could provide earlier support for new models on its own hardware or make deployment easier. At the same time, AMD, Intel, and AWS may have to reconsider how much engineering work they want to contribute to integrations maintained within a competitor-owned platform. Some of that work could eventually move elsewhere.

For developers, the difference may come down to which path requires less work. A competing chip doesn’t have to disappear from Hugging Face to become less appealing if an Nvidia model deployment takes fewer steps. We’ve seen a similar fight over the layers between AI models and the developers using them, with [Cloudflare building more of that infrastructure itself](https://thenewstack.io/cloudflare-ai-web-economics/).

## Open models counter custom chips

That tension also helps explain why Hugging Face could be worth considerably more to Nvidia than its revenue alone would suggest.

Nvidia has been expanding its own Nemotron family of open models while investing heavily across the AI ecosystem. At the same time, some of its biggest customers are working to reduce their dependence on Nvidia hardware.

Google has its TPUs, AWS has Trainium, and Microsoft has Maia. OpenAI and Anthropic are also developing their own AI server chips. The push extends beyond the hyperscalers. Earlier this month, [five European companies committed to purchasing AI compute built around non-Nvidia hardware that hasn’t been manufactured yet](https://thenewstack.io/mistral-third-party-open-models/) — a sign that the appetite for alternative accelerators is strong enough to attract forward contracts.

OpenAI this week published results from its new Jalapeño accelerator, which [showed 1.5 to 1.9 times more work per watt while cutting end-to-end latency by up to 3.6 times](https://thenewstack.io/openai-jalapeno-inference-chip/) on large open-weight models — although the chip has not yet been deployed at anything approaching Nvidia’s scale. A strong open-model ecosystem gives Nvidia a counterweight to that trend.

Open models are often expected to run in very different environments, and Hugging Face helps developers make that possible. A model found on the Hub might end up running on Nvidia hardware, an AMD GPU, or a cloud accelerator.

That flexibility is part of what Nvidia would be buying. Pushing Hugging Face too heavily toward its own hardware could make the platform less useful to developers who rely on it to work across different systems.

Interest in those models is also growing. Models from companies including DeepSeek, Moonshot AI and Z.ai have narrowed the gap with proprietary systems. At the same time, Hugging Face CEO Clément Delangue told *The Information* in June that the company had doubled its number of paying subscribers during the first six months of 2026. Delangue later said the company was “close to profitability.”

*The Information* puts Hugging Face’s annualized revenue at about $150 million. Against a $12.9 billion price tag, that’s a multiple of roughly 86.

So Nvidia would be paying for much more than Hugging Face’s current business. It would be buying a place developers already turn to when they want to work with open models, including models that don’t have to run on Nvidia hardware.

> It would be buying a place developers already turn to when they want to work with open models, including models that don’t have to run on Nvidia hardware.

Buying Hugging Face wouldn’t give Nvidia control over everything developers find there. Libraries such as transformers and diffusers are open source, and models on the Hub remain subject to their own licenses. Openly licensed models can still be hosted elsewhere, while the underlying libraries can be forked.

Much harder to recreate is the community Hugging Face has built around them. Developers already know where to look for models and have built workflows around the Hub and its integrations.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)