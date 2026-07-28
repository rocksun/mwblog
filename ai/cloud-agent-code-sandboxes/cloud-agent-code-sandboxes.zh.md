Google Cloud 在本月初于柏林举行的 WeAreDevelopers 世界大会上宣布，[Cloud Run 沙箱](https://cloud.google.com/blog/topics/developers-practitioners/google-cloud-run-sandboxes-are-in-public-preview)已进入公开预览阶段，这距离 AWS 发布其版本仅过去几周。这两个沙箱都回答了同一个问题：*代理刚刚编写的代码实际上应该在哪里运行？*

这之所以重要，是因为两家超大规模云服务商在同一季度推出沙箱，补齐了这一拼图。现在，四大云服务商（AWS、Google Cloud、Microsoft Azure 和 Cloudflare）都提供了作为原生原语的隔离代码执行环境，并且它们展示了截然不同的隔离堆栈和生命周期模型。

## 四朵云，四种隔离技术，一种产品形态

AWS 在 Firecracker 之上构建了 [Lambda MicroVMs](https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/)，为每个会话提供一个专用虚拟机，运行时间最长可达 8 小时，并具备保留内存、磁盘和运行进程的挂起-恢复周期。Google 采取了两种方式：将 gVisor 内核拦截用于 GKE Agent Sandbox，而 Cloud Run 则在现有的 Cloud Run 实例内增加了一个轻量级的隔离执行边界。

Microsoft 在这一模式上起步较早。Azure Container Apps 的[动态会话](https://learn.microsoft.com/en-us/azure/container-apps/sessions)自 2024 年起就在 Hyper-V 边界上运行，Microsoft 报告称仅 Copilot 每天就消耗超过 40 万个此类会话。Cloudflare 基于容器构建了沙箱，每个沙箱都在其独立的虚拟机中隔离，并通过 Workers 和 Durable Objects 进行控制。

四家供应商，四种关于安全边界应该归属何处的真实架构分歧。它们销售的产品都是一样的：提交不可信的代码，平台将其在远离调用应用程序的地方隔离运行，凭据暴露也受到独立管理。

## 在 Cloud Run 上，沙箱成为了一个标志

Cloud Run 的实现让这种转变变得清晰。部署命令上的 `--sandbox-launcher` 标志会在容器内挂载一个位于 `/usr/local/gcp/bin/sandbox` 的沙箱二进制文件，应用程序通过普通的子进程调用来执行它。Google 不对该功能收取额外费用，因为沙箱借用了已分配给运行实例的 CPU 和内存。Google 报告了一个演示：一个 Cloud Run 服务启动、执行并停止了 1000 个沙箱，每个沙箱平均耗时 500 毫秒。

Google 自己的公告将此替代方案描述为：不必在容器集群上构建复杂的沙箱基础设施，也不必付费购买专门的第三方 microVM 运行时。这句话针对的是一类供应商。他们在共享内核的容器与启动需要几分钟的虚拟机之间的空隙中建立了真正的业务。这四家供应商现在都提供托管沙箱执行环境，尽管它们的封装和定价各不相同。

## 隔离是容器化边界，而非治理层

Firecracker 虚拟机将生成的代码与宿主机和其他会话隔离；凭据和网络访问仍然是配置决策。它对于代码如何处理开发者刻意给予的凭据无能为力，治理处于完全独立的层级。容器化边界设定了你可以安全授予多少自主权的上限，这是问题中较容易解决的一半。

供应商限制在商品化后依然存在，且各具特点。Lambda MicroVMs 在五个区域的 Graviton 上运行且上限为 8 小时，因此需要 x86 或更长运行时间团队仍需自行编排。Cloud Run 沙箱共享父实例的 CPU 和内存，这意味着失控的脚本会与生成它的服务竞争。如果这些供应商特定的限制保持得如此严格，中立的多云沙箱仍有其市场价值，这读起来像是一场永远无法完成的商品化过程。

每家云服务商现在都同意代理不应该在宿主机上运行代码，这使得讨论的焦点转移到：谁来管理代码在被安全隔离后所做的事情。