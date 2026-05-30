AWS on Thursday launched what it calls a near-total rebuild of its managed search and vector engine, in an effort to better meet demands of the agentic age.

This next generation of [Amazon OpenSearch Serverless](https://aws.amazon.com/opensearch-service/features/serverless/) scales to zero when idle and aims to cut costs by up to 60 percent compared with provisioned clusters running at peak capacity.

The usage patterns of AI agents, which tend to come in bursts with long idle stretches, essentially broke the assumptions of the original serverless architecture AWS originally used for OpenSearch Serverless.

> “About 97 percent of it has been built from the ground up by the engineers on the managed service.”

[Tia White](https://www.linkedin.com/in/tia-white-tech-transformation/), who became general manager for OpenSearch at AWS in February, tells *The New Stack*, “The vast majority of it is a massive rebuild. About 97 percent of it has been built from the ground up by the engineers on the managed service. And then there are pieces that are already available via the open source repo, but anything that’s truly novel or true IP, we don’t make available via that open source project.”

## The “Swiss Army Knife” problem

The biggest architectural change is the separation of storage and compute, White explains, with OpenSearch sitting on a new proprietary storage layer. “Collections can truly shrink all the way to zero, meaning you’re not paying for anything if your resources are not active,” White explains. “And then they can spin back up in a matter of seconds to handle the needs of agents because of the bursty workload. We don’t want a cold-start problem.”

She also notes that the service auto-scales 20 times faster than the previous generation and also now supports search and vector collection types at launch. All of this is priced per OpenSearch Compute Unit for indexing, search, and GPU acceleration. Native integrations with Vercel and AWS’s own Kiro IDE are also part of the launch, along with a set of OpenSearch Agent Skills that let developers work with their preferred tools, including Claude Code and Cursor.

The 60 percent cost savings compared to running at peak capacity come from two places, White says: the new proprietary storage layer with its compression feature, and the auto-scaler being aggressive enough to drop capacity in seconds when traffic falls off.

“Since we’re able to predict what you need and we’re able to deliver and scale back down in a very rapid fashion, you’re going to automatically save money,” White says.

White is also candid about why OpenSearch needed to make these changes. “Predominantly, OpenSearch has been the Swiss Army knife, a hodgepodge of everything,” she says. “We even tried to do a pivot into SIEM [Security Information and Event Management] last year.” That detour did not stick. The new framing pairs the traditional search OpenSearch is known for with log analytics, but shaped around agent workloads.

## Coming soon: agent memory, log analytics, and a reasoning model for search workloads

That two-pillar refocus comes with a roadmap White previewed a bit in the interview.

A long-term memory feature for agents is slated for the second half of 2026, with built-in evaluation and governance from day one. As White describes the design problem: “Evaluation, which you could argue is a governance aspect, is an art and a science. The evaluation approach to what is good, what should be stored, what should be purged — that constant feedback loop.”

> “Building an agentic-first platform for our customers, those are things that we understand we have to provide at day one. It can’t be an afterthought or an add-on.”

She says those guardrails cannot be retrofitted. “Building an agentic-first platform for our customers, those are things that we understand we have to provide at day one. It can’t be an afterthought or an add-on.” The company is also focusing on building out OpenSearch Serverless’ features around knowledge graphs and semantic layers, alongside what White describes as “an advanced reasoning model for search-specific workloads.”

A major log analytics launch is coming in June, White says. That will put AWS back into a market currently dominated by Datadog, Splunk, and Grafana. A TIMESERIES collection type will follow at AWS’s New York Summit, extending OpenSearch Serverless to more observability workloads.

“Eventually, when the precision is there, and the token optimization is there, and all of these things, you beg the question of can LLMs replace something like OpenSearch,” White asks. But to AWS, the answer here is that OpenSearch Serverless (and OpenSearch in general) will become a vital semantic layer for the LLM to call — not something replaced by the LLM.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)