# 重新授权的开源项目及其分支发生了什么？

![重新授权的开源项目及其分支发生了什么？的特色图片](https://cdn.thenewstack.io/media/2024/12/62f2b75e-open-source-forks-1024x576.jpg)

许多流行的[开源项目](https://thenewstack.io/open-source/)都由单一公司拥有和驱动，在当今艰难的经济环境下，这些公司面临着[越来越大的压力](https://redmonk.com/rstephens/2024/08/26/software-licensing-changes-and-their-impact-on-financial-outcomes/)，需要为其投资带来强劲的回报。应对这种压力的一种方法是将流行的开源项目重新授权为更严格的许可证，以期产生更多收入。在某些情况下，重新授权已[导致原始项目的硬分叉](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/)。这些重新授权事件及其分支可能会扰乱使用和贡献受影响开源项目的组织和个人。

在过去几年中，几家公司重新授权了它们的开源项目，因此[CHAOSS 项目](https://chaoss.community/)决定研究开源项目的[组织动态](https://chaoss.community/practitioner-guide-organizational-participation/)在重新授权后是如何演变的，包括原始项目及其分支。我们的研究比较和对比了三个案例研究的数据，这些案例研究的项目在重新授权后被分叉：Elasticsearch 及其分支[OpenSearch](https://thenewstack.io/opensearch-how-the-project-went-from-fork-to-foundation)、Redis 及其分支[Valkey](https://thenewstack.io/navigating-the-path-from-redis-to-valkey) 以及 Terraform 及其分支[OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next)。

这些重新授权的项目及其分支代表了三种场景，以略微不同的方式阐明了这个主题。以下是我们在查看数据时发现的总结，您可以在我们最近在[OpenForum Academy Symposium](https://symposium.openforumeurope.org/)上分享的[论文、演示文稿和数据](https://github.com/chaoss/wg-data-science/tree/main/publications)中深入了解这六个项目。

## Elasticsearch 和 OpenSearch

几乎所有对原始 Elasticsearch 项目的贡献都来自重新授权公司 (Elastic) 的员工，而分支是由新的贡献者创建的，并由单一公司 ([Amazon](https://aws.amazon.com/?utm_content=inline+mention)) 拥有。

### Elasticsearch

Elasticsearch 是一个在 Apache 2.0 许可证下的开源项目，直到 2021 年 2 月 3 日，[项目被重新授权](https://www.elastic.co/blog/licensing-change)为服务器端公共许可证 (SSPL) 和 Elastic 许可证。2024 年 8 月 29 日，Elastic 宣布添加 GNU Affero 通用公共许可证 (AGPLv3) 作为额外的许可选项，它再次成为一个开源项目，但目前尚无足够的数据将其纳入分析。

在重新授权之前和之后，对[Elasticsearch 代码库](https://github.com/elastic/elasticsearch) 的贡献者大多是 Elastic 员工；他们始终贡献了超过 95% 的添加到 Elasticsearch 的代码行和删除的代码行，Elastic 外部的贡献者几乎没有参与。因此，2021 年的重新授权对贡献者几乎没有影响，但对 Elasticsearch 的用户或消费者产生了更大的影响，他们被迫决定是否继续使用它，如果继续使用，则是在哪两种可用的许可证下使用。

### OpenSearch

OpenSearch 于 2021 年 4 月 12 日由 Amazon Web Services (AWS) 团队在 Apache 2.0 许可证下从 Elasticsearch 分支出来，以便它可以继续向其客户提供此服务。OpenSearch 由 Amazon 拥有，直到 2024 年 9 月 16 日，它[将项目转移](https://thenewstack.io/aws-transfers-opensearch-to-the-linux-foundation/)到 Linux 基金会。

与 Elasticsearch 一样，对[OpenSearch 代码库](https://github.com/opensearch-project/OpenSearch) 的大多数贡献来自 Amazon 员工，但是，程度较小，并且随着时间的推移，组织多样性有所提高。在分叉的第一年，少数 Amazon 员工贡献了 80% 的总添加量和 91% 的总删除量。只有两名非 Amazon 员工提交了 10 次或更多提交，占添加量的 7% 和删除量的 4%。
在亚马逊拥有该项目（在项目移交给 Linux 基金会之前）的最后一年，其组织多样性有所改善，63% 的新增代码和 64% 的删除代码来自提交了 10 次或以上代码的亚马逊员工。六位非亚马逊员工提交了 10 次或以上代码，占新增代码的 11% 和删除代码的 13%。总而言之，贡献者主要来自亚马逊，但组织多样性正在逐步改善。

## Terraform 和 OpenTofu
几乎所有对重新授权的 Terraform 项目的贡献都来自 HashiCorp 公司的员工，而分支项目 (OpenTofu) 则由新的贡献者作为基金会项目创建。

### Terraform
Terraform 在 2023 年 8 月 10 日之前一直使用 Mozilla 公共许可证 v2.0 (MPL 2.0) 开源，之后与 HashiCorp 的其他开源项目（例如，Vagrant、Vault）一起重新授权为商业源代码许可证 (BSL)。与 Elasticsearch 类似，[Terraform 代码库](https://github.com/hashicorp/terraform) 几乎没有非 HashiCorp 员工的贡献者。在重新授权的前一年和后一年，只有两位与 HashiCorp 无关的贡献者为 Terraform 做出了贡献，而且他们的贡献数量都非常少。

由于公司外部的贡献很少，重新授权事件对贡献者社区没有实质性影响，因此受影响的可能只有 Terraform 用户。

### OpenTofu
OpenTofu 于 2023 年 8 月 25 日由一群用户作为 Linux 基金会项目，在 MPL 2.0 许可下，从 Terraform 分支而来。这些用户从代码库的初始状态开始，因为[OpenTofu 代码库](https://github.com/opentofu/opentofu) 的贡献者之前都没有为 Terraform 做过贡献。

在第一年，来自 11 个组织的 31 人对 OpenTofu 代码库做出了五次或五次以上的贡献。Spacelift 的员工贡献最大，他们贡献了超过一半的代码新增和删除。Env0 和 Scalr 的员工也做了一些贡献，因此项目具有一定的组织多样性。

## Redis 和 Valkey
重新授权的项目 (Redis) 有大量的非公司员工贡献者，而分支项目 (Valkey) 由这些现有的贡献者作为基金会项目创建。

### Redis
Redis 项目在 2024 年 3 月 20 日之前是一个使用伯克利软件发行版 3 条款许可证 (BSD-3) 的开源项目，之后该项目被重新授权为 Redis 源代码可用许可证 (RSALv2) 和 SSPLv1。这与[2018 年 Redis 博客文章](https://redis.io/blog/redis-license-bsd-will-remain-bsd/) 中声明 Redis 开源项目将始终使用 BSD 许可证的说法相矛盾。

Redis 项目在非 Redis 员工的贡献数量上与 Elasticsearch 和 Terraform 不同。在重新授权前的一年中，Redis 仍然是开源项目时，其他公司员工做出了大量的贡献：非 Redis 员工中提交了五次或五次以上代码的人数是 Redis 员工的两倍，而且其他公司的大约十几个员工提交的代码几乎是 Redis 员工的两倍。

在重新授权后的六个月内，所有在重新授权前一年对 Redis 项目提交了五次以上代码的外部公司贡献者（包括亚马逊、阿里巴巴、腾讯、华为和爱立信）都停止了贡献。总而言之，Redis 在重新授权之前具有很强的组织多样性，但之后只有 Redis 员工做出了重大贡献。

### Valkey
[Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/) 于 2024 年 3 月 28 日从 Redis 7.2.4 分支而来，是一个在 BSD-3 许可下运行的 Linux 基金会项目。该分支项目是由一群之前为 Redis 做出贡献并得到其雇主公开支持的人员推动的。在其最初的六个月内，[Valkey 代码库](https://github.com/valkey-io/valkey) 有来自 10 家公司的 29 位贡献者，其中 18 位之前曾为 Redis 做出贡献。Valkey 拥有来自不同公司的多样化贡献者群体，其中亚马逊的贡献者最多。

## 下一步
这是[CHAOSS 数据科学工作组](https://github.com/chaoss/wg-data-science/tree/main/dataset/license-changes/fork-case-study)正在进行的一个更大研究项目的第一步。到目前为止，我们只研究了每个项目的 primary repository 和组织关联数据，因此我们正在努力纳入更多 repository 和其他指标，以更好地了解这些项目中的项目健康动态。我们也可能会扩展到研究其他在重新授权后被分支的项目。
纵观所有这些项目，我们可以看到，来自重新授权项目的衍生项目往往比原始项目具有更多组织的多样性。当这些衍生项目是在一个中立的基金会（例如Linux基金会）下创建的，而不是由单一公司创建时，这一点尤其明显。

现在判断这些项目的最终成败（无论是原始项目还是衍生项目）还为时过早。新的衍生项目具有更多组织多样性，而具有更大组织多样性的项目往往更具可持续性。然而，我们尚不知道这是否适用于这些项目，特别是对于那些仍在努力满足投资者期望的公司而言。

*CHAOSS 将参加 State of Open Con 大会，该大会涵盖开源软件、开源硬件、开放数据、开放标准和 AI 开放性，将于 2 月 4 日和 5 日在伦敦举行。The New Stack 的创始人兼出版人 Alex Williams 将主持关于开源未来的主题环节。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展日新月异，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。