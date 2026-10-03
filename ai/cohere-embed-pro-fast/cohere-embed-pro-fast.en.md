**Cohere released Embed 5 on Wednesday**, giving teams the option to index data with Embed 5 Pro and query those same vectors with the faster, cheaper Embed 5 Fast without creating a second index.

The company recommends using Pro for indexing and Fast for queries, particularly in RAG and agent workloads where [latency compounds](https://thenewstack.io/agentic-ai-latency-infrastructure/) as the same data is searched repeatedly.

There is a tradeoff in retrieval quality, although Cohere’s testing suggests it is fairly small. Across 40 datasets covering text, images, fused documents, and parsed documents, Fast queries against a Pro index scored 98.4 relative to a Pro-to-Pro baseline of 100. Using Fast for both indexing and queries dropped that score to 96.6. Cohere says none of the individual datasets showed a major drop when Pro and Fast were used together.

## One embedding space, two models

Because Pro and Fast share an embedding space, teams can switch between them without re-embedding the corpus. Both produce compatible vectors at the same dimensions, and Cohere says teams can still mix the two when using Matryoshka truncation or int8 quantization.

> Because Pro and Fast share an embedding space, teams can switch between them without re-embedding the corpus.

Pro costs $0.12 per million tokens, while Fast costs $0.08 and delivers an average of 2.4 times the document throughput in Cohere’s tests. For RAG systems that ingest documents less often than they search them, Pro can handle documents as they enter the index while Fast handles the much heavier query traffic.

## Shrinking vectors with Matryoshka

Both models support six vector dimensions from 256 to 2,048, with float32, int8 and binary formats. The storage difference becomes significant at scale, particularly for teams already [rethinking where their vectors live](https://thenewstack.io/spark-4-2-ai-workloads/).

Cohere puts a 2,048-dimensional float32 vector at 8 KB, or roughly 819 GB for 100 million chunks. A 1,024-dimensional int8 vector cuts that to about 102 GB, while a 256-dimensional binary vector brings the same corpus down to roughly 3.2 GB.

For most deployments, Cohere recommends 1,024-dimensional int8, which reduces memory and storage while retaining close to full-precision retrieval quality. Binary representations offer heavier compression with some accuracy loss and are better suited to an initial retrieval stage before higher-precision reranking.

> Both models support six vector dimensions from 256 to 2,048, with float32, int8 and binary formats.

## Retrieval beyond plain text

Embed 5 supports text, images, and fused text-image inputs across more than 100 languages, with a 128K-token context window. It can embed page images directly or combine image and text inputs in a single vector.

Cohere [reports](https://docs.cohere.com/changelog/embed-v5) an average score of 82.3 for Pro on its five-dataset fused text-image evaluation, compared with 81.2 for Fast and 61.3 for Google’s Gemini Embedding 2. On its parsed-PDF evaluation, Pro scored 84.8, followed by Voyage 4 Large at 83.6, Fast at 83.4, and Gemini Embedding 2 at 80.8.

On ViDoRe V3, which Cohere evaluated using parsed text outputs curated by the benchmark’s authors rather than page images, Pro averaged 85.8 and Fast 84.5, compared with 83.7 for Voyage 4 Large, 83.2 for Gemini Embedding 2 and 77 for Cohere’s previous Embed 4.

Cohere’s multilingual results are less one-sided, which stands out given the company’s [recent push into machine translation](https://thenewstack.io/cohere-north-translate-sovereignty/). Pro leads its five-language European average with a score of 77, against 76 for Voyage 4 Large and 73 for Gemini Embedding 2, but trails Gemini Embedding 2 on nine of the tests.

## Reading the benchmark fine print

The benchmark results require some context because Embed 5 is Cohere’s first model family evaluated with RCP-nDCG@10, which uses query-specific relevance criteria rather than fixed relevance labels.

Cohere says this approach can catch relevant results missed by the original benchmark labels, but RCP-nDCG@10 measures reranking over a fixed candidate set rather than first-stage retrieval from the full corpus.

First-stage retrieval is evaluated separately using standard nDCG and Recall, while the fused text-image, page-image, and cross-model tests use standard nDCG@10, so the reported scores aren’t directly comparable across evaluations.

## Separating indexing from serving

The more consequential change in Embed 5 is the ability to treat indexing and serving as [separate infrastructure decisions](https://thenewstack.io/ai-agent-retrieval-infrastructure/). The same corpus can be indexed for retrieval quality while the query path is optimized for throughput and latency, without maintaining two data representations.

Cohere’s 98.4 score suggests the Pro-to-Fast setup sacrifices relatively little retrieval quality in its tests, although that figure averages across Cohere’s own evaluation suite. Production RAG and agent systems will still need to benchmark Pro-to-Fast against Pro-to-Pro on their own corpus and query distribution, particularly when retrieval errors can carry through multiple steps of an agent workflow.

Embed 5 Pro and Fast are available through Cohere’s API and Model Vault, Microsoft Foundry, and Amazon SageMaker, with private VPC and on-premises deployment supported through vLLM.

> Production RAG and agent systems will still need to benchmark Pro-to-Fast against Pro-to-Pro on their own corpus and query distribution, particularly when retrieval errors can carry through multiple steps of an agent workflow.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)