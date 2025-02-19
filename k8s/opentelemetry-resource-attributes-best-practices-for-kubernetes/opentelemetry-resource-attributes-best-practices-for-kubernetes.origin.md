[ Resources in OpenTelemetry](https://www.dash0.com/faq/what-are-opentelemetry-resources) are used to document which systems the telemetry is describing, and they are often the difference between telemetry from which you can gain insights from, and “just data”.
When instrumenting services with OpenTelemetry, adhering to semantic conventions ensures consistent, accurate, and meaningful telemetry data across systems.

A variety of attributes allow you to describe which workload on your Kubernetes cluster is emitting which telemetry. The [Kubernetes resource semantic conventions](https://opentelemetry.io/docs/specs/semconv/resource/k8s/) specify, among others, pairs of `k8s.*.uid`
and `k8s.*.name`
attributes for pods (`k8s.pod.uid`
and `k8s.pod.name`
), as well for all workloads “higher level” constructs (which in Kubernetes are also called “resources”, but we don’t want to confuse the two terms), like deployment (`k8s.deployment.uid`
and `k8s.deployment.name`
), daemonset (`k8s.daemonset.uid`
and `k8s.daemonset.name`
) and so on.

Nevertheless, despite the well-defined attributes, it is not entirely straightforward to have all the right Kubernetes-related metadata attached to your telemetry.

[It all starts with k8s.pod.uid](#it-all-starts-with-k8s.pod.uid)
Among all the resource attributes that describe telemetry coming from your workloads on Kubernetes, `k8s.pod.uid`
is by far the most important: through it, you can add most other pieces of k8s-related metadata by funneling your telemetry through the [ k8sattributeprocessor component](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/k8sattributesprocessor/README.md) of an OpenTelemetry collector running inside the same cluster. The

`k8sattributeprocessor`
“fills” the blanks using data it gets from Kubernetes API, and with the right tool, you can effortlessly filter and group your telemetry across all types of aggregations.The fact that the `k8sattributeprocessor`
exists actually fills a very important gap in telemetry metadata: the OpenTelemetry SDKs running within your containers have access to virtually no metadata about *why *the pod surrounding them is running. They are not going to know, unless you specifically add it to the pod, e.g., using environment variables, which daemonset scheduled the pod, or which replicaset of which deployment.

As a matter of fact, without additional assistance by you, for example via environment variables (either setting values yourself, or adding pod uid, pod name, and namespace name to the environment via Kubernetes’ [Downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/)), an OpenTelemetry SDK within a container can pretty much know only the pod uid (though very esoteric magic involving the parsing of [cgroup](https://en.wikipedia.org/wiki/Cgroups) metadata, see e.g. this [resource detector](https://github.com/dash0hq/opentelemetry-js-distribution/blob/main/src/detectors/node/opentelemetry-resource-detector-kubernetes-pod/index.ts) in the Dash0 distribution of OpenTelemetry for Node.js) and the pod name (via the networking hostname). And unfortunately, as of writing, OpenTelemetry SDKs do not even implement those consistently (see, e.g., [this issue](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/1474)).

So, make sure the `k8s.pod.uid`
is set correctly and reliably in your Kubernetes manifests via the Downward API and “[dependent environment variables](https://kubernetes.io/docs/tasks/inject-data-application/define-interdependent-environment-variables/)”:

pod spec yaml snippet012345678env:...- name: K8S_POD_UIDvalueFrom:fieldRef:apiVersion: v1fieldPath: metadata.uid- name: OTEL_RESOURCE_ATTRIBUTESvalue: k8s.pod.uid=$(K8S_POD_UID), ...
*A Kubernetes pod spec template snippet showing how to use the Downward API together with the OTEL_RESOURCE_ATTRIBUTES environment variable to set the k8s.pod.uid resource attribute.*
By the way, the `k8sattributeprocessor`
is capable of identifying which pod is sending telemetry to it via the unique pod ip (see the [“associations” configurations](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/k8sattributesprocessor/README.md#configuration)): the processor in the OpenTelemetry Collector matches the IP address of the “other side” of the TCP connection that sends the telemetry, and since each pod in a Kubernetes cluster has a unique IP address assigned to it, it can figure out from which pod it’s coming from. *Mostly…*

And here, there is a caveat: the detection of the pod based on the IP address is known not to work reliably if you use a service mesh or some of the less conventional network setups. (Don’t ask us how we know. It was not fun to troubleshoot that.) So, better safe than sorry: ensure your telemetry is annotated with `k8s.pod.uid`
and, if you are OK with proxying your telemetry through an OpenTelemetry Collector inside the cluster, have that fill most of the resource attributes mentioned in the remainder of this article for you using a [configuration like this](https://www.otelbin.io/s/249772c6c88ab31e77c168af6131df0248902bbf).

[Pleased to meet you, hope you guess the pod’s name](#pleased-to-meet-you-hope-you-guess-the-pod's-name)
Pod UIDs are effectively unique across all your workloads. (And all Kubernetes workloads anywhere, ever.) But long, random strings of characters are not something we humans are good at remembering things by, or even searching for in lists.

So, in a similar way same way we set the `k8s.pod.uid`
resource attribute, we can set the `k8s.pod.name`
:

pod spec yaml snippet012345678env:...- name: K8S_POD_NAMEvalueFrom:fieldRef:apiVersion: v1fieldPath: metadata.name- name: OTEL_RESOURCE_ATTRIBUTESvalue: k8s.pod.name=$(K8S_POD_NAME), ...
*A Kubernetes pod spec template snippet showing how to use the Downward API together with the OTEL_RESOURCE_ATTRIBUTES environment variable to set the k8s.pod.name resource attribute.*
[Intermezzo: Why are they called Pods anyhow?](#intermezzo:-why-are-they-called-pods-anyhow)
Did you know that the Kubernetes pod, i.e., one or more containers that share local networking and other resources like CPU and memory allotment and volumes, is called like that because:

- “pod” is the collective name of a group of whales
- the logo of Docker, the original container runtime of Kubernetes, is a whale
Now you know!

[If you have sidecars, you probably want k8s.container.name](#if-you-have-sidecars-you-probably-want-k8s.container.name)
If your pod has more than one container, you are really going to need to know which of them is having issues. Usually, applications on Kubernetes have just one “main” container, running your application and may have one or more “sidecars”, i.e., containers that have inside ancillary processes like log collectors or service mesh proxies. The `k8sattributeprocessor`
(see previous section) cannot tell containers apart (all your containers in the same pod share the same IP address and pod uid, among other things), so you should set the `k8s.container.name`
yourself. It can be a bit toilsome, because you cannot do it generically using the Downward API the way we did for `k8s.pod.uid`
, but in the end is as simple as adding another entry to `OTEL_RESOURCE_ATTRIBUTES`
:

0123env:...- name: OTEL_RESOURCE_ATTRIBUTESvalue: k8s.container.name=<my_container_name>, ...
*A Kubernetes pod spec template snippet showing how to use the OTEL_RESOURCE_ATTRIBUTES environment variable to set the k8s.container.name resource attribute. Be sure to set it to the same value of the container name!*
Note that `k8s.container.name`
could be redundant: the `container.name`
attribute is supposed to contain the same data, and there are detectors in most OpenTelemetry SDKs (see e.g. for [Node.js](http://node.js/)), that can collect `container.name`
for you by parsing, for example, the `cgroup`
metadata ([cgroups](https://en.wikipedia.org/wiki/Cgroups) are one of the foundational Linux facilities for containers). However, it may not always be possible to add detectors to your containerized applications, especially when you are using sidecars from 3rd parties. But if they support the `OTEL_RESOURCE_ATTRIBUTES`
environment variable, you can fill the gaps in resource attributes through the process environment.

[Names are not enough, you need UIDs](#names-are-not-enough-you-need-uids)
The same way you are likely to have a `frontend`
service in most applications (`service.name=frontend`
) service, that service will likely be powered by a `frontend`
deployment (`k8s.deployment.name=frontend`
). Names in Kubernetes are unique only for resources of the same type (e.g., deployments) within the same Kubernetes namespace. If you want to avoid confusion and simplify your life aggregating data, set not only `k8s.*.name`
but also `k8s.*.uid`
, and use the UIDs to group.

After reading the previous paragraph, you might have wondered:

“The deployment name is unique inside the namespace, and the namespace name is unique inside the cluster. So why do I need unique identifiers anyhow?”

That logic works if you deploy your software in only one cluster. But that is seldom the case. Between development, testing, and various production clusters (which is a rather common type of layout), most organizations run the same software, at the same time, on *a lot* of Kubernetes clusters. And, to make matters more complicated, telling Kubernetes clusters apart is harder than it should (see next section).

[Which cluster is this?](#which-cluster-is-this)
The fun with identifiers is not over yet. Now let’s talk about some identifiers that *do not actually exist*. Specifically, the identifier of a specific Kubernetes cluster. In most Kubernetes setups, it literally does not exist. In other words, a* Kubernetes cluster has no own notion of identity*!

You surely have names for your clusters, but the name “prod-eu-awesomesauce” that you define in your Kubernetes cluster management tool is more a matter of how you call the profile in `kubectl`
to connect to that cluster rather than some metadata you can find from within the cluster itself! (Your mileage may vary with specific setups and Kubernetes flavor; but in general, this is the case.) So, you should use the OpenTelemetry collector’s [ resourceprocessor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/resourceprocessor) to inject the value of

`k8s.cluster.name`
like this:012345processors:resource:attributes:- key: k8s.cluster.namevalue: "prod-eu-awesomesauce"action: upsert
*A snippet of the OpenTelemetry collector configuration to add the k8s.cluster.name resource attribute to all telemetry coming through.*
Moreover, the same way most Kubernetes `k8s.*.name`
attributes have matching `k8s.*.uid`
ones, so does `k8s.cluster.name`
have a match in `k8s.cluster.uid`
. The common practice in this case is to set `k8s.cluster.uid`
using as value the uid of the `kube-system`
namespace, which is pretty much the only namespace you are guaranteed to find in every Kubernetes cluster you will ever see (as it is the one that by default hosts the control plane components).

[Don’t forget the nodes!](#don't-forget-the-nodes!)
The `k8s.node.name`
attribute, and its far lesser used `k8s.node.uid`
sibling, are really useful when investigating performance issues due to resource underprovisioning (pods on the same node fighting for resources like CPU or memory) or [node-pressure evictions](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/). The only notable exception to this is when you run on AWS EKS on Fargate, where each pod, from the point of view of Kubernetes, runs on a dedicated node.

If you have already set up the `k8sattributeprocessor`
so that it can add resource attributes to your telemetry, it can also take care of `k8s.node.name`
for you. Otherwise, setting the `k8s.node.name`
attribute is pretty simple using Kubernetes’ Downward API and “[dependent environment variables](https://kubernetes.io/docs/tasks/inject-data-application/define-interdependent-environment-variables/)”:

012345678env:...- name: K8S_NODE_NAMEvalueFrom:fieldRef:apiVersion: v1fieldPath: spec.nodeName- name: OTEL_RESOURCE_ATTRIBUTESvalue: k8s.node.name=$(K8S_NODE_NAME),...
*A Kubernetes pod spec template snippet showing how to use the Downward API together with the OTEL_RESOURCE_ATTRIBUTES environment variable to set the k8s.node.name resource attribute.*
[Conclusions ](#conclusions)
Resource attributes are a key ingredient to make your telemetry useful. In this blog post, we have looked at the OpenTelemetry resource semantic conventions for Kubernetes, and how you can ensure to always know which workload of which cluster is sending the errors.

In this post, we kept to the fundamental Kubernetes metadata your telemetry should have. There is, of course, a lot more to be said about OpenTelemetry semantic conventions, even just for resources on Kubernetes. For example, you will find more resource attributes specified in the [Kubernetes resource semantic conventions](https://opentelemetry.io/docs/specs/semconv/resource/k8s/). Also, there are semantic conventions for [metrics about Kubernetes](https://opentelemetry.io/docs/specs/semconv/system/k8s-metrics/), which are, at the time of writing, in an experimental state (meaning: the convention is not declared stable, so it might still change in backwards-incompatible ways) and are based on what the OpenTelemetry Collector knows how to collect with various receivers like [ k8sclusterreceiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/k8sclusterreceiver) and

[.](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kubeletstatsreceiver)
`kubeletstatsreceiver`
By the way, if you liked this article, you are probably going to love Ben's "[Top 10 OpenTelemetry Collector Components](https://www.dash0.com/blog/top-10-opentelemetry-collector-components)" blog post. It will likely give you a bunch more ideas about what you can do to ensure that your resource metadata is top-notch.

And if you want all the awesomeness of the resource metadata we covered in this post, but do none of the work to get them, give the [Dash0 operator](https://www.dash0.com/documentation/dash0/dash0-kubernetes-operator) a spin: it is open source, built on OpenTelemetry components with opinionation and an appliance-like philosophy (“it just works™”), and under the hood it uses most of the techniques described in this post to get your telemetry annotated to the state of the art, with literally none of the toil from on your side.