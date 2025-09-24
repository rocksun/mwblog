
<!--
title: Snowflake、Salesforce推出AI数据统一新标准
cover: https://cdn.thenewstack.io/media/2025/09/d2818833-arturo-esparza-oji8px8laro-unsplash.jpg
summary: Snowflake推出开放语义互换(OSI)倡议，旨在为AI和BI数据创建通用语义标准。以YAML构建，解决数据定义冲突，实现系统互操作性。由Snowflake、Salesforce等牵头。
-->

Snowflake推出开放语义互换(OSI)倡议，旨在为AI和BI数据创建通用语义标准。以YAML构建，解决数据定义冲突，实现系统互操作性。由Snowflake、Salesforce等牵头。

> 译自：[Snowflake, Salesforce Launch New Standard To Unify Data for AI](https://thenewstack.io/snowflake-salesforce-launch-new-standard-to-unify-data-for-ai/)
> 
> 作者：Joab Jackson

商业智能服务提供商 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) 已启动一项供应商中立的倡议，旨在为结构化和非结构化商业智能数据添加上下文信息创建标准。

开放语义互换 (OSI) 将以 YAML（很可能）构建，并最终由一个独立的实体管理，其目标是成为一个“通用语义数据框架”，使不同组织能够使用一套通用的定义在其平台之间共享数据。

目前，[Snowflake](https://thenewstack.io/qa-snowflake-analytics-chief-on-centralizing-data-for-ai/)、[Salesforce](https://www.salesforce.com/data/?utm_content=inline+mention) 和 [dbt Labs](https://www.getdbt.com/product/what-is-dbt) 正在牵头这项工作。该项目的其他合作伙伴包括 BlackRock、Mistral AI 和 RelationalAI。该项目于周二公布了其章程。

## 对 AI 通用数据标准日益增长的需求

尽管我们已经有很多数据共享标准，但 AI 代理的日益普及带来了新的标准化需求。

“我与之交谈的每一个客户都在努力弄清楚如何满足对代理式体验的疯狂需求，以及如何以一种不会造成信息冲突混乱的方式来实现，”负责 Snowflake 数据云产品管理的 Josh Klahr 说。

他表示，相互冲突的定义长期以来一直是商业智能领域面临的挑战，但现在代理式开发已成为现实，对某种统一性的需求猛增。

Klahr 说：“你需要有一个单一的语义模型，理想情况下，它应该处于一个能够实现所有不同合作伙伴之间互操作性的层。”

到目前为止，大多数组织都有多种数据源，采用多种格式，这使得 AI 系统难以查找并进行计算。Snowflake 的客户平均使用五种不同的商业智能工具。

“广告支出”、“活跃客户”和“毛利率”等概念和公式在不同系统中可能定义不同。OSI 将为所有这些提供统一的标准定义。

Klahr 说：“这样，大型语言模型（LLM）就不需要弄清楚如何计算利润率，你只需给它度量指标的名称，该名称已与实际计算相关联，大型语言模型（LLM）就知道如何计算利润率。”

“然后，当我在 Tableau 或 ThoughtSpot 中请求利润率时，计算结果是一致的。”

## 推出开放语义互换 (OSI)

新成立的 OSI 工作组的职责不是提供定义，而是建立一个用于指定各种定义格式。由最终用户来定义度量指标及其定义。

Klahr 说，OSI 的实际规范尚未发布。工作组需要先启动并运行起来。

他们最有可能基于 [YAML](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/) 来构建 OSI 的格式，YAML 是一种[广泛使用的](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/)配置语言，具有一些[基本编程能力](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)。他说，该工作组的许多参与者已经将 YAML 用于各种任务。

BlackRock 在一份新闻声明中表示，OSI 将与其 [Aladdin 平台](https://www.blackrock.com/aladdin/resources/faqs)合作，在该平台中，它将通过为公共和私人市场提供通用的数据语言来统一投资管理流程。

Tableau 首席产品官 Southard Jones 在一份声明中说：“这是商业数据的‘罗塞塔石碑’。”

## OSI 框架如何旨在标准化定义

Snowflake 工程师们将语义层的想法建立在其自身 AI 和商业智能 (BI) 平台的一项名为[语义视图](https://docs.snowflake.com/en/user-guide/views-semantic/overview)的功能上，该功能帮助客户协调多个数据源。他们可能正在运行商业智能工具并维护数据目录，但很少能真正实现交叉引用。

Klahr 说：“互操作性问题确实开始出现在客户对话中。”

语义定义文件将包含许多其他属性，包括指向基础表的指针、联合键和关系。它还可能包含该定义的一组度量、同义词和度量，以及针对 AI 的自定义指令。

## 供应商和开源社区的作用

工作组目前没有计划构建运行时引擎。这将是供应商提供的工作。例如，Snowflake 本身就有一项服务，可以将类似 OSI 的定义渲染为物化视图。

该工作组计划创建一个开源存储库，以存放规范本身以及不同合作伙伴可能贡献的转换器。

它还邀请其他组织加入。“我们希望尽可能多的成员参与，”他说。

OSI 工作组并非唯一旨在为 AI 提供更多元数据以供使用的努力。RSS 聚合格式的创建者帮助推出了 [“真正简单的许可”](https://rslcollective.org/)，这是一个[类似 robots.txt 的文件](https://arstechnica.com/tech-policy/2025/09/pay-per-output-ai-firms-blindsided-by-beefed-up-robots-txt-instructions/)，旨在提供统一的方式向网络爬虫表达内容版权和许可信息。