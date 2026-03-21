As the observability industry pivots from proprietary systems to open frameworks, the traditional “pillars” of metrics, logs, and traces are gone. Instead, with the emergence of integrated data streams and open standards like OpenTelemetry, the race is on to help companies make sense of their newly-unified information.

It’s no longer just about access. Operators now face information overload, with thousands of alerts hitting their dashboards daily. The challenge is determining the actual cause of the problem and how to solve it amid all the chaos. This targeted analysis was difficult in the era of observability pillars, where disconnected data led to disconnected workflows. Companies used bespoke, proprietary solutions – sometimes even separate teams – to manage metrics, logs, traces, and profiles. Signals were siloed, and merging them was a time-consuming and expensive endeavor.

Now, as most observability vendors coalesce around one open framework in [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/), these pillars are collapsing. Instead of isolated, independent signals, data is consolidated to one feed, eliminating the need for signal-specific systems or teams. Instead, the new era will be defined by comprehensive, AI-powered platforms that empower operators to use unified telemetry data in more dynamic ways.

> “As the observability industry pivots from proprietary systems to open frameworks, the traditional ‘pillars’ of metrics, logs, and traces are gone.”

It won’t matter what’s a log, trace or metric. What matters is the intelligence provided. With a single search box, operators can use natural language prompts to query all signals simultaneously and return an ultimate answer. And this shift is poised to transform how operators detect and remedy issues that annoy users and add unnecessary operational costs – so long as it’s designed in a user-friendly manner.

## A focus on workflows

Operators used to complain about not having access to enough data. But as the [growing adoption of OpenTelemetry](https://thenewstack.io/what-new-data-tells-us-about-opentelemetry-adoption-for-mobile/) leads to more integrated data sets, the problem is quickly becoming filtering and presenting all the available information in a way that’s helpful to end users.

The more integrated the data becomes, the noisier it gets. As a result, the important signals, the root cause of the problem operators are trying to address, disappear into all the noise. This makes sense: human brains aren’t designed to find both correlation and causation across thousands of data points.

It’s why, instead of bespoke features targeted at a subset of the information, observability vendors are now battling to build the AI engines that can analyze metrics, logs, traces, and profiles together to provide actionable and auditable advice in a seamless and intuitive way. And within the enterprise setting, that means mimicking the workflows of human operators.

> “The more integrated the data becomes, the noisier it gets… human brains aren’t designed to find both correlation and causation across thousands of data points.”

For example, in the past, when there was a user-facing issue, operators would get an alert, go investigate a bunch of dashboards and try to find similarities between a bunch of, in essence, squiggly lines on a chart. Trying to uncover the potentially dozen of misconfigured Kafka nodes that are causing the issue could take a long time, and would likely require skillsets that remain in short supply. Operators must often start with a single trace as a starting point, and meticulously and tediously work from symptom to diagnosis.

Instead, AI can act as an intelligence layer above integrated observability data sets to alert operators to the issue, as well as provide the likely root cause and suggested next actions. Instead of just a single trace, the AI engine could analyze a much broader set of information. Not just individual traces, for example, but traces with profiles embedded in them, or logs that include links to a trace.

To effectively cut through the noise, there is a new set of core capabilities that organizations need, including:

* **An audit trail:** Users have to be able to verify the actions of the AI systems, and access the evidence that the underlying analytic engines are using to support the conclusion.
* **A [knowledge graph:](https://thenewstack.io/how-knowledge-graphs-make-data-more-useful-to-organizations/)** Can’t just dump a bunch of data into one place. Need to be able to map out how signals relate to each other, including interactions with other services and all their derivatives.
* **Cost controls:** The best way to control costs is to not process data that you don’t need. Also need to be able to track the small, single-percentage point increases in usage that add up quickly over time.

## Conclusion: The shift to AI

The observability industry’s evolution from siloed pillars to open, AI-powered platforms marks a fundamental shift. With OpenTelemetry driving data unification and AI engines providing real-time root cause analysis, operators are finally moving beyond drowning in alerts to acting on real insights.

What does this look like in practice? It’s not just automating alerts, it’s SRE-style AI agents running continuous analysis in the background, surfacing real-time insights in a simple, conversational interface. Instead of hunting through dashboards, operators will ask questions and get answers, moving from reactive troubleshooting to proactive, cost-efficient operations.

Looking ahead, observability is no longer about collecting signals. It’s about combining open data standards, cost-aware telemetry pipelines, and intuitive interfaces to transform noise into intelligence so operators can detect, diagnose, and fix problems faster – before users even notice.

*This guest column is being published ahead of [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), the Cloud Native Computing Foundation’s flagship conference, which will bring together adopters and technologists from leading open-source and cloud-native communities in Amsterdam, the Netherlands, from March 23-26, 2026.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/03/2466dc40-ted-young_-_alexa_becker.png)

Ted Young is the Developer Programs Director at Grafana Labs and is also one of the OpenTelemetry co-founders, currently serving as a member of the OpenTelemetry Governance Committee.](https://thenewstack.io/author/tedyoung/)