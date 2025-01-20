# Spacelift 扩展遗留自动化：先用 Terraform，再用 Ansible

![Spacelift 扩展遗留自动化：先用 Terraform，再用 Ansible 的特色图片](https://cdn.thenewstack.io/media/2025/01/028448f7-spacelift-dimitri_vlachos-1024x768.jpg)

上周发布了 [1.9 版本](https://thenewstack.io/opentofu-turns-one-with-opentofu-1-9-0/) 的 [OpenTofu](https://opentofu.org/)，这是 HashiCorp Terraform 的一个分支，[由于许可限制](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)而产生，标志着这个 [基础设施即代码 (IaC)](https://thenewstack.io/introduction-to-infrastructure-as-code/) 软件的第一个完整 1.0 版本发布已满一年。

Spacelift 首席营销官在接受 TNS 采访时表示：“我们对所取得的进展感到非常惊喜。”“采用率、社区参与度和社区的增长可能超出了人们的预期。”

2023 年 8 月，HashiCorp [将其基础设施软件栈重新授权](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)，包括广泛使用的 Terraform，改为 BSL（[商业源许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)），[基本上禁止](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license) 其他公司提供[围绕 Terraform 的竞争产品](https://thenewstack.io/terraform-gets-ai-boost-in-new-cloud-management-platform/)，这是一款允许管理员以代码驱动方式管理基础设施的软件。Spacelift 正是众多受此影响的公司之一。

表示：“业内许多公司认为这违背了开源的精神。”

除了 Spacelift 之外，这些公司还包括 [Scalr](https://www.scalr.com/), [env0](https://www.env0.com/), [Gruntwork](https://gruntwork.io/), [Digger](https://digger.dev/), 和 [Cloud Posse](https://cloudposse.com/)，他们参与了 [启动分支](https://thenewstack.io/opentf-disgruntled-hashicorp-rivals-threaten-to-fork-terraform/) 的行动。

表示，他们“认为这种技术应该在底层保持开源，因为它构成了许多底层基础设施的框架。”

[Linux 基金会也同意这一观点，并很快支持](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/) 了该项目。

在过去的一年中，[该项目](https://thenewstack.io/getting-started-with-opentofu-alpha/) 能够包含新的功能，例如加密，这些功能[长期以来一直是用户所要求的](https://thenewstack.io/opentofu-registry-gets-a-user-interface-and-an-api/)，同时仍然与 Terraform 的最后一个开源版本 v 1.55 向后兼容。

表示：“我认为 OpenTofu 与许多开源项目不同，许多开源项目只有一个实体在赞助。我们有很多赞助商。它之所以被称为‘开源’，是有原因的。”

## Spacelift 不是 OpenTofu 的经销商

Spacelift 绝不仅仅是 OpenTofu 的再分销商。

该公司的使命始终是提供一个平台来管理[多种 IaC 工具](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/)，例如[HashiCorp 的 Terraform](https://thenewstack.io/experts-share-best-practices-for-building-terraform-modules/) 和 [Pulumi](https://www.pulumi.com?utm_content=inline+mention)，并为大规模使用配备额外的可观察性和治理工具。

表示：“我们允许客户以统一的方式管理基础设施管道。”

以下是 [Spacelift 平台的工作原理](https://spacelift.io/how-it-works)：使用您最喜欢的 IaC 工具（目前，该公司支持 Terraform、OpenTofu、[AWS CloudFormation](https://aws.amazon.com/?utm_content=inline+mention)、Ansible、[Kubernetes](https://thenewstack.io/Kubernetes/) 和 [Terragrunt](https://terragrunt.gruntwork.io/)）来描述您的系统。

然后将您的代码推送到代码存储库（[GitLab](https://about.gitlab.com/?utm_content=inline+mention)、GitHub、AzureDevOps、BitBucket），然后为您的存储库创建一个堆栈。

因此，每当此堆栈发生更改时，Spacelift 中都会触发运行。您可以选择是否要自动应用代码或通过手动干预来应用代码。如果是后者，则会应用基础设施更改。

使用 Spacelift，主要服务可以在 AWS、[Google Cloud](https://cloud.google.com/?utm_content=inline+mention) 和 Microsoft Azure 云以及本地部署中运行。
“企业难以快速发展，”Vlachos解释道。“应用开发者和工程师希望快速行动。他们希望发布代码。他们需要底层基础设施来实现这一点。但他们也必须具备所有必要的控制措施，以确保安全、高效且经济。”

基本的自动化工具不会提供诸如可视化或哪些个人控制管道哪些部分等功能，仅举两例。

“使用OpenTofu或Terraform之类的工具可以帮助你更快地部署基本架构，但它不会提供所有基础设施。当越来越多的人试图管理这些管道时，就会遇到问题。你没有策略引擎来了解谁可以做什么，”Vlachos补充道。

从这个意义上说，OpenTofu本身并不与Terraform竞争，而是与HashiCorp的[Terraform Enterprise](https://developer.hashicorp.com/terraform/enterprise)或其高级云产品[HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs)竞争，两者都提供类似的功能。HasiCorp正在被IBM[收购](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/)。

金融服务、零售和医疗保健公司都使用了Spacelift的服务。

## 先是Terraform，然后是Ansible
另一个在配置管理中广泛使用的工具是[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)的[Ansible](https://thenewstack.io/ansible-vs-salt-which-is-best-for-configuration-management/)，这是一种广泛使用的IT自动化工具，可在本地和云中使用。Red Hat是IBM的[子公司](https://thenewstack.io/red-hat-ibm-acquisition-clash-of-cultures-or-best-of-both-worlds/)。

“大规模运行Ansible有很多挑战，”Vlachos解释说，并指出难以了解该技术创建的工作流。

在一个组织中，在许多节点上运行大量Ansible Playbook可能会发现配置操作运行非常缓慢。此外，根据Vlachos的说法，Ansible本身几乎没有提供关于重新配置是否成功的反馈。

现在，用于OpenTofu和Terraform的相同工作流将涵盖Ansible。

Spacelift用其话来说，新功能包括：

**剧本自动化**: 从中心位置管理Ansible剧本。**清单可观察性**: 查看所有Ansible管理的主机和剧本，并提供最近运行的成功或失败的可视化指示器。**剧本运行洞察**: Ansible剧本运行结果，包含详细的洞察信息，以查明问题并简化故障排除。**集成IaC和Ansible工作流**: 将IaC（Terraform、OpenTofu、CloudFormation）和Ansible组合到单个工作簿中。**开发者自助服务**: 开发者委托工作流的门户。
Red Hat也一直在为Ansible配备云使用功能。去年12月，[它启动了](https://thenewstack.io/red-hat-brings-ansible-automation-to-amazon-web-services/)一项基于Ansible的AWS用户托管服务，允许用户使用Ansible管理其基于AWS的流程。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)