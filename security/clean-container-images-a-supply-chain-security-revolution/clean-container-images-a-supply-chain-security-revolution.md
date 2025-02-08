
<!--
title: 清洁的容器镜像：供应链安全革命
cover: https://cdn.thenewstack.io/media/2025/02/55eba463-cve-visualization-visual-1.png
-->

Chainguard 新推出的 CVE 可视化工具可以精确地向企业展示，通过使用无漏洞容器镜像代替传统的充满 CVE 的镜像，他们能够节省多少时间和金钱。

> 译自 [Clean Container Images: A Supply Chain Security Revolution](https://thenewstack.io/clean-container-images-a-supply-chain-security-revolution/)，作者 Jeffrey Burt。

[供应链安全](https://thenewstack.io/securing-the-software-supply-chain-a-2035-blueprint/) 初创公司 [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) 在过去四年多的时间里，一直试图改变开发者和企业看待和使用 [容器镜像](https://thenewstack.io/introduction-to-containers/) 以及其中包含的 [开源组件](https://thenewstack.io/open-source-in-2025-strap-in-disruption-straight-ahead/) 的方式。

通常，这些镜像带有许多 [CVE](https://www.cve.org/)，迫使开发人员去寻找它们，并创建一个耗时的流程来修复和管理它们。Chainguard 的创始人认为，有一种更好的构建容器的方法 —— 本质上是从一个干净的镜像开始，然后从那里开始构建。

其结果是 [Chainguard Images](https://thenewstack.io/chainguard-secure-software-supply-chain-images-arrive/) 的数量不断增加，这些开源组件不包含 CVE，组织可以选择使用，就像一个应用商店。这个想法引起了投资界的关注，这家位于华盛顿州柯克兰的公司通过四轮融资筹集了超过 2.5 亿美元，[包括去年夏天的 1.4 亿美元](https://www.prnewswire.com/news-releases/software-security-leader-chainguard-raises-140-million-in-series-c-funding-to-secure-the-next-frontier-of-ai-workloads-302206133.html)，这使其估值超过 11.2 亿美元。

现在，Chainguard 正在使其客户（2024 年，其客户群同比增长了五倍）更容易看到他们从使用供应商技术中获得的好处。

## 可视化 CVE

该公司本周 [宣布正式推出](https://www.chainguard.dev/unchained/chainguard-cve-visualizations-now-generally-available) [CVE Visualizations](https://edu.chainguard.dev/chainguard/chainguard-images/features/cve_visualizations/)，这是 [Chainguard Console](https://console.chainguard.dev/auth/login) 中的最新功能，是一个获取从安全到产品更新等所有信息的一站式平台。借助这项新功能，组织可以更好地量化使用 Chainguard 的无 CVE 镜像所带来的工程、安全和财务效益。

该功能包括查看 Chainguard 随时间推移在镜像中修复的 CVE 数量（以及工程团队因不必处理它们而节省的时间），以及 Chainguard 的 CVE 累积率与其他开源选项的比较。此外，CVE Visualizations 已集成到 Chainguard Directory 中，使任何开发人员都可以评估和比较容器镜像。

![](https://cdn.thenewstack.io/media/2025/02/6da53a25-cve-visualization-python-compare.png)

*CVE Visualization Python compare*

![](https://cdn.thenewstack.io/media/2025/02/97d26349-cve-visualization-resolved-cves.png)

*CVE Visualization Resolved CVEs*

据 Chainguard 产品管理高级总监 Julian Dunn 称，Chainguard 的高管们会向潜在客户展示表格和图表，说明他们的 CVE 清洁镜像与企业当时使用的镜像相比如何，以及选择 Chainguard 将如何受益。现在，客户可以获得一份个性化的报告，显示他们在过去几个月和几年中使用 Chainguard 镜像所积累的收益，这很好地提醒了他们当初做出改变的原因。

“六个月后，他们忘记了情节，或者他们的老板忘记了，”Dunn 告诉 The New Stack。“他们说，‘发生了什么变化’或‘你最近为我做了什么？我们六个月前签署了这份合同。它实际上是如何传递价值的？’拥有这些时间元素，例如我们随着时间的推移修复了多少 [CVE]，可以帮助那些购买了产品的客户内部人员 —— 或者当他们考虑扩展到其他业务部门时 —— 及时了解最新的个性化信息。”

他说，他们可以看到自注册 Chainguard 以来避免了多少工作，以及修复每个 CVE 的成本是多少。客户可以将他们从供应商那里获得的服务与工程师不必自己动手所节省的时间和成本联系起来。

## 软件融入血液

Chainguard 的四位创始人拥有多年的软件行业经验，这让他们对如何更好地创建容器镜像有了第一手的了解。CEO Dan Lorenc 和 CTO Matt Moore 曾在 Google 和 Microsoft 从事软件工程工作，Moore 还在 VMware 工作过一段时间，首席产品官 Kim Lewandowski 也在 Google 工作过。同样，杰出工程师 Ville Aikas 的履历中也有 Google 和 VMware。

Dunn 在 GitHub、PagerDuty 和 Chef 等公司担任产品管理职务后，于 10 个月前加入 Chainguard。他的背景是软件，但他被 Chainguard 正在做的事情所吸引，即为组织提供没有 CVE 的容器镜像。这与开发者世界的工作方式不同。

## 一个新的方向

Chainguard 提出了另一种看法。容器镜像中存在如此多的 CVE，并非因为主要软件包（例如 Python）存在漏洞，而是因为它们构建在完整的操作系统之上，而这些操作系统带来了 CVE。此外，构建容器的方式源于构建和管理服务器的方式：非常昂贵的机器加载了系统用于多种目的的所有软件。

在容器的世界里，容器往往是为一项任务而专门构建的。Dunn 说，Python 容器运行一项服务，因此它不需要周围的所有其他东西。获取完整的镜像，然后尝试删除不必要的和低质量的组件是很棘手的，并且可能导致 Python 崩溃。

Chainguard 采取了另一种方向：对于 Python，运行它所需的最低级别的依赖项是什么。有 C library 和相关的依赖链。

“我们只做了一次所有的依赖关系映射，”他说。“然后我们要做的就是构建一个没有任何东西的容器。我们不是从某个东西开始并从中删除组件，而是从一个空容器开始，然后说，‘从 Python 开始，你需要获得的所有最小的东西的列表是什么，才能使 Python 解释器运行？’”

这也是为什么 Chainguard 的容器比上游开源项目的容器更小的原因，Dunn 说。这一切的基础是 Wolfi，Chainguard 定制的 Linux 发行版——或者他们称之为（非）发行版——它在构建时具有默认安全性，适用于 supply chain。

Dunn 表示，该公司的 Directory 包含近 1,200 个各种开源组件的无 CVE 镜像，未来还会推出更多。获取镜像，部署应用程序，然后开始构建。此外，Chainguard 去年夏天将其功能扩展到 AI workloads and large language models (LLMs)，使构建这些应用程序更加安全。

## 为什么要与漏洞共存？

开发者已经习惯了他们的镜像中存在漏洞这一事实。Dunn 说这没有道理，他将其与在没有农业部确保食品安全的情况下在超市购物的想法进行了比较。他说，如果这个世界的食品购买者有开发者的心态，他们会将购买不安全食品的风险视为做生意的成本。

此外，CVE 的排名——一些需要立即关注的关键漏洞，以及一些可以稍后处理的不太危险的漏洞——虽然有帮助，但仍然会在攻击面中创建并留下缺陷。不良行为者可能会认为优先级较低的漏洞是进入系统的更安全的方式。

“Chainguard 只是改变了游戏规则，”他说。“为什么任何镜像——为什么任何你运行和构建软件的环境——有任何漏洞是可以接受的？”Dunn 问道。“以及为什么我们要说，‘我们只会消除我们食物中最糟糕的物质疾病，以及所有其他不会造成可怕影响的疾病……我们不会担心这一点。

“在现实世界中，我们不会接受这一点，那么为什么我们在软件世界中接受它呢？”
