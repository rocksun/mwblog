# Spring 和 Java 如何塑造内部开发者平台

![如何塑造内部开发者平台的特色图片：Spring 和 Java](https://cdn.thenewstack.io/media/2024/03/3bea1e0b-spring-java-idp-1024x576.jpg)

我早就注意到 [Java](https://roadmap.sh/java) 促进了编写代码的异常一致的方法。该语言的表面积相对较小，几乎没有粗糙的边缘，这使得开发人员从一个 Java 项目迁移到另一个项目非常简单。对于构建或维护 [内部开发者平台](https://thenewstack.io/year-in-review-platform-engineering-still-run-by-spreadsheet/) (IDP) 的任何人来说，教训就是促进一致性真的很重要。

虽然这始终适用于 Java SE，但并不总是适用于其扩展。如今，企业 Java 开发人员有很多优秀的框架可供选择，但有一定年龄的人可能还记得在 2000 年代初使用 J2EE 进行编程的情况。J2EE 标准于 1999 年末推出，它使用 Web 和分布式企业应用程序规范扩展了 Java SE，这些应用程序可以部署在诸如 BEA WebLogic 或 [IBM](https://www.ibm.com?utm_content=inline-mention) WebSphere 等应用程序服务器上。

J2EE 标准被广泛采用，但因难以使用而声名狼藉。该规范的某些部分，尤其是 IBM 开发的原始企业 JavaBean (EJB) 规范，确实很复杂，并且带来了相当大的性能损失。例如，EJB 仅允许通过诸如公共对象请求代理体系结构 (CORBA) 等协议进行远程方法调用，这与大多数其他业务应用程序形成对比。

此外，当时设计的应用程序服务器可以启动一次并在没有中断的情况下运行数月甚至数年。正如 Java 冠军 [Holly Cummins 解释的那样](https://www.youtube.com/watch?v=7bvQXb3Nv0E)，BEA、IBM 和其他支持完整 J2EE 规范的供应商做了一些非凡的工程工作来实现这一目标。缺点是启动它们（就像在开发代码时经常做的那样）需要几分钟时间。这使得开发人员难以保持流程；作为一名英国人，我过去每次必须重新启动开发服务器时都会泡一杯茶（并且经常喝掉），这可能比我的编码效率对 Twinings 的销售更有帮助。

## 笨重、缓慢且昂贵

此外，打包和部署用于生产的 J2EE 应用程序很麻烦。“我参与其中，” [DaShaun Carter](https://www.linkedin.com/in/dashaun/) 解释道，他是 VMware Tanzu（Broadcom 的一个部门）的研究开发软件工程师和 Spring 开发人员倡导者。当 Carter 在一家能源公司担任 J2EE 开发人员时，他的职责是进行构建。“当我开始时，构建需要一周时间，并且该规范有 12 个人将 J2EE 应用程序投入生产，”他说。Carter 能够使用 Apache Ant 和各种自定义插件来缩小流程。“我们处于每周构建和测试的周期中，但生成所有 WSDL [Web 服务描述语言文档] 和构建应用程序仍然需要四个小时。”

开发工具也很昂贵。Carter 说，他们的一个工具，统一建模语言工具 Rational，每个席位需要 20,000 美元才能拥有每个开发人员所需的一切。“这太荒谬了，”他说。

## Spring 的兴起改变了范例

2004 年推出的 Spring 框架做了一些重要的事情。首先也是最重要的，它推广了依赖注入的概念，其核心是控制反转 (IoC) 容器。它还表明，可以在诸如 Apache Tomcat 等更轻量级的 servlet 容器之上构建更简单的 Web 和分布式应用程序。这些应用程序启动得更快，使开发人员能够快速成功地开始工作，而且它们还是开源且免费的。大约在同一时间，诸如 Eclipse 和 NetBeans 等开源集成开发环境 (IDE) 开始取代专有 IDE 产品，进一步降低了成本。

Spring 还提供了一种使用 Java SE 提供的相同编码一致性构建企业应用程序的方法。

不过它并不完美。Spring 不幸的是在 XML 流行的高峰期开发的，它对 XML 的依赖造成了配置方面的问题。随着框架中添加了更多功能，Spring 也被认为过于复杂。

2006 年在 Java SE 6 中采用注释作为 XML 的替代方案，在一定程度上帮助 Spring 团队减轻了配置复杂性。然而，最终最大程度地减少配置问题的，是受 Ruby on Rails 启发的 Spring Boot，它提供了关于如何构建 Spring 应用程序的高度主观视图。

## IDP 如何减少摩擦

Spring Boot 还通过 Initializr 推动了模板化的想法，
[start.spring.io](http://start.spring.io)。“这是我了解 IDP 概念的开端，”Carter 说。“我可以获取我需要的东西，比如 Spring Data 和 Spring Web，并按需组合在一起。使用 IDP 方法，模式及其原因定义明确，因此它创造了良好的开发者体验。”

Initializr 提供了护栏，并允许开发者快速启动并运行。“我可以立即开始并期待快速交付，因为 IDP 提供了大量信息和示例，例如我们如何处理日志和指标等，”Carter 解释说。

在此背景下，IDP 充当传播者，在公司内部传播 [模式](https://thenewstack.io/6-patterns-for-platform-engineering-success/)，打破孤岛并减少摩擦。正如 VMware Tanzu 在 Broadcom 的研究和开发高级总监 [James Watters](https://tanzu.vmware.com/content/authors/james-watters) 所说，“它减少了安全、架构和开发团队之间的界限。”最终，目标是让 IDP 充当快速反馈、可组合性和模式扩散的真正切入点，尤其是在大型组织中。

以 Spring 为蓝本的 IDP 降低了开发者的灵活性，但 Watters 借用云计算进行了类比，解释了为什么这可能是一件好事：

“云计算在很大程度上减少了对第 2 层网络的依赖。你无法自定义第 2 层网络，就像你可能在数据中心中所做的那样。但你可以获得一个可弹性使用的可扩展模型。我认为 [帕累托效率](https://en.wikipedia.org/wiki/Pareto_efficiency) 适用于网络，一直到应用程序模式，而这是 IDP 擅长的领域。[Cloud Foundry](https://twitter.com/fintanr/status/1420511314875715585?s=20) 是模式力量的早期指标之一，我认为我们已经看到了许多其他模式的出现，包括应用程序模板化、默认安全性和构建服务模板化。如果你考虑 [Google Cloud Run](https://cloud.google.com/run?hl=en) 或 [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview)，整个行业都开始表示模式是实现效率和默认安全性的非常好的方法。”

此外，由于 Initializr 是开源的，并且在其下方有完整的 Spring 框架，因此组织可以 [根据](https://thenewstack.io/use-of-spring-shifts-toward-modern-apps-and-architecture/) 其需求和文化对其进行调整。

## Garmin 如何使用模式和自动化

消费电子公司 Garmin 的私有云平台架构师 [Jonathan Regehr](https://www.linkedin.com/in/jonathan-regehr/) 表示，这是他们采取的方法。作为黑客马拉松的一部分，Garmin 构建了一个工具，最好将其描述为早期后台类型的门户。它生成一个骨架代码库并将其加载到 Git 存储库中。它还创建 Jenkins 作业，首次运行它并将应用程序骨架一直推送到生产环境，因此开发者只需编写代码即可。“这个笑话是，你填写一份表格，小睡一会儿，醒来后就可以开始编码了，”Regehr 说。

他承认，该工具现在已经相当老了，他的团队正在寻找替代品。即便如此，这也展示了使用模板和自动化来入门的力量。“如果你仔细考虑监听器之类的内容，它就是一个模式。我不应该关心如何获取事件或处理一致性；让模式处理这些问题，我只需要监督业务价值部分，”Regehr 说。

当工程师在团队之间移动时，这种传播模式的方法具有进一步的优势，因为它提高了一致性。正如 Monzo Bank 的高级员工工程师 [Suhail Patel](https://www.linkedin.com/in/suhailpatel/) 在 2022 年 [解释](https://blog.container-solutions.com/how-monzos-opinionated-platform-and-tools-support-their-developer-experience) 的那样，“[在 Monzo] 当你开始处理微服务时，有一条明确的铺就道路，因此它们看起来都非常统一。你可以为其他团队的服务做出贡献，因为该结构对你来说完全熟悉。”

Regehr 也赞同这个想法。“我认为你不能指望把某人放到一个项目中，然后让他们立即发挥作用。人们在加入团队后会有一个学习曲线。但如果部署相同，代码库看起来相同，并且所有内容的布局相同，他们会说，‘好的，我需要了解你的业务逻辑，但其他部分都很容易。’”

## 可扩展性取决于决策
**Monzo 和 Garmin 的平台选择**

Monzo 和 Garmin 也说明了在平台内做出选择的重要性。“构建平台团队的大规模参与者往往有两种到四种关键模式，”沃特斯说。“他们概述了如何扩展 Java 服务或 Go 服务，而不是尝试为开发人员可能拥有的每个打开的标签页构建一个门户。这两种方法非常不同。”

Garmin 对集群配置采取了类似的方法。从语言和运行时角度来看，该环境是混合的。Garmin 约 70% 的代码（Web 应用程序和侦听器的混合）是用 Java 编写的。该公司还运行大量 [Node.js](https://roadmap.sh/nodejs) 和 .NET，一些 [Python](https://roadmap.sh/python) 和少量 PHP。

Garmin 运行两个平台：

- [Red Hat](https://www.openshift.com/try?utm_content=inline-mention) OpenShift 用于 Kubernetes 工作负载
- VMware Tanzu Application Service（一些客户仍将其称为 [Pivotal Cloud Foundry](https://www.cloudfoundry.org) (PCF)）用于其余部分

随着数百名开发人员使用 [VMware Tanzu 平台](https://thenewstack.io/vmware-expands-tanzu-into-a-full-platform-engineering-environment/)，Garmin 在一个非生产环境和四个生产基础上运行超过 9,000 个应用程序实例。它使用多云基础设施，部分原因是收购，还运行一个大型私有云。

Regehr 的团队完全在内部工作，他们遵循“自动化一切”的范例。例如，为了管理他们的 [Kubernetes](https://thenewstack.io/kubernetes/) 集群，他们编写了 140,000 行自动化代码。开发人员贡献少量配置代码，并由此和他们的自动化生成所有必需的集群配置，并将它们放入存储库中。

“我们正在自动生成 110 万行集群配置， [Argo CD](https://argo-cd.readthedocs.io/en/stable/) 正在喷洒和构建集群，”Regehr 说。“我们使用生成存储库来执行此操作，这意味着如果我犯了一个错误，我可以查看错误并修复它，而不是集群在我身上消失。”

## 短暂基础设施的优势

这种级别的自动化允许基础设施团队将所有内容视为短暂的。“一个例子是 [Concourse](https://concourse-ci.org)，”Regehr 解释说。“我们有一个与每个 Tanzu 平台部署配对的 Concourse 实例，该实例处理特定于该基础的自动化。如果 Concourse 的磁盘空间用完或其数据库损坏，解决方案始终相同——烧毁 Concourse，运行自动化脚本重新部署 Concourse，然后运行我们的“UpdatePipeline”管道。这个 Concourse 看起来与 10 分钟前完全一样，除了减少了一些作业运行历史记录。”

Regehr 说，采取这种方法也有助于 Garmin 提高安全性。“如果你想让黑客一无所获，其中一种方法就是如此快速地重建你的基础设施，即使他进入服务器并构建了他的‘邪恶框架’，它也会消失得如此之快，以至于他无法在它再次消失之前重建它。”

这可能对基础设施有效，但代码本身呢？詹姆斯·沃特斯说，“在我进行的对话中引起共鸣的头号话题是：我们如何在规模化组织中默认变得更加安全？”

沃特斯认为，开发者平台充当起点，提供标准化的应用程序模式和集成库，允许你对应用程序进行身份验证。“我们还拥有一个默认安全的构建系统，该系统已重新注入 IDP，并且我们可以在创建应用程序的确切时刻提供快速的安全记分卡，”他说。IDP 还可以向开发人员发出警报，例如，“你知道这个应用程序中存在漏洞并且有可用的修复程序吗？你想应用它吗？”

VMware Tanzu 团队正在探索人工智能对行业的影响，其中一些工作已经通过 [Spring.ai](https://github.com/spring-projects/spring-ai) 可见。沃特斯说他对人工智能的重要性感到“震惊”，但他也看到了安全方面还有很多未完成的工作。“做更多的事情来自动化安全任务并构建更多模式化和安全的系统，这是我们的客户希望看到的，”他说。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。