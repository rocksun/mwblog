**在一个月前** OpenAI 为 [ChatGPT Work](https://thenewstack.io/claude-cowork-vs-chatgpt-work-benchmark/) 推出一个构建数据看板的数据智能体之后，Anthropic 在周四推出了自己的版本。

[Claude Dashboards](https://claude.com/blog/dashboards-and-motion) 目前处于测试阶段，允许用户构建实时数据看板，查看提取数据的确切查询（query），并将这些看板导出到流行的商业智能工具中。

Dashboards 可以连接到 Snowflake、Databricks、Amazon Redshift 和 ClickHouse 等企业数据源。

此外，Anthropic 还推出了 Claude Motion，它通过编写代码来为报告和图表制作动画，并且 [Docs、Slides 和 Design](https://claude.com/resources/articles/cowork-is-now-claude) 也已结束测试阶段。

## 实时看板，查询可见

要开始使用看板，用户只需连接他们选择的数据平台，并描述他们想要了解的内容。

点击这些新看板中的任何一个数字，都会调出生成该数字的查询。不想阅读 SQL 的用户也可以让 Claude 解释该数字。

Dashboards 也可以与 Claude 现有的连接器协同工作，包括 Salesforce。

该公司表示，随着数据的变化，Claude 将刷新看板，每个图表上都会带有时间戳，显示其最后更新的时间。

值得注意的是，Anthropic 并未将 Dashboards 定位为商业智能工具的替代品（尽管某些用户肯定会这样使用它）。它的功能集无法完全取代专业的 BI 工具，但想要深入挖掘的用户可以将看板迁移到 Grafana、Hex、Mixpanel、monday.com、Omni、PostHog 或 Sigma 等服务中。

对 Looker、Perplexity 和 Tableau 的支持将在稍后推出。

## 业务定义与权限

值得注意的是，Anthropic 并不是第一个提出这个想法的公司。

[OpenAI 的数据智能体](https://openai.com/index/put-data-to-work/)在大约一个月前作为 ChatGPT Work 插件推出，它也允许用户构建类似的数据看板，并连接到 Redshift、BigQuery、ClickHouse、Databricks、MongoDB、Snowflake 和 Datadog 等企业数据平台。用户还可以直接在 Power BI、Tableau、ThoughtSpot 和其他 BI 工具中构建看板。

OpenAI 和 Anthropic 支持的供应商名单略有不同，并且 OpenAI 支持诸如 Databricks Genie Ontology 等[语义层](https://thenewstack.io/microsoft-fabric-agent-context/)，但总体方向基本相同。Anthropic 告诉我们，如果这些语义模型通过连接器暴露出来，Claude Dashboards 也将支持它们。

归根结底，两家公司都希望更深地扎根于企业市场——毕竟钱在那里——并超越单纯的 Token 提供商，向企业生产力技术栈的更高层迈进。

数据仓库供应商也没有闲着。

Snowflake 在 2025 年 12 月与 Anthropic 签署了一项 [2 亿美元的协议](https://www.businesswire.com/news/home/20251203124957/en)，但 OpenAI 的数据智能体发布公告中包含了来自 Snowflake 和 Databricks 产品领导者的评论。这两家供应商也拥有各自的自然语言分析工具：[Snowflake Intelligence](https://thenewstack.io/snowflake-streamlines-data-analysis-for-enterprise-ai/) 和 [Databricks Genie](https://thenewstack.io/databricks-launches-lakehouse-ai-bi-and-governance-advances-at-annual-summit/)。

根据 OpenAI 的说法，数据智能体的查询遵循所连接账户的现有表、行和列权限。

管理员可以允许用户在组织外部共享看板，包括通过公共链接。

“看板使用的是人们已经拥有的数据访问权限。看板对你来说默认是私密的，”Anthropic 的发言人告诉 *The New Stack*。“当你分享它时，每个查看者自己的连接默认会运行其查询，因此人们只能看到他们已经有权访问的数据。在企业版计划中，看板默认处于关闭状态，直到管理员在组织设置中将其开启。在团队版和企业版计划中，看板将保留在组织内部，除非所有者开启了外部共享。”

## Claude Motion 跳过视频模型

在相关的一项举措中，Anthropic 还推出了 Claude Motion，它可以将季度更新或董事会演示文稿（board deck）中的图表等材料变成简短的动画剪辑。

由于 Anthropic 没有视频模型，Claude 是通过编写代码来为用户的文本、图表和图像添加动画来实现这一点的。但这页使其更具灵活性，用户可以轻松编辑动画，直到将它们导出为 MP4。

![](https://cdn.thenewstack.io/media/2026/10/adef6665-claude-motion-1024x576.png)

图片来源：Anthropic。

开发者们一直都在用 Claude Code 以及诸如 [Remotion](https://thenewstack.io/framework-lets-react-developers-create-video-with-code/) 和 HeyGen 的开源 [HyperFrames](https://github.com/heygen-com/hyperframes) 等框架来构建类似的视频。Motion 将这种工作流直接带入了 Claude，你可以在任何视频工具中编辑最终的剪辑。

Motion 目前正面向团队版和企业版客户进行测试。

## 可用性与企业控制

Dashboards 目前在 Claude 的付费计划中处于测试阶段。企业管理员必须同时启用 Dashboards 和 Motion。

与此同时，Docs、Slides 和 Design 将于 10 月 15 日为企业组织默认启用。自 [9 月 16 日](https://thenewstack.io/anthropic-claude-unified-interface/)以来，它们就已经在 Claude 对话中进行测试。Anthropic 表示，自那时起，用户已经创建了超过 4500 万份文档、演示文稿和设计。

Artifacts（Anthropic 对 Claude 创建的文档、演示文稿和看板的称呼）现在支持客户管理的加密密钥（CMEK）。管理员可以控制用户能看到哪些 Artifacts 模板。

4 月份发布的独立 Claude Design 网站的用户[推出于 4 月](https://thenewstack.io/anthropic-claude-design-launch/)，必须在 12 月 14 日之前完成迁移。他们的聊天记录和评论将不会被转移。