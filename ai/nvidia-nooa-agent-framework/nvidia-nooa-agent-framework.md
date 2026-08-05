<!--
title: Nvidia的NOOA让智能体回归单一Python类
cover: https://cdn.thenewstack.io/media/2026/08/68d7ebad-and-machines-yv7g1hol9kg-unsplash-scaled.jpg
summary: Nvidia推出的NOOA框架旨在解决智能体开发碎片化问题，通过将智能体的能力、状态和提示词整合进单个Python类，提升代码可读性与可维护性，同时大幅优化基准测试性能，但也引发了关于安全性与调试复杂度的新讨论。
-->

Nvidia推出的NOOA框架旨在解决智能体开发碎片化问题，通过将智能体的能力、状态和提示词整合进单个Python类，提升代码可读性与可维护性，同时大幅优化基准测试性能，但也引发了关于安全性与调试复杂度的新讨论。

> 译自：[Nvidia's NOOA makes an agent one Python class](https://thenewstack.io/nvidia-nooa-agent-framework/)
> 
> 作者：Meredith Shubel

**上周，当Nvidia宣布 [NOOA (Object-Oriented Agents)](https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/) 时**，它标志着智能体开发领域的一个更广泛的转变：围绕模型构建的“外壳”（harness）可能与模型本身同样重要。

Nvidia 正在将 NOOA 贡献给 [Open Secure AI Alliance](https://thenewstack.io/open-secure-ai-alliance/)，这是一个 [备受关注的行业组织](https://www.google.com/search?q=%22open+secure+ai+alliance%22&sca_esv=fc15e49dbd266fb4&tbm=nws&sxsrf=APpeQnsnb-qNSpvEszrXHberS6Qb9HFlVA:1785851699526&tbas=0&source=lnt&sa=X&ved=2ahUKEwjiwq-BkIeWAxUEODQIHTWWMusQpwV6BAgFEBE&biw=1178&bih=860&dpr=2)，由 Nvidia 上周成立，旨在构建和共享用于AI开发的开源和开放权重工具。

NOOA 基于一个理念：智能体就是一个单一的 Python 类。以下是 Nvidia 在其发布博文中对它的描述：

*“它的方法是它的能力。它的字段是它的状态。它的文档字符串是它的提示词。它的类型注解是强制执行的契约。一个主体为省略号（…）的标准 Python 方法在运行时由一个大语言模型驱动的循环来完成。具有正常主体的方法则作为普通的、确定性的 Python 代码运行。”*

通过将智能体的能力、状态和提示词集中在一个 Python 类中，Nvidia 正在致力于解决智能体开发中存在的碎片化这一棘手问题。

这是一个 [Adnan Masood](https://www.linkedin.com/in/adnano/) 博士（[UST](https://www.ust.com/) 的首席AI架构师）经常见到的问题。

“‘外壳’是包裹在模型周围的一切，”Masood 告诉 *The New Stack*。“今天，它在设计上是分散的。一个基于 LangGraph 或 AutoGen 构建的团队，通常会将提示词放在 Jinja 模板中，工具定义放在 JSON 模式中，回调函数放在 Python 中，而工作流则以另一种抽象形式绘制为图形。”

## 单一 Python 类能否让智能体更容易测试？

Nvidia 的构想是让智能体开发更像传统的软件开发，这样人类和AI编程智能体都可以使用熟悉的编码工具来检查和管理智能体，从而使其更容易测试和追踪智能体行为。

Masood 认为，Nvidia 通过 NOOA 将能力、状态和提示词封装进一个单一 Python 类中，迈出了有意义的一步。但其他专家则持怀疑态度。

[IBM](https://www.ibm.com/us-en) 的解决方案架构师 [Karthik Karunanithi](https://www.linkedin.com/in/karthikkarunanithi/) 同意，将工作流图、提示词模板、模式和回调函数归拢到一个 Python 类中确实是一种改进，但他同时也告诉 *The New Stack*，他怀疑这样做是否会引入新的审查问题，因为“在该类内部，一个带有 `...` 的方法在运行时由模型补全，而下一个方法却只是普通的 Python 代码。”

由于两者具有相同的签名、缩进和文档字符串，Karunanithi 质疑是否会更难区分确定性代码和概率性行为。

当被问及 NOOA 如何帮助测试和追踪智能体行为时，[Thine](https://www.thine.com/) 和 [Merlin AI](https://www.getmerlin.in/) 的联合创始人 [Siddhartha Saxena](https://www.linkedin.com/in/siddsax/) 对 Nvidia 在单一 Python 类中使用类型化输入/输出，从而为智能体调用带来结构化的做法表示赞赏。

Saxena 告诉 *The New Stack*，挑战在于当活动扩展到数百万次工具调用时。因此，他认为测试智能体轨迹在很大程度上是一个**可观测性**问题，而不是像 NOOA 这样的框架能够独自解决的问题。

## 更具可检查性的智能体，但伴随新的执行风险

将智能体的能力、状态和提示词放入一个 Python 类中，可能使其行为更易于检查。但将逻辑集中在一个地方也引发了关于安全性的新问题。

> “一个状态可读且运行轨迹可检查的智能体，比逻辑散布在提示词文件和零散脚本中的智能体更容易审计。”

从大局来看，Saxena 将这种集中化视为一种净收益，称它使智能体代码更具可读性和可维护性。不过，他指出这种可读性可能伴随着代价：“显然，如果某样东西对人类来说是可读的，也就意味着它对‘外星人’来说也是可读的。”

当被问及集中化智能体逻辑是提高了安全性还是带来了新的风险时，Masood 似乎同意 Saxena 的观点，他告诉 *The New Stack* 两者可能同时成立：

“一个状态可读且运行轨迹可检查的智能体，比逻辑散布在提示词文件和零散脚本中的智能体更容易审计。”

但 Masood 补充道，NOOA 可能带来的另一个风险是该框架使用了“代码即动作”（code as action），这允许模型通过编写和运行 Python 来执行操作。“这很强大，”他解释道，“它扩大了提示词注入的爆炸半径，即文档或网页中的恶意文本会误导模型。”

Karunanithi 对这种权衡表示赞同，他承认集中化使智能体逻辑更易于理解，但也集中了风险。像 Masood 一样，他强调了沙箱（sandbox）的必要性，以及为每个智能体配置作用域凭据和独立身份的重要性。

值得注意的是，对于生产部署，Nvidia 将 NOOA 与 [Nvidia OpenShell](https://developer.nvidia.com/blog/run-autonomous-self-evolving-agents-more-safely-with-nvidia-openshell/) 安全运行时配对使用。

## Nvidia 声称基准测试有“两位数”的波动

Nvidia 在解释其发布 NOOA 时指出，外壳设计在智能体性能中起着重要作用，并表示：“仅外壳设计本身，在使用相同基础模型的情况下，就可能导致基准测试结果出现两位数的波动，并在 Token 成本上产生显著差异。”

它用三个基准测试的结果支持了这一主张。在 SWE-bench Verified 上，NOOA 使用 GPT-5.5 达到了 82.2% 的准确率，每个任务使用 29 次大语言模型调用和大约 110 万个 Token。Nvidia 表示，对比外壳需要 66 次调用和 220 万个 Token 才能达到 78.2%，或者需要 29 次调用和 130 万个 Token 才能达到 78.6%。这家科技公司将这一结果描述为“以大约一半的成本实现同等或更好的性能”。

> “仅外壳设计本身，在使用相同基础模型的情况下，就可能导致基准测试结果出现两位数的波动，并在 Token 成本上产生显著差异。”

在漏洞重新发现基准测试 CyberGym L1 上，NOOA 使用 GPT-5.5 解决了 86.8% 的任务。在通用推理基准测试 ARC-AGI-3 上，它达到了 50.2% 的平均 RHAE。

当被问及该框架的基准测试结果对开发者意味着什么时，Karunanithi 告诫不要过度概括。他说 SWE-bench Verified、CyberGym L1 和 ARC-AGI-3 都作为有用的基准测试，因为它们有程序化的预言机，但他指出它们与大多数受监管的生产系统有很大不同，“在那些系统中，没有人能在运行时告诉你保险索赔、访问决策或合规性判断是否真正正确。”

但 Nvidia 似乎追求的不仅仅是更好的基准测试分数。正如 Nvidia 的杰出研究科学家 [Paul Furgale](https://www.linkedin.com/in/paulfurgale/) 在 [LinkedIn](https://www.linkedin.com/posts/paulfurgale_ai-llms-agents-activity-7487524360161755136-7kvZ/) 上发布的：

“我们这样做是因为我们相信开放AI的未来不仅取决于开放模型。它还取决于对这些模型如何与计算机交互的开放研究。”

虽然 Furgale 表示，这家科技公司并不指望每个人都采用 NOOA，但它鼓励开发者社区采用、挑战并改进其技术。