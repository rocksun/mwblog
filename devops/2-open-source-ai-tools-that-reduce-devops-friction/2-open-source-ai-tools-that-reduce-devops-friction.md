
<!--
title: 两个开源 AI 工具，减少 DevOps 摩擦
cover: https://cdn.thenewstack.io/media/2024/09/d3665d01-open-source-ai-tools-devops.png
-->

AI 作为代码 (AIaC) 和 K8sGPT 是减少工作量的命令行工具，可自动执行生成 IaC 代码和排查 Kubernetes 故障等任务。

> 译自 [2 Open Source AI Tools That Reduce DevOps Friction](https://thenewstack.io/2-open-source-ai-tools-that-reduce-devops-friction/)，作者 Eran Bibi。

AI 在各个行业都扮演着变革性的角色。虽然有些人担心 AI 可能会导致[像天网一样的反乌托邦接管](https://www.firefly.ai/blog/chatgpt-can-code-iac-for-devops)，但我相信在我们达到那一点之前，还有很多空间可以进行创新和提高效率。这就是为什么我们正在大力投资构建 AI 驱动的云解决方案，以帮助团队更好地控制云（以及 AI 本身）。

我将分享一些真实的、实用的例子，说明如何通过两个开源工具将 AI 用于更高的[DevOps](https://thenewstack.io/devops/) 效率：AI 作为代码（[AIaC](https://aiac.dev/)) 和以[Kubernetes](https://thenewstack.io/kubernetes/) 为中心的[K8sGPT](https://k8sgpt.ai/)。

## DevOps 中的 AI 格局

使用 AI 时，首先想到的可能是使用 Stable Diffusion、DALL-E 2 和 Midjourney 等工具进行图像生成或内容创作，这些工具使将文本提示转换为令人惊叹的视觉效果成为可能。但 AI 的潜力远远超出了这些创造性的应用，进入了技术领域，特别是在 DevOps 中。

想象一下，您在 DevOps 中每天使用的工具——比如 Kubernetes (K8s)、Open Policy Agent (OPA) 或 Argo CD——可以转变为类似人类的助手。我们正在探索这种创新，使用 AI 来创建这些工具的人类化表示。

除了生成图像或视频的新奇性之外，AI 的真正力量在于它能够解析大量基于文本的数据。它可以将这种理解转化为生成代码（本质上是文本），然后将这种知识应用于诊断问题，甚至自动化基础设施管理。

我们决定测试这些新的领域，看看生成式 AI (GenAI) 在这些领域的表现如何，这些领域需要大量的人工工作。我们想看看 GenAI 对于典型的、常见的 DevOps 使用案例，能达到多接近人类的结果。

## 使用 AIaC 自动化代码生成

代码生成是 AI 对 DevOps 产生重大影响的最重要方式之一。一个很好的例子是 GitHub Copilot，它从新颖到广泛采用，甚至比 GitHub 预计的还要快。这也是为什么像[AWS](https://aws.amazon.com/?utm_content=inline+mention) 这样的竞争对手正在投入大量研发时间来生产和升级像[Amazon Q](https://aws.amazon.com/q/) 这样的竞争工具。

DevOps 是建立在将所有基础设施都转换为代码的基础上的，也就是[基础设施即代码 (IaC)](https://thenewstack.io/infrastructure-as-code/)。这包括部署管道、监控、存储库——任何基于配置构建的内容都可以用代码表示。这就是 ChatGPT 和 AIaC 等 AI 工具发挥作用的地方。

AIaC 是一款开源命令行界面 (CLI) 工具，使开发人员能够直接从终端使用自然语言提示生成 IaC 模板、shell 脚本等。这消除了手动编写和审查代码的需要，使流程更快、更不容易出错。

例如，当[为 Node.js 应用程序创建 Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) 并牢记安全最佳实践时，只需用自然语言描述需求，AIaC 就可以生成一个安全的 Dockerfile：

```aiac dockerfile for nodejs with comments```

这种方法扩展到生成 Kubernetes 清单、Helm 图表，甚至为 OPA 生成 Rego 中的策略配置。随着 DevOps 团队需要了解的配置语言和领域专业知识越来越多，这可以显著降低学习曲线和入门门槛。能够重新提示和改进输出有助于您获得所需的精确配置，并针对特定环境进行定制。

由于直接通过浏览器使用 GPT 模型并不总是高效的，尤其是在生产环境中，我们开发了 AIaC 作为 CLI。我们相信这使得将 AI 驱动的代码生成集成到现有工作流程中变得简单明了。

## 使用 K8sGPT 诊断和解决 Kubernetes 问题

虽然生成代码是一个强大的 AI 用途，但诊断和解决像 Kubernetes 这样的复杂系统中的问题可能更有价值。这就是 K8sGPT 的用武之地，K8sGPT 是云原生计算基金会 ([CNCF](https://cncf.io/?utm_content=inline+mention)) 沙箱中最近的[条目](https://github.com/cncf/sandbox/issues/38#issuecomment-1862551641)。K8sGPT 由[Alex Jones](https://github.com/AlexsJones) 开发，他是 CNCF 社区中长期贡献者和倡导者，是一款开源工具，使用 AI 分析和诊断 Kubernetes 集群中的问题。

在终端中执行命令即可轻松运行 K8sGPT。该工具连接到 Kubernetes 集群，识别问题并使用 AI 提供人类可读的解释和潜在的修复方案。例如，如果 Pod 处于挂起状态，K8sGPT 可以分析情况并建议纠正措施，例如修改亲和性选择器或调整资源限制。

这种 AI 驱动的方案显著减少了排查 Kubernetes 问题所需的时间和专业知识，它建立在已知和常见问题之上。即使是那些没有深入 Kubernetes 知识的人也能有效地管理和维护集群。它还从 AI 的解释和建议中学习，因为 K8s 已经存在了十年，许多挑战都已记录在案并得到解决。

## AI 在 DevOps 中的未来

AI 在 DevOps 中的应用仍处于起步阶段，但随着新的开源和商业服务的推出，它正在迅速发展。创新的快速步伐表明，AI 很快将嵌入到大多数 DevOps 工具中。从使用 AIaC 自动生成代码到使用 K8sGPT 进行高级诊断，可能性似乎无穷无尽。

Firefly 不仅仅是在观察这场革命，它还在积极地推动这场革命。通过将 AI 整合到 DevOps 工作流程中，团队可以更聪明地工作，而不是更努力地工作。无论是通过 AIaC 等开源项目，还是在 Kubernetes 中采用 AI 驱动的诊断，我们都在帮助铺平一条道路，让 AI 成为 DevOps 工具包中不可或缺的一部分。

随着这些工具的不断发展，我们不能忘记安全和隐私问题。GenAI 工具是第三方工具，确保敏感（内部或客户）数据在与 AI 模型交互期间不会泄露至关重要，尤其是在使用免费或实验性版本的 AI 工具时。您可能希望选择付费版本或基于 API 的集成，这些版本或集成可以提供更多对数据隐私的控制。

## 总结

AI 不再仅仅是一个流行语，它是一个实用且强大的工具，可以显著提高 DevOps 的效率。通过采用 AIaC 和 K8sGPT 等 AI 驱动的工具，可以减少工作流程中的摩擦，提高团队生产力，并使组织在竞争日益激烈的环境中保持领先地位。
