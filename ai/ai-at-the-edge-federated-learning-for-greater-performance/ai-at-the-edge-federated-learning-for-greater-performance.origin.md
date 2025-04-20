# AI at the Edge: Federated Learning for Greater Performance
![Featued image for: AI at the Edge: Federated Learning for Greater Performance](https://cdn.thenewstack.io/media/2025/04/3e0cdc23-ai-at-the-edge-2-1024x576.jpg)
The classical machine learning paradigm requires the aggregation of user data in a central location where data scientists can pre-process it, calculate features, tune models and evaluate performance. The advantages of this approach include being able to leverage high-performance hardware (such as GPUs), and the scope for a data science team to perform in-depth data analysis to improve model performance.

However, this data centralization comes at a cost to data privacy and may also fall foul of data sovereignty laws. Also, centralized training may not be viable for [Internet of Things (IoT) and other edge-based devices](https://thenewstack.io/edge-computing/) such as mobile phones, embedded systems and robots in factories. This is because network connectivity can prove unreliable, and IoT devices have limited memory, storage and compute power.

Federated learning, introduced by [Google](https://cloud.google.com/?utm_content=inline+mention) in 2016 and originally dubbed “[Federated Optimization](https://arxiv.org/abs/1610.02527v1),” offers an alternative. The core idea is that instead of the endpoints sending data to the server, the server sends models to the client endpoints and the endpoints send training or model updates. Multiple clients, coordinated by a central service, collaborate to solve a machine learning problem — improving on a model iteratively without sharing data.

## How Federated Learning Works
The most common architecture for federated learning is that each device first downloads a model from a data center in the cloud, such as a [foundation model](https://thenewstack.io/llm/). They train it on their private data, then summarize and optionally encrypt the model’s new configuration.

The model updates are sent back to the cloud, where a central coordinator/ aggregator decrypts, averages or otherwise combines the models using some sort of computation. The aggregator integrates the results back into the centralized model, which are sent back to the participating clients for further refinement. This iterative, collaborative process continues until the model is fully trained.

Architectural variations can increase the amount of distribution, for example, by clustering clients together into cohorts, with a separate coordinator for each one.

Working this way offers some data privacy since no raw data is shared. That said, sometimes, the entire model is shared. Also, model parameters can leak information; by knowing how one individual model is diverging, it is possible to infer a great deal about an individual’s data.

To limit this leakage during the model update process, federated learning may be combined with other techniques such as [differential privacy](https://www.semanticscholar.org/paper/Differential-Privacy-:-A-Historical-Survey-Hilton-Cal/4c99097af05e8de39370dd287c74653b715c8f6a) and [secure aggregation](https://research.google/pubs/practical-secure-aggregation-for-federated-learning-on-user-held-data/).

The authors of Google’s “[Deep Learning with Differential Privacy](https://arxiv.org/abs/1607.00133)” paper, for example, describe a differentially private stochastic gradient descent algorithm that applies clipping and noise at each step of the gradient descent. The random noise makes it harder to reverse training examples, while the clipping minimizes the contribution of each training sample.

## Real-World Uses of Federated Learning
Perhaps surprisingly, model training in this manner comes with fairly minimal degradation to model performance. According to [Katharine Jarmul](https://www.linkedin.com/in/katharinejarmul/?originalSubdomain=de), author of the O’Reilly book “[Practical Data Privacy,](https://www.oreilly.com/library/view/practical-data-privacy/9781098129453/)” and former principal data scientist at [Thoughtworks Germany](https://www.thoughtworks.com/en-de), federated learning “is increasingly deployed in non-consumer facing edge systems, such as learning factory floor behavior or predictive maintenance.”

When compared with classical machine learning, federated learning tends to be slower to converge. This means that the technique works best in situations where the model is relatively simple.

“Of course not everything is a transformer model or needs to be trained on 70GBs of parameter space,” Jarmul told The New Stack. “Companies like Cisco may still put basic models that perform very fast classification, such as decision trees, on edge devices for malware analysis.”

Federated learning is equally valuable in consumer devices. While it is still a maturing technology, the technique is already being used daily by millions of users as it has been deployed by many of the tech behemoths, including [Apple](https://www.apple.com/) and Google.

At Google, federated learning has been applied to training machine learning models [powering various features in the mobile keyboard](https://arxiv.org/abs/2305.18465) (Gboard), including next word prediction, smart compose, on-the-fly rescoring and [emoji suggestion](https://arxiv.org/abs/1906.04329).

With Gborad, one use case was to improve prediction for non-English languages such as Spanish and Portuguese. To do this, Google would have selected a subset of devices using a mixture of device settings and knowledge from analytics, favoring newer models over older ones to limit memory and CPU constraints.

The data science team would then have run multiple training rounds locally and sent the gradient update to the aggregator, which averaged all of the gradients together. The team would have kept training until the model was good enough and when the process stopped, everyone would have received an updated model.

[Federated analytics](https://research.google/blog/federated-analytics-collaborative-data-science-without-data-collection/), a concept closely related to federated learning, was introduced by Google later as “the practice of applying data science methods to the analysis of raw data that is stored locally on users’ devices.”
Both federated learning and analytics are particularly exciting in health care. Google uses federated analytics for [Google Health Studies](https://blog.google/technology/health/google-health-studies-app/). The New Stack [previously reported](https://thenewstack.io/how-rapidai-uses-edge-kubernetes-and-ai-to-boost-stroke-care/) how another company, [RapidAI](https://www.rapidai.com/), was using clinical AI at the edge to extend the ideal ischemic stroke treatment window from approximately six to 24 hours.

One can imagine that for anything from lung scans to brain MRIs, aggregating medical data and analyzing it at scale could lead to new ways of detecting and treating cancer and other diseases, all without sharing confidential medical records.

Researchers at Apple have described how they applied federated learning to [several features in Photos](https://machinelearning.apple.com/research/scenes-differential-privacy). As the app becomes familiar with significant people, places and events in the user’s library, it is able to choose key photos for Memories and Places in iOS 17.

The tech colossus also uses federated learning for [Siri App Selection in iOS](https://arxiv.org/abs/2502.04565). For example, when a user makes a request to play music, App Selection analyzes the user’s habits to determine the most suitable app. If a particular app is frequently used for similar requests, the model will prioritize launching that app, even if it wasn’t specifically mentioned.

The very advanced chips in Apple’s mobile devices, combined with a greater level of hardware standardization, will likely give Apple an advantage over Android in the long term.

“Many of the new features in Apple Intelligence, as well as the hardware privacy features Apple has built, show me that the company is way more advanced than Android,” Jarmul told The New Stack. “We’ve known for a long time that the best recommender would be one that is designed for an individual user, but training per person is hard to scale.

“Apple is doing some very interesting research, looking at how they can train a model and personalize it, rather than aggregate it, so your device just learns you.”

Several other big players have [released federated learning](https://github.com/aws-samples/federated-learning-greengrass-ecs) in production settings, including [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) and [NVIDIA](https://developer.nvidia.com/blog/federated-learning-clara/). There are also a number of federated learning open source libraries, the most popular of which is [Flower](https://flower.ai), an open-source platform from the AI startup [Flower Labs](https://flower.ai/).

## Is Federated Learning Better for the Planet?
Exciting though the rise of AI is, it currently comes with a considerable carbon cost:

[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)reported in May 2024 that its total carbon emissions had risen nearly 30% since 2020, primarily due to its construction of data centers, to meet its push into AI.- Google’s emissions have surged nearly 50% since 2019 and increased 13% year-on-year in 2023, according to the company’s own report. Google attributed the emissions spike to an increase in data center energy consumption and supply chain emissions, driven once again by AI.
Concerned by this, AI researchers in the [Department of Computer Science and Technology at the University of Cambridge](https://www.cst.cam.ac.uk/) looked into more energy-efficient approaches to training AI models. Working with collaborators at the [University of Oxford](https://www.ox.ac.uk/), [University College London](https://www.ucl.ac.uk/) and [Avignon Université](https://univ-avignon.fr/), they explored the environmental impact of federated learning.

Their paper, ‘[Can Federated Learning Save the Planet?](https://arxiv.org/abs/2010.06537)’ and follow-up [journal article](https://www.jmlr.org/papers/v24/21-0445.html), looked at the carbon cost of federated learning compared with centralized training.

Training a model to classify images in a large image dataset, they found that any federated learning setup in France emitted less CO2 than any centralized setup in either China or the U.S. When training a speech recognition model, federated learning was more efficient than centralized training in any country.

We should note that these observations were tied to the particular model and the settings of the experiment. [Nic Lane](https://www.cst.cam.ac.uk/people/ndl32), who led the research, told The New Stack, “Where we care about carbon emissions and machine learning, we can use federated learning methods to manipulate the overhead by having the compute happen in certain locations at certain times. That is much harder to achieve in a data center than a federated setting.”

This means that federated learning gives us a way to apply carbon-aware computing approaches to training models, such as [demand shifting and shaping](https://www.conissaunce.com/demand-shifting-and-shaping.html).

Lane’s team theorized that federated learning has three major advantages over a centralized approach in terms of emissions — it doesn’t require cooling, doesn’t need data to be moved, and it can reduce waste by allowing cross-organizational collaboration.

Typical data center power usage effectiveness (PUE) is 1.6, which means that 60% of the energy utilized in a data center is used for cooling. Even for the most efficient data centers run by companies like Google and Meta, cooling remains an appreciable factor. Of course, many data centers are run from universities and smaller organizations, and have a much higher PUE.

One solution to the data center cooling problem is to use waste heat for other purposes, such as heating homes or municipal swimming pools. You can’t do this with the huge facilities that Amazon, Google and Microsoft typically construct because you need to locate amenities close to where the waste will be used. However, there are small data centers, particularly in Europe, that are taking this approach.

“[T.Loop](https://www.tloop.se) is one company that transforms energy waste into heat, and there are others,” Lane told The New Stack. “Using federated learning, you can combine these smaller facilities and train an LLM.”

This opens up some interesting possibilities as we hit physical limits on GPU infrastructure.

“There are a very limited number of data centers worldwide that could train truly large-scale models, like [Llama](https://thenewstack.io/llama-3-how-metas-new-open-llm-compares-to-llama-1-and-2/) and [ChatGPT](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/), using the conventional paradigm of needing all the GPUs in one place,” Lane said. By using federated learning to combine a network of GPUs in different places, he added, “the number of virtual places where you can train these models increases dramatically.”

This could also be true for a large organization. “Even for a company that might have around 10,000 GPUs or more across the planet, like Samsung, if you don’t have enough GPUs in one place, it won’t be possible to train a large LLM,” Lane said. “Federated learning would allow you to utilize your resources more fully.”

We noted earlier that federated learning tends to be a slower process. However, Lane suggested that despite taking longer, these advantages might mean that you can ultimately train faster. “

There’s a performance illusion when you focus myopically on wall-clock time when you are working at large scale,” he said. “There are many companies who want to start a training run today, but there are no GPUs for them to use, so they wait six months. With federated learning, wall-clock time might be 30% slower, but you can start today and help the environment.”

The research team also noted that moving data from one place to another has a considerable cost.

“One memory operation uses a thousand times more energy than one compute operation,” Lane said.

Since federated learning doesn’t require data to be moved, there are potential efficiency gains here. Lane’s team has already shown strong demonstrations of this technology; using its [Photon system](https://arxiv.org/abs/2411.02908) built on top of Flower, the team was the first to show 7B parameter LLMs, and larger can be trained using federated learning — a result that has been later replicated by other industry labs and startups.

In addition, federated learning opens up the possibility of cross-organizational collaboration. There is currently a huge amount of redundant training as multiple organizations build very similar models. In theory, federated learning would give us another mechanism to share models across organizational boundaries.

Germany and the rest of the European Union are starting to push this advantage quite heavily.

“I’m a jury member on [Composite Learning](https://www.sprind.org/en/actions/challenges/composite-learning), which is funded by the German government,” Jarmul told us. “The idea is if you want to train on a large-scale model like an LLM, you can spread this across multiple data centers and hardware providers.”

Flower and the University of Cambridge were selected and provided funding under this scheme to build [a tool for large-scale federated learning](https://www.sprind.org/en/actions/challenges/composite-learning#anchor-teams).

In addition, “the German government agency responsible for climate and the economy has also just announced an EU project called [8ra](https://www.8ra.com), which is designed to build next-generation cloud infrastructure for AI at the edge, and will be distributed or federated by its nature,” Jarmul told TNS. “If we can create collaborative models that eliminate duplication waste, it will be very interesting for the industry.”

Beyond federated learning, there are a number of other techniques that can make a significant difference to the carbon cost of both training and inferencing, most of which are rooted in compression. By shrinking the model size, it is possible to speed up training time and increase its resource efficiency.

This is an ongoing research area, with several initiatives exploring topics like distillation, pruning and quantization as a means of compression.

Beyond these approaches, the same basic rules apply to machine learning as they do to any other compute job:

- Use the smallest hardware configuration that can safely execute the job.
- Run compute in areas where low-carbon electricity is abundant, and where there are credible plans to make the grid even cleaner.
- Use cloud services from providers that have data centers in green locations and provide good tooling to help reduce your footprint.
- And apply carbon-aware computing techniques, such as
[demand shifting and shaping](https://www.conissaunce.com/demand-shifting-and-shaping.html), to further reduce your footprint.
I explore these approaches in more depth in my eBook for The New Stack, “[Sustainable Software: A Developer’s Guide to Green Computing](https://thenewstack.io/ebooks/cloud-infrastructure/developers-guide-to-cloud-infrastructure-efficiency-and-sustainability/).”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)