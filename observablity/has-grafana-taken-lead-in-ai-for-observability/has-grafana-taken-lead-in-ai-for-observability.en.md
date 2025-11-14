[Grafana Labs](https://grafana.com/) has integrated AI support into its [observability platform](https://thenewstack.io/traceloop-launches-an-observability-platform-for-llms-based-on-openllmetry/) and panel, offering practical improvements to the [observability](https://thenewstack.io/introduction-to-observability/) experience.

Whether Grafana is surging ahead of the observability vendor pack or not depends on how one measures the different vendors’ offerings.

Providers currently hold diverging philosophies on how best to use AI for observability. [DataDog’s](https://www.datadoghq.com/?utm_content=inline+mention) AI is very much dependent and built on [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) agents. [Kloudfuse](https://www.kloudfuse.com/)’s AI functionality is largely in support of data lake observability. [Chronosphere](https://chronosphere.io/?utm_content=inline+mention) is not as bullish on AI’s worth and applicability to support observability at this time.

Meanwhile, I can attest firsthand that Grafana’s AI support is useful when setting up and integrating Grafana with [OpenTelemetry](https://thenewstack.io/how-opentelemetry-works-tracing-metrics-and-logs-on-kubernetes/), bringing metrics data from both [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) and [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Platform data sources to gather metrics to my Grafana panel.

At a workshop held at October’s [ObservabilityCon](https://grafana.com/events/observabilitycon/) in London, I found myself stuck while creating a panel. I simply asked the AI assistant to set up a panel for me, which it completed in just a few seconds. When I got stuck at different points during the workshop — specifically while setting up the panel to integrate AWS data into GCP — it offered me relevant ways to proceed (see image below).

[![](https://cdn.thenewstack.io/media/2025/11/386a1b22-screenshot-2025-10-13-at-12.12.59%E2%80%AFam-1024x615.png)](https://cdn.thenewstack.io/media/2025/11/386a1b22-screenshot-2025-10-13-at-12.12.59%E2%80%AFam-1024x615.png)

My experience was limited during the workshop, of course, and ReveCom, my analyst firm, has yet to put it through the paces to more deeply analyze Grafana’s AI effort. However, I can affirm that it was useful. That says a lot, and it was definitely more applicable than just asking questions through Cursor or [Claude](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) assistant — or worse yet, with ChatGPT, which is often more worthless than not.

## Automating Rollbacks

During ObservabilityCon, Grafana described Grafana Assistant as an AI-powered chat integration built directly into Grafana, enabling users to interact with observability data through natural language. It uses [large language models](https://thenewstack.io/introduction-to-llms/) to generate queries, analyze results and iterate intelligently.

The Assistant is designed to help both non-technical users — those who might ask questions without building dashboards — and expert site reliability engineers who can customize behavior using rules and infrastructure context. It connects with tools like GitHub, AWS, and ticketing systems through MCP servers, and features “infrastructure memory,” which maps telemetry to understand dependencies.

Overall, Grafana Assistant was designed to make observability more accessible for technical and non-technical folks. It accelerates investigations and integrates AI seamlessly into workflows, according to a number of speakers during ObservabilityCon.

Integrations with MCP servers, semantic language rules for metrics and traces, and the ability to output diagrams are provided.

Additionally, Grafana’s Assistant Investigations, an autonomous agent system for troubleshooting, was introduced at ObservabilityCon. This feature uses data sources like the [Extended Berkeley Packet Filter (eBPF)](https://thenewstack.io/what-is-ebpf/) and runs in the background to explore issues from multiple angles.

Grafana Labs CTO [Tom Wilkie](https://www.linkedin.com/in/tomwilkie) described it to me this way during the conference: “The concept of AI assist focuses on making AI actually useful now, not just a future promise. The goal is to bring real value now by making it easier for customers to get started and diagnose problems. The internal philosophy is to apply AI to reduce the toil for on-call engineers.”

The AI assist features, such as the assistant and swarming investigations, recommend next steps (e.g., increasing connection scaling). Internally, Wilkie said, the company is already automating the application of these fixes.

A key action automated is the rollback of releases: Engineers are trained to roll back releases immediately rather than spending 30 to 40 minutes applying a risky fix, but human nature often causes them to try to resolve the problem properly, Wilkie said.

“Automating the rollback achieves the desired behavior and handles a lot of the toil for our engineers,” he said. “The vision is that in a few years, 70 to 80% of on-call load will just be handled autonomously by safe actions like rollbacks and scaling.”

This approach is possible because the software is built on abstractions like service-level objectives (SLOs), which allow agents to understand if a release is a regression or not without knowing the ins and outs of every service, Wilkie said. Grafana’s deep grounding in open source has played a role as well.

As he noted, “The company believes its open source foundation is its superpower when it comes to AI, as the models are already trained on the content generated by their open source projects.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)