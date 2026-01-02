Observability is not living up to expectations. As [prices continue to rise](https://thenewstack.io/how-can-we-solve-observabilitys-data-capture-and-spending-problem/), the pain is increasingly felt.

This year has a foreboding sense of increased infrastructure complexity to manage at scale. In reaction to skyrocketing public cloud pricing, many organizations have shifted toward private cloud, often resulting in even more complexity.

At scale, organizations now increasingly face multi-cloud and heterogeneous environments spanning public cloud, private cloud and on-premises systems. In many cases, the cost buildup is seen as prohibitive.

At the same time, [observability](https://thenewstack.io/introduction-to-observability/) remains a necessity for organizations both large and small. In 2025, observability players and suppliers reflected a shift in how they help customers use their solutions, particularly by helping them avoid surprise observability bills of $130,000 per month or more.  (Stay tuned about how this happens, since observability metrics generally scale  much more than compute does.)

Up to 84% of current observability users struggle with the costs and complexity of their daily monitoring responsibilities, Gartner analysts Pankaj Prasad and Matt Crossley wrote in their [annual hype cycle report on observability and monitoring](https://www.gartner.com/en/documents/6755734), published in July. Still, they concluded, observability is uniquely positioned to address these technology challenges.

“The core issue is that the economics of observability have been upside-down for years. Costs grow linearly with telemetry volume, but the value doesn’t,” [Tom Wilkie,](https://uk.linkedin.com/in/tomwilkie) CTO at Grafana Labs, told me. “What we need, and what we’re now finally seeing, is a model where cost scales with insight, not ingestion.”

## Rethinking the ‘Big Data Lake’ Model

In 2025, the observability market was often seen as top-heavy and centralized, creating high levels of frustration and cost issues for customers while the value seemed to be declining.

Large vendors charge for indexing and retention by throwing everything into a big system or data lake, [Bob Quillin](https://www.linkedin.com/in/bob-quillin-46802511/), founder and CEO of ControlTheory, told me.  A more contrarian model, he said, involves putting more intelligence at the edge and using a feedback system.

“By distilling data at the edge, companies only send up what the AI tools need, allowing the system to run next to existing tools instead of trying to sit on top of them,” Quillin said. “The way the market has developed over the last 20 years has been to throw everything in a big system and users pay for indexing, retention, all that. But now that we have more intelligent systems, you don’t need to put all the data up there.”

Indeed, many platforms still encourage teams to collect everything while providing limited or no transparency into which telemetry data is actually valuable.

[Bill Hineline](https://www.linkedin.com/in/billhineline/), field CTO for [Chronosphere](https://chronosphere.io/?utm_content=inline+mention), told me: “The resulting surprise bills and increased operational overhead required to manage them have created the impression that observability itself was a bad investment, when in reality the investment was poorly governed.”

## How AI (Plus Context) Can Help

AI, of course, come into play in 2025, forcing organizations and [platform engineering teams](https://thenewstack.io/can-platform-engineering-accelerate-ai-adoption/) to choose how to integrate AI. At the very least, and especially in the tools I’ve tested — such as Grafana’s AI — it does no harm. In fact, it can help, if used properly.

However, AI can lend particularly good support for interpreting log data. Logs are essentially a language, and “if you throw the right information into a [large language model](https://thenewstack.io/introduction-to-llms/),” Quillin said, it can help explain what happened.

Users should be able to “throw a log into their favorite LLM via back-end APIs,” Quillin said. “This helps bubble up patterns, such as repeated critical metrics, and assists in pattern analysis and heat charts to separate the signal from the noise.

“As more code is created by AI, the complexity of logs is not getting simpler, necessitating a step back to look at the fundamentals of how data is analyzed. Since logs are language and if you throw the right information into an LLM, it can actually help explain what happened with the log – it looks across all your logs and bubbles that up and looks at a lot of pattern analysis.”

In many ways, Wilkie said, AI further “inflated and mis-set expectations,” in 2025.

“AI can be truly helpful, but only when it’s grounded in context rather than treated as a magic layer sprinkled on top of observability,” he said. “The mistake many vendors make is assuming AI adds value simply because it exists, when in practice, AI only works if the underlying telemetry is high-quality, well-structured and connected across systems.”

The real opportunity is what was observed in 2025, Wilkie said: “AI that turns observability from a specialist-only discipline into something every engineer — and even non-engineers — can use.”

“And importantly, instead of burying teams under more data, AI helps them extract more value from the data they already have,” he said. “AI won’t replace operators in 2026, but it will finally help them keep up with the complexity curve.”

AI applied superficially can feel like a productivity boost without delivering real operational clarity, [David Jones](https://www.linkedin.com/in/davidlewisjones/), vice president of NORAM solution engineering at [Dynatrace](https://www.dynatrace.com/?utm_content=inline+mention), told me.

“Many tools layer generative AI on top of raw telemetry, which may assist with querying but doesn’t fundamentally improve understanding,” Jones said. “That’s where confusion creeps in: AI without context amplifies uncertainty rather than reducing it.”

## OpenTelemetry: Poised to Make a Big Impact

With the added complexity at every level, and with environments becoming harder to manage through observability, the barrier to entry remains high—not only to understand how to make use of logs, metrics and traces, which I would argue are not so-called pillars of observability, but essential, intertwined components, along with other metrics, that must be used together.

This is where [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) (OTel) has made [huge strides in 2025](https://thenewstack.io/opentelemetry-adoption-update-rust-prometheus-and-other-speed-bumps/), becoming more accessible not only across different programming languages, but also across metrics, logs and now traces. Thanks to standardization, it has significantly lowered the entry threshold, which is why we are seeing a number of new and growing observability players offering their solutions.

Modern systems are becoming harder to operate, and that rising complexity is a big reason the barrier to entry has stayed high.

“OpenTelemetry has genuinely helped here: by standardizing instrumentation across languages and signal types, it’s removed a tremendous amount of friction,”  Wilkie said. “Teams no longer have to piece together vendor-specific SDKs, and new observability players can enter the market more easily because instrumentation is no longer the moat.”

OpenTelemetry helps by giving organizations vendor-neutrality, Wilkie said, allowing orgs to switch more easily to vendors that actually listen to and act on their customers’ cost and value concerns.

Indeed, OpenTelemetry helps “break the old dependence on proprietary agents and opaque pricing,” he said. “It’s when you pair OTel with intelligent systems — which can reduce data by 80 to 90% while increasing the value of what remains — you start to flip the equation so that cost scales with value, not telemetry volume. Observability hasn’t failed; the business model did.”

However, standards are only useful if they gain wide adoption, while legacy systems “stick around in organizations for decades,” Wilkie said.

“The cost of re-instrumentation is prohibitive,” he said. “OTel is making greenfield work easier, but customers still need to weave together new and old systems into a coherent picture – and need observability systems that don’t lock customers into one way of doing things.”

My bet is that OpenTelemetry will play a significant role if its experience can be improved. The complexity of the tools themselves also needs to be reduced so that observability is not usable only by an organization’s star in-house observability expert.

Vendors are beginning to wake up to the fact that non-technical users should be able to make use of observability and telemetry data as well — but we are not there yet. Maybe, one day, AI agents will monitor observability metrics and troubleshoot and predict future failures with no input from humans. But that day is not going to come in 2026.

## Closing the Usability Gap

In the meantime, the non-technical stakeholders must also invest time and effort into learning to interpret telemetry data, regardless of how simple to use observability tools become.

“OpenTelemetry is foundationally changing the potential for the future by democratizing how observability is done. It has become a de facto standard that lowers the barrier to entry, as organizations are now standardizing on it rather than just considering it,” Quillin said. “Using an open source tool built on these standards allows for a less commercial, more authoritative conversation about the broader problems in the industry.”

Wilkie echoed the notion that OpenTelemetry solves one part of the problem: standardizing and generating telemetry.

“But the usability gap, especially for non-experts, is still there,” he said. “Instrumentation today still feels too much like a tax: too many configuration knobs, too many semantic conventions to remember, too many edge cases when services behave in surprising ways. Standards solve interoperability, not usability. So yes, OTel will play a bigger role, but only if it becomes simpler.”

OpenTelemetry may not ultimately “save” observability, but it should go a long way by improving standardization for instrumentation and interoperability between different tools. It should also serve as a springboard for providers as they worry less about integration and can develop real solutions that empower what observability can and should do, for not only the in-house expert but all stakeholders.

“When OpenTelemetry is treated as foundational plumbing across the enterprise, observability platforms can deliver more consistent, out-of-the-box insights without relying on heavily customized dashboards,” Hineline said. “Today, many dashboards are still built by experts for experts, which leads to dashboard sprawl and limits who can effectively use observability. When combined with a strong strategy, OpenTelemetry can materially improve usability by enabling more consistent, reusable views across teams.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)