**Every product team is chasing the same moment:** The user opens a page and thinks, *this understands me*.

A shopper who loves floral prints should see more floral prints. A user who follows local politics should open their app to see news about local politics. A job candidate who keeps clicking remote roles should not keep getting shown in-office jobs.

That is not a niche feature anymore. It is the baseline expectation. Users decide quickly whether a product system understands them, and they rarely care whether the failure came from search, recommendations, merchandising rules, or stale data.

Here is the uncomfortable truth: Most teams do not have a personalization *quality* problem. They have a personalization *architecture* problem.

Personalization is not a widget bolted onto search. It is a ranking decision. The system has to decide, for this user and this request, what deserves the next slot. That means weighing the user, the item, the context, and the business goal at the same time. In many stacks, the ranking layer is the one place that cannot see all of those signals together.

> The hard part is not collecting signals. The hard part is combining them while the user is still there.

## Why personalization is hard in the first place

To put the right item in the right slot, a system has to understand several things at once:

* **Intent:** What is the user asking for right now?
* **Item quality:** What does each candidate actually contain or represent?
* **User history:** What has this person clicked, bought, read, watched, or ignored?
* **Availability:** Is the item in stock, fresh, nearby, legal to show, or ready to ship?
* **Business priority:** What should the business promote, protect, or de-emphasize?

Those signals often disagree. The most relevant item may not be the most profitable. The most profitable item may be out of stock. The user may say “running shoes,” but their behavior says “trail running, wide fit, under $120.”

They also move on different clocks. Product attributes change slowly. Inventory and price can move throughout the day. Preferences shift with every click. External context — weather, breaking news, a championship game, a cultural moment — can matter without warning.

Personalization means folding all of that into one ordered list, on every request, in milliseconds. The signals themselves are not the bottleneck. Query-time ranking is.

## The usual stack makes the problem harder

Most personalization systems are assembled from tools that were each designed for one slice of relevance.

**Keyword search engines** are excellent at lexical matching. They are good when the query language and catalog language line up. But shoppers, readers, and job seekers rarely speak in neat index terms. You indexed “athletic performance running footwear”; they typed “running shoes.” Synonym rules can help, but they do not scale gracefully across long-tail language, changing catalogs, and new user behavior.

**Vector databases** start from the opposite side. They are good at semantic similarity: “Find me things like this.” That is powerful, but nearest-neighbor search is not the same thing as personalization. Real ranking has to blend semantic similarity with live behavior, stock, price, margin, freshness, eligibility, and business rules.

**Re-rankers, recommendation services, feature stores, and rule engines** are usually added to glue everything together. That is where fragmentation creeps in.

![A fragmented personalization stack compared with a unified query-time ranking pipeline](https://cdn.thenewstack.io/media/2026/07/9927cdb1-image1-1024x603.png)

*Figure 1. A fragmented personalization stack compared with a unified query-time ranking pipeline*

When retrieval and ranking live in separate systems, the ranker often works from a partial, stale, or precomputed view of the world. Click history, session context, and the user’s live preference vector arrive too late. Business rules become filters or overrides instead of ranking signals. Fresh inventory or price changes require coordination across multiple systems.

Every hand-off adds latency. Every boundary creates another place for signals to drift. Every “quick rule” becomes another hard constraint that can accidentally turn “show the closest match” into “show nothing.”

> “Every hand-off adds latency. Every boundary creates another place for signals to drift.”

The deeper issue is a timing assumption. Many architectures were built around offline ranking: process the catalog, compute scores in a batch job, and serve those scores until the next rebuild. That works when preferences are stable. It breaks when the most valuable signal is the click that happened two seconds ago.

## What changes when ranking happens in one real-time pipeline

A real-time personalization architecture treats retrieval, ranking, and inference as one serving problem.

That is the core idea behind [Vespa’s approach](https://vespa.ai/): Text search, vector similarity, structured filtering, ranking expressions, tensor computation, and model inference can live inside one query pipeline. Instead of retrieving somewhere, enriching somewhere else, and ranking at the end, the system can rank with the relevant signals while it is still deciding what to return.

That architectural choice changes the shape of the problem.

### 1. Retrieval is hybrid from the start

Lexical search, semantic search, and structured filtering can run together instead of being reconciled after the fact. A product query can combine text, embeddings, filters, session behavior, and item attributes in one request.

That matters because personalization is rarely one signal. The user’s query still matters. So does semantic similarity. So do category, availability, price, and business constraints. Hybrid retrieval keeps those signals in play before ranking starts.

### 2. Ranking can express the actual objective

A personalization score should not be trapped inside one [similarity function](https://thenewstack.io/spark-4-2-ai-workloads/). It should be a formula that reflects the product’s goals.

That formula might combine BM25, vector similarity, user affinity, stock level, margin, popularity, discount depth, freshness, rating, distance, or a weather term. Some of those signals need normalization first. Some should matter only for certain categories or users. Some should be tested as weights.

The important part is that they are all terms in the same ranking expression, not scattered across services.

A simplified version might look like this:

```

final_score =
    0.30 * lexical_relevance +
    0.25 * semantic_similarity +
    0.25 * user_affinity +
    0.10 * availability +
    0.10 * business_priority

```

In production, the formula can be more nuanced. But the principle is simple: personalization, relevance, and business logic belong in the same scoring decision.

### 3. Model inference can run where the data lives

Some signals should come from learned models rather than hand-tuned rules: propensity to buy, churn risk, quality prediction, fraud risk, query classification, or a learned-to-rank model.

When inference runs in the serving path, those model outputs can become ranking features instead of delayed batch scores. That reduces the need to ship data to a separate inference service, wait for a response, and stitch the score back into ranking.

### 4. Updates become immediately useful

“Real time” should not mean “after the next index rebuild.” If inventory changes, stock should be rankable immediately. If a user clicks two yellow dresses, “yellow” should matter on the next request. If a merchandising team adjusts a ranking weight if the weight is exposed as a query-time input, the experiment should start producing useful feedback right away.

That is the difference between personalization as a nightly job and personalization as a live ranking decision.

## Tensors make the personalization concrete

The most useful mental model is simple: represent the user and the item in the same feature space, then rank by how well they match.

In Vespa, tensors make that practical. A tensor can be a scalar, a dense vector, a sparse map of feature-weight pairs, a matrix, or a more complex structure. That means the same framework can represent semantic embeddings, product attributes, user preferences, business objectives, and model features.

![User and item tensors combined into a personalization score, then blended with other ranking signals](https://cdn.thenewstack.io/media/2026/07/ac21c1d5-image2-1024x585.png)

*Figure 2. User and item tensors combined into a personalization score, then blended with other ranking signals*

For example, each **item** can carry a sparse feature tensor:

```

{
  "floral": 0.90,
  "yellow": 0.70,
  "short_sleeve": 0.80,
  "crew_neck": 0.65
}

```

Each **user** can carry a tensor with the same feature names:

```

{
  "floral": 1.00,
  "yellow": 0.37,
  "short_sleeve": 0.33,
  "crew_neck": 0.31
}

```

Because the two tensors share a shape, personalization becomes a dot product: multiply matching features, sum the result, and use that score inside ranking.

In a Vespa rank profile, the core expression is compact:

```

# schema: item attributes stored as a sparse tensor
field item_features type tensor&lt;float>(feature{}) {
    indexing: attribute | summary
}
 
# rank profile: the user's live preferences arrive as a query tensor
rank-profile personalized {
    inputs {
        query(user_features) tensor&lt;float>(feature{})
    }
    first-phase {
        expression: sum(query(user_features) * attribute(item_features))
    }
}

```

That one expression is not the whole ranking function. It is the personalization term. BM25, vector similarity, stock, margin, freshness, distance, or a model score can be added as other terms with their own weights.

The user tensor is where real-time behavior becomes powerful. Click a floral item, and the “floral” weight rises. Click two yellow items, and “yellow” rises; the application feeds click events into the user profile. The next query can use those updated preferences immediately, without waiting for a nightly profile build.

## Business goals stop fighting personalization

In fragmented stacks, business rules often become blunt instruments: boost this category, hide that brand, force these items to the top, filter these out. That can satisfy a short-term merchandising goal while damaging relevance.

When business logic is part of the ranking expression, it can be more subtle. You can boost overstocked inventory without ignoring intent. Promote umbrellas when rain is forecast without turning every search into an umbrella search. Give new sellers a small exploration boost. Prioritize destocking before a new product line launches. Surface team merchandise during a championship run.

> “When business logic is part of the ranking expression, the user still gets relevant results. The business still influences outcomes.”

The user still gets relevant results. The business still influences outcomes. The difference is that both are expressed as ranking signals instead of competing systems.

That also makes experimentation easier. A merchandising or growth team can test weights, traffic splits, and ranking profiles without asking engineering to rewrite the whole pipeline. Relevance becomes a controllable growth lever rather than a fragile side effect.

## The same pattern applies beyond commerce

The examples above are easy to picture in apparel, but the architecture is not commerce-specific. Personalization is the same ranking problem in many products:

* **Content feeds:** Blend topic affinity, freshness, engagement, creator quality, and business rules.
* **News:** Rank by reading history, topic interest, locality, freshness, and source diversity.
* **Jobs:** Match candidate preferences such as remote work, seniority, compensation, location, and tech stack against role attributes.
* **Geo search:** Treat distance as one normalized ranking term alongside relevance, quality, and preference.
* **Video and audio:** Combine embeddings, viewing history, metadata, freshness, and learned ranking models.

Different domains need different features. The architecture pattern is the same: retrieve candidates, rank with the signals that matter, update those signals as behavior changes, and keep the decision close to the data.

## Scale doesn’t have to be the trade-off

The natural concern is that a more expressive ranking system must be slower. In practice, that does not have to be true.

Vespa was built for large-scale serving from the beginning: billions of documents, high query volume, and low-latency ranking. The reason this works is multi-stage ranking. The system does not run the most expensive logic across every possible result. Instead, it uses a fast first phase to narrow the candidate set, then applies more precise ranking to the smaller group that remains.

For example, a cheap first phase narrows a huge candidate set. Then, once the candidate set is smaller, Vespa can apply full-precision scoring, richer [tensor operations](https://thenewstack.io/vectors-tensors-ai-search-explained/), business logic, and model inference where they matter most.

The result is a practical balance: speed across the full corpus, accuracy in the final ranking, and enough flexibility to personalize each query without turning the serving stack into a chain of fragile services.

## What’s next

Personalization is not failing because teams lack data. Most teams already have plenty of signals: query intent, clicks, product attributes, inventory, margin, freshness, location, and business priorities. The harder problem is that those signals often live in different systems, move at different speeds, and arrive too late to influence the final ranking decision.

That is why personalization should be treated as a ranking problem. When retrieval, ranking, personalization, and business logic are split across separate systems, the ranker is forced to work with [stale or incomplete context](https://thenewstack.io/vibe-coding-context-debt/). The user moves faster than the architecture can respond. Every new signal becomes another integration project.

A unified real-time ranking pipeline changes that. User behavior, item attributes, semantic similarity, lexical relevance, inventory, and business goals can all become parts of the same scoring function. Tensors make those signals directly comparable and usable at query time. Instead of bolting personalization onto the end of the system, personalization becomes part of the decision the engine makes for every query.

The goal is simple: rank each result with the best context available, at the moment the user asks. That is when personalization stops feeling like a feature and starts feeling like relevance.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/c68dec91-jennypic-600x600.jpeg)

Jenny Morris is a Senior Principal Solutions Architect at Vespa.ai, where she operates at the intersection of AI infrastructure and enterprise strategy, working with organizations to build scalable AI search, personalization, and retrieval-augmented generation (RAG) systems. With deep expertise in...

Read more from Jenny Morris](https://thenewstack.io/author/jenny-morris/)