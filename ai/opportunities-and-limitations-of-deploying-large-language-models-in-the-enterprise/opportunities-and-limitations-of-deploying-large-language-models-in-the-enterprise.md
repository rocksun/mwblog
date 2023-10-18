<!--
# 在企业环境中应用大规模语言模型的机遇与限制
https://cdn.thenewstack.io/media/2023/10/17ae17a7-brain-8258274_1280-1024x766.jpg
Image by Pete Linforth from Pixabay.
 -->

调控大语言模型的不确定性是可行的，每种方法都需要权衡利弊。


译自 [Opportunities and Limitations of Deploying Large Language Models in the Enterprise](https://thenewstack.io/opportunities-and-limitations-of-deploying-large-language-models-in-the-enterprise/) 。

生成式AI正[风靡全球](https://thenewstack.io/how-generative-ai-can-increase-developer-productivity-now/)。近几个月来，我们见证了大量现成的和开源的大型语言模型(LLM)的爆炸式增长，如Meta的Llama 2、OpenAI的GPT-4、Anthropic的Claude 2，以及ChatGPT代码解释器和GitHub Copilot等工具。这个生态系统正在爆炸式扩张，并迅速改变着各个行业。

客户服务和支持就是一个获得了巨大提升的领域。通过[运用LLM](https://thenewstack.io/fixie-and-its-agent-approach-to-leveraging-llms/)，组织能比过去任何时候都更快更个性化地回复客户查询。一个例子是达美航空的“Ask Delta”聊天机器人，它使用生成式AI来帮助客户订票、值机和追踪行李，从而使呼叫中心量大幅减少了20%。

在营销和销售方面，许多组织正在使用ChatGPT等生成式AI解决方案来[撰写营销文案](https://thenewstack.io/generative-ai-dont-fire-your-copywriters-just-yet/)和评分线索。在人力资源领域，许多人力资源主管现在正在使用[大语言模型](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)进行招聘、绩效管理和指导。

同时我们也看到了生成式AI在[软件开发领域](https://thenewstack.io/tns-research-devops-factions-software-development-world/)取得的进步。像[GitHub Copilot和Amazon CodeWhisperer等解决方案正在帮助开发者](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/)更快更准确地生成代码，大大减少了例行任务所需的时间和精力。

我可以继续举例，但总结一下：[每个企业都渴望运用生成式AI](https://thenewstack.io/the-digital-feedback-loop-powering-next-generation-businesses/)，但实际应用中会遇到比想象中更多困难和阻力。

尽管现成的模型正在帮助许多公司开始使用生成式AI，但要在企业内大规模应用还面临挑战。这需要专业人才、新的技术栈来管理和[部署模型](https://thenewstack.io/arrikto-ml-model-deployments-on-kubernetes-can-get-better/)、充足的预算来应对日益增加的计算成本，以及确保安全的防护措施。

## 好处：企业不应错过这次机遇

过去几个月中我们见证的进步可谓惊人。虽然[自然语言理解和处理](https://thenewstack.io/recent-advances-deep-learning-natural-language-processing/)不是全新技术，但现在变得更加易于获取。此外，这些模型的深度和功能在极短时间内就实现了指数级增长。

但是，对许多首席信息官来说，这些价值还不够明显。[过去一年](https://thenewstack.io/time-spent-on-project-licensing-and-dependencies-declined-in-last-year/)，许多组织削减了预算，盲目投资不在他们的考虑范围内。但这并不是可以置身事外的时机。AI有能力[以难以想象的方式](https://thenewstack.io/will-blockchain-change-way-businesses-operate/)塑造企业。以下简要列出一些好处:

- **即时获取全球知识**：这些模型通过训练所有公开数据，使人类全部知识都[可以通过API](https://thenewstack.io/with-auth0-purchase-okta-will-boost-access-apis-for-developers/)或对话提示轻松获取。
- **达到人类水平的语言理解**：这些模型具有[理解和生成](https://thenewstack.io/vector-primer-understand-the-lingua-franca-of-generative-ai/)语言的能力，可以部分或全部自动化企业中的语言理解和写作工作。
- **代码解释和生成**：像GPT-4代码解释器等先进模型可以理解和生成代码，实现与企业中的传统软件无缝对接。
- **内置多语言支持**：开箱即用支持20多种语言，这些模型可以轻松实现全球化应用。

## 目前的局限性

像GPT-4这样的大型语言模型(LLM)基于本质上具有概率特性的[神经网络](https://thenewstack.io/facebooks-open-ai-research-uses-gpu-neural-networks/)。这意味着对同样的输入，每次运行都可能产生略有不同的输出，因为[模型结构中存在随机性](https://thenewstack.io/how-to-choose-and-model-time-series-databases/)，训练过程也具有随机性。这就是我们说LLM是“不确定的”的含义。

这种不确定性会以多种方式成为[构建企业级业务应用](https://thenewstack.io/how-to-build-applications-over-streaming-data-the-right-way/)的局限:

- **一致性**：企业通常需要可靠、一致的结果，特别是在处理诸如金融、医疗或法律等敏感领域。LLM的不确定性可能导致输出不一致，在这些环境下会成问题。
- **审计性**：在许多行业，审计和追溯自动化系统的决策非常重要。如果LLM做出一个决定或建议，后续无法复制相同输出，则审计和问责会变得困难。
- **可预测性**：在许多商业场景下，基于确定输入预测系统行为至关重要。使用不确定模型难以保证特定输出，这使得规划和制定战略更具挑战性。
- **测试**：测试是任何软件开发流程(包括业务应用开发)的重要组成部分。LLM的不确定性使编写和运行稳定、可重复的测试变得困难。
- **风险管理**：由于LLM的概率性质，其输出总会存在不确定性。这可能增加业务应用中的风险，特别是在敏感领域。

尽管存在这些挑战，我们还是有方法来管理LLM的不确定性，例如使用集成方法、增加后处理规则或设置随机种子以获得可重复结果。但是，这些方法都存在取舍，无法完全解决问题。
