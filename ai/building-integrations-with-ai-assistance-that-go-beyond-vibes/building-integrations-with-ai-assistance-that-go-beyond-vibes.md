
<!--
title: 构建AI集成：不止于Vibe
cover: https://cdn.thenewstack.io/media/2025/07/5be1246a-integrations-ai-beyond-vibes.jpg
summary: 本文介绍了Docusign Developer AI Assistant，它通过提供集成的规划建议、代码生成和身份验证帮助，以负责任的方式进行“氛围编程”的编程。该助手旨在补充通用LLM，确保信息的及时性和准确性，尤其是在集成生产环境时，应谨慎使用，并将其作为学习辅助工具。
-->

本文介绍了Docusign Developer AI Assistant，它通过提供集成的规划建议、代码生成和身份验证帮助，以负责任的方式进行氛围编程。该助手旨在补充通用LLM，确保信息的及时性和准确性，尤其是在集成生产环境时，应谨慎使用，并将其作为学习辅助工具。

> 译自：[Building Integrations With AI Assistance That Go Beyond Vibes](https://thenewstack.io/building-integrations-with-ai-assistance-that-go-beyond-vibes/)
> 
> 作者：Paige Rossi

如今，氛围编程（Vibe coding）的编程方式非常流行，而且有了这么多人工智能驱动的工具，使得这种方式变得非常容易，因此很容易随波逐流，让像 GitHub Copilot 这样的工具来接管一切。但有时，比如在构建生产集成时，仅仅依靠感觉来编写代码是不够的。

尤其是在规划集成的架构，或决定使用第三方平台的哪些功能时，[大型语言模型（LLM）](https://thenewstack.io/introduction-to-llms)可能没有经过最新的信息训练。这使得人在决策过程中显得尤为重要。然而，当与您不熟悉的平台构建集成时，浏览无数的文档页面以快速上手可能会非常痛苦。

多年来，构建集成的开发人员一直面临着这一挑战，软件供应商也尝试了无数种方法来缩短学习曲线，从而提高生产力。[Docusign Developer AI Assistant for VS Code](https://developers.docusign.com/tools/ai-assistant-vs-code/)（目前处于 Beta 阶段）作为一个新的尝试，为这个长期存在的问题提供了一个潜在的解决方案。在本文中，我将向您介绍 Developer AI Assistant 如何帮助您以负责任的方式，氛围编程来编码 Docusign 集成。

## 安装 Developer AI Assistant

Docusign Developer AI Assistant 在 Visual Studio Code (VS Code) 市场中以扩展的形式提供。该助手基于 GitHub Copilot 运行，因此您还需要一个 [GitHub Copilot](https://github.com/features/copilot) 许可证或免费试用版，并且需要在 VS Code 中安装 [GitHub Copilot 扩展](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)。安装扩展后，您可以在 VS Code 中打开 Copilot 聊天窗口，并通过 `@Docusign` 将 Developer AI Assistant 添加到对话中。系统会提示您登录 Docusign 开发者帐户。

## 通过探索阶段氛围编程

开发人员在氛围编程时可能遇到的主要陷阱之一是，LLM 并不总是具有构建集成最佳选项所需的完整上下文。LLM 只知道它们经过训练的内容，并且由于文档经常更新，因此它们有时会返回过时的信息。用专门针对第三方提供商的信息进行训练的 AI 工具来补充更通用的 LLM 会很有帮助，这样您就可以相信他们的输入是最新的和准确的。

您可以将 AI 助手引入到项目的规划阶段，并咨询哪些 API 或其他 Docusign 产品最适合您的用例，而不是立即生成代码。

假设您想将数据从 Docusign 工作流程写入 Salesforce，但您不知道该怎么做。只需询问 AI 助手：

[![将数据从 Docusign 工作流程写入 Salesforce 的提示](https://cdn.thenewstack.io/media/2025/07/0cc2bc67-write-data-to-salesforce-prompt.png)](https://cdn.thenewstack.io/media/2025/07/0cc2bc67-write-data-to-salesforce-prompt.png)

*来源：Docusign*

该助手概述了集成的两个选项，一个使用 Docusign [Apex Toolkit](https://developers.docusign.com/docs/salesforce/salesforce101/apex-toolkit/)，另一个使用 [扩展应用程序](https://thenewstack.io/auto-read-data-into-agreement-workflows-with-docusign-extension-apps) 和 [Maestro 工作流程](https://developers.docusign.com/extension-apps/workflows/)。这两种解决方案都在较高的层次上进行了概述，而没有深入到细节中。

工作原理如下：如果我不熟悉 Developer AI Assistant 提到的任何概念，我可以简单地询问在哪里可以了解更多信息，助手会向我提供一个文档链接列表，并简要描述每个文档涵盖的内容。虽然它可能无法完全消除阅读文档的需要，但 Developer AI Assistant 为开发人员提供了一个直接进入相关文档的入口点，从而消除了构建实现过程的发现阶段中不必要的摩擦。

[![了解更多信息的提示](https://cdn.thenewstack.io/media/2025/07/6e31342e-learn-more-prompt.png)](https://cdn.thenewstack.io/media/2025/07/6e31342e-learn-more-prompt.png)

*来源：Docusign*

现在我有了更多信息，我可以从助手最初的回复中选择我想使用的选项，并获得有关如何实现它的分步说明。

[![获取实施步骤的提示](https://cdn.thenewstack.io/media/2025/07/b057cdf6-extension-steps.png)](https://cdn.thenewstack.io/media/2025/07/b057cdf6-extension-steps.png)

*来源：Docusign*

在不具备 Docusign 产品先验知识的情况下，您可以与 Developer AI Assistant 聊天，以了解最适合您用例的解决方案。您可以向助手描述您的问题，以实时了解潜在的解决方案，而无需花费时间阅读文档。

如果您立即开始氛围编程，那么您向 AI 助手发出的提示可能会比较模糊，并且可能无法引导您找到正确的解决方案。在本例中，您可能不知道要询问有关 [扩展应用程序](https://developers.docusign.com/extension-apps/) 的信息，但由于您花了一些时间描述您的问题，因此 Developer AI Assistant 能够将扩展应用程序识别为潜在的解决方案。

## 氛围编程检查：生成一些代码

如果您想拥抱氛围编程并让助手接管，您可以要求它以您选择的语言为您生成一些代码。

按照我之前的示例，一旦我构建了一个将数据写回 Salesforce 的工作流程，我就可以要求助手帮助我用 Node.js 编写一些代码来触发该工作流程。助手返回的第一个代码只是通过 [Maestro API](https://developers.docusign.com/docs/maestro-api/maestro101/) 触发了一个工作流程，但需要我硬编码我的工作流程 ID。经过更多的指导，助手能够返回一些代码，这些代码通过 API 调用 [获取工作流程](https://thenewstack.io/build-api-driven-custom-agreement-workflows-with-docusign-maestro) ID，然后触发该工作流程。

[![生成代码的提示](https://cdn.thenewstack.io/media/2025/07/fba7e87c-workflow-code.png)](https://cdn.thenewstack.io/media/2025/07/fba7e87c-workflow-code.png)

*来源：Docusign*

## 通过身份验证保持势头

在许多方面，氛围编程最适合原型设计，即您刚开始一个项目并且有更多的出错空间时。要运行 Developer AI Assistant 给我的代码，我需要一个访问令牌。

我可以要求助手生成一些为我进行身份验证的代码，或者帮助我理解 [可用的不同身份验证类型](https://www.docusign.com/blog/developers/demystifying-docusign-authentication)。但由于我只是在构建一个原型，并且我想在构建完整的实现之前了解它是如何工作的，因此我现在不想被身份验证所困扰。相反，我可以立即开始运行代码，方法是使用命令 `@docusign /getAccessToken` 要求助手为我生成一个访问令牌。

[![获取用于身份验证的访问令牌的提示](https://cdn.thenewstack.io/media/2025/07/21ee70b6-get-access-token.png)](https://cdn.thenewstack.io/media/2025/07/21ee70b6-get-access-token.png)

*来源：Docusign*

## 超越感觉的 AI 辅助

当然，当您准备好完全构建集成的生产版本时，您需要实施身份验证，并且在生产开发阶段您可能无法过多地依赖氛围编程。在开发生命周期的那个阶段，将 AI 工具用作学习辅助工具，而不是依赖它们为您生成代码，可能会最有帮助。

在氛围编程时保持理智非常重要 - 您不希望将任何不良因素引入生产环境。但是，借助受信任的工具，您可以平衡氛围编程和其他 AI 辅助的见解，以确保您从知情的地方构建集成。通过仔细考虑您使用的工具以及您使用它们的方式，可以在避免氛围编程的陷阱的同时，仍然使用 AI 来简化您的开发体验。