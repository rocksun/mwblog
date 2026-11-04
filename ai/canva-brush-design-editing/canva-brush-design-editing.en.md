Australian graphic design software company [Canva](https://www.canva.com/en_gb/) took the wraps off [Canva Brush](https://www.canva.com/newsroom/news/canva-brush/) last week, its new vision-language model for designers. Brush is an editing model rather than an image generator: [a vision-language model](https://thenewstack.io/a-developers-guide-to-vision-language-models/) that understands the intent behind a designer’s project and interprets design change requests.

Available to Canva Pro users, Canva says Brush reads a design’s content and structure, writes and executes small pieces of code to make changes, then checks its own result. Canva Brush arrived a week after Canva’s first in-house image-generation model, [Canva Craft](https://www.canva.com/newsroom/news/canva-craft/), which launched on October 22.

## Design is complex; design editing is even more complex

According to a Canva launch blog, generating high-quality designs is one of the biggest challenges for AI models, but “editing them is even more complex” today. This is because the model needs to understand what a designer wants to change, how the design is structured, and importantly, what needs to stay exactly as it is. Otherwise, a simple edit request can result in a “whole bunch of changes” nobody asked for.

In a prompt such as, “Make me a 3-page pitch deck for my bakery with Art Nouveau visuals and backgrounds,” an agent has to make a long chain of decisions. It needs to plan a narrative across pages, generate and place text, select imagery, and keep typography, color, and spacing consistent from the first page to the last. Each decision connects to the next, and small missteps can add up to a design that’s off-brand or feels out of kilter.

“That’s exactly the challenge we’ve built Brush to solve. Rather than treating design as a series of isolated decisions, Brush can continually evaluate and improve its work, helping [users] take an idea from a rough sketch to a polished design that’s ready to share. Behind the scenes, it uses an agentic loop that writes and runs code to adjust design elements, and can then inspect what’s happening on the page to guide its next step,” stated Canva.

> “Bounded problems – for well-defined, specific tasks – are where small specialized models have been quietly beating large general ones for years.”

## This is not a frontier lab challenge; it’s smarter than that

The question then is: can an art- and design-focused AI model lab from down under Australia challenge the frontier model behemoths on complex image design editing tasks over the long term?

Enterprise AI architect & founder of [Besk Tech](https://besk.tech/), [Vladimir Beskorovainyi](https://www.linkedin.com/in/vladimirbesk/), tells *The New Stack* that this question is “posed in the wrong frame” both metaphorically and literally.

“Canva is not challenging frontier models; it is in fact declining to compete with them,” Beskorovainyi says. “A model that reads how a design is assembled (and edits it) is solving a bounded problem (one with well-defined specific tasks with clear parameters and limited scope), and bounded problems are where small specialized models have been quietly beating large general ones for years.”

Urging us to look beyond the capabilities of the Canva Brush model and focus more directly on the cost per edit, Beskorovainyi thinks that “[the moat here](https://en.wikipedia.org/wiki/Economic_moat) is the artifact, not the weights”, primarily, Canva can train on how real designs are actually put together.

“A frontier lab can match the base processing capability of a tool like Canva Brush; the training signal is the harder thing to match, because it comes from holding the designs,” asserts Beskorovainyi. “Verticalization wins wherever the data is a by-product of the product rather than something you have to go and buy. That is the part most model developers still underestimate.”

## Design expertise, plus anonymized insights

Brush started by drawing from an unspecified open-weights model, which Canva then post-trained on real design and editing tasks, using a combination of design expertise and anonymized insights from people who opted in to help improve Canva AI. As a result, it understands not only what a finished result looks like, but also the steps needed to get there.

“We combined post-training with large-scale reinforcement learning, giving the model opportunities to work through complete design and editing tasks, learn from what worked, and continually shape its future behavior,” the company notes in its announcement.

> “A beautiful edit can still be an expensive proofreading assignment.”

Sensitive to designers’ real-world needs as they’re urged to put down their Rotring pens and Pantone color guides and adopt agentically driven toolsets, many in the marcoms industry have opinions on these new services.

Founder of [Dr. Rissy’s](https://www.drrissyswriting.com/) Writing & Marketing, [Dr. Morissa Schwartz](https://www.linkedin.com/in/morissaschwartz/), tells *The New Stack* that she has used many automation tools over the years, hasn’t yet used Canva Brush, but knows what she would do if she did.

“Here is the marketing and publishing test I would put it through. An AI design editor earns its keep when a ‘change this headline’ command still leaves the price, disclaimer, and layout intact,” Schwartz explains. “Canva’s opportunity is to make those small, frequent revisions dependable enough that a marketing team spends less time checking what else moved.”

She notes that she would further test Brush against a general-purpose model on the same approved design and measure unintended changes, legibility and time to human approval, rather than image-generation rankings.

“A beautiful edit can still be an expensive proofreading assignment,” adds Schwartz.

> “Frontier models know the Internet; Canva knows what hundreds of millions of people actually do with a slide deck. In a vertical, taste and distribution beat parameter count.”

## Canva is “out-niching” the frontier labs

Co-founder and CTO of deep-tech venture studio [The Capital Index](https://thecapitalindex.com/), [Rodion Sorokin](https://www.linkedin.com/in/rodion-sorokin-1a4bb2178/), tells *The New Stack* that he agrees with the sentiment expressed thus far and says “Canva isn’t trying to out-muscle the frontier labs; it’s out-niching them” in real terms.

“Brush started from an open-weights model and was trained with reinforcement learning against what Canva’s own designers call *good design*, a playbook any well-funded vertical player can now copy,” Sorokin says. “Frontier models know the Internet; Canva knows what hundreds of millions of people actually do with a slide deck. In a vertical, taste and distribution beat parameter count.”

“The clever bit is that Brush doesn’t paint pixels: it reads the layers, writes small pieces of code to change them and checks its own work, which is how a designer edits, not how an image generator guesses. Canva says that makes it up to 69% faster than its previous design agent at 46% lower cost per task. If that holds up outside a launch blog, specialized models will win on unit economics, not just quality: generation becomes the commodity, and editing becomes the business,” adds Sorokin.

## AI model benchmarking platform ranking

According to Canva, Craft (not Brush) debuted as the fourth-ranked model on crowdsourced benchmarking platform [Design Arena](https://www.designarena.ai/leaderboard?tab=image), behind OpenAI’s precision-focused image generation and editing model [GPT Image 2.5 Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst), the speed-focused image generation model [GPT Image 2.5 Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare), and [GPT Image 2](https://developers.openai.com/api/docs/models/gpt-image-2). Canva Research’s in-house 160-person AI lab developed both Canva Craft and the new Canva Brush models. Canva’s speed and cost figures for Brush are self-reported and compare it with the company’s previous design agent, not with frontier models.

Canva has stated that everything Canva Brush creates is fully editable. Every element, from the text and imagery to the colors, layouts, and finer details, remains available for designers to edit, manipulate, and rearrange however they like.

The organization also confirmed that this release represents the first version of Brush, and “there’s plenty more to come,” as the company is already working on the ability to reference attachments, improvements to how Brush handles image-heavy layouts, and Brand Kit support in the future.

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=canva-brush-design-editing)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)