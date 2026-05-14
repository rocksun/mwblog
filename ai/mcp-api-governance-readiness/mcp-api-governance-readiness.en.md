**When I recently talked to Kin Lane, API evangelist and co-founder of [Naftiko](https://naftiko.io)**, I was repeatedly struck by the parallels between what we’re seeing with GenAI adoption and what we saw with the migration from private data centers to public cloud.

For cloud adoption, companies with strong psychological safety were better positioned to experiment and learn quickly because they already had safe-to-fail cultures. Organizations that had adopted domain-driven design were better placed to refactor monoliths to microservices. Those who had embraced some variation of XP or Agile were better able to rapidly implement their independently deployable microservices.

In other words, companies with strong engineering practices, coupled with a good culture, are best placed to handle transitions. That’s hardly surprising, but it does imply that a lack of investment in, for example, good-quality API documentation, puts a company at a distinct disadvantage.

## **MCP is just an API**

With agentic adoption, Lane tells *The New Stack*, the organizations that are best positioned are those that already have clean data pipelines, mature API management, cloud fluency, and working governance structures.

> “MCP is just an API — a long-lived HTTP connection serving up JSON. We’ve been doing that for years, it’s nothing new.”

This is because everything in software builds on top of pre-existing foundations. “MCP is just an API — a long-lived HTTP connection serving up JSON,” Lane says. “We’ve been doing that for years, it’s nothing new.” This means that artifacts such as OpenAPI specifications, AsyncAPI contracts, API gateways, developer portals, and documentation standards become the raw material of the agentic world.

An OpenAPI specification already describes your API’s operations, data shapes, and semantics. The same specification can be used to generate an MCP server. From there, agent skills that call those MCP servers can be derived from the same source.

“OpenAPI offers that kind of menu, that source of truth,” Lane says. “The skill is what you do with that menu — how do you order that burger? Open API will serve that menu to an agent.”

Organizations that have been rigorous about their OpenAPI definitions are sitting on a reusable asset that maps closely to what agents require. Those who have treated API specs as an afterthought or allowed them to drift from implementation reality will find the translation considerably harder.

## **Reversing the polarity of the neutron flow**

Lane describes a conceptual shift in how to think about what is new about the AI moment. For the past 15 years, API investment has been primarily outward-facing: Organizations expose resources via APIs so that developers can build on top of them. The consumer was a known quantity: a handful of partners, a developer community, perhaps a few million API calls at scale.

What changes with AI agents is the direction and volume of that pressure.

“Your API consumers aren’t just Bob and Fred, who are interested in building something on your API, and then half a dozen people come along each month,” Lane says. “You have a DDoS of these agents. *The Matrix* sentinels are trying to get in, rather than you trying to get out and make your resources available. That reversal in polarity is a big shift.”

> “You have a DDoS of these agents. *The Matrix* sentinels are trying to get in, rather than you trying to get out and make your resources available. That reversal in polarity is a big shift.”

The implication for API governance is significant. Businesses that have already invested in access control, rate limiting, security policy, and fine-grained permissions are prepared for this inversion. Those who haven’t will find themselves exposed in terms of operational resilience and security posture.

## **Context engineering as API design**

Another recurring problem I’ve seen with AI projects is over-sharing. Preventing it adds a [considerable burden to an organization’s security teams](https://leaddev.com/technical-direction/if-95-of-generative-ai-pilots-fail-whats-going-wrong). The instinct when standing up an MCP server is to expose everything, thereby granting agents access to the platform’s full API surface. Figma’s MCP server, for example, gives access to the entire Figma API. Lane sees this as both a missed opportunity and a potential liability.

“Most MCPs, when generated from an open API or otherwise, should have more of a context. Who’s using this? What access do they need? You narrow that down to only the tools and operations they’re going to need to get the job done. Can they change anything, or just read something? If so, can they read everything or just the slice? That context engineering via MCPs is key to security, and also success: What do you want the agents to do?”

This is domain-driven design applied to a new context. The organizations that have practiced bounded context thinking, built APIs around business capabilities rather than database tables, and thought carefully about what each consumer type needs, have the conceptual muscle memory to get context engineering right.

## **The portal as a proxy for readiness**

Lane has developed a research methodology to assess enterprise API maturity, drawing on signals from job postings, press releases, and public API documentation across hundreds of major organizations. One of his most reliable leading indicators turns out to be surprisingly simple: does the company have a public or partner-facing API portal?

“If you’re Chase Bank or Ford Motor Company, you have an API portal,” Lane posits. “There are plenty of companies that don’t have API portals. They have APIs, but don’t have experience in making them available. It makes them nervous as hell, which creates a lot of infighting and political drama.”

The portal in Lane’s framework is a proxy for organizational processes: deciding what to make available and to whom, under what conditions, with what documentation, and by which actions it is supported. That experience is what determines how confidently a business can respond to agentic demand.

“The companies that are more nervous about it, who say ‘We don’t want to put things out there’, don’t understand how APIs work,” Lane says. “They’re hit harder by AI because they’re less flexible and unable to adjust to what the market needs.”

> In a world where AI agents navigate API surfaces autonomously, the quality of your semantic descriptions directly affects what those agents can and cannot do on your behalf.

The same logic applies to documentation, onboarding, and developer experience. Companies that have invested in reducing time to first call, writing documentation that helps developers succeed, and maintaining support models for API consumers have built the scaffolding that agentic tools can use. In a world where AI agents navigate API surfaces autonomously, the quality of your semantic descriptions directly affects what those agents can and cannot do on your behalf.

## **If you’re behind, you’re not out**

If your employer has underinvested in API governance, the picture is not hopeless, but it requires honesty about your starting point. “Understand what you’re capable of today,” Lane advises. “Have your internal API, internal data, and your external SaaS tooling landscapes all mapped. Know what you’re capable of and start there.”

There are, he suggests, some advantages to starting later. Legacy organizations carry technical debt that constrains their choices. A company without entrenched Oracle infrastructure and decades of accumulated API sprawl can make cleaner decisions about data pipelines and cloud architecture. Modern tooling — Snowflake for data, contemporary API gateways, and cloud-native architecture — is accessible in ways that it wasn’t five years ago.

But there is a knowledge gap. “If you don’t have that robust toolbox, you have to develop it. What is REST — or events, webhooks, WebSockets, or GraphQL — good for? You’ll need to be much more cautious, and you’ll learn some hard lessons.”

## **Stay the course**

The broader argument that Lane’s research supports across more than 300 enterprises is that AI rewards consistency over reactivity. The organizations that jumped from trend to trend without building durable API foundations are now the most exposed. The ones that made dull, compounding investments in governance, documentation, design standards, and business practice are discovering that those investments were, in effect, preparation for exactly this.

As Lane puts it: “The deeper your roots, the less you’re likely to respond in a knee-jerk or emotional way, or see every new thing as a solution. You can’t just jump away from these long-term investments.”

MCP rewards the organizations that already know how to design for reusability, govern for security, and build for consumers they haven’t yet met. If that describes your organization, the message is simple: keep going. If it doesn’t, the first step is knowing where you actually stand.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/b0ce81f3-cropped-5f5868db-nick-luchessi-2-600x600.png)

Nick Lucchesi serves as the editor-in-chief of The New Stack, where he directs editorial strategy and oversees coverage of the technologies and professionals driving software development, deployment and management at scale. Before joining The New Stack, Lucchesi held the position...

Read more from Nick Lucchesi](https://thenewstack.io/author/nick-lucchesi/)