# 基础设施即代码的历史与未来

基础设施即代码（Infrastructure as Code）是软件开发中一个引人入胜的领域。虽然作为一门学科，它相对年轻，但在其短暂的存在期间，它已经经历了几次具有开创性意义的转变。我认为它是当今软件开发创新最热门的领域之一，许多参与者——从大型科技公司到初创企业——都在创造新的方法。如果完全实现，这些方法有可能彻底改变我们编写和部署软件的方式。

翻译自 [End of Line blog](https://www.endoflineblog.com/) 的 [History and future of Infrastructure as Code](https://www.endoflineblog.com/history-and-future-of-infrastructure-as-code)，作者是 Adam Ruka 。

![](cover.jpg)

在本文中，我想深入探讨基础设施即代码的主题：它是什么，它带来了什么好处，它已经经历了哪些具有开创性意义的转变，以及未来可能的发展。

## 什么是基础设施即代码（IaC）？

让我们从解释这个概念开始。基础设施即代码是一个涵盖一系列实践和工具的总称，旨在将应用程序开发的严谨性和经验应用于基础设施供应和维护的领域。

这里的“基础设施”是有意模糊的，但我们可以将其定义为运行给定应用程序所需的环境中不属于应用程序本身的一切。一些常见的例子包括：服务器、配置、网络、数据库、存储等。本文后面还会有更多的例子。

基础设施即代码的实践方式与运行时代码的实践方式相似。包括版本控制、自动化测试、CI/CD 部署流水线、本地开发以获得快速反馈等。

遵循这些基础设施实践可以带来哪些优势？

* **性能**。如果需要提供或更改大量基础设施，基础设施即代码将始终比人工手动执行相同操作更快。
* **可复现性**。人类在可靠地重复执行相同任务方面往往表现不佳。如果我们需要重复做同一件事情一百次，很可能会分心，并在途中出错。基础设施即代码不会受到这个问题的困扰。
* **文档**。你的基础设施代码兼作系统架构的文档。当维护系统的团队规模扩大时，这一点变得至关重要——你不希望依赖部落知识，或者只有少数团队成员知道系统基础设施的工作原理。作为额外的好处，这些文档永远不会过时，不像传统文档那样。
* **审计历史**。通过基础设施即代码，由于你以与应用程序代码相同的方式对基础设施代码进行版本控制（有时被称为 [GitOps](https://about.gitlab.com/topics/gitops)），它为你提供了历史记录，可以查看基础设施随时间的变化，并在任何更改引发问题时回滚到安全点。
* **可测试性**。基础设施代码可以像应用程序代码一样进行测试。你可以在各个级别进行测试，包括[单元测试](https://www.endoflineblog.com/unit-acceptance-or-functional-demystifying-the-test-types-part2)、[集成测试](https://www.endoflineblog.com/unit-acceptance-or-functional-demystifying-the-test-types-part3)和[端到端](https://www.endoflineblog.com/unit-acceptance-or-functional-demystifying-the-test-types-part4)测试。

现在，让我们谈谈基础设施即代码工具在实践过程中经历的主要阶段。

## 第一代：声明性的主机配置

**例子**：[Chef](https://docs.chef.io/)，[Puppet](https://www.puppet.com/blog/what-is-infrastructure-as-code)，[Ansible](https://www.ansible.com/)

基础设施即代码工具的第一代主要关注**主机配置**。这是有道理的，因为在软件系统中，基础设施在最低抽象级别上由单个机器组成。因此，这个领域的第一批工具主要专注于配置这些机器。

这些工具管理的基础设施资源是 Unix 中熟悉的概念：文件、包管理器（如 [Apt](https://ubuntu.com/server/docs/package-management) 或 [RPM](https://rpm.org/) ）中的软件包、用户、组、权限、init服务等等。

以下是一个创建 Java 服务的 [Ansible playbook](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html) 示例：

```yaml
- hosts: app
  tasks:
  - name: Update apt-get
    apt: update_cache=yes

  - name: Install Apache
    apt: name=apache2 state=present

  - name: Install Libapache-mod-jk
    apt: name=libapache2-mod-jk state=present

  - name: Install Java
    apt: name=default-jdk state=present

  - name: Create Tomcat node directories
    file: path=/etc/tomcat state=directory mode=0777
  - file: path=/etc/tomcat/server state=directory mode=0775

  - name: Download Tomcat 7 package
    get_url: url=http://apache.mirror.digionline.de/tomcat/tomcat-7/v7.0.92/bin/apache-tomcat-7.0.92.tar.gz dest='/etc/tomcat'
  - unarchive: src=/etc/tomcat/apache-tomcat-7.0.92.tar.gz dest=/etc/tomcat/server copy=no

  - name: Configuring Mod-Jk & Apache
    replace: dest=/etc/apache2/sites-enabled/000-default.conf regexp='^</VirtualHost>' replace="JkMount /status status \n JkMount /* loadbalancer \n JkMountCopy On \n </VirtualHost>"

  - name: Download sample Tomcat application
    get_url: url=https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war dest='/etc/tomcat/server/apache-tomcat-7.0.92/webapps' validate_certs=no

  - name: Restart Apache
    service: name=apache2 state=restarted

  - name: Start Tomcat nodes
    command: nohup /etc/tomcat/server/apache-tomcat-7.0.92/bin/catalina.sh start
```

这个 playbook 操作的抽象级别是一个具有 Linux 操作系统的单个计算机。我们声明要安装的 Apt 软件包，要创建的文件（有多种方法可以创建：直接在给定路径的目录中，从给定 URL 下载，从存档中提取文件，或根据正则表达式替换编辑现有文件），要运行的系统服务或命令等等。事实上，如果你稍微看一下，这个 playbook 看起来非常类似于一个 Bash 脚本。主要区别在于 playbook 是声明性的 - 它描述了它想要发生的事情，比如在机器上安装给定的 Apt 软件包。这与脚本不同，脚本包含要执行的命令。虽然差别很小，但很重要；这使得 playbook 具有幂等性，这意味着即使它在中间某个地方失败了（也许 tomcat.apache.org 暂时中断，因此从该网站下载失败），你可以重新启动它，先前成功执行的步骤将识别到这一事实，并且会直接跳过而不执行任何操作，这通常不适用于 Bash 脚本。

这些工具非常重要，它们在许多方面推动了软件开发行业的进步。然而，它们仅适用于单个主机的层面，这是一个巨大的限制。这意味着你要么手动管理这些主机，从而抵消了基础设施即代码的许多好处，要么需要将这些工具与管理主机的工具结合使用，例如用于本地开发的 [Vagrant](https://developer.hashicorp.com/vagrant/tutorials/getting-started) 或用于共享环境（如生产环境）的 [OpenStack](https://www.openstack.org/) 。例如，如果你想创建一个经典的[三层架构](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture)，你需要创建三种不同的虚拟机类型，每种类型都有自己的 Ansible playbook ，根据其在架构中的角色配置主机。

基础设施即代码工具的下一个阶段将消除这个限制。

## 第二代：声明式，云计算

**例子**：[CloudFormation](https://aws.amazon.com/cloudformation)，[Terraform](https://www.terraform.io/)，[Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)

2000 年代中期引入的云计算是软件开发历史上的一个里程碑事件。在很多方面上，我认为我们仍在思考它真正引发了多大的革命。

突然之间，管理主机的问题得到了解决。你不需要运行和操作自己的 OpenStack 集群来自动化管理虚拟机；云提供商会为你处理所有这些。

但更重要的是，云立即提高了我们设计系统的抽象级别。不再只是给主机分配不同的角色。如果你需要[发布-订阅资源](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)，那么就没有必要在虚拟机上进行配置，并在其上安装 Apt 上的 [ZeroMQ](https://zeromq.org/download) 软件包；相反，你使用 [Amazon SNS](https://aws.amazon.com/sns) 。如果你想存储一些文件，你不需要将一堆主机指定为存储层；相反，你创建一个 [S3 存储桶](https://aws.amazon.com/s3)。依此类推。

**主机配置**不再是核心，我们进入了配置托管服务的阶段。由于上一代工具只能在单个主机的层面上工作，因此需要一种新的方法来解决这个问题。

为解决这个问题，出现了 CloudFormation 和 Terraform 等工具。与第一代类似，它们也是声明式的；但与第一代不同的是，它们操作的抽象级别不是单个机器上的文件和软件包，而是属于不同托管服务的单个资源、它们的属性以及它们彼此之间的关系。

例如，下面是一个定义由 [SQS queue](https://aws.amazon.com/sqs) 触发的 [AWS Lambda function](https://aws.amazon.com/pm/lambda) 的 CloudFormation 模板：

```yaml
AWSTemplateFormatVersion : 2010-09-09
Resources:
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      Code:
        S3Bucket: my-source-bucket
        S3Key: lambda/my-java-app.zip
      Handler: example.Handler
      Role: !GetAtt LambdaExecutionRole.Arn
      Runtime: java17
      Timeout: 60
      MemorySize: 512
  MyQueue:
    Type: AWS::SQS::Queue
    Properties:
      VisibilityTimeout: 120
  LambdaFunctionEventSourceMapping:
    Type: AWS::Lambda::EventSourceMapping
    Properties:
      BatchSize: 10
      Enabled: true
      EventSourceArn: !GetAtt MyQueue.Arn
      FunctionName: !GetAtt LambdaFunction.Arn
  LambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - sts:AssumeRole
      Policies:
        - PolicyName: allowLambdaLogs
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - logs:*
                Resource: arn:aws:logs:*:*:*
        - PolicyName: allowSqs
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - sqs:ReceiveMessage
                  - sqs:DeleteMessage
                  - sqs:GetQueueAttributes
                  - sqs:ChangeMessageVisibility
                Resource: !GetAtt MyQueue.Arn

```

这个 CloudFormation 模板与我们之前看到的 Ansible playbook 非常不同。它不包含任何有关文件、软件包或初始化服务的内容；相反，它使用托管服务的语言。我们提供了 AWS::Lambda::Function 和 AWS::SQS::Queue 类型的资源。我们不定义这些东西将在哪些主机上执行，以及如何配置这些主机——我们只关心正确使用云供应商提供的托管服务。

然而，它与 Ansible 共同的地方是它们都具有声明式的特性。我们不编写调用 SQS API 来[创建队列](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html)的代码——我们只声明我们想要一个具有 `VisibilityTimeout` 属性设置为 `120` 的队列，部署引擎（在这种情况下是 CloudFormation ）会处理哪些 AWS API 调用以实现该目标。如果我们以后决定修改队列（也许我们希望超时时间是 `240` 而不是 `120` ），或者完全删除它，我们只需更改模板，引擎将确定必要的 API 调用来更新或删除它。

这些工具是基础设施即代码演变中的重大里程碑，大大提高了抽象级别。然而，它们也有一些缺点。

首先，为了实现声明式的特性，它们使用自定义的 DSL （在 CloudFormation 的情况下，是 JSON 或 YAML 格式）。这意味着在该 DSL 中没有通用编程语言的所有功能，例如变量、函数、循环、条件语句、类等。这意味着没有简单的方法来减少重复；例如，如果我们想要在应用程序中有不止一个相同配置的队列，我们不能只编写一个循环执行三次；我们必须复制粘贴相同的定义三次，这并不理想。它还意味着无法将模板拆分为逻辑单元；无法将一组资源指定为存储层，另一组资源指定为前端层等——所有资源属于一个扁平的命名空间。

这些工具的另一个问题是，虽然它们显然比第一代的主机配置更高级，但仍要求你指定系统中使用的所有资源的所有细节。例如，你可能注意到在上面的示例模板中，除了我们主要关注的 Lambda 和 SQS 资源之外，还有这些事件映射和 IAM 资源。这是为了连接 SQS 和 Lambda 而需要的“粘合剂”，正确配置这些“粘合剂”资源并不容易。例如，在函数执行上下文中成功触发给定队列的情况下，需要授予 IAM 角色一组非常特定的权限（`sqs:ReceiveMessage`、`sqs:DeleteMessage`、`sqs:GetQueueAttributes` 和 `sqs:ChangeMessageVisibility`）。

在某种程度上，这是一个非常低级的问题；然而，由于前述 DSL 缺乏抽象工具，因此实际上没有可用的工具可以隐藏这些实现细节。因此，每次你需要创建一个由 SQS 队列触发的新的 Lambda 函数时，你没有选择，只能复制包含这 4 个权限的片段。因此，这些模板很容易变得冗长，并且包含大量重复的内容。

## 第三代：命令式，云端

**例子**：[AWS CDK](https://aws.amazon.com/cdk)，[Pulumi](https://www.pulumi.com/)，[SST](https://sst.dev/)

第二代工具的所有缺点都可以追溯到它们使用了缺乏典型抽象工具的自定义 DSL ，例如：变量、函数、循环、类、方法等，这些是我们在使用通用编程语言时习惯使用的工具。因此，基础设施即代码工具的第三代的主要思想很简单：如果通用编程语言已经具备了这些工具，为什么不使用它们来定义基础设施，而不是使用自定义的 JSON 或 YAML DSL 呢？

例如，让我们来看一个与上述 CloudFormation 模板等效的 Cloud Development Kit（CDK） 程序（本例中我将使用 TypeScript ，但任何其他受 CDK 支持的语言看起来都非常相似）：

```TypeScript
class LambdaStack extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const func = new lambda.Function(this, 'Function', {
            code: lambda.Code.fromBucket(
                s3.Bucket.fromBucketName(this, 'CodeBucket', 'my-source-bucket'), 
                'lambda/my-java-app.zip'),
            handler: 'example.Handler',
            runtime: lambda.Runtime.JAVA_17,
        });

        const queue = new sqs.Queue(this, 'Queue', {
            visibilityTimeout: cdk.Duration.minutes(2),
        });

        func.addEventSource(new lambda_events.SqsEventSource(queue));
    }
}

const app = new cdk.App();
new LambdaStack(app, 'LambdaStack');
```

CDK 代码的第一个有趣之处在于它比等效的 CloudFormation 模板要短得多，大约只有 20 行 TypeScript 代码，而 YAML 代码大约有 60 行，大约是 3 比 1 的比例。这是一个非常简单的示例；随着基础设施变得更加复杂，这个比例会越来越大——在某些情况下，我看到的比例高达 30 比 1 。

第二个有趣之处在于 CDK 代码比 CloudFormation 模板更高级。注意到如何从队列触发函数的细节是通过 addEventSource() 方法和 SqsEventSource 类优雅地封装的。这两个 API 都是类型安全的——你不会因为错误而将 SNS 主题传递给 SqsEventSource ，因为编译器不会允许这样做。还要注意的是，我们在代码中没有提及 IAM —— CDK 会为我们处理所有这些细节，因此我们不需要知道允许函数被队列触发所需的确切 4 个权限是什么。

所有这些都是由于高级编程语言允许我们构建的抽象机制。我可以将重复或复杂的代码放入一个类或函数中，并使用简洁的 API 呈现给我的项目，这样就能将所有混乱的实现细节整洁地封装在内部，就像由 CDK 团队创建和维护的 SqsEventSource 类一样。如果其他项目也可以从中受益，我可以将我的抽象封装成一个库，使用所编写的编程语言，并通过该语言的包管理器（例如 JavaScript/TypeScript 的 [npmjs.com](https://www.npmjs.com/) 或 Java 的 [Maven Central](https://central.sonatype.com/) ） 进行分发，以便其他人可以依赖它，就像我们为应用程序代码分发库一样。我甚至可以将它添加到 [constructs.dev](https://constructs.dev/) 的可用开源 CDK 库目录中，以便更容易找到。

## 第四代：来自代码的基础设施

**示例**：[Wing](https://www.winglang.io/)、[Dark](https://darklang.com/)、[Eventual](https://www.eventual.ai/cloud)、[Ampt](https://www.getampt.com/)、[Klotho](https://klo.dev/)

虽然第三代基础设施即代码工具在使云更易用方面取得了巨大的进步（可能因为我是 AWS CDK 团队的前成员，所以我可能有些偏见，但我认为这种说法并不离谱），但它们仍然有改进的空间。

它们的第一个缺点是它们主要在单个云服务的层面上操作。因此，虽然它们使使用 Lambda 或 SQS 变得简单，但您仍然需要知道这些服务是什么，以及为什么考虑使用它们。

在这个现代云时代，我们看到每个供应商提供的服务数量爆炸式增长。仅 AWS 就有 200 多个服务。随着可用选择的多样性越来越大，选择适合您要求的正确服务变得越来越困难。我应该在 AWS Lambda、AWS EKS 还是 AWS AppRunner 上运行我的容器？我应该使用 Google Cloud Functions 还是 Google Cloud Run ？什么情况下使用哪种服务更合适？

许多开发人员对每个云供应商的服务了解不够详细，特别是因为这些服务往往经常发生变化，引入新服务（或现有服务的新功能）并废弃旧服务。但是他们确实对系统设计的基本原理有很好的理解。因此，他们知道他们需要一个在负载均衡器后面进行水平扩展的无状态 HTTP 服务、一个 NoSQL 文档存储、一个缓存层、一个静态网站前端等。对于他们来说，第三代工具的层次太低了；理想情况下，他们希望以这些高级系统架构术语描述基础设施，然后将如何最好地实现该架构在特定云提供商上的细节委托给其 IaC 工具。

第三代工具的第二个缺点是它们完全将基础设施代码与应用程序代码分离。例如，在上面的 CDK 示例中， Lambda 函数的代码与其基础设施定义完全无关。虽然 CDK 具有允许两种代码类型存在于同一个版本控制存储库中的 Assets 概念，但它们仍然无法相互交互。在某种意义上，这是重复——我的应用程序代码使用 SQS 队列对我的基础设施代码提出了隐含的要求，以正确地配置该队列。但是，就像所有的重复和隐含要求一样，当两侧不小心不同步时（例如，如果我从基础设施代码中删除队列，但忘记更新应用程序代码不再使用它），可能会引发问题，并且没有语言编译器在部署更改之前捕捉这些错误，潜在地引发问题。

第四代基础设施即代码工具旨在解决这两个问题。它们的主要前提是在现代云时代，基础设施代码与应用程序代码之间的区别不再有太大意义。由于双方都使用托管服务的语言进行交流，我在应用程序代码中想要使用的任何资源都需要在基础设施代码中存在，就像我们在 Lambda 和 SQS 示例中看到的那样。

因此，这些工具将两者统一起来。它们不再有独立的基础设施和应用程序代码，而是消除了前者，只留下应用程序代码，基础设施完全由应用程序代码派生。因此，这种方法被称为来自代码的基础设施（Infrastructure **from** Code），与即代码（**as** Code）相对应（也以框架定义的基础设施（[Framework-defined Infrastructure](https://vercel.com/blog/framework-defined-infrastructure)）的名称而闻名）。

让我们看两个 IfC 工具的示例。

### Eventual

第一个是 [Eventual](https://docs.eventual.ai/) ，它是一个 TypeScript 库，定义了现代云应用程序的几个通用构建块：Services（服务）、APIs（API接口）、Workflows（工作流）、Tasks（任务）、Events（事件）等等。通过将它们组合在一起，您可以使用这些通用构建块创建任意复杂的应用程序，就像乐高积木一样。 Eventual 部署引擎知道如何将这些构建块转换为 AWS 资源，例如 Lambda 函数、 [API 网关](https://aws.amazon.com/api-gateway)、 [StepFunction 状态机](https://aws.amazon.com/step-functions)、 [EventBridge 规则](https://aws.amazon.com/eventbridge)等等。这种转换的细节被库抽象隐藏起来，因此作为用户，您不必担心这些细节 - 您只需使用提供的构建块，部署由库处理。

以下是一个简单的示例，展示了一个Event（事件）、Subscription（订阅）、Task（任务）、Workflow（工作流）和API（应用程序接口）：


```TypeScript
import { event, subscription, task, workflow, command } from "@eventual/core";

// 定义一个Event
export interface HelloEvent {
    message: string;
}
export const helloEvent = event<HelloEvent>("HelloEvent");

// 每次事件被触发时收到通知
export const onHelloEvent = subscription("onHelloEvent", {
    events: [helloEvent],
}, async (event) => {
    console.log("received event:", event);
});

// 一个格式化接收到的消息的任务
export const helloTask = task("helloTask", async (name: string) => {
    return `hello ${name}`;
});

// 使用上述任务的示例工作流
export const helloWorkflow = workflow("helloWorkflow", async (name: string) => {
    // 调用任务以格式化消息
    const message = await helloTask(name);

    // 发出一个事件，传递一些数据
    await helloEvent.emit({
        message,
    });

    return message;
});

// 为 POST /hello <name> 创建一个REST API
export const hello = command("hello", async (name: string) => {
    // 触发上述工作流
    const { executionId } = await helloWorkflow.startExecution({
        input: name,
    });

    return { executionId };
});
```

### Wing

另一种方法是创建一种全新的通用编程语言：这种语言的设计目标不是在单台机器上执行，而是从头开始构建以在许多机器上分布式运行的语言，以适应云环境。[Wing](https://docs.winglang.io/) 是由 [Monada](https://www.linkedin.com/company/monadahq) 公司创建的语言， AWS CDK 的创始人 [Elad Ben-Israel](https://twitter.com/emeshbi) 是该公司的联合创始人。

它通过引入执行阶段的概念将基础设施和应用程序代码合并在一起。Preflight（预检）是默认阶段，大致对应于“构建时间”，在此阶段执行基础设施代码；Inflight（运行时间）对应于“运行时间”，应用程序代码运行，旨在在云中执行。Inflight 代码可以通过 Wing 编译器实现对预检代码中定义的对象的引用，从而实现二者之间的交互。然而， Inflight 阶段不能创建新的预检对象，只能使用明确标记为 Inflight 修饰符的这些对象的特定 API 。 Wing 编译器确保您的程序遵守这些规则，因此如果您试图违反规则，编译将失败，并为您提供有关应用程序正确性的快速反馈。

因此，上面提到的由队列触发的无服务器函数的示例在 Wing 中如下所示：

```java
bring cloud;

let queue = new cloud.Queue(timeout: 2m);
let bucket = new cloud.Bucket();

queue.addConsumer(inflight (item: str): str => {
    // 获取具有与消息相等的名称的bucket中的项目
    let object = bucket.get(item);
    // 对'object'进行一些操作...
});
```


这段代码非常高级 - 我们甚至没有明确提及无服务器函数资源，只是在一个带有 Inflight 修饰符的匿名函数内编写应用程序代码。该匿名函数将部署在一个无服务器函数中，并在云中执行（或在 Wing 附带的本地模拟器中执行，以提供快速的开发体验）。

请注意，我们不能在应用程序代码中错误地使用错误的资源 - 例如，使用 SNS 主题而不是 SQS 队列，因为预检代码中没有定义 Topic 对象，所以我们无法在 Inflight 代码中引用它。同样，您不能在预检代码中使用 bucket.get() 方法，因为那是仅限 Inflight 的 API 。通过这种方式，语言本身防止我们在基础设施和应用程序代码分离的情况下犯下许多错误。

如果您想了解更多关于基于代码的基础设施这一新趋势的信息，我建议阅读另一个工具 [Klotho](https://klo.dev/) 的共同创始人 [Ala Shiban](https://twitter.com/alashiban) 撰写的[这篇文章](https://klo.dev/state-of-infrastructure-from-code-2023)。

## 总结

这就是基础设施即代码领域的历史和最新发展。我认为这是值得密切关注的领域，因为它是当今软件工程领域最热门的领域之一，甚至将最新的人工智能进展应用到一些产品中，例如 [EventualAI](https://www.eventual.ai/) 和 [Pulumi Insights](https://www.pulumi.com/docs/intro/insights) 。

我相信，在不久的将来，这个领域将会出现许多新的方法，对我们编写和发布软件的方式产生深远影响。

如果您想深入了解这个主题，[Yehuda Cohen](https://twitter.com/funwiththecloud) 的[这篇文章](https://yehudacohen.substack.com/p/exploring-the-emerging-cloud-development)是对基础设施即代码在云环境中的全面探索，非常长且详细。
