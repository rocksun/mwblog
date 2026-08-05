**It’s undeniable that enterprise AI has a context problem**. Although frontier models are incredibly capable, if they can’t securely access the information enterprises actually need, they don’t offer much. That’s [a problem rooted in what some call context debt](https://thenewstack.io/vibe-coding-context-debt/), and the challenge OpenAI and Elastic are targeting with an expanded partnership announced on Thursday.

## When retrieval meets reasoning

Combining OpenAI’s reasoning models with Elasticsearch’s search, retrieval, and permissions capabilities, the two companies are tackling head-on one of the biggest bottlenecks in production AI. Typically, information lives scattered across documentation, support tickets, log files, security alerts, and years of internal knowledge within the company. But much of it is protected by role-based access controls (RBAC), requiring an AI agent to retrieve it only if they have permission to see it.

That’s where Elastic comes into play. [OpenAI is leaning on Elasticsearch](https://www.elastic.co/blog/elastic-openai-partnership) to surface enterprise data while abiding by existing access controls, ensuring the model only reasons over data the requesting user is explicitly authorized to view.

> The better an AI system gets at finding only the information it needs before it starts reasoning, the cheaper and often more accurate it becomes.

Both companies have offered basic connectors since 2023, but this deeper integration covers three core operational fronts of context-aware AI agents, agentic observability, and agentic security.

The better an AI system gets at finding only the information it needs before it starts reasoning, the cheaper and often more accurate it becomes. It’s a point that [extends beyond inference pricing to architecture-level decisions about how agents manage context](https://thenewstack.io/agentic-ai-token-costs/).   
  
To show what that looks like in practice, Elastic shared results from its internal benchmarks. The company said Elasticsearch achieved a 0.89 recall score in retrieval tests while maintaining multi-tenant data isolation. In a separate experiment using the BrowseComp-Plus benchmark, Elastic reported that its precomputed Knowledge Indicators cut input token usage by up to 75% compared to a standard RAG pipeline, while improving answer accuracy from 60% to 92%.

## Observability for autonomous agents

The partnership also extends directly into system observability. As engineers push autonomous agents into production, visibility into model behavior, token consumption, and runtime failure modes becomes a critical part of the process.

Elastic consolidates OpenAI API usage metrics and audit records, enabling SRE teams to monitor token usage, model activity, and infrastructure telemetry within a single control plane. So when incidents do occur, Elastic’s agentic investigation workflows correlate these signals to identify root causes and suggest next steps, which cuts the time developers spend jumping between logs and metrics.

## Security alerts become attack chains

On the security side, the integration offers immediate practical utility for enterprise SOCs. Security analysts often face thousands of isolated alerts. Using OpenAI’s models, Elastic Security powers an “Attack Discovery” engine that automatically synthesizes disparate alerts into cohesive attack chains mapped to the MITRE ATT&CK framework. This allows analysts the opportunity to review evidence-backed narratives instead of sifting through raw log entries.

> Analysts can review evidence-backed narratives instead of sifting through raw log entries.

Early adopters are reporting measurable operational improvements:

* **Visa:** As part of a SIEM modernization initiative, Visa implemented an agentic workflow with human-in-the-loop validation, cutting triage times on high-stakes mainframe detections from 15 minutes to seconds while maintaining full audit records, the kind of [evidence-backed decision trail that every AI agent workflow demands](https://thenewstack.io/agent-evidence-packet-analytics/).
* **Airtel:** The company’s managed security team reported up to 40% faster alert triage and a 30% reduction in overall incident investigation times using Attack Discovery alongside Elastic Agent Builder.

Looking ahead, the collaboration connects into OpenAI’s Daybreak Cyber initiative, with plans to integrate specialized security models into Elastic Security workflows to automate incident response recommendations and generate detection rules dynamically.

> Elasticsearch spent over a decade indexing enterprise data for humans to query. Now, it is fulfilling that same role for autonomous agents.

## Search Engines as Context Engines

Elasticsearch spent over a decade indexing enterprise data for humans to query. Now, it is fulfilling that same role for autonomous agents. Through support for the [Model Context Protocol (MCP)](https://thenewstack.io/api-vs-mcp-incident-management/), Elastic Agent Builder, and deep integrations with [OpenAI Codex](https://thenewstack.io/gpt-5-6-codex-user-surge/), developers can connect agents directly to corporate data sources without building complex authorization and retrieval glue code from scratch.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)