# Kubernetes and AI: Are They a Fit?
![Featued image for: Kubernetes and AI: Are They a Fit?](https://cdn.thenewstack.io/media/2024/03/67dab3fc-kubcon-paris-2-1024x576.jpg)
PARIS — Let’s say a machine learning researcher has read a research paper and wants to test it with a Python-based GPU in a PyTorch environment. She asks her engineering team to access a
[Jupyter notebook](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) with two GPUs and all her libraries.
The engineering team tells her it will take three days. They will have to source the GPUs, create a stack, and then give access to
[JupyterHub](https://jupyter.org/hub).
“This is exactly what
[DevOps](https://thenewstack.io/devops/) experienced 10 years ago,” said [Janakiram MSV](https://janakiram.com/), an independent analyst and [frequent contributor to The New Stack](https://thenewstack.io/author/janakiram/), in a conversation at [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) this month.
“So now the whole idea is, how do we accelerate this and enable enterprise IT to bring infrastructure to a point where it is readily available for ML researchers, engineers and developers, where they can quickly translate their ideas into code?”
New personas reflect
[large language models’](https://thenewstack.io/what-is-a-large-language-model/) (LLMs) impact on the cloud native community and raise questions about identity and [Kubernetes’s](https://thenewstack.io/kubernetes/) role. Is Kubernetes even needed for data scientists to get their models into production?
“At NVIDIA’s GTC conference, they announced something called
[Nim](https://developer.nvidia.com/blog/nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/),” said [Sanjeev Mohan](https://www.sanjmo.com/), an independent analyst, in a recording for an upcoming episode of The New Stack Makers. “NVIDIA inference microservices Nim is a [Docker](https://www.docker.com/?utm_content=inline+mention) container orchestrated by Kubernetes. This only happened last week when we were at KubeCon, and [NVIDIA GTC](https://thenewstack.io/nvidia-gtc-hyperscaler-happiness-and-enterprise-indigestion/) was going on at the same time.”
The stateful nature of data and the pace of change make the transition challenging for Kubernetes to become deeply data-centric. Never has data played such an essential part in the Kubernetes community. Never before has the Kubernetes community needed to adapt in such a way to the new demands brought by generative AI, model development, integration, deployment and management.
Without standard ways for data models to deploy on Kubernetes, the work ahead will require the community to accommodate the new data personas with new hardware integrations and projects.
## Kubernetes and LLMs
But really, what is Kubernetes’s role in AI? The persona question brings this matter to the forefront. Kubernetes is a control plane — yes, that makes sense. Since 2014, it has served as an application architecture for DevOps.
So a question that Mohan poses becomes more relevant: Is Kubernetes for AI or is AI for Kubernetes?
At KubeCon, we saw a lot of how Kubernetes is for AI, serving as a control plane. NVIDIA was on stage in the keynote, and they talked about dynamic resource allocation to allocate fractional GPUs. That way you can save costs. So that is Kubernetes for AI. All that development is going very well, Mohan said, We will see more and more of Kubernetes becoming the control plane for general AI.
But how does AI make Kubernetes much more powerful, for example, with the use of LLMs? Mohan asked.
“I have not seen a lot on that side, maybe by next, next KubeCon or the one after that we will start seeing a higher integration,” he said.
[OpenAI](https://thenewstack.io/openai-chats-about-scaling-llms-at-anyscales-ray-summit/) serves as a testament to Kubernetes, which the company uses to [launch and scale experiments](https://kubernetes.io/case-studies/openai/).
How will Kubernetes become more default for all AI workloads without having the data scientists and data engineers have to think about how to configure it, to use whatever hardware GPUs most efficiently, asked Sudha Raghavan, a senior vice president at
[Oracle](https://developer.oracle.com/?utm_content=inline+mention), at KubeCon.
Raghavan, also on a panel at KubeCon, talked about a world where work on a per-workload basis gets easier, where engineers can configure out-of-the-box templates, understanding that these are the patterns of AI workloads that are yet to come and have predefined templates for them.
So any data scientists who want to do experiments don’t have to learn it on their own but rather can pick up on what the
[Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) can provide within its ecosystem for the AI and ML community. [Arun Gupta](https://www.linkedin.com/in/arunpgupta/), vice president and general manager for open ecosystems at Intel, said on a panel the cloud native community’s responsibility is bridging the gap. There must be empathy for the customer, who is the data scientist. A new [Cloud Native AI paper](https://www.cncf.io/wp-content/uploads/2024/03/cloud_native_ai24_031424a-2.pdf) addresses these sorts of challenges, he said. [Lachlan Evenson](https://www.linkedin.com/in/lachlanevenson/), principal product manager at [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), said on the same panel as Gupta that a new persona in the Kubernetes community also includes AI engineers, who sit between the data scientist and the infrastructure engineer or platform engineer.
Evenson noted in the panel discussion that the AI engineer needs to understand not only all the terminology that comes with the AI world but also how to use these distributed systems at scale and build these new platforms.
## The Promise of Extensibility
The Kubernetes founders made Kubernetes stateless, and then later built stateful technologies to integrate with its distributed platform.
“So that speaks to not only this community but the extensibility that we build into that platform through his community,” Evenson said. “And it’s not easy, you have to be one of these big companies. And I agree with what everybody else has said, we need to make it easier to run for everybody.
“We need to give out open source alternatives and open source platforms, so that companies that are looking to start investing and understanding how AI can impact their business, that they can take models and not worry about data governance or security concerns and start to tinker with them on their local environments and get familiar with them. “
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)