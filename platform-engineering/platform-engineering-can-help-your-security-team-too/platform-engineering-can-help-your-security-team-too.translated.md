# 平台工程也能帮助您的安全团队

![Featued image for: Platform Engineering Can Help Your Security Team, Too](https://cdn.thenewstack.io/media/2024/07/d951d55c-platform-engineering-can-help-your-security-team-too-2-1024x576.jpg)

您收到通知，一个流行的 [开源项目](https://thenewstack.io/a-guide-to-open-source-software-security/) 中存在新的严重漏洞。该软件包与所有最流行的 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/) 一起提供。它位于您用于构建 [容器](https://thenewstack.io/containers/) 的基础镜像中。该漏洞已部署在您运行的每个 [微服务](https://thenewstack.io/microservices/) 中。接下来您该怎么办？您有 [计划](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/) 吗？

如果我们有一个团队擅长自动化软件开发生命周期，为开发人员提供友好的工具来持续发布更新，并且可以为您的开发团队选择和验证运行应用程序所需的开源构建块，那该多好。

如果我们有 [平台工程](https://thenewstack.io/platform-engineering/)，那该多好。

平台工程旨在解决开发人员面临的许多摩擦、延迟和中断问题。然而，我作为网络安全产品总监的亲身经历告诉我，平台工程还可以提高组织的安全性。

2022 年 10 月，我参与了我的第一次 [零日](https://thenewstack.io/zero-day-vulnerabilities-a-beginners-guide/) 响应。OpenSSL 通知全世界，它在 OpenSSL 3.0.0 – 3.0.6 版本中发现了一个严重漏洞。毫无疑问，此公告需要紧急、有组织的响应。

OpenSSL 不仅与大多数 Linux 发行版捆绑在一起，而且还是处理网络连接加密的软件。我们在开始准备时并不知道漏洞的性质，但我们知道潜在的影响非常严重。

我们做好了应对另一个 [心脏滴血](https://nvd.nist.gov/vuln/detail/cve-2014-0160) 的准备，该漏洞 [于 2014 年在 OpenSSL 加密软件库中发现](https://thenewstack.io/vulnerabilities-versus-intentionally-malicious-software-components/)，影响了大量的 Web 服务器。

我们需要确定我们在生产环境中运行 OpenSSL 的位置，并制定一个计划来修补漏洞。我们的微服务作为容器部署，每个容器中都包含一个 Linux 发行版。我们很快发现，每个生产服务都受到了影响。深吸一口气。好的，接下来该怎么办？

确定了爆炸半径后，我们必须准备修补，而且要快速修补！在这种情况下，修复过程是更新我们基于容器的镜像。

为此，我们必须识别每个服务的每个 Dockerfile，并确保 `FROM:` 行中的基础镜像已更新。每个容器都需要通过我们的 [CI/CD](https://thenewstack.io/ci-cd/) 管道重建并重新部署到生产环境中。数百个服务、数百个 [Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)、数百个更新、数百个重新部署……数百人参与其中。

CI 和 CD 流程是自动化的，但不幸的是，基础镜像升级不是自动化的。我们需要每个开发团队参与响应。一些团队只有少数几个服务，而另一些团队则有更多服务。这不是一个复杂的过程，但它打乱了数百名开发人员，不可避免地造成了上下文切换、通信开销和验证的成本。

## 建立对安全团队的同理心

我经常讲这个故事，即使漏洞的严重程度在 11 月 1 日披露后被降级为高。([CVE-2022-3602](https://nvd.nist.gov/vuln/detail/CVE-2022-3602) 和 [CVE-2022-3786](https://nvd.nist.gov/vuln/detail/CVE-2022-3786)，如果您感兴趣的话！

我讲这个故事是因为在那一天之前，我一直抵制 [“DevSecOps”](https://thenewstack.io/ebooks/devsecops/best-of-devsecops-trends-in-cloud-native-security-practices/) 作为一项独立的事物。我相信“DevOps 一直都包含安全性”和“我的平台工程团队正在构建安全性”。但我从未体验过安全团队的一天生活。我缺乏对安全团队的同理心。
像许多其他平台工程领导者一样，我优先考虑了[开发人员体验 (DevEx)](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/)。当我谈到构建[平台即产品](https://thenewstack.io/platform-as-a-product-in-4-steps/) (PaaS) 的必要性时，我专注于生产力和开发人员摩擦。我的平台产品经理团队会与开发人员进行用户访谈，然后像外围的利益相关者一样管理安全。我们没有将安全视为产品的用户。

安全自动化的投资回报率 (ROI) 很容易用“响应成本”来计算。但下一个零日漏洞的真正成本可能不仅仅是中断和时间损失。这些漏洞可能会被利用，使您的系统容易受到黑客攻击，并对您的公司造成无法弥补的声誉损害。

Marc Cluet 是一位全球金融服务机构的核心平台工程执行总监（也是[伦敦 DevOps](https://www.meetup.com/london-devops/) 的组织者，已经组织了十年），他一直倡导将安全作为解决方案的一部分。

“作为在高度监管环境中工作的人，安全一直是我参与的 DevOps 转型计划的一部分，”Cluet 在接受 The New Stack 的在线采访时表示。“您构建的安全流程和解决方案需要满足监管机构和组织中许多不同团队的需求，包括开发、运营、安全、审计、合规、治理等。”

[“左移”](https://thenewstack.io/the-limits-of-shift-left-whats-next-for-developer-security/) 一直是 DevOps 运动的口号，已经超过十年了。但这种理念的诱惑在于将安全委托给开发团队，而没有考虑他们需要什么才能取得成功。
[Andy Burgin](https://www.linkedin.com/in/andyburgin) 是一位博彩行业的首席平台工程师，他在接受 The New Stack 的在线采访时对此表示警告：“如果您使用‘左移’作为一种方式，以‘赋能’的名义将工作/责任/问责制变成别人的问题，那么您完全误用了这个词。
“拥有工具/培训，最重要的是承诺而不是合规，比简单地将您不想再处理的事情 YOLO 到另一个团队要好得多。社会技术系统不是玩所有权游戏的游乐场。”

## 考虑“安全体验”
当我们关注我们想要通过“左移”来推动的结果时，对话就会改变。我们希望在开发过程的早期阶段预防和解决更多安全问题，理想情况下是在它们部署到生产环境之前。我们不一定非要把所有这些工作都委托给开发团队。

为了确保您不会在开发过程中引入更多摩擦，您需要采用高度自动化的方式，并根据安全团队的用户需求以及开发人员的需求来进行。

平台工程社区正在蓬勃发展，越来越多的团队正在为其[内部开发平台 (IDP)](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) 采用平台即产品的方法——但通常，团队会犯我犯过的错误。他们将安全视为利益相关者，而不是平台的用户。为了取得成功，我们必须对开发人员体验和安全体验都采用以用户为中心的 подход。

如果您是平台工程团队的一员，我敦促您与安全部门的同事进行用户研究。询问他们需要从您的 IDP 中获得什么。询问他们您如何帮助他们更轻松地完成工作。

安全团队需要从代码到生产的[软件开发生命周期](https://thenewstack.io/ebooks/security/a-blueprint-for-supply-chain-security/) 的可见性。他们需要应用程序上下文来评估风险并做出适当的响应。他们需要高度自动化的主动预防和被动事件响应。

安全团队重视反馈循环来衡量他们的成功；我们在这方面做得越来越好吗？我们对新的关键通用漏洞和披露 (CVE) 的平均修复时间 (MTTR) 是多少？开发人员是否正确使用我们的安全工具？我们有哪些盲点？开发人员需要哪些安全教育？

谁比平台工程团队更适合提供这些结果？

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)