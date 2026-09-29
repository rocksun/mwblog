**You built a search system using the latest, greatest models**, and maybe you were thrilled with the outcome. But what happens if the search results were… sort of… *bad?* Your first instinct might be to invest time and resources in a bigger, better reranker. Maybe you thought, “We just need a better way to bubble the best result to the top of the heap.” That could be true. Or you may need a different approach altogether.

The problem with devoting all your energy toward improving your reranker is twofold. First, large-scale reranking gets expensive fast. It also increases latency as your system meticulously combs through a mountain of candidate results. Second, your reranker can’t surface better results if it never had them to begin with. Before dedicating efforts solely to a better reranker, check whether the right results are making it to your candidate pool and the overall cost of reranking everything. You may want to take a different approach.

> *Join Vespa.ai on October 13 to learn how to reframe your retrieval process as an efficient funnel instead of one expensive step.*

**Join the live conversation**: On October 13, [Vespa.ai](http://vespa.ai)’s Director of Product Marketing [Bonnie Chase](https://www.linkedin.com/in/bonnie-chase/) and Senior Principal Solutions Architect [Jenny Morris](https://www.linkedin.com/in/jennyjmorris/) will walk you through creating a multi-stage retrieval process to maximize efficiency while minimizing cost.

REGISTER NOW FOR THIS WEBINAR

You have successfully registered for the webinar.

**Instead of one expensive reranking step**, you can think of your retrieval process as a multi-stage funnel. Start with a large corpus of documents and generate a broad pool of candidate results using relatively inexpensive lexical, vector, or hybrid retrieval methods. From there, narrow the pool before passing a select group of likely choices to a more expensive reranking step that involves machine learning inference. This funnel approach provides wider coverage early on while limiting costly operations later in the process.

Of course, several tradeoffs come into play when designing your retrieval funnel. The interplay between recall, relevance, latency, and cost should inform your architecture. For example, retrieving more candidates may improve recall, but it also means you’ll have more results to evaluate and potentially rerank, which could impact cost and latency.

This funnel approach also applies to RAG applications. [As RAG systems scale](https://thenewstack.io/rag-retrieval-scaling-architecture/), retrieval becomes even more important to make sure the right information reaches the LLM in the first place. Even after you retrieve the right documents, you still need to decide which passages deserve space in the model’s context window. The same progressive narrowing approach can help there, too.

**You can expect** to learn about this retrieval funnel approach and much more at the upcoming live webinar, “[Why the Best Reranker Can’t Fix Bad Retrieval](https://thenewstack.io/webinar/why-the-best-reranker-cant-fix-bad-retrieval/).” You can ask experts from the [Vespa.ai](http://vespa.ai) team your own questions, but they’ll also address practical questions such as:

* How many candidates should you carry from one stage to the next?
* When is lexical retrieval enough, and when does a vector or hybrid approach add value?
* How will you know if the expensive reranking is actually improving your results?
* How can this approach extend to RAG for passages to include in your context window?

If you’re ready to rethink your retrieval process or simply want to learn more about modern retrieval architecture, [join us on October 13](https://thenewstack.io/webinar/why-the-best-reranker-cant-fix-bad-retrieval/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/09/285d5883-cropped-0d52977e-dr-kim.jpeg)

Kimberly Fessel is a data consultant, author, instructor, and founder of Dr Kim Data LLC, partnering with clients worldwide on data science, machine learning, and AI projects and delivering technical instruction in Python, SQL, and modern data workflows. She holds...

Read more from Kimberly Fessel](https://thenewstack.io/author/kimberly-fessel/)