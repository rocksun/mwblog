AI agents are poised to become the new big API consumer.

[Tollbit reports](https://tollbit.com/bots/25q1/) that traffic from [retrieval-augmented generation (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) bots surged 49% in early 2025. As agents become [more actionable](https://thenewstack.io/what-are-large-action-models/), they’re starting to call external APIs too.

“AI has the potential to be your API’s fastest growing customer base, if you play your cards right,” [Adrian Machado](https://www.linkedin.com/in/adrianmachado/), staff software engineer at [Zuplo](https://zuplo.com/), an API gateway, told The New Stack. “Without proper AI support, you’re going to be left behind as companies push ahead with AI automation.”

Yet most enterprise APIs remain ill-equipped to support dynamic, goal-oriented agent behavior, according to a [2025 paper](https://arxiv.org/pdf/2502.17443) by [IBM](https://www.ibm.com?utm_content=inline+mention) and [Equinix](https://metal.equinix.com/?utm_content=inline+mention) researchers. That’s because most APIs were designed for human developers, not machines. So, how do you make them agent-ready?

“There’s a huge shift happening right now in API discovery and use,” says [Jeffrey Wang](https://www.linkedin.com/in/wangzjeff/), co-founder at [Exa](https://exa.ai/), an AI-powered search engine. “The API economy is no longer, ‘Who has the best developer relations.’ It’s, ‘Who made themselves most machine legible?'”

Without clear signposting, an agent might miss your API entirely. If it does discover it, [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) may stumble with undocumented behaviors, hallucinate methods or flood your servers with random calls.

So, it’s important to get it right. Thankfully, strategies are emerging to position APIs for AI agents, from new standards to underground tricks. And, it’s more than just “get an MCP server” (though that’s a crucial step).

The jury’s out on what strategy will be most effective. So I’ve structured this guide to start with broadly agreed-upon best practices, then explore ones still taking shape. Most tips apply equally to public, partner and private APIs.

## Use A Well-Defined OpenAPI Specification

A well-defined, accessible [OpenAPI specification](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) (OAS) is table stakes. You need a precise API definition that outlines endpoints, methods, schemas, parameters and authentication.

“Having a validated and tested OpenAPI specification is essential, as it serves as a reliable source of truth for agents,” [Taylor Barnett-Torabi](https://www.linkedin.com/in/taylormbarnett/), senior product manager at [Netlify](https://www.netlify.com/), told The New Stack.

This allows agents to fully understand how your API operates. “LLMs struggle with JSON and rely on descriptive OAS specs, not just structure, but context-rich descriptions,” [Martin Buhr](https://www.linkedin.com/in/martinpbuhr), CEO and co-founder of [Tyk](https://tyk.io/), an open source API life cycle management platform, told TNS.

The challenge, however, is API drift: Seventy-five percent of production APIs have endpoints that don’t match their specs, according to a [2024 report from APIContext](https://apicontext.com/resources/api-drift-white-paper/), an API monitoring platform. Keeping definitions up to date takes ongoing discipline.

[David O’Neill](https://www.linkedin.com/in/davidon/), chief operations officer at [APIContext](https://apicontext.com/), suggested a means of practicing that discipline. “Implement an OpenAPI specification directly into the development workflow and apply strict schema validation,” O’Neill told The New Stack. “This ensures consistency and reliability in how APIs are defined, discovered and consumed by agents.”

Even then, providing an API specification to an LLM is not foolproof — it can still lead to ambiguous behavior. “LLMs may misinterpret parameters, overlook required fields or misuse endpoints due to a lack of contextual understanding,” [Edgar Kussberg](https://www.linkedin.com/in/kussberg/), group product manager at [Sonar](https://www.sonarsource.com/%20?utm_content=inline+mention), a code quality company, told The New Stack.

To increase precision, he recommends function calling with structured output. This is [an approach](https://platform.openai.com/docs/guides/function-calling/function-calling-with-structured-outputs?api-mode=responses) offered by providers like OpenAI to help models fetch data and take action.

## Create An MCP Server

Another key strategy is to adopt standard protocols for connectivity and discovery. Chief among them is [Anthropic’s](https://www.anthropic.com/) open source [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP).

“Just like we build SDKs to make APIs easier for human developers to consume, MCP aims to do the same for AI agents,” said Kussberg. It goes beyond specs to provide semantics for autonomous agents.

MCP servers provide a seamless way for AI agents to discover and integrate with your tools, data and APIs. To assist in creating them, a number of converters can turn any OpenAPI into an MCP server, such as [Speakeasy’s](https://www.speakeasy.com/) [Gram](https://getgram.ai/) or Tyk’s open source [API to MCP](https://www.npmjs.com/package/@tyk-technologies/api-to-mcp).

Machado put it bluntly: “MCP is the future. If you really want to enable AI agents accessing your APIs, wrap them in an MCP server that exposes key functionality via tools.”

But, there’s an art to doing it right. He recommends exposing “chunky” tools that combine multiple endpoints to achieve a specific business outcome.

For example, Exa uses MCP to unify its various API endpoints under one cloud-hosted interface. These search capabilities span real-time web search, academic papers, company research and content crawling.

Said Wang: “MCP solves a fundamental problem: agents need to understand when to use your API, not just what your API does.”

## Use Well-Defined Error Responses

With quality error descriptions, AI agents can understand what went wrong when API requests fail and automatically remediate. This goes beyond opaque HTTP codes — it will require detailed, machine-friendly instructions.

“Error messages must be specific and documented,” [Kristen Womack](https://www.linkedin.com/in/kristenwomack/), principal product manager for the Azure Developer CLI at [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), told The New Stack. “For each error code, provide its definition, the next action to take, and examples of common failure cases.”

Such information could live in your OpenAPI specification.

This also improves back-and-forth interactions with AI agents. “I think we will see ‘chatty’ agents, so providing them clear guidance will be critical for the future of API-to-AI communication and even API-to-API integrations via AI,” Womack added.

Others agree: status codes aren’t enough. Machado recommended documenting common error messages agents may encounter and returning an application/problem+json media type, a machine-friendly way to send error messages in HTTP responses, as standardized by Problem Details for HTTP APIs ([IETF RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807)).

More descriptive errors mean a better user experience, said Barnett-Torabi. “The more thorough and detailed your error messages and logs are, the more likely agents can resolve issues without numerous back-and-forth prompts.”

## Document Workflows and Next Steps

Documenting common use cases and workflows helps agents understand context. It also brings more determinism to interlinked API flows.

“Showcasing how to combine endpoints together to achieve a business or technical outcome will help tremendously,” said Machado. “Agents may prefer APIs that clearly demonstrate how to solve specific tasks.”

The [Arazzo specification](https://thenewstack.io/the-rise-of-ai-agents-how-arazzo-is-defining-the-future-of-api-workflows/) offers a standard way to document chained API operations. This could include [common multistep workflows](https://www.speakeasy.com/blog/5-potential-use-cases-for-Arazzo), like onboarding processes, authentication workflows or payment initiations.

Another way to give agents “next steps” is through hypermedia, an underused constraint of RESTful API design. As [Roy Fielding](https://www.linkedin.com/in/royfielding/), the architect of REST, defined it, HATEOAS (hypermedia as the engine of application state) means including links to further interactions in every API response.

Hypermedia gives agents a clearer awareness of what actions are possible. Said Tyk’s Buhr, “HATEOAS-style responses help to provide next and previous links in paginated data to reduce hallucinations.”

## Consider Other AI-to-API Standards

While excitement around MCP is brewing, experts point out that lingering [security concerns](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/), like the lack of built-in authentication, must be addressed for safe, scalable use. And it’s not the only protocol in play.

While she acknowledged that MCP has “got the momentum,” Microsoft’s Womack also noted that [alternatives](https://thenewstack.io/why-are-agent-protocols-like-mcp-and-a2a-needed/) like [Agent2Agent (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/), ACP, ANP, and AGENCY have emerged.

It’s still too early, Womack said, to tell which protocol will dominate AI-to-API connectivity. While MCP may evolve the fastest, she encourages API producers to experiment, follow the protocols closely, and contribute to the evolution of emerging standards.

## Provide LLM-Optimized Metadata

One low-effort strategy is adding an [llms.txt file](https://llmstxt.org/) to your website’s root directory. While not designed specifically for APIs, it provides metadata that can help LLMs with discovery and site traversal.

“I could see this becoming like robots.txt and sitemap.xml, which are long-standing and widely adopted,” said Womack. But it’s unclear whether AI model providers will fully support the standard, she added.

[One directory](https://directory.llmstxt.cloud/) now catalogs more than 600 llms.txt files in use. Early adopters include [Anthropic](https://docs.anthropic.com/llms.txt), [Cursor](https://docs.cursor.com/llms.txt), and [Perplexity](https://docs.perplexity.ai/llms.txt). API documentation platforms like [Mintlify](https://mintlify.com/blog/what-is-llms-txt) even generate them automatically.

However, not everyone is convinced llms.txt adds much value beyond standard web parsing. “I think llms.txt is really silly,” said Machado. It would require both major companies and crawlers to support it, which he views as unlikely: “Definitely a chicken and egg problem.”

That said, structured metadata can still offer value, especially when optimized for LLMs.

For instance, beyond MCP, Exa has made additional agent-ready design choices: parsing sites into clean, LLM-ready Markdown and offering custom schemas tailored to client application needs.

## Use A Clear API Design

AI agents work best with predictable patterns. “All the usual best practices in API design matter more when making an API agent-ready,” said Buhr. “LLMs are pattern-followers.”

That means applying RESTful guidelines, using consistent naming and maintaining clear data hierarchies. “If your API has confusing abstractions or names, you’ll need to refine them before agents can work effectively,” said Barnett-Torabi.

One common source of unpredictability is inconsistent handling of optional fields, she added:  “Sometimes, an agent will or will not include optional fields in a request, which can result in unexpected responses.”

Reducing ambiguity could help agents behave more predictably. That said, others API experts note that achieving design harmony is difficult as teams evolve and requirements shift.

Said Womack, “We’ve seen some inconsistent APIs rise to the top despite design consistency being important.”  Even APIs like [Stripe](https://stripe.com/) and [Twilio](https://www.twilio.com/?utm_content=inline+mention) are less consistent than people think, she added: “I’m a holdout on whether this will really matter for agents.”

Still, she recommended designing minimal, relevant payloads to improve performance — especially in real-time interactions. “Slow or unreliable endpoints can lead to timeouts for the agent,” she warned.

## Evolve Your Traffic Controls

Agentic AI is prone to unpredictability and bursty behaviors, requiring new [traffic-handling techniques](https://thenewstack.io/what-is-semantic-caching/). “AI agents behave differently from human users, so it’s critical to adapt accordingly,” said APIContext’s O’Neil.

He recommended nuanced rate limiting, concurrency caps and tiered quotas to separate AI traffic from human use. Greater visibility — through logging, monitoring and caching — could help detect and respond to abnormal behavior.

Agents might be tasked with looping through a repetitive process, like sending emails in bulk. “This will result in a bunch of API calls in a short amount of time,” says Machado.

Still, detecting agent traffic isn’t easy, he adds. “There’s no guarantee you can identify agents or bots, and they are incentivized to avoid such safeguards as they mature, in order to complete their task.”

Dynamic rate limiting can prevent backend overload, Machado suggested. Providing endpoints that allow for bulk operations and asynchronous processes can also help reduce strain.

## Build Rich Developer Resources

Many familiar developer experience best practices, like self-serviceability, clear documentation, smart defaults and predictable naming, also apply to agentic AI.

“A good developer experience can also lead to a good agent experience,” said Barnett-Torabi. The key difference, though, is that AI has a higher threshold for information overload, so extra context doesn’t hurt.

A context-rich developer portal can enhance an agent’s understanding. Beyond documentation, things like tutorials, guides and blog posts help steer agents toward the best results.

Stuffing information beyond sign-in walls won’t work well, Barnett-Torabi warned: “APIs that are difficult to access, hidden and require complex processes to obtain access will not be very agent-friendly and will prevent adoption.”

## Don’t Forget About Security

Access control remains a major weak point for external-facing APIs. According to [Salt Security](https://salt.security/press-releases/salt-labs-state-of-api-security-report-reveals-99-of-respondents-experienced-api-security-issues-in-past-12-months), 95% of API attacks originate from authenticated sources; 98% of attacks target public-facing APIs.

So, the fear is that increased agent-driven traffic will exacerbate API gaps that are already in place. To avoid agents leaking sensitive data, there are a few tactics to take.

First, it’s important to log your total API inventory — this is a good practice to understand your landscape, what can be publicly accessed and if shadow APIs exist.

“You need a full list of all of the APIs that are exposed to the public web,” said Machado. This includes official public APIs and web APIs that your applications call. “Agents can potentially call these too, so don’t assume they are ‘internal.'”

A standards-based approach should also benefit security, said Barnett-Torabi. “For authentication, you should follow common open standards like OAuth closely,” she said. “Deviating from web standards makes your API harder for agents to work with.”

## Follow Ethical Standards

APIs, once static connectors, are now data highways for autonomous agents to train on and reason with. Their rise puts new pressure on providers to ensure systems (and underlying data) are ethically sound.

“APIs are poised to play an even more critical role in software development, becoming trusted channels of information whose integrity and accountability directly shape how AI agents behave,” [Ellen Brandenberger](https://www.linkedin.com/in/ellenbrandenberger/), senior director of product, knowledge solutions at [Stack Overflow](https://stackoverflow.com/), told The New Stack.

“The most important techniques, tools and standards emerging to enable agent-ready APIs are those that prioritize responsibility, transparency and community trust.” She recommended transparent data sourcing, user privacy and fairness in algorithmic decisions.

## Figure Out Monetization

Not all APIs are public-facing or monetized. But for those that are, agentic AI could unlock a sizeable new revenue stream. This will require some form of usage-based billing.

“AI presents a great business opportunity for companies that want to monetize access to their platforms or proprietary data,” said Machado. “Many API-first companies like Stripe are already launching MCP servers to capture AI traffic.”

He added, “Being first to market with an MCP server can be a competitive advantage over other public APIs, and increase your market share with innovative companies that are adopting AI agents.”

## From DevRel to AgentRel

[Akamai](https://www.linode.com/?utm_content=inline+mention) [reports](https://www.akamai.com/blog/security/rise-llm-ai-scrapers-bot-management) that scraping from RAG-based AI agents is fueling an “exponential increase” in bot traffic. Now, APIs are the next logical step for agents to interface with the real world.

Beyond the API community, others validate this incoming surge. [Dor Sasson](https://www.linkedin.com/in/datapm), co-founder and CEO of [Stigg](https://www.stigg.io/), [wrote in a post on his company blog in January](https://www.stigg.io/blog-posts/the-agents-are-coming-are-your-apis-ready-for-agentic-ai-consumption) that AI agents will soon hammer APIs with traffic no human could generate alone.

But positioning APIs well for AI agents isn’t magic. It requires rethinking traditional dev-focused marketing and design for machine-first consumption. Standards like MCP help address this machine-driven shift.

The rest — like comprehensive docs, rate limiting, error handling, meaningful errors and input validation — are good API hygiene in general. Other smart moves include avoiding exposing raw APIs, using a gateway and testing your APIs regularly with agents.

If this all seems like a big ask, it is. It requires discipline and fundamental API-first thinking, which isn’t universally applied today.

So, the reality? We’ll likely see shortcuts emerge to help Software as a Service (SaaS) providers quickly hop on the agentic wagon, for better or worse.

“These strategies are only as effective as your governance and engineering culture,” said Machado. “In reality, many will just slap an MCP on top of their existing API mess and call it a day.”

History suggests this isn’t such a bad move. Wang compared MCP adoption to the SEO gold rush of the dotcom era. Essentially, MCP is helping companies optimize for “agent SEO,” he said.

Quick action now could pay off later, Wang added: “Today, the app providers standing up MCP servers will be the ones dominating agentic search and orchestration flows over the next few years.”

So, at the very least, wrap your API in MCP to stake your claim. On Day Two, figure out how to operationalize the rest.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)