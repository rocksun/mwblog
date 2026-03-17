## Introduction: the scaling wall

In 2015, Uber’s growth was outpacing its infrastructure. As the company evolved from a luxury car service into a global logistics powerhouse, every engineering team began building their own machine learning “silos.” Data scientists were spending 80% of their time on manual “plumbing”—managing servers and data pipelines—rather than building models. The “cold start” problem was a reality: it took months to get a single model from a laptop into a production environment.

> “Data scientists were spending 80% of their time on manual ‘plumbing’—managing servers and data pipelines—rather than building models.”

**Michelangelo** was born from this chaos. It was designed to be Uber’s centralized “spine,” democratizing AI by creating a standardized, end-to-end conveyor belt for ML. But as we crossed the threshold of **30 million predictions per second** we hit a scaling wall that required a fundamental architectural shift: moving from a monolithic legacy stack to a **cloud-native Kubernetes foundation**.

![Evolution of Uber's AI platform, Michelangelo](https://cdn.thenewstack.io/media/2026/03/b57e2e6f-uber_evolutionofmichaelangelo.jpg)

## The architecture: solving the “platform reality”

Modern platform engineering isn’t just about running containers; it’s about managing the distributed state of every model Uber trains. We leveraged Kubernetes as a distributed state machine to solve these critical scaling bottlenecks.

### Scaling the control plane: high-cardinality CRDs and transparent persistence

At the volume Uber operates, a vanilla Kubernetes implementation faces significant pressure. Standard clusters rely on [ETCD](https://etcd.io/), which is optimized for small, flat key-value pairs. However, Michelangelo manages thousands of projects and models with intricate, high-cardinality relational links.

**The strategy: architectural abstraction through custom resources.** Rather than forcing a relational data model into a non-relational store, we adopted a “best-of-both-worlds” approach using advanced Kubernetes patterns:

* **100+ purpose-built CRDs:** We defined an extensive ecosystem of over 100 [Custom Resource Definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) that represent the full machine learning lifecycle. This allows us to leverage the standard Kubernetes API and controller-runtime while maintaining a rich, domain-specific data model.
* **Transparent relational persistence:** To solve the scaling limits of etcd, we engineered a storage abstraction that is entirely transparent to the user. While developers interact with standard Kubernetes objects via *kubectl* or our API, the underlying metadata is synchronized with a **horizontally scalable MySQL backend.**
* **High-efficiency reconciliation:** By mapping CRDs to an optimized relational schema, we enable complex joins and millisecond-latency filtering that are impossible in standard [Kubernetes](https://thenewstack.io/codiac-kubernetes-doesnt-need-to-be-that-complex/).

### Curing stranded compute: the federation pattern

Uber operates dozens of regional clusters. Before federation, the data scientists and engineers had to manually choose a cluster. This led to the “stranded compute” problem: Cluster A would be at 100% capacity with a massive queue, while Cluster B sat 50% empty.

The Lesson: Abstract the physical cluster. We implemented a **Unified Batch Federation Layer** using a **PropagationPolicy CRD:**

* Engineers now submit jobs to a **“Virtual Regional Cluster.”** A **Federated Controller** acts as a global traffic cop, checking real-time GPU availability across all physical zones and “stamping” the job with a target cluster.
* A zonal Clusterlet then “pulls” the [workload specification to local hardware](https://thenewstack.io/do-all-your-ai-workloads-actually-require-expensive-gpus/). This ensures a **99.9% scheduling success rate** by shifting workloads to where capacity actually exists.

### Bridging the “friction gap” with Uniflow

Even with a robust Kubernetes core, we faced the “orchestration trap”. Developers were struggling with rigid infrastructure languages to chain complex tasks like “process data → train → safety check → deploy.”

To solve this, we leverage **Uniflow**, a Python-native workflow service designed specifically for the ML lifecycle. Unlike general-purpose ETL engines, Uniflow is a “flex” workflow service that prioritizes the unique needs of model development over traditional batch data movement:

* **Python-first experience:** Data scientists author entire workflows in standard Python, eliminating the need for YAML or complex domain-specific languages.
* **Resource-aware scheduling:** Moves beyond basic CPU/GPU requests by intelligently tracking “consumable” resources and specialized hardware SKUs to prevent contention.
* **Write once, run anywhere:** Ensures code used for local debugging works identically in the global cloud, eliminating “it worked on my machine” inconsistencies.
* **Zero-touch & agentic automation:** Automates everything from model evaluation to human-in-the-loop governance.

### The Universal Compute Mesh: multi-cloud batch orchestration

In 2026, single-cloud dependency is a strategic risk. For Michelangelo, the challenge was twofold: accessing specialized hardware (like **NVIDIA H100s**) often restricted to specific regions, and leveraging **Spot Instances** across providers to keep training costs sustainable.

* **Cloud as a commodity:** By utilizing Kubernetes-native abstractions, we built a **cloud-agnostic batch processing layer** spanning on a single control plant and multiple public providers (GCP, OCI, AWS, and Azure).
* **Provider-agnostic scheduling:** Our federation layer treats a cluster in GCP identically to an Uber-owned data center. The **PropagationPolicy CRD** handles the heavy lifting, translating high-level requirements into the specific networking and storage primitives of each provider.
* **Unified data access:** We implemented a global data mesh to ensure transparency. Whether a **RayJob** runs in a local zone or a remote cloud VPC, a cloud-native solution mounts datasets and secrets securely, making cloud boundaries invisible to the ML model.

> “In 2026, single-cloud dependency is a strategic risk.”

## Impact: production reality at Uber

As of 2026, the platform manages mission-critical workloads at an unprecedented magnitude:

* **30 million+ predictions per second:** Powering real-time matching, pricing, and safety services globally.
* **40 million total trips per day:** Supporting significant growth in mobility and delivery services.
* **450 trips per second:** Seamlessly processing high-velocity data from more than 70 countries and 15,000+ cities.

## Future directions: the next operational frontier

As we scale, the “maintenance tax” of managing **100+ CRDs and dozens of specialized controllers** cannot be solved by headcount alone. Our 2026 roadmap focuses on shifting Michelangelo from a managed platform to an **autonomous, self-healing ecosystem** through three strategic pillars:

* **Self-healing debugging:** AI agents parse logs in real-time to provide instant root-cause analysis and fixes for failed jobs.
* **Agent-assisted governance:** [Intelligent CI/CD](https://thenewstack.io/introduction-to-ci-cd/) automates complex integration testing, ensuring safe, high-velocity daily deployments.
* **Zero-toil upgrades:** Automated workflows pre-validate and migrate pipelines to the latest frameworks, making library updates transparent.

*This guest column is being published ahead of [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), the Cloud Native Computing Foundation’s flagship conference, which will bring together adopters and technologists from leading open-source and cloud-native communities in Amsterdam, the Netherlands, from March 23-26, 2026.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/03/e26bd0f4-cropped-cf44fc45-ericwang_headshot-chris-howard.jpeg)

Eric Wang is a Senior Staff Software Engineer at Uber.](https://thenewstack.io/author/eric-wang/)

[![](https://cdn.thenewstack.io/media/2026/03/8033e4da-cropped-f4282ada-yingzheng_headshot_-_chris_howard.jpeg)

Ying Zheng is a Senior Staff Software Engineer at Uber.

Read more from Ying Zheng](https://thenewstack.io/author/ying-zheng/)