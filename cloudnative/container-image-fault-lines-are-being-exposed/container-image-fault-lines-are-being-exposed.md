
<!--
title: 容器镜像的缺陷正在暴露
cover: https://cdn.thenewstack.io/media/2024/07/358d615b-container-images-fault-lines-exposed.jpg
-->

未来，企业必须改造其云原生基础设施，以防范重大漏洞。

> 译自 [Container Image Fault Lines Are Being Exposed](https://thenewstack.io/container-image-fault-lines-are-being-exposed/)，作者 Kim Lewandowski; Adrian Mouat。

加州有近 16,000 条断层，其中 500 条处于“活跃”状态，[科学家表示](https://www.californiaresidentialmitigationprogram.com/resources/blog/california-earthquake-probabilities)，未来 30 年发生大地震的可能性超过 95%。这就是为什么旧金山在 2013 年实施了强制性抗震改造计划，[超过 90%](https://www.nbcbayarea.com/investigations/soft-story-retrofits-in-san-francisco/3267556/) 的目标结构已成功完成改造。

如今，我们在软件供应链安全方面也处于类似的境地，该行业的大部分人因 [XZ Utils 威胁](https://www.chainguard.dev/unchained/if-xzs-backdoors-are-inevitable-how-do-we-stay-secure-the-answer-is-move-faster) 而感到震惊，该威胁迅速加入了其他漏洞，如 [SolarWinds](https://thenewstack.io/lessons-learned-from-2021-software-supply-chain-attacks/) 和 [Log4j](https://thenewstack.io/one-year-of-log4j/)，成为臭名昭著的漏洞。公司正在认真审视其供应链，并思考如何保护自己免受“大地震”的侵害。

让我们来看看导致软件供应链安全成为一个棘手领域的基础问题，以及一些正在解决这些问题的基础工作，以及一些关于如何为您的公司未来做好准备，使其免受重大软件漏洞影响的建议。

## 暴露软件安全中的漏洞

根据 [Sonatype](https://www.sonatype.com/?utm_content=inline+mention) 的 [第九届年度软件供应链状况报告](https://www.sonatype.com/state-of-the-software-supply-chain/Introduction)，去年发现了超过 245,000 个恶意 [开源软件包](https://thenewstack.io/do-open-source-obligations-change-with-packaging-ecosystems/)（是之前所有年份总和的两倍）。他们还发现，每 8 次下载开源软件包中就有一次包含已知的风险。

软件安全的根基存在一些严重的裂缝，需要解决。

一个明显需要改进的领域是来源。当您安装 [容器](https://thenewstack.io/containers/) 镜像时，您需要知道它的来源，但太多开发人员仍然依赖于镜像的名称，该名称基于存储库的命名空间和它来自的注册表。他们信任一个镜像，因为它有大量的下载量，或者在搜索中排在首位，或者因为它的名称表明它来自他们的组织或另一个可信的注册表。但是，来自命名空间的这种类型的数据完全不可靠：恶意行为者可以模仿命名约定，而名称无法证明镜像的来源，更不用说谁可能在传输过程中篡改了它。

可重复性也存在一个单独的问题。即使我有一个 Dockerfile 和用于创建镜像的源代码，如果我再次运行 Docker 构建，我最终会得到一个略微不同的镜像。会有不同的时间戳和构建 ID 之类的东西，这意味着我最终会得到一个不完全相同的镜像（按位）。

安全扫描就像打地鼠游戏。这些工具很棒，功能也很强大，但它们会为大多数容器镜像提供大量输出。大多数组织不知道如何处理这些输出。如果您得到 100 个漏洞或 200 个漏洞，您该怎么办？您没有时间去调查每一个漏洞。即使您调查了，下周又会出现十几个漏洞。这是一个非常困难的情况。

最后但并非最不重要的一点是，评估暴露程度非常困难。如果明天出现一个看起来很重要的漏洞，CISO 希望能够查明他们正在生产环境中运行的可能暴露于该漏洞的容器。但现实情况是，即使是试图使用 [软件物料清单 (SBOM)](https://thenewstack.io/a-good-sbom-is-hard-to-find/) 的组织也远不能识别所有软件。现有的工具经常会遗漏项目和传递依赖项。（您可能没有直接使用有漏洞的库，但您在生产环境中运行的数据库可能使用了！）

当您的软件供应链链接到一个存在如此多未知因素的基础时，您不仅会将漏洞引入您的环境：您甚至无法以允许更快修复的方式验证您正在运行的内容。

让我们来看看控制这个问题的两个关键步骤。

## 签署和验证您引入的软件
过去两年，在为容器镜像添加签名方面取得了重大进展，这主要得益于 [Sigstore](https://www.sigstore.dev/) 项目的广泛采用。这一进展极大地提高了理解和证明镜像来源的能力——它们来自哪里，谁构建了它们，以及它们是否以任何方式被意外更改。

Sigstore 现在用于签署所有 [Kubernetes](https://roadmap.sh/kubernetes) 项目的官方镜像，并且它也被 npm 和 Homebrew 包生态系统采用。Sigstore 签名可以直接存储在容器注册表中，与镜像一起，因此您无需运行单独的基础设施来存储签名。Sigstore 还支持通过 OpenID Connect (OIDC) 协议进行“无密钥”签名，因此您无需担心私钥的安全问题。

如果您不检查签名，那么签名就没有意义。如今，在 Kubernetes 集群中通常的做法是使用策略管理工具，例如 Kyverno 或 Open Policy Agent (OPA)。

## 消除基础镜像中的臃肿
典型的容器镜像附带大量臃肿——通常是基础 Linux 发行版提供的操作系统工具——这些工具对于运行应用程序来说是不必要的。除了增加存储和传输成本外，这种臃肿还代表着风险，因为它可能包含可利用的漏洞。

例如，查看 [Docker](https://www.docker.com/?utm_content=inline+mention) Hub 中的 [NGINX](https://www.nginx.com?utm_content=inline+mention) 镜像（默认使用 Debian），并运行 Snyk、Trivy、Grype 或任何其他扫描程序。您会发现该单个 NGINX 镜像附带了大约 100 多个依赖项，并且您会继承相应的漏洞，无论您是否使用任何其他软件工件。

典型的容器镜像中臃肿带来的数百个依赖项和漏洞是有成本的。即使只有很小一部分漏洞实际上是可利用的，它们也会影响您对环境的推理能力。

可以大幅减少这种噪音，并达到您的报告只发现少数几个可以应对的漏洞的程度。基本上，答案是将容器镜像中的软件组件减少到所需的最小依赖项集，并不断更新该集合。

## 更好的供应链基础带来的好处
从短期来看，使用软件签名和最小化发行版和容器镜像的组合将为您带来更少的暴露：漏洞暴露、传递依赖暴露以及软件被篡改的暴露。

所有这些工作的目的都是为了达到您知道——并且能够证明——所有软件来自哪里，以及能够详尽地识别所有正在使用的软件的所有版本。漏洞将永远存在，但通过使用最小的、经过硬化的镜像，您可以将漏洞数量降至最低，并在下一个“重大漏洞”出现时立即识别所有出现漏洞软件的情况。

[Chainguard Images](https://www.chainguard.dev/chainguard-images) 为安全团队提供了软件供应链安全的关键“零 CVE”起点——设计上最小的容器镜像，具有描述所有软件包的来源和确切版本的内置证明，并不断更新以修复新的漏洞。