<!--
title: 三级AI协作：开发者的理想境界
cover: https://cdn.thenewstack.io/media/2026/01/738affc7-collaboration-sweet-spot.jpg
summary: 文章探讨AI委托的五个级别，强调三级AI协作为开发者保留架构监督又能代理繁重工作的“黄金点”，并提出根据经验选择级别、批判AI代码、利用上下文窗口和AI测试的重要性。
-->

文章探讨AI委托的五个级别，强调三级AI协作为开发者保留架构监督又能代理繁重工作的“黄金点”，并提出根据经验选择级别、批判AI代码、利用上下文窗口和AI测试的重要性。

> 译自：[Level 3 AI Collaboration: The Sweet Spot for Developers](https://thenewstack.io/level-3-ai-collaboration-the-sweet-spot-for-developers/)
> 
> 作者：Jennifer Riggins

*这节选自[《企业级AI：制定和扩展AI战略的行动指南》](https://thenewstack.io/ebooks/generative-ai/ai-for-the-enterprise-the-playbook-for-developing-and-scaling-your-ai-strategy/)一书的第五章，该书由著名科技记者Jennifer Riggins撰写，并由[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)和[Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention)赞助。*

*从采用“双速”AI投资模式的优势到衡量AI的实际影响，这本[免费书籍现已开放下载](https://thenewstack.io/ebooks/generative-ai/ai-for-the-enterprise-the-playbook-for-developing-and-scaling-your-ai-strategy/)，它帮助企业领导者制定AI战略，以实现生产力提升，解决以前不可能解决的问题，并获得真正的竞争优势。*

---

## AI究竟应该掌管多少？

这在未来一两年内可能会发生巨大变化，但就目前而言，你的企业必须在组织层面、用例层面和团队层面决定你想赋予AI多少自主权。生成式AI（GenAI）仍然给用户留下了大量的控制权——除了面向公众的聊天机器人——但当你进入代码代理甚至代理AI集群时，这种情况就会改变。

“两个极端是：让AI完成所有事情，[或者]让所有事情都手动完成，”软件工程师兼技术负责人Peter Szel说。“但在中间有多个层次，例如，我定义架构，我定义我想要遵循的模式和实践，我创建计划，”而AI则根据这些进行操作。

Szel已经确定了[AI委托的五个级别](https://agentcommander.academy/blog/5-levels-of-ai-delegation?utm_source=ebook&utm_medium=referral&utm_campaign=Series13Book2)，旨在帮助企业摆脱“AI与否”的二元选择：

*   **级别 1 – 手动编码：** 特别适用于关键系统或工程师学习新事物时。
*   **级别 2 – 目标辅助：** 请求AI执行单个函数或类。
*   **级别 3 – 逐步协作：** 工程师创建计划，AI对其进行审查和迭代，然后为每个任务请求批准。
*   **级别 4 – 计划后执行：** 工程师定义问题，然后AI创建计划。工程师随后进行完善，AI自主执行。
*   **级别 5 – 氛围编程：** 工程师用自然语言编写提示，AI无需审查即可编写和执行代码。这最适用于头脑风暴和快速原型开发。

他指出，前两个级别速度不快，但你的团队保留了架构监督权。后两个级别速度确实更快，但即使是工程师也不太可能知道实现细节，这使得发现问题变得更加困难。

Szel认为，级别3是“黄金点”，在此级别上，开发者保留了架构监督权，但将繁重的工作委托出去。

一切也取决于工程师的经验。初级到中级开发者必须优化学习，应避免级别5，而专注于级别1和2。更重要的是养成“严厉批判”AI生成代码的习惯：

1.  尝试找出它可能失败的原因。
2.  思考类似或替代的方法。
3.  考虑这段代码如何适应整体应用程序架构。

级别4与[规范驱动的AI开发](https://thenewstack.io/what-is-an-ai-native-developer/?utm_source=ebook&utm_medium=referral&utm_campaign=Series13Book2)不同，后者将规范作为单一事实来源，AI代理执行。Szel认为，规范驱动的开发剥夺了工程的创造性工作。

“只根据规范工作，让代理生成代码，这对我来说听起来很糟糕，”他说。“尽管它可能有效，但我真的不想每天花八个小时在规范上。”

此外，他认为，规范驱动的开发将要求开发者不仅维护更多的代码，还需要维护更多的规范。

确保你的工程师和数据科学家为开发者精心策划上下文窗口。Szel说，这包括你正在使用的代码库或代码文件，以及编码和架构指南——任何你需要大型语言模型（LLM）在分配任务时注意到的信息。

他警告说，如果工程师将上下文窗口留空，LLM肯定会产生幻觉。但如果上下文窗口过于混乱，LLM将难以弄清楚该做什么。

然后，他继续说，让编码代理通过尝试自己运行代码来测试其结果。

Szel“要求代理首先创建自动化测试，这是我在它们开始之前会审查的东西。”

他表示，这提供了几个优势，因为“如果它们能编写出正确的测试，这意味着它们至少理解了正在解决的问题，然后它们就可以继续实施。然后，在它们实施新功能或修复bug之后，它们可以自己运行测试，检查它们是否真的修复了bug或实施了功能。”