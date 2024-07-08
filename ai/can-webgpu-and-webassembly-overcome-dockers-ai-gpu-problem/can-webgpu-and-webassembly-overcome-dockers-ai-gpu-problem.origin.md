# Can WebGPU and WebAssembly Overcome Docker’s AI GPU Problem?
![Featued image for: Can WebGPU and WebAssembly Overcome Docker’s AI GPU Problem?](https://cdn.thenewstack.io/media/2024/07/7b93c78a-mariia-shalabaieva-0sqstxwhgnu-unsplash-1024x576.jpg)
PARIS — [WebAssembly](https://thenewstack.io/webassembly-to-let-developers-combine-languages/) and [Docker](https://www.docker.com/?utm_content=inline+mention) have proven to provide advanced capabilities for the portability of applications and code. In WebAssembly’s case, the motto holds true in that it’s designed to allow for deployments once and anywhere. Docker, of course, has famously provided a level of abstraction that was largely responsible for the massive adoption of [containerization](https://thenewstack.io/containers/), and arguably, [Kubernetes](https://thenewstack.io/kubernetes/) for its now tried and trusted way to port applications.

However, in both cases, the use of GPUs has proven to be not exactly a roadblock, but a speed bump for Docker and WebAssembly, experts said at the recent [AI_dev](https://aidevsummit.co/) conference here in June. In Docker’s case, it has been possible to port its containers as an abstraction on GPUs, but this has involved additional work for adding configurations for different GPUs. This entails extra effort, whereas the idea is to run Docker containers anywhere, especially on any GPU, without additional configurations such as adding drivers, which you would otherwise have to do with directly supported CPUs in Docker.

In WebAssembly’s case, often less discussed is how WebAssembly is designed to run on any CPU instruction set. CPUs and GPUs represent different types of instruction sets. For that reason, WebAssembly developers have been looking for a way to overcome the impediment of deploying WebAssembly on GPUs. In both cases, GPUs are central for [large language models (LLMs)](https://thenewstack.io/llm/) and AI functionalities and processing. For extending WebAssembly and Docker for AI applications, they are almost exclusively GPU-centric. Improving the abstraction for GPUs has been a subject of interest, especially during the past few months.

## Enter WebGPU
It seems that [WebGPU](https://thenewstack.io/pytorch-docker-and-ai-openness-highlight-ai_dev-europe/) offers a way to overcome these GPU shortcomings. With it, WebAssembly modules and Docker containers serving as abstractions can be deployed directly on GPUs without separate configurations for compatibility with different kinds of GPUs, including of course, [Nvidia’s CUDA](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/) GPUs for AI applications. Docker is now shipping the preview of WebGPU for Docker Engine, [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) and other platforms.

WebGPU has been in use as a [W3C](https://thenewstack.io/dev-news-w3c-accessibility-openai-python-sdk-and-more/) standard for a JavaScript-written API for application compatibility with GPUs, particularly on the Web. For WebAssembly to run AI workloads, WebGPU has served as a hardware accelerator on the Web. Standards such as WASI-NN have offered a compatibility interface to run inference in hardware available for the host, but the newer WebGPU standard has been shown recently to extend its reach to GPUs beyond browser environments.

As [Justin Cormack,](https://uk.linkedin.com/in/justincormack) CTO and co-founder at Docker, explained during his keynote at the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) AI_dev conference, Docker developers were looking for a portable abstraction, especially for your local development situation for GPUs.

“We spent a bit of time looking around about those things, and WebGPU came across as actually something that already exists, is already shipping in most of the browsers across all consumer GPUs and mobile, and it has an ecosystem,” Cormack said. “So, we’re announcing today that we’re supporting WebGPU in Docker.”

During the sidelines of the conference, Cormack explained how WebGPUs are showing a lot of promise. Speaking with me, he described how WebGPU serves as a particularly good fit for Docker containers ported to GPU environments.

“It’s actually fascinating because, in many cases, as long as you can get the hardware offload, there’s been significant work on abstracting that hardware offload to make it more portable,” Cormack told me.

Historically, many applications using GPUs were tightly coupled to Nvidia CUDA. Complex applications, such as scientific computing, were developed for GPUs, Cormack said. In contrast, ML models are much simpler in structure, requiring fast but not necessarily accurate operations, repeated many times.

“This means they don’t necessarily need to be tightly integrated with specific hardware to function properly,” Cormack said.

For WebAssembly, [Michael Yuan,](https://www.linkedin.com/in/myuan/) the maintainer of the [WasmEdge](https://thenewstack.io/rust-and-webassembly-serverless-functions-in-vercel/) project and CEO of [Second State](https://thenewstack.io/demo-use-webassembly-to-run-llms-on-your-own-device-with-wasmedge/), described how Docker containers are useful with WebGPU and open source projects like WasmEdge, a CNCF WebAssembly runtime project, and [LlamaEdge](https://github.com/LlamaEdge/LlamaEdge) for AI applications on the edge.

Yuan described how WebGPU really starts with the browser.

“You’ve already seen many WebAssembly components compiled to run in the browser, taking advantage of WebGPU,” Yuan said. “However, our story with Docker is focused on the edge and server-side use cases outside the browser. Some people may ask, ‘What do I use Wasm for on server-side AI?’ In fact, it’s widely used as an embedded runtime for AI models.”

The idea is that for applications that need AI services, instead of having the AI model run on a separate server providing an API, the open source AI model can be embedded in your application and packaged together, Yuan said.

“This approach is especially useful for edge use cases, development use cases and a variety of other scenarios,” Yuan said. “You want to package your large language model with the rest of the application to tightly coupled elements like the prompt and the context window. People are using WebAssembly as a runtime or middleware for the application to interact with the large language model.”

« GPUs have broken » the cloud computing paradigm traditionally on CPUs » for LLMs, but one

[#Wasm]module in a[@Docker]container can help, from Efficient and Cross-Platform LLM Inference in the Heterogenous Cloud,[@juntao]of Second State at the[#AIDev]Conference in Paris.[pic.twitter.com/Fexkae50ym]— BC Gain (@bcamerongain)

[June 20, 2024]
With LlamaEdge built on WasmEdge, which is also written in [Rust,](https://thenewstack.io/rust-meets-dart-with-release-of-rust_core-1-0-0/) and compiled to WebAssembly, it can be directly embedded into a host application. “This allows the application to access a large language model included in the same package,” Yuan said.

The process is targeted at developers and is “very easy,” Yuan said during his conference talk “Efficient and Cross-Platform LLM Inference in the Heterogenous Cloud, which he described as an extension of the keynote with Cormack.

“You just write to this API and then compile to Wasm,” Yuan said. ”Then, you can package the Wasm application with the runtime versions and model versions into a Docker image.”

To achieve this, you have a monolithic application with an embedded runtime and an embedded large language model, Yuan said. The embedded runtime allows this whole setup to run on different hardware and on WebGPU inside Docker, as well as on Nvidia hardware when the appropriate sharing is installed on Docker for speech-to-text, Yuan said.

The model files, including `tinyen.config`
and `tinyen.mpk`
, are bundled into a Docker image. Additionally, a runtime called the Whisper API server, written in Rust and compiled to WebAssembly, is included within the same Docker image. “That’s all that is needed in the Docker image,” Yuan said.

The resulting Docker image is created as follows:

This design ensures that any application, whether it’s a [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/) application, a Rust application, or another, can interact with the WebAssembly API included in the Docker image, Yuan said. Running this application provides an OpenAI-compatible speech-to-text API server, allowing the upload of voice documents such as WAV files. Currently, only WAV files are supported as MP3 support has not yet been configured,” Yuan said.

“The OpenAI-compatible API can be used to interact with this server,” Yuan said. “The entire Docker image, including all the model files, the LamaEdge runtime, and everything else, is just 90 megabytes.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)