At [KubeCon+CloudNativeCon North America](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) last month, the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) accepted the open source [KServe](https://kserve.github.io/website/) software as an incubating project.

KServe’s prominence in the [cloud native space](https://thenewstack.io/cloud-native/) illustrates how much Kubernetes has come to be a bedrock for AI computing, offering a [scalable open source platform](https://thenewstack.io/kserve-a-robust-and-extensible-cloud-native-model-server/) for enterprises to run their own generative AI and predictive work.

“The rising complexity of modern AI workloads drives an urgent need for robust, standardized [model serving platforms](https://thenewstack.io/model-server-the-critical-building-block-of-mlops/) on Kubernetes,” said TOC sponsor [Kevin Wang](https://www.cncf.io/blog/2021/01/25/maintainer-spotlight-kevin-wang-of-kubeedge-and-volcano/), in a statement. “Its focus on scalability, particularly multinode inference for large language models, is key to providing efficient serving and deployment solutions for cloud native AI infrastructure.”

The KServe development team will work through the [CNCF Graduation Criteria](https://github.com/cncf/toc/blob/main/process/graduation_criteria.md) with the goal of becoming “a fully abstracted, elastic inference platform where users solely focus on models and pre/post-processing while KServe handles the orchestration, scaling, resource management, and deployment,” according to the CNCF.

## The Origins and Evolution of KServe

What does KServe do? It defines how a model is served within an organization, providing a single API to access.

It “gives us a standard scalable way to run self-hosted models on-prem and it gives every model a stable internal endpoint that the gateway can talk to,” explained [Bloomberg](https://www.bloomberg.com/subscriptions/what-you-get/) senior engineer for AI infrastructure [Alexa Griffith](https://www.linkedin.com/in/alexa-griffith/) in a presentation at KubeCon.

[Google,](https://cloud.google.com/?utm_content=inline+mention) [IBM](https://www.ibm.com/cloud?utm_content=inline+mention), [Bloomberg](https://thenewstack.io/why-bloombergs-openapi-participation-is-important-for-the-financial-industry/), [Nvidia](https://thenewstack.io/nvidias-ai-factories-and-agentic-software-development/) and [Seldon Technologies LLC](https://www.seldon.io/about/) collectively created KServe, launching it in 2019 originally under the [KubeFlow project](https://thenewstack.io/smooth-sailing-for-kubeflow-1-9-thanks-to-cncf-red-hat-support/) (as “KFServing”).

The project was then donated to [LF AI and Data Foundation](https://lfaidata.foundation/) in 2022, and then submitted to the CNCF lasty September. In September 2022, the project rebranded from KFServing to the standalone KServe, graduating from Kubeflow. KServe then moved to CNCF as an incubator in September 2025.

The software was originally built for predictive inference, but was expanded for [LLM-based](https://thenewstack.io/introduction-to-llms/) generative AI usage when [ChatGPT caught the public’s imagination](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/). Every problem Bloomberg encountered running LLMs, it was able to use to help build in KServe support for generative AI work in KServe, Griffith said.

[![Presentation screenshot](https://cdn.thenewstack.io/media/2025/11/12686ed3-kubecon-kserve-griffith.png)](https://cdn.thenewstack.io/media/2025/11/12686ed3-kubecon-kserve-griffith.png)

Although KServe was built for predictive inference, the project “created all these new features for generative AI”–Bloomberg’s Alexa Griffith

## Understanding KServe’s Core Components

KServe actually has three components. One is the namesake **KServe Kubernetes controller**, which reconciles KServe custom resource definitions (CRDs) that define ML resources and other Kubernetes objects. The InferenceService CRD manages predictive inference, and the LLMInferenceService CRD covers the GenAI use cases.

The [ModelMesh](https://kserve.github.io/website/docs/admin-guide/modelmesh) is the management and routing layer for models, built to rapidly change out model use cases. And the [Open Inference Protocol](https://kserve.github.io/website/docs/concepts/architecture/data-plane/v2-protocol) provides a standard way, via either HTTP or [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/), to perform machine learning model inference across serving runtimes for different ML frameworks.

“On the technical front, KServe’s rich integration with Envoy, Knative, and the Gateway API anchors it powerfully within the CNCF ecosystem,” explained [Faseela K](https://www.linkedin.com/in/faseela-k-42178528/), CNCF [Technical Oversight Committee](https://www.cncf.io/people/technical-oversight-committee/) sponsor, in a statement. “The community’s welcoming nature has made it easy for new contributors and adopters to get involved, which speaks volumes about its health and inclusiveness.”

[![Marketing chart](https://cdn.thenewstack.io/media/2025/11/e8ec80e1-kserve_new.png)](https://cdn.thenewstack.io/media/2025/11/e8ec80e1-kserve_new.png)

## Key Features for Predictive and Generative AI

For predictive modeling jobs, KServe offers:

* **Multi-Framework** support, spanning [TensorFlow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/), Python’s [PyTorch](https://thenewstack.io/why-pytorch-won/) and [scikit-learn](https://scikit-learn.org/stable/), [XGBoost](https://xgboost.readthedocs.io/en/stable/), [ONNX](https://thenewstack.io/why-the-frontend-should-run-ai-models-locally-with-onnx/), and others.
* **Intelligent Routing** that understand the routing requirements for predictor, transformer, and explainer components with automatic traffic management.
* **Advanced Deployment patterns** for [Canary rollouts](https://thenewstack.io/primer-blue-green-deployments-and-canary-releases/), inference pipelines, and ensembles with [InferenceGraph](https://thenewstack.io/a-guide-to-model-composition/).
* **Autoscaling**, including scale-to-zero capabilities.

And for [generative AI](https://thenewstack.io/the-production-generative-ai-stack-architecture-and-components/) the software provides:

* **LLM-Optimized**: OpenAI-compatible inference protocol for seamless integration with large language models.
* **GPU Acceleration**: High-performance serving with GPU support and optimized memory management for large models.
* **Model Caching**: Intelligent model caching to reduce loading times and improve response latency for frequently used models.

At present, the project has 19 maintainers, along with more than 300 contributors. Over 30 companies have adopted the technology, and either contribute to the project or just use the technology. It has gathered over [4,600 GitHub stars](https://github.com/kserve/kserve).

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)