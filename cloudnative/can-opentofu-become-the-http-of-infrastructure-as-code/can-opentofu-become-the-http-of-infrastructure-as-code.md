<!--
title: OpenTofu：基础设施代码新时代
cover: https://cdn.thenewstack.io/media/2024/02/39efc52d-tofu-5512571_1280-1024x682.jpg
-->

从生态系统的视角看，OpenTofu 那颇具变革性的"可信潜力"或可为推广通用标准扮演关键引领角色。

> 译自 [Can OpenTofu Become the HTTP of Infrastructure as Code?](https://thenewstack.io/can-opentofu-become-the-http-of-infrastructure-as-code/)，作者 Ohad Maislish 是 env0 的首席执行官和联合创始人，也是 OpenTofu 项目的创始团队成员。在 env0 之前，Ohad 是 Arno Software(一家云基础设施服务公司)的首席执行官和创始人，以及 Capester(一家初创公司)的创始人。

当 [OpenTofu](https://thenewstack.io/getting-started-with-opentofu-alpha/) 最初[从 Terraform 分叉](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/)时，我[最喜欢的开源和 Kubernetes 社区的声音](https://thenewstack.io/kelsey-hightower-on-open-source-pitfalls-and-challenges/)之一 [Kelsey Hightower](https://github.com/kelseyhightower) 发表评论说。

> 相信作为 HashiCorp 的 Terraform 项目的一个分支的 OpenTF 最终会提高 Terraform 在长期的采用率。
> 
>以 HTTP 为例，它拥有许多实现方式，其采用率比以往任何时候都要高。TF 已成为配置管理方面的 HTTP。
> -- Kelsey Hightower 

几个月后，我加入了一个[小组讨论](https://www.env0.com/blog/unpacking-opentofu-expert-panel-on-ga-release-licensing-and-oss-future)，探讨 [OpenTofu 广泛存在的](https://opentofu.org/blog/opentofu-is-going-ga/)影响。在我们的对话中，我们一直围绕着 Kelsey 的评论展开讨论。

在这个过程中，我感受到有必要写这篇文章分享我的想法，关于为什么 OpenTofu 可能成为 Terraform 协议[所需的演进](https://thenewstack.io/opentofu-1-6-general-availability-open-source-infrastructure-as-code/)，从而成为"云计算的 HTTP"。

## 成熟的证明

在 2024 年 1 月 10 日，也就是 HashiCorp 改变许可证整整 5 个月后，[OpenTofu v1.6](https://github.com/opentofu/opentofu/releases) 的正式发布实现了一个重大里程碑。

我们是如何走到这一步的，这一过程令人难以置信，但我并不打算在这里重新讲述那个故事。足以说，达到这个里程碑需要付出巨大的努力——不仅仅是建设这个项目本身，还包括构建它的支持环境，包括[新的公共注册中心](https://github.com/opentofu/registry)。

在短短 5 个月内完成这一切，是 Terraform 历史上最伟大的成就之一。更重要的是，这一成就完全属于 [Terraform 社区](https://thenewstack.io/how-to-manage-cloud-services-with-terraform/)。

正式发布做到了两件重要的事情: 

1. 它表明 Terraform 可以拥有独立的、由社区驱动的未来;
2. 它证明了 Terraform 的技术成熟度和稳定性——这两点现在已经融入了 OpenTofu 的 DNA。

在此基础上，OpenTofu 现在为全新的可能性打开了大门，提供了在 [HashiCorp 供应商支持的](https://thenewstack.io/hashicorp-hears-users-rolls-out-new-testing-qa-tools-for-terraform/)非开源软件 (OSS) Terraform 版本和同等出色的、社区支持的公正开源版本之间的选择。

拥有这第二种选择，我相信，将有助于 Terraform 的广泛采用——不仅仅是作为一种具体的解决方案，更是作为一种基础技术和概念。反过来，这为重新思考"Terraform 生态系统"的含义铺平了道路——不仅是一群用户，也是一个多种二进制文件使用同一核心技术来实现各种概念的技术集群。

从这个生态系统的角度来看，我现在想重点关注 OpenTofu 的两个特性，我认为这两个特性将独特地影响其未来。

## 真正的开源

我想谈的第一件事是 OpenTofu 真正的开源性质。我在这里强调"真正"是有原因的。甚至在整个许可证变更之前，Terraform 就已经是[商业开源](https://thenewstack.io/what-the-fork-amazon/) (COSS) 领域的一部分，HashiCorp 对路线图拥有完全控制权。

很自然地，这使得 Terraform 处于受到公司业务需求影响的位置。例如，长期以来一个功能请求就是 Terraform 状态加密。然而，由于供应商的自主权，它从未被列为优先事项。

今天，[同样的功能](https://github.com/opentofu/opentofu/issues/297)成为 OpenTofu 官方路线图的一部分，这是在社区提案后根据其优点而被选中的。

![](https://cdn.thenewstack.io/media/2024/02/97895a3f-opentf.png)

这个例子指出了一个更大的真理。为了让 Terraform 技术获得类似 HTTP 的普遍采用，它必须超越其商业起源。换句话说:在它属于所有人之前，它必须不属于任何人。

作为一个基金会支持的项目，OpenTofu 符合这些中立标准。在这样做的同时，它创造了长期、普遍广泛采用的新可能性。

## 信誉因素

我想讨论的另一件事是信誉——这枚硬币的另一面。这也与所有权有关。

多年来，我们见证了早期的商业开源项目。包括 HashiCorp 以及像 [Redis](https://redis.com/blog/redis-labs-modules-license-changes/) 和 [Elastic](https://www.elastic.co/blog/elastic-license-update) 这样的其他公司，改变了它们的许可证，并远离了它们的开源根基。

每次发生这种情况，都会侵蚀一层对所有非基金会拥有的开源软件的信任。然而，作为一个基金会支持的项目，我看到 OpenTofu 从一开始就赢得了极高的信任。

观察将其移至 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline-mention)后的后果，我看到 [Alpine](https://wiki.alpinelinux.org/wiki/Release_Notes_for_Alpine_3.19.0%23HashiCorp_packages)、[Brew](https://github.com/Homebrew/homebrew-core/pull/149678)、[Gitlab](https://gitlab.com/groups/gitlab-org/-/epics/12401) 等迅速纳入了对 OpenTofu 的支持(甚至弃用了对 Terraform 的支持)。

对我来说，很明显这些重量级公司并非随意如此行事。所有这些组织都有许多方式利用它们的工程资源，除非它们信任其背后的团队和 Linux 基金会的声誉，否则它们不会将 OpenTofu 列为优先事项。

OpenTofu 集成被引入的速度说明了很多。展望未来，我已经看到这些信任投票正在扩大和叠加，最终将滚雪球般提供一个公司拥有的 Terraform 永远无法企及的信任水平。

从生态系统的角度来看，OpenTofu 的"可信潜力"是一个改变游戏规则的因素，并且可能在推动普及标准方面发挥关键作用。

## 独特的可能性

在许可证改变之前，Terraform 已在 DevOps 生态系统中获得了广泛采用。

其他工具如 [Pulumi](https://www.pulumi.com/?utm_content=inline-mention) 和 [Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/)，以及像 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline-mention) 的 [CloudFormation](https://aws.amazon.com/cloudformation/) 和 [Microsoft Azure](https://news.microsoft.com/?utm_content=inline-mention) 的 [ARM](https://thenewstack.io/microsoft-finally-brings-arm-based-vms-to-azure/) 这样的平台原生框架也取得了成功。不过，在很大程度上，需要统一的方式来部署和管理多云的人都使用 HashiStack。

然而，尽管多年来一直占据无可争议的主导地位，由于上述所有原因，Terraform 从未定位于演变成真正的类似 HTTP 的通用标准。

OpenTofu 独特地结合了开源中立性、基金会支持的可信度、成熟的技术和社区支持，有潜力改变这种动态。而且，我不会在这里试图预测是否会出现一个通用的云原生配置标准。

我可以确定地说，这是 Terraform 历史上首次出现了这种可能性。对我来说，这足以让人对 OpenTofu 的未来感到兴奋，并感激有机会成为其旅程的一部分。
