
<!--
title: 为什么纯AI编码不适用于企业软件
cover: https://cdn.thenewstack.io/media/2025/05/3e5398eb-hogarth-de-la-plante-7-plwj1zf58-unsplash-1.jpg
summary: 企业软件拥抱AI并非全盘替代！文章强调“AI应用生成”，即利用AI和自然语言生成结构化业务资产而非原始代码。Pega的Blueprint工具将自然语言转化为结构化工作流，兼顾创新与合规。专业开发者需关注数据服务、底层配置，与AI和Low-Code平台协同，实现“氛围编码”与企业治理的平衡。
-->

企业软件拥抱AI并非全盘替代！文章强调“AI应用生成”，即利用AI和自然语言生成结构化业务资产而非原始代码。Pega的Blueprint工具将自然语言转化为结构化工作流，兼顾创新与合规。专业开发者需关注数据服务、底层配置，与AI和Low-Code平台协同，实现“氛围编码”与企业治理的平衡。

> 译自：[Why Pure AI Coding Won't Work for Enterprise Software](https://thenewstack.io/why-pure-ai-coding-wont-work-for-enterprise-software/)
> 
> 作者：Darryl K Taft

随着[生成式 AI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) 重塑软件开发，一个关键问题浮出水面：面对[自然语言“氛围编码”](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/)，传统的低代码和无代码平台是否会变得过时？

虽然一些业内人士预测，结构化开发方法将被 [AI 代理](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/) 完全取代，但企业软件领域的资深企业 [Pega](https://www.pega.com/) 提出了一个更为细致的观点，将两个世界联系起来。

## 企业现实检验

“[很多人认为一切都将是代理](https://www.linkedin.com/in/donschuerman/)，”首席技术官兼产品营销副总裁 Don Schuerman 在接受 The New Stack 采访时表示。“我认为这些人从未处理过实际企业 IT 组织的复杂性。坦率地说，我认为这里面有点天真。”

这一观察突显了 AI 驱动开发的前景与企业软件的实际情况之间的紧张关系。虽然像 [Cursor](https://www.cursor.com/) 这样的工具使开发人员能够通过自然语言提示构建应用程序（有些人称之为“[氛围编码](https://thenewstack.io/vibing-dangerously-the-hidden-risks-of-ai-generated-code/)”），但企业需要额外的保障措施，而纯 AI 生成本身并不提供这些措施。

## 非结构化 AI 开发的陷阱

Schuerman 列举了企业对不受限制的 AI 代码生成的一些担忧：

- **安全和合规风险**，在没有适当监督的情况下。
- **数据访问管理**复杂化。
- **技术债务激增**，因为成千上万的开发人员可能会在没有集中协调的情况下创建类似的应用程序。
- **缺乏可审计性**，对于必须准确解释流程如何运作的受监管行业。

## 中间道路：AI 应用生成

Schuerman 说，Pega 提倡 Forrester Research 所谓的“AI 应用生成”，即使用 AI 和自然语言来生成结构化的业务资产，而不是原始代码，而不是在传统 [低代码](https://thenewstack.io/the-highs-and-lows-of-low-code-tools/) 和 AI 代理之间进行二选一。

“我们一直在思考的是，如何采用[氛围编码的精神](https://thenewstack.io/vibe-coding-is-here-how-ai-is-reshaping-the-software-developer-profession/)，即借助这些 AI 工具，我应该能够用自然的业务语言表达我想要完成的事情，并让软件开始接受它，但要以一种在沿途设置结构性检查点的方式进行，以适应企业正在寻找的东西，”他解释说。

## 蓝图：AI 遇上结构化工作流设计

Pega 应对这一挑战的答案是 [Blueprint](https://www.pega.com/blueprint)，这是一种由 AI 代理驱动的工作流设计工具，可将自然语言描述转换为结构化的业务流程。

在工具演示期间，Schuerman 展示了用户如何：

1. 用自然语言指定其行业、业务领域和应用程序目的。
2. 接收 AI 生成的工作流、用户界面和适合其描述需求的的数据模型。
3. 受益于特定领域的知识（例如，为医疗保健应用程序添加可访问性审查）。
4. 跨渠道（移动、Web、联络中心、对话界面）预览体验。
5. 导出与低代码平台集成的结构化定义。

Schuerman 说，结果是一个蓝图，以一种对治理友好的格式提供了大约 60-70% 的构建完成度。

## AI 代理的两面性

他还强调了不同代理角色之间的区别。设计时代理应该具有创造性，在设计阶段提出改进建议并引入领域专业知识。而运行时代理在为用户提供服务时需要严格遵循已建立的工作流，确保[合规性和法规要求](https://thenewstack.io/you-must-prioritize-compliance-in-modern-infrastructure/)，他说。

“在设计时，我希望我的代理具有创造性。我希望他们提出我可能没有想到的事情，”Schuerman 解释说。“当我进入运行时，我不希望我的代理具有创造性。我希望他们完全按照我制定的工作流执行，并且我希望他们每次都一致地执行，因为这就是我向监管机构辩护的方式。”

## 无代码的有限企业角色
虽然 Schuerman 承认，传统的 [无代码工具](https://thenewstack.io/celebrate-national-no-code-day-today/) 确实可能被 AI 取代，用于简单的个人应用程序——“无代码一直更像是个人应用程序”，他说——但他强烈反对所有企业开发都将遵循同样的道路的观点。

Schuerman 表示，对于银行、医疗保健和政府等受监管的行业来说，能够准确展示流程如何运作的能力——而不仅仅是“代理算出来的”——仍然至关重要。

## 专业开发人员的定位

专业开发人员不会被取代，但会看到他们的重点发生转变。根据 Pega 的说法，他们仍然需要：构建和维护数据服务，开发自定义应用程序和框架，创建数字体验以及处理底层数据配置。

这表明 AI 和低代码平台将处理更多的业务领域实现，而专业开发人员则专注于基础设施和专门需求。

## 混合方法

与此同时，随着 AI 改变软件开发，企业领域似乎正朝着一种混合方法发展——一种既包含“氛围编码”的自然语言优势，又保持企业所需的结构、安全性和治理的方法，Schuerman 说。

他认为，我们所看到的不是一场席卷现有范式的 AI 革命，而是一场 AI 增强和加速结构化开发方法的演变，特别是对于审计和合规性不能妥协的复杂企业需求。

因此，这种中间道路认识到，虽然消费者应用程序可能会越来越多地通过纯 AI 生成来构建，但企业软件开发必须在创新与责任之间取得平衡。