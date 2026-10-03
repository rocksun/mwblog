**The debate over what size, shape, and scale of model** best suits each task isn’t going away any time soon. Joining the fray now is serverless inference provider [Featherless](http://featherless.ai/). The company has released [Simple Jev](https://simple-jev.featherless.ai/), an open-source library that converts open-source AI models into high-speed, [zero-shot classification engines](https://huggingface.co/tasks/zero-shot-classification).

Building on this month’s [TypeSafe](https://typesafe.ai/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) launch of closed-source, text-only [Jev](https://thenewstack.io/typesafe-jev-system-one/), Featherless’s Simple Jev extends structured decision functionality to open-source models, with image capabilities on Featherless’s hosted endpoints. It enables applications to evaluate incoming data and return categorical assignments or binary choices without generating conversational text.

## Don’t use a tank to deliver a pizza

[Eugene Cheah](https://www.linkedin.com/in/eugene-cheah-a47791126/), CEO and co-founder of Featherless, tells *The New Stack* that using bleeding-edge frontier models to classify something like a support ticket is “like using a tank to deliver a pizza” in terms of tooling overload.

“Sure, the pizza tank gets there eventually, but it’s slow, it’s expensive, and it’s the wrong vehicle,” Cheah says. “Businesses need the fast reflexes, the instant they are called for, and that’s a different kind of AI that the industry has neglected for far too long.”

Featherless’s hosted Simple Jev endpoints also include [vision support](https://thenewstack.io/which-vision-language-models-should-you-use-for-your-apps/) for decision workflows. Currently available only with Gemma or Qwen models, this feature lets developer teams use images as context for instant classification. By bypassing conversational text, the software reduces latency and cuts compute usage.

> “The pizza tank gets there eventually, but it’s slow, it’s expensive, and it’s the wrong vehicle.”

Featherless has carefully positioned its stance on multi-modal vision support. Cheah concedes that big closed-source models can work on these tasks. Still, he insists that “it’s the wrong tool for the job”, because they get there by generating text through “enormous multi-trillion-parameter LLMs”, and developers obviously pay frontier prices for that kind of service.

“The industry has been so focused on the size of LLMs it hasn’t stepped back to think about cost and efficiency for a while. Simple Jev never ‘writes’ an answer: we stop the model right where it would choose, read its scores for each allowed option, and output the probabilities,” explains Cheah.

## What is a zero-shot classification engine?

For the uninitiated, zero-shot engines use pre-trained language models to classify inputs into unseen target categories without task-specific training data. Because a zero-shot engine classifies inputs it wasn’t explicitly trained on, it relies on transfer learning to predict categories for new inputs without prior exposure.

“But classifiers aren’t new; it’s what universities taught for AI before ChatGPT. What’s new (and credit to Jev here) is a well-designed zero-shot API for it. The core pieces were already there, and we knew them well, which is why we got it up so quickly. What was old is new again,” enthuses Cheah.

Illustrating how his team built the new tooling, Cheah thinks that “Any graduating AI/ML PhD could reimplement Simple Jev from one sentence.”

“They would implement a ‘shared-prefix, two-stage, prefill-only, logit-based classifier’ to do it. We’re open sourcing it to make it easier to replicate and more efficient, and I expect hundreds more open source Jev clones,” adds Cheah.

> “Any graduating AI/ML PhD could reimplement Simple Jev from one sentence. I expect hundreds more open source Jev clones.”

Featherless is also introducing free public endpoints, which it says will let developers test classification models without API keys or logins (the demo is capped at 2,000 tokens of context and two requests per second). For production use, Simple Jev pricing starts at $0.03 per million input tokens, with output tokens free, compared with TypeSafe’s $0.042 per million input tokens for Jev. That is a beta floor price that may rise, and Featherless’s own listings put its Qwen-based classifiers at $0.28 and $0.30 per million input tokens. So is that expensive, or as cheap as a Little Caesars pizza deal?

“It’s almost too cheap to meter in a literal sense,” details Cheah. “Let’s say a typical decision when classifying an image/paragraph of text is roughly 500 to 1,200 tokens, so at $0.03 per million you’re paying about three thousandths of a cent for a decision. To put that in perspective, that’s about $15–35 per *million* decisions. And the output is free, too.”

## **Moving on from** monolithic generalist models

Urging us to move on from what it has called “monolithic generalist models,” Featherless has offered its latest tooling, promising that millions of lightweight, dedicated models will drive the future.

***“***First they said open models would never catch up. Then they said open only wins in isolated cases. Soon they’ll be saying closed models only win in isolated cases,” adds Cheah.

As the Featherless CEO conceded, classifiers are not new. As a sub-classification of model toolset engineering, other zero-shot vision and multi-modal classification technologies have been around for a while.

## Other models that work in the zero-shot arena

First introduced in early 2021, [OpenAI’s CLIP](https://openai.com/index/clip/) might reasonably be called an early open pioneer for zero-shot image classification. The model learns visual concepts from natural language supervision and can be applied to any visual classification benchmark.

[Microsoft’s Florence-2](https://www.microsoft.com/en-us/research/publication/florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks/) arrived in summer 2024 as an open-weight vision-language foundation model. It promised to overcome the complexities of “spatial hierarchy and semantic granularity” and is said to be well-suited to zero-shot and fine-tuning tasks, including visual object detection, grounding and segmentation, and image captioning. Other contenders in the zero-shot visual tagging and object classification arena include [Roboflow](https://roboflow.com/) and [Mixpeek](https://mixpeek.com/).

**“**Everyone in this space is standing on each other’s shoulders; that’s how open source works. CLIP and the rest are great tools that changed the industry. We’re bringing an old idea back with today’s models, because sometimes you don’t need the tank; you need something small and fast,” concludes Cheah.

Simple Jev is now available as a fully open-source library on [GitHub](https://github.com/featherless-ai/simple-jev). Featherless says it offers developers a dedicated model distillation workflow (a process that transfers capabilities from large frontier models into smaller, efficient architectures) to compress complex prompts and decisions from large frontier models into smaller, highly efficient open models for production.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)