Kubernetes has always been sensitive to bad inputs. What’s changed is how often teams are running into it. As more bursty workloads—especially inference—land on Kubernetes, a familiar pattern shows up more often: clusters add nodes even when utilization looks fine. The CNCF’s [latest annual survey](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/) frames Kubernetes as the default platform for running AI in production, which means more teams are now feeling the edges of scheduling and autoscaling behavior that used to stay in the background. 

If you’ve ever looked at a cluster and wondered why it’s adding nodes when the dashboards suggest plenty of headroom, you’re not alone. This tends to show up after Cluster Autoscaler or Karpenter is already in place and obvious capacity issues such as mis-sized nodes, overly tight constraints, or consolidation settings have been cleaned up. 

And yet capacity keeps creeping up. Why is that? 

Most of the time it isn’t because Cluster Autoscaler or Karpenter is misconfigured. It’s the inputs. Requests are often set with a bit of guesswork and a safety buffer on top, and they don’t always get revisited as the workload changes. 

## The confusing part is that metrics look fine

The graphs you’re staring at can look calm, but when you look across a lot of clusters, the signs show up in a familiar order: 

* Cluster-wide CPU and memory graphs suggest there’s
* The scheduler still can’t place new pods.
* Pods sit Pending.
* Capacity gets added so those pods can land.

 From the outside, it looks like the [cluster is scaling](https://thenewstack.io/kubernetes-gets-back-to-scaling-with-virtual-clusters/) when it shouldn’t. But under the hood, it’s doing what it was built to do: place pods conservatively based on declared reservations. 

The scheduler places and packs pods based on requests. Usage graphs don’t factor into that placement decision. 

So when requests drift high, nodes get treated as full long before usage gets there. Once the scheduler can’t place pods, the autoscaler adds enough capacity so the pods can land, and that’s when the cluster starts growing even though usage dashboards still look fine. 

## This shows up in well-run clusters too

Request drift doesn’t require a messy environment. Actually, the causes are usually boring. 

A service has an incident and someone bumps requests to stabilize it. The incident fades, the request values stay, and nobody wants to be the person who lowers them and finds out the hard way they were masking a real issue. 

Defaults get standardized because [teams need a way to ship](https://thenewstack.io/think-like-a-developer-to-help-dev-teams-ship-faster/), and those defaults get copied into new services long after anyone remembers why they were chosen. 

Workloads change. Traffic shape shifts. Dependencies change. A request that was reasonable a quarter ago can be off after a launch, a new customer profile, or a batch job that quietly becomes part of the daily baseline. 

Inference workloads make this show up faster because replica counts move quickly, and a padded request doesn’t stay small for long. Either way, you end up with drift: old values surviving in YAML because nothing forced them to get revisited. 

## The first question to ask when scaling feels wrong

Instead, the question I’d start with is: do our requests still resemble how these workloads run today? 

If requests are inflated, the [scheduler blocks placements that should have fit](https://thenewstack.io/webassembly-needs-schedulers-and-kubernetes-doesnt-quite-fit-the-bill/) if you were going off usage. Packing looks worse than it should, so the autoscaler adds nodes to satisfy reservations rather than actual pressure. Consolidation can’t save you because the cluster is full on paper. 

You’re not trying to nail perfect numbers. You’re trying to get requests back into the neighborhood so the scheduler and autoscaler stop amplifying stale reservations. 

## How to confirm drift without turning it into a project

You can sanity-check this pretty quickly. Start with the handful of namespaces that dominate capacity and do two checks over a week or two. 

First, compare requests to observed usage over time. Not a single snapshot. Look for a gap that repeats day after day. 

Second, look at what happens when the workload scales out. Padding doesn’t stay small when replicas climb. If a deployment goes from 5 to 50 replicas under load, a little extra request turns into a lot of reserved capacity fast. 

Once requests are inflated and replicas climb, extra nodes are the expected outcome. 

## Where cost allocation helps without turning this into a billing conversation

Allocation views can help here because they make baseline drivers easier to see, even if you’re not doing chargeback. 

When requests are inflated, the same mismatch tends to surface: allocated looks high while usage looks low, and shared overhead becomes the part nobody can explain cleanly. Usually the tool is telling the truth — it’s just showing an uncomfortable mix of reserved capacity, safety headroom, and shared services that everyone depends on. 

The useful questions are practical: 

* Which namespaces or services are the biggest offenders?
* Is the gap driven by a few steady workloads, or bursts that scale outhard?
* How much of the gap is shared services / idle headroom vs direct workload footprint?

Once those buckets are explicit, the conversation gets more straightforward. You stop debating the output and start looking at the biggest gaps. 

## Getting unstuck is usually smaller than it feels

This is where teams sometimes over-scope it. You can usually get traction by starting with a small set of workloads. 

Start with the few services that dominate baseline capacity. If you bring those requests back in line, packing improves and the autoscaler stops chasing reservations that aren’t real. That’s often the point where the cluster stops feeling like it’s scaling for no reason. 

The other make-or-break factor is rollout safety. If request changes reliably create pager noise, nobody keeps doing them. The padded values stick around because they feel safer. 

So the sustainable approach is intentionally boring: make changes gradually, make rollback easy, and [put guardrails around](https://thenewstack.io/how-to-put-guardrails-around-containerized-llms-on-kubernetes/) how aggressive you’re willing to be. Once teams trust that request changes won’t destabilize things, drift becomes manageable instead of permanent. 

## What changes when drift is under control

When requests are closer to reality, a few things stop being weird. 

The scheduler can pack workloads more cleanly. Pending pods line up with real demand instead of stale reservations. Autoscaling adds capacity when there’s actual pressure, not because requests are reserving empty space. 

Allocation also gets easier to explain, mostly because [shared overhead is visible instead of hidden inside](https://thenewstack.io/apple-insiders-share-the-story-of-the-birth-of-the-macintosh/) everyone’s numbers. 

If capacity has been creeping up and cluster-level tuning isn’t sticking, start with the workloads that reserve the most. Compare requests to usage over time. If they’re far apart, you’ve probably found the driver behind the strange scaling behavior. 

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/03/ef632ec9-cropped-6af8874c-7xl80xrcanikrplucbevvxfkjuymwyrfsehjbhuxqui-600x600.png)

Yasmin Rajabi is the Chief Operating Officer at CloudBolt Software. She is a recognized leader in the FinOps and Kubernetes communities, and her background as an engineer, product leader, and operator gives her a holistic perspective on the challenges facing...

Read more from Yasmin Rajabi](https://thenewstack.io/author/yasmin-rajabi/)