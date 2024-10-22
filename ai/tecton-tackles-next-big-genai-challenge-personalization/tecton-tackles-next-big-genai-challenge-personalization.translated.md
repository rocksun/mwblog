# Tecton 应对下一代生成式 AI 的重大挑战：个性化

![Featued image for: Tecton Tackles Next Big GenAI Challenge: Personalization](https://cdn.thenewstack.io/media/2024/10/1ecae9cc-tecton-1024x683.jpg)

仅仅拥有一个经过良好调优的模型不足以在生成式 AI 中取得成功。您还需要将其牢固地连接到业务实践中。

“现在每个人都可以访问相同的模型。每个人都可以使用 OpenAI 或 Anthropic，因此每个人在 AI 应用的某个部分都处于相同的最低共同点，”Tecton 首席执行官兼联合创始人 [Mike Del Balso](https://www.linkedin.com/in/michaeldelbalso/) 在与 The New Stack 的对话中解释道。“真正的竞争优势来自您收集了哪些数据以及您可以继续收集和使用哪些数据。”

## 推向生产

Tecton 的使命是 [提供一个平台](https://thenewstack.io/tecton-helps-data-scientists-own-features-and-the-model-lifecycle/) 来完成像 Uber 和 Netflix 这样的规模化公司所拥有的数千名工程师的工作，以便小型企业能够获得类似的结果，从而使他们能够轻松地测试其数据的新的 AI 应用，然后将结果产品化。

对于 Tecton 来说，每家公司都有可能成为 Pinterest、Uber 或 Instagram；它们都只是简单地重新包装用户生成的数据，并以新颖且有用的方式将其反馈给用户。

该公司引用了 Gartner 的数据，Gartner 发现只有 [53% 的 AI 项目最终投入生产](https://www.forbes.com/councils/forbestechcouncil/2023/04/10/why-most-machine-learning-applications-fail-to-deploy/#)，这表明组织在将他们对 [大型语言模型](https://thenewstack.io/how-to-increase-plasticity-in-llms-and-ai-applications/) (LLM) 的实验产品化到他们自己的动态业务环境中时遇到了困难。[LLM 需要特定的公司和客户](https://thenewstack.io/new-ai-dev-platform-allows-you-to-customize-open-source-llms/) 信息，以便为用户有意义地个性化信息。

在加速发展之前，Tecton Del Balso 和 Tecton 首席技术官 [Kevin Stumpf](https://www.linkedin.com/in/kevinstumpf/) 曾在 Uber 团队中，该团队构建了 Uber 的第一个机器学习平台之一，称为 [Michelangelo](https://www.uber.com/blog/michelangelo-machine-learning-platform/)，该平台 [专注于使 ML 流程对业务开发团队更易访问](https://www.tecton.ai/resources/how-michelangelo-ml-enabled-uber-to-scale-up-its-ml-models-mike-del-balso-tecton)。

“如果你把工具用对了，它就能让公司快速扩展其 AI 应用，”Del Balso 说，并指出 Michelangelo 使 Uber 在两年内从没有 AI 到生产中拥有数千个模型。

积累数据是 ML 模型构建中的一个重要过程，但将模型连接到业务流程同样重要。

## Tecton 1.0

现在，该公司已 [扩展其平台](https://www.tecton.ai/blog/expanding-tecton-to-activate-data-for-genai/)，以帮助组织个性化其生成式 AI 应用，以更好地满足其用户的需求。

一个重要的新功能是嵌入。这项服务将非结构化文本转换为捕获语义含义的数值向量，因此它可以被 [生成式 AI 应用](https://thenewstack.io/agents-shift-genai-from-order-takers-to-collaborators/) 使用。例如，它可以用于捕获 [情绪](https://thenewstack.io/machine-learning-for-twitter-sentiment-analysis/) 和用户评论的关键方面。Tecton 管理整个嵌入过程，为用户提供软件开发工具包 (SDK) 来识别要嵌入的表格。

“所以现在我们可以将结构化和非结构化数据都作为嵌入进行处理，而嵌入可以用于传统的机器学习模型和生成式 AI 模型，并实时提供服务，”Del Balso 说。

![Tecton 个性化图表。](https://cdn.thenewstack.io/media/2024/10/b7991ec3-tecton-image2-1024x389.webp)
来源：Tecton。

另一个新功能是特征检索 API。这种集成提供了一种方法，使 LLM 可以访问实时和流式数据，这些数据可以用于用户行为、交易和运营指标。这些数据可以用于根据有关个人的上下文（或者，正如 Del Balso 所称的，“超级个性化”）来定制用户体验。

对于客户服务应用来说，一个由 LLM 驱动的应用还可以整合来自客户最近购买的数据。一个旅游网站可以根据对客户之前旅程的了解，推荐新的目的地。一个美食网站可以推荐一家刚开业的餐厅，专门提供用户最喜欢的菜肴。
几乎在每家公司，“都有一些数据以特定方式被锁定，而负责 AI 团队的人员并非负责构建整套数据基础设施以连接这两者的人员。您确实需要一个高质量的桥梁来连接这些系统，才能使您的数据和 AI 应用程序协同工作，成为一个 AI 产品，”Del Balso 说。“我们已经构建了这座桥梁。”

刚刚发布的 Tecton 1.0 的其他新功能有助于个性化，包括：

* **动态、版本控制的提示**提供了一种方法，使应用程序能够将个人数据注入提示本身。Tecton 还提供版本控制、更改跟踪以及在必要时轻松回滚提示。
* **工程师的自然语言界面**利用 LLM 允许开发人员和工程师通过自然语言来表达他们想要构建的功能或数据格式。

“开发人员很喜欢它，”Del Balso 说。“它使他们的一些工作更快，但也使他们能够实现以前从未实现过的事情。”