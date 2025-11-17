<!--
title: OpenAI 神迹！Fluent Bit 巧调，3万CPU核心满血复活！
cover: https://cdn.thenewstack.io/media/2025/11/422018ea-fabian_ponce.jpg
summary: OpenAI优化Fluent Bit，通过禁用fstatat64函数，释放了30,000个CPU核心，凸显大规模系统小优化的巨大价值和性能分析的重要性。
-->

OpenAI优化Fluent Bit，通过禁用fstatat64函数，释放了30,000个CPU核心，凸显大规模系统小优化的巨大价值和性能分析的重要性。

> 译自：[OpenAI Recovers 30,000 CPU Cores With Fluent Bit Tweak](https://thenewstack.io/openai-recovers-30000-cpu-cores-with-fluent-bit-tweak/)
> 
> 作者：Joab Jackson

亚特兰大 — 当系统规模足够大时，即使是非常小的优化也能带来巨大的节省。

这是 OpenAI 技术人员 [Fabian Ponce](https://x.com/fabianmponce) 在本周于亚特兰大举行的 [KubeCon+CloudNativeCon North America 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event) 主题演讲前向观众传达的教训。

## OpenAI 规模化下的可观测性挑战

OpenAI 的 ChatGPT 的每次迭代都带来了巨大的改进，以及更多的 Kubernetes 集群和更大的流量——“还有数量级更多的遥测数据来保持所有系统的运行，” Ponce 说。

为了让所有系统平稳运行，OpenAI 需要“海量的遥测数据，并确保其在规模化时快速、可查询且可操作”，他说。

## Fluent Bit 在数据遥测中的关键作用

[OpenAI](https://thenewstack.io/openais-sam-altman-sees-a-future-with-a-collective-superintelligence/) 在每个 Kubernetes 节点上运行 [Fluent Bit](https://thenewstack.io/how-to-deploy-fluent-bit-in-a-kubernetes-native-way/)，这是一个由 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) 管理的**可观测性**平台。它处理日志文件，用网络流样本丰富它们，格式化结果并将其发送到适当的数据存储。

通过这种架构，Fluent Bit 每天生成 10PB 的数据，存储在 [Clickhouse](https://thenewstack.io/moving-from-c-to-rust-clickhouse-has-some-advice/) 上。

## 巨大增长背景下的资源效率驱动

Ponce 承认，OpenAI 对 GPU 有着“绝对无法满足的胃口”。OpenAI 首席执行官 [Sam Altman](https://thenewstack.io/openais-sam-altman-ai-is-now-ready-for-the-enterprise/) 计划让公司在今年年底前使用超过 100 万个 GPU，并[承诺将这一数字增加 100 倍](https://x.com/sama/status/1947057625780396512)。

所有这些 GPU 也需要 CPU 来运行。

因此，尽管有这些[巨大的采购订单](https://techcrunch.com/2025/11/06/sam-altman-says-openai-has-20b-arr-and-about-1-4-trillion-in-data-center-commitments/)，但公司的可观测性工程师们仍然注重高效利用资源。因此，其中一个任务是让 [Fluent Bit](https://fluentbit.io/) 尽可能“精简”。

## 使用 perf 发现令人惊讶的 CPU 瓶颈

利用 [perf](https://www.brendangregg.com/perf.html)（一个用于收集性能数据的 Linux 工具），**可观测性**团队查看了 Fluent Bit 正在使用的 CPU 周期。Ponce 推测 Fluent D 大部分工作都集中在准备和格式化传入数据上。

但令 Ponce 惊讶的是，情况并非如此。相反，至少 35% 的数据被一个单一函数 (`fstatat64`) 占用，该函数的作用是在读取日志文件之前确定其大小。

于是，团队关闭了这项功能——结果立竿见影：

[![](https://cdn.thenewstack.io/media/2025/11/b23f50ff-openai-02.jpg)](https://cdn.thenewstack.io/media/2025/11/b23f50ff-openai-02.jpg)

“结果不言自明，” Fabian Ponce 告诉大家。“我们这里有一个新的负载模式，它只用了大约一半的 CPU，却完成了完全相同的工作。”

每当写入新文件时，Fluent Bit 都会执行 `fstatat64` 来读取文件大小。

“如果进程持续逐行发出新日志，那么 Fluent Bit 将会与之竞争，并在此每次发生时继续运行 `fstatat64`，” Ponce 解释说。“这将消耗大量的额外计算资源。”

事实证明，公司并不真正需要这些信息，至少不需要如此细致的信息。

## 禁用高耗能函数的影响

虽然维护团队知道这一改变会减少 CPU 使用率，但他们可能没有意识到会节省多少资源，这或许可以原谅。

事实上，当 Fluent Bit [在全系统范围内进行修改](https://x.com/Joab_Jackson/status/1988618222376034488)后，最终“为我们的 Kubernetes 集群释放了大约 30,000 个 CPU 核心，” Ponce 说。

[![](https://cdn.thenewstack.io/media/2025/11/4d62533a-openai-03.jpg)](https://cdn.thenewstack.io/media/2025/11/4d62533a-openai-03.jpg)

“如果我们能为每个节点释放一个 CPU，那么我们也许就能在一个给定的主机中再容纳一个微服务，”他说。

团队还以其他方式优化了 Fluent Bit，尽管这次调整产生了最大的整体影响。该公司工程师正在为 Fluent Bit 准备一个补丁，允许用户指定一个更低的通知阈值。

## 性能优化的主要经验

Ponce 的收获很明确：拿出你“选择的分析器，看看幕后发生了什么”总是很有价值的。

正如著名的 Golang 程序员 [Rob Pike](https://github.com/robpike) 在他的[编程五法则](https://users.ece.utexas.edu/~adnan/pike.html)中曾建议的那样：“你无法预知程序会在哪里耗费时间。瓶颈会出现在意想不到的地方。”

在大型分布式系统中，这些小瓶颈可能代价高昂，除非它们被消除。