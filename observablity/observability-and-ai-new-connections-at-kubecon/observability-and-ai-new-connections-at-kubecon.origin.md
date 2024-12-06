# Observability and AI: New Connections at KubeCon
![Featued image for: Observability and AI: New Connections at KubeCon](https://cdn.thenewstack.io/media/2024/12/20bff831-observability-ai-1024x576.jpg)
SALT LAKE CITY — An undercurrent running so much of the product news and conversations at [KubeCon + CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) was how [AI](https://thenewstack.io/ai/) is now connecting with so much established tech.

Case in point: announcements by [observability](https://thenewstack.io/observability/) companies [New Relic](http://newrelic.com/?utm_content=inline+mention) and [Splunk, a Cisco Company](https://www.splunk.com/en_us/products/observability.html?utm_content=inline+mention).

New Relic announced general availability for its [new one-step observability for Kubernetes](https://newrelic.com/platform/kubernetes-pixie), which automatically connects application performance monitoring (APM) with Kubernetes deployments, requiring no additional configurations. The product gathers telemetry data (it offers native support to [Prometheus](https://prometheus.io/) and [OpenTelemetry](https://thenewstack.io/new-relics-opentelemetry-and-open-source-commitment/)) and, through dashboards, displays AI-based insights based on that data.

The benefit is that visibility is easier, [Jemiah Sius](https://www.linkedin.com/in/jemiahsius/), senior director of developer relations at New Relic, told The New Stack at KubeCon.

“What we’re doing with one-step observability, we’re removing all of that hassle, basically,“ Sius said. “So out of the box, you’re getting insight into your Kubernetes environment, but also into the applications that are deployed into your cluster.”

How does it work? “We’re gonna have our own container, basically, that is going to handle all of the work of pulling in or auto-instrumenting the application.

“You already get that out of the box with adding New Relic in for your infrastructure tier. So now, instead of you having to actually augment any of your configurations, it will just run it as kind of like a side call, and then pull all that data together.”

![Jemiah Sius of New Relic.](https://cdn.thenewstack.io/media/2024/12/db777591-jemiah-sius-300x260.jpg)
Jemiah Sius of New Relic .(Source: Heather Joslyn)

In a follow-up email, Sius drilled down into just how that “container” works: “In Kubernetes, the Mutating WebHook intercepts API requests for deploying pods onto nodes. Reflecting the configurations specified, it mutates the pod specification to add an NR init container and environment variables using a standalone newrelic-mutate-pod. Following the establishment of the pod, the New Relic APM Agent is seamlessly integrated into the application housed within the user’s K8s pod.”

At KubeCon, Splunk announced the general availability of some new features of its comprehensive [observability](https://thenewstack.io/observability/) portfolio. Among them, Splunk Observability Cloud’s Tag Spotlight capability now has an AI enhancement that provides a more nuanced understanding of common problems that arise across applications and the end-user experience, enabling faster troubleshooting and better resolution of incidents.

The company is investing in AI-enhanced solutions, [Morgan McLean](https://www.linkedin.com/in/morganmclean), senior director of product management at Splunk, told TNS.

Cisco’s [AppDynamics](https://www.appdynamics.com/?utm_content=inline+mention), McLean noted, has traditionally served older, legacy systems. “The big focus right now in our part of Splunk observability is on the integration with AppDynamics, and being able to take features that people really loved in AppDynamics, like business transactions and snap results and various others, and bring those to Splunk observability for customers who want to use them there, as well as increasing our general support in AppDynamics for more platforms.”

## Alleviating Alert Fatigue
Investment in AI capabilities is part of that effort to integrate Splunk and AppDynamics’ offerings. Nearly everyone (97%) [surveyed by Splunk in a report it released in October](https://www.splunk.com/en_us/form/state-of-observability.html) said they use AI- and machine learning-powered systems to enhance observability operations. That’s up from 66% in the 2023 version of the study.

When you drill down into the data, there’s definitely room for more use of AI in observability solutions. AI- and ML-enabled tools were used by 55% of Splunk’s respondents to complete investigations and determine the [root cause](https://thenewstack.io/machine-learning-for-automated-root-cause-analysis-promise-and-pain/) of issues.

The Splunk report is based on a survey of 1,850 IT professionals in May and June 2024.

One pain point AI can help solve is alert fatigue. Fifty-seven percent of participants [in a survey Splunk released in October](https://www.splunk.com/en_us/form/state-of-observability.html) said they associate alert fatigue with observability solutions.

In the past, McLean said, he’s been an on-call engineer, and he understands the pain.

“Alert fatigue is brutal,” he said. “Woken up in the middle of the night, your phone starts going crazy, and you look at it, and maybe it’s important, maybe it’s not, and you need to sit down and register and decide whether this is something that should be ignored or needs immediate action.

“Some organizations have good hygiene about it, but that requires a lot of manual effort and processes to constantly update and prune your alerts to make sure they’re good. There are a lot of things that we can do, and we’re investing in Splunk to improve that,”

## What’s Next for OpenTelemetry?
McLean is also the co-founder of [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/), a standardized way to collect observability data (metrics, logs and traces). The release of OpenTelemetry [profiling signals](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/) into general availability, once slated for the end of 2024, is now likely to slide into the middle of 2025, he said.

“In [OpenTelemetry](https://opentelemetry.io/), or any sort of standard like this, there’s a lot of work that takes place on specifying behavior,” he said. “This is not code, this is actual people writing human language.”

In addition to OTel’s collector agent, it also must capture data from applications within languages like [Java](https://thenewstack.io/java/), [Python](https://thenewstack.io/python/), etc.

“And all of those have to behave consistently because if one of them decides to capture data in a different way, that’s shaped in a different way than all the others, you can’t process it,” McLean told The New Stack. “You need to get consistent data. So there’s still a bit of spec work that’s taking place for profiling.”

![Morgan McLean, of Splunk, a Cisco Company.](https://cdn.thenewstack.io/media/2024/12/b10e83b6-morgan-mclean-300x254.jpg)
Morgan McLean, of Splunk, a Cisco Company. (Source: Heather Joslyn)

The bulk of the work involved in getting those specs into the OTel protocol is already done, but the job isn’t finished, he said. Specific language implementations still need to be finalized.

“A lot of the remaining work is getting our Java support to talk to the Java profiling that’s built-in … None of this is particularly difficult, but we just have to do it on every single language.”

Another thing on the agenda: Finalizing the semantic conventions for integers. As McLean mentioned, the team is creating specifications to create consistency in how OTel profiling works across different languages.

“Not only do we need those implications to behave consistently, they need the data that they generate to have the exact same tags and attributes and things, so you can get some powerful analytics,” he said. “There’s a lot of work happening on that. It can be perceived as kind of boring work, but it’s really, really critical.”

Bringing profiling signals into open source OTel, McLean said, will help more organizations take advantage of profiling and reduce their costs, bringing a potentially niche capability into the mainstream.

“Splunk offers a profiling product,” he noted. “Many of the observability vendors do, and yet it’s usually a sort of small part of the offering.”

He drew an analogy: “Distributed tracing had existed for years before it really hit the mainstream, and much of the reason it did hit the mainstream was open . If you’re making it easy to do, profiling is similar.”

Last January, TNS expected that [OpenTelemetry’s support and adoption](https://thenewstack.io/opentelemetry-and-observability-looking-forward/) would continue through 2024.

- Fifty-eight percent of participants in the Splunk study said their primary observability solution relies on OpenTelemetry. This follows what our expectations were.
- However,
[a study](https://newrelic.com/resources/report/observability-forecast/2024)by New Relic and[Enterprise Technology Research](https://etr.ai/), also released in October, provides a bleaker picture, with only 10% of the more than 1,700 IT professionals surveyed saying they use an open source solution that integrates OpenTelemetry.
As for what’s farther out on the roadmap for OTel, McLean pointed to serving legacy systems. “OpenTelemetry is coming to mainframes,” he said. “There’s a workgroup, working on that. We’re adding support for IBM z/OS, IBM Z Linux.”

The goal is to help “large financial institutions and airlines and others who use OpenTelemetry already — on their Kubernetes clusters, on their [virtual machines], on most of their modern infrastructure,” which are still also dependent on legacy systems, capture all their data using modern rather than mainframe-specific observability tools. Those legacy tools, McLean said, won’t give those organizations full visibility of their entire systems.

## AIOps: In Decline or Just Rebranding?
However, the new data from New Relic and Splunk also point to some areas of concern for the future of AI in observability:

- Only 34% of respondents in the Splunk survey said their organizations can resolve a majority of their alerts using AI/ML. However, Splunk found that companies that have embraced observability are more than twice as likely to be meeting that milestone.
- AIOps tools are used extensively by 20% of the Splunk study.
- The New Relic report found that 24% of its survey participants use AIOps capabilities, down from 41% when the same study was conducted in 2023.
- Perhaps the drop is a response to
[AIOps’ bad reputation](https://thenewstack.io/sres-wish-automation-solved-all-their-problems/), and a rebranding to[AI-powered observability](https://thenewstack.io/ai-powered-observability-picking-up-where-aiops-failed/)better picks up actual usage patterns.
In a follow-up email to TNS, New Relic’s Sius explained the drop in people deploying AIOps capabilities: “The drop can likely be attributed to the rapid evolution of AI technologies, with new innovations like [large language models (LLMs)](https://thenewstack.io/supercharge-aiops-efficiency-with-llms/) reshaping how people define ‘AI.’”

“In 2023, most people were likely viewing AIOps as an umbrella term that encompassed a wide range of applications. But with significant advancements in AI over the past year, those surveyed in 2024 likely understood the AIOps label in a much different and more specific way.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)