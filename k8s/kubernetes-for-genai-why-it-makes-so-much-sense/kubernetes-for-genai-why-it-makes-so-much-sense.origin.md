# Kubernetes for GenAI: Why It Makes So Much Sense
![Featued image for: Kubernetes for GenAI: Why It Makes So Much Sense](https://cdn.thenewstack.io/media/2024/06/b26282f2-kubernetesforgenai-1024x576.jpg)
[Generative AI (or GenAI)](https://thenewstack.io/ai/) is quickly evolving, becoming essential to many organizations. It’s moved beyond simple prediction to enhancing applications with code completion, automation, deep knowledge and expertise. Whether your use case is web-based chat, customer service, documentation search, content generation, image manipulation, infrastructure troubleshooting or countless other functions, GenAI promises to help us become more efficient problem solvers.
[Kubernetes](https://thenewstack.io/kubernetes/), which recently marked [its 10th birthday](https://www.dell.com/community/en/conversations/developer-blog/a-big-toast-celebrating-kubernetes-10th-birthday/6663114a1980ce7ac8c15e7e), offers valuable features for running GenAI workloads. Over the years, Kubernetes and the cloud native community have been improving, integrating and automating numerous infrastructure layers to make the lives of admins, developers and operations professionals easier.
GenAI can take advantage of this work to build frameworks that work well on top of Kubernetes. For example, the [Operator Framework](https://operatorframework.io/) is already being used to adopt GenAI within Kubernetes, as it allows building applications in an automated and scalable way.

Let’s look a little deeper at why Kubernetes makes a great home for building GenAI workloads.

## Why Generative AI on Kubernetes Makes Sense
[Kubernetes](https://roadmap.sh/kubernetes) provides building blocks for any type of application. It provides workload scheduling, automation, [observability](https://thenewstack.io/10-ways-kubernetes-observability-boosts-productivity-cuts-costs/), persistent storage, security, networking, high availability, node labeling and other capabilities that are crucial for GenAI and other applications.
Take, for instance, making a foundational GenAI model like [Google](https://cloud.google.com/?utm_content=inline+mention)‘s Gemma or Meta’s Llama2 available to worker nodes with graphics processing units (GPUs). Kubernetes’ built-in [Container Storage Interface (CSI)](https://thenewstack.io/how-the-container-storage-interface-csi-boosts-cloud-native-devops/) driver mechanisms make it much simpler to expose persistent shared storage for a model so that inference engines can quickly load it to the GPU’s core memory.

Another example is running a [vector database like Chroma](https://github.com/amikos-tech/chromadb-chart) within a [retrieval-augmented generation (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/) pipeline. Databases often need to remain highly available, and Kubernetes’ built-in scheduling capability coupled with CSI drivers can enable vector databases to move to different workers in the Kubernetes cluster. This is critical in case of node, network, zone and other failures, as it keeps your pipelines up and running with access to the embeddings.

Whether you’re looking at observability, networking or much more, Kubernetes is a suitable place for GenAI applications because of its “batteries included” architecture.

## Enabling GPUs on Kubernetes
Upstream Kubernetes supports managing [Intel](https://www.granulate.io?utm_content=inline+mention), [AMD](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention) [and NVIDIA GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/) through its [device plugin framework](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/), as long as an administrator has provisioned and installed the necessary hardware and drivers to the nodes.

This, along with third-party integrations via plugins and operators, sets up Kubernetes with the essential building blocks needed for enabling GenAI workloads.

Vendor support, such as the [Intel Device Plugins Operator](https://operatorhub.io/operator/intel-device-plugins-operator) and [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html), can also help simplify administrative overhead. For instance, the NVIDIA GPU Operator helps manage the driver, [CUDA](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/) runtime and [container toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) installation and life cycle without having to perform them separately.

## Deploying Models and Inference Engines
Enabling GPUs on a Kubernetes cluster is only a small part of the full GenAI puzzle. GPUs are needed to run GenAI models on Kubernetes; however, the full infrastructure layer includes other elements such as shared storage, [inference](https://infohub.delltechnologies.com/en-us/l/design-guide-generative-ai-in-the-enterprise-inferencing/what-is-inferencing-1/) engines, serving layers, embedding models, web apps and batch jobs that are needed to run a GenAI application.

Once a model is trained and available, the model needs to be downloaded and pulled into the Kubernetes environment. Many of the foundation models can be [downloaded from Hugging Face](https://huggingface.co/models), then loaded into the serving layer, which is part of the inference server or engine.

An inference engine or server, such as [NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/getting_started/quickstart.html) and [Hugging Face Text Generation Interface](https://github.com/huggingface/text-generation-inference) (TGI), is made up of software that interfaces with pretrained models. It loads and unloads models, handles requests to the model, returns results, monitors logs and versions, and more.

Inference engines and serving layers do not have to be run on Kubernetes, but that’s what I will focus on here. You can deploy Hugging Face TGI to Kubernetes via [Helm](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/), a Kubernetes application package manager. This [Helm chart from Substratus AI](https://github.com/substratusai/helm/tree/main/charts/text-generation-inference) is an example of how to deploy and make TGI available to a Kubernetes environment using a simple configuration file to define the model and GPU-labeled nodes.

## Data and Storage
Several types of data storage are required for running models and GenAI architectures, outside of the raw [datasets](https://huggingface.co/datasets) that are fed into the training process.

For one, it is not realistic to replicate [large language models (LLMs)](https://thenewstack.io/llm/), which can be gigabytes to terabytes in size, after they’re downloaded to an environment. A better approach is using shared storage, such as a performant shared file system like a Network File System (NFS). This enables a model to be loaded into shared storage and mounted to any node that may need to load and serve the model on an available GPU.

Another potential use case for data storage is running a RAG framework to supplement running models with external or more recent sources. RAG frameworks often use vectorized data and vector databases, and a block storage-based Persistent Volume (PV) and Persistent Volume Claim (PVC) in Kubernetes can improve availability of the vector database.

Lastly, the application utilizing the model may need its own persistence to store user data, sessions and more. This will be highly dependent on the application and its data storage requirements. For example, a chatbot may store a specific user’s recent prompt queries to save the history for lookback.

## RAG Frameworks
Another deployment scenario is implementing RAG or a context augmentation framework using tools such as [LlamaIndex](https://docs.llamaindex.ai/en/stable/) or [Langchain](https://python.langchain.com/v0.2/docs/tutorials/rag/). Deployed foundational models are typically trained on datasets at a point in time, and RAG or context augmentation can add additional context to an LLM. These frameworks add a step in the query process that can take newly sourced data and feed it and the user query to the LLM.

For example, a model trained on a company’s documents can implement a RAG framework to add newly sourced documents created after the model was trained to add context for a query. Data in a RAG framework is usually loaded and then processed into smaller chunks (called vectors) and stored in [embeddings](https://huggingface.co/blog/getting-started-with-embeddings) within [a vector database](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/), such as [Chroma](https://github.com/amikos-tech/chromadb-chart), [PGVector](https://github.com/pgvector/pgvector) or [Milvus](https://milvus.io/). These embeddings can represent diverse types of data including text, audio and images.

RAG frameworks can retrieve relevant information from the embeddings, and the model can use them as additional context in its generative response. Vector data is often more condensed and smaller than the model, but it can still benefit from using persistent storage.

Using [Kubernetes to run stateful workloads is nothing new](https://dok.community/community/), Existing projects such as Postgres can add the PGVector extension to a [Postgres cluster deployed via CloudNativePG using a PVC](https://github.com/cloudnative-pg/cloudnative-pg/blob/v1.23.1/docs/src/samples/cluster-pvc-template.yaml). PVCs enable high availability of persistent locations for databases, which allow data to move around a Kubernetes cluster. This can be important for the health of the RAG framework in case of failures or pod life cycle events.

## Conclusion
Kubernetes provides a GenAI toolbox that supports compute scheduling, third-party operators, storage integrations, GPU enablement, security frameworks, monitoring and logging, application life cycle management and more. These are all considerable tactical advantages to using Kubernetes as a platform for GenAI.

In the end, using Kubernetes as the platform for your GenAI application extends the advantages it provides for operators, engineers, DevOps professionals and application developers to the deployment and usability of GenAI infrastructure and applications.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)