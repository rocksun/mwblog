The seemingly unquenchable thirst of the AI data ingestion pipeline spans [language](https://thenewstack.io/7-guiding-principles-for-working-with-llms/), numerical, and tabular data in the first instance, while other tangential platforms have been building large audio, image, and video models at the same time.

Straddling potentially all of these domains are the file structures where complex documents and forms of [unstructured data](https://thenewstack.io/what-is-unstructured-data/) reside; this is the road less traveled in terms of the source DNA modern AI draws from.

## The schema-less, freeform, uncurated data lake

In a bid to bridge connections to the schema-less, freeform, uncurated information that all organizations naturally harbor, enterprise visual intelligence company [Valantor](https://www.valantor.com/) announced its acquisition of unstructured information RAG specialist [EyeLevel](https://www.eyelevel.ai/) on Tuesday. The acquisition formally launches Valantor’s Enterprise Visual Intelligence platform, combining EyeLevel’s document intelligence with its own operational expertise.

[Benjamin Fletcher](https://www.linkedin.com/in/benjamin-fletcher-bb73334/), CEO and co-founder of EyeLevel, tells *The New Stack* that where organizations fail to adopt visual intelligence, human-only processing breaks down pretty quickly in the age of AI.

“About [80% of corporate knowledge](https://www.databricks.com/blog/pdfs-production-announcing-state-art-document-intelligence-databricks) is in millions of pages of visually complex PDFs, PPTX, and DOCX files,” Fletcher says. “This information is far beyond the capacity of any LLM context window and is effectively inaccessible to LLMs and agents.”

> “We’ve found the golden datasets that teams build by hand routinely carry 10 to 25 percent error rates. Ironically, those same teams often hold AI to a far higher standard than their own people.”

## Humans are slow, expensive & prone to errors

He explains that transactional workflows (such as invoice and claims processing) typically involve documents “so visually complex and diverse” that enterprises still rely on humans to process them, who can be slow, expensive, and error-prone.

“We’ve found the golden datasets that teams build by hand routinely carry 10 to 25 percent error rates,” Fletcher says. “Ironically, those same teams often hold AI to a far higher standard than their own people. If data sovereignty matters to a business, everything gets harder now: solving these problems with AI while your documents stay inside your own infrastructure is the hard mode version of the job, and very few tools can do it.”

## Where does invisible corporate information live?

Valantor has noted that while most AI companies concentrate on models, the company itself is “focused on the information those models can’t see” today. The suggestion is that this unseen morass of valuable data is locked inside documents, claims files, contracts, engineering drawings, reports, forms, presentations, and other visually complex content.

Valantor’s flagship platform product, GroundX, operates where data resides, including private cloud, sovereign infrastructure, on-premises deployments, and fully air-gapped environments.

“GroundX is the ingestion and retrieval layer for unstructured documents,” explains Fletcher. “It is one tightly tuned system where retrieval consumes exactly what ingestion produces. Everything is exposed through REST APIs, SDKs, and MCP. It ships as REST APIs, SDKs, and MCP, and the Helm chart drops straight into a team’s existing deploy pipeline, and our agent harness gives coding agents like Claude and Codex the skills to build the integration themselves.

As part of the acquisition announcement, Valantor is introducing [GroundX Studio](https://www.valantor.com/#groundx-studio). The harness capabilities within GroundX Studio integrate with modern AI development environments, enabling developers to build secure AI applications that operate on enterprise knowledge while remaining within existing infrastructure.

GroundX Studio also extends capabilities to business users, allowing organizations to create AI-powered workflows and applications without extensive custom development.

> “Each agent does one small task, so cheaper models are often good enough, and teams that want direct control over cost can run the whole stack on their own hardware with Helm.”

## Risk of latency-laden performance and spiraling costs?

If it feels like this new data ingestion stream is going to place a new burden on cloud workloads, application execution latency, database retrieval times, and (of course) overall token usage, then Valantor and EyeLevel say that this consideration has been taken into account by dint of their own platform’s orchestration layers.

**“**We never send a whole schematic to a language model; our vision model splits each page into its elements first,” Fletcher confirms. “Processing runs in multiple passes at different levels of the document, and everything inside a pass runs in parallel, so there’s a minimum processing time, but it does not scale linearly with page count. Each agent does one small task, so cheaper models are often good enough, and teams that want direct control over cost can run the whole stack on their own hardware with Helm.”

## The intersection of AI and handwriting

sWhile we already know that AI and handwriting do mix in the same cocktail glass — the [ViWoods AiPaper](https://viwoods-eu.com/?utm_source=Google_CPC&utm_medium=Google_CPC&utm_campaign=Search-12&gad_source=1&gad_campaignid=23263953290&gbraid=0AAAABAvr13pEXv0R7LZAuPWJ4_awxrrLs&gclid=Cj0KCQjwsMLSBhD9ARIsAIpUTDq3CDtec8WME1EQkMXFJHCCxRFCXOjxpAkBJ1bL_PnaxhUZf4a6OCMaAqMFEALw_wcB) digital e-ink handwriting tablets have a useful set of AI functions on board, and similar products are available from manufacturers including [reMarkable](https://remarkable.com/products/remarkable-paper/pure?utm_source=google&utm_medium=paid&utm_campaign=tt01-co01-dn01%7Cgse%7Cprosp%7Cpurchase%7Cbrand-uk%7C0226&utm_content=tt01-co01-dn01%7Cuk%7Ckeyword%7Cbrand-exactsearch%7C0226&utm_term=23646619836,195097822238,807817876021&gad_source=1&gad_campaignid=23646619836&gbraid=0AAAAACTQ8CyvJMCFr1CpcmQJFJmkFdAk6&gclid=Cj0KCQjwsMLSBhD9ARIsAIpUTDq9Yl5TNt4z6caf3jWoXRMDtmIEKY3Ptuust0dc0_5cS9osWGm5naIaAtUsEALw_wcB) — it’s not a widely deployed use case yet. Valantor claims that its underlying data models and custom heuristics bridge the “data comprehension gap” when processing handwritten annotations.

“Our proprietary vision model, fine-tuned on more than a million pages of enterprise documents, sees the page the way a human does: tables, paragraphs, and figures,” underlines Fletcher.

He says that handwritten marks are captured as page elements with their layout context intact. Narrow agents then distill each element into a contextual object tuned for both search and LLM completion.

“Smaller pieces, less cognitive load — that’s how we close the gap, with better accuracy at lower cost, driving better performance and significant cost advantages,” he adds.

Working examples of this technology include Air France-KLM, which used GroundX to develop an AI-powered customer service assistant trained on thousands of policy documents, achieving 96+% accuracy on complex policy-related questions. AskVet used the platform to operationalize more than a decade of proprietary veterinary data, enabling autonomous resolution of up to 85% of customer inquiries while significantly improving operational efficiency.

## Is document management sexy now?

Taking all of this on board, are we at the point where we can ask whether document management has just become interesting, compelling, and sexy?

No, of course it didn’t; it will arguably always suffer from a degree of stigmatized disdain. That may change in the future as we interact more directly with AI tools that begin analyzing the unstructured information we know organizations have been sitting on for so long. For now, it may still remain the corporate equivalent of eating your vegetables — pass the [Brussels sprouts](https://www.healthyseasonalrecipes.com/wp-content/uploads/2023/11/simple-steamed-brussels-sprouts-1200-024-scaled.jpg) and steamed turnips, please.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)