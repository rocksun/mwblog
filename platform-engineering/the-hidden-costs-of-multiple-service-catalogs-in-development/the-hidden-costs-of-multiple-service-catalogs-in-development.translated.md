# 开发中多个服务目录的隐藏成本

![开发中多个服务目录的隐藏成本特色图片](https://cdn.thenewstack.io/media/2025/01/05e3f4b1-aleksi-tappura-cjcqksp2wc4-unsplash-1024x678.jpg)

Unsplash上的[Aleksi Tappura](https://unsplash.com/@a?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

开发人员[工具](https://thenewstack.io/platform-engineering-it-is-all-about-the-tooling/)越来越需要服务目录来确定其内创建的数据范围，尤其是在这些工具与组织开发的每一款软件相关联时。

因此，您最终常常会拥有[多个服务目录](https://thenewstack.io/30-of-engineer-leads-use-a-spreadsheet-as-a-service-catalog/)来管理您引入的服务。多个目录意味着宝贵的时间从平台和软件团队转移，转向填充关于他们应该构建的事物的元数据。

构建软件目录需要时间和合适的工具。我是一名软件工程师和产品经理，负责构建开发者工具和内部门户。因此，我亲眼目睹了团队需要手动将数据输入根本不是为此目的而构建的目录，或者在工具不支持此类监控时跟踪目录与生产环境的差异，以及组织通常难以保持其各种目录同步的困境。

您很容易不知不觉地拥有位于不同位置、具有多个范围级别的[多个服务目录](https://thenewstack.io/simplify-ci-cd-with-a-general-purpose-software-catalog/)。这是低效的，目录很快就会不同步。

这很痛苦。

**为什么会发生这种情况？**

软件目录作为DataDog和New Relic等工具中的核心概念越来越普遍：

* **数据和可观察性**，例如DataDog和New Relic
* **事件管理**，例如[Incident.io](http://incident.io)、PagerDuty和FireHydrant
* **开发者体验**，例如DX

虽然很重要，但成为软件目录并不是这些服务的首要目的，因此目录的摄取、可视化和操作的质量低于最佳水平。

某种形式的目录来描述组织构建的软件类型是使其有效工作的必要条件，但这并不意味着该软件专注于创建出色的目录创建摄取机制。

如今，大多数工具都需要软件目录，因此它允许您在应用程序内构建一个。但是，这很少是最佳方法。

## 为什么应该使用IDP来构建一个目录？

为了避免多个目录，您需要一个单一的事实来源——一个统治所有目录的目录。

[内部开发者门户](https://thenewstack.io/internal-developer-portals-should-be-internal-developer-hubs/)(IDP)成为该目录的理由非常充分。

像Backstage、Port和Cortex这样的IDP，其核心是软件目录。它们还有一些其他重要功能（记分卡、用于帮助执行任务的自动化运行器等），但其核心是使服务目录易于创建、配置和使用。

来自各种系统的信息会被呈现给开发团队，以创建一个单一窗口。在构建IDP时，组织会固有地创建一个集成和丰富其软件数据的点，然后可以将其用作更广泛、更复杂的数据流的一部分。

考虑数据流：

- 关于软件的元数据进入，无论是自动摄取还是手动添加。
- 为每一款软件创建丰富的对象。
- 结构化信息在目录的数据模型中定义和包含，允许构建一个软件图，显示每一款软件与其他软件之间的关系。

该目录是关于您已构建的软件的丰富的存储库。它距离成为其他需要该信息的服务的事实来源只有一步之遥。

**登场：Backstage**

Backstage作为IDP的内置优势使其在此用例中表现出色。作为一个开放系统，它比Port、Cortex等专有软件更具可扩展性。

作为市场上主要的IDP，Backstage从您随后需要连接到的第三方服务提供商以及目录信息提供商（例如，特别活跃的插件开发商AWS）那里获得了大量支持：
**插件生态系统**。第三方不断构建新的选项来支持此用例。这些插件支持可视化目录中的信息，或者，更重要的是，支持从Backstage导入或提取目录数据。**自动导入**。Backstage拥有自动导入功能。例如，AWS最近发布了一个插件，支持自动导入S3存储桶和RDS实例等资源，使完成软件目录比使用其他服务更直接。**易于编辑**。Backstage附带大量简单的丰富选项，主要依赖于以一种格式进行民主编辑的YAML文件。**数据提取**。当您准备好连接到第三方系统时，Backstage目录API和插件生态系统使从Backstage获取数据变得容易。

**如何使用Backstage目录作为真相来源**
让我们来看一些例子，说明如何通过事故管理、数据可视化和开发者体验的例子来实现这一点：

- DataDog
- [Incident.io](http://incident.io) - DX

**DataDog**

**使用`catalog-info.yaml`文件**

Backstage软件目录的核心是一系列YAML文件，这些文件与您选择的源代码管理(SCM)工具中的代码一起存储(Backstage支持所有这些工具)。这些通常简称为`catalog-info.yaml`文件。它们只是服务元数据和对其他服务的引用键。

DataDog维护其使用此`catalog-info.yaml`文件来导入目录信息的导入机制。该集成会不断扫描SCM中的存储库，查找名为`service.datadog.yaml`和`catalog-info.yaml`的Backstage YAML文件——当您将服务添加到Backstage软件目录时，您会创建这些文件。下面的代码片段显示了`catalog-info.yaml`的示例。

您需要为此示例启用[GitHub集成](https://docs.datadoghq.com/integrations/github/)

**使用DataDog API**

您还可以将Backstage YAML文件POST到DataDog API。这允许您以编程方式发送可能不存在于GitHub存储库中的Backstage服务定义。[Backstage目录API](https://www.datadoghq.com/blog/service-catalog-backstage-yaml/)可以响应您的整个目录(或仅其子集)，因此可以使用此路由同步两者。

[Incident.io](http://incident.io)维护各种方法来将其内部软件目录连接到真相来源。

**使用`catalog-info.yaml`文件**

[Incident.io](http://incident.io)通过其`catalog-importer`以类似的方式工作。`catalog-importer`稍微复杂一些，因此值得一看。

导入器可以从各种来源提取数据，“满足人们通常存储目录数据的所有方式”，正如他们所说。

一个选项是[GitHub](https://github.com/incident-io/catalog-importer/blob/master/docs/sources.md#github)。这与上面概述的DataDog导入机制的工作方式大致相同。

**使用目录API**

另一种选择是通过Backstage目录API直接从Backstage读取目录信息。本质上，这会对您的目录发出[GET /entities](https://backstage.io/docs/features/software-catalog/software-catalog-api/#get-entities)调用并直接检索信息。您可以根据需要对其进行过滤，以确保只提取与[Incident.io](http://incident.io)相关的子集数据。

**DX**

DX采用不同的方法。他们构建了一个完整的Backstage后端插件来从Backstage提取数据。

**使用Backstage后端插件**

DX Backstage后端插件在Backstage中设置作业以同步DX目录。

这些作业调用DX API来发送目录信息。

由于这可能是大量数据(我经常看到包含10万到20万个实体的Backstage目录)，您可能应该使用可选参数进行过滤。您可以在应用程序配置中设置这些参数。

```yaml
# app-config.yaml
dx:
  catalogSyncAllowedKinds: [API, Component, User, Group]
```

您还可以控制同步调度，以免向您的目录发送垃圾邮件。同样，这只是一些配置。

```yaml
# app-config.yaml
dx:
  schedule:
    frequency:
      minutes: 45
```

**如果您需要目录，请获取目录。**

我们主要关注Backstage，但这里核心信息是，单个目录优于多个目录，每个目录提供不同的真相来源。假设您必须选择一个软件作为最终目录。在这种情况下，您应该选择一个本身擅长作为软件目录的软件，而不是一个次要包含目录的工具。

内部开发者门户在这方面表现出色。无论是Backstage、Port、Cortex、Rely还是任何其他IDP，在日益基于结构化软件目录的开发工具世界中，它都是明智的选择。

[YOUTUBE.COM/THENEWSTACK](YOUTUBE.COM/THENEWSTACK)
技术发展迅速，不要错过任何一集。订阅我们的YouTube
频道，收听我们所有的播客、访谈、演示等等。 [YouTube](https://youtube.com/thenewstack?sub_confirmation=1)