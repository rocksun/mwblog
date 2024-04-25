
<!--
title: IBM 收购HashiCorp以实现多云IT自动化
cover: https://cdn.thenewstack.io/media/2024/04/967925a7-hashicorp-ibm.jpg
-->

HashiCorp 的基础设施和安全生命周期管理软件，加上 Red Hat 的产品组合，可以帮助 IBM 使多云计算成为一种实际的可能性。

> 译自 [IBM Purchases HashiCorp for Multicloud IT Automation](https://thenewstack.io/ibm-purchases-hashicorp-for-multi-cloud-it-automation/)，作者 Joab Jackson。

企业软件和服务巨头 [IBM](https://www.ibm.com/cloud?utm_content=inline+mention) 宣布以 64 亿美元（每股 HashiCorp 股票 35 美元现金）收购 IT 基础设施提供商 HashiCorp。

两家公司的董事会已批准这笔交易，预计将于 2024 年底完成。

HashiCorp 用于[基础设施和安全生命周期管理](https://thenewstack.io/hashicorp-hears-users-rolls-out-new-testing-qa-tools-for-terraform/)的软件将补充 IBM 围绕混合云和 AI 的服务，IBM 在新闻稿中 [断言](https://www.prnewswire.com/news-releases/ibm-to-acquire-hashicorp-inc-creating-a-comprehensive-end-to-end-hybrid-cloud-platform-302126646.html)。

HashiCorp 将继续作为 IBM 旗下的一个部门运营。

此次收购与 IBM [收购](https://thenewstack.io/turning-blue-ibm-to-acquire-red-hat/) [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)（2018 年）类似，将进一步巩固 IBM 在云原生计算领域的领先地位，其中许多部署已使用 HashiCorp 的 [Terraform 多云基础设施配置工具](https://thenewstack.io/automating-retry-for-failed-terraform-launches/)。

HashiCorp 联合创始人兼首席技术官 [Armon Dadgar](https://thenewstack.io/qa-hashicorp-cto-armon-dadgar-on-idps-and-iac/) 在 [一篇博文中](https://www.hashicorp.com/blog/hashicorp-joins-ibm) 写道：“通过加入 IBM，HashiCorp 产品可以面向更广泛的受众，使我们能够服务更多用户和客户。对于我们的客户和合作伙伴而言，这种组合将使我们能够超越独立公司。”

对于 IBM 而言，HashiCorp 可以支持 Big Blue 的战略增长领域，如 Red Hat、Watsonx AI 产品、数据安全、IT 自动化和咨询。

它还将为一套新的集成产品奠定基础，将 HashiCorp 的软件与 IBM 和 Red Hat 的软件相结合，使客户能够跨多个公共云提供商（“多云”）重新运行操作。

## HashiCorp 的 Terraform 在组合中

HashiCorp 拥有 4,400 名令人印象深刻的客户名单，其中包括 85% 的财富 500 强企业，客户包括彭博社、康卡斯特、德意志银行、GitHub、摩根大通、星巴克和沃达丰。

该公司的软件产品组合包括：

- [Terraform](https://thenewstack.io/how-to-manage-cloud-services-with-terraform/) 用于跨云环境自动配置 IT 资源。
- [Vault](https://thenewstack.io/hashicorp-vault-operator-manages-kubernetes-secrets/) 为系统和敏感数据提供基于身份的安全。
- [Boundary](https://www.hashicorp.com/products/boundary/) 用于安全远程访问。
- [Consul](https://www.hashicorp.com/products/consul/) 用于基于服务的网络。
- [Nomad](https://www.hashicorp.com/products/nomad/) 用于工作负载编排。
- [Packer](https://www.hashicorp.com/products/packer/) 用于构建和管理图像作为代码；以及
- [Waypoint](https://www.hashicorp.com/products/waypoint/) 一个内部开发人员平台。

Terraform 一直是 HashiCorp 的旗舰产品，尽管其使用在过去几年中有所下降—— [JetBrains 最近的一项调查](https://thenewstack.io/jetbrains-developer-survey-tracks-rapid-adoption-of-ai-chatgpt/) 显示，开发人员的使用率从 2022 年的 37% 下降到 2023 年的 33%——因为新一代更灵活的基础设施即代码工具已从 [Nitric](https://nitric.io?utm_content=inline+mention)、Pulumi 和 [其他](https://thenewstack.io/if-dev-and-ops-had-a-baby-it-would-be-called-winglang/) 进入市场。

Terraform 也可能因用户群分散而受到影响。

8 月份，HashiCorp[将](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)以前开源的 Terraform 及其产品组合的其余部分转移到非开源商业源许可证 (BSL)。竞争的 Terraform 服务提供商（包括 Scalr、env0 和 Spacelift）迅速分叉了代码[以创建开源 OpenTofu](https://thenewstack.io/opentf-disgruntled-hashicorp-rivals-threaten-to-fork-terraform/)，该代码得到了 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) 的 [迅速支持](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/)。

12 月份，Vault 也分叉为[一个名为 OpenBao 的开源版本](https://thenewstack.io/meet-openbao-an-open-source-fork-of-hashicorp-vault/)——该项目具有讽刺意味的是由一位 IBM 工程师指导。

现在 HashiCorp 的软件将由历史上对开源友好的 IBM 管理，一些开源倡导者希望 Big Blue 能够撤销 HashiCorp 去年突然的 BSL 许可证变更。

“如果我是 IBM 负责 HashiCorp 交易的领导者，我会做的第一个决定就是将所有 HashiCorp 产品迁移到 Apache-2.0，并确保在最初的新闻稿中突出这一决定，”[Kelsey Hightower](https://thenewstack.io/kelsey-hightower-on-his-very-personal-kubernetes-journey/) 在 [X 社交媒体服务](https://twitter.com/kelseyhightower/status/1782912507608469686) 上写道。

*TNS 分析师 Lawrence Hecht 为这篇文章做出了贡献。*
