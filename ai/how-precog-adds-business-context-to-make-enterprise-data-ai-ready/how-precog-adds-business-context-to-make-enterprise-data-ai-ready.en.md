Extracting data from enterprise tools like Salesforce, [SAP](https://www.sap.com/index.html?utm_content=inline+mention) Ariba, or NetSuite is relatively easy. Making that [data usable for AI models](https://thenewstack.io/ai-data-dilemma-balancing-innovation-with-ironclad-governance/) to reason over is much harder. Just having massive amounts of tables and columns or giant multidimensional JSON files isn’t going to help those models reason over that data. What’s missing here is the business context in which the data was generated.

[Precog](https://www.precog.com/), which focuses on helping businesses extract data from Software as a Service (SaaS) API sources and prepare it for use in analytics or AI applications, is launching a new feature today that will bring this business context back into the extraction process.

## The challenge of preparing enterprise data for AI

The manual process of prepping data for AI analysis can take months, Precog’s CEO [Jon Finegold](https://www.linkedin.com/in/jfinegold/) says in an interview ahead of the launch.

“When you get into the enterprise and you want to start analyzing your mission-critical business data, it tends to be siloed in various applications, sometimes over 100 applications in the enterprise,” Finegold says. “And then the process to get it from those applications — not just to extract it and load it, but to give it enough context so that the models can actually make sense of it — is a very manual process.”

And despite their ever-increasing capabilities, large language models (LLMs) are also not exactly dependable when it comes to reasoning over large amounts of data.

“If someone hears that they’re gonna send all of their data off to Gemini, not only is the chunking and tokenization, etc., incredibly expensive, but also your answers are gonna be different every time you call it,” Finegold noted.

![A diagram of Precog's data ingestion platform.](https://cdn.thenewstack.io/media/2026/01/0a8978fe-precog_architecture-semantic-modeling-fnl-scaled.jpg)

Precog’s data ingestion platform. (Credit: Precog)

## How Precog adds business context to data

To get around all of this, Precog is taking a different approach to helping its customers get more value from their data. When a Precog user wants to configure a new source for use in an AI application, they can now broadly describe their use case (e.g., “I want to understand which customers are the most profitable and which are losing us money”). Precog will then use its existing ETL capabilities to look at the data that is available in your SaaS application and only extract the required fields for this specific use case, and add the necessary context to help the model understand the meaning of each of these fields.

What’s important to note here is that Precog never actually passes company data to the LLM. Instead, it loads the actual data into a data warehouse and only passes the metadata to its semantic engine.

## Generating synthetic questions to build semantic models

One nifty aspect of how Precog built this system is that it also uses another model to automatically create hundreds of potential questions — you can think of it as synthetic question generation.

As Precog Chief Product Officer [Becky Conning](https://www.linkedin.com/in/becky-conning-5a3930165/?originalSubdomain=uk) notes, the idea here is to generate a “matrix of questions that’s going to allow the LLM to generate the semantic model to be able to answer all those questions.”

All of this is necessary, Conning argues, because simply building a giant semantic that’s tied to a single normalized table will only be able to answer a very limited set of questions.

## Leveraging LLMs for natural language-to-SQL queries

Meanwhile, including all the data doesn’t work either. “If you include all of the data — and some of these applications have hundreds of thousands of datasets in them, each one which might not just represent one table due to the JSON structure, it may include sort of dimensional information as it breaks down — then Cortex just doesn’t work. And really, any of these NLQ LLMs do not work.”

The advantage of modern LLMs is that they are very good at turning natural language queries into SQL, so to query the data, Precog doesn’t rely on a model directly — and doesn’t feed data to that model — but instead uses [Snowflake](https://www.snowflake.com/?utm_content=inline+mention)’s Cortex NLQ LLM. The service could also use another LLM, but the team noted they do like Cortex NLQ for this use case.

Overall, this looks like a smart way to use LLMs for what they are best at without trying to shoehorn them into a use case where they are far more likely to fail than existing technologies.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)