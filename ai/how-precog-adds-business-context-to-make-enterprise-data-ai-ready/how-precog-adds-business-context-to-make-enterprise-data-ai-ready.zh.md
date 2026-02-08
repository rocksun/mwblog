从Salesforce、[SAP](https://www.sap.com/index.html?utm_content=inline+mention) Ariba或NetSuite等企业工具中提取数据相对容易。但让[数据可供AI模型](https://thenewstack.io/ai-data-dilemma-balancing-innovation-with-ironclad-governance/)推理使用则要困难得多。仅仅拥有大量的表格和列或巨大的多维JSON文件并不能帮助这些模型对数据进行推理。这里缺少的是数据生成时的业务上下文。

专注于帮助企业从软件即服务（SaaS）API源中提取数据并为分析或AI应用做好准备的[Precog](https://www.precog.com/)，今天将推出一项新功能，旨在将业务上下文带回数据提取过程中。

## 准备企业数据以供AI使用的挑战

Precog首席执行官Jon Finegold在发布前的一次采访中表示，为AI分析准备数据的手动过程可能需要数月。

“当你进入企业并希望开始分析你的任务关键型业务数据时，它往往被孤立在各种应用中，有时企业内部有超过100个应用，”Finegold说。“然后，将数据从这些应用中取出——不仅仅是提取和加载，而是赋予其足够的上下文，以便模型能够真正理解它——这是一个非常手动的过程。”

尽管大型语言模型（LLM）的能力不断增强，但在对大量数据进行推理时，它们也并非完全可靠。

“如果有人听说他们要把所有数据都发送给Gemini，那么不仅分块和token化等操作会非常昂贵，而且每次调用时你的答案都会不同，”Finegold指出。

![Precog数据摄取平台示意图。](https://cdn.thenewstack.io/media/2026/01/0a8978fe-precog_architecture-semantic-modeling-fnl-scaled.jpg)
Precog的数据摄取平台。（图片来源：Precog）

## Precog如何为数据添加业务上下文

为了解决这些问题，Precog正在采取一种不同的方法来帮助客户从数据中获得更多价值。当Precog用户想要配置一个新源以用于AI应用时，他们现在可以大致描述他们的用例（例如，“我想了解哪些客户最有利可图，哪些客户正在让我们亏损”）。Precog将利用其现有的ETL能力查看SaaS应用中可用的数据，并仅提取此特定用例所需的字段，并添加必要的上下文以帮助模型理解这些字段的含义。

这里需要注意的是，Precog从不真正将公司数据传递给LLM。相反，它将实际数据加载到数据仓库中，只将元数据传递给其语义引擎。

## 生成合成问题以构建语义模型

Precog构建此系统的一个巧妙之处在于，它还使用另一个模型自动创建数百个潜在问题——你可以将其视为合成问题生成。

正如Precog首席产品官Becky Conning所指出的，这里的想法是生成一个“问题矩阵，它将允许LLM生成语义模型，从而能够回答所有这些问题。”

Conning认为，所有这些都是必要的，因为简单地构建一个与单个标准化表绑定的巨大语义模型将只能回答非常有限的问题集。

## 利用LLM进行自然语言到SQL查询

同时，包含所有数据也行不通。“如果你包含所有数据——其中一些应用程序包含数十万个数据集，每个数据集由于JSON结构可能不仅仅代表一个表，它可能包含分解后的维度信息——那么Cortex就无法工作。实际上，任何这些NLQ LLM都无法工作。”

现代LLM的优势在于它们非常擅长将自然语言查询转换为SQL，因此为了查询数据，Precog不直接依赖模型——也不向该模型馈送数据——而是使用[Snowflake](https://www.snowflake.com/?utm_content=inline+mention)的Cortex NLQ LLM。该服务也可以使用其他LLM，但团队指出他们确实喜欢Cortex NLQ用于此用例。

总的来说，这看起来是利用LLM发挥其最大优势的明智方式，而不是试图将它们强行塞入现有技术更可能失败的用例中。