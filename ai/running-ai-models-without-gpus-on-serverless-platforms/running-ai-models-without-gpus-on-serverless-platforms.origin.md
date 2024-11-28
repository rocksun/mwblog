# Running AI Models Without GPUs on Serverless Platforms
![Featued image for: Running AI Models Without GPUs on Serverless Platforms](https://cdn.thenewstack.io/media/2024/11/31d53ef8-ai-without-gpu-serverless-1024x576.jpg)
As machine learning (ML) technologies evolve, the choice of computing resources becomes a pivotal decision influencing both performance and cost efficiency. GPUs are the preferred choice for machine learning due to their parallel processing capabilities; however, recent advancements have also improved CPU performance for certain types of [ML tasks](https://roadmap.sh/mlops).

Llama (which stands for Large Language Model Meta AI) exemplifies this shift. I will explore the viability of the Llama model across various [serverless](https://thenewstack.io/serverless/) platforms without the use of GPUs.

## Choosing a Model
[Llama models](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/), created by Meta, are a series of [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) designed to deliver advanced natural language understanding and generation capabilities. These models are versatile and increasingly popular among organizations looking to implement AI-powered solutions without relying on extensive computational resources.
This may make Llama models a viable option for deployment on serverless platforms — that is, if there’s a model that fits within the limitations of serverless compute. The first challenge will be to figure out which Llama models to experiment with, as there are many to choose from.

To make an informed choice, you need to understand quantization. Quantization is a technique used in machine learning to compress large models by reducing the precision of their weights and other numerical values. Instead of using full 32-bit or 16-bit floating-point numbers to store these values, quantization represents them in lower-bit formats like 8-bit, 4-bit or even 2-bit integers. This reduction in precision significantly shrinks the model’s size and lowers its memory and computational requirements, but it can come at the cost of accuracy or quality.

Imagine tracking item prices in a store. Typically, you’d note prices with exact cents, like $4.99 or $6.33. Rounding to the nearest dollar (e.g., $5, $6) gives a rough approximation and simplifies the complexity of future calculations like estimated profit margins, tax or tips.

[LM Studio](https://lmstudio.ai/) distributes several quantized versions of the Llama 3.2 1B model on Hugging Face. In the naming scheme for quantized models, each part signals an aspect of the model’s compression. For example, with the Q4_K_M model:
**Q4**: The “Q” indicates quantization, and “4” shows that this model uses 4-bit precision for its weights. Lower bits mean a lighter model, suitable for limited resources but with a potential accuracy trade-off.**K**: Refers to the quantization technique, tailored to retain as much quality as possible while compressing the model.**M**: Stands for medium precision level, balancing accuracy and size. Other models may use “L” for low precision or “H” for high precision, depending on your application’s needs.
At the end of the day, there is a process of trial and error required to find a model that has the right mix of trade-offs and benefits that will run on the target infrastructure.

## Experiment Setup: Deploying Llama 3.2
After some trial and error and while researching what others have tried, I decided to start with the 4_K_M 1B model. This billion-parameter model can manage complex language tasks, generate nuanced responses and understand intricate relationships in data. It also promises a balance between computational complexity and output quality within my memory allocation limits.

Using Nitric, a framework that allows seamless deployment across multiple clouds, I set up the Llama model on both [AWS](https://aws.amazon.com/?utm_content=inline+mention) Lambda and [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Run.

Nitric also allows configuration of memory and/or CPU allocations for compute functions. However, there are some differences between the cloud vendors that limit the ability to create identical environments. For example, AWS [Lambda](https://aws.amazon.com/pm/lambda) does not allow explicit CPU configuration, while Google Compute Platform (GCP) [Cloud Run](https://cloud.google.com/run) restricts memory allocation to a maximum of 4GB per CPU.

This makes it particularly challenging to directly and fairly compare the performance of the models, so I will have to make a few approximations using “similar” hardware configurations. The final comparison will take tokens per second (TPS) and cost per second (CPS) into account to further control for these differences.

## Technical Implementation
Implementing the serverless deployment involves loading the model using `llama_cpp`
, defining API routes and setting up the necessary code to process prompts. Here’s the code used for loading the Llama model. I will deploy this same codebase for both AWS and GCP using Nitric for the deployments.

Note: For a step-by-step guide on how to run this project yourself, follow the [Llama 3.2 on AWS Lambda](https://thenewstack.io/running-llama-3-2-on-aws-lambda/) guide.

## Jumping Some Hurdles
While deploying the application went smoothly, loading and running the Llama models in my functions posed a few challenges.

### Memory
Initially, I encountered issues with timeouts, which indicated that my configuration was under-resourced for the model’s demands. Although the suggested memory requirement from Hugging Face was 16GB, through trial and error, I determined that the model would run with at least 6GB across environments. Scaling to 6GB on Cloud Run required increasing the CPU count from 1 to 2 due to GCP’s 4GB memory-per-CPU limit. On AWS, CPU configuration proved less flexible; I could only set the memory allocation to 6GB.

### Ephemeral Storage
Ephemeral storage is temporary storage that exists for the duration of a specific process or instance. Once the process completes or the instance is terminated, the data stored in ephemeral storage is lost.

Loading a Llama model requires higher ephemeral storage due to the large file sizes of the model, temporary decompression needs and intermediate computations during inference. AWS required an increase in default ephemeral storage from 512MB to 1024MB to accommodate model loading. As a side note, GCP Cloud Run allocates 2GB of ephemeral storage by default, so no changes were required there.

### CPU
Even with the CPU and memory settings, the model would load only about 50% of the time on GCP. The failures often resulted in timeouts, which were beginning to indicate that the CPU allocation wasn’t powerful enough for the model’s initial load requirements. After some trial and error, I enabled GCP’s CPU boost, a feature that temporarily provides extra CPU power during the startup phase of a serverless application.

The boost gave the container the extra processing power it needed to complete its intensive loading sequence within the timeout limits. The tradeoff is cost; you are charged for the boosted CPU during the startup time of the container plus an additional 10 seconds. For example, if your container startup time is 15 seconds and you allocate 2 CPUs, you’ll be charged for 4 CPUs for the entire 25 seconds.

## Results
**Tokens per Second**
My code includes a calculation of tokens generated per second (TPS). TPS quantifies the throughput of a model by determining how many units of text it can process or generate within a second. It’s similar to measuring a human’s reading or writing speed. A token can be a word, part of a word or sometimes even just a punctuation mark or a special character. For this example, just assume that a token is equal to a word. A typical human reads at about 300 words per minute (around five words per second), and writes about 40 words per minute (fewer than one word per second).

While it’s not entirely fair to compare the rate of token generation between a computer and a human, these estimates serve as a rough guide to help identify the right model for the right task. For instance, a prompt generator would be most useful when it generated content at least as fast as the average human reading speed.

### Cost Analysis
Although the environments managed vCPUs differently, the average TPS with the 6GB memory configurations were fairly similar on both platforms. They were calculated with a set of 50 sample prompts, like “Explain how a rainbow forms,” with slightly better results from prompts that limited response length — for example, “Explain how a rainbow forms, in 50 words.”

Using TPS, you can roughly calculate how much token generation costs in each environment for a typical prompt, which is approximately 500 tokens.

AWS Lambda |
GCP Cloud Run (Boosted) |
|
Memory allocation | 6GB | 6GB |
CPU allocation | Managed by AWS | 4 vCPU (2x for CPU Boost) |
Cost per GB-second | $0.00001667 | $0.00000250 |
Cost per vCPU-second | – | $0.00002400 |
Average TPS | 7.42 | 7.39 |
Compute CPS | 6GB × $0.00001667 = $0.00010002 | (4 vCPUs × $0.00002400) + (6 GB × $0.00000250) = $0.00010200 |
Cost per token (CPS / TPS) | $0.00001348 | 0.0000138 |
Cost per typical request (500 tokens) | $0.00674 | 0.0069 |
*Note: Pricing may vary based on region; these values used are estimates and based on U.S. Tier 1 regions for the compute resources only.*
## Conclusion
Based on these trials, Llama models can indeed be deployed on serverless platforms for lightweight or moderate tasks, with careful configuration to meet memory, CPU and storage needs. For specific applications where processing time and throughput are manageable within the serverless limitations, this setup is viable.

The cost differences are almost negligible, but only because I was forced to use CPU boost with Cloud Run to ensure that the model loaded within reasonable startup limits. If I could find a way to avoid CPU boosting, the cost could potentially be reduced on GCP as I wouldn’t be doubling up on CPUs. The other thing to consider is the recommended memory is 16GB, which would likely result in better model performance. GCP Cloud Run supports up to 32GB, while AWS supports up to 10GB.

Ultimately, serverless compute will likely struggle with larger models or when the application demands intensive computation over sustained periods. It is clear, however, that Llama on serverless can work well for specific low- to mid-tier applications but will require moving to GPUs as demands increase. In this experiment, I used Nitric to deploy serverless compute across multiple clouds. Nitric can also be used to to [deploy jobs that require substantial compute resources or GPU access](https://nitric.io/blog/introducing-nitric-batch) without writing complex deployment automation.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)