# No, MCP Hasn’t Killed RAG — in Fact, They’re Complementary
![Featued image for: No, MCP Hasn’t Killed RAG — in Fact, They’re Complementary](https://cdn.thenewstack.io/media/2025/05/160e561e-aakash-dhage-xpmgpcdqboq-unsplashb-1024x576.jpg)
Is RAG dead yet? That was the tongue-in-cheek question [posed recently](https://contextual.ai/blog/is-rag-dead-yet/) by [Douwe Kiela](https://www.linkedin.com/in/douwekiela/), CEO of Contextual AI. And Kiela knows a thing or two about RAG (Retrieval-Augmented Generation) — he led the team at Meta that introduced the technique in a [May 2020 research paper](https://arxiv.org/abs/2005.11401).

Of course, Kiela’s post was a reaction to the current hype around [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP), which has (wrongly) been touted as a [RAG](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/)-killer. But as Kiela pointed out in an interview with The New Stack, RAG can be used *with* MCP — something that his own RAG-based company, Contextual AI, does regularly.

## The Road to RAG Agents
Firstly, how did Kiela and his Meta colleagues come to invent RAG? He told me that it traces back to his PhD work on grounding language in real-world context, which later continued at Facebook AI Research. There, he and his team explored how AI models could stay aligned with an evolving ground truth — like Wikipedia — without constant retraining. With the emergence of early language models and vector databases, they combined the two: retrieval (R) from a vector database and generation (G) via a language model. This led to the RAG technique, allowing generative AI to reference external knowledge.

“And so I think it’s just a very intuitive way to make it so that GenAI — generative models — can work on top of ground-truth data without needing to be trained on it,” he said.

After RAG began gaining traction, Kiela decided to leave Meta and start his own RAG-based company in early 2023. Now, Contextual AI markets itself as “the fastest way to build accurate, scalable RAG agents.”

I asked whether the term’ RAG agents” is a recent addition, given the current hype surrounding the agents. Kiela replied that yes, the agents wording was added in 2024.

“The way our systems work, we used to call them applications before, but that sounds kind of passive, and what really makes it work in the modern paradigm is being much more active. So that’s why it’s an agent.”

## RAG Workflow Spectrum: Static to Agentic
AI agents are typically seen as autonomous [software applications](https://thenewstack.io/how-to-build-rag-applications-using-model-context-protocol) — they go out and do things on behalf of the human user. So, is a “RAG agent” also mostly autonomous?

Kiela replied that there’s a spectrum between static RAG workflows and more advanced agentic systems. A typical RAG pipeline, he said, is a kind of static agent: it plans a retrieval strategy, fetches relevant data, re-ranks results, and sends them to a grounded language model trained for RAG to generate an answer. While this is somewhat agentic — since it makes decisions about whether and how to retrieve — it’s still a fixed process.

In contrast, he continued, a fully agentic system dynamically generates executable code (like Python) at runtime, allowing it to adapt its retrieval and reasoning strategies based on intermediate results. This can include re-running searches or adjusting its approach as needed. The key innovation, according to Kiela, is not autonomy, but active reasoning at test time — what he called “test-time compute.”

“There’s a lot of fluff around it, a lot of hype,” he said, referring to agentic systems in 2025. “A lot of people are saying, ‘Oh, it has to be like it’s active and it’s taking actions, or it’s autonomous, or…but what really matters is that it reasons actively.”

I asked him to clarify what he means by “reasons actively,” to which he replied that the agent is “thinking through, what do I need to do now?”

## RAG and MCP
Just as [agentic systems](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) are all the rage this year, so is MCP. But MCP is sometimes talked about as if it’s *a replacement* for RAG. So let’s review the definitions.

In his “Is RAG dead yet?” post, Kiela defined RAG as follows:

“In simple terms, RAG extends a language model’s knowledge base by retrieving relevant information from data sources that a language model was not trained on and injecting it into the model’s context.”

As for MCP (and the middle letter stands for “context”), according to [Anthropic’s documentation](https://modelcontextprotocol.io/introduction), it “provides a standardized way to connect AI models to different data sources and tools.”

That’s the same definition, isn’t it? Not according to Kiela. In his post, he argued that MCP complements RAG and other AI tools: “MCP simplifies agent integrations with RAG systems (and other tools).”

MCP is “not as revolutionary as a lot of people make it seem.”

– Douwe Kiela, CEO of Contextual AI
In our conversation, Kiela added further (ahem) context. He explained that MCP is a communication protocol — akin to REST or SOAP for APIs — based on JSON-RPC. It enables different components, like a retriever and a generator, to speak the same language. MCP doesn’t perform retrieval itself, he noted, it’s just the channel through which components interact.

“So I would say that if you have a vector database and then you make that available through MCP, and then you let the language model use it through MCP, that is RAG,” he continued. “So it’s basically…you’re using retrieval to augment the generator. So that is RAG. It’s just that the way that those two parts talk to each other is through MCP, rather than what you do with standard RAG, which is just put it in the context […] more directly.”

Kiela added that MCP is “not as revolutionary as a lot of people make it seem, because we already had standardized API communications — but it’s a nice, sort of clean way to do it.”

“We have our own MCP servers available, so people can access us through MCP.”

– Kiela
As for Contextual AI’s customers, Kiela says that MCP is just one of the ways they access external content for their models.

“We have our own MCP servers available, so people can access us through MCP,” he said. “We can call MCP from our agent. It hasn’t been the standard way, it’s just one of the ways that we can interact with these systems.”

I then asked about Agent2Agent (A2A), the open protocol developed by Google that allows agents to talk to each other. Kiela replied that Contextual AI is one of Google’s partners for this, so they support A2A too.

“So I think that’s a great idea. It’s basically one level higher, right. So, MCP is for: how do agents use tools? And then A2A is more about: how do agents talk to agents?”

## RAG, RAG, and More RAG
Ultimately, Contextual AI is a company focused on bringing the RAG technique to enterprises, in all its varied guises. It seems like the sudden emergence of MCP this year has put the company into a defensive mode — or at least explanatory, in that it has been forced to explain why MCP isn’t a replacement for RAG.

That aside, Contextual AI has RAG products aplenty — such as an [instruction-following reranker](https://contextual.ai/blog/introducing-instruction-following-reranker/) released in March, and a new [Document Parser for RAG](https://contextual.ai/blog/document-parser-for-rag/) released just this month. Kiela says products like these make its platform more modular.

“You can use our opinionated APIs for just doing RAG in a box,” he said, “but you can also use the individual components to make your existing RAG pipelines better.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)