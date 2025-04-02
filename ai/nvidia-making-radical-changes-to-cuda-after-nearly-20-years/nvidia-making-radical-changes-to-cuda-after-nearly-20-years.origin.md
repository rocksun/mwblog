# NVIDIA Making Radical Changes to CUDA After Nearly 20 Years
![Featued image for: NVIDIA Making Radical Changes to CUDA After Nearly 20 Years](https://cdn.thenewstack.io/media/2025/04/23ecc719-boliviainteligente-zs3s9a3jeq-unsplashb-1024x576.jpg)
NVIDIA announced it’s making wholesale changes to the way [CUDA](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/) operates. It will also transform the way programmers conceive and write AI programs for the company’s [red-hot GPUs](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/).

The past was about creating runtimes for standalone GPUs, but now NVIDIA wants to create a single runtime for hundreds of thousands of GPUs.

“We’ve been talking about programming *a* GPU — how do I get my program on one GPU. And the reality is no one runs on one GPU anymore,” said [Stephen Jones](https://www.linkedin.com/in/stephen-jones-profile/), a CUDA architect at NVIDIA, during a technical session at the company’s recent GTC conference.

AI is now being done in tandem over hundreds of thousands of GPUs.

“Because the future is this massive data center scale computing, I’m going to be working on multinode CUDA [runtime],” Jones said.

The ongoing thinking within NVIDIA is to build a single runtime system that scales across whole data centers as opposed to standalone GPUs. NVIDIA has labeled the next-generation product CUDA DTX, or CUDA Distributed Execution.

“I’m literally telling you about something two years from now. I have no idea what the final thing looks like,” Jones said.

NVIDIA rarely talks about CUDA’s future, so it came as a bit of a shock when NVIDIA revealed that it was developing the next generation of CUDA at GTC.

In today’s AI world, there’s no escaping [CUDA](https://developer.nvidia.com/cuda-toolkit). The company’s GPUs are everywhere, and coders will run into NVIDIA’s CUDA tools somewhere in the programming stack, even if it is built mostly around open source tools.

NVIDIA’s GPUs mostly don’t work for AI without the CUDA framework, which includes libraries, compilers, runtimes and kernels. At a minimum, coders need to learn how to load the neural network library called [CuDNN](https://developer.nvidia.com/cudnn) to use NVIDIA’s authoring tools for AI.

Major AI frameworks TensorFlow and PyTorch are optimized for NVIDIA’s GPUs. AMD’s GPUs, Apple Macs or alternative AI chips don’t need NVIDIA’s CUDA stack, but that’s rare as NVIDIA’s hardware and software are driving today’s AI.

NVIDIA is usually tight-lipped about its plans for CUDA programming tools. But it releases a new version of CUDA with every new GPU architecture. CUDA 12 — which was [released](https://thenewstack.io/cuda-12-harnesses-a-nvidias-speedier-gpu-architecture/) way back in 2022 and is now on version 12.8 — was based on the Hopper architecture.

There’s no sign of CUDA 13, which should have launched with Blackwell, a new GPU architecture that succeeds Hopper. The company hasn’t talked about the release.

“CUDA follows semantic versioning, so we update versions based on changes to the API and ABI. We don’t expect to change the CUDA name or the versioning method as we introduce the new features that Stephen spoke about in his talk,” a spokeswoman for NVIDIA told The New Stack.

NVIDIA CEO Jensen Huang visualizes the data center as one giant GPU packed with hundreds of thousands of its chips. That aligns with the vision of CUDA DTX, which is a single runtime running across hundreds of thousands of GPUs. It also makes business sense — NVIDIA made $11 billion off Blackwell GPU sales in the most recent quarter.

The company is building [massive servers](https://thenewstack.io/after-deepseek-nvidia-puts-its-focus-on-inference-at-gtc/) packing fleets of GPUs. This year’s GB300 NVL72 server system has 72 next-generation Blackwell Ultra GPUs, and the mammoth DGX SuperPod, which will network 576 Blackwell Ultra GPUs by connecting multiple DGX B300 systems.

CUDA takes a program and breaks it into thousands of smaller blocks that are processed separately on GPUs. Blocks are further broken into thousands of threads, which gang up into a single operation. The bulk parallelism gives the GPUs their massive computing power.

The current version of CUDA is a confluence of all accelerated applications at one level, and execution on hardware at low levels. NVIDIA is trying to connect applications to disparate hardware in CUDA DTX.

“When I think about distributed CUDA, I think we need to think of a distributed machine model and a distributed runtime,” Jones said.

There could be a whole set of problems when running one massive CUDA runtime across 100,000 nodes, he added. “What works well at scale is not necessarily what works well on a single GPU,” Jones said.

The distributed runtime has to be dynamic to handle and manage hardware resources, topology and execution across a complicated structure of hundreds of thousands of GPUs. “It’s got to be resilient. If I have got a 100,000-node machine, things are going to go down all the time… it happens every day,” he said.

Jones elaborated further on considerations of the distributed CUDA DTX and its architecture, which is built around two core components.

The first is the unified machine model, in which the GPUs, CPUs, networking, accelerators and other chips all look the same. That means developers will be able to write an application only once, instead of multiple times for each chip.

“CUDA’s job is to unify what the machine does without compromising the performance you can get out of it,” Jones said.

The machine model is fundamental in treating the GPU as a GPU instead of different pieces of hardware, he noted.

Here’s where Jones pointed out that NVIDIA had an advantage as the hardware and software maker. The company can negotiate what it puts in the hardware and the software.

The second part to CUDA DTX is a “unified runtime,” in which the instructions/APIs are launched, create work and manage resources, topology and execution.

The distributed runtime includes asynchronous execution, which involves managing the parallel operation over the distributed GPU network.

“If I had to allocate memory differently on different hardware, you’d go crazy,” Jones said.

Jones reiterated that CUDA DTX’s final design could change. He also said NVIDIA had “ninjas” that took care of the backend work so that programmers can focus on plugging into CUDA and creating applications.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)