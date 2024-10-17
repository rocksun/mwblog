# The Secret Sauce for Vector Search: Training Embedding Models
![Featued image for: The Secret Sauce for Vector Search: Training Embedding Models](https://cdn.thenewstack.io/media/2024/10/49cc3ad5-sauce-1770431_1280.jpg)
In their zeal to reap the countless benefits of generative [machine learning models](https://thenewstack.io/how-i-enhanced-large-language-models-with-simple-rag/), organizations are rushing to embed their data for various forms of vector similarity search. Many are focused on prompt engineering and getting the best results for ad-hoc question answering, natural language search and summarizations of their data.

Some are concerned with prompt augmentation techniques like [Retrieval-Augmented Generation](https://thenewstack.io/how-to-build-a-rag-agent-with-nvidia-nim-and-langchain/) (RAG) and multi-agent architecture approaches. Most concentrate on a chunking strategy to ensure their embeddings are comprehensive enough.

Very few organizations, however, give due credence to what may well be the most influential factor for actually succeeding with these generative AI endeavors — which could explain why, despite significant tinkering with this technology, there’s still few mission-critical use cases actually in deployment.

According to [Marqo](https://www.marqo.ai/) CEO Tom Hamer, “Vector similarity search is only as good as the vector embedding are.” The need to fine-tune or train the models that create the embeddings and (usually) perform the embedding-based search is imperative to optimize results. However, most organizations treat the embedding process as a foregone conclusion before attending to more oft-discussed concerns regarding prompting, architecture and security.

According to Marqo CTO Jesse Clark, organizations using general embedding models–such as those available from OpenAI or Google — might actually get worse search results than they do using a keyword search algorithm, BM25, which doesn’t support summarization or semantic search.

However, by availing themselves of solutions designed to fine-tune embedding models (which can be trained in a matter of hours or minutes, depending on the size of the training dataset), organizations can redouble the efficacy of embedding-based search. Fine-tuning familiarizes the model with the context of the business domain and the specific task, teaches it business metrics, introduces notions of rank for search relevance and defines nomenclature encountered for the first time.

## General Embedding Model Problems
General embedding models are typically trained on general datasets that may not pertain to an organization’s use case. When embedding content like product names or internal enterprise jargon, they lack the semantic clarification to comprehend what that data means in an organization’s particular context.

Thus, when organizations embed their data with these models, issues arise because “for many search applications, it’s not just general, free text which is related to the documents organizations have or the queries they’re supplying,” Clark said. “The model hasn’t seen this type of query pattern; it hasn’t seen this type of language for a document. So, it performs much worse than what might’ve been reported on a benchmark.”

[Benchmarks](https://arxiv.org/abs/2210.07316) for generic embedding models can be deceptive because the data used for them could be unrelated to an organization’s specific needs. Clark recounted working with a customer using such a model for product search. In production, “it was something like 50% worse than using the keyword system they were using before, which is catastrophic from a business perspective,” Clark said.
## Fine-Tuning Embedding Models
Organizations fine-tune embedding models by retraining certain parameters with their own data that are most relevant to their deployments. For semantic search or product recommendations, “the best kind of data is what users have searched for previously and engaged with,” Clark commented. “We use those relationships to provide good data for these embedding models, so they’re working back from known positive examples for that business.”

Marqo Cloud is an API-based platform for accessing language models, fine-tuning embedding models, and implementing AI retrieval with its vector search engine. It provides best practices for fine-tuning models based on the amount of training data available, which is critical for introducing the [concept of ranking](https://arxiv.org/abs/2406.18740) for enhanced search result relevance. For example, when building an e-commerce search system for an item like jeans, if there’s one pair that’s been purchased several times and another that’s been purchased much less, this metric of item popularity can be input into the model’s parameters.

“So, using this historic data for businesses based on queries or purchases, and even the quantity that that’s happening in, means the embedding model is learning how to map the queries to the product and know which ones are more popular,” Clark mentioned. Organizations can do the same thing with any other business metric reflected in their data.

## Data Validation, Model Evaluation
Prior to fine-tuning embedding models, organizations must validate their training data to ensure it’s reliable. Marqo’s data validation features assess factors like completeness because, otherwise, “Often these things can be silent values,” Clark explained. “Someone might not know that the value is, in fact, missing and the model can be trained on blank spaces, for example, instead of it being a word.” Other validation capabilities involve formatting. In addition to scrutinizing text for consistency so it’s properly decoded, Marqo applies formatting techniques to image data, which is crucial for multimodality use cases.

Image [processing](https://thenewstack.io/get-more-out-of-machine-learning-with-data-preprocessing/) capabilities like resizing and uniformly formatting data are required to optimize the model’s ingestion of this training data. In addition to facilitating these advantages, Marqo Cloud allows organizations to “use that model in Marqo and the exact same processing happens to those inputs, so the model sees the same kind of data in Marqo when you’re using it for search as when it was trained,” Clark said. The platform also has an evaluation phase in which, once models have been fine-tuned, organizations can upload evaluation data to assess the trained model’s performance versus that of the untrained model.

## Continuous Learning Systems
The need to train the models vectorizing enterprise data for generative AI use cases is far from fleeting. It’s a reality of employing almost any form of statistical AI. “Vector search is still a machine learning system with machine learning models, and what we know about machine learning systems is they do require retraining,” Clark said. “The cadence will differ, but it’s an inevitability if you want to maintain performance.”

To that end, the API-based approach of Marqo and its capabilities for automating the core facets of training data validation, fine-tuning embedding models, and assessing them prior to deployment provides a virtuous cycle for operationalizing these models in what Clark termed “a continuous learning system.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)