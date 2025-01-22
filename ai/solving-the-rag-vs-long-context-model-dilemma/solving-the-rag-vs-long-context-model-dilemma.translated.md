# 解决RAG与长上下文模型的困境

![Featued image for: Solving the RAG vs. Long Context Model Dilemma](https://cdn.thenewstack.io/media/2025/01/b2c53656-llm-1024x572.jpg)

许多开发者一直在使用检索增强生成 (RAG) 和大规模上下文语料库来构建生成式AI应用程序，并解决诸如通用型[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms)面临的AI幻觉等问题。

现在，长上下文模型正在兴起，例如[具有200万个token上下文窗口的Gemini](https://ai.google.dev/gemini-api/docs/long-context)，其潜在优势使您不禁想知道是否应该完全放弃RAG。解决这一难题的关键在于了解使用长上下文模型的优缺点，并根据您的用例做出明智的决定。

**RAG与长上下文模型的优缺点**

传统上，[LLM具有较小的上下文窗口](https://thenewstack.io/do-enormous-llm-context-windows-spell-the-end-of-rag/)，这限制了可以一次处理的文本或token数量。到目前为止，RAG一直是解决此限制的有效方案。通过检索最相关的文本或上下文片段，用它来增强用户提示，然后将其传递给LLM，RAG可以有效地处理比上下文窗口通常支持的大得多的数据集。

然而，像Gemini这样的长上下文模型可以直接处理提供的上下文，而无需单独的RAG系统，从而简化了应用程序工作流程并可能减少延迟。要了解100万个token的上下文窗口，它相当于[八部中等长度的英文小说](https://ai.google.dev/gemini-api/docs/long-context)或超过200集中等长度播客节目的文字记录。然而，它绝不是减少幻觉的灵丹妙药，并且也有其自身的局限性。

首先，长上下文模型会降低对相关信息的关注度，这会导致答案质量下降，[NVIDIA的研究](https://arxiv.org/pdf/2409.01666)证实了这一点。

其次，对于问答聊天机器人等用例，重要的不是上下文信息的数量，而是质量。高质量的上下文是通过针对所提问题进行高度选择性的细粒度搜索实现的，而这是RAG能够实现的。

最后，长上下文模型需要更多GPU资源来处理长上下文，从而导致处理时间更长，成本更高。可以肯定地说，这些模型每次查询的成本更高。您可以使用键值 (KV) 缓存来缓存输入token以跨请求重用，但这需要大量的GPU内存，因此会增加相关成本。关键在于用更少的输入token实现高质量的答案。

尽管存在局限性，但长上下文模型支持一些需要更长上下文的引人注目的用例，例如翻译或摘要，例如，将文档从英语翻译成梵语（印度使用人数最少的语言）用于教育目的。由于梵语复杂的语法结构以及与其他广泛使用的语言相比，训练数据的有限性，LLM难以进行这种翻译。因此，提供足够数量的示例作为上下文将有助于提高翻译的准确性。其他方法包括一次对多个大型文档进行摘要和比较以生成见解，例如，比较多家公司的10K报告以创建财务基准。

长上下文模型对于某些需要更长上下文的用例[非常适合减少幻觉](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)。但是，对于所有其他用例，我们建议使用[RAG检索与回答用户问题相关的上下文](https://thenewstack.io/rag-still-relevant-in-the-era-of-long-context-models/)，以实现高精度和成本效益。如果RAG无法达到预期的精度，我们建议将RAG与微调结合使用以提高领域特异性。

Couchbase的[Capella AI服务](https://www.couchbase.com/products/ai-services/)帮助像您这样的开发者快速构建高性能的RAG和自主代理应用程序。请随时[注册我们的私人预览](https://info.couchbase.com/capella-ai-services-signup)以开始您的AI项目。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)