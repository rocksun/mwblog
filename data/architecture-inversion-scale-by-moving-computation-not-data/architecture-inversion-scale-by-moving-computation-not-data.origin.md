# Architecture Inversion: Scale by Moving Computation, Not Data
![Featued image for: Architecture Inversion: Scale by Moving Computation, Not Data](https://cdn.thenewstack.io/media/2024/10/adb9b1be-giraffe-1024x576.jpg)
[Sergey Novikov](https://www.shutterstock.com/g/serrnovik)on Shutterstock.
Have you ever wondered how the world’s largest internet and social-media companies can deliver algorithmic content to so many users so fast?

Consider what the likes of TikTok need to do to provide people with an endless stream of personalized video clips to people’s phones. They have [some model](https://thenewstack.io/data-models-a-key-step-on-your-data-journey/) representing the user, and they need to use this to find the most suitable clips to show to that particular user among billions of alternatives. And since they also have billions of users, they need to do this millions of times per second.

## Traditional Solutions
The naive way to solve TikTok’s problem is to compare the user model to every video clip to determine how well each one fits that user. It is widely understood that this brute-force approach doesn’t scale — with a billion videos and a million requests per second, this becomes a quadrillion comparisons per second!

The obvious solution to this is indexing: maintain a [data structure](https://thenewstack.io/how-golang-range-simplifies-data-structure-iteration/) that makes it possible to find suitable video clips from the user model without having to consider every clip. For example, if the user model notes a preference for English-speaking videos, the videos can be indexed with a B-tree that points directly to English videos so the rest can be ignored. Or, if the user is represented as an interest vector embedding, a vector index such as the Hierarchical Navigable Small World (HNSW) algorithm can be used to find videos with similar vectors without considering the rest.

Real systems will use a combination of such indexes. Now, the indexes only give a rough indication of what videos may be suitable to the user. To really surface the content users find most interesting or useful, you need to do a more accurate comparison between the user model and each candidate item — these days often done using [neural nets](https://thenewstack.io/airbnb-builds-a-second-neural-network-to-diversify-listings/). Here is where it gets interesting.

## Scaling Without Compromising Quality
The common way to rescore is to pass the candidate items retrieved from the indexes to another component in your architecture doing the detailed scoring of each. How many should be rescored in this way? This should be a certain fraction of all the candidates.

To see this, consider that indexed retrieval plus rescoring is an approximation to brute-force scoring of all candidates, and what we need to consider is the quality loss from this optimization. This can be expressed in terms of the probability that a given video that would be shown to the user with brute-force evaluation is present in the set to be reranked.

This probability goes toward zero as the size of that set relative to the full set of candidates gets smaller. The quality loss will get larger as the fraction to be rescored decreases, and it also gets larger the better your full scoring algorithm becomes as there is more to lose.

Let’s get concrete and say we want to rescore 1% of the candidates, and that each item contains 2kb of data useful for final scoring (roughly one vector and hundred properties). With a billion items this becomes 10 million items to rescore per request, and with a million requests per second that means we need to move 20 petabytes of data per second for reranking! Even this small fraction is clearly very far from being viable, so what are the big players doing?

The answer is that they are not moving the data to the scoring compute nodes, but instead are moving the scoring compute into the index to be done locally where the data resides, thus circumventing the entire problem.

## The Architecture Inversion Is Coming to the Rest of Us
Now why should the rest of us care, blessed as we are with a lack of most of the billions of users TikTok, Google and the likes are burdened with? A number of factors are becoming relevant:

- ML algorithms are improving and so is local compute capacity, meaning fully scoring items gives a larger boost in quality and ultimately profit than used to be the case.
- With the advent of
[vector embeddings](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai/), the signals consumed by such algorithms have grown by one to two orders of magnitude, making the network bottleneck more severe. - Applying ever more data to solve problems is increasingly cost effective, which means more data needs to be rescored to maintain a constant quality loss.
- As the consumers of data from such systems move from being mostly humans to mostly LLMs in
[RAG solutions](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/), it becomes beneficial to deliver larger amounts of scored data faster in more applications than before. This will culminate in most applications being about delivering high-quality data to LLMs to reason in long chains to make high-quality business decisions at an inhumanely fast pace.
For these reasons, the scaling tricks of the very biggest players are becoming increasingly relevant for the rest of us, which has led to the current proliferation of architecture inversion, going from traditional two-tier systems where data is looked up from a search engine or database and sent to a stateless compute tier to inserting that compute into the data itself.

Now, to really do this, you also need a platform that can actually manage your data, indexing and compute in this way. This has led to the increasing popularity of [Vespa.ai](http://vespa.ai), the platform that got its start as Yahoo’s solution for architecture inversion back when it was one of the big players. The technology has since been open sourced.

Vespa.ai allows you to store and index structured data, vectors/tensors and full text together over any number of machines and do any kind of tensor computation and machine-learned inference locally where the data is stored.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)