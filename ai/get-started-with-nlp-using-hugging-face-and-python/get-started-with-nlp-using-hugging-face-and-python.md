
<!--
title: Hugging Face与Python：NLP入门实战指南
cover: https://cdn.thenewstack.io/media/2025/12/0663b9fa-sigmund-0o6v5e9jyvc-unsplash-1.jpg
summary: Hugging Face是强大的AI和NLP库，应用GPT等预训练模型解决现实问题。能进行文本生成、情感分析、分类等复杂任务，并用于市场、客服和研究领域。易于使用。
-->

Hugging Face是强大的AI和NLP库，应用GPT等预训练模型解决现实问题。能进行文本生成、情感分析、分类等复杂任务，并用于市场、客服和研究领域。易于使用。

> 译自：[Get Started With NLP Using Hugging Face and Python](https://thenewstack.io/get-started-with-nlp-using-hugging-face-and-python/)
> 
> 作者：Jessica Wachtel

[Hugging Face](https://huggingface.co/) 是一个强大的 AI 库，它应用预训练模型来解决现实世界中的问题。它是一个[自然语言处理 (NLP)](https://thenewstack.io/top-10-nlp-tools-in-python-for-text-analysis-applications/) 库，因此主要关注基于文本的输入和输出。Hugging Face 能够大规模地执行复杂的任务，例如文本摘要、问答和情感分析。虽然其目的与[本博客中讨论的](https://thenewstack.io/how-to-perform-basic-nlp-in-javascript-with-the-natural-library/)其他 NLP 库（如 Natural 库）相似，但 Hugging Face 更为先进，因为它由 GPT、BERT 和 [LLaMA](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/) 等更强大的模型驱动。得益于这些先进模型，Hugging Face 能够大规模处理更复杂的任务，将 Natural 等简单库的功能进一步提升。

Hugging Face 能够大规模执行复杂的 NLP 任务，具体是做什么的呢？以下是一些基本示例。

**市场和媒体分析**
这将非结构化文本数据转化为可操作的洞察，用于战略决策。示例包括情感分析，它可以帮助您了解对品牌、营销活动和产品的看法。它还有助于预测，例如趋势监控，以帮助您掌握未来动向。

**客户服务**
Hugging Face 提高了响应时间并减少了手动工作量。我们现在在日常生活中就能看到这一点，虚拟聊天机器人帮助处理常见问题解答，以及一些实时 24 小时帮助系统。在幕后，Hugging Face 处理[情感分析](https://thenewstack.io/build-an-advanced-chat-app-with-quix-and-redpanda-part-1/)，可以将愤怒的客户优先推到客服热线的前端。

**研究与学术**
先进的 NLP 库加快了研究时间。Hugging Face 可以将冗长的科学论文、文章和报告浓缩成关键要点。

以下教程非常基础。我们将生成文本、分析文本的情感，并对另一段文本进行分类。完成之后，您可能会想，我们为什么要构建这个？我同意：这个教程表面上看毫无目的。我们不需要一个基本的文本分析器。然而，这样做的益处在于能看到使用 Hugging Face 是多么容易。希望这个基本教程能让您思考使用 Hugging Face 到底能构建什么。

## 使用 Python 和 Hugging Face 开始

本教程最适合对 Python 或类似语言有基本了解的开发者。

在您的 IDE 中打开一个新项目并创建一个 [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/) 文件。我将我的文件命名为 `main.py`。

打开一个新终端，让我们开始安装。
`transformers` 是带有预训练 NLP 模型的 Hugging Face 库。`torch` 是高效运行模型的后端。`numpy<2` 修复了与 mac 的任何兼容性问题。

```
pip install transformers torch
pip install "numpy<2"
```

我第一次运行我的代码文件时，出现了一堆错误。结果是我在 [NumPy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) 和我的 Python 环境上出了问题。这会在设置过程的稍后发生，但我将其放在这里，以便您在错误出现之前（如果发生的话）就能获得修复。

安装 `numpy<2`。这会将 NumPy 降级到与 [PyTorch](https://thenewstack.io/why-pytorch-won/) 兼容的 1.x 版本。

```
pip install "numpy<2"
```

然后卸载 `torch` 并立即重新安装，验证 NumPy 是否正常工作。

```
pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cpu
python3 -c "import numpy; print(numpy.__version__)"
```

我们将在同一个文件中运行所有 Python/Hugging Face 代码。

我们要做的第一件事是导入 Hugging Face 的 `pipeline` 功能。`pipeline` 是一种使用预训练模型执行常见任务（例如我们现在正在构建的基本文本应用程序）的简单方法。借助 `pipeline` 及其即用型管道，您可以生成文本、分析情感和回答问题，而无需手动处理分词或设置。

```
from transformers import pipeline
```

## 使用 GP2-2 生成文本

我们使用 GPT-2 是因为它免费且易于访问。您可以通过将 `model=“gpt2”` 更新为您选择的模型来轻松更改为更高级的模型（注意：高级模型需要账户并产生费用）。

Hugging Face 的 `generator` 将返回一个结果列表。如果您不填写 `max_length`，Hugging Face 将默认设置为大约 1024 个令牌，这会非常长。`num_return_sequences` 的默认值为 1。

```
generator = pipeline("text-generation", model="gpt2")


prompt = "Explain how self-driving cars work in simple terms."
result = generator(prompt, max_length=50, num_return_sequences=1)


print("=== Text Generation ===")
print(result[0]['generated_text'])
```

输出：
关于自动驾驶汽车的 50 个词的文本，对您而言是独一无二的

## 分析情感

我们接下来要编写的代码将分析我们生成的文本的情感。Hugging Face 的情感分析器使用预训练模型来确定文本是积极的、消极的还是中性的。该模型将首先分词（将文本分解成单独的词）。然后它处理这些令牌，并使用其神经网络预测整体情感。它将返回一个分数和一个标签，显示模型对其分类的置信度。分数将是一个介于 0-1 之间的数字，0 表示不自信，1 表示绝对确定。该分数并非文本积极或消极程度的分数。

```
classifier = pipeline("sentiment-analysis")


text = "I love sunny days."
result = classifier(text)


text2 = "I don't like the rain."
result2 = classifier(text2)


print("\n=== Sentiment Analysis ===")
print(result)
print(result2)
```

输出：

```
[{‘label’: ‘POSITIVE’, ‘score’: 0.9998550415039062}]
[{‘label’: ‘NEGATIVE’, ‘score’: 0.9930094480514526}]
```

## 文本分类

文本分类“阅读”所提供的文本，然后为其分配一个分类。使用 Hugging Face，对于更模糊的类别，您需要提供标签。在处理像天气这样普遍分类的事物时，您可以选择一个特定的模型来为您分类。对于下面的示例，我们将分配自己的类别。

与情感分析类似，Hugging Face 将返回一个介于 0-1 之间的分数，1 表示确定分类是正确的，0 基本表示模型分配了分类但不支持其主张。

对于此示例，我们将使用 `“zero-shot-classification”`。`“zero-shot-classification”` 允许将文本分类到它未明确训练过的新标签中。它有助于模型理解文本和标签描述的含义。

```
classifier = pipeline("zero-shot-classification")


text_to_classify = "I love my new blender! It makes smoothies so smooth."
candidate_labels = ["electronics", "kitchen appliance", "sports equipment", "furniture"]


result3 = classifier(text_to_classify, candidate_labels)
print(result3)
```

输出：

```
{‘sequence’: ‘I love my new blender! It makes smoothies so smooth.’, ‘labels’: [‘kitchen appliance’, ‘sports equipment’, ‘electronics’, ‘furniture’], ‘scores’: [0.9792253375053406, 0.010719629935920238, 0.007687257137149572, 0.002367804991081357]}
```

## 结论

现在您已经第一次体验了 Hugging Face 库。在了解了该库的功能预览之后，您能构建些什么呢？