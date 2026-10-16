On BrowseComp-Plus, GPT-4.1 answered **93.49%** of the questions correctly when it was given the supporting documents directly. When an agent used the same model but relied on BM25 to search for evidence to pass to the model, accuracy fell to **14.58%**.

That difference matters because a system that gets the answer right 93% of the time is far more useful than one that gets it right only 15% of the time.

An agent can look excellent in a controlled demo. The corpus is clean, the task is familiar, and the relevant material is easy to find. Production is messier. Documents may be duplicated, outdated drafts can remain searchable, and teams may use different terminology for the same thing. Several versions of a policy can coexist, while the task itself may unfold in ways the evaluation set never covered.

> “More model intelligence does not compensate for evidence the agent never retrieved.”

Under those conditions, the agent may retrieve incomplete, stale, or simply wrong material. More model intelligence does not compensate for evidence the agent never retrieved.

This is where retrieval starts to determine what the model can actually do.

## What BrowseComp-Plus shows

[BrowseComp-Plus](https://arxiv.org/abs/2508.06600) provides a useful way to separate these effects because it evaluates agents against a fixed corpus rather than a changing web-search service. The benchmark includes 100,195 documents and 830 research questions, each with human-verified supporting documents.

One evaluation gives the model all labeled positive documents directly. The paper calls this the *oracle* setting. Another requires the agent to search the corpus and gather the material it needs.

The difference is large. GPT-4.1 scores **93.49%** with the labeled supporting documents supplied and **14.58%** when the agent searches with the BM25 baseline. Qwen3-32B moves from **83.25%** to **3.49%** under the same two conditions.

The oracle result shows how well the model can answer when the required material is already in front of it. For system design, comparing retrieval systems is even more useful. The reasoning model stayed the same, while better retrieval improved the final answer rate and reduced the number of search calls.

> “The lesson is practical: before changing the model, examine what reaches it. A capable model working from poor retrieval results still has poor material to reason over.”

The lesson is practical: before changing the model, examine what reaches it. A capable model working from [poor retrieval results](https://thenewstack.io/search-retrieval-reranking-funnel/) still has poor material to reason over.

![Chart showing the accuracy disparity between a model answering with oracle evidence versus searching for evidence with BM25.](https://cdn.thenewstack.io/media/2026/10/8cb05df2-image3-1024x768.png)

***Figure 1. Same model, different evidence access:** BrowseComp-Plus: oracle evidence supplied directly versus agentic search with BM25.*

Enterprises can build agents around proprietary information that competitors do not have, from product and customer data to internal knowledge and operational records. That advantage depends on whether the agent can find the right information and rank it well, while also keeping up with changes in the underlying data.

## One task. A few minutes. A thousand retrievals.

In its [Search as Code research](https://www.perplexity.ai/hub/blog/rethinking-search-as-code-generation), Perplexity describes tasks that can trigger hundreds or thousands of retrieval operations within a few minutes. Search becomes a sustained part of the agent’s workflow rather than an occasional lookup.

Traditional search usually returns one ranked result set per query. An agent can decompose a task into multiple searches, fan them out in parallel, combine the results, and issue follow-up searches as it learns more.

At that scale, fan-out becomes a normal part of the workload. If an agent runs ten searches in parallel and needs all ten results before it can continue, the slowest search sets the pace for that step. If the agent repeats that pattern several times during the task, tail latency matters even more than it does for a single interactive query.

The same multiplication shows up in capacity. One user task can generate hundreds of search operations, and many agents may be doing that at once. Measured in user requests, the service may look lightly loaded while the retrieval layer is processing a much larger volume of searches.

When one task fans out into many searches, retrieval quality matters even more. People judge search results using context they have built up over time. They know which sources they trust and can often recognize when something looks stale, unreliable, or out of place. An agent usually starts with far less background and has to build its understanding from the evidence it retrieves during the task. It is often on its first day on the job. If one of those early results is wrong, the next search may be wrong too, and the rest of the task can drift from there.

> “People judge search results using context they have built up over time. An agent usually starts with far less background and has to build its understanding from the evidence it retrieves during the task. It is often on its first day on the job.”

A simple model shows why repeated retrieval steps raise the stakes. Suppose a workflow requires five retrieval steps, each with a 90% probability of supplying what the agent needs, and assume there are no retries or recovery. The probability that all five succeed is 0.9^5, or about **59%**. Real agents can retry, use redundant evidence, branch, and recover, so this is an illustration rather than a measured agent success rate. It shows how small per-step weaknesses can accumulate when later work depends on earlier retrievals.

![Chart showing how end-to-end success fails multiplicatively.](https://cdn.thenewstack.io/media/2026/10/85faf204-image4-1024x768.png)

***Figure 2. Small retrieval errors can compound across a multi-step task**Illustrative model: if every required retrieval step must succeed and there is no recovery, end-to-end success falls as the number of steps increases.*

Agentic search therefore asks the retrieval layer to handle more queries for each user task, more searches running in parallel, and retrieval steps whose results influence later work. As those patterns scale, capacity, tail latency, and retrieval quality all become more important.

## Your retrieval layer was tuned for a different user

Web search spent decades adapting to human search behavior.

As Jon Bratseth [writes in *Your agent wants to search like a 2010 quant*](https://blog.vespa.ai/your-agent-wants-to-search-like-a-2010-quant/?utm_source=chatgpt.com), people are often “lazy and clueless” when they search. The wording is blunt, but the point is straightforward: people tend to enter short queries without knowing much about the corpus or the search system behind it.

Search engines evolved around those habits. Short, underspecified queries became the norm, and much of the complexity moved behind the interface, where the search system inferred intent and returned a ranked list.

An agent can use a much richer interface. It can search for exact terms, construct filters, specify dates, group results, choose among ranking strategies, and issue follow-up searches based on what it has already found. Jon gives examples ranging from proximity search for names in a legal case to semantic search over high-quality sources and grouping events by month. In [an agentic workflow](https://thenewstack.io/ai-agent-infrastructure-performance/), those searches can be chained together as the agent narrows, expands, and verifies its answer.

That means the retrieval layer receives more than a short text query. It may receive several kinds of input: lexical terms, query embeddings, structured filters, or combinations of them. An agent-facing interface should make those choices explicit so the agent can use the right retrieval method for the task instead of collapsing every request into one text string.

Evaluation needs to reflect the same shift. A retriever tested mostly on short, human-written questions may behave differently when an agent generates its own filters, search terms, and follow-up queries. Retrieval quality should therefore be measured on the queries the agent actually sends in production, not only on the questions in the evaluation set.

Before changing the model or retuning retrieval, inspect those production queries first.

## A search API returns results. An agent needs more control.

Traditional search often exposes a narrow contract: send a query, let the server run a retrieval pipeline, and receive a ranked result list.

That works well when the caller only needs the output. An agent may need more control over how retrieval and ranking are carried out at runtime, depending on what the task requires.

Vespa exposes that control through its query language and rank profiles. The caller can combine lexical or semantic retrieval, structured filters, ranking choices, and grouping in the same request, affecting how candidates are selected, scored, and returned.

The interface matters because the agent can only use the controls it can reach. A system may support filtering, ranking, aggregation, or several retrieval methods internally, but those capabilities do not help if the agent cannot invoke them when the task calls for them.

![List comparing a narrow interface against a richer interface.](https://cdn.thenewstack.io/media/2026/10/96b3b55b-image5-1024x768.png)

***Figure 3. How much of the retrieval stack can the agent reach?** Illustrative comparison of a narrow search interface with richer query-time controls. Product categories do not determine which capabilities are exposed. Trusted application code enforces authorization.*

A fixed pipeline is still a good fit for many well-defined applications. Agentic workflows become more demanding when the task changes from one step to the next and the agent needs different retrieval behavior at runtime.

The goal is to expose the controls the agent needs while keeping authorization, validation, budgets, and other safeguards on the trusted server side.

## Exposing the controls is not enough

An engine can expose filters, lexical matching, nearest-neighbor search, grouping, multiple rank profiles, reranking, and query-time controls. Those capabilities only become useful to the agent when the interface explains what is available and when to use it. If rank profiles, filterable fields, or grouping operations are not described, the agent may default to a free-text query and push more of the work into later reasoning or tool calls.

One way to handle this is to put a query-translation model between the agent and the retrieval system. The translator takes the agent’s request and converts it into the engine’s query syntax. This can be useful when an application wants query construction centralized behind a stable interface.

When the caller is already an agent, a separate translator often inserts a specialized model between the agent and the retrieval system. The agent already has the task, prior results, and constraints in context; the translator must reconstruct that intent from a narrower request and convert it into a query. This extra handoff adds latency and another opportunity to lose or distort what the agent meant, making retrieval harder and less reliable.

Another approach is to describe the retrieval interface directly to the agent: which fields are available and what they mean, and what rank profiles are provided.

We call that an **agent-ready schema**: a description of the fields, controls, and retrieval options the agent can use, along with the application-specific meaning behind them. Vespa has described work on convenience tooling in this direction, and much of that guidance can be generated from the application schema itself.

## From schema to skill

[A search schema](https://thenewstack.io/building-agent-friendly-apis/) already contains much of the information an agent needs: field names and types, which fields can be searched or used as filters, available rank profiles, and configured tensors and models.

What it lacks is a description of what the fields mean and how they could be used. A field called `tier` may represent an account plan, a service level, or something else entirely. A timestamp such as `published` may mean first publication, last modification, or ingestion time. A rank profile named `exact` tells the agent very little about the kinds of queries it was designed for.

Those meanings can be added as explanations in the schema. That gives the agent more than names and types; it gives it enough context to choose the right fields, filters, and ranking options for the task.

**Schema-to-Skill** is the proposed generation step: combine the Vespa application schema, engine guidance, and application-specific knowledge into a short Markdown skill the agent can consult when constructing queries. The schema provides the structure, engine guidance explains how to use the available capabilities safely, and application-specific knowledge adds the vocabulary and meaning that cannot be inferred from the schema alone.

![Workflow illustrating the architecture of a translation layer and an agent-ready schema.](https://cdn.thenewstack.io/media/2026/10/040a5a3d-image2-1024x768.png)

***Figure 4. Translate for the agent, or teach it.** A translation layer uses a separate model call to construct the search query. With an agent-ready schema, the agent receives the guidance needed to construct queries using the retrieval controls exposed by the application. Schema-to-Skill is the proposed generation workflow.*

The agent uses that skill to choose among the retrieval strategies the Vespa application exposes. Vespa still does the actual retrieval work over the corpus, including matching, filtering, ranking, and aggregation. The agent decides what to ask for; the retrieval system executes it.

Better models can help, but agents still fail when they search for the wrong evidence, cannot express the [right retrieval strategy](https://thenewstack.io/the-precision-engine-why-agentic-rag-is-genais-next-leap/), or do not understand the search system they are calling.

> “Better models can help, but agents still fail when they search for the wrong evidence, cannot express the right retrieval strategy, or do not understand the search system they are calling.”

Agentic workloads make those weaknesses more costly because retrieval happens throughout the task. Each search can affect what the agent sees next, how much context it carries, and whether it needs to search again. At scale, retrieval quality, tail latency, and query volume become part of the task itself.

That puts more pressure on the retrieval interface. Agents need access to the filters, ranking strategies, grouping, and other controls the task requires, along with enough guidance to use them correctly. An **agent-ready schema** makes those capabilities explicit, and **Schema-to-Skill** is one way to turn that structure, engine guidance, and application-specific knowledge into something the agent can use when constructing queries.

Before upgrading the model, inspect the searches the agent is issuing, the evidence those searches return, and whether the retrieval system gives the agent both the controls and the guidance it needs. Better retrieval can improve the answer, reduce unnecessary work, and make the rest of the agentic system more effective.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/c68dec91-jennypic-600x600.jpeg)

Jenny Morris is a Senior Principal Solutions Architect at Vespa.ai, where she operates at the intersection of AI infrastructure and enterprise strategy, working with organizations to build scalable AI search, personalization, and retrieval-augmented generation (RAG) systems. With deep expertise in...

Read more from Jenny Morris](https://thenewstack.io/author/jenny-morris/)