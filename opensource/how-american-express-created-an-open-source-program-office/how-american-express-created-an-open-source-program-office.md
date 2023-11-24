<!--
title:美国运通：建立开源项目管理体系
cover: https://cdn.thenewstack.io/media/2023/11/928a20e8-gamification-1024x768.png
-->

美国运通成立开源程序办公室，将开源代码开发转化为一种有趣的游戏，既确保代码安全，也为社区提供代码贡献。

> 译自 [How American Express Created an Open Source Program Office](https://thenewstack.io/how-american-express-created-an-open-source-program-office/)，作者 Agam Shah 已经报道企业 IT 超过 10 年。除了机器学习、硬件和芯片，他也对武术和俄罗斯感兴趣。

金融公司正在向 IT 环境注入大量[开源软件](https://thenewstack.io/scaling-open-source-community-by-getting-closer-to-users/)，以慢慢减少对专有软件的依赖。

[开源采用](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/)在过去三年特别增加，因为公司完成了软件依赖性映射和审计流程以最小化软件风险。

与云原生公司相比，银行和投资公司无法那么容易地投入开源，因为该行业受到高度监管，控制很严格。

根据 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline-mention)运营的 Fintech 开源基金会上个月发布的一项调查，约 78% 的金融公司从开源软件中获取价值，而去年这一比例为 62%。

FINOS 在调查中断言：“对于金融服务实体来说，开源为减少 IT 基础设施成本、加快数字应用发布速度以及在人才吸引和保留方面保持竞争优势提供了途径。”

## 开源程序办公室

开源软件的影响力大到足以让金融服务公司建立[开源程序办公室](https://thenewstack.io/operationalize-the-enterprise-developer-part-3-ospo-3-0/)(也称为 [OSPO](https://thenewstack.io/how-an-ospo-can-help-your-engineers-give-back-to-open-source/))，专门用于平稳过渡到开源。

开源程序办公室负责人 [Gabriele Columbro](https://www.linkedin.com/in/columbro/) 说：“我们看到，现在有超过 50% 的受访者所在的组织都有一个开源程序办公室，这表明开源程序办公室正在兴起。” 他是在上个月在纽约市举行的[金融业开源论坛](https://events.linuxfoundation.org/open-source-finance-forum-new-york/)(OSFF) 会议上说这番话的。

这些办公室负责创建结构化流程以使用和贡献开源。Columbro 说，贡献政策正在变得更加宽松。

![](https://cdn.thenewstack.io/media/2023/11/01a60d67-amexospoimage-1024x598.jpg)

## 美国运通 OSPO

[美国运通](https://www.americanexpress.com/en-us/company/?inav=us_footer_about_about_american_express)建立了一个开源程序办公室，将安全开发开源代码进行游戏化处理，这些代码可以反馈到社区中。

AmEx 软件工程师 [Amanda Chesin](https://www.linkedin.com/in/amandachesin/) 在 OSFF 的演讲中说：“如果没有这个计划的存在，公司里的许多人都不会知道回馈开源，他们不会看到其中蕴含的力量。”

AmEx OSPO 最初是一个开发者的非正式组，试图与开源社区建立互惠关系，会议上的 AmEx 开发体验副总裁 [Tim Klever](https://www.linkedin.com/in/tim-klever-5820b56/) 说。

第一步是说服对开源价值持怀疑态度的高层管理人员。根据 FINOS 对受访高管的调查，安全问题是 56% 的高管最关注的问题。其次是组件质量、遵守外部法规以及知识产权许可。

围绕开源的开发者热情也在加剧，Klever 说服管理层批准了 OSPO。Klever 让实习生 Chesin 来设置和运行这个办公室，她立即开始了工作。

“那真的是我们成为官方的时刻，因为我们有人整天担心和处理这些事情，尽管我们只找到她一个夏天，”Klever 说。

像“我们在这里做开源”这样的说法可以成为吸引顶级人才的重要动机，这也是说服管理层创建 OSPO 的卖点之一。开源贡献和在发行说明中被提及可以帮助开发者建立信誉。

Klever 说：“像‘看哪，我正在做所有这些伟大的事情来造福自己’这样的想法并不符合我们对我们正在寻找的定义。我们谈论的是回馈第三方，回馈支持我们的人。”

启动 OSPO 面临许多挑战。该团队不得不在 AmEx 的行列中识别出可以为开源做贡献的开发者，并确保为他们提供贡献资源和时间。

Chesin 说:“像获得法律措辞、知识产权等东西......然后让员工以某种方式看到他们正在做出的贡献，这就是我们的最小可行产品。”

Klever 和 Chesin 通过一个内部网站使 OSPO 实现了游戏化，该网站维护一个开发者对存储库做出贡献数量的积分榜。

Chesin 说:“我们在内部网站上创建了项目和所有者页面，以向人们展示人们正在贡献的项目。我们......建立了这个社交平台，作为连接的方式。”

AmEx 利用开源[良好首次问题](https://github.com/topics/good-first-issue)项目欢迎 AmEx 的新开源贡献者。该开源项目指导开发者进行首次贡献。

AmEx 从 Github API 中提取数据，快速显示易于开发者贡献的项目，贡献形式可以是文档或增强。

还有视觉化表示，以便开发人员知道其他 AmEx 开发人员的工作重点。

Chesin 说:“我们有一个所有项目表，您可以看到同事最近的贡献，人们一直在贡献什么，以及公司其他人投入时间和精力的地方。”

2020 年，AmEx 管理层开始正式资助[开源项目办公室](https://thenewstack.io/how-one-open-source-project-derived-from-anothers-limits/)。2020 年 12 月，OSPO 实现了为 100 名“社会责任”贡献者制定的目标。

Klever 将“社会责任”贡献解释为提出问题或拉取请求，确保项目不受公司所有或维护，并以某种方式授权项目，这样可以在公司内部使用，而且通过贡献来加强项目。

Klever 说:“我们不仅仅是一个反馈回路，只是贡献给我们自己的项目。我们实际上是在回馈其他人，成为我们社区的良好管家，结交新朋友。”

OSPO 还有“开源日”，高管们会给予开发者从常规工作中休息的时间来贡献开源。

AmEx 现在每天大约贡献 6 次，并且在 2022 年 11 月成为 FINOS 的成员，FINOS 已成为金融机构的开源技术协会。

根据 FINOS 的调查，Capital One 有一个更加严肃的 OSPO，它侧重于流程、安全性、合规性和隐私性。

Capital One 开源程序办公室主任 Nureen D'Souza 说：“这包括在摄入开源软件之前对我们所有库的自动扫描。”

该公司记录了复杂的软件工具矩阵。这可以确保只使用活跃和定期更新的开源工具，因为被抛弃的项目可能会在 IT 环境中创建注入恶意代码的空白。

D'Souza 说：“例如，我们试图了解每个项目周围的社区运行状况——谁在背后支持以及有什么样的支持？”

Capital One OSPO 还评估开源工具的许可和法律方面。
