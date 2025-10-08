Every Kubernetes release brings the good, the bad, and the blind spots you only discover in production. The latest version (1.34) is no exception. From GPU scheduling to swap support, the latest features deliver real value but also introduce new complexities that platform engineers cannot afford to ignore.

The temptation is to turn these features on and move forward. But first, let’s unpack the new risks, observability gaps, and operational overhead they create, so you can adjust your playbooks before deploying them at scale.

## **Dynamic Resource Allocation**

One of the most visible changes in v1.34 is the graduation of dynamic resource allocation (DRA) to GA. It gives [Kubernetes clusters more flexibility when scheduling](https://thenewstack.io/kueue-can-now-schedule-kubernetes-batch-jobs-across-clusters/) GPUs, TPUs, and other specialized devices. This is a clear win for AI and ML workloads that need accelerators to scale.

But this flexibility also adds complexity. More scheduling logic means more places for misconfigurations to creep in. An application may request resources that cannot be met, which can cause scheduling delays or fallback scenarios that behave differently than expected. On the financial side, over-allocating GPUs can waste tens of thousands of dollars per month.

The practical takeaway is to thoroughly test allocation scenarios in staging before rolling them out into production. Engineers should also ensure monitoring is in place to track accelerator requests and usage. Without visibility, the benefits of DRA can easily turn into cost and performance liabilities.

## **Linux Node Swap Support**

Another major change is the GA release of [Linux node swap support](https://thenewstack.io/canonical-extends-kubernetes-distro-support-to-a-dozen-years/). Swap is a long-requested feature that helps nodes remain stable under memory pressure. Instead of crashing pods when memory is exhausted, nodes can now shift some of that pressure to disk.

On paper, this sounds like a safeguard against out-of-memory events, but in practice, swap introduces new performance issues. Heavy reliance on swap can mask workloads with poor memory behavior, creating the illusion of stability while latency spikes mount. Tuning swap behavior requires careful attention, and troubleshooting memory issues can be tricky as engineers must now distinguish between physical memory pressure and swap-related slowdowns.

Swap should be viewed as a safety net, not a performance strategy. Engineers adopting it should update dashboards to track swap-in and swap-out activity and treat any sustained use as a signal to fix resource requests and limits at the workload level.

## **Pod-Level Resource Requests and Limits**

With v1.34, [Kubernetes now allows requests and limits](https://thenewstack.io/kubernetes-requests-and-limits-demystified/) to be defined at the pod level instead of just at the container level. For workloads with multiple containers, this makes quota management easier and reduces the risk of overcommitting resources.

However, this feature can obscure per-container overuse. If one container monopolizes resources, the problem may not be visible when limits are set at the pod level. Horizontal Pod Autoscalers (HPAs) may also misbehave since their assumptions are tied to container-level metrics.

Before adopting pod-level limits broadly, engineers should revisit how autoscaling is configured in their clusters. [Observability tools may also need](https://thenewstack.io/using-ai-for-devops-what-developers-and-ops-need-to-know/) updating to ensure they capture per-container consumption even when pod-level requests are in place. Without that visibility, it becomes harder to hold teams accountable for runaway containers or to troubleshoot performance regressions.

## **Security Enhancements**

The release also introduces important security improvements. Short-lived tokens, external signing, and pod-level certificates strengthen compliance postures and reduce long-lived credential risk. These changes are steps in the right direction, but they add operational overhead.

Integrating with external key management or hardware security modules introduces new dependencies that must be reliable at all times. If the external signing system goes down, deployments can fail. Frequent certificate rotation requires automation and alerting to avoid outages caused by expired credentials.

For platform teams, the lesson is to treat these new features as critical dependencies that need full observability and automation. Token and certificate lifecycles must be monitored like any other part of the system, with failure modes clearly documented in runbooks.

## **Storage and Scheduling Improvements**

Several smaller but important changes round out the release. Volume expansion recovery and the introduction of VolumeAttributesClass give workloads more dynamic control over storage. Smarter job pod replacement and non-blocking API calls reduce bottlenecks for large clusters.

These features deliver flexibility and scalability, but they also expand the range of possible failure modes. For example, when workloads can change volume attributes on the fly, troubleshooting I/O slowdowns becomes more difficult. Non-blocking APIs and streaming responses reduce API server pressure but increase reliance on cache states, which can create subtle consistency issues.

When adopting these features expand monitoring to track IOPS, storage expansion attempts, and cache behavior. The benefits are real, but so are the new debugging scenarios they introduce.

## **What This Means for Platform Engineers**

Taken together, v1.34 gives [platform teams better tools to manage modern workloads](https://thenewstack.io/streamlining-your-platform-teams-workloads/). But none of these enhancements reduce work. Instead, they shift it. Before [deploying each new feature platform engineers](https://thenewstack.io/build-and-deploy-scalable-technical-architecture-a-bit-easier/) should ask themselves three questions:

1. What new metrics must we capture?
2. What new failure modes are introduced?
3. Who owns remediation when something breaks?

By [building answers to those questions into observability](https://thenewstack.io/building-an-ergonomic-opentelemetry-for-javascript/) stacks, policies, and runbooks, engineers can get the benefits of v1.34 without creating hidden liabilities.

Kubernetes v1.34 is a reminder that progress often comes at a price. The release brings capabilities that make clusters more resilient and adaptable, but each one introduces operational blind spots if adopted without preparation.

Platform engineers who treat upgrades as simple feature toggles will be caught off guard by new debugging challenges, performance tradeoffs, and governance gaps. Those who approach v1.34 with discipline, testing in staging, expanding monitoring, automating governance, and updating ownership models, will be able to deliver both speed and stability

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/02/7c0d6ed0-itiel-shwartz-cto-and-co-founder-komodor-headshot.jpg)

Itiel Shwartz, CTO and co-founder of Komodor, is an expert in Kubernetes, cloud-native technologies and infrastructure. He has served in technical leadership roles at eBay, Forter, and Rookout.

Read more from Itiel Shwartz](https://thenewstack.io/author/itiel-shwartz/)