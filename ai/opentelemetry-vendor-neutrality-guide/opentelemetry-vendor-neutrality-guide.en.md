The [OpenTelemetry](https://opentelemetry.io) (OTel) ecosystem provides us not only with a standard data format and transport mechanism for generating, processing, and exporting telemetry data, but also promises vendor neutrality. But what does that actually mean?

It’s certainly something that many have pondered before us, in conference hallway tracks and on LinkedIn. And it was a [LinkedIn post](https://www.linkedin.com/posts/joshuamlee_opentelemetry-otel-activity-7303855232763998208-ccf7) by Josh that got us started exploring this topic.

“I still hear people saying that ‘OpenTelemetry is vendor neutral so you can switch vendors any time you want to.’ … This is like saying that because the vCard format exists, it’s easy to switch from iOS to Android.”

![Josh Lee's LinkedIn post discussing vendor neutrality.](https://cdn.thenewstack.io/media/2026/05/c6911c89-0.png)

This, of course, got Adriana thinking and led [to this blog post](https://medium.com/womenintechnology/the-truth-about-opentelemetry-vendor-neutrality-d385957e2c2d), which expands on Josh’s initial musings.

We realized, however, that we had more to examine on this subject, specifically:

* How the OpenTelemetry community’s roots in distributed tracing steered it in a vendor-neutral direction.
* Understanding how the OpenTelemetry standard’s design makes it vendor-neutral.
* Understanding where the OpenTelemetry ecosystem’s vendor neutrality ends.
* Looking ahead: Can we make the OpenTelemetry ecosystem fully vendor-neutral, and should we?

Buckle up, kids! Let’s start exploring!

It’s helpful to understand why — why use the OpenTelemetry standard at all? Why use distributed tracing? Why care about vendor neutrality?

Let’s start with openness. **Observability (and monitoring) begs to be open**. Specifically, when we undertake the task of monitoring all the different systems used by an organization, open protocols that can serve as translation layers become invaluable.

> “Observability (and monitoring) begs to be open.”

But the OpenTelemetry ecosystem is somewhat new — and other attempts at universal monitoring formats have floundered. So why has the OpenTelemetry ecosystem seen such widespread adoption?

**Distributed tracing is the key to understanding the OpenTelemetry ecosystem’s success as a unifying force*****.*** Before microservices, monitoring meant logs and metrics; these signals had widely adopted and relatively open standards: e.g., [Prometheus](https://prometheus.io/docs/instrumenting/exposition_formats/#exposition-formats) or [SNMP](https://splunk.github.io/splunk-connect-for-snmp/v1.9.2/configuration/snmp-data-format/) for metrics, [syslog](https://en.wikipedia.org/wiki/Syslog) or the ELK stack’s JSON format for logs.

The open protocols in this case were straightforward: If each monitored entity could emit metrics and logs in some compatible format, they could be ingested and stored centrally by any number of tools.

As has been written about *ad infinitum* by Observability vendors, **microservices demand distributed tracing**. The information that could previously be gleaned from a single stack trace or log was now spread across dozens or hundreds of different processes.

Distributed tracing isn’t just a change in scope — it’s also a complete shift in context. To emit correct trace spans, each process needs to understand a small piece of context from the process that called it and communicate that context to downstream services. The boundary of an individual process’s instrumentation has expanded greatly.

This has enormous benefits. Reading a single distributed trace is *much* simpler than piecing together disparate logs based on tags. But it also comes at the cost of increased complexity that crosses the boundaries of individual technologies. All of a sudden, the [Java](https://thenewstack.io/in-the-ai-age-java-is-more-relevant-than-ever/) people must care a lot more about the instrumentation of the Python people and vice versa.

The first solution to this increased complexity came from vendors with proprietary agents and protocols. Each vendor created instrumentation SDKs for as many programming languages, frameworks, and runtimes as possible  — this duplicated effort. Before the OpenTelemetry standard came into existence, each vendor invested significant time, people, and money in creating their own instrumentation frameworks. It also created a lock-in effect for customers who had to embed proprietary SDKs in *every single software artifact* they shipped.

There’s an infamous [xkcd cartoon about standards](https://xkcd.com/927/) that makes fun of how we try to fix having too many competing standards by creating a new standard.  While that has held true in many cases, the OpenTelemetry standard has enabled format compaction. Instead of competing against each other, vendors were collaborating on a common standard. Soon, what differentiated vendors from one another was what they could do with the data ingested to provide value to their customers. We believe that this was possible because everybody working in the space agreed on some fundamental truths:

* Microservices demand more than traditional monitoring.
* Standardization is one of the core challenges of [monitoring and observability](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "monitoring and observability").
* Open formats enable collaboration on standardization across technological and organizational boundaries.

In other words: ***Observability begs to be open.***

## What makes an OpenTelemetry tool vendor neutral?

Now that we’ve established the need for the vendor neutrality provided by the OpenTelemetry ecosystem, we are forced to ask: What does it *mean* for the ecosystem to be vendor-neutral? It means that ***if you choose to send your Observability data to a different vendor, you don’t need to update your instrumentation***. THIS IS A BIG DEAL, because in the Before Times, changing vendors meant that you had to go through the painful process of updating your instrumentation, which meant that it was oftentimes easier to stick with the current vendor than go through the pain of re-instrumenting code to work with a new vendor.

Thanks to the OpenTelemetry standard’s vendor neutrality, you just need to update the destination you send your telemetry data to. In fact, if you’re evaluating multiple vendors, you can even send the same data to different vendors at the same time (à la “vendor bake-off”) to help you determine which vendor best suits your organization’s needs.

> “Thanks to the OpenTelemetry standard’s vendor neutrality, you just need to update the destination you send your telemetry data to.”

All this is made possible by the following components of the OpenTelemetry ecosystem:

* APIs & SDKs
* OTLP
* Collector

Let’s dig into how each one of these provides an additional layer of flexibility and compatibility.

### OpenTelemetry APIs and SDKs

The OpenTelemetry specification provides a standard definition of telemetry data and describes how to instrument code. The OpenTelemetry APIs and SDKs (more on those shortly) are defined in the specification. This ensures that users have a similar experience, regardless of the language they use.

The **OpenTelemetry application programming interface (API)** defines the methods for instrumenting applications and serves as the entry point for instrumentation. Each language supported by OpenTelemetry has its own API implementation.

The **OpenTelemetry software development kit (SDK)** implements the API and determines *how* the telemetry is generated and correlated. Each language supported by OpenTelemetry has its own SDK.

The API is intentionally separate from the SDK (i.e., the code that produces telemetry). This allows you to plug in any OpenTelemetry SDK of your choosing, whether it’s the official OpenTelemetry SDK, a vendor SDK, or your own. (Yes! You can write your own OpenTelemetry SDK! 🤯) As long as they implement the OpenTelemetry API, it doesn’t matter which one you choose.

This means that libraries (and your own code) can be agnostic about which SDK is used. This, in turn, empowers library vendors to provide out-of-the-box (OOB) instrumentation, which offers all the benefits of auto-instrumentation without the complexity or additional overhead. (Although auto-instrumentation is worth it if OOB-instrumentation is not provided!)

Not ready to commit to an SDK? No problem! Because the OpenTelemetry API also includes a minimal SDK. This allows you to instrument an application that will still run; however, keep in mind that no telemetry data will be sent to your backend until you plug in a proper SDK.

![Diagram of how OpenTelemetry sits between your service and backends.](https://cdn.thenewstack.io/media/2026/05/0d52fb5f-1-1024x284.png)

### OTLP

OpenTelemetry Protocol (OTLP) is a vendor- and tool-agnostic specification for encoding, transmitting, and delivering OpenTelemetry data. Telemetry data emitted by the SDK uses OTLP, and most Observability backends now support OTLP and are strongly encouraged to ingest it. For those who do not, there are exporters available that convert OTLP data to a tool-specific format. OTLP supports both HTTP and gRPC.

**OTLP is a kind of magic sauce.** There has been a burst of OTLP-compatible tools, which are all interoperable thanks to the shared protocol, format, and semantic conventions.

### Collector

The **OpenTelemetry Collector** is a vendor-neutral binary that ingests, transforms, and exports data to one or more Observability solutions.

The collector could be perceived as the agnostic agent that you will deploy in your environment.

Advantages of the Collector:

* **Decouples the telemetry source from its destination.** The Collector acts as a proxy of sorts. Telemetry is sent directly to a single destination — the Collector — which then forwards it to one or more backends.
* **Acts as a single agent for multiple data types.** The Collector can ingest multiple data formats from multiple data sources, including applications and infrastructure.
* **Distributed telemetry [data to multiple backend systems](https://thenewstack.io/data-intensive-applications-rewrite-2026/)**, effectively allowing you to do a vendor bake-off (or let teams use a combination of tools).

![Diagram of how OpenTelemetry Collector interacts with receivers, processors, and exporters](https://cdn.thenewstack.io/media/2026/05/77ecf221-2.png)

#### The beauty of interoperability

Speaking of multicast — this is one of the most awesome uses of the OpenTelemetry specification, and it’s not limited only to bake-off situations. The OpenTelemetry ecosystem’s open formats mean that interoperable tools can be used together at *all* *times*.

Let’s consider a few use cases.

Because the Collector allows you to send telemetry to one or more backends at the same time, you can choose to send each signal to a different destination.

![Diagram showing that the Collector can send telemetry to multiple backends at the same time.](https://cdn.thenewstack.io/media/2026/05/34a43f47-3-1024x284.png)

Perhaps you have an all-in-one backend that supports the OpenTelemetry signals. In that case, you can send all signals to the single backend.

If you’re between backends and don’t know which one to choose, you can send your telemetry data to two all-in-one backends at the same time, and compare them, bake-off style.

![Diagram showing OpenTelemetry Collector sending signals to two vendors.](https://cdn.thenewstack.io/media/2026/05/dbdfac62-4-1024x284.png)

Many organizations require long-term data storage for compliance reasons. In that case, you might choose not only to send your telemetry data to your favorite backend but also to send it to an on-premises tool for long-term storage.

Or suppose that you have an observability vendor that you absolutely love, and they meet 95% of your requirements. Still, they are missing one critical tool (e.g., not all commercial solutions support Profiling). The OpenTelemetry ecosystem helps you fill those gaps with other compatible open source or vendor tools.

![Diagram showing OpenTelemetry Collector sending signals to a vendor backend, and logs to On Premise long-term storage.](https://cdn.thenewstack.io/media/2026/05/5de53413-5-1024x284.png)

## Use Case 4: specific pipelines for specific teams

Suppose that your company uses backend A for production. Development teams might also want to use OpenTelemetry signals to troubleshoot their own code. These teams might therefore use a local open-source observability tool, such as [otel-tui](https://github.com/ymtdzzz/otel-tui), [OTel Front](https://github.com/mesaglio/otel-front), [or OTel Viewer,](https://github.com/CtrlSpice/otel-desktop-viewer) to help with troubleshooting.

Or consider another scenario. Suppose you work at Company A. It merges with Company B. Company A uses backend X, and Company B uses backend Y. Until both organizations are fully integrated, you might find the merged organization using two different backends at the same time.

![Diagram of two merged companies using different backends at the same time.](https://cdn.thenewstack.io/media/2026/05/0c88fac5-6-1024x284.png)

Using the OpenTelemetry standard means you can have everything you want. You can have your cake and eat it too… (As long as you are willing to pay for storing two cakes.)

## The vendor switch: know what you’re getting into

Now, what about those non-vendor-neutral parts of the OpenTelemetry ecosystem? Is that even a thing?

***When it comes to data ingestion, the OpenTelemetry protocol is absolutely vendor-neutral.***

Case in point: When Adriana switched jobs from Lightstep to Dynatrace, she was able to keep existing instrumentation on the demo code she’s used for various talks and courses, and all she had to do was repoint her OpenTelemetry Collector to a different backend. Boom. Magic. ✨ She was able to see her traces, logs, and metrics in the Dynatrace UI, just like she had in the Lightstep UI.

> “What nobody talks about, however, is that it’s not just about data ingestion, is it?”

What nobody talks about, however, is that it’s not *just* about data ingestion, is it? We must also consider things like:

* Look & feel
* Storage & historical data
* Queries & dashboards
* Alerts & SLOs
* Infrastructure-as-Code (IaC)

### Look & feel

If you’ve been working with Vendor X for a while, you’ve been used to doing things in a certain way. A certain workflow, if you will. Whether it’s your personal workflow or one your SRE team follows. Bottom line: using a new vendor means getting used to a new UI and the vendor’s specific nuances. Maybe Vendor X has features that Vendor Y doesn’t, which let you do some cool stuff with your OpenTelemetry data — which means that you must familiarize yourself with these new features to get the most out of them.

### Storage & historical data

The observability business model is data-driven. — practically every vendor charges based on some combination of *ingested* and *retained data*. As far as we know, no vendor allows historical telemetry data to be exported, which means that if you switch vendors, you lose your historical data unless you also send your telemetry data to an internally managed datastore at the same time\*.

(\*) *But you can do this now, thanks to the* OpenTelemetry protocol*— cool*

### Queries & dashboards

Most vendors have their own dashboards and querying languages — think PromQL for Prometheus, DQL for Dynatrace, and SPL for Splunk, to name a few. That means that when you switch vendors, you can’t simply “lift and shift” your dashboards. You must learn a new dashboarding interface, a new query language, and then translate your old vendor’s dashboard into the new vendor’s dashboard. Bottom line: they require time and effort to build out.

Like all things, there are exceptions to the rule:

### Alerts & SLOs

Some Observability vendors provide the ability to alert on service-level objectives (SLOs), which are themselves informed by OpenTelemetry metrics. If you choose to switch vendors, you must re-create your alerts and your SLOs. That is, if that vendor even supports alerts and SLOs.

## IaC

Many [major Observability vendors have their own Terraform providers](https://registry.terraform.io/search/providers?q=logging%20%26%20monitoring), which are super helpful for automating configuration across various aspects of your Observability vendor tool. Unfortunately, changing Observability vendors means changing Terraform providers as well. Also, not all Observability vendors’ Terraform providers let you configure the same things, which means this is, again, not a “lift and shift” situation.

**It should be noted that, thanks to agentic AI, some tasks, such as creating queries and dashboards and writing IaC code, greatly reduce migration efforts when moving from one vendor to another.**

## A future vision for vendor-neutrality

Every Observability Platform has its areas to shine; if they weren’t unique, there’d be no reason to switch. But they also share some fundamental characteristics. We need somewhere to put the telemetry we’ve collected (**Storage**), a way to explore that data (**Ad-Hoc Queries**), a way to share those explorations with our teams and future selves (**Dashboards**, usually), and a way to be notified when things aren’t good (**Alerts**).

![Diagram of a future vision for vendor-netruality](https://cdn.thenewstack.io/media/2026/05/9e054d79-7-1024x284.png)

While the OpenTelemetry project itself does not include any backend components, there are several open-source options, especially for storage, querying, and visualization.

But as we’ve also discussed, interoperability isn’t just about switching. What if our favorite vendor made their data store accessible via a universally available API, allowing us to store one copy of our observability data as a Single Source of Truth, while making it accessible to multiple analysis tools *at the same time*? This would allow us to add specialized analysis tools, in-house model training, customized reporting, and more, all from a single API — we think that would be neat.

![Diagram of Open Telemetry Collector sending signals to the vendor platform, making it accessible to multiple analysis tools at the same time.](https://cdn.thenewstack.io/media/2026/05/08274e15-8-1024x284.png)

## Can we live up to the promise of vendor neutrality?

The OpenTelemetry community has come a long way since it first came onto the scene. It emerged as a vendor-neutral solution to the challenge of distributed tracing, and has grown into the *de facto* standard for generating, collecting, and exporting Observability data.

We credit the strength of the OpenTelemetry project to a few key factors:

* **The fact that observability is open.** End-users have demanded it.
* **Support — since its inception — of multiple vendors.** No vendor takes up the spotlight.
* **The stewardship and governance of the CNCF.** The project truly feels like a community, with individuals and organizations working together toward a common goal of a standard telemetry framework.

And it continues to evolve. Just a few years ago, OpenTelemetry tooling was predominantly used in the instrumentation layer, with vendors providing proprietary exporters to speak with their agents. Now, OTLP is widely supported, and running OpenTelemetry Collectors instead of or alongside vendor agents is commonplace.

The open source ecosystem has also embraced the OpenTelemetry community. Jaeger was originally built around its own (open) tracing protocol. [It now](https://opentelemetry.io/blog/2022/jaeger-native-otlp/) natively supports the OpenTelemetry protocol. And Prometheus, a popular tool, [is now co-evolving with the OpenTelemetry](https://prometheus.io/docs/guides/opentelemetry/) ecosystem so that the benefits of shared standards can be enjoyed everywhere.

Will we continue to see more such changes? Only time will tell, but the future is looking bright.

Until then, remember this: the wonderful thing about the OpenTelemetry ecosystem is choice. Vendor neutrality and [open standards enable](https://thenewstack.io/how-open-standards-enable-zero-trust-on-commodity-hardware/) so much more than “switching vendors” one day — although they certainly help with that too. The benefits of open formats are portable data and interoperable tools, allowing you to compose the observability solution youneed *today*.

The key is — does a solution enable you to ask meaningful questions, get useful answers, and act on what you’ve learned? Because at the end of the day, if your applications and systems are more reliable, that’s what matters most.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/05/261847bb-cropped-ed369392-64d6-400o400o2-94yyamxsepfa2wpkmp51hk.jpg)

Adriana Villela is a Sr. Developer Advocate at ServiceNow Cloud Observability (formerly Lightstep). She helps companies achieve reliability greatness through observability, SRE, and DevOps practices. Previously, she managed a Platform Engineering team and an Observability Practices team at Tucows. Adriana...

Read more from Adriana Villela](https://thenewstack.io/author/adriana-villela/)

[![](https://cdn.thenewstack.io/media/2026/05/8602095d-joshlee_headshot.jpg)

Josh is a Developer Advocate at Altinity, where he applies his observability and engineering background to ClickHouse use cases. He has over 15 years of experience developing and leading software projects for clients across various industries. Josh is also a...](https://thenewstack.io/author/josh-lee/)