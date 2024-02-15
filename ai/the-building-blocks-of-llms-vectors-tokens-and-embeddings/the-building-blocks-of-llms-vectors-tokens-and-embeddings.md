<!--
title: LLM的构建基石：向量、Token和嵌入
cover: https://cdn.thenewstack.io/media/2024/02/adcb521f-la-rel-easter-kucglbxjh_o-unsplash-1024x683-1.jpg
-->

理解向量、Token和嵌入对于理解大型语言模型处理语言的方式至关重要。

> 译自 [The Building Blocks of LLMs: Vectors, Tokens and Embeddings](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/)，作者 Janakiram MSV。

当你处理 LLMs 时，你经常会遇到术语“向量”，“Token”和“嵌入”。在深入构建聊天机器人和 AI 助手之前，充分理解这些概念非常重要。随着[多模态](https://thenewstack.io/building-ai-driven-applications-with-a-multimodal-approach/)方法的兴起，这些术语不仅仅局限于大型语言模型（LLMs），还可以解释图像和视频。

本教程的目标是通过简单、直接的例子和代码片段向你介绍这些核心概念。

## 向量：机器的语言

向量在 LLMs 和生成式人工智能的功能中起着至关重要的作用。要理解它们的重要性，就必须了解向量是什么，以及它们在 LLMs 中如何生成和利用。

在数学和物理学中，向量是具有大小和方向的对象。它可以在几何上表示为一个有向线段，线段的长度表示大小，箭头指向向量的方向。向量在表示那些不能完全用一个数字描述的量时起着基础作用，例如力、速度或位移，这些量既有大小又有方向。

在 LLMs 的领域中，向量被用来表示文本或数据的数值形式，以便模型能够理解和处理。这种表示被称为嵌入。嵌入是捕捉单词、句子甚至整个文档语义含义的高维向量。将文本转换为嵌入的过程使得 LLMs 能够执行各种自然语言处理任务，如文本生成、情感分析等。

> 简单来说，向量是一个单一维度的数组。

由于机器只能理解数字，因此文本和图像等数据被转换为向量。向量是神经网络和变压器架构能够理解的唯一格式。

对向量进行的操作，如点积，帮助我们发现两个向量是否相同或不同。在高层次上，这构成了在存储在内存中或专门的向量数据库中的向量上执行相似性搜索的基础。

下面的代码片段介绍了向量的基本概念。正如你所见，它是一个简单的一维数组：

```python
import numpy as np
 
# Creating a vector from a list
vector = np.array([1, 2, 3])
print("Vector:", vector)
 
# Vector addition
vector2 = np.array([4, 5, 6])
sum_vector = vector + vector2
print("Vector addition:", sum_vector)
 
# Scalar multiplication
scalar = 2
scaled_vector = vector * scalar
print("Scalar multiplication:", scaled_vector)
```

虽然上面显示的向量与文本没有关联，但它传达了这个概念。我们在下一节探讨的"Token"是在向量中表示文本的机制。

## Token：LLM 的基本组成单元

Token是由LLMs处理的基本数据单元。在文本的背景下，一个Token可以是一个单词、单词的一部分（子词）或甚至是一个字符，这取决于Token化过程。

当文本通过Token器传递时，它根据特定的方案对输入进行编码，并发出可以被LLM理解的专门向量。编码方案高度依赖于LLM。Token器可能决定将每个单词和单词的一部分转换为基于编码的向量。当一个Token通过解码器传递时，它可以很容易地再次转换为文本。

通常将LLMs的上下文长度称为主要的区分因素之一。从技术上讲，它映射到LLMs接受特定数量的Token作为输入并生成另一组Token作为输出的能力。Token器负责将提示（输入）编码为Token，并将响应（输出）再次编码为文本。

> Token是文本的向量表示形式。

下面的代码片段解释了如何将文本转换为Token，以供像Llama 2这样的开放模型和像GPT-4这样的商业模型使用。这些都基于Hugging Face的transformers模块和OpenAI的Tiktoken。

```python
from transformers import AutoTokenizer
 
model = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model,token="HF_TOKEN")
 
text = "Apple is a fruit"
 
token = tokenizer.encode(text)
print(token)
 
decoded_text = tokenizer.decode(token)
print(decoded_text)
```

![](https://cdn.thenewstack.io/media/2024/02/a6f7ca16-llama_token-1024x407.png)

```python
import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-4")

text = "Apple is a fruit"

token = tokenizer.encode(text)
print(token)

decoded_text = tokenizer.decode(token)
print(decoded_text)
```

![](https://cdn.thenewstack.io/media/2024/02/141191d7-tiktoken.png)

所以，关键要点是Token是基于特定 tokenizer 的向量。

## 嵌入：语义空间

如果Token是文本的向量表示，那么嵌入就是带有语义上下文的Token。它们表示文本的含义和上下文。如果Token由Token器编码或解码，那么嵌入模型负责生成文本嵌入，形式为向量。嵌入使得LLMs能够理解单词和短语的上下文、细微差别和微妙含义。它们是模型从大量文本数据中学习的结果，不仅编码了Token的身份，还编码了它与其他Token的关系。

> 嵌入是LLMs的基础方面。

通过嵌入，LLMs 实现了对语言的深入理解，实现了情感分析、文本摘要和问题回答等任务，具有细致的理解和生成能力。它们是LLMs的入口点，但它们也被用于LLMs之外，将文本转换为向量同时保留语义上下文。当文本通过嵌入模型传递时，会产生包含嵌入的向量。下面是来自开源嵌入模型 sentence-transformers/all-MiniLM-L6-v2 以及 OpenAI 模型 text-embedding-3-small 的示例。

```python
from sentence_transformers import SentenceTransformer

sentences = ["Apple is a fruit", "Car is a vehicle"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

print(len(embeddings[0]))

print(embeddings)
```

![](https://cdn.thenewstack.io/media/2024/02/14d78892-minilm-1020x1024.png)

```python
from openai import OpenAI

client = OpenAI(api_key="OPENAI_API_KEY")

model = "text-embedding-3-small"
sentences = ["Apple is a fruit", "Car is a vehicle"]

embeddings = client.embeddings.create(input=sentences, model=model).data[0].embedding

print(len(embeddings))

print(embeddings)
```

![](https://cdn.thenewstack.io/media/2024/02/31130346-text-ada-1024x899.png)

## 比较和交互

**Token vs. 向量**：Token是语言单位，而向量是这些单位的数学表示。在LLMs的处理流程中，每个Token都映射到一个向量。

**向量 vs. 嵌入**：所有嵌入都是向量，但并非所有向量都是嵌入。嵌入是经过专门训练以捕捉深层语义关系的向量。

**Token与嵌入**：从Token到嵌入的转变代表了从语言的离散表示到细致、连续且具有上下文感知的语义空间的移动。

理解向量、Token和嵌入对于把握LLMs如何处理语言至关重要。Token作为基本的数据单元，向量提供了机器处理的数学框架，而嵌入则带来了深度和理解，使LLMs能够以类似人类的多才多艺和准确性执行任务。这些组件共同构成了LLM技术的支柱，推动着今天AI应用的先进语言模型。
