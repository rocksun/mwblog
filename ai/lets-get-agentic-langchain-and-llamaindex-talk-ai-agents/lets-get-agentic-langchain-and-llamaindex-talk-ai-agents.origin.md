# Let’s Get Agentic: LangChain and LlamaIndex Talk AI Agents
![Featued image for: Let’s Get Agentic: LangChain and LlamaIndex Talk AI Agents](https://cdn.thenewstack.io/media/2024/07/0a0a10f7-aie_agents_2024-1024x648.jpg)
The phrase “agentic systems” (or “agentic workflows”) popped up more than a few times at last week’s [AI Engineer World’s Fair](https://www.ai.engineer/worldsfair), held in San Francisco. AI agents were the focus of two leading AI engineering startups: [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) and [LlamaIndex](https://thenewstack.io/llamaindex-and-the-new-world-of-llm-orchestration-frameworks/), each of which offered their own spin on the technology in presentations.

The term “agent” in the AI landscape refers to an automated piece of software that uses large language models (LLMs) for various tasks. But [when I attended the first AI Engineer event](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/) last October, when it was known as the AI Engineer Summit, I felt that AI agents were the most hyped — and least convincing — aspect of that event. AutoGPT was the hottest agent startup at the time (and a lead sponsor of the October event), but its presentation left me highly skeptical.

## LangChain
At the World’s Fair, AutoGPT didn’t appear to be among the sponsors, but it was mentioned by Harrison Chase, the founder and CEO of LangChain. In a quickfire presentation on the topic of agents, Chase began by pouring cold water on the 2023 hype of agents.

“To me, AutoGPT represents the peak of hype in agents,” he told the World’s Fair audience. “And I actually think for a few months after that, there was a bit of a fall-off in interest as people realized that the generic agent architecture wasn’t reliable enough to build systems to ship to production.”

He mentioned [OpenAI’s Assistants API](https://platform.openai.com/docs/assistants/overview) as a turning point for agents. Then, earlier this year, LangChain released [LangGraph](https://www.langchain.com/langgraph), which Chase described as “purpose-built for agents.” He noted that LangGraph is designed to be “highly controllable and low level.”

“Companies that were shipping agents to production were building custom cognitive architectures, encoding little differences in how they wanted their agents to behave,” he explained. But this wasn’t something the “generic agent” systems could deliver.

Another criticism I had of agents back in October was that they seemed to want to take humans out of the equation — which I thought was hubristic. Chase struck a much more modest tone and even listed “human in the loop” as one of the defining features of LangGraph.

LangGraph “comes with a built-in persistence layer,” he said, “which enables a lot of really cool ‘human in the loop’ interaction patterns.”

Chase announced on-stage that it was releasing “the first stable version of LangGraph” — version 0.1 according to a graphic — which he said reaffirmed its “commitment to building an agent architecture that allows you to build the custom cognitive architectures that are necessary for bringing agents to production.”

He then circled back to the OpenAI Assistants API, which he said was a good agents platform, although it had some flaws. “It came with a specific state that it expected your application to have, a list of messages, and it was a little bit rigid and didn’t let you easily do other things besides that,” he said.

This led LangChain to develop a SaaS product for LangGraph, simply called LangGraph Cloud. It offers “1-click deployment, scalable servers and task queues, and integrated monitoring” for agents.

He added that another benefit of LangGraph Cloud is that “it’s not bound to OpenAI, and it supports any cognitive architecture that you can build with LangGraph.”

## LlamaIndex
Another approach to AI agents was offered by LlamaIndex creator Jerry Liu, in a separate presentation at the World’s Fair. He pitched agents as the natural successor to RAG ([Retrieval-Augmented Generation](https://thenewstack.io/improving-llm-output-by-combining-rag-and-fine-tuning/)), which has — up till now — been the most common method of integrating a pre-trained LLM with an external data source.

“If you’ve followed our Twitter for the past year or so, basically we’ve talked about RAG probably 75% of the time,” he said, adding that it’s become common to “not only do a one-shot querying search but actually store your conversation history over time.”

But this year, continued Lio, “a lot of people are excited about building agentic workflows that can not only synthesize information but actually perform actions and interact with a lot of services to basically get you back the thing that you need.”

LlamaIndex has wisely decided to rebrand AI agents into something less sinister-sounding for enterprises: they’re calling them “knowledge assistants.”

RAG “was just the beginning” of its goal to build knowledge assistants, said Liu. He characterized RAG as “a glorified search system on top of some retrieval methods that have been around for decades.”

Liu went on to explain a rather complex set of options for LlamaIndex users, but the overall gist was that users can build more advanced agents with techniques that go beyond RAG. Users can even build “a general multi-agent task solver,” he said, “where you extend beyond even the capabilities of a single agent towards multi-agent orchestration.”

Having seemingly coined “knowledge assistants” to make it easier for enterprises to understand the concept of AI agents, Liu then tried to explain the concept of “agentic RAG,” which rather over-complicated matters again.

“Not only are you just directly feeding the query to a vector database,” Lui said about agentic RAG, “in the end, everything is just an LLM interacting with a set of data services as tools, right?”

Erm, right.

Provided it all works, Liu said that this process results in more advanced agents — such as “personalized QA systems,” agents that can maintain user state over time, and agents that are able to look up information from both unstructured and structured data sources.

To wrap it up, Liu announced a new feature of LlamaIndex, called (you guessed it): [Llama Agents](https://www.llamaindex.ai/blog/introducing-llama-agents-a-powerful-framework-for-building-production-multi-agent-ai-systems). “We see this as a key ingredient in helping you build something that’s production-grade — a production-grade knowledge assistant — especially, you know, as the world gets more agentic over time,” said Liu.

## Agentic World
Harrison Chase had begun his presentation with an apparent diss of last year’s AI agents sensation, AutoGPT. But of course, it remains to be seen whether the solutions provided by LangChain and LlamaIndex fare any better.

LangChain’s solution has a complicated catchphrase (“custom cognitive architectures”), but seems simpler than LlamaIndex, which has a simple catchphrase (“knowledge assistants”) but a complicated workflow. But check back in a year to see if either of them works in the wild.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)