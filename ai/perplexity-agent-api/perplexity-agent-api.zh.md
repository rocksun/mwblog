紧随[上月Perplexity Computer发布](https://thenewstack.io/perplexity-computer-vibe-coding-openai-anthropic-pentagon/)之后，该公司周四[宣布](https://www.perplexity.ai/hub/blog/computer-for-enterprise)扩展Perplexity API平台，推出三款新的开发者工具：Embeddings API、Agent API和Sandbox API。

这些API向开发者公开了Perplexity Computer背后更多的系统，包括协调搜索、工具、模型和执行的编排层。

## 统一编排，取代碎片化堆栈

随着现代AI系统日益依赖多种专业模型和工具，正是这种编排层发挥着关键作用。

开发者转向多个供应商获取搜索、模型、嵌入和计算，拼凑堆栈来构建智能代理工作流已成为常态。但Perplexity凭借其新的API套件，旨在为开发者提供其自身Computer的构建模块，以便他们能够用一个单一的API密钥取代这种拼凑式方法，统一检索、智能和计算层。

Embeddings API、Agent API和Sandbox API加入了Search API，后者是API平台下的检索层，每秒索引2000亿个URL并进行数万次索引更新，[于2025年9月推出](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api)。Search API从开放网络检索，而Embeddings API则通过双向、原生量化编码器实现跨内部系统和文件的向量搜索，这些编码器可生成小4-32倍的嵌入。

Perplexity的技术人员James Liounis告诉*The New Stack*，“嵌入本质上是一种获取你自己的专有数据并创建它们的嵌入的方式，然后你可以大规模检索。”

当文本匹配不足以满足需求，开发者需要语义相似性来理解上下文时，这是一个解决方案。

“我们有点将我们用于网络的技术扩展到……这些嵌入模型……能够基本上……在你自己的内部文档上复制它，”Liounis补充道。

Search API和Embeddings API共同输入到新的Agent API，这是一个用于智能代理工作流的托管运行时，它编排完整的智能代理循环：检索、工具执行、推理和多模型回退。

凭借集成的搜索、工具执行和多模型编排，Agent API为开发者提供了一个单一的集成点，以取代碎片化的堆栈，有效地用一个端点、一个账户和一个API密钥取代了模型路由器、搜索层、嵌入提供商、沙盒服务和监控堆栈。

但Liounis表示，Agent API的价值不仅限于模型访问；它还包括访问决定如何协同使用模型和工具来完成任务的系统。开发者无需自己组装堆栈，而是可以使用一个基于Perplexity已在生产中使用的基础设施构建的更统一的系统。

> “我们希望减轻开发者构建智能代理所需的繁琐工作。”

“我们希望减轻开发者构建智能代理所需的繁琐工作，”Liounis说。“我们希望他们能够访问最好的搜索；与支持我们核心业务的搜索相同。我们希望他们能够本质上在构建智能代理时专注于真正重要的事情——智能代理的能力——而不是担心‘我将使用哪个模型？’或者‘我将如何同时集成所有这些不同的模型？’”

Sandbox API则提供Python、JavaScript和SQL的隔离执行，具有文件系统访问、运行时包安装和内置资源限制。

## “一切皆计算机”——计算机为人人所有

这些新的API是Perplexity Computer更广泛的扩展，以及该公司[“一切皆计算机”](https://www.perplexity.ai/hub/blog/everything-is-computer)理念的一部分。

“Computer是一系列广泛的工具，”Liounis说，并补充道，它“是一系列广泛的模型和各种连接器，它们位于……主编排器之上。Agent API本质上就是……将这些能力扩展给开发者。”

并且横跨Perplexity自己的生态系统，包括个人计算机（Personal Computer）和企业计算机（Computer for Enterprise）。

个人计算机（Personal Computer）可以在专用Mac mini上24/7运行，连接到本地应用程序和Perplexity的安全服务器，充当数字代理，即代表用户从任何设备、任何地方协调工具、任务和文件。安全检查包括每个会话的完整审计跟踪、敏感操作的强制批准和紧急终止开关。

其专注于企业的产品，企业计算机（Computer for Enterprise），也同样扩展了Computer的能力。

企业计算机（Computer for Enterprise）原生连接团队日常使用的工具（例如，Snowflake、Salesforce和Hubspot等数百种工具），自然融入现有工作流。例如，为了创建财务模型，Computer可以接管编写和运行查询，然后提供结构化的结果，而无需你等待数据或分析团队。

在这里，安全性通过SOC 2 Type II合规性、SAML SSO、审计日志和每个查询的安全沙箱得到提升。

Perplexity功能的其他扩展包括更深入的研究能力和工具。Perplexity Finance，Computer的数据和分析层，现在可以访问40多个实时金融工具，例如S&P Global和Coinbase。同样，Premium Sources允许Computer直接将付费来源（例如，Statista、CB Insights）引入研究工作流。

Embeddings API和Agent API现已上线，Sandbox API处于测试阶段。

“Perplexity本身就是一个编排器，”Liounis说。“我们的大多数产品……都是通过将许多前沿模型结合在一起并调整这些非常庞大和复杂的智能代理循环而构建的……我们已经在这个智能代理领域深入发展，我们真的想开始与开发者分享这些经验。”