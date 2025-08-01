
<!--
title: MCP网关：赋能安全与可扩展的企业AI集成
cover: https://www.infracloud.io/assets/img/Blog/mcp-gateway/mcp-gateway-1200x628.png
summary: 本文介绍了如何使用 MCP 网关集中管理和保护多个 MCP 服务器，解决安全碎片化、运营开销和开发者体验问题。通过 Lasso 网关的实践案例，展示了其在事件响应等场景中的应用，并展望了 MCP 网关集成的未来发展趋势。
-->

本文介绍了如何使用 MCP 网关集中管理和保护多个 MCP 服务器，解决安全碎片化、运营开销和开发者体验问题。通过 Lasso 网关的实践案例，展示了其在事件响应等场景中的应用，并展望了 MCP 网关集成的未来发展趋势。

> 译自：[The MCP Gateway: Enabling Secure and Scalable Enterprise AI Integration](https://www.infracloud.io/blogs/mcp-gateway/)
> 
> 作者：Himanshu Sharma

模型上下文协议（MCP）生态系统已经蓬勃发展，社区构建的服务器被开发者们描述为他们“ [离不开的](https://www.reddit.com/r/mcp/comments/1lc85c4/what_are_the_mcp_servers_you_already_cant_live/) ”工具。从Web自动化到文档管理，这些专门的服务器解决了特定的生产力挑战，并已成为AI驱动工作流程不可或缺的一部分。然而，随着团队从一两个MCP服务器扩展到几十个，他们面临着一个关键的挑战，这个挑战可能会破坏这些工具所提供的生产力提升。

单独保护每个MCP服务器会导致重复性的工作和分散的控制。随着服务器数量的增长，团队面临着越来越多的挑战：复制OAuth和RBAC设置、管理跨工具的不一致访问，以及处理不可避免的配置偏差。最初的生产力提升很快变成了运营负担。

在这篇博文中，我们将介绍如何使用MCP网关作为一个中心化的集成枢纽来解决这些扩展挑战。我们将逐步介绍将多个社区MCP服务器整合到一个安全的网关后面的技术实现，探索真实的生产力工作流程，并研究企业部署的高级安全功能。最后，您将拥有一个可用于生产的网关，将孤立的工具转变为一个有凝聚力的AI生产力平台。

## 扩展问题：当成功变成复杂性

当您精心选择的MCP服务器从可控的少数几个增加到几十个关键工具时，会发生什么？答案不仅仅是“更多的工作”，而是指数级增长的复杂性，这会削弱您试图实现的生产力。

### 安全碎片化

每个服务器单独的OAuth设置会产生多个故障点和不一致的安全态势。每个服务器都维护着自己的身份验证状态和会话管理，以及独特的授权策略和角色定义。令牌验证和刷新逻辑在不同的实现中有所不同，而安全事件日志记录和监控则分散在各个系统中。这种碎片化使得几乎不可能实施组织范围内的安全策略，并在安全监控中造成危险的盲点。

### 运营开销

运营负担随着每个额外的MCP服务器而增加。配置管理成为一项持续的挑战，因为团队努力保持服务器配置在不同部署环境中的同步和更新。监控从一个单一的仪表板转变为具有单独警报配置的多个监控端点。故障排除需要深入了解每个MCP服务器的实现细节，而性能优化则需要为堆栈中的每个服务器制定单独的调整策略。

### 开发者体验问题

从开发者的角度来看，这些挑战每天都在加剧。如果没有可用工具和功能的中心注册表，工具发现变得越来越困难。随着每个MCP服务器实现不同的连接模式和身份验证要求，集成复杂性成倍增加。多系统调试变成了一场噩梦，需要在具有不同日志格式和调试接口的多个服务器上跟踪请求。文档分散在各个存储库中，使得理解工具如何协同工作变得更加困难。

## 解决方案：MCP网关作为生产力控制中心

与其接受复杂性是不可避免的，不如采用一种更好的架构方法，即MCP网关。

### 什么是MCP网关？

MCP网关充当位于LLM客户端和MCP服务器之间的反向代理和协调器。您可以将其视为一个智能的流量控制器，它可以路由请求并增强它们。网关抽象了后端工具执行的复杂性，同时为客户端提供了一个统一的接口。它处理：

* 将请求路由到适当的后端服务器
* 强制执行一致的身份验证和授权
* 聚合和格式化响应
* 实施安全策略
* 通过缓存和负载均衡优化性能

![MCP网关周期](https://www.infracloud.io/assets/img/Blog/mcp-gateway/mcp-gateway-cycle.webp)

### 架构原则

网关基于三个核心原则运行，这些原则解决了我们已经确定的扩展问题。

1. **关注点分离**：这意味着网关将安全、身份验证和路由职责从各个工具服务器上卸载，使它们能够专注于其核心功能。
2. **统一端点原则**：它确保客户端连接到单个网关端点，而不是管理到多个服务器的连接，从而大大简化了客户端实现和配置。
3. **策略执行原则**：它集中了安全策略、速率限制和访问控制，以便通过网关层在所有后端服务器上一致地应用它们。

这种架构简化了MCP集成和管理，而不会降低灵活性。

### MCP网关对开发团队的好处

网关实现了统一的工具发现，因此客户端可以列出和使用来自许多MCP服务器的工具，而无需知道它们托管在哪里。它消除了对硬编码路由逻辑的需求，因为它确定了每个请求的最佳服务器。集中式身份验证和策略控制减少了重复，并确保了跨工具的一致性。通过共享缓存、速率限制和自动负载分配来提高性能，所有这些都在网关层处理。

简而言之，网关模型用一个可管理、可扩展的AI驱动生产力工作流程入口点取代了碎片化的基础设施。

## 动手实践：构建以生产力为中心的MCP网关

现在有几种MCP网关实现可用，所有实现都具有**开源项目或组件**。选择正确的实现取决于您的技术需求、安全要求和部署环境。以下是一些值得注意的选择：

* **[Lasso MCP网关](https://github.com/lasso-security/mcp-gateway)**：一个以安全为中心的网关，支持令牌屏蔽、PII检测和提示注入过滤器。它使用一个插件系统来应用不同的保护。
* **[WunderGraph MCP网关](https://cosmo-docs.wundergraph.com/router/mcp)**：专为基于GraphQL的系统设计。它包括基于模式的发现和基于角色的访问控制。
* **[Zuplo远程MCP服务器](https://zuplo.com/blog/2025/06/10/introducing-remote-mcp-servers)**：将任何API转换为MCP服务器。提供日志记录、威胁过滤器和生产部署选项。
* **[kgateway](https://kgateway.dev/docs/mcp/)**：一个简单的网关，支持基本授权并且易于设置。
* **[IBM MCP网关](https://github.com/IBM/mcp-context-forge)**：构建在FastAPI上，适用于大规模企业使用。
* **[AmoyLab的Unla](https://github.com/amoylab/unla)**：一个由社区维护的基本协调器，适用于测试和开发。

在本指南中，我们将使用[Lasso的开源网关](https://github.com/lasso-security/mcp-gateway)。它提供了我们所需的功能，并且易于扩展。它可以卸载身份验证和授权，应用安全过滤器，如[令牌屏蔽](https://arxiv.org/abs/2505.11746#:~:text=While%20transformer-based%20models%20achieve,smoothing%20acts%20as%20implicit%20ensembling.)和[个人身份信息（PII）](https://en.wikipedia.org/wiki/Personal_data)检测，并将请求路由到适当的后端MCP服务器。

除了这些控制之外，Lasso网关还提供集中式监控和可观测性。借助[Xetrack](https://github.com/lasso-security/mcp-gateway?tab=readme-ov-file#xetrack)等插件，团队可以跟踪哪些工具被使用、检测安全事件以及监控系统性能，所有这些都来自一个单一的日志流。内置的可观测性使得调试工作流程、审计活动以及了解工具在实践中如何被使用变得更加容易。

![MCP流程](https://www.infracloud.io/assets/img/Blog/mcp-gateway/mcp-flow.webp)

*[(图片来源)](https://github.com/lasso-security/mcp-gateway/blob/main/docs/MCP_Flow.png)*

我们将构建一个MCP网关，该网关连接四个工具：

* Kubernetes诊断服务器
* 用于代码和问题跟踪的GitHub服务器
* 用于文档查找的Context7服务器
* 用于结构化规划的推理服务器

所有请求都将通过一个网关。您将使用阻止密钥、检测敏感数据和阻止风险行为的插件来保护它。

### 前提条件

在实现任何MCP网关之前，您需要一个工作MCP服务器和一个兼容的客户端环境的基础。因此，请确保以下设置已准备就绪：

* 多个MCP服务器
* [Claude Desktop](https://claude.ai/download)或兼容的MCP客户端，用于与网关交互
* Python 3.x：在本地运行Lasso MCP网关所需。
  （*我们建议使用[虚拟环境](https://docs.python.org/3/library/venv.html)以避免依赖冲突。）*
* API密钥：用于GitHub MCP服务器的[GitHub令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)。
* Kubeconfig：Kubernetes诊断服务器需要它来检查您的本地或远程集群。

### 设置说明

1. **安装网关：** 安装过程非常简单，但我们还将设置可选依赖项，以启用高级功能：

   ```
   pip install mcp-gateway
   ```

   这将安装具有基本功能的网关。对于生产部署，您可能需要[其他安全插件](https://github.com/lasso-security/mcp-gateway?tab=readme-ov-file#plugins)。

2. **配置后端服务器：** 配置确定您的网关将协调哪些MCP服务器以及应用哪些安全策略。此步骤至关重要，因为它定义了您的整个MCP生态系统：

   创建一个文件，其中列出您要使用的所有MCP服务器（mcp.json）。在本例中，我们将包括GitHub、Kubernetes诊断、Context7和顺序思维服务器。

   ```json
    {
      "mcpServers": {
        "mcp-gateway": {
          "command": "/Users/<your_path_to_python>/venv/bin/python",
          "args": [
            "-m",
            "mcp_gateway.server",
            "--mcp-json-path",
            "/Users/<your_path_to_mpc.json>/mcp.json",
            "--plugin",
            "basic"
          ],
          "servers": {
            "k8s-diagnostics": {
              "command": "/Users/<your_path_to_k8s-diagnostics-mcp-server>k8s-diagnostics-mcp-server/bin/k8s-diagnostics-mcp-server",
              "args": [],
              "env": {
                "KUBECONFIG": "/Users/<your_path_to_kubeconfig>/.kube/config"
              }
            },
            "github": {
              "command": "/Users/<your_path_to_github-mcp-server>/github-mcp-server/bin/github-mcp-server",
              "args": [],
              "env": {
                "GITHUB_TOKEN": "<your_github_token>"
              }
            },
            "context7": {
              "command": "npx",
              "args": ["-y", "@upstash/context7-mcp"]
            },
            "sequential-thinking": {
              "command": "npx",
              "args": [
                "-y",
                "@modelcontextprotocol/server-sequential-thinking"
              ]
            }
          }
        }
      }
    }
   ```
3. **启用安全插件：** MCP网关通过集中控制并支持各种安全插件来显著增强安全性。这些插件提供诸如令牌和密钥屏蔽、PII检测以及高级威胁分析（如提示注入保护）等功能。这些功能可以防止敏感数据泄露并缓解常见的AI特定威胁。

   **基本安全插件** - 使用12个内置模式的基本令牌保护：

   ```
    mcp-gateway --mcp-json-path ~/mcp.json -p basic
   ```

输出：“BasicGuardrailPlugin loaded. Secret patterns enabled: 12”

验证*：*检查日志是否成功加载模式

**高级PII检测** - 使用[Microsoft Presidio](https://microsoft.github.io/presidio/)的全面数据保护：

```
 # 首先安装依赖项
 pip install mcp-gateway[presidio]

 # 然后使用两个插件运行
 mcp-gateway --mcp-json-path ~/mcp.json -p basic -p presidio
```

目的：检测姓名、电子邮件、电话号码、SSN和其他PII

验证：不应显示“Presidio libraries not found”警告

**企业安全** - 使用提示注入检测的完整威胁防护：

```
 # 首先设置API密钥
 export LASSO_API_KEY="your-api-key"

 # 使用企业保护运行
 mcp-gateway --mcp-json-path ~/mcp.json -p basic -p lasso
```

目的：高级AI威胁分析和提示注入保护 验证：不应显示“Lasso API key not provided”警告

4. **启动网关：** 配置完成后，网关将激活您的安全策略并开始代理MCP请求。启动过程会验证所有配置并建立与后端服务器的连接：

```
 mcp-gateway --mcp-json-path ~/mcp.json -p basic
```

输出：

```
 2025-06-25 20:49:11,384 - mcp_gateway.server - INFO - Starting MCP gateway server directly...
 2025-06-25 20:49:11,386 - mcp_gateway.server - INFO - MCP gateway lifespan starting...
 2025-06-25 20:49:11,386 - mcp_gateway.plugins.manager - INFO - Registered plugin: BasicGuardrailPlugin (type: guardrail)
 2025-06-25 20:49:11,386 - mcp_gateway.plugins.manager - INFO - Registered plugin: LassoGuardrailPlugin (type: guardrail)
 . . .
 2025-06-25 20:49:12,323 - mcp_gateway.server - INFO - Dynamic registration process complete. Attempted to register 18 tools and 0 prompts with FastMCP.
```

为了在初始设置期间进行故障排除，调试日志会揭示配置问题和连接问题：

```
 LOGLEVEL=DEBUG mcp-gateway --mcp-json-path ~/mcp.json -p basic -p presidio
```

### 与Claude Desktop集成

Claude Desktop集成需要更新您的Claude配置以使用网关而不是直接MCP服务器连接。这会将所有MCP流量集中到您的安全策略中：

通过编辑配置文件（例如，macOS上的〜/Library/Application Support/Claude/claude\_desktop\_config.json），使用与最近为mcp.json所做的相同的配置来更新您的Claude Desktop：

```json
{
  "mcpServers": {
    "mcp-gateway": {
      "command": "/Users/<your_path_to_python>/bin/python",
      "args": [
        "-m",
        "mcp_gateway.server",
        "--mcp-json-path",
        "/Users/<your_path_to_mpc.json>/mcp.json",
        "--plugin",
        "basic",
        "--plugin",
        "xetrack"
      ],
      "servers": {
        "k8s-diagnostics": {
          "command": "/Users/<your_path_to_k8s-diagnostics-mcp-server>k8s-diagnostics-mcp-server/bin/k8s-diagnostics-mcp-server",
          "args": [],
          "env": {
            "KUBECONFIG": "/Users/<your_path_to_kubeconfig>/.kube/config"
          }
        },
        "github": {
          "command": "/Users/<your_path_to_github-mcp-server>/github-mcp-server/bin/github-mcp-server",
          "args": [],
          "env": {
            "GITHUB_TOKEN": "<your_github_token>"
          }
        },
        "context7": {
          "command": "npx",
          "args": ["-y", "@upstash/context7-mcp"]
        },
        "sequential-thinking": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-sequential-thinking"
          ]
        }
      }
    }
  }
}
```

此配置将单个MCP服务器条目替换为管理所有后端服务器的单个网关条目。

**重新启动Claude Desktop：** 为了使更改生效。您还可以返回到Claude Desktop的Developer Settings以检查配置：

![重新启动Claude Desktop](https://www.infracloud.io/assets/img/Blog/mcp-gateway/restart-claude-desktop.webp)

![MCP网关](https://www.infracloud.io/assets/img/Blog/mcp-gateway/search-mcp-gateway.webp)

现在让我们继续并在实际场景中对其进行测试。

## 真实的生产力场景

我们的MCP网关设置已完成，四个集成服务器（Kubernetes诊断、GitHub、Context7和顺序思维）都通过单个网关进行保护。让我们看看这种统一的架构如何在真实的事件响应场景中提供切实的收益。

我们的网关设置没有采用传统的碎片化工作流程，团队在kubectl命令、GitHub存储库、文档系统和监控仪表板之间跳转，而是启用了一个简化的对话界面，该界面可以安全地连接到所有运营系统并指导结构化的解决方案。

### 问题：传统的事件响应复杂性

在任何不断发展的工程组织中，事件都不可避免，服务宕机，容器无法启动，根本原因并不总是显而易见。团队经常争先恐后地对问题进行分类，在多个工具和界面之间切换，以拼凑出发生了什么。

这种碎片化的工作流程不仅会减慢响应时间，还会带来关键风险：

* 基础设施、代码和文档的部分可见性
* 压力下决策不一致
* 恢复过程中遗漏步骤
* 用于合规性和学习的弱审计跟踪

### 解决方案：我们正在运行的集成网关

使用我们之前配置的精确设置，即具有K8s诊断、GitHub、Context7和顺序思维服务器的MCP网关，让我们逐步了解如何将完整的事件响应工作流程简化为一个单一的对话界面。

### 场景设置：故障链

让我们通过一个使用通过单个安全MCP网关路由的四个MCP服务器的事件场景：

1. 集群触发警报，demo-app命名空间中的某些内容发生故障
2. 我们通过网关使用Kubernetes诊断服务器诊断问题
3. 我们通过GitHub服务器检查最近的GitHub活动以与部署相关联
4. 我们查阅存储在Context7中的事件响应手册
5. 我们使用顺序思维生成结构化的行动计划
6. 我们通过同一安全网关将整个事件记录回GitHub

让我创建一个具有问题的pod的演示场景：

```
➜  ~ kubectl get pods -A
NAMESPACE       NAME                               READY   STATUS             RESTARTS          AGE
default         test-container                     0/1     CrashLoopBackOff   736 (3m18s ago)   105d
demo-app        broken-pod                         0/1     Completed          0                 112m
```

### 实践中的工作流程

以下是所有集成工具的流程：

1. **发现**：k8s-diagnostics识别具有错误的损坏的pod。

**提示**：*“检查<YOUR\_NAMESPACE>命名空间中是否有任何有问题的pod。你看到了什么问题？”*

![发现](https://www.infracloud.io/assets/img/Blog/mcp-gateway/discovery.webp)

**注意：** *Claude的桌面将要求访问以执行所有这些任务。*

![访问](https://www.infracloud.io/assets/img/Blog/mcp-gateway/access-pods.webp) ![访问](https://www.infracloud.io/assets/img/Blog/mcp-gateway/access-issues.webp)

2. **上下文收集：** GitHub MCP显示最近的提交和未解决的问题 **提示**：*“检查<YOUR\_REPO>存储库中是否有任何可能与此故障相关的最近提交或未解决的问题。”*

![上下文收集](https://www.infracloud.io/assets/img/Blog/mcp-gateway/context-gathering.webp)

3. **文档查找：** Context7检索上传的手册 **提示**：*“查找我们用于处理服务故障和pod问题的事件响应手册。使用context7”*

![文档查找](https://www.infracloud.io/assets/img/Blog/mcp-gateway/documentation-lookup.webp)

4. **结构化问题解决：** 使用k8s-diagnostics构建结构化计划行动计划 **提示**：*“根据pod故障、最近提交和我们的手册，创建一个逐步行动计划以解决此问题。”*

![结构化问题解决](https://www.infracloud.io/assets/img/Blog/mcp-gateway/structured-problem-solving.webp)

5. **采取行动：** 顺序思维和GitHub CP创建一个全面的事件问题 **提示：** *“在<YOUR\_REPO>存储库中创建一个GitHub问题，记录此事件，包括pod错误、调查步骤和我们创建的行动计划。”*

![采取行动](https://www.infracloud.io/assets/img/Blog/mcp-gateway/action-taking.webp)

此事件响应工作流程展示了MCP网关如何充当实际调试的统一控制平面，将诊断、文档、代码活动和结构化推理无缝集成到一个单一的对话界面中。

## MCP网关集成的未来

在技术进步和不断增长的企业采用需求的推动下，MCP网关生态系统持续快速发展。

### 新兴模式

一些重要的趋势正在塑造下一代网关功能。

* 专门的网关插件正在为医疗保健、金融和法律等行业的特定领域需求而出现，在这些行业中，合规性和安全要求需要量身定制的解决方案。
* AI驱动的路由决策代表了一种引人入胜的发展，其中机器学习算法根据历史性能和当前上下文优化工具选择和路由。
* 联邦网关架构使多个网关能够在组织边界之间协同工作，从而支持复杂的企业场景。
* 复杂的工具编排功能正在不断发展，以支持跨多个工具和决策点的自动化工作流程，而无需人工干预。

围绕MCP网关构建的社区反映了该技术的成熟和广泛采用。

* 插件市场正在发展成为网关插件和扩展的集中式存储库，从而使团队可以更轻松地查找和共享解决方案。
* 配置模板共享为常见用例提供预构建的配置，从而加快了实施时间。
* 最佳实践文档通过社区驱动的努力而不断增长，从而捕获了从实际部署中获得的经验教训。
* 监控仪表板模板提供了可重用的监控和警报配置，团队可以根据自己的特定需求进行调整。

## 结语：您的集中式AI生产力中心

从管理独立的MCP服务器到通过集中式网关进行运营的转变，标志着团队如何实现AI驱动的生产力的更深层次的转变。MCP网关将集成、安全性和可观测性统一到一个单一、可管理的界面中，从而降低了运营复杂性并简化了开发工作流程。团队无需处理特定于工具的配置，而是可以专注于构建更智能的自动化和可扩展系统，并具有一致的策略和集中的监督。

从小处着手，连接您最常用的工具，观察它们的使用情况，并根据实际需求进行扩展。开源实现为您提供了开始所需的一切，并且有一个不断壮大的社区可以从中学习和贡献。

MCP网关不仅仅是一项技术改进；它还是大规模构建弹性、安全和智能AI基础设施的途径。要了解有关AI的最新信息，请观看我们的[AI-Xplore网络研讨会](https://www.infracloud.io/webinars/ai-xplore/)。如果您需要[构建AI云](https://www.infracloud.io/build-ai-cloud/)方面的帮助，我们的AI专家可以为您提供帮助。

如果您发现本指南有用并且想讨论更多关于MCP和AI代理的信息，请随时在[LinkedIn](https://www.linkedin.com/in/himanshusharma89/)上与我联系。
