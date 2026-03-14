<!--
title: NanoClaw联手Docker：MicroVM沙盒安全隔离AI代理
cover: https://cdn.thenewstack.io/media/2026/03/fb0dcba1-eva-wahyuni-bw1u-glp6w-unsplash-scaled.jpg
summary: NanoClaw与Docker合作，利用MicroVM沙盒技术隔离AI代理，解决其安全隐患，为企业提供可信赖的AI代理运行环境。
-->

NanoClaw与Docker合作，利用MicroVM沙盒技术隔离AI代理，解决其安全隐患，为企业提供可信赖的AI代理运行环境。

> 译自：[NanoClaw and Docker team up to isolate AI agents inside MicroVM sandboxes](https://thenewstack.io/nanoclaw-docker-sandboxes-ai-agents/)
> 
> 作者：Steven J. Vaughan-Nichols

喜欢 OpenClaw 风格的代理的想法，但它们的不安全性让你头疼？NanoClaw 和 Docker Sandboxes 的组合可能正是你所需要的。

[OpenClaw 备受关注](https://thenewstack.io/openclaw-github-stars-security/)，但那些没有被 OpenClaw 迷住的人都知道它的安全性极差。这就是 [NanoClaw](https://github.com/qwibitai/nanoclaw) 的用武之地，它是一个开源的、专注于安全的 AI 代理运行时，旨在隔离容器内部运行，而不是直接在你的主机上运行。

[NanoClaw 被定位为 OpenClaw 的极简主义、生产就绪替代方案](https://thenewstack.io/nanoclaw-minimalist-ai-agents/)，拥有更小、更可审计的代码库以及围绕每个代理隔离构建的架构。现在为了进一步加强安全，其开发人员已与 [Docker](https://www.docker.com/) 合作，以运行 Docker 新兴的基于微虚拟机（MicroVM）的 [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/)。

过去一年，Docker 一直将实验性的 Docker Desktop 功能 Docker Sandboxes 打造为 AI 编码和任务代理的安全执行基础。这是一种 [从简单的容器隔离转向带有私有 Docker 守护进程的专用微虚拟机](https://www.ajeetraina.com/docker-sandboxes-containers-vs-microvms-when-to-use-what/) 的转变。Sandboxes 目前支持 macOS (Apple Silicon) 和 Windows，Linux 支持将在未来几周内推出。

每个沙盒现在都在其自己的轻量级 MicroVM 中运行，拥有自己的内核和 Docker 引擎。这使得你的代理可以安装软件包、构建镜像和运行容器，而不会接触主机 Docker 守护进程或主机文件系统。该公司将其宣传为自主代理的“深度防御”。

因此，即使代理实现容器逃逸或利用其环境中的零日漏洞，损害也仅限于 MicroVM 边界，而不是开发人员的笔记本电脑或 CI 运行器。这比 OpenClaw 的“安全？什么安全方法？”要安全得多。

此次集成使你能够通过单个命令将基于 NanoClaw 的代理部署到隔离的沙盒环境中。NanoClaw 针对一类快速增长的 AI 代理，它们不仅回答问题，还能连接到实时数据、执行代码并代表用户和团队采取行动。

这种扩展的范围增加了隔离和爆炸半径控制的风险，因为单个受损代理在共享主机时，可能会访问凭据、会话历史记录或由其他代理拥有的数据。NanoClaw 加 Docker Sandboxes 明确旨在解决这一风险。

根据 NanoClaw 的创建者 [Gavriel Cohen](https://www.linkedin.com/in/gavrielco/) 在一篇博客文章中写道：

*“当你使用 [AI 代理进行构建时，它们应该被视为不可信的，并可能具有恶意](https://nanoclaw.dev/blog/nanoclaw-docker-sandboxes)。……正确的方法是采用一种架构，它假设代理会行为不端，并在它们行为不端时控制损害。这一原则驱动着 NanoClaw 的每一个设计决策。不要将秘密或凭据放入代理的环境中。只向代理提供其工作所需的数据和工具，不多不少。将所有其他内容保留在硬边界的另一侧。借助 Docker Sandboxes，这个边界现在有两层深。每个代理都在自己的容器中运行（无法看到其他代理的数据），所有容器都在微虚拟机内部运行（无法接触你的主机）。如果幻觉或行为不端的代理可能导致安全问题，则安全模型就失效了。安全性必须在代理表面之外强制执行，而不是依赖于代理的正确行为。”*

[Mark Cavage](https://www.linkedin.com/in/mcavage/)，Docker 的总裁兼首席运营官，在一份新闻稿中表示：“每个组织都希望让 AI 代理投入工作，但障碍在于控制：这些代理可以访问什么，它们可以连接到哪里，以及它们可以改变什么。“Docker Sandboxes 提供了安全执行层，用于安全地运行代理，NanoClaw 展示了当这个基础到位时，一切皆有可能。”

Cohen 在新闻稿中补充道：“我们正处在一个转变的开端，每个组织中的每个团队都将拥有自己的 AI 代理团队，代表其完成实际工作。NanoClaw 的构建旨在使之成为现实，而 Docker Sandboxes 则使其成为组织可以真正信任的现实。”

公司越来越警惕在没有强大隔离的情况下运行可以执行任意代码、安装软件包或调用云 API 的代理。[使用 Firecracker、Sandboxes 或 Kata Containers 等程序的基于微虚拟机的隔离正成为保护主机免受 AI 生成代码影响的事实标准](https://northflank.com/blog/how-to-sandbox-ai-agents)。在这种方法中，单独的容器仅用于受信任的内部自动化。

通过将 Docker 的 MicroVM 沙盒与 NanoClaw 的最小攻击面和可审计的开源代码库相结合，两家公司正在将他们的集成推向企业安全审查。该堆栈的设计使得如果代理尝试容器逃逸或触发未知漏洞，它仍然在一个可丢弃的、由 MicroVM 支持的沙盒中运行，该沙盒可以在不影响其他工作负载或泄露主机秘密的情况下重置。批评者指出，仅靠沙盒不足以实现“代理安全”。他们强调在此之上需要细粒度的身份验证和授权。Docker 和 NanoClaw 都不会对此提出异议，但他们坚持认为强大的隔离是任何更高级别安全控制的必要基础。他们没有错。

要开始在 Docker Sandboxes 上使用 NanoClaw，开发人员可以访问 [NanoClaw 的 GitHub 存储库](https://github.com/qwibitai/nanoclaw) 和官方 [Docker Sandboxes 文档](https://docs.docker.com/ai/sandboxes/get-started/)。