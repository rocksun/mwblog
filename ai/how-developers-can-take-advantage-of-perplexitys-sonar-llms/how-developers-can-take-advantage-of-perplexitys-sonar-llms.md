
<!--
title: 开发者如何利用Perplexity的Sonar大型语言模型
cover: https://cdn.thenewstack.io/media/2025/01/b44afe14-getty-images-iod0xnmozbe-unsplashb.jpg
-->

对于开发者而言，Perplexity 的 Sonar 提供了一个构建创新型应用程序的机会，这些应用程序可以利用实时 AI 搜索的强大功能。

> 译自 [How Developers Can Take Advantage of Perplexity’s Sonar LLMs](https://thenewstack.io/how-developers-can-take-advantage-of-perplexitys-sonar-llms/)，作者 Janakiram MSV。

Perplexity，这家[AI搜索初创公司](https://thenewstack.io/more-than-an-openai-wrapper-perplexity-pivots-to-open-source/)，已经开发了Sonar系列[大型语言模型](https://thenewstack.io/llm/) (LLMs)。这些模型通过提供对互联网信息的实时访问来改变AI搜索能力。它们旨在克服传统语言模型的关键限制，例如信息过时和潜在的[幻觉](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)。

## 了解Sonar模型

Sonar有两个版本：Sonar（基础版）和Sonar Pro。这些模型通过利用实时互联网连接与传统的LLMs区别开来，使它们能够提供基于最新信息的响应。与受训练数据限制的传统LLMs不同，Sonar的实时网络访问确保提供的信息始终是最新的和相关的，这使得它成为搜索增强型LLMs领域的一项重大进步。

Sonar是一个轻量级且经济实惠的选项，针对速度和基本查询进行了优化，使其成为简单问答和直接集成的理想选择。另一方面，Sonar Pro专为需要更深入理解和上下文保留的复杂多步骤查询而设计。

> Sonar模型支持结构化输出，使开发人员能够以适合各种应用程序的有组织的格式接收响应。

这些Sonar模型的一个关键特性是扩展的上下文窗口，能够处理大量的输入数据，同时保持长时间交互的一致性。此外，Sonar模型在其响应中提供内置引用，确保透明度并允许用户验证信息来源。此外，它们支持结构化输出，使开发人员能够以适合各种应用程序的有组织的格式接收响应。

## 开发者为什么要关注

对于开发者来说，Sonar提供了一个独特的机会，可以使用实时AI搜索的功能来构建创新型应用程序。以下是一些主要好处：

- **实时信息**：Sonar模型访问网络上的最新信息，确保您的应用程序始终提供最新的结果。
- **更高的准确性**：通过将响应建立在现实世界的数据上，Sonar降低了幻觉的风险并提供更可靠的信息。
- **内置引用**：Sonar模型会自动为其响应生成引用，使您可以构建透明且值得信赖的应用程序。
- **灵活的API**：Perplexity API提供了一种简单有效的方法，可以将Sonar模型集成到您的项目中。
- **可定制的输出**：Sonar支持结构化输出，使您可以根据您的特定需求定制响应。

## 仔细看看这些模型

Perplexity的Sonar Pro模型旨在处理需要深入理解和上下文保留的复杂多步骤任务。这些模型特别适用于需要全面信息检索和细致入微的响应的应用程序。

Sonar Pro的一些关键特性包括：

- **增强的复杂性处理**：Sonar Pro模型针对复杂查询进行了优化，与标准Sonar模型相比，它提供更深入的答案和更多引用。
- **高级信息检索**：这些模型执行多次网络搜索以收集和综合信息，确保响应全面且周到。
- **更大的上下文窗口**：通过扩展的上下文窗口，Sonar Pro模型在更长时间的交互中保持一致性，使其成为详细讨论的理想选择。

Sonar和Sonar Pro之间的主要区别在于它们的复杂性、引用量和信息检索方法。虽然标准Sonar模型专为简单的查询而设计，但Sonar Pro模型专门用于处理更复杂的任务，提供更深入的见解和更全面的答案。此外，Sonar Pro模型提供的引用数量大约是标准Sonar模型的两倍，大大提高了信息的透明度和可验证性。

在信息检索方面，标准Sonar模型通常依赖于单次网络搜索。相比之下，Sonar Pro模型会进行多次搜索以收集不同的观点和数据点，从而产生更细致入微且全面的响应。

![](https://cdn.thenewstack.io/media/2025/01/32effb66-sonar-1-1024x121.png)

Sonar 提供灵活的定价方案，以满足各种需求和预算。基本的 Sonar 模型是一种经济高效的选择，价格为每 1000 次搜索 5 美元，另外每 750,000 个输入或输出单词收取 1 美元，使其成为轻量级集成和基本查询的理想选择。对于更苛刻的应用，Sonar Pro 的价格为每 750,000 个输入单词 3 美元，每 750,000 个输出单词 15 美元。

## 通过 API 探索 Sonar 模型

让我们深入研究一些代码示例，这些示例演示了如何将 Sonar 模型用于引用和结构化输出。

虽然代码看起来很熟悉，几乎与调用任何 LLM 的聊天完成 API 相同，但 Sonar 的独特之处在于能够根据在线和实时搜索结果获取最新信息。响应牢牢基于搜索结果，增强了用户的信心。

Sonar 的另一个关键方面是引用。API 响应包含用于引用的 URL 列表。

下面的代码片段打印搜索结果以及引用。请注意，查询基于近期新闻。API 不仅返回正确的响应，还引用用于聚合它的实际来源。

```python
import requests

def get_results_citations(api_key, query):
    """Retrieves citations from the Perplexity Sonar API for a given query.

    Args:
        api_key: Your Perplexity API key.
        query: The question you want to ask Sonar.

    Returns:
        A list of citations (URLs).
    """
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": query}]
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

# Example usage
api_key = "YOUR_API_KEY"
query = "Who are the prominent tech CEOs that attended Trump's inauguration?"
response = get_results_citations(api_key, query)

# Extract content and citations
content = response['choices'][0]['message']['content']
citations = response['citations']

# Print the results
print("Content:\n", content)
print("\nCitations:")
for i, citation in enumerate(citations, start=1):
    print(f"[{i}] {citation}")
```

输出同时包含内容和指向结果的引用。

![](https://cdn.thenewstack.io/media/2025/01/204c5478-sonar-2-1024x675.png)

Sonar 使用 JSON Schema 支持结构化输出。您可以在 API 请求的 `response_format` 字段中指定所需的输出格式。

例如，以下查询检索正确的响应（特朗普担任总统的任期数）并将其格式化为 JSON。这对于将 Sonar 与自主工作流程集成非常有用。

```python
import requests
from pydantic import BaseModel

class AnswerFormat(BaseModel):
    first_name: str
    last_name: str
    year_of_birth: int
    num_seasons_in_nba: int

url = "https://api.perplexity.ai/chat/completions"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
payload = {
    "model": "sonar",
    "messages": [
        {"role": "system", "content": "Be precise and concise."},
        {"role": "user", "content": (
            "Tell me about Donald Trump."
            "Please output a JSON object containing the following fields: "
            "first_name, last_name, year_of_birth, num_times_as_president. "
        )},
    ],
    "response_format": {
        "type": "json_schema",
        "json_schema": {"schema": AnswerFormat.model_json_schema()},
    },
}
response = requests.post(url, headers=headers, json=payload).json()
print(response["choices"][0]["message"]["content"])
```

这将打印以下输出：

![](https://cdn.thenewstack.io/media/2025/01/d82c490f-sonar-2b-1024x538.png)

Perplexity 的 Sonar 模型为寻求将其应用程序集成到高级 AI 驱动的搜索功能的开发人员提供了强大的工具。凭借实时网络访问、扩展上下文窗口、内置引用和结构化输出等功能，这些模型增强了信息检索的质量和可靠性。使用 Perplexity API，开发人员可以无缝地整合这些功能，为用户提供准确和最新的信息，以满足他们的需求。
