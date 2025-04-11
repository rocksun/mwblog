# Ironwood: Google’s Answer to Nvidia in the AI Chip Wars
![Featued image for: Ironwood: Google’s Answer to Nvidia in the AI Chip Wars](https://cdn.thenewstack.io/media/2025/04/e9f2b7df-osarugue-igbinoba-t354dnfdjkq-unsplash-1024x576.jpg)
[Hallucinations](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/) apart, customers in the past complained of [Google’s Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) being slow, especially with larger contexts and token counts.
To solve that problem, the company announced it was building some of its [fastest computers](https://thenewstack.io/top500-chinas-supercomputing-silence-aggravates-tech-cold-war-with-u-s/) to date with its new AI chip called Ironwood, the seventh-generation [TPU](https://thenewstack.io/ai-hardware-and-open-models-headed-in-the-linux-direction/), which was announced at [Google Cloud Next](https://cloud.withgoogle.com/next/25).

Each server, called a “pod” by [Google](https://cloud.google.com/?utm_content=inline+mention), will interconnect 9,216 Ironwood chips that can jointly run as one mega chip. One pod can deliver 42.5 exaflops of AI performance.

“The world’s number one supercomputer, El Capitan, supports 1.7 exaflops per pod. Ironwood offers more than 24 times that compute power,” said [Amin Vahdat](https://www.linkedin.com/in/vahdat/), vice president and general manager of [machine learning](https://thenewstack.io/simplify-ai-development-with-machine-learning-containers/), systems, and cloud AI at Google, in a press briefing.

Each of the 9,216 Ironwood chips delivers 4,614 teraflops of FP8 performance and is linked together by Google’s proprietary technology.

The interconnected chips are liquid-cooled and “span nearly 10 megawatts,” Google said in a press release.

That’s a lot of energy, but it’s the only way Google can lock down solid AI performance.

## Google Needs Ironwood
Google organizes the world’s digital information and presents it to users, first via search and now via AI.

The Ironwood chip will define just how quickly Google presents information via Gemini.

The demand for AI is overwhelming data centers, and faster chips like Ironwood meet the demand. Ironwood is the seventh version of the line of AI chips released by Google starting in 2015.

“As an industry, over the last eight years, we’ve seen a 10x year-over-year increase in demand for training and serving models. That is a factor of 100 million,” Vahdat said.

The chip is designed to run on Gemini workloads, which runs in the Google Cloud infrastructure. It won’t be available off the shelf.

Ironwood is faster and more power-efficient than the sixth-generation TPU called Trillium, which was released last year.

“Ironwood TPU is two times more power-efficient than our sixth-generation TPU, Trillium,” Vahdat said.

Each Ironwood TPU has 192GB of HBM memory, which is six times more than the 32GB HBM (High Bandwidth Memory) memory on Trillium.

On-chip HBM capacity is more important than the AI chip speed. Higher memory helps chips retain and process higher chunks needed for faster AI processing.

## Competition
Google’s Ironwood comes at the right time. Other proprietary AI models run on competitive chips.

Nvidia [announced last month](https://thenewstack.io/nvidia-unveils-next-gen-rubin-and-feynman-architectures-pushing-ai-power-limits/) its latest Blackwell Ultra chip and next-generation Rubin and Feynman GPUs. These chips power OpenAI’s latest AI models.

Amazon will ship its Trainium3 AI chip this year. Anthropic’s Claude model is optimized for the Trainium2 chip.

Microsoft currently uses Nvidia GPUs but has deployed its own AI accelerator called [Maia](https://thenewstack.io/why-microsoft-has-to-save-openai/) for inferencing workloads.

## Built for Inference
Ironwood, which Google also referred to as TPU7, is the first TPU built for reasoning and power thinking, Vahdat said.

In the early years, AI chips were built for training. But AI is now all about inferencing, with smarter models such as OpenAI o1 and DeepSeek R1 that can reason and think before providing answers.

“It’s no longer about the data put into the model, but what the model can do with data after it’s been trained,” Vahdat said.

Nvidia CEO [Jensen Huang](https://www.linkedin.com/in/jenhsunhuang/) last month said that reasoning models would drive compute demand by more than 100x compared to non-reasoning models.

The Ironwood TPU is designed only to serve Gemini, which is in version 2.5. Nvidia’s GPUs are more general-purpose and can run virtually any model except Gemini.

The “TPU launch builds on a commitment to delivering AI hardware optionality to our customers, including our expansive Nvidia GPU-based offerings,” Vahdat said.

The demand for faster chips is overwhelming the likes of Google, OpenAI, and Microsoft. As a result, GPU makers Nvidia and AMD are also introducing a new AI chip every year. The chips were previously released every one-and-a-half to two years.

## Availability
Ironwood TPUs will be available in two configurations, TPU7 and TPU7x. These technical names will show up for Google customers in the console, documentation, and billing, a Google spokeswoman told The New Stack.

Google didn’t announce a specific availability date for Ironwood in Google Cloud.

But it’s safe to assume that Ironwood TPUs will be the most expensive, and the older TPUs like Trillium (TPU6) or TPU v5 offerings will drop in price. Customers can select those chips for their AI workloads.

“Some may need the advanced inference capabilities of Ironwood while others may prefer the cost-effective training of TPU v5e,” the Google spokeswoman said.

## Data Types
The Ironwood peak performance numbers reflected above are for the FP8 data type, which is a preferred data type for inference.

“Ironwood also supports FP4, for customers to get an additional boost in data movement and power efficiency at lower precision,” the spokeswoman said.

Nvidia’s benchmarking of its GPU performance, shared at last month’s GTC, was on the FP4 data type. Lower-precision data types such as FP4 generally produce less accurate responses than FP8 but are significantly more power-efficient.

Ironwood also supports training workloads that require high-precision data types.

The training workloads “benefit from the massive parallel processing and efficient memory access that Ironwood enables,” the Google spokeswoman said.

## Google’s Stack
Google’s global data center infrastructure is divided into “[AI Hypercomputers](https://cloud.google.com/solutions/ai-hypercomputer?hl=en),” which house the AI chips, storage, networking, and memory.

Ironwood gives an AI Hypercomputer a lot more muscle.

Developers can enter the Hypercomputer and define the type of chip they need, such as a GPU, TPU, or CPU. The selection depends on the problem.

The Hypercomputer software layers include Vertex AI, which hosts Gemini, Llama, Gemma, and other AI models.

Developers can select the AI framework and reference implementations — such as JAX or [PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/) — and orchestration software such as [GKE](https://thenewstack.io/run-a-google-kubernetes-engine-cluster-for-under-25-month/) or [Slurm](https://thenewstack.io/kubernetes-evolution-from-microservices-to-batch-processing-powerhouse/).

A new layer announced at Google Cloud Next places AI agents as a way to engage or respond to queries. Gemini 2.5 is a reasoning model.

Google guarantees the availability and delivery of AI services in Google Cloud via service-level contracts.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)