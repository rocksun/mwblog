<!--
title: Render取消AI沙盒时间限制，Vercel仍维持24小时上限
cover: https://cdn.thenewstack.io/media/2026/11/88af2b32-getty-images-1rdhxhol-xu-unsplash-scaled.jpg
summary: Render近日取消了其付费工作区中AI沙盒的持续运行时间限制，支持无限期运行并能在空闲时挂起恢复，直面竞争对手Vercel的24小时上限。同时，Render还推出了持久化工作流与共享存储等新功能，旨在为复杂的智能体工作负载提供更灵活的后端支持。
-->

Render近日取消了其付费工作区中AI沙盒的持续运行时间限制，支持无限期运行并能在空闲时挂起恢复，直面竞争对手Vercel的24小时上限。同时，Render还推出了持久化工作流与共享存储等新功能，旨在为复杂的智能体工作负载提供更灵活的后端支持。

> 译自：[Render just removed its AI sandbox time limit — and Vercel still has a 24-hour cap](https://thenewstack.io/render-vercel-ai-sandboxes/)
> 
> 作者：Amanda Caswell

Render正通过能够无限期运行的AI沙盒与Vercel展开竞争，同时推出了用于管理长期运行的智能体工作流和共享存储的新工具。

周三宣布的这一发布取消了 [Render](https://render.com/) 此前对付费工作区计划中 30 天连续运行时间的限制。Vercel 将单个沙盒会话限制在 24 小时以内，而 Render 表示其环境可以在空闲时挂起，并在恢复时保持其文件、内存和正在运行的进程完好无损。

Render 创始人兼首席执行官 [Anurag Goel](https://www.linkedin.com/in/anuragoel/) 曾是 Stripe 的工程师兼风险主管，他构建该平台是为了作为 AWS 的替代方案，同时没有那么复杂的底层架构。现在，他将这种方法延伸到了 AI 智能体，将沙盒、持久化工作流、共享存储与它们所依赖的应用程序和数据库结合起来。

并非所有功能都已准备就绪。凭证代理（Credential brokering）最初将仅向部分客户开放，沙盒的私有网络功能仍在开发中，且 Render 尚未确定其共享存储将如何处理对同一文件的并发写入。

## 可在任务中途恢复的沙盒

随着这一发布，Render 沙盒可以在长达数天的代码库迁移期间保持活动状态，或者在智能体测试整个应用程序时保持运行。

更大的区别在于沙盒需要恢复工作的时候。Vercel [将不间断会话限制在 24 小时以内](https://vercel.com/changelog/vercel-sandbox-can-now-run-for-up-to-24-hours)，虽然持久化沙盒可以重启，但它们正在运行的进程会重新开始。

Render 采取了不同的方法。该公司告诉 *The New Stack*，沙盒“在空闲时挂起，并在下一个命令唤醒时保持其文件和内存完好无损，因此智能体可以从任务中途继续，而无需重建其状态。”

> “在空闲时挂起，并在下一个命令唤醒时保持其文件和内存完好无损，因此智能体可以从任务中途继续，而无需重建其状态。”

## 绝不进入的凭证

该发布的安全功能之一是凭证代理，它在凭证离开沙盒时将其附加到智能体的出站请求中，从而使密钥永远不会进入沙盒。

当被问及这是否使 Render 与 Vercel 区别开来时（Vercel 已经通过其 Connect 服务为智能体提供了作用域凭证，并且[一直在推动其自己的供应商采用短生命周期凭证](https://thenewstack.io/vercel-oidc-static-credentials/)），该公司并未声称自己具有优势。

Render 告诉 *The New Stack*，凭证代理“不是一个竞争差异点”，并且“正迅速成为基本要求”，称其为“我们认为 Render 用户会很高兴能够访问的功能，而不是其他平台的用户会因此进行迁移的功能。”

Render 告诉 *The New Stack*，它正在“首先为一小群客户开启凭证代理，以确保体验达到我们的质量标准”，然后将在未来几周内进行扩展，同时参加测试版的每个开发人员都将获得出站控制权，可以“阻止来自沙盒的所有流量或仅允许您列出的域。”

该公司更大的论点是，沙盒远不如它周围的一切重要。该公司辩称，开发人员选择 Render 而不是 Vercel，是因为智能体通常必须在更大的产品内部运行，并执行需要保持 API 处于活动状态并保持其数据库连接的大量后台工作，以及后台工作进程、定时任务（cron jobs）和数据库本身。

## 计算灵活性，更低的复杂度

Vercel 从前端和无服务器函数（serverless functions）起步并在那里表现强劲；Render 允许这样做，但该公司告诉 *The New Stack*，Vercel 的“底层‘流体计算’模型对于运行智能体应用程序所依赖的计算密集型后端工作负载来说是不灵活且低效的”，并指出单个函数“最高可达 2 个 CPU 和 4 GB 内存”，这个上限适用于 Vercel 函数而不是其沙盒。

Render 告诉 *The New Stack*，它“为开发人员提供了 AWS 的计算灵活性，但免除了他们的复杂性。”正在从 AWS 迁移并考虑过 Vercel 的 OCMI 首席技术官 [Cristian Herrera](https://www.linkedin.com/in/cristianhg/) 告诉 Render，“Vercel 是一个不同的故事”，并补充说“如果你需要做 Next.js 之外的任何事情，你就是在与平台对抗。”

> “如果你需要做 Next.js 之外的任何事情，你就是在与平台对抗。”

Vercel 确认收到了 *The New Stack* 的置评请求，但在截稿前未提供声明。

## 能够从崩溃中恢复的工作流

Render 的新持久化工作流（Durable Workflows）允许开发人员在失败后恢复长期运行的作业，而无需重新开始。开发人员可以使用 Python 或 TypeScript 编写工作流，单个任务的运行时间长达 24 小时。该公司告诉 *The New Stack*，Render “在每个步骤完成时保存其结果”。如果进程崩溃，工作流可以使用这些保存的结果在新的机器上恢复，因此“已经成功的模型调用、支付和数据库写入不会再次运行。”

如果进程在支付完成后但在结果保存之前崩溃，仍然存在风险。Render 建议使用幂等键（idempotency keys）来防止重复扣费或数据库写入。共享文件系统（Shared Filesystems）允许沙盒和工作流任务访问相同的持久文件，即使创建它们的计算关闭后也是如此。

Render 表示该功能专为“许多智能体读取相同的代码库或数据集，每个智能体写入自己的输出”而设计。但该公司告诉 *The New Stack*，“处理对同一文件的并发写入，包括锁机制和冲突解决，是我们仍在研究的事情。”

该公司告诉 *The New Stack*，Render 表示 AWS 和 Vercel 是“新用户今天最常告诉我们他们正在离开的两个平台，他们将复杂性和[成本](https://thenewstack.io/minimax-flash-agent-costs/)视为主要因素。”Render 尚未公布显示有多少客户从 Vercel 迁移过来的数据。

> Render 表示 AWS 和 Vercel 是“新用户今天最常告诉我们他们正在离开的两个平台”