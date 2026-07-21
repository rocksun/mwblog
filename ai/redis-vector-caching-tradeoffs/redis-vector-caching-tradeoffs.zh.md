缓存是现代 AI 系统中最关键的优化手段之一，这一点在大多数团队意识到之前就已经确立了。早期的检索增强生成 (RAG) 流水线、AI 辅助编程工具和语义搜索平台，在处理小型数据集和有限流量时往往表现完美。

但一旦进入真正的生产工作负载，长尾延迟、不断增加的基础设施成本以及重复的检索操作便开始变得不容忽视。

我们的第一直觉是这很容易解决。Redis 可以毫不费力地搞定。

它速度快、简单、经过充分测试，并且在高性能系统的会话存储、API 缓存和速率限制方面已深受信赖。精确匹配的 Prompt 缓存显著缩短了响应时间，使得许多重复的 AI 请求可以在毫秒级内完成，而无需再次触及昂贵的检索或推理层。在一段时间内，Redis 证明了我们的选择是正确的，解决了我们几乎所有的性能问题。

直到我们的工作负载发生了变化。

当你的基础设施变得具有“语义”能力时，传统的字符串匹配缓存就会失效。人类语言的多样性意味着两个用户会用完全不同的措辞询问完全相同的信息。

> “当你的基础设施变得具有‘语义’能力时，传统的字符串匹配缓存就会失效。”

由于 Redis 依赖精确的字符串匹配，它完全忽略了这些联系，为相同的意图创建了重复且碎片化的缓存条目。没过多久，我们的命中率就直线下滑，内存利用率飙升，而且我们还背负了高昂的云账单，仅仅是因为存储了冗余的数据上下文。

就在那时，通过向量数据库实现的语义缓存开始显得具有吸引力。从理论上讲，这似乎是完美的架构进化：基于向量距离数学进行查询匹配，从而使不同的 Prompt 可以复用旧的嵌入（embedding）、上下文块或过去的 LLM 答案。

当然，生产环境的现实远比炒作中描述的混乱。向量数据库缓存引入了一系列自身的问题：延迟峰值、误报匹配、嵌入漂移（embedding drift）、操作复杂性以及关于相似度阈值的棘手调整决策。在某些工作负载中，语义缓存显著提高了性能；而在另一些工作负载中，它反而比它本应取代的 Redis 配置更慢、更昂贵。

> “当然，生产环境的现实远比炒作中描述的混乱。”

我们最终认识到，Redis 和向量数据库解决的是截然不同的缓存问题。前者优化的是精确检索速度，后者优化的是语义复用。将它们视为可互换的技术导致了架构上的错误，这些错误只有在真实的生产流量下才会显现出来。

## 我们最初采用的 AI 架构

在缓存问题出现之前，我们的 AI 技术栈对于现代检索增强生成 (RAG) 系统来说非常标准。流水线围绕三个主要阶段设计：嵌入生成、文档检索和 LLM 推理。

用户查询首先进入 API 层，预处理在这里处理标准化、身份验证、速率限制和对话上下文组装。一旦请求通过验证，查询就会使用嵌入模型转换为嵌入向量。随后，该向量被用于从向量数据库中检索语义相关的块，最后将上下文传递给语言模型以生成响应。

简化的请求流程如下：

* 用户发送查询
* 查询被嵌入为向量
* [向量搜索](https://thenewstack.io/beyond-vector-search-the-move-to-tensor-based-retrieval/)检索相关文档
* 检索到的上下文被组合成一个 Prompt
* LLM 生成最终响应
* 响应可选择性地缓存

在小规模场景下，这运行完美。真正的头疼问题出现在流量扩大时，我们注意到完全相同的数据库查询和繁重的推理工作负载每小时冲击我们数千次。

## 我们引入的首批优化措施之一是基于 Redis 的缓存

最初的思路很直接：避免对重复请求进行昂贵的重复计算。我们开始缓存精确的 Prompt-响应对、嵌入结果以及频繁访问的检索输出。

由于 Redis 完全在内存中运行，查找时间非常快，立即减轻了向量数据库和 LLM 层的压力。

一个简化的 Redis 缓存流程如下：

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

直接效果非常出色：对重复 Prompt 的响应近乎瞬时，降低了 API 成本，且基础设施稳定，无需激进地扩容 LLM 即可处理高流量。如果查询与现有查询逐字匹配，我们就会跳过整个昂贵的 AI 流水线，直接从内存中提供答案。

## 为何 Redis 看似是完美的解决方案

与向量索引不同，Redis 为我们在负载下的内存使用、吞吐量和延迟特性提供了清晰、可预测的指标。没有需要配置的相似度阈值，没有需要优化的 ANN 索引，也不必担心召回率与延迟之间的权衡。缓存键要么存在，要么不存在。这种可预测性使得系统在发生事故时更容易进行诊断，并在压力下更容易扩展。

我们最初在 AI 流水线的多个层级使用了 Redis，包括 Prompt-响应缓存、嵌入缓存、会话状态存储、速率限制、临时对话记忆以及缓存频繁访问的检索输出。

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

我们还开始缓存嵌入，因为在大规模场景下生成嵌入变得出奇地昂贵。尽管嵌入比 LLM 推理便宜得多，但对流行查询重复生成它们仍然消耗了可观的计算资源。

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

作为额外的好处，通过 Redis 集群进行水平扩展对于大多数基础设施团队来说是一个熟悉的过程。在一段时间内，Redis 显著降低了延迟和基础设施成本。缓存命中率很高，GPU 工作负载下降，向量数据库处理的检索请求也少了很多。

架构看起来足够高效，以至于我们最初认为仅凭 Redis 就能解决我们大部分的 AI 缓存挑战。但这种信念在真实的语义工作负载面前并没有坚持多久。

问题在于 AI 工作负载很少能长时间表现得像传统的 Web 工作负载。用户几乎从不重复提问同一个问题。相反，他们会用略有不同的措辞、语气或上下文询问语义相似的问题。从 Redis 的角度来看，即使检索结果和最终答案几乎完全相同，它们也是完全不同的缓存键。这种局限性最终推动我们转向使用向量数据库进行语义缓存。

## 为何我们转向向量数据库缓存

与 Redis 不同，向量数据库不依赖精确的字符串匹配。相反，它们比较代表文本语义含义的数值嵌入。这使得我们可以为语义上相似但在措辞上完全不同的 Prompt 检索缓存结果。

我们不再将原始 Prompt 哈希成 Redis 键，而是为传入的查询生成一个嵌入，并搜索之前缓存的、在语义上足够接近可供复用的嵌入。如果存在足够相似的匹配，系统就可以跳过检索或推理流水线的大部分内容。

缓存流程如下：

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

这种方法立即解决了 Redis 最大的弱点之一：措辞变化。之前会产生不同 Redis 条目的查询，如果它们的嵌入在向量空间中足够接近，现在就可以复用缓存的检索结果或响应。这意味着对于真实的对话工作负载，缓存命中率显著提高。

语义缓存带来的收益是立竿见影的，尤其是对于用户以十种不同方式询问同一个问题的对话式流量。像 Redis 这样的字符串匹配设置，如果用户修改了一个单词，就会完全丢失。使用向量数据库，像“如何加快向量搜索？”和“优化语义检索性能的最佳方法是什么？”这样的 Prompt 会被解析为相同的底层意图，使我们能够无缝地循环利用相同的缓存响应、上下文块或嵌入。

我们也看到了除了响应缓存之外的潜在成本降低。嵌入复用变得更加有效，因为语义相似的 Prompt 通常会生成几乎相同的检索行为。检索输出本身也可以在相关查询之间复用，从而降低向量搜索层的负载，减少重复上下文组装操作的数量。

对于 RAG 系统、AI 辅助编程工具、内部知识助手、搜索密集型 AI 应用以及具有重复意图模式的对话式代理，语义缓存显得尤为有前景，因为这些工作负载通常涉及可以从智能缓存复用中受益的语义相似查询。

起初，结果令人振奋。语义缓存立即优化了我们的命中率，并减少了跨不同 Prompt 的冗余检索调用。然而，在全量生产流量下扩展这种布局，很快就暴露出一类全新的延迟和性能限制。

## 向量数据库开始出现问题的环节

语义缓存的优势是真实的，但它引入的新问题也是如此。随着流量增加和向量索引变大，系统开始出现比我们之前处理 Redis 问题时更难预测和调试的问题。

第一个主要问题是延迟不稳定。与提供高度可预测的精确匹配查找的 Redis 不同，向量相似度搜索的性能在负载、查询复杂性、元数据过滤和并发级别下会不可预测地退化。在繁重的工作负载下，一些语义缓存查找变得比预期慢得多，尤其是在系统搜索数百万个嵌入时。

一个典型的语义查找现在涉及多个操作：

* 生成嵌入
* 运行 ANN 相似度搜索
* 评估相似度阈值
* 检索元数据和缓存响应

甚至在 LLM 推理发生之前，缓存层本身就已经变得计算昂贵了。

误报匹配也成为了一个严重的问题。两个 Prompt 在向量空间中可能看起来语义相似，但在实践中却需要截然不同的响应。这偶尔会导致缓存的响应被复用在仅部分相关或微妙错误的环境中。例如，一个关于为低延迟聊天应用优化向量搜索的查询，可能会意外复用旨在用于大规模离线分析系统的缓存检索，仅仅因为它们的嵌入看起来非常相似。

最困难的部分是正确调整相似度阈值。

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

const embedding = await createEmbedding(query);

const result = await vectorIndex.query({
vector: embedding,
topK: 3,
});

if (result.matches && result.matches.length > 0) {
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

另一个好处是减少了重复的嵌入和检索工作负载。由于语义相关的 Prompt 通常产生高度相似的检索模式，基础设施处理的冗余搜索总体上变少了。在高并发环境下，这一点变得尤为重要，因为减少重复的向量搜索显著降低了基础设施负载。

语义缓存还在某些场景下改善了用户体验。相似的 Prompt 倾向于获得更一致的响应，因为它们复用了之前验证过的检索上下文，而不是每次都生成全新的检索路径。

在一段时间内，向量数据库缓存看起来是 AI 缓存系统的清晰进化方向。该架构看起来更智能、更具适应性，并且更符合人类自然交流的方式。

但我们越深入生产环境，就越开始发现语义相似性本身隐藏的成本。找到一个稳定的相似度阈值变得极其脆弱。低阈值以牺牲精度为代价最大化了缓存命中率，而严格的阈值抑制了误报，但却破坏了缓存的实用性。这种敏感性使阈值管理成为了一个[重大的工程瓶颈](https://thenewstack.io/how-to-find-and-solve-engineering-bottlenecks/)，直接影响下游推理成本和系统准确性。

```

if (match.score >= 0.90) {
return match.cachedResponse;
}

```

嵌入漂移带来了另一个长期挑战。随着嵌入模型随时间变化，较旧的缓存向量逐渐变得与较新的嵌入不兼容。语义关系发生了变化，降低了检索准确性，并迫使缓存层进行昂贵的重新索引操作。

与 Redis 相比，操作复杂性也显著增加。维护向量索引需要调整 ANN 算法、平衡分片、处理索引重建，以及随着工作负载变化监控召回准确性。基础设施变得更难理解，因为语义正确性不再是确定性的。

我们还发现，语义缓存消耗资源的方式与传统缓存系统不同。即使是缓存命中，在识别出匹配项之前也需要嵌入生成和向量搜索操作。与 Redis 成功查找几乎是免费的不同，语义缓存命中仍然带有明显的计算开销。

在生产中，系统开始揭示一个令人不安的现实。语义缓存解决了精确匹配问题，但它引入了传统缓存系统很少遇到的一类全新的延迟、准确性和操作挑战。

## Redis 与向量数据库：真实的生产权衡

一旦这两个系统在生产环境中运行了足够长的时间，Redis 和向量数据库缓存之间的对比就变得清晰多了。没有哪种技术是普遍更好的。每一种技术都针对完全不同的工作负载类型进行了优化，真正的权衡只有在大规模 AI 流量下才会显现出来。

Redis 在纯速度和可预测性方面占主导地位。精确匹配查找速度极快，操作简单，且相对容易扩展。如果以前以完全相同的形式见过查询，Redis 几乎总是能提供最低的延迟。缓存命中通常在毫秒级完成，且计算开销极小。

在操作上，Redis 也更容易维护。调试缓存未命中很直观，因为其行为是确定性的。缓存键要么存在，要么不存在。基础设施团队已经理解了复制、分片、持久性和监控策略，因为 Redis 已经在传统分布式系统中经过了多年的实战考验。

它的弱点是语义僵化。人类不会写出完全相同的字符串。如果有人添加了一个错别字或更改了一个单词，Redis 就会失灵，并将其视为全新的缓存条目。向量数据库通过让我们根据含义缓存响应来修复了这种精确匹配的僵化性。从理论上讲，这对 RAG 流水线和辅助编程工具来说是一个梦想。然而在生产中，你会意识到你只是支付了不同的税。向量查找有实际的计算权重。不像 Redis 的 O(1) RAM 读取只需个位数毫秒，检查语义缓存意味着你必须等待嵌入模型调用和图遍历步骤，才能看到是否有匹配项。

> “不像 Redis 的 O(1) RAM 读取只需个位数毫秒，检查语义缓存意味着你必须等待嵌入模型调用和图遍历步骤。”

更糟糕的是，你失去了确定性。使用 Redis，键要么在，要么不在。向量缓存迫使你管理一个模糊的阈值，系统偶尔会将两个完全不同的用户意图视为“足够相似”，盲目地提供错误的数据。我们的基础设施账单也发生了改变：我们从一个高度依赖 RAM 内存的系统，变成了一个为了优化和搜索索引而积极消耗计算资源的系统。

## 最终生效的混合架构

在分别尝试了这两个系统几个月后，我们最终不再试图在它们之间做出选择，而是开始将 Redis 和向量数据库作为互补层，而不是竞争技术。

最终的架构采用了一种多层缓存策略。Redis 处理高度重复请求、会话状态、临时对话记忆和热路径检索的超快速精确匹配缓存。向量数据库处理在概念上相似但文本上不相同的 Prompt 的语义复用。

请求流程变得分层。系统首先检查 Redis 是否有精确匹配的缓存命中，如果失败，则进入[语义向量缓存](https://thenewstack.io/redis-launches-vector-sets-and-a-new-tool-for-semantic-caching-of-llm-responses/)查找。如果语义查找也未命中，请求将通过检索和推理的完整流水线，之后将结果输出在适当的情况下存回两个缓存层。

一个简化的混合流程如下：

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

这种混合方法同时解决了几个问题。Redis 继续处理最低延迟的精确缓存命中，在流量高峰和重复工作负载期间保护基础设施。向量缓存改善了语义复用，而无需强制每个请求都经过不必要的昂贵 ANN 搜索。

分层设计也提高了可靠性。即使向量搜索延迟暂时增加，Redis 仍然承担了很大一部分重复流量。同样，如果精确匹配缓存命中率下降，语义缓存仍然能挽回一些丢失的复用效率。

该架构变得更容易优化，因为每一层都有明确的职责：Redis 优化速度，向量数据库优化语义理解，推理层仅处理真正的缓存未命中。

随着时间的推移，我们在进入语义缓存的内容上也变得更加有选择性。并非每个响应都能从语义复用中受益，特别是高度动态或上下文敏感的输出。将语义缓存限制为稳定的检索模式提高了精度和基础设施效率。

## 我们学到的生产经验

最大的教训是 AI 缓存的行为与传统应用缓存有着本质上的不同。人类语言引入了精确匹配系统难以处理的语义变化，但语义系统引入了精确匹配系统可以避免的概率复杂性。

在生产中，我们了解到 Redis 和向量数据库不是竞争的解决方案，而是针对 AI 缓存不同层级优化的工具。Redis 擅长快速、确定性的精确匹配检索，而向量数据库更适合变量驱动、基于意图的工作负载中的语义复用。最稳定的系统不是建立在二选一的基础上，而是建立在将两者结合在一个与 AI 流量性质相匹配的分层架构中。

归根结底，对于 AI 工作负载没有“最好”的缓存系统。Redis 和向量数据库解决的是截然不同的问题，将它们视为可互换的会导致大规模下的架构低效。

Redis 为精确匹配场景提供了速度和可预测性，而向量数据库缓存则在用户意图比确切措辞更重要的场景下实现了语义复用。在真正的生产系统中，最可靠的方法不是替代，而是组合。