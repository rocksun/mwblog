<!--
title: 如何从数据库生成“AI”：Bruce Momjian
cover: https://cdn.thenewstack.io/media/2025/02/3ed2bd43-bruce-monjian.jpg
summary: EDB 副总裁 Bruce Momjian 解读数据库如何赋能 AI。关键技术包括：向量处理、word2vec 模型、LLM 训练和状态转换器。通过 PGVector 扩展，可实现基于向量的语义搜索。注意力机制模块和 RAG 进一步提升生成式 AI 的能力，但需注意 LLM 本质是复杂的数据操作。
-->

EDB 副总裁 Bruce Momjian 解读数据库如何赋能 AI。关键技术包括：**向量处理**、**word2vec** 模型、**LLM** 训练和**状态转换器**。通过 **PGVector** 扩展，可实现基于向量的语义搜索。**注意力机制模块**和 **RAG** 进一步提升生成式 AI 的能力，但需注意 LLM 本质是复杂的数据操作。

> 译自：[How To Generate 'AI' From a Database: Bruce Momjian](https://thenewstack.io/how-to-generate-ai-from-a-database-bruce-momjian/)
> 
> 作者：Joab Jackson

下次你向 ChatGPT 或其他生成式 AI 服务提问时，请注意你得到的答案中单词的顺序。

你的查询中的最后几个词几乎总是生成的回复中的前几个词。

[Bruce Momjian](https://momjian.us/)指出，这是大型语言模型 (LLM) 工作的一个重要过程——向后评估每个词相对于前一个词——他是 [EDB](https://www.enterprisedb.com/?utm_content=inline+mention)的副总裁和 [Postgres](https://thenewstack.io/the-slow-climb-of-postgres-and-the-value-of-persistence/) 的推广者，在上个月在布鲁塞尔举行的 [FOSDEM 2025](https://fosdem.org/2025/schedule/) 的一次演讲中说道。

Momjian 以数据库技术为出发点，向观众介绍了数据如何转化为 AI，以及为什么我们还不应该将数据操作误认为是真正的人类智能。

## 从描述性到生成性

在 2022 年之前，我们所知的“AI”主要是区分和澄清的任务，AI 会回答诸如“狗还是猫？”或信用卡交易是否真实等问题。它非常适合预测、分类、推荐。

新的“AI”，以 [ChatGPT 的即时成功](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/) 为代表，是关于生成以前不存在的内容：摘要、聊天机器人、语义搜索、图像、编程、声音和视频的创建。

生成式 AI 实际上是在*生成*新内容，而不是像早期的预测性 AI 那样寻找边界。

“我们正处于狂野西部。我们实际上并不知道我们可以做的所有事情，”Momjian 说。

## 庞大的向量宇宙

这种方法的关键始于 [向量处理](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/)。Google 在 2018 年的一篇论文中率先提出了这项技术，该论文题为“[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781)”，并提供了一个名为 [word2vec](https://www.tensorflow.org/text/tutorials/word2vec) 的模型。

向量是一个具有两个数字的数学对象，即大小（长度）和方向。

[训练数据](https://thenewstack.io/pyconus-simon-willison-on-hacking-llms-for-fun-and-profit/)中的每个词都有一个与其他每个词的向量，形成一个高度维度的向量空间。（为了简单起见，Momjian 专注于基于文本的生成式 AI，尽管图像和其他形式的内容生成也基于类似的原理）。

![Slide showing generative vector.](https://cdn.thenewstack.io/media/2025/03/6e38898c-fosdem-momjian-databases_ai-vectors.png)

*幻灯片：Bruce Momjian*

这个词的宇宙确实非常大。

“我们处理的规模远远超出了我们可以在物理世界中理解的任何事物，”Momjian 说。

ChatGPT LLM 可以 [拥有多达](https://community.openai.com/t/what-version-of-gpt-is-text-embedding-ada-002-based-on/404462) 12,288 个维度，总计超过 10 的 188,000 次方个维度，这远远超过了宇宙中原子的总数，Momjian 指出。

每个词的向量都具有相同的长度。它还被分配了一个方向，一个随机的浮点数，存在于这个 10 的 188,000 次方维度的宇宙中的某个地方。

## 训练日

下一步是将大量的训练文档 [输入到这个空间中](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/)。

对于每个词，它的向量将被调整为更接近其周围的词，并且对于它的每个周围的词，使其更接近原始词。

在这个著名的训练数据集里：

*The king is a tall man.*
*The queen is a beautiful woman.*
*They sit together in the throne room of the castle.*

向量“king”向“man”弯曲，“queen”向“woman”弯曲，“throne”向“castle”弯曲，依此类推，在数千个维度上相乘。

经过连续的迭代，“man”和“woman”等词将越来越接近，而“king”和“queen”也将越来越接近。

另请注意，“man”和“woman”的距离与“king”和“queen”的距离相似，这使得 LLM 可以进行一些基本的数学运算，以进一步理解词之间的关系。

而且，由于维度非常多，在一个维度上将一个词移动到更接近另一个词的位置，并不一定意味着这些词与其他词的距离会更远。

“当我们把‘man’移近‘woman’时，我们不一定把它移离‘king’更远，因为‘king’与‘man’的接近程度可能与‘man’与‘woman’的接近程度不在同一个维度上，”Momjian 说。

## 从数据到智能
关系型数据库确实提供全文搜索，但不搜索单词的含义。这就是基于向量的语义搜索的强大之处。

通常，在 [LLM 训练过程](https://thenewstack.io/3-ways-llms-can-let-you-down/)中，文本块可以“分块”成较短的段落。它们可以被分成句子、段落，或者整个段落可以是一个单独的块。

语义搜索对每个块的所有向量分数进行平均。

然后，生成式 AI 对查询本身中的向量进行平均，并找到得分最接近的句子或文本块。

因此，查询“谁是国王？”将最接近于“国王是一个高个子男人”这句话的平均值，这意味着这句话的平均向量最接近于查询的平均向量。

Momjian 展示了 [一些 SQL 代码](https://momjian.us/main/writings/pgsql/trenches.sql) 来实现这个示例，可以使用 [PGVector](https://github.com/pgvector/pgvector)（PostGreSQL 的向量扩展）来执行。他创建了一个表来保存内容，以及一个表来保存它们嵌入。Momjian 创建了一个 Python 脚本，调用 OpenAI，发送每个单词并取回一个嵌入。向量被平均并存储在数据库中。

然后，通过 API 调用将查询“谁是国王？”发送到 [OpenAI](https://platform.openai.com/docs/overview) 以获取嵌入数字。它也被平均，然后与数据库中的所有平均值进行比较，这些平均值从最相似到最不相似进行排序：

![Comparing vector scores](https://cdn.thenewstack.io/media/2025/03/916ed384-fosdem-momjian-databases_ai-vector-compare.png)

比较最接近匹配的向量分数

Momjian 说：“这与全文搜索不同，因为它理解单词之间的关系。”

## 生成式 AI

Momjian 解释说，向量处理只是生成式 AI 的第一个模块。要生成完整的句子，还需要 [状态转换器](https://thenewstack.io/get-ready-for-faster-text-generation-with-diffusion-llms/)，这是一种用于 [自然语言处理](https://thenewstack.io/recent-advances-deep-learning-natural-language-processing/) 的 [神经网络](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)。

[注意力机制模块](https://www.datacamp.com/blog/attention-mechanism-in-llms-intuition)（也是 [谷歌在 2017 年率先提出的](https://arxiv.org/abs/1706.03762)）是输入文本的加权版本。每个查询都会获得一个新的注意力机制模块。从 LLM 中查找每个单词并给出 128 维数字。输入文本中的每个单词都被加权，以便更接近其他单词，逐个单词地进行。

![](https://cdn.thenewstack.io/media/2025/03/a0493345-fosdem-momjian-databases_ai-attention_block.png)

在向量空间中将单词移动到一起的这个过程会持续多次迭代，直到生成一个完整的句子。

这就是为什么你的 ChatGPT 答案中的最后一个短语通常会首先出现在答案中——“法国的首都是巴黎”——因为它最后被向量化。LLM 以相反的顺序解释一个句子：

*哥伦布在俄亥俄州。巴黎在哪里？*

…可能会给你带来这个答案：

*巴黎在法国。美国德克萨斯州也有一个名为巴黎的城市。如果您指的是不同的巴黎，请具体说明！*

答案还可以通过 [检索增强生成](https://thenewstack.io/rag-and-model-optimization-a-practical-guide-to-ai/) 进一步完善，这为 LLM 提供了额外的指令，例如保持回复简洁。在这种情况下，关于巴黎位置的问题将得到简单的回复，即巴黎在法国。

你还可以使用 RAG 来返回 [数据分析问题](https://thenewstack.io/save-valuable-genai-tokens-with-this-one-simple-trick/) 的答案。例如，Momjian 展示了如何将三个 SQL 数据库插入输入到 RAG 前缀中，它将返回每个命令被提交的数据，因为 LLM“知道”SQL。

总而言之，Momjian 总结说，虽然 AI 的发展速度确实惊人，但 LLM 仍然是一种复杂的数据操作形式，不具备任何实际的感知能力。

*在此处欣赏 Momjian 的完整[演示](https://fosdem.org/2025/schedule/event/fosdem-2025-4748-databases-in-the-ai-trenches/)文稿。幻灯片可在[此处](https://momjian.us/main/writings/pgsql/trenches.pdf)获得。*