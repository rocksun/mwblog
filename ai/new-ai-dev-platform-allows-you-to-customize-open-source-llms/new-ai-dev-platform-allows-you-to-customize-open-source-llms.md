<!--
# 新推出的AI开发平台让您可自定义开源大语言模型
https://cdn.thenewstack.io/media/2023/11/1e8b4b98-gradient_llama3-1024x573.jpg
Image via Gradient. 
-->

Gradient承诺通过开源大语言模型帮助开发者构建自定义的AI系统。我们采访了其CEO Chris Chang(前Netflix AI工程师)。

译自 [New AI Dev Platform Allows You to Customize Open Source LLMs](https://thenewstack.io/new-ai-dev-platform-allows-you-to-customize-open-source-llms/) 。

Gradient是今年新推出的大语言模型(LLM)应用开发平台之一。它引起我注意的原因有两个：一是它的创始人包括前Netflix、谷歌和Splunk的AI团队成员；二是Gradient承诺[基于开源大语言模型](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)帮助开发者构建定制的AI系统。

后者表明大语言模型生态正在趋向成熟——开源通常意味着软件市场的扩张——依赖度不再仅限于OpenAI和谷歌等公司的专有系统。

为了进一步了解[Gradient](https://gradient.ai/)为开发者提供的内容，我采访了联合创始人兼CEO [Chris Chang](https://www.linkedin.com/in/chriscchang/)，他之前是Netflix“Studio AI”的主管。

Chang解释说，Gradient的开发者平台使用户能够在自己的数据集上训练开源大语言模型，包括运行推理和微调模型。到目前为止，支持的开源模型只有三个——Llama-2、Bloom-560和Nous-Hermes-Llama-2——[但Gradient表示](https://docs.gradient.ai/docs/faqs)“我们正在积极增加更多开源模型以供微调”。

Gradient称其方法为“专家混合”或“多模型系统”，根据Chang的说法。注意他说的是多`模型`，而不是多`模式`——后者涉及不同媒体形式(如图像、视频)，而多模型就是使用多个大语言模型。Chang补充说，“这一切都是通过API接口实现的”，因此“非常面向开发者，对开发者也很友好，真正目的是简化所需的基础架构”。

## 开发工具

开发者可以通过两种方式使用Gradient。第一种是通过该公司的网页界面——基本上是一个软件即服务平台。或者，开发者可以通过其软件开发工具包使用Gradient的API。

对于网页界面，Chang说，您通常需要“上传训练数据集，选择用于训练的模型，然后启动微调任务”。

Chang表示，网页界面是针对“不太擅长开发的用户设计的——可能是更习惯处理数据而不是在平台上开发的分析师或数据科学家”。

而对于专业开发者，他继续说，“软件开发工具包和命令行界面也允许您以编程方式在这些模型上进行开发”。

软件开发工具包有[两种形式](https://docs.gradient.ai/docs/sdk-quickstart): Python和JavaScript。

![](https://cdn.thenewstack.io/media/2023/11/7667d1bd-gradient_js_sdk.png)

*JavaScript 软件开发工具包示例*

与许多新兴大语言模型应用平台一样，Gradient与两种流行的AI工程框架兼容得很好: [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)和[LlamaIndex](https://thenewstack.io/llamaindex-and-the-new-world-of-llm-orchestration-frameworks/)。它还与[向量数据库](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/)集成良好。

开发者需要注意的最后一点是，Gradient托管[嵌入](https://thenewstack.io/how-to-get-the-right-vector-embeddings/)向量，尽管目前微调嵌入向量是企业专享功能。

“我们为嵌入向量提供支持，”Chang说。“所以我们不仅在平台上托管可微调的大语言模型，还有嵌入向量。目前微调嵌入向量仅面向企业客户，但我们也在努力将其引入自助服务产品。”

## 并非全都是开源: Gradient的行业定制大语言模型

虽然其网站强调开源模型，但Gradient也开发了自己的专有大语言模型。它们是面向医疗保健和金融等行业的定制化大语言模型，可在Gradient的企业云平台上使用。

在医疗保健领域，Gradient最近推出了[Nightingale](https://gradient.ai/healthcare)，被描述为“具备医学学位的大语言模型”。除了在医学数据上进行训练，Gradient还声称它“了解逻辑推理的最佳实践”(假设是为了帮助其进行诊断)。在金融领域，Gradient推出了[Albatross](https://gradient.ai/finance)，这是一个“在投资、监管、教育和专属金融记录数据上进行训练的大语言模型”。

对于医疗保健解决方案，Chang说目前主要有以下几个使用案例。首先是特定医疗领域的结构化数据处理——例如组织患者的病例和账单历史。其次是他标记的“面向用户的体验”，包括聊天机器人。第三个主要用例是知识管理，“为管理团队构建知识库以访问机构知识”，用Chang的话说。  

## 企业AI开发面临的挑战

我询问了Gradient的早期企业客户在使用大语言模型开发应用时遇到的痛点。

“我认为最有意思的领域是围绕微调、检索增强生成[RAG]、提示工程存在的一些基本误解，”Chang回复说。“当我们谈论定制AI解决方案时，它并非非此即彼，而是需要综合运用这三项技术。”

他说，很多时候人们试图仅依赖这三项中的一项。

“这些不同技术提供了很多选择，也可以通过多种方式导致失败，”他表示，“所以我们试图在这方面提供更多指导。”

他还指出，在大语言模型上完成这三项任务仍然“极其复杂”。为微调设置基础设施并让其与现有框架配合运行可能非常具挑战性，他警告说。

Gradient以开发者为目标用户，因此提供了处理所有后端复杂性的服务。Chang只希望开发者使用其API。他说: “调用它，我们确保它每次都可靠运行。”

## AI工程师需要什么技能？

最后，我想听听Chang对[AI工程师](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)这一新兴角色在IT部门中的看法。他认为这是一个热门角色吗？

“所以，我们的观点是，AI工程师来自各种技术背景，”他说。“我们见过的有分析师转型成AI工程师，数据工程师转型成AI工程师，产品工程师转型成AI工程师，当然还有机器学习工程师转型成AI工程师。”

根据Chang的说法，担任AI工程师的角色不需要专门的知识集。

“你现在需要思考的问题空间是，推理实际业务用例，推理数据来源，以及在训练模型、提示模型或部署AI服务时找到批判性分析出现情况的方法。”

Chang认为这些都是通用的技能组合，这也解释了为何现在许多技术角色正在转型成所谓的AI工程师。

“在我们看来，世界将朝着‘任何人都可以成为AI工程师’的方向发展——我们的产品也是为此设计的。”
