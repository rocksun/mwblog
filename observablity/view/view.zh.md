可观测性的未来不仅仅是仪表盘和警报——而是关于**会话式运维**。今天，我们很高兴推出 **OneUptime MCP Server**，这是一个生产就绪的 Model Context Protocol 实现，它将 AI 原生的可观测性带入您的开发工作流程。

## 什么是模型上下文协议？

模型上下文协议 (MCP) 是一种开放标准，使 AI 助手能够安全地连接到外部系统和服务。可以将其视为 AI 模型和现实世界工具之间的桥梁——允许 AI 助手代表您执行操作、查询数据和自动化复杂的工作流程。

有了 MCP，您无需将错误日志复制粘贴到 ChatGPT 中或手动创建事件报告，只需让您的 AI 助手：

* “检查我们的生产 API 监控器的状态”
* “为数据库中断创建一个严重事件”
* “显示我过去一小时的错误日志”

## 为什么 OneUptime + MCP = 游戏规则改变者

作为**开源可观测性平台**，OneUptime 与 MCP 的集成代表着向**AI 优先运维**的根本转变：

### **🤖 自然语言运维**

用简单的对话代替复杂的 CLI 命令和仪表板导航：

```
Human: "Are there any incidents in our production project right now?"

AI: Let me check your OneUptime incidents...
[Queries OneUptime via MCP]
I found 2 open incidents in your production project:
- Critical: Database connection timeout (started 15 minutes ago)
- Warning: High memory usage on web servers (started 2 hours ago)

Would you like me to get more details or take any actions?
```

### **🌊 工作流程自动化**

通过自然对话将多个操作链接在一起：

```
Human: "Something's wrong with our checkout service"

AI: I
1. Check monitors for the checkout service
2. Look for recent incidents
3. Query error logs from the last 30 minutes
4. Create an incident if needed

[Executes multiple MCP calls]

I found elevated error rates and created incident #INC-2024-001 
"Checkout Service Degradation" with high severity. The incident 
has been assigned to the on-call engineer.
```

## 全面的 OneUptime 集成

MCP 服务器通过 AI 对话提供对 OneUptime 功能的**完全访问**：

### **📊 监控与告警**

* **监控管理**：跨所有类型创建、更新和查询监控器
* **告警操作**：确认、解决和升级告警
* **状态检查**：服务和基础设施的实时状态
* **探针管理**：配置和监控全球探针位置

```
AI Tools Available:
- oneuptime_create_monitor
- oneuptime_list_onitors  
- oneuptime_get_monitor
- oneuptime_update_monitor
- oneuptime_delete_monitor
- oneuptime_count_monitors
```

### **🚨 事件管理**

* **事件生命周期**：创建、更新和解决事件
* **团队协作**：分配事件和管理升级
* **沟通**：添加注释、更新和状态更改
* **事后分析**：记录解决方案和经验教训

```
Example Conversation:
Human: "Create a critical incident for our API being down"

AI: I

[Creates incident via MCP]

✅ Created incident INC-2024-001 "API Service Outage"
- Severity: Critical
- Status: Created
- Assigned to: On-call team
- Created: 2024-07-01 14:30 UTC

The incident has been automatically escalated to your on-call policy.
```

### **📈 日志分析与指标**

* **日志查询**：使用自然语言搜索和过滤日志
* **指标分析**：查询性能数据和趋势
* **追踪调查**：分析分布式追踪和跨度
* **错误调查**：深入研究异常和错误

```
Human: "Show me all error logs from the checkout service in the last hour"

AI: [Queries logs via MCP]
Found 47 error logs from checkout service in the last hour:

Top errors:
- Database timeout (23 occurrences)
- Payment gateway 503 (12 occurrences)  
- Redis connection failed (8 occurrences)
- Session validation error (4 occurrences)

Would you like me to create an incident or investigate any specific error?
```

### **👥 团队与项目管理**

* **用户管理**：添加、更新和管理团队成员
* **权限控制**：配置角色和访问级别
* **项目组织**：管理多个项目和环境
* **值班安排**：更新计划和处理覆盖

## 真实世界的用例

### **1. 智能事件响应**

```
Human: "Our customers are reporting the website is slow"

AI: Let me investigate this issue for you:

1. Checking website monitors... ✅
   - Response time: 2.3s (normal: 0.8s)
   - Availability: 98.2% (down 1.8%)

2. Looking for related incidents... ✅
   - Found 1 similar incident from last month

3. Querying recent logs... ✅
   - High database query times detected
   - Memory usage at 89% on web servers

4. Creating incident... ✅
   - Created INC-2024-002 "Website Performance Degradation"
   - Assigned to platform team
   - Added investigation findings

Recommended actions:
- Scale web servers
- Investigate database performance
- Monitor response times closely
```

### **2. 主动监控设置**

```
Human: "We're launching a new microservice called 'user-auth' at https://api.example.com/auth/health. Can you set up monitoring for it?"

AI: I

1. Creating health check monitor... ✅
2. Setting up performance monitoring... ✅
3. Configuring error rate alerts... ✅
4. Adding to production status page... ✅

Your user-auth service is now fully monitored with:
- Health endpoint checks every 30 seconds
- Response time alerts if > 2 seconds
- Error rate alerts if > 5%
- Automatic incident creation for failures

The service is also visible on your public status page.
```

### **3. 运维报告**

```
Human: "Give me a summary of our infrastructure health this week"

AI: Here's your infrastructure health summary for this week:

📊 **Monitors**: 47 active (2 new this week)
- Uptime: 99.8% average
- Response time: 0.7s average
- 3 brief outages (total: 14 minutes)

🚨 **Incidents**: 8 total (5 resolved, 3 ongoing)
- Critical: 1 (database issue - resolved)
- High: 2 (API rate limiting - ongoing)
- Medium: 5 (minor performance issues)

📈 **Performance Trends**:
- Database queries 15% slower than last week
- Error rates down 8% overall
- Memory usage increased 12%

🔧 **Recommendations**:
- Consider database optimization
- Monitor memory usage trends
- Review API rate limiting strategy
```

## 快速开始

### **安装**

```

git clone https://github.com/oneuptime/oneuptime
cd oneuptime/MCP


npm install


cp .env.example .env



npm run build
npm start
```

### **配置**

```

ONEUPTIME_API_KEY=your_api_key_here
ONEUPTIME_URL=https://oneuptime.com  
```

### **与 AI 助手集成**

MCP 服务器与任何 MCP 兼容的 AI 助手一起使用：

```

{
  "mcpServers": {
    "oneuptime": {
        "command": "oneuptime-mcp",
        "env": {
          "ONEUPTIME_API_KEY": "oneuptime-api-key",
          "ONEUPTIME_URL": "https://oneuptime.com"  
        }
    }
  }
}
```

## AI 驱动的运维的未来

OneUptime MCP 服务器不仅仅代表集成，它还是 **AI 原生运维的愿景**，其中：

### **🗣️ 自然语言是界面**

不再需要记住 CLI 命令或浏览复杂的仪表板。描述你想要什么，AI 会处理实现。

### **🤝 AI 成为你的运维伙伴**

AI 助手成为知识渊博的团队成员，他们可以调查问题、采取行动并从你的运维模式中学习。

### **⚡ 运维变得会话化**

复杂的操作工作流程变得像与知识渊博的同事进行对话一样简单。

### **🔄 持续学习**

AI 助手可以从运维模式中学习，建议优化，并主动识别潜在问题。

## 开源创新

与 OneUptime 构建的所有产品一样，MCP 服务器是**完全开源的**：

* **完整源代码**可在我们的 GitHub 存储库中找到
* **Apache 2.0 许可证**，具有最大的灵活性
* **欢迎并鼓励社区贡献**
* **透明开发**，带有公共路线图

这种开放的方法能够实现：

* **社区扩展**，用于专门的用例
* **自定义实现**，用于特定环境
* **集成示例**，用于其他可观测性工具
* **来自社区的协作改进**

## 接下来是什么？

OneUptime MCP 服务器仅仅是个开始。我们正在积极努力：

### **增强的 AI 功能**

* **跨多个数据源的智能事件关联**
* **基于模式识别的预测性告警**
* **常见问题的自动化修复**
* **基于上下文和紧急程度的智能升级**

### **扩展的集成**

* **对各种 AI 助手的多平台支持**
* **用于实时更新的 Webhook 集成**
* **自定义工具开发框架**
* **用于社区扩展的插件生态系统**

### **高级工作流程**

* **具有审批工作流程的多步骤操作**
* **用于复杂自动化的条件逻辑**
* **与其他工具的跨平台协调**
* **所有 AI 驱动操作的审计跟踪**

## 加入 AI 原生运维革命

OneUptime MCP 服务器现已上市，可供生产使用。无论你是管理少量服务还是复杂的微服务架构，AI 驱动的运维都可以改变你的团队的工作方式。

**立即开始：**

1. 从我们的 GitHub 存储库**[下载 MCP 服务器](https://github.com/oneuptime/oneuptime/tree/master/MCP)**
2. 使用你的 OneUptime API 密钥**配置你的环境**
3. 使用 MCP 协议**连接你的 AI 助手**
4. **开始与你的可观测性基础设施对话**

运维的未来是会话式的、智能的且开源的。借助 OneUptime 的 MCP 服务器，这个未来现在触手可及。

---

*准备好使用 AI 改造你的运维了吗？[查看我们的 MCP 服务器文档](https://github.com/oneuptime/oneuptime/tree/master/MCP) 并[加入我们的社区](https://oneuptime.com/support) 分享你的经验。*