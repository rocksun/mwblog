# Docker Model Runner Brings Local LLMs to Your Desktop
![Featued image for: Docker Model Runner Brings Local LLMs to Your Desktop](https://cdn.thenewstack.io/media/2025/04/a94b6455-hu-chen-jazlbmkqf0u-unsplash-1024x684.jpg)
[Docker](https://www.docker.com/) made its name by making containers accessible to everyone. Now, [the company](https://www.docker.com/?utm_content=inline+mention) that’s synonymous with containerized development is trying to gain more fame by making it easy for developers to run and test [AI Large Language Models](https://thenewstack.io/LLM/) (LLMs) on their PCs with the launch of [Docker Model Runner](https://www.docker.com/blog/introducing-docker-model-runner/).
Docker Model Runner is a new beta feature in [Docker Desktop 4.40](https://www.docker.com/blog/docker-desktop-4-40/) for Apple silicon-powered Macs. This feature enables developers to run LLMs and other AI models on their PCs. You can access it directly from the command line. It also seamlessly integrates into the rest of the [Docker ecosystem](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/).

Why do it locally? Besides being able to integrate it directly into your workflow, Docker Model Runner eliminates the need to call out to external cloud application programming interfaces (APIs). This, in turn, ensures data privacy, reduces latency, and lowers costs.

With Docker Model Runner, your LLMs are packaged up as [Open Container Initiative](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/) (OCI) Artifacts. This enables you to pull models from Docker Hub or other registries and integrate them into CI/CD pipelines using familiar tools. For example, you can work with the models using familiar Docker CLI commands, such as “docker model pull”, “docker model run,” and “docker model list.” In other words, AI models are “first-class citizens” in the Docker workflow, just like containers and images.

Running LLMs on local machines has long been a challenge, hindered by fragmented tooling, hardware compatibility issues, and disconnected workflows. Developers often juggle multiple tools, configure complex environments, and manage models outside their containerized setups, leading to friction and rising cloud inference costs.

To pull this trick off, Docker Model Runner uses [llama.cpp](https://github.com/ggml-org/llama.cpp). This is an open-source C++ library that enables the efficient deployment and inference of LLMs without GPUs. Indeed, [Chris Wellons](https://nullprogram.com/about/), the well-known software engineer, reports he was able to successfully [port llama.cpp to Windows XP](https://nullprogram.com/blog/2024/11/10/) and run [a 360M model](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct) on a 2008-era laptop. In short, you can do real work on your work PC with these models.

Llama.cpp, as the name suggests, works well with Meta AI’s LLaMA LLMs. However, it is not limited to LLaMA models. Thanks to its use of an OpenAI-compatible API, it can work with other models. Docker has already made available a curated list of the most popular LLMs that are best-suited for local use cases. The easiest way to get started is by checking out [Docker Hub’s AI repository](https://hub.docker.com/u/ai).

There are currently just over a dozen LLMs, but more are on the way. Docker is partnering with AI leaders such as Google, HuggingFace, Qualcomm, Spring AI, VMware Tanzu, and Dagger. These collaborations bring a wide selection of high-quality, optimized models and tools directly into the Docker workflow, making it easier for developers to experiment and build AI-powered applications locally.

Looking ahead, Docker plans to expand support to more platforms, including Windows with GPU acceleration. Additionally, the plan is to enable developers to publish custom models with deeper integration into the broader AI ecosystem. The company envisions a future where running, sharing, and deploying AI models is as seamless and standardized as working with containers today.

But, wait! There’s more.

## Model Context Protocol
Docker is also integrating the [Model Context Protocol](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/) (MCP). This is an [open standard](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) designed to streamline the connection between AI agents and data sources, tools, and application environments.

Developed initially by [Anthropic](https://www.anthropic.com/), MCP has quickly emerged as a de facto standard — sometimes described as “[USB-C for AI](https://modelcontextprotocol.io/introduction)” — for connecting AI assistants to a wide range of resources, including databases, APIs, cloud services, and local file systems. By providing a universal protocol, MCP eliminates the need for custom connectors for each new tool or data source, making it dramatically easier for developers to build, deploy, and scale AI agents that can perform meaningful, context-rich tasks across diverse environments.

Docker is bringing it via [Docker MCP Catalog](https://www.docker.com/blog/introducing-docker-mcp-catalog-and-toolkit/). This Docker Hub catalog provides a centralized way to discover, run, and manage more than 100 MCP servers from leading providers, including Grafana Labs, [Kong](https://konghq.com/?utm_content=inline+mention), Neo4j, Pulumi, [Heroku](https://www.heroku.com/?utm_content=inline+mention), and Elasticsearch. Developers can now browse and launch MCP-enabled tools as easily as they would traditional containerized services.

The company is also providing the Docker MCP Toolkit, which brings enterprise-grade management and security to MCP workflows. It includes features like registry and image access management, secrets handling, and OAuth integration, making it easier for teams to securely publish, manage, and connect MCP servers within their existing Docker environments.

The point of all this, according to a statement by [new Docker President](https://www.globenewswire.com/news-release/2025/03/05/3037425/0/en/Docker-Appoints-Mark-Cavage-as-President-and-Chief-Operating-Officer-to-Accelerate-Next-Phase-of-Growth.html) and COO [Mark Cavage](https://www.linkedin.com/in/mcavage/), is that “Building functional AI applications shouldn’t feel radically different from building any other app. Developers want to integrate AI into their existing workflows — build locally, test, and ship to production with confidence. With agentic tools starting to behave like full-fledged software systems, the old challenges of packaging, versioning, and authentication come back fast. The Docker MCP Catalog brings that all together in one place, a trusted, developer-friendly experience within Docker Hub, where tools are verified, secure, and easy to run.”

So, if you want to make AI a part of your workflow without blood, sweat, and tears, and you’re already using Docker for your development workflow, this new set of AI tools looks like a sure winner.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)