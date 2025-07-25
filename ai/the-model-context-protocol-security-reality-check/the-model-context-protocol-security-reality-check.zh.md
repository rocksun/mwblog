[模型上下文协议](https://modelcontextprotocol.io/introduction) (MCP) 正在迅速成为 AI 代理和服务器的标准，它定义了代理如何发现远程工具和服务、如何进行身份验证以及如何调用它们。但是，保护基于 OAuth 的 MCP 服务器比看起来要棘手。

由安全专家（包括 [Den Delimarsky](https://github.com/dend) 和 [Paul Carleton](https://www.linkedin.com/in/paulcarletonjr/?originalSubdomain=uk)）领导的 MCP 安全最佳实践规范的最新更新，[强调了当前部署中的关键差距](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/)，特别是在混淆代理人攻击和令牌处理漏洞方面。在本文中，我将介绍如何弥补这些差距，以及为什么代理强制执行 OAuth 对于安全 MCP 架构至关重要。

## **MCP 规范的要求 —— 以及它遗漏的内容**

[MCP 安全最佳实践规范](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) 建立了明确的要求：

* **将 MCP 服务器置于代理之后** —— 生产部署的强制要求
* **强制执行身份验证并验证令牌受众和范围** —— 所有受保护资源的要求
* **防止令牌传递** —— 避免漏洞的关键
* **审计所有访问** —— 符合性和事件响应的关键

然而，检查当前的 MCP 部署模式会发现一个重要的实施差距。许多开发人员部署直接暴露给客户端的 MCP 服务器，在应用程序级别而不是通过专用代理基础设施实施 [OAuth](https://thenewstack.io/oauth-2-0-a-standard-in-name-only/)。这种方法虽然在功能上足以满足基本的身份验证，但未能满足安全规范预期的动态授权要求，包括每次请求的策略评估、防止令牌传递以及超越 [静态 OAuth 范围](https://auth0.com/docs/get-started/apis/scopes) 的上下文信任强制执行。

该规范明确警告了“混淆代理人”问题，即调用下游服务的 MCP 服务器可能会无意中代表攻击者执行特权操作。安全专家（包括 [Delimarsky](https://www.linkedin.com/posts/activity-7333383043421716480-kzjS)）贡献的安全指南的最新更新强调了三个关键要求：通过每次客户端用户同意验证来防止混淆代理人攻击，消除令牌传递以维持适当的信任边界，以及为每次令牌使用保留审计跟踪。MCP 安全最佳实践规范的这些更新强调了基本 OAuth 实施与生产就绪的 MCP 安全之间的差距。

## **为什么 VPN 会破坏现代代理架构**

传统的企业安全模型依赖于基于 VPN 的边界保护，但这种方法与现代代理访问模式存在根本的不兼容性。当组织尝试使用 VPN 要求保护 MCP 服务器时，它们会遇到一个关键限制：托管的 AI 服务（如 [Claude](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) 或 [ChatGPT](https://thenewstack.io/ai-agents-must-learn-from-chatgpts-data-wrongs/)）无法建立到专用网络的 VPN 连接。

这种限制迫使人们做出架构选择：要么将代理访问限制为完全内部的部署（消除托管 AI 服务和访问前沿模型的好处），要么将 MCP 服务器暴露给具有强大应用层安全性的公共网络。后一种方法直接符合零信任原则，即网络位置不提供固有的信任，并且所有授权决策都在应用层进行。

MCP 规范通过强制执行代理架构而不是网络级别控制来承认了这一现实。但是，该规范没有定义这些代理应如何实施 [代理访问场景所需的动态授权策略](https://thenewstack.io/agentic-access-is-here-your-authorization-model-is-probably-broken/)。

## **零信任：MCP 需要的强制执行层**

MCP 安全最佳实践承认了许多安全挑战，但未能强制执行全面的解决方案。虽然该规范要求代理架构和令牌验证，但它没有指定如何实施每次请求的上下文评估 —— 这是代理访问的一个关键差距。

这就是 [零信任安全](https://thenewstack.io/what-is-zero-trust-security/ "zero trust security") 原则变得至关重要的地方。零信任增加了 OAuth 甚至良好实施的 MCP 代理所缺乏的上下文层：

* **谁** 在发出请求（身份验证）
* 他们试图访问 **什么**（资源验证）
* 请求 **何时** 发生（基于时间的策略）
* 它从 **哪里** 发起（位置和设备上下文）
* 为什么需要该 **操作**（行为分析）

**应用于 MCP 的零信任核心原则：**

* **永不信任，始终验证**：独立评估每个 MCP 方法调用，即使对于具有有效凭据的代理也是如此。
* **最小权限访问**：使用细粒度的上下文限制超出 OAuth 范围的操作。
* **假设违规**：即使来自有效令牌，也要监控异常行为。
* **持续验证**：随着条件的变化重新评估每个请求。
* **上下文感知的授权**：根据实时条件（而不仅仅是静态范围）验证请求。

## **身份感知代理：在现实世界中强制执行 MCP 安全**

[MCP 规范](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) 强烈建议使用代理架构，但没有指定如何实施强制执行逻辑。身份感知代理 (IAP) 提供了缺失的强制执行层。

了解 MCP 协议的 IAP 可以：

1. **拦截和解码 MCP 请求** —— 包括 MCP 特定的操作，例如 `InvokeMethod`，从而能够强制执行提示注入保护和数据丢失防护 (DLP) 策略。
2. **提取上下文** —— 例如身份、设备状态、位置和请求细节。
3. **实时评估策略** —— 使用集中定义的规则。
4. **强制执行每次请求的决策** —— 而不仅仅是基于会话的检查。
5. **审计每个请求** —— 具有完整的上下文和决策依据。

### **MCP 身份验证的基本身份感知代理流程**

![MCP 身份验证的基本身份感知代理流程](https://cdn.thenewstack.io/media/2025/06/9b844950-ztna-mcp.png)

来源：Pomerium

这种架构模式转化为简单的代理配置：

|  |  |
| --- | --- |
|  | ```yaml
# MCP 的基本 IAP 配置
routes:
  - from: https://mcp-server.company.com
    to: http://internal-mcp-server:8080/mcp
    name: 内部 MCP 服务器
    mcp: {}
``` |

这使得：

* **精细的操作控制**：评估方法调用，而不仅仅是范围
* **集中式强制执行**：在服务之间保持一致的策略
* **动态委派**：根据上下文调整权限

## **参考实现：身份感知代理模式**

身份感知代理可以弥合 MCP 安全规范和零信任强制执行之间的差距。Pomerium 等开源实现展示了这种方法，具有 MCP 支持，可供寻求参考架构的组织使用。一些供应商提供适用于 MCP 部署的 IAP 功能，每种功能都有不同的优势：开源解决方案提供透明性和自定义，而商业平台提供企业支持和集成。

### **MCP 规范合规模式**

* **代理架构**：拦截 MCP 流量并强制执行方法级别的访问控制
* **OAuth 2.1 集成**：支持代码交换的密钥证明 (PKCE)、动态客户端注册并防止令牌传递
* **令牌验证**：确保特定于受众、范围适当的访问
* **审计**：包括每个日志中的方法调用、工具参数和授权决策

### **防止传递漏洞的令牌分离模式**

![防止传递漏洞的令牌分离模式](https://cdn.thenewstack.io/media/2025/06/0e606bc1-ztna-oauth-mcp.png)

来源：Pomerium

此模式通过配置实现适当的令牌分离。以下示例显示了用于令牌分离的特定于 Pomerium 的配置模式：

|  |  |
| --- | --- |
|  | ```yaml
# 用于上游 OAuth 的令牌分离模式
routes:
  - from: https://github-mcp.company.com
    to: http://github-mcp:8080/mcp
    name: GitHub MCP
    mcp:
      upstream_oauth2:
        client_id: ${GITHUB_CLIENT_ID}
        client_secret: ${GITHUB_CLIENT_SECRET}
        scopes: ['read:user', 'user:email']
        # ... 端点配置
``` |

除了强制执行适当的信任边界之外，使用身份感知代理保护 MCP 服务器还可以保护敏感的第三方 OAuth 令牌，例如 GitHub、Salesforce 等，使其免受 AI 代理或大型语言模型 (LLM) 的攻击。如果没有代理，这些上游令牌可能会传递给代理，在那里它们可能会被存储、记录甚至在发生违规时暴露。这种风险并非理论上的：最近的法律案件（例如 OpenAI 法院命令）强调，LLM 提供商可能会保留所有用户数据，包括令牌。

正确配置的代理将颁发仅在当前用户会话的上下文中以及用于特定下游调用中有效的短期内部令牌，从而大大减少了敏感凭据的暴露面。

### **零信任增强模式**

* **每次请求的上下文评估**：根据时间、位置、用户状态等评估请求
* **动态策略引擎**：使用策略语言进行实时、数据驱动的决策
* **与会话无关的授权**：单独授权每个调用
* **行为监控**：检测并限制异常代理行为

如果您想查看一个可用的示例，[Pomerium MCP 演示](https://github.com/pomerium/mcp-app-demo) 提供了这些模式的参考实现，包括安全的 OAuth 2.1 流程、令牌分离和用于 MCP 服务器的零信任策略强制执行。

### **实施示例**

参考实现通常演示：

* 适用于代理的有效 OAuth 2.1 流程
* 安全 MCP 部署的配置模式
* 示例策略（基于时间、基于组、速率限制）
* 与代理行为相关的监控和警报

## **从合规到信心：安全的 MCP 路线图**

### **实施阶段**

**第 1 阶段：MCP 安全合规性**

* 部署代理架构
* 根据 OAuth 2.1 验证令牌和范围
* 记录所有具有完整上下文的访问
* 防止令牌传递

**第 2 阶段：增强的授权**

* 添加每次请求的策略评估
* 使用上下文感知的决策
* 集中管理策略
* 动态评估风险

**第 3 阶段：运营集成**

* 将 MCP 身份验证集成到现有的 IAM 系统中
* 持续监控代理行为
* 规划自主访问的事件响应
* 设置代理权限的治理

### **解决方案评估框架**

在评估 MCP 安全的 IAP 解决方案时，请考虑策略表达的灵活性、MCP 协议支持、与现有身份系统的集成、审计功能和运营开销。组织应根据其对策略复杂性、集成需求和运营模型的特定要求来评估选项。

### **运营影响**

安全现在需要：

* **基础设施** 变更以支持代理和 IAP 组件
* 动态的、基于行为的授权方面的 **安全专业知识**
* 针对机器驱动的代理行为（而不是人类工作流程）调整的 **监控和警报**
* 平台、应用程序和安全团队之间的 **跨职能对齐**

模型上下文协议标准化了代理与工具和数据交互的方式。实施决定了这些交互在生产中是否保持安全和可审计。

[MCP 中的 OAuth 2.1](https://modelcontextprotocol.io/specification/draft/basic/authorization) 提供了基础。零信任使其安全。