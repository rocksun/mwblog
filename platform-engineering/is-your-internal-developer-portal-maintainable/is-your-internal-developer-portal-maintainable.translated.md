# 您的内部开发者门户可维护吗？

![用于：您的内部开发者门户可维护吗？的特色图片](https://cdn.thenewstack.io/media/2024/05/c7750283-maintenance2-1024x576.jpg)

[内部开发者门户](https://thenewstack.io/how-do-the-internal-developer-platform-and-portal-connect/) 相当新。与所有新事物一样，关于如何使用它们来完成确切任务有多种理论。有一件事每个人都同意：内部开发者门户和平台是开发者[核心界面](https://thenewstack.io/internal-developer-portals-can-do-more-than-you-think/)，它们需要易于维护和易于演进。毕竟，如果人员、流程和技术演进，那么为开发者服务的界面也会演进。

您如何判断您选择的门户是否可以演进并可维护？让我们对此进行全面探讨。

一个有效的内部开发者门户由以下几个元素组成：

- [软件目录](https://www.getport.io/product/software-catalog)
- [开发者自助服务](https://www.getport.io/product/self-service)
- [记分卡](https://www.getport.io/product/scorecards-and-initiatives)
- [自动化](https://www.getport.io/product/workflow-automation)
- [可视化](https://www.getport.io/product/dashboards-and-visualizations)

虽然所有这些都是提供开发者体验的一部分，但我们将检查两个：

- 软件目录（服务目录）
- 自助服务操作

## 软件目录需要一个灵活的数据模型

灵活的数据模型意味着能够在门户中建模您的工程 DNA 和用例，以：

- 反映门户中的实际软件交付生命周期 (SDLC) 和技术栈，这将使门户受到开发者和管理者的信任。
- 向门户添加用例，例如添加 AppSec 数据以支持门户中的 AppSec 标准合规性。

一个好的门户允许您在软件目录中定义、更改或添加实体类型以及这些实体类型之间的不同关系。

让我们更详细地了解这两个方面。

### 自定义实体类型

实体类型是资源、组件和 API 等内容。实体类型形成我们所说的软件目录的数据模型。这是软件目录用来向其用户解释 SDLC 世界的地图。地图中遗漏的内容在门户中不存在。

以下是一些您可能希望包含在门户中的实体示例：

- 云权限，以便您可以提供[即时访问](https://www.getport.io/blog/managing-just-in-time-permissions-in-a-developer-portal)并更安全地工作。
- 警报，以便您可以[在开发者门户中统一警报](https://thenewstack.io/can-the-internal-developer-portal-solve-alert-chaos/)并使开发者更容易理解和解决问题。
- 事件，以便您可以[支持随叫随到](https://www.getport.io/blog/how-internal-developer-portals-improve-incident-management)并为开发者提供更好的体验，并减少平均修复时间 (MTTR)。
- 漏洞，以便您可以[将安全性融入每个开发人员例程](https://www.getport.io/usecase/appsec)。
- CI/CD，以便您可以将门户用作[CI/CD 目录](https://thenewstack.io/simplify-ci-cd-with-a-general-purpose-software-catalog/)。
- API 数据，以便您可以将门户用于[API 治理](https://www.getport.io/blog/manage-your-apis-using-an-internal-developer-portal)等。

能够在没有大量编码的情况下包含这些实体至关重要。

**需要注意的是：**具有固定数量实体类型（例如，仅 C4 模型）或需要编码才能更改它们的 portal。

### 理解依赖关系

与其假设实体之间存在固定的关系，您需要能够区分不同类型的依赖关系，例如将运行时云资源（计算实例）与存储资源（数据库和[AWS](https://aws.amazon.com/?utm_content=inline+mention) S3 存储桶）分开。

您还希望您的门户能够指定实体之间多个不同的关系，从而在理解资源依赖关系时提供粒度和清晰度。

**需要注意的是：**您无法控制实体类型之间关系的门户

### 缺乏上下文和信任 = 缺乏采用

如果没有使用自定义实体类型或区分依赖关系的能力，您的软件目录在表示 SDLC 的关键方面时就会不足。因此，它为您的利益相关者提供的上下文和实用性较少。这一点至关重要，因为开发者不太愿意完全采用无法满足其许多需求的门户。

## 自动化、实时数据摄取
### 内部开发者门户的软件目录自动化

**基本要求：**

**自动发现：**
- 目录应自动查找整个组织中的相关软件实体。
- 扫描各种系统和平台，识别和编目新的或更新的实体，无需手动输入。

**对账和实时更新：**
- 目录应定期更新其数据以匹配“真实来源”（如第三方系统），确保准确性。
- 更正编目信息与资源实际状态之间的差异。
- 例如，目录中的 AppSec 漏洞数据必须保持最新。

**多个摄取途径：**
- 自动化数据输入，尽可能避免手动输入。
- 自动化选项包括：
    - REST API：允许自动化系统和脚本直接更新目录。
    - IaC（基础设施即代码）：与 IaC 工具集成，在部署过程中自动更新目录。
    - Webhook：接收来自各种平台的 Webhook，获取有关资源或配置更改的更新。

**插件的局限性：**

- 插件无法解决不灵活的数据模型。
- 插件可能缺乏功能和灵活性，阻碍内部开发者门户的有效性。

**开发者门户的有效性：**

- 开发者门户应提供针对开发者特定需求定制的相关抽象信息。
- 关键要素：
    - **中心元数据存储：**所有数据（来自核心模型或第三方工具）按上下文进行搜索，创建全面的信息视图。
    - **抽象数据：**从第三方系统获取的数据与用户界面之间的链接受到限制，难以显示更多或更少的详细信息或以不同的方式显示数据。

**自助服务操作：**

- 大量自助服务操作，包括第 2 天运营。
### 更正后的 Markdown 文本

您希望您的门户能够直接为各种操作提供自助服务，例如：

- 部署服务
- 回滚
- 触发事件
- 创建云资源
- 切换功能标志
- 添加机密
- 获取临时数据库权限
- 设置开发环境

这意味着开发人员不仅可以构建新服务，还可以对 [第 2 天运营](https://www.getport.io/blog/give-day-2-operations-autonomy-to-your-developers) 使用自助服务操作。

GitHub Workflows、GitLab CI、Argo Workflows、AWS Lambda 和 Kubernetes 运营商等现有的 CI/CD 管道附带功能强大、可立即使用的操作，可快速可靠地执行各种任务。

例如，GitHub Workflows 在其市场中提供了数百个内置操作，可用于高效管理各种操作。即使对于脚手架，Cookiecutter 库也可以合并到 CI/CD 管道中，以便更轻松、更灵活地根据指定标准自定义和创建存储库。

鉴于这些功能，内部开发人员门户应专注于增强自助服务操作表单的 UI 层，并加强与这些现有 CI/CD 引擎的集成。这种方法确保了开发人员的无缝体验，利用了成熟工具的优势，同时提供了用户友好的界面。

**需要注意的是：**只有单一方式触发自助服务操作的门户，迫使您废弃并替换以前的工作，并且与您当前的 CI/CD 管道没有强有力的集成。

## 主要要点

一个有效的内部开发人员门户取决于集成一个强大的软件目录和全面的自助服务操作。支持自定义实体类型并准确表示依赖关系的灵活数据模型对于创建有用且动态的目录至关重要。

自动化的实时数据提取确保信息保持最新、可靠且没有手动维护的负担。这些功能共同使开发人员能够高效地查找和使用他们需要的资源，从而营造更具生产力和精简的开发环境。

此外，虽然插件可以提供快速修复，但它们在灵活性和功能方面往往不足，可能会阻碍门户的整体有效性。相反，专注于增强自助服务操作表单的 UI 层并加强与现有 CI/CD 管道的集成，可确保开发人员获得无缝且高效的体验。

通过利用成熟工具的优势并提供用户友好的界面，组织可以构建一个开发人员门户，不仅满足当前需求，而且随着这些需求的发展而进行调整和扩展，最终提高开发人员的采用率和满意度。

在 [Portal Talks](https://www.portaltalks.io/) 上了解有关内部开发人员门户的更多信息，6 月 26 日至 27 日，The New Stack 的 [Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/) 将主持。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。