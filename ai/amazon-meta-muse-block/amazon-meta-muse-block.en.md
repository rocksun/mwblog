**Amazon started blocking Meta’s Muse from browsing and buying on Amazon.com on Sunday**, roughly two weeks after the personal agent [launched](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) on September 8. Shoppers who ask Muse to buy something there now get a pop-up telling them that continued access by an unauthorized AI agent violates Amazon’s Conditions of Use.

Amazon’s objections have little to do with shopping itself. Meta never told Amazon that Muse would visit the store, the agent does not identify itself while it browses, and it appears to capture and store customer credentials. Those three properties describe almost every personal agent shipping this year. Grok Bot from xAI also drives signed-in browser sessions, and so does the open-source [OpenClaw](https://thenewstack.io/openclaw-hermes-agent-harness/) project that Muse is modeled on. The block is a category design problem rather than a disagreement between two companies.

## What Amazon actually blocked

Muse runs on a dedicated virtual machine that Meta calls [Muse Secure VM](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse), and it reaches services in two ways: It uses built-in connectors for partners such as Gmail and OpenTable, and it drives an ordinary browser session for everything else. Shopping on Amazon.com used the second path.

That second path is what Amazon objects to. From the server’s side, a browser-driving agent looks like a signed-in customer with unusually fast reflexes, moving through search, product pages, account history, and checkout without ever declaring what it is. Amazon told *[GeekWire](https://www.geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping/)* it asked Meta to exclude the store voluntarily, but Meta did not agree before the block went live.

The credential dispute is harder to settle from outside. Meta says Muse has no visibility into passwords or payment methods and that credentials sit in secure storage, while Amazon says the agent appears to capture and retain them. Both statements may be sincere, and the merchant can verify neither, since an unannounced session provides no evidence of which software holds the password.

## The legal ground shifted seven weeks ago

Amazon reached for its Conditions of Use rather than the Computer Fraud and Abuse Act. Those terms, updated August 14, now require agents to identify themselves in user-agent strings and stop when asked. The likely reason sits in a ruling from early August. The Ninth Circuit [vacated](https://law.justia.com/cases/federal/appellate-courts/ca9/26-1444/26-1444-2026-08-04.html) the preliminary injunction Amazon had won against Perplexity, and the panel held that a user directing the Comet assistant is the party accessing Amazon’s computers. Writing for the court, Judge Milan Smith described the assistant as a tool, not a person, for statutory purposes.

If you’re operating a public API or storefront, the ruling makes lawsuits a weaker tool for keeping agents out. Blocking them in your own infrastructure is now the more reliable option. A site cannot easily argue that an agent trespassed, so it has to decide for itself which automated clients it admits, publish that decision, and enforce it in its own infrastructure. Amazon’s pop-up is that enforcement, written in product rather than in a filing.

## The identity layer already exists

Platform teams have solved a version of this problem before. Inside a service mesh, no workload is trusted by default because it looks like a normal client, and every call carries a verifiable identity that the receiving service checks before applying policy. Agent traffic on the public web faces the same requirement, and the specification is further along than most teams realize.

An IETF draft called Web Bot Auth builds on HTTP Message Signatures (RFC 9421). An agent signs its requests with a private key and publishes the matching public key at a well-known directory on its own domain. The verifier reads the Signature-Agent header, fetches the key set, and learns which operator is calling. Cloudflare [validates](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) these signatures at its edge for verified bots and agents. AWS WAF Bot Control added the same support for CloudFront distributions in November 2025.

The limits matter as much as the mechanism. A signature identifies the operator behind the agent, not the person it is acting for. The merchant learns that a request came from a named vendor, without learning whose account is in use or what the shopper approved. Amazon’s complaint about stored credentials sits in that gap. Signed identity settles the disclosure question and leaves authorization open.

## Shopify took the other route within a day

While Amazon was blocking Muse, Shopify was wiring it in. On September 21, the two companies [announced](https://www.pymnts.com/commerce/ecommerce/2026/shopify-brings-shop-pay-checkout-solution-to-metas-muse-ai-agent/) agentic checkout with Shop Pay across Shopify stores, extending the arrangement that made Meta an AI channel in Shopify Catalog on the day Muse launched. Muse reads structured product data and completes payment through a declared path, so the merchant knows an agent is transacting, and each purchase draws a single-use credential, so the card number never reaches Muse.

The plumbing for that path is public. Google and Shopify’s Universal Commerce Protocol covers discovery, cart, and checkout. The Agentic Commerce Protocol from OpenAI and Stripe covers checkout execution while the merchant stays the system of record. Google’s Agent Payments Protocol, donated to the FIDO Alliance in April, includes proof of the shopper’s authorization. A merchant that adopts it gets identity, scope, and an audit trail in the same transaction, which is what Amazon says it wanted and did not get.

Both routes follow from the business underneath them. Amazon runs its own storefront, recommendations, and assistant, so an outside agent that hides its identity takes the customer relationship and gives nothing measurable in return. Shopify sells infrastructure to merchants, so every new agent channel that reads its catalog and settles through Shop Pay reinforces the rails underneath. The key difference is who owns the demand surface, which explains why the same agent got a block from one company and a partnership from the other in the same 24 hours.

## Choosing how to handle agent traffic

Most teams exposing an API or a storefront now have to make this call deliberately rather than by default. The decision depends on how much the business relies on the customer relationship at the point of contact and whether an agent can be identified when the customer arrives.

| Scenario | Recommended option | Rationale |
| --- | --- | --- |
| Public content and catalog data, no account access | Verify signatures at the edge and allow named agents | Web Bot Auth is checked by default on Cloudflare and AWS WAF, so the cost is policy configuration rather than engineering, though it tells you the operator and not the shopper |
| Agent transactions where you want the revenue | Publish a declared channel using ACP, UCP, or an MCP server | Structured access gives scope and an audit trail, at the cost of building and maintaining a second interface alongside the site |
| Account access with stored credentials | Require a scoped token, never a replayed password | Delegated tokens can be revoked per agent, though few consumer agents support them yet, which pushes the burden back onto your login flow |
| Competitive surfaces you intend to keep | State the rule in terms of service and enforce it at the edge | Legally durable after the Ninth Circuit ruling, though it invites the same public standoff Amazon is now in |

Most real deployments will combine these rows rather than pick one. A retailer can verify signed agents on product pages, route purchases through a declared checkout, and still refuse an unannounced browser session inside a logged-in account. That combination is closer to Amazon’s position than its pop-up suggests.

## What platform teams should do this quarter

Enterprise buyers and the teams running these systems face the same three questions, in a specific order.

### Decide what an unidentified agent may do

The first question to settle is admission, and most sites have not settled it. They treat agent traffic as either a scraper to block or a browser to serve, and neither answer survives contact with a customer who wants an agent to act for them. Write policies for public pages, logged-in pages, and checkout separately, then publish them where an agent vendor can find them.

### Give identified agents somewhere better to go

The second question is substitution, and it decides whether the first one holds. Blocking a browser-driving agent without offering a structured path leaves the demand intact and pushes it toward workarounds. Sabre reported that nearly 80 of its customers now pilot or run its MCP server for booking rather than let agents work through a booking screen. A catalog feed, an MCP server, or an ACP endpoint converts hostile traffic into a channel you can meter.

### Fix credential handling before agents force it

The third question is authorization, and Amazon raised it loudest. An agent replaying a stored password is indistinguishable from credential stuffing at the network layer, regardless of any goodwill between the two companies. Scoped, revocable tokens tied to a named agent and a spending limit are the only version a risk owner can approve.

## Where agent access is headed

Amazon and Meta will settle this commercially, because Amazon has an advertising arrangement that lets Facebook and Instagram users shop its products, and Meta buys compute from AWS, and neither gains from a long standoff over one shopping flow. The precedent is already set regardless of how they settle. Every site that matters to an agent now has to answer whether it admits anonymous automation, and it will enforce that answer through bot management rules and protocol endpoints rather than cease-and-desist letters.

Agent builders should read the block as an argument for declaring themselves. An agent that signs its requests, identifies its operator, and transacts via a published protocol can be allowed, rate-limited, and billed, while one that arrives disguised as a browser will keep encountering pop-ups. For developers building the services these agents reach, the signed identity layer arriving through Cloudflare, AWS, and the commerce protocols is the most useful infrastructure the open web has gained in years. It is worth adopting before the next agent shows up unannounced.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)