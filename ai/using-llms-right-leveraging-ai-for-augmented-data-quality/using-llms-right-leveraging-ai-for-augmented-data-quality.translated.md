# 正确使用 LLM：利用 AI 增强数据质量

![Featued image for: Using LLMs Right: Leveraging AI for Augmented Data Quality](https://cdn.thenewstack.io/media/2025/05/27e80697-mohammad-rahmani-1bnqvgzuy0u-unsplash-1024x683.jpg)

[Mohammad Rahmani](https://unsplash.com/@afgprogrammer?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/black-laptop-computer-turned-on-beside-black-ceramic-mug-1bNQVGzuy0U?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)上。

数据质量已经从“锦上添花”发展成为数据运营中必不可少的，在某些情况下甚至是任务关键的部分。当 AI 开始受到关注时，许多数据治理和数据科学负责人看到了未来的趋势。竞争环境正在变得公平，那些能够正确利用其数据的人将通过新的用例获胜。对数据质量投资不足的公司正在努力跟上。

最初，AI 被视为一种灵丹妙药，有望自动化复杂流程并毫不费力地处理大量数据。然而，现在已经很清楚，如果没有战略框架，AI 可能会像它带来的好处一样带来问题。

简而言之，似乎我们可以通过规模来克服“垃圾进，垃圾出”的经典问题。然而，最近最大模型的放缓表明存在限制。训练数据的量至关重要，但数据质量正迅速成为一个差异化因素。

## 现代数据栈中的数据质量

几十年来，组织一直在运行数据质量程序。指南、最佳实践和专家将告诉您如何编写数据质量规则、部署它们以及确定数据栈中不同部分的优先级。所以，这应该很容易，对吧？

不幸的是，现代数据环境绝非简单。十年前，当每家公司都有一个中央企业数据仓库或数据库以及几个互连系统时，有效的方法现在已经无法扩展。

企业必须处理包含数百或数千个不同数据系统的数据环境，而不是处理几个系统和数据格式。虽然可以将处理能力提高到 PB 级的技术是可用的（如果你有足够的钱），但最近对数据民主化的推动意味着数据复杂性即将爆发。

这是一个被广泛认可的问题。Gartner 甚至将其数据质量解决方案的魔力象限重新分类为[增强数据质量解决方案](https://www.gartner.com/en/documents/6246519)，增加了对自动化和规模的关注。

未来的趋势已经很明显。要赢得 AI 竞赛，您必须重新思考如何处理数据质量。

## AI 会修复……AI 吗？

在过去，为了[管理日益增长的复杂性](https://thenewstack.io/managing-complexity-and-avoiding-chaos-in-digital-operations/)，您会雇用更多的人来照顾更多的系统。这种方法已经使用了多年，并导致整个部门的数据工程师编写数据质量规则、配置和报告。这种方法不再具有可扩展性，但幸运的是，现代 LLM [革命恰逢其时](https://thenewstack.io/2024-streaming-roadmap-navigating-the-real-time-revolution/)。

考虑以下用例。ChatGPT 已被用于修复来自各种[应用程序的用户交互数据库中的数据质量问题，以准备用于 AI](https://thenewstack.io/real-time-ai-apps-using-apache-flink-for-model-inference/)模型，该模型将提供个性化推荐。它展示了我们如何使用 AI 来修复 AI 的数据。

在这个例子中，我们只需要每天在新数据进来时运行这个请求，并在我们的其他系统上运行它，覆盖各种数据源和各种数据量……

您可能已经看到了这里的问题，而且它不是孤立的。

考虑一下依赖 LLM 来自动化复杂的数据清理，而没有适当的监督，这通常[会导致错误](https://thenewstack.io/red-hat-human-error-a-leading-cause-of-kubernetes-security-mishaps/)和不一致，这些错误和不一致只会在大规模时显现出来。即使是上面的例子在特定的用例中也能很好地工作，但[在规模、一致性和幻觉方面会遇到困难](https://thenewstack.io/case-study-how-lacework-scaled-data-streaming-with-redpanda/)。

## AI 会修复 AI……但事情没那么简单

AI 无法仅凭其当前形式的原始能力进行扩展。您必须有意识地在哪里以及如何使用它。在数千个来源和 PB 级数据上运行基于 LLM 的 AI 处理是不可行的。但是，我们知道如何解决不断增长的数据量，因为有大数据方法几乎可以在任何规模上运行；它们只需要正确配置。那么，如果我们问 ChatGPT 一个不同的问题呢？

在这种情况下，该模型被要求编写数据质量规则。它没有收到完整的数据集，而是只收到一个样本，并被要求提出要在数据之上运行的规则。
模型提出的规则是可以在可预测的结果下重复使用的逻辑示例。如果使用合适的处理技术，这些规则可以扩展到任何数据大小和来源。

只有当数据源或配置文件发生显著变化时，才需要运行此提示。您可以将此新生成的数据质量规则列表用作规则映射的输入，将其应用于不同的数据集，而无需重新生成规则逻辑。这比要求 AI 检测数据中的问题更具扩展性。

当然，也存在一些注意事项。可预测性和幻觉问题并未消除，并且为大型数据环境扩展它也会带来一些编排方面的挑战。

## 有意地使用 AI

正确应用 LLM 进行数据质量管理是一项战略要务。LLM 具有彻底改变数据质量实践的巨大潜力，但前提是必须精确且有目的地使用它们。

组织[必须将 AI 作为](https://thenewstack.io/building-privacy-aware-ai-software-with-vector-databases/)更广泛、经过深思熟虑的数据治理战略的一部分来参与。要成功地将 LLM 集成到数据质量流程中，需要清楚地了解这些模型的功能以及您的数据环境的独特挑战。

展望未来，问题仍然存在：您将如何调整您的数据质量策略，以负责任且有效地利用 AI 的全部潜力？

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。