# A Call To Use Generative AI To Create More Trustworthy Data
![Featued image for: A Call To Use Generative AI To Create More Trustworthy Data](https://cdn.thenewstack.io/media/2024/08/8c179c8b-governance-1024x576.jpg)
It sounds counterintuitive — using a technology that has trust issues to create more trustworthy data. But smart engineers can put [generative AI](https://thenewstack.io/ai/) to work to improve the quality of their data, allowing them to build more accurate and trustworthy AI-powered applications.

Generative AI models are remarkable for their ability to answer questions in human-like sentences, but they are prone to hallucination, and they can’t derive insight from internal company data that wasn’t part of their training. Yet this internal data is critical for many enterprise use cases.

Imagine an AI chatbot that tells employees how many days of PTO they have left or one that tells airline customers if they’re eligible for a seat upgrade. These use cases require precise responses, and machine learning engineers need access to accurate, timely data to maximize the value of generative AI in business.

Data governance can play a key role here, helping to [manage the operational and reputational risks](https://thenewstack.io/the-disconnected-state-of-enterprise-risk-management/) that can result from improper AI decision-making. Specifically, by applying metadata that describes the structure and provenance of data and how it should be used, data teams can ensure data quality and improve the accuracy of generative AI-powered applications. This extends beyond the business domain to emerging compliance frameworks, which require policies to ensure data integrity, security and accountability.

Creating this metadata is time-consuming work for data producers, however, which means busy data teams often cut corners or don’t create it at all. For an analogy, you may remember that Tim Berners-Lee once called for the creation of a “[semantic web](https://www-sop.inria.fr/acacia/cours/essi2006/Scientific%20American_%20Feature%20Article_%20The%20Semantic%20Web_%20May%202001.pdf),” where web content would be much more useful because it was described in a machine-readable form. This required sites to manually tag their content, which mostly never happened. That’s not unlike the governance problem data teams face today.

But while generative AI is driving the need for stronger data governance, it can also help to meet that need. By presenting a generative AI model with examples of how data should be labeled, generative AI can create the required metadata automatically. A human will still need to review the results, but the process will be much less laborious than creating metadata from scratch.

**Get Started With a Data Product Mindset **
The need for high-quality data doesn’t apply only to generative AI. As data becomes more important for all types of analysis, there’s been an accompanying surge of interest in building unified data catalogs that make it easier for other teams to discover and use data. By employing generative AI to create metadata, along with a data-streaming platform to create reusable [data products](https://medium.com/data-mesh-learning/what-exactly-is-a-data-product-7f6935a17912), data becomes much more available, boosting innovation and productivity.

This metadata includes machine-readable information, such as a data schema and field descriptions, as well as human-readable information, such as who created the data and how it should be used. The key is to provide sufficient information so that someone elsewhere in the organization who wants to consume a data asset will know where it originated, how it can be used, any associated service-level agreement (SLA) and its degree of trustworthiness.

The foundational element of data governance is a schema — specific metadata that describes the structure of data. If we present a generative AI model with enough examples of the data being collected or the code that produces it, the model can induce the schema.

This process works best when the metadata is created when data is produced. We can retroactively run a generative AI program over older data sets to induce metadata, but we may get less fidelity in the results because the original schema evolved over time. By creating metadata when data is produced, the metadata tends to be more accurate at describing the underlying data set.

**Keep Humans in the Loop**
Human review is needed because of limitations with the current state of AI. The AI will be good at seeing patterns, but it may not be able to generalize the entire schema based on a limited set of examples that it’s been shown. We’ve not yet totally replicated expert intuition and understanding, and this can complement the volume of information that AI can rapidly process. We know there are 12 months in the year, or 50 states in the United States, or that street addresses typically require a street number — and that allows us to easily spot mislabeled data. The AI process may make errors because it lacks this basic knowledge or because it hasn’t seen enough examples. However, a human can quickly fix these mistakes and still save a lot of time and effort before nonconformant data is used by engineers downstream.

To make this work well, producers of data need to adhere to the data policies that the organization has established. In addition, when a schema evolves, you may need to adjust the model to reflect the new schema. The choice of LLM matters, but it is less important than the workflows that support data curation and the contextualization of the system prompt. For the best results, the model needs examples not only of the data set or production code, but also guidance for the metadata you want the model to create.

**A Data-Streaming Platform Is the Optimal Pattern**
Recalling the Semantic Web, we never saw its vision realized of making the web machine-readable in the way its creators envisioned. Yet the web became machine-readable in a way that few foresaw in the early 2000s, because [machine learning got far better at understanding media created](https://thenewstack.io/creating-machine-learning-models-takes-too-much-time/) for humans. In a similar way, better machine learning presents a better alternative to completing the rote tasks necessary for data governance.

Applying generative AI in this way requires a platform to work with, and a data-streaming platform that can process data generated in real time is a good fit. [Data streaming platforms](https://developer.confluent.io/patterns/event-stream/event-streaming-platform/) are designed from the ground up to present data in a way that’s consumable, so it’s an efficient environment to apply metadata at the time of production and to create data products that can be reused in other applications.

A data streaming platform also helps to ensure that governance controls and metadata are incorporated into a common data catalog for discovery and reuse.

The rapid emergence of generative AI has created a critical need for high-quality data and data governance, but it has also provided a solution. In time, generative AI may be able to take on additional governance tasks, such as applying data policies, but it’s not ready for that yet in general.

Nevertheless, generative AI can help eliminate much of the rote work for defining and applying schema and other important data characteristics, creating a virtuous cycle that increases the quality of generative AI-powered applications and makes data much more widely available for reuse.

Industry and academia are beginning to define what [AI governance](https://academic.oup.com/edited-volume/41989/chapter-abstract/408516484?redirectedFrom=fulltext) should look like, but it’s still an emerging concept. Practitioners lack a consensus definition of what AI governance entails, let alone anything resembling a framework. But we can say for sure that AI governance depends on data governance, by helping engineers trust data that they can use to build generative AI applications.

In the future, I would like to see the industry further define what AI governance should look like, and for data infrastructure vendors to bring more focus to integrating generative AI into tools and abstractions that promote better data quality.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)