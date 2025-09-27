<!--
title: IBM Infragraph项目：基础设施资产实时模型
cover: https://cdn.thenewstack.io/media/2025/09/65f5d399-project_infra-v2.001.jpeg
summary: IBM HashiCorp 推出 Project infragraph，利用 AI 统一基础设施、安全和应用运维，提升可见性和合规性。HashiConf 2025 还发布了 Terraform、Packer 等多项 ILM 和安全功能增强。
-->

IBM HashiCorp 推出 Project infragraph，利用 AI 统一基础设施、安全和应用运维，提升可见性和合规性。HashiConf 2025 还发布了 Terraform、Packer 等多项 ILM 和安全功能增强。

> 译自：[Project infragraph: IBM's Real-Time Model for Infrastructure Assets](https://thenewstack.io/project-infragraph-ibms-real-time-model-for-infrastructure-assets/)
> 
> 作者：Joab Jackson

任何从事基础设施工作的人都知道，[了解](https://thenewstack.io/infrastructure-from-code-what-went-wrong/)组织所有 IT 资产的[工具是有限的](https://thenewstack.io/infrastructure-from-code-what-went-wrong/)，这限制了可见性和上下文。因此，像打补丁这样的 [Day 2 运维](https://thenewstack.io/enterprise-platform-teams-are-stuck-in-day-two-hell/)可能会因为这种不完整的记录而受到影响。

结果是，治理和合规性也常常因此而缺失。

本周在旧金山举行的 IBM HashiCorp [HashiConf 2025](https://www.hashicorp.com/en/conferences/hashiconf) 用户大会上，该公司[首次展示](https://www.stocktitan.net/news/IBM/hashi-corp-previews-the-future-of-agentic-infrastructure-automation-u1w1mgs8uw3r.html)了一个新的基础设施管理项目，该项目可以帮助组织通过一个支持 AI 的控制平面来统一基础设施和安全运维。

在其实现形式中，Project infragraph 将组织的所有基础设施、安全和应用程序整合在一起，采用单一的数据和策略模型。

## 什么是 Project infragraph？

技术细节仍然有些稀缺——该项目将于 12 月开始仅限受邀者参与的私有 Beta 阶段——但其范围将是全面的，因为它将与 IBM 庞大的软件组合集成，并提议与 Red Hat Ansible、OpenShift、IBM watsonx Orchestrate、Cloudability 和其他平台进行集成。

这些平台将通过基于模型上下文协议（MCP）服务器的自然语言接口与 Project infragraph 配对。

## infragraph 的技术意义

“这里面的技术意义再怎么强调也不为过。Project infragraph 本质上构建了一个连接基础设施、应用程序、服务和所有权的实时关系模型，为未来的代理式（AI 驱动的自主）工作流奠定了必要的基础，”商业分析公司 StockTitan 在一份说明中[观察到](https://www.stocktitan.net/news/IBM/hashi-corp-previews-the-future-of-agentic-infrastructure-automation-u1w1mgs8uw3r.html)。

今年 2 月，[IBM](https://www.ibm.com/cloud?utm_content=inline+mention)[最终完成了对](https://thenewstack.io/ibm-buying-hashicorp-what-devs-analysts-and-competitors-are-saying/)云计算基础设施软件提供商 [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) 的收购。

这是本周展会上推出的 HashiCorp 产品组合的多项增强功能之一。

## 统一的基础设施管理系统

Project infragraph 将建立在 [HashiConf 云平台](https://thenewstack.io/hashicorp-cloud-platform-unifies-the-hashicorp-portfolio-for-seamless-multicloud-use/)之上，将成为一个统一的控制平面，可以提供更全面的记录，它使用图谱列出所有资产、它们服务于哪些系统以及它们如何连接。它应该能跨多个云和内部部署工作。

不同资产间的工作流将以关系模型的形式捕获。因此，任何更改都将以接近实时的视图捕获。团队所有权和配置更改也将被记录，为自动化和策略执行带来新的可能性。

它也为使用 [AI 代理](https://thenewstack.io/the-cross-app-access-protocol-makes-ai-agents-enterprise-ready/) 以编程方式执行修复、优化和规划工作流打开了大门。

## HashiConf 2025 的其他公告

总的来说，信息生命周期管理（ILM）是 HashiCorp 今年关注的一个重点，因为该公司在其产品组合中构建了多项支持 ILM 的[新功能](https://www.hashicorp.com/en/blog/scale-infrastructure-with-new-terraform-and-packer-features-at-hashiconf-2025)，在 [HashiCorp Terraform](https://thenewstack.io/terraform-gets-ai-boost-in-new-cloud-management-platform/) 和 [Packer](https://developer.hashicorp.com/packer/docs/intro) 中，重点是支持混合环境中的自动化、成本优化和合规性。

其他发布内容包括 HCP Terraform Search（Beta 版）、HCP Terraform Actions（Beta 版）以及 [HCP Terraform Stacks](https://www.hashicorp.com/en/blog/terraform-stacks-explained) 的全面重新发布，后者是一个用于管理 Terraform 多个运行实例的工具。

身份驱动的安全[也是一个重点关注领域](https://www.hashicorp.com/en/blog/strengthen-security-with-vault-boundary-and-radar-features-at-hashiconf-2025)，该公司公布了 HCP Boundary RDP 凭证注入（Beta 版）、HCP Vault Radar Jira SaaS 扫描、IDE 插件增强（Beta 版）和 HCP Vault Dedicated – 秘密清单报告（Beta 版）。