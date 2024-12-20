# Stop Treating Your LLM Like a Database
![Featued image for: Stop Treating Your LLM Like a Database](https://cdn.thenewstack.io/media/2024/12/8765b171-batch-1024x576.jpg)
Imagine driving a car with a headset that only updates your view every five minutes instead of providing a continuous video stream. How long would it take before you crashed?

While this type of batch processing clearly doesn’t work in the real world, it’s how many systems operate today. Batch processing, born out of outdated technology constraints, forces applications to rely on static, delayed data. This approach may have been the only viable solution when compute, memory and storage were limited, but it’s completely misaligned with the way we interact with the real world — and even more so with how AI should function.

Generative AI holds incredible potential, but treating [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms) like [static databases](https://thenewstack.io/data/) — reactive systems that wait for inputs and deliver outputs — misses the point entirely. AI thrives on real-time, contextual data. Yet, by sticking to the batch-processing mindset, we’re stifling its capabilities.

Let’s explore why the batch paradigm is a relic of the past, how it hinders AI applications and why the [future of AI](https://thenewstack.io/ai/) demands a real-time event-streaming platform.

## Why Are We Stuck in Batch Mode?
Batch-oriented systems for analytics and machine learning have dominated technology for decades. These systems were born out of necessity, created in a time when computers had limited memory, constrained compute power and minimal storage. However, the same legacy approach is now being applied to the new world of generative AI.

MLOps has largely evolved around a set of discrete, sequential tasks, like feature engineering, model training, model testing, model deployment and bias characterization. This conceptual model lends itself well to batch-oriented development and delivery, but it creates limits to how reactive and accurate these applications can be in a changing world. Those applications that require better responsiveness [must necessarily eschew the common MLOps infrastructure](https://thenewstack.io/why-infrastructure-must-be-serverless-in-the-ai-age/).

We believe this to be a flawed approach.

## No One Ever Gets Fired for Designing a Batch Process
At its core, this paradigm aggregates data into a central database, where it passively waits to be polled and recalled by systems or users. This creates systems that are only as useful as the specificity of the queries they receive. While this approach worked within the constraints of its time, it fundamentally disconnects from the way we experience and interact with the world.

![High-level view of a batch process](https://cdn.thenewstack.io/media/2024/12/2a6979a2-image1-1024x322.png)
High-level view of a batch process

Even as technology has evolved, this mindset remains deeply ingrained. Today, we have alternative technologies like data-streaming platforms that allow for real-time, event-driven architectures. But batch systems persist — not because they’re the best solution, but because they’ve become the accepted way of doing things.

Just like the old adage, “No one ever got fired for buying IBM,” the same could be said of batch systems: No one gets fired for designing a system that aggregates data in one place, with the premise that acting on this centralized data is efficient and reliable. We have conditioned ourselves to model work as a series of tasks, finishing one before going on to the next. Well-established outcomes from disciplines like operations research and lean manufacturing reinforce that humans do well when we do batch-oriented work because we get better through practice and less efficient with mental switching. Modern distributed systems don’t need to be constrained by our limitations.

## Batch Thinking in ML
In our daily lives, we don’t process the world based on “batch updates.” We process information continuously, reacting and adapting to evolving contexts. Yet, historical limitations led to batch processing becoming the default paradigm.

Traditional machine learning mirrors this batch-oriented thinking. Models are operationalized around a rigid, linear workflow:

**Gather training data**: A domain-specific static data set is collected, often representing a snapshot in time.**Feature engineering**: The data is preprocessed, refined and prepared for the model.**Train the model**: The model is built based on the curated data.**Test the model:**Some portion of existing data is isolated from training data and used to test the efficacy of the model against some predefined performance threshold.**Deploy the model**: Once deployed, the model becomes a fixed artifact, queried for predictions.
![Batch process for traditional ML](https://cdn.thenewstack.io/media/2024/12/60cfd098-image2a-1024x493.png)
Batch process for traditional ML

While effective for specific use cases, this process is inherently rigid and lacks adaptability.

In contrast, one of the reasons generative AI is so transformative is because foundation models are inherently reusable and capable of solving diverse problems across many domains. However, to make these models reusable across various domains, data must be contextualized during prompt assembly — a need that batch processing simply cannot fulfill.

## LLMs Can’t Drive Value Without Contextualized Data
Let’s consider a simple example. Imagine we were to create an AI-powered flight assistant that helps customers when their flights are delayed.

![Example interaction between a user and an AI flight assistant.](https://cdn.thenewstack.io/media/2024/12/4a09338a-image3a-1024x398.png)
Example interaction between a user and an AI flight assistant

In the two-turn interaction above, there’s a lot of context needed to serve the needs of the customer.

The LLM needs to remember that the city in question is New York. It needs to know the customer identity and current bookings, current flight information, departure and arrival times, seat layouts, seating preferences, pricing information and airline change policies.

In contrast to traditional ML, where the model is trained on app-specific data, LLMs are not trained on your data; they are trained on general information. The app-specific data engineering happens during prompt assembly rather than model creation.

![LLM re-usability and customization through prompt assembly](https://cdn.thenewstack.io/media/2024/12/07822f07-image4-1024x579.png)
LLM reusability and customization through prompt assembly

In a world where [two medical papers are published every minute](https://nature.com/articles/nj7612-457a#:~:text=In%20the%20biomedical%20field%20alone%2C%20more%20than,year%20%E2%80%94%20about%20two%20papers%20per%20minute.&text=Each%20day%2C%20she%20scans%2030%E2%80%9350%20papers%20through,each%20consisting%20of%205%E2%80%9320%20papers%20and%20articles.) and [8,400 legal cases are resolved every hour](https://www.ncsc.org/__data/assets/pdf_file/0017/53216/Delivering-Timely-Justice-in-Criminal-Cases-A-National-Picture.pdf), static data is insufficient. AI systems need real-time, fluid data to deliver on their promise. Persisting with batch-oriented systems, despite better alternatives, constrains the potential of modern applications, especially in AI. It’s time to rethink this outdated approach and embrace architectures that reflect how we live and work in a dynamic, real-time world.

## LLMs Are Extroverts
As we design the next generation of AI applications, we risk falling into the same batch-oriented trap. We treat LLMs like databases — reactive tools that wait for inputs and respond to specific queries. But this mindset is fundamentally mismatched with what LLMs are capable of. AI isn’t just about holding information; it’s about reasoning, generating and evolving.

Where [databases are introverts](https://www.confluent.io/blog/how-change-data-capture-works-patterns-solutions-implementation/), holding information close until explicitly asked, LLMs are extroverts, designed to engage, synthesize and proactively contribute. They thrive in environments where the context is constantly changing and require architectures that can support this dynamic behavior. A batch-oriented approach, where models and data are periodically updated but otherwise static, stifles the true potential of generative AI.

To truly unlock the potential of AI, we need to shift our thinking.

AI systems should be proactive participants in the workflow — contributing ideas, engaging in dynamic conversations, and, in some cases, operating autonomously. This requires an architectural overhaul. Instead of static, query-response systems, we need event-driven architectures that enable fluid, real-time interaction and adaptation.

## How Stream Processing Unlocks AI’s Potential
The need for data streaming platforms arose from the inadequacy of batch systems to handle real-time demands. In fields like finance, telecommunications and e-commerce, where milliseconds can determine success or failure, batch-oriented architectures can’t keep up. Applications are needed to detect fraud as transactions occur, update stock levels as products are sold or provide real-time personalization during customer interactions.

![High-level view of stream processing](https://cdn.thenewstack.io/media/2024/12/341d7db8-image5-1024x371.png)
High-level view of stream processing

Stream processing platforms addressed these gaps by enabling continuous, event-driven workflows that aligned with the needs of dynamic, fast-paced systems.

## Stream Processing for Generative AI
Most practical use cases of generative AI thrive on real-time, contextual data. Stream processing platforms complement these models by solving critical challenges that batch systems cannot address.

**Real-time contextualization**: LLMs[require up-to-date data](https://thenewstack.io/enterprise-ai-requires-a-lean-mean-data-machine/)to generate meaningful responses. For example, an AI-powered flight assistant needs immediate access to flight delays, cancellations and rebooking options. Stream-processing platforms provide this real-time context, ensuring the AI has the information it needs when it needs it.**Dynamic decision-making**: Generative AI systems can do more than just respond to queries. Stream-processing platforms allow AI to react dynamically to changing inputs, such as adjusting product recommendations when stock levels change or responding to new legal cases as they’re published.**Scalable, decoupled architectures**: LLMs often need to integrate with multiple systems, from CRMs to analytics platforms. Stream-processing platforms enable a decoupled architecture, where each component can operate independently while consuming the same data streams. This avoids the bottlenecks and rigidity of batch systems, allowing AI applications to scale effectively.**Reducing latency in AI workflows**: In batch systems, the delay between data collection and processing can lead to outdated insights. For instance, a batch-updated vector database storing customer data might recommend a product that is already out of stock. Stream processing eliminates this latency, keeping AI workflows aligned with real-world conditions.
## Agentic AI: AI That Acts, Not Waits
The rise of agentic AI has fueled excitement around agents that move beyond simple query-response interactions. These systems can autonomously initiate actions, make decisions and adapt to changing environments.

Consider a typical AI agent. We can think of the agent as an automated process that reasons about its environment and proactively takes action to achieve some specified goals. Its decision-making may be complex, incorporating conditional, branching logic influenced by intermediate data queries.

It may need to pull data from multiple sources, handle prompt engineering and RAG workflows, and interact directly with various tools to execute deterministic and stochastic workflows. The orchestration required is complex, with dependencies on multiple systems. And if the agent needs to communicate with other agents, the complexity only increases. Without a flexible architecture, these dependencies make scaling and modification nearly impossible.

![Overview of agent dependencies](https://cdn.thenewstack.io/media/2024/12/ef92ed8c-image6.png)
Overview of agent dependencies

To achieve this, they require:

**Continuous awareness**: Real-time streams of events, such as changes in inventory, user behavior or system states.**Contextual reasoning**: The ability to synthesize dynamic data to infer intent and plan actions.**Autonomous decision-making**: Acting without waiting for explicit user instructions, such as rebooking flights or adjusting system configurations on the fly.
For example, an AI-powered travel assistant using stream processing could autonomously monitor flight schedules, identify delays, rebook affected flights and notify the user — all without manual intervention. This level of autonomy would be impossible with static, batch-updated data.

Stream-processing platforms meet these demands by delivering the infrastructure necessary for continuous, low-latency data flows and real-time computation. Without this foundation, the vision of autonomous, collaborative AI systems remains out of reach.

## Stream Processing Is the Future of Generative AI
Generative AI represents a paradigm shift in the way we build and use technology. But to unlock its full potential, we need systems that align with the way AI processes and generates insights — continuously, dynamically and in real time. Stream-processing platforms provide the foundation for this evolution.

By integrating AI applications with stream processing platforms, we can:

- Move from reactive to proactive AI systems.
- Enable real-time personalization and decision-making.
- Ensure LLMs operate on the freshest, most relevant data.
- Create scalable, flexible architectures that can evolve alongside AI advancements.
Generative AI is not just about building smarter systems; it’s about building systems that reflect the way we experience the world: as a continuous, ever-changing stream of events. Stream processing platforms make this possible, bridging the gap between the static systems of the past and the dynamic, AI-powered future.

To learn more, visit [www.confluent.io/generative-ai/](https://www.confluent.io/generative-ai/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)