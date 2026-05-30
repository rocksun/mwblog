[Automation Anywhere](https://www.automationanywhere.com/) 发布的关于 [EnterpriseClaw](https://www.automationanywhere.com/products/enterprise-claw) 的新闻稿版本非常直截了当：一种用于部署该公司所谓的“爪型” AI 智能体的新功能。

这些是[自主智能体](https://thenewstack.io/why-apis-are-the-missing-link-for-truly-autonomous-ai-agents/)，能够访问设备文件系统、在运行时创建工具，并直接与整个企业基础设施中的应用程序进行交互。这得到了与 [Cisco](https://thenewstack.io/cisco-is-using-ebpf-to-rethink-firewalls-vulnerability-mitigation/)、[Nvidia](https://thenewstack.io/nvidia-nemoclaw-launch/)、[Okta](https://thenewstack.io/okta-expands-free-identity-management-services-cloud-native-deployment-options/) 和 [OpenAI](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/) 合作伙伴关系的支持。它提供了更好的安全性，Nvidia 贡献了 [OpenShell](https://thenewstack.io/nvidia-openshell-agent-runtime/)，Okta 将提供身份管理，而 OpenAI 将允许企业在 EnterpriseClaw 中使用全新的 GPT 5.5。

更引人深思的是，在上周该公司的 [Imagine 2026](https://imagine.automationanywhere.com/) 大会上推出的 EnterpriseClaw，揭示了 AI 智能体的构建方式与企业实际运作方式之间的差距。

## **“爪型”智能体**

Automation Anywhere 的首席 AI 及开发官 [Adi Kuruganti](https://www.linkedin.com/in/adikuruganti27/) 坦率地透露了这一想法的来源。Nvidia 的 OpenShell —— 一个用于自主、自我进化智能体的开源运行时，基本上可以让智能体复制人类操作员在键盘上能做的任何事情。这种能力的结合正是 Automation Anywhere 所称的“爪型”智能体（这是该公司创造的一个词汇）。

他表示，EnterpriseClaw 基本上是将 OpenShell 的能力包裹在集中式治理之中。一个“爪型”智能体与传统智能体在三个方面有所不同：设备级访问（本地或共享）、运行时动态工具创建，以及与电脑屏幕的交互。

Kuruganti 表示，问题在于 OpenShell “几乎可以访问所有内容，这在企业环境中并不是一件好事。”

对于个人用户或孤立的云环境，广泛的系统访问是一项功能。但对于在物理隔离的数据中心运行流程的医疗系统、银行或制造商来说，这可能会导致治理失效。

EnterpriseClaw 就是 Automation Anywhere 给出的答案。它采用了自主模型，增加了集中式治理、凭据控制、可观测性，以及在靠近数据所在地运行智能体的能力。这包括防火墙背后的环境以及永远不会接触公共云的环境。

## **行业性的身份危机**

在这四个合作伙伴集成中，最能说明问题的也许是 Okta 的。Kuruganti 告诉 *The New Stack*，智能体身份（涉及自主智能体如何向企业系统进行身份验证、获得什么访问权限，以及如何独立于其代表的人类对其行为进行审计）在整个行业中仍处于建设阶段。

他说，现状有些尴尬。大多数企业仍在使用人类凭证让智能体访问 Salesforce 或 SAP 等系统。这意味着当智能体自主执行某个流程时，审计追踪会显示是人类执行了该操作。

“无法清晰记录哪些是智能体做的，哪些是人类做的，” Kuruganti 说道。

Okta 的“一等公民身份”模型——每个智能体都拥有自己的身份、访问范围和审计追踪——是目前提出的解决方案，该公司正在努力将其建立为跨供应商的标准，而不仅仅是与 Automation Anywhere 的集成。这项工作目前仍在进行中。

## **混合云的现实**

Kuruganti 指出，几乎所有人都在面向云端进行构建，但企业数据尚未完全迁移到云端。

“目前市面上的大多数智能体平台都只想到了完全依赖云端，”他说，“但现实是，大多数数据并不存在于云端。”

对于医疗保健、金融服务和制造业的大型企业（Kuruganti 将其确定为 Automation Anywhere 的三个核心客户行业），数据存在于本地、私有云 VPC 中，在某些情况下，还存在于无法选择云连接的物理隔离环境中。

Kuruganti 表示，这正是 EnterpriseClaw 在架构上做出的赌注：对企业自动化而言最关键的客户，并不是那些已经将一切迁移到云端的客户，而是那些还没有迁移且短期内也不会迁移的客户。

他补充道，Nvidia 在合作伙伴关系中的角色直接反映了这一点——通过 OpenShell 在本地运行的 [Nemotron](https://thenewstack.io/nvidia-launches-nemotron-3-super-a-120b-open-model-for-large-scale-ai-systems/) 模型正是为了满足那些裸金属数据中心无法连接到云端推理端点的客户需求。

## **编排之争**

Automation Anywhere 如何定位 EnterpriseClaw 及其编排能力，以对抗 ServiceNow、Microsoft 等竞争对手，同样值得探究。Kuruganti 将该公司定位为“业务流程编排领域的瑞士”，这是对那些以平台为中心的竞争对手的一种讽刺。

他的观点是，ServiceNow 在 ServiceNow 的生态系统内进行自动化；Microsoft 在 Microsoft 的生态系统内进行自动化。相比之下，Automation Anywhere 的 Mozart Orchestrator 旨在统一的治理层下，管理在任何平台（包括竞争对手的平台）上构建的智能体。

这就是该公司的价值主张。客户是否真的有这样的体验则是另一个问题。但智能体平台的激增正在带来新的编排挑战，并且需要一种跨平台的智能体治理解决方案。

## **现状与进展**

EnterpriseClaw 目前处于预览阶段，Automation Anywhere 的客户现在可以根据现有的消费定价进行使用。预计今年晚些时候将推出包含专属包装的正式商用版（GA）。该公司表示，预览版的定位并非技术限制（生产部署已经在进行中），而是出于商业考虑：他们尚未最终确定定价方式。

在 Imagine 大会上，Automation Anywhere 还宣布了自主 IT 和自主财务——这些是针对 CIO 和 CFO 办公室的预构建解决方案，将 AI 智能体、流程智能和治理控制结合在一起。这两项方案目前均已可用。