[NanoCo](https://nanoco.ai), the Tel Aviv startup behind the open source [NanoClaw agent framework](https://thenewstack.io/nanoclaw-minimalist-ai-agents/), on Wednesday launched a managed enterprise service that aims to give every employee a personal AI agent, each isolated in its own [Docker sandbox](https://thenewstack.io/nanoclaw-docker-sandboxes-ai-agents/). The company also raised $12 million in a seed round led by Valley Capital Partners, with Docker and Vercel among the participants.

Most enterprise AI agent services on the market today, including Microsoft Copilot, ChatGPT Enterprise, and Glean, typically deploy as a single shared assistant for the whole company. NanoCo is betting on a very different way to deploy its agents, with one sandboxed agent per employee that, over time, adapts to that person’s role and tools.

[Gavriel Cohen](https://www.linkedin.com/in/gavrielco/), NanoCo’s co-founder and CEO, tells *The New Stack* that “most companies do not want to build an agent platform. They want a working assistant for each employee.”

NanoClaw has now accumulated nearly 29,000 GitHub stars since it launched in February. The developer community around the project remains very active, and its users now include executives at Amazon, Google, Meta, and Accenture, as well as a somewhat unexpected NanoClaw superfan: Singapore’s foreign minister, Vivian Balakrishnan (Cohen and his co-founder and brother Lazer Cohen actually flew out to Singapore recently to meet with him).

![](https://cdn.thenewstack.io/media/2026/05/a9577240-screenshot-2026-05-20-at-08.56.39-1024x895.png)

*NanoClaw founders Lazer and Gavriel Cohen. Credit: NanoCo.*

## Credentials never reach the agent

Claws will only be acceptable in a business setting if they are secure. With NanoClaw, every employee’s agent runs in its own Docker sandbox. Requests from the user’s Slack or Teams app, for example, pass through a bridge component into what NanoCo calls a Router, which pulls credentials from a separate component called the Agent Vault and injects them only at the moment of an outbound call. The agent itself never sees them.

“An agent has to be able to work inside the most sensitive parts of a business,” Cohen says. “Their email. Their customer records.”

By default, the design assumes that any input could be hostile, so this credential isolation limits what the agent can do if it is tricked.

![](https://cdn.thenewstack.io/media/2026/05/0cdf5a7d-screenshot-2026-05-20-at-09.56.56-1024x572.png)

*NanoClaw credential handling. Credit: NanoCo.*

## Approval as identity binding

When an action is approved (either automatically or by a human), NanoCo’s system runs it with the approver’s credentials rather than the agent’s. This means a write to a Salesforce CRM field is logged against the human who approved it, for example.

Cohen argues that approval flows in most agent platforms don’t do this. They route a yes/no decision to a human without binding the human’s identity to the resulting action, leaving an incomplete audit trail.

Each per-employee agent acts as a supervisor that can spawn specialized sub-agents on demand, which then also run in their own sandbox. In NanoCo’s example of a PR Factory, a supervisor agent dispatches to a separate review agent and test agent. The test agent spins up a VM to run the actual tests.

## Skipping the conversion funnel

When it comes to its business model, NanoCo is taking a somewhat unusual approach. The company doesn’t necessarily see NanoClaw’s open source users as the top of the conversion funnel for its enterprise product.

“We’re not doing the normal thing like Elastic or Redis, where you’re trying to get your same open source users to force them at some point to convert,” Cohen says.

The open-core model may be useful for driving adoption, with the commercial teams then upselling the same users on enterprise features, but the NanoCo team says it is targeting companies that don’t have the engineering team to build their own agent platform on top of NanoClaw in the first place.

## White-glove for now

The question is how NanoCo can scale this, though. As of now, the company has 10 people. More than 100 companies have left their details on the company’s intake page, asking for help deploying agents. But for now, each deployment is currently bespoke and may involve an on-premises deployment for finance and other industries with strict data residency requirements, or a fully hosted deployment in the cloud. The team integrates with the customer’s internal tools and then operates the assistant on an ongoing basis.

“We’re going to be capacity-constrained for a while,” Cohen says. Channel partners and resellers are the longer-term answer, but Cohen also argues that the team learns from every deployment and integration it builds.

As of now, NanoCo hasn’t disclosed its pricing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)