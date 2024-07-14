
<!--
title: 从零到K8s大师：Kubernetes 的 5 个必备工具
cover: https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cb3354e-7e77-4b47-a112-b644a154ab3d_1024x1024.png
-->

掌握这 3 个初学者工具和 2 个高级用户工具，领先竞争对手。

> 译自 [From Zero to K8s Hero: 5 Must-Have Tools for Kubernetes](https://cloudnativeengineer.substack.com/p/5-must-have-tools-for-kubernetes)，作者 Giuseppe Santoro。


本文将介绍 5 个必备工具，帮助你开启 Kubernetes 之旅。

列表中的前三个工具对于初学者来说绝对不可或缺。后两个工具可以让你从初学者脱颖而出，看起来像高级用户。

我将分享我对哪些工具可以让你在同事中脱颖而出，以及哪些工具不值得学习的观点。

是什么让我有资格给出这样的建议？

在过去的几年里，我花费了无数个小时尝试所有我能接触到的 Kubernetes 工具，无论是工作时间还是业余时间用于我的副项目。

我不得不承认，我是一个工具狂热者。我喜欢玩弄所有闪闪发光的工具，而 Kubernetes 生态系统中有很多这样的工具。

鉴于每天都有像蘑菇一样冒出来的新工具，我一直认为我需要一些建议，告诉我哪些工具值得学习，哪些工具不值得我花时间。

因此，我尝试了尽可能多的工具，经过多年的经验，我现在已经准备好指导其他人。

在本文中，我想要提供我在几年前刚开始使用 Kubernetes 时所缺少的指导。

所以请不要再浪费时间，让我们深入探讨这篇文章。

## 1. 浏览你的 Kubernetes 集群：K9s

我最喜欢的 Kubernetes 工具是 [K9s](https://k9scli.io/)，这是一个基于终端的 UI，可以让你与 Kubernetes 集群交互。

如果你像我一样，从小就使用“面包和... Linux”，你会欣赏使用 CLI 工具的美丽，这些工具既是开源的，又高度可定制，可以自定义皮肤、插件、命令别名和自定义键绑定。

使用 K9s 作为浏览集群的主要工具有哪些好处：

* **支持所有标准 Kubernetes 对象**: 查看和交互 pod、容器、服务、RBAC、卷、事件等。
* **CRD 支持**: 支持与自定义资源定义 (CRD) 交互。
* **随处运行**: 在任何操作系统上运行，可以使用大多数包管理器安装。
* [皮肤](https://github.com/derailed/k9s#skins): 更改 UI 的外观和感觉，以及根据你正在使用的集群和上下文更改 UI 的行为。在高级功能中，你还可以创建一个只读上下文，防止在生产集群中进行任何非故意的修改。
* [插件](https://github.com/derailed/k9s#plugins): 我个人在一段时间前使用过这个功能，当时我想解析 Kubernetes pod 中的一些 JSON 日志并以表格形式显示它们。我用 Python 创建了一个 Kubectl 插件，我称之为 [rich-json-logs](https://github.com/gsantoro/rich-json-logs#k9s-plugin)，然后将其插入 K9s。几乎是直接的。
* [命令别名](https://github.com/derailed/k9s#plugins): 命令别名不如插件强大，但可以节省一些按键。
* [自定义键绑定](https://github.com/derailed/k9s#hotkey-support): 只需一两个按键，你就可以查看特定类型的 Kubernetes 资源、调用插件、命令别名或许多其他功能。

有哪些替代方案：

* [Lens](https://k8slens.dev/): 一个付费的替代方案，提供慷慨的免费个人计划。这个桌面应用程序除了 K9s 之外没有提供更多功能，除非你拥有非常昂贵的 Pro 或企业许可证。
* [OpenLens](https://github.com/MuhammedKalkan/OpenLens): Lens 的开源版本。由于 Lens 背后的公司 Mirantis 已经放弃了开源，这个项目将不再获得任何更新。

## 2. 自动化一切：Kubectl

如果你曾经使用过 Kubernetes，你一定已经遇到过 [Kubectl](https://kubernetes.io/docs/reference/kubectl/)，Kubernetes 命令行工具。

为什么我只把它放在我的列表中的第二位？

这个工具可以完成你使用 Kubernetes 所需的一切，但它没有像 K9s 那样提供良好的用户体验。

在使用 Kubernetes 时，尤其是当你是一个 DevOps 并且处于事故处理过程中时，你必须快速行动！

鉴于我记不住 Kubectl 命令的语法，并且每个命令都需要大量输入，K9s 对于我的需求来说是一个更好的工具。

为什么我仍然建议使用 Kubectl？

每当需要编写一些与 Kubernetes 交互的自动化脚本时，Kubectl 都是我的首选工具。

最好的部分是，你不需要在这两者之间做出选择。

你可以使用 K9s 来提高速度和用户体验，使用 Kubectl 来提高可扩展性，并将它们结合起来使用。

看看下面的命令。不使用任何其他工具，我将获取所有带有标签 `app=cassandra` 的 pod 的版本标签。

```
kubectl get pods --selector=app=cassandra -o jsonpath='{.items[*].metadata.labels.version}'
```
我从 [Kubernetes 快速参考](https://kubernetes.io/docs/reference/kubectl/quick-reference/) 中获得了最后一个命令，如果你想 [准备你的认证 Kubernetes 管理员考试](https://cloudnativeengineer.substack.com/p/prepare-for-your-cka-exam-e1c33883eaf2) ，这是一个很棒的资源，因为你可以在考试中使用它。

有哪些替代方案：

K9s：我们在上一节中已经讨论过这个问题。

[Kubernetes 客户端库](https://kubernetes.io/docs/reference/using-api/client-libraries/)：如果你需要在代码中自动与你的 Kubernetes 集群交互，并且想要避免在 bash 中使用 Kubectl，你可以在你选择的语言中使用 Kubernetes SDK。

## 3. 包管理器：Krew

我的列表中的第三个工具是 [Krew](https://krew.sigs.k8s.io/plugins/)，它是 Kubectl 的官方包管理器。

我最近才了解到这个工具，但它是我武器库中的一项绝佳补充。

像任何包管理器一样，除了它能很好地完成工作并得到所有操作系统的支持之外，没有太多可说的。

该工具最好的部分是其文档，其中包含 [官方插件](https://krew.sigs.k8s.io/plugins/) 的列表，Krew 支持这些插件。

如果你浏览该列表，你可能会发现你不知道存在的插件。

## 4. 从多个 Kubernetes 资源聚合日志：Stern

Stern 是此工具列表中第一个面向更高级用户的工具。

如果你查看过 Kubernetes 中的 pod 日志，你可能遇到过这样的用例：你想将来自 pod 中不同 pod 或容器的日志组合到同一个输出中。

[Stern] 允许你 `tail` Kubernetes 上的多个 pod 以及 pod 中的多个容器。每个结果都用颜色编码，以便更快地进行调试。

## 5. 查看内部：node-shell

node-shell 允许你启动一个 shell 来访问 Kubernetes 节点的底层操作系统。

这个工具在为 Kubernetes 开发可观察性工具时非常宝贵。

正如我在我的深入文章 [Kubernetes：node-shell](https://cloudnativeengineer.substack.com/p/ep-2-kubernetes-node-shell) 中解释的那样，不止一次，我不得不查看 Kubernetes 节点，以便跟踪直接写入节点主机以馈送到 Elasticsearch 的 pod/容器日志。

没有 node-shell，我无法做到这一点。

node-shell，就像此列表中的许多其他工具一样，可以通过 Krew 安装并集成到 K9s 中。

## 结论

本文中的工具列表绝对不完整。

我本可以提到：

- Helm
- Customise
- K3d
- Kind

等等。

它们中的大多数都比较高级，值得单独写一篇文章。

我可能会在将来介绍其中的一些。
