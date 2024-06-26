# 使用通用软件目录简化 CI/CD

翻译自 [Simplify CI/CD with a General-Purpose Software Catalog](https://thenewstack.io/simplify-ci-cd-with-a-general-purpose-software-catalog/) 。

通过开发人员门户网站，包含适用于开发人员和机器的单一真实数据来源，推动平台工程计划。

![](https://cdn.thenewstack.io/media/2023/03/fb3776d7-atlas-2-1024x768.jpg)

为了自动化部署流程，CI/CD 需要上下文：部署配置、构建配置、工件、版本号、依赖项、环境变量、测试结果等。这些数据不在一个地方 - 通常分散在多个系统和工具中。

例如，部署配置可能存储在单独的 YAML 文件中，环境变量可能在脚本或部署清单中定义，版本号可能手动在电子表格中跟踪。

太多的真实来源会导致几个问题，包括复杂性增加、元数据不一致、更新数据困难，最重要的是无法应用自动化。软件目录是内部开发人员门户的核心，可以提供解决方案。

##  第一步：一个可以存储 CI/CD 数据的软件目录

第一步是创建一个包含正确数据的软件目录。它应该是一个通用的软件目录，允许添加具有不同属性和关系的数据类型，提供灵活性，使每个人都能将自己的数据模型带入目录中。

![](https://cdn.thenewstack.io/media/2023/03/74e3b2d7-image1.png)

内部开发人员门户网站是平台工程的核心。它向开发人员展示作为平台的一部分构建的自助服务操作以及软件目录。

这就是有趣的地方。从开发人员体验的角度来看，可以将软件目录解释为经过审查、经过白名单处理的数据存储，以帮助开发人员克服认知负荷（例如，[请参见如何向开发人员呈现 K8s 数据](https://thenewstack.io/developer-portals-can-abstract-away-kubernetes-complexity/)）。

但这并不是全部。实际上，使用软件目录进行 CI/CD 非常强大。软件目录可以存储有关构建、环境、云和更多的数据。这种软件目录可以极大地有助于为 CI/CD 上下文创建单一真实数据来源。

与我们交谈的平台工程团队正在积极实现这些好处，尤其是在 CI/CD 元数据方面。他们将软件目录用作 CI/CD 的单一真实来源，并将软件目录中的 CI/CD 数据用作其自动化工作流程的一部分。

通过在软件目录中包含有关集群、环境、云区域和供应商的相关数据，CI/CD 过程可以更加智能和自动化，从而带来更好的工程。它将 CI/CD 与其所需的上下文数据分离，分离控件并更容易排除故障和损坏的 pipelines 。

通过开发人员门户，这些功能还有助于平台工程团队为开发人员提供更好的部署过程可见性，因为他们可以实时查看部署状态和发生的任何错误。

## 下一步：版本控制和安全

设置软件目录后，当 CI/CD 数据还用于版本控制和安全性时，可以进一步发挥 CI/CD 数据单一真实来源的优势，

跟踪对元数据和配置文件所做的所有更改可以提高元数据随时间变化的可追溯性。这对于审计目的和理解部署过程的演变很有用。

此外，它还可以促进更好的协作（通过版本和变更跟踪）、更快地解决问题以及快速恢复到先前版本和提高合规性的能力。当 CI/CD 数据碎片化时——想想 git 中分散的版本历史——很难做到这一点，但使用软件目录就容易多了。

软件目录通常确保只有授权用户才能访问和修改元数据，从而降低未经授权访问、数据泄露和其他安全事件的风险。例如，配置错误会导致 S3 存储桶公开或将带有个人身份信息的服务暴露给互联网。

## 怎么运作的？

软件目录本质上是一个集中式数据库，存储与 CI/CD 过程相关的所有元数据。可以通过 REST API 访问和修改它，这使 CI/CD 管道能够以编程方式与元数据存储进行交互。数据类型、属性和关系可以在需要时轻松添加，因为不同的组织以不同的方式执行 DevOps。

应该访问和存储哪些数据？这取决于我们所说的数据模型，即管道中重要的属性和类别。例如：

* 您可以按不同类别组织目录，每个类别都包含与 CI/CD 过程的特定方面相关的元数据。例如，可能有一个用于部署配置的类别、一个用于环境变量的类别和一个用于版本控制的类别。
* 在每个类别中，会有不同的元数据项或键。例如，在部署配置类别中，可能有部署目标、部署策略和部署版本的元数据项。

CI/CD 管道可以使用 REST API 与元数据存储交互，指定它们要访问的类别和元数据项。例如，要检索特定应用程序的部署目标，CI/CD 管道可能会向部署配置类别发送 GET 请求，指定部署目标的元数据项。

## 图数据库对软件目录的重要性

图数据库可用于软件目录。由于软件目录中的不同实体具有复杂的关系（例如，服务部署在云帐户中 K8s 集群的命名空间上）并且这些关系很重要，因此您需要能够本地查询它们。图数据库可以让您做到这一点。这在 CI/CD 管道的上下文中特别有用，开发人员、DevOps 和机器需要能够快速访问有关系统不同部分如何相关的信息。

* 或者假设我们想要识别使用特定镜像版本的所有服务。如果没有元数据存储，您将需要手动搜索各种服务的配置和文档以找到匹配的。但是有了图数据库，我们可以为每个服务创建节点，并将它们链接到它们使用的图像版本。这使我们能够快速查询图以找到使用所需镜像版本的所有服务。我们可以从查询镜像版本节点开始，然后遍历它与服务节点的关系。我们甚至可以向节点添加其他信息，例如服务运行的环境、上次更新的日期以及任何相关的警报或问题。这提供了整个系统的全面视图，使我们能够轻松跟踪和管理我们的服务。
* 例如，假设我们要识别在特定区域中运行的所有服务（例如，如果您正在运营一个大型云平台，为不同区域的客户提供服务）。如果没有图形数据库，我们将需要跨不同的数据源执行多个查询并尝试拼凑信息。但是，使用图形数据库，我们可以在一次查询中完成。

这种本机查询复杂关系的能力对于使开发人员和机器能够更有效地执行影响分析、管理配置、运行连续测试和管理发布至关重要。这不仅简化了 CI/CD 流程，还有助于确保系统的整体稳定性和可靠性。

![](https://cdn.thenewstack.io/media/2023/03/bf554090-image2.png)

## 软件目录需要 API 优先

现在我们需要考虑如何轻松地将数据放入软件目录中。轻松地将数据提取到软件目录中需要 API 优先的方法。这包括来自云提供商、Kubernetes（用于集群数据）、git 提供商、基础架构即代码 (IaC) 工具（如 Terraform 或 Crossplane 等）的数据。

API 优先的方法还可以轻松构建与其他工具和系统的集成，例如创建包含有关基础架构和应用程序信息的仪表板。这可以帮助您构建更全面、更有用的元数据存储，提供您的基础架构和应用程序的整体视图。

## 结论

平台工程和用作开发人员核心界面的内部开发人员门户的兴起也提供了创建软件目录的机会，该目录不仅对开发人员有用。具有 CI/CD 元数据的软件目录可以创建单一事实来源、解决版本和安全问题，并允许部署过程自动化等。要查看通用软件目录可以包含什么，请在此处转到 Port 的现场演示。