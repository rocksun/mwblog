
<!--
title: AI 基准测试的不足之处，以及如何评估模型
cover: https://cdn.thenewstack.io/media/2025/02/388ceb49-charlesdeluvio-pjah2ax4uwk-unsplash-scaled.jpg
-->

2025年将是[各组织]越来越多地寻求从他们投入巨资的模型中获得价值的一年。

> 译自 [Where AI Benchmarks Fall Short, and How To Evaluate Models Instead](https://thenewstack.io/where-ai-benchmarks-fall-short-and-how-to-evaluate-models-instead/)，作者 Victor Botev。

[企业面临着大量的大型语言模型 (LLM)，从中进行选择。][随着 Meta 的 Llama 3.3 等新版本以及 Google 的 Gemma 和 Microsoft 的 Phi 等模型，选择从未如此多样化。][当您深入了解时，这些选择也会变得复杂。]

[对于希望利用 LLM、聊天机器人和 Agentic 系统的企业来说，挑战在于评估哪种模型符合其独特的需求，从而消除传统基准和表面指标的干扰。]

## 标准指标的缺陷

[虽然大多数评估指标在学术上都很可靠，但它们未能考虑到企业细致入微的需求。][像 Perplexity 和 BLEU (Bilingual Evaluation Understudy) 这样的工具通常用于研究中，以衡量预测准确性或与参考文本的一致性。][然而，它们对企业的实际效用是有限的。]

[以 Perplexity 为例。][虽然它旨在评估模型预测样本文本的能力，但它很少说明该模型在处理行业特定术语、解释复杂关系或为专家领域提供可操作的见解方面的能力。][同样，BLEU 最初是为机器翻译开发的，它通常会奖励模型严格遵守参考输出。][这可能会阻碍动态响应至关重要的领域的创造性和灵活性。][在 BLEU 上得分很高的聊天机器人可能会严格遵循预定义的脚本，但无法有效地处理细致入微的客户查询。]

[企业经常发现自己对那些在纸面上应该表现良好的模型感到失望，因为它们在这些指标方面表现出色。][但在现实中，这些模型在应用于现实世界的挑战时会显得不足。]

## 合成数据问题

[另一个重大障碍源于许多开源模型对合成训练数据的依赖](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)。[合成数据集通常由广泛使用的[大型语言模型](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) (LLM)（如 GPT-4）生成，从而能够加快开发周期，但可能会引入系统性偏差。][如果 GPT-4 的输出无法掌握法律文本的细微差别，那么在这些输出上训练的模型也可能无法捕捉到这些复杂性。]

[这种对合成数据的依赖会产生反馈循环的风险，即在这些数据集上训练的模型会模仿原始生成器的模式和偏差，而不是发展真正的理解。][通过使用 LLM-as-a-judge 功能会加剧这个问题，因为这种准确性评估方法会强化[许多 LLM-as-a-judge 模型](https://thenewstack.io/the-future-of-ai-and-travel-relies-on-synthetic-data/)所训练的合成数据中的偏差。]

[企业可能会错误地信任这些基于表面上强大的评估分数的模型，但后来才发现它们缺乏专业任务所需的深度。][对于大多数企业来说，[解决方案在于使用特定领域的数据微调模型](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)。][在定制数据集上训练的模型可以在专业任务中表现出大大提高的性能。][然而，微调需要大量的资源，并且需要[访问高质量的数据](https://thenewstack.io/a-look-at-datastaxs-ai-and-push-cache-for-data-access-at-scale/)]，这使得它成为许多组织具有挑战性但必要的步骤。

## 上下文敏感性

[不同的模型在上下文敏感性方面表现出不同的优势和劣势，这是业务应用程序的一个关键因素。][例如，[Meta 的 Llama 模型](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)擅长在长时间的交互中保持上下文理解。][它们非常适合需要扩展推理的用例，例如法律或医学分析。]
相比之下，[Google 的 Gemma 模型](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/) 在通用任务中表现出色，但在需要深入的、特定领域专业知识的应用程序中表现不佳。同样，虽然 Microsoft 的 Phi 模型在创造性和探索性任务中表现出色，但有时会偏离严格的指令。这在某些情况下可能是一种优势，但在监管合规性至关重要的行业中也可能是一种负担。为了准确评估每个模型的价值，任何评估框架都必须考虑每个模型的细微差别和倾向。

## 开发有效的评估框架

还应根据反映组织特定用例和能力的场景来评估模型。例如，金融机构可能会优先测试模型分析监管文件的能力，确保它可以处理 [合规性文件中常见的密集、结构化的语言](https://thenewstack.io/building-privacy-aware-ai-software-with-vector-databases/)。同样，医疗保健提供商可能需要专注于模型解释临床笔记的能力，这通常需要理解医学术语和患者特定的背景信息。定制评估场景以 [与这些实际应用保持一致，确保所选模型](https://thenewstack.io/ai-alignment-in-practice-what-it-means-and-how-to-get-it/) 为具有深厚领域专业知识的用户提供有意义的结果。

组织应避免在测试过程中过度依赖合成数据。相反，他们应该采取平衡的方法，使用真实世界和特定领域的数据集混合。这种方法有助于发现可能被忽视的潜在偏差，并确保 [模型可以管理实际业务的复杂性和可变性](https://thenewstack.io/apis-are-driving-new-business-models-and-unlocking-revenue-streams/) 环境。真实世界的 [数据可以更准确地反映模型在实践中面临的](https://thenewstack.io/data-unions-offer-a-new-model-for-user-data/) 挑战，从而带来更好的长期性能和可靠性。

部署后，应 [持续监控模型性能](https://thenewstack.io/linux-deploy-the-netdata-server-performance-monitor/)，以识别和解决与预期行为的任何偏差。生产环境中的真实世界测试可以为模型如何适应动态条件提供宝贵的见解。通过定期审查输出和性能指标，组织可以进行迭代改进并完善其 AI 系统，确保它们与不断发展的业务需求保持一致。

最后，检索增强生成 (RAG) 技术在业务环境中特别有益，[通过整合外部知识来提高模型输出的可靠性](https://thenewstack.io/5-ways-ai-improves-knowledge-management/)。评估模型将此外部数据整合到其响应中的能力对于理解其实用性至关重要。在上下文评估中的出色表现可以让人放心，该模型可以有效地适应复杂、信息丰富的场景，并提供与特定业务需求的细微差别相一致的输出。

2025 年，各组织将越来越多地寻求从他们投入巨资的模型中获得价值。信任输出的准确性并拥有足够的专业知识将是这里的关键。企业必须谨慎而精确地进行模型评估。公开可用的基准可能提供一个起点。然而，真正的成功需要一种更细致的策略，优先考虑特定领域的需求、多样化的数据测试以及对上下文敏感性的深刻理解。
