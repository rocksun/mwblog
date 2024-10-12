# Llama Stack Released To Help Developers Build ‘Agentic Apps’
![Featued image for: Llama Stack Released To Help Developers Build ‘Agentic Apps’](https://cdn.thenewstack.io/media/2024/10/eb6497fd-llama-stack-feature-1024x576.jpg)
At Facebook Connect 2024, Meta’s annual developer conference, the company released [Llama 3.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/), its latest large language model. Meta says its [Llama LLMs are open source](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/), although others [don’t necessarily agree](https://thenewstack.io/why-open-source-ai-has-no-meaning/). In any case, Meta’s chief product officer [Chris Cox](https://www.linkedin.com/in/chris-cox-2896b841/) called Llama 3.2 “our most developer focused release yet” and during his [developer keynote](https://developers.facebook.com/m/meta-connect-developer-sessions/developer-keynote) presentation he explained what he meant by that.

“In the past — Llama 1, Llama 2, Llama 3 and 3.1 — we’ve been very focused on model performance, getting to the most intelligent state-of-the-art models, opening them to consumers and opening them to you,” Cox said. “For this release, we’ve been burning down the list of what we’ve heard from all of you, [what] you need to make your tools better and to take the industry to the next level.”

“The Llama Stack is a set of reference APIs for every component piece of a modern LLM system that’s deployed.”

– Chris Cox, Meta
Although the new image-generation features of Llama 3.2 were what attracted the most social media chatter during and after the event, for developers the key announcement was the final one from Cox. He explained how people had been complaining to him that using Llama models as a developer was too difficult.

“You guys are just like throwing these models over the wall, and everybody’s doing the same work, everybody’s doing batch inference, synthetic data,” he said, summarizing some of the complaints. “Everybody’s distilling the models, everybody’s doing evals. Please, just make it really simple to get started, and also make these things modular.”

To answer those criticisms, Meta is releasing a “Llama Stack” to help developers more easily start using its Llama models.

“The Llama Stack is a set of reference APIs for every component piece of a modern LLM system that’s deployed,” said Cox. “It’s also a bunch of libraries with PyTorch and other development environments to help you get started right away.”

## The Nitty Gritty
The stack includes a series of “building blocks” that developers can use to build LLM applications, which in practical terms means the following set of APIs:

- Inference
- Safety
- Memory
- Agentic System
- Evaluation
- Post Training
- Synthetic Data Generation
- Reward Scoring
Each of these APIs is a collection of REST endpoints, states Meta in [the associated GitHub repository](https://github.com/meta-llama/llama-stack). The API providers could be practically anyone — “cloud providers or dedicated inference providers could serve these APIs.”

To make it easier for developers, Meta has organized a series of “distributions,” which it states is “where APIs and Providers are assembled together to provide a consistent whole to the end application developer.” Currently, there are three distributions available on Docker: Local GPU, Local CPU, and Local TGI + Chroma.

As [Ahmad Al-Dahle](https://www.linkedin.com/in/ahmad-al-dahle-63a963a0/), who leads generative AI at Meta, [put it on X](https://x.com/Ahmad_Al_Dahle/status/1839384436703666309), “Our Llama Stack Distribution is a huge step forward in how we support developers with a single endpoint. We are now sharing with the community a simplified and consistent experience that will enable them to work with Llama models in multiple environments, including on-prem, cloud, single-node, and on-device.”

On LinkedIn, [Prashant Ratanchandani](https://www.linkedin.com/in/prashantratanchandani/), a VP of engineering for GenAI at Meta, [added his thoughts](https://www.linkedin.com/posts/prashantratanchandani_in-pursuit-of-our-goal-of-open-innovation-activity-7245551523517104128-SqmE?utm_source=share&utm_medium=member_desktop). “The Llama Stack is our attempt to define and standardize all the building blocks to bring AI applications to users. Doing this today requires developers to reason through and choose several building blocks, and the LlamaStack brings these together in one neat package — across model training and fine-tuning, to evals, and finally building and deploying the app.”

It’s also interesting to see how Meta’s corporate partners are implementing the Llama Stack. Dell, for instance, is clearly prioritizing agentic apps [in its offering](https://www.dell.com/en-us/blog/redefining-ai-integration-in-the-llama-ecosystem-with-dell-ai-solutions/). “By combining Llama Stack with Dell’s AI Factory, organizations have enterprise-grade infrastructure that makes it easy to prototype and build agent-based AI applications with Llama models,” the company claims.

## Agentic System API
Of the currently available APIs, the “agentic system” one is clearly the key, given the [excitement around AI agents](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) among the AI developer community. It also happens to be at the top of the stack — for Meta and for Dell — so it’s likely to be an API that AI engineers will want to use regularly.

When the Llama Stack was first proposed as an RFC back in July, [early commentators](https://www.youtube.com/watch?v=A0UCOek8Yc0) suggested this was Meta’s “agentic framework.” Meta itself uses the term “agentic applications” to indicate the type of apps it envisions being built using the Llama Stack.

Prior to the official release of Llama Stack, Meta [released a repo on GitHub](https://github.com/meta-llama/llama-stack-apps) that “shows examples of applications built on top of Llama Stack.” Starting with Llama 3.1, it said, you can build agentic applications capable of:

- Breaking a task down and performing multistep reasoning.
- Using tools to perform some actions:
- Built-in: the model has built-in knowledge of tools like search or code interpreter.
- Zero-shot: the model can learn to call tools using previously unseen, in-context tool definitions.
- Providing system-level safety protections using models like Llama Guard.
## Conclusion
It’s too early to determine what kinds of apps developers will want to build with the Llama Stack, but it’s another example of the standardization now happening with AI development tools. Using Llama Stack, alongside Meta’s LLMs, is an alternative to using independent AI tools like [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) or [LlamaIndex](https://thenewstack.io/a-developers-guide-to-getting-started-with-llamaindex/) and looking for a suitable LLM in [Hugging Face’s directory](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/). With Llama Stack, especially when used as a distribution, those choices all get made for you.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)