<!--
title:三个云管理步骤确保数据安全
cover: https://cdn.thenewstack.io/media/2023/10/2953c281-gambling-2001129_1280-1024x538.jpg
-->

即使是一些最明显的预防措施，在工程组织已经负担沉重的情况下，也未得到足够的关注和优先考虑。

> 译自 [3 Steps Cloud Governance Steps to Avoid the Next Hack](https://thenewstack.io/3-steps-cloud-governance-steps-to-avoid-the-next-hack/)，作者 Cindy Blake 是 Firefly 的市场营销副总裁，这是一家旨在解决在 DevOps 环境中使用和管理多云基础设施的许多挑战的种子资助创业公司。Blake 善于利用 AI 并将营销投资集中在努力上......

网络犯罪和黑客攻击总是令人痛心，但当它们没有任何新意，仅仅是因为 IT 治理和安全卫生不断被推迟时，它们甚至更加令人难过。

在写《[每个首席信息安全官应该采取的 10 个步骤来确保下一代软件的安全](https://www.oreilly.com/library/view/10-steps-every/9781492082910/)》这本书时，我了解到即使是最明显的一些预防措施，当涉及到已经过载的工程组织时，也没有得到足够的重视和优先级。

由于跨职能和角色之间的理解不足，优先顺序常常受到阻碍：安全团队不理解云应用开发、部署和维护方式的变化对风险的影响；DevOps 团队也不理解他们的行为如何注入或制造额外的风险。尽管这本书发表已经有几年了，但这些功能失调现象仍然存在。

MGM 遭黑客攻击告诉我们，一些众所[周知的策略](https://thenewstack.io/what-cloud-native-security-means-for-you-and-your-peers-today/)(例如社会工程学作为获得特权访问的手段)仍然是奏效的方法。一旦成功，它们将悲剧性地继续为恶意实体获取重大收益铺路。

事后诸葛亮容易，说“你本应该......”也很容易，但是重新强调和重申一些最佳实践总是有好处的，特别是在 IT 保健和治理方面。刷新一下基础知识，提醒自己一些更不起眼的待办事项，希望能有助于防止下一次黑客攻击。

## 一个随时查看的云治理检查清单

在云治理、GitOps 和云安全方面，我们已经[走过了一段很长的路程](https://thenewstack.io/4-ways-cloud-visibility-and-security-boost-innovation/)。如今，通过自动化、策略即代码以及改进的可见性的结合，可以实时准确获取信息，这些信息可以帮助你检测和补救潜在的风险。随着攻击面不断增长和演变，通过简单的警戒线最小化风险，这可能就是快速恢复和代价高昂、停机时间长的差别。

下面我们将分享每位 IT、DevOps、SRE 和安全工程师应该立即采用的一些最佳实践，以帮助[使云端符合更好的安全性和可靠性的“编码要求”](https://thenewstack.io/palo-alto-networks-brings-out-of-band-web-security-to-cloud/)。

### 1. 不变性和策略管理

我们先从不变性谈起——这个概念并不新鲜，并且通过类似 [Terraform 和基础设施即代码](https://thenewstack.io/how-to-manage-cloud-services-with-terraform/)等工具已经成为标准的最佳实践，这些工具已经将“不变性代码化”到了我们的系统中。

不变性提供的安全保障可以确保在没有干预或单个实体的情况下无法更改配置——无论是外部的恶意还是内部的无知。

这已经作为一个标准被融入了 DevOps 中，主要是为了预防生产事故和宕机时间，但作为副产品，它还提供了安全性的额外优点，确保没有人可以黑进你基于云的系统并进行未被检测到的更改，也确保没有初学者可以在没有恢复路径的情况下意外删除生产环境。

进一步推动这一点的是将成本、可靠性和安全性的警戒线编码到策略中，然后自动执行这些治理。

在吸取的另一个痛苦教训中，我们都知道，如果没有自动化，就不会发生。补丁程序就是一个很好的例子。

多年来，Fortify(我以前的雇主)的年度威胁报告中都将失败修补引用为最大的单一威胁。现在，2023年，在其年度报告《2023年 M-趋势报告》中，Mandiant 解释了为什么补丁程序和[漏洞仍然导致利用常见漏洞的全球事件](https://thenewstack.io/youll-soon-be-using-vulnerability-exploitability-exchange/)："当系统管理员需要时间来测试和验证补丁程序时，威胁者只需要最基本的概念验证(PoC)代码覆盖就可以开始针对那些组织。"

2018年的一个安全会议上，我宣布随着云采用和 DevOps 工具的使用，我预计配置错误将与补丁失败的威胁并驾齐驱。

我认为我们已经到了这一步！在他们的《M-Trends 2023报告》中，Mandiant 指出，"多层[身份管理和应用程序部署](https://thenewstack.io/okta-expands-free-identity-management-services-cloud-native-deployment-options/)为客户环境带来了必须确保安全的新的垂直性。"

报告中还说："随着[云服务迁移](https://thenewstack.io/when-you-need-or-dont-need-service-mesh/)的实施和设计阶段遇到业务运营的现实，配置错误并不少见。组织应该考虑测试其云架构部署，以提高弹性，抵御敏捷的、有动机的对手。"

[策略即代码](https://thenewstack.io/is-policy-as-code-the-cure-for-multicloud-config-chaos/)使您能够自动执行适用于云系统的规范和重复的良好实践和控制，以确保即使某些东西确实发生了变化，您也可以持续和实时地检测到云漂移和策略违规，并可以立即果断地处理这些问题。

### 2. 可见性和审计性

虽然软件物料清单 (SBOM) 和[确保您的软件供应链](https://thenewstack.io/chainguard-enforce-software-supply-chain-security-for-k8s/)一直是最新的流行词和炒作，但很少有人真正关注同样重要的基础设施物料清单 (IBOM)。

许多人都知道应用软件包含依赖项——特定子功能的模块，通常由第三方和/或开源编写。

类似地，[云原生应用所依赖的云基础设施](https://thenewstack.io/tutorial-configure-deploy-an-edge-application-on-cloud-native-edge-infrastructure/)也由依赖项组成——定义和配置特定环境使用的特定资源的子功能。

举个例子，考虑一个 EC2 实例，其依赖项可能包括网络接口和 EBS 卷。依赖可以延伸好几层。

现在考虑一下，我可能会用 Terraform 模块来管理它。此图像描述了云资源之间的实际关系。

![](https://cdn.thenewstack.io/media/2023/10/3e3846f4-iam.png)

如果开发人员更改了 HashiCorp 的 Terraform 状态，或者云工程师更改了云资源结构内的一个元素，那么我们现在就会在认为已配置的(Terraform)和实际配置的(云资源)之间出现脱节。

这被称为配置漂移，管理起来非常重要。在[2023年基础设施即代码报告](http://www.firefly.ai/state-of-iac)中，我们发现大多数人都是手动识别这种漂移的，而解决它可能需要几周的时间。

回到配置错误与修补失败并驾齐驱，这有点像让系统在无修补和脆弱的状态下保持几周。

对您的云基础设施堆栈进行全面清点和运行状况检查是进行良好审计的支柱。

那些“天生基于云”的新兴组织可以学习那些拥有本地 IT 系统遗留的组织的做法：您需要从了解自己拥有的资产开始，然后才能获得对更改历史、版本控制和管理的可见性。

对于本地 IT 系统，这种做法使用 CMDB(配置管理数据库)工具(如 ServiceNow)来编录您的资产，并使用 IT 资产管理来管理对它们的更改。

当您不得不刷员工卡进入数据中心更改硬件配置时开发的这些工具，在保持对日益变化的云资产的准确记账方面常常力不从心。

当您将所有云资源编码并自动检测漂移时，您可以[像应用代码一样对基础设施应用版本控制和历史管理](https://thenewstack.io/how-to-manage-a-home-network-with-infrastructure-as-code/)。您可以监控资产的更改时间、更改位置以及由谁更改，然后在必要时将它们回滚到以前的版本。

### 3. 由代码和 IT 治理支持的灾难恢复

除了能够查看以代码方式管理的云资产何时发生更改，并像回滚错误的提交一样回滚它们之外，这也提供了灾难恢复的额外和可能更重要的好处。

为了能够从 MGM 攻击中恢复，resort chain[遭遇 1 亿美元的勒索软件攻击](https://www.bleepingcomputer.com/news/security/mgm-resorts-ransomware-attack-led-to-100-million-loss-data-theft/)，不得不做出的最艰难的决定之一就是删除没有备份的关键资产。

黑客利用的应用程序之一是 Okta，这使他们最终获得了公司服务器的访问权限，并对许多关键业务应用程序发起了非常痛苦的拒绝服务攻击。

我们历来都在谈论对关键业务云资产进行编码的必要性，以及对所有 SaaS 应用程序配置进行编码的必要性，这包括像 Okta 这样的身份管理服务。

如果[ Okta 配置也以代码的方式进行管理](https://www.firefly.ai/blog/okta-as-code)，并将相同的版本控制实践应用于这个关键的单点登录服务，那么这次违规的平均恢复时间会大大缩短，业务中断和损失也会最小化。

如果 IT 管理员意外删除了重要的系统配置，或者由于数据损坏甚至软件被勒索(就像 [Caesars 度假村在 MGM 攻击前一周遭遇的那样](https://www.reuters.com/technology/cybersecurity/okta-says-hackers-stole-data-all-customer-support-users-cyber-breach-2023-11-29/))，也是如此。

这是以代码方式管理所有云资产(也称为一切即代码)的固有优势，以及自动化、一致部署和审计性的附加优势。

Okta 不是您应该以代码方式管理的唯一 SaaS 应用程序，所有 SaaS 应用程序——从监控工具到应用性能管理 (APM)、身份和访问管理 (IAM) 工具和内容分发网络 (CDN)——都应当纳入以代码方式管理其配置的策略中，以获得灾难恢复的好处。

有很多工具(其中包括 Firefly)可以扫描您的云，找到这些资源并自动将其导入基础设施即代码(如 Terraform、Pulumi 或 CDK)，它可以作为重要应用程序(如 CloudFlare、DataDog 和您的 git 存储库)的快速备份服务。如果您的软件存储库被损坏或勒索，没有这些备份，您需要多长时间才能恢复？

[典型的云基础设施还包括许多其他需要编码和治理的安全设置](https://thenewstack.io/accurics-secures-cloud-infrastructure-through-policy-as-code/)。例如，考虑安全组。

[安全组充当防火墙，控制允许进入和离开您虚拟私有云(VPC)中的资源的流量](https://thenewstack.io/service-mesh-adds-security-observability-and-traffic-control-to-kubernetes/)。您可以选择允许入站流量和出站流量的端口和协议。几种云服务依赖安全组，包括:

- Amazon EC2 实例
- AWS Lambda
- AWS 弹性负载均衡
- 容器和 Kubernetes 服务(ECS 和 EKS)

如果安全组设置发生更改，您可以想象可能的后果。将此重要资源捕获为基础设施即代码，然后管理其更改和策略对齐，是[保护您的组织](https://thenewstack.io/zeronorth-one-risk-based-view-for-all-an-organizations-security-tools/)的重要方面。

## 检查您的云

云治理并非未知领域。尽管它确实需要一些领域专业知识，但现在许多这些实践已经确立并被广泛了解。

如果不对 IT 和云环境应用简单的推荐良好实践，您就会危及敏感的客户信息和业务关键系统。

随着云利用率的增长，对我们的云基础设施的 IT 治理和安全的基本面进行更好的覆盖已势在必行。让我们不要关闭旧的缺口，是时候让我们的工程师专注于更加新颖和新兴的威胁了。

