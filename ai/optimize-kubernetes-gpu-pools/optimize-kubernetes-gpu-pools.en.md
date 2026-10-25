**For teams running AI workloads** on Kubernetes, a fully allocated GPU pool and a growing batch-job queue might make expanding the pool seem like the obvious next step. But a growing queue could point to timing, serving capacity, or the choice of model and hardware. Before expanding a GPU pool, teams should define what success looks like, when it must finish, and what it costs to deliver.

> “An allocated GPU, a busy GPU, and a workload producing valuable results are not the same thing.”

That starts with a distinction: an allocated GPU, a busy GPU, and a workload producing valuable results are not the same thing. Understanding how they relate can help teams use existing capacity more effectively before provisioning additional capacity they genuinely need.

## Start with the outcome and deadline

Look at the workloads and the underlying use cases they support. A customer service chatbot may need around-the-clock inference capacity, while results from a model evaluation job might only be needed before the next internal release sync. Classifying workloads into broad categories like “inference” and “training” does not determine urgency. Some batch inference can wait, while a training job may have a firm deadline.

---

***KubeCon + CloudNativeCon is taking place in Salt Lake City from November 9 to 12.*** [***Register now***](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)***!***

---

For each workload, document its deadline, expected runtime, resource requirements, and whether interruption is acceptable. Also define what counts as a valuable output. An inference service should have a task-specific quality threshold and a latency objective. A completed request or valid JSON response alone does not show whether the workload met its objective.

Keep start-time flexibility separate from interruption tolerance. A job that can wait to start may still need to run without interruption.

## Use scheduling flexibility before expanding the pool

Suppose four compatible GPUs are available for batch work from noon until 5 p.m. Four independent evaluation jobs are ready at noon. Each needs two GPUs for one hour, and all results are due at 5 p.m.

Starting all four jobs immediately requires eight GPUs. But running two at noon and two at 1 p.m. completes all four jobs by 2 p.m. using the four GPUs already available. Assuming runtimes and supporting resources remain unchanged, both schedules consume eight GPU-hours, excluding startup overhead.

> “Staggering reduces peak demand. The jobs still finish on time without expanding the pool.”

Staggering reduces peak demand. The jobs still finish on time without expanding the pool. Before provisioning more GPUs to clear a queue, consider how much flexibility exists in start times.

Tools like [Kueue](https://kueue.sigs.k8s.io/docs/overview/) provide an admission control point, using configured quotas and policies to determine when work is admitted. Teams still need to decide how to represent and enforce deadlines and workload requirements. Flexible queueing can support capacity planning and reduce the need to start jobs early, only to preempt them later.

## Measure how much useful work the deployment can sustain

Flexible scheduling can ease capacity constraints. But inference teams must also examine how well the model and serving configuration match that work.

High GPU activity does not establish how much additional throughput is available. [Nvidia’s profiling documentation](https://docs.nvidia.com/datacenter/dcgm/latest/learn/modules/profiling.html) explains that streaming multiprocessor activity can include warps waiting on memory. Serving metrics like running requests, waiting requests, and cache occupancy add context, while preemption counts help explain behavior. In vLLM, [KV-cache usage measures the fraction of occupied cache blocks](https://docs.vllm.ai/en/latest/usage/metrics/), but it doesn’t directly measure total serving capacity.

> “High GPU activity does not establish how much additional throughput is available.”

Measure sustainable capacity with a representative load test. Keep the model, hardware, serving settings, and request mix constant. Then, increase the arrival rate and observe throughput, quality, and latency. The highest sustained rate that still meets the workload’s requirements, including error limits and selected latency percentiles, provides a useful capacity estimate. For interactive generation, include time to first token and subsequent token delivery, not just average completion time. [DistServe](https://arxiv.org/abs/2401.09670) shows why you should evaluate serving capacity against application-level objectives like latency.

Compare production traffic with that tested capacity. Low cache occupancy may warrant further investigation, but claiming ten times more throughput requires a throughput test. Brief queues can represent temporary bursts, while persistent queues might require diagnosis. Neither on its own identifies the limiting resource.

## Connect OpenCost data to verified outcomes

The FinOps community frames AI efficiency around [cost and useful outcomes](https://www.finops.org/insights/token-economics-the-atomic-unit-of-ai-value/). For [AI workloads](https://thenewstack.io/agentic-ai-kubernetes-management/), cost becomes more useful when it connects to the outcomes the infrastructure helps deliver. Kubernetes teams can make that relationship concrete by combining workload cost, serving behavior, and application results.

Use [OpenCost’s allocation API](https://opencost.io/docs/integrations/api/) for workload costs at defined intervals, then join that data with serving telemetry and outcome records using workload identities and timestamps. OpenCost also provides opt-in [inference cost tracking](https://github.com/opencost/opencost/blob/v1.121.3/docs/inference-cost-tracking.md), including cost per million tokens. When calculating cost per outcome, include applicable GPU, CPU, memory, and other infrastructure costs, and document how shared and idle costs are assigned. Add relevant costs outside OpenCost separately without counting them twice.

One useful metric is [cost per verified outcome](https://thenewstack.io/greenops-and-finops-a-dual-strategy-for-sustainable-ai/): total attributable cost divided by the number of results that meet the defined quality requirements and are delivered within the required time. Account for retries, failures, startup, and idle periods where they contribute to total cost. Count the final business result once. When correctness is estimated from sampled reviews, document the sampling method and uncertainty.

OpenCost supplies the cost allocation details; the application supplies the outcome definition and evaluation evidence. Capacity still requires a separate measurement. [OpenCost proposal 3915](https://github.com/opencost/opencost/pull/3915) explores bringing serving-engine telemetry into the cost model. The proposal remains a draft, rather than a released saturation or correctness score.

## Test whether the spare capacity earns its cost

Consider an illustrative service receiving 1,000 tasks per hour with a 98% correctness requirement. A small model that achieves 90% is unsuitable, even if its GPU is cheap and fully occupied.

A stronger model might produce 990 correct and timely results for $2 per hour while using only a fraction of its tested serving capacity. Its cost is about $2.02 per 1,000 qualifying outcomes, and that spare capacity may be an acceptable price for meeting quality requirements and absorbing bursty activity.

The next test is whether a smaller GPU, fewer replicas, or a different batching setting can preserve those outcomes and the required reliability. If a tested configuration produces the same 990 qualifying results for $1.50, the cost falls to about $1.52 per 1,000 qualifying outcomes. Savings come from using fewer resources to deliver the same outcome. Increasing utilization on the original GPU without improving the outcome would provide no comparable value.

> “The target is a deployment that delivers the required outcomes at a defensible cost, with enough headroom to meet its requirements.”

When two models both meet the minimum requirements, an additional quality improvement may justify a higher cost if it provides fewer consequential errors or requires less human review. Compare that value with actual demand. Cost per correct outcome is most useful when the outcomes being compared have similar value and error consequences.

Change one major variable at a time, then compare the cost, verified outcomes, latency, and deadline attainment under representative demand. Preserve capacity for bursts and failures, and confirm that low activity corresponds to usable capacity. A GPU allocated exclusively to one Pod cannot be reassigned to another until it is released.

Teams can then choose the change the evidence supports: delay flexible jobs, improve batching, resize a deployment, select a different model, or [provision additional GPUs](https://thenewstack.io/kubernetes-gpu-management-just-got-a-major-upgrade/). The target is a deployment that delivers the required outcomes at a defensible cost, with enough headroom to meet its requirements.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/10/8d9c1fef-danielle_zeis-danielle-zeis-600x600.jpg)

Danielle Zeis is a principal product marketing manager at IBM, where she works across the FinOps portfolio, including IBM Kubecost and IBM Cloudability. She focuses on cloud cost management, Kubernetes cost visibility and optimization, and helping organizations connect infrastructure usage...

Read more from Danielle Zeis](https://thenewstack.io/author/danielle-zeis/)