# 为什么API是必不可少的，而MCP是可选的（目前）

![Featued image for: Why APIs Are Essential and MCP Is Optional (for Now)](https://cdn.thenewstack.io/media/2025/05/0f4eef27-douglas-lopes-ehyv_xoz4ia-unsplash-1-1024x683.jpg)

[Douglas Lopes](https://unsplash.com/@douglasamarelo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)在 [Unsplash](https://unsplash.com/photos/a-laptop-computer-sitting-on-top-of-a-wooden-desk-ehyV_XOZ4iA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)上发布。

AI助手在产品体验中正变得越来越重要，并且出现了一个新的标准来帮助构建它们：模型上下文协议（Model Context Protocol，MCP）。随着Anthropic、OpenAI和Gemini等主要大型语言模型（LLM）提供商的采用，该协议已在更广泛的软件生态系统中迅速获得关注，各公司都在构建自己的MCP服务器。

作为[构建MCP服务器](https://thenewstack.io/tutorial-build-a-simple-mcp-server-with-claude-desktop/)和API集成的人员，我看到这种快速采用导致了混乱。一些开发人员和产品经理将MCP视为API的替代品，而另一些人则认为MCP不如API。

现实情况更为微妙：MCP和API是互补的。许多精心设计的AI系统都需要两者，并且一些AI工程师可能不会构建一个足够复杂的系统来保证使用MCP。

为了帮助您了解哪种解决方案适合您的特定场景，我将解释每种解决方案的工作方式、其局限性以及它们如何协同工作。

**MCP和API如何协同工作**

MCP的核心是为大型语言模型提供了一种与外部数据源交互的标准化方式，但这些交互通常通过现有的API进行。例如，当LLM从MCP服务器调用一个工具以在Jira中创建一个工单时，仍然会向相关的Jira端点发出API调用。

MCP的价值在于它[管理LLM和数据之间的上下文](https://thenewstack.io/aws-brings-trusted-extension-support-to-managed-postgres/)源。它为以下方面提供了一个标准化的框架：

*   **工具选择和调用：**MCP允许LLM根据用户提示动态选择要使用的工具，而不是需要硬编码的API调用。
*   **上下文保留：**该协议帮助LLM保留、更新和获取上下文，这对于管理多步骤工作流程至关重要。
*   **简化的交互：**MCP通过提供标准协议，使LLM和应用程序更容易集成。

同时，[API仍然处理核心数据](https://thenewstack.io/the-fundamentals-of-data-api-design/)传输、身份验证流程以及与不同应用程序的连接。

**MCP的安全挑战需要API级别的解决方案**

MCP的灵活和[开放式架构引入了独特的安全](https://thenewstack.io/the-3-ss-of-software-supply-chain-security-sboms-signing-slimming/)挑战。开发人员希望使用尽可能多的工具（API端点）。这导致密钥通常具有对敏感服务（如电子邮件、机密计划工具和销售数据）的全面访问权限。另一个例子是，LLM可能会错误地理解字段标签（将“SN”误认为是社会安全号码而不是姓氏），并无意中暴露敏感数据。

为了防止出现这种情况，工程师需要集成访问控制级别、模式强制执行和数据丢失防护。最有效的方法是将MCP的上下文[管理功能与强大的API基础设施](https://thenewstack.io/ansible-vs-salt-which-is-best-for-configuration-management/)相结合。

例如，API提供商的身份验证方法（例如，OAuth 2.0）使LLM能够确认用户是否具有访问底层API端点所需的权限。API提供商的响应代码可以帮助您的LLM诊断和解决问题（例如，在请求失败时提醒用户并提供解决方案）。

**大多数AI用例只需要API**

我看到AI团队采用MCP来掩盖更深层次的问题，例如组织混乱的检索系统、失控的提示链以及团队之间缺乏明确的约定。他们没有修复架构，而是添加了另一层，导致更多的抽象和更少的清晰度。

这些AI团队还不需要MCP；他们只需要[清理他们的提示和数据](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/)管道（通过构建强大的API集成）。如果一个团队只是使用MCP来组织基础设施层，那可能还为时过早。
当您已经积累了一定的复杂性时，MCP会非常强大：需要处理多个模型、来源和下游消费者，并且需要结构化的合约。但在那之前，请考虑首先在您的基础设施中构建一致性，然后实施自动化的策略来进行归档、去重和权限管理，以减少手动开销并保持秩序。

**了解何时以及如何利用它们将为您带来竞争优势**

随着我们构建日益复杂的AI助手，至关重要的是要理解MCP和API是集成生态系统中互补的层。MCP提供了上下文管理层，帮助LLM更有效地与外部系统交互，而[APIs提供安全的](https://thenewstack.io/the-state-of-api-management-in-an-age-of-ai-insecurity/)、可靠的连接到这些系统。

那些成功构建真正有用的AI助手的公司将认识到这种关系，并在构建有效的MCP实现（如果确实有必要）之前，投资于强大的API基础设施、有组织的检索系统和标准化的约定。

[技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)