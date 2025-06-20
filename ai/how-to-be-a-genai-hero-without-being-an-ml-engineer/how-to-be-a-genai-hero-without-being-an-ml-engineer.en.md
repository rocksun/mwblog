*Vishnu Kammari also contributed to this article.*

Generative AI (GenAI) is rapidly becoming a cornerstone of modern business strategies, with many organizations actively integrating AI capabilities into their software and workflows. While enterprises are pushing forward with proofs of concept (PoCs), specialized expertise is often needed to turn these into production workloads, creating hurdles in advancing beyond initial implementation.

## Choosing an AI Stack: Overwhelming, Time-Consuming

The fast-paced evolution of AI — driven by new techniques, improved models, cutting-edge GPUs and open source innovations — adds another layer of complexity. Organizations must constantly reassess their AI stacks to avoid relying on outdated technologies. For example, Meta’s frequent releases of the [Llama models](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/) present both opportunities for innovation and challenges in keeping up with the latest versions during evaluations and fine-tuning.

Beyond model selection, organizations face the daunting task of efficiently managing high-cost GPU compute resources. Decisions around purchasing, scaling and optimizing these assets have become critical in navigating the GenAI landscape. With these factors at play, organizations must continuously refine their strategies to balance innovation with practicality.

There are distinct differences in how organizations approach their AI journey, from small-scale users operating 1–10 bare metal instances to enterprises running massive GPU clusters to develop next-generation [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/).

Organizations that manage large-scale clusters and train cutting-edge LLMs tend to stay ahead of industry advancements, efficiently optimizing infrastructure through strategic investments in tools and techniques. Most importantly, they have specialized machine learning (ML) engineers focused on GenAI methodologies. On the other hand, businesses looking to apply GenAI in practical use cases, such as consuming existing LLMs, often seek guidance from cloud providers or system integrators to navigate best practices, efficient techniques and foundational steps.

Take, for example, a major insurance provider working on a PoC for an AI-powered customer service chatbot. By leveraging historical customer interactions, it aimed to reduce resolution times and enhance support quality. However, determining the right fine-tuning approach, selecting the ideal model, integrating with MLOps pipelines and optimizing GPU usage presented complex challenges that required careful consideration and months of research to get started. Even the decisions of [choosing GPU types](https://thenewstack.io/ebooks/cloud-infrastructure/developers-guide-to-cloud-infrastructure-efficiency-and-sustainability/) ideal for this scenario and future growth, plus concerns about how to scale and manage this infrastructure, added months of time, slowing down the project.

Scenarios like these are common across industries, leading us to turn to the [world of open source](https://thenewstack.io/open-source/) to build a new solution to help streamline the deployment process for different use cases.

## How Open Source Solutions Can Cut Deployment Time

After months of work identifying several scenarios, recurring use cases and patterns for GenAI applications, we released [OCI AI Blueprints](http://www.oracle.com/application-development/ai-blueprints/?source=:ex:pw:::::TNS_OCIAIBlueprints_C&SC=:ex:pw:::::TNS_OCIAIBlueprints_C&pcode=). This free-to-use, no-code deployment platform is built on Kubernetes packaging Oracle best practices, default infrastructure and ML application layer configurations as a single deployment manifest file.

Each blueprint manifest is tailored to a common GenAI implementation scenario. Instead of manually stitching together traditional [Terraform](https://thenewstack.io/how-to-use-terraforms-for_each-with-examples/) for infrastructure and Kubernetes YAML manifests for software configurations while choosing between libraries, using a blueprint brings the elements needed to get you up and running in a matter of minutes with a single click within the platform.

However, launching a new AI application on a GPU is just a first step. Managing the infrastructure dependencies efficiently can be stressful, especially when new workloads scale unexpectedly. This requires end-to-end observability and cluster management capabilities to consolidate software stack configuration and infrastructure dependency decisions in a single control plane.

The control plane deployed by OCI AI Blueprints is a provider set that understands configurations related to multiple open source software components like Prometheus, KEDA and KubeRay, as well as OCI-related infrastructure configurations like File Storage Service (FSS) that make up the deployment manifest file. A developer no longer needs to manually incorporate FSS as part of their ML application deployment, since the control plane has the logic to understand and create one without touching the OCI Console.

For example, LLM serving, which involves deploying pre-trained language models to handle inference requests in production environments, is an everyday use case for chatbots. Researching software platforms to choose, what hardware is optimal, what [Kubernetes](https://thenewstack.io/kubernetes/) configurations are needed, etc., can require weeks of evaluations. The following OCI AI Blueprint deployment manifest has infrastructure components, replication settings using KEDA and Prometheus-based scale settings, vLLM code and LLM Inference server integration and an LLM. All in a single deployment manifest, making it easy and straightforward.

We had a customer who used this inference recipe to quickly spin up GPU nodes and deploy multimodal LLMs for document and image batch processing use cases for its business process management platform. Previously, the process had taken weeks, but an open source, no-code solution enabled its team to fully automate the entire process and achieve success in a few days. Also, with autoscaling and shared storage deployed and managed through this blueprint, GPU resource utilization was optimized for this batched inference scenario.

Thanks to open source tools, you don’t need to be an ML engineer or have specialized expertise to get these blueprints up and running. These blueprints are packaged and simplified to deploy through a dedicated OCI AI Blueprints platform, yet flexible enough for a developer to use API-based deployments.

*Learn more about [OCI AI Blueprints](http://www.oracle.com/application-development/ai-blueprints/?source=:ex:pw:::::TNS_OCIAIBlueprints_C&SC=:ex:pw:::::TNS_OCIAIBlueprints_C&pcode=) or visit the [GitHub repository](https://github.com/oracle-quickstart/oci-ai-blueprints) to get started.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/8702bb1e-amar-gowda.jpg)

Amar is a senior principal product manager leading AI strategy and incubation initiatives for Oracle Cloud Infrastructure (OCI). Amar is an expert in High Performance Computing (HPC), GPUs, Generative AI, and Kubernetes.

Read more from Amar Gowda](https://thenewstack.io/author/amar-gowda/)

[![](https://cdn.thenewstack.io/media/2025/06/d363623b-maywun-wong.jpg)

Maywun Wong is the Director of Product Marketing for Oracle Cloud Infrastructure, focusing on Application Development. She has worked in marketing, product management, and engineering for technology and cloud companies of all sizes, including Cisco, Nokia, Siebel, Motorola, and AT&T....

Read more from Maywun Wong](https://thenewstack.io/author/maywun-wong/)