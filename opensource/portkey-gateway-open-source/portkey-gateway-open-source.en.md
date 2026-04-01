[Portkey](http://portkey.ai/) defines itself as a company that provides a control plane for production AI deployments. This month, the company launched its newly unified Portkey Gateway service and made it fully open-source.

Like any gateway technology at this level (such as an [API gateway](https://thenewstack.io/ai-gateways-vs-api-gateways-whats-the-difference/)), this branded product acts as a control plane to manage and monitor AI model traffic and agent behavior, while also enforcing policy controls across the infrastructure on which agents run.

## A kick in the aaS for SaaS?

In terms of why the push to open source matters here, the argument rests on the need to align with the open approach used across many AI models, tools, and functions today.

[Rohit Agarwal](https://www.linkedin.com/in/1rohitagarwal/), CEO and co-founder of Portkey, tells *The New Stack* that without the progression to open source, every major computing function or service of AI infrastructure would require a separate SaaS subscription.

In this case, that would span governance, observability, authentication, cost controls, and Portkey’s MCP Gateway for governing AI agents (now also open source), as well as how they operate across enterprise tools and systems.

## Finding freedom in foundations

“The core gateway technology should be democratized, i.e., every engineering team building AI in production needs governance and observability — and that shouldn’t require a SaaS contract. What we’ve open-sourced is the thing we think should just exist as standard reference architecture. The value we build on top of it is where we (or anyone else) run a business. But the foundation? That should be free,” Agarwal says.

Agarwal’s assertion mostly holds water, but to temper his enthusiasm for a moment, we can point out that some on-premises [self-hosted deployments](https://docs.zerve.ai/guide/integrations/cloud/aws-self-hosting) would circumvent the need for a SaaS contract. Further, there are options for pay-as-you-go contracts in which customers are charged only for the tokens, API calls, or other [inference-related functions](https://thenewstack.io/confronting-ais-next-big-challenge-inference-compute/) they use. But overall, the drive for open source here is (arguably) largely laudable.

Portkey’s Gateway runs in the “critical path of production AI systems” at a global scale. The company’s platform is already processing trillions of tokens and more than 120 million AI requests every day, managing $180 million in annualized AI spend across some 24,000 organizations.

## 1000x more tokens by 2027

“Enterprises are finally going to production with AI, and when you go to production, you realize very quickly that at that scale, you’d need something like a gateway to manage all of that token traffic going across your whole company.

Teams will be overshooting their budgets, [exchanging PII data](https://thenewstack.io/protect-sensitive-data-and-prevent-bad-practices-in-apache-kafka/), running non-compliant models, and so on. Portkey just hit two trillion tokens processed in a day to solve this exactly – my goal by the end of the year is to multiply this by 1000x,” Agarwal says.

He explains that initially, Portkey’s Gateway gave software engineering and data science teams the foundation they needed to run AI in production, by which he means fast, reliable routing across every major model and provider. This new release offers full governance and a cost control layer, while adding the ability to manage and govern agentic workflows through the company’s newly open-sourced MCP gateway.

> MCP has completely changed what it means to run AI in production… You can’t have a thousand engineers all routing through an MCP server with no way to shut it down if something goes wrong.

## An MCP gateway needs a latch

“MCP has completely changed what it means to run AI in production,” Agarwal says. “Six months ago, the conversation was about managing LLM traffic; now, enterprises are asking how they govern agents that can actually take actions inside their systems. The same anxiety that existed with LLMs exists with MCP; it’s just higher stakes.

“You can’t have a thousand engineers all routing through an MCP server with no way to shut it down if something goes wrong. That’s why the MCP gateway has been the fastest-adopted thing we’ve built — enterprises don’t want to block MCP, they want a way to trust it.”

Inside the newly open-sourced Portkey Gateway, there are new usage policy controls to help engineers define and enforce model usage rules, limits, and access controls at the gateway level. A model catalog provides a continuously updated registry of models across providers, and a control-plane connection service here connects the gateway to the observability and management infrastructure.

Additionally, real-time metrics enable teams to track cost, latency, and usage. An MCP registry is present to help users discover, manage, and version MCP servers in one place. Finally, Portkey has provided enterprise-grade authentication for MCP traffic with built-in support for OAuth 2.1 and [OAuth 2.0](https://thenewstack.io/oauth-2-0-a-standard-in-name-only/).

## Agents are now operational actors

The technology proposition from Portkey rests on our ability to accept and understand instances of agentic software as something more than just plain old software features. Once agents access tools, query systems, and execute actions, they become “operational actors” within the enterprise.

Following that argument through, this leads to the point that organizations need to treat agentic instances the same as any other element of mission-critical technology infrastructure. This is where a control plane that governs access, enforces policy, and provides real-time visibility into what’s happening starts to be validated.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)