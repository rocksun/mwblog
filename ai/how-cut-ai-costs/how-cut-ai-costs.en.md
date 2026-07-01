AI costs are rising, and not for the reason most people assume. It’s true that the models are getting more expensive and that teams are using them recklessly.

But there’s another reason contributing to rising costs: messy context.

Context management is one of the biggest unsolved problems in enterprise today. There are mountains of knowledge that need to be converted to context so agents can use it reliably (and cheaply). To give agents access to that knowledge today, engineers are connecting their agents to dozens of [MCP servers](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/).

According to Gartner, “Context accumulation is the main cost driver. Every agent task assembles a context window from enterprise documents, tool schemas, compliance rules, and conversation history. Each step reingests this growing context, compounding costs across workflows.”¹

> “Context management is one of the biggest unsolved problems in enterprise today.”

So when an agent needs to figure something out, like whether a [service outage](https://thenewstack.io/a-cascade-of-failures-a-breakdown-of-the-massive-aws-outage/) is related to a recent deployment, it asks GitHub MCP who owns the service, then asks Jira for recent tickets, then asks PagerDuty for incidents. That’s three separate calls, repeated in different combinations every time something similar comes up.

When that happens once, it isn’t a big deal. But when it happens hundreds of times a month, like in a workflow or because it’s a popular question, the cost starts to add up. Putting aside cache, the 1,000th time it runs costs the same as the first.

That’s exactly what our data shows. Agent queries to AI repeat themselves in slightly varied forms, thousands of times a month.

Every time that query runs, the agent pulls hundreds of thousands of tokens of input context (which is the majority of the context for agent queries).

![Chart showing the ratio of input to output tokens against time.](https://cdn.thenewstack.io/media/2026/06/7e4d2ffb-image1-1024x576.png)

So we decided to run an experiment to see if we could reduce AI cost when fetching context.

Our hypothesis: By pre-relating context and building a semantic layer that matches popular query patterns, you can reduce the amount of data hops and reasoning agents have to do. Fewer hops should mean fewer tokens consumed and therefore lower costs.

## The experiment

We pulled thousands of agent queries from production, categorized them, and created a test set of 1000 commonly asked SDLC queries.

We then created the following four conditions to run the queries on:

**Claude + MCPs (baseline).** The agent had direct access to GitHub, Jira, and PagerDuty via their respective MCP servers, which is the same setup most teams are running today. The agent had to figure out on its own which tool to call, in what order, and how to reconcile results that came back in different formats with different naming conventions. Every query that touched more than one tool required the agent to resolve these mismatches mid-flight, burning tokens on each attempt.

**Claude + MCPs with a skill file.** Same tool access as the previous condition, but we added a markdown skill file that describes what each tool is authoritative for, explains the repo structure and potential naming mismatches, and outlines a lookup strategy for each type of question: start in GitHub, find the owning team, then use that team name to look up the PagerDuty schedule.

[**Context lake**](https://thenewstack.io/context-lake-ai-agents/)**.** The agent had access only to Port’s MCP server, which exposes a unified software catalog where GitHub, Jira, and PagerDuty data are already pre-integrated. Services in the catalog already have their PagerDuty service, GitHub repository, and Jira project linked as relations.

**Context lake with a skill file.** Same catalog access as the previous condition, plus a skill file optimized for the catalog’s structure. Instead of a lookup strategy, it’s a routing table: a mapping of query type to the entity type and property field that answers it. “Who’s on call for service X?” → read `service[X].on_call`. The agent’s only job is to find the right entity and read the right field.

We then ran the queries across all 4 conditions and across three models.

In total, we ran 12,000 queries and measured token usage for every query.

### The results

|  |  |
| --- | --- |
| **Condition** | **Avg. savings** |
| Claude + MCPs | — |
| Claude + MCPs + Skill | +18% (worse) |
| Context Lake | 58% cheaper |
| Context Lake + Skill | 80% cheaper |

![](https://cdn.thenewstack.io/media/2026/06/1310ee61-avg-savings-1024x524.png)

Here’s the full average cost breakdown per query across all four conditions and three models:

|  |  |  |  |
| --- | --- | --- | --- |
| **Condition** | **Haiku** | **Sonnet** | **Opus** |
| Claude + MCPs | $0.087 | $0.333 | $1.761 |
| Claude + MCPs + Skill | $0.103 | $0.375 | $2.187 |
| Context Lake | $0.038 | $0.131 | $0.771 |
| Context Lake + Skill | $0.018 | $0.059 | $0.354 |

![](https://cdn.thenewstack.io/media/2026/06/e60916b4-avg-cost-per-query-1024x557.png)

In percentage terms vs. baseline:

|  |  |  |  |
| --- | --- | --- | --- |
| **Condition** | **Haiku** | **Sonnet** | **Opus** |
| Claude + MCPs | — | — | — |
| Claude + MCPs + Skill | +18% | +13% | +24% |
| Context Lake | -56% | -61% | -56% |
| Context Lake + Skill | -79% | -82% | -80% |

![](https://cdn.thenewstack.io/media/2026/06/bc5b270a-avg-savings-per-model-1024x570.png)

Our key findings:

* Context lake with skills is consistently 80% cheaper than Claude + MCPs across every model.
* Haiku dropped from $0.087 to $0.018, Sonnet from $0.333 to $0.059, and Opus from $1.761 to $0.354. The savings hold regardless of which model you’re using.
* Expensive models become more viable for everyday queries with a context lake. Opus at $1.761 per query is something you’d normally reserve for the most critical tasks. At context lake prices, that same Opus query costs $0.354 – still the most expensive option, but within range for common use.

The effect of skills surprised us in a couple of ways:

Adding a skill to Claude + MCPs actually made things worse: 18% more expensive on Haiku, 13% on Sonnet, 24% on Opus. We expected routing guidance to help agents take more direct paths. What actually happened was that agents followed the skill file like a checklist, executing every step in order rather than reasoning about what they actually needed.

On the context lake, the skill file did help, but in a different way. The data was already joined, so the agent wasn’t making redundant calls. The skill file’s only job was to point toward the right entry point.

Skill files aren’t a bad idea, but they’re not a silver bullet. They seem to work better when the underlying data is already well-structured.

### What makes the context lake more efficient

A context lake is a continuously updated, unified knowledge layer that connects all your organizational data, such as services, teams, incidents, deployments, and tickets, into a single structured model with explicit relationships. Agents query it instead of querying individual tools.

> “The agent never has to reason about how things connect, because that’s already baked into the data model.”

Two characteristics of context lake help agents fetch context more efficiently:

1. **Pre-joined data.** In a direct-to-MCP setup, the agent is the one connecting entities, using partial results from tools that don’t know about each other. Every query reinvents the same connections. In the catalog, a `service` entity already knows its team, repo, PagerDuty service, and Jira project. The agent reads one thing and gets the full picture. The efficiency gain isn’t just fewer calls. It’s that the agent never has to reason about *how* things connect, because that’s already baked into the data model.
2. **Data shortcuts.** Mirror and aggregation properties can shorten paths between data points. For example, `service.on_call` isn’t a relation the agent traverses. It’s a field already populated by mirroring `team.on_call_user` at sync time. `open_incident_count` isn’t something the agent has to count; it’s stored. When an agent counts incidents by querying each service one by one, it’s spending tokens on arithmetic that could have been done once. The catalog does that work at ingestion and serves the result directly.

### What it all means

If you’re building with agents today, here’s what you should take with you:

1. You probably don’t need the most expensive model for most of your queries. Haiku handled a significant portion of our test cases adequately, and if your data layer is efficient, the cheaper model has less context to wade through anyway.
2. Platform engineering needs to own context management. Right now, most organizations treat agent costs as an agent problem: tune the prompt, add more tools, and hope the model figures it out. But the agent is just responding to whatever structure it’s given. If the data is fragmented, the agent will hop. And that’s expensive.
3. The context window is a managed resource with a budget. Someone has to own it, and platform engineering is the right team for the job.
4. Pre-integrating data into a shared model moves the work from inference time to ingestion time. You pay to build the relations once; every subsequent query is cheaper. Those savings get better the more you use them.

To read more about context lake, check out: [Why agents need a context lake](https://www.port.io/blog/why-ai-agents-need-a-context-lake).

---

¹*Shiva Varma, “How to Manage Token Costs for Custom-Built AI Agents,” Gartner, 26 March 2026.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/05/24f5579b-cropped-bff51576-zohar.png)

Zohar Einy is the CEO of Port, the agentic engineering platform that is helping customers like GitHub, Visa, and PwC move from manual to autonomous engineering. Zohar began his career in the Israel Defense Forces' 8200 unit as an engineer,...

Read more from Zohar Einy](https://thenewstack.io/author/zohar-einy/)