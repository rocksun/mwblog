# NVIDIA Finally Adds Native Python Support to CUDA
![Featued image for: NVIDIA Finally Adds Native Python Support to CUDA](https://cdn.thenewstack.io/media/2024/02/467cc713-python-logo-square-1024x576.jpg)
In 2024, Python became the most popular programming language in the world — overtaking JavaScript — according to [GitHub’s 2024 open source survey](https://github.blog/news-insights/octoverse/octoverse-2024/).

For years, NVIDIA’s [CUDA](https://developer.nvidia.com/cuda-toolkit) software toolkit didn’t have native Python support. But that’s now changed.

At GTC, NVIDIA announced native support and full integration of Python in its CUDA toolkit. Developers will be able to use Python for direct execution of algorithmic-style computing on GPUs.

“We’ve been working hard to bring accelerated Python, first class, into the CUDA stack,” said [Stephen Jones](https://developer.nvidia.com/blog/author/stjones/), CUDA architect, during a presentation at the recent GTC conference.

For programmers, the implications are massive. CUDA was born from C and C++, and now coders don’t need knowledge of those programming languages to use the toolkit.

“Python for CUDA should not look like C. It should look like Python,” Jones said.

“Python CUDA is not just C translated into Python syntax.”

— Stephen Jones, CUDA architect
Coders can use natural Python interfaces and the scripting model of calling functions and libraries to create AI programs for execution on NVIDIA GPUs.

“Python CUDA is not just C translated into Python syntax. It’s got to be something which is natural to a Python developer,” Jones said.

## Native Python Opens New Doors
NVIDIA’s native support for Python on CUDA opens the developer toolkit to millions of developers. CUDA previously required developers to know C++ or Fortran. The programming kit had some Python tooling, but it wasn’t natively supported.

The number of CUDA users was only 4 million in 2023, up from 2 million in 2020, [according](https://futurumgroup.com/insights/ai-in-context-uxl-to-be-an-open-source-alternative-to-nvidias-cuda/) to The Futurum Group. But Python is the fastest-growing language in the world. NVIDIA will get access to millions of Python coders — especially in developing countries such as India and Brazil, where coders make fervent contributions to open source projects.

Python support will also make NVIDIA’s infrastructure ready to use in emerging markets. A bulk of NVIDIA GPUs are in the U.S. and Europe, but telecom and infrastructure companies in India are building out major GPU installations that will be operational in the coming years.

NVIDIA is pouring fuel into recruiting programmers and wants to [support more programming languages](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/), including Rust and Julia.

## How Pythonic CUDA Was Built
CUDA includes libraries, SDKs, compilers, host runtimes, tools, and pre-packaged software and algorithms. NVIDIA has added pieces to the entire [Pythonic CUDA stack](https://nvidia.github.io/cuda-python/latest/).

NVIDIA’s focus was to provide GPU acceleration without getting out of Python. CUDA Python can’t be just kernel offerings; it needs everything across the stack and a smooth execution flow, Jones said.

“You have to be able to write a kernel and drop it into PyTorch, but you also have to be able to call Pythonic libraries and all of these other things,” Jones said.

Effectively, there’s nothing at the compiler layer, as it’s built around just-in-time (JIT) compilation. That significantly reduces the number of dependencies in the tree for GPUs in the stack.

“Keeping this interoperability between all the layers is going to be a huge gain for productivity and being able to use Python end-to-end,” Jones said.

Initially, NVIDIA built base Python bindings (which include the runtime compiler) and Python libraries such as cuPyNumeric, which is a drop-in replacement for NumPy, the most widely used computational library in Python. cuPyNumeric changes just one import directive, and NumPy code goes from running on the CPU to running on a GPU.

CUDA Core is a “Pythonic reimagining of the CUDA runtime to be naturally and natively Python.”

— Stephen Jones, CUDA architect
Over the last year, NVIDIA made [CUDA Core](https://nvidia.github.io/cuda-python/cuda-core/latest/), which Jones said is a “Pythonic reimagining of the CUDA runtime to be naturally and natively Python.”

CUDA Core has the execution flow of Python, which is fully in process and leans heavily into JIT compilation.

“You should not be dropping out command-line compilers or anything like that, you should be fully in process,” Jones said, adding that this significantly reduces the number of dependencies in the tree for GPUs in the stack.

NVIDIA created a library called NVMath Python with unified interfaces for both host-side and device-side library calls. The ability to fuse library calls brings big performance improvements, Jones said.

The company has also built libraries that can access accelerated C++ libraries directly from Python code.

“Because this sits on top of the underlying infrastructure that we’ve built over the years… we didn’t re-implement these in Python. We made sure that it links in the underlying fine-tuned C++ code so [that] your performance difference is negligible,” Jones said.

NVIDIA also added tools for profilers and code analyzers.

## The Programming Model
Python makes coding straightforward and coders don’t have to worry much about the underlying hardware. With that in mind, NVIDIA is adding a coding layer that aligns with higher-level abstraction for execution on GPUs.

The new programming model, called CuTile interface, is being developed first for Pythonic CUDA with an extension for C++ CUDA coming later.

CuTile is “fundamentally more platonic,” as Python programmers today think more in terms of arrays than threads (which is more of a C++ trait).

Developers can’t magically take Python code and export it for GPU acceleration. CUDA typically takes a problem and breaks it into thousands of smaller blocks that are processed separately on GPUs.

The blocks are broken up into smaller tiles, which run thousands of threads processing single elements. The threads gang up into a single operation.

The ability to go all the way down to process single elements at the thread level in parallel gives the GPUs their massive computing power.

But NVIDIA figured that GPU execution doesn’t need to go all the way down to the thread level. Processing can also be done midway at the level of tiles, which is where the CuTile programming model fits in.

Unlike C++, Python isn’t granular by design.

CuTile does an efficient job of mapping arrays to GPUs at a less granular level, which makes the code easier to understand and debug. “And fundamentally, it comes out to the same performance,” Jones said.

Data in tiles could be structured as vectors, tensors, or arrays. Compilers can do a better job of thread mapping whole array operations from one block of threads to GPUs.

“Very often the compiler will do better than I can do because the compiler deeply understands what I’m doing… [and] the fine details of how the GPU runs,” Jones said.

Unlike C++, Python isn’t granular by design.

“There’s a lot of these things out there. OpenAI’s Triton would be a good example. And I think that those are a natural fit for Python programs,” Jones said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)