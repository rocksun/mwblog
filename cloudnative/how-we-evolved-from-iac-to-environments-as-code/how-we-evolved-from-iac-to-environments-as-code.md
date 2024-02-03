<!--
title: 从基础设施即代码到环境即代码的进化之路
cover: https://cdn.thenewstack.io/media/2024/01/4973b279-environment-as-code-1024x576.jpg
-->

运用GitOps来启动环境，可为开发团队带来一致性、版本控制、速度等多方面的好处。

> 译自 [How We Evolved from IaC to Environments as Code](https://thenewstack.io/how-we-evolved-from-iac-to-environments-as-code/)，作者 Edan Evantal 是 Quali 的CTO Edan Evantal负责Quali基础设施自动化和环境交付平台的所有产品工程。在加入Quali之前，Edan曾在Matrix IT和Sibam Ltd担任工程管理职务。他在高科技行业拥有18年以上的经验......

这些年来，在构建我们的平台的过程中，并与我们的产品所支持的其他[DevOps](https://roadmap.sh/devops)和[平台工程师](https://thenewstack.io/platform-engineering/)一起工作，我亲眼见证了应用基础架构的演变正在打破它本来意在提供的自动化。

[基础设施即代码](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)(IaC)工具对于定义和自动交付云服务非常宝贵。当一个开发团队的需求扩展到此范围之外时，自动化通常就会中断。

原因有两个:

- **IaC工具的设计目的在于速度和自动化，而不是作为环境的真实来源**。大型团队在大规模利用基础设施和了解代码更改可能如何扰乱应用性能方面可能会遇到困难。
- **IaC工具之间不兼容**。应用日益依赖于用各种技术定义的复杂基础设施，需要手动编排来协调工具的细微差异。

开发人员在基础设施自动化功能与应用需求实际情况之间存在鸿沟。其结果是速度降低，基础设施存在未管理或配置错误的风险增加。

我们询问自己，我们能做些什么来弥合这一鸿沟，这让我们想到了一个简单的问题:

如果您可以以代码的形式启动所有环境，而不管基础设施的范围或用于定义它的 IaC 工具是什么，会怎么样？

## 在Git中将环境定义为代码

为了将环境定义为代码，我们首先需要以开发人员启动环境所需的一切来定义，这种格式对于DevOps来说既易于理解，又方便自动化机器读取。

使用我们的Torque平台，我们连接到一个Git仓库，发现其中定义的IaC模块，并将资源配置打包成一个新的由平台自动生成的YAML。

从那里，我们可以修改任何YAML代码，以包含环境启动时将生成的基础架构组件、参数、依赖项、元数据、身份验证和输出。

下面是YAML代码片段示例:

```yaml
kind: environment
environment_name: "Workstation Staging A"
description: "EC2 workstation for staging workloads"
state: inactive
owner_email: "myemail@email.com"
blueprint:
 name: "test-workstation"
 repository_name: "cloud-native-application"
 branch: "main"
 commit: "536955389cd4ecbd1b8895c4a1093fe14a809b65"
inputs:
 service-account: "sa"
 agent: "review3"
grains:
 create-ec2:
   source:
     commit: "697d1"
   specs:
     instance_type: "t2.large"
     ami: "ami-0c55b159ertafe1f0"
     security_groups: ["sg-0246e9ddc2b2f23f4"]
 post-deployment:
   scripts: ["./configure-environment.sh", "./deploy-application.sh"]
```

这包含了环境所有必要元数据的单一定义，以结构化格式呈现。

简单来说，我们利用现有的基础设施代码来定义环境为代码。

## 使用GitOps启动应用环境

为了满足客户的需求，我们需要使这一定义具有操作性。

我们的初始答案是依赖我们的自助门户。当我们平台中的管理员创建这些YAML文件(我们称之为环境的“蓝图”)时，他们可以选择“发布”它。这会将环境添加到平台中的一个自助服务目录中，拥有最终用户权限的用户可以按需启动该环境。对于那些将环境集成到开发者工具、CI/CD或内部开发者门户的人来说，发布新蓝图也可以通过这些工具访问。

为了支持采用GitOps的团队，我们需要将已发布的蓝图集成到日常工作流程中。

通过在我们发现IaC模块的原始仓库中存储这个新的YAML文件，我们使环境定义在GitOps中可访问。实际上，我们为能够访问该仓库的用户“发布”了环境定义。

现在，开发人员可以使用单个命令启动完整的环境。

这种方法还提供了几个额外的优势:

- **版本控制**: 就像应用代码一样，环境可以进行版本控制，以确保跟踪每一次更改，并在必要时进行回滚。
- **一致性**: 利用这一定义每次都以一致的方式预配环境，消除了“它在我的机器上能工作”的问题。
- **速度**: 开发人员可以通过简单地提交代码来预配环境——这是他们熟悉的动作，所以他们可以快速响应开发、测试或生产需求，而无需其他团队的帮助。
- **协作和治理**: 创建环境的共享定义为仅靠IaC本身所不能轻松做到的协作奠定了基础。
- **运营效率**: 自动化预配流程意味着减少冗余的手动工作(和疲惫)，以及DevOps工程师可以承担更有价值的任务。

在平台工程中，每一秒都是宝贵的，每一个资源都很重要。随着基础设施变得越来越复杂，以代码的形式管理环境是现代DevOps组织成熟的下一步。
