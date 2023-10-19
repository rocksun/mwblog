<!--
# 利用AI辅助工具Userdoc定义软件需求
https://cdn.thenewstack.io/media/2023/10/69f6b3f1-kaleidico-7lryofj0h9s-unsplash-1024x683.jpg
Image via Unsplash

 -->

Userdoc是一个AI辅助服务，可以帮助创建软件需求文档。在最近举行的AI工程师峰会上，笔者与Userdoc的创始人Chris Rickard进行了交流。

译自 [AI for Dev Tools: Create Software Requirements with Userdoc](https://thenewstack.io/ai-for-dev-tools-create-software-requirements-with-userdoc/) 。

## 利用AI服务Userdoc定义软件需求

[AI编码工具](https://thenewstack.io/learning-while-coding-how-llms-teach-you-implicitly/)现已成为软件开发的标准配置，但生成式AI的应用也在向[开发流程](https://thenewstack.io/ai-improves-developer-workflow-says-gradle-dev-evangelist/)的其他方面扩散。[Userdoc](https://userdoc.fyi/)是一个初创公司，他们开发了一个AI辅助服务，用于定义软件需求。在[上周于旧金山举行的AI工程师峰会](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)上，笔者与Userdoc的联合创始人兼首席开发者[Chris Rickard](https://www.linkedin.com/in/chrickard/)进行了交流，探讨他创建Userdoc的初衷，以及它将如何帮助开发者。

在一个新项目中，确定软件将要实现的功能以满足一个或多个“用户角色(personas)”的需求，通常是第一步。

“构建优秀软件的关键之一，是定义准确的需求，以确保开发的方向正确。”Rickard表示，“我很感兴趣AI如何促进这个过程，帮助发现可能导致漏洞的问题所在；更糟的是，发现巨大的系统功能其实并未解决原始问题，或者根本就不需要。”

![](https://cdn.thenewstack.io/media/2023/10/a5f5e509-userdoc3-scaled.jpg)

*Userdoc*

Userdoc允许用户先输入业务相关的背景信息，作为AI理解需求的上下文。Rickard向我演示了一个例子，一个杂货配送企业使用Userdoc为配送员定义需求。在这样的场景下，AI可以对开发者构建系统提供一定的“监督”作用。

“在这个例子里，人工智能就像一个业务分析师，”Rickard说，“它理解相关变更的其他影响。”

## 直接用ChatGPT定义需求有何不同?

这一切听起来不错，但是相比直接使用ChatGPT，Userdoc的AI生成软件需求有什么不同呢?

Rickard回答说，ChatGPT存在“编造信息”的风险。他补充说，Userdoc使用GPT-4作为底层技术，但是业务背景才是关键。

“所以，当我们与GPT-4交互时，”他说，“我们提供系统的所有其他相关信息作为上下文。”

他承认，ChatGPT也可以实现类似的功能，但需要构建一个“巨大的提示”，才能得到与Userdoc类似的响应。

每个Userdoc项目通常包含一系列“用户故事”，这些故事对应软件中的各项功能。如果一个系统有成百上千的功能，事情就会变得非常复杂，这正是Userdoc试图解决的痛点之一。

“我们这里试图解决的一个大问题是，”Rickard说，“当一个系统拥有繁杂的功能时，[开发人员]需要考虑和记忆很多细节；软件成本和进度超支的一个重要原因，是人们在前期没有把这些小细节想清楚。”

## Userdoc的使用

创建一个新的Userdoc项目，需要通过向导输入用户信息和各种需求目标。这个设置工作通常由产品负责人、产品经理和业务分析师完成，之后项目移交给开发团队。但Rickard表示，Userdoc也可以直接帮助开发者。

“一旦特征和需求确定后，[...]可以和项目管理工具集成。它可以连接到Jira、Azure DevOps等，与工作项的待办、进行中、已完成状态保持同步，这样就能随时查看每个功能的详细信息。”

![](https://cdn.thenewstack.io/media/2023/10/ab58508d-userdoc1.jpg)

*Userdoc 向导*

Rickard指出，在某些情况下，开发人员也参与需求的确定。所以开发者如何使用Userdoc，需要根据具体业务需求来决定。在返回项目后，它也是一个很好的参考。

“我们与许多有大量并行项目的机构合作，”他说，“开发人员和设计师在项目后期返回时，就可以通过Userdoc快速了解当前需实现的功能。”

Rickard还说，Userdoc中的信息也可以成为系统的“活文档”。

“如果一开始就用相当详细的需求，并持续更新，作为业务可以参考的唯一版本，那么它就成为了[软件系统]的准确信息来源。”

## 考虑 LangChain

既然我们在AI工程师峰会上交流，我想了解Rickard是否有使用[AI工程界当前热门的工具](https://thenewstack.io/llm-app-ecosystem-whats-new-and-how-cloud-native-is-adapting/)。由于Userdoc使用GPT-4，我问他是否将[LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)作为与OpenAI模型通信的中间层？

“我在Userdoc第一个原型中确实用了LangChain几周，”他说，“但后来想更清楚背后运行的细节，这对我理解其中的区别很有帮助。LangChain无疑很强大，但是它的优势在于提供了处理某些任务的便捷方法，如将文档分块，将其发送给LLM，并提出问题。我同时学习LLM和LangChain时，很难区分两者的边界。所以我自己编写了一套与GPT-4交互的组件。”

## Userdoc的扩展

如果Userdoc随时间沉淀可以成为软件文档的源头，那么它是否也可以用来为客户提供帮助聊天机器人(例如，为那个杂货配送服务)？

“答案是肯定的，”Rickard说，“主要考量是内部知识和外部公开的区分，以及人们的信息安全意愿。”

他指出，Userdoc目前是自举的，如果扩充团队，他更希望从事软件合规方面的工作。所以他情愿朝这个方向发展，而不是重复做网站和App的客户聊天机器人。

“我非常认同这个理念，确保软件开发真正实现业务最初同意的需求，”他解释说，“开发者现在可以使用各种自动化测试，我希望AI可以增强这个验证过程。”