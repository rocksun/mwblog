# Why PyTorch Gets All the Love
![Featued image for: Why PyTorch Gets All the Love](https://cdn.thenewstack.io/media/2024/11/5aae1c0e-pytorch-love-1024x684.jpg)
PyTorch has grown exponentially since rising from the research community in 2016 and finding its place in the data science world. PyTorch’s star count on GitHub grew 388% between 2017 and 2018, according to GitHub data. Even though growth steadied to about 17% from 2022 to 2023, and TensorFlow remains the top deep learning framework, with [nearly 39% market share](https://6sense.com/tech/data-science-machine-learning/tensorflow-market-share), according to 6Sense, vs. 24% for PyTorch, [momentum is on PyTorch’s side](https://survey.stackoverflow.co/2024/technology#1-other-frameworks-and-libraries).

The booming [popularity of the Python programming language](https://thenewstack.io/25000-python-devs-surveyed-on-tools-ides-and-python-2/) is one factor in the [open source deep learning framework](https://thenewstack.io/genai-wont-replace-open-source-says-aws-exec/)’s success. But now, the growth in generative AI has made PyTorch the choice for thousands of developers. It’s relatively easy to use, and its performance gets high marks.

So, what’s the PyTorch story? Why did it rise so fast in popularity? What are the tradeoffs it now faces?

## Before PyTorch
[PyTorch emerged](https://thenewstack.io/official-pytorch-documentary-revisits-its-past-and-its-future/) in 2016 from the Facebook AI Research Lab (FAIR) as a reimplementation of the concepts developed in [Torch](http://torch.ch/), which started in 2002 as a machine learning (ML) and scientific computing project at the Idiap Research Institute in Switzerland. Originally written in [Lua](https://thenewstack.io/how-roblox-makes-programming-beginner-friendly-with-luau/), Torch later adopted [LuaJT](https://luajit.org/), a tracing just-in-time compiler for the Lua programming language that helped improve performance.
The Torch developers did a lot to make the framework user-friendly. They built it to support GPU acceleration. They chose Lua, a relatively easy programming language to learn. The Torch neural network libraries received high marks for their usability.

According to the [Torch website](http://torch.ch/#why-torch), the community built packages for machine learning, computer vision, signal processing, parallel processing, multimedia (images, video, audio), and networking, among others. Torch developed “neural network and optimization libraries that were simple to use while having maximum flexibility in implementing complex neural network topologies.” Developers could build “arbitrary graphs of neural networks and parallelize them over CPUs and GPUs.”

In all, the Torch community had a winner. But Lua? Yes, it’s awesome, but other trends were afoot.

## Early Days
In 2017, [Soumith Chintala](https://www.linkedin.com/in/soumith/), who led Torch 7, received an inquiry from [Adam Paszke](https://www.linkedin.com/in/apaszke/), a computer scientist and then a university student in Poland, who volunteered to replace Lua in Torch with Python.

But why?

Python was on a tear, with 27% year-over-year growth, according to [Stack Overflow](https://stackoverflow.blog/2017/09/06/incredible-growth-python/) data. Over the prior five years, the community outpaced almost every other programming language, including Swift, Rust and Go.

In 2017, PyTorch released its API in version 0.2, and to this day, the API’s foundation remains much the same. Considered PyTorch’s co-creators, Chintala is now Meta’s “AI fixer,” and Paszke is at Google.

“They designed something that was really great,” said [Luca Antiga](https://www.linkedin.com/in/lantiga/), CTO at [Lightning AI](https://thenewstack.io/lightning-ai-teases-app-development-platform-an-os-for-ai/), in an interview. “They took some inspiration from [Chainer](https://stackshare.io/stackups/chainer-vs-pytorch), a framework developed in Japan. And then when [PyTorch] came out, I started contributing as an external contributor, and others joined. And, yeah, it was a great time.”

What makes PyTorch unique? It’s the ease of use, sure, but PyTorch’s strength comes with its tensors, gradient features and dynamic graph, James Birkenau wrote last year [in TensorScience](https://www.tensorscience.com/posts/a-short-introduction-to-pytorch-in-python-2023.html). He said understanding PyTorch and its ecosystem starts with becoming familiar with tensors. “In essence, tensors are multidimensional arrays — the building blocks of data in PyTorch. They resemble NumPy arrays but have the superpower of being able to run on GPUs,” he wrote.

But what’s a dynamic graph? In essence, it allows the developer to build a graph on the fly, and specifically, it bolsters PyTorch’s focus on ease of use.

As the DevLearningDaily team wrote in a [comparison of TensorFlow and PyTorch](https://learningdaily.dev/pytorch-vs-tensorflow-the-key-differences-that-you-should-know-534184a22f90):

“The dynamic nature of PyTorch’s computational graph is advantageous during model development and debugging because we can print, modify or analyze the computation graph at runtime.”

Birkenau wrote that the next step is understanding [Autograd](https://pytorch.org/tutorials/beginner/introyt/autogradyt_tutorial.html), the PyTorch module that manages differentiation. Birkenau describes Autograd as the “computational graph [that] crystallizes how operations on tensors are connected. It’s like a blueprint that shows how data flows and is transformed by different operations until we get our output.”

## The Define-by-Run Breakthrough
Before PyTorch, architects often used domain-specific languages to build deep learning frameworks. But that created problems. Something might break, and the researcher would have to piece through layers in the stack to decipher C++ tracebacks to understand the problem. It could get complex if, for example, an error appeared long after the architect wrote the code.

Chainer introduced the core [concept of define-by-run principle](https://pytorch.org/blog/pytorch-adds-new-tools-and-libraries-welcomes-preferred-networks-to-its-community/) to speed up its development. In its documentation, Chainer described define-by-run as a scheme in which the “network is defined dynamically via the actual forward computation. More precisely, Chainer stores the history of computation instead of programming logic.”

It’s an interesting delineation. Back when frameworks emerged, researchers used programming logic to build graphs. PyTorch began using computations, building the graph on the fly. With computations, the researchers built in automatic differentiation, meaning, as Chainer explained, they could go backward through the stored operations.

The internals changed over time. However, Antiga said, ergonomics and attention to developer efficiency remained at PyTorch’s core.

The dynamic graph made PyTorch easy to debug. Before, a researcher would build a graph and begin debugging — a significant task to find a bug. With the define-by-run principle, the researcher would write a line of code and, upon execution, know precisely where the line of code broke. PyTorch became natural to debug and play with, allowing greater risk-taking without a considerable time investment.

## The PyTorch Ecosystem
By 2019, the PyTorch ecosystem started to grow at quite a clip. Then managed by [Meta](https://about.meta.com/?utm_content=inline+mention) (then Facebook), PyTorch was not yet under the umbrella of the Linux Foundation, which [began managing it in 2022](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/). The ecosystem’s growth meant even a company as large as Meta needed to move the open source project outside its walls and into the hands of an open source organization.

And that ecosystem is massive: Today, the PyTorch core project has almost 84,000 stars on GitHub. It consists of the core project, official libraries such as Torchvision, and popular technologies built on top of PyTorch such as PyTorch Lightning and Hugging Face, which allow developers to train and build their models. It also includes thousands of community libraries and tools. In addition to Meta, the PyTorch Foundation’s governing board consists of [AWS](https://aws.amazon.com/?utm_content=inline+mention), [AMD](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention), [Arm](https://www.arm.com/campaigns/multi-arch-cloud-infrastructure?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention), [Huawei](https://www.huawei.com/en/), [Hugging Face](https://huggingface.co/), [Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention), [IBM](https://www.ibm.com?utm_content=inline+mention), Lightning AI, [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure and [Nvidia](https://www.nvidia.com/en-us/).

As [Adam Seligman](https://www.linkedin.com/in/adamseligman/), vice president of developer experience at AWS, said in an interview at the [2024 PyTorch Conference](https://events.linuxfoundation.org/pytorch-conference/) in September, “PyTorch is super exciting. With the support of Meta and a broader community, it has enabled amazing model, AI and research innovations.”

[AWS got involved with PyTorch](https://aws.amazon.com/pytorch/) around 2018 or 2019, said [Trevor Harvey](https://www.linkedin.com/in/trevorharvey1/), a principal specialist in generative AI at AWS. Harvey also sits on the [PyTorch governing board](https://pytorch.org/governing-board) as an alternate to AWS’s [Brian Granger](https://www.linkedin.com/in/brian-granger-b9998662/). AWS wanted its customers to have a choice of frameworks, and PyTorch had started to take off in the research community. The popularity served as a leading indicator for future customer adoption. Harvey said:
“We knew that there’d be a lot of new developers and researchers who are diving into ML for the first time, and PyTorch makes it easy to learn and work interactively. It ties back to our goal at AWS to help democratize ML and make it accessible to anyone who wants to leverage it.”

Much of the ecosystem’s growth came from work by technologists such as [William Falcon](https://www.linkedin.com/in/wfalcon/). While a doctoral student at New York University, Falcon saw an opportunity to make research work easier and more efficient, and he developed PyTorch Lightning. Lightning makes it easier for users to train at scale and iterate faster. Developers do not have to worry about as many details such as recording metrics, logging metrics and distributed sampling for data loading. It saves time because the developer does not need to know what is working under the hood.

“We’re not sugar-coating PyTorch,” Lightning AI’s Antiga said. “We’re just adding more structure to the user code so we can take care of certain aspects of it, like how you make it distributed, and how you run on different accelerators without changing your code.”

## The Community Grows
In 2021, [Chintala wrote](https://soumith.ch/blog/2021-08-02-growing-opensource.md.html) that ease of use stood as a core value for the PyTorch deep learning framework and aided its growth. He wrote:

“This view was really useful in bringing people along. Over time, PyTorch brought along and integrated the Caffe2 and Chainer communities and stayed friendly with [JAX ](https://github.com/jax-ml/jax)and Swift4TF. Bringing others along has enormous advantages. The community gets bigger, you arguably get wider perspectives that make the project better and broader over time.”

Chainer, a flexible framework for neural network development, joined forces in 2019 with PyTorch. It offered a streamlined approach to leveraging GPUs. JAX still exists as an alternative to PyTorch, but [developers say](https://www.reddit.com/r/MachineLearning/comments/1b08qv6/d_is_it_worth_switching_to_jax_from/?rdt=43487) PyTorch is easier to use and has a deeper community. Google archived Swift for TensorFlow (Swift4TF) in 2022.

Caffe2 and Chainer helped broaden the community. In 2018, Meta (then Facebook) managed Caffe2, the deep learning framework created at Berkeley by [Yangqing Jia](https://www.linkedin.com/in/yangqing-jia/). Jia is the founder of Lepton AI, who helped build Facebook’s AI infrastructure and later the AI and data analytics platform for cloud provider Alibaba.

## PyTorch in 2024 — and Beyond
Today, PyTorch is one of the most popular deep learning frameworks. [Ji Li](https://www.linkedin.com/in/vieplivee/), PyTorch analytics lead at Meta, [outlined the framework’s growth](https://youtu.be/ibgW_ali0Gc?feature=shared) at the PyTorch Conference in September. Li said over the previous 12 months, developers created more than 140,000 GitHub repositories using PyTorch, with more than 13,000 commits made to the PyTorch core repository and more than 1,000 new contributors.

PyTorch 2.0 was released in March 2023, and 2.5 in October 2024. Features added to PyTorch in recent months show how far it has come since its early days:

- In April 2024, the community added
[ExecuTorch Alpha](https://pytorch.org/blog/executorch-alpha/), which deploys large language models (LLMs) and large ML models to the edge, stabilizing the API surface and improving its installation processes. - The community introduced
[TorchChat](https://pytorch.org/blog/torchchat-local-llm-inference/)in July, which showed how to run Llama 3, 3.1 and other LLMs across laptops, desktops and mobile, focusing on seamlessness and performance. - In August,
[FlexAttention](https://arxiv.org/abs/2407.20228)was added to allow the implementation of variants in a few lines of idiomatic PyTorch code. - The community added
[TorchAO](https://github.com/pytorch/ao)in September. It quantizes and sparsifies weights, gradients, optimizers and activations for inference and training.
In an interview, [Alban Desmaison](https://www.linkedin.com/in/albandesmaison), a PyTorch maintainer with Meta, said PyTorch 2.5, the latest release, had 4,095 commits from 504 contributors.

### Introducing Compile Mode and Eager Mode
Recent PyTorch development, post v2.0, shows how generative AI has impacted its development. Developers want more efficient ways to debug models and get them into production. [Eager mode](https://medium.com/@sim30217/eager-mode-in-pytorch-e289c0e84eb1) is the default way to execute code. [Compile mode](https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) allows for an extra kick. According to [PyTorch documentation](https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html), it “makes PyTorch code run faster by JIT-compiling PyTorch code into optimized kernels, all while requiring minimal code changes.” The compiler has been a major focus of PyTorch development after 2.0, Antiga said.

[Sunita Nadampalli](https://www.linkedin.com/in/sunita-nadampalli-17882523/), a principal engineer at AWS who [spoke at the PyTorch Conference](https://www.youtube.com/watch?v=_9xohmSa2G8) in September, also credited the two development modes. AWS has customers that develop and train models and customers that increasingly deploy models into production. Compile mode removes a lot of [Python](https://thenewstack.io/what-is-python/) overhead, bringing the model or the workload very close to the usage mode, Nadampalli said.
“As a developer, I use both modes,” Nadampalli said. “For example, when there is something new, I start with eager mode so that I have a lot of flexibility in debugging and extracting the major hardware details, and at the same time, ease of experimenting, iterating more and more. And once I’m close to the performance that I want, I move to the compile mode and tune it further for our production use cases.”

As generative AI becomes even more popular, developers are building larger models, Antiga said. The GPUs are getting more optimized for computing. Demand is increasing to run models in parallel across different accelerators, different GPUs on the machine or different machines.

Seligman said AWS is “super excited” to contribute to PyTorch and to “make sure data scientists, ML researchers and developers have this amazing library they can work with, innovate, build new models and explore this new world of generative AI.”

The work to make PyTorch compatible on multiple backends shows the value of OpenAI’s [Triton](https://www.nvidia.com/en-us/ai-data-science/products/triton-inference-server/) and the importance the PyTorch team puts on making things easier for developers, a theme that continues to distinguish PyTorch from other frameworks.

For example, Desmaison explained Triton is the piece that brings a specifically written Python function into a GPU kernel. It enables developers to take their Python code and use it on another backend. It’s still in the early days, but it is there. For instance, a developer may move the code to an AMD GPU as an example. The engineer can generate something for Triton and extend it to different backends.

“Our goal is for the user to swap that device object from CPU to CUDA, and that’s it,” Desmaison said. “They don’t need to know about these horrible things we do in the backend to decide which one to use and how we are making choices for the different compilers.”

## What’s Ahead
PyTorch took eight years to get to a place of dominance. But how long can the community keep up the pace? Does the community just keep growing on a broad basis?

These are the questions that will need answering in the years to come. More specialized frameworks are bound to emerge.

A lot depends on how broad an approach the community takes. PyTorch supports a lot of applications. But what happens if more specialized frameworks emerge? What direction will the PyTorch community take?

PyTorch will be challenged by frameworks that do less and may be more optimized for certain things, Antigua said. But since PyTorch’s design allows it to adapt, as exemplified with its compiler approach, there’s a lot of room for it to evolve to satisfy more specialized workloads, he concluded.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)