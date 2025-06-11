# PayPal 谈如何为 Agentic AI 的未来准备 API

![Featued image for: PayPal on How To Prepare APIs for Agentic AI Future](https://cdn.thenewstack.io/media/2025/06/a8890dbb-paypallogo-1024x576.jpg)

Photo by Mariia Shalabaieva on Unsplash.

PayPal 预测，五年内，其 20% 到 30% 的客户将通过 AI 代理和 AI 工具开始购物。为了应对这种可能性，它正在创建一个 [模型上下文协议 (MCP) 服务器](https://thenewstack.io/mcp-is-rss-for-ai-more-use-cases-for-model-context-protocol/)，以一种易于 AI 理解的方式公开 [PayPal 现有的 API](https://thenewstack.io/api-governance-using-patterns-from-paypal-netflix-and-more/)。

“我们可能离代理完全自动化、大规模购买东西并在没有任何交互的情况下发送给你的那一天还有一段距离，但我们比人们想象的要近得多，”PayPal 开发者产品高级主管 Brenden Lane 说。“PayPal 正在努力成为代理商务的基础设施层。”

PayPal 使用了 Postman 新的 [具有 MCP 集成的 Agentic AI Builder](https://learning.postman.com/docs/postman-ai-agent-builder/ai-tool-builder/overview/)，它允许开发人员使用 MCP 将 [API 集合](https://thenewstack.io/introduction-to-api-management/) 转换为可调用的代理工具。Lane 解释说，MCP 服务器将是开发人员访问 PayPal 将为代理 AI 商务提供的工具的方式。（要了解为什么除了 API 之外还需要 MCP，请查看工程师 Frank Fiegel 对 [MCP 与 API 的区别](https://glama.ai/blog/2025-06-06-mcp-vs-api) 的解释。）

PayPal 有兴趣拥有的代理 AI 交易的一部分是身份识别。

Lane 告诉 The New Stack：“我们认为提供诸如身份信息之类的东西，只是验证我是否是我所说的那个人，这在未来可能非常有价值。”

PayPal 的 MCP 服务器使 AI 代理能够通过 PayPal 发起和管理支付处理。它提供对交易历史记录、帐户信息以及有关付款争议或索赔的信息的访问。它还与 PayPal 的发票或订阅管理功能交互。

[PayPal 的 MCP 服务器](https://www.postman.com/paypal/paypal-public-api-workspace/collection/6830d951bcd2d577d7632320) 可通过 Postman 新的 [MCP 服务器精选网络](https://www.postman.com/explore/mcp-servers) 获得，该网络上周在洛杉矶举行的 Post/Con 2025 上宣布。
Lane 解释说，MCP 服务器实际上只是 API 之上的丰富数据。

他说：“Postman 提供的一大好处是真正帮助那些今天可能拥有 API 的人将它们带入这个 AI 世界。”“AI 的一大优点是，代理或 AI 工具实际上可以通过 MCP 服务器开始将这些不同的工具和服务组合在一起，并且基本上可以 [非常容易地构建](https://thenewstack.io/tutorial-build-a-simple-mcp-server-with-claude-desktop/) 我们以前没有的许多体验。”

## 管理用户界面
Lane 说，当 PayPal 了解到有多少体验从传统的 API 世界转移到新的 AI 代理世界时，“非常惊喜”。但他补充说，为 AI 开发时，有些事情变得很重要。

“我们建议开发人员考虑并处理体验上的差异。在我们看来，一个经典的例子是，当有人想购买东西时，那是真金白银的流动——这是我们希望谨慎对待的事情，”他说。

在当今世界，这意味着多因素身份验证。AI 也需要相同级别的验证，但它可能看起来不同，因为现在启用了许多其他类型的交互，例如聊天提示，他说。

事实上，AI 可以支持多种模式，这意味着您的内容可以以与您计划的不同的格式交付。例如，内容可以被总结并读给某人听，而不是以视觉方式查看。

但是，这可能会给企业带来问题。并非所有客户端或代理都具有强大的视觉体验，但产品目录可能主要依赖于图片，Lane 说。

他说：“作为一家企业，您可能想考虑是否有不同的方法可以向人们提供图片？或者，如果不是图片，还有其他方法可以告诉和展示人们，如果我去购买这个东西，我会得到什么，”他说。“MCP 服务器和 AI 的一个优势是，它确实突然使您的信息和体验有可能在许多不同类型的用户界面上可用。”

他补充说，如果无法很好地支持某些类型的界面选项，前端开发人员可能必须阻止某些类型的界面选项。

## 提升 API 以适应 AI
Lane 的同事，PayPal 首席产品经理 [Rebecca Hauck](https://www.linkedin.com/in/rebecca-hauck/) 在 Post/Con 会议上介绍了 PayPal 在 AI 的 [API 设计](https://roadmap.sh/api-design) 方面的经验。她说，本质上，这意味着 API 开发必须“升级”才能成为一个优秀的 AI 公民。

她说：“我们通常努力做到清晰的文档、符合逻辑的端点，也许还有一些示例代码，但 AI 不像我们那样阅读文档，所以我们需要认识到 AI 的角色、视角和能力，”她说。“AI 需要在 API 本身中具有结构和上下文，才能理解如何正确使用它。因此，我们需要进化到下一个层次。”

她补充说，开发人员必须认识到 AI 不仅仅是一个工具，而是一种新的 API 消费者形式。

Hauck 说：“这意味着重新思考[我们设计 API 的方式](https://thenewstack.io/how-radical-api-design-changed-the-way-we-access-databases/)，以便它们可以被机器和人可靠地解释和使用。”“简而言之，这意味着创建清晰、易于使用且对人类和 AI 系统都有效的 API，以便它们可以轻松地相互理解并顺利协作。”

这转化为一些具体的要求。首先，API 和支持文档必须明确，因为与人类不同，如果文档不清楚，AI 不会“修补”以弄清楚文档的含义。

她说，API 和文档必须是可预测和透明的。

她说：“API 应该说到做到。”“[AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 依赖于一致性。如果行为发生意外变化，它们就会迷失方向。强大的模式设计仍然是实现这一目标的关键。”

她补充说，因此，遵循 [OpenAPI](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) 和 [JSON](https://thenewstack.io/how-we-built-the-new-json-api-for-cassandra-and-astra-db/) 等格式非常重要。

她说：“API 模式更像是一份合同。”“它就像 AI 的作弊表。它告诉他们期望什么、如何表现以及边界是什么。”

除了解释 API 可以做什么（通常在文档中涵盖）之外，开发人员还应该更进一步，解释 API 为什么要做什么以及何时应该使用它。她建议，告诉 AI 端点是做什么用的，目标是什么，以及何时应该使用它。

Hauck 说：“我们可能认为一个端点非常直观，但如果 AI 无法弄清楚它，或者它做什么或如何调用它，那就完蛋了。”“目标不是选择一个受众而不是另一个受众。而是以一种支持所有 API 消费者和公民的方式进行设计。”

[元数据](https://thenewstack.io/use-ai-to-improve-your-organizations-metadata/)也变得更加重要。
Hauck 说：“结构化格式的元数据提供了额外的上下文，使代理可以做更多的事情，而不仅仅是盲目地四处摸索。”“这就像在你的工具箱中标记所有东西，这样即使是机器人也能弄清楚该使用什么以及何时使用。”

她补充说，MCP 解决了许多这些问题。它提供了一个额外的[语义层](https://thenewstack.io/demystifying-the-metrics-store-and-semantic-layer/)，作为 API 合同的附录，特别是对于[大型语言模型](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)（LLM）。她说，它添加了其他无法通过 API 访问的功能。

最后，她说，不要忘记实际的[问题，例如安全性](https://thenewstack.io/shadow-zombie-and-misconfigured-apis-are-a-security-issue/)。

她说，Postman 为组织提供了一种沙箱，用于测试 API 是否为开发人员和人类而设计。

她对 Post/Con 的观众说：“Postman 不再仅仅是供人类开发人员测试端点使用的。”“我们还可以使用它来设计和模拟基于 LLM 的代理如何与我们的 API 交互。”

她建议，开发人员应该通过创建示例调用和模拟来测试 API 对开发人员和代理的有效性，这些示例调用和模拟显示了开发人员和代理将如何“走”过一个工作流程。

虽然 API 传统上一直专注于[开发者体验](https://thenewstack.io/api-governance-and-developer-experience-in-a-developer-portal/)，但它们现在必须专注于代理体验，她强调说。

她说：“这完全是关于设计机器代理（如 LLM 和自主工具）可以理解而不会感到困惑或卡住的 API。”“这意味着诸如丰富的元数据、一致的模式、清晰的命名[和]结构化响应等，人们和代理都可以使用。”

*Postman 支付了 Loraine Lawson 的差旅费和住宿费，以报道 Post/Con。*

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)