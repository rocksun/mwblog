
<!--
title: 2024年的基础设施即代码：为什么它仍然如此糟糕
cover: https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1.png
-->

工具碎片化，集成困难，配置噩梦：IaC 工具的用户们忍无可忍了。基础设施即代码的兴起能否带来帮助？

> 译自 [Infrastructure as Code in 2024: Why It's Still So Terrible](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/)，作者 Joab Jackson。

从The New Stack的Looker流量报告深处，我们挖掘出了2024年关于[基础设施即代码(IaC)](https://thenewstack.io/infrastructure-as-code/)主题中最受关注的帖子。总的来说，这些帖子表明，尽管IaC在扩展IT系统方面具有优势，但它仍然存在许多让DevOps人员抓狂的问题。

“在广泛使用Terraform之后，我确实欣赏基础设施即代码作为加速器的魔力。然而，重构是‘第2天’运营的现实，而使用Terraform进行重构仍然非常痛苦，”安全公司[Chainguard](https://www.chainguard.dev/?utm_content=inline+mention)的创始人兼CTO告诉TNS。

云服务创造了“基础设施即代码”实践的需求，因为组织在[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)和其他提供商上建立其运营。[Puppet](https://thenewstack.io/puppets-open-source-community-plans-to-fork-the-program/)和[Chef](https://www.chef.io?utm_content=inline+mention)创建了声明性的、特定领域的语言，以此来自动化配置和供应工作，以建立和维护这些系统。

而[Kubernetes](https://roadmap.sh/kubernetes)凭借其编排微服务的能力，使这种实践加速发展。因此，[HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention)的[Terraform](https://thenewstack.io/new-terraform-features-manage-migrations-modules/)出现了，以管理下一级别的云供应。

但是，尽管Terraform和相关的IaC工具带来了巨大的价值，[DevOps团队](https://thenewstack.io/DevOps/)却比以往任何时候都感到更加沮丧。

The New Stack在2024年最受欢迎的10个IaC故事展示了他们感受到的挫败感，以及一些可能的未来发展方向。

## 1. [基础设施即代码已死：代码生成的基础设施万岁](https://thenewstack.io/infrastructure-as-code-is-dead-long-live-infrastructure-from-code/)


在这篇投稿文章中，一家当时名为[appCD](https://thenewstack.io/appcd-lifts-developer-load-by-automating-infrastructure-from-code/)，现在名为[StackGen](https://stackgen.com/)的公司联合创始人兼首席产品官指出，安全可靠且一致地管理、维护和部署应用程序和基础设施仍然是一个极其复杂的挑战。

他指出，解决方案是“根据正在部署的应用程序版本生成应用程序所需的基础设施”。

他将这种方法称为“代码生成的基础设施”。

## 2. [我们如何从IaC演变到环境即代码](https://thenewstack.io/how-we-evolved-from-iac-to-environments-as-code/)

[Quali](https://www.quali.com/?utm_content=inline+mention)的CTO指出，IaC工具的设计目标是速度和自动化，而不是作为环境的真相来源。它们非常适合部署云服务，但作为预测代码更改如何改变应用程序性能的工具，它们非常糟糕。
此外，IaC工具之间不能很好地协同工作。

他指出，Quali重新思考了IaC流程，定义了开发人员启动环境所需的一切，使其易于机器和人类理解。然后，团队可以使用[GitOps](https://thenewstack.io/4-core-principles-of-gitops/)作为基础来启动应用程序。

## 3. [Terraform并没有死](https://thenewstack.io/terraform-isnt-dead/)

[Nitric](https://nitric.io?utm_content=inline+mention)的也是代码生成的基础设施(IfC)的支持者。

问题是，Siva 写道，“当开发人员决定用第三方服务替代手动管理的存储桶时，相应的 IaC 脚本也必须手动更新，这在项目规模扩大时会变得繁琐且容易出错。应用程序及其运行时之间发生的脱同步可能导致严重的安全隐患，例如资源被授予远超其所需权限，或被遗忘而成为游离资源。”

他补充道：“基础设施即代码自动化了以前手动操作的部分。每当应用程序发生变化时，IaC 就能帮助配置准确反映其运行时需求的资源和配置，从而消除通常涉及的大量手动工作。”

Siva 指出，开发人员无需编写低级配置代码来执行诸如设置 IAM 角色和权限之类的任务，而只需要知道它可用即可。

Nitric 提供了一个开源 IaC 框架，用于在您选择的语言中构建并在所有主要云平台上部署。


> 基础设施即代码是单向的，具有非对称体验，其中更改（写入）和观察（读取）通过不同的工具执行。这会带来哪些后果？这真的必要吗？
>
> [https://t.co/O1WJX6yhic][#infrastructureascode]— Brian Grant (@bgrant0607) 2024年12月23日

## 4. [OpenTofu 项目否认 HashiCorp 的代码窃取指控](https://thenewstack.io/opentofu-project-denies-hashicorps-allegations-of-code-theft/)

除了 Terraform 给开发人员造成的所有手动工作之外，在过去一年中，围绕这个工具集本身也存在很多不确定性。2023 年 8 月，[HashiCorp 将该软件从开源许可证更改为更严格的商业源许可证 (BSL)](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)，以阻止竞争服务提供商。

因此，一些公司，例如 [Spacelift](https://spacelift.io/)，[将开源代码的最后一个版本分叉到自己的项目中](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/)，该项目将被称为 [OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next/)，并[迅速得到 Linux 基金会的支持](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/)，后者需要一个开源 IaC 工具作为其 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 堆栈的一部分。

许可证也不是唯一的问题；Terraform 的高级用户抱怨 HashiCorp 接受外部错误修复的速度很慢。他们认为需要一种更易于接受的软件管理模式。

当然，HashiCorp 对此分叉并不满意，并在 4 月份试图通过指控开源集体从现在采用 BSL 许可的 Terraform 中窃取代码来质疑这项工作。OpenTofu 团队迅速驳斥了这些指控，并继续其 [现代化](https://thenewstack.io/new-opentofu-release-challenges-terraforms-dominance/) OpenTofu 的旅程。

## 5. 为什么大多数公司都在努力使用基础设施即代码

根据 StackGen 最近的一项调查，“[Stacked Up：IaC 成熟度报告](https://stackgen.com/stackedup-infographic-2024)”显示，迄今为止，只有 13% 的组织实现了 IaC 成熟度。大多数人认为只有他们的一些基础设施以代码形式表示，但只有 10% 的组织启动了试点项目。

StackGen 的联合创始人兼首席商务官 [Arshad Sayyad] 在这篇文章中指出，实现 IaC 成熟度很难。

大多数接受调查的公司仍处于早期阶段，只有一小部分基础设施存储在试点项目的代码中。Sayyad 还推荐了 IaC，他写道：“IaC 本身是从应用程序代码自动生成的，并内置了符合最佳实践的防护措施。”

## 6. [超越基础设施即代码：系统计划正式启动](https://thenewstack.io/system-initiative-goes-live-beyond-infrastructure-as-code/)

寻求超越 Terraform 的解决方案。今年，Chef 前 CTO [Adam Jacob] 推出了自己的公司 [System Initiative](https://www.systeminit.com/)，该公司提供了一个自动化平台，在这个平台上，管理员可以使用基于图形网格的工作区将小型、反应式函数拼接在一起，从而允许系统被管理为“活架构”。
管理基础设施即代码似乎是个好主意，但它会导致“各种下游问题”，Jacob 告诉 TNS。

“这不是单一的技术问题，而是我们被要求使用的形状、基础和基元，在绝大多数情况下会导致这些[负面]结果。”

## 7. [用于基础设施即代码的生成式 AI 工具](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/)

但是等等，也许 AI 可以提供帮助！[戴尔科技](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline+mention)的[Parasar Kodati](https://www.linkedin.com/in/parasarkodati) 指出，[大型语言模型](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) (LLM) 非常擅长分析错误消息和日志，以识别频繁出现问题的根本原因。这种方法也适用于任何平台，包括[红帽](https://www.openshift.com/try?utm_content=inline+mention)[Ansible Playbooks](https://thenewstack.io/red-hat-brings-ansible-automation-to-amazon-web-services/) 和 Terraform。

除了检查错误代码外，生成式 AI 还可用于设置您自己的个性化聊天机器人来回答问题。

“您可以使用任何内容（例如策略文档、编码指南或 IT 基础设施大小计算器）来训练 GPT 模型，并让聊天机器人使用这些后端模型来回答客户或内部利益相关者的查询，”Kodati 写道。

## 8. 对于 Terraform 部署，任何 CI/CD 都能胜过 TACOS

解决 IaC 分裂问题的第一个解决方案之一是[Terraform 自动化和协作软件](https://spacelift.io/terraform-automation) (TACOS)，它试图找到一种方法，将 IaC 置于与我们用于应用程序代码相同的治理和协作工作流程下。但管理员没有看到 TACOS 实施的隐藏成本，这些成本以集成挑战、配置混乱和潜在的系统碎片的形式出现，[Eran Bibi](https://www.linkedin.com/in/eran-bibi)（[Firefly](https://www.firefly.ai?utm_content=inline+mention) 的联合创始人兼首席产品官）在这篇文章中指出。

Bibi 认为，答案在于改进[CI/CD](https://thenewstack.io/ci-cd/) 管道上的工具。这种方法可以轻松地与“代码即策略”和“代码即治理”计划集成，从而提供“一种更全面的基础设施管理方法，无需额外一层工具”。

## 9. [OpenTofu 乐于进行 Terraform 协调](https://thenewstack.io/opentofu-amiable-to-a-terraform-reconciliation/)

与此同时，关于 Terraform 分裂方面有一些潜在的好消息。4 月，[IBM](https://www.ibm.com?utm_content=inline+mention)[宣布](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) 将收购 HashiCorp 及其围绕 Terraform 构建的 IaC 产品组合。

将 Terraform 置于 BSL 许可证下的主要原因之一是财务性质的，许多人很快开始[猜测](https://thenewstack.io/with-ibms-open-source-roots-terraform-could-be-free-again/)，IBM（历史上一直对开源友好）可能会撤销 BSL 决定，并将软件重新置于开源之下。并且，在接受 The New Stack 采访时，OpenTofu 的维护者表示，如果将其放回开源，他们将很乐意将其工作合并回 Terraform。

到目前为止，IBM 没有任何迹象表明它计划做任何类似的事情，尽管一旦交易完成（应该很快就会发生），我们可能会听到更多消息。

而且，截至发稿时，另一个 IaC 工具[正在被分叉](https://thenewstack.io/puppets-open-source-community-plans-to-fork-the-program/)，即[Puppet](https://puppet.com/?utm_content=inline+mention)，从其目前的拥有者[Perforce](https://www.perforce.com/) 分叉，原因是对该公司改进的[分发](https://www.puppet.com/blog/open-source-puppet-updates-2025) 方法的反对。因此，IaC 社区应该为更多工具碎片化做好准备。

## 10. OpenTofu 能否成为基础设施即代码的 HTTP？

围绕OpenTofu的开源工作或许指明了摆脱困境的道路。至少行业观察员的观点如此，他将Terraform的开源比作开启互联网技术的先河，认为OpenTofu是“云计算的HTTP”，env0公司首席执行官兼联合创始人写道。

“为了让Terraform技术实现像HTTP一样的普遍采用，它必须超越其商业起源，”  写道。“换句话说：在它能属于每个人之前，它不需要属于任何人。”

*TNS分析师 Lawrence E. Hecht 为本报告做出了贡献。*

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展日新月异，不要错过任何一期。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。