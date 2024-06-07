# Kubernetes：48% 的用户在工具选择上遇到困难

![Kubernetes：48% 的用户在工具选择上遇到困难的特色图片](https://cdn.thenewstack.io/media/2024/06/87bb8b97-kubernetes-48-percent-struggle-with-tool-choice-2-1024x576.jpg)

也许 Kubernetes 生态系统变得过于复杂，以至于不利于自身发展。

在 Spectro Cloud 的一份 [新报告](https://info.spectrocloud.com/2024-state-of-production-kubernetes) 中接受调查的近一半 [Kubernetes](https://thenewstack.io/kubernetes/) 用户表示，他们在选择和验证要在生产环境中使用的基础设施组件时遇到了问题。

**主要原因：Kubernetes 的成熟度。**

根据调查参与者的回答，对于组织来说，选择实在太多了。在新报告中，48% 的人表示，他们发现很难从 [广泛的云原生生态系统](https://landscape.cncf.io/) 中决定使用哪些堆栈组件。这一数字从 Spectro Cloud 2023 年报告中表示同样观点的 29% 猛增。

“
[Spectro Cloud 2024 年生产 Kubernetes 状况”报告](https://info.spectrocloud.com/2024-state-of-production-kubernetes) 基于 4 月完成的一项调查。所有 416 名受访者都在拥有至少 250 名员工的组织工作，直接参与其组织对 Kubernetes 的使用，并且在生产中至少有一个 Kubernetes 集群。
”

调查参与者提到的痛点包括：

**更大的部署。**57% 的调查参与者报告称在生产中拥有超过 20 个集群，高于在 Spectro Cloud 2022 年报告中询问此问题时约 35% 的类似回答。

- 这与 2023 年 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention) [调查](https://www.cncf.io/reports/cncf-annual-survey-2023/) 中 39% 的人表示相同的说法相比较。（此统计数据仅来自在拥有至少 500 名员工的公司工作的调查参与者。）

**复杂性增加。**随着 Kubernetes 市场成熟，我们看到在 Kubernetes 中运行的工作负载数量有所增加，这些工作负载通常是支持 [可观察性](https://thenewstack.io/observability/)、[CI/CD](https://thenewstack.io/ci-cd/) 和服务网格等内容的其他云原生元素。57% 的受访者表示，他们的 Kubernetes 基础设施包含 11 个以上的不同软件元素，高于 2022 年告诉 Spectro Cloud 相同内容的 42%。

## 复杂性导致痛苦

复杂性带来了麻烦：不仅要选择哪些工具，还要确保它们都能很好地协同工作。

27% 的调查参与者表示，其堆栈元素的互操作性经常导致生产 Kubernetes 集群出现问题。高于 2022 年 Spectro Cloud 报告中表示同样观点的 11%。

此类互操作性问题很常见：只有 26% 的人表示他们很少遇到此类问题，这意味着大约四分之三的生产部署必须比应有的更多地处理问题。

- 对于在生产中运行 Kubernetes 的组织来说，出现了一系列新的挑战。除了调查参与者报告的难以选择所需的工具之外，配置漂移（45% 的人将其列为挑战，高于 2023 年 Spectro Cloud 报告中的 33%）以及难以防止安全漏洞（43%，高于 26%）是其他主要痛点。
- 合并、[收购](https://thenewstack.io/ibm-buying-hashicorp-what-devs-analysts-and-competitors-are-saying/) 和 [公司倒闭](https://thenewstack.io/end-of-an-era-weaveworks-closes-shop-amid-cloud-native-turbulence/) 可能会解决一些挑战。70% 的受访者表示，他们认为云原生生态系统已准备好进行市场整合。

## 采用平台工程的用户遇到的问题较少

[平台工程](https://thenewstack.io/platform-engineering/) 已成为在 Kubernetes 上运行分布式系统时解决复杂性过高和工具选择过多的问题的解决方案。Spectro Cloud 调查表明，这种做法可能会缓解其中一些问题。

- 在采用平台工程的 70% 的组织中，不到一半的人强烈认为它已被完全采用。
- 只有 22% 采用平台工程的组织经常遇到运行生产 Kubernetes 集群的问题，而 40% 的非平台工程采用者经常遇到这些问题。

![图表显示了采用和未采用平台工程的 Kubernetes 用户之间的差异，以及前者在 K8s 中遇到的问题较少。](https://cdn.thenewstack.io/media/2024/06/8cb67083-platform-engineering-kubernetes-2-1024x750.png)
**更正后的 Markdown 格式：**

**强烈或比较同意其组织已采用平台工程的调查受访者在生产 Kubernetes 中遇到的问题，与未采用平台工程的组织相比。**

来源：“Spectro Cloud 2024 生产 Kubernetes 现状”报告。

## 人工智能和边缘使用量不断上升

Kubernetes 看起来很可能在持续的人工智能革命中发挥重要作用。68% 的调查参与者表示，Kubernetes 基础设施对于充分利用其应用程序工作负载中的人工智能至关重要。

**其他与 Kubernetes 和人工智能相关的调查结果：**

- 与 Kubernetes 结合使用人工智能的最常见方式是帮助管理 Kubernetes 环境的人工智能助手（44% 报告了此用例）以及在云端或本地运行生产人工智能工作负载。此外，32% 的人报告使用 Kubernetes 在边缘运行生产人工智能工作负载。
- 基于边缘的 Kubernetes 用于生产的全面使用量已从 2023 年报告使用量的 7% 上升到 2024 年的 27%。算上部分部署，38% 的组织正在边缘使用 Kubernetes。这意味着几乎四分之三的边缘 Kubernetes 采用者已经在部署人工智能工作负载。

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)