<!--
# 极适CDE：SaaS和自托管之间的Gitpod
https://cdn.thenewstack.io/media/2023/09/ab3ec9e3-goldilocks-1024x680.jpg

图片来源:Unsplash。
 -->

云开发环境供应商Gitpod表示，它也提供了一个“自托管”的CDE，但与Coder.com不同，它不是“自我管理”的。

译自 [The Goldilocks CDE: Gitpod Fits Between SaaS and Self-Hosted](https://thenewstack.io/the-goldilocks-cde-gitpod-fits-between-saas-and-self-hosted/) 。

CDE代表“云开发环境”，目前是开发者关注的一个热门产品类别。到目前为止，人们普遍认为CDE主要有两种类型：SaaS模式和所谓的“自主托管”模式，其中CDE托管在客户的云环境内。

但是，根据[Gitpod](https://www.gitpod.io/)公司的说法，存在第三种方式：“专用”，它被定义为自主托管但不是自我管理。本文与Gitpod首席产品官[Mike Brevoort](https://www.linkedin.com/in/mikebrevoort/)和市场主管[Talia Moyal](https://www.linkedin.com/in/taliamoyal/)进行了交谈，以了解Gitpod与GitHub Codespaces(SaaS)和 Coder.com (自主托管)的区别。

Brevoort简要介绍了Gitpod的起源。原始产品是一款名为Theia的IDE，其灵感来自Jupyter实验室。Theia后来被移交给Eclipse基金会，而Gitpod则转型为一项基于VS Code的SaaS服务。

Brevoort表示:“Gitpod是第一个fork VS Code并在服务器上运行它的团队。在Codespaces之前，我们就与GitHub团队密切合作，总体而言，核心团队已经在这个项目上工作了大约5年，从构思到现在。”

## Gitpod模式的演变

起初，Gitpod提供了一个面向个人开发者的SaaS模式，但最终由于大公司的需求，他们引入了一个自主托管模式。Brevoort表示，自主托管版本被广泛采用，但他们担心它会给客户带来运营管理负担。这促使他们提供了所谓的“混合服务”，称为Gitpod专用，这是托管在客户的云帐户中，但由Gitpod管理。

Brevoort说：“所以它结合了自主托管和SaaS的最大优点。它运行在您的云账户中，满足您的安全要求，连接要求。它由我们管理，不是由您管理。我们维护它，每天改进它。我们大规模地管理它，因为这是我们的业务。”

Gitpod仍提供其最初的SaaS版本Gitpod云，Brevoort说这适合较小的公司和开源开发者。

Moyal补充说，其竞争对手Coder实际上是自主托管和自我管理，客户必须做这两项工作。而使用Gitpod，客户只需要做托管部分，Gitpod负责CDE的管理。

![](https://cdn.thenewstack.io/media/2023/09/1c0928ac-gitpod-scaled.webp)

*浏览器中运行的 VS Code，Gitpod 提供的图片*

本文指出，在与Coder的讨论中，安全是其企业客户希望自行管理CDE的主要原因。对于某些公司(如医疗服务提供商)来说，自主管理CDE将是必不可少的，以便完全控制安全性。

Brevoort反驳说，与Coder一样，Gitpod也以大型企业和高安全需求为目标。他表示，Gitpod始终确保满足大型企业的安全、合规和连接需求。他补充，Gitpod的自主托管版本有助于提高开发效率和生产力，因为Gitpod会处理所有运营工作。

Brevoort说：“每个人都在跟我们讨论如何提高开发者效率、增强开发速度、从团队中获得更多输出。这对于AI编程助手和Copilot等工具是非常重要的，CDE也在其中发挥重要作用，因为它可以尽可能快地让开发者准备好编码，减少设置环境、运行配置等所需时间。现在每个人都高度关注如何提升开发者效率。”

Brevoort进一步表示，Gitpod的专用服务正在大幅增长，其中还为有严格安全和数据管理需求的客户提供服务。他说，专用现在占收入增长的90%以上。许多客户本来更倾向于SaaS解决方案的便捷性，但由于特定的运营和安全需求，尤其是数据分类和软件供应链安全，他们选择了专用服务。

关于企业中谁负责选择专用，Brevoort表示：“这通常由对提升开发者生产力感兴趣的人来驱动，或者是安全团队。” 无论是谁选择CDE，他们通常需要其他部门从安全和合规性方面进行批准，专用满足这些要求。

## CDE 还处于早期采用市场，但情况在改变

尽管Gitpod、Coder、GitHub Codespaces等CDE产品之间存在激烈竞争，且不断有新进入者如Daytona，但对于企业内外的开发者来说，CDE仍然是一个相对较新的现象。Brevoort承认："目前采用CDE的公司仍是少数。"

他表示：“我们看到许多硅谷和湾区创业公司以不同方式采用了它们，其中许多构建了自己的版本。我们与其中一些合作，它们通常更具前瞻性，特别是那些拥有大型代码库的公司。我认为这是让行业其他公司也采用这些实践的机会。”

当被问到是否SaaS公司如GitHub会在CDE上向自主托管转变时，Brevoort回应，虽然他无法代表GitHub，但他注意到Codespaces已经与Azure云计算环境互联互通。

他说：“我认为GitHub和微软有很大动力让您在Azure上运行这些工作负载，所以我确定他们会继续促进其更容易在私有环境中实现，但显然我无法代表他们。”

就CDE作为一个市场类别来看，Brevoort认为未来几年它们会变得更主流。

“我认为它将变得非常主流；可能会更简单地被采用。现在，我们仍在讨论如何启动和运行它，是否必须自主托管，可以连接到什么，以及它如何改变软件开发方式等问题。但我认为这将成为正常的开发方式。”

## LLM 将会来到 CDE

他补充说，拥有开发者工作的中心化云服务，也就是CDE的本质，会促进其他新工具的出现。“因为有一个更一致的集中地来运行开发流程，可以做更多有趣的集成。”

这些集成中肯定会有许多与AI产品相关的。Brevoort建议，CDE将是开发者体验大型语言模型(LLM)的完美场所。

“当人们谈论LLM时，他们可能会将LLM带到数据所在的位置，而不是相反。因此，如果云中有中心化的开发环境，LLM就会被引入这些环境中。”
