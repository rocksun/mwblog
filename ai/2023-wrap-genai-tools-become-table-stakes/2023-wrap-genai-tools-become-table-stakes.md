<!--
title: 2023生成式AI大盘点
cover: https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png
-->

2023年，生成式AI在协助开发者构建应用方面取得突破，各大工具商纷纷推出产品，以满足开发者的实际需求。

> 译自 [Generative AI: In 2023, GenAI Tools Became Table Stakes](https://thenewstack.io/2023-wrap-genai-tools-become-table-stakes/)，作者 Darryl K. Taft  从他位于巴尔的摩地区的办公室报道了 DevOps、软件开发工具和开发者相关的问题。他在该行业有超过 25 年的经验，一直在寻找下一个重大新闻。他曾在......

[很长一段时间以来](https://www.eweek.com/development/ibm-watson-provides-self-service-ai-for-developers/)，我一直想知道人工智能如何能更好地支持软件开发者的工作。

2023年 对于软件开发领域的人工智能而言是一个关键的一年，像 [GitHub 的 Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 这样的工具进化到可以帮助开发者构建应用程序的程度。

至少十年来，我断断续续地向我的技术伙伴 [Grady Booch](https://www.linkedin.com/in/gradybooch/) 提出这个问题。他是 [IBM](https://www.ibm.com/?utm_content=inline-mention) 研究院的首席软件工程师，也是 IBM 的 Fellow。起初，他认为人工智能在[软件开发](https://thenewstack.io/software-development/)中会有用处，但他对其作用持怀疑态度。

他仍持这种态度。去年年底，Booch 在 [Twitter(现在是 X)上](https://twitter.com/Grady_Booch/status/1595878463298105344)与 Replit CEO [Amjad Masad](https://www.linkedin.com/in/amjadmasad/) 就人工智能对开发者的贡献进行了一次交锋。Masad 写道，随着人工智能模型的进步，到某个时候，"世界上每个人都至少会[具备 John Carmack 级别的软件开发能力](https://twitter.com/amasad/status/1595557798850461702?lang=en)"。Carmack 是一位知名的游戏开发者([Doom](https://en.wikipedia.org/wiki/Doom_(1993_video_game)) 等游戏的共同创造者)，也是 AR/VR 大师，曾任 Oculus VR 的 CTO 和 [Meta](https://about.meta.com/?utm_content=inline-mention) 收购 Oculus 后任咨询 CTO。

不过，我们现在还远未达到那个阶段。但是 2023 年对于[开发者生产力](https://thenewstack.io/how-generative-ai-can-increase-developer-productivity-now/)的人工智能而言是一个巨大的一年。

"2023年确实是人工智能辅助编程和软件开发的关键之年"，Omdia 的应用智能首席分析师 [Lian Jye Su](https://www.linkedin.com/in/lianjye/?originalSubdomain=sg) 通过电子邮件告诉 The New Stack。"Copilot 和其他生成式人工智能工具在用作开发者工具时展现出了高度的准确性、自动化和最重要的灵活性。开发者可以使用自然语言来表达他们的意图，并专注于创造性和评估方面，因为工具会处理枯燥的部分。"

"因此，一些开发者使用这些工具生成近 40% 的代码。除了 Copilot，其他关键工具包括 OpenAI Codex、Replit、[Tabnine](https://www.tabnine.com/?utm_content=inline-mention)、Codacy 和 Durable。"

JetBrains 关于[开发者生态系统状况](https://thenewstack.io/jetbrains-developer-survey-tracks-rapid-adoption-of-ai-chatgpt/)的最新[研究](https://blog.jetbrains.com/team/2023/11/20/the-state-of-developer-ecosystem-2023/)显示，如果有机会，56% 的受访者会让[人工智能助手编写](https://www.jetbrains.com/lp/devecosystem-2023/ai/#ai_delegate_activities)代码注释和文档。

## Copilot 的演变

与此同时，46% 的受访者表示他们[使用 Copilot](https://www.jetbrains.com/lp/devecosystem-2023/ai/#ai_tools_experience)。

GitHub 在 2022 年 6 月启动了其代码自动完成功能/结对编程工具 Copilot。它现在拥有超过 150 万用户，GitHub 首席产品官 [Inbal Shani](https://www.linkedin.com/in/inbalshani/) 在接受 The New Stack 采访时表示。此外，使用 Copilot 编写的新代码的百分比已从 35% 增长到 60%，预计在未来几年将达到 80-90%，她说。

像 GitHub Copilot 这样的人工智能驱动的开发者工具正在经历大规模增长，并在软件开发中产生变革性影响，对生产力、质量和工作满意度具有积极作用，Shani 指出。

开发者采用人工智能工具的情况呈指数增长。根据 GitHub 的数据，现在有 92% 的开发者在工作中使用某种形式的人工智能。这在很大程度上得益于使人工智能普及化的 GenAI 模型的兴起。

像 GitHub Copilot 这样的人工智能辅助工具现在可以生成完整的代码块、代码的解释、文档以及对开发者问题的回答。这可以更快地帮助新开发者上手，微软开发者部门的产品、设计、用户研究和工程系统公司副总裁[阿曼达·西尔弗](https://www.linkedin.com/in/amandaksilver/)(Amanda Silver)在接受 The New Stack 的视频采访时表示。

此外，Copilot 可以优化和重构代码、排除故障、建议安全修复、辅助调试等，从而减少对多个领域深厚专业知识的需求，她解释道。

在内部，随着微软工程师构建自己的产品，他们会对 Copilot 的功能进行“[吃自己的狗粮](https://thenewstack.io/what-launchdarkly-learned-from-eating-its-own-dog-food/)”，为 GitHub 提供反馈来改进该技术。的确，微软工程师使用 Copilot 执行内部系统的大规模迁移，这也帮助测试了其大规模重构能力，西尔弗说。

## 对代码 Whispering

虽然亚马逊去年也推出了其 Copilot 竞争对手 [CodeWhisperer](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-codewhisperer-the-ml-powered-coding-companion/)，与 Copilot 和其他工具一样，2023 年看到它作为日常使用工具出现。亚马逊 [CodeWhisperer](https://aws.amazon.com/codewhisperer) 是一个利用[机器学习](https://thenewstack.io/the-ultimate-guide-to-machine-learning-frameworks/)为开发者提供基于开发者自然注释和先前代码的代码建议从而提高开发者生产力的服务。

[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline-mention)在生成式人工智能方面迎来了一个大年，推出了 CodeWhisperer 生成可用性，用于构建自定义人工智能应用程序的 [Bedrock](https://aws.amazon.com/bedrock/)，以及目前处于预览阶段的无代码人工智能应用程序构建工具 [PartyRock](https://aws.amazon.com/about-aws/whats-new/2023/11/partyrock-amazon-bedrock-playground/)。在去年秋天的 re:Invent 上，该公司还宣布了 [Amazon Q](https://thenewstack.io/amazon-q-a-genai-to-understand-aws-and-your-business-docs/)，这是一种专为工作而定制的 GenAI 助手，可以根据组织的业务进行定制。

亚马逊的研究显示，CodeWhisperer 实现了 50-60% 的开发者生产力提升，而定制化等功能进一步提升了它，亚马逊网络服务人工智能平台的软件开发总监兼 CodeWhisperer 和 [Amazon Q](https://aws.amazon.com/q/) 总经理 [Doug Seven](https://www.linkedin.com/in/dseven/) 在接受 The New Stack 采访时表示。

"亚马逊在人工智能方面具有竞争力，因为它的工作横跨从针对人工智能工作负载优化的芯片到利用人工智能的开发者工具的整个技术栈"，Seven 说。

## 整个行业

直到 2023 年，在整个数字计算的历史上，编程的核心活动一直是人类编写代码行。一些人工智能工具已经出现来增强这种能力，但人类编码始终处于中心位置。

这已经改变了，Intellyx 的分析师[杰森·布隆伯格](https://www.linkedin.com/in/jasonbloomberg/)(Jason Bloomberg)通过电子邮件告诉 The New Stack。他说:"如今，随着编程活动的发展，人工智能(主要是生成式人工智能和神经网络)创建应用程序已经成为核心。人类创建和管理模型和训练人工智能的数据集，而不是编写代码。"

当然，手动编码仍在继续——但布隆伯格说，他认为它已经进入了一个次要位置。他说:"任何没有意识到这一点的组织、供应商或企业都注定会变得缺乏竞争力，最终变得无关紧要。"

确实，正如 GitHub 的 Shani 所说，"人工智能现在是软件开发的基本配置。"GitHub 正致力于用其工具覆盖软件开发生命周期(SDLC)的更多方面。

Gartner 分析师[托马斯·墨菲](https://www.linkedin.com/in/thomasmurphy4/)(Thomas Murphy)通过电子邮件表示："显然，Copilot 凭借上市时间和量而脱颖而出，但其他像 Tabnine、CodeStory、Codium 等工具也都在扩展"生成式人工智能空间。除了 AWS 和谷歌之外，像 [GitLab](https://about.gitlab.com/?utm_content=inline-mention) 和 Atlassian 这样的云提供商也在扩展代码生成和更广泛的人工智能辅助功能，用于 SDLC，他说。

[JetBrains](https://www.jetbrains.com/) 是另一家著名的开发工具制造商，一直在构建自己的人工智能助手功能，并在最新的产品更新中发布了它，主要集中在旗舰集成开发环境(IDE) [IntelliJ IDEA](https://thenewstack.io/jetbrains-formulates-ide-go-called-gogland/) 上。该公司新的[人工智能助手](https://thenewstack.io/jetbrains-launches-new-ai-assistant-powered-by-multiple-llms/)插件引入了不同的功能——它可以"在更高、更抽象的层面上建议代码重构，而不仅仅是修复特定的模式"，JetBrains 开发倡导者 [Matt Ellis](https://www.linkedin.com/in/mtellis/?originalSubdomain=uk) 告诉 The New Stack。

Ellis 说，为未来，该公司希望改进助手使其变得“更智能”，以便它可以利用现有的内部代码索引和元数据更好地理解代码上下文，并探索企业托管其模型的选项。

“像 Copilot 这样的工具在本地代码建议方面表现不错，但缺乏应用程序上下文，”[AppMap](https://thenewstack.io/appmap-releases-runtime-code-review-as-a-github-action/) 首席执行官 [Elizabeth Lawler](https://www.linkedin.com/in/elizabethlawler/) 告诉 The New Stack。“新玩家可以整合可观察性数据、架构信息等，以使建议更准确。”

然而，她说，2023 年使人工智能基础设施和模型足够可访问，以至于现在较小的公司也可以利用可定制的人工智能。这将带来新的增值服务，Lawler 指出。此外，她补充说，人工智能生成的代码仍存在质量问题，但它迫使开发人员批判性地评估建议。

与此同时，从风险投资的角度来看，[Differential Ventures](https://www.differential.vc/) 的创始人兼管理合伙人[尼克·亚当斯](https://www.linkedin.com/in/nickadams11/)(Nick Adams)表示，他正在看到公司利用 [GenAI](https://d.docs.live.net/0b94a229cf596ada/GenAI) 来帮助商业分析师的机会，后者经常编写重复的查询来提取数据。

“人工智能工具可以通过获取业务用户的自然语言问题，生成 SQL 或 Python 中的查询作为起点，并允许分析师完善代码来提供帮助，”亚当斯告诉 The New Stack。“这加快了过程，并避免每次从头开始编写查询。”

他指出，迁移遗留代码(如 [COBOL](https://thenewstack.io/u-s-unemployment-surge-highlights-dire-need-for-cobol-skills/))是另一个机会。这是 [IBM 与其 watsonx](https://newsroom.ibm.com/2023-08-22-IBM-Unveils-watsonx-Generative-AI-Capabilities-to-Accelerate-Mainframe-Application-Modernization) 生成式人工智能将旧 COBOL 代码迁移到 Java 所做的工作。

“许多旧系统现在由即将退休的开发人员编写而接近退休，”亚当斯说。“电气工程也积累了几十年即将退休的专业知识，需要用现代工具和培训传承给新一代。”

## 生成式人工智能和低代码

我曾经认为生成式人工智能会以某种方式取代[低代码、无代码开发](https://thenewstack.io/low-code-vs-no-code/)，但 [Pegasystems](https://thenewstack.io/pega-infinity-23-advances-low-code-application-development/) 的首席技术官兼产品营销副总裁 [Don Schuerman](https://www.linkedin.com/in/donschuerman) 纠正了我的想法。

生成式人工智能正在对软件行业产生重大影响，包括低代码平台，因为可以自动生成代码的工具可能会破坏市场的低端。

“然而，企业级低代码更专注于架构、集成、[DevOps](https://thenewstack.io/devops/)、[安全性](https://thenewstack.io/security/)、可重用性等。这种复杂性不仅仅是关于生成代码片段的。”Schuerman 告诉 The New Stack。

Pegasystems 正在使用生成式人工智能来自动生成低代码工件以加速开发者，例如标准工作流模板、测试数据、流程文档、数据映射等。

亚马逊的 Seven 表示，虽然 CodeWhisperer 可以辅助在 IDE 中工作的专业开发者，但 Party Rock 旨在面向其他群体，例如主题专家，让他们可以用很少或不用代码来构建应用程序。

他说:"我不认为生成式人工智能会使低代码、无代码过时。我认为它会使低代码变得更好。"

关于人工智能是否会取代开发者的问题，Schuerman 说:"我看不到生成式人工智能完全取代开发者。它将通过提供起点和建议来提高他们的生产力。开发人员很少完全从零开始编写所有内容。"

JetBrains 的研究显示，60% 的受访者表示，他们认为[人工智能编码工具将从根本上改变就业市场](https://thenewstack.io/how-will-generative-ai-change-the-tech-job-market/)，51% 的人表示，他们认为这些工具将增加对专业软件开发者的需求。然而，人们一致认为，人工智能永远不会完全接管编写代码的工作。

## 工作室之年

11 月，微软推出了 [Azure AI Studio](https://azure.microsoft.com/en-us/products/ai-studio) 的预览版，这是一种新的平台，它使所有能力和偏好的开发者都可以使用最新的人工智能工具和机器学习模型对人工智能进行创新、探索、构建、测试和部署，这些都基于负责任的人工智能实践，微软人工智能平台项目管理公司副总裁[约翰·蒙特诺默里](https://www.linkedin.com/in/johnmont)(John Montgomery)告诉 The New Stack。

他说:"我们认为人工智能是终极的放大器。这最新一轮的生成式人工智能完全改变了世界。这对应用程序来说是巨大的改变。我在微软工作了 25 年，我从未见过客户采用技术的速度这么快。在不到一年的时间里，我们就有超过 18，000 个客户使用 Azure OpenAI 制作自己的东西。"

例如:他说，Instacart 正在使用配备 Vision 的 [GPT-4 Turbo](https://thenewstack.io/dev-news-gpt-4-turbo-chrome-talks-pretty-and-worlds-merge/)，让用户可以拍一张手写购物列表的照片，并在其应用程序中生成一个虚拟购物列表。

"你可以把人工智能工作室看作是生成式人工智能的终极工具包。" 蒙哥马利说，"它汇集了正确的模型、数据和负责任的人工智能系统，以便客户能够放心，他们的解决方案将是安全、可靠和可扩展的。"

微软宣布支持其自己最新的大型语言模型(LLM)，以及来自 [OpenAI](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/)、Meta、Nvidia、Mistral AI 和 [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 的最新模型。

此外，该公司以 Azure AI 服务的形式宣布了 Azure AI 模型即服务，“这将使客户更容易部署和运行尖端模型”，蒙哥马利说。微软还推出了名为 [prompt flow](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-what-is-prompt-flow?view=azureml-api-2) 的提示工程工具。Prompt flow 是一个高级的提示工程、评估和部署系统，是 Azure AI Studio 和 Azure 机器学习的关键组成部分。

尽管 OpenAI 在这个领域非常重要，与微软有着密切合作，但一位公司发言人告诉 The New Stack，团队无法接受采访。

与此同时，谷歌最近宣布了[谷歌人工智能工作室](https://makersuite.google.com/)，以示不甘落后。谷歌人工智能工作室是一个免费工具，可以让开发者快速开发提示，然后获取 API 密钥在应用开发中使用。它目前在限制内免费使用，谷歌表示其[定价将具有竞争力](https://ai.google.dev/pricing)。

在一次新闻简报中，谷歌实验室副总裁[乔希·伍德沃德](https://www.linkedin.com/in/joshwoodward/)(Josh Woodward)演示了如何使用谷歌帐户登录谷歌人工智能工作室，并利用每分钟 60 次请求的免费配额。伍德沃德还演示了开发人员如何通过简单地点击“获取代码”将他们的工作转移到首选 IDE。

谷歌内部一直在通过代码补全、文档、聊天机器人等多种方式使用其人工智能技术，谷歌开发者体验部门副总裁兼总经理 [Jeanine Banks](https://io.google/2022/speakers/jeanine-banks/) 告诉 The New Stack。她说:"在内部应用这项技术真的给了我们很多学习经验"，公司可以将这些经验带回产品中。

