# What Makes TikTok’s Algorithms So Effective?
![Featued image for: What Makes TikTok’s Algorithms So Effective?](https://cdn.thenewstack.io/media/2025/01/beed1e48-tiktok-1024x768.png)
On Tuesday, the newly-elected U.S. President Donald J. Trump [signed](https://www.nytimes.com/2025/01/22/us/politics/what-is-an-executive-order.html) an [executive order](https://www.whitehouse.gov/presidential-actions/2025/01/application-of-protecting-americans-from-foreign-adversary-controlled-applications-act-to-tiktok/) that gave TikTok a [75-day reprieve](https://www.nytimes.com/2025/01/20/technology/trump-tiktok-ban-delay-executive-order.html) from being shut down in the U.S. by the Justice Department, much to the delight of fervent TikTok users.

But, during the signing, the President made his [intention clear](https://x.com/Acyn/status/1881510272529240260): TikTok would have to sell [half of itself to the U.S](https://www.theregister.com/2025/01/20/trump_tiktok_nationalization_idea/)., by way of a U.S.-owned entity of some sort, to remain operating in the U.S.

The transactionally-minded President then added, as an aside, “Every rich person has called me about TikTok.”

Half can be tricky, though. You want to make sure you get the right half. Otherwise, you’ll end up with the empty husk of a media service, ala [Friendster](https://www.therunway.ventures/p/friendster).

The company now has about 170 million users in the U.S. But that audience can vanish quickly. You want the part that keeps users logging in. The valuable part is the algorithm that runs the recommendation service.

TikTok’s massive user base is a testament to its addictive nature. The key to keeping users engaged? It’s powerful algorithms. These algorithms drive the recommendation system, constantly feeding users a stream of content tailored to their interests.

As University of Zurich researchers Maximilian Boeker and Aleksandra Urman noted in their study, “[An Empirical Investigation of Personalization Factors on TikTok](https://www.researchgate.net/publication/358233121_An_Empirical_Investigation_of_Personalization_Factors_on_TikTok),” the platform’s recommendation system is arguably its most important success driver.

[TikTok](https://www.tiktok.com/en/), and its parent company, the Bejing-based [ByteDance](https://www.bytedance.com/en/), has been tight-lipped when it comes to the design and operation of the algorithms that feed their users content.
Those willing to dive into a research paper from ByteDance engineers and other researchers may find some hints into how TikTok keeps its users coming back.

## Unveiling the Monolith
The paper, “[Monolith: Real Time Recommendation System With Collisionless Embedding Table](https://arxiv.org/pdf/2209.07663),” presented at the 2022 ACM Conference on Recommender Systems (RecSys), offers valuable insights. While not claiming to describe TikTok’s exact algorithms, it reveals ByteDance engineer’s approach to designing a highly -effective recommendation system.

The paper details the “unorthodox” trade-offs the researchers made that led to significant performance improvements, resulting in a recommendation system called “Monolith” that consistently outperforms other systems with the same memory usage, the researchers asserted.

Former TikTok engineer [Arman Khondker](https://armankhondker.com/) pointed to this paper as [being fundamental](https://x.com/armankhon/status/1880860565889040428) to understanding TikTok’s approach. Khondker [hailed](https://x.com/armankhon/status/1880860565889040428) the TikTok algorithm as “years ahead of the competition” and “without question, the most valuable piece of software in existence.” Elon Musk himself responded to this claim with a succinct “For now.”

## The Goals of TikTok’s Algorithm
A 2021 internal TikTok document [obtained by the New York Times](https://www.nytimes.com/2021/12/05/business/media/tiktok-algorithm.html) revealed the four main goals of the company’s algorithm: user value, long-term user value, creator value, and platform value. Essentially, TikTok prioritizes keeping users engaged and spending time on the platform.

The algorithm considers various factors, including likes, comments, and video watch time, to determine which content to show users. It also aims to diversify recommendations to prevent users from getting bored and losing interest.

For analysts familiar with user retention, it all looked like pretty routine stuff. “Totally reasonable, but traditional stuff,” quipped Julian McAuley, a professor of computer science at the University of California San Diego.

So perhaps the true power of the TikTok algos come not only from the user analysis but also the [the considerable speed](https://thenewstack.io/tiktok-to-open-source-cloud-neutralizing-edge-accelerator/) at which they are executed.

## The Power of Real-Time Feedback
The “Monolith” paper highlights the challenges of building recommendation systems that can keep up with users’ rapidly changing preferences.

In a nutshell, the job of a recommendation engine is to predict users’ interests and future behavior, using the latest interactions as the primary input for training the model.

To do this, traditional systems often rely on complex models that are slow to adapt to new data.

The conventional wisdom for building such systems has been to maintain individual models for each task. “Predicting clicks” would get one model, and “predicting watch time” would get another model. Analysis is usually done by batch processing, slowing the rate at which the system learns about the user. The models can’t interact with customer feedback in real time.

The more frequently someone uses TikTok, “the more accurate the algorithm will be.”

— Zhengwei Zhao, Sun Yat-sen University

Deep learning frameworks like [Pytorch](https://thenewstack.io/why-pytorch-gets-all-the-love/) and [TensorFlow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/), built for general usage, aren’t really geared for the urgent production demands of online recommendations. Tensorflow separates training from inference, which cuts the model off from the latest input from users. As a result, any competitive system design has to build all sorts of workarounds to jam these [batch frameworks](https://thenewstack.io/real-time-ai-apps-using-apache-flink-for-model-inference/) into [real-time systems](https://thenewstack.io/data-streaming/).

Monolith, on the other hand, utilizes a single model for all tasks and incorporates real-time feedback through online training. This allows the system to quickly learn and adapt to users’ evolving interests.

The paper describes how [Kafka](https://thenewstack.io/confluent-wants-to-make-batch-processing-a-thing-of-the-past/) can be used to log actions of users, and, in a parallel operation, log features. An[ Apache Flink](https://thenewstack.io/a-developers-guide-to-getting-started-with-apache-flink/) job “concatenates features with labels from user actions and produces training examples, which are then written to a Kafka queue. The queue for training examples is consumed by both online training and batch training.”

- The Monolith architecture emphasizes faster online training.
## ‘Doomscrolling’ and Table Size
Another challenge for recommendation systems is dealing with “sparse features” and “concept drift.” Sparse features mean that users are only interested in a small subset of content, while concept drift refers to the tendency for users’ interests to change over time as they scroll through an endless stream of videos.

“The same user interested in one topic could shift their zeal every next minute,” the paper states.

If you were to put everything into the embedding table, it would be too large to fit into memory. And traditional fixed-sized models don’t take kindly to being enlarged, which they would have to constantly be as new users came aboard.

Monolith tackles these issues by:

- Rapidly incorporating user feedback into the training process.
- Keeping the data table manageable through a “collisionless hash table” and fancy feature eviction mechanisms.
Meeting these objectives ensures that the system can keep up with users’ changing preferences without it being overwhelmed by the sheer volume of data.

To mash the wide array of sparse features into computer memory, the researchers advocated using a [Cuckoo Hashmap](https://en.wikipedia.org/wiki/Cuckoo_hashing) design, which minimizes collisions, or two keys inadvertently occupying the same space.

To further reduce memory usage, seldomly-used IDs are trimmed away.

## Personalized Content Fast
In essence, Monolith represents a shift away from the [traditional microservices approach](https://thenewstack.io/microservices/) to building systems, opting instead for a more [unified, monolithic architecture](https://thenewstack.io/return-of-the-monolith-amazon-dumps-microservices-for-video-monitoring/).

While ByteDance has not confirmed whether the Monolith architecture is used in TikTok (or the Chinese version, Douyin), the services’ ability to deliver personalized content at lightning speed is undeniable. (The Monolith architecture is officially used in [BytePlus Recommend](https://www.byteplus.com/en/product/recommend), the company’s hosted recommendation engine service.).

On TikTok, there is almost no work needed on the part of the user to find compelling content, [observed](https://www.researchgate.net/publication/349000779_Analysis_on_the_Douyin_Tiktok_Mania_Phenomenon_Based_on_Recommendation_Algorithms) researcher Zhengwei Zhao, Sun Yat-sen University, China. As soon as the user starts swiping, the app starts learning.

The more frequently someone uses TikTok, “the more accurate the algorithm will be.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)