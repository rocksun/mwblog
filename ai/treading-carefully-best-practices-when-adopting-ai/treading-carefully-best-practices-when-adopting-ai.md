<!--
title: 谨慎采用人工智能的最佳实践
cover: https://cdn.thenewstack.io/media/2023/12/4aef2fab-map-1024x364.jpg
-->

为了助力我们正确运用人工智能，以下提供几点建议，在实践使用人工智能时需谨记这些建议，以便您能够牢固掌舵，安全驾驭人工智能。

> 译自 [Treading Carefully: Best Practices When Adopting AI](https://thenewstack.io/treading-carefully-best-practices-when-adopting-ai/)，作者 Tim Banks 是Dell Technologies的首席开发者倡导者。他在技术行业拥有超过25年的经验。Tim的技术之路始于美国海军陆战队，他最初加入是为了成为一名音乐家。后来他被重新分配到航空电子学......

人类创新的普遍特征是使我们能够比以往更快地在更大规模上出错。我们可以更快地制造有缺陷的东西。我们可以开车更快。我们可以在几分钟内破坏整个自然生态系统。我们可以用一条推文破坏世界的金融稳定。我们可以通过按几个按钮消灭地球表面所有的生命。

这一认识对于认识使用新的 AI 项目的热情可能带来的灾难风险至关重要。我们距离实现真正的 AI 意识还有(希望是)一代人的时间。然而，意识的基本要素现在正在开发。主要的担忧是这些要素目前充满了偏见和错误。例如，面部识别无法区分有色人种。生成式图像 AI 在数据集中没有此类输入的情况下会产生不适当的输出。[大型语言模型](https://roadmap.sh/guides/free-resources-to-learn-llms)(LLM)会编造答案，称为“[幻觉](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)”，或产生包含已知错误的结果。

除了技术本身的缺陷之外，我们并不是总是以安全的方式使用技术。用户正在查询或数据集中输入敏感数据。用户已经开始依赖AI生成他们没有经验审核的答案。一些方面正在创建深度伪造来帮助他们进行误导性宣传。其他人正在使用深度伪造在未经被利用者知情或同意的情况下滥用他们的肖像。而且，由于这些技术的发展势头，组织正在优先考虑提高AI的采用和变现，而不是先解决这些问题。

我们还没有对AI对社会或我们周围的世界的长期影响有清晰的认识。我们还没有制定[任何监管标准](https://thenewstack.io/regulating-ai-presents-confounding-issues/)来为这些技术的创造和使用设置护栏。我们无法透明地了解某些AI模型是如何做出决定的。我们尚未对日益增长和计算复杂度更高的数据集的存储和计算需求的生态影响进行充分研究。我们还没有关于AI结果中受保护财产的包含的法规。我们还没有解决滥用AI或编造结果的责任问题。当涉及到我们当前AI努力的长期影响和结果时，我们正在闯入一个盲区。如果我们不及时踩刹车，在建立护栏之前，我们可能会看到峡谷的底部！

考虑到所有这些有效的担忧，AI正在越来越多的领域和产品中被采用，这种情况不太可能改变。有几家大型科技公司都在开展竞争性项目和产品，争相成为首选的AI。无论我们怎么努力，我们都无法抵御流入AI的资金潮流。然而，我们可以通过在实践和产品中思考选择和使用AI来驾驭这种潮流。为了帮助我们导航，这里有一些关于你的AI实践和使用的考虑，这些考虑应该可以帮助你安全地驾驭这片水域：

- **永远不要向模型或聊天机器人输入个人身份识别信息(PII)、凭据、机密或其他敏感信息**: 这应该是不言自明的，但在这方面已经发生过[事故](https://techcrunch.com/2023/09/18/microsoft-ai-researchers-accidentally-exposed-terabytes-of-internal-sensitive-data/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuYmluZy5jb20v&guce_referrer_sig=AQAAAIRYskV5-HzlnAStgfIh98yUqrOmuDKsasVWNOMDbk9x62Dl9iC_YrVcoOki-1XAFNmmZc0DcKEAavJiOPw72ruj7OerMxtxAQfrVv1K0Bd0VG7TwHIxsid3DjsYouzGcgWhGJeUSo5wgtjRcYtjLoLUhdbY48w6OP4fkpPAfRID)。信息如果公开可用就视为可以输入模型和聊天机器人。
- **使用AI照片编辑器时要谨慎**: 要意识到潜在的风险，如错误信息的传播、版权和知识产权问题以及数据隐私问题。
- **在使用AI工具提供的数据之前，一定要验证数据的准确性**: 一定要仔细检查从AI工具获得的数据，以确保其准确性。在未经验证的情况下接受一个答案的正确性可能会对您的业务产生持久影响。
- **了解AI应用程序格局**: 了解AI的不同应用，并选择最符合您需求的应用。AI领域没有供应商短缺的问题，选择困难症是真实存在的。为您的用例选择合适的供应商不是一个应该轻视的决定。
- **数据准备和管理**: 确保您使用的数据准确、相关并且是最新的。当心将自己的错误输入模型和[数据毒化](https://www.techradar.com/news/what-is-data-poisoning-and-how-do-we-stop-it)。
- 为您的特定用例**选择合适的算法和模型**。这将避免您在建模和呈现数据时“海纳百川”。
- **AI开发服务**: 使用可靠并有良好记录的开发服务。
- **训练和评估**: 定期训练和评估AI模型，以确保它们是最新和准确的。它们是否一致地产生您想要的结果?错误出现的频率如何以及这些错误的性质是什么?
- **部署和可扩展性**: 确保AI模型可以有效和可持续地部署和扩展。收集有关可持续性和建模以及AI使用的环境影响的指标，这将帮助您对其使用做出更好的决定。
- **伦理和隐私考量**: 确保AI模型是道德的并尊重用户隐私。虽然这很模糊，但如果您的组织为[AI伦理](https://www.dell.com/content/dam/documents-and-videos/dv1/en/solutions/business-solutions/briefs-summaries/principles-for-ethical-ai.pdf)建立原则来指导您的实践会有所帮助。

AI来势汹汹，我们有责任以一种安全、道德和可持续的方式将其融入我们的世界。
