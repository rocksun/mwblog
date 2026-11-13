<!--
title: 平台团队才是用户
cover: https://cdn.thenewstack.io/media/2026/07/45a2a83b-img_0484-1024x768.jpg
summary: 英伟达将其开源智能体安全运行时OpenShell捐赠给CNCF。文章探讨了为何将其纳入云原生基金会、平台团队如何作为其核心用户，以及不同开源基金会在AI智能体技术栈中扮演的分工角色。
-->

英伟达将其开源智能体安全运行时OpenShell捐赠给CNCF。文章探讨了为何将其纳入云原生基金会、平台团队如何作为其核心用户，以及不同开源基金会在AI智能体技术栈中扮演的分工角色。

> 译自：[The platform team is the user](https://thenewstack.io/nvidia-donates-openshell-cncf/)
> 
> 作者：Frederic Lardinois

**本周，Nvidia将OpenShell捐赠给**云原生计算基金会（CNCF）。OpenShell是Nvidia用于保障AI智能体安全和管理的开源运行时。Nvidia负责该项目的AI软件高级总监Ali Golshan表示，在生产环境中运行该项目的团队已经在使用Kubernetes以及CNCF的其他项目。

该公司周二在盐湖城举行的KubeCon + CloudNativeCon北美峰会上[宣布](https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/)了这一举动。[OpenShell](https://github.com/ai-openshell)是Nvidia在3月份的GTC大会上推出的，它[作为Sandbox项目加入CNCF](https://www.cncf.io/blog/2026/11/10/welcoming-openshell-to-cncf-open-governance-to-secure-agentic-ai/)，这是该基金会针对早期项目的入门级层级。CNCF于9月下旬正式接受了该项目。

CNCF目前托管了262个项目，其中包括155个Sandbox级别的项目，但CNCF并不是OpenShell唯一的潜在归宿。CNCF的母公司Linux基金会还运营着智能体AI基金会（AAIF），该基金会托管了agentgateway、模型上下文协议（MCP）和Agent2Agent（A2A）协议。上个月，AAIF还[接纳了OpenSandbox](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox)，这是一个由阿里巴巴贡献的AI智能体沙箱平台。

> “围绕AI确保安全和建立信任实际上就是基础设施。这正是你需要开始的地方。”

但正如[Golshan](https://www.linkedin.com/in/ali-golshan)告诉 *The New Stack* 的那样，“围绕AI确保安全和建立信任实际上就是基础设施。这正是你需要开始的地方。”他说，这正是让CNCF成为该项目落地的合乎逻辑的地方。

## 平台团队才是用户

OpenShell在沙箱中运行智能体，并强制执行关于该智能体可以访问哪些文件、网络、凭证和模型端点的策略。[据CNCF称](https://www.cncf.io/announcements/2026/11/10/cncf-hits-major-milestones-with-global-community-growth-record-industry-investment-and-a-new-generation-of-projects-to-build-ai-systems-in-production/)，这种强制执行发生在智能体周围的基础设施中，该项目正在采用另一个CNCF项目[Cedar](https://cedarpolicy.com/en)作为其策略语言。

Golshan表示，保护智能体需要一个全栈解决方案，Nvidia无法一块一块地构建该技术栈。

“我们不能先构建OpenShell，再去构建它的后续部分，”他说。“从基础设施的角度来看，其中许多部分在CNCF中已经存在了。”他以Kubernetes本身、轻量级的K3s发行版以及服务网格作为相邻项目的例子。

Golshan说，在构建OpenShell的过程中，谁来运营它也变得更加清晰。这个画像与已经建立公司其余基础设施的DevSecOps工程师相吻合。

他指出[SAP](https://news.sap.com/2026/09/sap-nvidia-openshell-auditable-ai-agents-enterprise-systems/)就是一个 DevOps 和基础设施团队建立大型智能体环境的公司。

他说，与智能体协同工作的人可能是工程师或研究人员，但操作员是“那些正在启动Kube、Linux和整个技术栈的相同团队”。

理想情况下，这些最终用户永远不会看到OpenShell。“你其实看不到Kubernetes，”Golshan说。“你只是得到了那个环境。”

当CNCF执行董事[Jonathan Bryce](https://www.linkedin.com/in/jbryce/)思考一项技术应该在哪里落脚时，他告诉 *The New Stack*，需要问的问题是“那些将要做出部署、使用、贡献特定技术决策的人在哪里？”

Bryce说，智能体最初是由人们在家里的Mac Mini上运行OpenClaw开始的，但长期运行的、SaaS风格的智能体看起来更像是在数据中心运行的其他软件。他补充说，在OpenShell加入CNCF之前，其早期的大部分采用来自新云（neoclouds），即希望对其客户在基础设施上运行的工作负载进行治理的GPU云提供商。

Bryce说，由于OpenShell可以接入Kubernetes和生态系统中的其他项目，已经运行该技术栈的团队可以轻松地将其实施到他们想要容器化的工作负载中。

## 智能体项目栖息何处

Bryce说，智能体将存在于整个技术栈中，支持它们的开源项目将分布在几个基金会中，每个基金会都有不同类型的贡献者。

[PyTorch基金会](https://pytorch.org/foundation/)是PyTorch、vLLM、DeepSpeed和Ray的大本营，这里汇聚了拥有深厚AI专业知识的工程师。Bryce将他们比作“编写Postgres的人”。

他说，CNCF是“一大批了解如何采用成熟系统并对其进行部署、扩展、可观测性、保护的人。”

Bryce说，拥有MCP和A2A等协议的AAIF面向智能体的前端体验。他将这些协议比作HTTP和JavaScript，正是这些标准造就了数百万个Web应用。

Bryce说，这些基金会是“维恩图”而不是孤岛，“我认为这很好”。他指出了在Kubernetes上运行Ray工作负载的KubeRay，以及将vLLM与Kubernetes配对的llm-d。AAIF的agentgateway也与Kubernetes协同工作。

他指出，CNCF在项目落脚点方面也往往很灵活，并允许维护人员“在某种程度上选择自己的冒险”。

同时，Bryce表示，Nvidia对人们如何运行AI工作负载的能见度是“无与伦比的”，该公司将基于这种经验构建的新项目带到了每一届KubeCon上。“其中一些最终进入了基金会，”他说。“有些则没有。”

## 治理与安全委员会

Golshan于2025年加入Nvidia，当时该公司收购了他共同创立的合成数据初创公司Gretel。在此之前，他还共同创立了Kubernetes安全公司StackRox，该公司于2021年被红帽[收购](https://thenewstack.io/what-red-hats-purchase-of-stackrox-means-for-openshift-security-and-observability/)。

他说，启动OpenShell的人一直是CNCF项目的贡献者，并且从内部了解其治理模型。

他说，该模型符合团队的期望：为OpenShell确立单一使命，并在更大的生态系统中占据一席之地。

他说，安全治理仍在制定中。OpenShell目前是一个Sandbox项目，Golshan表示团队正在“花时间思考”如何在其周围建立一个独立的安全委员会。

“我认为变得非常重要的一件事是，你如何管理披露、漏洞之类的事情，”他说。他补充说，如果OpenShell要成为关键基础设施的重要组成部分，它需要来自许多参与者的贡献，“不一定只是我们。”

Nvidia的工程师将继续致力于该项目的核心，但红帽、Docker和Canonical自项目开始以来一直与Nvidia并肩作为核心贡献者。

Golshan说，当Nvidia在3月份开放OpenShell的早期访问权限时，大约有10到15家公司在进行贡献。该项目在9月份随着0.1.0版本的发布放弃了alpha标签，[CNCF的项目页面](https://www.cncf.io/projects/openshell/)现在列出了大约380个贡献组织。

“有很多人会在一定层面上参与，而不需要它处于中立治理之中，”Bryce说。“但一旦它转向完全中立的治理，那么这种参与就会深入得多。”

Bryce说，过去需要两到三年才能完成的采用周期现在在六到十二个月内就会上演，他将中立治理形容为集成和采用的“火箭燃料”。

“llm-d于今年3月加入CNCF，他们现在已经发布了1.0版本，”Bryce在谈到这个分布式推理框架时说道，“他们拥有一整套真正在生产环境中运行它的公司，包括一些新云。”

Golshan表示，OpenShell需要围绕它构建一个工具生态系统，然后才能在生产环境中大规模运行。他说，到目前为止，已有大约50到60家公司（从初创公司到大型供应商）在其基础进行了构建。OpenShell现在为计算、凭证管理、推理提供商和策略执行定义了明确的扩展点，他希望CNCF社区能够将它们作为将OpenShell与云原生技术栈其余部分联系起来的蓝图。

“如果在未来六个月内，我们能够支持从Istio到Envoy再到边缘的K3s的一切，那将是令人惊叹的，”Golshan说。

他说，自0.1.0版本发布以来，那些正在将智能体从研究阶段转向生产阶段的早期采用者一直在寻求关于安全性、隐私性和可观测性工具的建议，这些工具需要能够与OpenShell原生配合。他们还希望获得有关优化在其中运行的智能体和工具包的帮助。

Golshan描述了最近在柏林与一个对Datadog和分布式追踪非常了解的人的对话。“我甚至不知道该为智能体观察什么，”他回忆那个人这样说。

Golshan希望社区从这些边缘案例中学到的东西能够回馈到OpenShell的核心中，就像Kubernetes当年那样。“现在说我要把我的公司押在Kube上是非常容易的，”他说。“没有人会因此被解雇。”他希望OpenShell也能达到那个地位。

## 动荡的智能体技术栈

Bryce说，模型训练的技术栈已经很清晰，推理的技术栈也相当稳定，但对于智能体来说，“完全不是这样”。

“如果没有一个清晰的技术栈，那么行业就无法围绕最重要的问题走到一起，并真正取得非常迅速的进展，”他说。

在未来六到十二个月内，他预计实验将最终确定关于OpenShell如何与Kata Containers、gVisor、Agent Substrate以及现有的OpenTelemetry项目集成的答案。一旦这种情况发生，他预计智能体会像过去八个月的推理一样腾飞。

其中两个项目是CNCF的新成员。谷歌在本周的KubeCon上[贡献了](https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html)Agent Substrate（其用于在Kubernetes上运行长期智能体的框架）和gVisor沙箱运行时。Nvidia表示，它正在与谷歌合作实现OpenShell和Agent Substrate之间的集成。