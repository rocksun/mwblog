每家企业都在摸索如何让其AI工具与自身数据协同工作。与此同时，所有与这些企业合作的大型企业级供应商（如 SAP、Microsoft、Salesforce、Workday 等）都在争夺成为管理和保护这些数据的核心枢纽。

但对于那些希望自己动手的公司呢？

周三，英伟达[宣布](https://blogs.nvidia.com/blog/enterprise-platforms-agent-toolkit)了它将如何为企业智能体提供理解公司数据所需的上下文，且完全不与已经存储数据的平台形成竞争。

在周三的 GTC 柏林大会上，该公司将 Agent Knowledge Foundation（智能体知识基础）加入了其[Agent Toolkit（智能体工具包）](https://thenewstack.io/thenewstack.io/nvidia-openshell-agent-runtime/)中。这一全新的开源组件集合捆绑了该公司的 Nemotron Retriever 模型、全新的 Auto-Ontology 库、用于结构化数据的 Kumo 系列模型以及 CUDA-X 数据处理库。

英伟达表示，通过这个系统，数据可以留在原地，并继续按照这些公司已经建立的访问规则进行管理。

正如英伟达代理式 AI 产品副总裁 Adel El Hallak 告诉 *The New Stack* 的那样，如今企业或许可以将智能体连接到 Snowflake 等供应商，但这并不能帮助智能体理解整体的企业上下文。

“我希望事情能像连接我的 Snowflake 系统、连接我的电子邮件交换、连接我的知识库那样简单，然后突然之间，神奇的是，AI 就理解了所有数据。但现实并非如此，”他说。

El Hallak 认为，大语言模型“非常擅长预测下一个 Token”，但当面对一个“包含整整一堆标签页”的单一电子表格时，智能体会很难找到特定的内容。“它会举步维艰，”他说。

## 更好的检索，更少的查找

“在智能体的世界里，你需要最准确的嵌入模型或重排模型，”El Hallak 说，即使这会给每次查找增加一点延迟。随后，智能体就能获得“更多相关的信息。因此，最终的查找次数和总体延迟实际上会下降。”

英伟达表示，在其开源 OpenSearch 设置的测试中，Nemotron Retriever 嵌入模型的搜索相关性提升了 65%，所需的搜索步骤更少，且几乎没有增加延迟。英伟达称，SAP 微调版本的重排器运行速度快了近三倍，而 ServiceNow 在延迟减少近 25% 的同时获得了更好的重排质量。

## 从 RAG 到本体论

“RAG 曾经很棒，但它足够好吗？”El Hallak 问道。他说，知识图谱比基于相似性拉取文本块的检索增强生成（RAG）更能代表概念及其之间的关系。

英伟达的 [Auto-Ontology 库](https://catalog.ngc.nvidia.com/orgs/nvidia/-/containers/auto-ontology/-)从公司自己的表格中构建这些图谱，并将原始数据映射到客户、产品和订单等业务概念。它在英伟达的 NGC 软件目录中的列表展示了一个 REST API 和一个模型上下文协议（MCP）服务器，智能体可以使用它们来查询。

“你和我，我们很容易理解。当你查看移动运营商时，级别（tier）和套餐（plan）是同一回事，”El Hallak 说，但大语言模型“会把这些弄混。”

今年 2 月，英伟达以据报道 7500 万美元的价格收购了 Illumex，这是一家为企业数据自动化创建语义层和本体论的以色列初创公司。当时，英伟达发言人告诉 [Globes](https://en.globes.co.il/en/article-1001535871)，该团队在本体论方面的专业知识将有助于构建“使组织能够采用智能体式 AI 的库和模型”。

## 来自表格的预测

Kumo 是英伟达在 6 月份的一笔交易中收购的初创公司，The Information 估值超过 4 号亿美元，该公司构建了[用于关系数据的基础模型](https://thenewstack.io/kumo-ai-foundation-models/)。此后，英伟达在 Hugging Face 上以开源权重形式发布了几个 Kumo 模型，其中包括 9 月发布的 Kumo Tabular。

El Hallak 表示，这些模型取代了数据团队过去“为每个分类、每个流失、每个情感分析”构建的每个任务的管道。

“本体论的全部意义……是在你创建这些知识图谱时带来统一性，从而使各个表格之间保持[一致性]，然后你就可以使用 Kumo 来驱动预测性分析，”他说。

## 合作伙伴，而非竞争对手

“我并不想与 Snowflake 等公司竞争。恰恰相反，我想与他们合作，”El Hallak 说。

英伟达自己的供应链团队通过 Palantir 的 Foundry 平台使用了 Agent Knowledge Foundation，[在此前两家公司合作的基础之上](https://thenewstack.io/ai-factories-are-among-the-most-complex-systems-ever-built-nvidia-and-palantir-turn-nvidias-supply-chain-into-a-proving-ground-for-sovereign-ai/)更进一步。Databricks 正在将 Kumo 异常检测模型与 Genie Ontology（其在 6 月推出的上下文层）进行配对，而 Snowflake 客户可以在 Snowflake Notebooks 中运行 Kumo 模型。

“我没有在考虑 ACL（访问控制列表）、数据访问以及所有这些事情。这就是我需要合作伙伴的原因，”El Hallak 在谈到其企业合作伙伴提供的访问控制列表和其他安全功能时说道。

## 掌控技术栈

并非每家供应商都走这条路线。SAP 在 7 月完成了对 TabPFN 表格模型背后的公司 Prior Labs 的收购，并在四年内承诺投入超过 10 亿欧元。它现在在 SAP AI Core 中提供 TabPFN-3.5 Plus 以及[其自己的 RPT 模型](https://thenewstack.io/sap-expands-its-ai-stack-for-developers/)。

与此同时，英伟达通过 Hugging Face 分发其模型，该公司同意在 9 月以 129 亿美元收购 Hugging Face。“我们只是构建小权重和模型，并将它们发布在 Hugging Face 上，”El Hallak 说。

这使得英伟达专注于构建模型，而像 Snowflake 和 Databricks 这样的公司则保留了对数据及其周围权限的控制权。