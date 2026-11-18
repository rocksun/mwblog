<!--
title: 可预测的性能，还是更高的速度？
cover: https://cdn.thenewstack.io/media/2026/11/f01f76df-azure-cobalt-200-image-01-updated-1024x576.png
summary: 微软正式推出 Cobalt 200 虚拟机，搭载二代 Arm 芯片，性能提升最高达 50%，专为 AI 智能体优化，提供稳频与加速双模式及新型实例。
-->

微软正式推出 Cobalt 200 虚拟机，搭载二代 Arm 芯片，性能提升最高达 50%，专为 AI 智能体优化，提供稳频与加速双模式及新型实例。

> 译自：[Predictable performance or more speed](https://thenewstack.io/microsoft-cobalt-200-ga/)
> 
> 作者：Frederic Lardinois

微软现已正式发布其 Cobalt 200 虚拟机，该产品的 CPU 改进专为支撑 AI 智能体运行的沙盒、工具及代码执行而设计。

在周二于旧金山举行的 Ignite 大会上，微软宣布这款搭载其第二代基于 Arm 架构 CPU 的虚拟机已在 14 个 Azure 区域上线，并将在年底前扩展至 23 个区域。微软表示，与 Cobalt 100 相比，其性能提升高达 50%。

距离微软首次公布 Cobalt 200 几乎正好过去一年，距离新虚拟机[进入预览阶段](https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/)也大约过去六个月。微软的基准测试显示，在文件搜索、代码编译以及[在沙盒中执行任务](https://thenewstack.io/cloud-agent-code-sandboxes/)等工作负载下，其 AI 智能体工具的执行性能最高可达 Cobalt 100 的 1.5 倍。

微软 Azure Cobalt 副总裁 Pat Stemen 向 *The New Stack* 透露，团队在过去一年的部分时间里一直在针对这些操作调优基础设施。他表示，该芯片的大容量缓存、内存性能和物理核心本身就非常适合启动沙盒等工作负载。随后，微软“在公司内部针对这些常见操作构建了一套基准测试”，并据此对产品进行了调优。

![](https://cdn.thenewstack.io/media/2026/11/4809ba9a-01-1024x576.jpg)

## 可预测的性能，还是更高的速度

Cobalt 200 允许开发者在两种处理器模式之间进行选择。确定性模式（Deterministic mode）以稳定的 3.2 GHz 频率运行核心，而机会性模式（Opportunistic mode）则允许核心在功耗和散热余量允许的情况下达到 3.6 GHz。

微软表示，机会性模式可额外提供高达 12% 的性能，但时钟频率会有所波动。

“顺便说一句，客户非常喜欢固定频率，”Stemen 说，“他们喜欢由此带来的可预测性。”

微软建议在分布式数据和分析集群（最慢的节点往往决定整体节奏）以及性能指标要求严苛的服务中使用确定性模式。而 Web 和 API 服务、事务处理及媒体工作负载则可能从机会性模式的额外速度中获益更多。

![](https://cdn.thenewstack.io/media/2026/11/caf98dfa-image-4.png)

开发者可以在创建每台虚拟机时选择模式，也可以在之后通过 Azure 门户、命令行工具或基础设施模板进行更改。

“因此，如果你向我们购买四个核心，”Stemen 说，“你可以选择让这四个核心全部以灵活模式或确定性模式运行。”

他补充道，这种额外的性能通常在机器核心处于高负载之前都是可用的。

## 围绕 Azure 工作负载进行设计

Cobalt 200 采用台积电 3nm 工艺制造，配备 132 个 [Arm Neoverse V3 核心](https://thenewstack.io/arm-eyes-ai-with-its-latest-neoverse-cores-and-subsystems/)，虚拟机最高可扩展至 128 个 vCPU。每个 vCPU 对应一个完整的物理核心，并配有 3 MB 的私有二级缓存。该芯片还包含 192 MB 的系统级缓存和 12 通道 DDR5 内存。

Stemen 表示，从 Cobalt 100 升级到 Cobalt 200 涉及从成本优化型 Arm 核心转向性能优化型设计，同时配备了更大的缓存并提升了内存带宽。

每台 Cobalt 200 虚拟机还集成了 [Azure Boost](https://thenewstack.io/microsofts-rust-bet-from-blue-screens-to-safer-code/)，用于从主机卸载网络和存储处理任务。据微软报告，与 Cobalt 100 相比，其网络带宽提升了高达 15%，远程存储 IOPS 提升了 20%。

![](https://cdn.thenewstack.io/media/2026/11/937a6751-04-1024x576.png)

“他们需要远程存储，需要高性能网络，也需要本地 SSD，”Stemen 在谈及客户迁移到 Azure 的工作负载时说道。

Stemen 表示，团队将微软自身的工作负载拆解为更小的组件，在硬件制造出来之前就对其行为进行建模，并利用这些结果来决定缓存大小、内存配置，甚至服务器机架中的风扇选型。产品团队在最早期的规划评审阶段就会参与其中。

“从产品还仅仅停留在 PowerPoint 演示文稿阶段开始，他们就在影响产品的初期设计了，”Stemen 说。

例如，Teams 媒体处理服务报告称，其在 Cobalt 200 上的性能是 Cobalt 100 的 1.65 倍。微软表示，该服务在物理核心上实现了线性扩展，并且能够在处理流量的同时将 vCPU 利用率负载至 90%。

在微软之外，Amadeus 在其基准测试实验室中报告称，与 Cobalt 100 相比，其航班搜索吞吐量提高了 30% 以上。

## 更广泛的 Arm 工作负载

事实上，Azure Database for PostgreSQL、Azure DevOps、Azure SQL、Microsoft 365、Xbox 等众多微软服务目前已经运行在 Cobalt 之上。

Stemen 说，不久前，“客户对迁移的代价确实心存顾虑”。但自那以后，“有越来越多的证据表明这种架构行之有效，开发工具得到了改进，产品本身也同步变得更好。”

除了通用型和内存优化型虚拟机外，Cobalt 200 还正式推出了另外两个系列：高内存型 Mpsv4 系列（每个 vCPU 配备 16 GiB 内存）和存储优化型 Lpsv5 系列（配备高达 23 TB 的本地 NVMe 存储）。

“但现在我们看到市场对大型内存数据库和大型现有企业工作负载表现出了浓厚兴趣与需求，”Stemen 说，“而如今这些工作负载迁移难度的降低也起到了推动作用。”

尽管微软将继续投资 x86 芯片，但该公司表示，预计 Cobalt 200 将在“2027 年及以后占据我们新增 Azure 计算容量的很大一部分”。

开发者可以通过现有的 Azure 工具部署这些虚拟机，并将其用于虚拟机规模集或作为 Azure Kubernetes Service 节点池。