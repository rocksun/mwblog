<!--
title: AI代理加速漏洞发现：AppSec团队亟需变革与适应
cover: https://cdn.thenewstack.io/media/2026/02/4bb91d3f-dina-gazizova-9ogyfwh4kbm-unsplash-scaled.jpg
summary: 文章阐述AI代理加速漏洞发现，AppSec团队需通过集成AI于安全工作流、规模化威胁建模及改进SAST等方式，积极适应以应对快速发展的软件开发。
-->

文章阐述AI代理加速漏洞发现，AppSec团队需通过集成AI于安全工作流、规模化威胁建模及改进SAST等方式，积极适应以应对快速发展的软件开发。

> 译自：[AI agents are accelerating vulnerability discovery. Here's how AppSec teams must adapt.](https://thenewstack.io/ai-agents-appsec-strategy/)
> 
> 作者：Josh Lemos

快速、大规模地发现安全漏洞从未如此简单。[Linus定律](https://en.wikipedia.org/wiki/Linus%27s_law)，埃里克·雷蒙德关于开源软件的著名论断，指出“只要有足够多的眼睛，所有Bug都无处遁形”。换句话说，如果有足够多的人审视一段代码，最终总会有人发现问题。

AI极大地强化了这一原则，推动新工具加速并扩展了发现漏洞的能力。

问题是，谁会首先发现它们：是您的安全团队，还是威胁行为者？

## AI红队：不再是理论或可选项

XBOW登上[HackerOne美国排行榜](https://xbow.com/blog/top-1-how-xbow-did-it)榜首，标志着应用程序安全（AppSec）的一个里程碑。在短短90天内，其自主AI渗透测试仪提交了超过1,060个漏洞，超越了数千名人类研究人员的产出。

与许多[低质量的AI内容](https://www.nytimes.com/2024/06/11/style/ai-search-slop.html)不同，这些发现并非理论性的。漏洞赏金计划帮助公司解决了XBOW发现的130个关键漏洞，另有300多个已分类并等待解决。

XBOW成就的特别之处在于其规模经济效应。[该系统自主运行](https://thenewstack.io/operations-shift-assistants-to-autonomous-multiagent-systems/)，无需休息，并能同时处理数千个目标。

当人类研究人员选择高价值目标时，AI系统可以[系统地测试整个攻击面](https://thenewstack.io/modern-attack-methods-jeopardize-cybersecurity-strategies/)。HackerOne[报告](https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy)称，仅在2025年，自主代理就提交了超过560份有效报告。

曾经需要经验丰富的安全研究人员才能利用的已知漏洞，现在可以以机器的规模和速度被发现。

## AI速度下的威胁建模

摩根大通发布其[AI威胁建模Co-Pilot研究](https://www.jpmorganchase.com/about/technology/blog/aitmc)表明，企业应用安全团队已在部署AI以解决速度限制问题。其[Auspex系统](https://arxiv.org/pdf/2503.09586)通过专业提示捕获威胁建模技巧，指导AI进行系统分解、威胁识别和缓解策略，使开发人员能够通过自助服务模式解决这些问题。

Auspex将生成式AI与专家框架、行业最佳实践以及摩根大通的机构知识相结合。该系统通过一种称为“技巧提示”（tradecraft prompting）的技术，将这些上下文直接编码到AI提示中。

它处理架构图和文本描述，然后链式生成提示，创建威胁矩阵，明确场景、类型、安全分类和潜在的缓解措施。
传统的威胁建模可能需要数周或数月。而摩根大通采用的AI驱动方法，将这一时间线缩短至数分钟，同时提高了[人工分析的质量](https://thenewstack.io/level-up-your-software-quality-with-static-code-analysis/)。

## 循环中的安全人员

XBOW和Auspex所展示的新兴AI用例，为AppSec团队提供了一种替代传统AppSec模型的方案。传统模型在开发过程中消耗大量资源，但覆盖范围有限。

代码审查积压增多，安全债积累，关键漏洞悄然进入生产环境，因为人类在[软件开发](https://thenewstack.io/ai-use-cases-that-actually-fix-engineering-bottlenecks/)生命周期中仍然是瓶颈。最近一项[GitLab调查](https://about.gitlab.com/developer-survey/)发现，团队每周因低效流程损失7小时。

AI改变了这一局面。安全团队现在可以系统地将资源从手动、重复性活动中重新部署，转向构建将AI直接集成到开发人员工作流中的安全工程解决方案。

一些经过验证的AI驱动策略可以帮助现代AppSec团队高效扩展：

*   **构建可查询的安全情报：** 将每个安全Bug、漏洞报告和事件摄入到支持语义搜索的结构化数据存储中。这将把历史安全发现转化为嵌入向量，使AI系统能够在代码库中识别相似模式。当新的漏洞类别出现时，您的AI可以立即查询其他地方是否存在类似问题。
*   **针对您的环境微调模型：** AppSec团队不应依赖通用商业工具，而应利用RAG（检索增强生成）方法，用组织特定的安全反模式和架构标准来增强LLM。最近的[研究](https://arxiv.org/html/2502.06633v1)表明，将PMD和Checkstyle等静态分析器与微调的LLM相结合，可以显著提高代码审查的准确性，同时减少误报。
*   **将AI集成到开发人员工具链中：** 代码编写完成数天或数周后才出现安全发现会造成摩擦，并要求开发人员进行更多的上下文切换。相反，应将AI驱动的分析直接嵌入到您的IDE、CI/CD管道和拉取请求工作流中。开发人员将在编写代码时（而非之后）收到实时安全指导。
*   **大规模应用AI进行威胁建模：** 效仿摩根大通的做法，实施AI驱动的威胁建模，分析每一个新的系统设计、API规范和基础设施变更。目标不是完美，而是广度：为100%的系统生成AI威胁模型，优于为10%的系统提供专家审查模型。
*   **利用AI改进您的静态应用安全测试（SAST）：** 传统SAST工具会产生大量误报，这可能会使开发人员麻木，并增加分类开销。AI可以通过[理解代码上下文](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/)、分析数据流并识别模式匹配工具遗漏的真实漏洞，显著提高这些工具的准确性。

## AI安全优先级

安全团队正面临一个关键时刻。当开发速度如此之快时，在代码审查中增加更多工程师的旧策略已不再奏效。AI可以匹配这一速度，以与团队创建软件同样快的速度保护软件。

但这种转变不会偶然发生。安全负责人需要主动调整团队重心，重新设计工作流，并重新思考人机协作时哪些技能至关重要。那些预先付出努力的组织更有可能做好这一点，并以更强的安全性、更低的成本和更快的发布周期脱颖而出。