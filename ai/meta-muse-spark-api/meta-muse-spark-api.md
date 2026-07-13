<!--
title: Meta推出首个付费AI模型Muse Spark 1.1
cover: https://cdn.thenewstack.io/media/2026/05/15f241cf-mylene-caneso-vbagaelzprw-unsplash-scaled.jpg
summary: Meta发布首个付费AI模型Muse Spark 1.1，主打高性价比API，旨在通过强大的智能代理与编程能力与OpenAI和Anthropic竞争，并以此作为推动公司AI商业化进程的核心举措。
-->

Meta发布首个付费AI模型Muse Spark 1.1，主打高性价比API，旨在通过强大的智能代理与编程能力与OpenAI和Anthropic竞争，并以此作为推动公司AI商业化进程的核心举措。

> 译自：[Meta debuts Muse Spark 1.1 — its first paid AI model](https://thenewstack.io/meta-muse-spark-api/)
> 
> 作者：Amanda Caswell

Meta周四推出了Muse Spark 1.1，这是其AI平台的重大更新。距离其在AI主管Alexandr Wang领导下发布首个模型仅过去三个月。此次发布似乎表明了Meta Platforms首席执行官Mark Zuckerberg想要缩小与OpenAI和Anthropic之间差距的迫切心情。

Wang在最近的一次[CNBC采访](https://www.cnbc.com/2026/07/09/meta-jumps-into-ai-coding-market-to-chase-anthropic-and-openai.html)中将Muse Spark 1.1描述为实验室“迄今为止最强大的代理和编程模型”。第一个Muse Spark（内部代号为Avocado）于4月在封闭合作伙伴计划下发布，没有面向公众的API。这一次，Meta正在开设一个带有公开等候名单的开发者门户。不过，不要指望在OpenRouter或其他第三方市场上找到它——Meta目前将分发权保留在自己的服务器上。

这是几天内发布的第二个Muse模型。周二，该公司发布了Muse Image（最初代号为Mango），这是一款旨在吸引创作者和广告商的图像生成模型。

## 以价格压制竞争对手

在拥挤的AI工具市场中，Zuckerberg正在重新思考价格。Muse Spark 1.1附带了一个付费开发者层级——这是Meta首次对其AI模型进行定价，也是投资者一直期待的新收入来源。

“由于这不是一个开源模型，我认为这是我们第一次做真正严肃的API，”Zuckerberg在[*Bloomberg Intelligence*播客](https://www.bloomberg.com/news/audio/2026-07-09/bloomberg-intelligence-meta-unveils-ai-model-podcast)上说。“而且定价将非常有侵略性和吸引力。”

新的Meta Model API的价格大约是OpenAI和Anthropic对其顶级模型收费的四分之一。新账户预先获得20美元的免费额度。此后，每百万输入token收费1.25美元，每百万输出token收费4.25美元。

定价只是转变的一部分。到目前为止，想要使用Meta前沿AI进行构建的开发者通常会下载Llama权重并自行托管模型，或者依赖第三方云提供商。Muse Spark 1.1通过允许开发者通过新的Meta Model API调用Meta自己的托管基础设施来改变这一局面，使该公司在API工作负载方面直接与OpenAI、Anthropic和Google竞争。

这代表了Meta企业战略的显著变化。Meta不再将可下载模型视为主要产品，而是开始将自己的平台定位为开发者的首选，这些开发者需要托管推理、更低的运营开销，并在公司最新前沿模型发布时立即获得访问权限。

“其他一些实验室的定价非常极端，利润率很高，”Zuckerberg指出。“我们认为，我们确实有能力以更实惠的成本提供前沿或非常高水平的智能。”

> “其他一些实验室的定价非常极端，利润率很高。”

## 智能代理成为核心

新模型最突出的改进在于其代理能力——即能够代表用户自主完成多步骤任务的系统。Zuckerberg将Muse Spark 1.1描述为具有“最先进或非常接近最先进”的代理推理和工具使用能力。

Wang在Meta Superintelligence Labs的团队非常注重编程性能，理由是精通代码的模型可以处理并行工作流并将工具链接在一起——这是AI代理所需的核心能力。

对于工程团队来说，这种关注反映了企业AI开发的发展方向。生产级代理花在生成文本上的时间越来越少，而花在调用API、编写代码、协调工作流和与外部工具交互上的时间越来越多。针对这些能力进行优化，使得Muse Spark 1.1对于构建自动化系统的开发者来说，比那些单纯寻找聊天机器人的用户更有意义。

“你必须将编程能力作为整体代理能力的一部分来构建，”Wang告诉CNBC。据Wang称，该模型在测试AI如何与第三方开发工具协同工作的基准测试中击败了竞争对手——并且MSL特意针对开发者已经在使用的工具进行了优化，押注兼容性将比原始基准测试分数更快地推动采用。

> “你必须将编程能力作为整体代理能力的一部分来构建。”

Zuckerberg还表示，该模型在涵盖代理工作流、编程和多模态推理的几项内部基准测试中表现优于Google的Gemini。“这是一个非常有趣的里程碑，因为我认为这可能是我记忆中第一次Meta的模型优于所有Google的模型，”他说。

> “这是一个非常有趣的里程碑，因为我认为这可能是我记忆中第一次Meta的模型优于所有Google的模型。”

Llama在2025年春季的发布可以说令人失望，Zuckerberg通过实质上的重新开始做出了回应。他从Scale AI挖来了Wang来管理它，裁减了员工，并重组了团队。

这种转变并不一定意味着Meta正在放弃开源模型。相反，它表明该公司现在将托管AI服务视为同样重要的业务。开放权重模型帮助建立了Meta在开发者中的信誉，但托管API可以产生经常性收入，并将开发者保留在Meta的生态系统中，而不是将推理工作负载发送给云提供商或竞争的AI平台。计划中的Muse Spark开源版本表明，Meta试图平衡这两种方法，而不是二选一。

## AI投资的变现

Meta的2026年资本支出预测处于创纪录水平；该公司正在向计算、芯片和数据中心投入数千亿美元，在加拿大投资100亿美元的设施是其最新举措。华尔街对Zuckerberg施加了巨大的压力，要求其展示回报；在Meta的4月财报发布后，尽管收入强劲，但由于缺乏明确的AI变现计划，股价下跌了近9%。

Muse Spark API的推出，以及消费者聊天机器人订阅计划和潜在的企业AI代理计划，是Meta的直接回应。

Zuckerberg驳斥了AI模型不可避免地会变成难以区分的商品这一观点，并以Anthropic的最新模型Mythos为例，说明了公司如何控制技术。“这些能力实际上并没有扩散或广泛提供给每个人，”他警告说。

目前，Meta希望Muse Spark 1.1及其极具侵略性的定价能确保高质量的智能保持可访问性，为Meta AI聊天机器人等免费工具提供动力，同时在开发者市场中开辟一个有利可图的空间。