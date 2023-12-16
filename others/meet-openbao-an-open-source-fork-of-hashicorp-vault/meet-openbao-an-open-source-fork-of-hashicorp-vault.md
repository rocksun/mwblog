<!--
title: Vault的开源分支OpenBao
cover: https://cdn.thenewstack.io/media/2023/12/e8c997dd-openbao-1024x683.png
-->

首先是 Terraform，现在又是 Vault：HashiCorp 留下的更多开源代码正在找到潜在竞争对手的新归宿。这一次，IBM 正在探寻这些战利品。

> 译自 [Meet OpenBao, an Open Source Fork of HashiCorp Vagrant](https://thenewstack.io/meet-openbao-an-open-source-fork-of-hashicorp-Vagrant/)，作者 Joab Jackson 是 The New Stack 的高级编辑，负责报道云原生计算和系统运维。他已经在 IT 基础设施和开发领域报道超过 25 年，包括在 IDG 和 Government Computer News 的工作。原文可能有误，分叉的应该是 Vault 不是 Vagrant 。

首先是 Terraform，现在又是 Vault：[HashiCorp 放弃的](https://thenewstack.io/opentf-disgruntled-hashicorp-rivals-threaten-to-fork-terraform/)更多开源代码正在找到潜在竞争对手的归宿。

在九月份，HashiCorp 的[竞争对手分叉了](https://thenewstack.io/open-source-fights-back-opentofu-is-the-entree-we-need/)基础设施即代码（IaC）软件 Terraform，创建了 [OpenTofu](https://opentofu.org/)，之前 HashiCorp 将其核心企业软件大部分[从开源转移到 Business Source License](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license)。现在，[OpenBAO 项目](https://github.com/openbao/openbao/tree/development?ref=dailydev)致力于维护 HashiCorp 广泛使用的 Vault 安全软件的开源版本。

OpenTofu 项目[迅速吸引了贡献者](https://www.linuxfoundation.org/press/announcing-opentofu)，主要是饥渴的第三方 Terraform 导向的初创公司，如 [Scalr](https://www.scalr.com/)、[Gruntwork](https://gruntwork.io/)、[Spacelift](https://spacelift.io/)、[env0](https://www.env0.com/)、[Terrateam](https://terrateam.io/) 和 [Terramate](https://terramate.io/) 等。

而且，对于 OpenBAO 项目来说，它至少有一个潜在的强大支持者：[IBM](https://www.ibm.com/?utm_content=inline-mention)。

尽管 IBM 没有正式宣布任何消息，但两位 IBM 工程师正在努力使 OpenTofu 成为 Linux 基金会下 LF Edge Umbrella 项目的一部分。

## Vault 对比 OpenBAO

由 HashiCorp 开发，Vault 在许多分布式计算设置中用于管理秘密，即加密密码、API 密钥和其他敏感信息的工具。HashiCorp 为使 Vault 成为行业标准以及使其与 Terraform 无缝配合而做了大量工作，这使得它在与云提供商的秘密管理软件（如 [AWS Secrets Manager](https://thenewstack.io/managing-kubernetes-secrets-with-aws-secrets-manager/)）相比具有自然优势。

Vault 还是云无关的，对于寻求采用[多云战略](https://thenewstack.io/karmada-finally-brings-multicloud-control-to-kubernetes/)的组织而言，这是一个重要属性。

IBM 工程师发起了 OpenBao，尽管 IBM 尚未正式认可它为官方项目（尽管公司在其官方网站上保留了一个[指向该项目的链接](http://ibm.biz/openbao)）。OpenBao 提案目前存放在 [Linux 基金会 Edge](https://lfedge.org/) 网站上，尽管尚未列为项目。IBM 工程师 Nathan Phelps 和 [Joe Pearson](https://twitter.com/JoePearson_edge) 被列为新项目的联系人。

“OpenBao 旨在提供一种软件解决方案，用于管理、存储和分发包括密码、证书和密钥在内的敏感数据。OpenBao 社区打算在一个遵循开放治理原则的社区领导下，以经 OSI 批准的开源许可证提供此软件，”一份[项目 FAQ](https://wiki.lfedge.org/display/OH/OpenBao+%28Hashicorp+Vault+Fork+effort%29+FAQ) 上于 10 月 20 日的使命声明中写道。

OpenBao 将从 Vault 的最后一个开源版本启动，即 HashiCorp 在 [Mozilla Public License 2.0（MPL 2.0）](https://opensource.org/license/mpl-2-0/) 下获得的最后一个版本，即 [1.14 分支](https://github.com/hashicorp/vault/tree/release/1.14.x)。

## 全程开源

在今年早些时候接受 TNS 采访时，Scalr 创始人（兼 OpenTofu 贡献者）[Sebastian Stadil](https://www.linkedin.com/in/sstadil/) 解释说，OpenTofu 的分支部分源于一些 Terraform 用户对 HashiCorp 对错误修复的迟缓响应的不满，即使是由外部用户提交的错误修复。

在 Vault 周围似乎也存在类似的不耐烦，至少可以从 [Hacker News 上的一条评论中看出](https://news.ycombinator.com/item?id=38578247)：“Vault 有很多社区贡献被阻塞或由于 [HashiCorp] 内部政治/路线图问题而停滞。我认为有一个社区分支将鼓励人们解决 [HashiCorp] 不愿意加入产品的问题。”

读者还期待有一个替代 Vault 插件模式的解决方案。“生命周期插件，特别是在使用容器部署 Vault 时，是一场噩梦，”他们写道。

事实上，除了修复错误之外，该项目的一个倡议是构建一些仅存在于 [Vault 企业](https://www.hashicorp.com/products/vault)商业版中的[高级功能](https://developer.hashicorp.com/vault/docs/enterprise)，如高速复制、多个命名空间，甚至可能是[策略即代码框架](https://developer.hashicorp.com/vault/docs/enterprise/sentinel)。与 [OpenTofu](https://thenewstack.io/getting-started-with-opentofu-alpha/) 的紧密集成也将是一个主要关注点。

## HashiCorp 会变成大餐吗？

今年早些时候 OpenTofu 的一个令人惊讶的情节转折是 Linux 基金会在项目启动仅几周后就迅速参与其中，并且对 OpenTofu 表示认可。

但正如 Stadil 解释的那样，这是可以预期的，考虑到 Terraform 在开源[云原生社区](https://cncf.io/?utm_content=inline-mention)中的广泛使用。在一个专有的基础设施即代码平台上构建完全开源的堆栈，这不太妙，这是由云原生计算社区维护的。

据推测，对于同样受欢迎的 HashiCorp 机密软件，也可以提出类似的论点。Linux 基金会没有回应最后一分钟的评论请求。HashiCorp 拒绝回应 TNS 的最后一分钟请求。

除了 Terraform 和 Vault，HashiCorp 还将 [Consul](https://thenewstack.io/hashicorps-consul-brings-namespace-management-to-the-service-mesh/)、[Packer](https://www.packer.io/) 和 [Vagrant](https://thenewstack.io/hashicorp-revamps-vagrant-and-retools-for-microservices/) 也转移到了 BSL。猜猜这些开源变种可能以什么食物命名呢？
