<!--
title:AI与React结合，打造更智能的前端
cover: https://cdn.thenewstack.io/media/2023/11/0619b605-lautaro-andreani-uysbcu9rp3y-unsplash-1024x683.jpg
-->

MongoDB资深开发者倡导者Jesse Hall阐述了将人工智能技术融入React应用的基础框架。

> 译自 [Combining AI with React for a Smarter Frontend](https://thenewstack.io/combining-ai-with-react-for-a-smarter-frontend/)，作者 Loraine Lawson 是一位资深的技术记者，她已经报道了从数据集成到安全性等技术问题25年。在加入The New Stack之前，她担任银行技术网站Bank Automation News的编辑。她已经......

前端开发在不久的将来就不可避免的要结合人工智能。然而，最紧迫的问题是，这到底意味着什么，一定非要是聊天机器人吗？

[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline-mention)的高级开发者倡导者[Jesse Hall](https://github.com/codeSTACKr)在上周第二届[React峰会美国](https://thenewstack.io/rachel-nabors-on-revamping-reacts-documentation/)虚拟日上说："几乎每个应用程序在某种程度上都将使用AI，AI会无视所有人。为了保持竞争力，我们需要在应用程序中构建智能，以便从数据中获得丰富的洞察力。"

## React AI应用的技术栈

首先，开发人员可以采取自定义数据(图像、博客、视频、文章、PDF等)，并使用嵌入模型生成嵌入，然后将这些嵌入存储在向量数据库中。他补充说，这并不需要LangChain，但LangChain可以有助于促进这一过程。一旦创建了嵌入，就可以接受自然语言查询来查找相关的自定义数据信息。

![](https://cdn.thenewstack.io/media/2023/11/329786cc-jesse-hall-ragii.png)

*MongoDB高级开发倡导者Jesse Hall解释了RAG工作流程。*

“我们将用户的自然语言查询发送到LLM，LLM将查询向量化，然后我们使用向量搜索找到与用户查询语义相关的信息，然后返回结果”。

例如，结果可能提供文本摘要或指向特定文档页面的链接。

想象一下，你的React应用程序有一个基于RAG [检索增强生成] 和向量嵌入的智能聊天机器人。这个聊天机器人可以获取实时数据，可能是最新的产品库存，并在客户服务互动过程中提供它，[使用] RAG和向量嵌入。你的React应用程序不仅很智能，还可以适应、实时和非常意识上下文。

为此提供一个技术栈，他建议开发人员可以使用包含[Vercel的app Router](https://thenewstack.io/vercels-next-js-14-introduces-partial-pre-rendering/)的Next.js 13.5版本，然后连接OpenAI的Chat GPT 3.5、Turbo和GPT 4。然后，LangChain可以是栈的关键部分，因为它有助于数据预处理、将数据路由到适当的存储以及使应用程序的AI部分更高效。他还建议使用[Vercel的AI SDK](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/)，这是一个开源库，用于构建会话式的流式用户界面。

然后，对于MongoDB的开发者倡导者来说，不出所料，他建议利用[MongoDB](https://thenewstack.io/mongodb-builds-out-its-full-platform-play/)来存储向量嵌入和MongoDB Atlas向量搜索。

这是AI应用程序的游戏规则，通过直接在我们的应用程序数据库中存储我们的向量嵌入，而不是添加另一个外部服务，我们可以提供一个更加上下文和有意义的用户体验。它不仅仅是向量搜索。MongoDB Atlas本身为我们的生成AI能力带来了一个新的能力级别。

他说，结合使用这些技术栈将能够实现更智能、更强大的React应用程序。

请记住，未来不仅仅是更智能的AI，还有它集成到以你的下一个基于React的项目为代表的以用户为中心的平台中的程度。

## 如何对付GPTs

创建YouTube show [codeSTACKr](https://www.youtube.com/c/codeSTACKr)的Hall还拆解了开发人员需要掌握的术语和技术，以便将人工智能合并到其React应用程序中，从对通用预训练模型(GPTs)的处理开始。

这不仅仅是利用[React](https://thenewstack.io/redwood-framework-all-in-on-react-server-components/)中的GPT力量。这是通过使它们变得更智能和更具上下文感知能力来使React应用程序达到下一个级别。我们不仅将AI集成到React中，我们还对其进行了优化，使其尽可能智能和意识上下文。

他补充说，为应用程序构建智能和为用户创造更快、更加个性化的体验的需求巨大。更智能的应用程序将使用AI驱动的模型代表用户进行自治操作。这可能看起来像一个聊天机器人，但它也可能是个性化建议和欺诈检测。

Hall说，结果将是双重的。

首先，你的应用程序通过深化用户参与和满意度来获得竞争优势，因为他们与你的应用程序进行交互。其次，你的应用可以通过在更新、更准确的数据上更快地做出明智的决定，来实现更高的效率和利润。

AI将被用来驱动应用程序面向用户的方面，但它也将导致来自这些交互的“新鲜数据和洞察力”，而这些洞察力将驱动一个更高效的业务决策模型。

## GPTs，满足React

深入研究GPTs，也就是[大语言模型](https://thenewstack.io/what-is-a-large-language-model/)，他指出GPTs不是完美的。

它们的一个关键局限性是知识库静态。它们只知道它们所接受的训练。一些模型现在的集成可以搜索互联网以获取更多信息。但是我们怎么知道它们在互联网上找到的信息是否准确？我不得不补充一点，它们可以非常自信地产生幻觉。那么我们如何最大限度地减少这种情况呢？

通过使用React、大语言模型和RAG，可以使这些模型实时化、适应性更强、更符合特定需求。

我们不仅将AI集成到React中，我们还对其进行了优化，使其尽可能智能和意识上下文。

他解释了RAG的相关内容，从向量开始。向量是允许开发人员以易于操作和理解的格式表示复杂的多维数据的基本构建块。有时，向量被称为[向量嵌入](https://thenewstack.io/comparing-different-vector-embeddings/)或嵌入。

最简单的解释是一个向量是数据的数字表示和数字数组。这些数字是n维空间中的坐标，其中n是数组的长度。所以，我们数组中的数字数量决定了我们的维数。

例如，视频游戏使用2D和3D坐标来知道游戏世界中的对象在哪里。但Hall说，在AI中使向量变得重要的是，它们实现了语义搜索。

简单来说，它们允许我们找到与上下文相关的信息，而不仅仅是关键词搜索。数据源不仅限于文本。它也可以是图像、视频或音频——所有这些都可以转换为向量。

所以第一步就是创建向量，而做到这一点的方法是通过一个编码器。编码器定义信息在虚拟空间中的组织方式，并且有不同类型的编码器可以以不同的方式组织向量。例如，有用于文本、音频、图像等的编码器。大多数流行的编码器都可以在[Hugging Face](https://thenewstack.io/hugging-face-aws-partner-to-help-devs-jump-start-ai-use/)或[OpenAI](https://thenewstack.io/openai-chats-about-scaling-llms-at-anyscales-ray-summit/)上找到。

最后，RAG发挥了作用。[根据IBM的说法](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)，RAG是“一个AI框架，用于从外部知识库中检索行为，以便基于最准确、最新的数据来解释[大语言模型](https://thenewstack.io/meeting-the-operational-challenges-of-training-llms/)(LLM)，并向用户展示LLM的生成过程”。

它的实现方式是将生成模型与[向量数据库](https://thenewstack.io/grounding-transformer-large-language-models-with-vector-databases/)和[LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)结合起来。

“RAG利用向量来获取实时、与上下文相关的数据，并增强LLM的功能”。矢量搜索功能可以通过提供内存或基本事实来增强GPT模型的性能和准确性，以减少幻觉，提供最新信息，并允许访问私人数据。
