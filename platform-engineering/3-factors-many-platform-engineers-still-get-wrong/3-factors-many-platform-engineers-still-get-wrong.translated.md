# 平台工程师仍然搞错的 3 个因素

![Featued image for: 平台工程师仍然搞错的 3 个因素](https://cdn.thenewstack.io/media/2025/05/e3dc6828-platform-engineer-3-mistakes-1024x576.jpg)

在过去的十年中，云基础设施和应用程序部署领域发生了根本性的变化。我们见证了云提供商、Kubernetes 和 OpenTelemetry 的迅速崛起，以及曾经流行的工具（如 Subversion、Yeoman 和 Grunt）的衰落。即使在云演进的过程中，许多基础知识，包括基于 Twelve Factor 的软件开发，仍然是基础。

2011 年，Heroku 的联合创始人 Adam Wiggins 提出了 [Twelve Factor App](https://blog.heroku.com/twelve-factor-apps)（十二要素应用程序），这是一份基于 Heroku 经验教训的最佳实践宣言。凭借将数千个应用程序发布到云端的信心，Heroku 团队利用他们的经验，总结了哪些对开发者有效，哪些无效。他们应用所学到的经验，创建了 Twelve Factor 模型——[成功部署应用程序的 12 个范例](https://thenewstack.io/open-source-drives-the-twelve-factor-modernization-project/)。

![Twelve Factor principles](https://cdn.thenewstack.io/media/2025/05/707baa04-12-factors-heroku_350px.png)

（来源：Heroku）

但是，在过去的 10 年中，云部署发生了根本性的变化，Twelve Factors 没有涵盖某些新的开发实践——例如现代可观测性、日志、追踪和错误处理。因此，在 2024 年末，Heroku [开源并开始现代化](https://thenewstack.io/heroku-moved-twelve-factor-apps-to-open-source-whats-next) Twelve Factors，以适应当今的基础设施。

## 构建坚实的基础

Twelve Factors 已经变得非常出名，“它的许多原则都被认为是整个行业的标准最佳实践，”Heroku 的首席架构师 Vish Abrams 在接受 The New Stack 采访时说。

本文将更仔细地研究前三个因素，因为它们为 Twelve Factor 的更高层次[奠定了基础](https://thenewstack.io/platform-engineers-must-have-strong-opinions)。“如果你看一下 Twelve Factors 的结构，它们是相互构建的，”他继续说道。“你从前三个因素（代码库、依赖项、配置）开始，然后构建到后面的因素的概念中。”

## 因素 1：代码库

“一个 Twelve-Factor 应用程序始终在版本控制系统（如 Git、Mercurial 或 Subversion）中进行跟踪。修订跟踪数据库的副本称为代码仓库，通常缩短为代码库或仅称为 repo。”

第一个因素围绕着使用[代码库](https://12factor.net/codebase)版本控制系统。比较有经验的读者可能还记得 [Mercurial](https://www.mercurial-scm.org/) 或 [Subversion](http://subversion.apache.org/)，但每个开发人员都熟悉 [Git](https://roadmap.sh/git-github)，它目前被广泛用作 GitHub。

第一个因素非常明确：如果有“多个代码库，它就不是一个应用程序；它是一个分布式系统。”代码仓库强化了这一点：一个应用程序只存在一个代码库。

那么，我们今天的情况如何呢？Abrams 解释说：“当 Heroku 首次创建时，使用源代码管理并不是很常见，尤其是在团队中。现在这已经成为一种标准做法，而且更重要的是，像 GitHub 这样的平台允许发现和共享项目。”

随着 GitHub 成为软件开发中的事实标准，开发的范例也发生了变化。代码审查和批准现在是集中式的，并且已成为部署过程不可或缺的一部分。代码更加安全，因为所有更改都会自动记录（[DORA 指标](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/) FTW！），并且可以设置权限以仅允许团队的特定成员执行更新。部署自动化已从自制脚本转移到 GitHub Actions，这些脚本也经过团队的代码审查和测试。

Heroku 也随着现代部署的[新范例](https://thenewstack.io/sustainable-development-balancing-innovation-with-longevity)而发展壮大。正如 Abrams 解释的那样：“最初，期望是你将 `git push heroku main`
来启动你的应用程序。但是现在有了 GitHub 集成，你可以将你的代码推送到 GitHub 并基于拉取请求 (PR) 进行构建，它将创建一个 Heroku 部署，以便你可以测试你的应用程序是否仍然有效。”
Heroku 还构建了几个开源库，以方便使用 GitHub Actions 实现自动化。在 Heroku 上托管您自己的 [GitHub Runner](https://github.com/heroku-reference-apps/github-self-hosted-runner-for-github-actions) 实例，可以为您提供一个用于自动化工作流程的自托管 runner。例如，您可以创建一个 Heroku Review Apps API，并从您的自托管 GitHub Runner 部署 Heroku Apps。您还可以使用 [Heroku Flow Actions](https://github.com/heroku-reference-apps/github-heroku-flow-action) 将您的私有 GitHub 仓库源代码上传到 Heroku。

## 要素 2：依赖项

“一个 Twelve-Factor 应用程序永远不会依赖于系统级软件包的隐式存在。它通过依赖项声明清单完全且准确地声明所有[依赖项]。”

要素二是关于永远不要依赖于软件包的隐式存在。虽然几乎每个现有的操作系统都安装了 `curl` 版本，但基于 Twelve-Factor 的应用程序不会假定 `curl` 存在。相反，应用程序在清单中将 `curl` 声明为依赖项。

每个开发人员都复制过代码并尝试运行它，但却发现本地环境缺少依赖项。依赖项清单确保定义了所有必需的库和应用程序，并且可以在应用程序部署到服务器时轻松安装。

Abrams 说：“依赖项管理中最大的挑战之一是它在每种语言中都不同——而且不仅仅是每种语言；有时它在语言中的每个框架中都不同。” “Heroku 的 buildpack 允许用户以他们想要的方式管理依赖项，并且仍然获得一个构建好的、易于运行和管理的工件。”

自 Twelve Factors 发布以来，开发人员可使用的外部库数量呈爆炸式增长。这导致了另一个担忧：过度依赖第三方库以及由此带来的潜在安全风险。像 [Log4j zero day](https://thenewstack.io/log4j-the-pain-just-keeps-going-and-going/) 和 [OpenSSH 中的关键漏洞](https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh/) 这样广泛的安全事件提醒我们，必须对我们的部署保持警惕。

Abrams 建议说：“小心引入依赖项。” “当功能很简单时，不要引入依赖项；自己编写即可。对于更复杂的功能，选择支持良好且具有维护和发布的库，以便他们可以处理出现的安全漏洞。”

## 要素 3：配置

“应用程序有时会将配置存储为代码中的常量。这违反了 Twelve Factor，它要求。[将配置与代码严格分离]配置在部署之间差异很大；代码则不然。”

大多数应用程序都有存储在 `.env` 文件中的环境变量和密钥，该文件未保存在代码存储库中。`.env` 文件是自定义的，并且为代码的每个分支手动部署，以确保在测试、暂存和生产中发生正确的连接。通过独立管理每个环境的凭据和连接，可以实现严格的分离，并且环境意外交叉的可能性较小。

对于测试，Heroku 允许您使用仪表板或命令行界面 (CLI)（使用诸如 `heroku config:set SECRET_TOKEN=test-secret` 之类的命令）安全地管理跨部署不同阶段的配置。

## 构建在前三个要素之上

前三个要素构成了其余九个要素的基础。它们已被证明是具有先见之明的——这些建议在今天仍然像 2011 年一样有效。

Abrams 说：“最令人惊奇的事情之一是，我们有一些应用程序已经在 Heroku 上运行了很多年，并且它们具有弹性，因为它们遵循了这些原则。Twelve Factors 不仅使我们能够轻松更新这些应用程序，而且还使它们在进行更改时保持稳定和正常运行。”

对于任何构建弹性、可维护的云基础设施的人来说，“最重要的事情是回顾并阅读 Twelve Factors。您会惊讶于有多少仍然有效……这些概念在今天仍然有意义。如果您不遵循它们，您将拥有一个维护不善且难以保持运行的应用程序，”Abrams 总结道。

**如果您想了解更多信息，请查看以下其他资源：**

[YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)