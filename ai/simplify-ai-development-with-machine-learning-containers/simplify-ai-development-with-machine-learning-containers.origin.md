# Simplify AI Development with Machine Learning Containers
![Featued image for: Simplify AI Development with Machine Learning Containers](https://cdn.thenewstack.io/media/2025/01/0f393dc3-getty-images-0w9_dz4sjdg-unsplashb-1024x576.jpg)
Replicate has a very simple premise: run and share machine learning models in the cloud, using [containers](https://thenewstack.io/containers/) technology. Sound familiar? That may be because Replicate’s founder and CEO, [Ben Firshman](https://www.linkedin.com/in/bfirsh/), was previously the creator of Fig, which was [acquired by Docker](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/) and then became Docker Compose.

[Replicate](https://replicate.com/) is the end result of Firshman and his business partner [Andreas Jansson](https://www.linkedin.com/in/janssonandreas/) wanting to create a similar technology for [machine learning](https://thenewstack.io/how-machine-learning-works-an-overview/).
## Bringing Containers to AI
What Firshman and Jansson created first was a product called [Cog](https://cog.run/), which he [has described as](https://replicate.com/blog/machine-learning-needs-better-tools) “Docker for machine learning.” Cog, according to Firshman, “makes it easy to package a machine learning model inside a container so that you can share it and deploy it to production.” This tool was open sourced, but like many developers who open source their creations, Firshman and Jansson then created a cloud platform to commercialize the technology, called Replicate.

According to its [documentation](https://replicate.com/docs), Replicate “lets you run AI models with a cloud API, without having to understand machine learning or manage your own infrastructure.”

Cog essentially abstracts the technical aspects of deploying machine learning applications. But similar to Modal, the [severless platform for AI apps](https://thenewstack.io/serverless-for-ai-devs-modals-python-and-rust-based-platform/) that I profiled last week, Replicate mostly rents the compute needed to run these models.

“We don’t own our own GPUs,” Firshman explained [on the Latent Space podcast](https://www.latent.space/p/replicate) last year. “We’ve got a few that we play around with, but not for production workloads. And we are primarily built on public clouds, so primarily GCP and CoreWeave and, like, some smatterings elsewhere.”

## Helping Devs Tinker With LLMs
One of the keys to Replicate is that it allows developers to customize, fine-tune and tinker with open source LLM models. As Firshman noted in the podcast, “the whole point of open source is that you can tinker on it and you can customize it and you can fine-tune it and you can smush it together with another model.”

Replicate really came into its own when Meta released its [open source Llama models](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/), because of course that allows developers to tinker much more than with APIs from the likes of OpenAI and [Google](https://cloud.google.com/?utm_content=inline+mention). “The beautiful thing about Llama 2 as a base model is that… you can fine-tune it for like 50 bucks,” Firshman said. “And that’s what’s so beautiful about the open source ecosystem.”

Just this week, the open source LLM ecosystem got another shot in the arm with the sudden emergence of DeepSeek, a Chinese company that [claims to have built](https://www.theverge.com/24353060/deepseek-ai-china-nvidia-openai) a reasoning LLM (called R1) that is the equal of OpenAI’s most powerful model, the o1. This claim is still being prodded by developers and the media, but regardless it is undoubtedly good news for developers — the more open source models for its users to tinker with, the better!

“Just start playing around with it, get a feel of how language models work, get a feel of how these diffusion models work, get a feel of what fine-tuning is and how it works…”

– Ben Firshman, Replicate CEO
From a developer perspective, platforms like Replicate and Modal are a boon because they make using machine learning technology in applications viable. In the Latent Space podcast, Firshman likened it to when developers were introduced to web development platforms in the 1990s.

“You don’t need to be digging down into [the] [PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/) level, if you don’t want to — in the same way as a software engineer in the ’90s [didn’t] need to be understanding how network stacks work to be able to build a website. But you need to understand the shape of this thing.”

He urged developers to learn about modern AI, because it is becoming more and more important in the application development landscape.

“Just start playing around with it, get a feel of how language models work, get a feel of how these diffusion models work, get a feel of what fine-tuning is and how it works — because some of your job might be building datasets, you know. Get a feeling of how prompting works, because some of your job might be writing a prompt. And those are just all really important skills to sort of figure out.”

## A Plethora of AI Models
In an interview with one of his investors, A16Z, last November, [Firshman said](https://a16z.com/podcast/building-developers-tools-from-docker-to-diffusion-models/) there are around 20,000 models in the Replicate ecosystem. [These include models](https://replicate.com/explore) that generate or enhance images and videos, transcription models, models for chat or music, models that help you “make 3D stuff,” and more. By far the most popular modal, with 726.9 million “runs” as of writing, is [SDXL-Lightning](https://replicate.com/bytedance/sdxl-lightning-4step) by TikTok owners ByteDance, described as “a fast text-to-image model that makes high-quality images in 4 steps.”

Firshman also said, in an interview [with Assembly AI](https://www.assemblyai.com/assembly-required/assemblyai-replicate), that “we’re primarily building for startups.”

“And when we say startups, it’s both actual startups, but also small teams inside large companies that are kind of behaving like startups,” he clarified. “These teams are having a lot of success building, like, either whole products that are native to AI, or like particular point solutions to certain things inside the product.”

He added that some of Replicate’s customers are using it to fine-tune language models, but that this isn’t the primary use case.

## Democratizing AI: Why Open Source Models Matter
Replicate and Modal are both good examples of a new type of platform providing value to developers: one that makes it easier to integrate AI into applications by abstracting away much of the complexity of machine learning technologies.

You could also argue that Replicate is helping democratize access to open source LLM models by enabling developers to customize and/or fine-tune models such as Meta’s [Llama 3](https://thenewstack.io/llama-3-how-metas-new-open-llm-compares-to-llama-1-and-2/) (the latest Llama version) — or even experiment with cutting-edge models like DeepSeek’s R1.

While it’s still early days in this evolution — given that OpenAI and the other industry heavyweights keep their most powerful models proprietary — platforms like Replicate show how open source could yet flourish in the AI engineering ecosystem. The more models that open up and become accessible to tinkerers, the better it will be for devs.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)