开源一直以来都受到社区理想与商业现实之间张力的影响。过去一周凸显了这两种力量之间依然存在的显著差异。

一方面，活动家和开源倡导者[发布了一封公开信](https://keepandroidopen.org/open-letter/)，反对Google计划要求所有Android应用开发者直接向公司注册，才能在Google Play商店之外分发应用。签署者认为，这一要求实际上将平台上谁可以发布软件的控制权集中起来——甚至超出了Google自己的应用市场。

“我们敦促Google撤回此政策，并与开源和安全社区合作，寻找限制性更小的替代方案，”签署者写道。

另一方面，Meta正式宣布将React纳入[Linux Foundation旗下的一个专门基金会](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-react-foundation)的计划，将法律管理权从单一公司所有者手中转移出去——尽管大部分行政转移仍在进行中。

这两项发展的核心都是控制权问题：谁拥有它，它是如何构建的，以及当一个由供应商主导的开源项目成为现代软件构建和分发的基础时会发生什么。

## React的崛起

![React基金会标志](https://cdn.thenewstack.io/media/2026/03/9fc5938c-reactfoundation-300x169.webp)

React基金会标志

最初为自己的产品内部开发，Meta（当时的Facebook）于2013年[将React开源](https://engineering.fb.com/2013/12/20/web/2013-a-year-of-open-source-at-facebook/)，并迅速成为创建现代网络应用的主导工具之一。在过去十年中，React已成为前端生态系统的基础层，数百万开发者和无数公司依赖于它。

但其由供应商主导的治理长期以来引发了关于这种规模的项目是否应继续由单一公司管理的问题。因此，在2025年10月，[Meta宣布计划](https://thenewstack.io/new-react-foundation-to-manage-framework/)将React、[React Native](https://reactnative.dev/)及相关技术剥离，成立全新的[React基金会](https://react.foundation/)，由Linux Foundation赞助。长期担任React负责人[Seth Webster](https://www.linkedin.com/in/swebster)被任命为执行董事。

当时，[Webster告诉*The New Stack*](https://thenewstack.io/react-foundation-leader-on-whats-next-for-the-framework)说，React“已成为网络构建和运行方式中不可或缺的一部分……它的重要性已超过一个团队所能承担的维护责任。”

然而，他也承认社区的一部分有时感到被边缘化——这暗示了过去的争议点，例如[2017年的许可争议](https://www.theregister.com/2017/08/21/facebook_apache_openbsd_plus_license_dispute/)，当时React的BSD + 专利许可证及其专利终止条款引发了持续的批评。例如，Apache Software Foundation[禁止React](https://www.theregister.com/2017/07/17/apache_says_no_to_facebook_code_libraries/)在其Apache项目中使用，之后Meta[最终将该项目重新许可](https://engineering.fb.com/2017/09/22/web/relicensing-react-jest-flow-and-immutable-js/)为MIT许可证。

Webster还指出，React这样规模的项目会伴随着更普遍的推拉效应，其中重大的架构转变和治理问题可能会让一些开发者感到不被重视。

“我们做了很多事情，疏远了社区的一部分，并导致人们转向竞争性框架等，”[他去年10月告诉*The New Stack*](https://thenewstack.io/react-foundation-leader-on-whats-next-for-the-framework)。“这是创新如此成功的一个重要部分，有这种压力，所以我很高兴看到这一点。但是，我也想尽我们所能，确保每个人都感到自己受欢迎、被倾听，并像他们应该的那样成为React社区的一部分。”

## 那么，究竟有什么变化？

React基金会由一系列企业巨头组成。除Meta之外，初始成员还包括Amazon、Microsoft、Huawei、Vercel、Expo、Callstack和Software Mansion——这是一个由云提供商、框架供应商和React生态系统专家组成的组合。

但中立性，至少在早期阶段，伴随着显著的警示。Webster在担任React基金会新职务的同时，仍然是Meta的员工。这种安排在开源基金会中并不罕见，但这突显出机构的重心并未突然从Meta转移开来。

根据*The New Stack*去年的报道，Meta还将在基金会公司治理委员会中保持在头两年半的绝对多数席位，这意味着它将在基金会的形成阶段保留重大影响力。

> 中立性，至少在早期阶段，伴随着显著的警示。

[Deb Bryant](https://www.linkedin.com/in/opengovernment/)，Open Source Initiative (OSI) 的临时执行董事兼前Eclipse Foundation董事会成员表示，基金会转型很少会导致即时的技术变革。

根据Bryant的经验，那些转向中立治理结构的项目，尤其是当它们已经达到显著规模和采用程度时，往往会延续其现有的路线图和核心贡献者。

“通常保持不变的是近期技术路线图以及对项目成功至关重要的核心技术贡献者的参与，”Bryant告诉*The New Stack*。“项目当前状态下的某种临界规模和兴趣水平让单一供应商相信之前的投入将继续增长；中期方向的潜在变化通常被理解为将项目转移到中立治理结构的最终决定的一部分。”

对于开发者而言，这种转变可能意味着更清晰的责任划分。业务监督转移到董事会；技术方向仍由那些编写和审查代码的人负责。

“参与转移到中立基金会的项目的开发者……受益于其治理中业务与技术的分离，”Bryant说。“商业领导层和对非技术性事务——法律、资金、营销、社区活动等——的投资得到解决，而开发者则能够专注于共同推动技术路线图和发布代码。”

简而言之，治理处理管理开销；工程师处理工程。Bryant还指出，由基金会支持的项目通常会随着时间吸引更广泛的贡献者群体，并重新激发其活力。

“技术社区的快速增长带来了挑战，但新成员的涌入提供了新的友谊、专业成长和指导机会，”Bryant说。“这使得社区更加健康、更可持续，并拥有更强大的后备力量，这预示着项目的良好未来。”

## 坚实的基础

事实上，对于许多开发者而言，项目治理可能根本不会出现在他们的关注范围之内——除非出了问题。在开源领域，新的基金会往往是在紧张局势已经爆发之后才出现的。[JP Caparas](https://jpcaparas.com/)，软件工程师兼[*Sulat*时事通讯](https://sulat.com/)的作者，认为React的转型之所以引人注目，恰恰因为它没有遵循这种模式。

“React没有经历过治理危机，”Caparas[写道](https://sulat.com/p/react-just-left-meta)。“没有人因为对Meta的管理感到沮丧而分叉React。此举是预防性的，而非反应性的，这可以说是更明智的做法。最好在需要桥梁之前就把它建好。”

> 对于许多开发者而言，项目治理可能根本不会出现在他们的关注范围之内——除非出了问题。

Kubernetes常被视为基金会历史上主要的成功案例之一。它最初由Google创建，[很早就捐赠给](https://www.cncf.io/blog/2018/03/06/kubernetes-first-cncf-project-graduate/)Cloud Native Computing Foundation，在那里它发展了一个广泛的、多供应商的贡献者基础。Caparas认为，一旦该项目不再被视为属于单一竞争对手，Microsoft和Amazon等竞争公司就更愿意投入工程资源——这一转变有助于加速Kubernetes在整个行业的增长和合法性。

“中立性为企业所有权永远无法实现的采用打开了大门——这是从Kubernetes中学到的最大教训，”Caparas说。

Node.js走向中立基金会的道路并不平坦。2014年末，对Joyent治理项目的不满促使开发者[将Node.js分叉为一个竞争项目](https://www.infoq.com/news/2014/12/iojs/)，名为io.js，迫使了一场清算，最终[导致了Node.js基金会的成立](https://nodejs.org/en/blog/announcements/foundation-v4-announce)。

这些例子表明，基金会地位可以根据时机发挥不同的作用。在Kubernetes的案例中，中立性帮助其早期实现了增长和竞争对手的投资。在Node.js的案例中，它是在分裂之后作为一种修复机制出现的。

> React没有经历过真正的治理危机，也没有面临迫使Meta出手的强制性分叉。但它也不再是一个寻求合法性的新兴项目。

React介于这些先例之间。它没有经历过真正的治理危机，也没有面临迫使Meta出手的强制性分叉。但它也不再是一个寻求合法性的新兴项目——它已在整个行业中根深蒂固。然而，对于Caparas来说，最终决定一个基金会是否能提供有意义的独立性，在于那些实际做出贡献的人。

“区分成功与失败的模式非常具体，”Caparas[认为](https://www.linkedin.com/in/jpcaparas/recent-activity/all/)。“重要的不是谁坐在董事会里，而是谁雇佣了核心维护者。”

在React的案例中，Meta仍然雇佣着大部分核心团队，基金会的执行董事直接来自Meta的React组织。Caparas指出，Kubernetes在加入CNCF后，花了几年时间才真正实现了贡献者雇佣的多样化。

“React应该为同样的（时间）规划，社区也应该关注这一点，”Caparas说。

因此，这次转型的实际影响将取决于未来几年React的贡献者基础是否能在Meta之外实现多样化。