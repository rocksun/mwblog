# Top 5 AI Engineering Trends of 2024
![Featued image for: Top 5 AI Engineering Trends of 2024](https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1-1024x576.png)
[This time last year](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/), I wrote that AI engineering in 2023 was defined by a proliferation of LLMs and an expansion of AI dev tooling. In 2024, those trends continued — but also the market for both LLMs and AI development tools matured considerably. This year, AI got integrated into the core tools of developers (IDEs), while new techniques for creating “AI agents” arose in secondary tools like LangChain and LlamaIndex. The types of LLMs available also became more varied, with smaller models and local development capabilities of particular interest to developers.
Let’s take a deeper look at five key AI engineering trends that emerged this year.

## 1. Agentic Systems
If “prompting” was the word of the year in AI development last year, then “agentic” was this year’s buzzy word. An AI agent is an automated piece of software that uses large language models (LLMs) for various tasks, and this year [everyone was building an agent](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) and/or an “agentic system.”

At the AI Engineer World’s Fair, held in San Francisco in late June, two leading AI engineering startups — LangChain and LlamaIndex — each offered their own vision for agentic systems.

LangChain had released LangGraph earlier in the year, which its CEO, Harrison Chase, described as “purpose-built for agents” and designed to be “highly controllable and low level.”

One of the criticisms of early AI agents, such as [AutoGPT in 2023](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/), was that they tried to do too much without human involvement. In 2024, Chase was keen to emphasize that humans are very much still “in the loop” in its vision for AI agents. LangGraph “comes with a built-in persistence layer,” he said, “which enables a lot of really cool ‘human in the loop’ interaction patterns.”

Meanwhile, in a separate presentation at the World’s Fair, LlamaIndex creator Jerry Liu pitched agents as the natural successor to RAG (Retrieval-Augmented Generation), the most common method of integrating a pretrained LLM with an external data source. LlamaIndex calls its AI agents “knowledge assistants,” perhaps to make them more enterprise-friendly.

A new feature of LlamaIndex this year was Llama Agents, which Liu pitched as “a production-grade knowledge assistant — especially, you know, as the world gets more agentic over time.”

Also worth noting, in October [Meta released the “Llama Stack”](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/) to help developers build “agentic apps” with its Llama models. “The Llama Stack is a set of reference APIs for every component piece of a modern LLM system that’s deployed,” said Meta’s chief product officer, Chris Cox. “It’s also a bunch of libraries with PyTorch and other development environments to help you get started right away.”

## 2. AI Coding Tools
If AI agents still feel a little early in their evolution, then AI-assisted coding is now commonplace among developers. According to the latest [Stack Overflow survey](https://survey.stackoverflow.co/2024/ai#sentiment-and-usage-ai-select), 76% of all developers either use AI or intend to use it. In [the latest JetBrains developer survey](https://blog.jetbrains.com/team/2024/12/11/the-state-of-developer-ecosystem-2024-unveiling-current-developer-trends-the-unstoppable-rise-of-ai-adoption-leading-languages-and-impact-on-developer-experience/), users overwhelmingly said that saving time and doing things faster are the top benefits of using AI tools for development. On the other hand, only 23% said that using AI tools for coding actually improves the quality of the code and solutions being created. So there is still a question about the quality of code that AI produces.

There’s no doubt, though, that developers are finding many uses for these AI tools. A developer-writer for The New Stack, Jon Udell, wrote a series of posts this year explaining how he uses various LLMs as a “[team of assistants](https://thenewstack.io/lets-talk-conversational-software-development/)” that help him complete and/or explain coding tasks. He also found some game-changing use cases for AI, such as [creating software diagrams](https://thenewstack.io/how-to-create-software-diagrams-with-chatgpt-and-claude/).

Another trend is that developers no longer need special tooling to use AI — it’s often integrated right into their IDE, making AI just a normal part of their development flow. Earlier this year, our resident engineer-writer, David Eastman, tested the AI functionality in JetBrains’ range of IDEs. [He concluded](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/):

“To some degree, the ‘Hey! Look! We have AI’ is a current business necessity for IDEs as the environment expands and while agreed expectations are still forming. By next year, much of this will exist as part of the IDE experience, just as Cut and Paste does today.”

Eastman also conducted reviews of two other trending AI coding tools, [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) and [Zed AI](https://thenewstack.io/an-introduction-to-zed-ai-and-how-it-compares-to-cursor-ai/). He was impressed by both, commenting, “most likely, in less than a year and with a more demonstrative add / remove / replace mechanism, both Cursor and Zed will become exemplars of code flow using AI.”

In October, I looked at yet another [new AI coding tool, Solver](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/). It claims to be a paradigm shift in AI-assisted coding, because it allows developers to hand off tasks for AI to build autonomously. The company says it’s a clear step up from mere “AI autocomplete tools” like GitHub Copilot, Cursor and Devin.

Finally, in addition to straight coding tools, there are increasing options for choosing and deploying LLMs. For example, in August, GitHub [launched GitHub Models](https://thenewstack.io/github-models-review-of-microsofts-new-ai-engineer-platform/) — making it easy for developers to consume the latest generative AI models.

## 3. AI Engineer as a Career
Last year the job title “AI engineer” was just ramping up. But this year, as more and more organizations implemented some form of AI software, AI engineers became indispensable.

As Fatih Nar and Roy Chua recently wrote in [a contributed article on The New Stack](https://thenewstack.io/ai-engineering-level-up-your-it-career/), “as AI becomes more deeply embedded in business operations, AI engineers play a pivotal role in ensuring the successful design, implementation and scaling of AI solutions in the enterprise software ecosystem.”

Nar and Chua observed that AI engineers “must be proficient in managing data pipelines, ensuring data quality and deploying data for model training.”

Our sister site Roadmap has a step by step [guide to becoming an AI Engineer](https://roadmap.sh/ai-engineer), if you’re interested in making this career move in 2025. Also check out our article outlining [five leading JavaScript tools for AI engineering](https://thenewstack.io/top-5-javascript-tools-for-ai-engineering/).

## 4. Small Models and Locally Hosted LLMs
Two LLM trends in 2024 were especially attractive to developers.

The first is the rise of small language models, or SLMs. As Kimberley Mok put it in [a February overview](https://thenewstack.io/the-rise-of-small-language-models/), “these models are slimmed-down versions of their larger cousins, and for smaller enterprises with tighter budgets, SLMs are becoming a more attractive option, because they are generally easier to train, fine-tune and deploy, and also cheaper to run.”

In February, [Google launched two smaller, open models](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/) with a permissive commercial license: Gemma 2B and Gemma 7B. Google claimed these two models out-performed Llama 2 and Mistral in that size range.

So what kinds of applications might be built with Gemini and similar SLMs? According to Tris Warkentin, director of Google DeepMind, “there are a wide variety of applications for these models.”

“In fact, if you look at usage across the ecosystem, this is the most common size that developers would like to use — the 7B size for sort of text generation and understanding applications, from an open model standpoint,” Warkentin said.

Because small language models are basically more streamlined versions of LLMs, they are usually easier to implement on your computer. Which leads us to the second LLM-related trend for devs, locally hosted AI models.

Earlier this year, The New Stack’s David Eastman looked at [how to run an open source LLM locally](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/), using Ollama and Llama 2. He found that this allowed him to run queries on private data without any security concerns. More recently, our frontend tutorial writer Alexander T. Williams gave further [tips and recommendations for both SLMs and local development](https://thenewstack.io/coding-with-slms-and-local-llms-tips-and-recommendations/). Also check out Janakiram MSV’s tutorial on how to build a RAG-based LLM application with Nvidia NIM and Milvus [running locally on a GPU-boosted machine](https://thenewstack.io/build-a-rag-app-with-nvidia-nim-and-milvus-running-locally/).

![](https://cdn.thenewstack.io/media/2024/02/0deb09f2-untitled-1024x499.png)
A GenAI testing presentation from @patrickdubois

## 5. Open Source AI
There was a lot of robust discussion this year on what is — or *isn’t* — open source when it comes to AI.

In particular, some have claimed that Meta’s LLaMA models [aren’t truly open source](https://thenewstack.io/metas-llama-2-is-not-open-source-and-thats-ok/), because of limited access to training data and other issues — such as the licensing terms encouraging development within Meta’s ecosystem (rather than allowing unrestricted use and modification, as is typical of open source software). Meta also imposes commercial restrictions on LLaMA model use.

As Mark Collier, chief operating officer at the Open Infrastructure Foundation, put it in [an April post](https://thenewstack.io/open-source-has-a-definition-lets-get-serious-about-defending-it/), “Meta’s custom license, by restricting usage and the ability to create derivative works, violates multiple tenets of both the current definition of open source and any final work of the OSI community that’s specific to AI.”

To try and clarify the situation, in October the Open Source Initiative (OSI) published Release Candidate 1 of [its long-awaited definition for open source AI](https://thenewstack.io/osi-finalizes-a-humble-first-definition-of-open-source-ai/). As TNS editor Heather Joslyn noted, the OSI document recommends organizations using the term ‘open source’ for their AI systems to “share the data (if shareable), along with the source code used to train and run the system, and the model’s parameters.”

## Conclusion
In 2024, we’ve observed the maturing of AI software (especially AI coding tools for developers), a push toward more automation (AI agents), the emergence of small models and locally hosted LLMs, and some clarification on what is or isn’t open source (although that debate will continue into the new year).

This year also proved that being an AI engineer is a viable career option — especially if you want to dive even deeper into AI than tools like GitHub Copilot or Cursor allow.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)