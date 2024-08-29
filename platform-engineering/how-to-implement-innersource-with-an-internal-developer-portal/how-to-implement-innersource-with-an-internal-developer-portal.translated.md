# 如何使用内部开发者门户实施 InnerSource

![如何使用内部开发者门户实施 InnerSource 的专题图片](https://cdn.thenewstack.io/media/2024/08/f53a0533-diving-1024x576.jpg)

InnerSource 的核心是加强协作和打破孤岛。这种方法鼓励以开源的方式进行软件开发。这不是一种新做法；事实上，这个词早在 2000 年 12 月就被 O'Reilly Media 的创始人 Tim O'Reilly 首次提出。

尽管它在这个喜欢追逐最新流行语和趋势的行业中是一个比较古老的术语，但它仍然是 [许多工程团队](https://thenewstack.io/monitoring-developer-metrics-team-approach-is-best/) 希望融入其组织的一种 [方法](https://thenewstack.io/monitoring-developer-metrics-team-approach-is-best/)。Gartner 预计，到 2026 年，40% 的软件工程组织将拥有 [InnerSource 计划](https://thenewstack.io/github-bloomberg-talk-using-innersource-build-open-source-project-development-behind-company-firewalls/)。这是因为他们相信这种方法将提高代码可重用性，提高标准化程度，并在开发人员中激发自主和主人翁意识的文化。

最终，InnerSource 的目标是减少开发中的重复工作、缺乏重用以及由此产生的成本增加。然而，企业往往难以在总体战略和战术实施之间进行交接。

虽然没有任何一种工具可以确保开发人员 [采用 InnerSource](https://thenewstack.io/adopting-inner-source-culture-within-organizations/)，但有一些方法可以帮助实施 InnerSource，包括使用内部开发者门户。

以下是可以使用 [内部开发者门户](https://www.getport.io/blog/what-is-an-internal-developer-portal) 帮助在组织内实施和鼓励 InnerSource 的五种主要方法：

## “可信赖的提交者”的重要性

Silona Bonewald 在她的《理解 InnerSource 清单》一书中，将“可信赖的提交者”的角色描述为实施 InnerSource 最佳实践的关键。可信赖的提交者是一名开发人员（通常轮换时间为两周），负责指导其他开发人员，并确保人们在创建新的拉取请求 (PR) 时符合标准。可信赖的提交者通过以下方式领导减少其服务孤岛的工作：

- 维护贡献指南
- 审查传入的拉取请求，以确保它们符合这些指南
- 指导 [不符合贡献指南的开发人员](https://thenewstack.io/building-polyglot-developer-experiences-in-2024/)
- 向那些向其服务提交代码的人寻求帮助。

门户网站创建了一个场所，使可信赖的提交者的工作更容易、更明显、更容易被认可和遵循。

从最基本的意义上说，内部开发者门户可以让可信赖的提交者的存在为人所知，就像可以通过门户推动软件所有权一样。拥有一个门户可以确保每个服务的“可信赖的提交者”都能为人所知并获得奖励，方法是：

- 包含一个自动更新的“可信赖的提交者”时间表。
- 为当前担任此角色的开发人员分配“可信赖的提交者”标签或属性。
- 通过维护一个仪表板（例如，描述在他们监督下合并的 PR 数量或他们对每个 PR 的响应速度）来游戏化每个可信赖的提交者的贡献。

最后，Bonewald 指出，担任可信赖的提交者会占用开发人员编写代码的时间，因此使用门户被动地记录他们的贡献是在年终绩效对话中提供客观绩效指标的绝佳方式。

Bonewald 建议为那些在担任可信赖的提交者方面表现出色的开发人员提供晋升为“研究员”的途径，这可以是在门户网站的用户资料中自豪地展示的标签或属性。

![开发人员可能会发现，查看他们发现的服务的当前可信赖的提交者很有帮助。可信赖的提交者也会发现，使用自动更新的时间表来识别自己很有帮助。](https://cdn.thenewstack.io/media/2024/08/786a11a6-image2.png)

开发人员可能会发现，查看他们发现的服务的当前可信赖的提交者很有帮助。可信赖的提交者也会发现，使用自动更新的时间表来识别自己很有帮助。

## 提高可发现性

这种方法和下一种方法对于那些通过收购而无组织地发展起来的组织尤其重要。无论被收购的公司是成为单一法人实体的一部分还是成为子公司，将其合并到单一源代码管理工具或将所有开发人员添加到所有现有源代码管理工具的行政负担都是一项不可逾越的任务，如果不这样做，InnerSource 的努力往往会在幻灯片中 languish，而不是在开发人员的日常工作中蓬勃发展。
将工具或组织整合的另一种方法是将所有现有存储库集成到一个充当门户基础的 [目录](https://www.getport.io/blog/service-catalog-what-is-it-benefits-components) 中，开发人员可以在其中发现有关所有可用服务的元数据，而默认情况下不会公开源代码。这样做，开发人员无需查看源代码即可了解服务的用途、如何为其做出贡献以及谁是可信赖的提交者。这立即减少了 [服务和 API](https://thenewstack.io/extending-kubernetes-services-with-multi-cluster-services-api/) 的重复。

## 能够向合适的人发送访问请求

一旦开发人员准备好使用门户发现的服务做出贡献或使用该服务，他们就可以使用自助服务操作来请求仅访问相关存储库。通过实施动态审批，此请求可以发送给合适的人员，无论是可信赖的提交者、产品经理还是技术主管。

![可以通过下拉菜单和简短消息来实现对存储库的访问，然后可以将其路由到可信赖的提交者（或最适合处理这些请求的人）。](https://cdn.thenewstack.io/media/2024/08/13988dad-image1.png)

可以通过下拉菜单和简短消息来实现对存储库的访问，然后可以将其路由到可信赖的提交者（或最适合处理这些请求的人）。

## 创建支持内部开源的新服务

[不使用门户的工程组织](https://thenewstack.io/which-features-does-your-platform-engineering-portal-need/) 已经在简化新服务创建方面遇到了困难：开发人员必须为新的存储库、新的管道、新的项目管理工具等提交单独的、相互依赖的票据。将内部开源要求添加到构建新服务的过程中是开发人员在应该（并且想要）编写代码时切换上下文的另一个触发因素。
票据驱动流程的一个受欢迎的替代方案是 [自助服务操作](https://www.getport.io/product/self-service)，它允许开发人员从一开始就轻松满足这些要求。不要指示他们查找、修改和添加内部开源文档要求（`README.md`、`CONTRIBUTING.md`、`GETTINGSTARTED.md` 和 `HELPWANTED.md`），只需要求他们在自助服务表单中从一开始就填写这些要求的最低要求。自动化创建新的存储库、管道和项目管理工具，其他人可以将这些文件写入新的存储库，从而使开发人员能够几乎立即将注意力转移到为新服务编写代码上。

![自动填充此自助服务操作中的模板，以确保开发人员从一开始就提供正确的信息。](https://cdn.thenewstack.io/media/2024/08/53835f57-image4.png)

自动填充此自助服务操作中的模板，以确保开发人员从一开始就提供正确的信息。

## 服务记分卡

上述方法将满足新服务的内部开源要求，但组织往往拥有大量现有服务，必须评估其是否符合内部开源标准。在指示内部开源或 DevOps 团队创建评估所有存储库的存储库扫描程序之前，请考虑在门户中使用自定义 [记分卡](https://www.getport.io/blog/using-scorecards-for-standards-compliance-a-repeatable-framework-and-examples)。记分卡可用于定义、衡量和跟踪内部开发人员门户中每个服务或实体的相关指标。在这种情况下，记分卡可以帮助建立指标来评估内部开源标准的合规性，这将帮助经理或团队负责人了解现有服务中的差距，然后推动有时限的计划来填补这些差距。

![在构建存储库扫描程序以检查内部开源标准之前，请考虑改用记分卡。](https://cdn.thenewstack.io/media/2024/08/3d5259fc-image3.png)

在构建存储库扫描程序以检查内部开源标准之前，请考虑改用记分卡。

## 结论

通过实施门户并特意将其配置为服务于内部开源目的，工程负责人可以在其组织中享受内部开源的优势。开发人员同样也会享受到增强的可发现性和轻松构建新的支持内部开源的服务并快速找到合适的人员来支持他们的贡献的优势。

[YOUTUBE.COM/THENEWSTACK
技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等内容。](https://youtube.com/thenewstack?sub_confirmation=1)