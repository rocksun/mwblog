<!--
title: 使用 OpenTelemetry 和 SigNoz 实现 LLM 可观测性
cover: ./cover.png
-->

在快速发展的大语言模型（LLM）世界中，确保最佳性能和可靠性比以往任何时候都更为关键。这就是'LLM 可观测性'的概念发挥作用的地方。这不仅仅是监控输出；更是深入洞察这些复杂系统内部运作的关键。

> 译自 [LLM Observability with OpenTelemetry and SigNoz](https://signoz.io/blog/llm-observability)。作者是 SigNoz Community 的 Jaikanth J 。

大语言模型（LLMs）代表了人工智能领域的一项变革性进展，通过复杂的语言理解和生成提供了解决问题的广泛能力。

Langchain 是构建 LLM 应用的热门框架之一，它与流行的 LLM 模型 API，如 OpenAI 的 GPT-4，Google 的 Gemini，Meta 的 Llama2 或 Anthropic 的 Claude 等集成。它还与向量数据库集成，并提供了良好的链抽象，以实现类似代理的实现。

谈到经济高效的监控解决方案，嵌入高基数的自定义度量标准，如准确性、延迟或详细的模型属性，是非常宝贵的。高基数的度量标准指的是具有广泛且独特值范围的数据，这可以显著增强跟踪分析。然而，与传统的可观测性平台相关的成本可能是禁锢的，通常类似于隐含的“数据税”。

OpenTelemetry，搭配像 SigNoz 这样的解决方案，为整合这些细致入微的见解提供了一种引人注目且经济实惠的替代方案。在类似 Datadog 这样的工具中，[高基数的自定义度量标准的成本可能无法控制](https://signoz.io/blog/datadog-pricing/#datadogs-custom-metrics-pricing-can-get-out-of-control-quickly)。OpenTelemetry 和 SigNoz 组合是建立强大的 LLM 可观测性的完美选择。

在本文中，我们涵盖了：

- 为什么我们需要 LLM 可观测性？
- OpenTelemetry 用于 LLM 可观测性
- OpenTelemetry & SigNoz - 为 LLM 可观测性的完美组合
- 先决条件
- 设置 SigNoz
- 在 LangChain LLM 应用中添加仪器的方法
- 使用 OpenTelemetry SDK 进行手动插桩
- 使用 OpenLLMetry 进行自动插桩
- 使用 SigNoz 仪表板进行监控
- 结论

## 为什么我们需要 LLM 可观测性？

LLMs 是错综复杂的系统，其中无数的过程同时发生。缺乏适当的可观测性，理解这些内部动态就变成了猜测游戏，导致效率低下和潜在的错误。

我们需要 LLM 可观测性的用例有：

- **模型性能和准确性洞见**：提供有关LLM准确性和处理能力的关键数据，指导对模型可靠性和性能的卓越改进。
- **实时性能跟踪**：实现对LLM操作的即时反馈，确保系统达到最佳效率并适应不同的性能需求。
- **资源利用和效率**：识别计算需求和效率低下，优化资源分配以提高成本效益和系统吞吐量。
- **问题检测和故障排除**：促使对LLM基础架构中的复杂问题进行快速识别和解决，减少停机时间并提高用户体验。

在本教程中，我们将使用OpenTelemetry和SigNoz来建立LLM可观测性。在开始之前，让我们简要了解一下OpenTelemetry。

## OpenTelemetry 用于 LLM 可观测性

OpenTelemetry 是一组API、SDK、库和集成，旨在标准化遥测数据（日志、指标和跟踪）的生成、收集和管理。它由云原生计算基金会支持，是可观测性领域中的领先开源项目。

由于其对遥测数据收集的全面而灵活的方法，OpenTelemetry非常适合为LLM应用进行可观测性插桩。它提供了一个统一的解决方案，用于收集和管理度量、日志和跟踪，这对于观察诸如LLMs这样的复杂系统至关重要。

使用OpenTelemetry进行LLM可观测性的一些关键优势如下：

- **统一插桩**：OpenTelemetry 提供了一个单一、统一的解决方案，用于收集全范围的遥测数据。这种统一的方法简化了插桩过程，使其更容易维护和更新。
- **厂商中立性**：OpenTelemetry 的关键优势之一是其厂商中立的设计。这意味着它可以与各种监控和分析平台配合使用。这种灵活性使组织能够在不重新插桩其应用程序的情况下切换不同的后端。
- **社区驱动和开源**：作为由社区驱动和开源的项目，OpenTelemetry受益于来自广泛的开发人员和公司的贡献。这导致持续改进、创新功能和一个强大、经过充分测试的产品。
- **定制和可扩展性**：OpenTelemetry 被设计为可扩展的，允许开发人员定制以满足其特定需求。这包括添加新的遥测源、与其他工具集成以及修改数据收集和处理行为。
- **未来保障**：随着技术和标准的发展，OpenTelemetry 的积极开发和广泛采用确保它始终与软件监控和遥测领域的最新趋势和实践保持同步。

使用 OpenTelemetry 收集的数据是与厂商无关的，可以导出到任何后端，但哪个后端最适合 OpenTelemetry 呢？

## OpenTelemetry & SigNoz - LLM 可观测性的完美组合

OpenTelemetry 不提供任何后端。在生成遥测数据后，需要将其发送到后端进行存储和可视化。SigNoz 是一款[天生支持 OpenTelemetry 的 APM](https://signoz.io/blog/opentelemetry-apm/)，从一开始就专为支持 OpenTelemetry 而构建。

SigNoz 支持 OpenTelemetry 语义约定，并为 OpenTelemetry 支持的三种不同类型的信号提供可视化。大多数流行的可观测性供应商声称他们支持 OpenTelemetry 数据，但在许多情况下[现实情况是不同的](https://signoz.io/blog/is-opentelemetry-a-first-class-citizen-in-your-dashboard-a-datadog-and-newrelic-comparison/)。

SigNoz 也是开源的，如果你使用 OpenTelemetry 和 SigNoz，那么你的整个可观测性堆栈将是开源的。

有了足够的背景，现在让我们开始演示。

## 先决条件

- Langchain 应用：如果你只是想玩一下，了解 SigNoz 的功能，这里有一个[示例的 Langchain 应用](https://github.com/SigNoz/langchain-sample-app)。
- [SigNoz 云帐户](https://signoz.io/teams/)

## 设置 SigNoz

你需要一个后端，可以将收集到的数据发送到该后端进行监控和可视化。[SigNoz](https://signoz.io/) 是一款天生支持 OpenTelemetry 的 APM，非常适合可视化 OpenTelemetry 数据。

SigNoz 云是运行 SigNoz 的最简单方法。你可以在[这里](https://signoz.io/teams/)注册一个免费帐户，并获得 30 天的免费无限制使用。

你还可以自己安装和自托管 SigNoz。查看[文档](https://signoz.io/docs/install/)以安装自托管 SigNoz。

## 在 LangChain LLM 应用中插桩的方法

- **使用 OpenTelemetry SDK 进行手动插桩**：允许进行细粒度控制和深入洞察，但实施起来比较耗时。
- **使用 OpenLLMetry SDK 进行自动插桩**：除了自动插桩 API 和数据库调用外，此版本的 SDK 还会插桩 Langchain 应用，如 OpenAI 调用和 Vector DB 检索。在此向我们在 [Traceloop](https://www.traceloop.com/blog/openllmetry) 的朋友们致以崇高的敬意，感谢他们构建了 OpenLLMetry。

## 使用 OpenTelemetry SDK 进行手动插桩

OpenTelemetry 是一个面向云原生软件的开源可观测性框架。它提供了捕获跟踪、指标和日志的工具，这对于理解应用程序的行为至关重要。以下是一个手动将 OpenTelemetry 集成到 LLM 应用程序中的指南。

**安装**：要将 OpenTelemetry 集成到您的 LLM 应用程序中，首先需要安装必要的 SDK。您可以使用以下命令执行此操作：

```bash
pip install opentelemetry-sdk
```

## 设置：设置环境变量以将数据发送到 SigNoz：

```bash
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT="ingest.{region}.signoz.cloud"
export OTEL_EXPORTER_OTLP_HEADERS="signoz-access-token=<SIGNOZ_INGESTION_KEY>"
```

您可以在 SigNoz 云帐户的 settings —> ingestion settings 下找到用于摄取的详细信息。

![](https://signoz.io/img/blog/common/ingestion-key-details.webp)

*SigNoz 中的摄取详细信息。*

**集成**：一旦您安装了 SDK，就需要将 OpenTelemetry 库合并到您的应用程序代码库中。这涉及创建代表应用程序执行操作的跟踪和跨度。以下是一个演示如何在 API 请求到 OpenAI 服务周围创建跨度的片段：

```python
from opentelemetry import trace
from opentelemetry.trace import SpanKind

tracer = trace.get_tracer(__name__)

with tracer.start_span("OpenAI_API_Request", kind=SpanKind.CLIENT) as span:
    # Code to perform the API request goes here
    response = perform_api_request()
    span.set_attribute("response.status_code", response.status_code)

```

在这个代码块中，我们使用 `start_span` 方法创建了一个新的 span。这个 span 的名称是 "OpenAI_API_Request"，表示它所代表的操作。在 span 的上下文中，我们进行了 API 请求，然后将响应状态码记录为 span 的属性。这种细粒度的记录允许进行深入监控和故障排除。

## 使用 OpenLLMetry 进行自动插桩

尽管手动插桩提供了细粒度的控制，但它可能会耗费时间。这就是自动插桩发挥作用的地方。我们在 [Traceloop](https://www.traceloop.com/blog/openllmetry) 的朋友们构建了 OpenLLMetry，这是一个用于快速插桩 Langchain 应用程序的 OpenTelemetry 库。对于我们的目的，可以将 OpenLLMetry 想象成具有内置功能来插桩 LLM 生态系统组件的 OpenTelemetry。

**安装**：要开始使用 OpenLLMetry，请安装 SDK 并在应用程序中初始化它：

```bash
pip install traceloop-sdk
```

**设置**：设置以下环境变量或将它们添加到 dotenv 文件中。

```bash
export TRACELOOP_BASE_URL=ingest.{region}.signoz.cloud
export TRACELOOP_HEADERS="signoz-access-token=<SIGNOZ_INGESTION_KEY>"
```

在应用程序入口点的开头初始化 SDK。

```python
from traceloop import Traceloop

Traceloop.init(app_name="Signoz PDF Chat")
```

**设置属性**：使用 OpenLLMetry，您可以设置关联属性，以帮助将跟踪与特定用户或会话关联起来。以下是如何实现的示例：

```python
import uuid
from traceloop import Traceloop

@app.post('/chat')
async def ask(question: str, user: User):
    Traceloop.set_association_properties({
        "user_id": user.username,
        "chat_id": str(uuid.uuid4()),
    })

    chain = load_qa_chain(ChatOpenAI(temperature=0), chain_type="stuff")
    return chain.run(input_documents=docs, question=query)
```

此代码将当前跟踪上下文与用户 ID 和唯一的聊天会话 ID 关联起来。这种元数据对于调试特定用户或会话的问题非常有价值。

**示例代码：**

```python
import uuid
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader

from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from traceloop.sdk import Traceloop
from dotenv import load_dotenv
load_dotenv()

Traceloop.init(app_name="Signoz PDF Chat")

loader = UnstructuredPDFLoader("book.pdf")
pages = loader.load_and_split()
embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(pages, embeddings).as_retriever()

queries = [
    "What is the name of the author?",
    "What is the name of the book?",
    "Who is Rich Dad?",
    "Who is Poor Dad?",
    "Give me a summary of the book?"
    "What is the 3 key takeaways from the book?"
]
for queryroot in queries:
    for querysuffix in enumerate([' Concise Answer', 'Answer in (~250 words)', 'Long Answer (~750 words)']):
        # Sets Properties to be used in the dashboard
                Traceloop.set_association_properties({ "user_id": "John McClane", "chat_id": str(uuid.uuid4()) })
        query = queryroot + querysuffix
        docs = docsearch.get_relevant_documents(query)
        chain = load_qa_chain(ChatOpenAI(temperature=0), chain_type="stuff")
        output = chain.run(input_documents=docs, question=query)
        print(output)
```

要了解更多信息并以非函数名称的方式丰富工作流程，请参阅 [OpenLLMetry 文档](https://www.traceloop.com/docs/openllmetry/tracing/annotations)。

## 使用 SigNoz 仪表板进行监控

完成上述设置后，您将能够在 SigNoz 仪表板中访问指标。您可以转到“仪表板”选项卡并尝试添加新面板。您可以[在此](https://signoz.io/docs/userguide/manage-dashboards-and-panels/)了解如何在 SigNoz 中创建仪表板。

您可以使用 SigNoz 中的[查询构建器](https://signoz.io/docs/userguide/create-a-custom-query/#sample-examples-to-create-custom-query)轻松创建图表。以下是将新面板添加到仪表板的[步骤](https://signoz.io/docs/userguide/manage-panels/#steps-to-add-a-panel-to-a-dashboard)。

![](https://signoz.io/img/blog/2024/01/llm-observability-performance-dashboard.webp)

*一个用于测量 Langchain 应用性能的仪表板，显示重要的指标如总 LLM 调用、延迟、令牌吞吐量等。*

您还可以创建用于监视运行 Langchain 应用成本的仪表板。

![](https://signoz.io/img/blog/2024/01/llm-observability-cost-monitor-dashboard.webp)

*用于监控运行 Langchain 应用成本的仪表板。*

## 带有变量的动态仪表板视图

为了满足不同团队的需求，SigNoz 支持通过仪表板变量实现动态仪表板视图。例如，应用团队可能需要查看特定于“服务”或“用户”的指标。

要使用此功能，您可以创建变量和相应的选项（请参见“[管理变量](https://signoz.io/docs/userguide/manage-variables/)”）。本文附带的示例仪表板 JSON 文件也有很好的例子。

![](https://signoz.io/img/blog/2024/01/llm-observability-dynamic-filter-dashboard.webp)

*SigNoz 中的动态仪表板，您可以根据特定服务或用户进行筛选。*

了解如何在仪表板中创建变量请点击[这里](https://signoz.io/docs/userguide/manage-variables/)。

### 阈值

为了帮助操作员快速识别关键点，您可以在 SigNoz 仪表板中为可视化设置阈值。这些阈值可以作为可接受性能水平的基准，也可以作为潜在问题的警告。

![](https://signoz.io/img/blog/2024/01/llm-observability-threshold.webp)

*设置阈值作为可接受性能水平的基准。*

### 报警

通过为任何指标创建警报，可以增强监控功能。SigNoz 允许您通过 Slack、Teams 或 PagerDuty 等各种渠道发送通知，确保对关键条件的快速响应。请[在此](https://signoz.io/docs/userguide/alerts-management/)详细指南中了解设置警报的流程。

![](https://signoz.io/img/blog/2024/01/llm-observability-alerts.webp)

*设置重要指标的警报，以在您喜欢的通知渠道中收到通知。*

### 预构建仪表板

如果您想快速开始监控 Langchain 应用程序，您可以使用 SigNoz 的两个预构建仪表板：性能仪表板和成本仪表板。您可以使用“导入 JSON”按钮加载 SigNoz 仪表板并开始使用。

- [Langchain 应用性能仪表板的 JSON](https://github.com/SigNoz/dashboards/blob/main/llm-observability/sample-chatpdf-performance-metrics.json)
- [Langchain 应用成本仪表板的 JSON](https://github.com/SigNoz/dashboards/blob/main/llm-observability/sample-chatpdf-cost-dashboard.json)

**注意**：性能仪表板适用于任何 Langchain 应用。成本仪表板的“按用户成本”面板仅在传输 user_id 属性时起作用。有关更多详细信息，请参考示例应用程序或示例代码，了解如何设置关联属性。

## 结论

在本文中，我们探讨了LLM的可观察性的重要性，并介绍了OpenTelemetry。我们演示了如何使用手动和自动的OpenTelemetry工具来为样本Langchain应用程序添加仪表。为了建立LLM的可观察性，我们选择了SigNoz，这是一个全栈、开源的工具，将日志、指标和跟踪集中在一个界面上。

OpenTelemetry正迅速成为全球开源可观察性的标准。它的使用带来了多个好处，包括所有遥测信号的统一标准和摆脱供应商锁定的自由，使其成为LLM应用的理想选择。

SigNoz是一个开源的、[基于OpenTelemetry的APM](https://signoz.io/blog/opentelemetry-apm/)，为您的所有可观察性需求提供了一个全面的后端解决方案。
