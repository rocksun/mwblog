
<!--
title: 什么是LLM Token：面向开发者的初学者友好指南
cover: https://cdn.thenewstack.io/media/2025/03/2211b433-osarugue-igbinoba-_3bulzbmtyc-unsplashb.jpg
summary: LLM开发者必看！Token是AI核心，影响模型性能和成本。文章详解Token化原理，包括WordPiece、BPE等算法，及NLTK、Hugging Face Tokenizers等工具。掌握Token优化技巧，助力打造高效聊天机器人、文本摘要等云原生AI应用，突破Token限制，提升SEO内容创作！
-->

LLM开发者必看！Token是AI核心，影响模型性能和成本。文章详解Token化原理，包括WordPiece、BPE等算法，及NLTK、Hugging Face Tokenizers等工具。掌握Token优化技巧，助力打造高效聊天机器人、文本摘要等云原生AI应用，突破Token限制，提升SEO内容创作！

> 译自：[What Is an LLM Token: Beginner-Friendly Guide for Developers](https://thenewstack.io/what-is-an-llm-token-beginner-friendly-guide-for-developers/)
> 
> 作者：Janakiram MSV

[大型语言模型](https://thenewstack.io/llm/) 已经改变了机器理解和生成人类语言的方式，为从聊天机器人到内容生成器的所有事物提供动力。 在它们令人印象深刻的功能背后，隐藏着每个开发人员都应该理解的基本概念：token。 在使用 LLM 时，这些构建块直接影响模型性能和成本。 本指南探讨了什么是 token，它们在 LLM 中的功能以及为什么理解 token 化对于有效的 AI 实施至关重要。

## 了解大型语言模型 Token

在 [AI](https://thenewstack.io/ai/) 和 [自然语言处理](https://thenewstack.io/top-5-nlp-tools-in-python-for-text-analysis-applications/) 中，token 是模型处理的文本的基本单位。 与将文本视为连续字符流的人类不同，LLM 将输入文本分解为称为 token 的小段。 token 可以是整个单词、单词的一部分、单个字符，甚至是标点符号或空格。

LLM 识别的一组唯一 token 构成了它的词汇表。 通过将文本转换为 token，LLM 可以以一种更易于分析和生成的形式处理语言，从而作为理解和生成文本的基础。

## LLM 如何使用 Token？

LLM 使用 token 作为从文本中学习和生成新内容的基础：

1. 在训练期间，LLM 读取大量的文本，并将每个句子或文档转换为 token 序列。
2. 每个 token 都被映射到一个称为嵌入的数字表示，因此模型可以对其执行数学运算。
3. 该模型学习 token 序列的模式——哪些 token 通常在各种上下文中跟随其他 token。
4. 在[推理](https://thenewstack.io/inference-is-table-stakes-thats-a-good-thing-for-ampere/)期间，输入文本被 token 化，模型处理这些 token 序列以预测下一个最可能的 token。
5. 模型根据学习到的概率依次输出每个 token，一次构建一个 token 的最终响应。

这种基于 token 的方法允许 LLM 捕获单词和短语之间的统计关系，使它们能够生成连贯且与上下文相关的文本。

## Token 化：文本如何转换为 Token

Token 化是将原始文本转换为 token 的过程——对于 LLM 来说，这是至关重要的第一步，因为它们无法直接理解人类语言。 token 化方法会显着影响模型处理文本的效率以及它处理不同语言和写作风格的能力。

### 基于单词、基于字符和子词 Token 化

token 化有三种主要方法，每种方法都有其独特的优点和缺点：

**基于单词的 Token 化：** 将每个单词（由空格或标点符号分隔）视为单个 token。 例如，“LLMs are amazing!” 变成 [“LLMs”, “are”, “amazing”, “!”]。 这种方法很直观，但在处理不熟悉的单词（词汇表外项目）时会遇到困难，并且需要非常大的词汇表。

**基于字符的 Token 化：** 这种方法将文本分解为单个字符或字节。 使用相同的示例，它变为 [“L”, “L”, “M”, “s”, ” “, “a”, “r”, “e”, 等]。 这种方法可以表示任何可能的字符串，但会显着增加序列长度，从而降低处理效率。

**子词 Token 化：** 通过将单词分解为有意义的片段来达到平衡，这些片段可能比单词短，但比字符长。 一个像“unhappiness”这样的罕见词可能会变成 [“un”, “happiness”]。 这种方法可以有效地处理新的或罕见的单词，同时保持词汇表的可管理性——使其成为现代 LLM 的首选方法。

### 单词 vs. Token

token 是 LLM 处理的基本单位，而单词是语言单位。 Token 可以是整个单词、单词的一部分、字符或标点符号。 在英语中，一个单词平均等于大约 1.3 个 token，但这因语言和 token 化方法而异。

### 不同 Token 化方法的示例

考虑不同的 token 器将如何处理单词“internationalization”：

- 基于单词的 token 器可能会将其视为单个 token（如果已知）或将其标记为 [UNK]（未知）。
- 基于字符的 token 器会将其分解为 20 个单独的字符。
- 子词 token 器可能会将其拆分为 [“inter”, “national”, “ization”]，从而识别常见的形态单位。

这些差异说明了为什么 token 化很重要——选择会影响模型处理文本的效率以及它们处理不熟悉的单词或表达方式的方式。

### 常用 Token 化工具
一些工具和库可以帮助开发人员实现 token 化：

- [NLTK](https://www.nltk.org/) 和 [spaCy](https://spacy.io/)：常用的 NLP 库，带有基本的基于单词的分词器。
- [SentencePiece](https://github.com/google/sentencepiece)：Google 的库，支持 BPE 和 Unigram 分词方法。
- [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/en/index)：各种分词算法的高效实现。
- [OpenAI’s Tiktoken](https://github.com/openai/tiktoken)：针对 OpenAI 的 GPT-3 和 GPT-4 等模型优化的快速分词器。
- **特定于语言的分词器**: 例如用于日语的 [Mecab](https://pypi.org/project/mecab-python3/) 或用于其他语言的专用工具。

## Token 限制和模型约束

每个语言模型都有预定义的 token 限制，这些限制为输入和输出建立了边界。这些约束定义了“上下文长度”——模型可以在单个操作中处理的 token 数量。例如，具有 2,048 个 token 上下文长度的模型和 500 个 token 的输入最多可以生成 1,548 个 token 的响应。这些限制的存在是由于计算约束、内存限制和架构设计选择。

理解这些边界至关重要，因为超过这些边界可能会导致响应被截断、信息丢失或模型错误。模型不断发展，上下文窗口不断扩大，但在 token 限制内有效工作仍然是 LLM 开发人员的一项基本技能。

### Token 限制如何影响性能

Token 限制直接影响 LLM 保持上下文和生成连贯响应的能力。当输入接近或超过这些限制时，模型可能会丢失文本前面呈现的信息，从而导致准确性降低、细节遗忘或输出相互矛盾。有限的 token 上下文尤其会阻碍需要远程推理、复杂问题解决或参考文档中分散的信息的任务。

此外，不同的分词方法会影响文本编码的效率——低效的分词会导致 token 浪费，这些 token 会占用上下文限制，而不会增加有意义的信息。理解这些性能影响有助于开发人员设计更有效的提示和交互。

### 优化 Token 使用的策略

有效的 token 优化始于制作简洁、清晰的提示，消除冗余和不必要的细节。开发人员可以通过在适当的情况下使用缩写、删除重复信息以及将查询重点放在特定点而不是广泛的主题上来减少 token 使用量。使用后续问题而不是冗长的单个提示来构建交互可以最大限度地利用上下文。

当处理大型文档时，实施分块（将内容分成更小的片段）等技术有助于管理 token 约束。选择具有更有效分词方法的模型并监控对成本敏感的应用程序的 token 使用情况可以显着降低运营费用，同时保持输出质量。

## LLM 分词实践

从聊天机器人到内容生成系统，分词会影响与 LLM 的每次交互。理解它的实际意义有助于开发人员创建更有效的 AI 应用程序。

AI 应用程序中的分词示例：

- **聊天机器人和虚拟助手**：对用户查询和之前的对话历史进行分词，以保持上下文。
- **机器翻译**：对源文本进行分词，在语言之间映射 token，并生成翻译后的输出。
- **文本摘要**：将文档分解为 token，以识别用于提取或抽象的关键信息。
- **代码完成**：使用了解编程语言语法的专用分词器。

### 分词对 SEO 和内容创建的影响

当使用 LLM 进行内容创建时，分词会影响以下方面：

- **内容长度和结构**：Token 限制可能需要将内容分成多个部分或计划多部分生成。
- **关键词使用**：理解特定术语如何分词有助于确保它们在生成的内容中完整出现。
- **内容规划**：有效的提示需要了解不同指令的分词效率。

## 常用的分词算法及其差异

现代 LLM 通常使用子词分词算法，每种算法都有不同的方法：

### 字节对编码 (BPE)

BPE 从单个字符开始，并迭代地合并最频繁的相邻 token 对，直到达到目标词汇量大小。这种数据驱动的方法可以有效地处理常用词，同时仍然能够表示稀有术语。OpenAI 的 GPT 模型使用 BPE 的变体。

### Unigram 语言模型

Unigram 分词采用概率方法，从许多候选 token 开始，并迭代地删除那些对生成训练文本的可能性影响最小的 token。这会创建往往在语言上更有意义的 token。

### WordPiece 分词
WordPiece 是为 BERT 开发的，它与 BPE 类似，但优先考虑使训练数据可能性最大化的合并，而不仅仅是频率。它通常用特殊前缀（如 BERT 中的“##”）标记子词单元，以指示单词延续。

### Tiktoken (OpenAI 的 Tokenizer)

OpenAI 为 GPT-3.5 和 GPT-4 等模型定制的 tokenizer 实现了 BPE，并针对速度和效率进行了优化。它可以处理多语言文本、特殊字符和各种格式，同时保持可逆性（token 可以完美地转换回原始文本）。

## 结论

Token 构成了大型语言模型理解、处理和生成文本的基础。理解 tokenization 不仅仅是学术上的——它直接影响应用程序的效率、成本管理和输出质量。通过掌握 tokenization 概念和优化策略，开发人员可以构建更有效的 AI 应用程序，从而最大限度地发挥 LLM 的潜力，同时最大限度地减少其局限性。

随着模型不断发展，具有更大的上下文窗口和更复杂的架构，有效的 token 管理将仍然是 AI 开发人员创建最先进应用程序的关键技能。