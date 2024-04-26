# Apache NiFi 2.0.0：构建 Python 处理器

![Apache NiFi 2.0.0：构建 Python 处理器的特色图片](https://cdn.thenewstack.io/media/2024/04/12717baa-python-processors-2-1024x576.jpg)

[Apache NiFi](https://nifi.apache.org/) 是一个专门用于 [数据流管理](https://thenewstack.io/the-architects-guide-to-the-modern-data-stack/) 的强大平台，它提供了许多旨在提高数据处理效率和灵活性的功能。其基于 Web 的用户界面为设计、控制和监控数据流提供了无缝体验。

NiFi 支持构建自定义处理器和扩展，使用户能够根据自己的特定需求定制平台。

凭借多租户用户体验，NiFi 确保多个用户可以同时与系统交互，每个用户都有自己的一组访问权限。

[Python 处理器](https://medium.com/cloudera-inc/building-a-library-of-python-processors-6b5517404a58) 提供了一种强大的方式来扩展 NiFi 的功能，使用户能够在数据流中利用丰富的 [Python](https://thenewstack.io/python/) 库和工具生态系统。在这里，我们将讨论将 Python 纳入 NiFi 工作流的优势，并探讨 Python 处理器可以简化数据处理任务、增强灵活性和加速开发的实际用例。

无论您是想集成机器学习算法、执行自定义数据转换还是与外部系统交互，在 Apache NiFi 中构建 Python 处理器都可以帮助您满足这些数据集成需求。

## Apache NiFi 有什么用？

NiFi 的一个突出特点是其高度可配置的特性，允许用户根据其特定要求定制数据路由、转换和系统中介逻辑。NiFi 帮助用户实现他们想要的数据处理结果，例如优先考虑容错性而不是保证交付，或者针对低延迟而不是高吞吐量进行优化。

动态优先级确定允许实时调整流中的数据优先级，而运行时修改流的能力为适应不断变化的需求增加了一层灵活性。NiFi 还结合了反压机制来调节数据流速并防止过载，确保即使在不同的工作负载下也能平稳高效地运行。

NiFi 被设计为支持垂直和水平扩展。无论是扩展以利用单台机器的全部功能，还是使用零领导者集群模型进行扩展，NiFi 都可以适应任何规模的数据处理任务。

数据来源是另一个关键特性，它允许用户跟踪数据从其开始到最终目的地的旅程。这为审计、故障排除和确保整个过程中的数据完整性提供了宝贵的见解。

[安全性](https://thenewstack.io/security/) 在 NiFi 中至关重要，它支持 SSL、SSH、HTTPS 和加密内容以及其他安全措施。可插拔的细粒度基于角色的 [身份验证和授权](https://thenewstack.io/how-do-authentication-and-authorization-differ/) 机制确保对数据流的访问受到仔细控制，允许多个团队安全地管理和共享流的特定部分。

NiFi 的设计理念受到 [基于流的编程](https://github.com/samuell/awesome-fbp) 和 [分阶段事件驱动架构](https://thenewstack.io/the-rise-of-event-driven-architecture/) 等概念的启发，提供了几个引人注目的优势：

- 直观的可视化界面，用于设计和管理数据流，提高生产力和易用性。
- 异步处理模型，支持高吞吐量和自然缓冲，以适应波动的负载。
- 内置并发管理，抽象了多线程编程的复杂性。
- 强调组件的可重用性和可测试性，促进模块化和稳健的设计方法。
- 本机支持反压和错误处理，确保数据处理管道中的稳健性和可靠性。
- 全面了解数据流动态，实现有效的监控和故障排除。

## 为什么在 Apache NiFi 中使用 Python 构建？

[Apache NiFi](https://github.com/apache/nifi) 是一个用于数据摄取、转换和路由的强大工具。NiFi 中的 Python 处理器提供了一种灵活的方式来扩展其功能，特别是对于处理非结构化数据或与外部系统（如 AI 模型或云原生向量数据库 [Milvus](https://milvus.io/) 等向量存储）集成。

在处理像
## Cloudera Data Flow

[Cloudera Data Flow](https://thenewstack.io/pulsar-nifi-better-together-for-messaging-streaming/) 可以摄取数据，Python 处理器对于实现自定义逻辑来解析和处理数据非常宝贵。例如，你可以使用 Python 从文本文档中提取特定信息，对文本数据执行情感分析，或在进一步分析之前预处理图像。

另一方面，结构化文件类型通常可以使用 NiFi 的内置处理器进行处理，而无需自定义 Python 代码。NiFi 提供了广泛的处理器，用于处理 CSV、JSON、Avro 等结构化数据格式，以及用于与 [数据库](https://thenewstack.io/data/)、[API](https://thenewstack.io/api-management/) 和其他企业系统进行交互。

当你需要与 AI 模型或 Milvus 等其他外部系统进行交互时，Python 处理器提供了一种便捷的方式，可以将此功能集成到你的 NiFi 数据流中。对于文本到文本、文本到图像或文本到语音处理等任务，你可以编写 Python 代码与相关模型或服务进行交互，并将此处理合并到你的 NiFi 管道中。

## Python：NiFi 2.0.0 中的新时代

[Apache NiFi 2.0.0](https://nifi.apache.org/documentation/v2/) 对该平台进行了一些重大改进，尤其是在 Python 集成和性能增强方面。将 Python 脚本无缝集成到 NiFi 数据流中的能力为使用各种数据源和利用生成式 AI 的强大功能开辟了广泛的可能性。

在此版本之前，虽然可以在 NiFi 中使用 Python，但灵活性可能受到限制，并且执行 Python 脚本可能不像用户希望的那样精简。然而，使用最新版本，Python 集成得到了极大改善，允许在 NiFi 管道中更无缝地执行 Python 代码。

此外，对 JDK 21+ 的支持带来了性能改进，使 NiFi 更快、更高效，尤其是在处理多线程任务时。这可以显著提高 NiFi 数据流的可扩展性和响应能力，尤其是在处理大量数据或复杂处理任务时。

引入诸如将进程组作为无状态运行和规则引擎用于开发辅助等功能进一步增强了 NiFi 的功能和可用性，为开发人员提供了更多灵活性和工具来构建强大的数据流管道。

## 一个示例处理器：Watson SDK 到基础 AI 模型

此 Python 代码定义了一个名为的 NiFi 处理器，它与 IBM WatsonX AI 服务进行交互，以根据输入提示生成响应。请注意，对于 NiFi 2.0.0，Python3.10+ 是最低要求。

[CallWatsonXAI](https://github.com/tspannhw/FLaNK-python-watsonx-processor/blob/main/WatsonXAI.py)

### 导入

```python
import json
import re
from nifiapi.flowfiletransform import FlowFileTransform, FlowFileTransformResult
from nifiapi.properties import PropertyDescriptor, StandardValidators, ExpressionLanguageScope
```

### 类定义

```python
class CallWatsonXAI(FlowFileTransform):
    ...
```

### 处理器详细信息

```python
processor_details = {
    'name': 'Call WatsonX AI',
    'version': '2.0.0-M2',
    'description': 'Calls IBM WatsonX AI service to generate responses based on input prompts.',
    'tags': ['watsonx', 'ai', 'response', 'generation'],
}
```

### 属性描述符

```python
property_descriptors = [
    PropertyDescriptor(
        name='PROMPT_TEXT',
        displayName='Prompt Text',
        description='The prompt text to send to the WatsonX AI service.',
        required=True,
        default_value='',
        validators=[StandardValidators.NON_EMPTY_VALIDATOR],
        expression_language_scope=ExpressionLanguageScope.FLOWFILE_ATTRIBUTES
    ),
    PropertyDescriptor(
        name='WATSONXAI_API_KEY',
        displayName='WatsonX AI API Key',
        description='The API key for the WatsonX AI service.',
        required=True,
        default_value='',
        validators=[StandardValidators.NON_EMPTY_VALIDATOR],
        expression_language_scope=ExpressionLanguageScope.FLOWFILE_ATTRIBUTES
    ),
    PropertyDescriptor(
        name='WATSONXAI_PROJECT_ID',
        displayName='WatsonX AI Project ID',
        description='The project ID for the WatsonX AI service.',
        required=True,
        default_value='',
        validators=[StandardValidators.NON_EMPTY_VALIDATOR],
        expression_language_scope=ExpressionLanguageScope.FLOWFILE_ATTRIBUTES
    ),
]
```

### 构造函数

```python
def __init__(self):
    super().__init__()
    self.property_descriptors.append_all(property_descriptors)
```

### getPropertyDescriptors 方法

```python
def get_property_descriptors(self):
    return self.property_descriptors
```

### transform 方法

```python
def transform(self, context, flowfile):
    ...
```

### IBM WatsonX 集成

```python
from ibm_watson import AssistantV2
...
```

### 输出处理

```python
output_attributes = {
    'watsonxai.response': json.dumps(response)
}
```

### 日志记录和返回

```python
logger.info(f'Prompt text: {prompt_text}')
return FlowFileTransformResult(flowfile, output_attributes)
```
- 返回转换结果，指示成功并提供输出数据和属性。

## 预打包 Python 处理器

NiFi 2.0.0 附带了一组多样化的 Python 处理器，它们提供了广泛的功能。

**Pinecone 的 VectorDB 接口：**此处理器促进了与 [Pinecone](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/)（一种矢量数据库服务）的交互，使用户能够高效地查询和存储数据。

**ChunkDocument：**此处理器将大型文档分解为较小的块，使其适合于处理和存储，尤其是在可能应用大小限制的矢量数据库中。

**ParseDocument：**此处理器似乎非常通用，能够解析各种文档格式，如 Markdown、PowerPoint、Google Docs 和 [Excel](https://thenewstack.io/python-delights-excel-data-nerds-plus-data-lake-enthusiasts/)，提取文本内容以供进一步处理或存储。

**ConvertCSVtoExcel：**顾名思义，此处理器将数据从 CSV 格式转换为 Excel 格式，为数据交换和处理提供了灵活性。

**DetectObjectInImage：**此处理器似乎利用深度学习技术进行 [图像中的对象检测](https://medium.com/@tspann/image-processing-with-custom-python-and-nifi-2-0-06eadc62c03c)，使用户能够分析图像数据并提取有价值的见解。

**PromptChatGPT：**此处理器听起来很有趣——它与 ChatGPT 或类似的会话式 AI 模型集成，使用户能够根据提示生成响应或参与对话。

**PutChroma 和 QueryChroma：**这些处理器与 [Chroma](https://thenewstack.io/exploring-chroma-the-open-source-vector-database-for-llms/)（一种针对大型语言模型 (LLM) 的开源数据库）相关。它们促进了 Chroma 数据库或类似系统中的数据存储（PutChroma）和检索/查询（QueryChroma）。

## 结论

在 Apache NiFi 中优先考虑 Python 集成标志着弥合 [数据工程师](https://thenewstack.io/what-data-engineering-is-and-why-its-not-just-about-data-science/) 和 [数据科学家](https://thenewstack.io/is-the-answer-to-your-data-science-needs-inside-your-it-team/) 之间差距的一个重要里程碑，同时扩展了该平台的多功能性和适用性。

通过使 Python 爱好者能够在 Python 中无缝开发 NiFi 组件，开发周期得到简化，从而加速了数据管道和工作流的实施。

对于 [NiFi 中的 Python 处理器](https://github.com/tspannhw/EverythingApacheNiFi) 来说，这是一个激动人心的时刻，为生态系统做出贡献可能非常有价值。开发和共享 Python 处理器可以扩展 NiFi 的功能，并解决特定用例。

要开始使用 NiFi，用户可以参考快速入门指南进行开发，并参考 [NiFi 开发人员指南](https://nifi.apache.org/documentation/v2/) 以获取有关如何为该项目做出贡献的更全面信息。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。