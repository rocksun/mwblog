
<!--
title: 科技主管正在放缓AI项目的3个原因
cover: https://cdn.thenewstack.io/media/2024/04/45b1022d-slow.jpg
-->

人们越来越意识到在不受管理的情况下使用生成式人工智能所涉及的风险，以及在这个快速发展领域中寻找可信赖的合作伙伴和解决方案的必要性。

> 译自 [3 Reasons Tech Execs Are Slowing Down GenAI Projects](https://thenewstack.io/3-reasons-tech-execs-are-slowing-down-genai-projects/)，作者 Mandi Walls。

众所周知，IT 趋势难以预测，但自 2022 年底 ChatGPT 发布以来，生成式 AI (GenAI) 已呈指数级增长。IDC [预测](https://www.idc.com/getdoc.jsp?containerId=US51881324)企业今年将在全球范围内花费 400 亿美元，三年后将增长近四倍至 1510 亿美元。它得到了另一项 [PagerDuty 研究](https://www.pagerduty.com/assets/whitepaper-generative-ai-survey.pdf) 的支持，该研究发现 64% 的财富 1000 强高管在其组织的大部分或所有部门部署了 [GenAI](https://thenewstack.io/ai/)。几乎所有 (98%) 这些公司都在尝试用例。

但这并不是全部。Wakefield Research 对 100 位财富 1000 强高管进行的同一项研究显示，98% 的组织在制定准则和政策时暂停了内部计划。它表明人们越来越意识到未管理的 GenAI 使用所涉及的风险，以及企业需要在这个快速发展的新兴领域找到值得信赖的合作伙伴和解决方案。

## GenAI 如何改变 ITOps

GenAI 如此之新，以至于组织仍在研究部署该技术的最佳方式。IT 已被吹捧为在营销、软件开发和客户服务等用例中具有潜在变革性。但它还可以为 ITOps 团队极大地提高生产力。

我们在三个关键领域看到了这一点：

- **网络运营中心**，其中手动操作和过时的流程可能导致过度升级和较长的平均解决时间 (MTTR)。GenAI 可以帮助将诊断信息汇总在一起，为利益相关者生成定期状态更新，简化事件管理工作流程和通信，同时释放 ITOps 以专注于手头的工作。
- **重大事件管理**团队经常[难以应对复杂性](https://thenewstack.io/managing-complexity-and-avoiding-chaos-in-digital-operations/)、警报噪音和缺乏上下文，这会延长 MTTR。GenAI 使响应者能够快速创建工作流以进行状态更新，将高优先级事件路由到合适的专家。它还可以通过对加速 MTTR 所需的流程自动化进行编码来提供帮助。
- **分布式服务所有团队**由于警报噪音、不同的监控工具和有限的上下文，经常承受着极大的压力，以提供改进的客户体验。GenAI 可以通过生成状态更新和事后报告来提供帮助——后者对于推动持续改进至关重要。

## 高管们为何谨慎

我们交谈过的财富 1000 强技术高管敏锐地意识到需要利用这些能力来获得竞争优势。近一半 (46%) 的人认为，如果不尽快采用 GenAI，他们就有落后的风险。即便如此，对于过快地这样做还是持谨慎态度。速度很重要，但不能不惜一切代价。组织暂停 GenAI 项目的前三个原因是：

### 1. 版权和法律风险 (51%)

GenAI 模型可能在受版权保护的作品上进行训练，这意味着使用此类模型输出的组织可能会不知不觉地陷入法律纠纷。2023 年底，纽约时报[起诉](https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html) OpenAI 和 Microsoft 侵犯版权。

组织可能越来越需要在与 GenAI 提供商的合同中写明法律保证，规定模型接受训练的任何作品都已获得许可并扩展到该工具的用户。他们可能还需要加强对潜在 GenAI 供应商的尽职调查，以检查其风险敞口，并可能运行检查以确保任何 AI 生成的软件不会侵犯先前发布的代码。

### 2. 敏感信息泄露 (48%)

基于[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms) 构建的 GenAI 应用程序可能会意外泄露敏感信息，例如专有算法或其他知识产权 (IP)。三星[禁止](https://www.cnbc.com/2023/05/02/samsung-bans-use-of-ai-like-chatgpt-for-staff-after-misuse-of-chatbot.html)去年 5 月内部使用 ChatGPT 和类似工具，此前开发人员将敏感代码上传到该工具以帮助他们调试和优化它。摩根大通和亚马逊等公司也限制了员工使用此类工具。

组织必须制定可接受的使用政策和更新的员工意识培训，以规范员工如何使用基于 LLM 的工具。他们可能还希望更新数据丢失预防 (DLP) 解决方案，以部署细粒度控制并限制员工的访问权限。企业许可证对于通过对 AI 模型对任何用户输入/提示的操作施加严格限制来减轻此类风险可能变得越来越重要。

### 3. 数据隐私违规 (47%)

与上述示例类似，用户可能无意中将敏感信息输入到 GenAI 模型中。如果这是受监管的个人信息，则可能使企业面临违反 GDPR 或 CCPA（加州消费者隐私法）等法律的风险。[OpenAI 在其隐私政策中声明](https://www.weirfoulds.com/to-use-or-not-to-use-navigating-privacy-risks-associated-with-generative-ai-tools#_ftnref1)，它可能会使用此类输入来提供、分析和改进其服务，以及开发新程序和服务。它还可能在不另行通知的情况下与供应商和服务提供商等第三方共享该信息。

如上所述，企业将[需要制定水密的用户政策和程序](https://thenewstack.io/ai-engineering-what-developers-need-to-think-about-in-2024/)，并结合更新的员工培训，以最大程度地降低其风险敞口。他们甚至可能需要阻止使用“泄漏”模型，而只坚持使用经过严格审查的企业级 GenAI 提供商，这些提供商承诺不会以这种方式使用个人信息。

## 信任至上

最后，我们应该赞扬那些正在放慢 GenAI 项目的技术主管。超过一半 (51%) 的人认为，只有在制定了正确的准则后，他们才应该采用 GenAI。这表明他们意识到了这些风险，并希望确保以负责任且合规的方式使用该技术。

下一步将至关重要：即他们制定的政策和程序以及他们选择合作的技术公司。越来越多的旅行方向将是能够提供内置了适当护栏以减轻版权、数据丢失、合规性和幻觉等其他风险的工具的专业提供商。好消息是，这些提供商今天已经存在。
