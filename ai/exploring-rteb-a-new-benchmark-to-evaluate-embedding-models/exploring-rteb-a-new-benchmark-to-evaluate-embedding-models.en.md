With the rise of large language models (LLMs), our exposure to benchmarks — not to mention the sheer number and variety of them — has surged. Given the opaque nature of LLMs and other AI systems, benchmarks have become the standard way to compare their performance.

These are standardized tests or data sets that evaluate how well models perform on specific tasks. As a result, every new model release brings updated leaderboard results, and [embedding models](https://thenewstack.io/the-secret-sauce-for-vector-search-training-embedding-models/) are no exception.

Today, embeddings [power the search layer](https://thenewstack.io/combining-the-power-of-text-based-keyword-and-vector-search/) of AI applications, yet choosing the right model remains difficult. The [Massive Text Embedding Benchmark](https://huggingface.co/spaces/mteb/leaderboard) (MTEB), released in 2022, has become the standard for evaluating embeddings, but it’s a broad, general-purpose benchmark covering many tasks unrelated to retrieval.

MTEB also uses public data sets, and while this promotes transparency, it can lead to overfitting — models being trained on evaluation data. As a result, MTEB scores don’t always reflect real-world retrieval accuracy.

Retrieval Embedding Benchmark (RTEB), [a new retrieval-first benchmark](https://huggingface.co/blog/rteb), addresses these limitations by focusing on real-world retrieval tasks and using both open and private data sets to better reflect true generalization across new unseen data. Let’s explore RTEB, its focus, data sets and how to use it.

## How Are Embeddings Benchmarked?

Before diving into RTEB, it’s important to understand benchmarks and why they matter. Because AI models like embedding models are black boxes, assessing their quality is challenging. A benchmark is a standardized set of tasks used to evaluate those models. Benchmarks help measure performance, identify areas for improvement and compare results against a standard baseline, other models or past performance.

[![Example RTEB results of benchmarked embedding models.](https://cdn.thenewstack.io/media/2025/11/5c8a365b-image3.png)](https://cdn.thenewstack.io/media/2025/11/5c8a365b-image3.png)

Figure 1. Example RTEB results of benchmarked embedding models.

Building effective benchmarks is not trivial. Data sets and task definitions must reflect real-world usage to enable meaningful comparisons. However, many benchmarks fail at this, using data sets that don’t represent real use cases, which leads to results that don’t reflect real applications.

Another major issue is overfitting. Since benchmark data sets are usually public, models often end up trained — intentionally or not — on evaluation data. This leads to inflated benchmark scores that don’t reflect true generalization to unseen data.

Beyond these concerns, benchmark coverage is also crucial. For example, MTEB, the most popular benchmark for evaluating embedding model accuracy, spans eight distinct task categories. While this broad coverage is useful for general comparison, it can be misleading if you care about performance on specific use cases. In practice, you should focus on benchmarks or tasks that align closely with your intended applications.

## RTEB: A New Retrieval-Focused Benchmark

While embedding models can be used for many tasks, their most common production use case today is retrieval — powering search, enabling Retrieval-Augmented Generation (RAG) systems and matching queries to relevant documents.

This is why the [Retrieval Embedding Benchmark](https://huggingface.co/blog/rteb) was created. RTEB is a new benchmark focused specifically on retrieval tasks. It builds on MTEB by providing a retrieval-focused evaluation framework designed to accurately measure the true retrieval accuracy of embedding models through:

* **A hybrid approach:** RTEB combines public data sets (some shared with MTEB) and private ones. This prevents overfitting — aka, “teaching to the test” — ensuring models aren’t trained on evaluation data. The inclusion of private data sets provides a more accurate measure of generalization to unseen data.
* **Real-world and multilingual coverage:** RTEB spans key enterprise domains such as finance, healthcare and code, and evaluates retrieval in over 20 languages. These data sets better represent the use cases found in enterprises today.

[![RTEB (Retrieval Embedding Benchmark) overview](https://cdn.thenewstack.io/media/2025/11/b1b06d63-image4.png)](https://cdn.thenewstack.io/media/2025/11/b1b06d63-image4.png)

Figure 2. RTEB overview.

The accuracy for each data set task, measured using the [Normalized Discounted Cumulative Gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) at rank 10 (nDCG@10), is used to rank the models, producing a rank per task. This metric is preferred for measuring retrieval accuracy because it captures both relevance and ranking quality, aligning closely with how humans perceive search results.

These ranks are then combined using the [Borda count](https://en.wikipedia.org/wiki/Borda_count) to determine the final leaderboard ranking. The mean of task scores is not directly used because raw measures differ across tasks — some data sets have larger or smaller score ranges, which can unbalance the average. The Borda count normalizes these scale differences and emphasizes relative performance, providing a fairer comparison across tasks.

## Navigating RTEB in MTEB

The [RTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard?benchmark_name=RTEB%28beta%29) is available under the Retrieval section of the MTEB leaderboard on Hugging Face.

[![RTEB in MTEB](https://cdn.thenewstack.io/media/2025/11/88b2c15e-image2.png)](https://cdn.thenewstack.io/media/2025/11/88b2c15e-image2.png)

Figure 3. RTEB in MTEB.

In addition to the main ranking, a few other parameters are important to take into account when consuming the RTEB leaderboard:

* **Embedding dimensions:** This represents the length of the embedding vector. Smaller embeddings offer faster inference and lower storage costs, while larger ones can capture more nuanced relationships in the data. The goal is to balance semantic depth with computational efficiency.
* **Max tokens:** This is the maximum number of tokens that can be converted into a single embedding. This depends on your [data’s structure and chunking strategy](https://thenewstack.io/boost-ai-efficiency-data-chunking-meets-document-databases/). Larger token limits enable embedding longer text segments.
* **Number of parameters** (when available): This represents the model’s size. More parameters generally correlate to higher accuracy, but also greater latency and resource needs. Proprietary models may not disclose exact sizes, but often provide options such as “small,” “lite” or “large,” with different pricing to match your needs.

Subsets of RTEB are available for different domains and language categories, offering focused insights into each model’s performance in specific areas. These can be accessed under the Retrieval section of MTEB on Hugging Face.

RTEB is an important step forward in evaluating embedding models for retrieval. Its hybrid combination of public and private data sets to prevent overfitting, along with its focus on real-world enterprise domains and multilingual coverage, makes it a more accurate and practical tool for developers evaluating different embedding models.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/3cfb1a95-cropped-17b02f8b-screenshot-2025-06-30-at-10.26.20%E2%80%AFam.png)

Thibaut Gourdel is a technical product marketing manager at MongoDB, where he focuses on MongoDB's integration with AI frameworks to support and accelerate developer adoption. With a background in data engineering, integration and applied AI, Thibaut brings expertise in practical...

Read more from Thibaut Gourdel](https://thenewstack.io/author/thibautgourdel/)