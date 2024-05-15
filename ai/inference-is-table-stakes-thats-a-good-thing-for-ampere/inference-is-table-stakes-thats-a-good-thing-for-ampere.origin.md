# Inference Is Table Stakes. That’s a Good Thing for Ampere
![Featued image for: Inference Is Table Stakes. That’s a Good Thing for Ampere](https://cdn.thenewstack.io/media/2024/05/c259c0c0-table-stakes-2-1024x576.jpg)
PARIS —
[Ampere](https://amperecomputing.com/), the maker of CPUs based on ARM architecture, is making its presence known, using [inference](https://thenewstack.io/when-cloud-meets-intelligence-inference-ai-as-a-service/) as a big hook. [AI training](https://thenewstack.io/hpc-kubernetes-ai-training-on-3500-gpus/) is a batch job workflow, but inference is crucial in AI-focused application development. All applications eventually require inference to stay fine-tuned and updated.
The hook for Ampere? Cloud native is one of them, plus its performance and its take on the noisy neighbor problem that can come with virtual machines.
Ampere is a semiconductor company
[started by Intel executives](https://www.reuters.com/technology/oracle-use-amperes-newest-chips-its-cloud-offering-2023-09-20/) led by [CEO Renée James](https://www.linkedin.com/in/renee-j-james-64182424/). It makes chips for cloud services and companies building out their infrastructure. Its customers include all the major cloud providers, except [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), which has a similar technology, [Gravitron](https://thenewstack.io/amazon-q-a-genai-to-understand-aws-and-your-business-docs/).
The story for Ampere centers on
[open source](https://thenewstack.io/open-source/) and the ability to run any workload on its architecture without the hassle of using [NVIDIA](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/) and integrating its CUDA library, which is the software needed to integrate GPUs with the software.
“So the focus is on enabling this entire open source ecosystem,” said
[Victor Jakubiuk](https://www.linkedin.com/in/jakubiuk/), Ampere’s vice president of AI, told The New Stack at KubeCon + CloudNativeCon Europe, in Paris.
## Inference Matters at Scale
Open source
[frameworks](https://thenewstack.io/the-ultimate-guide-to-machine-learning-frameworks/) like PyTorch and TensorFlow run efficiently for inference on pure CPUs, said Jakubiuk. They optimize for inference specifically to ensure the code generated during the runtime for those AI models is optimal for its CPUs and can scale across multiple servers simultaneously.
The efficiency of inference matters at scale, Jakubiuk said.
“If, for AI training, you trained a model once it might be expensive,” he said. “But once you have that model, once you go into deployment, you’re essentially multiplying this by 10x, 100x, 1,000x, because you’re deploying this at scale. And the moment you multiply this by a factor of 1,000, any sort of inefficiency you might have multiplies 1,000 times. And the same time, any efficiency gain multiplies significantly.”
By combining software and hardware optimization, a customer can get much better performance per watt of energy provided to their data center and, therefore, much better total cost of ownership (TCO) for end users in the cloud.
There are three core use cases, Jakubiuk said:
**Computer vision workloads:**Anything that processes videos and images. **Recommendation engines:**For example, ecommerce recommendation engines. **Large language models (LLMs):**Processing text to generate text, or try to understand the text. Ampere has seen particular interest in open source models such as Mistral and Llama.
First, the raw performance of the CPUs, with their large number of cores, makes them suitable for use with LLMs. The next step is the TCO in terms of performance per watt. It’s an advantage that Jakubiuk said gives Ampere’s CPUs an advantage over GPUs. That makes a difference if you run your organization’s data center; power is an issue almost everywhere. Maxing performance becomes critical as data centers require lots of power.
Ampere CPUs run upwards of more than 128 cores, Jakubiuk said. They can run any workload without noisy neighbor problems, avoiding the performance throttling issues that x86 CPUs suffer from the issues that surface when running virtual machines. One virtual machine may become compute-intensive, and a second may be running a database or a heavy workload that slows down the x86 CPU performance due to heat and power issues. Ampere redesigned the CPU to avoid problems with noisy neighbors.
Ampere provides out-of-the-box inference, according to Jakubiuk. Models trained by GPUs run on Ampere, which recommends using TensorFlow or PyTorch. Three core AI frameworks run on Ampere’s CPUs: TensorFlow, PyTorch, and Onyx. They focus on enabling support for the open source community and from sources like Hugging Face and models built with VMs on Jupyter Notebook.
“Probably the two that are worth mentioning are LLama and Mistral because these are by far the most popular models,” Jakubiuk said. “They run with very good performance, and especially performance per watt. And as I said, for LLama, you can get up to 80% better performance per dollar spent versus running them on GPUs.”
[Janakiram MSV](https://thenewstack.io/author/janakiram/), a longtime analyst and frequent contributor to The New Stack, said inference will become essential to application development, similar to the importance of APIs. Agents will emerge from inference, which will be developed with Retrieval Augmentation Generation (RAG).
And that will lead to a new emergence of agents for the cloud native community, which he said will come into focus this year and into 2025.
“Every observability company will have their own agent that can find anomalies, perform root-cause analysis and use this data to implement RAG,”
[Janakiram](https://thenewstack.io/large-language-model-observability-the-breakdown/) said.
Agents — the talk is all about agents. They’ll emerge in consumer technologies such as
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)