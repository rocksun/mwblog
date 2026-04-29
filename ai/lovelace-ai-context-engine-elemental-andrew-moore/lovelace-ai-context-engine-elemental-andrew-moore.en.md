[Andrew Moore](https://www.linkedin.com/in/andrew-moore-016b751/) has spent two decades watching [enterprise AI projects](https://thenewstack.io/turning-ai-experiments-into-enterprise-impact-lessons-learned/) fail the tests that mattered most. Not the demos. Not the chatbots. The hard ones — the investigative questions that require joining millions of dots across petabytes of data in environments where a wrong answer can cost a fortune, a freedom, or a life.

Now Moore, the former head of Google Cloud AI, former dean of [Carnegie Mellon University’s School of Computer Science](https://www.cs.cmu.edu/), and the first [AI advisor to US CENTCOM](https://press.lovelace.ai/articles/us-centcom-hires-dr-andrew-moore-one-of-worlds-leading-experts-on-ai-ml), is coming out of stealth with [Lovelace AI](https://press.lovelace.ai/about) and its flagship product [Elemental](https://press.lovelace.ai/), an [enterprise context engine](https://www.tabnine.com/blog/introducing-the-tabnine-enterprise-context-engine/) builder designed to fix what he says is the core reason high-stakes AI deployments keep failing.

“Throughout my career, I’ve been driven by a simple question: how can we use advanced intelligence to help people make the right decision when the cost of being wrong is catastrophic?” Moore said in the company’s launch statement. “AI has extraordinary potential in investigative contexts – but only if it unambiguously helps humans make better decisions.”

## The problem with investigative questions

Moore said he draws a sharp distinction between what large language models do well and where they consistently fall short. Summarization tasks, conversational queries, and basic research all work. But what he calls “investigative questions” are a different animal entirely, he says.

“A person responsible for loans at a large bank might want to ask, ‘Is there any reason that the news today means I’ve got to be worried that some of the collateral on the loans I’ve agreed to is looking flaky?'” Moore said in a briefing with *The New Stack*. “To answer that, your [large language model](https://thenewstack.io/llm/) is having to look at and touch millions of pieces of information.”

This same problem shows up in national security contexts, he said in the briefing. Moore described a customs inspector trying to determine, from thousands of ships entering port weekly, which ones most likely conceal weapons or human trafficking violations — a question that requires aggregating and cross-referencing enormous volumes of behavioral, cargo, and ownership data in near real time.

Current LLMs choke on this class of question, Moore argues, because they are forced to search a massive wall of data inefficiently, burning tokens and time without the structured context needed to reason reliably. Standard [retrieval-augmented generation, or RAG](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/), helps but only goes so far, he says.

“RAG is very effective, but for many investigative questions, you really need information aggregated and searched over millions of source documents,” Moore told *The New Stack*. “That’s the difference: RAG lets us do hundreds; a multi-terabyte context engine lets us do millions.”

## What Elemental does

Elemental sits between the agent and the data, pre-computing and caching billions of facts — Moore’s largest current deployment holds 55 million entities and over two billion facts — into what he calls a context engine: a structured knowledge graph held hot in memory, ready to travel with an investigative query through each step of its reasoning.

“As the reasoning happens, Elemental has created this treasure trove of information being carried around with the investigative query as it goes through the steps of reasoning,” Moore said in written responses following the initial briefing. “That treasure trove of information is the context engine.”

The result, Moore claims, is that agents using Elemental require roughly one-thousandth the tokens of leading models like GPT and Gemini on complex investigative tasks — a 1000x reduction that translates directly into economics. Customers can run a thousand parallel investigations for the cost of one on a standard large model, he said. Lovelace also claims over 99.5% entity accuracy and a median query latency of 20 seconds, with a 99th percentile ceiling of 60 seconds even on queries touching millions of source facts.

Elemental’s public launch also introduces [YottaGraph](https://github.com/Lovelace-AI), Lovelace’s proprietary knowledge graph projected to scale to a trillion interconnected facts by the end of Q2. YottaGraph enables enterprises to enrich internal data with real-time global intelligence — satellite transponder data, news feeds, intelligence reports, legal documents, legacy structured databases — unified into a single entity space.

Moreover, the hallucination problem, Moore argues, is addressed architecturally.

“Our context engines address this directly by doing as little work as possible in the brilliant but black box embedding space of language models, and as much of it as possible in the direct entities-and-linkages model of the context engine,” he said in written responses.

Every inference the system makes comes with citations pointing to source material, a non-negotiable design requirement Moore says is driven by the regulatory and legal environments his customers operate in. “The final answer generated is checked against all source facts before being presented to the user,” he said.

## The fishing boats

Moore offered a concrete illustration of the system working as designed. Elemental was monitoring for unusual maritime activity when it detected about 200 boats launching from a specific location over a few hours — the kind of sudden bloom that would normally trigger an alert.

“At first, when the context engine saw this, it was ready to page that there was a big problem,” Moore said in written responses. “However, because it also has access to news in its double-checking, it realized that today was the start of fishing season in the region, and corroboration with behavior the previous year showed that this is a standard event — and so although worth commenting on, it is not something to wake people up in the middle of the night.”

It is the kind of contextual correction — obvious to a human expert, historically invisible to an AI system without sufficient grounding — that Moore says defines the difference between AI that helps and AI that creates new problems.

## Huge shift

“Holy crap that’s cool,” [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at the Futurum Group, told *The New Stack* after hearing about Lovelace. “Seriously, this move mirrors a huge shift going on right now in how companies bring data and AI agents. In a nutshell, what Lovelace is promising is a collapse of what has been a very convoluted and messy approach to building context pipelines, pipelines that were not consistent, not scalable, and often just wrong. Instead, Lovelace is offering what you might call structured relationship maps, otherwise known as knowledge graphs.”

Working alongside the semantic layer, these graphs are becoming rather important with companies like Microsoft and Google pushing in this same direction, even going as far as to do automatic data enrichment, he explained. When data lands in Google Cloud Storage, for example, Google can automatically identify entities and build a graph of how they interrelate, effectively merging meaning and context into a single entity.

“What makes Lovelace’s new offering interesting is how it neatly packages the typically messy plumbing of data ingestion and entity mapping into one automated pipeline,” Shimmin told *The New Stack*. “For data leaders deploying AI in areas where a wrong guess is costly, the takeaway is very straightforward: it is time to look past basic search databases and explore automated, citation-backed knowledge structures, because even the most eager AI agent needs a solid foundation of facts to do its job well.

## The market and the competition

Lovelace is not alone in pursuing cited, verifiable AI output. [Perplexity](https://www.perplexity.ai/), [Google NotebookLM](https://notebooklm.google/), and a growing field of enterprise search vendors make similar claims. Moore’s answer is scale. “It’s one thing to verify when you’re dealing with hundreds of documents,” he said in written responses. “It’s a completely different thing when you have billions of facts. You have to design data lineage into the core infrastructure to operate on that scale.”

Moore estimates Lovelace is six months ahead of the competition on technology and 18 months ahead on the harder-to-replicate “knowhow” — the organizational and regulatory experience of actually deploying AI in safety-critical environments. The company has been conducting experiments with government customers for 18 months and with financial institutions for six months, all under NDA, he said.

At 25 engineers and launched in 2023, Lovelace is smaller than the scale of its ambitions might suggest. Moore is unbothered. “Most of our development work is done by teams of thousands of agents,” he said in the briefing.

Moore was a delight to interview, and he went just as deep in his written responses to follow-up questions.

## The ethics question

Moore’s safety-critical framing is genuine on a technical level. Elemental is built for air-gapped, on-premises deployments with no data exfiltration, full lineage on every inference, and verification against source facts before any answer reaches a user. The system is designed to meet the evidentiary standards of regulated industries.

But Moore’s position on the limits of that work is less defined. Asked directly whether Lovelace has categories of work it will not take on regardless of technical safeguards — a question prompted by the [current Pentagon leadership’s approach to AI oversight](https://thenewstack.io/pentagon-anthropic-model-orchestration/) — Moore said: “Everything we do has to abide by the laws of the countries we operate in. We are absolutely willing and able to work in any safety-critical industry.”

That answer sets a legal floor, not an ethical one. It contrasts with AI vendors like [Anthropic](https://www.anthropic.com/news/statement-department-of-war), [which publishes explicit prohibited use policies](https://thenewstack.io/perplexity-computer-vibe-coding-openai-anthropic-pentagon/) and has spoken publicly about existential risk as a constraint on deployment decisions. For Moore, the guardrail appears to be process — rigorous engineering, verified lineage, human decision-makers retaining accountability — rather than prohibition.

He also said an AI needs to follow the same evidentiary standards as a military officer justifying a targeting decision.

Moore’s origin story makes the national security focus explicit. “My role at Carnegie Mellon meant that I did a great deal of government work where I was shaken by the potential for bad actors, including rogue states, to use artificial intelligence maliciously against the West,” he said in written responses. His CENTCOM advisory role underscores where he sees the most urgent application for what Lovelace has built.

The company named itself after [Ada Lovelace](https://thenewstack.io/2025-the-year-of-the-return-of-the-ada-programming-language/) — the world’s first computer programmer and, Moore notes, a “serious [probabilist](https://en.wikipedia.org/wiki/List_of_mathematical_probabilists)” who spent considerable energy thinking about how to rationally combine uncertain evidence. She also tried to make a living gambling on it. “I call that,” Moore said in written responses, “putting your money where your mouth is.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)