<!--
title: AWS让智能体自主构建并维护免费开源的AWS模拟器
cover: https://cdn.thenewstack.io/media/2026/11/ad6fe451-img_5814-1024x768.jpg
summary: AWS近日推出一款名为AWS Emulator的免费开源模拟器，该项目完全由智能体团队自主构建并负责后续维护。该模拟器基于Smithy模型生成，采用CCO许可证开源，旨在帮助智能体在无需AWS凭证的情况下高效测试代码。
-->

AWS近日推出一款名为AWS Emulator的免费开源模拟器，该项目完全由智能体团队自主构建并负责后续维护。该模拟器基于Smithy模型生成，采用CCO许可证开源，旨在帮助智能体在无需AWS凭证的情况下高效测试代码。

> 译自：[AWS had its agents build a free and open emulator for AWS. They now maintain it, too.](https://thenewstack.io/aws-emulator-ai-agents/)
> 
> 作者：Frederic Lardinois

AWS于周三推出了一款名为AWS Emulator的AWS模拟器。

单凭这一点，就已经足够有趣，并且可能会引发人们对 [LocalStack 未来](https://www.localstack.cloud)的种种疑问。但最有趣的地方在于，这个模拟器完全是由一个智能体团队构建的，并且在未来也将由它们进行维护。

由于AWS不确定能否对这些智能体的工作主张版权——并且不想在可能不存在版权的地方宣称版权——因此该模拟器在 [Creative Commons Zero 许可证](https://creativecommons.org/publicdomain/zero/1.0/deed.en)下发布，这意味着该代码已被置于公共领域。

AWS首席开源软件策略师Tom ‘Spot’ Callaway向The New Stack透露，过去显然出现过其他模拟器——AWS自己也构建过一些。

他解释说：“面临的挑战是它们过时得非常快。它们并不总能反映地面的实际情况，正因如此，人们往往不信任它们。甚至我们在内部也不信任它们。”

随着 [智能体编程工具](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/)的崛起，该团队也看到了对更好模拟器的需求，这个模拟器可以帮助智能体 [针对AWS服务测试代码](https://thenewstack.io/runtime-verification-coding-agents/)，而无需将AWS凭证交给智能体。

![](https://cdn.thenewstack.io/media/2026/11/e05101e5-screenshot-2026-11-11-084900-1024x556.png)

构建AWS Emulator的智能体系统。图片来源：AWS。

与此同时，该团队还在寻找一个使用智能体构建完整项目的测试用例，而这个模拟器被证明是一个很好的试验场，在很大程度上是因为它提供了一个边界清晰、目标明确且能够测试结果的问题空间。

Callaway表示，由于AWS已经发布了一整套作为Smithy模型的API模型，并从这些文件中生成了所有SDK，“我们没有任何理由不能围绕相同的逻辑生成模拟仿真。”

### 一个周末的Kiro实验

这个项目可以追溯到AWS开发者工具团队高级首席工程师Matt Goldberg的一个实验。Callaway说，团队“深受Anthropic实例化编译器的工作启发”，他指的是Anthropic研究人员在今年早些时候让 [一个智能体团队](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/)构建的C编译器。

Goldberg在 [一篇博客文章](https://aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator)中写道，他首先让AWS的智能体编程工具 [Kiro](https://thenewstack.io/kiro-is-awss-specs-centric-answer-to-windsurf-and-cursor/) 为Amazon Simple Queue Service (SQS) 构建一个模拟器。15分钟后，它交出了第一个版本。随后，他在一个周末让Kiro构建了AWS的其余部分。他指出，不出所料，该版本存在一些漏洞，但他的团队在接下来的星期一就开始针对它测试自己的软件。

Callaway说：“我必须承认，当我第一次听到这个消息时，我的反应是：‘我们确定这是一个好主意吗？’”

他补充说，随着团队不断对其进行迭代，他越来越确信这是一个适合智能体去解决的好问题。

在其当前版本中，AWS Emulator支持438个公共AWS API模型，涵盖200多个服务。随着AWS更新它们并发布新服务，智能体也会迅速更新模拟器。

Callaway预计，新AWS服务发布与模拟器支持它之间的时间差将是“几天，而不是几周，也不是几个月”，尽管他指出团队尚未看到该项目公开后面临的具体情况。

模拟器本身是用Rust编写的，在Linux、macOS和Windows上本地运行，无需网络连接或AWS账户。

Callaway说：“AWS Emulator内部没有AI。它根本不进行LLM调用。”

### 三个智能体团队

AWS表示，它将工作分配给三个智能体团队。第一个团队从公共Smithy模型开发测试场景，并针对真实的AWS服务运行这些场景，以确立模拟器应该如何表现。

这些场景可以涉及多个服务协同工作，而不仅仅是单独的API调用。正如Callaway所解释的，“如果文档没有说实话，那么云就变成了真相的来源。”

第二个团队针对模拟器运行这些场景，并调查其行为与AWS有何不同。它将那些似乎具有共同原因的故障分组，并在代码库中提交问题。

最后，第三个团队接收这些问题并修改代码以解决它们。在这些代码更改能够合并之前，它们必须通过构建和测试检查，以及其他智能体对安全性、编码标准以及模拟器行为回归的审查。

与此同时，人类工程师则专注于改进指导智能体的系统。

Callaway在谈到模拟器的代码时说：“我们不编辑它。我们不修改它。如果我们发现代码有问​​题，我们会尝试将这些问题追溯到智能体并修复智能体，这样它就不会写出糟糕的代码。”

因此，当这些智能体生成的代码出现问题时，团队会改变智能体的工作方式，而不是手修代码。

Goldberg写道，早期版本的智能体一度决定编写自己的Python解释器，以便模拟器能够支持Lambda函数。此后，团队指示它们重用现有的库。

Callaway说：“我想我们在沙盒方面学到了很多，过去几个月大家不都是这样吗？”

他说，该系统的早期迭代“没有他们所需要的那么激进的 [沙盒](https://thenewstack.io/cloud-agent-code-sandboxes/)”，并且早期人们担心智能体会查看AWS内部服务的源代码，以弄清楚如何实现像Aurora这样的功能。团队还花了很多时间向亚马逊高管保证，构建模拟器的框架不会“失控”。

### 不接受拉取请求（Pull Request）

这种放手的态度同样适用于外部贡献者。

Callaway说：“我们根本不会在这个项目上接受拉取请求。智能体将处理这些。我们会接受客户提出的问题。”

他将智能体描述为“它们自己的微型拉取请求军队”。他说，如果它们一直弄错某个API，“那是智能体中的一个bug”，他预计客户主要会贡献模拟器目前处理得不那么好的场景。

Callaway说，AWS还在发布用于测试模拟器的基准测试，“这样你就可以不信任我们。你可以运行该基准测试。”他指出，其他人也可以用它来对自己工作进行基准测试。

### 模拟器做不到的事

不过，用户不应该指望模拟器能做实际服务所做的事情。

Callaway说：“我运行了这个SQL查询，却没有得到正确的结果。嗯，你猜怎么着？这里没有数据库。”他说，模拟器“确实是为了测试覆盖率的目的而构建的”。

AWS表示将在11月30日开始的re:Invent大会上分享更多关于该项目的消息。The New Stack将亲临现场——并且 [我们甚至将举办一场派对](https://thenewstack.io/event/aws-reinvent-reception-with-sourcegraph-and-opslevel/)。