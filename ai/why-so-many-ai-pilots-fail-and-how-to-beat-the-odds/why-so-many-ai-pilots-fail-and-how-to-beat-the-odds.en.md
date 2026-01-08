In mid-2025, a widely publicized report claimed that almost all AI pilots fail. While there’s been some [debate](https://thenewstack.io/how-mits-project-nanda-aims-to-decentralize-ai-agents/) around the reported failure rate, there are obvious reasons why some [AI projects are successful](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436665742;dc_trk_aid=629928261;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) while others never make it past the pilot stage.

In my experience, much of what makes or breaks an AI project is connected to how well it’s set up — from the start — to identify and fix the major operational challenges that can stand in the way of success.

## **An Ideal World**

Consider what an ideal environment for developing AI applications would look like: You would have access to abundant resources, starting with a dedicated, diverse, complete and unsiloed team necessary to pilot, develop and launch an AI app.

From the outset, you would [optimize observability](https://thenewstack.io/how-can-we-solve-observabilitys-data-capture-and-spending-problem/), so you can continually monitor the complete system. You would also collaborate with your security team to establish security checks and balances.

You would ensure that everything runs in a pipeline, and every new AI project runs through the same pipeline, enabling repeatability and making it easier to accommodate any guardrails set up to protect the app and its users.

In this ideal world, you would have everything in place to help you identify and close any workflow gaps before they become an issue. The development process would no longer be hindered by stop/go gates; it would become a continuous cycle, from pilot to development to production, enabling you to get your AI product out the door faster.

Sounds idyllic, right? But back here in the real world, can you put any of this into practice?

## **Common Challenges in Developing AI Software**

Teams developing and deploying AI software face substantial challenges, particularly when they’re moving from internal testing to application production and scaling. Since AI is inherently probabilistic, developers cannot account for every possible edge case. Introducing diverse external datasets and variables often causes AI software to “fall over.”

Whether you’re developing a chat-based AI system, an agent operating behind the scenes, an algorithm or an advanced analytics tool, the application finds patterns and makes correlations across different datasets. In a chat-based system, the AI converts natural language into a machine-readable format for analysis, and then translates the findings back for the human user.

The standard software development life cycle (the classic [DevOps cycle](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.437165523;dc_trk_aid=629929182;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) of “test, repeat and build”) is even [more complex](https://thenewstack.io/how-ai-is-reshaping-the-software-development-life-cycle/) with AI systems. This is partially due to new AI-driven requirements such as preparing the data, auditing the models, conducting performance testing and retraining the models.

## **How Security Friction Slows Delivery**

A major hurdle to developing AI is security friction, largely rooted in distrust over how AI or third parties might use their data. Companies want to be certain that the AI is not being trained with their data, nor will their data be stolen or stored on an external server used by the AI.

To manage these risks, companies have implemented numerous security guardrails to prevent AI from being used for malicious purposes, such as stealing data or introducing bias. However, the time required to move an AI product through these extensive guardrails and checkpoints slows down the process. Since technology moves very fast, the AI product may be outdated by the time it is approved.

One way enterprises try to prevent data theft is to establish internal [AI policies](https://thenewstack.io/how-to-create-an-effective-ai-usage-policy) that restrict the use of third-party AI tools. Many try to build and maintain (with frequent retraining) equivalent internal tools for employees, potentially using less performant models. But if the tools don’t meet users’ needs, “shadow AI,” where employees mask corporate data so that they can use prohibited external systems, will creep into the enterprise anyway.

> The team acts like a parent, setting boundaries and using automation to direct the AI back to the intended path as it learns from its surroundings.

Compliance with differing regulatory and governance requirements is another potential impediment. From data sovereignty rules, such as those that require data generated in the European Union to stay in the region, to complying with strict regulations like the EU AI Act, companies with a global footprint may need to create different work streams for different regions.

## **Why Workflow Gaps Break Automation in AI**

Many AI development workflows are highly siloed. Teams are disparate, with frontend, backend and data engineers, alongside data scientists, AI engineers and researchers. I’ve seen AI and data science teams build a model, “throw it over the fence” to the developer team for product integration, then move on to the next project.

However, as models drift and data changes, the AI system can evolve down the wrong path. For example, unlike traditional, static software, AI is organic; it changes and evolves as it learns. This can cause unexpected behavior, such as an AI deciding to move a user interface (UI) button to the bottom-right of the interface, or breaking established automations as it attempts to use its new knowledge to improve performance.

One solution to these workflow gaps is to create a new type of team to continuously maintain and monitor the model by collecting observability metrics such as [model drift](https://thenewstack.io/the-engineers-guide-to-controlling-configuration-drift/), confidence limits and user feedback. As needed, this team pulls the model back, retrains it or even removes it if it degrades too far. The team acts like a parent, setting boundaries and using automation to direct the AI back to the intended path as it learns from its surroundings.

## **The Risks of Insufficient AI System Observability**

Observability is crucial to managing and maintaining complex AI systems. The observability metrics you focus on may vary depending on the type of AI application.

For chatbots, key metrics include:

* **Tokens:** Monitoring input and output tokens allows you to track operating costs.
* **User success:** This assesses how well an answer worked for a user. Could the user use the response and complete a task? Or did they have to continue asking questions to get the right information?
* **Hallucination rate:** Does the large language model (LLM) provide incorrect answers, even if it’s confident its answer is correct? If so, when, where and how often does that happen?
* **Latency:** Monitoring how long the system takes to return a response is essential, as too much delay causes users to cancel.

For predictive models, you need to measure:

* **Confidence levels:** Monitoring the model’s predicted confidence score (e.g., 90%) will assess its reliability.
* **Model drift:** Regularly retesting against the original training data’s “base truth” will show if confidence levels are dropping, which indicates the model is becoming less accurate.
* **Feedback loop:** If a prediction fails, is the outcome fed back into the model to retrain it and adjust the variables that led to the incorrect result?

## **Understanding Cost and Infrastructure Limitations**

The [cost of running AI](https://thenewstack.io/finops-and-ai-a-winning-strategy-for-cost-efficient-growth/) is extremely high. And costs can skyrocket due to things like uncontrolled cloud compute, hiring or training for AI skills, and [model bloat](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436668922;dc_trk_aid=629927463;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1).

> If an AI response takes five minutes, it could be faster for the user to do the task themselves or to use conventional automation.

Infrastructure is another limiting factor. Companies operating in on-premises and [air-gapped environments](https://thenewstack.io/deploying-ai-in-air-gapped-environments-what-it-really-takes/) must procure their own GPUs. Since usage is often calculated per user, scaling to an organization with 1,000 employees quickly becomes expensive. Solutions involve using smaller models (like Mistral Small) that run on [fewer GPUs](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436822571;dc_trk_aid=629929521;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) or complex [virtual LLM](https://www.redhat.com/en/topics/ai/what-is-vllm) techniques to optimize parallel processing.

Alternatively, companies can use cloud infrastructure like Google’s Vertex AI, IBM’s watsonx or Amazon Bedrock, relying on the provider to manage the GPUs and paying a [consumption-based fee](https://youtu.be/Nism4CK2nqQ?si=Fq4krtHiGiAXrdVy) per token.

Most AI applications seem to rely on a few of the major AI players (e.g., OpenAI or Anthropic) for their underlying inference stack, which limits your ability to have control over the pricing.

You must also constantly battle rising tech costs and user expectations — if an AI response takes five minutes, it could be faster for the user to do the task themselves or to use conventional automation.

## **AI Pilots in the Real World**

The ideal world I described in the introduction, the one with nearly unlimited resources for developing AI applications, is elusive. But that doesn’t mean that you can’t put some of that into practice to overcome limitations in the real world.

The core to success is [full-stack observability](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436822574;dc_trk_aid=629758844;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) — continuously monitoring the system, understanding what is happening and correcting any issues before they become problems — powered by agentic AI. For more insight, get the [guide to full-stack observability for DevOps teams](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436822355;dc_trk_aid=629928258;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/9b01cb98-juliebanfield.png)

Julie Banfield is a Technical Product Manager and data scientist, holding a PhD in astrophysics. In her current role with IBM Concert, Julie bridges the gap between data science and product management around AI-powered solutions that solve complex business problems....

Read more from Julie Banfield](https://thenewstack.io/author/julie-banfield/)