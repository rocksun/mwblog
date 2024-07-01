# 幽灵秘密：代码库中的隐藏威胁

![Featued image for: Phantom Secrets: The Hidden Threat in Code Repositories](https://cdn.thenewstack.io/media/2024/06/0fa327ff-getty-images-bwvuu8mlx9w-unsplash-1024x683.jpg)

近年来，现代软件开发环境日益复杂，导致程序员将[秘密暴露在代码库中](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/)的问题日益严重，使它们成为网络犯罪分子的唾手可得之物。

[GitGuardian](https://www.gitguardian.com/) 几年来一直在跟踪这个问题，在其年度《秘密蔓延状况报告》中详细说明了每年在[GitHub](https://thenewstack.io/githubs-2fa-push-boosts-adoption-among-developers/) 中发现的暴露[秘密](https://thenewstack.io/managing-secrets-in-your-devops-pipeline/)数量不断攀升。今年发布的最新报告显示，该公司[在 2023 年的 GitHub 提交中检测到近 1280 万个新秘密](https://www.gitguardian.com/state-of-secrets-sprawl-report-2024)，比前一年增加了近 300 万个。
2020 年，在报告的第一年，这个数字是 300 万。2023 年，GitGuardian 扫描的 11 亿次提交中，有 800 万次提交至少暴露了一个秘密。

来自[Aqua Security](https://thenewstack.io/aqua-security-uncovers-major-kubernetes-attacks/) 的研究人员上周加剧了人们的担忧，他们表示发现了一些秘密——[API 令牌](https://thenewstack.io/why-your-api-keys-are-leaving-you-vulnerable-to-attack/)、[凭据](https://thenewstack.io/unused-credentials-key-culprits-in-cloud-attacks-study-says/) 和[密码](https://thenewstack.io/stytch-takes-the-hassle-out-of-passkey-authentication/)——这些秘密已经暴露了数年。他们还发现，将一个秘密硬编码到代码中一次，即使它被认为已删除，也可能永久暴露它。

更令人担忧的是：大多数扫描方法都错过了这些“幽灵秘密”，研究人员发现，[Git 存储库](https://thenewstack.io/create-a-local-git-repository-on-linux-with-the-help-of-ssh/) 中近 18% 的秘密可能会被忽略。

“我们发现了重要的秘密，包括云环境、内部基础设施和遥测平台的凭据，这些凭据暴露在互联网上，”Aqua 安全部门 Aqua Nautilus 的研究人员[Yakir Kadkoda](https://www.linkedin.com/in/yakir-kadkoda/) 和[Ilay Goldman](https://www.linkedin.com/in/ilaygoldman/) [在一份报告中写道](https://www.aquasec.com/blog/undetected-hard-code-secrets-expose-corporations/)。“通过各种基于 Git 的流程，这些流程对开发人员和 AppSec 专业人员的影响尚不清楚，以及[源代码管理 (SCM)](https://thenewstack.io/5-version-control-tools-game-developers-should-know-about/) 平台的行为，即使在被认为已删除后，秘密仍然暴露。”

## 开发人员及其秘密

多年来，开发人员一直在将秘密硬编码到软件中，以实现更快的配置和其他合法目的。如今，云计算的兴起以及编程日益复杂和分散的性质，开源和第三方代码以及[代码重用](https://thenewstack.io/coding-from-scratch-creates-new-risks/) 成为常态，使编程速度更快，但也使其面临着越来越多的网络威胁和[供应链风险](https://thenewstack.io/fortifying-the-software-supply-chain/)。

无数安全供应商已经发出关于暴露秘密的警报，Kadkoda 和 Goldman 写道，他们多年来一直在“教育开发人员不要将秘密硬编码到他们的代码中”。此外，全球秘密管理软件市场预计将快速增长，一项预测称，该市场将从去年的 670 亿美元增长到[2031 年的 1046 亿美元](https://www.linkedin.com/pulse/secret-management-software-market-size-2031-overview-iqjaf/)。

幽灵秘密问题很大程度上是由于 SCM 系统（如 GitHub、Bitbucket 和[GitLab](https://about.gitlab.com/?utm_content=inline+mention)）在其基于 Git 的基础设施中保存已删除或更新的代码提交的方式造成的，Aqua Nautilus 团队表示。这意味着即使是在代码中使用过一次的秘密，或者被认为已删除的秘密，也可能仍然暴露。

为了撰写这份报告，Aqua 研究人员扫描了 GitHub 上排名前 100 的组织，其中包括 52,000 多个公开可用的存储库。
“在我们进行研究的过程中，我们发现了一些重大的秘密，包括获取世界上一些最大组织的完整云环境的访问权限，渗透敏感项目的内部模糊测试基础设施，访问遥测平台，甚至获取网络设备、简单网络管理协议 (SNMP) 秘密和财富 500 强公司的摄像头画面，”Kadkoda 和 Goldman 写道。“这些发现可能会对受影响的组织造成重大攻击。”

## Mozilla 和思科作为警示故事

在一个案例中，研究人员发现了一个 Mozilla 的 FuzzManager 的 API 令牌，FuzzManager 是一个内部工具，用于收集和分析 [模糊测试](https://thenewstack.io/api-fuzzing-what-is-it-and-why-should-you-use-it/) 数据以查找安全漏洞。该令牌使他们能够访问 Mozilla 的内部模糊测试数据，这些数据通常保密，以防止恶意行为者利用未修补的漏洞。在另一个案例中，他们发现了思科 Meraki 仪表板的特权 API 令牌，该仪表板允许组织管理其网络。找到此类令牌的攻击者可以控制网络资源并访问敏感信息，包括 SNMP 秘密和摄像头画面。

在另一个案例中，他们在大型医疗保健公司的 Git 提交中发现了一个 Azure 服务主体令牌。该令牌使持有者能够高度访问该公司的 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure 资源，包括其内部 [Azure Kubernetes 服务](https://thenewstack.io/install-cloud-foundry-on-azure-kubernetes-clusters/) 和 Azure 容器注册表。拥有该令牌的恶意行为者可以控制该公司的 [Kubernetes](https://thenewstack.io/kubernetes/) 集群。

所有暴露秘密的组织都收到了通知，并且秘密已被撤销。

尽管如此，幽灵秘密的问题仍然存在。Aqua 使用两个工具扫描了存储库——[git clone](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) 和 [git clone –mirror](https://git-scm.com/docs/git-clone)——在存储库的镜像版本中，发现它们错过了近 18% 的秘密。问题在于提交仍然可以通过 SCM 上的“缓存视图”访问，因此从存储库的克隆和镜像版本中删除的任何秘密仍然可以供任何知道提交哈希的人访问。

## 获取缓存视图

研究人员概述了四种检索缓存视图提交的策略，从暴力破解提交哈希和使用 REST API 端点到查看拉取请求的 GUI 和使用 GitHub 历史数据集。

网络安全专家表示，如果组织想要阻止对开发人员的网络风险，他们将不得不解决幽灵秘密问题。

“[Eric Schwake](https://www.linkedin.com/in/ericschwake/)，[Salt Security](https://salt.security/) 的网络安全策略总监，告诉 The New Stack：“这个问题至关重要，因为它指出了基于 Git 的系统中秘密管理方式的根本缺陷，这会影响许多组织。暴露 API 令牌和凭据等秘密会导致严重后果，例如未经授权的访问、数据泄露和经济损失。即使在删除或更新后，‘幽灵秘密’的持久性会加剧问题，构成长期风险。由于 API 是现代应用程序的基础，它们正成为攻击者的目标。”

[Sarah Jones](https://www.linkedin.com/in/sarah-jones-209b9690/)，[Critical Start](https://www.criticalstart.com/) 的网络威胁情报研究分析师，表示组织将需要采用多层方法来缓解此类风险。
Jones 告诉 The New Stack：“开发人员需要接受有关安全编码实践、使用专用工具进行适当的秘密管理以及防止意外泄露的必要性的全面培训。自动化扫描工具可以在秘密被推送到公共存储库之前识别它们，代码审查流程会增加一层安全保障。此外，组织应实施专门的秘密管理解决方案，以确保安全存储和细粒度访问控制。”

## 恶意行为者喜欢开发人员

Schwake 和 Jones 都表示，开发人员将继续成为威胁行为者的诱人目标，因为他们可以访问敏感信息和系统，并且由于开源代码和 [云原生开发](https://thenewstack.io/cloud-native/) 的使用不断增加，攻击面也随之扩大。此外，随着 [DevSecOps](https://thenewstack.io/5-tips-for-developer-friendly-devsecops/) 实践被集成到开发生命周期中，攻击者将继续将重点转移到利用开发过程本身的漏洞，Schwake 说。
“然而，情况正在逐渐改善，”他说。“随着安全漏洞越来越频繁，其影响也越来越严重，开发人员开始认识到安全的重要性。组织应该投资于安全培训计划，并将安全工具集成到开发工作流程中。采用 DevSecOps 实践也有助于培养一种安全责任共担的文化，鼓励开发人员在工作中承担安全责任。”

他补充说，“我们也看到在整个 API 开发生命周期中，姿态治理的重要性越来越高，以尽早预防安全问题。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。