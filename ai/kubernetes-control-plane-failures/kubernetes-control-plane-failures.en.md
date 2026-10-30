Kubernetes control planes are designed to contain individual failures, but their availability still depends on how components in the critical path behave under pressure. At fleet scale, a component does not have to crash to contribute to an outage. A valid mechanism can amplify a local defect through shared metadata, synchronized startup work, or an overly aggressive health check.

For example, an informer gives a controller a local view of cluster state, letting its workers make progress without repeatedly querying the API server. This is efficient when controllers start independently. When many controllers restart simultaneously across a fleet, rebuilding those views can place significant pressure on the control plane. The informer mechanism itself becomes the amplifier.

> “At fleet scale, a component does not have to crash to contribute to an outage. A valid mechanism can amplify a local defect through shared metadata, synchronized startup work, or an overly aggressive health check.”

This article examines three cases. In the first, an extension API server published an invalid schema after [a dependency upgrade](https://thenewstack.io/eks-kubernetes-upgrade-rollback/) and blocked clients that had never used its API. In the second, DaemonSet agents restarted across a large fleet, turning routine startup work into a request storm the API server couldn’t absorb. In the third, a deep liveness check on a component in the API request path treated a dependency outage as a process failure and drove repeated restarts while the dependency remained unavailable.

These cases matter for teams running extension APIs, controllers that watch large object collections, and components in the API request path that rely on deep dependency checks.

In one of the cluster, Helm deployments started failing for charts that contained only standard Kubernetes resources. The charts had no relationship to the extension API that caused the failure. Users who had never heard of the extension saw validation errors before their requests reached the API server. The failure path ran through metadata, through a schema document that combined definitions from APIs registered in the cluster.

Understanding why requires knowing how Kubernetes exposes API metadata to clients.

Kubernetes can be extended through aggregated API servers, which add new APIs without modifying the core API server. To users, an aggregated API looks native: it has a group, version, kind, and resource paths, and kubectl accesses it through the cluster’s normal API endpoint. An extension API server generates an OpenAPI schema describing its objects and fields. Clients retrieve this schema to understand and validate resources before sending requests.

![Diagram of extension API server validation flow](https://cdn.thenewstack.io/media/2026/10/44feb4bb-image1.png)

## OpenAPI v2 and v3

Kubernetes exposes this schema contract in two forms, and the difference determines the blast radius of a broken extension. OpenAPI v2 is a single combined document available at /openapi/v2, containing definitions from the core API server and aggregated extension APIs. OpenAPI v3 separates schemas by API group and version. That separation narrows the impact because clients using a core API don’t need to retrieve every extension’s document.

> “The v2 format creates a shared failure domain: an invalid definition from one extension can prevent clients from parsing the document used to validate unrelated resources.”

The v2 format creates a shared failure domain: an invalid definition from one extension can prevent clients from parsing the document used to validate unrelated resources.

## Explicit OpenAPI model names

Kubernetes PR #[131755](https://github.com/kubernetes/kubernetes/pull/131755) made OpenAPI model names explicit. Before this change, Kubernetes could derive a model name from a Go package path. That made it easy to start with a valid schema, but it also tied published model names to implementation details. Moving code or reorganizing packages could change a name that OpenAPI clients saw. The newer approach lets API authors declare a stable model package, and code generation uses that declared value when building schema definitions and references.

Before the change, a schema could expose a definition derived from the raw Go package path:

```

{
   "com.example.platform.pkg.apis.metrics.v1.MetricReportSpec": {
     "type": "object"
   }
 }
After the change, once the package declares an OpenAPI model namespace, the same definition uses an explicit, stable name:
{
   "com.example.platform.metrics.v1.MetricReportSpec": {
     "type": "object"
   }
 }

```

## A missing declaration

One extension API server upgraded the Kubernetes API machinery dependency without including the +k8s:openapi-model-package annotation required by the updated model name generation. Its generated code continued to supply raw Go package paths when building schema definitions. Earlier API machinery transformed those paths into OpenAPI-safe names; the newer behavior expects the extension to provide a declared model package. Without that declaration, the extension began publishing raw package paths as OpenAPI model identifiers. Because those paths contain /, they made the resulting schema invalid.

The extension server started successfully and continued serving its API. Process health checks do not validate the OpenAPI document a process publishes. The problem appeared in clients that read OpenAPI v2. Because v2 combines API schemas into one document, an invalid definition from one extension can cause a client to report an error before it sends the requested API call, even when the requested resource belongs to a different API.

Helm’s behavior made this especially visible. Depending on the Helm version, command, and validation settings, Helm retrieves the OpenAPI v2 document before applying a chart. A chart using only ordinary Kubernetes resources can fail because an unrelated aggregated API publishes an invalid schema. Clients using v3 for core resources follow a narrower path: they retrieve the relevant core API document rather than the extension schema that contains the problem.

## Test the schema you publish

The most revealing test validates the artifact that clients actually receive. After an upgrade, start the extension and fetch both schema formats:

```

kubectl get --raw /openapi/v2 > openapi-v2.json
 kubectl get --raw /openapi/v3/apis/&lt;group>/&lt;version> > openapi-v3.json

```

Parse and validate those documents before enabling the extension in production. Also test with clients that validate requests against the OpenAPI v2 schema. These tests follow the user path and reveal problems that endpoint health checks cannot detect.

## 2. When a rolling restart becomes a request storm

### The cost of rebuilding a local view

A DaemonSet runs one copy of a Pod on every node in a cluster. It suits monitoring, network policy, logging, and security agents that need an up-to-date view of cluster Pods. For example, a network agent may need to map an IP address to its owning Pod for policy or telemetry.

The standard way to maintain that view is through an informer: a client mechanism that lists the required objects and then watches for changes to keep a local cache current.

On a cluster with a few thousand nodes, a cluster-wide Pod informer means a few thousand potential initial list operations. When agents start at different times, the load spreads across the API server’s capacity without incident.

### When recovery synchronizes the work

The cost changes when recovery synchronizes the work. In one incident, a DaemonSet ran across thousands of nodes, and its agents repeatedly crashed across much of the fleet. An operator initiated a rolling restart to recover them. The DaemonSet’s maxUnavailable setting seemed protective because it limits how many Pods an update may make unavailable at once.

Those Pods were already unavailable. Their replacements did not necessarily face the same pacing constraints. Many agents started nearly simultaneously.

Each new agent creates its informer. Each informer begins by listing the same collection of Pods. A recovery operation intended to reduce the failure footprint can therefore create a large, synchronized population of requests against the API server.

### The cost of a list request

Informers commonly make their initial request with the resourceVersion parameter set to 0. By using 0, the client allows the API server to answer from its watch cache in memory rather than performing a direct read from [etcd, the API server’s](https://thenewstack.io/eks-kubernetes-etcd-scale/) backend datastore. This is normally the fast path. It avoids repeated storage reads and uses a view of the state the API server has already assembled for watches.

For years, that path had an unintuitive limitation. The watch cache could not provide pagination in the same way that lists served from etcd could. A client could include limit=500 and reasonably believe it had bounded the response to 500 objects. In affected request paths, when the list was served from the watch cache with resourceVersion=0, the API server could ignore the limit and return every matching object.

On a large cluster, a response containing all Pods may include tens of thousands of objects and occupy hundreds of megabytes while the API server decodes, filters, serializes, and sends it. When thousands of replacement agents request the same full collection together, the server can exhaust available memory and CPU constructing many copies of the same answer. Ordinary control plane traffic then waits.

### Reducing the startup load

The Kubernetes community has improved this part of the stack. API Priority and Fairness list-cost estimation was corrected in Kubernetes 1.31. WatchList can also replace the traditional list-then-watch startup path in clients that support it. These improvements reduce the per-request cost, but they do not change the broader design calculation: a cluster-wide informer in a DaemonSet still multiplies its startup cost by the number of nodes, and a retry policy can still synchronize that cost during a failure.

The question for an agent owner is: what is the smallest Kubernetes resource collection this informer can watch and still fulfill its function?

An agent that only needs Pods in one namespace should not list all Pods cluster-wide. An agent that needs Pod metadata should consider a metadata-only informer rather than transferring full Pod specifications. An agent interested in service backends may be able to use EndpointSlices instead of listing every Pod because EndpointSlices describe service endpoints directly and are typically much smaller than the full Pod inventory.

An agent that truly needs Pod-to-IP ownership, labels, or other Pod metadata may still need to watch Pods, but it should restrict that watch to the relevant namespaces, nodes, or labels whenever its semantics allow. The goal is not to eliminate Pod informers. It is to avoid reconstructing more cluster state than the agent can use, especially when recovery causes many instances to start together.

## 3. When a liveness check restarts what it cannot fix

[A liveness probe](https://thenewstack.io/top-10-kubernetes-deployment-errors-causes-and-fixes-and-tips/) that checks downstream dependencies will restart a process whenever those dependencies are unavailable. If the process sits in the API request path, each restart can interrupt API traffic. When the dependency outage persists, the probe drives a cycle of restart, initialize, fail dependency check, and restart again. Each iteration adds latency without repairing the dependency.

> “The probe may faithfully execute its contract. The contract may still be wrong.”

The probe may faithfully execute its contract. The contract may still be wrong.

## Static stability depends on cached key material

Kubernetes control planes may depend on an external Key Management Service, or KMS, to encrypt Secrets. The KMS provider uses that service for key operations, while the API server can retain cached encryption material in memory. That cached state is part of the system’s availability design. A transient loss of KMS connectivity may delay operations that require fresh key material without immediately making the API server unable to serve useful requests.

## A Liveness probe that tested the wrong thing

In one incident, an encryption provider that integrated Kubernetes with an external KMS had a liveness probe monitored by the kubelet. The probe performed a fresh encryption operation, followed by a decryption operation, against the external KMS every few seconds. When a network impairment made the KMS endpoint unreachable, the probe failed, and the kubelet restarted the provider. The restarted provider couldn’t establish a new KMS session, so it kept restarting while the dependency remained unavailable.

The probe accurately reported that the KMS endpoint was unreachable. It could not determine whether the provider process could no longer serve its local interface, or whether the API server had exhausted the cached encryption material that let it keep working. Neither conclusion followed from a failed call to the external KMS.

## The cascade through API server health

The risk was broader because the API server’s composite /healthz check included the KMS provider’s status. A failed provider could therefore replace an API server with usable cached encryption state. The new API server had no warm encryption cache, needed to establish a new KMS session, and faced the same unreachable dependency. Repeated replacements could turn a transient KMS impairment into a loss of control plane serving capacity.

## Preserve capability during an impairment

This is the difference between testing dependencies and testing capabilities. KMS reachability was a useful monitoring signal, but it was not sufficient evidence that either the provider process or the API server had lost all useful capability. The liveness probe should determine whether the provider is stuck or unable to serve its local interface. A separate dependency check can alert operators that KMS is unavailable without automatically triggering a restart.

The same reasoning applies to any component in the control plane path. A cached credential, an established connection, or an in-memory view of state may be the only thing allowing useful work to continue while an upstream service recovers. This behavior is already built into components such as kube-proxy and CoreDNS: kube-proxy continues using its last-known Service and Endpoint state, while CoreDNS continues answering from the Kubernetes data it already has, even when the API server is temporarily unavailable.

> “Each case shares a structural property: a mechanism can operate correctly within its own contract yet still violate the availability contract of the system it belongs to. Component-level correctness is necessary but insufficient.”

Restarting every process that cannot reach every dependency discards cached state, increases the amount of state that must be rebuilt, and creates synchronized demand on an already impaired dependency.

Each case shares a structural property: a mechanism can operate correctly within its own contract yet still violate the availability contract of the system it belongs to. Component-level correctness is necessary but insufficient for system availability.

The general design principle is to evaluate every mechanism on the critical path for its behavior when its assumptions are violated. Schema aggregation assumes extensions publish valid schemas. Rolling restart pacing assumes Pods are available to become unavailable. Liveness probes assume restart moves a process closer to health. When those assumptions break, the mechanism can amplify the failure it was designed to contain.

For platform teams operating shared control plane components at scale, these are practical review criteria for upgrades, recovery exercises, and health-check design:

* Validate the schema artifacts that clients receive, not only the extension process.
* Limit informer scope and startup work to the smallest resource collection the component requires.
* Separate dependency monitoring from liveness decisions when a component can retain useful capability during an impairment.
* Test recovery behavior when many replicas restart simultaneously.

These practices help keep a local failure local, preserve useful capability during dependency outages, and prevent ordinary recovery work from becoming a control plane incident.

***For additional resilience guidance, see the Amazon*** [***EKS Best Practices Guide***](https://docs.aws.amazon.com/eks/latest/best-practices/reliability.html)***.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/7f8a61d7-srisaranbalaji-600x600.png)

Sri Saran Balaji Vellore Rajakumar is a Principal Engineer at Amazon Web Services and a founding engineer of Amazon EKS, where he has spent nearly a decade building the infrastructure that keeps the EKS control plane available and performant at...

Read more from Sri Saran Balaji Vellore Rajakumar](https://thenewstack.io/author/sri-saran-balaji-vellore-rajakumar/)