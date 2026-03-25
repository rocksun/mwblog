If I search for “black running shoes for winter,” `marksandspencer.com` finds me a lovely pair of lace-up boots…for women. In the last six months, I’ve made 30 orders for 45 products, only one of which came from the women’s department — a pair of slippers for my mother. So there is an important signal being ignored here. Or perhaps M&S knows something about me that I don’t know myself.

In fairness to M&S, modern product discovery is far more complex than it appears. A discovery system must evaluate many signals to determine which products should appear first. It may consider keyword matches, semantic similarity to the shopper’s query, click and purchase behavior, inventory availability, promotions, and personalization signals such as browsing history. Product attributes like category, brand, price, and ratings may also influence ranking.

Product discovery is therefore not simply about retrieving products from a catalog. It is about evaluating many signals together to determine relevance. Modern product discovery has effectively become a multidimensional ranking problem, where dozens of signals must be evaluated simultaneously to determine which products appear first.

## What is tensor-based ranking?

In the context of product discovery, tensor-based ranking refers to ranking models that represent and evaluate multiple relevance signals simultaneously within a multidimensional structure. These signals may include

* semantic embeddings from vector search
* structured product attributes such as brand, price, or category
* shopper behavior signals such as clicks and purchases
* contextual information such as seasonality or promotions
* business priorities such as margin or merchandising rules

By representing these signals as tensors, ranking models can evaluate their interactions directly rather than processing them through separate ranking stages. This approach allows discovery systems to model relevance more closely, reflecting the complexity of real-world commerce environments.

## The limits of traditional ranking

Many commerce search platforms were originally designed for an earlier generation of online retail. Ranking strategies typically relied on keyword matching combined with relatively simple rules. Over time, additional signals were layered onto these systems. Behavioral signals such as click-through and conversion rates were introduced. Merchandising rules were added to promote certain products. More recently, semantic embeddings have been used to support vector search and natural-language queries.

While these additions have improved discovery capabilities, they have also made ranking models far more complex. Modern discovery systems must combine structured attributes, machine-learned signals, embeddings, contextual information, and business priorities.

In many architectures, these signals are processed through separate pipelines. Retrieval may occur in the search engine, model inference in another system, and final ranking in yet another stage. As ranking models become more sophisticated, these pipelines can become difficult to manage and introduce additional latency.

## Vectors vs. tensors in product discovery

Vector search has become an important capability in modern product discovery, enabling systems to match products based on semantic similarity. By representing queries and products as embeddings, vector search can retrieve products that are conceptually related to a shopper’s request, even when the exact keywords do not match.

However, vectors are just a subset of tensors. They are one-dimensional units that represent a point in space. Tensors, on the other hand, are multidimensional and preserve relationships among their dimensions.

|  |  |  |  |
| --- | --- | --- | --- |
| **Structure** | **Dimensions** | **Example** | |
| Scalar | 0 | Price (one measurement) | price = $175 |
| Vector | 1 | product embedding (attributes of one object) | shoe = [price, rating, popularity] |
| Matrix | 2 | product catalog table(many objects) | products × attributes |
| Tensor | N | multi-signal ranking(multi-dimensional signals) | product × user × signals × time |

When a user searches for something like running shoes, there is no single “correct” answer. You might want to surface the most textually relevant item, the one with the highest margin, a product that’s in stock, or the option most likely to convert for that specific user. Each of these is a valid signal, but deciding which should rank first is not straightforward.

These signals often conflict. The most relevant item may be out of stock, the most profitable option may not fulfill the shopper’s intent, and the most personalized result may not align with the current campaign. In practice, relevance is a decision problem that requires evaluating multiple signals together in real time.

Traditional vector databases fall short here. They are designed to retrieve similar items based on embeddings, but not to combine and balance a broader set of signals within a single ranking decision.

Tensor-based ranking models extend this approach by allowing all these signals to be evaluated together within a single ranking function. Embeddings, product attributes, user behavior, and business context all contribute to the final score, driving more controlled and adaptable ranking decisions.

## Why tensor support needs to be built into the search platform

Representing relevance signals with tensors is only part of the story. For modern commerce systems, ranking models must also be evaluated efficiently at query time. Many search architectures handle machine-learning ranking through external pipelines. Retrieval occurs in the search engine, candidate results are sent to a separate system for model inference, and the results are then returned for re-ranking. While this approach can work, it introduces additional latency and operational complexity.

For this reason, tensor support should be built directly into the discovery platform. When ranking models are evaluated within the search engine as part of the query pipeline, discovery systems can combine embeddings, structured attributes, behavioral signals, and business context into a single model executed in real time.

This architecture allows complex ranking models to run while maintaining the low latency required for high-traffic commerce environments. It also simplifies experimentation, enabling teams to evolve ranking strategies without introducing additional infrastructure.

Because commerce environments change constantly, including price updates, inventory fluctuations, and promotional start and end, evaluating these signals directly at query time ensures that discovery results reflect current business conditions.

## Evaluating product discovery platforms for tensor-based ranking

When evaluating modern product discovery platforms, several architectural capabilities become important:

* **Native tensor support**  
  The platform should support tensor representations directly within the ranking model.

* **In-engine model evaluation**  
  Ranking models should be evaluated inside the search engine rather than through external inference pipelines.

* **Real-time feature evaluation**  
  Signals such as inventory, price, and behavioral data should be incorporated at query time.

* **Multimodal signal support**  
  The platform should combine embeddings, structured attributes, and behavioral signals within a unified ranking function.

* **Low-latency ranking at scale**  
  Complex ranking models must operate within the latency requirements of high-traffic commerce systems.

Platforms that support these capabilities are better suited to the multidimensional nature of modern product discovery.

## Looking Ahead

Product discovery has evolved far beyond simple keyword search. Today’s discovery systems must understand shopper intent, interpret product catalog data, incorporate behavioral signals, and respond to rapidly changing business conditions.

Meeting these requirements requires ranking architectures capable of evaluating many signals together in real time. Tensor-based ranking models provide one way to achieve this, enabling discovery systems to represent and evaluate the multidimensional nature of relevance in modern commerce environments.

And hopefully, get me quickly to the “black running shoes for winter” I was looking for.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/b24ea863-tim-young--541x600.jpg)

Tim Young leads marketing at Vespa.ai, drawing on his technical background to implement data-driven strategies. He began his career in large-scale data management for enterprises like British Telecom, T-Mobile, Shell, British Airways, and Ford. Tim has held key marketing roles...](https://thenewstack.io/author/tim-young/)