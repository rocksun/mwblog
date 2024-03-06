# 探索 Google 的 Gemini 语言模型的 API

![Gemini 语言模型 API 探索的特色图片](https://cdn.thenewstack.io/media/2024/03/13c7662b-boliviainteligente-ie7pkrxbsa4-unsplash-1024x640.jpg)

[提示工程](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/)是利用[Gemini API](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/)从语言模型生成定制且有效输出的关键方面。此实践涉及设计和优化提示以指导 LLM 生成所需内容，无论用于创意写作、编码、数据分析还是可以应用自然语言生成的任何其他应用程序。提示工程的成功不仅取决于提示本身的巧妙制作，还取决于理解和优化 Gemini API 提供的参数，例如：

- temperature
- max_output_tokens
- top_p
- top_k

这些参数在提示工程中的重要性怎么强调都不为过，因为它们使用户能够根据特定需求自定义模型的行为，确保生成的内容满足所需的准确性、相关性、创造性和连贯性标准。

本文旨在探讨 Gemini API 参数的细微差别，深入了解如何利用这些参数最大化各种应用程序中生成内容的有效性。

## 仔细了解 API 参数

Gemini API 提供了一套参数来微调文本生成，使用户能够有效地在创造性和准确性之间取得平衡。以下是关键参数的概述，以及它们对 LLM 响应的创造性和准确性的影响。

下面的代码片段提供了文本生成和聊天完成的 API 调用的基本结构。有关安装和配置 Vertex AI 的 Python SDK 的详细信息，请参阅之前的教程“
[如何开始使用 Google 的 Gemini 大型语言模型](https://thenewstack.io/how-to-get-started-with-googles-gemini-large-language-model/)”。

```python
from google.cloud import aiplatform
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
vertexai.init()
model = GenerativeModel("gemini-pro")
response = model.generate_content(“What's the meaning of life?”,
max_output_tokens=128,
temperature=0,
top_p=1,
top_k=5
)
print(response.text)
```

**max_output_tokens**：此参数设置模型响应的最大长度（以标记为单位），这大致相当于单词数。它控制输出的详细程度，较高的限制允许更长、更详细的响应。此限制的选择会影响响应的深度和全面性，但不会直接影响其创造性或准确性。

**temperature**：此参数控制输出的随机性。较高的温度通过使不太可能的标记更有可能被选择来提高创造性，从而产生更多样化和出乎意料的输出。相反，较低的温度会导致更可预测、更保守的输出。它是控制模型响应中创造性和确定性之间平衡的关键参数。

**top_p（核采样）**：此参数（也称为核采样）控制标记选择的累积概率阈值，确保仅考虑最可能的标记（直至指定的累积概率）。这允许在创造性和准确性之间实现动态平衡。较低的阈值（接近 0）将使模型的输出更加集中且多样性较低，而较高的阈值会增加所用标记的多样性，从而可能使输出更具创造性但可预测性较低。

**top_k**：此参数将下一个标记的选择限制为最可能的 k 个标记。较低的 k 值将模型限制在较窄的单词选择范围内，从而产生更可预测的输出，而较高的值允许更广泛的标记选择，从而增加输出的潜在创造性。但是，将其设置得太高可能会降低内容的相关性和准确性。

相比之下，**temperature** 和 **top_p** 更直接地与控制模型的创造性相关，较高的值会导致更多新颖且多样的输出。**top_k** 参数提供了对下一个标记的选择池的更精细控制，直接影响输出的多样性和潜在创造性。参数 **max_output_tokens** 虽然不会直接影响创造性，但会设置响应的范围，影响模型充分发展思想或提供详细信息的能力。
## Gemini 的接地和函数调用扩展了其能力

Gemini 引入了高级函数调用功能，允许开发人员将外部工具和 API 无缝集成到其 AI 驱动的应用程序中。此功能使模型能够与外部数据源和服务进行交互，从而将其实用性和应用范围扩展到独立 AI 模型所能实现的范围之外。例如，通过定义模型可以根据其接收的输入调用的函数，开发人员可以创建更动态、更响应且更有用的 AI 应用程序。这可以从从外部 API 获取实时数据到基于复杂的外部数据集处理和生成输出。

Gemini 函数调用机制的复杂性证明了其设计为高度交互且可集成的 AI 模型，可以解决广泛的实际用例。在本系列的后续部分中，我将指导你通过函数调用技术将实时航班跟踪 API 与 Gemini 集成的步骤。

接地是另一种技术，它通过将特定于上下文的 data 纳入其处理中来增强 Gemini 提供相关且准确信息的能力。此功能通常由语义搜索和 [检索增强生成](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/) 模型支持，使 LLM 能够有效地访问和使用外部知识库，使其更擅长以高精度回答查询。

接地提供以下好处：

- **减少幻觉：**接地通过防止生成非事实内容来最大程度地减少模型幻觉的发生。
- **锚定响应：**接地确保模型响应牢固地锚定在特定信息上，从而增强其相关性和可靠性。
- **增强可信度和适用性：**接地内容更可信且更实用，从而提高用户满意度和对生成输出的信心。

Google 已将 [Vertex AI Search](https://cloud.google.com/vertex-ai-search-and-conversation) 与 Gemini 集成，为 LLM 提供接地功能。类似于函数调用，可以将模型指向 Search 中的数据存储索引以检索上下文信息。

Gemini API 及其可自定义的参数（例如 `temperature`、`max_output_tokens`、`top_p` 和 `top_k`）在根据特定需求定制 AI 生成的内容方面提供了无与伦比的灵活性，有效地平衡了创造力和准确性。

此外，Gemini 的接地和函数调用功能极大地扩展了其实用性，使其能够将外部数据源和服务无缝集成到其响应中。这些功能共同增强了 Gemini 在广泛领域提供与上下文相关的、准确且高度交互的 AI 应用程序的能力。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。