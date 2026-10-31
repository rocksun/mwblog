**A Kubernetes cluster can be healthy while the AI service running on it disappoints users.** A model might return its first token quickly but take too long to finish an answer. It might respond promptly and still give the wrong answer. And a busy GPU tells the operations team little about either outcome. The operational challenge is connecting AI service behavior with the Kubernetes, GPU, compute, storage, and network conditions behind it—not viewing each layer in isolation.

That’s why you should measure an inference service before production, then compare live behavior with the baseline. In the fourth article in this HPE-sponsored series on AI and Kubernetes, *The New Stack* speaks with [Marius Bogoevici](https://www.linkedin.com/in/marius-bogoevici), Senior Principal Product Manager for HPE Morpheus Software; [Mahesh Ramachandran](https://www.linkedin.com/in/ramachandranm/), Vice President of Product Management for [HPE OpsRamp Software](https://www.hpe.com/us/en/products/software/opsramp-software.html); and [Karthik Subramanian](https://www.linkedin.com/in/karthik-subramanian-lnkd/), Principal Product Manager for [HPE Morpheus Software](https://www.hpe.com/us/en/products/software/morpheus-software.html).

Inference adds a further question: Does the whole service deliver a useful result at a cost and speed the business can support?

*Earlier in this series:*

## **Start with the experience, then establish a baseline**

For a conversational service, Bogoevici recommends measuring time to first token, time per output token, reliability, capacity, resource efficiency, cost, and answer quality. The right mix depends on the experience a team intends to deliver. A quick first token can mask slow subsequent generation; a fast complete response can still be inaccurate or unhelpful.

> “A quick first token can mask slow subsequent generation; a fast complete response can still be inaccurate or unhelpful.”

Time to first token and time to a complete response answer different questions. Inter-token latency and time per output token help explain generation speed after the first token arrives. Teams should document where they measure each interval and compare results under sustained load and demand spikes. Set targets for the particular workload and user experience.

Ramachandran urges teams to profile the AI serving system before customers depend on it. Test representative prompt and context lengths, output volumes, and traffic levels. Record token throughput, latency, and service-level measures under those conditions. The resulting baseline gives operators a reference to measure  production behavior changes.

Correlating those workload measures with infrastructure performance and capacity helps teams distinguish rising inference demand from resource contention and plan capacity more effectively. As Ramachandran tells *The New Stack*, teams should “profile it before you launch.”

Quality needs its own evaluation. Bogoevici says teams should ask whether the service gives proper answers or hallucinates. Platform telemetry can show a request was served, but data science and domain specialists need representative tests and acceptance criteria for the answer.

The newly published ebook, [*Kubernetes in 2027: Building platforms for AI, autonomy, and scale*](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/), recommends assessing output quality alongside service performance and revisiting both after model, prompt, retrieval, or serving changes.

## **When the GPU is busy but the service is slow**

GPU utilization is a useful signal, but it [does not identify the bottleneck](https://www.hpe.com/us/en/newsroom/blog-post/2026/02/the-next-bottleneck-in-enterprise-ai-isnt-compute-its-context.html). Bogoevici sketches a misleading victory lap: “Our GPUs are maxed at 100%. So we’re doing well.” That tells teams little about how the service actually performs. Ramachandran suggests checking whether inference pods scale on workload-appropriate metrics, whether requests reach the intended model, and whether related components can be scheduled when needed. Different models can have different latency and capacity demands, so a change in request mix can change the user experience even while GPU activity looks normal.

> Bogoevici sketches a misleading victory lap: “Our GPUs are maxed at 100%. So we’re doing well.”

Subramanian adds dependencies around the model: network configuration and database or vector-database response time. He raises another question: “Is the GPU partition too small to serve that model?” These are investigation paths, not a diagnosis that applies to every deployment. Teams should correlate them with the affected requests and time window before choosing a fix.

Kubernetes’ [Horizontal Pod Autoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) can use configured custom or external metrics, so teams do not have to replace it simply because CPU utilization is a poor trigger for inference. They do need to supply and test the metrics pipeline, scaling bounds, and available accelerator capacity for their serving stack. A scaling policy cannot make additional GPU capacity appear instantly.

## **What HPE Morpheus and OpsRamp contribute**

HPE describes [HPE](https://www.hpe.com/us/en/products/software/morpheus-software.html) [Morpheus Software](https://www.hpe.com/us/en/products/software/morpheus-software.html) as a platform for governed provisioning and automation across hybrid environments. Its Advanced and Enterprise versions include [HPE Kubernetes Service (HKS)](https://developer.hpe.com/blog/hpe-morpheus-enterprise-software-enhances-its-kubernetes-service-with-new-features/); Enterprise extends the operating model across hybrid and public-cloud environments. Platform teams can use catalog items, blueprints, access controls, and approvals to define how they request and manage supported environments. This gives platform teams a consistent way to deliver governed self-service and manage VMs and Kubernetes clusters together, reducing separate tooling and manual handoffs. Those capabilities alone do not benchmark a model or decide whether its answers are good.

[HPE OpsRamp Software](https://www.hpe.com/us/en/products/software/opsramp-software.html) provides full-stack observability and monitoring across multi-vendor hybrid infrastructure and applications, with service maps, AI-powered event correlation, and operational automation to help teams understand dependencies and move from detection to resolution. Ramachandran describes HPE Morpheus as the provisioning engine and OpsRamp as the observability engine in HPE’s broader cloud operations approach.

Ramachandran says HPE’s combined solution includes Morpheus, OpsRamp and runtimes. He says it can measure token service rates in a model-serving environment and token request rates in an agentic workload. HPE is extending OpsRamp’s AI workload observability to connect model and agent activity, token volumes, token serving rates, inference latency, and time to first token with supporting infrastructure telemetry.

The operational value is the correlation: teams can investigate whether slow responses originate in the application, model-serving layer, or infrastructure, while using workload demand to inform capacity planning and cost accountability. For a specific deployment, teams should confirm which component emits each metric, how it is collected, and what additional application instrumentation is needed.

For agentic applications, HPE’s planned observability enhancements extend that context to AI traces, tool calls, errors, and quality signals alongside Kubernetes, CPU, GPU, memory, storage, and network telemetry. Lightweight eBPF and OpenTelemetry-based instrumentation are also planned to deepen visibility while minimizing collection overhead. These signals support investigation; they do not replace domain-specific answer evaluation or security controls.

As the preceding [article in this series](https://thenewstack.io/kubernetes-hidden-latency-telemetry/) explains, collecting telemetry across a stack depends on deployed agents, integrations, permissions, and application instrumentation. For an inference service, connect user-facing measurements with model-server metrics and traces, Kubernetes events, and relevant network, database, and accelerator signals. Check where visibility stops, especially at an external model or service boundary.

## **Plan for AI-specific routing and scheduling**

Looking toward 2027, Ramachandran urges teams to examine autoscaling, model routing and scheduling as deliberate design choices for AI workloads. He discusses content-aware request routing, co-scheduling related components, and disaggregated serving. These are areas to evaluate for a specific architecture, not features that every Kubernetes installation or HPE product provides automatically.

An [experimental Gateway API proposal](https://gateway-api.sigs.k8s.io/geps/gep-5224/) describes pre-routing filters and cites the Inference Extension’s Body-Based Router as an example. That router can extract a model name from a request body for use in routing, but teams need a compatible implementation and configuration. They should measure any latency or efficiency benefit from routing and scheduling choices with their own models, traffic, and hardware.

## **Protect telemetry and share the launch decision**

Inference observability also has a data-handling problem. Bogoevici warns that prompts, responses, and retrieved documents may appear in logs and traces. He asks, “What information is actually captured and where does it go?” Teams should decide what to collect, where to store it, how long to retain it, and who can see it. He stresses a simple point: prompts are data. Sensitive content needs protection even when teams collect it for troubleshooting.

Ramachandran sees operations and security observability moving closer together as AI agents introduce new events and access records. He says OpsRamp is preparing to interpret existing telemetry from a security perspective, while agent-specific activity may require additional instrumentation. Teams still need to design and test their security controls and incident response.

Before launch, Ramachandran recommends that business and IT stakeholders agree on the value the service should deliver, including a [plausible inference volume tied to a business outcome](https://developer.hpe.com/blog/tokenomics-understanding-the-economics-of-enterprise-ai/). “There has to be measurable business value,” he says.

> “The goal is not simply busy GPUs, but reliable AI services with performance and resource use aligned to business needs.”

Subramanian makes the sign-off point plainly: “It can’t be a single person.” Platform administrators, machine learning and data science teams, and security teams need to work together and plan for failures or attacks. Add the relevant business owner, test representative load and failure cases, and record the capacity, quality, cost, and recovery evidence behind the decision.

A launch decision should rest on evidence that the service can meet agreed user and business targets and that the responsible teams know what to measure and how to respond when it cannot. After launch, continue comparing AI workload behavior with infrastructure conditions so teams can detect regressions, troubleshoot across layers, and adjust capacity as demand changes. The goal is not simply busy GPUs, but reliable AI services with performance and resource use aligned to business needs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)