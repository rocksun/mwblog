
<!--
title: AI辅助编码、开源及更多领域的未来展望
cover: https://cdn.thenewstack.io/media/2023/12/95c34a5e-year-forecast-1.png
-->

The New Stack 联系了120多位行业专家，就软件开发领域的一些热门话题进行了探讨。以下是他们的观点。

> 译自 [What's Ahead for AI-Assisted Coding, Open Source and More](https://thenewstack.io/whats-ahead-for-ai-assisted-coding-open-source-and-more/)，作者 Lawrence E Hecht。

我们努力掌握读者关注的趋势。但在回顾去年的[数据研究](https://thenewstack.io/what-2024s-data-told-us-about-how-developers-work-now/)和许多2025年的预测后，我们仍然有一些问题没有答案。

为了更好地了解未来的发展方向，The New Stack的编辑们确定了14个需要解答的问题。然后，我们找到了120多位行业专家，帮助我们了解开源、开发者对AI的使用以及IT基础设施的未来。

30多位专家做出了回应，平均每位专家对他们最了解的主题提供了四个深入的预测。其中一些答案已在The New Stack上报道。在这篇文章中，我们首先重点介绍最重要的结论。然后，重点介绍具体的问题和答案，以详细阐述这些结论。

**开源与竞争力**

- [安全和维护人员的时间是开源面临的主要威胁](https://thenewstack.io/open-source-in-2025-strap-in-disruption-straight-ahead/)。
- 预计在未维护的组件上将取得渐进式进展。
- 开源可能是对抗开发者平台中心化控制的最有效方法。
- 大平台公司是否会在AI技术栈的竞争中胜出，目前尚无共识。

**AI代理**

- 尽管长期以来人们对此持乐观态度，但人们普遍担心许多内部
[AI代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)项目将在2025年被放弃。

**AI对开发者流程的影响**

- AI辅助开发将挑战开发者审查代码质量并将其工具集成到其工作流程中。
- 开发人员在2025年手动测试软件所花费的时间与24年大致相同。

**云和数据基础设施**

- 专家们认为，工作负载迁移到私有云和本地云的速度不会超过迁移到公共云的速度。
- 组织从批处理迁移到流处理的过程中将克服哪些障碍，目前尚无共识。

## 开源与竞争力

**考虑到普通的企业应用程序组件，到2025年，未维护或过时的开源组件的比例将增加还是减少？增加或减少的百分比是多少？**

**预计在未维护的组件上将取得渐进式进展**。回答这个问题的六位专家中有五位认为，到2025年，开源且未维护的组件比例将会下降，其中两位认为下降幅度约为10%。AI和DevOps工具的持续采用被认为是改进的原因。以下是他们的一些说法：

- “这种下降将由对软件供应链安全的认识增强所驱动，这受到了[Log4Shell](https://thenewstack.io/burning-down-the-house-quantifying-the-impact-of-log4j/)等事件的刺激，以及[Snyk](https://thenewstack.io/spotify-taps-snyk-for-security-testing-automation/)等自动化依赖项更新工具的广泛采用。对[软件物料清单(SBOM)](https://thenewstack.io/rust-will-explode-sboms-will-be-duds-open-source-predictions/)的监管要求以及[npm](https://thenewstack.io/npm-to-adopt-sigstore-for-software-supply-chain-security/)等平台上改进的生态系统治理也在识别和解决不受支持的组件方面发挥着至关重要的作用……总的来说，积极主动地维护依赖项卫生状况可能会在减少企业系统中过时的组件方面产生可观的收益。” — [Eran Kinsbruner](https://www.linkedin.com/in/erankinsbruner/)，[Lightrun](https://lightrun.com/?utm_content=inline+mention)产品营销主管

- “希望依赖项管理和更新自动化的采用增加，以及改进持续集成和持续部署等DevOps实践，能够帮助企业应用程序在2025年平均减少5-10%的过时组件。然而，这种减少将取决于技术债务和资源约束的程度，以及各个企业的优先级。” — [Kat Gaines](https://www.linkedin.com/in/katgaines/)，[PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention)开发者关系和社区高级经理

**您认为到2025年，对抗开发者平台中心化控制最成功的努力是什么？**

**开源可能是对抗开发者平台中心化控制的最有效方式**。在回答这个问题的八位专家中，有三位认为开发者平台的中心化控制是对抗其中心化的最佳方式。其他人则看到迹象表明，开源、AI辅助编码工具正在有效地与大型平台公司竞争。

- “开源方法应该自动减少对开发者平台的中心化控制，因为可以fork项目或自己构建所需内容。然而，实际上，由于与保持社区团结相比，这是一个耗时且可能浪费资源的过程，因此很多人不愿意fork。如果社区没有必要，他们就不会fork。” — Kate Obiidykhat，云原生产品和服务解决方案营销经理，Percona
- “我认为，随着Cursor AI（将用户从GitHub Copilot转移）、Surfer/Codium IDE、用于全栈应用程序的Bolt.new，甚至允许基于共享应用程序（如Xcode）编写Swift代码的桌面ChatGPT应用程序的新功能的兴起，我们已经看到了开发者平台控制权的去中心化。” — Madhukar Kumar，SingleStore首席营销官

**开发者会在2025年迁移到大型平台公司构建的AI栈吗？**

**关于大型平台公司是否会在AI栈之争中获胜，目前尚无共识**。一些专家认为，未来专业公司可以与大型平台公司竞争。从长远来看，获得广泛数据源的访问权限可能会让大型平台公司占据优势。

- “数据是AI的生命线。为了构建有意义的AI驱动型应用程序，开发者必须直接访问为其提供支持的相关企业数据。当开发者迁移到平台公司，他们的AI栈和数据共存于同一位置时，他们可以释放数据的全部潜力，防止与跨平台移动数据相关的冗余治理风险，并加快应用程序的价值实现时间。” — Jeff Hollen，Snowflake Snowpark、生态系统和开发者平台产品总监
- “我认为开发者会倾向于那些能够帮助他们更快地构建应用程序和解决方案，并且易于使用的工具。组织希望AI栈能够将生产力和效率与一流的安全性和数据隐私相结合。能够获得开发者信任的工具将是那些能够建议高质量代码和适合其代码开发流程的编辑器的工具……开发者现在正在评估这些AI技术将如何为他们带来价值。少数大型平台公司通过早期推出获得了市场份额和影响力。我认为小型公司将通过为开发者带来有针对性的价值而获得发展。” — Bhawna Singh，Okta客户身份CTO
- “我认为AI支持许多不同的利基用例，我们将看到开发者同时使用大型平台提供的功能以及解决非常具体问题的工具。例如，开发团队可能会利用GitHub Copilot来帮助完成日常编码任务，但会使用不同的AI栈来执行代码审查、生成测试或管理基础设施即代码。我目前正在构建这样一个工具Blackbird，它使用AI来生成和编辑OpenAPI规范。大型平台将涵盖大多数常见用例，有些可能会扩展到利基领域。但作为一名开发者，我认为我们将开始将一些替代AI栈组合在一起，这些栈将能够以更低的价格更有效地解决利基问题。” — Matt Voget，Ambassador Labs技术总监

## AI代理

**到2025年底，至少一半在2024年内部构建的AI代理项目会被放弃吗？**

**尽管长期以来人们对此持乐观态度，但我们的调查参与者表示，人们普遍担心许多内部AI代理项目将在2025年被放弃**。在回答这个问题的14位专家中，有5位专家预计至少一半的2024年项目将被放弃，两位专家不同意这一前提。其余七位回答这个问题的专家承认，他们不确定结果会如何。

## AI对开发流程的影响

**2025年，依赖于AI辅助软件开发的开发人员将面临哪些最大的挑战？这些挑战将如何影响GitHub Copilot用户？**

**AI辅助开发将挑战开发人员审查生成的代码质量并将工具集成到他们的工作流程中。** 许多回答这个问题的17位专家都表示担心，AI生成的代码数量增加实际上增加了开发人员的工作量，因为它需要人工审查。一些专家担心，经验不足的开发人员将无法识别AI何时输出错误代码。安全和信任是其他提到的挑战。

- 对于依赖它的开发人员来说，需要问的问题是，如果它被拿走，他们会非常失望、有点失望还是不会失望？今年早些时候对我们工程师进行的一项非正式调查显示，在28名受访者（我们积极参与AI技术实验的工程师）中，只有两人如果因为预算原因而被裁掉会非常失望。我的结论是，这些工具在某种程度上是有用的，但并没有证明它们宝贵到如果因为预算原因而被裁掉，工程师们会强烈反对的程度。——Octopus Deploy高级副总裁Colin Bowern
- 由于无法识别AI代码中的缺陷，代码质量下降可能会成为一个问题。目前，经验丰富的开发人员可以从AI辅助软件开发中获得显著的好处，因为他们有经验可以识别AI代码何时不正确。随着AI辅助编码的继续，查找AI错误的技能下降的速度可能会超过AI在生成无错误代码方面的改进。—— Scott Wheeler 是 Asperitas 的云实践负责人。
- “虽然像GitHub Copilot这样的AI编程助手被宣传为通用的生产力工具，但它们不成比例地增强了经验丰富的开发人员的能力，同时可能会阻碍新来者的学习过程。高级开发人员凭借其对系统设计、架构模式和技术权衡的深刻理解，可以有效地‘使用AI助手的语言’。他们知道确切要问什么，能够迅速验证生成的代码，并理解实施建议解决方案的更广泛影响……而经验不足的初级开发人员则只能依赖于AI的建议。虽然这可能会增强他们需要语言无关地思考的需求，但现在看来相当乌托邦，因为人们担心从学习过程中消除失败。” —— Artem Barmin，Freshcode的联合创始人和董事会成员。

**由于自动化和人工智能技术的采用，开发人员手动测试软件的小时数会大幅下降吗？**

**到2025年，开发人员手动测试软件的时间将与2024年大致相同**。在回答这个问题的15位专家中，有7位回答“不会”，3位回答“会”，其余的则给出了更复杂的答案。




- 虽然许多组织一直专注于内部构建AI代理，但我们预计到2025年底将发生重大转变。市场预计将在2025年至2026年之间出现大量商用AI代理进入主流市场。在Kobiton，我们认识到在AI代理发展的早期阶段，内部开发仍然是可行的。然而，随着更复杂和完善的AI解决方案在商业上变得更容易获得，维护内部开发工作的成本和复杂性可能会超过其益处。因此，我们预计，2024年内部构建AI代理的大部分计划将逐步淘汰，转而采用这些先进的、随时可部署的解决方案。这种转变反映了整个行业的一个更广泛趋势，即利用专业的、市场驱动的AI工具，这些工具提供比定制的内部开发更好的性能和可扩展性。——Kobiton首席技术官Frank Moyer
- AI的本质往往使得早期的努力在相对较短的时间内变得过时，导致许多努力被放弃。我们在大型数据模型项目中已经看到了这一点，重新调整资源以继续前进可能代价高昂。——Aiven流媒体服务工程总监Josep Prat
- 较小的努力将会消亡，因为公司会意识到两件事：他们的数据比他们想象的要脏得多，需要付出巨大的努力才能清理，而且当GPT-5和Claude 4（在2025年）发布时，它们开箱即用的性能将使规模小于标准普尔500强公司的内部项目变得多余。——Cosine首席运营官Yang Li
- 新兴技术需要时间才能成熟，AI代理的使用也将经历类似的成熟曲线。成功的组织是那些采取循序渐进的步骤，逐步整合AI代理并在学习中适应的组织。期望快速获得结果的企业可能会感到厌倦并放弃他们的努力。——Komprise联合创始人兼首席运营官Krishna Subramanian
- 目前很难判断。构建AI代理的成功将取决于组织适应其API策略以支持机器与机器交互的能力。未能解决安全漏洞、可扩展性和投资回报等挑战的公司可能会放弃这些努力。然而，那些投资于设计模块化、可重用、可外部化的API并实施强大的合规框架的公司将更有可能实现可持续的AI集成并避免项目被放弃。——Postman首席执行官Abhinav Asthana
Asperitas公司云实践负责人：虽然像GitHub Copilot这样的AI编码助手被宣传为通用的生产力工具，但它们不成比例地放大了经验丰富的开发人员的能力，同时可能阻碍新手的学习过程。资深开发人员凭借其对系统设计、架构模式和技术权衡的深刻理解，可以有效地“理解”AI助手的语言。他们确切地知道需要什么，可以快速验证生成的代码，并理解实施建议解决方案的更广泛影响……经验不足的初级人员只能依赖AI的建议。虽然这可能会增强他们无需考虑语言的需要，但在考虑到消除学习过程中失败的担忧后，这似乎相当乌托邦式。——Freshcode公司联合创始人兼董事会成员


开发人员手动测试软件的时间是否会因为自动化程度的提高和AI技术的采用而大幅减少？

**2025年，开发人员手动测试软件的时间将与24年大致相同。**在回答这个问题的15位专家中，7位回答“否”，3位回答“是”，其余人则给出了更细致的答案。

- “当整体结果由于较慢的质量保证和测试来解决问题而导致微小的边际收益时，让一些开发人员指出他们生产力提高了‘10倍’是没有意义的。”——OpenUK公司CEO
- “我认为它会增加。开发人员将花费更多时间运行自定义测试和工作流程来验证他们没有编写且难以解释的代码。”——Yang Li，Cosine公司
- “自动化通常在应用于稳定且变化最小的产品时能产生最高的回报。然而，在Kobiton，我们观察到了一种意想不到的趋势：手动测试时间环比增长了22%，超过了自动化测试的17%增长。这种转变主要是由AI辅助工具促进的新应用开发速度加快所驱动的。随着这些应用程序发展得越来越快，变化的频率和程度使得全面的自动化变得不太可行。因此，对灵活的手动测试的需求增加了，以确保新功能和更新保持质量标准。这种动态强调了平衡方法的必要性，即自动化和手动测试相互补充，以适应AI技术所促进的快节奏开发环境。”——Frank Moyer，Kobiton公司
- “是的，团队将能够自动化单元测试和基于意图的功能测试的创建。这不会消除诸如用户验收测试之类的手动测试，但将有助于将这些手动测试转换为自动化测试以进行回归测试。”——Copado公司高级副总裁
- “AI正在被用来简化一些任务，例如生成测试用例，提供快速的小收益。虽然这些初步改进可以提高效率并减少人工工作量，但AI对测试基础设施的更具变革性的影响需要更长的时间才能实现。将需要付出巨大的努力来构建和采用能够替代或大幅改变现有测试框架的AI驱动型解决方案。虽然2025年用于测试的时间可能不会大幅减少，但随着这些技术成熟并更多地融入标准实践中，预计2026年将出现更明显的减少。”——Yelp公司集团技术主管
- “是与否。开发人员将能够使用AI工具完成更大的编码任务，这意味着他们将花费更少的时间重新运行他们的本地开发循环（其中一部分包括手动测试）。他们还能够快速编写自动化和单元测试，目的是防止回归并尽早发现错误。但我认为这不会减少开发人员花费在手动测试上的时间。如果有什么不同的话，AI工具允许开发人员花费更多的时间来确保他们的代码实际上解决了业务问题，因为许多样板工作都是自动完成的。这意味着可能花费在编码上的时间更少，而花费在手动测试上的时间更多。”——Matt Voget，Ambassador Labs公司


## 云和数据基础设施

**平均企业迁移到私有云和本地云的工作负载是否会多于迁移到公共云环境的工作负载？**

**专家们认为，工作负载迁移到私有云和本地云的速度不会超过迁移到公有云的速度**。在回答这个问题的15位专家中，6位回答“否”，3位回答“是”，其余的则描述了一幅混合图景，不同类型的公司和工作负载更有可能倾向于某个环境。

- “是的，有两个主要原因。首先是优化IT支出的压力越来越大。将工作负载迁移到云中的企业发现，公有云并不总是像本地云或私有云那样具有成本效益。此外，一些首席财务官怀念资本支出模型的稳定性和可预测性。第二个因素是供应商格局和产品组合的变化，例如[博通收购VMware](https://thenewstack.io/vmware-to-be-acquired-by-broadcom-in-a-61-billion-deal/)之后的变化。这些变化促使一些公司重新评估其平台战略。在某些情况下，这可能会导致将适当的工作负载迁移到公有云，但在其他情况下，我们看到组织选择替代模型，例如私有数据中心中的托管基础设施，这提供了本地模型的控制能力以及公有云的灵活性和易于维护性。”
- “企业更有可能将更多工作负载迁移到私有云和本地云，而不是迁移到公有云环境。这一趋势是由几个因素驱动的，最值得注意的是对AI基础设施建设的需求，这需要对数据资产进行完全控制，并从网络基础设施获得最大性能，避免共享或虚拟网络。”

- “到2025年，企业将越来越多地优先考虑私有云和本地云环境，作为平衡灵活性和控制性的混合解决方案的一部分。法规遵从性和成本优化将推动这种转变，因为公司寻求更好地管理数据主权并满足关键任务工作负载的需求，同时仍然利用公有云服务的敏捷性。这种转变反映了对提供灵活性和控制性的解决方案的偏好日益增强，尤其是在数据和人工智能成为业务创新的基础时。”

- “‘平均’企业（包括中型企业和长尾企业）将在2025年继续增加向公有云迁移工作负载。对于大型全球2000强企业而言，前景更加复杂。大部分行动将是迁移到公有云，但由于以下几个因素的融合，混合/私有云的采用率将显著提高：
  - [Kubernetes](https://kubernetes.io/)平台的成熟度，特别是[Red Hat OpenShift](https://www.openshift.com/try?utm_content=inline+mention)，正在获得关键规模的采用。现在出现了一种可行的替代超大规模厂商原生平台的方案。
  - 他们已经完成了许多“唾手可得”的工作负载，例如已经迁移到公有云的云原生客户参与系统。
  - 在下一阶段，大型企业开始关注关键任务后端系统，其中许多（如果不是大多数）可能对哪些内容可以流入公有云有限制。一个例子是即将淘汰的SAP ECC，这促使许多企业重新审视其ERP系统。其中许多将最终进入私有云。如上所述，虽然大部分行动仍将是公有云迁移，但越来越多的全球2000强工作负载将迁移到私有云或混合云。”
- “不。事实恰恰相反：首席信息官和首席技术官已经厌倦了本地解决方案。”Broadcom收购VMware导致许多组织寻求加快从本地部署迁移到云端的步伐。边缘和云之间计算的连续性使得组织能够充分利用其云/边缘服务的性能——这对组织自身而言几乎是不可能的。现在Kubernetes被认为是通用的控制平面，对厂商锁定的担忧正在减弱。一些规模较小（但声音很大）的组织大胆宣称要“回迁”，但这些公司远不能代表主流组织的担忧。“仅仅因为一家只有几十名员工的公司[37Signals]可以节省资金，并不意味着普通企业从回迁到本地部署中会获得任何好处。”——[Matt Butcher]，[Ferymon Technologies]联合创始人兼首席执行官
- “这取决于企业的优先事项，特别是速度和成本匹配之间的权衡。优先考虑速度的部门或组织将继续将其更多工作负载迁移到公共云环境。但是，对于稳定、资源密集型业务流程，企业可能会越来越多地考虑将其工作负载迁移到私有云或本地云以优化成本。无论目的地如何，企业都必须专注于开发在不同环境之间无缝迁移和管理工作负载的能力。”——[Rohit Choudhary]，[Acceldata]首席执行官兼联合创始人


## 数据架构

**2025年将克服哪些从批处理迁移到流处理的障碍？**

**对于在组织从批处理迁移到流处理的过程中将克服哪些障碍，目前尚无共识**。七位专家回答了这个问题，但他们更多的时间花在了解释挑战上，而不是如何克服这些挑战。也就是说，5G网络切片技术的改进、实时API和协议的标准化、向量数据库成本/复杂性的降低以及由于AI用例而导致的需求增加，都是专家们预计流处理技术采用率增长的原因。
- “5G网络切片的改进将为关键的流应用程序提供专用带宽，使流处理对于企业用例更可靠、更可预测。”——Artem Barmin, Freshcode
- “在不支持高效流插入的向量数据库中，成本和基础设施复杂性问题很常见。有些向量数据库根本不支持它。为了应对这些挑战，开发人员不得不构建和实现额外的系统来处理实时数据，这往往会导致维护多个系统时的架构复杂性……随着越来越多的企业努力克服这些挑战，我们预计Milvus的采用率将会增加，因为它旨在处理历史数据，同时还为新数据提供了一条新途径，以便对新数据的插入和搜索更高效。”——[James Luan]，[Zilliz]工程副总裁
- “我们最终将能够同时查看静态数据湖和仓库数据以及实时流数据，从而使批处理和内部应用程序成为实时应用程序，也包括面向外部的应用程序。一个典型的例子是能够在Snowflake中将像SingleStore这样的实时多模数据库作为容器运行。”——Madhukar Kumar, SingleStore
- “我们遇到的一个重大障碍是由于不同的格式、模型、API和延迟，难以实时操作来自不同来源的数据。但是，今天，我们拥有更好的工具来对动态数据进行建模，而这些工具在2025年只会得到改进。我们看到了来自[Apache Flink]和使用它们的平台的改进。一些改进围绕着实时API和协议的更好标准化，总的来说，我们看到数据网格和事件驱动架构的广泛采用，这些架构更好地支持去中心化的流处理。但是，这个问题仍然存在，而且永远都会存在需要解决的工作。”——Josep Prat, Aiven
- “数据聚合在流处理中更具挑战性，因为数据是零散到达的。像Apache Flink和[Apache Spark] Streaming这样的新兴框架正在改进有状态流处理能力，从而能够更有效地处理实时环境中的聚合和连接。”——Scott Wheeler, Asperitas

