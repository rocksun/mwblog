When AI developer and ops teams first adopt large models on Kubernetes, the focus is usually on getting something to run. Initially, the inference service may respond correctly, latency is acceptable, and a proof of concept becomes a production endpoint. It can feel like the hard part is over.

As adoption grows, however, operations start to change. Running a model is relatively straightforward on Day 0, but operating inference infrastructure reliably across regions, unpredictable traffic patterns, and cloud providers is where Day 1 and 2 operations get complex.

To make these infrastructure challenges more concrete, let’s examine a real-world use case: event-driven incident triage and [root cause analysis](https://thenewstack.io/machine-learning-for-automated-root-cause-analysis-promise-and-pain/) (RCA). This scenario combines several characteristics that stress AI platforms simultaneously: latency sensitivity, unpredictable traffic spikes, and a low tolerance for failure.

Consider a production environment in which an on-call engineer is paged in response to a service degradation. The system aggregates logs from multiple services, inspects recent configuration changes and deployments, and correlates metrics across dependencies. An LLM-powered analysis step evaluates the collected signals and produces a structured summary proposing a likely root cause. That summary is then posted into the incident management channel for review.

> “Running a model is relatively straightforward on Day 0, but operating inference infrastructure reliably… is where Day 1 and 2 operations get complex.”

At a glance, this process appears straightforward. In practice, the pipeline depends on GPU-backed inference capacity and consistent low-latency routing across environments. The core challenge is not obtaining a single model response under ideal conditions. It is ensuring that this multi-stage, model-dependent workflow executes reliably and predictably during periods of operational stress.

## Common pain points in AI platform operations

Let’s think about some of the common pain points that teams face when operating AI platforms at scale.

### 1. Fragmented GPU Capacity

GPUs are usually added incrementally: distinct SKUs introduced from different regions and clouds, often tied to specific projects. Over time, capacity becomes scattered.

From a Kubernetes standpoint, you need a single scheduling domain. You may have idle GPUs in one cluster or region while another is saturated. Even if total capacity is sufficient, it is not fungible. Shifting workloads across regions or clouds requires external orchestration and increases operational complexity.

### 2. Inconsistent inference interfaces

Teams expose models in different ways: custom model servers, managed endpoints, or lightweight HTTP wrappers. Each approach defines its own error semantics, scaling behavior, and metrics.

For multi-stage pipelines, this creates tight coupling. Application code must handle different request formats and retry logic per model. Rather than functioning as a platform primitive, inference becomes a collection of bespoke integrations.

### 3. Batch-oriented infrastructure

GPU clusters are typically optimized for steady-state batch workloads. Event-driven inference, however, is bursty and latency-sensitive. When infrastructure is sized for predictable demand, spikes result in queueing or added latency.

Inference should be treated as a first-class, declaratively managed workload with elastic scheduling, not as an overlay on batch infrastructure.

## A Kubernetes-native pattern that scales with you

Instead, we can treat AI infrastructure as a standard cloud-native systems problem. Rather than introducing a separate control plane for models and GPUs, we extend Kubernetes primitives – declarative state, reconciliation, scheduling – to inference workloads.

A cloud-native AI architecture can be understood as three logical layers running on a shared Kubernetes control plane:

1. The model layer
2. The inference access layer
3. The compute layer

### Model layer: Declarative lifecycle management

The model layer handles lifecycle management declaratively, treating models as first-class Kubernetes resources. Several open-source projects address this, including KServe, Ray Serve, and NVIDIA Dynamo. For this architecture, we use [Kubernetes AI Toolchain Operator](https://github.com/kaito-project/kaito) (KAITO), a CNCF Sandbox project.

KAITO bundles model definition and GPU provisioning into a single custom resource. Teams define desired state, including model type, configuration, and GPU requirements, and KAITO’s controllers reconcile that state automatically. Resource requests are explicit, providing the scheduler with the information needed to place workloads predictably. By making the cluster the source of truth, KAITO removes ad hoc scripts and reduces operational risk during model or node pool updates.

### Inference access layer: Unified gateway with liteLLM

The inference access layer centralizes routing, rate limiting, and [observability across models](https://thenewstack.io/large-language-model-observability-the-breakdown/) and providers. Projects like the Kubernetes Gateway API Inference Extension, Envoy AI Gateway, and kgateway each address this problem. For this architecture, we use [liteLLM](https://docs.litellm.ai/docs/).

Rather than having multiple applications call different model servers directly, inference traffic passes through liteLLM, which provides a consistent API surface. In multi-stage pipelines, this reduces coupling between services and simplifies failure handling. Applications see a single stable endpoint while the gateway routes requests to the appropriate model version, transparently handling retries and falling back to alternative compute nodes when needed.

### Compute layer: Elastic GPU scheduling with Flex Nodes

The compute layer addresses GPU fragmentation and bursty demand. Projects like Karpenter, KubeFleet, and the Kubernetes Cluster Autoscaler take different approaches to this problem. For this architecture, we use [GPU Flex Nodes](https://github.com/Azure/AKSFlexNode).

Flex Nodes allow GPU-backed nodes from multiple clouds or regions to join a single Kubernetes cluster. Scheduling then happens within Kubernetes, using the declaratively defined resource requirements from the model layer. Workloads are placed where capacity is available, rather than being tied to a specific cloud or cluster. Ultimately, this approach improves utilization and eliminates the operational friction of managing GPUs across fragmented environments.  
![Chart showing LiteLLM AI Gateway utilizing GPU Flex Nodes.](https://cdn.thenewstack.io/media/2026/03/a479fca0-picture1-1024x609.png)

## Why this pattern fits event-driven AI

Event-driven workloads such as incident triage require rapid scale-up and predictable routing under unpredictable demand. In this architecture:

* Flex Nodes absorb spikes by provisioning GPU capacity across additional cloud or regional GPU capacity
* LiteLLM provides a stable API that routes requests consistently to the correct model
* KAITO ensures models are declaratively ready and versioned

When an alert triggers a workflow, data analysis and inference run as Kubernetes-native components. Requests pass through liteLLM and are scheduled onto available GPU nodes, even across clouds when needed. The system remains predictable because model lifecycle, routing, and compute all operate under a single control plane.

## Looking forward

Ultimately, AI workloads do not require a separate operational paradigm. By standardizing model lifecycle, inference, and GPU capacity as first-class Kubernetes primitives, teams gain declarative configuration and elastic scheduling.

> “Ultimately, AI workloads do not require a separate operational paradigm.”

With KAITO, liteLLM, and GPU Flex Nodes in a cloud native architecture, platform engineers can provide [a reliable foundation](https://thenewstack.io/temporal-durable-execution-platform/) for AI developers. Cross-cloud capacity becomes a fungible resource, allowing [workloads to scale](https://thenewstack.io/kubernetes-vpa-inplace-resize/) elastically and fail over efficiently.

Looking ahead, as clusters span multiple regions and providers, topology-aware scheduling will become increasingly valuable. Placement decisions can incorporate latency, data locality, and cost considerations, expressed declaratively in the cluster rather than embedded in application logic. This makes scaling and failover more intelligent, without departing from cloud-native, Kubernetes-driven principles.

*This guest column is being published ahead of [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), the Cloud Native Computing Foundation’s flagship conference, which will bring together adopters and technologists from leading open-source and cloud-native communities in Amsterdam, the Netherlands, from March 23-26, 2026.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/5c7d28c2-cropped-467a414e-sachi-desai.jpg)

Sachi Desai is a product manager at Microsoft, where she focuses on improving the experience of running AI workloads and customizing scheduler on Azure Kubernetes Service (AKS). She has driven features that simplify inferencing and fine-tuning of containerized models and...

Read more from Sachi Desai](https://thenewstack.io/author/sachi-desai/)