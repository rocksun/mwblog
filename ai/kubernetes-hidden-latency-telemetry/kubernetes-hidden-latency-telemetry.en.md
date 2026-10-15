**In cloud-native operations, few scenarios are as maddening as the “phantom slowdown.”** This happens when [Grafana](https://grafana.com/) or [Kubernetes](https://kubernetes.io/) dashboards show a sea of green: pods are running, liveness and readiness probes return success codes, and node CPU utilization stays well below capacity limits. Yet users submit urgent tickets complaining of sporadic, severe latency when querying an application or waiting for an AI model’s response.

Why do basic health checks pass inspection while application performance degrades? And how can engineering teams trace the root cause when the issue is intermittent and spans multi-tier hybrid infrastructure?

To understand the mechanics of these sometimes evasive performance regressions, *The New Stack* spoke with [Mahesh Ramachandran](https://www.linkedin.com/in/ramachandranm/), who leads product management for [HPE OpsRamp Software](https://www.hpe.com/us/en/products/software/opsramp-software.html).

Ramachandran tells TNS how continuous telemetry and retrospective analysis help teams investigate intermittent slowdowns, and how AI-assisted investigation can complement dashboards.

---

#### ***Earlier stories in this special series:***

Part 1: [Developers and platform teams both want Kubernetes self-service. They disagree on who owns it.](https://thenewstack.io/kubernetes-self-service-platform-teams/)

Part 2: [A live Kubernetes cluster can still have an ownership gap](https://thenewstack.io/kubernetes-operations-ownership-governance/)

---

## The illusion of cluster health

Kubernetes probes report whether their configured checks succeed. A liveness probe helps determine when to restart a container, including one whose process is running but stuck. A readiness probe helps determine whether a container is ready to accept traffic.

Custom checks can include application or dependency conditions, but passing a basic probe doesn’t mean a complete user request meets its response-time target. Teams still need application performance measurements.

“Consider a composite scenario based on what we see across enterprise deployments,” Ramachandran says.

“Users of a system — such as an AI prompt-serving application on Kubernetes — report sporadic slowness in query response times.

“The engineering team inspects the cluster, the nodes, and the pods. Everything appears healthy on the surface with zero reported pod failures. The difficulty lies in the slowdown’s sporadic nature. When degradation happens intermittently, pinpointing the source without historical evidence becomes almost impossible.”

Passing probes narrow the investigation; they do not close it. A snapshot of a healthy cluster may miss an earlier slowdown, and the absence of container failures does not establish that the application or its dependencies are performing well. The next step is to connect the user’s reported delay to measurements from the affected period.

## Telemetry across the hybrid stack: Sifting signal from noise

Resolving sporadic slowness requires moving beyond surface-level Kubernetes metrics to continuous, multi-layer telemetry. Modern cloud-native architectures do not exist in isolation; a user request may depend on application code, container runtimes, virtualized or bare-metal infrastructure, and public cloud APIs. The relevant layers depend on the deployment.

“HPE OpsRamp collects signals continuously across every layer of the stack — Kubernetes nodes, pods, ingress controllers, and services — capturing logs, events, and metrics,” Ramachandran says. “The foundational step in troubleshooting sporadic issues is having a continuous record. You must go back into the telemetry history to correlate user-reported symptoms with actual signal evidence.”

> “When degradation happens intermittently, pinpointing the source without historical evidence becomes almost impossible.”

However, Ramachandran emphasizes that finding the evidence within telemetry signals is rarely straightforward.

“It often requires intelligence to sift through the noise,” he says. “An anomaly might not appear as an obvious spike in a single metric. Instead, it might be a subtle variation or a correlated behavior where two separate signals both look normal individually, but their combined behavior produces latency.”

A practical investigation starts with the affected transaction and time window. Compare query response times and queries per second with pod health and counts, then look for variations in the collected signals that coincide with the slowdown.

A correlation identifies a candidate explanation; it does not prove the cause on its own. After making a change, compare the same user-facing measures with the earlier behavior to check whether performance improves. Because the scenario is composite, the team still needs to validate any suspected cause in its own environment.

> “An anomaly might not appear as an obvious spike in a single metric. Instead, it might be a subtle variation or a correlated behavior where two separate signals both look normal individually, but their combined behavior produces latency.”

Coverage depends on the agents, integrations, permissions, and application instrumentation teams configure.

OpsRamp provides several ways to collect evidence across the relevant tiers:

* **Application:** OpenTelemetry-compatible trace collection for instrumented applications. Teams must configure application instrumentation and the collection path; infrastructure monitoring alone does not generate application traces.
* **Orchestration:** Kubernetes agents collect cluster and workload telemetry; additional monitoring configuration can provide visibility into components such as ingress controllers.
* **Virtualization and HCI:** Integrations with [VMware](https://vmware.com), [Nutanix](https://nutanix.com), and [HPE Morpheus VM Essentials Software](https://docs.opsramp.com/integrations/virtualization/vm-essentials/) collect inventory and performance data to help investigate infrastructure bottlenecks.
* **Hardware:** [Redfish protocol](https://www.dmtf.org/standards/redfish) integration for telemetry from supported physical servers, with the required API access and gateway connectivity.

## Navigating black-box dependencies outside the cluster

Applications can depend on services outside their Kubernetes cluster, Ramachandran says. A user request might originate inside a private cluster but call an external SaaS endpoint, a database outside the mesh, or a public cloud AI model.

When an application relies on external third-party services, visibility hits a boundary. “If your application makes calls to a public AI model or an external web service, you enter a domain outside your direct monitoring control,” Ramachandran explains. “To rule out external dependencies as the source of slowness, you must quantify their performance as a black box.”

To bridge this visibility gap, teams can use synthetic transactions or other response-time measurements, Ramachandran says. Comparing those measurements with the affected application’s transactions helps assess whether an external dependency’s behavior coincides with the slowdown.

Teams still need to check that the measurements reflect the relevant request path and workload. Synthetic checks provide evidence at the service boundary; they do not reveal the provider’s internal root cause or automatically distinguish every external delay from an internal one. Teams should also identify who owns each dependency and who can investigate when access or instrumentation stops at that boundary.

Telemetry also needs security controls. In AI workloads, prompts, responses, and retrieved documents can appear in logs and traces. Teams should decide what to collect, where that information goes, and who can access it. Design cross-layer visibility alongside existing access and data-handling policies.

## Alerting philosophy: From static dashboards to agentic copilots

As environments grow more complex, interpreting telemetry across multiple dashboards becomes difficult. Determining which metrics warrant a real-time alert versus passive monitoring is an ongoing operational challenge.

“Deciding which signals deserve an alert is where science and technology meet domain art,” Ramachandran says. “There is no magic formula. It requires encoding explicit and tacit human operational knowledge into the monitoring platform so the system understands what actually impacts user experience.”

Curated dashboards remain useful for predefined views of system behavior, while AI assistants offer another way to explore operational data. [HPE OpsRamp Software](https://www.hpe.com/us/en/products/software/opsramp-software.html) includes an AI-powered operations copilot that lets operators explore complex telemetry through natural language.

HPE describes capabilities for investigating incidents, correlating evidence, and recommending next steps. Those capabilities depend on the data available to the platform and the features enabled in the customer’s deployment.

Looking ahead, Ramachandran sees an even more fundamental change in cloud-native operations. He frames machine-led interpretation as a direction for increasingly complex environments, with safeguards still needed before operational changes.

> “We are rapidly approaching a point where the first responder to telemetry must be machine intelligence.”

“Today, human operators remain the primary first point of interpretation for telemetry,” Ramachandran tells TNS. “But as stack complexity increases with more moving parts and dynamic interactions, expecting a human to digest all these signals first becomes intractable. We are rapidly approaching a point where the first responder to telemetry must be machine intelligence.”

AI-assisted analysis and autonomous changes are separate operational decisions. Ramachandran cautions that AI outputs can be nondeterministic while IT operations often require repeatable behavior.

He recommends retaining human oversight and establishing reliable safeguards before allowing AI findings to trigger operational changes. Teams need to validate a diagnosis and confirm the effect of any response, even when an assistant helps assemble the evidence.

The foundation is instrumentation: Collect the necessary telemetry, establish workload-specific baselines and thresholds, and verify improvements against the user’s experience.

Green cluster indicators are a useful starting point, but application measurements determine whether the service delivers what users need.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)