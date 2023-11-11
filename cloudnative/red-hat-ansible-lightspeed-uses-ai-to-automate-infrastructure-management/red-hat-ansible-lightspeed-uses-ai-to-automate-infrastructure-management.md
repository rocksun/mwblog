<!-- 
# 红帽Ansible Lightspeed使用AI来自动化基础设施管理
 -->

红帽 Ansible Lightspeed 借助 IBM 的 AI 技术，可以极大地减轻使用 Ansible 作为基础设施即代码相关的许多软件配置和管理任务的负担。

> 译自 [Red Hat Ansible Lightspeed Uses AI to Automate Infrastructure Management](https://thenewstack.io/red-hat-ansible-lightspeed-uses-ai-to-automate-infrastructure-management/) 。作者 BC Gain 是 ReveCom Media 的创始人和首席分析师。 他对计算机的迷恋始于20世纪80年代初，当时他破解了太空侵略者游戏机，使其可以在当地视频游戏厅以25美分的价格连续玩一整天。 之后，他开始为家用Commodore 64编写非常基本的游戏代码，并在高中电脑上用BASIC进行编程。 自那以后，他成为了一个长期坚定的Linux倡导者，并喜欢写关于IT和技术的文章。 他的署名文章散见于《连线》、《PC World》、《CIO》、《Technology Review》、《Popular Science》和《Automotive News》等刊物。

AI 和机器学习能够减轻软件配置和管理以及其他相关任务中的许多枯燥乏味、耗时耗力的方面。

这对那些服务器人员和人力知识不足的组织来说是个好消息。根据 [IDC 的统计](https://www.idc.com/getdoc.jsp?containerId=US49563122&amp;pageType=PRINTFRIENDLY)数据，到 2024 年，IT 行业领导者在云计算、数据和自动化投资方面的关键技能培训不足，将使 65% 的企业无法从中获得全部价值。

如果红帽 Ansible Lightspeed 能够做到[红帽](https://www.openshift.com/try?utm_content=inline-mention)所声称的——没有理由怀疑它做不到——其企业版红帽 Ansible Lightspeed 的全面推出可以极大地减轻使用 Ansible 作为基础设施即代码相关的许多任务的负担。

得益于 [IBM](https://www.ibm.com/?utm_content=inline-mention) Watson 提供的大语言模型([LLM](https://thenewstack.io/new-ai-dev-platform-allows-you-to-customize-open-source-llms/))和其他资源，以及红帽的实现，加上 Ansible 长期以来作为领先的基础设施即代码支持者的作用，IT 自动化将发挥关键作用。此次面向公众发布随着 [IBM 在 2018 年宣布收购红帽](https://thenewstack.io/turning-blue-ibm-to-acquire-red-hat/)，而[红帽在 2015 年收购了](https://thenewstack.io/red-hat-ansible-staying-better-together/) Ansible。

![](https://cdn.thenewstack.io/media/2023/11/1f1548ba-capture-decran-2023-11-01-202037.png)

具体来说，这个新的红帽 IT 自动化工具——尽管在其营销文本中没有被推广为基础设施即代码(IaC)产品——被红帽称为“IT 自动化工具”。它不仅可以在无人参与的情况下自动化某些流程，还可以启动和协调来自 Ansible playbook 的操作，称为“Runbook”。

正如红帽的文档中所述，Ansible Lightspeed 与 watsonx Code Assistant 一起作为 Ansible 内容创建的 AI 体验。该系统利用面向自动化的特定 IBM watsonx 基础模型，将文本提示转换为用于创建 Ansible 内容的 Ansible 代码段。生成的内容遵循公认的 Ansible 最佳实践，与 Ansible 代码机器人功能结合使用时，可以让团队对自动化代码库更有信心，红帽如是说。

![](https://cdn.thenewstack.io/media/2023/11/00668190-capture-decran-2023-11-01-202101.png)

*生成 Ansible 任务(来源: Red Hat)*

该服务由三个组件组成:

- **开发者接口**: 这个接口通过 Ansible 扩展内置于 VS Code 扩展中。这使得 Ansible 内容创建者可以在 Ansible Playbook 或任务文件中使用自然语言提示来生成 Ansible Lightspeed 的单任务和多任务建议。
- **集成服务**: 它充当开发者接口和 watsonx.ai 服务之间的胶合剂或代理。它为 Ansible Automation Platform 提供了 AI 的支持，并通过后处理功能增强了 AI 的响应效果。
- **AI**: IBM watsonx Code Assistant 提供了访问针对 Ansible 的 watsonx.ai 基础模型，该模型生成 Ansible 内容建议。这是该解决方案的“AI 核心”。

如上所述，[红帽 Ansible Lightspeed](https://www.redhat.com/en/technologies/management/ansible/ansible-lightspeed) 是 IBM 著名的 Watson 项目中开发面向自动化的特定 IBM watsonx 团队之间合作的成果，红帽 Ansible Lightspeed 利用 watsonx 进行培训。“我们真正利用了 Watson next 的培训和模型服务组件，但从我们红帽 Ansible 方面的角度来看，我们是收集组件的一方，确保它被正确训练，”红帽的 Ansible 自动化首席架构师 [Matthew Jones](https://www.linkedin.com/in/matburt/) 在接受采访时表示。

与其他通用 AI 系统不同，红帽 Ansible Lightspeed 的开发旨在产生“非常具有针对性和实用性的东西”，Jones说。“这可能听起来像营销，但这正是我们正在做的。我们主要关注产生可操作的内容，”Jones说。“您不会使用我们的产品来写书报告或类似的东西。我们是 Ansible 内容和 Ansible 创作工具的权威专家，我们非常适合整理这些内容。”

目标是“将任何想要编写代码的人变成专家，因为他们利用了我们的专业知识”，Jones说。“虽然您肯定可以从 [Copilot](https://github.com/features/copilot) 或类似的产品中获得 Ansible 内容，但我们了解编写良好 Ansible 代码的最佳实践和功能，我们有能力生成它，”Jones说。

红帽 Ansible Lightspeed 语言模型的结果具有高度可参考性。当生成推断时，例如“您要我管理这个 Azure 资源组；这是推断和底层代码”，会传达提供建议的源代码仓库。

这允许用户查看 GitHub 上建议的来源，并了解 Playbook 信息的编译方式。有了它，用户可以通过检查来源来验证建议的上下文，例如建议的 Azure 资源组名称和权限，Jones说。

“在 Lightspeed 模块中，我们不仅提供推断，而且要求您不要盲目相信我们，还提供了文档详细信息。我们会引导您访问相关的文档部分，突出显示必填字段和更多细节，”Jones说。“这种方法让您能够交叉检查并充分理解上下文。”

## 基础设施即代码组件

基础设施即代码(IaC)在 Playbook 允许用户“创建自动化”的方式中起着“至关重要”的作用，Jones说。

Playbook 始终针对特定目标自定义。例如，它可以用于在虚拟机上部署应用程序或在 Kubernetes 上部署 pod。另一方面，基础设施即代码强调组件的可组合性。客户可能有 5，000 个应用程序要部署和管理，所有这些应用程序都需要部署在组织规定的特定数据库上，如 SQL Server、Postgres 或 MySQL。

可以指示 Playbook 根据需要部署到不同的数据库，而部署数据库的自动化可能已经创建好了。例如，一个名叫“Fred”的管理员可能已经使用 Lightspeed 创建了一个安装和配置 PostgreSQL 的角色，这会被考虑在内，Jones说。

“在一个拥有 2，500 名自动化开发人员的大型企业场景中，所有人都使用 Ansible，他们不需要重写安装和配置数据库的任务。这些任务已经解决了。例如，Fred 的角色处理了 PostgreSQL 的安装和配置，”Jones说。“因此，当开发人员正在使用 playbook 且需要与数据库交互时，语言模型应该能够建议‘这里是您应该导入以处理此操作的角色’。”

## 人类的作用又是什么呢?

有了 LLM 解决方案和全面的 IT 自动化，一个永恒的问题总是出现: 到什么程度可以信任机器，以及人类什么时候以及如何应该接管控制权？这个考量对红帽 Ansible Lightspeed 尤为相关。在大规模地配置和管理基础设施时，特别是在安全和策略方面，如何确定每一个选项和组件都已正确选择，并且所有必要的配置都已正确设置?

正如 Jones 所说，答案是“您永远不应该盲目相信语言模型或 AI 建议的输出”。

“在设计该系统时，我们不仅将用户连接到语言模型。光有这还不够。在过去的两三年中，我们一直在构建开发者工具系统，其中 Lightspeed 是关键组件之一，”Jones继续说道。“它包括 Ansible 开发环境中的工具，以 VS Code 为开发的主要起点。但是，您不局限于使用 VS Code；您可以选择首选的环境。这个工具集不仅包括 Ansible，还包括我们使用 Molecule 和 Ansible 测试的测试基础设施。我们为您提供此基础设施，以允许您测试和验证语言模型的输出是否与您的专业知识和预期结果一致。”
