<!--
title: NixOS: Linux系统与包管理新结合
cover: https://cdn.thenewstack.io/media/2023/12/71786ca2-josh_rossso-kubecon23-1024x717.jpg
-->

NixOS Linux发行版承诺跨硬件平台提供更快的可重复构建，但有一定的学习曲线。

> 译自 [NixOS: A Combination Linux OS and Package Manager](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/)，作者 Joab Jackson。

如果您准备以一种新的方式来思考基于容器的应用程序的构建和部署，那么 NixOS Linux 发行版提供了在不同类型的系统上进行更快速可重复构建的承诺。

NixOS 是一款 Linux 发行版，使用自己的打包系统 Nix 来构建操作系统和支持其他 Linux 应用程序，它采用声明式模型和函数式构建语言。尽管 [NixOS](https://nixos.org/) 有许多优点，但 Reddit 的工程师 Josh Rosso 在 KubeCon+CloudNativeCon 的技术会议上指出，将 NixOS 引入到类似 Reddit 这样的环境中仍存在一定困难。

NixOS 通过声明式添加方式构建操作系统，可以精确控制系统的组成。软件工程师 Jethro Kuan 认为这使得他总是知道系统上有哪些组件。NixOS 最新版本 23.11 已经发布，创业公司 Flox 正在将它商业化，面向企业和开发者用户。

YouTube 是流媒体技术快速发展的见证，订阅 TheNewStack 的 YouTube 频道可以收看最新的技术访谈、演示等内容。

Nix 可以用于基础设施即代码(IaC)。它使用声明式蓝图快速构建操作系统或基于容器的应用，支持原子升级和回滚。Nix 的这种可重现性日益受到关注。GitHub 报告显示，NixOS/nixpkgs 连续两年成为贡献者最多的开源项目。云原生计算基金会的数据也显示，Nix 的提交数量超过了 Kubernetes。

Reddit 的 Josh Rosso 最初在配置文件丢失后接触到 Nix。他演示了如何用 Nix 设置虚拟化、虚拟机和容器镜像，并组合运行以构建 Kubernetes 集群，简化了流程。

Nix 的模块模型允许构建系统API，用户可以向这些API插入值进行复杂的操作。Nix 有模块和软件包，模块用于在特定平台上安装这些打包好的软件包，如 libvert 库。NixOS中有超过8万个软件包可用。Nix 通过哈希系统跟踪构建，并可以快速重建。

Josh Rosso演示了如何用Nix设置Kubernetes。他配置了一个装有Kubernetes、containerd 和 kubeadm 的虚拟机磁盘镜像，启动了3个实例。安装网络插件Cilium可以得到一个工作的Kubernetes集群。Nix中有像dockerTools这样的工具用于构建分层的容器镜像。

Nix 使用纯函数实现了“无限回归”。这些 Nix 语言函数接受输入、构建输出。尽管 Nix 功能强大，但 Rosso 由于以下原因并不会在 Reddit 使用它:已经有类似的面向容器的 Linux 发行版，如 BottleRocket 和 Flatcar;Nix API 存在学习曲线，新用户可能觉得晦涩;Nix 还需要更好地吸引终端用户。所以现阶段，Nix 的价值还不足以弥补组织为适应它而学习的代价。值得一提的是，Rosso 的演讲讲得非常精彩。
