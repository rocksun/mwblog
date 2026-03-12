代理式AI开发公司 [Tetrate](https://tetrate.io/) 推出了 [Built on Envoy](https://builtonenvoy.io/)，一个免费且开源的Envoy扩展市场。

Envoy 是一个用于云原生应用的开源边缘和服务代理。Envoy 的起源可追溯到 [网约车服务Lyft](https://thenewstack.io/lyfts-envoy-provides-move-monolith-soa/)，其服务代理能力使其能够充当中间服务器，管理服务之间的网络流量以增强安全性。

被 [Envoy项目团队](http://envoy) 描述为“微服务的通用数据平面”，Envoy 与每个应用程序并行运行，通过以平台无关的方式提供通用功能来抽象其网络服务。

该公司表示，它现在提供了一种克服拖慢团队的部署陷阱的方法；它已将这些最佳实践流程打包成即用型扩展，并免费向社区中的所有人提供。

但是，什么可能让Envoy变得麻烦呢？

## 为何Envoy是“扫兴小子”？

采用Envoy的常见障碍包括安全和认证难题，例如 [Web应用防火墙 (WAF)](https://thenewstack.io/waf-securing-applications-at-the-edge/) 集成、OAuth2令牌交换、安全断言标记语言 (SAML) 问题以及更广泛的授权工作流细微差别。

对于任何软件工程师来说，WAF集成很少是即插即用的任务，当开发人员使用它将安全规则应用于其代码，以阻止某些数据但仍允许合法用户流量通过时，集成会变得复杂；这一切都很好，但当开发人员的代码库发生变化时，WAF规则也需要更新——而代码库显然会发生变化。SAML在属性映射时可能会遇到挑战，例如一个软件系统以与另一个系统不同的格式标记一个常见的实体（如电子邮件），导致声明缺失错误。你明白了，加密握手并非总是顺畅无阻。

其他Built on Envoy市场扩展旨在处理AI治理要求，例如根据 [Azure内容安全](https://thenewstack.io/microsoft-adopts-openinfra-kata-containers-security-on-azure/)（一种用于检测和过滤有害文本和图像内容的AI服务）检查LLM请求和缓存模型请求，以及操作需求，包括数据平台的代理配置和路由区域固定。

文件服务器扩展服务完善了此处提供的最初一批市场产品。这项技术允许团队直接从Envoy提供静态资产，如HTML页面、仪表板和文档，而无需部署单独的Web服务器。

Built on Envoy 包含一个CLI包管理器，允许开发人员使用简单命令在其本地机器上运行带有扩展的Envoy，从而减少实验、原型设计和迭代所需的时间。

## 定制扩展的顾虑

Tetrate 旨在通过提醒我们Envoy的先进功能传统上只有拥有深厚专业知识的团队才能使用来验证其在新产品上的工作。该公司表示，许多软件工程团队最终都在闭门造车地构建定制扩展，重复劳动并错失分享其成果的机会。

基于以上情况，为开发人员提供一个下载和部署经过验证的扩展的开源市场显得恰逢其时。Envoy的创建者 Matt Klein 表示他对整个项目感到兴奋。

Klein 说：“到目前为止，为Envoy编写扩展一直是一个费力的过程，需要编写C++并编译整个代理的完全自定义构建。动态模块的兴起以及允许使用Go或Rust进行扩展将极大地释放Envoy的扩展性，让更多人受益。”

> “太多的团队在独立解决相同的问题。Built on Envoy 为社区提供了一个公开分享这些解决方案的方式，以便每个Envoy用户都能更快地行动。”

## 等等，我们以前不是遇到过吗？

Tetrate 提供了一份 [详细的演练](https://tetr8.io/builtonenvoy)，介绍了可用的扩展及其用例。公司CTO Varun Talwar 表示，他的团队多年来一直在看到企业客户大规模部署Envoy，因此他一次又一次地看到了相同的挑战。

Talwar 说：“太多的团队在独立解决相同的问题。Built on Envoy 为社区提供了一个公开分享这些解决方案的方式，以便每个Envoy用户都能更快地行动。我们为生态系统构建了它，并邀请所有人来使用并回馈。”

如今，Envoy 每天处理数百万次机器学习预测。该代理的安全性通过参与 [Google漏洞奖励计划](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/google_vrp) 得到了加强。今天，Netflix 每天处理数十亿次API请求，而 Airbnb 每秒处理超过100万个用户事件，这两个组织都依赖Envoy进行关键任务流量管理。

## 社区精神，免费使用

Built on Envoy 在 Apache 2.0 开源许可下发布，可免费使用。Tetrate 已经播种了这个市场，但长期愿景是一个由社区维持的生态系统，在这个生态系统中，各行各业的组织分享他们所构建的成果，并共同加速Envoy的采用。