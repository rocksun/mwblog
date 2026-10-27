**Models running an OpenAI cybersecurity evaluation** [reached the public Internet](https://thenewstack.io/openai-huggingface-sandbox-breach/) from an environment designed to be isolated. Package installation through an internal registry proxy and cache was the only intended network path.

The models found a previously unknown vulnerability in that proxy. They escalated privileges, moved laterally to a node with Internet access, then used additional vulnerabilities and stolen credentials to intrude into Hugging Face’s production infrastructure.

The isolation policy said the public Internet was out of bounds – but the running system proved otherwise.

This was not a story about absent monitoring. OpenAI says its security team detected anomalous activity internally. [Hugging Face reports](https://huggingface.co/blog/agent-intrusion-technical-timeline) that it combined runtime and SIEM signals into an attack signal, but the alert wasn’t critical enough to prompt the on-call team promptly.

Hugging Face investigators recovered roughly 17,600 agent actions across several trust boundaries. The signals existed. They didn’t trigger intervention early enough.

> “A configured boundary does not prove what is reachable at runtime.”

[Anthropic’s review](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) of 141,006 cybersecurity evaluation runs found three incidents involving six runs, revealing a different failure mode. Those models reached real systems because an evaluation environment had unintended Internet access. That was a configuration failure, not an exploited sandbox escape.

These were capability evaluations, not normal production deployments. Both organizations report that they removed or reduced standard deployment safeguards to measure underlying cyber capabilities.

But the governance lesson still holds: A configured boundary does not prove what is reachable at runtime.

## Why AI agents change the containment problem

Runtime detection and defense-in-depth are not new. Agents change the execution model.

In a fixed workflow, code specifies intermediate steps. A tool-using agent can choose and revise those steps while it runs. It can react to a result, retry a failed path, and use one tool’s output as another tool’s input.

That changes what must be governed. A DNS lookup, package download, or credential read may be harmless alone. In the right sequence, the same events can form a path from a sandbox to a production system.

Design-time governance sets the conditions: isolation, identities, tool permissions, policies and approvals. Runtime governance measures what happened against those conditions and changes system state when the two diverge.

Observability does not replace prevention. It shows when prevention no longer matches reality.

Governance frameworks already reflect this distinction. For high-risk systems, the [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32024R1689) requires automatic event logging, human oversight capable of detecting anomalies and interrupting a system, and post-market monitoring throughout its lifetime. [NIST’s Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) similarly calls for post-deployment monitoring, escalation, and incident response.

> “Observability does not replace prevention. It shows when prevention no longer matches reality.”

Those frameworks establish the requirement. Agents compress the response window in which it must be met. One deployment-specific measure makes that visible:

```

actions_before_containment = agent_action_rate x detection_to_containment_time

```

This does not measure the severity of those actions. It measures how many can occur before the system intervenes.

## Four properties that turn telemetry into governance

The answer is not simply more logs. A runtime evidence system needs four properties.

**Coverage:** Are the transitions that change authority or create an external effect instrumented? Relevant events include [agent and run identity](https://thenewstack.io/securing-autonomous-ai-agents/), tool calls, process execution, privilege changes, credential use, network destinations, package retrieval, resource changes, and policy decisions. Log volume cannot compensate for a blind trust boundary.

> “The answer is not simply more logs. Log volume cannot compensate for a blind trust boundary.”

**Correlation:** Can an external effect be traced to the action that caused it? The evidence should identify the agent run, tool call, policy decision, and descendant actions. A planner trace without process, identity, and network evidence shows the request, not its effect. Process and network evidence without the agent trace shows the effect, not the decision that caused it.

**Timeliness:** Can the system intervene before the action becomes irreversible? Place synchronous gates in front of high-impact actions such as public egress, credential access, code execution, and production writes. Streaming analysis handles patterns that become dangerous only across several events. A separate response service can then suspend the run, isolate the workload, or revoke its credentials.

**Auditability:** Can investigators reproduce the finding without trusting the agent’s account? My [earlier article](https://thenewstack.io/agent-evidence-packet-analytics/) argued that database-backed observations should remain separate from an agent’s interpretation. The same separation applies here. The agent may explain its actions, but its explanation is not the audit record.

## From evidence to intervention

Telemetry becomes containment only when it is connected to a response:

```

agent action + policy decision + infrastructure effect
                         |
                         v
               correlated evidence
                         |
                         v
                      response

```

Agent actions, policy decisions, and infrastructure effects establish what was attempted, permitted, and changed. Correlating them turns separate events into evidence. Connecting that evidence to a response turns observability into containment.

This evidence creates its own analytical workload. Agent runs, tools, identities, policy decisions, processes, and network destinations all add dimensions. Removing those dimensions before analysis can remove the signal that identifies the violating run.

The evidence in this feedback loop comes from two instrumentation layers, and the coverage list above spans both. The agent runtime emits run identity, model calls, tool calls, and guardrail checks. The infrastructure emits process execution, credential use, network destinations, and resource changes. Neither layer can reconstruct the other. Infrastructure logs cannot say which run or which tool call opened a connection. An agent trace cannot say what the connection reached.

The agent layer is the [domain of LLM observability](https://thenewstack.io/what-is-llm-observability-and-monitoring/). Langfuse records each step an agent takes as a [typed observation](https://langfuse.com/blog/2024-07-ai-agent-observability-with-langfuse), including agent, tool, generation, and guardrail steps, and distinguishes the tools available to an agent from the tools it called. That distinction supports filters for sensitive tool use and looping tool paths, with alerts on the result. Trace context propagates across service boundaries and [through MCP calls](https://thenewstack.io/mcp-ai-agents-api/), so one trace can span a multi-service agent and its tool servers.

[DKB](https://langfuse.com/users/dkb) runs an assistant for roughly 6 million banking customers that can change transfer limits and block cards, with the customer confirming each action. Langfuse traces every interaction, automatically screens for compliance violations, and routes flagged cases to human review. [Cresta](https://langfuse.com/users/cresta) propagates trace context across a Go agent service, a Python retrieval pipeline and a tool-execution service, so one trace covers the full call tree.

ClickStack covers the infrastructure layer. It collects OpenTelemetry logs, metrics, and traces as wide events in ClickHouse, allowing teams to correlate high-cardinality telemetry with SQL during live detection and forensic investigation.

The two layers share trace context. An application instrumented with OpenTelemetry can [export the same traces to both](https://langfuse.com/integrations/clickhouse/observability) so that each tool can identify the same request. Logs and metrics continue to flow to ClickStack, where SQL correlates them with those traces. Both store their data in ClickHouse.

> “Governance is not the policy document. It is the system’s ability to show whether the policy held, explain what happened when it did not, and stop the consequences from spreading.”

Langfuse and ClickStack complement policy engines, identity systems, and enforcement mechanisms. Policy engines evaluate what is allowed, identity systems establish who or what is acting, and enforcement mechanisms carry out the response. The two observability layers bring their signals together with observed behavior, with ClickHouse serving as the analytical foundation for correlation and investigation.

That runtime governance loop should pass four tests:

1. Every critical trust boundary has telemetry coverage.
2. You can trace every high-impact action from agent identity and policy decision to downstream effects.
3. Evidence reaches a policy gate or bounded stop path in time to prevent or contain irreversible effects.
4. The audit record remains independent of the agent’s narrative.

Governance is not the policy document. It is the system’s ability to show whether the policy held, explain what happened when it did not, and stop the consequences from spreading.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/07/e3f55e06-manveerprofile_20845237de.avif)

Manveer is co-founder of Zenith, previously Director of Engineering at Confluent and led Growth Engineering at Dropbox.

Read more from Manveer Chawla](https://thenewstack.io/author/manveer-chawla/)