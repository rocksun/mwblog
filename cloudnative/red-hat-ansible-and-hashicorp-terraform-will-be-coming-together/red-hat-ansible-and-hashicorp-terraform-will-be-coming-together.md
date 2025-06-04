
<!--
title: 红帽Ansible和HashiCorp Terraform即将结合
cover: https://cdn.thenewstack.io/media/2025/05/a5fbc86d-jorge-ramirez-vadci9b4hbo-unsplash.jpg
summary: Red Hat Summit重磅！Ansible将与Terraform、Vault深度集成，简化混合云环境配置与部署。Terraform将能动态生成Ansible清单，反之亦然。或将探索Ansible Lightspeed AI技术赋能Terraform，打造IaC、CaC一体化平台。
-->

Red Hat Summit重磅！Ansible将与Terraform、Vault深度集成，简化混合云环境配置与部署。Terraform将能动态生成Ansible清单，反之亦然。或将探索Ansible Lightspeed AI技术赋能Terraform，打造IaC、CaC一体化平台。

> 译自：[Red Hat Ansible and HashiCorp Terraform Will Be Coming Together](https://thenewstack.io/red-hat-ansible-and-hashicorp-terraform-will-be-coming-together/)
> 
> 作者：Steven J Vaughan-Nichols

波士顿 — 如果您期望 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 和 [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) 在 [Red Hat Summit](https://www.redhat.com/en/summit) 上发布新闻，说明他们将如何把卓越的 DevOps 程序 [Ansible](https://www.redhat.com/en/ansible-collaborative) 与基础设施即代码 (IaC) [Terraform](https://developer.hashicorp.com/terraform) 和密钥管理器 [Vault](https://www.hashicorp.com/en/products/vault) 集成，那么您可能会失望。但是，如果您仔细听，就会听到一些计划正在酝酿中，目的是让这三个程序更容易地协同工作。

毕竟，这很有意义。在 [IBM 收购 HashiCorp](https://thenewstack.io/ibm-buying-hashicorp-what-devs-analysts-and-competitors-are-saying/) 于 2025 年 2 月完成后，IBM 准备为企业提供一个紧密集成的端到端自动化设置，以应对日益复杂的云环境。IBM 首席财务官 James Kavanaugh 在 IBM 2024 年 4 月的 [财报电话会议](https://newsroom.ibm.com/2024-04-24-IBM-to-Acquire-HashiCorp-Inc-Creating-a-Comprehensive-End-to-End-Hybrid-Cloud-Platform) 中告诉我们，这始终是计划的一部分，“Red Hat 的 Ansible Automation Platform (AAP) 的配置管理和 Terraform 的自动化的强大结合将简化跨混合云环境的应用程序的配置和部署。”

不仅仅是技术上的良好结合；它们的商业案例也很好地同步了。根据企业对企业市场分析公司 [6Sense](https://6sense.com/) 的数据，[Terraform 在配置管理市场中](https://6sense.com/tech/configuration-management/terraform-market-share) 占有 33.48% 的市场份额。紧随其后的是 Ansible，以 31.66% 的份额位居第二。

从历史上看，组织一直将 Terraform 和 Ansible 配对使用，以实现基础设施和应用程序部署的自动化：Terraform [配置和管理](https://thenewstack.io/lessons-from-humanas-migration-to-hcp-terraform-cloud/) IaC 部署，而 Ansible 处理[配置管理和应用程序部署](https://thenewstack.io/install-ansible-on-ubuntu-server-to-automate-linux-server-deployments/)。然而，这些集成通常需要手动步骤、自定义脚本或“粘合代码”来保持工作流的同步。

## 混乱

总而言之，这是“混乱的”。因此，正如 HashiCorp 联合创始人兼首席技术官 Armon Dadgar 在收购完成后不久的一篇博文中解释的那样，这是合理的，“我们听到了极大的热情的一个机会——并且是当今客户解决方案的积极组成部分——是 [HashiCorp Terraform 与 Red Hat Ansible Automation Platform 以及 HashiCorp Vault 与 Red Hat OpenShift](https://www.hashicorp.com/en/blog/hashicorp-and-red-hat-better-together)。”

Dadgar 随后概述了几个具体的计划和正在进行的项目，以加深 Terraform 和 Ansible 之间的协同作用。首先，您将能够使用 Terraform 动态生成 Ansible 清单，因为它配置基础设施，从而确保 Ansible 始终具有托管资源的最新视图，而无需手动干预。两家公司还在开发 Ansible 的官方支持的 Terraform 模块，反之亦然。这将使您能够从 Terraform 触发 Ansible playbook，并从 Ansible 工作流调用 Terraform 操作。

本周，在与 AnsibleFest 同地举行的 Red Hat Summit 上，Dadgar 补充说，“Terraform Enterprise 将添加一个配置后钩子，以在使用 IaC 创建资源后调用 AAP 配置工作流。” 相反，Ansible 会将工作流作业模板链接到 Terraform Enterprise，并为 Terraform 和 Vault 基础设施提供 AAP 配置即代码 (CaC) 支持。因此，Ansible 将能够使用 Vault 凭据。这将简化从基础设施配置到配置管理的过渡。

此外，通过利用 Terraform 的状态管理作为事实来源，Ansible 可以确保配置一致性，并支持高级的 Day 2 操作，例如漂移检测和修复。

Dadgar 补充说，Terraform Enterprise 和事件驱动的 Ansible 将“更深入一层”，以加强超出配置的集成。最终，Ansible 用户将能够共享官方支持的 Terraform providers 和模块。

## 你无法从这里到达那里
在今天的峰会炉边谈话中，Dadgar 和红帽 CTO [Chris Wright](https://www.linkedin.com/in/chris-wright-b733851/) 总结道：“Terraform 没有实现 Ansible 的机制。” 例如，“你到了第 n 天，你说，‘好吧，在从 Ansible 清理 VM 以便从 ServiceNow 取消注册，或者取出所有证书，或者删除我的 EDR 软件之前。’ 今天没有办法做到这一点。因此，我们在生命周期中识别出了一堆这样的钩子点，并说，‘我们如何才能将 Terraform 和 Ansible 紧密集成起来’……最终，这实际上是告诉客户 Terraform 和 Ansible 紧密集成，以至于他们感觉像是一个单一的平台，而不是你必须用胶带粘在一起的工具。”

不仅仅是这两个顶级程序被整合在一起。在一次采访中，Wright 告诉我，“HashiCorp 有兴趣了解我们使用 [Ansible Lightspeed](https://www.redhat.com/en/technologies/management/ansible/ansible-lightspeed) 所做的事情”，因此也许我们可以期待 Terraform Lightspeed 将 AI 技术支持带给 Terraform 用户。由于 Lightspeed 平台已经移植到 Red Hat Enterprise Linux (RHEL) 10 和 OpenShift，因此这一举措应该相对容易做到，并且肯定会找到热情的用户。不过，Wright 告诉我，它尚未列入路线图，但也许 Dadgar 将在今年晚些时候宣布它。敬请关注。

从我的角度来看，从长远来看，这一切意味着 IBM 将 Red Hat Ansible 和 HashiCorp Terraform 集成在一起，不仅仅是一项技术增强，更是一项巩固 IBM 在混合云自动化领域领导地位的战略举措。Ansible、Terraform 和 Vault 可能会很快为客户提供一个用于基础设施配置、配置、安全性和成本管理的一体化平台。