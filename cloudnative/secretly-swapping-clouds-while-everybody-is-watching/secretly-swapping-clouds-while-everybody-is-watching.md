
<!--
title: 在众目睽睽之下偷偷换云
cover: https://cdn.thenewstack.io/media/2025/02/cf524aff-clouds1.jpg
-->

> 译自：[Secretly Swapping Clouds While Everybody Is Watching](https://thenewstack.io/secretly-swapping-clouds-while-everybody-is-watching/)
> 作者：John Dietz

品牌重塑期间，开源项目Konstruct决定更换DNS、Git和云提供商。以下是如何在隐秘状态下完成这一过程的介绍。

---


# Secretly Switching Cloud Platforms Under Everyone's Nose

![Article Feature Image: Secretly Switching Cloud Platforms Under Everyone's Nose](https://cdn.thenewstack.io/media/2025/02/cf524aff-clouds1-1024x576.jpg)

Earlier this year, our team secretly began developing a new bare-metal product called [Colony](https://konstruct.io/colony). At the time, our company was called Kubefirst, sharing a brand with our popular [Kubefirst platform](https://thenewstack.io/taming-the-cncf-landscape-with-kubefirst/). With the addition of the Colony product line, it was time to rename the company to Konstruct.

Because the rebranding effort was conducted in secret, this also presented a unique opportunity for us to secretly establish a new company. As an open-source company, secretly establishing a new organization presented a very interesting challenge for our engineering team.

Ultimately, we were only discovered by a member of the community a few days before our [major announcement](https://blog.konstruct.io/introducing-konstruct/). The launch of our new brand and company was very successful, and we'd like to share our approach so you can use it the next time you secretly rebrand.

**Choosing a Simpler Cloud Platform as a New Home**

For the past five years, we've been running our production environment for Kubefirst on the AWS cloud. [AWS](https://aws.amazon.com/?utm_content=inline+mention) was the first cloud platform supported by the Kubefirst platform. In fact, Kubefirst supported Kubernetes on AWS before the Elastic Kubernetes Service (EKS) existed. AWS has been incredibly reliable for us, and it was a great place to store our YAML files for five and a half years.

Since we started building our engineering team two years ago, our platform has expanded to support GCP, Azure, Civo, Akamai, DigitalOcean, Vultr, and bare metal. This gave us a unique opportunity to choose any cloud platform to host our rebranded Konstruct ecosystem. We've been using the Civo cloud as our development environment for the past two years and really enjoyed the simplicity and speed of its [cloud-native approach](https://thenewstack.io/the-rise-of-the-cloud-native-cloud/). We ultimately decided on Civo as our new permanent production environment, and it was time to get building.

## Secret Migration Checklist
- Git organization hosting our [open-source and closed-source code repositories](https://thenewstack.io/build-an-open-source-kubernetes-gitops-platform-part-1/) - Publicly hosted CLI binaries
- Public Helm charts
- Public container images
- Public Homebrew Tap
- DNS (previously AWS Route53, migrated to Cloudflare)
- Our internal management (users, teams, permissions, and Git repositories)
- Our CI/CD ecosystem (Argo Workflows + GitHub Actions)
- Our cluster control plane (Kubefirst + Crossplane + Atlantis + Argo CD)
- Self-hosted marketing website (React), documentation website (Docusaurus), and blog (Ghost)

## Preparing Bot Accounts

We set up our [konstruct.io](https://konstruct.io/) domain in Cloudflare and created a new bot account for our automation. We created an API key for the new platform so that `external-dns` could automatically manage its DNS records.

Next, we created a new GitHub bot user account for creating and managing our new [konstruct.io GitHub organization](https://github.com/konstructio), along with a personal access token for the platform's infrastructure-as-code (IaC) layer. If this weren't a secret operation, we could simply rename our GitHub organization to automatically migrate the repositories. However, in a secret operation, your private repositories should be migrated before your public repositories, making a complete organization rename less desirable.

The last bot account we created was a new Civo cloud account, from which we generated an API token that allowed the platform to manage our cloud resources.

**Build Day**

Setting up the new management account was refreshing. No manual clicks required. Take a deep breath. Can you smell the sterile air?

After exporting our new key set, we ran `kubefirst civo create` to build our Kubefirst platform, brand new, in a very different cloud environment. It used our favorite new DNS provider and built us a shiny new `gitops` repository, placing it in our new GitHub organization.

Next, we needed to create new clusters to represent our pre-production and production environments. For the clusters, we used the Kubefirst Pro user interface to create them. We copied the environment directories from the old `gitops` repository to the new `gitops` repository, and Argo CD ensured that all Helm charts were safely delivered to their new home.

If you're migrating cloud providers, DNS providers, and Git organizations, you'll need to update some old values when transferring repository contents to their new home. Pay attention to any references to the old Git organization or old DNS hostnames when copying these settings.
在进行这些更改的同时，Argo CD 是评估集群状态和健康状况的绝佳空间。Argo CD 通常会通过 UI 中的事件来显示错误，从而告知您问题所在。在我们的案例中，这些问题大多只是一些需要在新环境中复制的旧环境密钥。

![图片 1](https://cdn.thenewstack.io/media/2025/02/49d5f9f8-image2.png)

我们逐一解决了这些问题，平台也转向了我们所喜爱的 Argo CD 中心。

## 迁移 Chartmuseum 实例间的图表

我们对图表托管有一个棘手的细节需要考虑。我们将图表托管在 ChartMuseum 中，因此我们的新实例一开始是空的。任何新内容都会自动发布到其中，但我们希望用所有现有的 Kubefirst 图表填充它，以便在我们准备好后，大家可以完全切换到我们的新图表存储库。

如果您了解 ChartMuseum，您可能会认为您可以直接复制存储桶并更新 `index.yaml`，但实际上比这更复杂。网上没有特别好的关于此迁移的资料，因此我们编写了一个新的开源实用程序来帮助大家完成此操作。如果您需要备份或迁移 ChartMuseum，请试用我们的 [charts-mirror](https://github.com/konstructio/charts-mirror) 仓库。它允许您在 ChartMuseum 实例之间移动图表，并允许您在 ChartMuseum 和 GitHub 之间备份和恢复图表以进行灾难恢复。

## 迁移 IaC

Kubefirst 使用 IaC 管理我们的云、用户、Vault 配置和 Git 配置，而对于[其他所有内容，我们使用 GitOps](https://thenewstack.io/i-need-to-talk-to-you-about-kubernetes-gitops/)。创建 Kubefirst 平台时，这四个目录都会使用默认设置创建，但我们希望迁移我们最初的 Kubefirst 内容。

**云：**云 IaC 不需要任何调整。我们位于新的云环境中，因此无需迁移任何内容。**用户：**我们能够在新分支中直接复制这些文件。我们的拉取请求提示 Atlantis 提供了我们喜欢的计划；我们添加了注释`atlantis apply`，然后，我们的用户就在他们的新家了。此时，我们向团队的所有成员发送了关于他们新的 Git 组织访问权限的邀请，每个人都可以使用新平台并登录到他们在新云中的所有喜欢的平台工具。一切进展顺利。**Vault：**这不需要任何调整。默认配置非常适合我们的团队。**GitHub：**这是一个棘手的问题。我们接下来讨论一下。

## 隐身模式下迁移 GitHub 仓库

这可能是我们最难处理的部分。我们通过旧管理集群上的 Atlantis 管理我们的仓库，并且所有内容都设置在我们开始使用的原始 `kubefirst` 组织中。

我们希望将我们的仓库迁移到新的 `konstructio` 组织，但我们不想过早透露我们的品牌重塑计划。这意味着对于我们的开源代码库，在最后一刻之前什么都不能改变。

对于我们所有的闭源仓库，我们只是将文件从旧的 `terraform/github` 文件夹复制到新的文件夹。当打开拉取请求时，计划显示它将创建所有新的仓库。

我们将每个私有仓库转移到 `konstructio` 组织，然后为每个仓库运行 `atlantis import`，以便其状态将由新的 IaC 继承。然后我们重新运行 Atlantis 计划以显示没有更改。应用后，我们所有私有仓库的迁移都已同步。

对于我们的开源仓库，我们在公开未知的 `konstructio` 位置创建了它们的副本，有效地复制了我们现有的公共仓库。这使我们有机会在验证发布和交付管道并确保一切准备就绪后，从他们的新家构建和发布我们的产品时识别更改。

此测试暴露了我们唯一的错误：Homebrew。

## Homebrew 注意事项

Homebrew 不想帮助我们保守秘密。通过复制我们的公共 Homebrew 仓库，我们暴露了我们的计划。

当您在 GitHub 中创建仓库时，会自动发现 Homebrew tap 仓库。如果它们配置到新的空间，它们可以遵循重定向并监视您在传输时的新公共仓库。

这是在我们宣布之前暴露我们计划的一个细节。由于 GitHub 仓库转发规则，我们的一些新候选版本在我们想要之前就开始出现在旧 tap 中了。如果您也维护 Homebrew tap，请在迁移期间特别注意您的 Homebrew 配置和仓库重定向。

## 迁移日

将我们的私有仓库迁移到新家后，我们确保它们可以构建并交付到新的容器注册表、图表注册表和 Kubernetes 集群。我们最后一次检查 Argo CD 以验证所有应用程序是否正常且没有错误。在最后一批仓库迁移之前，可以设置的所有内容都已完成，监听其新的域并且运行良好。
当进行大规模迁移时，我们转移了所有剩余的 git 组织，包括所有开源仓库，尤其小心处理与我们[1900 个 GitHub 星标](https://github.com/konstructio/kubefirst)相关的操作。如果您不小心将仓库设为私有——或复制而不是转移仓库——您将不可挽回地丢失这个重要的虚荣指标。

## 切记保持SEO防护

域名更改后，一个容易出错的细节是SEO。只要您的原始品牌和域名存在于互联网上，谷歌和其他搜索引擎就会部署SEO机器人来读取和索引与用户相关的相关内容。您需要确保不会丢失围绕原始域名的SEO足迹。如果您选择更新，以下是一些可能有帮助的想法。

更改域名时，最好更改的单词和页面越少越好。如果您能避免，现在不是引入新文档或更改博客技术的好时机。我们无论如何都做了这两件事，并且最终成功了。保持资产和位置不变有助于您让机器人相信您是同一家公司，并且仍然值得您在旧域名上建立的SEO声誉。

订阅 Ahrefs 等反向链接研究工具可以帮助您查找所有因域名更改而中断的链接。如果可以，通过更新其原始源内容来修复损坏的链接非常重要；如果不能，则可以通过在DNS托管配置中添加重定向来修复。重定向将允许您将错误链接发送到它们新的正确位置以安抚机器人。我们对 Cloudflare DNS 的更新使管理重定向变得非常简单。Google 搜索也有一些可能有帮助的域名迁移工具。

一旦您确认所有流量都已停止流向您的原始资源，并且所有必要的重定向都将最终用户导航到他们的新位置，您就可以安全地拆除旧系统，并惊叹于您的云原生可移植性。

## 向世界宣布您的伟大成就

恭喜您，您已经迁移到新的域名！现在是时候邀请所有公共用户访问您的新数字家园了。

能够更改DNS、git和云提供商对于许多公司来说可能是一项繁重的工作，但对于Konstruct来说并不难，因为我们使用Kubefirst。

Kubefirst 与云、git 和 DNS 提供商无关，因此您可以在任何地方拥有相同的平台。您的组织更改云、git 组织或 DNS 提供商需要多长时间？[查看我们的概述文档](https://kubefirst-pro.konstruct.io/docs/overview/feature)以了解有关我们即时 GitOps 功能的更多信息，或[与我预约演示](https://ro.am/johndietz)以立即获得快速浏览。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)