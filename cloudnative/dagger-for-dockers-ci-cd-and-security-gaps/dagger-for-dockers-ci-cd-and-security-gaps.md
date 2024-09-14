
<!--
title: 用于Docker CI/CD的Dagger和安全漏洞
cover: https://cdn.thenewstack.io/media/2024/09/b31bafd4-olivie-strauss-fsdvg0_9haa-unsplash-1.jpg
-->

Dagger非常适合CI/CD，并且可以与GitHub集成以用于CI/CD项目。

> 译自 [Dagger for Docker’s CI/CD and Security Gaps](https://thenewstack.io/dagger-for-dockers-ci-cd-and-security-gaps/)，作者 B Cameron Gain。

我的想法是将我的 [Neo4j 知识图谱](https://thenewstack.io/build-a-movie-database-with-neo4js-knowledge-graph-sandbox/) 项目分享到 [Docker](https://thenewstack.io/why-capistrano-got-usurped-by-docker-and-then-kubernetes/) [容器](https://thenewstack.io/containers/) 上，以便可能与可以帮助该项目的人员进行工作和修改。再次强调，这不是一个商业项目，而是一个涉及海洋数据分析的沙盒项目。

然而，我与至少两位开发人员交谈过，他们坚决反对这样做，他们说我需要 [GitHub](https://thenewstack.io/this-year-in-programming-go-rust-github-lead-2021-stories/) 或 [git](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/) 来进行任何工作，原因有很多——我所知道的，也是众所周知的——例如它的系统化方法、它对拉取请求的有效性以及它跟踪和审计过去更改的能力等等。

但再次强调，我想要一些简单的东西，我认为只需要最多两三个人来审查应用程序中的代码，仅此而已，因为其他所有事情都将由我来做。当在我的项目中使用来自其他运行时的代码时，我也可以使用来自 [DockerHub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/) 的经过硬化的 [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) 容器来确保安全性，而不是必须费心处理签名和 [SBOM](https://thenewstack.io/software-composition-analysis-and-sboms-a-united-defense/) 等等。由于 Chainguard 持续更新其容器镜像，因此您可以将安全更新交给它来管理。

在寻找分享我的知识图谱应用程序的正确选项时，我想起了 Chainguard 开发者关系倡导者 [Adrian Mouat](https://www.linkedin.com/in/adrianmouat/) 在今年早些时候在巴黎举行的 KubeCon + CloudNativeCon EU 上发表的演讲。该演讲名为“以现代方式构建容器镜像”（我当时就在那里听演讲，而且座无虚席）。

我从中学到的关键要素，不一定是针对我的项目，而是总体而言，是 GitHub 确实一直是部署和其他许多方面的首选方式。但是，它可以通过改进得到补充，尤其是在流水线 CI/CD 组织方面。

Docker 专门针对 CI/CD 而言，存在不足。虽然回到我的原始项目，是的，我认为 Docker 非常适合我想要做的事情。但事实证明，再次强调，对于 CI/CD 而言，Docker 确实存在缺点，在某些安全方面也是如此。

Mouat 演讲中提出的一个关键点是，[Dagger](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/) 似乎非常适合 CI/CD，此外，它还可以与 GitHub 集成以用于 CI/CD 项目，正如 Mouat 所解释的那样。

## 我想要我的 CI/CD

Dagger 通过容器化提供可编程的 CI/CD。但如上所述，这不是非此即彼的情况，就像我的项目一样。再次强调，我的项目只是关于将一个简单的应用程序打包到容器中，然后发送给几个人。它绝对不是一个完整的 CI/CD 类型的协作。

正如 Mouat 在他的演讲中所定义的那样，Dagger 是一种利用 [BuildKit](https://docs.docker.com/build/buildkit/) 的强大功能来定义代码中的 CI/CD 流水线的工具。他说，它擅长创建可以在项目之间重复使用的复杂构建流水线，并提供强大的缓存和并行功能。

这些可重复使用的容器中的构建流水线是关键。

“将可重复使用的构建流水线定义为代码是减少 [DevOps](https://thenewstack.io/devops/) 复杂性和增强安全性和合规性的关键先决条件。允许开发人员使用他们熟悉的 Docker BuildKit 工具在本地运行这些流水线，可以自动确保开发和生产环境之间的一致性，”TechTarget 的企业战略集团分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk/) 说。“这对实施策略驱动的安全至关重要，可以提高开发人员的生产力，同时确保安全性。”

再次强调，Dagger 是与 GitHub、[GitLab](https://about.gitlab.com/?utm_content=inline+mention) 或纯 git 集成，或者可以集成。因此，在许多方面，您都获得了两全其美，兼具安全性方面和简化性。

CI/CD 流水线的可编程性和 Dagger 提供的不同选项使其特别适合于 CI/CD。虽然一个简单的 Docker 容器很适合我的项目，但从这个角度来说，它可能会显得力不从心——至少，这是 Dagger 的一位创建者、Dagger 的联合创始人兼工程副总裁以及 Docker 的前工程副总裁 Sam Alba 的看法。

在 2018 年 Dagger 项目创建之前，Alba 在 Docker 时曾在 The New Stack 上写了一篇博客文章：“虽然我们已经取得了重大进展，但我们仍有更多工作要做，特别是超越容器作为唯一单元并编制容器的流水线流程。”

在 Docker 期间，Alba 写道：“软件供应链的整体自动化”还没有解决，“我们释放了供应链末期的许多价值，但没有充分解决开发人员在编码和协作时的需求，时至今日 CI/CD 仍然一团糟。”

对于本地镜像共享，Docker 可能很棒。在 Mouat 的演讲中，他展示了使用上游 Golang 镜像的可行性，在 Go 应用程序中编译该镜像并设置入口点。

“就像你可能意识到的，这很有用。问题是，我们的构建工具仍然在那个镜像当中，”Mouat说。“所以，我们的最终镜像不仅包含应用程序。它还包含所有的构建工具，和我们运行应用程序不需要的所有底层的 Debian 操作系统。理想情况下，我想摆脱它，因为它只是潜在 CVE [常见漏洞和风险] 和问题的根源。”

正如 Mouat 在演讲中所说，Dagger 不仅仅是为构建容器镜像而设计的。它真正的设计目的是解决整个 CI/CD 问题，“即你尝试调试 CI/CD，但它却以不同的方式工作，”Mouat 说。“你无法在本地运行它，或者至少在本地运行它与在远程运行时不相同，而且最终留下 20 条提交，所有这些提交都像‘这次有效，差不多吧’，”Mouat 说。“它总是继续失败，让你抓狂。这就是 Dagger 的目标。”



## 合适的容器 

Docker 从多个方面来说仍然是王道，包括其轻量级的特性和可重复性。虽然在某些方面来说可能有限制，但它对于其他使用案例来说是完全合适的。这在我的项目中很明显，我只需要与几个人分享我的 Neo4j 知识图谱。

但是，对于全面的 CI/CD，尤其是与之相关的安全挑战，Dagger 值得密切考虑。这也与在安全方面向左转移的公认需求相一致，而这仍然是一个挑战。

“将软件供应链安全性和合规性左移是限制组织运营风险的唯一途径，这也是与大多数政府合作的先决条件。在软件供应链中构建策略驱动的安全管理为增强的安全态势奠定了基础，”Volk 说。“这以主动自动化的方式保护了整个软件供应链，而不会变成应用开发者锚上的海藻。这让首席信息官们非常高兴。”
