# Spacelift 的 Saturnhead AI 加速 DevOps 故障排除

![Featued image for: Spacelift’s Saturnhead AI To Speed DevOps Troubleshooting](https://cdn.thenewstack.io/media/2025/04/5a301087-spacelift-2-1024x683.png)

[Spacelift](https://docs.google.com/document/u/0/d/1wKhHoyU1fFE75F2WB-3wIx2dzR8LI0gvjzVRc6KR6FI/edit)是一家[基础设施即代码 (IaC)](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)公司，根据其研究表明，超过“[40% 的公司在正确部署基础设施之前会部署四次以上](https://learn.spacelift.io/the-infrastructure-automation-report-2025)”。

我不想这么说，但这听起来对我来说很正确。

为了解决这个问题，Spacelift 推出了一项新服务 [Saturnhead AI](https://spacelift.io/blog/introducing-saturnhead-ai)。[Spacelift](https://thenewstack.io/spacelift-scales-legacy-automation-terraform-first-ansible-next/) 的 CEO [Pawel Hytry](https://www.linkedin.com/in/hytry/) 在一封电子邮件中表示：“我们为从业者构建了 Saturnhead AI——那些过度劳累的工程师，他们应该在构建时却陷入了解读日志的困境。漂亮的仪表板和精美的图表可以帮助向高层受众传达特定时间点的性能。但是，真正有效的解决方案必须首先满足前线人员的实时需求，而这正是 Saturnhead AI 旨在提供的。它旨在快速解决失败的部署，并使 [DevOps](https://thenewstack.io/introduction-to-devops/) 团队能够以其组织和客户要求的速度前进。”

它通过审查您的 [IaC](https://thenewstack.io/introduction-to-infrastructure-as-code/) 运行器阶段日志、分析它们，然后提供关于特定运行器阶段中发生的事情或整个运行中发生的事情（如果出现故障）的清晰且可操作的反馈来实现这一点。通过自动化手动、耗时的故障排除过程并指导 DevOps 团队完成解决方案，Saturnhead AI 减少了解决时间并消除了运营瓶颈。

## 可操作的见解

此分析是使用生成式 AI (GenAI) 引擎进行的，该引擎可以实时分析基础设施运行日志。这为您提供了清晰、可操作的故障解释，将手动筛选日志的数小时变成瞬间洞察的几秒钟。使用哪种 AI？这取决于您。您可以将数据输入到您选择的大型语言模型 (LLM) 中。目前，您可以选择 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 的 [Bedrock (Anthropic)](https://aws.amazon.com/bedrock/claude/) 或 [Google Gemini](https://gemini.google.com/)。

当您运行它时，您将获得两个选项：

**Summarize:** 这提供了运行中每个步骤中发生的事情的概述。即使运行失败，这也会提供一个简单的报告。
**Explanation:** 这为失败的运行提供故障排除报告。运行的所有阶段（初始化、计划和应用）都经过分析，以提供：

- 识别出的问题：让您知道发生了什么。
- 可能的原因：告诉您为什么会发生这种情况。
- 行动步骤：提供您应该采取的逐步行动来解决问题。

该公司声称，通过使用 Saturnhead AI，即使运行失败率仅为 5%，Saturnhead AI 也能消除每周对 1,000 多次失败运行进行故障排除的需求。我不确定是否会有那么多失败的运行，但老实说，任何可以减少 DecOps 或 IaC 故障排除运行的东西，在我看来都是一种胜利。

如果您想试用 Saturnhead AI，您可以立即[创建一个 Spacelift 免费帐户](https://spacelift.io/free-trial)或与其中一位 IaC 专家[预约演示](https://spacelift.io/schedule-demo)。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.