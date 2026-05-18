<!--
title: 前置部署工程师成为 AI 领域最火岗位：OpenAI 与谷歌竞相抢人，教你如何转型。
cover: https://cdn.thenewstack.io/media/2026/05/1869ee7a-fde-1024x683.png
summary: 随着 OpenAI 和谷歌等巨头竞相招聘，前置部署工程师（FDE）成为 AI 领域最炙手可热的岗位。该角色旨在填补模型与企业落地间的鸿沟，是 AI 规模化应用的关键。
-->

随着 OpenAI 和谷歌等巨头竞相招聘，前置部署工程师（FDE）成为 AI 领域最炙手可热的岗位。该角色旨在填补模型与企业落地间的鸿沟，是 AI 规模化应用的关键。

> 译自：[Forward deployed engineer is AI’s hottest job as OpenAI and Google race to hire. Here’s how to become one.](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/)
> 
> 作者：Matthew Burns

*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我会汇总最重要的 AI 进展，解释它们对于将技术付诸实践的个人和组织的意义。核心论点很简单：学习使用 AI 的员工将定义其行业的下一个时代，而本通讯旨在帮助你成为其中之一。*

---

OpenAI 本周推出了[部署公司 (Deployment Company)](https://openai.com/index/openai-launches-the-deployment-company)，这是一项耗资 40 亿美元的举措，旨在为大型企业配备前置部署工程师（Forward Deployed Engineer，简称 FDE）。第二天，Google Cloud 首席执行官 Thomas Kurian [在 LinkedIn 上](https://www.linkedin.com/feed/update/urn:li:activity:7460023647102078976)为该岗位招贤纳士，而 Google Cloud [已经开放了 59 个相关职位](https://www.channeldive.com/news/google-cloud-forward-deployed-engineering-jobs/820176/)，并报告称公司计划招聘数百人。Anthropic 将其前置部署工程师派驻到 FIS 内部，共同构建反洗钱智能体。ServiceNow 和 Accenture 也启动了一项联合前置部署工程师项目。

这一切都发生在过去的 10 天内。

如果你一直在思考哪种 AI 职位是持久的、待遇优厚，且不像 2023 年的提示词工程师那样纯属炒作，答案已经变得显而易见。前置部署工程师是 AI 模型与公司内部实际生产成果之间的桥梁。成为前置部署工程师的路径似乎是可行的：学习 AI 工程技术栈，围绕实际工作流进行构建，并训练大多数工程师避而远之的面向客户的判断力。想开始走这条路吗？我强烈建议从 [Roadmap 的 AI 工程学习路径](https://roadmap.sh/ai-engineer)开始。它包含了你入门所需的一切。

## 前置部署工程师到底是做什么的

关于前置部署工程师的权威解读就在我们的网站上。今年 1 月，Jennifer Riggins 在 *The New Stack* 上发表了“[为什么前置部署工程师是科技界最热门的工作](https://thenewstack.io/why-the-forward-deployed-engineer-is-techs-hottest-job/)”——这是一篇清晰、来源详尽的解释，说明了该岗位的起源、需求以及为何 AI 加速了它的发展。

**简短版本：** 前置部署工程师介于后台软件工程师和面向客户的软件架构师之间。这个角色最初由 Palantir 创造，模仿了“驻扎在海外，随时准备快速响应”的前线部署士兵，并基于一个简单的洞察：企业数据是杂乱的，交付一个可运行的系统需要工程师嵌入到客户的环境中。AWS 首席解决方案架构师 Prasad Rao 向 Riggins [描述这项工作](https://thenewstack.io/why-the-forward-deployed-engineer-is-techs-hottest-job/)时称其为“贯穿客户生命周期的亲身实践”——设计、交付，然后留下来解决问题，并根据现场实际发生的情况调整系统。这个岗位之所以迎来高光时刻，部分原因是麻省理工学院 NANDA 的《2025 年商业 AI 现状报告》[[PDF](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)] 发现，95% 的企业生成式 AI 试点项目没有产生可衡量的业务影响——这不是因为模型不好，而是因为模型不会自动部署。

NetBox Labs 联合创始人 [Mark Coleman](https://www.linkedin.com/in/markrobertcoleman/) 更直白地向 Riggins 表达了软技能的角度：“人们在看到自己不想要的东西之前，不知道自己想要什么。”这句话就是前置部署工程师的职位描述。模型可以生成十个合理的答案。前置部署工程师决定客户实际需要哪一个，将其交付，并随着客户反应的变化调整方案。

> 我看到了模型在解决方案中所能达到的效果与我们团队实际能交付的效果之间的差距。这个差距需要人类工作来填补。这就是前置部署工程师的工作。

我不是开发人员。我是一名编辑，每天运行 Claude Cowork 和 OpenAI Codex 会话。我看到了模型在解决方案中所能达到的效果与我们团队实际能交付的效果之间的差距。这个差距需要人类工作来填补。这就是前置部署工程师的工作——以工业规模、资深薪酬标准进行，而在 OpenAI 的案例中，还有 40 亿美元的资金在推动它。

## 该岗位在十天内走向主流

OpenAI 是头条新闻。[OpenAI 部署公司于周一成立](https://openai.com/business/the-openai-deployment-company/)，这是一家由 TPG 领导的多股控股合资企业，Advent、Bain Capital 和 Brookfield 为共同领投方，[Bain & Company、Capgemini 和 McKinsey & Company](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-4-billion-dollar-company-accelerate-enterprise-ai-adoption/) 为创始合作伙伴。OpenAI 还收购了伦敦的应用 AI 咨询公司 [Tomoro](https://tomoro.ai/insights/tomoro-acquired-by-openai-deployment-company)，在第一天就引入了约 150 名 AI 工程师和部署专家。初始支持资金：超过 40 亿美元。

这是一群严肃的商业顾问，每个人都拥有丰富的人脉和经验丰富的销售团队。

谷歌的举动则是更大的结构性信号。就在几周前的 Google Cloud Next 2026 上，Kurian 宣称：“试点的时代已经结束。智能体的时代已经到来”，并制定了扩大谷歌现场组织、核心技术工程和跨行业前置部署工程的计划。他[在 5 月 12 日的 LinkedIn 帖子](https://www.linkedin.com/feed/update/urn:li:activity:7460023647102078976/)中给出了具体数据：第一周在美国、印度、巴西、澳大利亚、墨西哥、新加坡、韩国和加拿大发布了 59 个新的前置部署工程师职位，职业阶梯涵盖了从 FDE II 到 FDE IV。

[已发布的职位列表](https://www.google.com/about/careers/applications/jobs/results/101918593561567942-forward-deployed-engineer-applied-ai-google-cloud)显示，在美国，应用型前置部署工程师职位的基本工资范围为 12.7 万美元至 18.3 万美元，FDE IV 职位的基本工资范围为 18.3 万美元至 26.5 万美元，这还不包括奖金、股权和福利。他们不是销售工程师——谷歌将他们描述为建设者，期望他们“直接在客户环境中编写代码、调试并联合交付定制的智能体解决方案”。*The Information* 报道称，更广泛的目标是数百名工程师，而披露该报告的 [*First Squawk* 帖子](https://x.com/FirstSquawk/status/2054265532728438990)在 X 上的浏览量达到了 130 万。对该职位的需求现在本身就是一个新闻周期。

Anthropic 也加入了前置部署工程师的热潮，交付了一次部署。FIS [宣布了一个智能体反洗钱平台](https://www.cio.com/article/4167981/anthropics-financial-agents-expose-forward-deployed-engineers-as-new-ai-limiting-factor.html)，该平台由嵌入的 Anthropic 前置部署工程师共同构建，蒙特利尔银行和联合银行是首批计划部署该平台的机构。新闻稿的用词传达了信号：Anthropic 工程师与 FIS 嵌入合作，共同设计金融犯罪智能体，并“转让知识，以便 FIS 以后能够独立构建和扩展更多的智能体”。简单来说，前置部署工程师负责嵌入、构建和转让。

行业巨头 ServiceNow 和 Accenture 先走了一步。前一周，两家公司启动了一个联合前置部署工程师计划，将他们的工程师共同嵌入到客户环境中，在 ServiceNow AI 平台上构建智能体工作流。Accenture 自己的《变革脉搏》研究解释了原因：只有 32% 的企业领导者报告了持续的、全企业范围的 AI 影响。剩下的 68% 只有试点项目、PPT 和交付差距。IBM 的 Varun Bijlani [本周也指出了同样的问题](https://www.ibm.com/think/insights/conversation-forward-deployed-engineers-incomplete)，他表示“执行速度”现在是 2000 名高管中排名第三的高级战略优先级。

> “前置部署工程师或类似职位即将成为科技界需求量最大的工作之一。部署智能体是一项比大多数人意识到的要技术化得多的任务，通常比部署软件要复杂得多。”

Box 首席执行官 Aaron Levie 在 5 月 12 日[总结了这一时刻](https://x.com/levie/status/2054398342852194386)：“前置部署工程师或类似职位即将成为科技界需求量最大的工作之一。部署智能体是一项比大多数人意识到的要技术化得多的任务，通常比部署软件要复杂得多。”Levie 说的没错。有了智能体，你不再是部署软件，而是在企业内部部署一个工作产出，客户期望你一次性将他们从当前状态带到最终状态。这是一项艰巨的工作，即使对于经验丰富（且高薪）的前置部署工程师也是如此。

## 如何为前置部署工程师角色进行培训

Foundation Capital 的 [Jaya Gupta](https://www.linkedin.com/in/jayagupta10/)（曾任职于麦肯锡）[针对谷歌的声明](https://x.com/JayaGup10/status/2054596613075763623)对该角色的重新定义比任何人都好：“前置部署工程师模式的核心是人才，而不不仅仅是部署。麦肯锡让‘客户服务’对商业通才来说变得体面。Palantir 让‘嵌入式部署’对技术通才来说变得体面。AI 时代待解决的问题是，谁能让 AI 落地感觉像是一项尖端工作？现在你可以看到很多大四学生在问：‘在哪些地方做这些前置部署工作会显得很酷。’”

> “AI 时代待解决的问题是，谁能让 AI 落地感觉像是一项尖端工作？”

前置部署工程师之于 AI 时代，就像麦肯锡的客户服务通才之于咨询业，Palantir 的嵌入式部署角色之于国防和情报业——它是吸引技术人才的高威望早期职业磁铁。本科生们已经明白了这一点。问题在于哪家实验室会成为这些人才梦寐以求的雇主。

如果你已经过了本科阶段，这条路径同样稳固。在发布第一条推文的第二天，Aaron Levie [写了一篇后续文章](https://x.com/levie/status/205472996663044100)，读起来就像一份教学大纲。值得全文引用：

*“如果我是大学职业顾问或从事职业服务工作，我会迅速弄清楚如何让学生理解这些前置部署工程师职位的存在以及如何获得这些职位。要求是深厚的技术技能，通常是计算机科学专业或辅修。你必须擅长理解问题解决、如何具备系统思维，并拥有强大的业务敏锐度。当然，关键是要确保你在 AI 智能体方面非常深入；你需要流利地使用智能体编码、MCP、CLI、Skills 等。成百上千（数千？）家技术公司将招聘这些职位，任何咨询和 IT 服务公司也是如此，绝大多数中大型企业也将内部招聘此类人才。”*

Levie 给了你技术栈。计算机科学基础。系统思维。业务敏锐度。深厚的 AI 智能体熟练度——智能体编码 (Claude Code, Cursor, Codex)、模型上下文协议 (MCP)、智能体命令行界面 (CLI) 以及顶层的 Skills 层。如果你是一名开发人员，这是在你已有知识基础上的附加课程。如果你是工程领域的邻近人员——产品经理、分析师、运营人员、像我这样的编辑——这是转向最高杠杆角色的最直接地图。

**最直接的培训路径已经公开。** 我们在 IMG 的团队运行着 [Roadmap.sh](http://roadmap.sh)，而 [AI 工程师路线图](https://roadmap.sh/ai-engineer)是与 Levie 的技术栈最匹配的一页纸指南——涵盖了大语言模型基础、RAG、智能体、MCP、评估、提示词工程和部署模式。将其与谷歌发布的 FDE 要求相结合作为你的就绪清单：具备 RAG 架构、向量数据库、基础模型微调以及在云平台上进行生产级 AI 部署的实战经验。

这就是谷歌或 Anthropic 的招聘人员目前对候选人的要求。将路线图作为课程进行学习，配合在 Claude Code、Cursor 或 Codex 中的日常动手练习，并构建出一些可以交付的东西。将 AI 工程师与前置部署工程师区分开来的是客户背景，而获得客户背景的唯一方法就是向客户交付东西——内部客户也算。

如果你是从数据端切入，同样会出现向重塑该职位的转变。在上周的 *Towards Data Science* 上，Sara A. Metwalli 在“[从数据科学家到 AI 架构师](https://towardsdatascience.com/from-data-scientist-to-ai-architect/)”一文中提出，现代数据科学家的日常工作已经发生了反转：“只有 10% 到 20% 的时间花在模型使用上（API 调用、推理），而 80% 到 90% 的时间花在编排上——处理数据流、集成和基础设施。”这与谷歌发布的职位描述是一样的，只是从数据的角度来写的。

这项工作的非技术部分至少同样重要。Riggins 的文章引用了 Coleman 关于被低估技能的看法：“现在，擅长写作是一项比以往任何时候都更重要的技能，因为即使 AI 能够抛出各种东西，它仍然遵循‘垃圾进，垃圾出’的逻辑。”Riggins 在文章中采访的 AI 职业教练 [Sundeep Teki](https://www.linkedin.com/in/sundeepteki/) 将 AI 前置部署工程师的工作日描述为“默认生活在模糊性中”。模型几乎可以做任何事情。前置部署工程师需要弄清楚模型应该做什么、为谁做、在什么时间线上做以及成本是多少。前置部署工程师必须具备判断力、沟通技巧和领域专业知识。

虽然前置部署工程师在今天很火，但我怀疑这个岗位的持久性。最终，随着更多的工程师、产品经理和技术领导者变得精通 AI，企业会将这个角色转为内部职能。然而，无论你是想成为嵌入式工程师还是其内部对接人员，技能栈都是一样的，我建议你今天就开始学习 AI 工程路线图。

---

## 往期内容