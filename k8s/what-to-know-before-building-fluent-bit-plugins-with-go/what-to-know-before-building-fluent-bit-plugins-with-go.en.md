***Editor’s note:** The following article is an excerpt from the Manning book: “[Fluent Bit with Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS),” a practical guide on optimizing systems for Kubernetes — from fundamental configuration to advanced integrations for log, metric and trace routing and processing. This article excerpt focuses on Go-based Fluent Bit plugins. Explore working with SQL-like expressions over signals and deciding when and how to build custom plugins by downloading the book in its entirety [here](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS).*  
[Go](https://go.dev) is the most dominant language for [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) [projects](https://gloutnikov.com/post/cncf-language-stats/), bringing the benefits of native binary performance while retaining features of languages such as Java in the form of memory management, abstractions and ease of development. It helps that the originators of Kubernetes (Google) are the driving force behind the [development of Go](https://thenewstack.io/introduction-to-go-programming-language/).

The emphasis on native binary performance benefits for cloud solutions, particularly at hyperscale, makes easy direct integration between C/C++ and Go important, as the Linux kernel is written with C/C++, and it is second after Go in terms of native binary languages used by CNCF projects.

The [Go plugins interact with the Fluent Bit](https://docs.chronosphere.io/pipeline-data/plugins/source-plugins/fluent-bit?&utm_source=sponsored-content&utm_id=TNS) framework through the [Goproxy module](https://github.com/fluent/fluent-bit/tree/master/src/proxy/go) in Fluent Bit. At this writing, the Goproxy and the associated Go binding code expose only input and output plugins, not the filter method interfaces.

## Organizational and Technical Benefits of Building in Go

Using Go and configuring the addition of Go plugins into Fluent Bit provides a range of organizational and technical benefits:

* The open source project does not dictate release cycles and development processes.
* Because the result is delivered as a native binary, the plugin can be offered without exposing proprietary code or intellectual property.
* Specialist use cases are ideal for niche use cases that reflect specific organizational needs or niche requirements. These kinds of use cases often have a level of intellectual property rights (even if it is indirect when it comes to support functionality).

For example, in the case of a plugin that handles errors from a video transcoder, the number of organizations using video transcoders is relatively small, and the number using a specific transcoder with a custom means to generate [logs and events](https://docs.chronosphere.io/ingest/logs/pipeline-logs?utm_source=c&utm_id=TNS) is even smaller.

* Plugins can be implemented to meet specific internal needs without giving due consideration to the community. If our organization has a specific standard for naming conventions, we can hardwire it into the plugin without concern about whether it meets wider community needs.

The technical benefits of using Go to build the plugin are:

* Go retains the performance of native binary executables without losing the benefits of memory management being performed by a language runtime.
* The [Go language](https://chronosphere.io/learn/best-languages-for-microservices/?&utm_source=sponsored-content&utm_id=TNS) provides [binding to C applications](https://pkg.go.dev/cmd/cgo) as standard, and Fluent Bit includes a library that further [helps with interfacing](https://github.com/fluent/fluent-bit-go).
* Development approaches, particularly for closed source or private solution implementation, can be aligned to internal principles and practices without considering the wider community.

## Operational Drawbacks of Go-Based Fluent Bit Plugins

The drawbacks are more operational than specific to code development itself. These challenges include the following:

* At this writing, the filter interfaces are not available.
* If the development team(s) don’t work with Go, overhead remains in implementing and maintaining processes such as continuous integration. We need to include regression testing for major and minor revisions.
* If we intend to make the plugin open source, it is not as likely to get the same level of attention as the core Fluent Bit repositories. As a result, more of the maintenance burden will be on the plugin provider.
* Users have additional deployment effort when deploying our plugin in their existing environments, which could be problematic if customers use [prepackaged platforms like OpenShift](https://www.imaginarycloud.com/blog/openshift-vs-kubernetes-differences#:~:text=Developed%20by%20Red%20Hat%2C%20OpenShift%20is%20written,be%20extended%20to%20support%20other%20programming%20languages.).
* The scope of paid support services can be ambiguous, as third-party support offerings typically don’t cover third-party plugins.
* The plugin needs to be subject to ongoing periodic updates, even if the solution is stable and mature, to prevent the possible perception that the plugin is stale.
* Additional development effort is needed to translate between C- and Go-native data types. We will have to use other Go language libraries and frameworks.
* We may have to rebuild Fluent Bit with Go support enabled (`cmake -DFLB_ DEBUG=On -DFLB_PROXY_GO=On`) depending on the build of Fluent Bit we use. Note that the images provided by the Fluent Bit project have this build flag enabled by default. NOTE: Resources for Go-based development are available at <https://github.com/fluent/fluent-bit-go>, including example implementations and a Go utility library to ease the workaround for the Go-C interface.

If you’d like to go deeper into how Fluent Bit processors can [reshape metrics, traces and logs](https://docs.chronosphere.io/ingest/metrics-traces/collector/install/kubernetes?utm_source=c&utm_id=TNS), including SQL-like expressions over signals, when to reach for a custom plugin and how to choose between the different implementation technologies, download the full book “[Fluent Bit with Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/?utm_source=sponsored-content&utm_id=TNS).” In the rest of this chapter, you’ll get a practical, end-to-end understanding of the plug-in landscape so you can confidently design, build and operate custom extensions in your own environments.

To learn more about Fluent Bit, read:

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/c3489f3d-cropped-ba30d14d-phil-wilkins.jpeg)

Writing for Chronosphere, Phil Wilkins has spent more than 30 years in the software industry, with broad experience in businesses and environments from multinationals to software startups and consumer organizations to consultancy. He started as a developer on real-time, mission-critical...

Read more from Phil Wilkins](https://thenewstack.io/author/phil-wilkins/)