
<!--
title: API对接AI Agent最佳实践
cover: https://cdn.thenewstack.io/media/2025/06/dbe4fa74-api-ai-agents-2.jpg
summary: AI智能体将成为API的主要消费者。为应对这一趋势，企业需优化API，使其更易于机器读取。关键策略包括：完善OpenAPI规范，创建MCP服务器，定义清晰的错误响应，记录工作流程，考虑AI到API的标准，提供LLM优化的元数据，采用清晰的API设计，发展流量控制，构建丰富的开发者资源，加强安全性，遵循道德标准，找出货币化方法，并从DevRel转向AgentRel。
-->

AI智能体将成为API的主要消费者。为应对这一趋势，企业需优化API，使其更易于机器读取。关键策略包括：完善OpenAPI规范，创建MCP服务器，定义清晰的错误响应，记录工作流程，考虑AI到API的标准，提供LLM优化的元数据，采用清晰的API设计，发展流量控制，构建丰富的开发者资源，加强安全性，遵循道德标准，找出货币化方法，并从DevRel转向AgentRel。

> 译自：[How To Prepare Your API for AI Agents](https://thenewstack.io/how-to-prepare-your-api-for-ai-agents/)
> 
> 作者：Bill Doerrfeld

AI 智能体准备好成为新的大型 API 消费者。

[Tollbit 的报告](https://tollbit.com/bots/25q1/)显示，2025 年初，来自[检索增强生成 (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) 机器人的流量激增 49%。随着智能体变得[更具可操作性](https://thenewstack.io/what-are-large-action-models/)，它们也开始调用外部 API。

API 网关 [Zuplo](https://zuplo.com/) 的资深软件工程师 [Adrian Machado](https://www.linkedin.com/in/adrianmachado/) 告诉 The New Stack：“如果策略得当，AI 有可能成为你 API 增长最快的客户群。如果没有适当的 AI 支持，随着公司推进 AI 自动化，你将会被抛在后面。”

然而，[IBM](https://www.ibm.com?utm_content=inline+mention) 和 [Equinix](https://metal.equinix.com/?utm_content=inline+mention) 研究人员在 [2025 年发表的一篇论文](https://arxiv.org/pdf/2502.17443) 中指出，大多数企业 API 仍然无法很好地支持动态、目标导向的智能体行为。这是因为大多数 API 都是为人类开发人员设计的，而不是为机器设计的。那么，如何使它们为智能体做好准备呢？

AI 驱动的搜索引擎 [Exa](https://exa.ai/) 的联合创始人 [Jeffrey Wang](https://www.linkedin.com/in/wangzjeff/) 说：“API 的发现和使用正在发生巨大的转变。API 经济不再是‘谁拥有最好的开发者关系’，而是‘谁让自己最容易被机器读取？’”

如果没有明确的引导，智能体可能会完全错过你的 API。如果它确实发现了你的 API，[大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/) 可能会遇到未记录的行为、产生幻觉方法或用随机调用淹没你的服务器。

因此，正确地做好这件事非常重要。值得庆幸的是，从新的标准到非公开的技巧，各种将 API 定位为 AI 智能体的策略正在涌现。而且，这不仅仅是“获得一个 MCP 服务器”（尽管这是一个关键步骤）。

哪种策略最有效尚未有定论。因此，我构建本指南时，先从广泛认可的最佳实践开始，然后探讨仍在形成的实践。大多数技巧同样适用于公共、合作伙伴和私有 API。

## 使用定义完善的 OpenAPI 规范

定义完善、可访问的 [OpenAPI 规范](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) (OAS) 是基本要求。你需要一个精确的 API 定义，其中概述了端点、方法、模式、参数和身份验证。

[Netlify](https://www.netlify.com/) 的高级产品经理 [Taylor Barnett-Torabi](https://www.linkedin.com/in/taylormbarnett/) 告诉 The New Stack：“拥有经过验证和测试的 OpenAPI 规范至关重要，因为它可以作为智能体的可靠信息来源。”

这使智能体能够充分了解你的 API 的运作方式。[Tyk](https://tyk.io/) 是一家开源 API 生命周期管理平台的 CEO 兼联合创始人 [Martin Buhr](https://www.linkedin.com/in/martinpbuhr) 告诉 TNS：“LLM 在处理 JSON 时会遇到困难，并且依赖于描述性的 OAS 规范，不仅是结构，还有上下文丰富的描述。”

然而，挑战在于 API 漂移：根据 API 监控平台 [APIContext](https://apicontext.com/) [2024 年的一份报告](https://apicontext.com/resources/api-drift-white-paper/)，75% 的生产 API 的端点与其规范不符。保持定义更新需要持续的规范。

[APIContext](https://apicontext.com/) 的首席运营官 [David O’Neill](https://www.linkedin.com/in/davidon/) 提出了实践该规范的方法。“将 OpenAPI 规范直接实施到开发工作流程中，并应用严格的模式验证，”O’Neill 告诉 The New Stack。“这确保了 API 在被智能体定义、发现和使用时的一致性和可靠性。”

即便如此，向 LLM 提供 API 规范也并非万无一失——它仍然可能导致模糊的行为。[Sonar](https://www.sonarsource.com/%20?utm_content=inline+mention) 的集团产品经理 [Edgar Kussberg](https://www.linkedin.com/in/kussberg/) 告诉 The New Stack：“由于缺乏上下文理解，LLM 可能会错误地解释参数、忽略必填字段或滥用端点。”Sonar 是一家代码质量公司。

为了提高精确度，他建议使用具有结构化输出的函数调用。这是 OpenAI 等提供商提供的[一种方法](https://platform.openai.com/docs/guides/function-calling/function-calling-with-structured-outputs?api-mode=responses)，可以帮助模型获取数据并采取行动。

## 创建一个 MCP 服务器

另一个关键策略是采用用于连接和发现的标准协议。其中最主要的是 [Anthropic](https://www.anthropic.com/) 的开源[模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP)。

Kussberg 说：“就像我们构建 SDK 以使人类开发人员更容易使用 API 一样，MCP 的目标是为 AI 智能体做同样的事情。”它超越了规范，为自主智能体提供了语义。

MCP 服务器为 AI 智能体提供了一种无缝的方式来发现和集成你的工具、数据和 API。为了帮助创建它们，许多转换器可以将任何 OpenAPI 转换为 MCP 服务器，例如 [Speakeasy](https://www.speakeasy.com/) 的 [Gram](https://getgram.ai/) 或 Tyk 的开源 [API to MCP](https://www.npmjs.com/package/@tyk-technologies/api-to-mcp)。

Machado 直言不讳地说：“MCP 是未来。如果你真的想让 AI 智能体访问你的 API，请将它们包装在一个 MCP 服务器中，该服务器通过工具公开关键功能。”

但是，正确地做到这一点是一门艺术。他建议公开“大块”工具，这些工具结合了多个端点来实现特定的业务成果。

例如，Exa 使用 MCP 将其各种 API 端点统一在一个云托管界面下。这些搜索功能涵盖实时网络搜索、学术论文、公司研究和内容抓取。

Wang 说：“MCP 解决了一个根本问题：智能体需要了解何时使用你的 API，而不仅仅是你的 API 的作用。”

## 使用定义良好的错误响应

通过高质量的错误描述，AI 智能体可以了解 API 请求失败的原因并自动修复。这不仅仅是不透明的 HTTP 代码——它将需要详细的、机器友好的说明。

[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure Developer CLI 的首席产品经理 [Kristen Womack](https://www.linkedin.com/in/kristenwomack/) 告诉 The New Stack：“错误消息必须具体且有据可查。对于每个错误代码，提供其定义、要采取的下一个操作以及常见故障案例的示例。”

这些信息可以存在于你的 OpenAPI 规范中。

这也改善了与 AI 智能体的来回交互。Womack 补充说：“我认为我们将看到‘健谈’的智能体，因此为它们提供明确的指导对于 API 到 AI 通信的未来，甚至是通过 AI 进行的 API 到 API 集成至关重要。”

其他人也同意：状态代码是不够的。Machado 建议记录智能体可能遇到的常见错误消息，并返回 application/problem+json 媒体类型，这是一种机器友好的方式，用于在 HTTP 响应中发送错误消息，如 HTTP API 的问题详细信息（[IETF RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807)）所标准化。

Barnett-Torabi 说，更具描述性的错误意味着更好的用户体验。“你的错误消息和日志越彻底和详细，智能体就越有可能在没有多次来回提示的情况下解决问题。”

## 记录工作流程和后续步骤

记录常见用例和工作流程有助于智能体理解上下文。它还为互连的 API 流程带来了更多的确定性。

Machado 说：“展示如何将端点组合在一起以实现业务或技术成果将非常有帮助。智能体可能更喜欢那些清楚地展示如何解决特定任务的 API。”

[Arazzo 规范](https://thenewstack.io/the-rise-of-ai-agents-how-arazzo-is-defining-the-future-of-api-workflows/) 提供了一种标准方法来记录链接的 API 操作。这可能包括[常见的多步骤工作流程](https://www.speakeasy.com/blog/5-potential-use-cases-for-Arazzo)，例如入职流程、身份验证工作流程或付款发起。

为智能体提供“后续步骤”的另一种方法是通过超媒体，这是 RESTful API 设计中一种未被充分利用的约束。正如 REST 的架构师 [Roy Fielding](https://www.linkedin.com/in/royfielding/) 所定义的那样，HATEOAS（超媒体作为应用程序状态的引擎）意味着在每个 API 响应中包含指向进一步交互的链接。

超媒体使智能体更清楚地了解哪些操作是可能的。Tyk 的 Buhr 说：“HATEOAS 风格的响应有助于在分页数据中提供下一个和上一个链接，以减少幻觉。”

## 考虑其他 AI 到 API 标准

虽然围绕 MCP 的热情正在升温，但专家指出，仍然存在的[安全问题](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/)，例如缺乏内置身份验证，必须解决才能实现安全、可扩展的使用。而且，它不是唯一在发挥作用的协议。

虽然她承认 MCP“获得了动力”，但 Microsoft 的 Womack 也指出，像 [Agent2Agent (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/)、ACP、ANP 和 AGENCY 这样的[替代方案](https://thenewstack.io/why-are-agent-protocols-like-mcp-and-a2a-needed/) 已经出现。

Womack 说，现在判断哪种协议将主导 AI 到 API 的连接还为时过早。虽然 MCP 可能会以最快的速度发展，但她鼓励 API 生产者进行实验，密切关注协议，并为新兴标准的发展做出贡献。

## 提供 LLM 优化的元数据

一种低成本的策略是在你网站的根目录中添加一个 [llms.txt 文件](https://llmstxt.org/)。虽然不是专门为 API 设计的，但它提供的元数据可以帮助 LLM 进行发现和站点遍历。

Womack 说：“我可以看到这会变得像 robots.txt 和 sitemap.xml 一样，它们是长期存在且被广泛采用的。”但她补充说，目前尚不清楚 AI 模型提供商是否会完全支持该标准。

[一个目录](https://directory.llmstxt.cloud/) 现在编目了 600 多个正在使用的 llms.txt 文件。早期的采用者包括 [Anthropic](https://docs.anthropic.com/llms.txt)、[Cursor](https://docs.cursor.com/llms.txt) 和 [Perplexity](https://docs.perplexity.ai/llms.txt)。像 [Mintlify](https://mintlify.com/blog/what-is-llms-txt) 这样的 API 文档平台甚至会自动生成它们。

然而，并非所有人都确信 llms.txt 除了标准 Web 解析之外还能增加多少价值。Machado 说：“我认为 llms.txt 真的很愚蠢。”它需要主要公司和爬虫都支持它，他认为这不太可能：“绝对是一个先有鸡还是先有蛋的问题。”

也就是说，结构化的元数据仍然可以提供价值，尤其是在针对 LLM 进行优化时。

例如，除了 MCP 之外，Exa 还做出了其他为智能体准备的设计选择：将站点解析为干净的、为 LLM 准备的 Markdown，并提供根据客户端应用程序需求定制的自定义模式。

## 使用清晰的 API 设计

AI 智能体在可预测的模式下工作得最好。Buhr 说：“在使 API 做好智能体准备时，所有通常的最佳 API 设计实践都更加重要。LLM 是模式追随者。”

这意味着应用 RESTful 指南、使用一致的命名并维护清晰的数据层次结构。Barnett-Torabi 说：“如果你的 API 具有令人困惑的抽象或名称，你需要在使用智能体之前对其进行改进。”

她补充说，一个常见的不可预测性的来源是不一致地处理可选字段：“有时，智能体将或不会在请求中包含可选字段，这可能会导致意外的响应。”

减少歧义可以帮助智能体表现得更加可预测。也就是说，其他 API 专家指出，随着团队的发展和需求的变化，实现设计和谐是困难的。

Womack 说：“我们已经看到一些不一致的 API  несмотря design 一致性很重要。” 她补充说，即使像 [Stripe](https://stripe.com/) 和 [Twilio](https://www.twilio.com/?utm_content=inline+mention) 这样的 API 也比人们想象的要不一致：“我仍然怀疑这是否真的对智能体很重要。”

尽管如此，她建议设计最小的、相关的有效负载以提高性能——尤其是在实时交互中。她警告说：“慢或不可靠的端点可能会导致智能体超时。”

## 发展你的流量控制

Agentic AI 容易出现不可预测性和突发行为，需要新的[流量处理技术](https://thenewstack.io/what-is-semantic-caching/)。APIContext 的 O’Neil 说：“AI 智能体的行为与人类用户不同，因此相应地进行调整至关重要。”

他建议使用细致的速率限制、并发上限和分层配额来区分 AI 流量和人类使用。通过日志记录、监控和缓存提高可见性可以帮助检测和响应异常行为。

智能体可能被赋予循环执行重复过程的任务，例如批量发送电子邮件。Machado 说：“这将导致在短时间内进行大量 API 调用。”

不过，他补充说，检测智能体流量并不容易。“无法保证你可以识别智能体或机器人，而且它们有动机避免此类保障措施，以便完成其任务。”

Machado 建议使用动态速率限制来防止后端过载。提供允许批量操作和异步过程的端点也有助于减轻压力。

## 构建丰富的开发者资源

许多熟悉的开发者体验最佳实践，例如自助服务能力、清晰的文档、智能默认值和可预测的命名，也适用于 agentic AI。

Barnett-Torabi 说：“良好的开发者体验也可以带来良好的智能体体验。” 不过，关键的区别在于，AI 对信息过载的阈值更高，因此额外的上下文不会造成伤害。

上下文丰富的开发者门户可以增强智能体的理解。除了文档之外，教程、指南和博客文章等内容也有助于引导智能体获得最佳结果。

Barnett-Torabi 警告说，在登录墙之外塞入信息不会很好地发挥作用：“难以访问、隐藏且需要复杂流程才能获得访问权限的 API 不会非常适合智能体，并且会阻碍采用。”

## 不要忘记安全性

访问控制仍然是面向外部的 API 的一个主要弱点。根据 [Salt Security](https://salt.security/press-releases/salt-labs-state-of-api-security-report-reveals-99-of-respondents-experienced-api-security-issues-in-past-12-months) 的数据，95% 的 API 攻击来自经过身份验证的来源；98% 的攻击针对面向公众的 API。

因此，人们担心，智能体驱动的流量增加会加剧已经存在的 API 差距。为了避免智能体泄露敏感数据，可以采取一些策略。

首先，记录你的 API 总库存非常重要——这是一个了解你的环境、可以公开访问的内容以及是否存在影子 API 的好方法。

Machado 说：“你需要一个暴露给公共 Web 的所有 API 的完整列表。” 这包括官方公共 API 和你的应用程序调用的 Web API。“智能体也可能调用这些 API，所以不要认为它们是‘内部的’。”

Barnett-Torabi 说，基于标准的方法也应该有利于安全性。“对于身份验证，你应该密切遵循像 OAuth 这样的常见开放标准，”她说。“偏离 Web 标准会使你的 API 更难与智能体协同工作。”

## 遵循道德标准

API 一旦成为静态连接器，现在就变成了自主智能体进行训练和推理的数据高速公路。它们的兴起给提供商带来了新的压力，以确保系统（和底层数据）在道德上是合理的。

[Stack Overflow](https://stackoverflow.com/) 产品、知识解决方案高级总监 [Ellen Brandenberger](https://www.linkedin.com/in/ellenbrandenberger/) 告诉 The New Stack：“API 将在软件开发中发挥更关键的作用，成为值得信赖的信息渠道，其完整性和问责制直接影响 AI 智能体的行为方式。”

“为实现智能体就绪的 API 而出现的最重要的技术、工具和标准是那些优先考虑责任、透明度和社区信任的技术、工具和标准。” 她建议采用透明的数据来源、用户隐私和算法决策中的公平性。

## 找出货币化方法

并非所有 API 都是面向公众的或货币化的。但对于那些是面向公众的或货币化的 API 而言，agentic AI 可能会释放出可观的新收入来源。这将需要某种形式的基于使用量的计费。

Machado 说：“对于希望通过访问其平台或专有数据来获利的公司来说，AI 提供了一个巨大的商机。许多像 Stripe 这样的 API 优先公司已经在推出 MCP 服务器来捕获 AI 流量。”

他补充说：“与其他公共 API 相比，率先推出 MCP 服务器可以成为一种竞争优势，并提高你在采用 AI 智能体的创新公司中的市场份额。”

## 从 DevRel 到 AgentRel

[Akamai](https://www.linode.com/?utm_content=inline+mention) [报告](https://www.akamai.com/blog/security/rise-llm-ai-scrapers-bot-management) 称，来自基于 RAG 的 AI 智能体的抓取正在推动机器人流量的“指数级增长”。现在，API 是智能体与现实世界交互的下一个逻辑步骤。

除了 API 社区之外，其他人也证实了即将到来的激增。[Stigg](https://www.stigg.io/) 的联合创始人兼 CEO [Dor Sasson](https://www.linkedin.com/in/datapm) [在 1 月份的公司博客上写道](https://www.stigg.io/blog-posts/the-agents-are-coming-are-your-apis-ready-for-agentic-ai-consumption)，AI 智能体很快就会用人类无法单独生成的流量来冲击 API。

但是，为 AI 智能体做好 API 的定位并不是魔术。它需要重新思考传统的以开发者为中心的营销和设计，以实现机器优先的消费。像 MCP 这样的标准有助于解决这种机器驱动的转变。

其余的——比如全面的文档、速率限制、错误处理、有意义的错误和输入验证——通常都是良好的 API 卫生习惯。其他明智的举措包括避免暴露原始 API、使用网关以及定期使用智能体测试你的 API。

如果这一切看起来要求很高，那确实如此。它需要规范和基本的 API 优先思维，而这在今天并没有得到普遍应用。

因此，现实情况是？我们可能会看到捷径出现，以帮助软件即服务 (SaaS) 提供商快速登上 agentic 战车，无论是好是坏。

Machado 说：“这些策略的有效性仅取决于你的治理和工程文化。实际上，许多人只会将 MCP 贴在他们现有的 API 混乱之上，然后就此作罢。”

历史表明，这并不是一个糟糕的举动。Wang 将 MCP 的采用比作互联网时代的 SEO 淘金热。他说，本质上，MCP 正在帮助公司针对“智能体 SEO”进行优化。

Wang 补充说，现在采取快速行动可能会在以后获得回报：“今天，建立 MCP 服务器的应用程序提供商将在未来几年内主导 agentic 搜索和编排流程。”

因此，至少将你的 API 封装在 MCP 中以声明你的所有权。在第二天，弄清楚如何实施其余部分。