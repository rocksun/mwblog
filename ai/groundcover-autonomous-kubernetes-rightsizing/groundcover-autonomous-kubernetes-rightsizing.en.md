**On Tuesday, [groundcover](https://www.groundcover.com/) launched [Autonomous Infrastructure](https://www.groundcover.com/product/autonomous-infra) in beta** to continuously adjust CPU and memory requests for Kubernetes (K8s) Deployments based on production data.

Built on technology from Wand, the K8s resource optimization platform [groundcover acquired in September](https://www.groundcover.com/news/groundcover-acquires-wand-to-build-toward-autonomous-infrastructure), the beta uses data already collected from groundcover’s eBPF sensor to inform resource allocation decisions, while giving engineers a direct view into how those decisions could affect infrastructure costs and workload performance.

[Shahar Azulay](https://www.linkedin.com/in/shahar-azulay-54156bb4?originalSubdomain=il), CEO and co-founder of groundcover, tells *The New Stack* about the balance the company is trying to get right: “The goal isn’t simply to reduce resource requests as much as possible. It’s to find the right balance between efficiency and stability across the entire environment.”

That can mean reducing requests for workloads consuming far less than they’ve been allocated, but it can also mean increasing requests when a workload needs additional resources to operate reliably. The objective is not simply a smaller infrastructure footprint. It’s an environment that continuously receives the resources it needs, without paying for capacity it doesn’t.

How to get there? Azulay says teams need “a continuous feedback loop that uses real production telemetry to identify when workloads are over- or under-provisioned and safely adjust them.”

## Does nobody know a good way to right-size K8s workloads?

It’s not for lack of trying. There are already a lot of different ways to tackle the burden of right-sizing K8s workloads.

For example, scheduled rightsizing applies changes at chosen intervals, so it may not respond between scheduled updates. [In-place resizing](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/) can change resources on running pods, although some changes require container restarts. Automated tools can also generate and apply recommendations within policies engineers set.

When asked why he thinks K8s rightsizing continues to trip people up, Azulay tells *The New Stack* the challenge lies in striking the right balance between cost efficiency and application stability:

“Resource requests are typically set at deployment time, when teams are making their best estimates before a workload has experienced real-world production traffic,” he explains. “The challenge is that workloads are constantly changing, but resource configurations often aren’t.”

> “The challenge is that workloads are constantly changing, but resource configurations often aren’t.”

After initial deployment, teams may simply let sleeping workloads lie, i.e., they don’t revisit original resource requests for reconfiguration. While workloads may keep spinning along just fine, this approach means teams risk unknowingly leaving them over- or under-provisioned—with costly consequences.

For organizations running hundreds or thousands of workloads, keeping those configurations accurate becomes an ongoing engineering task. Teams must analyze utilization, identify opportunities, test new settings, and revisit them as traffic and application behavior change. Even with the expertise, they may not have the time to do it continuously.

Azulay describes over-provisioning as “the safer choice because nobody wants to risk performance issues or outages.” But that extra peace of mind can come with unnecessary infrastructure costs; in a 2025 [study](https://www.mdpi.com/2076-3417/15/18/10098) published in *Applied Sciences*, researchers found that optimizing K8s resource allocation improved a combined performance-and-cost score by approximately 50% compared to the conventional maximum resource allocation approach.

Under-provisioning carries different risks. [Requests](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) help Kubernetes schedule pods, and CPU requests influence how CPU time is shared under contention; setting them too low can leave workloads short of CPU time. Limits work differently: CPU limits cause throttling, while exceeding a memory limit can trigger an out-of-memory (OOM) kill. Low memory requests can also increase eviction risk when a node is under memory pressure.

There’s also a relationship between workload requests and the cost of the cluster itself. Node autoscalers such as Karpenter can provision or remove nodes based on the resources workloads request, but they don’t determine whether those requests accurately reflect what each application needs. If workloads consistently request too much, the autoscaler may maintain more capacity than necessary. Right-sizing those requests gives the node autoscaler a more accurate basis for allocating infrastructure.

## What if the answer to done-right right-sizing is sitting in your production data?

Groundcover thinks so. That’s why its new Autonomous Infrastructure draws on the groundcover [eBPF sensor](https://www.groundcover.com/ebpf-sensor), which is already collecting telemetry across applications and infrastructure. The beta uses that production history to recommend CPU and memory requests for Kubernetes Deployments. Brand-new Deployments remain in a learning state until enough data is available.

But the approach isn’t simply to observe a spike in resource consumption and increase requests afterward. By the time a reactive system responds, the performance impact may already have occurred. Instead, groundcover’s optimization engine analyzes workload behavior over time, including usage patterns and resource contention, to anticipate capacity requirements and prepare workloads for expected changes in demand.

That distinction matters for workloads with recurring traffic spikes. The goal is to have enough resources available when demand arrives, without permanently allocating for peak consumption.

When engineers open the beta, they get a direct view of how much CPU and memory each workload requests versus what it uses, plus the number of under-provisioned workloads and estimated monthly savings if they apply changes. Groundcover’s [product page](https://www.groundcover.com/product/autonomous-infra) says dollar estimates use default list prices that administrators can adjust with their own prices and discounts. These estimates do not establish that a cloud bill will fall by the same amount; realizing savings also depends on whether freed capacity lets teams [reduce billed infrastructure](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt-compute.html).

An important part of the experience is that customers can see those opportunities before enabling autonomous optimization. Because groundcover already collects the necessary telemetry, existing customers can evaluate potential savings without deploying a separate monitoring agent or conducting another data-collection exercise. They can inspect recommendations, understand their expected impact, and decide which workloads, if any, to optimize.

Rather than setting resource requests at deployment time and letting them run on autopilot, engineers can use Autonomous Infrastructure to put real-time telemetry to work and continuously adjust resources based on production behavior. And because groundcover already collects the necessary telemetry, teams running a supported sensor version don’t need a separate agent or a new data-collection period for existing Deployments with sufficient history.

## Why the answer lies in the context

When asked how real-time production data can improve K8s right-sizing, Azulay tells *The New Stack* it comes down to understanding how workloads affect one another in production.

While some resource optimization tools size each workload on its own, he claims that approach doesn’t tell the whole story.

> “Kubernetes workloads don’t operate in isolation. They share nodes, compete for available resources, and can directly affect one another’s performance.”

Instead, to find the optimal balance between efficiency and stability, Azulay says engineers need tools that consider the entire environment:

“Kubernetes workloads don’t operate in isolation. They share nodes, compete for available resources, and can directly affect one another’s performance.”

For example, [lowering CPU requests](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) changes how a workload shares CPU under contention and can let the scheduler pack more workloads onto a node. A recommendation based only on one workload’s usage can therefore miss contention effects across the node.

This is one limitation of approaches that rely primarily on historical utilization for each workload. Two applications with similar CPU consumption may require different resource allocations depending on their traffic patterns, neighboring workloads, and the contention they experience. Applying the same sizing formula to both can leave one over-provisioned and the other vulnerable to performance problems.

To right-size each workload without bruising others, Azulay tells *The New Stack* resource optimization tools must not only evaluate real-time resource consumption against what’s being requested but consider the traffic patterns, workload behavior, and available resources across the node:

“True optimization requires understanding both individual workload behavior and the broader environment in which those workloads operate.”

Azulay says Autonomous Infrastructure uses that broader context. Leaning on Wand’s optimization engine, the beta uses node-level contention to inform right-sizing recommendations and make adjustments that consider the entire environment.

“It also looks beyond application containers to account for injected sidecars, such as Istio, Linkerd and Vault agents, which can be overlooked sources of resource waste,” Azulay says.

The integration with groundcover also connects resource optimization to the observability workflows engineers already use. Rather than receiving an isolated recommendation from a separate optimization tool, engineers can investigate workload behavior using the logs, traces, metrics, and infrastructure context available in the same platform. That helps them understand why a change was recommended and evaluate its impact on the environment.

The result is a connection between observing infrastructure and acting on what the data reveals. Production telemetry informs optimization decisions, and engineers can use that same observability context to understand what happens afterward.

## But are engineers ready to automate right-sizing?

Letting a tool like Autonomous Infrastructure take over K8s right-sizing can sound like a convenient solution. As Azulay tells *The New Stack*, many teams simply don’t get around to reconfiguring resource requests because of time and resource constraints — and engineers aren’t always sure the changes will improve efficiency without impacting stability.

But that doesn’t necessarily mean engineers are ready to go all in on automated right-sizing, at least for now. In [Kube.today’s 2025 community poll](https://kube.today/kubernetes-resource-management-2025) on Kubernetes resource management, 56.5% of respondents selected manual tools such as kubectl and dashboards as their primary approach. That result reflects the poll’s respondents, not Kubernetes practitioners as a whole.

Groundcover’s own research, administered by Atomik Research, underlines engineers’ uncertainty about going fully autonomous. In the [survey](https://www.groundcover.com/third-party-reports/the-observability-imperative?utm_source=groundcover&utm_medium=media-coverage&utm_campaign=press_wand_announcement_q326-1601&utm_content=landingpage) of 500 U.S. technology professionals, 87% say AI or automation is already integrated into observability workflows, but only one-third (34%) call it “fully operational and trusted.”

For those hesitant to hand over the reins for resource optimization, groundcover’s beta might offer some relief.

Per groundcover, Autonomous Infrastructure is “opt-in at every level.” By default, automation is off; groundcover’s [launch blog](https://www.groundcover.com/blog/introducing-autonomous-infra) describes opting in a cluster and then enabling individual Deployments.

While the beta may use production telemetry to autonomously adjust resource requests, engineers still set the parameters, defining minimum and maximum bounds for CPU and memory requests. The beta changes requests only, leaving limits unchanged. A [declared limit](https://www.groundcover.com/product/autonomous-infra) caps the recommendation; a workload constrained by that limit appears as “Bounded.” Groundcover says every policy change is versioned and an audit log records who assigned each workload to a policy and when. A resource used by an HPA or KEDA utilization-based autoscaler is left unchanged. The beta uses [in-place resizing](https://www.groundcover.com/blog/introducing-autonomous-infra) when possible and falls back to a rollout when necessary.

For engineers who may be wary of giving a resource optimization tool full access to decide and execute K8s right-sizing, these constraints can ease the transition. Plus, they can easily keep a pulse on what the beta is doing, with groundcover’s view showing how many workloads are managed autonomously in each cluster and namespace.

> “…engineers aren’t being asked to trust a black box.”

Perhaps more importantly, engineers aren’t being asked to trust a black box. They can review the reasoning behind recommendations, inspect the expected effects, and choose precisely where to enable autonomous changes. The automation is designed to remain understandable and reversible.

## Who will get right-sizing right?

Groundcover says the [Autonomous Infrastructure beta](https://www.groundcover.com/news/groundcover-launches-autonomous-infrastructure-beta) is available at no additional cost to its customers running the groundcover sensor on Kubernetes, with a supported sensor version required. The beta covers [Deployments and their sidecars](https://www.groundcover.com/blog/introducing-autonomous-infra); support for other workload kinds is on the roadmap. The company is inviting design partners and plans demonstrations at booth #111 during [KubeCon + CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/), Nov. 9–12, 2026, in Salt Lake City.

The question for the next generation of Kubernetes optimization tools may be less about how aggressively they can reduce resource requests and more about how intelligently they can manage them. That means anticipating demand, accounting for contention across the environment, and making changes engineers can understand and trust.

For groundcover, bringing optimization into the same platform that collects and analyzes production telemetry is a step toward that model: infrastructure that doesn’t just report what’s happening, but uses that understanding to continuously improve how it runs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)