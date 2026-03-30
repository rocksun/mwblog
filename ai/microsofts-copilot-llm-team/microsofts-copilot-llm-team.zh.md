微软的AI战略在很大程度上一直在使用第三方大型语言模型（LLM）。起初主要使用OpenAI的GPT模型，但最近也包含了Anthropic的Claude——现在微软正同时使用它们来改进[Copilot 的研究员代理](https://learn.microsoft.com/en-us/copilot/microsoft-365/researcher-agent)。

研究员代理是微软推荐用于需要更深层次推理或跨多个来源解决问题的情况。现在，它包含一个可选的“批判”功能。有了这个功能，GPT将撰写草稿，然后由Claude进行审查。正如微软在其公告中指出，这项审查将包括对“准确性、完整性和引用完整性”的检查。

微软表示，未来也可能给用户提供选项，将这个流程反转，让Claude撰写而GPT检查。

## Claude和GPT：强强联合，更胜一筹？

这种工作流起初可能感觉有点粗糙，但这与开发者有时使用一个模型编写代码，然后使用另一个（来自不同模型家族的）模型进行代码审查的方式并没有太大区别。

至少在微软的基准测试中，这种方法也显示出一些明显的优势。使用Perplexity的[深度研究DRACO基准](https://research.perplexity.ai/articles/evaluating-deep-research-performance-in-the-wild-with-the-draco-benchmark)，Anthropic的Claude Opus 4.6单独得分42.7，在Perplexity的深度研究模式下得分50.4。Copilot的研究员代理开启批判功能后得分57.4，高于任何单个模型。

![](https://cdn.thenewstack.io/media/2026/03/df1112e3-image002-1024x615.png)

图片来源：微软。

遗憾的是，我们还没有OpenAI的GPT-5.4的基准测试数据，但其分数很可能与Opus 4.6处于同一范围。

Copilot研究的另一个新功能是所谓的“理事会”。这允许用户并排比较不同模型如何处理一个查询。

## Cowork现已加入M365前沿计划

最近，微软还[宣布](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/)将Anthropic的[Claude Cowork](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/)工具——本质上是为需要能完成多步骤工作流的长期运行代理的知识工作者提供的Claude Code——引入Copilot。

这个富有想象力地命名为Copilot Cowork的功能现已在早期访问的Microsoft 365[前沿计划](https://adoption.microsoft.com/en-us/copilot/frontier-program/)中提供。

![](https://cdn.thenewstack.io/media/2026/03/f000b995-copilot-cowork-hero-1024x576.webp)

图片来源：微软。

微软的优势在于，如果许多客户必须将他们的数据上传到Anthropic，他们可能会担心使用Cowork。但由于这些公司已经在使用Microsoft 365，并且Copilot Cowork数据在其控制范围内（Cowork在一个沙盒云环境中运行），这使得他们现在能够利用这些新工具。

“这不仅仅是生成内容或答案。它关乎采取实际行动——连接步骤、协调任务，并在日常工作流中贯彻执行，”Capital Group企业技术高级副总裁Barton Warner说。“因为Cowork在我们的企业数据和安全风险边界内运行，我们可以自信地进行实验、学习和扩展。这使我们能够更快地行动，并将AI专注于真正能创造价值的地方。”

## 微软为何这样做？

不得不引入Anthropic来推出Cowork和批判等功能，这确实说明了微软现在所处的境地：它正在摆脱早期对OpenAI的依赖，但在这样做的同时，也正在加深与另一个模型提供商的关系。对于为Copilot支付高价的客户来说，他们心中的一个问题肯定是，使用微软服务的价值在于它所协调的模型，还是在于使这些模型首先变得有用的企业数据和信任层。

微软显然正在押注后者，而对于Anthropic来说，这次合作是其成为企业AI供应商的又一步。

当微软首次宣布Cowork时，其业务应用和代理总裁Charles Lamanna指出：“正是这种多模型优势使Copilot与众不同。”如果微软拥有自己的前沿模型，它可能会采取不同的方法，但就目前情况而言，这是它能采取的最佳方法。