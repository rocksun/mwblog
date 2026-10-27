**The AI race** is often measured by model quality, speed, and token cost. For business leaders, those measures contribute to a larger question: Can an organization deliver useful AI outcomes reliably, at the right cost, and with a level of risk it can defend?

To answer that question, organizations need comparable evidence and data across changing models, frameworks, and providers. OpenTelemetry helps by giving teams a common way to capture and describe AI behavior. That can reduce the need to maintain a separate data model for each integration.

[Shared AI conventions](https://thenewstack.io/standardizing-the-language-of-observability-in-opentelemetry/) can reduce duplicate integration work, make providers and models easier to compare, and support decisions about quality, cost, and risk. Consistent data also gives teams a stronger basis for scaling AI applications.

## Interoperability reduces the cost of change

AI applications have many parts: model providers, orchestration frameworks, retrieval systems, tools, and evaluation services, to name a few. Each may handle a conversation or agent action differently. Teams spend time normalizing those differences before they can investigate failures or compare results. These subtle differences slow product improvement and make switching observability providers more expensive.

> “Standardization doesn’t require every system to store every detail in the same way. It does require enough shared meaning to compare what matters.”

That distinction matters to businesses. Standardization doesn’t require every system to store every detail in the same way. It does require enough shared meaning to compare what matters. [OpenTelemetry’s GenAI conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md) describe common conversation and message concepts while accounting for the limits of representing complex data in telemetry. They also allow large content to be stored externally, with references retained in telemetry.

Splunk’s Agent Observability work illustrates the practical value of this approach: it’s built on OpenTelemetry and [AGNTCY](https://agntcy.org/) standards to provide vendor-neutral monitoring across AI agents and applications. The aim is to give teams a way to correlate agent behavior with performance, quality, cost, and risk — even as the underlying stack changes.

## Measure the outcome, not just the tokens

Token counts help explain spend, but they don’t tell you whether that AI spend was tied to useful work or added business value. A less expensive model can consume more tokens or require more retries to complete a task. A higher-cost model may be more efficient if it reaches the desired result reliably on the first attempt.

That makes cost per outcome a more useful business measure than cost per token alone. A successful outcome might be a completed workflow or an accurate answer that meets an agreed quality bar. OpenTelemetry provides the framework for collecting consistent data about model calls, latency, errors, usage and tool interactions, regardless of what model, backend, provider, or tools are in use. The organization still needs to define success and measure it against the cost and use of these tools.

> “Token counts help explain spend, but they don’t tell you whether that AI spend was tied to useful work or added business value.”

Evaluation can help. An instrumentation-side evaluator can provide quick feedback close to the application, while platform-side evaluation can compare models and releases across workloads. With consistent telemetry, teams can use evaluation results to decide which model fits a task, whether a release improved performance, and where spending is driving value. They can do this regardless of changes to models, providers, or tool calls.

## Build for change without reinstrumenting

In addition, telemetry quality needs to be visible before production. Open source tools like [Observability Studio](https://github.com/signalfx/obstudio) provide a development-time example: teams can inspect local telemetry and validate whether it follows OpenTelemetry conventions. They can even use the tool to help add instrumentation that is compliant from the start. Catching missing or inconsistent data earlier can reduce rework and give operators stronger evidence when they need to troubleshoot or assess a release.

> “OpenTelemetry provides the framework for collecting consistent data, regardless of what model, backend, provider, or tools are in use.”

The business benefit is a quicker path from adopting a new AI capability to understanding how it behaves in connection with the organization’s business priorities and customers.

## Observability provides control for agent behavior

AI agents can select tools, retry operations, and trigger actions on behalf of users.  [An AI SRE agent](https://thenewstack.io/ai-devops-vs-sre-agents-compare-ai-incident-response-tools/), for example, might detect that customers can’t check out on a retail site, investigate the problem, restart a failing service, and confirm that purchases are working again. Teams need to know not just whether the agent responds, but whether it takes useful actions, follows safety rules, and knows when to stop and ask for help. A mistaken action can make an outage worse and damage customer trust, while repeated retries or endless troubleshooting can drive unexpected costs.

This is where observability starts to provide operational control. [Agent observability](https://thenewstack.io/agentic-ai-observability-operations/) can help teams evaluate behavior and track performance and cost. When connected to enforcement systems, it can also support guardrails that block harmful actions or outputs. Shared telemetry collected through OpenTelemetry can connect those controls to evidence about the agent’s steps, tool calls, and ultimately its business impact.

![Infographic comparing AI workflow telemetry and business insights, with and without shared OpenTelemetry conventions.](https://cdn.thenewstack.io/media/2026/10/d7274efd-image-1024x638.png)

The standard should make evidence portable; the business should define the policy to apply that evidence. Which actions require approval? What quality bar is acceptable? When should a request be routed to a person or a different model? OpenTelemetry doesn’t need to answer those questions. Instead, it gives teams the power to make those decisions using consistent information.

## Upstreaming is an investment in scale

For businesses, upstreaming their changes to open source can mean broader coverage and less duplicated engineering—but only when projects have clear ownership and sustained community maintenance.

AI instrumentation faces a similar challenge. Third-party libraries can support new frameworks and providers before the broader ecosystem catches up. Upstream proposals show the value of reusing mature instrumentation, along with the need to settle code scope, contribution rights, and long-term maintenance. For example, the [OpenInference proposal](https://github.com/open-telemetry/community/issues/3467) covers instrumentation code, while leaving its specification and semantic conventions outside the proposed scope.

> “The prize is not more data. It is the ability to scale AI with clearer decisions about value, reliability, and risk.”

For OpenTelemetry, the challenge is to agree on common evidence. Shared conventions can make model behavior easier to compare, reduce the cost of integrating new providers, and help teams connect AI performance to spend, customer experience, and business outcomes. Adopting OpenTelemetry’s standards also helps to minimize potential rework in the future.

The prize is not more data. It is the ability to scale AI with clearer decisions about value, reliability, and risk.

*KubeCon + CloudNativeCon is taking place in Salt Lake City, Utah, from November 9 to 12.* [*Register Now*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)*!*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/10/17262862-headshot-kceu-cc-kirby-mcthompson-600x600.jpeg)

Greg Leffler, Director of Developer Evangelism, is the lead evangelist for Splunk's Observability portfolio. He leads a team of engineer evangelists dedicated to educating the world about the need for and benefits of observability. He is the author of The...

Read more from Greg Leffler](https://thenewstack.io/author/greg-leffler/)