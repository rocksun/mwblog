<!--
title: Unikernel：下一代AI云负载的破局之道？
cover: https://cdn.thenewstack.io/media/2025/09/0bdb1432-unikraft.png
summary: Vercel投资，Prisma利用Unikraft独核技术。其优势为极速启动、低资源占用、高安全与成本效益，适用于数据库和AI工作负载，且可与Kubernetes集成管理。
-->

Vercel投资，Prisma利用Unikraft独核技术。其优势为极速启动、低资源占用、高安全与成本效益，适用于数据库和AI工作负载，且可与Kubernetes集成管理。

> 译自：[Are Unikernels the Answer for Next-Gen AI Cloud Workloads?](https://thenewstack.io/are-unikernels-the-answer-for-next-gen-ai-cloud-workloads/)
> 
> 作者：Joab Jackson

没人喜欢等着应用程序启动，或者数据库引导。Vercel 肯定不喜欢。Prisma 也不喜欢。

Vercel 的风险投资部门投资了 Unikraft，一家基于同名 Linux 基金会 unikernel 技术的云托管公司。该公司本月早些时候完成了 600 万美元的种子轮融资，其中包括 Vercel（一个面向前端开发者的云平台）的一笔投资。在这次交易中，Unikraft 还可以咨询 Vercel 在运行基于云的内容分发网络方面的专业知识。

而 Prisma，一家提供 [Postgres 数据库系统](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/) [无服务器](https://thenewstack.io/serverless/) 云服务的公司，甚至已经将 unikernel 投入使用。

事实上，基于 unikernel 的 Prisma Postgres 实例的微小占用空间，让该公司能够为好奇的用户提供免费套餐。

## Prisma 如何利用 Unikernels 提升数据库性能

通过网络运行数据库或任何时间敏感型应用程序，需要超低延迟和快速启动时间。

为此，Prisma 构建了一个技术栈，利用 [Cloudflare Workers](https://thenewstack.io/cloudflare-launches-workers-unbound-serverless-with-unthrottled-cpu-usage/) 边缘服务，在专用 unikernel 中运行每个数据库。该公司使用了基于 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) 支持的开源项目的 [Unikraft](https://github.com/unikraft/unikraft) SDK，通过 [Docker Compose](https://thenewstack.io/acorn-from-the-eyes-of-a-docker-compose-user/) 组装虚拟机，并将其部署到 [Unikraft Cloud](https://unikraft.com/blog/unikraft-cloud/) 上。

[Unikernels](https://thenewstack.io/why-the-unikernel-might-outpace-generic-linux-for-cloud-native-ops/) 是轻量级、单一用途的虚拟机。每个虚拟机只包含应用程序和运行该应用程序所需的最少量内核。

这种方法使 Prisma 能够在单个服务器上运行数千个 PostgreSQL 实例，并在不需要时将其缩减到零实例。

“这使得 Prisma 能够以每实例一小部分成本提供数据库，”Unikraft 公司的联合创始人兼首席执行官，也是 Unikraft 项目的最初研究人员之一 Felipe Huici 说。

![](https://cdn.thenewstack.io/media/2025/09/53c9487a-unikraft.gif)

## Unikernels 与容器：理解差异

Unikernels 大约在十年前曾获得一些关注，但在 [Docker 日益普及](https://thenewstack.io/docker-fork-talk-split-now-table/) 的热潮中几乎被遗忘。

这两种技术相似。它们都可以托管应用程序和支持库。但容器共享宿主机的操作系统，而每个 unikernel 都是一个拥有自己精简操作系统的“微型虚拟机”（microVM）。

在设计上，unikernel 是一个单地址空间二进制对象：它们 [没有](https://unikraft.org/docs/concepts) 传统操作系统中内核空间和用户地址空间的分离。这使得 [应用程序执行速度大大加快](https://thenewstack.io/beam-me-up-unikernels/)，甚至比传统容器技术更快。

unikernel 的概念通过 2013 年的一篇论文《[Unikernels：适用于云的库操作系统](https://dl.acm.org/doi/10.1145/2490301.2451167)》演变为目前的状态，该论文催生了 [MirageOS](https://thenewstack.io/qa-lars-kurth-unikernels/)，它是包括 Unikraft 本身在内的许多现代 unikernel 项目中的第一个。2016 年，[Docker 收购了 Unikernel Systems，](https://thenewstack.io/dockers-unikernel-purchase-changing-role-os/) 该公司维护着 MirageOS 的一个分支。Docker 随后在其对延迟敏感的本地应用程序（例如 [HyperKit](https://github.com/moby/hyperkit)）中使用了这项技术。

但当时的容器技术 [如此令人惊叹](https://thenewstack.io/shining-historical-lens-containers/)，能够使工作负载具有可移植性，以至于 unikernel 似乎显得多余。Unikernel 也需要大量的额外工作：对其工具和调试能力不足的批评不绝于耳。对于系统架构师来说，另一个无法接受的问题是其对 POSIX 标准（所有 Linux 系统的通用语言）的支持不足。

## Unikernels 在下一代云和 AI 工作负载中的应用

但是，面向新兴 AI 市场的新一代高度分布式云应用程序能否让 unikernel 变得有价值？这正是 Unikraft 所押注的。Huici 说，如果你正在将应用程序打包到大量的容器中，你可能需要重新审视一下 unikernel。

例如，AI 工作负载将非常适合。它们倾向于在大量容器上运行，并频繁地在在线和离线状态之间切换。

“所以如果你在做基础设施，你必须在数据中心里有成千上万的服务器，以满足随时都在启动和关闭的数百万个微小事物。这对标准基础设施来说是一个巨大的挑战，”Huici 说。

Huici 指出，unikernel 镜像比容器镜像更小、更快、更安全，启动时间以毫秒计，吞吐量比普通的 Linux 高出 50% 到 100%。

## Unikernels 的优势：速度、安全性与成本效率

这些特性巧妙地解决了 Prisma 的许多问题。由于 [Unikernels](https://thenewstack.io/beam-me-up-unikernels/) 启动更快，新实例可在几毫秒内准备就绪，而不是启动容器化版本的 Postgres 所需的几十秒。此外，[安全占用空间](http://unikernel.org/blog/2017/unikernels-are-secure) 更小，unikernel 可以为性能进行定制，并且它们在服务器内存中占用的空间也更少。

在 Prisma 的案例中，unikernel 还消除了可能困扰微服务和 Java 应用程序的 [冷启动问题](https://thenewstack.io/how-to-conquer-cold-starts-for-better-performance/)。在没有工作负载时保持虚拟机或容器运行可能会成本过高，但将其关闭会在新请求到来时导致延迟。

相比之下，由于其微小的占用空间，在服务器上保持 unikernel 运行的成本极低。

unikernel 架构还允许 Prisma 将连接池放置在运行 Prisma Postgres unikernel 实例的同一台机器上，从而节省了昂贵的网络跳跃。

## 通过 Kubernetes 集成管理 Unikernels

由于最近与 Kubernetes 的集成，Unikraft 平台进一步减轻了管理负担，使管理员能够与其他资源一起管理 unikernel。每个实例都作为一个独立的节点运行，你可以将所有 Kubernetes 伸缩逻辑应用到这些节点上，使它们像任何其他容器一样易于管理。