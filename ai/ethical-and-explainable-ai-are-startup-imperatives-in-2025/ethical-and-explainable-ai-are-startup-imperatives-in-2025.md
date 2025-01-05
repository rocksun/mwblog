
<!--
title: 2025年，道德和可解释AI是创业的当务之急
cover: https://cdn.thenewstack.io/media/2025/01/908499ff-artem-sapegin-b18trxc8upq-unsplash-1-scaled.jpg
-->

企业正在拥抱生成式 AI，但必须解决治理挑战，以确保其使用合乎道德和可解释。

> 译自 [Ethical and Explainable AI Are Startup Imperatives in 2025](https://thenewstack.io/ethical-and-explainable-ai-are-startup-imperatives-in-2025/)，作者 Octavian Tanase。

2024年，生成式AI渗透到工作场所，企业将其用于各种目的，从内部生产力工具到面向客户的产品和服务。

然而，许多人担心如何安全、合规和道德地使用这些技术。2025年，AI治理将成为讨论的主题，特别是关于道德和可解释AI。

许多公司仍然对生成式AI比较陌生，并且对数据安全和隐私问题感到担忧，特别是关于公共大型语言模型（LLM），这可能会暴露敏感数据。因此，企业选择通过基于现有LLM（通常是开源模型）构建、使用其专有数据对其进行微调、使用检索增强生成（RAG），然后将其部署到其私有数据中心来保护其数据。

对于供应商来说，这种情况是基本要求，但现在越来越多的公司正在管理这些AI模型，他们正面临着一些AI治理问题。为了提供用户信任并可以自信地使用的产品和服务，组织需要制定可解释和道德AI的路线图。

方法如下：

## 可解释AI

生成式AI以其分析、解释信息以及回答请求或提示的能力而闻名。通过训练[大型数据集](https://thenewstack.io/processing-large-data-sets-in-fine-grained-parallel-streams-with-sql/), LLM学习识别模式并理解底层信息。然后，当给出提示时，模型可以根据其学习到的内容生成答案。

正因为如此，一些LLM如何提供信息和回答查询，即使对于一些创建这些模型的人来说也不清楚。然而，微调其模型的公司希望从其LLM获得更高的透明度。

可解释AI由使AI对人类透明、易懂和值得信赖的方法组成，对于部署[生成式AI](https://thenewstack.io/ebooks/generative-ai/)的任何企业来说，这都是一个越来越重要的要求。随着AI技术的速度和能力不断提高，它将被整合到更多日常产品中，并能够完成以前似乎不可能的事情。为了应对这一显著的转变，人们希望了解这些AI产品是如何得出答案或决策的，它们的影响以及它们潜在的偏差或弱点。一旦人们了解了这一点，他们就会像信任其他任何新兴技术一样信任它们。

公司提供可解释AI的一种方法是随时提供AI系统的可审计性。随着生成式AI的使用，审计技术系统的复杂性[呈指数级增长](https://www.thomsonreuters.com/en-us/posts/technology/auditing-ai-transparency/)。然而，根据IEEE的说法，负责任的组织需要能够审计其LLM，以便“始终能够理解系统为何以及如何以某种[方式](https://ieeexplore.ieee.org/document/9726144/references#references)运行”。这包括AI模型的文档、训练数据的来源、算法的文档和评估指标。这最终可能导致为LLM构建一个[时间机器](https://support.apple.com/en-us/104984)，有人可以进入，回到过去，并展示，例如，他们当时对LLM进行了哪些信息的微调。

这种数字纸质追踪可能出于多种原因需要。公司正在高度监管的行业（如医疗保健、金融和法律）中使用AI，监管机构或公司的治理或法律委员会可能要求提供审计。

关于合规性，监管机构越来越关注企业的AI使用情况。立法正在迅速发展，从[欧盟的AI法案](https://artificialintelligenceact.eu/)（于2024年7月正式生效）到2022年美国[AI权利法案蓝图](https://www.whitehouse.gov/ostp/ai-bill-of-rights/)和加利福尼亚州最近通过的关于[生成式AI透明度](https://www.dlapiper.com/en/insights/publications/2024/10/california-enacts-sweeping-new-ai-regulation)的AB 2013法案。公司正在依靠新兴的技术工具来帮助他们跟踪和管理AI合规性。
数据被注入到向量数据库中的LLM中，该数据库将信息转换为LLM可用的参数。能够审核此过程并在每次注入新信息时拍摄向量数据库虚拟快照的技术合作伙伴将非常有帮助。这提供了可追溯性，这是寻求降低风险的企业的一项关键增值服务。


随着越来越多的公司使用生成式AI，他们将需要对以下问题给出可靠、可验证和可证明的答案：

- 你是如何得出这个结论的？
- 你是如何生成这份文件的？
- 你拥有该生成式AI生成的IP的权利吗？
- 你是否侵犯了某人的IP？

## 道德AI

除了可解释的AI之外，道德AI的相关领域还确保组织的AI系统遵守透明度、隐私、公平性和问责制等基本原则。


在隐私方面，[算法会摄取海量数据](https://thenewstack.io/open-source-library-taipy-turns-ai-algorithms-data-into-web-apps/)来运行AI程序，其中一些数据可能是个人身份信息。因此，根据2022年白宫[《人工智能权利法案蓝图》](https://www.whitehouse.gov/ostp/ai-bill-of-rights/#privacy)的非约束性规定，公司应努力在其产品中遵循数据最小化协议。他们还应尽可能匿名化个人数据。但是，即使是匿名化后的数据，AI也可能通过组合多个数据源来推断个人的身份。个人信息的泄露可能会导致隐私侵犯，因此，使用强大的网络安全协议保护数据也是必要的。


偏差可以通过多种方式引入AI系统。这可能包括偏向特定群体或观点的训练数据——例如，只有男性。算法可以根据其设计方式以及它们在决策中关注的内容来引入偏差。这可能导致抵押贷款申请[偏差](https://apnews.com/article/lifestyle-technology-business-race-and-ethnicity-racial-injustice-b920d945a6a13db1e1aee44d91475205)或[医疗保健](https://www.npr.org/sections/health-shots/2023/06/06/1180314219/artificial-intelligence-racial-bias-health-care)诊断或治疗偏差。公司有责任确保数据集以及使用这些数据集的算法和AI工具准确反映它们将服务的群体。AI工具用于从医疗保健到抵押贷款审批等关键服务，这可能会对最终客户造成严重后果，因此公司必须经常检查其算法和模型，以确保不包含对特定群体的偏见。


公司需要在其组织结构中建立问责制，以提供符合道德且无偏见的AI。公司应明确定义管理AI的角色和责任，以避免混淆或错误。负责人可能包括首席法律官、首席技术官或其他负责诚信、道德、合规或数据的管理人员。一些公司还在创建AI伦理委员会。对于关键的业务或面向客户的决策，人工监督也是必要的。这确保了不会忽视重要的决策，也不会错误地将其委托给AI。


所有这些考虑都基于广泛的AI伦理。强大的AI伦理框架或政策有助于以原则和标准指导决策，确保一致性、可靠性、透明度和可解释性。
