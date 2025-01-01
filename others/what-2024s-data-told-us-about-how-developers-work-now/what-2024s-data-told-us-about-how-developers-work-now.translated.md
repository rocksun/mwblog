# 2024 年数据告诉我们开发者现在的工作方式

![Featued image for: What 2024’s Data Told Us About How Developers Work Now](https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png)

2024 年，《The New Stack》报道了大量基于调查的软件开发研究。以下是我们认为在您规划 2025 年时最相关的要点。

## 平台工程和开发者平台

- 平台工程师专注于基础设施供应，由于所管理平台的多样性，这可能是个问题。
- 即使自助服务提高了开发团队的生产力，但过多的平台团队未能收集和展示成功指标。

## 开源

- 付费维护者使代码更安全。
- 维护者担心来自 AI 和未知开发者的贡献。

## AI 和开发者

- 开发者使用 AI 的原因是节省时间和提高生产力，而不是代码质量。
- 在年轻、经验不足的开发者的带领下，AI 工具已迅速被用于开发流程中。

[GitHub Copilot](https://thenewstack.io/a-developer-health-check-on-github-copilot-and-ai-assistants/)并未实现大规模采用。

## 招聘和职业

- 基于开发者普遍的焦虑，个人工作保障比预期的要强。
- 开发者的薪资和工资受到限制。

## 编程语言

12 月 28 日 [Darryl K. Taft](https://thenewstack.io/author/darryl-taft/) 的文章“[2024 年编程语言大战：Python 领先，Java 保持稳定，Rust 崛起](https://thenewstack.io/language-wars-2024-python-leads-java-maintains-rust-rises/)” 对今年的调查结果进行了很好的总结。与许多其他出版物不同，《The New Stack》对 2024 年收集的原始数据进行了独立分析，这些数据来自 [Stack Overflow](https://stackoverflow.com/) 的“[开发者调查](https://thenewstack.io/salary-pressures-not-ai-vex-developers-says-stack-overflow/)” 和 [Jetbrains](https://www.jetbrains.com/) 的“[开发者生态系统报告](https://thenewstack.io/developers-testing-more-jetbrains-study-finds/)”。

## 其他值得注意的发现

- 并非所有公司都离开云端。
- 面向客户的事件正在增加。

## 平台工程和开发者平台

虽然不像 [DevOps](https://roadmap.sh/devops) 那样是合成词，但[平台工程](https://thenewstack.io/platform-engineering/) 已成为开发和运维目标融合的学科。

在 2024 年，我们报道了超过四份基于调查的报告，这些报告提供了对平台工程和内部开发者平台 (IDP) 的见解。他们证明，绝大多数企业已经采用了平台工程，即使他们可能没有一个正式的团队使用这个名称。

标准化基础设施供应和 IDP 的使用是 68% 平台团队的主要关注点。根据最新版本的 Gitpod 和 [Humanitec](https://humanitec.com/?utm_content=inline+mention) 的“平台工程现状报告”，改进开发者在 IDP 上的体验和生产力紧随其后作为重点。

首次采用平台的公司绝大多数都获得了积极的投资回报，但许多[平台团队不知道如何衡量成功](https://thenewstack.io/the-2024-state-of-platform-engineering-fledgling-at-best/)。根据同一份“平台工程现状”研究，只有 43% 的平台团队将自己的反馈机制描述为“临时性”或“不一致”。

更糟糕的是，45% 的平台团队根本不进行任何衡量，而另外 26% 的团队正在收集性能数据，但实际上并没有对其进行分析。

即使在关注生产力的组织中，关于如何衡量平台团队成功的标准仍然存在争议。事实上，[谷歌云](https://cloud.google.com/?utm_content=inline+mention) 发布的最新 DORA 报告发现，[随着平台工程项目成熟度的提高，吞吐量和变更稳定性指标下降](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/)。另一方面，使用 IDP 的组织看到个人和团队生产力水平更高，这可能是由于通过 IDP 提供的自助服务。

展望未来，我们预计组织将面临有多少平台才算太多的问题。这个问题即将出现，因为在 [Puppet by Perforce](https://puppet.com/?utm_content=inline+mention) 的“2024 年 DevOps 现状报告”中接受调查的 75% 的人表示他们正在使用至少三个内部自助服务平台，这比[先前研究中使用三个或更多平台的 59%](https://thenewstack.io/platform-engineering-more-teams-now-running-3-or-more-idps/)要多得多。
随着平台工程在企业中获得至少基本的认可，投入到其中的资源应该会增加。[Rafay Systems](https://rafay.co?utm_content=inline+mention)的一项调查发现，69%拥有平台团队的组织预计，到2024年，这些团队的员工人数将至少增加25%。然而，Rafay报告指出，企业面临的一个挑战是，[只有47%的平台团队拥有独立于IT部门的预算](https://thenewstack.io/are-shared-platforms-too-restrictive-a-new-report-says-yes/)。

平台工程或许会转移一部分原本用于购买[基础设施即代码 (IaC)](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/)和CI/CD工具的资金。事实上，如[上图](#datawrapper-chart-25a6c)所示，许多平台团队都专注于实施IaC或在CI/CD系统之上构建平台。

平台团队或许能够在不同的环境中强制执行一致的配置，但由于IaC工具和框架的激增，他们也面临着挑战。事实上，[StackGen](https://stackgen.com/?utm_content=inline+mention)的“[Stacked Up 2024: The IaC Maturity Report](https://stackgen.com/2024-stacked-up-the-iac-maturity-report-stackgen)”调查显示，54%的受访者在IaC方面面临挑战，因为多种工具导致学习曲线陡峭且兼容性问题突出。确定[可以有效管理多少个IaC框架](https://thenewstack.io/terraform-and-the-tooling-multiverse-in-the-future-of-iac/)将在2025年继续成为一个问题。

### Kubernetes和平台工程
在CI/CD系统之上运行的平台通常也运行在Kubernetes之上，这就是为什么Rafay Systems对平台团队的调查侧重于Kubernetes用户。这两个主题都面临着由于工具激增而带来的复杂性问题。

事实上，根据[Spectro Cloud](https://www.spectrocloud.com/?utm_content=inline+mention) 2024年的一项调查，48%的Kubernetes用户发现，[很难决定从广泛的云原生生态系统中选择哪些堆栈组件](https://thenewstack.io/kubernetes-48-of-users-struggle-with-tool-choice/)。这一比例从Spectro Cloud 2023年报告中的29%大幅上升。

### 2024年最佳平台工程报告
- “[平台工程现状报告：第三卷](https://platformengineering.org/state-of-platform-engineering-vol-3)” [VMware by Broadcom's](https://tanzu.vmware.com?utm_content=inline+mention)“[2024年云原生应用平台现状](https://go-vmware.broadcom.com/2024-State-of-Cloud-Native-App-Platforms)”
- DORA的“[加速DevOps现状](https://dora.dev/research/2024/dora-report/)”
- Puppet by Perforce的“[2024年DevOps现状报告：平台工程的演变](https://www.puppet.com/blog/state-devops-report-2024)”
- Rafay的“[企业平台团队的脉搏：云、Kubernetes和AI](https://rafay.co/the-pulse-of-the-enterprise-platform-team-cloud-kubernetes-and-ai/)”
- Spectro Cloud的“[2024年生产Kubernetes现状](https://info.spectrocloud.com/2024-state-of-production-kubernetes)”

## 开源
开源维护者的资金，或资金的缺乏，继续危及开源软件。

2024年出现了大量的软件物料清单 (SBOM) 和自动化依赖项管理的工具，这些工具可以降低一些安全问题。然而，开源维护者根本没有足够的时间来优先考虑安全问题，尤其是在他们还面临着人工智能编码工具带来的大量新威胁的情况下。

主要发现包括：

[通过支付维护者的费用可以最好地解决安全需求](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/)。为其在开源方面的工作获得报酬的开发人员，遵循影响项目安全态势的最佳实践的可能性要高出50%以上。这是根据[Tidelift](https://tidelift.com/?utm_content=inline+mention)的“[开源维护者现状](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/)”得出的结论，该报告还考察了来自未知贡献者和人工智能生成的拉取请求的质量和安全问题。- 维护者担心来自AI和未知开发者的贡献。Tidelift报告发现，由于3月份发现的[Linux xz utils后门](https://thenewstack.io/linux-xz-and-the-great-flaws-in-open-source/)，三分之二的维护者比以前更不信任来自项目非维护者的拉取请求。更令人担忧的是，64%的人表示，他们不太可能审查和接受他们知道是用人工智能工具创建的项目贡献。

在2025年，我们预计无偿志愿者将继续难以遵循许多实践，而这些实践正日益成为遵守新的政府法规的强制性要求。
### 其他值得关注的开源研究
- OpenLogic 的“[2024 开源现状报告](https://www.openlogic.com/resources/state-of-open-source-report)”
- Linux 基金会的“[自由和开源软件普查三](https://www.linuxfoundation.org/research/census-iii)”

## AI 和开发者
**开发者使用 AI 的原因是节省时间和提高生产力，而不是代码质量。**
- 在定期使用 AI 工具进行编码和其他开发相关活动的开发者中，85% 的人表示这些类型的工具使他们比以前更快地完成工作。这是根据 Jetbrains 的“[开发者生态系统现状报告](https://www.jetbrains.com/lp/devecosystem-2024/)”得出的。大部分时间节省是渐进的，但 46% 的人表示，由于这些工具，他们每周至少节省了两个小时。相比之下，只有 23% 的人表示这些工具实际上提高了所创建代码和解决方案的质量。这一发现应该会降低 2024 年 GitHub 调查“[2024 GitHub 调查](https://github.blog/news-insights/research/survey-ai-wave-grows/)”报告的乐观情绪，该调查发现 90% 的美国开发者声称使用 AI 编码工具提高了他们的代码质量。总体而言，Jetbrains 的研究发现，65% 的人表示他们超过一半的工作时间用于编码，高于 2023 年的 57%。在即将到来的一年里，我们希望看到这一趋势是否会持续下去，并能否直接与 AI 编码工具的使用联系起来。

**在年轻、经验不足的开发者的带领下，AI 工具已被迅速应用于开发流程中。**
- 根据[Stack Overflow 的“2024 开发者调查](https://survey.stackoverflow.co/2024/)”，年轻的开发者、经验较少的开发者以及居住在印度和巴西等国家的开发者更有可能使用和信任 AI。71% 的经验少于五年的开发者报告在他们的开发过程中使用了 AI 工具，而拥有 20 年编码经验的开发者则为 49%。

**GitHub Copilot 没有实现大规模采用。**
- 在过去 12 个月中，41% 的受访者使用了 GitHub Copilot，低于 2023 年在“Stack Overflow 开发者调查”中询问相同问题时的 55%。我们认为这种下降是基于对 Copilot 产品的看法变化。
- 根据 Jetbrains 的“[开发者生态系统现状报告](https://www.jetbrains.com/lp/devecosystem-2024/)”，只有 26% 的开发者定期使用 GitHub Copilot 进行编码和其他开发活动，尽管另外 14% 的开发者之前曾尝试使用过它。相比之下，定期使用 ChatGPT 进行编码的开发者为 49%，而之前尝试过使用它的开发者为 20%。

## 招聘和职业
**个人工作保障比基于开发者普遍焦虑所预期的要强。**
- 根据 Jetbrains 的“[2024 开发者生态系统现状报告](https://www.jetbrains.com/lp/devecosystem-2024/)”，总体而言，67% 的受访者感觉他们在目前的工作中很安全，而 11% 的受访者表示感到不安全。在同一项研究中，46% 的人表示他们所在城市或地区的软件开发者当前就业市场充满挑战，而 30% 的人表示招聘前景良好。

根据 Linux 基金会的一份报告，[大多数雇主在 2023 年增加了工作岗位或维持现状](https://thenewstack.io/tech-hiring-most-employers-added-jobs-or-kept-the-status-quo-in-2023/)。

**开发人员的薪资和工资受到限制。**
- [Stack Overflow 的“2024 开发者调查](https://survey.stackoverflow.co/2024/)”的受访者中，[平均年薪大幅下降](https://thenewstack.io/salary-pressures-not-ai-vex-developers-says-stack-overflow/)。例如，与去年相比，2024 年全栈开发人员的平均中位数薪资下降了 11%，降至 63,333 美元。即使平均或平均薪资实际上并没有下降，[ADP 的研究也表明开发人员的薪资并没有](https://www.adpresearch.com/the-rise-and-fall-of-the-software-developer/)像许多其他职业那样大幅增长。

### 其他值得关注的技术工作和职业研究
- Linux 基金会的“[2024 年科技人才现状报告](https://www.linuxfoundation.org/research/open-source-jobs-report-2024?hsLang=en)”
- Dice 的“[2024 年科技薪资满意度报告](https://www.dice.com/recruiting/ebooks/dice-tech-salary-report/salary-satisfaction.html)”

## 其他值得关注的发现
- 并非所有公司都离开云端。虽然一些公司正在将工作负载从公共云迁移到本地，但关于大规模云回迁的消息被夸大了。事实上，
2024年云迁移比以往任何时候都更加普遍。根据Flexera的《2024年云状况报告》，58%的受访者表示计划在2024年将更多工作负载迁移到云端，高于2023年的44%。面向客户的事件正在增加。根据PagerDuty 6月份的一项调查，59%的IT领导者表示，他们看到的会影响客户的事件比前一年更多。此外，调查参与者表示，事件数量增加了43%。尽管有这种趋势，但69%的人表示他们的组织没有投资于减少此类事件。

[YOUTUBE.COM/THENEWSTACK](YOUTUBE.COM/THENEWSTACK)
Tech moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.