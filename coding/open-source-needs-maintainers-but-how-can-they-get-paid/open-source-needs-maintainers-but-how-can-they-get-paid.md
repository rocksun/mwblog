---
title: 开源需要维护者，但是他们如何获得报酬？
cover: https://cdn.thenewstack.io/media/2021/06/bd0d012a-opensource-1024x576.jpg
---

世界运行在很大程度上由一支无偿爱好者军团维护的代码之上。这种方式不可持续。谁在试图改变这种状况呢？

译自 [Open Source Needs Maintainers. But How Can They Get Paid?](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/)

[Jordan Harband](https://www.linkedin.com/in/ljharb/) 是科技行业所依赖的那类人：开源软件项目的维护者。

他维护了大量这样的项目 —— 根据他的统计，大约有 400 个。

Harband 曾在 Airbnb、Twitter 等公司工作，目前是 Coinbase 被裁员一年多的自由职业者，为 OpenJS 基金会担任安全工程师。

他也从 Tidelift 和其他赞助商那里获得报酬，以完成他估计每周 10 到 20 小时的开源维护工作。

他的工作对全球开发者的日常生产力至关重要。总计下来，他告诉 The New Stack，他[维护的一些项目](https://www.npmjs.com/~ljharb)负责 [npm](https://www.npmjs.com/) 下载流量的 5% 到 10%。

但是，他说，如果不“破坏我的生活、家庭、福利和生活方式”，就不可能把全部时间都花在开源项目上。

情况说明：他在 Coinbase 的 COBRA 健康保险福利将在年底终止。“如果我找不到全职工作，我就得自己购买医疗保险，”他说，“当然，这不该是任何人生命中的压力，更不应该是为那么多公司和经济体创造经济价值的任何人的压力。”

Harband 是他工作的许多项目的唯一维护者。他并非唯一身处这种情况的开发者。他说，过度依赖大批无偿爱好者是危险和不可持续的。

“我们生活在资本主义中，确保任何事情完成的唯一方法是资本或规章制度——胡萝卜或大棒，”他说。 “挑战在于，公司依赖的工作在资本或法规上没有激励。如果他们运送糟糕或不安全的软件，没有人会被追责，市场力量除外。”

而且，Harband 补充说：“对使用开源软件的公司——[基本上是所有公司](https://thenewstack.io/3-ways-to-drive-open-source-software-maturity/)——存在履行受托责任的缺失，因为投资在基础设施上是它们的受托责任。开源软件是每个人的基础设施，严重缺乏投资。”

## “巴士（Bus）因素”和“老板（Boss）因素”

世界对开源软件以及维护它的人的依赖度毋庸置疑。例如，Synopsys 2023 年开源安全报告审计了跨 17 个行业的 1700 多个代码库，发现：

- 96% 的代码库包含开源软件。
- 代码库中的代码有 76% 是开源的。
- 91% 的代码库包含在过去两年内没有开发者活动的开源软件 —— 报告暗示，这可能表明一个开源项目完全没有人维护。

本十年以来，有许多尝试为开源安全制定标准的行动：[拜登政府的行政命令](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)、[欧盟](https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/informatics/open-source-software-strategy_en)的新规定，以及 [Open Source Security Foundation(OpenSSF)](https://thenewstack.io/inside-a-150-million-plan-for-open-source-software-security/) 的成立和其[安全计分卡](https://github.com/ossf/scorecard?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)的发布。

2022 年 2 月，美国国家标准与技术研究所(NIST)发布了其更新的[安全软件开发框架](https://csrc.nist.gov/Projects/ssdf?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)，为开发者提供安全指南。

但是数据显示，开源维护者通常不了解当前的安全工具和标准，如软件清单(SBOM)和软件工件供应链安全等级(SLSA)，而且他们在很大程度上无偿工作，且令人恐惧地孤立无援。

Tidelift 5 月发布的一项研究发现，60% 的开源维护者将自己描述为“无偿爱好者”。 所有维护者中有 44% 说自己是项目的唯一维护者。

Tidelift 首席执行官兼联合创始人 Donald Fischer 对 The New Stack 说:“比起单人维护的项目，零维护者项目更令人担忧，而这类项目也有相当多，并被广泛使用。” “因为许多组织甚至没有遥测，没有数据或能见度，所以他们对此无知。”

在 Tidelift 的调查中，36% 的维护者说他们考虑过放弃自己的项目；22% 说他们已经这样做了。

这让人想起可怕的“巴士因素” —— 如果项目的唯一维护者被巴士撞倒，项目会发生什么？(有时这也被称为“[卡车因素](https://thenewstack.io/what-happens-when-developers-leave-their-open-source-projects/)”。但假设的悲惨结果是一样的。)

Fischer 说，比“巴士因素”更大的对维护工作连续性的威胁是“老板因素”。

他说，“老板因素”出现在“某人找到新工作，所以他们不再有那么多时间专注于开源项目了，他们会让这些项目被弃置不管”。

在开源社区，继任是一个棘手的问题。据 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline-mention) 7 月发布的一份报告，研究人员访问了前 200 大关键开源项目中的 32 名维护者，仅[有 35% 的人说他们的项目有强大的新贡献者流水线](https://www.linuxfoundation.org/research/open-source-maintainers?hsLang=en)。

[Valeri Karpov](https://www.linkedin.com/in/valeri-karpov-64b48138/) 已经获得 Tidelift 的支持，在过去五年中担任 [Mongoose](https://github.com/Automattic/mongoose) 的首席维护者，这是 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline-mention) 的对象建模器。这位迈阿密居民告诉 The New Stack，他每月在该项目上花费大约 60 个小时。

他在 2014 年担任 MongoDB 软件工程师时继承了首席维护者的角色。该项目以前的维护者决定不再继续维护它。如今，一名为 Karpov 的应用开发公司工作的初级开发者以及三名志愿者为 Mongoose 做出了贡献。

对于一个像他这样获得支持的首席维护者来说，他说，除了免费工作之外，还有其他挑战。首先是找到时间跟上项目生态系统的变化。

以 Mongoose 为例。该工具有助于使用 MongoDB 构建 Node.js 应用程序。  Karpov 说:“自从我开始处理 Mongoose 以来，JavaScript发生了很大变化， Node.js 也是如此。当我第一次开始使用 Mongoose 时，(JavaScript)[Promise](https://thenewstack.io/what-are-promises-in-javascript/) [甚至还不是语言的核心部分。TypeScript](https://thenewstack.io/typescript/) 存在，但还是无足轻重的东西。各种事物都发生了变化。”

如果你的项目走红了会怎么样？ Karpov 说，你会花越来越多的时间提供用户支持和响应 pull 请求：“我们每天收到几十个 GitHub 问题，跟上进度需要适应。”

## 维护者如何获得报酬

为那支建立和维护开源代码的庞大爱好者军团付费——补偿他们维护代码、招募新贡献者、制定继任计划以及学习最新语言和安全知识所花费的时间和精力——这似乎符合全球经济的最大利益。

但是，融资格局仍然参差不齐。获得财务支持的主要途径包括:

**开源计划办公室(OSPO)**。没有人确切知道有多少组织[维持某种 OSPO](https://thenewstack.io/how-an-ospo-can-help-your-engineers-give-back-to-open-source/) 或其他内部支持，为他们对开源软件做出贡献的开发者和工程师提供支持。

然而，来自 Linux 基金会研究的的数据显示，公共部门和教育机构采用 OSPO 的比例在增加，据该基金会高级副总裁 Hilary Carter 介绍。

据 GitHub 2022 年 Octoverse 关于开源软件状况的报告，[大约 30% 的财富 100 强公司维持 OSPO](https://octoverse.github.com/)。通常，企业只支持直接与雇主核心业务相关的开源工作。

为什么更多公司不支持开源工作？Carter 在通过电子邮件回答 The New Stack 的问题时说：“许多组织，特别是科技行业之外的组织，通常不完全理解拥有 OSPO 的优势，或开源使用的战略价值，或者开源贡献的好处。”

“他们的关注可能是短期的，或者可能担心知识产权和许可问题。根据开发者所在的行业，像金融服务等高度监管行业的政策通常禁止任何形式的开源贡献，即使是对其组织正在积极使用的项目。教育和宣传对改变这些看法至关重要。”

GitHub 社区副总裁 [Stormy Peters](https://www.linkedin.com/in/stormy/) 表示，许多公司对 OSPO 的益处仍然一无所知。

“OSPO 可以帮助软件开发者、采购人员和法律团队了解如何选择开源许可证，或者非技术人员如何吸引当地社区参与工具的设计和开发，”Peters 在通过电子邮件回答 The New Stack 问题时写道。

“OSPO 营造了一种文化转变，走向更加开放、透明和负责任的方法来构建技术工具，以确保可持续性。”

**基金会**。有时为开源项目设立的基金会会为该项目的维护者提供财务支持。例如，[Rust 基金会](https://foundation.rust-lang.org/)为该流行编程语言的[维护者提供资助](https://foundation.rust-lang.org/grants/)。

然而，Harband 指出，这种方法有其局限性。 “基金会对项目的一个巨大利好是它们提供那种继任路径，”他说。 “但私人基金会不可能支持每个项目。”

2019 年，[Linux 基金会推出了 CommunityBridge 项目](https://thenewstack.io/linux-foundation-unveils-communitybridge-an-open-source-funding-platform/)，旨在帮助开源维护者找到资金。该基金会承诺，对组织贡献者的匹配最高可达 50 万美元的累计总额; GitHub 作为初始支持者捐赠了 10 万美元。

但 CommunityBridge 已经发展成为 [LFX 众筹](https://lfx.linuxfoundation.org/tools/crowdfunding/)，这是该基金会为[开源项目设立的协作门户的一部分](https://lfx.linuxfoundation.org/)。“项目获得 100% 的捐款并自行管理资金，这些资金可以支持导师计划、活动或其他可持续性需求，” Carter 在给 TNS 的电子邮件中写道。

Carter 还指出了 OpenSSF 的 [Alpha-Omega](https://openssf.org/community/alpha-omega/) 项目。该项目于 2022 年 2 月启动，支持发现和修复关键开源项目中的安全漏洞的[维护者](https://thenewstack.io/alpha-omega-dishes-out-cash-to-secure-open-source-projects/)。例如，6 月，该项目宣布它已资助 [Python 软件基金会](https://www.python.org/psf-landing/)招聘[一名为期一年的新安全开发者](https://openssf.org/blog/2023/06/22/psf-welcomes-new-security-developer-in-residence-with-support-from-alpha-omega/)。

Carter 在电子邮件中写道：“Alpha-Omega 创建了一个途径，让关键的开源项目获得财务支持，并改善软件供应链的安全性。”她敦促有计划的组织或能提供资金的组织与 OpenSSF(这是一个 Linux 基金会项目)取得联系。

**赚钱平台**。 Tidelift 是 [oss.fund](https://www.oss.fund/) 列出的平台之一，后者是一个众包和精心策划的开源维护者可以获得财务支持的来源[目录](https://github.com/oss-fund/monetization-platforms)。 

Fischer 的组织支付人们“执行这些重要但有时繁琐的任务”，他说。 “我们成功吸引了新的维护者来处理项目，无论是主维护者不想做这些事情的项目，还是在某些罕见情况下，由于与其他人达成的雇佣协议而被禁止这样做的项目。”

这种工作的报酬各不相同，取决于诸如开源项目的规模和使用广泛程度等变量。 “我们平台上报酬最高的维护者现在的美国收入已经超过六位数，”Fischer 告诉 The New Stack。 “这很好，因为这基本上意味着独立的开源维护现在是一个职业。”

最高规格的赚钱平台之一是 [GitHub Sponsors](https://thenewstack.io/github-sees-open-source-organizational-donations-spike/)，它于 2019 年以测试版推出，并于今年 4 月对组织赞助开源工作者正式上线。 截至 4 月，GitHub 报告说，Sponsors 已为维护者筹集了超过 3300 万美元。

2022 年，GitHub 报告说，该计划的赞助资金中近 40% 来自组织，包括亚马逊网络服务、美国运通、梅赛德斯-奔驰和 Shopify。 2023 年，它增加了一种工具，以帮助赞助商一次支持多个开源项目。

GitHub 社区副总裁 Peters 表示，批量支持功能和其他升级的引入帮助 GitHub 赞助商看到过去一年支持开源项目的组织数量翻了一番。 3500 多家组织通过 GitHub 赞助支持维护者。

“长久以来，开发者不得不在职业和开源热情之间做出选择 —— 他们被付费做什么与他们真正喜爱的东西，” Peters 写道。 “开源开发者应该以他们正在加速世界的速度加速自己的职业生涯。”

Carter 告诉 TNS，LFX 众筹与 GitHub 赞助集成。 她提供了一些帮助用户建立联系的指导：“社区成员可以通过编辑存储库的 .github 文件夹中的 Funding.yml 文件来[添加和配置赞助按钮](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)，位于默认分支上。”

“任何方便项目找到所需支持的机制都很重要，我们很高兴为现有和新项目促成融资渠道，”她写道。

## 开源作为职业增长的催化剂

Peters 指出，GitHub 确定了一个新兴趋势：开发者通过为开源项目做贡献来学习编程和开始职业生涯。 公司最近启动的两个项目旨在帮助更多这类开源新贡献者获得支持。

11 月，GitHub 推出了 [GitHub 基金](https://github.blog/2022-11-09-an-open-source-economy-built-by-developers-for-developers/)，这是一个由微软的  M12支持的 1000 万美元种子基金。 该基金支持了 [CodeSee](https://thenewstack.io/codesee-helps-developers-understand-the-codebase/)(映射存储库) 和 [Novu](https://thenewstack.io/novu-tackles-notification-infrastructure-management/)(开源通知基础设施)。

“自 GitHub 投资 [CodeSee](https://thenewstack.io/a-lifelong-maker-tackles-a-developer-onboarding-problem/) 以来，该公司已经在平台中添加了生成式 AI，允许开发者用自然语言提出对代码库的问题，”Peters 写道。

4月，GitHub 启动了 [Accelerator](https://github.blog/2023-04-12-github-accelerator-our-first-cohort-and-whats-next/)，这是一个为期 10 周的计划，开源维护者获得 2 万美元的赞助来开展项目工作；此外，他们还获得指导和研讨会。 Peters 说，该项目收到来自 20 多个国家/地区的维护者的 1000 份申请；第一批参与者包括 32 人。

参与者包括 Mockoon (桌面 API 模拟应用程序)等项目。

Poly(一个用于工程生物学的 Go 包)；以及 Strawberry GraphQL(一个用于创建 GraphQL API 的 Python 库)。

翻译:

Peters 写道，直接投资对 Accelerator 参与者来说是一个“改变游戏规则”的举措。“我们发现，对于想全职进行开源维护的人来说，现有的支持很少，而针对这些人建立项目产生了不成比例的影响。”

她还补充说，这为未来融资奠定了基础：“根据专家的建议，人们构建了可持续发展的路径——无论是自力更生、风险资本融资、拨款、企业赞助还是其他。”

Karpov 为想支持员工开源项目工作的公司提出了一个想法：在常见的学习预算之外，为工程师提供“开源预算”。

他指出：“通常使用这些(开源)项目的开发人员完全没有预算。他们什么也买不了——而且坦白地说，他们经常甚至不知道该问谁购买这类东西。”

例如，开源预算可以用于 [GitHub 赞助](https://thenewstack.io/github-sees-open-source-organizational-donations-spike/)等。Karpov 说，作为赞助一个开源维护者的回报，也许“你可以直接与他们沟通，像‘嘿，你能回答这个问题吗？’这可以让这些大公司的开发者更有生产力。”
