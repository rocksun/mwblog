<!--
title: Python疾速演进，赋能现代企业AI
cover: https://cdn.thenewstack.io/media/2025/11/c3117c46-daniil-komov-ljsttwfiqqi-unsplash-scaled.jpg
summary: Python是AI基石，因其易学和扩展性。企业面临安全、性能、可审计和部署挑战。需加强治理、追踪使用、提升技能并提供安全方案，以化解风险，确保AI成功。
-->

Python是AI基石，因其易学和扩展性。企业面临安全、性能、可审计和部署挑战。需加强治理、追踪使用、提升技能并提供安全方案，以化解风险，确保AI成功。

> 译自：[Python Is Quickly Evolving To Meet Modern Enterprise AI Needs](https://thenewstack.io/python-is-quickly-evolving-to-meet-modern-enterprise-ai-needs/)
> 
> 作者：Steve Croce

Python无处不在。从科学家到软件开发者，数百万专业人士都依赖它。像[Google](https://cloud.google.com/?utm_content=inline+mention)和Meta这样的组织已经用它构建了关键基础设施。借助其图像处理能力，Python甚至帮助NASA探索[火星](https://thenewstack.io/python-in-unexpected-places/)。

而且它的增长短期内不会放缓。

2024年，Python在GitHub上[超越](https://github.blog/news-insights/octoverse/octoverse-2024/)JavaScript成为最受欢迎的语言，如今，它已成为现代AI系统的支柱。Python的多功能性和热情洋溢的社区使其取得了今天的成就。然而，随着越来越多的企业依赖Python来处理从Web服务到AI模型的一切事务，企业必须解决可见性、性能、治理和安全性方面的独特需求，以确保业务连续性、快速上市时间和真正的差异化。

## **Python如何成为通用的AI语言**

大多数流行的语言都受益于企业赞助。[Oracle](https://www.oracle.com/developer?utm_content=inline+mention)支持Java。微软支持C#。苹果力挺Swift。但Python几乎一直是一个[社区项目](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/)，由多家公司支持，并在几十年来由一群主要是志愿者的忠诚团体开发和改进，直到2018年由Guido van Rossum担任终身仁慈独裁者。

在20世纪80年代，van Rossum致力于创造一种既简洁又优美的语言。自90年代初作为一个开源项目以来，Python可供任何人检查、修改或改进。

![](https://cdn.thenewstack.io/media/2025/11/a3cbfa5c-picture1.png)

Python之禅，作者Tim Peters，图片最初由Pycon India发布于X。

Python很快就与同行区分开来。它易于学习、编写和理解。开发人员只需查看代码就能轻易了解自己和他人的代码在做什么，这在Perl、C++和复杂shell脚本的时代是异常的。这种低门槛使其对[新用户](https://thenewstack.io/why-beginning-developers-love-python/)极具吸引力。

此外还有Python的扩展性，这意味着它可以轻松与其他语言和系统集成。随着21世纪初互联网的兴起，这种扩展性使Python从脚本解决方案发展成为Web服务器、服务和应用程序的生产语言。

在2010年代，Python成为数值计算和数据科学的事实标准语言。如今，全球领先的AI和机器学习（ML）包，如PyTorch、TensorFlow、scikit-learn、SciPy、Pandas等，都是基于Python的。然而，它们使用的高性能数据和AI算法依赖于用C或C++等编译语言编写的高度优化代码。Python能够轻松与这些及其他语言集成，这对其提供两全其美的能力至关重要：为数百万希望使用这些包的用户提供简便的接口，同时为能够在他们选择的语言中优化这些包的专家提供灵活的接口。这些因素使Python在数据科学和AI工作流程中不可或缺。

如今，如果您正在使用任何类型的AI或ML应用程序，您很可能正在使用Python。然而，随着Python成为驱动现代AI系统的粘合剂和引擎，企业需要意识到围绕合规性、安全性、性能等方面的企业特有关键需求，社区也必须努力解决这些问题。

## **帮助Python满足企业需求**

资深Python核心贡献者Brett Cannon曾有名地说道：“我为语言而来，为社区而留。”

社区使Python成为今天这种非凡的语言，它服务于所有用户。然而，社区的使命一直是构建一种适用于所有人，从程序员到科学家再到数据工程师的语言。这已被证明是正确的方法。这也意味着Python并非专为使用Python运行业务的企业的特定需求而设计。

只要这些需求得到解决，这都不是问题。

[Anaconda的“2025年数据科学与AI现状报告”](https://www.anaconda.com/resources/report/8th-annual-state-of-data-science?utm_source=InsightMedia&utm_medium=organicsearch&utm_campaign=sods-2025-insight-media-tns)发现，企业在将数据和AI应用程序投入生产时面临许多相同的重复挑战。超过57%的受访者表示，将AI项目从开发阶段推向生产需要一个多月的时间。为了证明投资回报率，受访者主要关注商业问题，例如：

*   生产力提升 (58%)
*   成本节约 (48%)
*   收入影响 (46%)
*   客户体验/忠诚度 (45%)

把它想象成十五年前的云计算。组织可以立即看到将工作负载迁移到云端所带来的巨大成本和运营优势。然而，他们意识到安全、合规和成本模型已经完全改变。他们需要以全新的方式持续监控、治理和优化这一新工具。Python对企业来说也达到了同样的阶段。

我与数十位使用Python的组织领导者进行了交流，以下是我观察到的常见挑战和主题。

### **安全性**

尽管82%的组织[验证](https://www.anaconda.com/resources/report/bridging-the-ai-model-governance-gap)开源Python包的安全性，但近40%的受访者仍频繁在项目中遇到安全漏洞。这些安全问题导致超过三分之二的组织部署延迟。

Python和所有开源软件的优势之一是它们可以免费下载和使用。你可以获得最新最好的技术，并且可以实验、开发并将应用程序推向生产，而无需在软件上花费一分钱。

然而，历史表明，这种开放性和协作社区可能被恶意行为者滥用，甚至允许简单的错误蔓延，导致易受攻击和恶意软件的传播。一个看起来没问题的软件或包实际上可能很危险。这个问题现在正在加剧，AI系统现在在没有人为干预的情况下生成并执行Python代码。企业必须保护其人员、系统和数据，进而确保AI安全部署而不错过截止日期。

### **性能优化**

尽管Python易于使用，但它也可能*很慢*，这对于许多用例来说是可以接受的。但正如我们在“数据科学与AI现状报告”中看到的，现代企业主要关注的是“少投入多产出”——持续改进和提高效率、提升生产力、节约成本、增加收入等。生产AI应用的经济学只会加剧对性能和效率的担忧。

由于时间、专业知识或工具的限制，大多数企业难以对Python运行时进行精细调整，导致所需的计算资源远超实际需求，成本更高，或者运行的AI系统性能不足以提供可用体验。

### **可审计性**

我认识的每一位CIO和CISO都面临着一波又一波的法规，从欧盟AI法案到内部SOC 2和ISO 27001合规审计。企业必须能够证明正在运行的代码是什么、在哪里运行以及它如何与敏感数据和系统交互。

免费和开源软件使这变得具有挑战性，因为当任何人都可以自由下载和运行软件时，每个人都会这样做。新的Python应用程序出现在IT控制之外，包不断更新，未知或新的依赖被引入，并且运行时可观测性有限。特别是对于高度监管行业的组织来说，这种缺乏运行时可观测性会带来当前和未来的风险。

### **管理部署**

根据Anaconda用户最近的一项[调查](https://www.anaconda.com/resources/report/bridging-the-ai-model-governance-gap)，超过80%的从业者将其AI开发时间的10%以上用于解决依赖冲突或安全问题。超过40%的人将超过四分之一的时间花在这些任务上，而时间就是金钱。

一旦应用程序投入生产，持续的维护、升级和安全强化可能会加剧这些问题。对于运行和维护少量脚本和应用程序的个人来说，这并不难。然而，对于管理数千个生产应用程序的大型企业来说，这成为了一个巨大的挑战。

企业需要一种方法来轻松采用新版本的Python和新技术，同时最大限度地减少[版本蔓延](https://thenewstack.io/outdated-python-versions-cost-companies-millions/)、安全暴露和管理开销。

## **如何帮助企业AI满足现代企业需求**

好消息是，你今天就可以开始解决其中许多挑战。这都归结为有意识地制定你的治理策略。

[今天，超过一半的组织](https://www.anaconda.com/resources/report/8th-annual-state-of-data-science?utm_source=InsightMedia&utm_medium=organicsearch&utm_campaign=sods-2025-insight-media-tns)没有或只有非常有限的开源和AI治理政策或框架。围绕治理制定官方政策，并投资于可见性和可审计性，已经让你超越了大多数企业。

在构建治理策略时，首先要建立内部流程来跟踪跨团队和系统的Python使用情况。确保你知道哪些包正在运行、在哪里运行以及在何种配置下运行。

接下来，你需要确保你正在管理影子IT/AI并审查所有AI生成的代码。代理工具不能取代扎实的软件开发生命周期（SDLC）流程。确保你有正确的可见性、标准和流程，以防止未经验证的脚本进入生产环境。

投资于员工技能提升也至关重要，提高员工的AI素养，使他们更好地理解开源和AI解决方案的风险以及治理的重要性。最佳的学习方式之一是直接使用这些工具并获取经验。

最后，为你的团队提供AI和数据科学工作流程中的安全、可靠解决方案，这样“做正确的事”就成为阻力最小的路径。

## **让Python成为你的竞争优势**

Python的开放性是其最大的优势，也是其最重大的挑战。尽管它使AI开发民主化，但也带来了企业必须解决的新风险向量和盲点。IT团队需要对开源解决方案拥有与技术堆栈其他部分相同的可见性和治理能力。实践证明，这是企业创新的主要来源，因此为确保创新而进行的投资是值得的。尽管对语言本身进行特定升级会有所帮助，但有意识的治理今天就能带来改变。

在Anaconda，我们看到企业通过围绕其Python环境构建强大的SDLC、治理和可观测性层来应对这些挑战。这在前期会增加一些工作量，但这是一项关键的转变，从长远来看将保护您的组织，并确保您的AI计划取得成功和持久。