# Case Study: AI Agent Cuts API Connector Dev Time to Minutes
![Featued image for: Case Study: AI Agent Cuts API Connector Dev Time to Minutes](https://cdn.thenewstack.io/media/2025/04/661937e6-ai_created_connectors-1024x579.jpg)
Image by Getty Images via Unsplash

The software development company [Fractional AI](https://www.fractional.ai/) believes that AI’s biggest winners will be the non-AI companies that use generative AI to make their operations more efficient and to improve their products.

To that end, Fractional AI created an [AI agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) for open source data integration company [Airbyte](https://thenewstack.io/pyairbyte-airbytes-new-python-library-for-moving-data/) that builds connectors for [API](https://thenewstack.io/use-api-governance-tools-for-better-api-experiences/) integrations. But instead of taking days to hand code, these AI-created connectors are made in mere minutes.

“We’re growing really fast, and it’s been fun,” [Chris Taylor](https://www.linkedin.com/in/taylorcd/), CEO of Fractional AI, told The New Stack. “Been a lot of fun [working] on a lot of cool projects at the forefront.”

Airbyte is an [open source data integration engine](https://github.com/airbytehq/airbyte) for moving data to warehouses, [data lakes](https://thenewstack.io/observability-without-a-data-lake-might-no-longer-work/) or databases. It’s often used to extract data from Software as a Service products, which of course requires connectors to those SaaS APIs.

For example, if someone wanted to combine [Shopify](https://thenewstack.io/recreating-shopifys-bfcm-globe-using-react-globe-gl/) sales data with [ZenDesk](https://www.zendesk.com/) customer support, Airbyte could be used to set up a data pipeline to extract the customer data from Shopify and the customer support tickets from Zendesk to load it all into a data warehouse.

Airbyte already had a library of connectors to support that integration work — but the company envisioned simplifying the creation of thousands more connectors to SaaS products.

“Their software is pulling data out of third-party [SaaS](https://thenewstack.io/goodbye-saas-hello-ai-agents/) tools and moving data into data warehouses,” [Eddie Siegel](https://www.linkedin.com/in/eddiesiegel/), Fractional AI’s CTO, told The New Stack. “They need to build an integration with every third-party SaaS tool type tool that that that might exist.”

Airbyte calls the solution [AI Assistant](https://airbyte.com/blog/hands-on-with-the-new-ai-assistant), and it’s working well. Since the tool’s release, significantly more connectors have been added to its library.

![Chart showing Airbyte connectors made before AI Assist and climbing significantly after the introduction of AI Assist.](https://cdn.thenewstack.io/media/2025/04/0aad9a47-fractionalaiairbyteconnectors_built-1024x658.jpg)
Image Courtesy Fractional AI

## Building APIs Pre-AI
Building Airbyte’s solution wasn’t as simple as handing API documentation to the AI tool. Airbyte wanted an automated solution that would scan the API documentation, which tends to be somewhat randomly structured.

“What we realized was these developer-facing API docs are extremely complicated websites,” Siegel said. “They’re the kinds of pages that [Google](https://cloud.google.com/?utm_content=inline+mention) doesn’t index very well; they’re highly dynamic. They’re not designed by someone that wants it to be well indexed.”

API documentation isn’t standardized and can often be thick and dense reading material. Crawling these documents ended up being an unexpectedly complex problem Fractional had to solve before it could even involve the AI.

“They’re not making it very easily readable by web crawlers,” Siegel said.

Due to the context window size, he added, “The process of tuning the crawling was maybe an order of magnitude more difficult than we expected going in on the AI side of things.”

Once the documentation is poured through, developers face a lot of manual coding. The time-consuming, complex process diverted technical talent from higher-value work, as the [case study on Fractional AI’s website](https://www.fractional.ai/case-study/api-integrations-in-minutes-how-fractional-ai-airbyte-10xd-the-speed-of-building-connectors) noted.

## The AI/Developer Workflow
The resulting workflow allows users to input the URL for the API with which they are trying to integrate. The AI Connector Builder crawls those API documents, then pre-populates all the fields about the connector, such as the API URL base and authentication.

The AI Connector Builder then presents the full list of streams for that API — for example, for Shopify, the streams might include “orders,” “fulfillments,” and “discounts.”

The user then selects the streams of interest and for each stream selected, the Builder pre-populates each field (pagination, URL path, etc.) for those streams into Airbyte’s connector builder UI. The user can then review the AI’s draft and make edits or corrections before finalizing the connector.

So, basicall,y the ultimate workflow for the AI tooling has five parts:

- Scrape the documentation page.
- Large language model-powered crawling engine finds additional pages to scrape.
- Convert HTML to markdown and remove as much noise as possible.
- Extract the appropriate sections from the scraped pages and include them in carefully crafted, purpose-built prompts.
- Translate LLM output into appropriate sections of connector definitions.
## An AI Assist Under the Hood
Under the hood, AI Assistant leverages [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/). The team explored 4o-mini and a fine-tuned version of the 4o-mini but only ended up using [4o-mini](https://thenewstack.io/openais-realtime-api-takes-a-bow/) for integration tests. [Claude](https://claude.ai/) was also considered, but GTP-4o was chosen because of its strict structured output capabilities, the case study noted.

Fractional AI used [OpenAI’s](https://openai.com/) software development kit (SDK) to stitch together the prompts.

The first step is reading the API documents. The AI system starts with, “Is there an [OpenAPI](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) spec?” If so, it can pull the authentication parameters directly from the OpenAPI specs.

But if there’s no OpenAPI spec, Fractional AI crawls the API documentation using the AI search tool [Jina AI](https://jina.ai/) and [Firecrawl](https://www.firecrawl.dev/), which is an API service that takes a URL, crawls it and converts it into clean markdown or structured data.

“Finally, if we are unable to extract the information using the OpenAPI spec, Firecrawl, or Jina, we use a combination of services,” such as [Serper,](https://serper.dev/) a web scraper, and [Perplexity](https://www.perplexity.ai/), the AI search engine, “as a last-ditch effort to find relevant information to input to later [LLMs](https://thenewstack.io/ai-agents-are-dumb-robots-calling-llms/),” the case study noted.

The second step is to extract the relevant API connector sections. If the document is so large that it exceeds the context window, Fractional AI uses [OpenAI’s built-in retrieval augmented generation (RAG)](https://thenewstack.io/openai-rag-vs-your-customized-rag-which-one-is-better/) functionality to extract sections in the documentation related to authentication.

For smaller documents, Fractional built a flow to first extract links from the HTML then ask an LLM which links look related to authentication, then it embeds the content of the scraped pages into future prompts.

Finally, the process involves parsing and prompting the exact details from the HTML chunks. The challenge was coercing the LLM output into the exact format needed for the connector builder specification. Fractional’s solution was to “prompt with structured output to determine the authentication method in the specific format to populate the connector builder.”

Other tools used in the final solution were [Langsmith](https://www.langchain.com/langsmith), which is a platform that helps developers build, debug, test and monitor LLM applications, for observability and experimentation. Fractional also leveraged OpenAI’s built-in [vector store, where RAG was required,](https://thenewstack.io/how-to-store-embeddings-in-vector-search-and-implement-rag/) and [Redis](https://redis.com/?utm_content=inline+mention) was leveraged for caching and locking.

“We use the catalog of existing [Airbyte connectors](https://airbyte.com/connectors) as benchmarks to measure the accuracy of the AI-powered Connector Builder and improve quality,” the Fractional AI case study noted.

Although the case study doesn’t detail the test data, it notes that preparing it “took significant effort … and should be a significant focus for any applied AI project.”

In the final analysis, Fractional AI’s case study stated there are “many high-ROI places where the right AI applications can dramatically increase developer productivity.”

“Both an engineering and an AI problem: This project is a good reminder that the challenges getting AI into production aren’t pure issues from wrangling LLMs,” the team wrote. “In this case, quality crawling — a challenge as old as [Google](https://thenewstack.io/ironwood-googles-answer-to-nvidia-in-the-ai-chip-wars/) — posed a major challenge.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)