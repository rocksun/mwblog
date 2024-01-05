<!--
title: 开源安全供应链走向成熟的2023年
cover: https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1-1024x576.png
-->

开源安全一直都很重要，只是我们曾经假装否认。我们再也不能奢侈地懒惰下去了。

> 译自 [2023: The Year Open Source Security Supply Chain Grew Up](https://thenewstack.io/2023-the-year-open-source-security-supply-chain-grew-up/)，作者 Steven J. Vaughan-Nichols 别名sjvn，从CP/M-80成为尖端PC操作系统，300bps成为快速互联网连接，WordStar成为最先进的文字处理器开始，一直在撰写关于技术及技术业务的文章，我们也喜欢它。

开源安全现在不仅对开发者，也对政府和顶级公司至关重要。

[开源安全](https://thenewstack.io/tracy-ragan-my-favorite-open-source-security-projects/)一直很重要。我们只是假装不在乎。我们再也无法奢侈地懒惰了。现在，美国政府的网络安全和基础设施安全局(CISA)[开源软件安全路线图](https://www.cisa.gov/resources-tools/resources/cisa-open-source-software-security-roadmap)已经宣布我们必须确保开源软件的安全。这不仅仅在国家层面。在欧盟(EU)，[网络弹性法案(CRA)](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)正在迅速要求软件在24小时内披露软件漏洞，并提供至少5年的补丁支持保证。

CRA的最新版本对开源软件有所放松。它宣布: "为了不阻碍创新或研究，在商业活动之外开发或提供的自由开源软件不应受本条例约束。" 我不是律师，但我报道开源法律问题，里面有足够的模糊词语来担心开源开发者。

[Linux基金会欧洲](https://linuxfoundation.eu/)首席Gabriele Columbro担心"[为了防止责任，开源项目可能会被禁止下载到欧盟](https://thenewstack.io/lf-europe-chief-warns-developers-on-eus-cyber-resilience-act/)或发布声明不批准在欧盟使用“的预言可能会成真。

那么，为什么政府突然这么担心开源安全呢？原因很简单，他们终于意识到软件安全对整体安全的重要性。

几十年前，开源的创始人之一埃里克·S·雷蒙德（Eric S. Raymond）曾著名地创造了林纳斯（Linus）定律: "[只要眼球足够多，所有的漏洞都是浅显的](https://flight.beehiiv.net/v2/clicks/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJodHRwOi8vd3d3LmNhdGIub3JnL35lc3Ivd3JpdGluZ3MvY2F0aGVkcmFsLWJhemFhci9jYXRoZWRyYWwtYmF6YWFyL2luZGV4Lmh0bWw_dXRtX3NvdXJjZT1vcGVuc291cmNld2F0Y2guYmVlaGlpdi5jb20mdXRtX21lZGl1bT1yZWZlcnJhbCZ1dG1fY2FtcGFpZ249YS1uZXctdGFrZS1vbi1zb2Z0d2FyZS1jb2RlLXNlY3VyaXR5LXRoZS1vcGVuLXNvdXJjZS1jb25zdW1wdGlvbi1tYW5pZmVzdG8iLCJwb3N0X2lkIjoiMGEwNTA3MmItYzY1ZS00MDU2LWI4MmEtMDQxNTczNTBmMjIzIiwicHVibGljYXRpb25faWQiOiI0NzljNmYwNi0xNzVlLTRlOTMtOWRhOC0xM2RiOTNiNTU5MjMiLCJ2aXNpdF90b2tlbiI6IjY0OTBlYzZmLWQ5NzItNGE5Mi1hZThkLTc3MGI1NTkzMzFkYSIsImlhdCI6MTcwNDEzOTM5MywiaXNzIjoib3JjaGlkIn0.4FG5B8mYJc34xay_yqTBu8l_Z0A-JgmUxX09Fc7-Pd4)。"这让你感觉开源安全很温馨舒适，不是吗？不过，有一个推论。为了让林纳斯定律起作用，你需要专家的眼睛来寻找漏洞，需要手来修补漏洞。我们在这方面做得不够好。

这是一个真正的问题，因为正如安全公司[Synopsys](https://www.synopsys.com/)在其[2023年开源安全和风险分析报告](https://www.synopsys.com/content/dam/synopsys/sig-assets/reports/rep-ossra-2023.pdf)中所说，"开源无处不在"，它是"绝大多数商业代码库的基础。事实上，它与现代开发那么交织在一起，以至于代码所有者通常不知道自己软件中的开源组件。"

唉。

正如Synopsys报告的那样，"确保软件供应链安全的第一步是管理应用程序中的开源和第三方代码。如果您无法有效管理和确保开源和第三方软件的安全性，那么为确保供应链安全所做的任何其他努力都将失效 - 或者坦率地说，甚至无关紧要。"

Synopsys没有说错。这就是开源软件安全社区最近在提高自己水平的地方。

[软件物料清单(SBOM)](https://thenewstack.io/how-to-create-a-software-bill-of-materials/)的兴起，发音为S-Bomb，为构建代码安全防御提供了所需的基础。正如乔·拜登总统关于[改进国家网络安全的行政令](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/)所宣布的，SBOM是“包含用于构建软件的各种组件的详细信息和供应链关系的正式记录”。SBOM包括[软件包数据交换(SPDX)](https://spdx.dev/)、[CycloneDX](https://cyclonedx.org/specification/overview/): [GitHub](https://github.com/)的[依赖关系提交格式](https://docs.github.com/en/rest/dependency-graph/dependency-submission?apiVersion=2022-11-28);以及[Kubernetes安全运营中心(KSOC)](https://ksoc.com/)的[Kubernetes物料清单(KBOM)](https://github.com/ksoclabs/kbom)标准。

但是，为了保护开源软件工件的完整性，SBOM是不够的。这就是[供应链软件工件等级( Supply-chain Levels for Software Artifacts，SLSA，发音为Salsa)](https://slsa.dev/)的用武之地。

具体来说，[SLSA 1.0](https://thenewstack.io/openssf-boosts-software-supply-chain-security-with-slsa-1-0/)提供了:

- 讨论软件供应链安全的共同词汇。
- 通过评估您所使用的工件(如源代码、构建和容器镜像)的可信程度，来评估上游依赖项的一种方式。
- 一个可以改进您自己软件安全的行动清单。
- 一种衡量您在符合即将发布的[安全软件开发框架(SSDF)](https://csrc.nist.gov/Projects/ssdf)标准方面的努力的方法。

OpenSSF的总经理Brian Behlendorf强调，SLSA为组织提供了“保护其软件所需的工具”。我对SBOM和SLSA的简单描述是，SBOM是食谱，SLSA是程序的烹饪说明。

那么，如何知道这些食谱中的真实情况呢？这就是[Sigstore](https://www.sigstore.dev/) - 开源软件签名服务的用武之地。使用Sigstore，您可以加密签名发布文件、容器镜像和二进制文件。一旦签名，签名记录就会保存在防篡改的公共日志中。这为软件工件提供了一个更安全的保管链，可以追溯到其源头并得到保护。

为了便于使用Sigstore，[Kubernetes的联合创始人之一](https://thenewstack.io/beda-burns-and-mcluckie-the-creators-of-kubernetes-look-back/)Craig McLuckie联合创立了一家新公司[Stacklok](https://stacklok.com/)，它建立在Sigstore之上。它有两个项目，[Trusty](https://bit.ly/stackloktrusty)和[Minder](https://bit.ly/stacklokminder)。前者是一项免费服务，用于全面评估软件包的依赖风险。后者是一个平台，用于库创建者在多个存储库中自动化和执行工件签名和验证。

[开源安全基金会(OpenSSF)](https://openssf.org/)[安全洞见规范](https://github.com/ossf/security-insights-spec)是另一个最近增加到安全中的开源项目。它为维护者提供了一种机制，使用YAML以机器可处理的方式提供有关其项目安全流程的信息。有了这个，您不需要重写或重新定位现有的策略和文档。它们可以直接集成到规范中。

虽然2023年的大部分主要安全改进都是针对软件供应链的，但还有其他重大进展。其中之一是[漏洞利用可能性交换](https://www.cisa.gov/sites/default/files/2023-01/VEX_Use_Cases_Aprill2022.pdf)(VEX)及其开源实现[OpenVEX](https://github.com/openvex)的兴起。这种技术被[Anchore](https://anchore.com/)、[Chainguard](https://www.chainguard.dev/)和微软等公司使用，用于记录软件漏洞的状态。例如，使用OpenVEX，无需浪费时间创建电子表格来跟踪漏洞，可以记录漏洞，然后由开源漏洞扫描仪使用以减少管理漏洞的痛苦和减少假阳性的负担。

但是，就因为有了这些工具，并不意味着我们会使用它们。开发者安全公司[Snyk](https://snyk.io/)在其[2023年软件安全调查](https://snyk.io/reports/open-source-security/)中发现，尽管针对开源代码的网络攻击数量创历史新高，但40%的受访者仍然不使用关键的供应链安全技术。

当然，公司知道存在问题，但Synk发现他们正在特殊的基础上解决供应链安全问题。只有一半的公司有正式的供应链安全策略。

我们在2024年的安全任务很清晰。我们必须采用这些软件链安全工具，并开始将它们作为我们的工具链的一部分使用。

听起来很简单，不是吗？但事实并非如此。

一个证明这很困难的原因是，我们远远没有足够的IT安全工作人员。正如[国际信息系统安全认证联合会(ISC2)](https://www.isc2.org/)最近指出的，我们当前[缺少400万名网络安全专家来支持全球经济](https://www.isc2.org/Insights/2023/11/ISC2-Cybersecurity-Workforce-Study-Looking-Deeper-into-the-Workforce-Gap)。

使用开源代码的公司应该做些什么？首先，正如惠普企业(HPE)的首席安全官Bobby Ford所观察到的，"人们认为网络安全是一项高度技术性的事物。是的，一些角色确实需要深厚的技术专长，但网络安全是一个巨大的领域，使一个组织具有网络弹性也需要通用角色，这需要更广泛的技能组合。"

因此，95%的网络安全专业人士认为“[可以做更多的工作来鼓励更多员工加入网络安全相关角色](https://www.trellix.com/en-us/about/newsroom/stories/perspectives/trellix-survey-findings-a-closer-look-at-the-cyber-talent-gap.html)”。您公司中可能已经有准备好帮助保护您软件安全的人。

此外，研究表明，[70%的网络安全人力感到超负荷工作](https://www.isc2.org/-/media/ISC2/Research/2022-WorkForce-Study/ISC2-Cybersecurity-Workforce-Study.ashx)，而且由于多项工作相关压力，[25%的网络安全领导者将换工作](https://www.gartner.com/en/newsroom/press-releases/2023-02-22-gartner-predicts-nearly-half-of-cybersecurity-leaders-will-change-jobs-by-2025)。

简而言之，我们需要更多人，要比现在多很多。这意味着今后要花更多时间和精力进行安全教育。

这也意味着尽可能地使安全自动化。通过教育和使我们的安全自动化，我们可以在2023年取得的安全标准化进展上建立一个坚实的开源安全基础，面向未来。考虑到风险，这不仅仅是一个好主意，而是一个必需品。
