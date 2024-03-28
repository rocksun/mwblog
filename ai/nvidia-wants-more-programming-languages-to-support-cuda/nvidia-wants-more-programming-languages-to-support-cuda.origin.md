# NVIDIA Wants More Programming Languages to Support CUDA
![Featued image for: NVIDIA Wants More Programming Languages to Support CUDA](https://cdn.thenewstack.io/media/2024/03/4374a15f-woman-7780330_1280-1024x703.png)
NVIDIA is looking to expand support for more programming languages as it tries to woo more developers to write applications for its GPUs.
The company’s
[CUDA programming framework](https://thenewstack.io/how-nvidia-gpu-acceleration-supercharged-milvus-vector-database/) currently supports languages that include [C++,](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/) Fortran and [Python](https://thenewstack.io/instagram-makes-smooth-move-python-3/). But new programming languages are evolving, and the company is keen on opening up access to its GPUs for developers using those languages, said [Jeff Larkin](https://www.linkedin.com/in/jefflarkin/), HPC architect at NVIDIA, during a technical session at the company’s [GPU Technology Conference](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/) earlier this month.
Larkin didn’t provide specifics on what programming languages it was looking at.
“My team is definitely monitoring those and trying to look for opportunities to engage on those. But [C++, Fortran and Python] are the ones that are specifically supported within our products today. There are some technologies I’m aware of, and I can’t mention here, that will further enable more languages as well,” Larkin said.
Larkin gave some examples of how some programming languages already exploit its GPUs, named dropping Judia and
[Rust](https://thenewstack.io/the-rust-community-matures-with-jetbrains-rustrover-ide/).
**Why Switch to GPUs? ** ![](https://cdn.thenewstack.io/media/2024/03/c206efb3-jensen_huang-nvidia-300x172.png)
NVIDIA CEO and co-founder Jensen Huang speaking at GTC 2024.
The early programming models revolved around CPUs. The x86 architecture was the big kahuna, while GPUs were relegated to gaming and graphics.
Fast forward, and AI has become a reality with GPUs. NVIDIA argues that CPUs are not efficient at handling AI transactions, while GPUs — which consume more power — will provide more cost savings.
“Typically, although a GPU does use more power, it uses that more productively, and that’s where you’ll begin to see the savings,” Larkin said. “You’ll operate more quickly, more power efficiently.”
NVIDIA is tightly coupling its own ARM-based CPU, called Grace Hopper, along with GPUs. But developers
[need CUDA to take full advantage of the GPUs](https://thenewstack.io/zluda-a-cuda-for-intel-gpus-needs-a-new-maintainer/).
## How CUDA Works
At the heart of
[NVIDIA’s GPUs](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/) are Tensor Cores, which is the hot technology driving most of the AI computing today. The Tensor Cores are capable of low-precision math and matrix multiplication for AI computing.
The matrix style of computing is built on the GEMM algorithm, which takes advantage of the Tensor Cores and is central to NVIDIA’s AI computing model. The GEMM algorithm works with libraries in CUDA for programmers to interact with the GPU cores.
The libraries include:
**cuBLAS:**This is NVIDIA’s preferred library that provides direct access to the Tensor Cores and delivers the maximum performance. “That is your basic workhorse that has existed since the very beginning of CUDA. It is linear algebra APIs,” said [Stephen Jones](https://developer.nvidia.com/blog/author/stjones/), CUDA architect, during a presentation at GTC. cuBLAS provides the easiest way to harness the performance of GPUs. It automates the configuration of Tensor Cores, and developers don’t have to turn knobs — cuBLAS just works out of the box. **CUTLASS:**The lower-level CUTLASS library provides C++ and Python interfaces for coders to work with the GPU’s Tensor Cores. Developers to control the use of Tensor Cores, which means more work for developers. CUTLASS differs from cuBLAS, which automates that process. NVIDIA is building more tools for Python developers to access CUTLASS, which is a recent development and a work in progress. “You can use the PyTorch extension, and so you can emit PyTorch code from CUTLASS, and you can automatically bring CUTLASS extension Tensor Core custom kernels in Python into PyTorch,” Jones said. **cuBLASLt:**This library sits somewhere between the cuBLAS and CUTLASS libraries, and provides varying levels of control to Tensor Cores. “CUTLASS actually calls that one in the middle, cuBLASLt, which you can also access yourself. It’s a public library. It gives these advanced APIs where you can really control a lot more aspects of what the Tensor Cores are doing,” Jones said. The cuBLASLt has advanced APIs for GEMM libraries, which opens the door for mixed-precision computing, which involves mixed and low-precision computing. **cuBLASDx:**This can perform select linear algebra functions from cuBLAS on the device side, which improves performance and throughput. “The idea is to get your cuBLAS cores, activate it in your kernel just with a single GEMM core like you would do with cuBLAS from a CPU,” Jones said.
## Python Is a Priority
NVIDIA is looking to expand access to its SDKs and frameworks to Python, which provides accessibility to more developers. That will, in turn, bring more developers to its GPUs.
“Looking at the Python stack, you have to invest everywhere, all the way across it,” Jones said.
NVIDIA wants to make Python “a complete Nvidia experience, and make the Python developer and the whole CUDA ecosystem available and accessible to the Python programmer,” Jones said.
The goal is to make more SDKs, frameworks, and domain-specific languages at the
[top of the stack](https://thenewstack.io/the-new-stacks-top-kubernetes-stories-of-2021/) available to more developers. At the same time, making the lower layers — accelerated libraries, system libraries and utilities, and device kernels — invisible to users. It’s still a work in progress, Jones said.
NVIDIA has worked on integrating its libraries and tools with popular Python frameworks such as
[PyTorch](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/).
“JIT compilation is incredibly important in Python because Python is a very runtime-interpreted language, and you’re constantly generating data dynamically. A compiler in the loop is completely normal. In fact, the Python interpreter basically is one of those,” Jones said.
## Program Well, Reap Rewards
Programming — and doing it correctly — is important to making AI more power-efficient.
Companies are measuring cost-per-transaction and trying to bring it down. AI has a crypto problem — it takes a lot of energy to run — and the cost of inference came under the microscope at GTC.
Jones argued that GPUs are more efficient in the final equation: they can deliver more FLOPS — Floating point operations per second — when factoring in rack space, time, and power consumption.
“Nobody cares how many servers you’re buying, nobody cares how many data centers you’re renting, you are renting power per month, because power is the metric that really matters for computing,” Jones said.
NVIDIA introduced new data types — FP4 and FP6 — which are lower-precision but can squeeze out more performance per watt.
The company introduced a new GPU codenamed Blackwell at GTC. A new server called DGX-B200 has eight Blackwell chips and consumes about 1,000 watts. It succeeds the H100 GPU, which is the GPU powering AI computing efforts at
[Microsoft](https://news.microsoft.com/?utm_content=inline+mention), Meta, Tesla and other companies.
Compared to the DGX-H100, the DGX-B200 system power consumption is similar, but performance improves by a factor of two to three times, said
[Charlie Boyle](https://www.linkedin.com/in/charlie-boyle-0201a8/), vice president and general manager of DGX systems at NVIDIA, in an interview.
## No Updates to CUDA
NVIDIA’s hardware and software model is much like Apple’s: the hardware and software go hand-in-hand. The software is designed for the hardware, and vice versa.
NVIDIA is trying to lock developers into CUDA, which is a proprietary development model. To be sure, NVIDIA GPUs support other programming models such as
[OpenAI’s Triton](https://openai.com/research/triton), and open-source development models.
The company’s goal is to integrate the hardware and software into a so-called “AI factory,” where the input is raw data, and the output is the result. The hardware and software remain invisible to customers.
Usually, NVIDIA releases a new version of CUDA with a new GPU. However, Jones provided no significant updates to CUDA during the GTC session. NVIDIA released CUDA version 12.4 recently and may share more details later this month as the release of its Blackwell GPU draws closer.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)