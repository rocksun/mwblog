
<!--
title: LLM和Vibe Coding能否点燃开发者文艺复兴？
cover: https://cdn.thenewstack.io/media/2025/06/00a6d108-acr_2588-1-scaled.jpg
summary: AI正推动开发者角色转变，从技术任务转向管理AI代理团队，需扩展技能至产品和UX。可靠性成挑战，SRE需求增加。未来评估或更关注代理管理能力。
-->

AI正推动开发者角色转变，从技术任务转向管理AI代理团队，需扩展技能至产品和UX。可靠性成挑战，SRE需求增加。未来评估或更关注代理管理能力。

> 译自：[Will LLMs and Vibe Coding Fuel a Developer Renaissance?](https://thenewstack.io/will-llms-and-vibe-coding-fuel-a-developer-renaissance/)
> 
> 作者：Sylvain Kalache

随着越来越多的公司在其开发过程中使用[大型语言模型（LLMs）](https://thenewstack.io/what-is-a-large-language-model/)，例如微软[使用 AI 编写高达 30% 的代码](https://techcrunch.com/2025/04/29/microsoft-ceo-says-up-to-30-of-the-companys-code-was-written-by-ai)，以及站点可靠性工程师（SRE）采用[事件感知（incident vibing）](https://thenewstack.io/vibe-coding-is-here-but-are-you-ready-for-incident-vibing)，软件实践正在不断发展。

尽管[模型制造者](https://www.inc.com/joe-procopio/anthropics-ceo-said-all-code-will-be-ai-generated-in-a-year/91163367?utm_source=chatgpt.com)推动着完全自主的 AI 开发代理即将到来的说法，但共识仍然是，至少在一段时间内，让人类参与其中是不可或缺的。那么，AI 会否推动开发者文艺复兴？

## 向多代理工作流程的转变

我最近主持了一个关于此话题的 [Rootly AI Labs](https://labs.rootly.ai/) [小组讨论](https://lu.ma/ki58hev3)。[Solomon Hykes](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/)，[Dagger](https://dagger.io/)的 CEO 和 [Docker](https://www.docker.com/?utm_content=inline+mention) 的创始人，认为虽然业界一直忙于研究单代理方法，但多代理设置代表着下一个前沿。

例如，初创公司 [Factory](https://www.factory.ai/) 引入了 “Droids”，这是一种旨在处理并行开发任务的软件代理。一个代理可以管理代码重构，另一个可以进行代码审查，还有一个可以处理 [Linear](https://thenewstack.io/anti-agile-project-tracker-linear-the-latest-to-take-on-jira/) 上的任务积压，优先处理和分配工单。

这些设置将开发人员的角色从直接的技术任务转变为管理和验证这些代理的工作，从而将[开发人员转变为工程经理](https://thenewstack.io/ai-will-steal-developer-jobs-but-not-how-you-think/)。

Anthropic 最近发布了一份关于构建多代理系统的[蓝图](https://www.anthropic.com/engineering/built-multi-agent-research-system)，该蓝图基于其 Research 功能的经验教训，该功能协调多个 Claude 代理来探索复杂的主题。

该报告强调，在代理系统中，在传统软件中可能只是小问题的问题可能会加剧并完全破坏工作流程，从而使原型和生产之间的差距比预期的更大。

让多代理系统可靠地工作会将“最后一英里”变成大部分旅程，而开发人员则负责实现这一目标。

## 开发者角色正在扩展

随着开发人员过渡到管理 AI 代理团队，他们的角色自然会扩展到纯技术任务之外。[Malika Aubakirova](https://www.linkedin.com/in/malika-aubakirova-54759984/)，[Andreessen Horowitz](https://a16z.com/) AI 基础设施团队的合伙人，强调了纳米独角兽的崛起；这些独角兽是指团队规模小、收入增长快、收入高的初创公司，例如 [Cursor](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/)，该公司仅有 20 名员工就达到了 [3 亿美元的年度经常性收入](https://www.fastcompany.com/91322491/ai-coding-tools-could-bring-us-the-one-employee-unicorn)。

她注意到这些公司存在一致的模式。首先，他们通过工程、产品开发和面向客户的职能部门的 AI 代理来增强其团队。在这种模式下，AI 不是一个辅助工具；它被视为基础设施，并且是工作完成方式的核心。

其次，这些初创公司经常雇用通才而不是专家。例如，在这样的环境中，工程师不仅限于后端或前端任务；他们将为整个应用程序生命周期做出贡献，甚至协助上市计划。这种转变正在重新定义团队结构、工具以及扩展现代软件公司的意义。

![在 AWS Builder Loft 举行的关于 AI 时代开发者未来的小组讨论。](https://cdn.thenewstack.io/media/2025/06/332ff6e2-unnamed-1-1024x683.jpg)

*在 AWS Builder Loft 举行的关于 AI 时代开发者未来的小组讨论。*

这种趋势不仅限于初创公司；它也正在大型、成熟的科技公司内部上演。[LinkedIn](https://thenewstack.io/5-lessons-from-linkedins-first-foray-into-genai-development/) 的一位要求匿名的资深工程领导表示，角色期望已大大扩展。现在，工程师们不仅要充当开发人员，还要充当项目经理、数据科学家和 SRE，并利用 AI 代理来执行这些领域的工作，因此他们需要跨多个职能部门运作。

虽然 LLM 的实际用处仍在争论中，但有一件事是肯定的：工程师们被要求以更少的资源做更多的事情。

## 可靠性和 SRE 团队面临的挑战

尽管 AI 代理提高了生产力，但它们的采用也带来了可靠性挑战。[Kevin Van Gundy](https://www.linkedin.com/in/kevinvangundy/)，[Hypermode](http://hypermode.com) 的 CEO 和 Vercel 的前 COO，强调 [LLM 的非确定性](https://rootly.com/humans-of-reliability/kaspar-von-grunberg#the-limits-of-llms-for-reliability-and-automation)可能会产生幻觉，从而导致非常不寻常的事件。处理确定性系统中的事件已经很复杂了；现在想象一下，当系统本身的行为不可靠时，该如何处理。

Hykes 指出，随着 LLM 嵌入到软件开发生命周期的每个阶段，从编写应用程序代码和创建其他代理，到运行测试、配置基础设施和处理监控，出错的地方越来越多。

SRE 作为理智与混乱之间的最后一道防线，可能需要关注涌向他们的[事件的数量和复杂性](https://leaddev.com/software-quality/ai-assisted-coding-incident-magnet)。然而，好消息是，他们也将成为更受欢迎的人才，更具体地说，平台团队将掌握大规模提供这些代理工作流程的基础设施的关键。

## 驾驭 AI 驱动的市场：开发者的技能

那么，工程师应该怎么做才能跟上时代的步伐呢？Van Gundy 鼓励工程师继续使用最新和最热门的工具进行构建，例如 [Replit](https://replit.com/) 和 [Lovable](https://lovable.dev/)。重点应该放在扩展纯技术技能之外，并培养强大的产品直觉和 UX 专业知识。如果没有精心打磨的产品，仅凭快速开发能力并不能保证成功。

相反，[Mike Chambers](https://www.linkedin.com/in/mikegchambers)，[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 的机器学习专家开发者倡导者，建议开发人员深入了解 LLM 背后的底层技术。学习诸如 transformers 之类的基础 AI 概念可以显著提高工程师在使用这些工具时的效率。像任何其他系统一样，LLM 也有优点和缺点，你不应该用锤子来拧螺丝。

## 开发者文艺复兴正在进行中

小组一致认为，LLM 确实通过显著扩展开发人员的角色为他们提供了潜在的文艺复兴。在这个新时代取得成功很可能高度依赖于将人类监督与 AI 功能相结合，在技术深度与产品敏感性之间取得平衡。

未来，工程师的绩效评估可能更多地关注工程师如何有效地管理和指导他们的代理劳动力，而不是个人执行力。