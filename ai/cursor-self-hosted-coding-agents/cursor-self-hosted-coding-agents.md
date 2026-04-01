<!--
title: Cursor缘何将自托管AI代理带入财富500强
cover: https://cdn.thenewstack.io/media/2026/03/e88266d5-getty-images-rqfetz0o0ya-unsplash-scaled.jpg
summary: Cursor推出自托管AI编程代理，允许代码在企业内部安全运行，解决合规性问题。此举满足财富500强及受监管行业需求，提升产品部署灵活性和安全性，加速AI编程代理普及。
-->

Cursor推出自托管AI编程代理，允许代码在企业内部安全运行，解决合规性问题。此举满足财富500强及受监管行业需求，提升产品部署灵活性和安全性，加速AI编程代理普及。

> 译自：[Why Cursor is bringing self-hosted AI agents to the Fortune 500](https://thenewstack.io/cursor-self-hosted-coding-agents/)
> 
> 作者：Paul Sawers

为了让AI编程代理有效工作，它们需要访问广泛的系统——从私有代码库和依赖项到内部工具和构建管道。然而，由于对代码和数据处理方式的安全、法律和合规性限制，许多公司不愿授予外部服务这种级别的访问权限。

正因为如此，[Cursor](https://cursor.com/)现在允许公司在其自己的基础设施中运行其[云代理](https://cursor.com/docs/cloud-agent)。这家编程平台在11月完成23亿美元融资后，[最新估值达到293亿美元](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html)，它表示此举使其代理能够在本地运行代码、测试和开发任务，同时将源代码和构建数据保留在公司自己的环境中。

“自托管代理提供了云代理的所有优势，同时具备更严格的安全控制：您的代码库、工具执行和构建工件绝不会离开您的环境，”Cursor工程师 Katia Baza 在一篇[博客文章](https://cursor.com/blog/self-hosted-cloud-agents)中写道。“对于拥有复杂开发环境的团队来说，自托管代理可以访问您的缓存、依赖项和网络端点——就像工程师或服务账户一样。”

## **让代理更贴近代码**

Cursor [是一款AI代码编辑器](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/)，由 Anysphere 开发，该公司是由麻省理工学院（MIT）的学生于2022年创立的一家初创公司。其核心产品围绕着自主编程代理，这些代理能够处理长时间运行的软件任务，包括编写代码、运行测试以及准备变更以供审查。

这些代理被设计为高度自主地工作。为此，它们需要一个完整的开发环境来运行。Cursor的云代理通过启动独立的虚拟机来处理这个问题，在这些虚拟机中，它们克隆代码库、安装依赖项、进行更改并运行测试，作为给定任务的一部分。

然而，这取决于在Cursor自己的基础设施上运行这些环境，实际上是将代码带到代理。自托管则反其道而行之，将这些相同的代理带到公司代码和系统已有的位置。

它们可以直接与内部服务、依赖项和网络受限资源进行交互，作为任务的一部分。这消除了通过外部系统路由这些交互或暴露内部基础设施的需要，同时Cursor继续协调代理的运行方式。

## 需求旺盛

关于自托管Cursor云代理的请求[已经](https://forum.cursor.com/t/running-agents-in-company-managed-cloud-environments/150016)在用户中[浮现了数月](https://forum.cursor.com/t/self-hosted-cloud-agents/151880)。在论坛帖子和[社区讨论](https://www.reddit.com/r/cursor/comments/1psie9e/can_you_self_host_cloud_agents/)中，开发者们询问了在自己的环境中运行这些代理的问题，通常是为了避免外部暴露代码或更轻松地连接到内部系统。

其中一些讨论也强调了在这种背景下“自托管”的含义局限性。在本地运行核心代理逻辑是一回事；管理编排、生命周期和用户界面是另一回事。Cursor的云代理将这些组件捆绑在一起，使得完全独立的设置变得困难。

尽管如此，Cursor的更新至少弥补了部分差距。许多公司，特别是在受监管的行业中，被限制与第三方服务共享源代码或构建环境。即使技术上可行，内部政策也可能限制允许访问的工具。

自托管并不能消除所有挑战。公司仍然需要部署和管理这些代理运行的基础设施，并且代理的规划和协调仍然在Cursor的云端进行，只有执行是在本地处理的。

虽然最清晰的用例是针对需要将代码和系统保留在自己网络内的公司，但Cursor也正在利用对在个人机器上本地运行编程代理日益增长的需求，这一点反映在[最近OpenClaw等项目引发的热潮](https://thenewstack.io/openclaw-github-stars-security/)中。

事实上，Cursor在其[官方文档](https://cursor.com/docs/cloud-agent/self-hosted)中明确阐述了这种用例：
> > “随处运行Cursor——在您的笔记本电脑、开发盒或远程虚拟机上启动一个工作器。您将获得一个使用您的本地环境、依赖项和网络访问权限的云代理。”

因此，实际上，Cursor正在为用户提供更大的灵活性，使其代理能够在不同环境中运行，从而扩展了产品的部署范围——并消除了一个关键的采用障碍。

Cursor表示，自托管云代理目前支持每个用户最多10个工作器，每个团队最多50个，更大规模的公司级部署可根据请求提供。一旦在目标环境中设置好工作器，就可以通过Cursor仪表板启用自托管代理。

![在Cursor仪表板中选择“自托管”](https://cdn.thenewstack.io/media/2026/03/9e1115c8-self-hosted-og-image.png)

***在Cursor仪表板中选择“自托管”***

## 前沿领域

Cursor转向自托管代理的举动，是其更大努力的一部分，旨在使其工具在迄今难以触及的环境中可用。

该公司一直在扩展其代理能力，包括可以处理代码审查、错误分类和代码库中其他日常任务的[“常驻”代理](https://thenewstack.io/cursor-agents-developer-workflows/)。它还[开源了专注于安全的代理模板](https://thenewstack.io/cursor-open-sources-security-agents/)，允许团队定义代理如何与敏感代码和系统交互。

这些举动正值来自独立编程工具和主要模型提供商（包括 OpenAI、Anthropic 和 Google）的竞争加剧之际，这些提供商正在他们开发和控制的模型之上构建自己的代理系统。

这种动态有助于解释为什么Cursor也在努力控制其更多的技术栈。这包括[Composer 2](https://cursor.com/blog/composer-2)，一个最近发布的模型，旨在[以更低的成本处理更长的编程任务](https://thenewstack.io/cursors-composer-2-beats-opus/)。它减少了对第三方前沿模型的依赖，但[在Cursor承认](https://venturebeat.com/technology/cursors-composer-2-was-secretly-built-on-a-chinese-ai-model-and-it-exposes-a)其构建在月之暗面 Kimi K2.5（一个中国开放权重模型）之上且发布时未披露后，引发了审查。

因此，对于Cursor而言，挑战或许在于既要使其产品差异化，又要消除限制其使用方式和地点的障碍。该公司表示，其更广泛的平台目前被超过三分之二的财富500强公司使用，而像 Notion 和 Brex 这样的公司已成为其自托管云代理的早期采用者，这表明在具有更复杂基础设施和安全要求的团队中存在需求。

“自托管云代理是使编程代理达到企业级就绪状态的重要一步，” Notion 的软件工程师 Ben Kraft 在博客文章中写道。“在像 Notion 这样的大型代码库中，在我们的云环境中运行代理工作负载，使代理能够更安全地访问更多工具，并省去了我们团队维护多个技术栈的需求。”