发布在数据仓库中的 AI 智能体运行的查询量，可能比人类时代的分析工作流多出十倍甚至百倍。对于任何封闭的数据生态系统来说，问题在于这些查询往往都会路由到同一条昂贵的计算路径上。

[Anjan Kundavaram](https://www.linkedin.com/in/anjan-kundavaram/)，[Fivetran](https://www.fivetran.com/) 的首席产品官，在 *The New Stack* 播客的新一期节目中表示：“这有点像一直在用兰博基尼来除草。”

> “这有点像一直在用兰博基尼来除草。”

Anjan Kundavaram 在我们在 Google Cloud Next 大会上的交谈中阐述了这一观点。Fivetran 利用这次活动推行公司称为“开放数据基础设施（Open Data Infrastructure）”的框架，并推出了 [开放数据基础设施数据访问基准（Open Data Infrastructure Data Access Benchmark）](https://www.businesswire.com/news/home/20260422406594/en/Fivetran-Launches-Industry-Benchmark-Exposing-How-Vendors-Limit-Data-Access-for-AI-Workloads)，旨在让供应商更难悄悄地对客户的 AI 工作负载征收“隐形税”。这一论点在时机上极具优势。TNS [今年早些时候报道称](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/)，大多数企业数据系统在构建之初从未考虑过智能体集群。

VIDEO

Anjan Kundavaram 所描述的经济学转变，始于一个关于智能体的反直觉事实：它们不是人类。它们不需要在几秒钟内得到答案。

“如果智能体认为能为你节省 10 倍的成本，它可能会愿意花更多时间，”他说道。

在拥有多个可用计算引擎的堆栈中，智能体可以将昂贵的分析问题路由到一个引擎，而将便宜的问题路由到一个更轻量、成本更低的选项。但在封闭堆栈中，每一个问题都要经过那扇同样昂贵的大门。

这是 AI 成本挤压的一个来源。另一个来源是当 AI 所需的数据和上下文最初没有被整合时会发生什么。

> “这将是一场‘三重打击’。”

Anjan Kundavaram 表示，如果客户的信息分布在许多不同的系统中，且其上下文不在一处，其后果就会堆叠：AI 回答质量差、由于智能体运行的查询多得多而导致成本急剧上升，以及由于在弱上下文中运行这些查询而造成的浪费。

“所以这将像是一场‘三重打击’，”Anjan Kundavaram 说。

大多数数据组织内部的本能反应是加强管控。Anjan Kundavaram 认为这正是错误的做法：“一家大公司的数据负责人告诉我，‘嘿，我们的分析预算——仅仅是查询费用——就上涨了很多，’”他说。“事实上，我们 [Fivetran] 内部的分析负责人也曾表示，‘等等，我得加强控制。’但我们的态度是，‘不，不，不要管控。让我们去创新。’”

他更广泛的处方是：只有当客户拒绝封锁本能，转而投资于开放基础设施和语义规范时，智能体分析带来的生产力释放才会真正实现。

Fivetran 在提出这一论点时显然有商业利益考量，并且公司一直忙于将其转化为产品。TNS [报道过](https://thenewstack.io/fivetran-brings-data-lake-interoperability-to-google-cloud/) Fivetran 在 Google Cloud 上的数据湖互操作性工作，且该公司在三月份将 [SQLMesh 捐赠给了 Linux 基金会](https://thenewstack.io/fivetran-donates-sqlmesh-lf/)。

更难的问题在于，企业买家是否会像 Anjan Kundavaram 那样看待成本曲线，并在账单开始寄达之前足够快地采取行动。这一部分仍取决于他们自己。