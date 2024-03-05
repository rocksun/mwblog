[The hater’s guide to Kubernetes](https://paulbutler.org/2024/the-haters-guide-to-kubernetes/)
Among a certain tech set, Kubernetes has earned a reputation as an unnecessarily complicated time-sink that startups should avoid. Using Kubernetes with a small team is seen as a sign of over-engineering.
I’m guilty of taking
[pithy jabs](https://twitter.com/paulgb/status/1568257167882436608) myself.
I might gripe about Kubernetes sometimes, but it really is a great piece of technology. I highly recommend it to all my competitors.— Paul Butler (@paulgb)
[September 9, 2022]
Despite my snark, “great piece of technology” truly is sincere; at the time of that post I had
[recently written](https://driftingin.space/posts/complexity-kubernetes) about how much of Kubernetes’ complexity is necessary for what it does.
We’ve been running Kubernetes in production for a few years now at
[Jamsocket](https://jamsocket.com/), and I’ve found a good flow with it. Kubernetes serenity has been achieved internally. A big key to this has been [carving out a small chunk](https://twitter.com/paulgb/status/1743361919535260053) of Kubernetes’ features and pretending the rest don’t exist.
This post started as an internal guide to the way we use Kubernetes, so it’s not meant to apply prescriptively to every startup; nonetheless I think it’s a good starting place for avoiding many of the sandbars in the vast seas of Kubernetes.
**Why use Kubernetes at all?**
As I see it, Kubernetes is the best-travelled path if you want all three of these things:
- To run multiple processes/servers/scheduled jobs.
- To run them redundantly and load balance across them.
- To configure them, and the relationships between them, as code.
At its most basic, Kubernetes is just a layer of abstraction that lets you think about a pool of computers if it were one (headless) computer. If that’s your use case, and you can avoid the other parts of it, you can get pretty far.
Some people have told me that #2 is overkill, startups shouldn’t focus on zero-downtime deploys or high availability. But we often do multiple deploys per day, and when our products break, our customer’s products break for
*their* users. Even a minute of downtime is noticed by someone. Rolling deploys give us the confidence to deploy unceremoniously and often.
## How we use Kubernetes
For background,
[Jamsocket](https://jamsocket.com) is a service for dynamically spinning up processes that a web app can talk to. Kind of like AWS Lambda, but where the process lifetime is bound to a WebSocket connection instead of a single request/response.
We use Kubernetes to run the long-running processes that are needed to support that. The API server, container registry, controller, log collector, some DNS services, metrics collection, etc.
A few things we
*don’t* use Kubernetes for:
- The ephemeral processes themselves. We did for a hot minute very early on, but we quickly found it limiting (more on that later.)
- Static/marketing sites. We use
[Vercel](https://vercel.com/)for those. It’s more expensive, but so is the opportunity cost of an hour of engineering time at a small startup, and Vercel saves us more of that than it costs.
- Anything that directly stores data we would be sad to lose. We do use some persistent volumes for caching or derived data, but otherwise we use a managed Postgres DB outside of the cluster and blob storage.
It’s also worth noting that we don’t administer Kubernetes ourselves — the main advantage of using Kubernetes is that we can outsource the infrastructure-level operation of it! We have been happy with Google Kubernetes Engine, and while the
[Google Domains fiasco](https://blog.pragmaticengineer.com/google-domains-to-shut-down/) has shaken my faith in Google Cloud, I at least sleep soundly knowing that migrating to Amazon EKS would be relatively straightforward.
## Things we readily use
There are a few types of k8s resources we use without hesitation. I’m only listing resources here that we create explicitly; most of these resources implicitly create other resources (like Pods) that I will not mention but which we of course (indirectly) use.
**: Most of our pods are created through deployments. Every deployment critical to our service functioning has multiple replicas and rolling updates.** [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) **: specifically,** [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
ClusterIPfor internal services and
LoadBalancerfor external ones. We have avoided
NodePortand
ExternalNameservices, preferring for our DNS configuration to live outside of Kubernetes.
[: for cleanup scripts and that sort of thing.](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) **CronJobs** **ConfigMaps**and **Secrets**: for passing data to the above resources.
## Things we cautiously use
**StatefulSet**and **PersistentVolumeClaim**: we have used some StatefulSets. The configuration is a bit more convoluted than Deployments, but they can have a persistent volume across restarts. We prefer to persist important data in managed services outside of k8s. We don’t have a hard rule against volumes because sometimes it’s nice to persist e.g. a cache across a service restart, but I avoid them when possible because they can interact badly (deadlock) with rolling deploys. **RBAC**: we have used this in a few places, e.g. to give a service permission to refresh a secret. It adds enough complexity to our small cluster that I mostly avoid it.
## Things we actively avoid
**Hand-writing YAML**. YAML has [enough foot-guns](https://noyaml.com/)that I avoid it as much as possible. Instead, our Kubernetes resource definitions are created from TypeScript with [Pulumi](https://www.pulumi.com/). **Non-built-in resources and operators**. I’ve [written before](https://driftingin.space/posts/complexity-kubernetes)about how the [control loop](https://kubernetes.io/docs/concepts/architecture/controller/)pattern is a double-edged sword: it’s the core idea that makes K8s robust, but it’s also a source of indirection and complexity. The [operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)and [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)allow third-party software to use Kubernetes’ robust infrastructure for its own control loops, which is a great idea in theory that I’ve found to be clunky in practice. Rather than [cert-manager](https://cert-manager.io/), we use [Caddy’s](https://caddyserver.com/)certificate automation. **Helm**. Helm is a no-go because of the operators and no YAML rules, but I also just think that using unstructured string templating to generate something machine-parsable means introducing fragility for no gain. [is like nails-on-a-chalkboard to me, I’m sorry.](https://v2.helm.sh/docs/charts_tips_and_tricks/#using-the-include-function)
nindent
**Anything with “mesh” in the name.**I guess they’re useful to somebody, but not me, and not [this guy](https://matduggan.com/k8s-service-meshes/)either. **Ingress resources**. I don’t have any battle scars from these, and I know some people use them productively, but a theme of our successful use of Kubernetes is avoiding adding unnecessary layers of indirection. Configuring Caddy works for us, so we just do that. **Trying to replicate the entire k8s stack locally**. Instead of using things like k3s or kind to replicate production exactly, we just use Docker Compose or our own scripts that start the subset of the system we actually care about in the moment.
## A human should never wait for a pod
Above I alluded to the fact that we briefly ran ephemeral, interactive, session-lived processes on Kubernetes. We quickly realized that Kubernetes is designed for robustness and modularity over container start times. As a general rule, my take is that Kubernetes is good for when you want to redundantly run some long-running processes, but if a human is ever waiting for a pod to start,
[Kubernetes is the wrong choice](https://twitter.com/paulgb/status/1684718880353042432).
I’ll confess that I’m talking my book here, but at least it’s an open-source book: we use an MIT-licensed Rust orchestrator called
[Plane](https://plane.dev/) that we designed specifically for quickly scheduling and running processes for interactive workloads (i.e. ones with a human waiting on them).
## Higher-level abstractions
For completeness, I should also mention that some of the Kubernetes alternatives that have popped up are quite good. Particularly if you don’t want or need requirement #3 from my initial list (the ability to specify infrastructure as code.) For
[one of our products](https://y-sweet.cloud/), we opted to use [Railway](https://railway.app/) rather than our k8s cluster, mainly for the preview environments. Some friends I respect highly swear by [Render](https://render.com/) (I’ve dabbled but personally find Railway’s environment model cleaner.) I’m also partial to [Flight Control’s](https://www.flightcontrol.dev/) bring-your-own-cloud approach.
For a lot of SaaS type apps, you’ll probably get pretty far on those. But if you meet the three needs listed at the beginning of this article and you take a disciplined approach to it, don’t let anybody tell you that you’re too early for Kubernetes.