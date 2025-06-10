<!--
title: 你应该尝试的7个开源Diagram-as-Code工具
cover: https://miro.medium.com/v2/resize:fit:720/format:webp/1*PvLEcxhLPMCx6WGQdTWeEw.png
summary: 告别手动画图！7大开源“Diagram-as-Code”神器来袭，轻松搞定云原生架构图！支持AWS、Azure、GCP，集成K8s、Docker。Diagrams、PlantUML、Mermaid、Structurizr DSL、AWS Diagram-as-Code、D2、Kroki，总有一款适合你！YAML、DSL、Python多种姿势生成架构图，告别手动更新，拥抱IaC！
-->

告别手动画图！7大开源“Diagram-as-Code”神器来袭，轻松搞定云原生架构图！支持AWS、Azure、GCP，集成K8s、Docker。Diagrams、PlantUML、Mermaid、Structurizr DSL、AWS Diagram-as-Code、D2、Kroki，总有一款适合你！YAML、DSL、Python多种姿势生成架构图，告别手动更新，拥抱IaC！

> 译自：[7 Open Source Diagram-as-Code Tools You Should Try | by Prateek Jain](None)
> 
> 作者：Prateek Jain

无论您是在设计基础设施、解释应用程序流程还是记录云架构，图表都是技术交流的关键部分。但是，传统的图表工具可能会成为瓶颈，手动编辑、版本控制问题以及缺乏可重复性通常会减慢团队的速度。这就是**Diagram-as-Code**的用武之地。

Diagram-as-Code工具使您能够直接从代码生成架构图。它们受版本控制、可自动化并且在团队中保持一致。在本指南中，我们将探讨七个支持云和软件架构Diagram-as-Code的开源工具，特别关注基于 AWS 的基础设施。

让我们首先了解我们将在每个工具中尝试复制的图。

## 示例 AWS 架构

我们将使用一个示例架构，该架构反映了托管在 AWS 上的典型基于 Web 的应用程序。以下是组件：

- **Route53**：域的 DNS 路由。
- **Elastic Load Balancer (ELB)**：分配传入流量。
- **两个 EC2 实例**：托管应用程序后端。
- **Lambda 函数**：用于身份验证逻辑。
- **IAM 角色**：与 Lambda 关联以获得安全权限。
- **Primary RDS DB**：主应用程序数据库。
- **Replica RDS DB**：用于提高性能的只读副本。

每个工具都将生成相同的逻辑结构，以帮助您比较它们的性能。

## 1. Diagrams (by mingrammer)

[Diagrams](https://diagrams.mingrammer.com/) 是一个基于 Python 的开源库，可将简单的 Python 代码转换为美观的系统架构图。它支持主要的云提供商，如 AWS、Azure 和 GCP，以及 Kubernetes 和 Docker 等本地工具。这是直接从代码自动生成架构文档的最简单方法之一。

**主要优势**

- 开箱即用地支持大量的云和 DevOps 图标。
- 易于供熟悉 Python 的开发人员使用。
- 与 CI/CD 工具良好集成，可自动生成文档。

**缺点**

- 布局和样式方面的自定义有限。
- 不支持实时协作或 GUI。

**安装**

Diagrams 依赖 **Graphviz** 来渲染架构图。您需要先安装 Graphviz，然后才能使用 `diagrams` Python 包。

如果您使用的是 **macOS**，则可以使用 Homebrew。对于其他平台，请参阅官方 Graphviz 安装指南：[https://graphviz.org/download/](https://graphviz.org/download/)

```
# Install Graphviz first
brew install graphviz
# Then install Diagrams
pip install diagrams
```

**示例图代码**

将此代码段保存在文件 aws.py 中

```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.security import IAM
from diagrams.aws.compute import Lambda
with Diagram("AWS Architecture", show=False):
    dns = Route53("Route53")
    lb = ELB("Load Balancer")
    web1 = EC2("Web Server 1")
    web2 = EC2("Web Server 2")
    auth_lambda = Lambda("Auth")
    iam = IAM("IAM Role")
    db_primary = RDS("Primary DB")
    db_replica = RDS("Replica DB")
    dns >> lb >> [web1, web2]
    web1 >> auth_lambda >> iam
    [web1, web2] >> db_primary >> db_replica
```

现在，运行以下命令

`python3 aws.py`

**输出**

![Diagrams Output](https://miro.medium.com/v2/resize:fit:720/format:webp/1*GrCHCwPXPI8BV4ww2SgTFw.png)

## 2. PlantUML

[PlantUML](https://plantuml.com/) 是一个成熟而灵活的工具，允许您使用简单而强大的文本语言来定义图表。它支持序列图、用例图、类图、组件图等，使其适用于软件开发和基础设施建模。

**主要优势**

- 基于文本且易于版本控制。
- 适用于 Markdown、文档工具和 IDE。
- 灵活且支持多种图表类型。

**缺点**

- 需要学习其语法。
- 对于大型图表，可能会变得冗长。

**安装**

您可以使用 Docker 在本地运行 PlantUML，也可以直接在浏览器中使用官方的基于 Web 的编辑器：[https://editor.plantuml.com/](https://editor.plantuml.com/)

对于通过 Docker 进行本地设置：

`docker run -d -p 8080:8080 plantuml/plantuml-server:jetty`

**示例图代码**

```
@startuml
component "Route53" as DNS
component "ELB" as LB
component "EC2 Web 1" as WS1
component "EC2 Web 2" as WS2
component "Lambda Auth" as Lambda
component "IAM Role" as IAM
component "RDS Primary" as DB1
component "RDS Replica" as DB2

DNS --> LB
LB --> WS1
LB --> WS2
WS1 --> Lambda
Lambda --> IAM
WS1 --> DB1
WS2 --> DB1
DB1 --> DB2
@enduml
```

**输出**

![PlantUML Output](https://miro.medium.com/v2/resize:fit:720/format:webp/1*9uO_yvDgMf-P6uoEGdYMYQ.png)

## 3. Mermaid

[Mermaid](https://mermaid.js.org/) 是一个基于 JavaScript 的图表绘制工具，它使用 Markdown 风格的语法。它非常适合将简单、清晰的图表直接嵌入到 markdown 文档或像 Notion、GitHub 或 GitLab 这样的工具中。

**主要优点**

- 与 markdown 文件无缝协作。
- 简单易懂的语法，适合初学者。
- 许多平台原生支持。

**缺点**

- 不适合大型、复杂的图表。
- 视觉定制选项有限。

**用法（在 markdown 平台中无需安装）**

你可以在许多基于 markdown 的平台（如 GitHub、GitLab、Notion 和 Obsidian）中直接使用 Mermaid，而无需安装任何东西。

对于快速测试或在线分享图表，请使用其官方 playground：
[https://www.mermaidchart.com/play](https://www.mermaidchart.com/play)

**示例图表代码**

```
graph TD
DNS[Route53] --> LB[ELB]
LB --> WS1[Web Server 1]
LB --> WS2[Web Server 2]
WS1 --> Lambda[Lambda Function]
Lambda --> IAM[IAM Role]
WS1 --> DB1[Primary DB]
WS2 --> DB1
DB1 --> DB2[Replica DB]
```

输出

![Mermaid Example](https://miro.medium.com/v2/resize:fit:720/format:webp/1*J30bXQ-1cyPt0K2t142Ysg.png)

## 4. Structurizr DSL

[Structurizr](https://structurizr.com/) DSL 是一种强大的文本领域特定语言 (DSL)，可帮助你创建基于 C4 模型的软件架构图。它更侧重于概念清晰度而不是视觉完美，非常适合对企业级系统进行建模。

**主要优点**

- 完全支持 C4 建模标准。
- 模型和视图的清晰分离。
- 鼓励架构方面的最佳实践。

**缺点**

- 学习曲线较陡峭。
- 需要理解 C4 模型。

**安装**

你可以直接在浏览器中使用 Structurizr DSL，也可以在本地安装它。

- Web 编辑器：[https://structurizr.com/dsl](https://structurizr.com/dsl)
- 本地安装指南：[https://structurizr.com/help/dsl](https://structurizr.com/help/dsl)

**示例图表代码**

```
workspace {
    model {
        user = person "User"
        system = softwareSystem "Web Application" {
            lb = container "Load Balancer"
            web1 = container "Web Server 1"
            web2 = container "Web Server 2"
            auth = container "Auth Lambda"
            role = container "IAM Role"
            db1 = container "Primary DB"
            db2 = container "Replica DB"
            user -> lb
            lb -> web1
            lb -> web2
            web1 -> auth
            auth -> role
            web1 -> db1
            web2 -> db1
            db1 -> db2
        }
    }
    views {
        container system {
            include *
            autolayout lr
        }
    }
}
```

输出

![Structurizr Example](https://miro.medium.com/v2/resize:fit:720/format:webp/1*noUSCGjg8qKGvbZh9xgMMQ.png)

## 5. AWS Diagram-as-Code (by AWS Labs)

[AWS Diagram-as-Code](https://github.com/awslabs/diagram-as-code) 是一个由 AWS Labs 构建的基于 YAML 的开源工具。它专注于使用原生服务标识符和关系来表示 AWS 基础设施。对于 AWS 密集型环境来说，此工具非常理想，它可以从结构化的 YAML 格式输出静态架构图像。

**主要优点**

- 简单且声明式的 YAML 语法。
- 专为 AWS 服务量身定制。
- 轻量级且 CLI 驱动。

**缺点**

- 仅限于 AWS。
- 定制和布局控制非常有限。

**安装**

你可以使用 Homebrew 在 macOS 上轻松安装 AWS Diagram-as-Code：

```bash
$ brew install awsdac
```

对于其他系统或更高级的用法，请参阅官方文档：[https://github.com/awslabs/diagram-as-code](https://github.com/awslabs/aws-diagram-as-code)

**示例图表代码**

```yaml
Diagram:
  DefinitionFiles:
    - Type: URL
      Url: "https://raw.githubusercontent.com/awslabs/diagram-as-code/main/definitions/definition-for-aws-icons-light.yaml"
  Resources:
    Canvas:
      Type: AWS::Diagram::Canvas
      Direction: vertical
      Children:
        - AWSCloud
        - User
    AWSCloud:
      Type: AWS::Diagram::Cloud
      Direction: vertical
      Preset: AWSCloudNoLogo
      Align: center
      Children:
        - Route53
        - LoadBalancer
        - EC2Stack
        - Lambda
        - IAM
        - DBStack
    User:
      Type: AWS::Diagram::Resource
      Preset: User
      Label: User
    Route53:
      Type: AWS::Route53::HostedZone
      Label: Route 53
    LoadBalancer:
      Type: AWS::ElasticLoadBalancingV2::LoadBalancer
      Label: Load Balancer
    EC2Stack:
      Type: AWS::Diagram::HorizontalStack
      Children:
        - EC2_1
        - EC2_2
    EC2_1:
      Type: AWS::EC2::Instance
      Label: Web Server 1
    EC2_2:
      Type: AWS::EC2::Instance
      Label: Web Server 2
    Lambda:
      Type: AWS::Lambda::Function
      Label: Auth Lambda
    IAM:
      Type: AWS::IAM::Role
      Label: IAM Role
    DBStack:
      Type: AWS::Diagram::HorizontalStack
      Children:
        - DB1
        - DB2
    DB1:
      Type: AWS::RDS::DBInstance
      Label: Primary DB
    DB2:
      Type: AWS::RDS::DBInstance
      Label: Replica DB
  Links:
    - Source: User
      SourcePosition: N
      Target: Route53
      TargetPosition: S
      TargetArrowHead:
        Type: Open
    - Source: Route53
      SourcePosition: N
      Target: LoadBalancer
      TargetPosition: S
      TargetArrowHead:
        Type: Open
    - Source: LoadBalancer
      SourcePosition: SSW
      Target: EC2_1
      TargetPosition: NNW
      TargetArrowHead:
        Type: Open
    - Source: LoadBalancer
      SourcePosition: SSE
      Target: EC2_2
      TargetPosition: NNE
      TargetArrowHead:
        Type: Open
    - Source: EC2_1
      SourcePosition: S
      Target: Lambda
      TargetPosition: N
      TargetArrowHead:
        Type: Open
    - Source: Lambda
      SourcePosition: S
      Target: IAM
      TargetPosition: N
      TargetArrowHead:
      Type: Open
    - Source: EC2_1
      SourcePosition: SE
      Target: DB1
      TargetPosition: NW
      TargetArrowHead:
      Type: Open
    - Source: EC2_2
      SourcePosition: SW
      Target: DB1
      TargetPosition: NE
      TargetArrowHead:
      Type: Open
    - Source: DB1
      SourcePosition: E
      Target: DB2
      TargetPosition: W
      TargetArrowHead:
      Type: Open
```

将其另存为 aws.yaml 并运行以下命令

```
awsdac aws.yml
```

**输出**

![None](https://miro.medium.com/v2/resize:fit:720/format:webp/1*zgzH4BrYAQOLYVSrm8AwMA.png)

## 6. D2 (by Terrastruct)

[D2](https://d2lang.com/) 是一种由 Terrastruct 创建的现代图表脚本语言。它强调简洁和清晰，非常适合希望以最小的努力获得优雅图表的开发人员。它支持在 VS Code 扩展或浏览器中进行实时渲染。

**主要优点**

- 具有自动布局的简单语法。
- 支持主题和注释。
- 快速渲染，出色的开发者体验。

**缺点**

- 社区和生态系统仍在发展中。
- 缺乏开箱即用的 AWS 特定图标。

**安装**

您可以在本地安装 D2，或使用基于 Web 的 playground 进行快速可视化：[https://play.d2lang.com/](https://play.d2lang.com/)

```
brew install terrastruct/d2/d2
# or
curl -fsSL https://d2lang.com/install.sh | sh
```

**示例图表代码**

```
direction: right
DNS: "Route53: DNS"
LB: "ELB: Load Balancer"
WS1: "EC2: Web Server 1"
WS2: "EC2: Web Server 2"
Lambda: "Lambda: Auth Function"
IAM: "IAM Role"
DB1: "RDS: Primary DB"
DB2: "RDS: Replica DB"
DNS -> LB
LB -> WS1
LB -> WS2
WS1 -> Lambda
Lambda -> IAM
WS1 -> DB1
WS2 -> DB1
DB1 -> DB2
```

**输出**

![None](https://miro.medium.com/v2/resize:fit:720/format:webp/1*Y537hqE8VjkqeZqhuDqKBg.png)

## 7. Kroki

Kroki 是一个图表渲染引擎，它充当 20 多种流行的图表格式（如 Mermaid、PlantUML、Graphviz 等）的后端服务。如果您想在 CI/CD 或文档平台中标准化不同格式的图表渲染，它是理想的选择。

**主要优点**

- 集中渲染多种格式。
- 在管道、文档或应用程序中运行良好。
- 可以使用 Docker 轻松进行自托管。

**缺点**

- 仍然需要外部语法（Mermaid、PlantUML 等）。
- 需要配置自托管部署。

**安装**

您可以使用 Docker 在本地运行 Kroki，或直接调用其远程 API 进行快速渲染。

```
# Run Kroki locally
docker run -d -p 8000:8000 yuzutech/kroki
# Or call the public API
curl -X POST https://kroki.io/mermaid/svg -d 'graph TD; A-->B; B-->C; C-->A;' > diagram.svg
```

**示例用法 (Mermaid via curl)**

```
curl -X POST https://kroki.io/mermaid/svg -d 'graph TD
> DNS[Route53] --> LB[ELB]
> LB --> WS1[Web Server 1]
> LB --> WS2[Web Server 2]
> WS1 --> Lambda[Lambda Function]
> Lambda --> IAM[IAM Role]
> WS1 --> DB1[Primary DB]
> WS2 --> DB1
> DB1 --> DB2[Replica DB]' > diagram.svg
```

**输出**

![None](https://miro.medium.com/v2/resize:fit:640/format:webp/1*Cg6jCow0qACz32o3hCeTbA.png)

## 总结

Diagram-as-Code 工具正在改变开发人员、DevOps 工程师、架构师，甚至技术作家交流复杂基础设施和系统设计的方式。在当今快节奏的工程环境中，系统不断发展，以可重现、版本控制的格式记录架构不再是一种奢侈，而是一种必需品。

通过为您的工作流程选择合适的工具，您不仅可以提高文档质量，还可以解锁自动化可能性，例如直接从 CI/CD 管道渲染图表或在内部门户中嵌入最新的可视化效果。

您可以选择适合您个人工作流程或团队设置的工具。对我来说，**Diagrams** 效果很好，因为我熟悉 Python 并且主要在 AWS 生态系统中工作。它允许我轻松地将图表生成集成到我现有的基于 Python 的工作流程中。

虽然 **AWS Diagram-as-Code** 很有前景，并且感觉是 AWS 原生的，但它的 YAML 语法可能有点棘手，并且布局有时需要手动调整。因此，这完全取决于您的用例；有些人可能更喜欢简单性，而另一些人可能需要原生服务映射或高级布局控制。

无论您选择哪种工具，采用 Diagram as Code 都会使您的设计更易于维护、更易于扩展，并且更易于在团队之间共享。

让您的图表用代码说话，并随着您的基础设施扩展。