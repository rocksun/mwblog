So, is RAG (Retrieval-Augmented Generation) dead now? Last May [I asked that question](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary/) of [Douwe Kiela](https://www.linkedin.com/in/douwekiela/), CEO of Contextual AI, based on the growing hype around MCP (Model Context Protocol). Both are data retrieval mechanisms for Large Language Models, but it’s [MCP that has taken all the headlines](https://thenewstack.io/ai-engineering-trends-in-2025-agents-mcp-and-vibe-coding/) over the past year.

The truth is, RAG has fallen away as a term used by developers and AI engineers. Even Kiela, who co-authored [the 2020 academic paper](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) that introduced RAG to the world, admits that a trendy new term has taken over.

“I think people have rebranded it now as *context engineering*, which includes MCP and RAG,” he said. “I mean, the ‘R’ in RAG just stands for ‘retrieval.’ So, I think I said this last time too, if you’re using MCP to do your retrieval, then it’s basically RAG, right?”

RAG is still an integral part of Contextual AI’s stack — it’s [in their documentation](https://docs.contextual.ai/how-to-guides/platform), despite no longer rating a mention on the homepage. Regardless, Contextual AI chose the right company name if “context engineering” is the term du jour now.

## Agent Composer Launch

Like many other AI companies, [Contextual AI](https://contextual.ai/) is also now all-in on agents. This week it launched a new tool called [Agent Composer](https://contextual.ai/blog/introducing-agent-composer), which the company described in a press release as “the infrastructure and orchestration layer that manages context, enforces guardrails, and maintains agent reliability throughout multi-step engineering workflows.”

Agent Composer joins the other tools available on the Contextual AI platform, which Kiela describes as a “context layer.”

“So you have the language model, you have your data,” he explained. “And if you’re an enterprise, you have your data all over the place, and it’s very, very noisy, right? And these companies are not going to consolidate all of that data into one place, so what you can do with our platform is you can hook up all these different data sources.”

From all those data sources, users create what Contextual AI calls “data stores.” Part of what Agent Composer will do, says Kiela, is help enterprises build agents on top of their data stores.

As the diagram below shows, Agent Composer includes all the pieces an enterprise would want to create agents: pre-built templates, a prompting interface, a visual builder, APIs, and so on.

[![Contextual AI platform](https://cdn.thenewstack.io/media/2026/01/b3be3b64-contextual-agent-composer.png)](https://cdn.thenewstack.io/media/2026/01/b3be3b64-contextual-agent-composer.png)

Contextual AI platform; image via the company.

## Claude Code and Enterprise Wrappers

I noted that AI coding tools like Claude Code and Cursor have been tremendously popular in enterprises over the past year or so. Presumably, many enterprise developers are already using those tools to create custom agents, so what does Contextual AI’s Agent Composer offer that the likes of Claude Code don’t?

“I would say that those [AI coding tools], they’re essentially harnesses for language models,” Kiela replied. “So ‘harness’ is one of the buzzwords right now. So I think you can think of our platform as a way to create ‘custom harnesses.’ You can basically build your own Cursor, or you can run your own specific instance of Claude Code on our platform, so that you don’t have to worry about running things locally, or things like that.”

I think what he means is that Claude Code and Cursor are wrappers around an AI model, but they’re often tied to a developer’s computer by being a CLI tool or a desktop app. Contextual allows enterprises to create their own wrappers, but they’re hosted centrally — which comes with the security and governance benefits that enterprises typically require.

> “…you can think of our platform as a way to create ‘custom harnesses.’ You can basically build your own Cursor, or you can run your own specific instance of Claude Code on our platform.”  
> **– Douwe Kiela, CEO of Contextual AI**

Another big trend currently is agent development platforms. [LangChain](https://www.langchain.com/), perhaps [the original AI engineering tool](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/), is currently promoting its “agent engineering platform” — called LangSmith — on its homepage. I asked Kiela how Contextual AI compares to a product like LangSmith?

“I think they’re more focused on lower-level developers and what I would call more indie developers,” he replied. “So it’s really about SaaS prototyping, and they have lots of different options. I think we are much more opinionated and much more enterprise grade, so we’re really focused on enterprise developers and users of [those] solutions.”

## From Prompt Engineering to Context Engineering

Terminology changes so fast in the AI era of development. So what does “context engineering” even mean, in relation especially to AI agents? It just so happens that Anthropic, perhaps the most trendy AI development company right now, thanks to Claude Code, [wrote an explainer](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) last September.

Anthropic contends that “context engineering is the natural progression of prompt engineering.” Rather than giving a series of prompts to an LLM, as in [the old days of 2022-2023](https://thenewstack.io/generative-ai-how-companies-are-using-and-scaling-ai-models/), engineers are now encouraged to manage “the entire context state (system instructions, tools, Model Context Protocol (MCP), external data, message history, etc).”

The term “agent” itself is problematic, but most people agree that it’s a software program that runs in a loop. According to Anthropic, an agent “running in a loop generates more and more data that could be relevant for the next turn of inference, and this information must be cyclically refined.” So that’s what context engineering does.

> “…there’s always a trade-off between how much information you want to pre-process […] and how much information you want to search during query time.”  
> **– Kiela**

Specifically, Anthropic says that Claude Code takes a “just in time” approach to context engineering, meaning it will “dynamically load data into context at runtime using tools.” I asked Kiela if Contextual AI does a similar thing?

“Yeah, so, most of these solutions are just-in-time,” he said. “If you sort of zoom out, there’s always a trade-off between how much information you want to pre-process — so when you do the ingestion of documents — and how much information you want to search during query time… so, just-in-time, essentially. And so the right trade-off between those two modes of processing really depends on the problem that you’re solving. So in some cases, if you have to be blazingly fast, you probably want to do a lot more pre-processing. If you have a bit more time and you can be agentic, then maybe you don’t need to do as much of that, because you can have multiple tries and all kinds of different strategies for getting to the answer.”

## Agentic Use Cases

So what kinds of agentic solutions are Contextual AI’s customers actually implementing currently? Kiela replied that his company tends to focus on “hard engineering,” like the semiconductor industry.

“So within that, we see a lot of traction around enabling engineers to move faster by having access to all of the internal knowledge, so kind of unlocking institutional engineering knowledge,” he said.

One of their more popular use cases is doing a root cause analysis with an agent, a process described in [a November blog post](https://contextual.ai/blog/user-feedback-and-annotation).

“So that’s quite powerful,” he continued. “It’s really taking log dumps or all kinds of different data sets around something going wrong, and then you need to analyze what the root cause is. You can cross-reference that with internal documentation, maybe with existing bug reports. Maybe you want to automatically open up a PR on your code base that fixes it. So there’s a lot of interest in that.”

## Conclusion

In summary, then, RAG is not dead — it’s just been rebranded to “context engineering.”

Also, it’s clear that the practice of software engineering in the agentic era continues to evolve. Companies like Contextual AI and Anthropic provide tools for a range of developers to tweak agent loops.

Prompting? That’s so over. Now it’s about managing “the entire context state,” as Anthropic puts it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)