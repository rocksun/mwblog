<!--
title:增强ChatGPT处理模糊问题能力
cover: https://cdn.thenewstack.io/media/2023/11/c06f6443-chatgpt-refine-prompts-1024x805.jpg
-->

提示工程技术可帮助大语言模型在检索增强生成系统中处理代词等复杂核心参照物。

> 译自 [Improving ChatGPT’s Ability to Understand Ambiguous Prompts](https://thenewstack.io/improving-chatgpts-ability-to-understand-ambiguous-prompts/)，作者 Cheney Zhang 是 Zilliz 的一位杰出的算法工程师。他对前沿 AI 技术如 LLM 和检索增强生成(RAG)具有深厚的热情和专业知识，积极为许多创新 AI 项目做出贡献，包括 Towhee、Akcio 等。

在不断扩大的 AI 领域中，像 [ChatGPT](https://zilliz.com/learn/ChatGPT-Vector-Database-Prompt-as-code?utm_source=vendor&utm_medium=referral&utm_campaign=2021-11-09_blog_prompt-engineering-magic_tns) 这样的[大语言模型(LLM)](https://zilliz.com/glossary/large-language-models-(llms)?utm_source=vendor&utm_medium=referral&utm_campaign=2021-11-09_blog_prompt-engineering-magic_tns)正在以前所未有的速度推动创新研究和应用。一个重要的发展是[检索增强生成(RAG)](https://zilliz.com/use-cases/llm-retrieval-augmented-generation?utm_source=vendor&utm_medium=referral&utm_campaign=2021-11-09_blog_prompt-engineering-magic_tns)的出现。这种技术将 LLM 的力量与作为长期记忆的[向量数据库](https://zilliz.com/learn/what-is-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2021-11-09_blog_prompt-engineering-magic_tns)相结合，以增强生成响应的准确性。RAG 方法的典型体现是开源项目 [Akcio](https://github.com/zc277584121/akcio)，它提供了一个强大的问答系统。

![](https://cdn.thenewstack.io/media/2023/11/496d05b2-akcio-architecture-1024x863.png)

*Akcio 的架构*

在 Akcio 的架构中，使用数据加载器将特定领域的知识无缝集成到向量存储中，如 [Milvus](https://zilliz.com/what-is-milvus?utm_source=vendor&utm_medium=referral&utm_campaign=2021-11-09_blog_prompt-engineering-magic_tns) 或 [Zilliz](https://zilliz.com/cloud?utm_source=vendor&utm_medium=referral&utm_campaign=2021-11-09_blog_prompt-engineering-magic_tns)(完全托管的 Milvus)。向量存储检索与用户查询最相关的前 K 个结果，并将其传达给 LLM，为 LLM 提供有关用户问题的上下文。随后，LLM 根据外部知识完善其响应。

例如，如果用户查询“2023 年[大语言模型的使用案例](https://thenewstack.io/what-is-a-large-language-model/)是什么？”关于导入 Akcio 的题为“2023 年大语言模型进展洞察报告”的文章，系统会巧妙地从报告中检索出三个最相关的段落。

```
1. In 2023, the LLM use cases can be divided into two categories: generation AI and decision-making. Decision-making scenarios are expected to have higher business value.
2. The generation AI scenario mainly includes dialogue interaction, code development, intelligent agents, etc.
3. NLP applications include text classification, machine translation, sentiment analysis, automatic summarization, etc.
```

Akcio 将这些段落与原始查询相结合，并转发给 LLM，生成一个细致准确的响应:


```
The application scenarios of the large model industry can be divided into generation and decision-making scenarios.
```

## RAG 中指代消解的挑战

然而，尽管取得了进步，实施 RAG 系统仍带来挑战，特别是在涉及指代消解的多轮对话中。考虑这个问题序列：


```
Q1: What are the use cases of the large language model in 2023?
A1: The use cases of large language models can be divided into generation AI and decision-making.
Q2: What are their differences, and can you provide examples?
```


Q2 中的代词“their”指的是“生成式 AI 和决策制定”。然而，LLM 可能会生成与这个问题无关的结果，破坏对话的连贯性:
 
```
1. BERT and GPT are important models in the field of NLP, but they have significant differences in their design and application scenarios.
2. The difference between large models and small models lies in their scale and complexity. Large models usually have more parameters and more complex structures, requiring more computational resources and time for training and inference. Small models, on the other hand, are relatively simple with fewer parameters and faster training and inference speeds.
3. However, there is no additional information to distinguish between these two products because they appear very similar.
```

## 使用 ChatGPT 进行指代消解

传统方法，如使用递归神经网络的标记化、词形还原和关键词替换，通常不足以解析复杂的引用。因此，研究人员转向了 ChatGPT 等 LLM 进行指代消解任务。这种方法涉及指示 ChatGPT 根据提供的上下文替换代词或保留原始问题。虽然这种方法前景广阔，但它偶尔会直接生成答案，而不是遵循提示指令，这表明需要更精细的策略。

## 测试的例子

我们使用以下提示格式实验了直接命令 ChatGPT 替换代词的方法:

```python
prompt = f'''Please generate a new question adhering to the following guidelines:
1. Complete any missing pronouns or conditions in the question based on the context.
2. Retain the original question if it's already complete.


{history}
Question: {question}'''
```

### 例子1 

查询:

```
history = ''' What is NLP?
NLP stands for Natural Language Processing. It is a field of computer science and artificial intelligence that focuses on the interaction between computers and humans using natural language. '''
question = 'What problem does it solve?'
```


ChatGPT 的回应:

```
What problem does Natural Language Processing (NLP) solve?
```

在这种情况下，ChatGPT 做得很好，用 “自然语言处理(NLP)” 替换了 “it”。

### 例子2

查询:

```python
history = '''When was GPT4 released?
GPT4 was released in 2023'''
question = 'What progress has been made in computer vision this year?'
```

ChatGPT 的回应:

```
What progress has been made in computer vision this year?
```

在这种情况下，ChatGPT 在替换 “今年” 时遇到了困难，导致指代消解不完整。

### 例子3

查询:

```python
history = '''What is GPT3?
GPT-3 (Generative Pre-trained Transformer 3) is a state-of-the-art language processing model developed by OpenAI.
When was GPT4 released?
GPT4 was released in 2023'''
question = 'What is the difference between them? What are the advantages of the latter?'
```

ChatGPT 的回应:

```
Sorry, the information provided about GPT-4's release date is not accurate as it has not been officially announced by OpenAI. Therefore, it is not possible to answer the question about the difference between GPT-3 and GPT-4 or the advantages of the latter.
```

不幸的是，ChatGPT 偏离了指令，这可能是由于其复杂的决策过程。尽管我们努力加强提示，但 ChatGPT 有时会偏向直接答案，使指代消解任务复杂化。

## 少样本提示与思维链：一种改进的方法

[提示工程在有效利用 LLM 方面发挥着至关重要的作用](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/)。我们决定测试将少样本提示与[思维链(CoT)](https://arxiv.org/abs/2201.11903)方法相结合，作为一种有前途的策略。少样本提示向 LLM 展示多个参考示例，引导它们在响应中模仿这些示例。CoT 通过鼓励 LLM 在答案中逐步推理来增强它们在复杂推理任务中的表现。

通过集成这些技术，我们开发了一个提示格式来引导 ChatGPT 进行指代消解。经修订的提示格式包括空的对话历史记录、基本示例、失败的代词替换以及涉及多个代词的案例，为 ChatGPT 提供更明确的指示和参考示例。ChatGPT 返回 `NEED COREFERENCE RESOLUTION: Yes` 的实例至关重要，因为它们表明 ChatGPT 需要替换代词或模糊引用以获得连贯的响应。

以下是经过优化的提示格式:

```
REWRITE_TEMP = f'''
HISTORY:
[]
NOW QUESTION: Hello, how are you?
NEED COREFERENCE RESOLUTION: No => THOUGHT: Consequently, the output question mirrors the current query. => OUTPUT QUESTION: Hello, how are you?
-------------------
HISTORY:
[Q: Is Milvus a vector database?
A: Yes, Milvus is a vector database.]
NOW QUESTION: How to use it?
NEED COREFERENCE RESOLUTION: Yes => THOUGHT: I must substitute 'it' with 'Milvus' in the current question. => OUTPUT QUESTION: How to use Milvus?
-------------------
HISTORY:
[]
NOW QUESTION: What are its features?
NEED COREFERENCE RESOLUTION: Yes => THOUGHT: Although 'it' requires substitution, there's no suitable reference in the history. Thus, the output question remains unchanged. => OUTPUT QUESTION: What are its features?
-------------------
HISTORY:
[Q: What is PyTorch?
A: PyTorch is an open-source machine learning library for Python. It provides a flexible and efficient framework for building and training deep neural networks.
Q: What is Tensorflow?
A: TensorFlow is an open-source machine learning framework. It provides a comprehensive set of tools, libraries, and resources for building and deploying machine learning models.]
NOW QUESTION: What is the difference between them?
NEED COREFERENCE RESOLUTION: Yes => THOUGHT: 'Them' should be replaced with 'PyTorch and Tensorflow' in the current question. => OUTPUT QUESTION: What is the difference between PyTorch and Tensorflow?
-------------------
HISTORY:
[{history}]
NOW QUESTION: {question}
NEED COREFERENCE RESOLUTION: '''
```

### 测试的示例和优化后的响应

以下是我们使用优化提示进行实验的一些结果:

### 例子 1

查询:

```
history = '''When was GPT-4 released?
GPT-4 was released in 2023'''
question = 'What progress has been made in computer vision this year?'
```

ChatGPT 优化后的响应:

```
Yes => THOUGHT: I need to replace "this year" with "2023" in the now question. => OUTPUT QUESTION: What progress has been made in computer vision in 2023?
```

## 例子 2:

查询:

```
history = '''What is GPT-3?
GPT-3 (Generative Pre-trained Transformer 3) is a state-of-the-art language processing model developed by OpenAI.
When was GPT-4 released?
GPT-4 was released in 2023'''
question = 'What is the difference between the two? What are the advantages of the latter?'
```

ChatGPT 优化后的响应:

```
Yes => THOUGHT: I need to replace 'the two' with 'GPT-3 and GPT-4' and 'the latter' with 'GPT-4' in the now question. => OUTPUT QUESTION: What is the difference between GPT-3 and GPT-4? What are the advantages of GPT-4?
```

优化后的提示格式极大地增强了 ChatGPT 处理复杂指代消解任务的能力。此前带来挑战的涉及多个实体的问题现在可以有效解决。ChatGPT 灵巧地替换代词和模糊引用，提供准确和上下文相关的响应。

## 结论

提示工程在利用 LLM 的 [RAG](https://zilliz.com/use-cases/llm-retrieval-augmented-generation?utm_source=vendor&utm_medium=referral&utm_campaign=2021-11-09_blog_prompt-engineering-magic_tns) 系统中解决指代消解问题方面发挥着关键作用。通过集成创新技术，如少样本提示和 CoT 方法，我们极大地改进了 RAG 系统中处理复杂引用的能力，使得 ChatGPT 等 LLM 能够准确地替换代词和模糊引用，并产生连贯的响应。
