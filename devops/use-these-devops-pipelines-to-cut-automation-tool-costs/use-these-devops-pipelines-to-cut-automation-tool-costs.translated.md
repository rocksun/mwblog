# 使用这些DevOps流水线降低自动化工具成本

许多IT组织使用许可的自动化工具，但为所有QA和开发人员提供许可证是不切实际的。通常，许可证分配给指定的自动化工程师，他们根据需要创建和运行测试。这[给任何团队成员按需执行测试带来了挑战](https://thenewstack.io/top-challenges-to-creating-high-performing-engineering-teams/)。由于大多数自动化工程师都在海外，因此需要额外的许可证用于本地测试执行，这可能非常昂贵。此外，确保高质量的代码、足够的覆盖率、没有代码异味以及彻底的安全扫描至关重要。

我的组织规模庞大，业务涉及多个领域，例如ERP、数据、实验室信息管理系统(LIMS)、自动化和机器人软件、生物生产以及细胞/基因治疗软件。每个领域都使用其自身的内部DevOps解决方案，主要是Jenkins，这会产生月度成本。为了在整个组织中拥有一个统一的DevOps框架，我研究了几种DevOps工具，以确定最具成本效益的解决方案。目的是拥有一个可以在不同领域的不同项目中使用的单一框架。

作为回报，此DevOps解决方案降低了不同项目使用的第三方自动化工具的许可证成本。一旦此CI流水线准备就绪，任何拥有DevOps工具访问权限的人都可以调用自动化测试，而无需担心需要自动化测试工具许可证。

因此，我开始联系几家供应商，最终列出了Jenkins、GitHub Actions(GHA)和Gearset作为可在多个领域使用的常用工具。通过与我的团队进一步分析，我们发现GHA在成本和易于在流水线中加入安全检查和单元测试方面是最佳选择。

在本文中，我将演示GitHub Actions (GHA)作为CI工具的优势。GHA是开源的，但会根据运行器使用情况产生成本。我还提出了一种创新的解决方案来消除运行器成本。将[SonarQube和CodeQL等代码质量工具集成到流水线中](https://thenewstack.io/how-to-install-the-sonarqube-security-analysis-platform/)还可以确保安全扫描并突出显示部署前的問題。

## 实施持续集成(CI)流水线的优势

- **无需自动化工具用户访问即可调用测试**
需要许可证的自动化工具只能由获得许可证的个人使用。但是，当与CI流水线集成时，任何具有CI访问权限的用户都可以启动作业，而无需直接许可证。这种方法优化了许可证池的管理，降低了成本，并扩展了工具在测试自动化方面的效用。例如，所有具有GitHub Actions (GHA)访问权限的开发人员现在都可以调用自动化工具，而无需单独的许可证。

- **消除对QA资源的需求**
某些自动化工具会阻止测试人员/开发人员在UI测试执行期间离开UI屏幕，从而阻止他们在计算机上执行其他任务。利用GitHub Actions (GHA)流水线调用自动化工具消除了此限制，允许[开发人员和测试人员处理](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/)其他任务，而自动化则在后台运行。执行后，将发送包含详细、用户友好的PDF测试结果报告的电子邮件。

![](https://cdn.thenewstack.io/media/2024/11/7aeaa9aa-image_7.png)
图 – 描绘自动化有助于减少人工工作

CI流水线之前 — 手动测试执行设置已将我们的时间从XXX小时有效减少到XX小时，但我们仍然需要分配XX小时，因为QA资源必须在测试执行期间监控屏幕。

![](https://cdn.thenewstack.io/media/2024/11/246aeb70-image_8.png)
图 – 描绘GitHub Actions 将自动化工作进一步减少到零

自动CI/CD集成 — 将这XX小时减少到零，因为CI流水线管理会话，无需在测试执行期间进行手动监控。

**使用GHA作为自动化测试的CI/CD工具的其他好处**

- **使用用户GitHub帐户即可免费访问GHA**
GitHub Actions是GitHub的一个默认启用的功能；因此，不需要显式访问GHA。它直接在您的存储库中支持CI/CD工作流。

- **节省成本—消除AWS基础设施成本**
对于CI/CD流水线，我们需要集成一个运行器（运行CI作业所需的虚拟机），通常在AWS等云中进行配置，会产生额外成本，并且随着负载的增加而增长。然而，通过此方案，我们利用组织提供的Win365机器作为运行器，从而消除了使用云服务时产生的额外[基础设施运行器成本](https://thenewstack.io/cloud-vs-on-prem-comparing-long-term-costs/)。所有自动化工程师都配备了Win365机器用于安装和执行自动化脚本。

![](https://cdn.thenewstack.io/media/2024/11/354c6eef-image_5.png)
图 – Microsoft Win365 vs AWS EC2 实例

## 使用Win365运行器替换AWS运行器
如果提供与其桌面镜像相同的虚拟机，[自动化团队成员需要](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/)安装自动化工具。此云实例会产生固定费用。QA资源仅在工作时间使用此云实例，其余每天16个小时空闲。我们可以通过在空闲时间将这些虚拟机用作CI流水线运行器来显著减少AWS的使用，从而无需启动新的EC2实例。

下图显示了成本节省情况。在这里，我们每月产生55美元的固定虚拟机成本；因此，使用这些虚拟机的流水线将产生0美元的运行器成本，但如果使用新的AWS实例作为运行器，我们可能会产生80美元的月度成本。

![](https://cdn.thenewstack.io/media/2024/11/bace220b-image_2.png)
图 – 成本节省计算

- **防火墙限制和自动化工具配置**
由于GitHub在组织内部网络中进行管理，我们可以避免任何安全系统和自动化工具API权限问题，而这是外部托管CI/CD工具面临的挑战。

- **代码质量检查实施**
在CI流水线本身中，我们可以实现CodeQL和SonarQube代码质量工具，避免单独进行测试的需要。CodeQL是一个时间开销很大的工具。它需要大量时间才能执行流水线，因此建议在单独的流水线中触发CodeQL，结果可以在GitHub中查看。

### 什么是CodeQL
![](https://cdn.thenewstack.io/media/2024/11/7158fdea-image_4-1024x471.png)
图 - 流水线运行后，可以查看CodeQL突出显示的任何错误。

最后，用于部署代码并针对新发布的分支运行自动化测试的DevOps流水线如下所示：

![](https://cdn.thenewstack.io/media/2024/11/d60e743b-image_3-1024x707.png)
图 – 部署代码、运行代码质量检查并最终运行自动化测试的DevOps流水线

## 结论
将GitHub Actions作为各种领域的CICD工具的决定对我的组织来说是富有成效的。我们消除了额外自动化工具许可证的成本，并利用内部可用的虚拟机作为流水线运行器，降低了云实例成本。此外，GHA轻松集成SonarQube和CodeQL等代码质量工具，也有利于维护编码标准。

在当今组织面临预算挑战的世界中，此类技术可能具有重大影响。我们应该创造性地思考如何利用我们周围现有的解决方案，并寻找开源工具来提供安全且经济高效的自动化解决方案。

*本文是The New Stack贡献者网络的一部分。对影响开发人员的最新挑战和创新有见解吗？我们很乐意听到您的声音。成为贡献者并分享您的专业知识，请填写此表格或发送电子邮件至mattburns@thenewstack.io。*

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)