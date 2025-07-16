<!--
title: 当AI加速API开发，安全如何跟上？
cover: https://cdn.thenewstack.io/media/2025/07/cff330fa-penfer-_kbltjx-pt0-unsplash-scaled.jpg
summary: API 蔓延已成为重大业务风险，受 AI 驱动的代码生成加速了其发展。影子 API 和僵尸 API 构成安全威胁，降低开发者生产力。解决方案包括建立专门的 API 管理团队，实施持续治理，将安全性嵌入开发生命周期，并使用自动化工具进行 API 文档生成和冗余 API 合并。
-->

API 蔓延已成为重大业务风险，受 AI 驱动的代码生成加速了其发展。影子 API 和僵尸 API 构成安全威胁，降低开发者生产力。解决方案包括建立专门的 API 管理团队，实施持续治理，将安全性嵌入开发生命周期，并使用自动化工具进行 API 文档生成和冗余 API 合并。

> 译自：[Generative AI Creates APIs Faster Than Teams Can Secure Them](https://thenewstack.io/generative-ai-creates-apis-faster-than-teams-can-secure-them/)
> 
> 作者：Saqib Jan

API 对于增长非常重要，它允许团队以惊人的速度构建和发布功能。您的业务很可能依赖于 API 蓬勃发展。它们是连接您各项服务的桥梁，也是您的应用程序用来为客户提供独特价值的语言。但这种速度通常伴随着一个隐藏且错综复杂的阴影——日益增长的复杂性，这种复杂性正在悄悄地破坏原本旨在支持的创新。

多年来，围绕这种复杂性（或 API 蔓延）的讨论似乎仅限于工程团队内部。它通常被讨论为一种技术债务——一种混乱的后端，虽然令人讨厌，但主要只是减慢了开发速度。但根据 AI 原生软件测试平台 [LambdaTest](https://www.lambdatest.com/) 的 DevOps 和 DevSecOps 副总裁 [Akash Agrawal](https://in.linkedin.com/in/akashmagrawal) 的说法，这种观点现在已经过时且非常危险。“在当今的格局下，”他解释说，“数字供应链完全建立在 API 之上，不受管理的蔓延是一种直接且重大的业务风险。每个未知或不安全的 API 都是重大漏洞的潜在载体，影响从监管[合规性到客户](https://thenewstack.io/suse-launches-a-sovereign-premium-support-service-for-eu-customers/)信任的一切。”

现代开发疯狂的步伐正在加剧这种从受控问题到核心业务威胁的转变。随着组织展开创新军备竞赛，他们创建 API 的速度是手动治理根本无法处理的。最近 AI 领域的突破——尤其是在自动化代码和 API 生成方面——正在日益加速这种扩散。但是，再加上较差的可见性和对跨环境缺乏控制，这使得公司面临严重的[安全故障，同时削弱了他们有效前进的能力](https://thenewstack.io/how-attackers-move-from-azure-active-directory-to-on-prem-ad/)。

## 生成式 AI 如何加速 API 创建超出安全控制

这种广泛的风险通常始于两个众所周知但经常被忽视的漏洞。第一个是影子 API——完全在雷达之外运行的未记录端点，通常是为临时目的而创建，然后被遗忘。第二个是僵尸 API，即旨在退役但从未完全停用的旧版本。两者都代表了对攻击者的公开邀请，但如果通过传统的（即使是不完善的）人工监督，它们的数量仍然在某种程度上可控。

这种动态现在已经被彻底颠覆。“生成式 AI 是放大这个长期存在的问题的主要力量。它使团队能够比以往更快地构建和部署，这对创新来说非常棒，但它也在以手动治理根本无法处理的速度创建 API，”Agrawal 强调说：“结果是，为特定的 AI 驱动目的而创建的影子 API 激增，这些 API 从未被正确记录、保护或停用。”这强化了旧的安全真理——你看不到的东西，你就无法保护——而 AI 正在迅速扩大一个已经难以监控的领域。

这种加速催生了一种危险的新开发者行为——一种被称为“氛围编码”的趋势。Sonar 的 AI 部门产品经理 [Edgar Kussberg](https://www.linkedin.com/in/kussberg/) 指出，开发者越来越信任那些感觉正确的 AI 生成代码，而没有执行必要的尽职调查。由于氛围编码，[API 经常在没有关键安全](https://thenewstack.io/using-apis-with-low-code-tools-9-best-practices/)控制或适当文档的情况下部署，从而以前所未有的规模创建了新一波的广泛漏洞。

## 未管理 API 蔓延的生产力成本

API 蔓延最直接的后果是对开发者生产力的严重打击。[EPAM Systems](https://www.epam.com/) 的解决方案架构师 [Yauheni Kanavalik](https://www.linkedin.com/in/kanavalik) 解释说，这通常会导致团队陷入通常被称为“依赖地狱”的状态——在这种状态下，开发团队将其注意力从用户及其需求上转移开，而是变得超负荷，只是试图驾驭错综复杂的集成网络。这是一种瘫痪状态，会直接影响利润。

Kanavalik 指出，“调查时间”是关键的隐藏指标——可能需要几周的时间，一个新[功能才能准备好进行开发](https://thenewstack.io/top-5-code-completion-services/)。开发者可能需要确认是否已经存在类似的功能，草拟一系列 API 调用，然后尝试跨多个时区和支持渠道联系这些服务的所有者。这个最初的发现阶段，而不是编码本身，成为交付价值的最大瓶颈。

[Sigma](https://www.sigmacomputing.com/) 的高级工程经理 [Asad Akram](https://www.linkedin.com/in/aakram1/) 说，这种对生产力的拖累可以直接破坏战略业务计划。“当我们的商业智能团队构建一个 AI 助手来帮助用户从自然语言生成 API 调用时，他们亲身体验了这一点。但是，AI 经常给出不正确的建议，推荐一个看起来正确但未能交付预期结果的 API——导致用户感到沮丧。根本原因是 API 蔓延；AI 试图驾驭 12 个不同但相似的 API，这些 API 与同一功能目标相关联。”

这种摩擦会产生累积效应，业务领导者不能忽视。 [IBM](https://www.ibm.com/in-en) 自动化副总裁 [Madhu Kochar](https://www.linkedin.com/in/madhu-kochar-637a305/) 指出，这种“API 爆炸”最终会导致维护和运营成本增加、开发者生产力降低以及安全和合规风险增加，从而直接阻碍组织的数字化转型计划。

## 为 AI 生成的 API 实施持续治理

虽然 API 蔓延的图景似乎令人生畏，但组织可以通过解决人员、流程和技术的多层方法重新获得控制权。它不是从一个新工具开始，而是从一种新的所有权和专业知识方法开始。

最有效的组织修复方法之一是创建 EPAM Systems 的 Kanavalik 所谓的“外观团队”。这是一个专门的中央团队，充当所有 API 集成的单一入口点和所有者。外观团队不是让每个开发者都在与相同的第三方依赖项作斗争，而是管理这些关系、标准化文档并提供专家指导——从而使其他团队可以专注于构建价值。

在建立了明确的所有权结构后，团队可以继续进行清理和自动化的战术工作。例如，Sigma 团队通过将 12 个冗余 API 合并为仅 3 个灵活的端点，直接解决了其 AI 助手的故障。这种清理立即[提高了人类开发者](https://thenewstack.io/ai-improves-developer-workflow-says-gradle-dev-evangelist/)和 AI 系统的清晰度。EPAM 团队建议使用大型语言模型直接从难以理解的服务的源代码中自动生成高质量的 API 文档。

但是，这些战术修复必须是更大、面向未来的战略的一部分。Sonar 的 Kussberg 认为，传统的治理框架正在“追赶”，并且根本不是为 AI 可以自动生成代码的时代而构建的。他主张的解决方案是实施“CI/CD + CG（持续治理）”。这[意味着将自动化安全](https://thenewstack.io/6-reasons-why-more-automation-means-more-secure-software/)、版本控制和治理检查直接嵌入到开发生命周期中，确保每个 API（无论是人工生成的还是 AI 生成的）从创建之初就是安全且受管理的。

## 构建外观团队和自动化控制以实现 API 安全性

很明显，由于 AI 的进步，关于 API 蔓延的讨论已经发生了根本性的变化。未知、未管理和被遗忘的 API 错综复杂的网络不再是一个可以推迟到下个季度的技术债务的背景问题。它是一种积极且不断增长的[业务风险，会直接影响安全性](https://thenewstack.io/cloudflare-for-ai-helps-businesses-safely-use-ai/)、使合规性复杂化，并瘫痪了负责创新的开发团队。

“重新获得控制权的关键在于战略性地致力于可见性、所有权，并在整个 API 生命周期中嵌入主动安全性，”Agrawal 说。根据他在 LambdaTest 的工程经验以及领导 [Kane AI](https://www.lambdatest.com/kane-ai)（一种用于高速质量工程的 GenAI 原生测试代理）的安全工作，他强调了从一开始就协调安全性和速度的重要性。通过从救火状态转变为具有前瞻性的“持续治理”战略，组织可以开始转变其 API 格局。他们可以将它们从隐藏的负债转变为安全、战略性的资产，这对于构建值得信赖和创新的 AI 未来绝对必不可少。