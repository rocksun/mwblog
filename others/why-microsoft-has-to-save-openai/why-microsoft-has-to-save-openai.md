<!-- 
title: 为什么微软必须拯救OpenAI
cover: https://cdn.thenewstack.io/media/2023/11/77865193-clint-patterson-jcy4oema3o-unsplash-1024x768.jpg
 -->

雇佣 CEO，雇佣团队，派遣 CEO 回去，坐上董事会——微软将不惜一切代价让 OpenAI 保持运行。

译自 [Why Microsoft Has to Save OpenAI](https://thenewstack.io/why-microsoft-has-to-save-openai/) 。

生成式AI明星公司OpenAI的混乱瓦解，就像一个提前的感恩节家庭争吵，起初看似小事，却变得[异常激烈](https://twitter.com/ilyasut/status/1726590052392956028?s=20)。也许正是微软的果断但友好的干预，像个成年人制止了这一切纠葛，也许还会有更多转折。但通过这些起起伏伏，微软介入稳定OpenAI技术(如果不是公司本身)已经势在必行。

## 不仅仅是金钱

微软最近对 OpenAI 的[100亿美元投资](https://www.ft.com/content/dd9ba2f6-f509-42f0-8e97-4271c7b84ded)，绝非小数目(尽管这一部分是以公司范围的大规模裁员支付的，这损害了 CEO 纳德拉(Satya Nadella)为公司交付的令人印象深刻的文化变革)，但这已经被证明有点像资金螺旋，微软多年来对 OpenAI 投资的相当大一部分显然已经花在(Azure)云计算上，以运行 OpenAI 的大型语言模型。

忘记可能永远不会实现的创建通用人工智能的遥远计划。微软——希望你把它看作“人工智能公司”，尤其是“Copilot 公司”，而不是“Windows 公司”——将以大约 2021年收购 Nuance 时的一半价格或者略低于其在2019年花费的75亿美元收购 GitHub的价格(考虑通胀调整)获得 ChatGPT 的技术基础。这笔钱并不是全花在云上，但仅微软2023第一季度的资本支出就达到了78亿美元。

> 尽管拥有自己令人印象深刻的 AI 研究员名单和自己的极其大型基础模型，微软极其在意 OpenAI 的 ChatGPT 语言模型，因为它对支持这些模型所作的云计算机硬件和软件的巨额投资，以及几乎所有部门和产品线对 OpenAI 技术的依赖。

纳德拉在 Ignite 会议开幕主题演讲中[反复提到了 OpenAI](https://news.microsoft.com/wp-content/uploads/prod/2023/11/Microsoft-Ignite-Opening.pdf)，包括预览 GPT-4 Turbo 模型。微软自己的产品同样充满了 OpenAI 技术，OpenAI 技术是众多 Copilot 的核心。

## 实现基础模型的经济可行性

大型语言模型和其他基础模型的训练需要大量数据、时间和计算能力。微软的解决方案是将它们视为平台，一次构建少数几个模型，然后以越来越定制化和专业化的方式重复重用。

> 微软已经搭建 Copilot 的技术栈五年了——从低级基础设施和数据中心设计(2023年每3天一个新的数据中心投入使用)到其软件开发环境，全面优化效率改变了一切。

从 GitHub Copilot 开始，几乎每条微软产品线现在都有 Copilot 功能。这不仅是面向消费者和办公用户的生成式 AI，如 Microsoft 365 Copilot、Windows Copilot、Teams、Dynamics 和新命名的 Bing Chat，还有为 Power BI 提供智能支持的 GPT 工具；Copilot 渗透到各个角落，从安全产品 Microsoft Defender 365，到 Azure 基础设施，再到微软新推出的基础架构产品。

微软客户也在同一技术栈上构建自己的定制 Copilot。纳德拉列举了几个例子——从 Airbnb 和 BT 到 NVidia 和 Chevron——新的 Copilot Studio 是一个低代码平台，使企业能利用自己的数据和 JIRA、SAP ServiceNow、Trello 等常用工具插件轻松构建定制 Copilot，这可使 OpenAI 无所不在。

为实现这一目标，微软建立了一个内部流水线，它从 OpenAI 获取新的基础模型，在较小的服务(如 Power Platform 和 Bing)中对其进行测试，然后利用从中获得的经验教训，将这些模型构建成更专业的 AI 服务，供开发人员调用。它已经在[语义内核](https://learn.microsoft.com/en-us/semantic-kernel/overview/)和[提示流程](https://microsoft.github.io/promptflow/index.html#:~:text=Prompt%20flow%20is%20a%20suite%20of%20development%20tools，you%20to%20build%20LLM%20apps%20with%20production%20quality.)上实现了标准化，可以与 Python、C# 等常规编程语言一起编排 AI 服务(并为开发人员构建了一个友好的新前端 [Azure AI Studio](https://azure.microsoft.com/en-gb/products/ai-studio/) 工具)。这些工具帮助开发人员构建和理解基于大型语言模型的应用程序，而无需理解这些庞大的语言模型——但它们依赖于微软对支撑其下的 OpenAI 模型的专业知识。

## 硬件是真实的承诺

微软必然在Nvidia和[AMD](https://techcommunity.microsoft.com/t5/azure-high-performance-computing/azure-announces-new-ai-optimized-vm-series-featuring-amd-s/ba-p/3980770) GPU上作出了大量投资，这正是OpenAI所依赖的关键硬件，此外还有节点之间高带宽的InfiniBand网络互联，以及通过[去年收购Lumensity](https://blogs.microsoft.com/blog/2022/12/09/microsoft-acquires-lumenisity-an-innovator-in-hollow-core-fiber-hcf-cable/)获得的低延迟中空光纤(HFC)制造技术。这些都是构建AI系统必不可少的组件。

微软赞扬OpenAI不仅在其Nvidia驱动的AI超级计算机的[协作](https://news.microsoft.com/source/features/ai/how-microsofts-bet-on-azure-unlocked-an-ai-revolution/)上功不可没，这些[计算机经常出现在Top500超级计算机榜单上](https://thenewstack.io/sc500-microsoft-now-has-the-third-fastest-computer-in-the-world/)，还对Maia 100的一些优化做出了贡献。微软不仅向OpenAI出售这些Azure超级计算机，也将其作为其他客户购买类似基础设施(或者仅购买运行于该基础设施之上的服务)的有力证明——如今几乎所有的微软产品与服务都依赖这些基础设施。

过去，微软加速AI的主要手段是使用FPGA，因为它们允许极大的灵活性：最初用于[加速Azure网络](https://www.microsoft.com/en-us/research/publication/a-reconfigurable-fabric-for-accelerating-large-scale-datacenter-services/)的相同硬件后来成为[加速必应搜索](https://www.microsoft.com/en-us/research/project/project-brainwave/)的AI推理器，然后又演变为一种服务，供开发者扩展自己的深度神经网络到AKS上。随着新型AI模型和方法的出现，微软可以通过重新编程FPGA更快地创建软定制处理器来实现加速，而不是构建一个很快就会过时的新硬件加速器。

借助FPGA，微软不必为未来几年的AI选择系统架构、数据类型或运算符：它可以在需要时随时更新其软件加速器的功能——您甚至可以在任务执行期间重新加载FPGA电路的部分功能。

然而上周，微软宣布推出首款自定义硅芯片：Azure Maia AI加速器，内置定制芯片级液冷系统和机架，专门用于“大规模语言模型的训练和推理”，它将为必应、GitHub Copilot、ChatGPT和Azure OpenAI服务运行OpenAI模型。这是一次重要的投资，将显著降低训练和运行OpenAI模型的成本(以及用水量)——只有在训练和运行OpenAI模型仍是主要工作负载的情况下，这些成本节约才能实现。

> 从本质上讲，微软刚刚为OpenAI打造了一款定制硬件加速器，要到明年才会推向数据中心，未来的设计也已经在计划之中。这对其密切的合作伙伴OpenAI来说肯定不是一个适合裂变或衰退的时机。

## 保证车轮继续转动

尽管这些年可能已经暗示过收购的想法，但微软最初并不想收购OpenAI。它当初[故意选择与公司外的团队合作](https://www.microsoft.com/en-us/Investor/events/FY-2023/AI-Discussion-with-Amy-Hood-EVP-and-CFO-and-Kevin-Scott-EVP-of-AI-and-CTO)，以确保自己正在构建的AI训练和推理平台不仅考虑自身需求。

但随着OpenAI的模型持续领先竞争对手，微软对其的赌注也越来越重。 ChatGPT推出仅一年就宣称每周1亿用户，OpenAI不得不暂停ChatGPT Plus用户注册，因为新增用户已经超过了系统容量——这还没算上微软直接客户对OpenAI的使用量。

> 不管您是通过OpenAI还是通过微软产品内置的OpenAI模型使用ChatGPT，它们全部都是运行在Azure上的。微软对“第一方服务”(自己的代码)和“第三方服务”(任何外部代码)的区分也已变得模糊。

理论上，微软可以退出转向不同的基础模型，关键竞争对手的多数基础模型已经可以在Azure上运行。但中途更换不仅混乱且昂贵，很可能会失去领先地位，也会损害公司在股市和客户心中的地位。保证OpenAI技术的继续存活和繁荣确实是更好的选择。

尽管OpenAI的[开发者关系团队一直在向客户保证](https://x.com/OfficialLoganK/status/1726631481403941107?s=20)业务正常进行，[系统仍在运行](https://status.openai.com/)，并且工程团队一直待命，但据报道，OpenAI的客户已开始联系竞争对手Anthropic和Google；其中可能包括微软不愿失去的Azure OpenAI客户。[LangChain](https://github.com/langchain-ai/langchain)是一家初创公司，正在构建一个用于创建与Azure OpenAI服务紧密集成的基于LLM的应用程序框架，并已[宣布与Azure OpenAI Service进行了重要的集成](https://blog.langchain.dev/langchain-expands-collaboration-with-microsoft/)。该公司一直在向开发者分享建议，指出[切换到不同的LLM](https://twitter.com/LangChainAI/status/1726995678042210552)需要进行重大的提示工程更改（目前大多数示例都是针对OpenAI模型的）。

## 对OpenAI的依赖

如果微软内部的客户——这几乎涵盖了每个部门和产品线——正在进行类似的内部对话，尽可能多地将OpenAI的专业知识引入内部将有助于减轻它在OpenAI本身分裂或衰落时需要进行的任何过渡。

是的，微软拥有[首席财务官艾米·胡德（Amy Hood）所描述](https://www.microsoft.com/en-us/Investor/events/FY-2023/AI-Discussion-with-Amy-Hood-EVP-and-CFO-and-Kevin-Scott-EVP-of-AI-and-CTO)的“对所有OpenAI知识产权的广泛永久许可”，直到AGI（如果那会发生），即使与OpenAI的合作结束，但生成式人工智能发展如此之快，仅仅保持今天的模型运行是不够的。微软需要确保能够获得未来的语言模型，如GPT-5。

尽管名称中有“开放”两字，但OpenAI从未主要作为一个开源组织，只有[个别发布](https://openai.com/research?topics=open-source)，其核心大型语言模型也没有开源过。这一点值得与微软逐步接受开源进行比较：发布核心项目(如PowerShell和VS代码)作为开源只是开始，真正关键的是它开始依赖诸如Docker和Kubernetes等开源项目用于Windows Server和Azure。

相比之下，它对OpenAI的依赖性甚至更深，这反过来证明是一种比预期更不稳定、治理更弱的依赖。无论以何种方式，微软都将确保OpenAI对其必要的贡献得以延续。
