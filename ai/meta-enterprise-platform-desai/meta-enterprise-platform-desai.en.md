**Meta announced on Monday that it is building** a new enterprise business around its AI models and agents and has hired MongoDB CEO CJ Desai to run it. The effort, called Meta Enterprise Platform, will take technology Meta built for its consumer apps and advertisers and offer it to businesses and developers that want to deploy it inside their own operations.

In an X post, Mark Zuckerberg described it as the “next major pillar” of Meta’s business, putting enterprise AI alongside the company’s advertising and consumer apps.

[Desai](https://www.linkedin.com/in/chirantan-cj-desai-aa346/) joins as Chief Enterprise Platform Officer and will report directly to Zuckerberg. He [stepped down from MongoDB effective immediately](https://www.mongodb.com/company/newsroom/press-releases/mongodb-announces-ceo-transition), less than a year after becoming CEO in November 2025, and the company named former CEO [Dev Ittycheria](https://www.linkedin.com/in/dittycheria/) interim president and CEO.

For developers, the more pressing question out of [this launch](https://about.fb.com/news/2026/09/launching-meta-enterprise-platform/) is what they can build with it. Zuckerberg said Meta will bring its “full technology stack” to businesses and developers, starting with the Muse agent, Meta Business Agent, Muse API, and Muse Code.

Meta introduced Muse earlier this month as a personal AI agent for consumers, and Meta Business Agent, which launched in June, handles customer interactions for businesses across Meta’s platforms. Muse API and Muse Code are the products aimed most directly at developers, and they put Meta in closer competition with OpenAI, Anthropic, and Google for engineering teams building agents and coding workflows. Muse is also reaching past Meta’s own apps, [with Shopify integrating it across its stores as Amazon blocked it](https://thenewstack.io/amazon-meta-muse-block/).

## Muse API’s enterprise terms are still missing

Meta did not release enterprise pricing, general availability dates, or service terms for Muse API or Muse Code on Monday, even though developers can already use both: Muse Code has been in beta since August, and Meta began charging for its Muse Spark model through its API in July at $1.25 per million input tokens and $4.25 per million output tokens.

Once those terms arrive, teams have good reason to scrutinize them, including how Meta handles model updates, since a model change can easily disrupt a working system.

## Where Llama fits now

Llama, the model family Meta spent years promoting to developers as its open-weights option for teams that wanted to run and fine-tune models on their own infrastructure, does not appear anywhere in Meta’s description of the new enterprise stack. And Meta hasn’t said whether Llama will be part of the Enterprise Platform. The company began charging developers directly for one of its own models for the first time in July with Muse Spark, but it has also released open weights for its smaller Muse Glimmer model and promised an open-weights version of Muse Spark, so it’s too early to tell what the shift could mean for teams already running Llama in production.

## Desai’s data-layer playbook

At MongoDB, Desai was already thinking about what it takes to get agents into production. In May, the company [added persistent agent memory, automated embeddings, and other AI capabilities](https://www.mongodb.com/company/newsroom/press-releases/mongodb-makes-enterprise-ai-production-ready) to its data platform, with Desai arguing that the model is only part of the challenge and that getting agents into production depends heavily on the data layer behind them. Now Meta faces a similar challenge. Agents working inside a business need persistent context, access to constantly changing data, and a way to act inside the applications employees already use. Other companies are tackling the same problem in different ways, from Perplexity, whose [agents helped build a database they weren’t allowed to run](https://thenewstack.io/perplexity-cobbledb-ai-database/), to Microsoft, which [gave its Copilot agents their own email, calendar, and place in the org chart](https://thenewstack.io/copilot-agents-identity-runtime/).

Desai’s earlier roles extend that background into infrastructure and workflow software. He led product and engineering at Cloudflare, a company that has since pushed to become [the economic layer of the AI web](https://thenewstack.io/cloudflare-ai-web-economics/), and he spent nearly eight years at ServiceNow, eventually becoming president and COO.

In a [statement released with the announcement](https://about.fb.com/news/2026/09/launching-meta-enterprise-platform), Desai said Meta Enterprise Platform will focus on turning Meta’s AI stack into products and services that companies can deploy inside their own businesses, and that security and privacy are built into Meta’s enterprise products “from the outset.” Meta has [published its approach to security and safety for Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse), but Monday’s announcement did not address data retention, training on customer data, tenant isolation, identity controls, or compliance certifications, and enterprise buyers will want those answers before giving Meta’s agents access to internal data and systems.

Meta already has relationships with many of the businesses it wants to reach. Zuckerberg has pointed to the billions of people who use Meta’s products and the hundreds of millions of businesses on its platforms, many of which are small and midsize businesses that already use Facebook, Instagram, and WhatsApp for marketing and customer service. Enterprise Platform could take that relationship further by putting Meta’s AI directly inside a company’s own operations.

But winning over developers at the larger companies will be harder, since their engineering teams have spent the past several years building around models and platforms from OpenAI, Anthropic, Google, and others. Meta needs to offer something that gives teams more than reach before they add another platform to their stack or move over completely.

## A platform developers can only partly evaluate

For now, Meta Enterprise Platform is more strategy than product — even if some of its pieces are already in developers’ hands — and it leaves a big question unanswered: whether Meta’s enterprise AI future still includes Llama, or whether Muse signals a shift toward a more controlled platform where developers access Meta’s latest agent technology through Meta itself, even as Meta promises open weights for Muse Spark.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)