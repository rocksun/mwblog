Caching was one of the most critical optimizations in modern AI systems long before most teams realized it. Early prototypes of Retrieval-Augmented Generation (RAG) pipelines, AI copilots, and semantic search platforms often performed perfectly on small datasets and with limited traffic.

But as soon as real production workloads arrived, tail latency, compounding infrastructure costs, and repeated retrieval operations started becoming impossible to ignore.

Our first instinct was that it was an easy fix. Redis would solve this effortlessly.

It was fast, simple, tested, and already trusted in high-scale systems for session storage, API caching, and rate limiting. Exact-match prompt caching dramatically reduced response times, allowing many repeated AI requests to be served in milliseconds without touching the expensive retrieval or inference layers again. For a while, Redis proved us right and solved almost every performance problem we had.

Until our workloads changed.

Traditional string-matching caches break down the moment your infrastructure becomes semantic. Human language variation means two users will ask for the exact same information using completely different wording.

> “Traditional string-matching caches break down the moment your infrastructure becomes semantic.”

Because Redis relies on exact string matches, it misses those connections entirely, creating duplicate, fragmented cache entries for identical intents. Before long, our hit rates tanked, memory utilization spiked, and we were stuck with a massive cloud bill for storing redundant data contexts.

That was when semantic caching via vector databases started to look attractive. On paper, it seemed like the perfect architectural evolution: match queries based on vector-distance math so that varied prompts could reuse old embeddings, context chunks, or past LLM answers.

Of course, production reality was far messier than the hype suggested. Vector database caching introduced its own set of problems: latency spikes, false-positive matches, embedding drift, operational complexity, and difficult tuning decisions around similarity thresholds. In some workloads, semantic caching significantly improved performance. In others, it became slower and more expensive than the Redis setup it was supposed to replace.

> “Of course, production reality was far messier than the hype suggested.”

What we eventually learned is that Redis and vector databases solve fundamentally different caching problems. One optimizes exact retrieval speed. The other optimizes semantic reuse. Treating them as interchangeable technologies led to architectural mistakes that only became apparent under real production traffic.

## The AI architecture we started with

Before the caching problems started appearing, our AI stack looked fairly standard for a modern Retrieval-Augmented Generation (RAG) system. The pipeline was designed around three major stages: embedding generation, document retrieval, and LLM inference.

A user query first entered the API layer, where preprocessing handled normalization, authentication, rate limiting, and conversation context assembly. Once the request was validated, the query was converted into an embedding vector using an embedding model. That vector was then used to retrieve semantically relevant chunks from a vector database before the final context was passed into the language model for response generation.

The simplified request flow looked like this:

* User sends a query
* Query is embedded into a vector
* [Vector search](https://thenewstack.io/beyond-vector-search-the-move-to-tensor-based-retrieval/) retrieves relevant documents
* Retrieved context is assembled into a prompt
* LLM generates the final response
* Response is optionally cached

On a small scale, this worked perfectly. The real headaches started when traffic scaled and we noticed the exact same database queries and heavy inference workloads hitting us thousands of times an hour.

## One of the first optimizations we introduced was Redis-based caching

The initial idea was straightforward: avoid recomputing expensive operations for repeated requests. We started by caching exact prompt-response pairs, embedding results, and frequently accessed retrieval outputs.

Because Redis operates entirely in memory, lookup times were rapid, immediately reducing pressure on both the vector database and the LLM layer.

A simplified Redis caching flow looked like this:

```

const cacheKey = `llm_cache:${hash(userQuery)}`;

try {
const cachedResponse = await redis.get(cacheKey);
if (cachedResponse) {
return JSON.parse(cachedResponse);
}
} catch (cacheError) {
console.warn("Cache read failed, falling back to LLM:", cacheError);
}

const embedding = await generateEmbedding(userQuery);
const documents = await vectorSearch(embedding);
const response = await generateLLMResponse(documents);

try {
await redis.set(cacheKey, JSON.stringify(response), "EX", 3600);
} catch (cacheError) {
console.error("Failed to write response to cache:", cacheError);
}

return response;

```

The immediate results were excellent: near-instant response times for duplicate prompts, reduced API costs, and stable infrastructure that handled high traffic without requiring aggressive LLM scale-out. If a query matched an existing keyword-for-word, we skipped the entire expensive AI pipeline and served the answer straight from memory.

## Why Redis looked like the perfect solution

Unlike vector indexes, Redis gave us clean, predictable metrics for memory usage, throughput, and latency characteristics under load. There were no similarity thresholds to configure, no ANN indexes to optimize, and no recall-versus-latency trade-offs to worry about. A cache key either existed or it didn’t. That predictability made the system easier to reason about during incidents and easier to scale under pressure.

We initially used Redis across multiple layers of the AI pipeline, including prompt-response caching, embedding caching, session state storage, rate limiting, temporary conversation memory, and caching frequently accessed retrieval outputs.

```

const cacheKey = `prompt:${hash(query)}`;
try {
const cached = await redis.get(cacheKey);
if (cached) {
return JSON.parse(cached);
}
} catch (cacheError) {
console.warn("Cache read or parse failed, bypassing cache:", cacheError);
}

```

We also started caching embeddings because generating embeddings became surprisingly expensive at scale. Even though embeddings were much cheaper than LLM inference, generating them repeatedly for popular queries still consumed a noticeable amount of compute resources.

```

const embeddingKey = `embedding:${hash(query)}`;
let embedding;

try {
const cachedEmbedding = await redis.get(embeddingKey);
if (cachedEmbedding) {
embedding = JSON.parse(cachedEmbedding);
}
} catch (cacheError) {
console.warn("Redis read failed, proceeding to generate new embedding:", cacheError);
}

if (!embedding) {
embedding = await createEmbedding(query);

try {
await redis.set(
embeddingKey,
JSON.stringify(embedding),
"EX",
86400
);
} catch (cacheError) {
console.error("Failed to write embedding to Redis:", cacheError);
}
}

```

As an added bonus, scaling horizontally with Redis clusters is a familiar process for most infrastructure teams. For a while, Redis significantly reduced both latency and infrastructure costs. Cache hit rates were high, GPU workloads dropped, and the vector database handled far fewer retrieval requests.

The architecture looked efficient enough that we initially believed Redis alone would resolve most of our AI caching challenges. That belief did not survive real semantic workloads for very long.

The problem was that AI workloads rarely behave like traditional web workloads for long. Users almost never ask the same question repeatedly. Instead, they ask semantically similar questions with slightly different wording, tone, or context. From Redis’ perspective, these were entirely different cache keys, even when the retrieval results and final answers were nearly identical. That limitation eventually pushed us toward semantic caching using vector databases.

## Why we moved toward vector DB caching

Unlike Redis, vector databases do not rely on exact string matching. Instead, they compare numerical embeddings that represent the semantic meaning of text. This made it possible to retrieve cached results for prompts that were semantically similar, even when the wording was completely different.

Instead of hashing the raw prompt into a Redis key, we would generate an embedding for the incoming query and search for previously cached embeddings that were semantically close enough to reuse. If a sufficiently similar match existed, the system could skip large parts of the retrieval or inference pipeline.

The caching flow looked like this:

```

const embeddingKey = `embedding:${hash(query.toLowerCase().trim())}`;
const cachedString = await redis.get(embeddingKey);
let embedding;

if (cachedString) {
// Parse the stored string back into a workable array
embedding = JSON.parse(cachedString);
} else {
embedding = await createEmbedding(query);
await redis.set(
embeddingKey,
JSON.stringify(embedding),
"EX",
86400
);
}

```

This approach immediately solved one of Redis’ biggest weaknesses: wording variation. Queries that previously produced separate Redis entries could now reuse cached retrievals or responses if their embeddings were sufficiently close in vector space. This meant significantly higher cache hit rates for real conversational workloads.

The payoff from semantic caching was immediate, especially for conversational traffic where users ask the same question ten different ways. A string-matching setup like Redis misses completely if a user changes a single word. With a vector database, prompts like “How can I speed up vector search?” and “Best ways to optimize semantic retrieval performance?” resolve to the same underlying intent, allowing us to recycle the same cached response, context chunks, or embeddings seamlessly.

We also saw potential cost reductions beyond response caching alone. Embedding reuse became more effective because semantically similar prompts often generated nearly identical retrieval behavior. Retrieval outputs themselves could also be reused across related queries, reducing load on the vector search layer and decreasing the number of repeated context assembly operations.

Semantic caching appeared especially promising for RAG systems, AI copilots, internal knowledge assistants, search-heavy AI applications, and conversational agents with repeated intent patterns because these workloads frequently involve semantically similar queries that can benefit from intelligent cache reuse.

At first, the results were promising. Semantic caching immediately optimized our hit rates and reduced redundant retrieval calls across varied prompts. However, scaling this layout under full production traffic quickly exposed a brand new category of latency and performance constraints.

## Where vector DBs started breaking

The advantages of semantic caching were real, but so were the new problems it introduced. As traffic increased and vector indexes grew larger, the system began to develop issues that were harder to predict and debug than the Redis problems we had dealt with earlier.

The first major issue was latency instability. Unlike Redis, which provided highly predictable exact-match lookups, vector similarity search performance degraded unpredictably under load, query complexity, metadata filters, and concurrency levels. Under heavy workloads, some semantic cache lookups became significantly slower than expected, especially when the system searched across millions of embeddings.

A typical semantic lookup now involves multiple operations:

* Generating an embedding
* Running ANN similarity search
* Evaluating similarity thresholds
* Retrieving metadata and cached responses

Even before LLM inference occurred, the cache layer itself was becoming computationally expensive.

False-positive matches also became a serious problem. Two prompts could appear semantically similar in vector space yet require very different responses in practice. This occasionally caused cached responses to be reused in contexts where they were only partially relevant or subtly incorrect. For context, a query about optimizing vector search for low-latency chat applications might accidentally reuse cached retrievals intended for large-scale offline analytics systems simply because the embeddings appeared highly similar.

The hardest part was tuning similarity thresholds correctly.

```

const SIMILARITY_THRESHOLD = parseFloat(process.env.CACHE_SIMILARITY_THRESHOLD || "0.93");
const cacheKey = `llm_cache:${hash(userQuery)}`;

try {
const cachedResponse = await redis.get(cacheKey);
if (cachedResponse) {
return JSON.parse(cachedResponse);
}
} catch (cacheError) {
console.warn("Cache read failed, falling back to semantic search:", cacheError);
}

const embedding = await createEmbedding(userQuery);

const result = await vectorIndex.query({
vector: embedding,
topK: 3,
});

if (result.matches &amp;&amp; result.matches.length > 0) {
const bestMatch = result.matches[0];

if (bestMatch.score >= SIMILARITY_THRESHOLD) {
return bestMatch.metadata?.cachedResponse ?? bestMatch.cachedResponse;
}
}

const response = await generateLLMResponse(result.matches);

try {
await redis.set(cacheKey, JSON.stringify(response), "EX", 3600);
} catch (cacheError) {
console.error("Failed to write response to cache:", cacheError);
}

return response;

```

Another benefit was the reduction of repeated embedding and retrieval workloads. Since semantically related prompts often produced highly similar retrieval patterns, the infrastructure handled fewer redundant searches overall. This became especially valuable under high concurrency, where reducing repeated vector searches significantly lowered infrastructure load.

Semantic caching also improved the user experience in some scenarios. Similar prompts tended to receive more consistent responses because they reused previously validated retrieval contexts rather than generating entirely fresh retrieval paths every time.

For a while, vector database caching looked like the clear evolution of AI caching systems. The architecture appeared smarter, more adaptive, and better aligned with how humans naturally communicate.

But the more we pushed into production, the more we started discovering the hidden costs of semantic similarity itself. Finding a stable similarity threshold proved incredibly fragile. Low thresholds maximized cache hits at the expense of precision, while tight thresholds neutralized false positives but destroyed cache utility. This sensitivity turned threshold management into a [major operational bottleneck](https://thenewstack.io/how-to-find-and-solve-engineering-bottlenecks/), directly impacting downstream inference costs and system accuracy.

```

if (match.score >= 0.90) {
return match.cachedResponse;
}

```

Embedding drift introduced another long-term challenge. As embedding models changed over time, older cached vectors gradually became less compatible with newer embeddings. Semantic relationships shifted, reducing retrieval accuracy and forcing expensive re-indexing operations across the cache layer.

Operational complexity also increased substantially compared to Redis. Maintaining vector indexes required tuning ANN algorithms, balancing shards, handling index rebuilds, and monitoring recall accuracy as workloads changed. The infrastructure became harder to reason about because semantic correctness was no longer deterministic.

We also discovered that semantic caching consumed resources differently than traditional caching systems. Even cache hits still required embedding generation and vector search operations before matches could be identified. Unlike Redis, where a successful lookup was nearly free, semantic cache hits still carried noticeable computational overhead.

In production, the system began to reveal an uncomfortable reality. Semantic caching solved the exact-match problem, but it introduced an entirely new category of latency, accuracy, and operational challenges that traditional caching systems rarely encounter.

## Redis vs Vector DB: The real production trade-offs

Once both systems had been running in production long enough, the comparison between Redis and vector database caching became much clearer. Neither technology was universally better. Each one is optimized for a completely different type of workload, and the real trade-offs only become visible under large-scale AI traffic.

Redis dominated in raw speed and predictability. Exact-match lookups were extremely fast, operationally simple, and relatively easy to scale. If a query had already been seen before in the exact same form, Redis almost always delivered the lowest possible latency. Cache hits are often completed in milliseconds with minimal computational overhead.

Operationally, Redis was also easier to maintain. Debugging cache misses was straightforward because the behavior was deterministic. A cache key either existed or it did not. Infrastructure teams already understood replication, sharding, persistence, and monitoring strategies because Redis has been battle-tested for years across traditional distributed systems.

Its weakness was semantic rigidity. Humans don’t write identical strings. If someone adds a typo or changes a single word, Redis drops the ball and treats it as a brand-new cache entry. Vector databases fixed that exact-match rigidity by letting us cache responses based on meaning. On paper, it’s a dream for RAG pipelines and copilots. In production, though, you realize you’re just paying a different tax. Vector lookups have actual computational weight. Unlike Redis, where an O(1) RAM read takes single-digit milliseconds, checking a semantic cache means you’re stuck waiting on an embedding model call and a graph traversal step just to see if you have a match.

> “Unlike Redis, where an O(1) RAM read takes single-digit milliseconds, checking a semantic cache means you’re stuck waiting on an embedding model call and a graph traversal step.”

Worse, you lose determinism. With Redis, a key is either there or it isn’t. A vector cache forces you to manage a fuzzy threshold where the system occasionally treats two completely distinct user intents as “similar enough,” blindly serving bad data. Our infrastructure bill transformed too: we went from a system that was heavily memory-bound on RAM to one that aggressively chewed through compute just to optimize and search indexes.

## The hybrid architecture that finally worked

After months of experimenting with both systems independently, we eventually stopped trying to choose between them and began using Redis and vector databases as complementary layers rather than competing technologies.

The final architecture used a multi-layer caching strategy. Redis handled ultra-fast exact-match caching for highly repetitive requests, session state, temporary conversation memory, and hot-path retrievals. The vector database handled semantic reuse for prompts that were conceptually similar but not textually identical.

The request flow became layered. The system first checked Redis for an exact-match cache hit, and if that failed, it moved on to a [semantic vector cache](https://thenewstack.io/redis-launches-vector-sets-and-a-new-tool-for-semantic-caching-of-llm-responses/) lookup. If the semantic lookup also missed, the request proceeded through the full pipeline of retrieval and inference, after which the resulting output was stored back into both cache layers where appropriate.

A simplified hybrid flow looked like this:

```

try {
const exactCached = await redis.get(cacheKey);
if (exactCached) {
return JSON.parse(exactCached);
}
} catch (cacheError) {
console.warn("Redis read failed, proceeding to semantic search:", cacheError);
}

const embedding = await createEmbedding(query);
const semanticMatch = await vectorIndex.query({
vector: embedding,
topK: 1,
});
const SIMILARITY_THRESHOLD = parseFloat(process.env.SEMANTIC_CACHE_THRESHOLD || "0.93");

const bestMatch = semanticMatch.matches[0];

if (bestMatch?.score >= SIMILARITY_THRESHOLD) {
  return bestMatch.metadata?.response;
}


const response = await generateLLMResponse(query);
try {
await redis.set(cacheKey, JSON.stringify(response), "EX", 3600);
} catch (cacheError) {
console.error("Failed to write exact match to Redis:", cacheError);
}
await vectorIndex.upsert([
{
id: crypto.randomUUID(), // Most vector DBs require a unique ID
vector: embedding,
metadata: {
response,
},
},
]);
} catch (vectorError) {
console.error("Failed to upsert semantic cache to vector index:", vectorError);
}
return response;

```

This hybrid approach solved several problems simultaneously. Redis continued to handle the lowest-latency exact cache hits, protecting the infrastructure during traffic spikes and repetitive workloads. The vector cache improved semantic reuse without forcing every request through expensive ANN searches unnecessarily.

The layered design also improved reliability. Even if vector search latency increased temporarily, Redis still absorbed a large share of repeated traffic. Likewise, if exact-match cache hit rates dropped, semantic caching still recovered some of the lost reuse efficiency.

The architecture became easier to optimize because each layer had a clearly defined responsibility: Redis optimized speed, the vector database optimized semantic understanding, and the inference layer handled only true cache misses.

Over time, we also became more selective about what entered the semantic cache. Not every response benefited from semantic reuse, especially highly dynamic or context-sensitive outputs. Restricting semantic caching to stable retrieval patterns improved both precision and infrastructure efficiency.

## Production lessons we learned

The biggest lesson was that AI caching behaves fundamentally differently from traditional application caching. Human language introduces semantic variation that exact-match systems struggle with, but semantic systems introduce probabilistic complexity that exact-match systems avoid.

In production, we learned that Redis and vector databases are not competing solutions but tools optimized for different layers of AI caching. Redis excels at fast, deterministic exact-match retrievals, while vector databases are better suited for semantic reuse in variable, intent-driven workloads. The most stable systems are not built on choosing one over the other, but on combining both in a layered architecture that matches the nature of AI traffic.

Ultimately, there is no “best” caching system for AI workloads. Redis and vector databases solve fundamentally different problems, and treating them as interchangeable leads to architectural inefficiencies at scale.

Redis delivers speed and predictability for exact-match scenarios, while vector DB caching enables semantic reuse where user intent matters more than exact wording. In real production systems, the most reliable approach is not replacement but combination.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/05/9b23d2ba-cropped-9585988f-zzwia-raymond.jpeg)

Zziwa Raymond Ian is a full-stack engineer and a member of the Andela Talent Network, a private global marketplace for digital talent. Specializing in Next.js, React, JavaScript, TypeScript, NestJs and others, he has developed a deep holistic understanding of both...

Read more from Zziwa Raymond Ian](https://thenewstack.io/author/zziwa-raymond/)