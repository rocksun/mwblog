*This article is part of a series. Read also:*

When considering whether to use [Fluentd or Fluent Bit, and even Fluent Bit](https://chronosphere.io/fluent-bit/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform) or [Open Telemetry (OTel)](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/), the answer need not be one or the other. From the outset, [Fluent Bit and Fluentd](https://thenewstack.io/a-guide-to-migrating-from-fluentd-to-fluent-bit/) have been built to communicate easily and seamlessly. Because of the way the [Fluent Bit](https://chronosphere.io/fluent-bit-academy/?utm_source=TNs&utm_medium=sponsored+content&utm_content=inline-mention&utm_campaign=tns+platform) and Fluentd solutions structure their payloads internally, we can take an OTel payload, wrap it inside the Fluent model and unpack it again.

The key to answering the question about Fluentd lies with the adoption of OTel for more than microservice use cases and the speed at which additional adaptors are developed.

In my opinion, new developments will become [Fluent Bit–based over the next couple of years](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/) because developers who may have considered Logstash will look to Elastic application performance management (APM) agents. However, solutions in production will see a slower rate of change with [Fluent Bit replacing Fluentd](https://chronosphere.io/learn/forward-protocol-fluentd-fluent-bit/?utm_source=TNs&utm_medium=sponsored+content). The most likely driver of change in existing software will be the adoption of OpenTelemetry.

With the data captured within Fluent Bit, we can parse semi-structured content to extract more meaning from the event, allowing more informed actions to be performed downstream. This process can be as simple as extracting a value from some text, such as whether the [log](https://chronosphere.io/learn/chronosphere-logs-control/?utm_source=TNS&utm_medium=sponsored+content) entry contains an error, extracting a numeric value for Prometheus to use, or to influence the routing of the event. The process can also be as complex as converting a custom format to a JSON representation.

The natural next step is filtering events, perhaps to discard them when they are insignificant, or to route them to one or more outputs. We could send the data to a central log repository and pass the event’s numeric elements to [Prometheus](https://prometheus.io/) as a metric.

Transferring data in groups of events is more efficient than transferring one event at a time. The start and end of each conversation have some small overhead, such as opening and closing network connections or opening and locating the end of a file and then closing the file handle.

Buffering or grouping events helps us make trade-offs in these activities, which is one of the roles of buffers, regardless of where they are. Because a buffer may not be a simple in-memory structure, it’s better to perform buffering after filtering, so if the buffer involves more than managing the data we already have in memory, we’re minimizing the effort.

The final step is putting the events somewhere. That might well be another Fluent Bit (acting as an OpenTelemetry node or a simple log event processor) or [Fluentd](https://chronosphere.io/learn/fluent-bit-vs-fluentd/?utm_source=TNs&utm_medium=sponsored+content) (taking advantage of its larger collection of plugin options or existing deployed monitoring infrastructure) or it could be one of the supported data stores or custom outputs that have been plugged in.

The diagram below takes the architecture view and adds some example sources, destinations and technologies that allow us to enhance Fluent Bit. This figure underlines the flexibility and compatibility of Fluentd and OpenTelemetry-compliant tools, in addition to a diverse range of other applications and technologies.

You’ll probably have noticed that Fluent Bit doesn’t do anything about data presentation or visualization. This comes down to the philosophy that an application has a single responsibility: Do one thing and do it well. For Fluent Bit, that one thing is getting observability data from what needs to be observed to the tools that allow us to visualize and analyze the data.

[![Fluent Bit logical architecture with some of the available plugins.](https://cdn.thenewstack.io/media/2025/07/874e9002-image.png)](https://cdn.thenewstack.io/media/2025/07/874e9002-image.png)

Fluent Bit logical architecture with some of the available plugins.

If you’re familiar with the architecture of Fluentd, you’ll recognize that the architecture, although implemented with different technologies, is reasonably similar at this level of abstraction. This similarity reflects the relationship between the two solutions and is a simple truism of event processing.

## Is Fluent Bit a Child or a Successor of Fluentd?

Although Fluent Bit started as a sibling of [Fluentd](https://www.fluentd.org), with support for OTel and other features arriving in the late 1.x versions, and as part of v2.0, it is fair to say that it has grown up to be Fluentd’s equal. This fact spawns a couple of questions:

* Do I need to learn Fluentd to learn Fluent Bit?
* Is Fluentd a legacy solution now?

To come to grips with Fluent Bit, you don’t need to know anything about Fluentd. But if you understand Fluentd at a high level, you’ll find that getting to grips with Fluent Bit is easy. There is no dependency between the products. In many respects, although the two products have a lot of overlap, they are complementary.

Whether Fluentd is a legacy technology is an architectural question — the answer is always, “It depends.” The drivers and capabilities incorporated into Fluent Bit mean that it fits neatly into the modern [Kubernetes](https://chronosphere.io/learn/kubernetes-component-logs-fluent-bit/?utm_source=TNs&utm_medium=sponsored+content)-centered, cloud native ecosystem, with the means to address all the demands of that ecosystem, although some features currently are not available in Fluentd. As previously discussed, Fluent Bit has a smaller, lighter footprint, making it suitable for containerized use cases.

Another factor is OpenTelemetry support. At the time of this writing, we have not seen a roadmap to equip Fluentd with support for OTel, which makes Fluent Bit by far the better choice for deploying into container-orchestrated environments such as Kubernetes and working with services, such as [Istio](https://istio.io/). Nothing stops us from deploying Fluent Bit in noncloud native environments, which typically have a wider portfolio of technologies with which to work. This scenario lends itself more to Fluentd for the foreseeable future, given the number of adapters it has available.

The skills required to create custom plugins are also more readily available; you simply need to grasp Ruby or another object-oriented language with built-in memory management, as listed in the [TIOBE Index](https://www.tiobe.com/tiobe-index). Although [WebAssembly](https://thenewstack.io/webassembly/) can enable extensions to Fluent Bit in languages such as [Java](https://thenewstack.io/introduction-to-java-programming-language/) and Ruby, it demands additional skills for a technology that is still proving itself to the mainstream.

As to whether Fluentd is history, the answer is no. Major vendors have invested in and used Fluentd for a long time, and that sort of investment is not one to walk away from. Furthermore, Fluentd and Fluent Bit have different technologies, and although they have some common ideas, they execute those ideas differently.

Many of the key contributors to the development of Fluentd are also working on Fluent Bit. Both solutions are being propelled forward to meet the demands and innovation needed by the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) ecosystem. Cloud native ideas and CNCF influence the world of software; not all cloud software deployments are as tightly bound to Kubernetes as others.

Put simply, Fluent Bit can do a lot and be applied to many use cases, but today, Fluentd fits some use cases better than Fluent Bit, and vice versa.

To read more about Fluent Bit, you can download the entire book, [“Fluent Bit with Kubernetes.”](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/c3489f3d-cropped-ba30d14d-phil-wilkins.jpeg)

Writing for Chronosphere, Phil Wilkins has spent more than 30 years in the software industry, with broad experience in businesses and environments from multinationals to software startups and consumer organizations to consultancy. He started as a developer on real-time, mission-critical...

Read more from Phil Wilkins](https://thenewstack.io/author/phil-wilkins/)