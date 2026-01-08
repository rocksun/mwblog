Current attempts to centralize the increasingly fragmented data ecosystem — which is distributed across vendors, infrastructure, architectures, and tooling — are as vast as they are varied. However, they share one point of commonality in 2026: they reinforce the need for a cooperative approach for building applications, deploying them, and reaping their underlying business value.

For intelligent agents, this [collective approach](https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/) means greater specialization and quantities of agents interacting with each other. The models underpinning them will become more diverse, may very well become smaller, and will fuel cooperation between agents and humans as “AI assistants give rise to AI ‘team members’ that own well-defined responsibilities and outcomes,” said [Aniket Shaligram](https://in.linkedin.com/in/aniket-shaligram-a3b00b32), [Talentica Software](https://www.talentica.com/) VP of Technology. “Organizations will formalize how these AI agents contribute to workflows, measure performance, and collaborate with human teams.”

Such collaboration will range the gamut of data-centric resources, from federation infrastructure to traditional databases supporting different modalities, vector embeddings, and protocols such as MCP, Agent-User Interaction ([AG-UI](https://docs.ag-ui.com/introduction)), and Agent to UI ([A2UI](https://a2ui.org/)). Users will no longer look for a single hyperscaler or vendor offering these things, but rather “the ability to plug and play,” commented [Yugabyte](https://www.yugabyte.com/?utm_content=inline+mention) CEO [Karthik Ranganathan](https://www.linkedin.com/in/kranganathan). “Just saying one thing will do it all is like saying we know the answer to a question even before you’ve asked it.”

This interchangeability will even include cloud providers, as the industry transitions to more regional, specialized clouds for specific statistical AI-infused tasks.

## An Inter-Agent Collective

Cooperation between AI agents depends as much on a technological framework for recording and monitoring the actions of agents as it does respective agents working in concert. Users can implement the former with different databases, including document stores, graph databases, and [knowledge graph](https://thenewstack.io/better-llm-integration-with-content-centric-knowledge-graphs/) applications.

With this approach, “all the inputs and outputs of the agents, every decision, goes into the orchestrating knowledge graph,” said [Franz](https://franz.com/) CEO [Jans Aasman](https://www.linkedin.com/in/jans-aasman). The orchestrating graph is ideal for enforcing data governance policies and tracing the actions agents take. Agents can be codified according to different tasks, database-orientations (like those for human resources, customer satisfaction, inventorying, etc), or verticals.

Moreover, inter-agent collaboration spans AI models — which may stem from any provider, even competing vendors. “It’s like everything has a different superpower,” Ranganathan said. “But, if you go to Google, you only get one thing and if you go somewhere else, you only get one thing. But the way we built our vector algorithms and storage layer, we kept the pgvector interface layer, and made any of these [models] pluggable.”

## RAG’s Retirement

RAG is still the most pervasive way for language models to interact with the enterprise—albeit typically as assistants. Several developments will change this fact in 2026. Firstly, the [expansion of the size of prompt windows](https://ar5iv.labs.arxiv.org/html/2306.15595#:~:text=We%20present%20Position%20Interpolation%20%28PI%29%20that%20extends%20the,long%20document%20summarization%20from%20LLaMA%207B%20to%2065B.) greatly reduces the [need for RAG](https://thenewstack.io/beyond-basic-rag-ai-agents-for-context-aware-responses/), since users can input all relevant information (including documents or manuals) into a natural language question.

Ensemble modeling, in which multiple LLMs read documents or vectorized content before coming to a consensus response, is another means of collaboration between AI models. “You have three or five LLMs read a document,” Aasman explained. “You specify the information you want out of the document, and then there’s a resolver system that will work behind the scenes to harmonize the outputs of all the different models, so we ultimately get data that’s 99.9% correct. If you use one, it might be only 60% correct.”

## Retrieval Augmented Conversations

Instances in which language models direct interactions with humans, which some have termed [Retrieval Augmented Conversation](https://github.com/NLPlab-skku/rac) (RAC), typify the newfound role of models as coaches or collaborators with humans. With this method, “the AI knows the answer and is asking the user a question, and the user is answering while the AI evaluates the answer and provides some guidance,” said [Aquant](https://www.aquant.tech/) Founder [Assaf Melochna](https://www.linkedin.com/in/assafmelochna).

For example, a customer service agent may be working with a language model about the proper procedures to help customers with connectivity issues, and “the AI is saying this is good, but I would emphasize A, B, and C; let’s do it again, now,” Melochna said. These conversational systems may involve speech recognition and constructs for short term memory. In this and other implementations, the transfer of the power dynamic from the human to the model is perceptible. Aasman described a situation in which he interacted with a language model for a knowledge graph.

“It tells me what’s possible and I say what I really want, and it says ‘let’s try this’, and it tries it and it answers ‘this is cool, please store this in a visualization,’ and it keeps going,” Aasman said.

## AI Clouds Over Hyperscalers

The interchangeability of language models for different use cases, industries, and AI tasks will be reflected (if not enabled) by a corollary in cloud deployments. In some cases, this occurrence will result in new patterns for accessing models. According to [Roger Brulotte](https://ca.linkedin.com/in/rogerbrulotte?trk=public_post_feed-actor-name), CEO of [Leaseweb Canada](https://www.leaseweb.com/en/), “Labs, universities, and R&D teams are building and training models, then handing the commercialized version back to the customer through a licensing model or revenue-share arrangement.”

For both the users and suppliers of those models, the ability to rapidly spin-up data for training, fine-tuning, deploying, and implementing workflows for language models requires resources purpose-built for these tasks. Foremost among these is a proliferation of [GPUs](https://thenewstack.io/keeping-gpus-ticking-like-clockwork/). “As demand surges for inference-level GPU compute, organizations will adopt on-demand GPU services,” commented [Pankaj Mendki](https://thenewstack.io/author/pankaj-mendki/), Talentica Software Head of Emerging Tech. “Serverless GPU models will allow dynamic scaling, reduce operational overhead, and become the standard infrastructure approach for GenAI workloads.”

## GPU Clouds

[Neocloud](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-evolution-of-neoclouds-and-their-next-moves) providers — smaller clouds that specialize in providing resources for advanced machine learning jobs — and not hyperscalers, abundantly furnish such infrastructure and tooling. According to [Richard Copeland](https://www.linkedin.com/in/richardcopeland), CEO of Leaseweb, “When your model performance becomes a competitive advantage, you can’t afford wasted compute, unpredictable throttling, or hardware carved into fractional units you can’t see. This is where optimized IaaS and regional GPU clouds start to shine.”

Additionally, organizations will require a dynamic storage layer to position their data closest to their cloud of choice for their particular task, hydrate it for the job, then return their data — which can include the results of training and inference jobs — to their long-term object store. The ability to transition AI models and data between clouds to maximize cost reductions, compute, and storage options is part of the bold new future for 2026.

With this methodology, “Companies will be able to safely split compute across multiple clouds, regional providers, and even on-prem environments,” Copeland said. The particular cloud of choice will be determined by the needs of the enterprise at that specific time, as fleeting as they might be.

## Future-Proofing

The same adaptability that will be manifest in cloud services is applicable to the underlying AI models that organizations employ to collaborate together and with humans. According to Aasman, there’s no denying the cost concerns fueling both developments. “The CEO of IBM had a quote saying we can’t sustain the current investments in AI,” Aasman said. “They’re using LLMs for everything and there’s 8 trillion in investment, but the combination of OpenAI, [Oracle](https://www.oracle.com/developer?utm_content=inline+mention), Google, and Amazon, in terms of income, is only $230 billion dollars. This is unsustainable. So, the only way to go forward is with small models.”

A greater reliance on smaller language models only adds to the diversity of models, their areas of specialization, and the need to interchange them for the job at hand. Doing so is not only the vision for 2026, but also for the future. Ranganathan called such ad-hoc adaptability “future-proofing. It’s an ability to switch to be truly democratic.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/ee3e39b7-cropped-52925a32-jelani-harper-110x110-1.jpg)

Jelani Harper has worked as a research analyst, research lead, information technology editorial consultant, and journalist for over 10 years. During that time he has helped myriad vendors and publications in the data management space strategize, develop, compose, and place...

Read more from Jelani Harper](https://thenewstack.io/author/jelani-harper/)