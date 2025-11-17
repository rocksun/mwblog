Your [AI success](https://thenewstack.io/ai/) relies on your data. The more unified your data is across your organization, the more your AI strategy will deliver. But unlocking that value is far from straightforward, especially in light of siloed and sprawled data sources.

“You have these different lines of business,” said Joe Giordano, chief architect in the [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) field CTO organization. “They’re really all interested in different data, don’t necessarily know where all the data resides and they don’t have access to it.”

This has organizations struggling to find cross-sectional AI use cases. Or, as recent research out of MIT NANDA found, [95% of AI pilots fail](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) due to experimentation locked within data silos.

As engineering leadership, 2025 was likely the year you made AI your top-down priority. Want a resolution for 2026? Clean up and organize your internal data within an [internal developer platform](https://thenewstack.io/platform-engineering/platform-engineering-what-is-it-and-who-does-it/) so that you can actually deliver on last year’s goals. Here’s how.

## Acquire and Prepare Your Data

You don’t know what you have. Because data silos are real and even if you break them down and find all your data sources, they aren’t speaking the same language.

The business value of AI comes from cross-organizational data translation. But it’s not simple.

### Find and Label Data

Within financial services, for example, there are segregated divisions like wealth management and asset management. But, for AI adoption, Giordano said, they are essentially trying to do the same thing, although maybe one has the data stored in [Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention) and another on premises. AI data discovery kicks off with awareness of other services, databases and use cases across the business, but also recognition that an enormous amount of data is stuck in spreadsheets and PDFs.

Once data is found, it then has to be cleaned and labeled. Within the same financial services organization, the same raw data — for example, the record of a customer’s debit card purchase at their local coffee shop — can be labeled differently depending on the department:

* **Marketing and sales:** Given the goal of understanding customer behavior and target offers, labels can include `discretionary spending`, `food and drink`, `daily commute`.
* **Risk and fraud:** Depending on the location and regularity of this purchase, labels may include `normal transaction`, `high-risk location`, `possible account compromise`.
* **Regulatory compliance:** On the bank’s side, labels may include `AML monitoring flag` (referring to anti-money laundering), `low-risk transaction`.

Since AI is good at understanding relationships and at translating, it can be very useful in creating a cross-organizational, unified data model, which can be used to help train your large language models (LLMs).

“Scaling AI means unifying real-time layers across voice, text, search and transactions while embedding privacy, compliance and federated learning,” said Dana Lawson, CTO at Netlify. “Enterprises earn trust because of their privacy and security reputation — and they’ll need to extend that rigor to new AI-driven pipelines.”

A [platform engineering strategy](https://thenewstack.io/platform-engineering/) can help both with AI-backed discovery of these different data sources and the API endpoints that connect them. Then, you can add an internal chatbot overlay to make the data more searchable, translatable and usable across functions.

An [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") is also the industry-standard way to lay down golden paths, or the easiest way to achieve something with your data and code while remaining within guardrails to support your privacy and security requirements.

### Unlock Unstructured Data

Naming isn’t the only data disparity to tackle.

As Patrick Debois, coiner of the term “DevOps,” put it: “Much of the information within your company is unstructured data, and you want to index that information.”

Most organizations use a vector-based database, “which is similar to a search engine but a semantic search envoy,” he explained.

While structured data fits neatly in a spreadsheet, [unstructured data](https://thenewstack.io/beyond-ai-models-data-platform-requirements-for-agentic-ai/) — ranging from emails, PDFs, slideshows and social media posts, to audio and video files, to machine-generated data from things like sensors and satellites — is everything else.

If your organization can make sense of it all, you can potentially unlock the true value of AI. Again, AI is really good at reading information — even that which is stuck in a PDF or a scanned form from 20 years ago — and then making sense of it within a bigger context. You just need to decide, within your organization’s context, what is actually useful data to include.

## Preprocess and Clean Data

Next comes data preprocessing and cleaning to reduce “noise” or irrelevant information. Then, the translation of that unstructured data into a numerical representation, which can then be labeled and annotated.

Any AI strategy also has to consider stateful and stateless workloads.

So much of our cloud native, container-based world has been grounded in stateless workloads, where the application doesn’t retain the data or “state” from one request or transaction to the next.

Stateful workloads, on the other hand, retain persistent, reliable and consistent data within context and across sessions, requests and even application restarts. Common stateful use cases are databases, financial systems, real-time communication, email servers, messaging queues, content management systems and e-commerce shopping carts.

Any AI data strategy has to govern these different use cases with the highest level of security in mind.

## Centralize Data and Make It Accessible with a Platform

Once it’s cleaned up, you must centralize this data into a unified database or data lake. Include disparate data sources from within the organization and via third-party APIs, as well as relevant industry open data sources.

That data is best unified and shared in the cloud — whether public, private or hybrid cloud. And you must monitor it all to detect drift and ensure compliance and accuracy. A platform approach also enables you to measure performance against your service-level objectives (SLOs).

Data needs to be treated like infrastructure, explained Red Hat’s Giordano: “We need to continuously monitor it for these changes. An application is not necessarily changing or evolving on its own when it connects to a database.”

A cross-enterprise AI strategy needs a platform to unite the data discovery and manage access to it. This data pipeline must also be set up in an auditable way.

This arduous but important data preparation and centralization process demands a [platform-led approach](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/), with perhaps the platform engineering team — partnering with data science and the AI office — coordinating this centralization, data cleaning and role-based access control (RBAC).

A platform is also the preferred way to enable self-service access, which cuts the time needed to achieve a return on investment (ROI) for your now curated data and AI program.

In the end, the ROI on your AI has to apply to business and processes. And while the unique value of your AI strategy comes from your data, it all comes down to the cross-functional, cross-organizational conversations it facilitates.

***Sign up now to be one of the first to receive my free new eBook: [AI for the Enterprise: The Playbook for Developing and Scaling Your AI Strategy](https://thenewstack.io/ebooks/generative-ai/ai-for-the-enterprise-the-playbook-for-developing-and-scaling-your-ai-strategy/?utm_source=Jen+Riggins&utm_medium=referral&utm_campaign=Series13Book2).***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)