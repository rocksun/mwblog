<!--
# 生成式AI如何助力DevOps和SRE的工作流程
https://cdn.thenewstack.io/media/2023/05/8344e4a6-robot-ai-1-1024x576.jpg
Image by Alex Knight from Unsplash.
-->

工程师们自然会喜欢新技术。但他们现在如何利用AI革命来改善日常工作呢?这里有6点建议。

译自 [How Generative AI Can Support DevOps and SRE Workflows](https://thenewstack.io/how-generative-ai-can-support-devops-and-sre-workflows/) 。

随着关于[大语言模型(LLM)](https://thenewstack.io/what-is-a-large-language-model/)和[生成式AI](https://thenewstack.io/learning-to-love-generative-ai-in-software-development/)的讨论从热烈上升到轰动一时，有远见的软件团队戴上耳机，聚焦一个重要问题：我们如何让这项技术立竿见影？

这看起来是天作之合，毕竟技术人员会喜欢新技术，不言而喻。因此，尽管人力资源专业人员可能需要更长时间并更谨慎地考虑如何在工作中使用生成式AI，但开发者、网站可靠性工程师(SRE)和其他技术人员都非常适合尝试并将生成式AI工具应用于工作中。例如，根据Stack Overflow的一项调查，[70%的开发者已经或计划使用AI改进工作](https://thenewstack.io/70-percent-of-developers-using-or-will-use-ai-says-stack-overflow-survey/)。

问题仍然存在：我们该如何让生成式AI发挥作用？

在可预见的未来，用例会不断涌现，但对现代软件团队来说，根据PromptOps CEO兼创始人[Dev Nag](https://www.linkedin.com/in/devnag/)的说法，回答这个问题很大程度上归结为沟通，[PromptOps](https://www.promptops.com/?utm_content=inline-mention)是一个面向[DevOps](https://thenewstack.io/devops/)和SecOps团队的基于生成式AI的Slack助手。

“我认为企业中的所有工作，特别是对DevOps工程师来说，其实就是关于沟通，”Nag告诉The New Stack。“不仅包括人与人之间的沟通，也包括人与机器之间的沟通。”

Nag举了Slack、Jira或Monday等工具作为例子，但他也将DevOps常见任务中查询应用程序获取日志、指标和其他数据，然后根据响应采取行动视为一种沟通形式。

他指出，尽管这种交流是必要的，但也可能重复且浪费时间，这正是生成式AI能发挥巨大作用的地方。

Nag说：“语言模型和生成式AI本质上是交流的超级加速器。它们能够从过去的数据中找到模式，在你表达想法之前就理解你的意图。”

PromptOps最近推出了一款生成式AI工具，它可以通过类似ChatGPT的提示，自动化和优化各种DevOps工作流程，无论是直接在Slack还是网页端。

Nag认为，生成式AI[在DevOps、SRE和其他现代软件团队中的应用潜力是几乎无限的](https://thenewstack.io/promptops-how-generative-ai-can-help-devops/)。 在接受The New Stack的采访时，他分享了六个如今可以将生成式AI应用于DevOps工作流程的示例。

## 生成式AI工具的6个使用案例

### 1. 查询不同工具

DevOps和SRE专业人员经常使用海量工具。 在某些组织，技术“栈”更像一座高塔。

人工查询众多工具的日志和各种可观测数据既费时又费力，效率不高。 哪里有该指标？看板在哪儿？机器名称是啥？通常怎么称呼？通常查看什么时间范围？等等问题层出不穷。

Nag说：“这些背景信息都曾由他人完成。” 生成式AI可以让工程师用自然语言提示直接找到所需内容，通常还可以自动启动后续工作流程，无需离开Slack(或其他客户端)。

“这极大节省时间，因为我不用再掌握数十种工具。” Nag说，“我可以用英语下达提示，它就可以跨工具帮我完成任务。”

### 2. 发现额外环境

此外，生成式AI可以根据需要自动关联额外环境，这也很有用。 所以，尽管可以在Slack(或其他地方输入提示)直接产生所需响应或数据，但生成式AI还可以添加导航层，在适当的时候直接链接到该响应的全文或环境。

这在速度至关重要的情况下尤其有用，最典型的就是服务中断事件。 响应事件每花费一分钟都代价高昂。

Nag说：“任何任务如果投入足够时间都可完成。但问题是我们没有时间和人手，特别是在服务中断场景，速度至关重要，务必尽快恢复客户体验。”

### 3. 自动化和快速执行必要系统操作

就像[Kubernetes](https://thenewstack.io/kubernetes/)之类的编排工具因为能根据期望状态自动执行系统操作而流行起来一样，生成式AI也可以进一步简化和加速工作流程中的必要操作。

Nag说，云原生工具和平台自己也带来复杂性。 执行各种常见运维任务(如预配服务、管理配置、设置故障转移)通常需要与其他组件交互。

“这些任务可能接触许多API。比如[AWS](https://aws.amazon.com/?utm_content=inline-mention) API就有200多种服务。” 他说。

它们语法、控制台、命令行各不相同，子命令更是汗牛充栋——几乎没人会全部记住。 单就这一点，[Kubernetes的学习曲线就令人生畏](https://thenewstack.io/kubernetes-the-magic-is-in-the-complexity/)。

Nag说，要全面掌握云原生生态的庞杂细节几乎不可能。 有了生成式AI，工程师无需记住各系统与工具的细节。

用户只需下达“扩容Pod 2个副本”或“以某种方式配置Lambda函数”等提示。我可以把它转化为目标系统语言的实际代码，自动执行。” Nag说，“LLM几乎像这些非结构化数据与结构化数据之间的虫洞。”

### 4. 撰写事件报告

众所周知，生成式AI在内容创作方面有巨大潜力。 这也适用于系统故障值班人员编写事后报告的场景。

Nag指出，这类报告通常需要查看海量Slack消息、指标、图表、日志等数据。

他说，LLM“可以查看Slack对话——哪怕50万行也没问题——并总结提取关键发现。” 它专注相关数据，过滤无用信息——极大节省人工汇总故障原因的时间。

这再次证明了“虫洞”效应，可以将大量非结构化信息转化为可操作的结构化数据。

### 5. 创建事件

[内容创作](https://thenewstack.io/generative-ai-dont-fire-your-copywriters-just-yet/)类别还包括Nag提到的与事件管理相关的用例：创建工单。 LLM可以在事件或其他IT事件触发的工作流中，自动在Jira、Monday等系统创建工单并启动后续操作。

有时这些操作正是用例4中的事件报告结果：增强的事件报告可以确定如果事件再次发生要采取的更好做法。

“下次我要创建警报，可能还需要额外基础设施等等。” Nag说，“我们可以实际扫描对话，并将其转化为工单。”

### 6. 查找非技术文档

最后但同样重要的是，Nag说，他们发现越来越需要一种方法，无需大量时间就可以发现和调阅非技术文档，比如运行手册或公司政策——不仅包括IT政策，还包括HR福利等常见业务政策。

“你不一定知道这些文档的存储位置。” 他说，随着组织规模扩大，寻找过程可能非常耗时。 类似ChatGPT的提示可以在几秒钟内找到所需内容，而不必在各种维基或工具中进行搜索。
