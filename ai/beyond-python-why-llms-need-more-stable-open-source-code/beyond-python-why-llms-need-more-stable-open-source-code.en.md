In the future dreams of Large Language Models, there will be no need for human intervention and they will write code in a highly efficient form unreadable to us. Perhaps they will write directly in binary. But for now, we need our LLM assistants to write readable code, in an established programming language.

So what languages do LLMs prefer to use today? In terms of the programming language most popular with human developers, where we assume models get their training material from, the choices should be between JavaScript/TypeScript, Java and Python. But in fact, we don’t quite see that.

## The Current Python Bias in LLM Code Generation

What we see right now is a massive Python bias, as an [academic study](https://arxiv.org/html/2503.17181v1) points out. The conclusion is straightforward: “Our findings demonstrate that LLMs exhibit a strong bias towards Python, preferring it for both benchmark tasks and project initialisation tasks, even when there are more suitable choices.”

However, the same study makes a more important claim: “LLMs display a limited range when choosing coding libraries, favouring well-established options over high-quality alternatives.” Python is getting more popular, but one suspects that the LLM creators have favoured Python training sets.

This is not particularly worrying. In many cases LLM tools start working on legacy code, where a language has already been chosen. Or the language chosen is part of the identity of the main library or platform that isn’t available in Python.

But the study also found that when a Chain of Thought prompting is used for GPT-4o (e.g. “*think step by step”)*, the programming language used for project initialisation tasks has much less of a Python preference:

[![](https://cdn.thenewstack.io/media/2026/01/4df64806-image.png)](https://cdn.thenewstack.io/media/2026/01/4df64806-image.png)

[Chain of Thought](https://arxiv.org/html/2503.17181v1)

(The languages used are given, with the percentage of responses that used the language, and the rank assigned to the language by the LLM.)

But as LLM use grows within industry professionals, one assumes that Javascript and Java will assert themselves.

## The Growing Influence of Open Source Models

The better question is: what languages *should* an LLM choose? The answer to this will probably be guided by two things; the increase in open source models, and the growing influence of open source components.

I asked [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/), CEO of [Warp](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/) (the excellent terminal tool), what AI technology Warp is likely to exploit most in 2026? He made it clear that it was open source models. “As they continue improving, we’ll use them alongside proprietary options — giving us more optionality and resilience,” he said. “Competition at this layer is also great for the developer ecosystem because it drives quality up and prices down.”

Open source models have no corporate projects to favour. So you might expect OpenAI to gently push Microsoft’s C#, and maybe Gemini will have greater access to Golang. But open source models will just tend to train with the code legitimately available to the developers.

## Why Maintainability Matters in AI-Generated Code

The strongest signal from the ‘survival of the fittest’ tools will simply be the need for generated code to be less ‘vibey’ and more maintainable. This means a preference away from currently popular languages and frameworks, towards those with proven pedigree and more trusted examples.

For instance, we can see the prominence of Web Components for the same reason. Web components are a [standard](https://thenewstack.io/web-components-are-the-comeback-nobody-saw-coming/) that is finally achieving mass appeal. Yes, they have always [offered encapsulation, reusability and framework independence](https://thenewstack.io/the-pros-and-cons-of-web-components-via-lit-and-shoelace/), but only recently have some of the rough edges been smoothed off.

Engineers, especially senior ones, read and review more code than they write; and that is likely to increase with more LLM generated code. So cool new patterns are actually a friction if used too often.

## Reducing Nondeterminism in LLM Computing

The other reason to stick to tried and trusted code is to reduce the [nondeterministic nature](https://thenewstack.io/martin-fowler-on-preparing-for-ais-nondeterministic-computing/) of LLM computing — that is, their tendency to choose different options depending on what day it is. While the [temperature](https://thenewstack.io/what-temperature-means-in-natural-language-processing-and-ai/) for tools like coding assistants will always be set low, the nature of LLM token-by-token generation is that they don’t know what they will write until they are done generating.

The fuzzy ‘mind’ of an LLM may produce one answer at one point, and another entirely different answer another time. The answers it builds at any one time rely on [statistical reasoning,](https://thenewstack.io/how-to-generate-ai-from-a-database-bruce-momjian/) but these use sets of probabilities, not the binary methods we usually associate with computing.

So for these reasons, I can see training biases moving towards more stable projects, more open projects, and projects with a longer history of openly available examples. As LLMs move towards commoditisation, or to the right of a [Wardley Diagram](https://thenewstack.io/wardley-mapping-and-strategy-for-software-developers/), stability will become the dominant factor.

## The Case for a ‘Seed Bank’ for Code

We are told that all the world’s vital plants appear in seed banks, so that we can repopulate after a disaster. A seed bank is a repository that stores seeds from diverse plant species (wild and cultivated) under suitably stable conditions. So it is a “Noah’s Ark,” but for plants. I’m writing this within sight of Kew Gardens, which manages the [Millennium Seed Bank](https://www.kew.org/wakehurst/whats-at-wakehurst/millennium-seed-bank).

[![](https://cdn.thenewstack.io/media/2026/01/aaf427a6-image-1-1024x576.png)](https://cdn.thenewstack.io/media/2026/01/aaf427a6-image-1-1024x576.png)

Millennium Seed Bank; image via Kew Gardens.

Every time we say “training data,” we wave loosely at the forums and pages available on the internet. This is why we have to assume that training is based on what is on the internet right now. What we really need is a seed bank for code. This should be straightforward for a trusted organization to set up, so that a growing set of examples can be maintained without the risk of vendor taint or third-party poisoning. While the averaging of vast quantities of internet text will provide a solid average, clearly, a tighter set would be a better place for a new model to start training from.

We don’t like to talk about the internet suffering severe damage, as that might imply some catastrophic event. And we know the military design in its heritage makes this unlikely. What we really mean is that there should exist some “other” place, where we know a safe pool of data exists so that training isn’t always dependent on the current — and very dynamic — state of the web.

## The Future of Programming for LLMs

We are still near the start of the LLM journey; and right now they will use the code and projects that appear most often in their training data when generating greenfield example code. For now, that means the plusher bits of the internet with an added Python bias.

The next step will be to use code from projects that are least likely to alter over time, in order to beat down the nondeterminism of LLMs. We are probably on the edges of that now.

Only in the far future will AIs communicate with one another and develop their own intermediate language, in which human accessibility is not a priority.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)