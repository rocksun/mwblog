AI agents need the right information to work well. Whether they manage to find it is the difference between success and failure in most real-world cases, and increasingly so as models get smarter.

The practitioners in the field of *letting large language models find the information they need* have passed through several stages of enlightenment.

The *first stage* was the [vector database](https://thenewstack.io/rag-retrieval-scaling-architecture/) period of ’24, when the belief was that all you needed to do was chop text into independent chunks, create an embedding vector for each, and retrieve them via a nearest-neighbor search. This was simple, but alas, it did not work well. Chunks had too little context, and scoring [based solely on vector](https://thenewstack.io/vector-search-is-reaching-its-limit-heres-what-comes-next/) similarity failed to reliably surface useful information.

Enter the *second stage*, where the learnings from human information retrieval over the last half century were combined with vector retrieval: [Hybrid search](https://thenewstack.io/rag-pipeline-hybrid-search/), BM25, machine-learned ranking, and so on. This was a huge improvement which brought many use cases from demo stage to production quality.

But there is still vast room for improvement, and with Perplexity’s announcement of [search as code](https://research.perplexity.ai/articles/rethinking-search-as-code-generation), we might be officially entering the *third stage*. See, the search field has needed to deal with one big problem: Human users are lazy and clueless, at least when it comes to search. Given this, it turns out that the words typed into query boxes should be treated as vague indicators of what they might want, and providing any finer control is pointless, as nobody would be bothered to use it. You can see this most clearly in the evolution of Google search from letting you find web pages containing specific words to whatever it is now; [thoroughly lamented](https://www.quora.com/Why-is-Google-search-so-absolutely-garbage-useless-and-annoying-Its-total-trash-so-please-dont-respond-if-youre-just-a-nerd-loyalist-loser) but of course also deeply grounded in observation of real users.

> “The search field has needed to deal with one big problem: Human users are lazy and clueless, at least when it comes to search.”

Agents, in contrast, are not so clueless. And they certainly aren’t lazy! There’s no reason to limit their options to those of a casual human user. They should be able to:

* Search for the names of those involved *near* each other in text when researching a legal case
* Do a pure semantic search prioritizing high-quality sources when seeking a broad overview of a topic
* Select a year range and group by month when constructing a timeline of some events

The list goes on. Typically, an agent will string together many of these queries to reach its goal. First gaining an overview, then researching more specific topics, forming hypotheses, verifying important details in them, and so on. In short, search like an expert who knows what they are doing and really cares about the results— like a quant doing financial analysis.

It seems *obvious* that this will yield better results, and this is also what evaluations such as those published by Perplexity in its [search as code blog post](https://research.perplexity.ai/articles/rethinking-search-as-code-generation) show (ignore the “code” aspect, as code execution is generally useful and *where* that code runs doesn’t impact quality).

Doing this in practice, with your own data, is actually quite easy. The models already know how to write complex queries in the languages of [well-known AI search engines](https://docs.vespa.ai/en/querying/query-language.html); they just need to be told

* That they can
* What fields are available and what they mean
* What choices they have in ranking the results

*How* you tell them doesn’t actually matter that much; any simple textual description of what fields and ranking options are available will do. Models today are smart enough to use this effectively to connect their intents to practical detail queries.

> “It’s time to let your agents search like a 2010 quant.”

When creating search for humans, developers need to implement solutions that work well across a broad set of use cases, which involves making trade-offs where some types of queries cannot be improved because doing so would impact other types. When implementing for agents, the focus shifts to providing a wide toolbox for the agent to use to address their varied informational needs: broad *and* highly specific lexical recall, metadata attributes for filtering, grouping, and aggregation, as well as different ranking methods suited to different needs.

Accordingly, developers working on agentic search need to shift their focus from reusing techniques that have worked well for casual humans to the much richer capabilities traditionally provided by solutions for competent professionals.

It’s time to let your agents search like a 2010 quant.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/10/9c394e20-cropped-0129e807-jon-bratseth.png)

Jon Bratseth is the CEO and a cofounder of Vespa.ai, and the architect and one of the main contributors to Vespa, the platform for applications combining AI and data online. Jon has 25 years of experience as an architect and...

Read more from Jon Bratseth](https://thenewstack.io/author/jon-bratseth/)