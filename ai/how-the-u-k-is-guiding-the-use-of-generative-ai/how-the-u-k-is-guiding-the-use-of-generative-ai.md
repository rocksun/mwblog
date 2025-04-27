
<!--
title: 英国如何指导生成式人工智能的使用
cover: https://cdn.thenewstack.io/media/2025/04/4e7b04d2-uk-ai-playbook-2.jpg
summary: 英国政府发布AI行动手册，指导公共部门安全使用生成式AI。强调Agentic AI，提出十大原则，关注伦理、安全风险如数据投毒、提示注入等。强调人类控制，管理AI生命周期，选择合适工具，鼓励开放协作，提升技能，进行风险评估。拥抱RAG，进行战略规划。
-->

英国政府发布AI行动手册，指导公共部门安全使用生成式AI。强调Agentic AI，提出十大原则，关注伦理、安全风险如数据投毒、提示注入等。强调人类控制，管理AI生命周期，选择合适工具，鼓励开放协作，提升技能，进行风险评估。拥抱RAG，进行战略规划。

> 译自：[How the UK Is Guiding the Use of Generative AI](https://thenewstack.io/how-the-u-k-is-guiding-the-use-of-generative-ai/)
> 
> 作者：David Eastman

我希望在教皇去世后，有更多人关注梵蒂冈的[Antiqua et Nova](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html)，因为它对[生成式人工智能进行了相当成熟的伦理审查](https://thenewstack.io/cloud-service-what-the-pope-thinks-about-ai/)。 这篇文章超过 13,000 字，我不指望它会被大量阅读，但其中存在相当明智的立场，将滥用与潜力区分开来。

不过，在这篇文章中，我关注的是英国政府数字服务部的[生成式人工智能行动手册](https://gds.blog.gov.uk/2025/02/10/launching-the-artificial-intelligence-playbook-for-the-uk-government/)，因为这是针对实际部门和公共机构的积极建议。 虽然这应该引起任何面向公众的组织的兴趣，但公共资助机构有其自身的问题和偏好。 我将通过其 10 项原则来引导阅读本文档，但总的来说，该行动手册的存在是为了提供指导。

虽然 GDS 从未完全实现“政府即平台”，但该机构是该方法最早的认真倡导者。 它始终公开记录自己的技术流程。

本行动手册的明确目的是“帮助政府部门和公共部门组织安全、有效和负责任地利用更广泛的人工智能技术的力量”。 但在这背后，存在着模糊的政治背景，因为英国政府表示，应该拥抱人工智能以节省资金。 （我怀疑在制定这项战略时，整体政治框架并不那么紧张。）

阅读并遵守指南是我们通常会签署同意的事情，但并非充满热情。 本文档使用相当简单的语言来形成一致的叙述。 从定义[什么是人工智能？](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#what-is-ai)开始，该行动手册避免从 LLM 开始其时间线，而是回顾更早的时间：

![A word diagram showing the types of AI, according to the "Artificial Intelligence Playbook for the UK Government."](https://cdn.thenewstack.io/media/2025/04/7e99ce7a-image.png)

根据“英国政府人工智能行动手册”显示的人工智能类型。

还提到了 **Agentic AI**，因此该战略保持了新鲜感。 我认为这为其他人提供了一个有用的参考区域。

## 10 项原则

值得注意的是指导人工智能使用的[10 项原则](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principles)。 这些原则通常指向文档中更详细的部分。 除了“在使用前了解它是什么”等显而易见的事情之外，这些原则还强烈尝试让人们检查自己的推理。

并非所有内容都具有时效性； [第一项原则](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principle-1-you-know-what-ai-is-and-what-its-limitations-are)中的“人工智能系统目前缺乏推理和上下文感知”这句话看起来不太可能经受住时间的考验。 相比之下，梵蒂冈的指导方针明智地尽早隔离了人工智能中长期存在的弱点：它仅限于功能性反应，无法获得具身的独特人类视角。

良好的推理和上下文感知使大型语言模型生成的响应陷入困境，因为它们足够好，以至于在出错时非常烦人。 使用[谷歌](https://cloud.google.com/?utm_content=inline+mention)的[Gemini](https://thenewstack.io/gemini-code-assist-review-code-completions-need-improvement/)响应可以证明这一点。

关于[伦理和责任](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principle-2-you-use-ai-lawfully-ethically-and-responsibly)的原则 2 显然比梵蒂冈的声明弱得多，但至少强调了有偏见的训练数据的问题。 然而，该行业已经提供了大量增强训练数据的方法。 当然，梵蒂冈实际上并没有实施任何东西。
我喜欢该行动手册在原则 3 中特别指出的生成式 AI 独有的[安全风险](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principle-3-you-know-how-to-use-ai-securely)的方式。这部分抛弃了薄弱的泛泛而谈，而是专门指出了[数据投毒](https://thenewstack.io/poisoning-the-well-and-other-generative-ai-risks/)、[扰动攻击](https://machine-learning-made-simple.medium.com/an-introduction-to-adversarial-perturbation-5e6c61d84b71)、[提示注入](https://thenewstack.io/when-prompt-injections-attack-bing-and-ai-vulnerabilities/)以及幻觉。它指出，许多 AI 工具链“由 AI 研究人员和数据科学家快速开发，他们没有遵循安全编码实践。AI 工具通常具有对其运行系统的提升的访问权限”。

[原则 4](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principle-4-you-have-meaningful-human-control-at-the-right-stages)涵盖了人类的总体控制。这听起来总是危言耸听，因为没有人会质疑人类使用任何工具通常会保留总体控制权。但是，一旦你接受 GenAI 在输出方面根本不可靠或不一致，那么无论你在工具链中使用它，你都将控制权让给了一个完全[不透明的系统](https://thenewstack.io/why-llms-within-software-development-may-be-a-dead-end/)。该行动手册中涵盖人类监督的[章节](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#data-protection-and-privacy)直接承认，自主决策可能会侵犯英国通用数据保护条例 (GDPR)，该条例基于欧盟版本。

[原则 5](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principle-5-you-understand-how-to-manage-the-full-ai-life-cycle)指的是“完整的 AI 生命周期”，它暗示（我认为）在标准软件产品生命周期中使用生成式 AI，这绝对是[有问题的](https://thenewstack.io/why-llms-within-software-development-may-be-a-dead-end/)。如果部署在即，还需要考虑服务标准。

但是，最初通过供应商 API 设置 LLM 或在本地托管它们通常[有很好的文档记录](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)，除了安全问题外，可以快速进行原型设计——当然不比获得在政府内部托管任何其他软件的许可更糟糕。管理生命周期可能只是指管理软件开发人员，而不是[“氛围编码”](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)。

[原则 6](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principle-6-you-use-the-right-tool-for-the-job)的标题具有误导性“使用合适的工具来完成工作”，但其下的信息是正确的。太多的组织试图用一个答案来解决各种问题。LLM 只是另一种在你的工作中强制执行组织原则的方式；将重复性任务与它们之间的分支决策分开。
分解你的工作并重建它通常是有益的——无论你是否可以挤进一些 LLM 解决方案。这就是[实践社区](https://thenewstack.io/developers-need-a-community-of-practice-and-wikis-still-work/)可以帮助比较和对比当前 LLM 解决方案如何帮助你组织中的工作流程的地方。

碰巧的是，[原则 7](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principle-7-you-are-open-and-collaborative)直接指的是一个[跨政府实践社区](https://www.gov.uk/service-manual/communities/artificial-intelligence-community)，但主要鼓励沟通的开放性。这是试图为公共部门创建一个开放的 AI 社区，我再怎么推荐这种方法也不为过。这些文件包括关于“[GOV.UK 聊天](https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/)”的发现。不幸的是，在最近的政府换届中，这似乎没有继续下去。

![时间线显示了 GOV.UK 聊天实验是如何进行的，来自 2024 年 1 月英国政府数字服务博客文章。](https://cdn.thenewstack.io/media/2025/04/ba9ff9a7-image-1-1024x334.png)

*时间线显示了 GOV.UK 聊天实验是如何进行的，来自 2024 年 1 月英国政府数字服务博客文章。*

对于一个面向公众的机构而言，保持透明和开放几乎总是比热情的支持者想象的要困难得多。（[原则 8](https://www.notion.so/Working-inside-the-Panopticon-1ceba3b2748680f7a9c8d0f27647c4a4?pvs=21)，关于与商业同事合作，是英国政府对自己的一个信息，并不是特别重要。太多面向公众的机构的人在那里工作，明确是为了避免进入商业领域。）

[原则 9](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principle-9-you-have-the-skills-and-expertise-needed-to-implement-and-use-ai-solutions) 检查你是否拥有可用于 LLM 的团队。“训练你自己的模型”的含义最近发生了变化，但即使对于软件开发人员来说，它仍然是一项相当专业的活动。各种[检索增强生成 (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/)和向量嵌入工具正在慢慢地使该领域民主化。剧本中有一个“获取技能和人才”部分，其中链接到公务员的公开培训。
最后，[原则 10](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html#principle-10-you-use-these-principles-alongside-your-organisations-policies-and-have-the-right-assurance-in-place)（将这些原则与你组织的政策一起使用）介绍了与组织间孤岛政治合作以及与其他小组、委员会和压力团体对抗的阴暗世界。毫不奇怪，对于这样一个热门话题，仔细的风险评估和流程文档至关重要。但与此同时，这个非常开放的项目证明了政府鼓励拥抱生成式人工智能，这是值得称赞的。

## 结论

我认为大多数正式的公共组织至少应该采用 GDS 制定的一套原则，并且应该很容易在此基础上进行改进。这些当然不是一成不变的。大多数企业仍然太接近前线，无法花时间反思他们对人工智能的使用，并且不承担政府部门的责任。

虽然我们都希望确切地知道 OpenAI 和其他技术领导者正在走向何方，但最好在首先致力于 LLM 和生成式人工智能的使用之前进行战略规划。