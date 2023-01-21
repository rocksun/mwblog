## 介绍

受 DevOps 所承诺的跨职能合作的启发，平台工程已开始作为这种合作的一种明确形式出现在企业中：平台团队策划并展示基础能力、框架和经验，以促进和加速内部客户的工作，例如应用程序开发人员、数据科学家和信息工作者。

本文旨在通过描述以下内容来支持企业领导者、企业架构师和平台团队产品经理调查和规划内部平台：

1. 什么是平台
2. 为什么平台有价值
3. 成功平台的属性
4. 成功的平台团队的属性
5. 实施平台时的挑战
6. 如何衡量平台的成功
7. 平台能力

## 什么是平台

分布式计算中的平台是为多种用途提供通用支持能力和服务的层。平台为获取、使用和管理这些功能和服务提供一致的用户体验，包括 Web 门户和页面、特定于场景的代码模板、可自动化的 API 和命令行工具。

根据 Atlassian 的说法，“平台团队创建的功能可供众多采用相同流程的团队使用，开销很小......平台团队最大限度地减少了采用相同流程的团队的资源和认知负荷......平台团队可以创建一种有凝聚力的体验，跨越不同的用户体验或产品。”

根据 Martin Fowler 和 Evan Bottcher 的说法，“数字平台是自助服务的 API、工具、服务、知识和支持的基础，它们被安排为引人注目的内部产品。自治的交付团队可以利用该平台更快的交付产品功能，并减少协调工作。”

平台与分布式系统特别相关，分布式系统将支持功能与特定于应用程序的逻辑分开。在这样的环境中，数据库和对象存储、消息队列和代理、可观测性收集器和仪表板、用户目录和身份验证系统、任务运行器和协调器等能力都是独立管理的，并集成到在容器和机器中运行的应用程序中。平台以一种使他们易于集成到应用程序中的方式为许多团队提供这些功能。

一个基本平台为应用程序开发人员提供一致的体验，以实现一系列诸如数据库系统或秘密存储的单个能力这样功能和服务。更高级的平台还将功能和服务组合成特定场景的体验和模板，适用于 Web 应用程序开发或数据分析和模型训练等关键场景。例如，组织可以提供一个开发人员平台，该平台包含应用程序开发所需的功能，例如计算环境、流水线运行器、数据库系统、消息队列、身份和遥测收集器。另外，组织还可以提供由数据摄取和转换服务、模型训练服务、模型部署管道和模型服务器组成的数据分析平台。

通过为单个功能和/或面向场景的功能集提供一致的体验，平台可以让用户轻松交付有价值的产品。

### 平台能力提供者

正如刚才所描述的，一个平台封装和组合了来自许多支持平台能力提供者的能力和服务。这些提供商可能是企业内的其他团队或第三方，如“云”服务提供商。平台通过使用一致的 Web 门户、文档、代码模板以及可编程 API 和工具来包装这些提供商的能力和服务。通过实现并强制实施期望的安全性、性能和一致体验的实践，平台为底层能力提供者和应用程序开发人员这样的平台用户之间建立了桥梁。

下图说明了产品、平台和能力提供者之间的关系。

![](https://github.com/cncf/tag-app-delivery/raw/platforms-v1alpha1/platforms-whitepaper/v1alpha1/assets/platform_components.png)

[1]: https://www.atlassian.com/devops/frameworks/team-topologies
[2]: https://martinfowler.com/articles/talk-about-platforms.html

## 为什么平台有价值

哪些经济和商业原因促使企业实现平台？平台的价值来自 a) 团队中的专家所专注的共享能力的整合，b) 使这些服务和能力易于在数字产品和应用程序中集成和使用。

采用平台工程的企业有望实现以下目标：

1. 通过有意地设置专门的平台能力团队，从而减少产品团队的认知负担，从而加快产品开发和交付
2. 依靠专门的专家配置和管理的平台能力，提高依赖于此能力的产品的可靠性和弹性
3. 通过在企业中的多个团队之间重用和共享平台工具和知识来加速产品开发和交付
4. 通过管理平台能力及其周围的用户、工具和流程，降低产品和服务中安全、监管和功能问题的风险
5. 通过代理公有云和其他提供商的能力，实现更好的成本效益和效率的利用这些代理商，同时在保证用户体验的情况下保持控制能力

这些好处的产生部分是因为少量的平台团队为许多产品团队提供服务，从而放大了他们的影响；一部分原因是平台团队整合了通用功能的管理，促进了治理；还有部分原因是平台团队强调用户界面和体验高于一切。

平台专家团队不仅减少了产品团队的共同工作 [1] ，而且还优化了这些产品的平台能力 [2] 。而且由于平台提供了许多能力的模式，相关的能力、知识和工具可以更广泛的传播 [3]，开发人员可以快速为构建在同一基础上的其他团队和产品做出贡献。治理和控制 [4] 也可以嵌入到平台的模式和能力中。最后，由于平台团队聚集了能力提供者并在他们的产品上提供一致的体验，因此他们能够有效地使用公共云和服务提供者 [5] 来实现基础但无差别的能力，如数据库和身份。

满足企业可以使用的基本平台的主要用例包括：

1. 产品和服务的开发者可以自动实施计算、存储、数据库和服务标识等运行时能力，并立刻集成和使用这些能力来运行他们的产品
2. 产品和服务的开发者可以自动实施任务运行器、package registries、部署编排器和可观测性系统等支持服务来构建、验证、运行和观测他们的产品
3. 第三方产品和服务的 Operators 可以自动初始化空间和配套服务来部署和使用这些第三方产品和服务

正如上一节所述，成熟的平台包括面向场景的模板，也迎合更具体的用例。例如，内部开发人员平台包括用于配置完整开发环境的模板，并且可以服务于以下用例：

1. 产品或服务的开发者可以自动请求一个完整的开发环境来支持新功能的迭代研发。这包括相关服务中的空间，例如任务运行器和工件存储、指定团队的成员资格以及连接信息（例如 URL 和 secrets）的发布。
1. 产品或服务的开发人员可以使用特定于场景的代码和配置模板来快速引导、开发和交付新产品和功能
1. 产品或服务的利益相关者可以通过仪表、仪表板和告警观测这些产品和服务中的系统和用户行为

## 平台属性

以下是影响云或开发者平台成功的关键属性。一个平台应该：

1. 像任何产品一样，根据用户的要求进行设计和不断改进
1. 管理许多应用程序团队所需和使用的通用能力
1. 提供一致的界面和体验 - GUI、API 和工具 - 用于请求、管理和观测能力
1. 包括文档和代码模板以简化其能力的使用。高级平台应该为组合场景提供文档和模板。
1. 可自助服务——用户必须能够独立请求和接收功能力和组合
1. 可自动化——用户必须能够对能力请求进行编程
1. 封装能力和服务的实现，同时启用所需的配置和观测
1. 是可选的——用户应该能够使用一些平台功能，但在平台产品之外获得其他功能

存在一个平台来满足许多不同用户 [1,2] 和用例的共同需求。它通过多种类型 [3] 的一致接口满足这些需求，尤其是 HTTP API、Web 门户和命令行工具。例如，所有平台用户都需要能够观察他们的工作负载，因此平台可能会提供从应用程序收集和显示日志、指标和跟踪的功能。它可能使用户能够通过 API 和网页请求和使用该功能。

为了能够使用平台的能力，用户需要文档和示例 [4]。因此，平台团队不仅需要提供可观测性等功能，还需要发布模板和文档以帮助用户使用它。例如，平台团队可能会发布可重用的工作流，用于在 Kubernetes 上构建、测试、部署和验证 Web 应用程序。除了单一能力的示例之外，高级平台还应该分组绑定针对特定场景对模板和指南集合，这种捆绑通常被描述为黄金路径。

平台提供的功能应该按需提供给用户[5]，而人工干预最少。上面讨论的接口——API 和网页——应该能让用户在几分钟内获得他们需要的资源，最多需要一个批准。例如，描述数据库管理服务的网页应包含一个按钮，用于请求数据库并在请求后的几分钟内共享该数据库的定位器和凭据。

平台的目的之一是减少产品团队的认知负担，因此平台提供的服务不需要由消费者操作；平台提供商或其代表（例如云服务）应处理这些操作，从而向用户隐藏复杂性 [7]。例如，用户可能经常需要消息队列，但不必管理消息代理。

平台旨在提高产品开发的效率，因此当最有效的途径是不使用平台的能力时，平台不成为障碍是很重要的 [8]。平台应使产品团队能够在必要时提供和管理自己的能力。例如，如果平台团队不提供图形数据库，但产品需要它，那么该产品团队应该可以自己配置和操作图形数据库。

## 平台团队的属性

平台团队负责平台功能的接口和体验，例如 Web 门户、自定义 API 和黄金路径模板。一方面，平台团队与那些实现基础设施和支持能力的团队合作，以定义一致的体验；另一方面，他们与产品和用户团队合作收集反馈并确保这些体验符合要求。

以下是平台团队应负责的工作：

1. 调研平台用户需求
1. 管理和开发功能和服务的接口 - 门户、API、文档和模板、CLI
1. 营销、传播和倡导平台使用

最重要的是，平台团队必须了解平台用户 [1] 的需求，以了解并不断改进其平台提供的功能和界面。了解用户需求的方法包括用户访谈、交互式黑客马拉松、问题跟踪器和调查问卷，以及通过可观测性工具直接观测使用情况。例如，平台团队可以发布一个表单供用户提交功能请求；定期举行路线图会议，分享即将推出的功能并收集反馈。

平台团队不一定运行计算、网络、存储或其他服务。相反，他们拥有界面 [2]（GUI、CLI、API）和这些服务的用户体验。例如，一个门户网站页面可能会描述甚至提供一个按钮来为应用程序提供身份；而该能力的实现可能是通过云托管的身份服务。平台团队拥有网页和面向用户的 API，但不一定拥有实现。

早些时候有人说平台应该被视为产品。具体而言，该平台应根据用户需求不断改进并可选择使用（参见：平台属性 #1 和 #8）。研究和设计是产品交付的一方面，另一方面是营销和宣传 [3]。如果平台真正是根据用户需求构建的，人们应该会很高兴使用所提供的功能。平台团队可以通过内部营销活动来帮助采用的一些方法，包括发布部门范围内的公告、分享引人入胜的演示以及在正常办公时间欢迎提问。这里的关键是在用户所在的地方与他们会面，并让他们踏上与平台互动并从中受益的旅程。

### 启用平台团队

平台团队在支持许多产品团队的工作中很容易超负荷。减轻平台团队负担的方法包括：

1. 在合理的情况下使用托管服务提供商的实现
1. 使用开源框架和工具包创建供应用程序团队使用的文档、模板和组合
1. 确保平台团队配备适合其领域和客户数量的人员

## 平台挑战

虽然平台承诺了很多价值，但它们也带来了如下挑战，实施者应牢记这些挑战。

1. 平台团队必须像对待产品一样对待他们的平台，并与用户一起开发它们
1. 平台团队必须谨慎选择他们的优先级和初始合作伙伴应用程序团队
1. 平台团队必须寻求企业领导层的支持并展示对价值流的影响

也许最重要的是认识到平台的成功直接取决于其用户和产品的成功；因此，平台团队与应用程序团队和其他用户合作，对平台的能力和用户体验进行优先级排序、规划、实施和迭代至关重要。平台团队在没有反馈的情况下发布能力和体验，或者依靠自上而下的授权来实现采用，几乎肯定会遭到用户的抵制和不满，并错过很多承诺的价值。为了解决这个问题，平台团队应该从一开始就包括产品经理来分享路线图、收集反馈并普遍理解和代表平台用户的需求。

采用平台时的另一个挑战是首先选择正确的能力和体验。经常需要且未区分的能力，如流水线、数据库和可观测性，可能是一个很好的起点。平台团队也可以选择首先关注数量有限的敬业且熟练的应用程序团队。来自此类团队的详细反馈改善了首次平台体验；来自这些团队的人帮助支持该平台并将其传播给后来的采用者。

最后，在大型企业中，快速获得领导层对平台团队的支持至关重要。许多企业领导者将 IT 基础设施视为与其主要价值流完全脱节的支出，并可能试图限制分配给 IT 平台的成本和资源，从而导致实施不力、承诺无法兑现和挫败感。为了缓解这种情况，平台团队需要证明他们对产品和价值流团队的直接影响和关系（见前两段），将平台团队展示为产品团队的战略合作伙伴，为客户提供价值。

## 如何衡量平台的成功

定义了平台是什么以及它们打算提供的价值之后，让我们考虑如何衡量一个平台是否提供了这些价值。值得注意的是，平台的成功与部署在其上的产品的成功直接相关，而这又在很大程度上取决于用户对该平台的体验。

平台的首要价值是改进产品交付，因此平台成功指标应该反映这一点。谷歌建议的 DevOps 研究和评估 (DORA) 指标提供了一个基线，包括：

- 更新部署的频率
- 引入变更的准备时间
- 新引入变更的失败率
- 从失败的变更中恢复的平均时间

而且由于平台的成功还取决于其用户，因此平台还应该衡量用户的体验，包括：

- 新贡献者提交他们的第一个（或第 10 个！）PR 的时间到了
- 来自用户的贡献数量，例如 Backstage 插件、Crossplane compositions
- 偏离“黄金路径”和已提供能力的项目数量
- 与平台能力相关的工单数量
- 开发人员在企业中的满意度
  - 净推荐值 (NPS)
  - 空间框架：https://queue.acm.org/detail.cfm?id=3454124

## 平台能力

定义了平台和平台团队的关键属性后，以下是典型数字项目所需的功能，应考虑将其包含在平台中。

此列表的目的是指导平台团队确定应包含在其平台中的内容。

1. 用于配置和观测功能的 Web 门户
1. 用于按需自动配置功能的 API（和 CLI）
1. “黄金路径”模板和文档可实现功能的最佳使用
1. 构建和测试服务和产品的自动化
1. 交付和验证服务和产品的自动化
1. 支持产品研发的服务：托管IDE、远程连接工具
1. 用于实现服务和产品可观测性的仪器和仪表板
1. 基础设施服务：计算运行时、可编程网络、块存储
1. 数据服务：数据库、缓存、对象存储
1. 消息服务：代理、队列、事件结构
1. 身份和 secret 管理服务：服务和用户身份和授权、证书和密钥颁发、静态 secret 存储
1. 安全服务：代码和工件的静态分析、运行时分析、策略实施
1. 工件存储：容器镜像和特定语言的包管理、自定义二进制文件和库、源代码
1. 会计：跟踪资源和成本


<table>
  <thead>
    <tr><td>能力</td><td>描述</td><td>示例项目</td></tr>
  </thead>
  <tr>
    <td>应用程序开发人员界面和体验（#1、#2、#3）</td>
    <td>文档和代码模板。 API、Web UI 和 CLI。平台提供的所有自助服务体验和能力。</td>
    <td>Backstage (UI), Kubernetes (API, CLI), Kratix (API), Crossplane (API), Operator 框架, Dapr, Cartographer</td>
  </tr>
  <tr>
    <td>构建和测试服务和产品的自动化（#4）</td>
    <td>自动构建和测试数字产品和服务。</td>
    <td>Tekton, Jenkins, Buildpacks, ko, buildah, Carvel, pact, testcontainers, testkube, kuttl</td>
  </tr>
  <tr>
    <td>部署和交付服务和产品的自动化（#5）</td>
    <td>自动化和控制服务和应用程序的交付。例如，金丝雀、蓝/绿、特性开关、部署后验证</td>
    <td>ArgoCD, Flux, keptn, Flagger, OpenFeature, kapp (Carvel), Konveyor</td>
  </tr>
  <tr>
    <td>观测产品和服务（#6）</td>
    <td>使所有基础架构功能和产品工作负载能够发出遥测数据。收集、分析信息并将其发布给产品利益相关者</td>
    <td>OpenTelemetry, Jaeger, Prometheus, Thanos, Fluentd, Grafana</td>
  </tr>
  <tr>
    <td>基础设施服务（#7）</td>
    <td>运行应用程序代码。连接应用程序组件。保存应用程序的数据</td>
    <td>Kubernetes (containers), kubevirt (VMs), Knative (functions), Istio, Envoy, Contour, Cilium, Rook, Longhorn, OpenEBS</td>
  </tr>
  <tr>
    <td>数据服务（#8）</td>
    <td>为应用程序的持久化结构化数据</td>
    <td>TiKV, Vitess, etcd, SchemaHero</td>
  </tr>
  <tr>
    <td>消息服务（#9）</td>
    <td>使应用程序能够相互异步通信</td>
    <td>CloudEvents, NATS, gRPC, Knative (events)</td>
  </tr>
  <tr>
    <td>身份和 secret 服务（#10）</td>
    <td>确保工作负载具有访问和使用已配置资源和服务的定位器和 secret。使服务能够向其他服务安全地标识自己</td>
    <td>Directory, OAuth/OIDC, Hashicorp Vault, Dex, Keycloak, Pinniped, SPIFFE/SPIRE, servicebinding.io, cert-manager, Carvel secretgen</td>
  </tr>
  <tr>
    <td>安全服务（#11）</td>
    <td>观测运行时行为并报告/修复异常。验证构建和工件不包含漏洞。根据企业要求限制平台上的活动；通知和/或补救异常</td>
    <td>Falco, KubeArmor, StackRox, OPA, Kyverno, cloud custodian</td>
  </tr>
  <tr>
    <td>工件存储（#12）</td>
    <td>存储、发布和保护构建的工件以用于生产。缓存和分析第三方工件。存储源代码。</td>
    <td>ArtifactHub, sigstore, Harbor, Dragonfly, OCI</td>
  </tr>
  <tr>
    <td>可扩展性</td>
    <td>向平台添加 API、控制器和门户页面，以使用相同的模式提供新功能。</td>
    <td>Operator 框架</td>
  </tr>
  <tr>
    <td>多租户</td>
    <td>使用一种服务实现支持多个内部团队，同时保持团队彼此隔离。确保团队之间的隔离</td>
    <td>vcluster, Cluster API, Nephio, open-cluster-manager, karmada, kcp</td>
  </tr>
  <tr>
    <td>开发环境和工具</td>
    <td>提供工具来帮助编辑、测试和调试代码</td>
    <td>devfile, Tilt, Skaffold, DevSpaces, Telepresense, Eclipse Che, VS, JetBrains, Eclipse</td>
  </tr>
  <tr>
    <td>会计</td>
    <td>跟踪使用中的资源及其成本</td>
    <td>OpenCost</td>
</table>

## 术语

也可以参考 <https://glossary.cncf.io/> 。

一个**平台**聚合了为开发者和运营商提供产品、服务和应用程序开发和交付的能力。参考其旨在支持的场景，平台可能被命名为“开发者平台”、“交付平台”、“应用程序平台”甚至“云平台”。旧术语“平台即服务”或 PaaS 的含义也很有影响力。

**平台**通过提供和管理通用功能，使开发人员和运营商能够更快地交付应用程序和服务。平台是平台用户和平台能力提供者之间的桥梁。

**平台用户**包括但不限于应用程序开发人员和运营人员、数据科学家、COTS 软件运营人员和信息工作者——任何在平台上运行软件或使用平台提供的功能的人。

**平台能力提供者**实现基础设施服务，通常作为控制者和运营者。

**平台开发人员**设计接口和工具，以在应用程序中提供和集成平台能力。

**平台产品经理**负责了解平台用户的体验，并制定解决平台产品差距和机遇的路线图。

## 参考

- https://slack.engineering/mobile-developer-experience-at-slack/
- https://platformengineering.org/talks-library/netflix-platform-console-to-unify-engineering-experience
- https://platformengineering.org/blog/product-management-for-internal-developer-platforms
- https://humanitec.com/whitepapers/state-of-platform-engineering-report-volume-1
- https://www.gartner.com/en/articles/what-is-platform-engineering
- https://thenewstack.io/platform-engineering-infrastructure-meets-dev-experience/
- https://netflixtechblog.com/full-cycle-developers-at-netflix-a08c31f83249
- https://thenewstack.io/vmware-targets-the-platform-engineer/
- https://platformcon.com/
- https://medium.com/@michael.roy.galloway/your-platform-org-needs-a-purpose-heres-how-to-find-it-64874b082d80
- https://www.infoq.com/news/2022/10/platform-devops-summary/
- https://salaboy.com/2022/09/29/the-challenges-of-platform-building-on-top-of-kubernetes-1-4/
- https://engineering.atspotify.com/2020/08/how-we-improved-developer-productivity-for-our-devops-teams/
- https://cloud.redhat.com/blog/designing-golden-paths
- https://blog.container-solutions.com/how-to-design-an-internal-developer-platform
- https://www.honeycomb.io/blog/future-ops-platform-engineering
- https://www.getambassador.io/resources/rise-of-cloud-native-engineering-organizations/
- https://blog.getambassador.io/the-developer-experience-and-the-role-of-the-sre-are-changing-heres-how-6003a12571c4
- https://www.infoworld.com/article/3639050/complexity-is-killing-software-developers.html
- https://www.xenonstack.com/insights/internal-developer-platform
- https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem
- https://backstage.spotify.com/blog/measuring-backstage-success-at-spotify/
- https://martinfowler.com/articles/talk-about-platforms.html
- https://www.infoq.com/articles/platform-engineering-roadmap/
- https://github.com/adobe-platform/Adobe-Workshop-ArgoCon2022/blob/main/IDP-Capabilities.md
- https://humanitec.com/blog/top-10-fallacies-in-platform-engineering
- https://thenewstack.io/platform-engineering-challenges-and-solutions/
- https://www.cloudknit.io/blog/platform-engineering
- https://www.cloudknit.io/blog/platform-engineering-challenges-and-solutions
- https://blog.getambassador.io/top-8-mistakes-made-by-platform-engineers-d892c7448684
- https://www.hashicorp.com/resources/non-technical-challenges-of-platform-engineering
- https://www.gartner.com/en/documents/4010078
- https://reprints2.forrester.com/#/assets/2/108/RES176392/report