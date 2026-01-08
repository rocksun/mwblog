<!--
title: AI试点项目为何频频折戟？揭秘破局制胜之道
cover: https://cdn.thenewstack.io/media/2026/01/c7439fa9-why-so-many-ai-pilots-fail.jpg
summary: AI项目失败常因安全摩擦、工作流孤立、可观测性不足和成本高昂。成功关键在于初期良好设置、多元团队、全栈可观测及持续监控。
-->

AI项目失败常因安全摩擦、工作流孤立、可观测性不足和成本高昂。成功关键在于初期良好设置、多元团队、全栈可观测及持续监控。

> 译自：[Why So Many AI Pilots Fail and How To Beat the Odds](https://thenewstack.io/why-so-many-ai-pilots-fail-and-how-to-beat-the-odds/)
> 
> 作者：Julie Banfield

2025年中期，一份广为宣传的报告称，几乎所有AI试点项目都失败了。尽管围绕报告的失败率存在一些[争议](https://thenewstack.io/how-mits-project-nanda-aims-to-decentralize-ai-agents/)，但有些[AI项目成功](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436665742;dc_trk_aid=629928261;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)而另一些从未超出试点阶段，其原因显而易见。

根据我的经验，AI项目成败的关键，很大程度上取决于它从一开始就如何设置，以识别和解决可能阻碍成功的重大运营挑战。

## **理想世界**

设想一下开发AI应用的理想环境是怎样的：你将拥有丰富的资源，首先是一个专门的、多元化的、完整的、无竖井的团队，足以试点、开发和发布一个AI应用。

从一开始，你就会[优化可观测性](https://thenewstack.io/how-can-we-solve-observabilitys-data-capture-and-spending-problem/)，以便持续监控整个系统。你还会与安全团队协作，建立安全检查和制衡机制。

你会确保所有工作都在一个流水线中运行，并且每个新的AI项目都通过相同的流水线，从而实现可重复性，并更容易地适应为保护应用及其用户而设置的任何护栏。

在这个理想世界中，你将拥有所需的一切，帮助你在工作流程差距成为问题之前识别并弥补它们。开发过程将不再被停止/启动的关卡所阻碍；它将成为一个持续的循环，从试点到开发再到生产，使你的AI产品能够更快地推出。

听起来很田园诗般，对吧？但在现实世界中，你能将这些付诸实践吗？

## **开发AI软件的常见挑战**

开发和部署AI软件的团队面临巨大挑战，尤其是在从内部测试转向应用生产和扩展时。由于AI本质上是概率性的，开发者无法考虑到所有可能的边缘情况。引入多样化的外部数据集和变量常常导致AI软件“崩溃”。

无论是开发基于聊天的AI系统、在幕后运行的代理、算法还是高级分析工具，应用程序都会在不同数据集中寻找模式并建立关联。在基于聊天的系统中，AI将自然语言转换为机器可读的格式进行分析，然后将结果翻译回人类用户。

标准的软件开发生命周期（经典的“测试、重复和构建”[DevOps循环](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.437165523;dc_trk_aid=629929182;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)）在AI系统中会[更加复杂](https://thenewstack.io/how-ai-is-reshaping-the-software-development-life-cycle/)。这部分是由于新的AI驱动的需求，例如数据准备、模型审计、性能测试和模型再训练。

## **安全摩擦如何减缓交付**

开发AI的一个主要障碍是安全摩擦，这主要源于对AI或第三方可能如何使用其数据的不信任。公司希望确保AI没有使用他们的数据进行训练，并且他们的数据不会被窃取或存储在AI使用的外部服务器上。

为了管理这些风险，公司实施了许多安全护栏，以防止AI被用于恶意目的，例如窃取数据或引入偏见。然而，将AI产品通过这些广泛的护栏和检查点所需的时间减缓了整个过程。由于技术发展迅速，AI产品在获得批准时可能已经过时。

企业尝试防止数据窃取的一种方法是建立内部[AI政策](https://thenewstack.io/how-to-create-an-effective-ai-usage-policy)，限制第三方AI工具的使用。许多企业尝试为员工构建和维护（并频繁再训练）等效的内部工具，但可能使用性能较低的模型。但如果这些工具无法满足用户需求，“影子AI”（即员工掩盖公司数据以便使用被禁止的外部系统）无论如何都会悄悄进入企业。

> 团队就像一位家长，设定界限并利用自动化引导AI在其从环境中学习时回到预定路径。

遵守不同的监管和治理要求是另一个潜在障碍。从要求在欧盟生成的数据必须留在该区域的数据主权规则，到遵守像欧盟AI法案这样的严格法规，拥有全球业务的公司可能需要为不同区域创建不同的工作流程。

## **工作流差距为何破坏AI自动化**

许多AI开发工作流程是高度竖井化的。团队成员分散，包括前端、后端和数据工程师，以及数据科学家、AI工程师和研究人员。我见过AI和数据科学团队构建模型后，“一扔了之”给开发团队进行产品集成，然后转向下一个项目。

然而，随着模型的漂移和数据的变化，AI系统可能会朝着错误的方向发展。例如，与传统的静态软件不同，AI是有机变化的；它会随着学习而改变和演进。这可能导致意想不到的行为，例如AI决定将用户界面（UI）按钮移动到界面的右下角，或者在尝试利用新知识提高性能时破坏既有的自动化。

解决这些工作流差距的一个方法是创建一个新型团队，通过收集[模型漂移](https://thenewstack.io/the-engineers-guide-to-controlling-configuration-drift/)、置信区间和用户反馈等可观测性指标来持续维护和监控模型。在需要时，该团队会将模型拉回、再训练，甚至在模型退化严重时将其移除。团队就像一位家长，设定界限并利用自动化引导AI在其从环境中学习时回到预定路径。

## **AI系统可观测性不足的风险**

可观测性对于管理和维护复杂的AI系统至关重要。你关注的可观测性指标可能因AI应用的类型而异。

对于聊天机器人，关键指标包括：

*   **Token（令牌）：** 监控输入和输出令牌可以让你跟踪运营成本。
*   **用户成功率：** 这评估了答案对用户有多大帮助。用户能否利用回复完成任务？还是必须继续提问才能获得正确信息？
*   **幻觉率：** 大型语言模型（LLM）是否会提供不正确答案，即使它确信自己的答案是正确的？如果是，这种情况何时、何地以及多久发生一次？
*   **延迟：** 监控系统返回响应所需的时间至关重要，因为过多的延迟会导致用户取消操作。

对于预测模型，你需要衡量：

*   **置信水平：** 监控模型的预测置信分数（例如，90%）将评估其可靠性。
*   **模型漂移：** 定期根据原始训练数据的“基本真相”进行再测试，将显示置信水平是否正在下降，这表明模型准确性正在降低。
*   **反馈循环：** 如果预测失败，结果是否会被反馈回模型进行再训练，并调整导致错误结果的变量？

## **了解成本和基础设施限制**

运行[AI的成本](https://thenewstack.io/finops-and-ai-a-winning-strategy-for-cost-efficient-growth/)非常高。而由于不受控制的云计算、AI技能招聘或培训以及[模型膨胀](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436668922;dc_trk_aid=629927463;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)等因素，成本可能会飙升。

> 如果AI响应需要五分钟，那么用户自己完成任务或使用传统自动化可能会更快。

基础设施是另一个限制因素。在本地和[气隙环境](https://thenewstack.io/deploying-ai-in-air-gapped-environments-what-it-really-takes/)中运营的公司必须自行采购GPU。由于使用量通常按用户计算，扩展到拥有1000名员工的组织会迅速变得昂贵。解决方案包括使用在[更少GPU](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436822571;dc_trk_aid=629929521;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)上运行的较小型模型（如Mistral Small），或复杂的[虚拟LLM](https://www.redhat.com/en/topics/ai/what-is-vllm)技术来优化并行处理。

另外，公司可以使用Google的Vertex AI、IBM的watsonx或Amazon Bedrock等云基础设施，依靠提供商管理GPU，并按令牌支付[基于消耗的费用](https://youtu.be/Nism4CK2nqQ?si=Fq4krtHiGiAXrdVy)。

大多数AI应用似乎都依赖少数主要AI参与者（例如OpenAI或Anthropic）提供其底层推理堆栈，这限制了你对定价的控制能力。

你还必须不断应对不断上涨的技术成本和用户期望——如果AI响应需要五分钟，那么用户自己完成任务或使用传统自动化可能会更快。

## **现实世界中的AI试点项目**

我在引言中描述的理想世界，即拥有几乎无限资源来开发AI应用的世界，是难以实现的。但这并不意味着你无法将其中一些付诸实践，以克服现实世界的局限。

成功的核心是[全栈可观测性](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436822574;dc_trk_aid=629758844;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)——由代理AI驱动，持续监控系统，了解正在发生什么，并在问题出现之前纠正它们。如需更多见解，请获取[DevOps团队全栈可观测性指南](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.436822355;dc_trk_aid=629928258;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)。