# Developers: Get Ready for NVIDIA’s NIM-Based AI App Store
![Featued image for: Developers: Get Ready for NVIDIA’s NIM-Based AI App Store](https://cdn.thenewstack.io/media/2024/06/f8ada841-and-machines-1cnbglqibui-unsplash-1024x724.jpg)
[NVIDIA GPUs](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/) are now being received with the same enthusiasm as Apple iPhones. And just as the iPhone led to the rise of mobile app development, NVIDIA is increasingly providing development tools to access [AI apps](https://thenewstack.io/llm-app-ecosystem-whats-new-and-how-cloud-native-is-adapting/) on its GPUs.
Also like Apple, NVIDIA is looking to consolidate its early AI hardware domination with a series of software moves — including the creation of an AI app store.
The pathway to an AI app marketplace goes through NVIDIA’s NIM (NVIDIA Inference Microservices), which became widely available this month.
NVIDIA’s GPUs are everywhere, and like iPhones, won’t go away anytime soon. NVIDIA shipped 98% of data center GPUs in 2023, most of which were for AI, according to
[research from TechInsights](https://www.techinsights.com/blog/google-third-largest-designer-data-center-processors-2023-without-selling-single-chip).
NVIDIA CEO Jensen Huang’s vision is to create an AI marketplace where creators can set up their own models on video, image, voice and text, which then blend into other models. Creators can download LLMs or other AI models, then use Python or other scripting languages to create AI apps — which they can then sell to customers.
The pathway to this marketplace goes through
[NVIDIA’s NIM](https://developer.nvidia.com/blog/nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/) (NVIDIA Inference Microservices), which the company introduced in March at the company’s GPU Technology Conference, and became widely available this month.
## What Is a NIM?
A NIM is a virtualized container that serves AI services by utilizing a portion of the hardware capacity of NVIDIA’s GPUs.
NIM is an opening act in NVIDIA’s plan to create an AI app store, with everything running on NVIDIA’s chips. It is a virtualized container — much like CPU-based
[virtual machines](https://thenewstack.io/container-or-vm-how-to-choose-the-right-option-in-2023/) for general-purpose applications — that serves AI services by utilizing a portion of the hardware capacity of NVIDIA’s GPUs.
The downloaded containers can host pre-trained proprietary and open source large language models. It can also use RAG (
[Retrieval Augmented Generation](https://thenewstack.io/retrieval-augmented-generation-for-llms/)) to augment downloaded AI services with knowledge hosted in local documents, which allows companies to create their own unique services.
A NIM can be as simple as a chatbot that provides answers about a company’s services, or as complex as implementing comprehensive security plans to protect AI data from theft or poisoning.
## What
** Will an AI Marketplace Look Like?**
NVIDIA’s ultimate goal is to create an AI economy with storefronts selling their digital intelligence wares; in this case, based on NIMs. The AI assets will be secure in containers, with NVIDIA providing the hooks for collaborations and trustworthy connections between buyers and sellers.
The containers will be downloadable — but of course, you will need NVIDIA hardware.
The containers will be downloadable — but of course, you will need NVIDIA hardware. NVIDIA is following Apple’s blueprint. It will use software strategies like NIM to sell more hardware, and to lock down customers to its proprietary hardware.
Nvidia executives in the past have
[communicated its intent](https://www.hpcwire.com/2024/04/02/nvidia-exec-secure-ai-economies-could-help-everyone-profit/) to create an AI marketplace.
“Nvidia NIM gives enterprises a fast path to deploying efficient, optimized AI. Nvidia is working with our broad partner ecosystem to provide dozens of models from open source and enterprise providers as NIM microservices,” Erik Pounds, senior director for AI software at Nvidia, told The New Stack.
Nvidia is going beyond its own marketplace — it also is publishing its microservices on partner marketplaces, as it has with the Llama-3 NIM available on Hugging Face.
“NIM microservices based on our partners’ models serve AI use cases across the enterprise and industries such as healthcare and robotics,” Pounds said.
Companies will be able to create smaller proprietary AI assets instead of full-blown multimodal models that support text, video, voice, and images. Those containers can be linked to other NIM assets through APIs and plugins.
Trend Micro
[recently announced](https://www.darkreading.com/cloud-security/trend-micro-nvidia-partner-to-secure-ai-data-centers) that it is porting its AI-powered security software to NIMs, which will be made available to customers. They can send an API request to Trend Micro’s AI services — which include real-time security analysis and threat mitigation — and retrieve the necessary information or request actions.
NVIDIA offers a camera tracking NIM from its storefront to Pegatron, which will use it for worker safety. The company is also inviting customers to add their own NIMs to the storefront.
## What Developers Need to Know About NIMs
Developers can select their own NIM containers, which could include pre-trained proprietary and open source large language models, stored in a container built on top of Kubernetes.
Developers can select the programming tools of their choice.
For example, NVIDIA offers a container with Meta’s Llama-3 model with 70 billion parameters. Developers can enhance the NIM by adding their own corpus of knowledge from databases into the base model and improve the AI container to fit specific needs. Developers can create workflows that interconnect NIMs for data, images, video, and sound.
Developers can select the programming tools of their choice. The container — more of a black box — includes NVIDIA’s proprietary software and AI framework, NeMo Retriever, and the Triton Inference Server.
But don’t worry, you can use open source when working with NIMs. The NVIDIA stack also uses standard industry APIs for speech, text, images, and video. Each NIM has dependencies, drivers, and runtimes, with dependencies on deep learning frameworks such as TensorFlow and PyTorch verified when the Docker container is built.
For example, NIM could understand the languages used for SAP and ServiceNow, and retrieve some information from their platforms. NVIDIA’s point with NIM is that you’ll get faster results with AI and GPUs, compared to the CPUs and regular querying systems used today.
NIMs can work together to understand structured and unstructured data from all data types to generate and deliver end results. The NVIDIA software stack retrieves information from the database and converts it to conversational data.
“Once you create it, you can talk to it.”
– Nvidia CEO Jensen Huang
“Essentially take structured data or unstructured data, you learn its meaning, you encode its meaning. So now this becomes an AI database,” Huang said at GTC. “Once you create it, you can talk to it.”
[Vector embeddings](https://thenewstack.io/how-to-get-the-right-vector-embeddings/) help a NIM use information from local data to answer questions or retrieve relevant documents, videos, image or audio files on systems. RAG uses a base LLM to browse through local documents and augment knowledge, which helps it provide more accurate responses or retrieve relevant documents.
NVIDIA already has a desktop application called RTX that runs similar functions — the Mistral model indexes text documents and relevant documents from a PC based on user queries.
## Additional Skills Developers Should Learn
NVIDIA is trying to find ways to move workloads typically done on CPUs over to GPUs, Bob O’Donnell, an analyst with Technalysis, told me.
Working with NIMs requires understanding of how to work with NVIDIA hardware.
NIMs facilitate this shift, but people are still figuring out what to do with them and finding GPUs itself may be an issue, O’Donnell said.
Working with NIMs requires an understanding of how to work with NVIDIA hardware. Understanding CUDA helps, but isn’t a necessity; NIMs are compatible with other frameworks, APIs and open source tools.
Developers also need to understand the scale of an AI model. For example, a full-blown Llama-3 70B won’t run on an NVIDIA GPU with insufficient memory.
NVIDIA makes it easy to not worry about GPUs with hardware management tools in CUDA, but it helps to learn about the hardware resources. A script allows developers to select a GPU and manage memory capacity and other resources.
AI will ultimately become multimodal, and NIMs are built on interpreting different data types.
AI will ultimately become multimodal, and NIMs are built on interpreting different data types — such as images, text, videos, and speech. NIMs will request different documents, embeddings, and metadata via command line, with data sent back in JSON format. Working with APIs — making the correct requests, troubleshooting, and integrating the received information into a local AI model — is a crucial skill for developers to master.
**How to Get Started With NIMs**
NVIDIA is offering 1,000 free credits on its
[AI website](https://www.nvidia.com/en-us/ai/) to get started.
First, set up an Nvidia developer account, which you can use to log in to
[NVIDIA’s cloud service](https://ngc.nvidia.com). From there, obtain an API key from NVIDIA.
Developers should also install the
[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) on their system.
You can select a NIM from
[the catalog](https://catalog.ngc.nvidia.com/?filters=productNames%7CNVIDIA+Microservices%7Cnvidia_nim_da&orderBy=weightPopularDESC&query=&page=&pageSize=). For example, you could select a [Stable Diffusion XL NIM container](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nim/collections/stable-diffusion-xl) or a [Llama-3 70B container](https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama3-70b-instruct). The full NVIDIA list currently has about 24 NIMs, which will grow over time.
Command line typically works better for downloading and running NIMs. For example, the script to download Llama-3 70B and run it locally in a Docker container is
[available here](https://build.nvidia.com/explore/discover?snippet_tab=Docker#llama3-70b). Make sure to input your API key.
Users can also use Python and an OpenAI API to set up a local NIM installation. The script establishes tokens, hardware, and other details to run the environment.
Local NIMs can connect to other NIMs that are remotely or self-hosted, but you need the relevant API keys.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)