**OpenSearch is a top-level open-source project** under the Linux Foundation, backed by Amazon Web Services and other prominent players. The OpenSearch Observability Stack unifies AI agent tracing, APM, service maps, logs, metrics, and dashboards in a single open-source, OpenTelemetry-native platform, with built-in ML-powered anomaly detection and a new Piped Processing Language (PPL).

On September 10, [Joshua Bright](https://www.linkedin.com/in/joshua-bright-9411022/), senior product manager at [AWS OpenSearch](https://aws.amazon.com/what-is/opensearch/), will give a technical deep dive for site reliability engineers (SREs) and platform engineers running observability at scale, where alerting is usually the first thing to break.

## **Register now**

SREs aren’t short on telemetry. The problem is that the tools built to act on it haven’t kept pace, and the gap is widening as AI agents add a new, high-volume signal to what teams already monitor. The Linux Foundation has [reported](https://www.linuxfoundation.org/press/opensearchcon-north-america-2026-to-showcase-five-years-of-innovation-powering-enterprise-search-observability-and-analytics) that 77% of organizations already consider [OpenSearch](https://opensearch.org/) a core or supporting component of their AI infrastructure, with agent tracing among the reasons.

Query languages built for simple thresholds struggle with multi-signal correlation, alert rules sprawl across disconnected tools, and on-call engineers spend more time triaging false positives than investigating incidents.

To close that gap, the OpenSearch team is introducing two new capabilities: Piped Processing Language (PPL) for alerting, and a unified Alert Manager.

PPL brings a familiar Unix pipeline model to observability queries, allowing engineers to filter, transform, and correlate across logs, metrics, and traces using readable syntax.

By chaining steps together the same way you would at a terminal, PPL allows teams to build multi-step alert conditions that spot nuanced failure modes, such as a latency spike in an AI agent’s tool call that only becomes actionable when log error rates are also elevated. Because PPL skills transfer directly across search, analytics, and alerting workloads, conditions that were previously too complex to maintain become straightforward to build and pass on to teammates.

## **Centralized alert routing and Apache 2.0 licensing**

Alongside PPL, the new Alert Manager gives teams a centralized interface for managing alert rules, routing, suppression, and escalation, so the strategy on paper matches how the team actually responds to incidents. Everything covered in this webinar ships under the Apache 2.0 license, with no feature gating.

[**Join us on Thursday, September 10, 2026** **– Register Now**](https://thenewstack.io/webinar/smarter-alerting-at-scale-live-opensearch-demo-on-ppl-unified-alerting/)

The session includes a live demo of both capabilities against a realistic observability workload, plus an open Q&A, so bring your own alerting questions for the Amazon team. [Register now](https://thenewstack.io/webinar/smarter-alerting-at-scale-live-opensearch-demo-on-ppl-unified-alerting/) to save your spot for 12 p.m. Eastern/9 a.m. Pacific on Thursday, September 10.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/09/533ec2dc-cropped-379ef74d-charles-humble-5-600x600.jpg)

Charles Humble is a former software engineer, architect and CTO who has worked as a senior leader and executive of both technology and content groups. He was InfoQ’s editor-in-chief from 2014-2020, and was chief editor for Container Solutions from 2020-2023....

Read more from Charles Humble](https://thenewstack.io/author/charles-humble/)