Mistral 已通知企业客户，须在 8 月 31 日前将 Vibe Work 中使用的 Google Drive 和 Microsoft SharePoint Knowledge Connectors 替换为基于 MCP 的替代方案。该公司在其 [Knowledge Connectors 文档](https://docs.mistral.ai/vibe/work/connectors/knowledge-connectors)中表示，这两个现有连接器届时将被关闭并删除。

由于没有自动迁移功能，管理员需要先安装 MCP 替代方案，然后才能让每位用户重新连接其 Google 或 Microsoft 账号。此举改变了 Vibe Work 获取公司文档的方式，但 Mistral 对新连接器背后的检索架构鲜有说明。

## Mistral 存储了一个可搜索的索引

在当前的系统中，管理员选择组织想要启用的 Google Drive 文件夹或 SharePoint 站点，然后由 Mistral 处理这些文件，并将生成的索引存储在其欧洲的数据中心内。

一旦索引就绪，用户即可连接个人账号。当他们在 Vibe Work 中进行搜索时，连接器会检查从 Google Drive 或 SharePoint 复制过来的权限，确保结果仅包含他们有权访问的文件，同时预定的同步任务会抓取后续的更改和删除记录。

这种设置使得 Mistral 能够在用户提交查询时，通过搜索预建索引来处理检索。该公司表示，索引编制可能需要几分钟到几小时不等，具体取决于组织包含的数据量，尽管这项工作会在用户开始搜索之前完成。

> 该公司表示，索引编制可能需要几分钟到几小时不等，具体取决于组织包含的数据量，尽管这项工作会在用户开始搜索之前完成。

## MCP 将检索转移到平台之外

该公司将 MCP 定义为一种通用接口，允许模型调用工具并从外部服务检索数据——这正是[正在重塑 AI 产品如何连接外部 API](https://thenewstack.io/api-mcp-agent-integration/) 的行业协议层。

6 月，Mistral 将 Google Drive 和 SharePoint 添加到一个包含 60 多种集成的目录中，但并未解释这两个连接器如何检索文档，也没有说明谁在运营底层的 MCP 服务器。这种设置的范围可以从对源 API 的实时调用到服务器管理的搜索索引，以及介于两者之间的任何组合。这种灵活性是 [MCP 在某些环境中具有吸引力而在另一些环境中显得多余](https://thenewstack.io/when-is-mcp-actually-worth-it/)的原因之一，但也意味着特定连接器的行为完全取决于其运营者。

权限规则仍然不明。由于该公司并不运行这些连接器背后的第三方服务器，因此无法保证它们的行为方式，也无法保证它们将如何处理客户数据。Mistral 曾经提供的治理与现在移交给第三方之间的差距，反映了企业在[未完全解决治理层问题的情况下](https://thenewstack.io/mcp-enterprise-agent-governance/)采用 MCP 连接器的趋势。正如其他平台所了解到的，向外部服务器敞开大门意味着必须信任协议及其运营者，并[构建相应的护栏](https://thenewstack.io/godaddy-developer-platform-domains/)。

迁移通知提供的细节更少。它没有说明 Google Drive 和 SharePoint 的 MCP 服务器是否直接从 Google 和 Microsoft 获取文件。任何缓存机制仍然未得到解释，导致客户不确定留存数据会驻留在何处。Mistral 没有承诺搜索速度会一样快，或返回的结果具有同样的质量。

> Mistral 没有承诺搜索速度会一样快，或返回的结果具有同样的质量。

即将退役的 Google Drive 连接器遵循每个文件已有的共享规则，包括组和域访问权限。“任何拥有链接的人”都可以访问的文件，并不会自动对组织内的每个人可见。SharePoint 使用 Microsoft Entra ID 组，因此仅在 SharePoint 内部创建的旧组无法被识别。

Mistral 尚未说明 MCP 替代方案是否会遵循相同的规则。OAuth 可以限制服务器对已连接用户的访问，但这并不意味着搜索结果会像在旧索引中那样被精确过滤。[该协议的设计初衷并非为了执行此类企业权限模型](https://thenewstack.io/openai-elastic-enterprise-context/)；连接器的检索层必须自行处理。

> OAuth 可以限制服务器对已连接用户的访问，但这并不意味着搜索结果会像在旧索引中那样被精确过滤。

## 删除时间表仍未解决

该公司表示，禁用 Knowledge Connector 会导致索引数据被永久删除，但弃用通知中并未说明 8 月的关闭是否会自动触发该流程，或者删除需要多长时间。这同样让管理员不确定在截止日期前是否应该自行断开旧连接器。

由于相同的连接器也可在 Vibe Code 和 Mistral 的工作流系统中使用，团队可以采用相同的方法在聊天、氛围编程和自动化作业中公开外部数据——随着 [MCP 连接器从聊天机器人扩展到生产基础设施，这种模式正变得越来越普遍](https://thenewstack.io/elevenlabs-mcp-voice-agents/)。

Mistral 还建议检查服务器输出是否存在提示注入（prompt injection）的迹象——这一建议突显了[在 AI 代理与其访问的外部服务之间建立安全保障这一挑战依然存在](https://thenewstack.io/red-teaming-enterprise-ai-agents/)。