<!--
title: AWS Bedrock AgentCore策略新层：AI代理严守机密，杜绝泄露底牌
cover: https://cdn.thenewstack.io/media/2025/12/fb90841c-17d47d58-211f-4d37-a330-415fb51fd773-scaled.jpg
summary: AWS Bedrock AgentCore新增策略、评估和情景记忆功能，旨在提升AI代理的安全、可信赖性及个性化体验，助力企业更好地构建和部署AI代理。
-->

AWS Bedrock AgentCore新增策略、评估和情景记忆功能，旨在提升AI代理的安全、可信赖性及个性化体验，助力企业更好地构建和部署AI代理。

> 译自：[AWS' New Policy Layer in Bedrock AgentCore Makes Sure AI Agents Can't Give Away the Store](https://thenewstack.io/aws-new-policy-layer-in-bedrock-agentcore-makes-sure-ai-agents-cant-give-away-the-store/)
> 
> 作者：Frederic Lardinois

LAS VEGAS — 在拉斯维加斯举行的 re:Invent 大会上，[AWS](https://aws.amazon.com/?utm_content=inline+mention) 今天宣布对 [Amazon Bedrock AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) 进行多项更新，旨在让企业更容易在 AWS 平台上构建和部署 AI 代理。

Amazon Bedrock AgentCore 是 AWS 面向开发者的平台，用于构建、部署和管理 AI 代理。当它[于今年夏天推出](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/)时，就包含了构建生产就绪代理所需的许多核心工具，包括使用任何流行代理框架和大型语言模型 (LLM) 构建这些代理的能力、身份验证服务、为这些代理提供内存的功能等等。

现在，在 re:Invent 大会上，AWS 正在推出三个核心新功能，旨在解决一些仍然阻碍部分公司采用代理的问题。

“按照 AWS 一贯的风格，我们提供了一些原语，” AWS Amazon Bedrock AgentCore 副总裁 David Richardson 告诉我。“我们的意图是让它们能够很好地协同工作。事实上，我们甚至比 AWS 往常做得更努力，以确保这一点。我知道有时我们会暴露出一些不完美，但我们真的在努力使其成为一套完整的工具，这些工具很可能在各种代理中都会被需要。”

## 策略

这些新服务中的第一个是安全和策略执行功能，它解决了许多公司在将代理投入生产时发现的对额外防护措施的需求。毕竟，对于许多公司来说，这些模型的非确定性性质使得它们不愿超越试点阶段——当涉及到面向客户的产品时尤其如此。毕竟，提示注入攻击是非常难以防范的。

Richardson 解释说，这项名为“策略”的新功能有趣之处在于，它位于代理循环之外，并且是基于规则的。公司可以用它来创建（用自然语言表达的）防护措施，例如，确保如果 AI 代理想向用户提供价值超过 100 美元的信用额度，则必须由人工代理介入并验证此请求。

[![](https://cdn.thenewstack.io/media/2025/12/1cb23905-screenshot-2025-12-02-at-09.05.07.png)](https://cdn.thenewstack.io/media/2025/12/1cb23905-screenshot-2025-12-02-at-09.05.07.png)

图片来源：AWS。

“我认为……它控制着代理被允许要求工具做什么。在底层，你拥有[身份访问管理](identity access management)，它规定了可以使用哪些工具。有了策略，你可以控制你能要求工具做什么——然后通过我们现有的 Bedrock Guardrails，你可以控制 LLM 会向最终用户说什么，” Richardson 解释道。

他还指出，这里的意图是让策略成为分层安全故事的一部分，该故事始于代理运行时位于微型虚拟机 (VM) 之上，这些虚拟机提供会话级隔离，并在此基础上叠加 AWS 提供的所有常见安全功能。

Richardson 认为，最终，如果企业想从代理中获得任何真正的价值，他们就需要能够信任自己的代理。理想情况下，这种额外的安全网将帮助他们实现目标，并使他们能够更依赖代理的推理能力，因为当事情不按计划进行时，它会提供支持。

## 评估

第二个新增功能是自定义评估。Bedrock AgentCore 已经支持传统的[可观测性]工具——包括 AWS 生态系统内部的工具，如 CloudWatch 和分布式 X-Ray 追踪系统，或 OpenTelemetry 等行业标准。

新的评估工具将提供 13 种预构建评估，涵盖了许多基本方面（正确性、忠实性、有用性、响应相关性、简洁性、连贯性、指令遵循、拒绝、目标成功率、工具选择准确性、工具参数准确性、上下文相关性、有害性、刻板印象）。

开发者也可以创建自己的自定义评估。这些评估将使用 LLM 作为评判者。

[![](https://cdn.thenewstack.io/media/2025/12/48a2a2fb-screenshot-2025-12-02-at-09.07.49.png)](https://cdn.thenewstack.io/media/2025/12/48a2a2fb-screenshot-2025-12-02-at-09.07.49.png)

图片来源：AWS。

“我设想，至少在早期，它最终会有两种使用方式。一种可能是由代理开发者在开发和完善阶段使用，他们可能会自行测试或使用一些预设的追踪进行测试，并查看评估结果，” Richardson 说。“另一种将是运维团队的长期使用，类似于他们管理非代理应用程序的方式，在那个世界里，你可能有与延迟和错误指标相关的一组指标，而现在你可能有由评估者计算的用户情绪或准确性指标。”

## 内存

第三项宣布与其说是一个新功能，不如说是 Bedrock AgentCore 现有内存工具的补充。该内存工具已经提供了短期和长期内存功能，但现在它还提供了情景记忆。

“其理念是使其与单个用户对齐，这样你就可以记录他们的偏好——比如他们喜欢靠窗座位而不是靠过道座位，或者他们喜欢价格低于 500 美元的酒店等等，” Richardson 说。“我们认为不同的记忆规范、记忆机制将是创建有效代理的关键之一。因此，我们希望开始提供几种不同的记忆类型功能供客户使用。”