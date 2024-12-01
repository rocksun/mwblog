# 摒弃全云或全本地：拥抱混合云以提升敏捷性和降低成本

IT基础设施在过去二十年中不断发展，以满足日益增长的速度、灵活性和成本效率的需求。从2000年代初期向虚拟化环境的转变，到2010年代[基础设施即代码](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/) (IaC) 的普及，每一次新的技术进步都[推动企业更接近](https://thenewstack.io/why-companies-are-ditching-the-cloud-the-rise-of-cloud-repatriation/)无缝的基础设施管理。

如今的计算现实已超越简单的自动化。随着[企业应对日益复杂的数据](https://thenewstack.io/can-companies-really-self-host-at-scale/)、安全和监管需求，混合云模型——一种本地和云环境的融合——[成为可持续、多功能基础设施的逻辑选择](https://thenewstack.io/cloud-vs-on-prem-comparing-long-term-costs/)。

## 双重驱动：敏捷性和稳定性

混合云的核心思想很简单：在需要快速扩展和频繁更改的地方使用云环境，并依靠本地系统处理稳定、可预测的工作负载。这种方法允许公司为其在云环境中所需的灵活性付费，同时避免为稳定性和合规性过度付费，因为它们可以在本地系统中以较低的成本维护这些方面。  [需要快速扩展](https://thenewstack.io/ephemeral-environments-are-better-for-scaling-devops-tests/)

混合云在其根据特定需求迁移工作负载的能力方面表现出色。云非常适合测试和实验，但一旦应用程序稳定下来，将其在本地运行通常更具成本效益。

然而，令人担忧的是，HashiCorp的[2023年云战略调查](https://www.hashicorp.com/blog/hashicorp-state-of-cloud-strategy-survey-2023-maturity-drives-operational-efficiency)报告显示，近1000名受访者中有945人承认，由于云资源利用不足而产生了不必要的支出。纠正这种浪费是越来越多地采用混合架构的主要驱动力之一。

成本控制正促使更多公司将工作负载迁移回本地。[一项Citrix研究](https://www.citrix.com/news/announcements/feb-2024/research-finds-it-leaders-are-choosing-hybrid-cloud-strategies-due-to-flexibility-costeffectiveness-and-security.html)显示，42%的美国组织正在考虑或已经将至少一半的云工作负载迁移回本地。一个众所周知的例子是，[Basecamp](https://basecamp.com/cloud-exit) 将稳定的工作负载迁移回本地，预计五年内可节省700万美元。

另一个著名的案例是Dropbox，其在[2018年2月的S-1声明](https://www.sec.gov/Archives/edgar/data/1467623/000119312518055809/d451946ds1.htm)中报告称，通过转向混合方法，两年内节省了7500万美元的运营成本。在5月份的AnsibleFest上，我和Dropbox的一位人士进行了交谈，他告诉我，对该公司来说，将所有内容都保留在云中成本太高了。他说他们为很多未使用的服务付费——例如启动和关闭的灵活性。他告诉我，Dropbox现在有80%的工作负载回到了本地，而之前是100%在云端。

## 超越成本节约：混合云的额外优势

混合云不仅仅是降低成本——它还能提高速度、安全性以及性能。敏捷的应用程序在云中运行速度更快，团队可以快速启动、测试和启动，而无需受限于本地系统。当快速交付软件以满足市场[需求而又不影响整个系统的核心稳定性](https://thenewstack.io/why-cloud-native-systems-demand-a-zero-trust-approach/)时，这种敏捷性变得尤为宝贵。

安全性和合规性也是混合云采用的关键驱动力。监管要求通常需要数据保留在本地，以确保符合当地数据驻留法律。混合基础设施允许公司将面向客户的应用程序迁移到云端，同时将敏感数据保留在本地。这种将数据与前端层分离的做法已成为金融和政府等行业的常见做法，在这些行业中，合规性要求和数据安全是不可谈判的。

我一直在定期与美国两家大型银行的CTO进行交流。他们目前在云中管理15-20%的工作负载，并估计他们将来在云中最多只会拥有40-50%的工作负载。他们告诉我，其余部分将始终保留在本地——因此他们将始终需要管理混合环境。
最后，性能是另一个关键因素。针对特定应用程序微调基础设施的能力，在公司完全控制硬件和网络配置的本地环境中通常更容易实现。高性能工作负载可以保留在内部，以最大限度地减少延迟，而要求较低的工作负载则可以在云中扩展。企业可以同时获得两全其美的优势：他们可以在云基础设施上处理用户激增的情况，同时确保本地资源密集型稳定应用程序的稳定、高速运行。

## 编排工具：使混合环境易于管理
混合方法还会在管理单独环境的凝聚力方面带来复杂性。为了解决这个问题，公司需要编排平台来创建跨云和本地环境的统一视图，确保一致性、安全性和效率。编排平台不仅仅是自动化任务——它们协调跨[架构的流程以确保混合设置中的效率和安全性](https://thenewstack.io/how-to-secure-microservices-in-a-multicloud-architecture/)。这种协调有助于减少基于云的动态环境与本地稳定设置之间的摩擦，为平台团队创建流畅的工作流程。

例如，一个月前，我和一家大型金融服务公司的领导进行了交谈。由于安全和合规性原因，该公司无法将其所有工作负载完全迁移到云端。因此，他们使用 Ansible 管理一些内部工作负载，使用 Terraform 管理一些云端工作负载。该公司花费了超过一百万美元用于管理这些脱节的架构和独立的基础设施团队。他们告诉我：“我们永远不会只选择其中一种，所以我们需要一种方法来桥接和管理这个混合环境，因为它会一直存在。”

Spacelift 等编排平台有助于简化基础设施编排——使用单个仪表板与流行的工具集（如[OpenTofu](https://spacelift.io/blog/what-is-opentofu)、Terraform 和 Ansible）集成，跨混合基础设施。这些专为混合架构设计的统一平台，为[开发人员提供自助配置功能，同时解放平台团队](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/)，专注于更广泛的治理和控制措施。通过实现开发人员自主性和安全资源管理，编排工具直接解决了混合架构的核心目标：提高开发人员速度，同时确保安全性和成本控制。

## 混合的未来
随着公司扩展其基础设施，混合模型的适应性将成为企业架构中的主要内容。这并不是选择云还是本地环境的问题；而是为每个工作负载选择最佳环境的问题。但是，有效的编排对于管理这些混合设置的复杂性至关重要，使平台团队能够保持高开发速度并控制整个基础设施的安全性和成本。

*本文是The New Stack贡献者网络的一部分。对影响开发人员的最新挑战和创新有见解吗？我们很乐意听到您的声音。成为贡献者并分享您的专业知识，请填写此表格或发送电子邮件至mattburns@thenewstack.io。*

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)