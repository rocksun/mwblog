<!--
title: LinkedIn如何通过人工智能提升你的技能水平
cover: https://cdn.thenewstack.io/media/2023/12/960a5270-ai-generated-8407210_1280-1024x579.jpg
-->

LinkedIn视技能为一切，它是职业世界的通用语言，也是机会的伟大民主化者。

> 译自 [How LinkedIn Levels up Your Skillset … with AI](https://thenewstack.io/how-linkedin-levels-up-your-skillset-with-ai/)，作者 Joab Jackson 是The New Stack的高级编辑，负责报道云原生计算和系统运维。他已经在IT基础设施和开发领域报道了超过25年，包括在IDG和Government Computer News的工作。在此之前，他...

即使感觉您的简历未能充分展示您的广泛知识和潜在价值？别担心：LinkedIn 会为您提供支持。

公司通过运用人工智能、分类法的发展以及大量计算资源，极力打磨您向世界展示的技能组合，以更好地理解您的个人资料。

“我们看到未来职场将以技能为先导的经济为中心，”写道 LinkedIn 人工智能技术负责人[Ji Yan](https://www.linkedin.com/in/curiousitylens/)，他在上周三发表的一篇多人合著的博客中[解释了公司如何分析用户数据](https://engineering.linkedin.com/blog/2023/extracting-skills-from-content-to-fuel-the-linkedin-skills-graph)，更好地阐述其工作技能。

对于 LinkedIn，技能是一切，是专业语言，也是机会的伟大平等者。

因为正如 LinkedIn 的 Yi Pan [所言](https://engineering.linkedin.com/blog/2023/Building-maintaining-the-skills-taxonomy-that-powers-LinkedIns-Skills-Graph)：“技能在劳动力市场上拉平了竞争场地。”

技能展示了“会员的能力 - 而非他们上过哪所学校，成长在哪里，或者曾在哪里工作过。”

更实际地说，用户技能组合的[更好模型为 LinkedIn 提供了更多可操作的数据](https://thenewstack.io/ai-development-needs-to-focus-more-on-data-less-on-models/)，以帮助用户找到下一份工作或提升专业技能，同时也为企业找到更合适的候选人，尤其是在“积极寻找人才的领域，”潘指出。

## 一份简历并不足够

热衷使用LinkedIn的用户当然会在他们的个人资料中添加技能列表，位于专门的技能部分（有些用户可能更加详细）。但他们也在其他部分留下关于他们知识的各种细节。他们会上传简历，在摘要和经验部分包含额外的信息。如果某人参加了LinkedIn Learning的课程，他们也会积累相应的专业技能。

“我们不想错过这些技能，因此从文本中提取它们是至关重要的，”Pan 写道。

这就是人工智能派上用场的地方，从所有这些非结构化数据中[提取和映射技能](https://engineering.linkedin.com/blog/2023/extracting-skills-from-content-to-fuel-the-linkedin-skills-graph)。

![](https://cdn.thenewstack.io/media/2023/12/907e972a-linkedin-03-survey.png)

*LinkedIn收集更多关于您卓越技能的数据的方式。*

LinkedIn以一种精细调整的方式来了解不同格式的数据，比如简历或会员资料。“技能在何处以及以何种方式提到，可以提供关于技能相关性以及我们应该如何解释技能提及的重要信号，”研究人员强调。

一旦被发现，术语还必须被标准化（是“数据分析”还是“数据分析”？）并与LinkedIn的技能分类体系进行调和。

![](https://cdn.thenewstack.io/media/2023/12/4c5139f8-linkedin-01-mapping.png)

并非所有技能在文本中都明确命名。有人可能写“有设计iOS应用程序的经验”，但并未使用这种经验的规范名称，“移动开发”。

然后，技能标记器可以通过基于标记的方法和语义匹配连接短语与技能集。

语义方法基于一组[大型语言模型](https://thenewstack.io/3-ways-llms-can-let-you-down/)（LLM）文本编码器。研究人员提到了其中一个，[多语言BERT](https://huggingface.co/bert-base-multilingual-cased)（M-BERT），它为源文本和技能名称生成上下文嵌入。

通过使用[LinkedIn的技能图（Skills Graph）](https://thenewstack.io/linkedins-real-time-graph-database-is-liquid/)，技能也得以扩展，可以查询其他相关技能。

## 但是你是专家吗？

系统还尝试估计您在某项技能上的熟练程度，这是一项更具挑战性的任务，考虑到人们在各方面都倾向于[高估自己的能力](https://thenewstack.io/10x-programmer-just-jerk/)。

“虽然鼓励会员在LinkedIn个人资料中列出他们的技能很容易，但估计他们在这些技能上的专业水平更具挑战性，”研究人员写道。

他们使用了一个多任务学习框架，采用了“包含来自多个上下文的信号的不确定性加权方案”。

这项工作还帮助公司识别用户的重要技能，用于呈现用户可能忽略的机会。（要查看您自己的前10项技能，[请登录网站的“技能和背书”部分](https://www.linkedin.com/help/linkedin/answer/a507663/linkedin-skill-assessments?lang=en-us&intendedLocale=en)。）

## LinkedIn实时推荐

在十亿用户中进行的这种数据处理已经足够令人印象深刻，但使这项任务更具挑战性的是，这些信息必须始终保持更新。

“如果没有将内容映射到技能图的强大技术堆栈，它将只是一个随时间过去而过时的静态列表，”言等人写道。“相反，LinkedIn能够不断更新和演进技能图，以保持与不断变化的技能领域同步。”

结果被应用于许多LinkedIn产品和功能，包括搜索、推荐、动态排序、职位搜索和列表、招聘搜索等。

![](https://cdn.thenewstack.io/media/2023/12/9b332f3a-linkedin-01-workflow.png)

平均而言，LinkedIn用户每秒进行200次全球性的个人资料编辑。此外，LinkedIn希望每条消息的处理时间都在100毫秒以内。

“在像LinkedIn这样的平台上为一个完整的12层BERT模型提供服务，同时保持延迟标准，即使对于行业领导者来说也是一项艰巨的任务，因为BERT虽然在自然语言处理中非常强大，但参数数量庞大，计算需求大，”研究人员自豪地宣称。

然而，所有这些工作都回归到LinkedIn的主要使命，即连接全球的专业人士，使每个人更富裕、更成功。

“当求职者在LinkedIn上打开一个职位发布时，一个功能会显示他们的个人资料与该职位之间有多少技能重叠，”研究人员写道。“通常而言，重叠越多，申请成功的可能性就越大。”
