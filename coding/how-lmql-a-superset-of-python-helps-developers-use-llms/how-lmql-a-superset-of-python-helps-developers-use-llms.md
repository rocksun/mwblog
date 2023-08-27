# LMQL 是 Python 的超集，帮助开发者使用大型语言模型

据其创作者表示，一种新的 Python 超集编程语言使开发者能够从大型语言模型中提取更多价值。

翻译自 [How LMQL, a Superset of Python, Helps Developers Use LLMs](https://thenewstack.io/how-lmql-a-superset-of-python-helps-developers-use-llms/) 。

![](https://cdn.thenewstack.io/media/2023/08/6733d591-google-deepmind-luzt78a1g7m-unsplash-1024x576.jpg)

与 ChatGPT 交谈相对简单，但自然语言在与这些[大语言模型](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/)进行交互时也存在局限性。

“关于自然语言的问题在于，从定义上来说，它不是正式语言，而是一种非正式的语言形式，这意味着它不够精确，”瑞士苏黎世联邦理工学院（ETH Zürich）计算机科学系的博士生 [Luca Beurer-Kellner](https://github.com/lbeurerkellner) 说道，他还是 Secure, Reliable, and Intelligent Systems 实验室的一员。“你当然可以试图在使用自然语言时保持非常精确，但这显然有其限制。”

在五月份发表的[一篇学术论文](https://arxiv.org/pdf/2212.06094.pdf)中，Beurer-Kellner 与 [Marc Fischer](https://twitter.com/marc_r_fischer) 以及 [Martin Vechev](https://www.sri.inf.ethz.ch/people/martin) 提出了与生成式人工智能模型互动的另一种方式：[语言模型查询语言](https://github.com/eth-sri/lmql)（LMQL），这是一种设计用于与大型语言模型一起工作或互动的编程语言，它允许进行轻量级脚本编写、约束输出，除了自然语言查询之外。

“我们观察到的根本问题是……你与它们（LLMs）的工作方式，你提示它们，询问它们关于各种事情，以便为你完成各种任务，” Beurer-Kellner 告诉 The New Stack。 “我们发现这在某种程度上与编程存在某种相似之处，因为最初，我们的研究小组也专注于编程语言研究和机器学习研究的交叉领域。”

## LMQL 有助于从 LLMs 中提取更多价值

Beurer-Kellner 告诉 The New Stack，LMQL 是 [Python](https://thenewstack.io/python-gets-its-mojo-working-for-ai/) 的超集，它允许开发者在自然语言之上利用编程语言的正式方面。他说，这使得它更精确、更方便使用，同时对人们来说仍然易于理解和直观。

![](https://cdn.thenewstack.io/media/2023/08/9bcceb8f-lmql-use-this.png)
*来自“Prompting Is Programming: A Query Language for Large Language Models”的截屏。*

这也可以用于从大型语言模型中释放更多潜力。他补充说，LMQL 可以建立一个接口，可以在聊天机器人的限制之外受益于 LLMs 和机器学习。

“从机器学习的角度来看，非常有趣的一点是，这些模型可以做各种各样的事情，” Beurer-Kellner 说道。 “它们实际上可以与你进行对话，但它们真正擅长的是分类模型，或者它们可以进行实体标记，图像字幕等各种事情，尽管从根本上来说，它们是文本输入/文本输出。”

他说，LLMs 也可以建模为下游应用程序。这使它们成为各种领域的即用型机器学习模型，无需进行任何训练。

“通过限制并将模型强制到一定的结构和模板中，您可以确保模型始终遵循您事先定义的接口，”他说。 “这不仅仅是通过期望最好的并提示模型真正这样做，而是实际上以严格的方式强制模型，意味着在任何情况下，您都将获得是/否回答。如果您指定它这样做，模型确实没有其他方式来生成任何其他标记。”

当 LLMs 进行预测时，它们实际上在计算令牌。基本上，每个单词都是一个令牌，或者被分为几个令牌。

##使用 LMQL 可以节省 API 成本

LMQL 还是一种声明性语言，这意味着编程语言描述要做什么，而不是如何做。SQL 和 HTML 是声明性语言。然而，它也具有命令式语言（如 C、C++、Java 和 Python）的一些方面。这些语言描述如何做某事。

“[如果] 您希望某个输出始终是整数，例如，这些事情我们用声明性方式表示，这也使 LMQL 看起来几乎像 SQL。但是，当您构建输入并且希望从外部源拉入一些数据或将不同的内容连接在一起时，这可以采用完全命令式的风格，就像在 Python 中一样，” Beurer-Kellner 解释道。 “我们试图为这些不同方面实现不同的范式，以确保所有这些方面都以更或多或少方便的方式得到满足。”

使用 LMQL 的一个有用的副作用是，它实际上可以通过减少或缩短模型的 API 调用来减少使用 LLMs 的成本，LMQL 的创作者发现了这一点。

这一点非常重要：语言模型通常是非常大的神经网络，实际推理需要高计算成本和显著的延迟，该论文解释道。这可能导致每个查询在付费使用的API中的使用成本很高。

例如，如果模型正在生成超出所需响应，LMQL 可以帮助早早地拦截它，以确保它不会离题，他说道。

“我们实际上可以在文本生成过程中限制模型的空间或继续……，”他说。 “即使它在某个方向上跑偏，我们也可以早早地进行干预，这意味着我们可以提前终止并确保它不会生成很多不需要的文本；而所有这些您最终不会生成的文本，您都可以在计算或 API 成本上节省下来。”