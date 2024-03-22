# Nvidia CEO Details a New AI Way of Developing Software
![Featued image for: Nvidia CEO Details a New AI Way of Developing Software](https://cdn.thenewstack.io/media/2024/03/c206efb3-jensen_huang-nvidia-1024x589.png)
Over the last few weeks, Nvidia CEO Jensen Huang
[has bluntly said](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/) people, with the forthcoming advances in AI, [won’t need to know how to program](https://thenewstack.io/making-sense-of-sam-altmans-7-trillion-ai-chips-gambit/).
At Nvidia’s annual GPU Technology Conference (
[GTC](https://www.nvidia.com/gtc/)) being held this week, Huang [doubled down on his words](https://blogs.nvidia.com/blog/2024-GTC-keynote/) and explained in his keynote speech how the company was rewriting software development during his keynote speech
Many have talked about AI being used to generate code, but Nvidia is putting it to work. Huang talked bigger — about clearing out the entire development pipeline with new ways to write programs.
“How do we build software in the future? It is unlikely that you’ll write it from scratch or write a whole bunch of Python code or anything like that. It is very likely that you assemble a team of AIs,” Huang said.
## What’s the Plan?
Nvidia is creating an AI-specific
[software development cycle](https://thenewstack.io/security-testing-must-be-part-of-software-development-life-cycle/) that relies on chatbots and co-pilots to create applications.
“There’s probably going to be a super AI that takes the mission that you give it and breaks it down into an execution plan,” Huang said.
The programming language is English. Users can type in a program they want in a ChatGPT style interface, and the output will be the application, Huang said.
The shift to a new software creation model is coming as AI computers capable of reasoning gain a foothold. The
[current software development cycles](https://thenewstack.io/devops/) are heavily dependent on the logical nature of CPUs.
The new computer will “help you create a new type of application for the future. Not one that you wrote completely from scratch,” Huang said.
Nvidia announced the concept of an “AI foundry” as a so-called construction kit to generate the applications. Users can just spell out the type of application they want, and the AI foundry — which is based on Nvidia’s hardware and software — will spit out the application.
![](https://cdn.thenewstack.io/media/2024/03/8e4b0635-vivy0652-1-scaled.jpg-1024x683.webp)
Courtesy of Nvidia.
## What’s the Backend?
Nvidia’s development workflow relies on using conversational and automated interfaces to write, package and deploy software. The goal is to cut off the manual labor involved in traditional CI/CD pipelines.
“We’re going to invent a new way for you to receive and operate software,” Huang said.
Nvidia is hoping to automate software creation and code generation through co-pilots, AI interfaces, containers, and microservices. Nvidia’s interface
[automates the configuration of dependencies](https://thenewstack.io/automated-dependency-management-with-depfu/) and does relevant finetuning.
The most important component is NIMs (Nvidia Inference Microservices), which is more like an API for AI, which was announced at GTC. NIMs help users create applications by accessing the right data, large-language models, programming tools and dependencies.
All the pre-trained proprietary and open source
[large language models](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/) are stored in a container built on top of Kubernetes. The container — which is more of a black box — also includes a [cloud native stack](https://thenewstack.io/what-is-the-modern-cloud-native-stack/) optimized for GPUs, Nvidia’s [CUDA parallel programming language](https://thenewstack.io/nvidias-cuda-12-is-here-to-bring-out-the-animal-in-gpus/), the CuDNN neural network and other tools such as TensorRT, which improves inferencing performance.
A variety of NIMs work together to generate and execute code within the black box, which then delivers the end results to customers.
“That NIM could maybe understand SAP — the language of SAP is ABAP, it might understand ServiceNow and go retrieve some information from their platforms,” Huang said.
Instead of coding, users can speak in plain English.
“This is a piece of software in the future that has a really simple API. And that API is called human,” Huang said.
The Nvidia stack uses standard industry APIs for speech, text, images, and video. Nvidia announced new AI software called AI Enterprise 5.0 which includes the NeMo Retriever, which can retrieve information, and the Triton Inference Server, which serves the information.
The Nvidia software stack retrieves structured and unstructured data from the database and converts it to conversational data.
“Essentially take structured data or unstructured data, you learn its meaning, you encode its meaning. So now this becomes an AI database,” Huang said. “Once you create it, you can talk to it.”
SAP, ServiceNow, Cohesity and
[Snowflake ](https://www.snowflake.com/?utm_content=inline-mention)are among some customers using Nvidia’s NIMs to create co-pilots, chatbots and virtual assistants so customers can interface in plain English.
## Nvidia’s AI Stack Origins
Nvidia’s proprietary AI software stack,
[called CUDA](https://thenewstack.io/nvidia-hones-in-on-apple-like-approach-to-ai-with-cuda/), started off in 2006 as a programming model for high-performance computing.
In 2012, CUDA made “first contact” with AlexNet, a neural network for image recognition. It was the first trained on an Nvidia GPU.
“Recognizing the importance of this computing model, we invented a brand new type of computer we call the DGX-1 — 170 teraflops in this supercomputer, eight GPUs connected together for the very first time. I hand delivered the very first DGX-1 to a startup located in San Francisco called OpenAI,” Huang said.
In 2022, Nvidia’s GPUs were used to bring ChatGPT to life.
![](https://cdn.thenewstack.io/media/2024/03/ac4fee75-mjc_2441-2-scaled.jpg-1024x683.webp)
Courtesy of Nvidia.
## It Will Be an AI World
To be sure, Huang’s grand plans are more relevant to programming for AI systems, which can be targeted and specific to customer requirements. That differs from the conventional CI/CD model.
But the market demands that coders upskill to AI quickly — the number of AI-related tech jobs are on the upswing in a market where IT jobs are declining, according
[to research](https://www.aimaps.ai/) from the University of Maryland.
Nvidia dominates the AI market and is taking a ground-up approach — if you want to use Nvidia GPUs, you
[need to know how its development model](https://thenewstack.io/ai-development-needs-to-focus-more-on-data-less-on-models/) works.
“First is having the AI technology, second is to help you modify, and third is infrastructure for you to fine-tune it,” Huang said.
Nvidia introduced a new GPU called Blackwell at the trade show, which company executives said provides 20 petaflops of AI performance on a single GPU. A set of 576 Blackwell GPUs could train multi-trillion parameter models.
## Challenges
Nvidia wants customers to use its expensive hardware and software, which necessitates the use of CUDA, and creates a barrier to entry.
The Nvidia H100 GPU instances on cloud providers such as
[CoreWeave](https://www.coreweave.com/gpu-cloud-pricing) and [Lambda Labs](https://lambdalabs.com/service/gpu-cloud) are two times the price of the older A100 models per hour.
Google has floated the idea of its AI-based Duet service creating custom programs, such as financial tools, by just talking to the AI. Nvidia’s main rivals, AMD,
[Intel](https://thenewstack.io/intels-gelsinger-openais-altman-augur-the-future-of-genai/) and Cerebras, are taking an open source software approach. The companies support open models that include Llama 2 and Mixtral, but the chip makers do not provide tools where customers can write applications by just speaking to a computer. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)