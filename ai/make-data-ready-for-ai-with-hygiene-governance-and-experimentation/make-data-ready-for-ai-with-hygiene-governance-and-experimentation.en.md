Is your data ready for AI?

As more and more organizations enter the planning stages of AI adoption, it’s a serious question. Answering it properly poses serious challenges.

Part of this problem stems from expectations and bottlenecks.

AI models are flashy, innovative, and everywhere. They’ve become literal household names in a few short years. It’s understandable then that models would seem like the natural starting point for AI. But it’s not models that create the real bottleneck in AI adoption.

It’s data.

In this article, I’ll explore why many AI initiatives stall, not because of model limitations, but because organizations struggle to consistently provide clean, governed, and context-rich data to these models. I’ll show why trusted, high-quality data, not just more models, is the real backbone of effective AI.

## Why AI Projects Stall Because of Data

AI is a complex technology. To be successful, [AI requires data](https://www.starburst.io/blog/ai-data-quality/).

The most advanced models in the world can’t deliver value without a rock-solid data foundation. AI is only as good as the data that feeds it, but also as the hygiene, governance, and experimentation needed to make it work.

### The Importance of Data Access for AI

And underneath all of that is another problem: Data access. Without strong data access, models can’t use the data they need.

And it isn’t causing hypothetical problems; it’s causing real technological headaches. There is a disconnect between model demos and the reality of enterprise AI projects that stall.

Overall, this means that data quality and governance are only half the battle; operationalized experimentation is the missing ingredient for AI maturity.

In essence, this raises two core issues that work in tandem:

* Data federation for rapid experimentation and prototyping.
* Iceberg data lakehouses for scalability and production.

Let’s look at each of these in more detail.

[![](https://cdn.thenewstack.io/media/2025/10/39447135-image1-300x236.png)](https://cdn.thenewstack.io/media/2025/10/39447135-image1-300x236.png)

## Why Data Federation Is the Answer to AI Data Access

Data access cannot be an afterthought. Too often, the way around this problem has been a one-way path to data centralization in a data warehouse.

The problem with this is that it rarely works. When it does work, it is always expensive and time-consuming. Worst of all, the end state results in vendor lock-in, which curbs the ability for experimentation and [limits the adoption of future technologies](https://thenewstack.io/facing-technologys-limits-at-albuquerques-balloon-fiesta/), strategies, and approaches.

Solving this problem requires a different approach.

### How Data Federation Helps Data Access

Instead of moving data, federation makes distributed datasets accessible wherever they live, applying governance and fine-grained access controls along the way. This solves the data access problem in an elegant and sophisticated manner, enabling access to any data source now or in the future.

This has one particular advantage: **The ability to experiment**.

### How Data Federation Improves Experimentation Speed

Model [development is an iterative](https://thenewstack.io/ai-in-agile-managing-the-unpredictable-in-iterative-development/) process. Data scientists rarely know the exact shape of the features they need at the outset. Instead, they experiment, test hypotheses, and refine iteratively.

The Federation assists this effort, directly enhancing experimentation.

By making distributed datasets queryable where they live, data scientists can explore data from multiple sources without waiting for lengthy ETL cycles. This strategy accelerates prototyping, shortens feedback loops, and gives [teams the agility](https://thenewstack.io/can-agile-teams-have-a-design-first-approach-to-apis/) to explore more ideas in less time, improving a connection to the underlying business logic.

Once you’ve done those experiments, created those prototypes, and reconciled that business logic, another phase begins.

Scaling. This is where data lakehouses show their second benefit.

## Why Open Lakehouses Are a Game-Changer for Scaling AI Adoption

Data lakehouses are built to scale quickly and easily. By standardizing access through formats like [Apache Iceberg](https://www.starburst.io/blog/apache-iceberg/), teams can query data across the cloud, on-premises, and hybrid environments without locking their data into proprietary systems.  Additionally, as data volumes grow, lakehouses allow AI applications to grow with them, scaling efficiently, without the associated costs of a data warehouse.

The result is a model where data is both usable and governed, enabling analytics and AI to [operate on the same trusted](https://thenewstack.io/zero-trust-security-for-distributed-applications-with-dapr-open-source/) foundation.

### How To Adopt AI Successfully Through Iteration

A practical path to AI adoption begins with using the data you already have, where it lives.

From there, organizations can decide how much to centralize, balancing cost, compliance, and performance. Once consistent access is established, teams can iterate: experimenting on governed branches of data, validating results, and adapting quickly.

This cycle of access, choice, and experimentation is what turns AI from pilot projects into production outcomes.

## 

## How Data Products Are Essential for AI Data Governance

After you’ve solved the data access issue, the next major step in building your AI solution is solving for data governance. Without this, AI projects often cannot even get off the ground.

Given this, data governance is a necessary hurdle for any AI project to overcome, and although the need for data governance is often organizational or legal, the solutions to it are thoroughly technological.

Typically, designing data governance for AI follows three key milestones before an AI project can begin:

* Data security
* Data quality
* Business meaning

Without data security, any AI project is a nonstarter. All organizations require security at both the data source level as well as the agentic layer as a foundational aspect of their AI usage. Similarly, without quality data, the insights that AI will provide will be limited and problematic. Finally, if the business logic is not properly encoded into the data in the form of valuable metadata, the value to the [business will be limited and the insights](https://thenewstack.io/data-unleashed-unlocking-powerful-business-insights/) will be generic.

### Why Data Products Apply Product Thinking to Data

Data products are the single most important innovation in the area of governing access to data for AI. They provide an easy, accessible, and secure way to interact with underlying datasets, while also [delivering critical business](https://thenewstack.io/five-steps-to-build-ai-agents-that-actually-deliver-business-results/) meaning and semantics.

For AI projects, data products allow universal access to be governed appropriately, ensuring that AI models only receive the right data in the right way. Additionally, the business metadata and semantics improve the quality of model responses and reduce hallucinations.

This is the right choice for data access, but it’s also the right choice for compliance and regulatory oversight, which often demands that AI access be predictable and verifiable.

In project after project, we find similar problems in AI adoption. The models are already in place, but the issues of access and governance need to be addressed together.

It’s useful to look at an [example to see how this operates in practice](https://thenewstack.io/understanding-the-python-and-operator-usage-examples-and-best-practices/).

## 

## Case Study: How a Financial Services Company Powered AI, Without Moving Data

One of our customers, a large financial services company, faced one of the hardest problems in the industry: Creating Customer360 insights and risk analysis, within the context of regulatory requirements and operational systems.

Traditionally, solving this required replicating sensitive data into centralized systems, [creating compliance risks and slowing response times](https://thenewstack.io/physicists-create-time-crystals-using-new-quantum-computing-architecture/).

### How a Financial Services Company Used Data Federation

Instead, the financial services company adopted a federated approach. By leaving data in place and making it queryable where it resided, they enabled real-time customer and risk-based decision making without creating costly duplication and allowing analysts to rapidly iterate on questions. In addition, adopting a lakehouse strategy played a key role, giving the company governed, auditable tables that scaled to global workloads.

### How a Financial Services Company Adopted AI Successfully

The result was a system capable of scanning transactions as they arrived, surfacing real-time insights as they occurred, and supporting follow-up activities with governed access to the right data in the right context. Importantly, the same governed datasets that underpinned compliance workflows also powered AI models for Customer360 creation.

### Conclusion: AI Adoption Starts With Data

This approach showed what AI maturity looked like in practice. It was not just about deploying advanced [models but ensuring that clean](https://thenewstack.io/clean-data-trusted-model-ensure-good-data-hygiene-for-your-llms/), governed, and federated data was available on demand and without compromising compliance.

## Building a Successful Data Foundation for AI

It’s easy for AI projects to feel disconnected from other data projects. Despite the [power and revolutionary nature of AI models](https://thenewstack.io/right-sizing-ai-for-the-edge-power-models-and-security/), the success of AI projects often comes down to three things:

* Data access
* Data governance
* Data products

Without those foundational building blocks, AI models struggle to obtain the necessary access, and projects are hindered because they lack the governance to operate in a compliant manner.

### We Have the Tools to Solve These Problems

The good news is that we can solve these problems. Moreover, they’re actually the same problems that data engineers have been solving for years, with the additional technology of the AI model serving as the endpoint.

Seeing the problem in this way is good news for anyone tasked with rolling out a successful AI project. It means that the tools are in your hands, and the methodologies are too.

Approaches like data federation and data products were already useful in analytics. Now, they’re critical in AI.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/10/e18fb96c-1586830365427.jpeg)

Brian Luisi is Starburst VP of Technical Solutions and a veteran in the data space. He has worked at Starburst for well over six years, helping Starburst customers in their journey to AI and building the Solutions Architect, Support and...

Read more from Brian Luisi](https://thenewstack.io/author/brian-luisi/)