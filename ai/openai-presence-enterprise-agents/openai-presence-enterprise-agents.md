<!--
title: OpenAI为自家客服部门打造了AI代理，现在它希望大型企业也能信任并使用这些代理
cover: https://cdn.thenewstack.io/media/2026/07/feaa8b19-andania-humaira-9jlcaeefkio-unsplash-scaled.jpg
summary: OpenAI发布Presence产品，旨在为企业提供可信赖的AI客服代理。Presence不仅处理实时交互，还包含策略制定、模拟测试及可观测性监控功能，由工程师驻场支持，以确保AI在复杂业务环境下的可靠性与适应性。
-->

OpenAI发布Presence产品，旨在为企业提供可信赖的AI客服代理。Presence不仅处理实时交互，还包含策略制定、模拟测试及可观测性监控功能，由工程师驻场支持，以确保AI在复杂业务环境下的可靠性与适应性。

> 译自：[OpenAI built support agents for its own customer service line, now it hopes big enterprises will trust them too](https://thenewstack.io/openai-presence-enterprise-agents/)
> 
> 作者：Paul Sawers

在AI和工业领域，一个逐渐形成的普遍共识是，模型本身[已不再是瓶颈](https://thenewstack.io/ai-agent-infrastructure-bottleneck/)——它们的能力已经足够强大，可以支持深度对话、生成海量的生产级代码，并解决各种类型的客户支持请求。

更困难的问题在于模型之外的一切：决定代理能否自主行事的策略、无法解决问题时的升级路径，以及在出错时记录事发过程的机制。

## 让代理变得可靠

归根结底，这关乎信任：作为客户运营负责人或首席信息官，你是否愿意让一个系统处理实时客户电话并在未经明确授权边界的情况下操作账户？如果系统出错了，谁来负责？

OpenAI认为它找到了答案，这就是周三发布的产品——Presence。该产品将AI代理（即OpenAI一直在其自己的支持热线上运行的同款代理）应用于企业的电话和聊天渠道。

在宣布该产品的[博客文章](https://openai.com/index/introducing-openai-presence/)中，OpenAI指出，企业级AI代理真正的考验早已超越了证明其“能干活”的阶段——现在的关键在于，随着周边产品、策略和人员的不断变化，它们能否保持可靠性。

“对企业而言，挑战已不再是证明AI代理可行，而是使其足够可靠，从而在生产环境中执行高价值工作，”该公司写道。“代理的行为必须随着产品、策略和用户行为的变化而不断适应。”

> “对企业而言，挑战已不再是证明AI代理可行，而是使其足够可靠，从而在生产环境中执行高价值工作。”

## 稳健的方案

Presence 将代理及其在生产环境中运行所需的一切打包成一个产品——OpenAI 为每个客户构建并部署代理，并提供策略、测试工具和监控功能，确保其上线后持续稳定运行。

其核心是代理本身，它能够实时处理现场对话：验证通话对象、查询账户或订单，并直接解决问题（无论是重复扣款还是配送更新），无需人工介入。

![AI代理验证客户并解决重复扣款问题](https://cdn.thenewstack.io/media/2026/07/bc1fd68f-openai-presence-still-1-1024x576.webp)

*AI代理验证客户并解决重复扣款问题*

在上线之前，团队可以通过模拟来运行策略变更，针对一批过往案例进行测试，并在批准发布前对退款、取消和账户验证等类别的表现进行评分。

![模拟测试新的退款政策变更](https://cdn.thenewstack.io/media/2026/07/a61162d0-openai-presence-still-2-1024x576.webp)

*模拟测试新的退款政策变更*

一旦代理投入生产，实时仪表板就会跟踪其持续表现——包括响应准确性、呼叫量以及处理退款或取消等特定任务的能力——使团队能够及时发现并处理出现的问题。

![实时仪表板跟踪代理表现和呼叫量](https://cdn.thenewstack.io/media/2026/07/12e9003b-openai-presence-still-3-1024x576.webp)

*实时仪表板跟踪代理表现和呼叫量*

通过Presence，公司可以为代理选择一个单一的、具体的任务，例如保险索赔、IT请求或账单争议，代理仅能访问与该任务相关的信息和系统，不会超出范围。制定规则的是公司而非OpenAI：包括代理在无需确认的情况下可以做什么、哪些操作需要人工签字，以及何时停止并移交给人类。

然而，实现这一点并非简单地开关一下API。OpenAI的工程师会与每位客户坐在一起，确定工作内容、连接系统、设定权限、进行测试并上线，随后在部署规模扩大时，将后续支持移交给外部集成合作伙伴。

值得注意的是，OpenAI表示，这实际上早已是其内部支持业务的一部分，据称该代理现在能解决其英语电话热线上75%的入站问题，且无需人工干预。这显然是其推销的核心：如果这套方案对于世界上最有价值的私营公司之一（其声誉完全取决于人们对其产品的信任）来说足够好，那么它对其他人来说一定也足够好。

它是否真的可行，还有待观察。但该公司已经拥有了一些早期的设计合作伙伴，包括[BBVA](https://en.wikipedia.org/wiki/Banco_Bilbao_Vizcaya_Argentaria)、[SoftBank](https://en.wikipedia.org/wiki/SoftBank_Group)和[IAG](https://en.wikipedia.org/wiki/Insurance_Australia_Group)。显然，这距离全面推广还有很长一段路——它尚未作为自助服务产品提供，这便是一个信号。目前，该产品仅通过受限发布向符合条件的企业客户开放，部署工作直接由OpenAI自己的“前线部署工程师”和少数全球系统集成商处理。

Presence并非OpenAI在此方面的唯一动作。在此次发布的前一个月，这家ChatGPT的制造商与包括Google和Microsoft在内的科技巨头共同[发起了Appia Foundation](https://thenewstack.io/google-microsoft-and-openai-join-forces-to-help-create-ais-missing-trust-layer/)。这是一个Linux基金会的项目，旨在为企业提供一种标准化的方式来证明其AI系统符合安全和合规义务，而不是依赖自我声明。

如果说Appia是在构建全行业通用的文件证明AI系统值得信赖，那么Presence就是OpenAI试图通过每一个具体的客户来证明这一点。

## 前线部署工程师：AI的信任层

放眼宏观，Presence对OpenAI自身工程师的依赖本身就是一种更广泛趋势的一部分。科技公司不再仅仅交付一个API就撒手不管，而是将技术人员直接嵌入客户团队，现场设计、构建并支持AI系统。

正如 *The New Stack* [此前报道的那样](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/)，“前线部署工程师”（FDE）在5月份的大约十天内，一跃成为该行业最炙手可热的职位之一。OpenAI[创立了](https://openai.com/index/openai-launches-the-deployment-company/)一家价值40亿美元的新公司，专门为企业配备此类工程师；Google也发布了数十个相关职位，薪资高达数十万美元。与此同时，AWS在6月[宣布](https://thenewstack.io/aws-forward-deployed-engineering/)将投入10亿美元建立类似的团队，将工程师直接嵌入客户内部，帮助利用客户自己的数据和基础设施构建并运行AI系统。

> “制造一个AI代理很容易。困难的是制造一个可以被信任去直接与客户沟通的AI代理，并且它能随着需求变化而自我调整。”

OpenAI全球前线部署工程主管 [Colin Jarvis](https://www.linkedin.com/in/colin-jarvis-50019658/) 周三在LinkedIn上解释说，Presence源于OpenAI的FDE团队在直接解决客户部署中反复出现的问题时所做的工作。

“我们许多最具挑战性的客户工作始于面向外部的用例，代理需要能够应对变化的客户行为、业务政策调整和外部妥协，”Jarvis写道。

这指向的核心是信任：一家将电话热线交给代理的公司，想要确保身后有一位既懂系统又懂业务的人员在支持，而不是一个无人监管的模型。

OpenAI的前线部署工程师 [Zach Parent](https://www.linkedin.com/in/zachary-parent/) 在LinkedIn上[解释](https://www.linkedin.com/feed/update/urn:li:activity:7485690824257712128/)道，目前的困难已从如何构建代理，转移到如何构建一个在需求不断变化时，企业真正敢让其接近客户的代理。

“如今，制造一个AI代理很容易，”Parent写道。“困难的是制造一个可以被信任去直接与客户沟通的AI代理，并且它能随着需求变化而自我调整。”