***Editor’s note:** This article is an excerpt from Chapter 4 of the Manning Book, “[Fluent Bit with Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/),” a guide on logs, metrics and traces for enabling more efficient telemetry. This chapter focuses on how to capture events across Kubernetes applications using logs to measure activity, behavior and context. Download the book in its entirety [here](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/).*

Kubernetes looks at logs and [logging](https://thenewstack.io/using-logging-frameworks-for-application-development/) from multiple perspectives: logging, measuring and tracking what a container does, what the [wider Kubernetes cluster does](https://thenewstack.io/observability-is-a-multicluster-app-developers-best-friend/) (although the container and cluster can be considered the same) and what the application within the container does. As a result, we need to think about how to capture these forms of [events](https://thenewstack.io/understanding-log-events-why-context-is-key/).

## Understanding Kubernetes’ Position on Logging

As far as Kubernetes is concerned, logging from applications run by containers is the responsibility of the container runtime. The norm is for the container to handle standard out and standard error.

In addition to using [stdout and stderr](https://chronosphere.io/learn/dynamic-log-routing-on-kubernetes-labels-fluent-bit/), most container runtimes have adopted the idea of a logging driver, which allows for different ways to handle captured application logs. Other than typically implementing the stdout and stderr using the logging-driver model, implementations have little consistency.

Just handling what the container is doing doesn’t address logging at a cluster level, such as recording what is happening across the cluster, eviction of pods and the starting and stopping of nodes.

Again, Kubernetes does not prescribe a specific solution but promotes the idea of using logging agents in a sidecar configuration or having a logging agent operate on every node (as part of a DaemonSet).

Kubernetes has its own logging library, known as [klog](https://github.com/kubernetes/klog), and more recently has moved toward adopting [logr](https://github.com/go-logr/logr). Logr has a stronger decoupling between the logging interface and log-content output, so logr can be used to create klog and other outputs.

## Kubernetes Auditing

In addition to understanding what is happening with the applications within a Kubernetes ecosystem, we should be auditing Kubernetes.

We may want to find out, for example, who or what instructed Kubernetes to evict a container. Kubernetes addresses this situation with auditing capability, which we can configure to talk to a logging backend by using a webhook or writing the events in a log file in [JSON Lines format](https://jsonlines.org).

We shouldn’t confuse this auditing with the event capability that [Fluent Bit](https://thenewstack.io/what-are-the-differences-between-otel-fluent-bit-and-fluentd/) supports as a plugin source, as we’ll see. With the correct audit configuration, we can collect such data by using Fluent Bit. (For more information on configuring Kubernetes auditing, see <https://mng.bz/znZA>.)

## Kubernetes Events Input

Kubernetes exposes its activities and events to anyone requesting them via its API server. Through the Kubernetes events plugin (called kubernetes\_events), we can grab those events and put them in the log events pipeline. You’ll recognize many attributes that have the same or similar names and purposes as the `tail` plugin and a network-based plugin.

The plugin uses a SQLite database, as we can with `tail` (identified by the db attribute), so that events aren’t accidentally duplicated into the pipeline; we are given the same events each time we call the API server.

Because the process is based on polling, we have attributes to define the number of seconds or nanoseconds (`interval_sec` or `interval_nsec` attribute).

We need to be mindful that we can have only one active Fluent Bit instance running this plugin because of the constraints on the way SQLite works. This restriction isn’t catastrophic; we can lean on Kubernetes to monitor the health of the container.

A large cluster, however, will have a lot of events, so a single Fluent Bit instance needs [sufficient resources to keep up with Kubernetes](https://chronosphere.io/learn/kubernetes-cloud-native-app-challenges/). If more than one Fluent Bit instance starts retrieving the event data, we’ll see a duplication of events.

When it comes to connecting with the Kubernetes API to collect event data, this plugin has a common set of attributes with the Kubernetes filter plugin for defining the URL for the server, certificate location, TLS checking, token and token time to live (TTL) (`Kube_URL`, `Kube_CA_File`, `Kube_CA_Path`, `tls.debug`, `tls.verify`, `Kube_ Token_File`, `Kube_Token_TTL`).

See the following listing:

[![](https://cdn.thenewstack.io/media/2025/12/d40db03d-image2.png)](https://cdn.thenewstack.io/media/2025/12/d40db03d-image2.png)

[![](https://cdn.thenewstack.io/media/2025/12/eeec38da-image1.png)](https://cdn.thenewstack.io/media/2025/12/eeec38da-image1.png)

This plugin’s configuration raises challenges, specifically: safely exposing the Kubernetes token and the certificates to Fluent Bit. Assuming that this Fluent Bit deployment occurs within a [Kubernetes pod,](https://chronosphere.io/learn/what-is-a-kubernetes-pod/) a good way to overcome this challenge is to store the files as Kubernetes secrets and then, in the pod specs, define a mount point that maps to the secrets.

Data is kept securely, but we can map the value to whichever containers need the value. Within the pod, the file is seen as normal. It’s best not to provide the credentials via environment variables, as they’re fixed for the lifetime of the container. As a result, the configuration will fail if the credentials are rotated.

We should be [careful how we interpret the Kubernetes event data](https://chronosphere.io/learn/logging-best-practices/). As the documentation says, “[Events](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/event-v1/) should be treated as informative, best-effort, supplemental data.”

|  |
| --- |
| **Note:** With the Kubernetes filter, Kubernetes\_events plugins or any other way of interacting directly with Kubernetes APIs, role-based access control (RBAC) must be configured so that the service accounts used to run these containers have the necessary privileges to request data from the API server. |

We can find an illustration of the configuration at <https://mng.bz/KDGO>. Books such as “Core Kubernetes,” by Jay Vyas and Chris Love, are good guides to how RBAC works.

*You’ve just read an excerpt of the Manning book, “Fluent Bit with Kubernetes.” To learn even more about Fluent Bit and Kubernetes, including the different parts of a Kubernetes ecosystem, [download the full book](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/).*

## Frequently Asked Questions

**What is the purpose of auditing in Kubernetes?** Auditing in Kubernetes enables administrators to track what actions occurred in the cluster, when they happened and who initiated them, helping to ensure security and compliance by configuring logging backends or JSON Lines files for recorded events.

**How do you configure Kubernetes to capture audit logs?**

Kubernetes audit logging is set up by configuring audit policies on the API server and specifying where audit events should be sent, typically a webhook or a log file; the configuration must provide secure credential management, ideally using Kubernetes secrets mounted in [pods](https://chronosphere.io/learn/kubernetes-pod-vs-container/), rather than environment variables.

**What are the key fields found in a Kubernetes audit log entry?**

A Kubernetes audit log entry includes fields like timestamp, auditID, request stage, user information, verb (action taken), affected resource, namespace, source IP and the request Uniform Resource Identifier (URI). These details help administrators trace activity and diagnose security incidents within the cluster.

**How should organizations secure and interpret Kubernetes audit data?**

Credentials used for audit log collection, such as tokens and certificates, should be stored securely as secrets and mounted via pod specs, not set as environment variables, to maintain security during credential rotation. Audit events should be treated as informative, supplemental data rather than relied upon for billing or primary compliance analytics.

Read more about Fluent Bit:

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/c3489f3d-cropped-ba30d14d-phil-wilkins.jpeg)

Writing for Chronosphere, Phil Wilkins has spent more than 30 years in the software industry, with broad experience in businesses and environments from multinationals to software startups and consumer organizations to consultancy. He started as a developer on real-time, mission-critical...

Read more from Phil Wilkins](https://thenewstack.io/author/phil-wilkins/)