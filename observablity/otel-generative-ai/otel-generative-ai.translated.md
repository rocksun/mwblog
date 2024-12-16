# 用于生成式AI的OpenTelemetry

随着组织越来越多地采用大型语言模型（LLM）和其他生成式AI技术，确保可靠的性能、效率和安全性对于满足用户期望、优化资源成本以及防范意外输出至关重要。对AI操作、行为和结果进行有效的可观测性可以帮助实现这些目标。OpenTelemetry正在增强以专门支持生成式AI的这些需求。

两个主要资源正在开发中，以实现这一目标：**语义约定**和**检测库**。第一个检测库针对[OpenAI Python API库](https://pypi.org/project/openai/)。

[语义约定](/docs/concepts/semantic-conventions/)建立了跨平台遥测数据结构和收集的标准化指南，定义了输入、输出和操作细节。对于生成式AI，这些约定通过标准化模型参数、响应元数据和令牌使用等属性，简化了AI模型的监控、故障排除和优化。这种一致性支持跨工具、环境和API的更好可观测性，帮助组织轻松跟踪性能、成本和安全性。
[检测库](/docs/specs/otel/overview/#instrumentation-libraries)正在[OpenTelemetry Python Contrib](https://github.com/open-telemetry/opentelemetry-python-contrib)下的[instrumentation-genai](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation-genai)项目中开发，以自动化生成式AI应用程序的遥测数据收集。第一个版本是一个用于检测OpenAI客户端调用的Python库。该库捕获跨度和事件，以结构化格式收集模型输入、响应元数据和令牌使用等重要数据。

## 生成式AI的关键信号
[生成式AI的语义约定](/docs/specs/semconv/gen-ai/)侧重于通过三个主要信号捕获对AI模型行为的洞察：[跟踪](/docs/concepts/signals/traces/)、[指标](/docs/concepts/signals/metrics/)和[事件](/docs/specs/otel/logs/event-api/)。

这些信号共同提供了一个全面的监控框架，能够更好地进行成本管理、性能调整和请求跟踪。

### 跟踪：跟踪模型交互
跟踪跟踪每个模型交互的生命周期，涵盖输入参数（例如，temperature、top_p）和响应细节，如令牌计数或错误。它们提供了对每个请求的可见性，有助于识别瓶颈并分析设置对模型输出的影响。

### 指标：监控使用情况和性能
指标汇总高级指标，如请求量、延迟和令牌计数，这对于管理成本和性能至关重要。对于具有速率限制和成本考虑的依赖于API的AI应用程序，此数据尤其重要。

### 事件：捕获详细的交互
事件记录模型执行期间的详细时刻，例如用户提示和模型响应，提供对模型交互的细粒度视图。这些见解对于调试和优化可能出现意外行为的AI应用程序非常宝贵。

#### 注意
请注意，我们决定使用[发出的事件](/docs/specs/otel/logs/api/#emit-an-event)以及生成式AI的语义约定中的[日志API](/docs/specs/otel/logs/api/)规范。事件允许我们为我们捕获的用户提示和模型响应定义特定的[语义约定](/docs/specs/semconv/general/events/)。此API的添加正在开发中，并被认为是不稳定的。

### 使用供应商特定属性扩展可观测性
语义约定还定义了针对OpenAI和Azure推理API等平台的供应商特定属性，确保遥测捕获一般和提供商特定的详细信息。这种额外的灵活性支持多平台监控和深入的见解。

## 为OpenAI构建Python检测库
这个基于Python的OpenTelemetry库捕获OpenAI模型的关键遥测信号，为开发人员提供针对AI工作负载量身定制的开箱即用的可观测性解决方案。该库[托管在OpenTelemetry Python Contrib存储库中](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/opentelemetry-instrumentation-openai-v2%3D%3D2.0b0/instrumentation-genai/opentelemetry-instrumentation-openai-v2)，自动收集来自OpenAI模型交互的遥测数据，包括请求和响应元数据以及令牌使用情况。

随着生成式AI应用程序的增长，其他语言的附加检测库将陆续推出，从而扩展OpenTelemetry对更多工具和环境的支持。当前库对OpenAI的关注突显了其在AI开发中的普及程度和需求，使其成为有价值的初始实现。
### 示例用法
这是一个使用 OpenTelemetry Python 库监控带有 OpenAI 客户端的生成式 AI 应用程序的示例。

安装 OpenTelemetry 依赖项：

```bash
pip install opentelemetry-distro
opentelemetry-bootstrap -a install
```

设置以下环境变量，根据需要更新端点和协议：

```bash
OPENAI_API_KEY=<replace_with_your_openai_api_key>
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_SERVICE_NAME=python-opentelemetry-openai
OTEL_LOGS_EXPORTER=otlp_proto_http
OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
# 设置为 false 或删除以禁用日志事件
OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true
```

然后在您的 Python 应用程序中包含以下代码：

```python
import os
from openai import OpenAI

client = OpenAI()
chat_completion = client.chat.completions.create(
    model=os.getenv("CHAT_MODEL", "gpt-4o-mini"),
    messages=[
        {
            "role": "user",
            "content": "Write a short poem on OpenTelemetry.",
        },
    ],
)
print(chat_completion.choices[0].message.content)
```

然后使用 `opentelemetry-instrument` 运行示例：

```bash
opentelemetry-instrument python main.py
```

如果您没有运行的服务来收集遥测数据，您可以使用以下命令导出到控制台：

```bash
opentelemetry-instrument --traces_exporter console --metrics_exporter console python main.py
```

完整的示例
[此处提供](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation-genai/opentelemetry-instrumentation-openai-v2/example)。

通过这种简单的检测，可以开始捕获生成式 AI 应用程序的跟踪。以下是从
[Aspire 仪表板](https://learn.microsoft.com/dotnet/aspire/fundamentals/dashboard/standalone?tabs=bash)
进行本地调试的示例。

要启动 Jaeger，请运行以下 `docker` 命令并在您的 Web 浏览器中打开 `localhost:18888`：

```bash
docker run --rm -it -d -p 18888:18888 -p 4317:18889 -p 4318:18890 --name aspire-dashboard mcr.microsoft.com/dotnet/aspire-dashboard:9.0
```

![Aspire 仪表板中的聊天跟踪](/blog/2024/otel-generative-ai/aspire-dashboard-trace.png)

以下是
[Jaeger](https://www.jaegertracing.io/docs/1.63/getting-started/#all-in-one) 中捕获的类似跟踪。

要启动 Jaeger，请运行以下 `docker` 命令并在您的 Web 浏览器中打开 `localhost:16686`：

```bash
docker run --rm -it -d -p 16686:16686 -p 4317:4317 -p 4318:4318 --name jaeger jaegertracing/all-in-one:latest
```

![Jaeger 中的聊天跟踪](/blog/2024/otel-generative-ai/jaeger-trace.png)

捕获聊天的内容历史记录也很容易，以便于调试和改进您的应用程序。只需设置环境变量
`OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT`
如下所示：

```bash
export OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=True
```

这将开启内容捕获，它会收集包含有效负载的 OpenTelemetry 事件：

![内容捕获 Aspire 仪表板](/blog/2024/otel-generative-ai/aspire-dashboard-content-capture.png)

## 加入我们，共同塑造生成式 AI 可观测性的未来

社区协作是 OpenTelemetry 成功的重要因素。我们邀请开发人员、AI 从业人员和组织贡献代码、分享反馈或参与讨论。探索 OpenTelemetry Python Contrib 项目，贡献代码，或帮助塑造 AI 可观测性的发展。

我们目前的贡献者来自 [亚马逊](https://aws.amazon.com/)、[Elastic](https://www.elastic.co/)、[谷歌](https://www.google.com/)、[IBM](https://www.ibm.com)、[Langtrace](https://www.langtrace.ai/)、[微软](https://www.microsoft.com/)、[OpenLIT](https://openlit.io/)、[Scorecard](https://www.scorecard.io/)、[Traceloop](https://www.traceloop.com/) 等！

欢迎加入社区！更多信息可在
[生成式 AI 可观测性项目页面](https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md) 找到。