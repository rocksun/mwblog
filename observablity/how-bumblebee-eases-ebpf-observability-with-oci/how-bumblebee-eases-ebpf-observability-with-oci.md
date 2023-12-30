<!--
title: 利用OCI简化eBPF可观测性
cover: https://cdn.thenewstack.io/media/2023/10/6d6ac859-img_0194.jpg
-->

BumbleBee简化了构建和运行分布式eBPF程序的过程，将其封装到OCI镜像并发布到符合OCI标准的仓库中。

> 译自 [How BumbleBee Eases eBPF Observability with OCI](https://thenewstack.io/how-bumblebee-eases-ebpf-observability-with-oci/)，作者 B. Cameron Gain 是ReveCom Media的创始人兼首席分析师。他对计算机的痴迷始于20世纪80年代初，在当地的街机中黑客攻击Space Invaders游戏机，以25美分的价格整天游玩。然后...

开源工具 BumbleBee 扩展了 [eBPF 的范围](https://thenewstack.io/what-is-ebpf/)，并通过使用 [Open Container Initiative](https://thenewstack.io/open-container-initiative-creates-a-distribution-specification-for-registries/)（OCI）[镜像规范](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/)增强了其在各种环境中的适应性。

![Zoom](https://cdn.thenewstack.io/media/5a93c107-bumblebee.svg)

*开源 BumbleBee 扩展了 Extended Berkeley Packet Filter（eBPF）的范围。*

实质上，[BumbleBee](https://github.com/solo-io/bumblebee) 简化了构建和运行分布式 eBPF 程序的过程，将它们封装为 OCI 镜像，然后发布到符合 OCI 标准的仓库中。

它还允许您将事件公开为指标，使得更容易将您的指标与其他可观测性工具连接和可视化。

Istio 技术监督委员会成员、开源高级总监 [Lin Sun](https://www.linkedin.com/in/lin-sun-a9b7a81/) 在去年九月份的[比尔包开源峰会](https://osseu2023.sched.com/)上主持了一个研讨会，展示了这项技术的用途。

Sun 展示了 BumbleBee 使用 Berkeley Packet Filter（BPF）内核空间代码，并将现有代码转换为指标。

使用 BumbleBee，您可以更轻松地使用 OCI 镜像在多个内核上执行分布式 eBPF 程序，包括部署运行时。具体来说，在实际操作研讨会期间，参与者能够使用 BumbleBee 将 eBPF 内核空间代码转换为[指标以及执行](https://thenewstack.io/how-performance-metrics-and-distributed-tracing-will-drive-user-experience/)其他任务。

## 像 Docker 一样，但用于 eBPF

BumbleBee 的设计目标是[为 eBPF 开发人员提供 Docker 体验](https://thenewstack.io/ebpf-offers-a-new-way-to-secure-cloud-native-systems/)，Sun 说道。

使用 BumbleBee，用户可以将 eBPF 程序构建为 OCI 镜像，将 eBPF 程序发布为 OCI 镜像到任何符合 OCI 标准的仓库。您还可以将您的 eBPF 程序作为 OCI 镜像运行。

“这正是你熟悉的 Docker 体验：构建镜像，推送到仓库，然后运行 Docker 镜像。”  Sun 说。因此，我们相信 BumbleBee 确实为 [eBPF](https://thenewstack.io/solo-io-brings-docker-like-experience-to-ebpf-with-bumblebee/) 社区提供了这种类似 Docker 的体验，使您能够学习、构建并发布您的 eBPF 程序，供朋友、家人和同事使用。

BumbleBee 使用 [libBPF 内核空间代码](https://docs.kernel.org/next/bpf/libbpf/libbpf_overview.html)，并将现有的 eBPF 内核空间代码转换为指标，如上所述。

![Zoom](https://cdn.thenewstack.io/media/2023/10/77a115ba-capture-decran-2023-10-03-171810.png)

## 一次编写，随处运行

BumbleBee 利用了[一次编写，随处运行（CO-RE）](https://nakryiko.com/posts/bpf-core-reference-guide)框架，因此您必须在支持 CO-RE 的较新 Linux 内核上运行 BumbleBee。您还可以将一些[最初为与旧内核相关的 bcc-to-libBPF 工具](https://thenewstack.io/greg-kroah-hartman-lessons-for-developers-from-20-years-of-linux-kernel-work/)编写的现有 eBPF 程序迁移到支持 BumbleBee 的内核上运行（使用环形缓冲区需要 Linux 5.8 及更高版本）。

![Zoom](https://cdn.thenewstack.io/media/2023/10/e7d3ef0d-capture-decran-2023-10-03-173204.png)

以下是研讨会涵盖的内容：首先，使用 BumbleBee 构建并部署了一个应用程序。这涉及使用 BumbleBee 创建应用程序并将其推送到 OCI 仓库。

此外，与会者能够通过 Prometheus 用户界面（UI）看到 BumbleBee 收集的内核指标。研讨会参与者还看到了如何将多个内核空间代码组件捆绑并打包为单个 OCI 镜像。

在第一个研讨会中涵盖的项目，这里唯一涉及的项目，是检测“oomkills”程序的项目，该程序[终止了超出其内存分配的程序](https://spacelift.io/blog/oomkilled-exit-code-137)。在这个程序中，使用 bcc，通常有用户空间代码和内核空间代码，因此每个工具有两个文件，例如：

```
oomkill.c
oomkill.bpf.c
```

该程序最初是使用 HashMap 编写的，但 HashMap 的性能不如环形缓冲区。Sun 解释了将 HashMap 迁移到环形缓冲区的必要性。在研讨会期间，该程序还从 perf 缓冲区迁移到环形缓冲区。这是因为环形缓冲区允许更好地利用 CPU 层面的资源，Sun 说。

OOM最初在 Linux 早期的时候用于检测应用程序内存不足的情况。对于 Kubernetes，OOM用于确保[集群上运行](https://thenewstack.io/run-a-google-kubernetes-engine-cluster-for-under-25-month/)的代码不会耗尽内存，如果耗尽，旧实例将替换在集群中运行的当前实例。然而，还会运行测试来确定交换的可行性。

如果 pod 没有足够的内存运行代码，或者超过了其承诺的内存，通常会“oomkilled”该 pod。同样，在这个研讨会上使用 eBPF 来检测 oomkills。

![Zoom](https://cdn.thenewstack.io/media/2023/10/5d4da88c-capture-decran-2023-09-21-120053-1024x633.png)

通过“Bee Build”命令，我首先成功编译了“oomkill.c”，然后将其写入“oomkill.o”并将 eBPF OCI 镜像保存到本地主机：

![Zoom](https://cdn.thenewstack.io/media/2023/10/fa75b228-capture-decran-2023-10-02-185050.png)

使用 BumbleBee 显示的 Oomkill 事件：

![Zoom](https://cdn.thenewstack.io/media/2023/10/fadc9423-capture-decran-2023-09-21-120714-1024x692.png)

Prometheus为使用 eBPF 检测到的 oomkills 提供其可观测性信息：

![Zoom](https://cdn.thenewstack.io/media/2023/10/9ba796ae-capture-decran-2023-09-21-120842-1024x651.png)

## 结论

从GitHub下载BumbleBee并在本地安装可能比在云端的虚拟机上运行预安装版本面临更多挑战。然而，我认为这是完全可行的。

一旦所有东西都安装好，使其运行相对无缝。我成功地运行了BumbleBee，它用于获取eBPF代码并将其推送到OCI仓库，通过监控提供可观测性数据。

其中包括“oomkill”数据，并通过Prometheus进行了跟进。所有这些都进行得非常顺利。

此外，eBPF扩展到各个领域，包括可观测性和安全性，涵盖了日益增长的各种用例。由于工具制造商正在基于eBPF构建，利用可观测性数据来检测安全漏洞，提供缓解和解决这些漏洞的方法，甚至在某些情况下处理攻击，因此eBPF变得越来越值得采用。
