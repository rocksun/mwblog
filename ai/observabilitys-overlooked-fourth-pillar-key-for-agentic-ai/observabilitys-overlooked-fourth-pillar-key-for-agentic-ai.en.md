The move from observability 1.0 to 2.0 added a lot, but I think we’ve forgotten something along the way.

A quick reminder about the three pillars of observability 1.0. The three established pillars are [metrics, logs and traces](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/). I like to categorize them by cost (in system monitoring terms, CPU, memory and disk) and by strengths and weaknesses (cardinality, resolution and retention).

* **Metrics:** Numerical values with limited cardinality, unlimited resolution and very long retention. They have a low system cost.
* **Logs:** Logs have unlimited cardinality, limited resolution and limited retention. Due to disk usage, they are at least an order of magnitude more expensive than metrics.
* **Traces:** Traces feature high cardinality, low resolution, long retention and relatively high system demand. Again, they are at least one or two orders of magnitude more expensive than logs.

[Observability 2.0](https://thenewstack.io/beyond-monitoring-how-observability-2-0-is-revolutionizing-developer-experience/) introduces context as a first-class citizen. Context is something practitioners were already using. However, it existed outside the formal observability stack and wasn’t explicitly named. It also added the wide events concept, giving context to an observation. Both of these came from looking at what observability already had and identifying what was missing.

In the same way, there’s another piece we’ve been using all along without naming it: diagnostic procedures. If we don’t recognize this now, we risk repeating the same mistake: leaving a critical capability out of the observability model until it’s too late. And if we leave it out, we won’t have the tools or the machine-usable knowledge needed for an automated agent to perform these operations when moving to observability 2.0.

## A Medical Analogy

I want to give a medical analogy. I’ll admit, I’ve watched too many episodes of “House.” In my defense, I’ve also seen my fair share of system diagnoses.

A person is admitted to a hospital based on symptoms. The staff connects them to a monitor (OK, that’s the obvious part of the analogy), runs some blood tests and keeps track of their condition verbally. (Like when the patient shouts, “Nurse, my head hurts!”)

At this stage, a doctor might look at all these inputs and decide, “They’re just dehydrated,” and send them home. This is the routine first-line diagnosis, the part we almost never get to see in “House.”

But when the first line of diagnosis fails, a different set of diagnostic procedures comes into play: X-ray, MRI, catheterization, to name a few. These are far more expensive and can carry real risks to the patient’s health or well-being. That’s why they are initiated on an ad hoc basis, based on clinical judgment, and are highly targeted.

In more complicated cases, you might hear things like, “Let’s stress them until the symptoms get stronger,” or, “Let’s flush them so they’ll have another seizure.” These are deliberate interventions to make hidden issues visible.

The key point here is that diagnostic procedures are selective, deliberate and informed by other data as well as the investigator’s experience and understanding.

## Mapping to Observability

Before we go further, let’s clarify how medical diagnostics map to observability ones.

|  |  |  |
| --- | --- | --- |
| **Medical** | **Observability** | **Pros/Cons** |
| Vital signs monitor | Monitoring | Cheap to use, high sampling rate, low cardinality |
| Patient chart | Logs | Anyone can write anything here, free-form and unstructured, but there’s a limit to how much can be recorded |
| Blood tests | Traces | More expensive, gives an in-depth view, limited in how many you can reasonably run |

And then there’s the fourth pillar: diagnostic procedures, which are our MRIs, biopsies and catheterizations for systems. These are the rare, targeted, sometimes risky operations we perform when everything else has failed to explain the symptoms.

## Diagnostic Procedures in Systems

For software systems, diagnostics are targeted, often costly, ad hoc operations run to understand internal system behavior. Let’s unpack that a bit.

First, ad hoc and intentional. The initiator is outside the system, usually acting in response to a symptom or unexpected behavior. The key point is that a decision was made to trigger it … by a human or by automation.

Second, targeted. We perform the procedure to answer a specific question or validate a hypothesis. The key point is that it’s precise and focused (unlike metrics or logs, which are broad and continuous).

Finally, cost. This includes system resources like CPU, memory, network and disk, as well as any external resources (such as an engineer physically connecting a probe to a network card). Cost also includes risk: the potential impact on the system and the penalty if that risk materializes.

Here are a few real-world examples of diagnostic procedures:

* Setting the log level to DEBUG
* Generating core dumps
* Resetting a machine
* Connecting a debugger
* Running network packet diagnostics

Anyone who has tended to a struggling system can probably relate. You have a reason to do it, and you know it comes with risk, especially if the system is already showing degraded performance. Understanding the wider context from a cost and risk perspective is what makes the difference. Connecting a debugger to a host in a test environment to fix a known problem might earn you a raise; doing the same thing in production could get you fired.

Diagnostic procedures are typically:

* Triggered in response to an observation.
* Focused on a specific hypothesis.
* Potentially disruptive to system stability.
* Noncontinuous by design.

Look at the Wikipedia definition of observability: “Observability is the ability to collect data about a program’s execution, modules’ internal states, and the communication among components.” This is exactly what these diagnostic procedures do.

They’ve been here all along. They’re an important aspect of observability, yet they were left unnoticed and unnamed when the original pillars were defined. Just like context in observability 1.0, they were always part of the investigator’s toolkit, but not in the foreground.

## Why Diagnostic Procedures Are So Important Now

There’s a reason for the observability 2.0 hype. It starts with an “A” and ends with an “I.”

Once you try to teach an AI agent to make sense of your observability stack, you realize that context is hard. It’s hard for humans, too. That’s why we have skilled engineers working intensely to diagnose faulty systems. But we also see that some tasks that come naturally to humans are much harder for AI.

In observability 2.0, we aim to give context to events. For humans, context lives in our heads (and in our notebooks). This shift will likely help with first-tier support, the observability equivalent of an ER nurse. But soon we’ll hit the next bump: It’s not enough.

If we want AI to go beyond triaging and into active diagnosis, we need to give it the wheel, not just the map. And that means capturing diagnostic procedures in a way that machines can understand, complete with their context, cost and risk. Just like with wide events, AI needs wider context to make meaningful decisions. It needs a broader understanding of the system and the possible outcomes of its actions.

## A Distributed Database Example

Take a typical high-availability setup in a distributed database: replication factor 3. Every piece of data is stored on three nodes, allowing the system to continue operating normally if one node goes down.

Now imagine the cluster is suffering from sudden high latencies.

* **Scenario 1:** The system is overloaded. The right move might be to reduce unneeded background tasks or add more compute resources.
* **Scenario 2:** A faulty disk on one machine is slowing down operations.

Spotting that one node is lagging behind the others, a human operator might decide to restart that node or even remove it from service, knowing the remaining nodes can handle the load. That same human would also check for global events, like an ongoing upgrade, to decide whether this action is safe.

Although losing one node in this setup is fine, losing two would break availability. Making that judgment call requires broad context: awareness of current workloads, redundancy, recent changes and failure risks.

For an AI agent, making the right decision based on understanding the broader context can mean the difference between:

* Saving the system by intelligently removing a flaky node, and
* Taking it from high latency to complete downtime

## What’s Needed for Agentic AI

Without explicit recognition and encoding of diagnostic procedures — including their preconditions, costs and consequences — [AI will struggle](https://thenewstack.io/why-ai-demands-a-new-approach-to-observability/) to make these nuanced calls.

If we don’t recognize diagnostic procedures now, we’ll leave a critical capability behind as observability 2.0 tools and AI-driven workflows mature.

Context was absent from the formal pillars in observability 1.0. Tools and operators weren’t designed to capture or use it. And for AI agents, generating context on their own is a particularly hard task.

The same risk applies to diagnostic procedures today. Humans will keep performing these actions out of habit and experience, but AI agents and automated systems won’t have the hooks, safeguards or understanding to use them effectively. If we want the next generation of observability to truly match what our best engineers can do, we need to bring diagnostic procedures into the light now: name them, model them and design for them.

To start, we need a unified way to describe them, capturing attributes like risk, duration, cost, probable impact, service-level agreement (SLA) considerations, reversibility and impact criteria. (For example, see this [hypothetical diagnostic procedure definition](https://gist.github.com/amnonh/42b889f9f53648714565afe938c11bdb).)

The beauty of this approach is that once we normalize diagnostic procedures in this structured way, we’ll naturally start rethinking them. By making these risk factors explicit instead of relying solely on intuition, we can lower the danger of what support engineers are already doing today — and make it safer for AI agents to do the same tomorrow.

Second, we’ll need a unified and normalized way of running such procedures. For example, an AI agent might choose to validate a hypothesis about a faulty disk by selecting a “full-surface-scan” from a diagnostic procedure library. It would acknowledge the potential impact on the system, determine that it won’t violate SLA commitments and execute it with a normalized specification of SLA criteria: defining what constitutes a service interruption versus service degradation, how long an interruption is acceptable, under what conditions to stop and how much system resources the process is allowed to consume.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/09/642e33de-cropped-4c2e0405-image1.jpg)

Amnon Heiman has 20 years of experience in software development of large-scale systems. Previously he worked at Convergin, which was acquired by Oracle. Amnon holds bachelor’s and masters degrees in computer science from the Technion-Machon Technologi Le' Israel and an...

Read more from Amnon Heiman](https://thenewstack.io/author/amnon-heiman/)