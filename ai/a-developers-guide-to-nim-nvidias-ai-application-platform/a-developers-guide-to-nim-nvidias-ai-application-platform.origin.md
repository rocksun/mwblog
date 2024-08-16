# A Developers Guide to NIM, Nvidia’s AI Application Platform
![Featued image for: A Developers Guide to NIM, Nvidia’s AI Application Platform](https://cdn.thenewstack.io/media/2024/08/d2fa3e65-getty-images-mydwapzss_k-unsplash-1024x767.jpg)
In March 2024, Nvidia [announced](https://developer.Nvidia.com/blog/Nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/) NIM (Nvidia Inference Microservices), a set of easy-to-use [microservices](https://thenewstack.io/microservices/) designed to accelerate the deployment of generative AI models across the cloud, data centers and workstations.

This series delves into NIM, exploring its key features, benefits and applications, as well as providing a comprehensive guide for developers looking to leverage this generative AI platform.

NIM is available as APIs, within the Nvidia AI Enterprise software suite and as standalone container images.

## What is Nvidia NIM?
NIM stands for Nvidia Inference Microservices, which means this is an offering meant for performing inference on generative AI models. When it was announced, NIM was only available as a [set of APIs for developers](https://thenewstack.io/developers-get-ready-for-nvidias-nim-based-ai-app-store/). NIM is also a part of Nvidia AI Enterprise, which is built on infrastructure software from [VMware](https://tanzu.vmware.com?utm_content=inline+mention) and [Red Hat](https://www.openshift.com/try?utm_content=inline+mention). Recently, Nvidia has started to publish and maintain container images that are deployable locally on developer workstations and servers with Nvidia GPUs.

So, NIM is available as APIs, within the [Nvidia AI Enterprise software suite](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/) *and* as standalone container images.

Let’s take a look at each of these to understand them better.

## Nvidia NIM API
The [Nvidia NIM API](https://build.Nvidia.com/explore/discover) is a set of industry-standard APIs that enables developers to deploy AI models with ease, using just a few lines of code. Available as serverless inference endpoints, the NIM API provides a secure, streamlined path for iterating and building generative AI solutions.

The NIM API is built on a robust foundation, including inference engines like [Triton Inference Server](https://developer.Nvidia.com/triton-inference-server), [TensorRT](https://developer.Nvidia.com/tensorrt-getting-started), [TensorRT-LLM](https://docs.Nvidia.com/tensorrt-llm/index.html) and [PyTorch](https://pytorch.org/). This architecture facilitates seamless AI inferencing at scale, allowing developers to consume state-of-the-art foundation models and fine-tuned models without worrying about the infrastructure.

The NIM API is compatible with OpenAI, allowing developers to leverage the power of OpenAI’s models and tools within their applications. Developers can use standard HTTP REST clients or OpenAI client libraries to consume the NIM API.

The NIM API provides several API endpoints that enable developers to interact with AI models, including:

**Completions endpoint**: This allows developers to generate text completions based on a given prompt.**Embeddings endpoint**: This enables developers to generate text embeddings for a given input text.**Retrieval endpoint**: This allows developers to retrieve relevant documents based on a given query.**Ranking endpoint**: This enables developers to rank a list of passages or documents based on their relevance to a given query or prompt.
The NIM API has tight integration with popular LLM orchestration tools such as LangChain and LlamaIndex. Developers can easily build basic chatbots, AI assistants, retrieval augmented generation (RAG) applications and advanced applications based on agents.

Developers can get started with the NIM API by visiting the Nvidia API Catalog, where they can find documentation, API reference information and release notes. To use the NIM API, developers need to obtain an API key, available by joining the Nvidia Developer Program. There is a playground to explore models, prompts, parameters and responses. When developers sign up with NIM, they each receive 5,000 credits, with each credit corresponding to one inference call.

Nvidia NIM is quickly becoming the choice of developers to access the latest generative AI models. Recently, when [Google](https://cloud.google.com/?utm_content=inline+mention) [launched](https://developers.googleblog.com/en/smaller-safer-more-transparent-advancing-responsible-ai-with-gemma/) Gemma 2 2B LLM, it made it available on NIM along with Hugging Face and Kaggle. Going forward, you can expect other model providers to offer their models on the Nvidia NIM inference platform.

I will explore the NIM API in detail in an upcoming tutorial in this series.

## Nvidia NIM Within Nvidia AI Enterprise
[Nvidia AI Enterprise](https://www.Nvidia.com/en-in/data-center/products/ai-enterprise/) is a comprehensive, cloud native software platform that accelerates data science pipelines and streamlines development and deployment of production-grade copilots and other generative AI applications. As part of this platform, Nvidia NIM is a set of easy-to-use inference microservices that enable developers to deploy foundation models on any cloud or data center while keeping their data secure.
The software layer of the Nvidia AI platform, Nvidia AI Enterprise, accelerates the data science pipeline and streamlines the development and deployment of production AI — including generative AI, computer vision, speech AI and more. With over 100 frameworks, pretrained models, development tools and microservices, Nvidia AI Enterprise is designed to accelerate enterprises to the leading edge of AI while also simplifying AI to make it accessible to every enterprise.

Nvidia NIM is a critical component of the Nvidia AI Enterprise platform, providing optimized model performance with enterprise-grade security, support and stability. With NIM, developers can deploy AI models with ease, using just a few lines of code. This enables them to focus on building enterprise applications while Nvidia handles the complexities of AI model deployment.

The Nvidia AI Enterprise platform can be deployed on systems like Nvidia DGX, certified hardware from Nvidia partners, and public cloud environments like [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Azure](https://news.microsoft.com/?utm_content=inline+mention) and GCP.

## Nvidia NIM as Self-Hosted Container
For developers who do not have access to Nvidia AI Enterprise, NIM is available as a self-contained image that can be deployed using [Docker](https://www.docker.com/?utm_content=inline+mention) or [Kubernetes](https://roadmap.sh/kubernetes).

NIM abstracts model inference internals, including runtime operations and the execution engine. They are also the most efficient option available, regardless of whether they are used with [TRT-LLM](https://github.com/Nvidia/TensorRT-LLM), [vLLM](https://docs.vllm.ai/en/latest/) or a similar inference engine.

NIMs are packaged as container images for each model or model family. Each NIM is its own Docker container with a specific model, such as `meta/llama3-8b-instruct`
. These containers come with a runtime that works on any Nvidia GPU with enough memory, but some model/GPU combinations work better than others. Utilizing any local filesystem cache that is available, NIM automatically downloads the model from Nvidia’s NGC catalog. Because each NIM is built on the same base image, downloading additional NIMs is extremely fast.

To get started with Nvidia NIM, pull the NIM container from the Nvidia Docker Registry and run it using the `docker run`
command on a GPU machine configured with Docker and the Nvidia Container Toolkit. To access the NIM API, generate an API key from the Nvidia GPU Cloud and use the `docker login`
command to authenticate with the Nvidia Container Registry. Finally, launch the NIM container using the `docker run`
command, specifying the container name, repository and tag.

Once the container is running, you can validate the deployment by executing an inference request using the `curl`
command. Additionally, you can use the OpenAI Python API library to send requests to the NIM API. By following these steps, you can easily deploy and use Nvidia NIM on your system.

When NIM is first deployed, it inspects the local hardware configuration and the available optimized model in the model registry before automatically selecting the best version of the model for the available hardware. NIM downloads the optimized TensorRT (TRT) engine and runs inference using the TRT-LLM library on a subset of supported GPUs. For other GPUs, NIM downloads an unoptimized model and runs it with the vLLM library.

By offering a flexible suite of microservices through APIs, integration with Nvidia AI Enterprise and self-hosted container images, NIM provides developers with a robust, scalable and secure platform for AI inference.

What I like about NIM containers is that they are capable of running on consumer-grade GPUs such as [GeForce RTX 4090](https://www.Nvidia.com/en-in/geforce/graphics-cards/40-series/rtx-4090/), giving developers a chance to quickly prototype applications on accessible and affordable hardware. In the following parts of this series, I will explore how to deploy NIM locally and build applications that consume the API.

## Summing Up
Nvidia NIM represents a significant advancement in the deployment and utilization of generative AI models. By offering a flexible suite of microservices through APIs, integration with Nvidia AI Enterprise and self-hosted container images, NIM provides developers with a robust, scalable and secure platform for AI inference. Whether leveraging cloud infrastructure or local GPU resources, NIM simplifies the complexities of AI model deployment, enabling rapid development and iteration of AI applications. As I continue this series, I will delve deeper into each aspect of Nvidia NIM, providing detailed guidance and tutorials to help developers maximize the potential of this powerful platform.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)