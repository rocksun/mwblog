<!--
title: Vercel新增常驻Worker以运行更多后端任务
cover: https://cdn.thenewstack.io/media/2026/10/b6c422ed-screenshot-2026-10-15-at-11.25.32-am.png
summary: Vercel在Ship大会上推出了常驻后台任务服务Daemons的公开测试版，全面推出Python支持，并让AI智能体的持久化存储服务Drives正式商用，旨在帮助开发者在平台上运行更多复杂的后端负载。
-->

Vercel在Ship大会上推出了常驻后台任务服务Daemons的公开测试版，全面推出Python支持，并让AI智能体的持久化存储服务Drives正式商用，旨在帮助开发者在平台上运行更多复杂的后端负载。

> 译自：[Vercel adds always-on workers to run more of your backend](https://thenewstack.io/vercel-faces-its-daemons/)
> 
> 作者：Frederic Lardinois

Vercel 正在为开发者提供更多在其平台上运行后端的选择。

在周四于旧金山举行的 Ship 大会上，该公司推出了 Daemons，这是一项用于持续运行后台 Worker 的新服务，并使其 [Python 支持](https://vercel.com/docs/functions/runtimes/python) 正式全面可用。

它还使其针对 AI 智能体的持久化存储服务 Drives 正式全面可用。

## 常驻 Worker，基于拉取的任务

目前处于公开测试阶段的 Daemons 允许开发者部署容器，并指定每个区域运行的实例数量。Vercel 确保这些进程持续运行，并在它们退出或崩溃时将其重启。在发布时，它支持基于拉取的工作负载，允许 Worker 从队列或数据库获取任务，然后在任务到达时进行处理。

Vercel 首席技术官 Malte Ubl 告诉 *The New Stack*，该公司当前的推动方向是更深入地切入技术栈底层。

他说：“让我们看看人们在做什么，并确保其中更大一部分人可以只使用 Vercel 作为他们的基础设施提供商。”

该公司已经提供了 [队列](https://vercel.com/docs/queues) 和 [持久化工作流](https://vercel.com/docs/workflows)，而其 [服务](https://vercel.com/blog/vercel-services-run-full-stack-on-vercel) 功能允许开发者将前端和后端部署在一起。

Ubl 表示，这些功能涵盖了请求驱动的工作，但并非复杂后端所做的一切都能涵盖。他说：“真正不太适合这一范畴的是你在复杂的后端工作负载中发现的内容，你基本上希望在某种队列上进行处理。”

他以 Vercel 自己的部署管道作为此类工作负载的示例。

![](https://cdn.thenewstack.io/media/2026/10/8b5dcd02-backend-blog-diagram-light-1024x355.webp)

图片来源：Vercel.

Ubl 说：“当你调用我们的 API 进行部署时，我们不会在处理你请求的那个进程中进行该部署，因为我们实际上无法进行无限数量的并发部署。”GitHub 速率限制是退回的原因之一，并且 Vercel 现有的计算原语没有给开发者提供针对该类 Worker 的“对并发数量的良好控制”。

他说，有了 Daemons，“它们出现，开始说，我在这里，给我工作，然后它们就随之进行处理。”

该公司使用 Daemons 的示例将 Next.js 前端与 Python API 以及容器化的视频处理器结合起来。该容器打包了 Python 依赖项和 FFmpeg 媒体框架，然后从 Vercel Queues 拉取任务以生成播放文件和缩略图。

Ubl 说，转码是一个典型案例，具有“极端 CPU 密集型的工作负载”，其中“我只需要我希望 CPU 始终保持 100% 的计算机”。

这也使 Daemons 处于 Vercel 沙盒的对立面。他谈到 Daemons 时说：“它们几乎是临时性的对立面。对于临时性，你有沙盒。”Daemons 保持常驻，但不会被来自互联网的请求所调用。相反，它们会主动获取工作。

开发者可以通过 Git 或 Vercel CLI 进行部署。Vercel 构建容器镜像并将其存储在其 [容器注册表](https://vercel.com/docs/container-registry) 中。

Ubl 说，该公司自身在其控制平面 API 上运行了相当一部分。这大约占每月十亿次请求，Vercel 现在开始将其许多异步工作负载迁移到 Daemons 上。

他承认，Vercel 并没有发明这种模式，“我们发布它是因为人们非常需要这个。”

## 托管运行时还是容器

如果你对 Vercel 生态系统有深入了解，你可能会想这一切与 [Vercel Functions](https://vercel.com/docs/functions) 有何关联。

Vercel 表示，自从 [容器支持](https://vercel.com/docs/functions/container-images) 进入公开测试以来，已有 5,000 个团队进行了 150,000 次容器部署。容器允许开发者将应用程序与其自己的运行时和系统库打包在一起，从而扩展了他们可以部署的软件范围。

Ubl 认为，这里的权衡是谁来保持镜像的最新状态。Ubl 表示，对于 Node、Bun 或 Python 的托管运行时，Vercel 会在客户无需重新部署的情况下应用安全版本。对于容器，“你确实必须重新部署。这最终是你的责任，”他说。“从我们的角度来看，这只是字节。”

同时，Python 支持现在已对包括 FastAPI、Flask 和 Django 在内的框架全面可用。应用程序在标准的 CPython 上运行，并带有 PyPI 依赖项，而 Vercel 则负责框架检测、构建和扩缩容。该公司表示，已有 150,000 个团队在其平台上运行 Python 后端，其中包括来自 OpenAI、Polymarket 和 Exa 的工程师。

## 在环境变更中幸存的文件

Vercel Drives 是智能体如何改变诸如存储等后端服务需求的绝佳示例。Vercel 的 [Drives](https://vercel.com/docs/sandbox/concepts/drives) 服务将智能体的文件与其代码执行的 [沙盒](https://thenewstack.io/frontend-ai-vercel-abstracts-model-chaos-in-one-interface/) 隔离开来。智能体可以在新的沙盒中挂载驱动器，更改运行时，并继续使用它已经创建的文件。

Ubl 说：“我不会宣称它是行业首创，但它无疑是新型存储产品的一个实例。”他将其描述为 EBS 风格的网络驱动器和对象存储的混合体，他认为这是 AWS 所不提供的。

他说，写入操作总是落在本地 NVMe 磁盘上，并异步流式传输到对象存储，而读取操作则在数据已经存在时来自本地磁盘——或者逐块流式传输。

他说：“你有大量的独立磁盘，由于它们只是 S3 中的文件，因此运行成本极低。”

驱动器与快照

Ubl 说，包括 Vercel 在内的许多沙盒提供商都提供快照，但他认为驱动器是更好的模型。

他说：“快照的问题在于它们会变得非常大，因为你最终会拍摄每次都相同的各种东西的快照。在实践中，智能体真正做的是有一个目录，我不知道，/home/agent。这就是一切所在。其他一切它们其实并不关心。”

他说，挂载那个单一目录意味着每个智能体都可以从相同的缓存基础镜像启动。“对它们来说更便宜，速度更快。基本上没有什么缺点。”

Ubl 补充说，Vercel 并没有移除快照，但它正在鼓励客户进行切换。

Drives 允许这些智能体重复使用彼此的工作。一个智能体可以准备一个数据集，而其他智能体则挂载只读副本来分析它或生成报告，并将其结果单独保存。智能体还可以 [fork 一个驱动器](https://vercel.com/docs/sandbox/concepts/drives#forking-a-drive) 以在独立的可写工作区中测试不同的方法。这些 fork 不会合并回原始驱动器。

Ubl 说，在实践中，这意味着告诉智能体在哪里写入。“当你使用沙盒时，你总是会告诉你的智能体它应该在哪里写入东西，”他说，通常是诸如 /workspace 之类的根目录。“基本上每个提示词都会以那句话开头，然后那正是你挂载到持久化驱动器中的东西，就是这样。”

Drives 和 forking 现已全面可用。该服务适用于所有 Vercel 计划，默认容量为 1 TiB（Hobby 计划为 1 GiB），配置最高可达 16 TiB。

对于已经将其前端部署在 Vercel 上的团队来说，在其上运行 Worker 或 Python API 会成为一个更容易做出的决定。它能够在平台上保留的每个额外的后端服务，都是其开发者少维护的一个部署系统。