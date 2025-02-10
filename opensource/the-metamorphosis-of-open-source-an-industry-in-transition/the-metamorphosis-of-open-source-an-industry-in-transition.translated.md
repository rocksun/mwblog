# 开源的蜕变：转型中的行业
![Featued image for: The Metamorphosis of Open Source: An Industry in Transition](https://cdn.thenewstack.io/media/2025/02/96724193-pawel-czerwinski-hu6kulsi5dm-unsplash-1024x683.jpg)

[Pawel Czerwinski](https://unsplash.com/@pawel_czerwinski?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/blue-and-pink-painting-Hu6kULsI5dM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

二十年前，声明你的项目是“开源”是一种原则、哲学和社区的声明。今天，它更可能是一种商业决策、一种营销策略或一种人才获取工具。这种转变不是开源的失败，而是其成功的标志。

数字不会说谎：[GitHub’s 2024 Octoverse report](https://github.blog/news-insights/octoverse/octoverse-2024/#the-state-of-open-source) 发现，今年开发者为开源和公共存储库贡献了近 10 亿次，比以往任何时候都有更多的开发者在使用开源软件包，并且首次贡献者的数量持续增长。

根据许多调查和报告，包括 [contributions from the OSI](https://opensource.org/blog/announcing-the-2024-state-of-open-source-report)，我们有理由确信，全球超过 90% 的公司都在使用开源，甚至在他们的代码库中至少有一个开源组件。而且这些数字还在增长。

开源赢了。

## 从革命到惯例

[open source movement](https://thenewstack.io/open-source-movement-emerging-in-ai-to-counter-greed/) 最初是对自由软件意识形态的一种务实的回应。虽然 [Free Software Foundation](https://www.fsf.org/) 强调道德上的必要性 (*“promote computer user freedom”*)，但开源侧重于实际利益：无限的协作、无需许可的创新和更广泛的采用。这种战略转变效果非常好。[Open source became the default choice for infrastructure software](https://thenewstack.io/is-community-backed-open-source-software-worth-the-risk/)、开发者工具和关键业务应用程序。

但成功带来了挑战。

## 云改变了一切

当开源最初概念化时，软件通常在本地运行。云计算的兴起从根本上改变了这种局面。突然，修改和重新分发代码的能力变得不如大规模运行和操作它的能力重要。

Elastic 的历程是这种转变的一个典型例子。到 2019 年，亚马逊的 Elasticsearch 服务的收入超过了 Elastic 本身，尽管 Elastic 是 Elasticsearch 代码库的主要维护者。这导致了一场 [well-known conflict](https://www.nytimes.com/2019/12/15/technology/amazon-aws-cloud-competition.html)：在 Elastic 更改其许可后，亚马逊分叉了 Elasticsearch，创建了 OpenSearch。这个案例例证了云提供商和 [single-vendor open source projects](https://opensource.net/why-single-vendor-is-the-new-proprietary/) 之间的斗争，从而引发了关于云时代开源商业模式可持续性的根本问题。

这并不是 [open source companies sought to protect their interests from cloud](https://thenewstack.io/what-do-cloud-native-and-kubernetes-even-mean/) 提供商的第一次。在此之前，新的许可方法正在涌现。MariaDB 在 2016 年创建了 [Business Source License (BSL)](https://mariadb.com/bsl-faq-adopting/)，开创了一种延时开源转换模型，其中代码在一定时期后（通常在 GPL v2.0 或兼容版本下）完全开源。这种介于专有和 [open source models](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) 之间的中间地带被称为源代码可用，以区别于开源。

类似的担忧促使 MongoDB 在 2018 年创建了 [Server Side Public License (SSPL)](https://opensource.org/blog/the-sspl-is-not-an-open-source-license)，随后 Redis 也更改了许可。这些公司试图解决他们与云提供商之间的挑战。虽然 [not approved by OSI](https://opensource.org/licenses)，但 SSPL 代表了在商业可行性与开源原则之间取得平衡的又一次尝试。

令所有人惊讶的是，Elastic 几个月前 [returned to open source](https://www.elastic.co/blog/elasticsearch-is-open-source-again)，采用了 AGPL 作为 Elasticsearch 的可选许可。这证明了使用开源实现 SaaS 业务是可能的。

## 企业的影响

企业开源格局发生了巨大的变化。最初谨慎的参与已经演变为战略投资和领导。考虑以下事实：

- Google’s
Kubernetes 已成为容器编排的事实标准，拥有来自数百家公司的数千名贡献者。

- Meta 的 React/Vercel 的 Next.js 主导了前端开发，被数百万开发人员使用，并为数百万个网站提供支持。
- Microsoft 的 VS Code 凭借其[开源核心](https://thenewstack.io/the-future-of-open-source-or-why-open-core-is-dead/)赢得了重要的市场份额。
- Intel、Red Hat、Oracle、Google 和其他大型公司雇佣了[大多数 Linux 内核开发人员](https://kernelnewbies.org/DevelopmentStatistics)。
- Google 的 Chrome 团队推动了 V8（为 Node.js 提供支持的 JavaScript 引擎）的开发。
- Microsoft 和 Google 是 GitHub 上开源项目的[最重要贡献者](https://opensourceindex.io/)。

开源治理从根本上来说是基于基金会的。Linux 基金会[托管了 800 多个项目](https://www.linuxfoundation.org/resources/case-studies)，每年有数百万美元的资金；Eclipse 基金会[托管了 400 多个项目](https://projects.eclipse.org/)；目前有[296 个项目和其他计划](https://projects.apache.org/)由 Apache 软件基金会管理；更不用说由 [Python 软件基金会](https://www.python.org/psf-landing/)、[OpenInfra 基金会](https://openinfra.dev/)、[OpenJS 基金会](https://openjsf.org/)等托管或支持的数十个项目，以及 [Cloud Native Computing Foundation](https://www.cncf.io/) 也管理着数百万美元的资金，并组织开源领域中最大的会议。同样，像 Google、Microsoft 和 Amazon 这样的大公司共同向[开源基金会](https://thenewstack.io/nivenly-foundation-seeks-equity-for-open-source-maintainers/)贡献数亿美元。

这种公司的参与为许多项目带来了前所未有的资源和稳定性，但也改变了生态系统中的权力动态。决策通常是在公司董事会会议室中做出的，而不是在社区论坛中。虽然这使项目管理更加专业化并[改善了安全实践](https://openssf.org/)，但也引发了人们对开源开发独立性的担忧。

公司的参与也带来了重大挑战。Oracle 收购 Sun Microsystems 引发了人们对 Java 和 MySQL 未来的担忧，最终导致其创建者 Michael “Monty” Widenius 发起 [MariaDB 作为一个社区分支](https://mariadb.org/en/)。Docker 在货币化方面的挣扎导致了[其企业业务的出售](https://thenewstack.io/mirantis-acquires-docker-enterprise/)以及 Docker Hub 定价模式的巨大变化。最近，HashiCorp [从 Terraform 切换到 BSL](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/) 导致了 OpenTofu 的创建，突显了公司决策如何分裂社区。

尽管存在这些挑战，但公司的参与对于[开源可持续性](https://thenewstack.io/can-open-source-sustain-itself-without-losing-its-soul/)仍然至关重要。关键是建立平衡公司资源与社区利益的治理模式，正如我们列出的积极例子所证明的那样。

## 寻求可持续资金

开源中的可持续性危机引发了各种资金实验。传统的模式（如公司赞助和捐赠）已被证明对许多项目来说是不够的，从而导致了新的方法：

- GitHub Sponsors 通过直接支持维护者来改变个人资助。著名的成功案例包括 Vue.js 的 [Evan You](https://github.com/sponsors/yyx990803)，他的赞助层级为支持者提供各种好处，以及 [Sindre Sorhus](https://github.com/sponsors/sindresorhus)，通过社区支持维护数百个 npm 包。
- Open Collective 开创了透明的财政托管，为项目管理数百万美元的资金。例如，[webpack](https://opencollective.com/webpack) 已经筹集了超过 150 万美元，目前的余额约为 79,000 美元，所有这些都可以在他们的 Open Collective 页面上透明地跟踪。
- Tidelift 引入了一种[基于订阅的模式](https://tidelift.com/)，组织为跨多个依赖项的维护保证付费。这种方法有助于维持不太知名但至关重要的基础设施项目。

然而，这些模型并不完美。许多关键项目仍在努力获得稳定的资金。[Log4j 事件](https://www.csoonline.com/article/404962/log4j-one-year-later-the-log4shell-vulnerability-still-has-lessons-to-teach.html) 突出表明，即使是广泛使用的项目，尽管对全球基础设施至关重要，也可能资金严重不足并由志愿者维护。
这种资金缺口导致一些项目探索混合模式，结合了：

- 商业服务和支持
- 不同许可下的高级功能
- 与主要用户的开发合同
- 来自科技巨头和基金会的资助计划

寻找既能保持项目独立性，又能确保可持续发展的融资机制具有挑战性。 行业需要新的模式来支持备受瞩目的项目以及更多小型但至关重要的依赖项。

## AI 许可困境
人工智能的兴起为开源对话引入了一个新话题。 与传统软件不同，AI 系统包括代码和模型、数据和训练方法，[creating complexities that existing open source](https://thenewstack.io/how-american-express-created-an-open-source-program-office/) licenses were not designed to address。 认识到这一差距，OSI 于 2024 年推出了 [Open Source AI Definition (OSAID)](https://opensource.org/ai/open-source-ai-definition)，标志着开源原则发展的一个关键时刻。 OSAID v1.0 定义了 AI 系统的基本自由：不受限制地使用、研究、修改和共享 AI 技术的权利。 该框架旨在确保 [AI systems labeled as “open source”](https://thenewstack.io/a-nue-ux-web-framework-plus-anthropic-openai-boost-ai-apis/) 与支撑该运动的透明和协作的核心价值观保持一致。

然而，这一过程并非没有挑战。 OSI 的定义引发了争论，尤其是在 [legal ambiguities of model weights and data licensing](https://thenewstack.io/osis-definition-of-open-source-ai-raises-critical-legal-concerns-for-developers-and-businesses/) 方面。 例如，虽然 OSAID 强调数据来源和方法论的透明度，但它并未解决 [model weights derived from unlicensed data](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/) 是否可以自由共享或用于商业用途。 这使得企业和开发人员处于灰色地带，实际采用开源 AI 模型需要仔细的法律审查。

尽管存在这些挑战，但这项工作强调了开源原则的适应性。 它证明了它们可以不断发展以满足新兴技术的需求，同时保留其核心价值观，就像过去一样。

那么，接下来会发生什么？

开源的转型已经可以通过几个明显的趋势看到：

- Rise of *source-available* licenses and hybrid models, from BSL to Elastic approach.
- Increasing corporate guidance on significant projects, balanced with foundations.
- The ongoing search for sustainable funding, with experiments like GitHub Sponsors or Open Collective.
- AI-driven [development tools](https://thenewstack.io/tiddlywiki-an-open-source-alternative-to-notion-or-obsidian/) and models introduce new questions about the meaning of “open source” itself.

我们正在朝着一种超越传统 [definition of open source](https://thenewstack.io/the-open-source-ai-definition-what-the-critics-say/) 的新模式发展。 我们所看到的故事表明，未来在于利益相关者之间更明确的价值交换。 我们可能会看到更多分层许可系统和混合模式，以平衡商业利益与社区利益。

我还看到需要一种超越捐赠和企业赞助的新融资机制。 首先，企业资助意味着企业参与，直接或间接，这并不能保证 [open source maintainers](https://thenewstack.io/security-needs-create-more-work-for-open-source-maintainers/) 的自由或独立性。 其次，它不能保证长期成功或维护项目所需的财务稳定性。 我们最近目睹了未维护的 OSS 的 [potential disaster](https://www.sonatype.com/blog/cve-2024-3094-the-targeted-backdoor-supply-chain-attack-against-xz-and-liblzma)。

## 进化，而非死亡
这并不意味着我们将要目睹开源的消亡，而是它的进化。 正如开源从 *free software* 中脱颖而出，成为一种更务实的方法一样，新的模式正在出现以应对当今的挑战。 协作、透明和共享创新的原则仍然很有价值。 尽管如此，它们的实施适应了不断变化的技术环境，并且该定义本身甚至可能存在于 [Open Source Initiative](https://thenewstack.io/open-source/) 之外。

我甚至可以说下一个阶段可能不叫“开源”！ 问题不在于这种模式是否会继续存在，而在于它将如何转型以满足不断变化的行业的需求。
对于社区而言，真正的挑战在于确保这种演变在适应新现实的同时，能够保留开源的核心优势。我们需要积极参与塑造这个未来，而不仅仅是变革的观察者。开源的下一篇章将由那些能够成功应对这些挑战，同时坚守使其最初具有革命性的基本价值观的人们书写。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

Tech moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.