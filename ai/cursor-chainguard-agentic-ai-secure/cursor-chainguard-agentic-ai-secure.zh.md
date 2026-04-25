[Cursor](https://thenewstack.io/cursor-3-demotes-ide/) 和 [Chainguard](https://www.chainguard.dev/) 正致力于保护 [AI 生成代码](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/)中的开源依赖链。随着智能体开发（Agentic Development）从实验转向生产，这一问题变得愈发尖锐。

双方本周宣布的合作让 Cursor 能够访问 Chainguard 的 [加固容器镜像](https://thenewstack.io/dockers-sets-free-the-hardened-container-images/) 目录和语言库，将供应链保护直接嵌入编码工作流。两家公司表示，当 Cursor 的智能体选择依赖项时，现在可以从 Chainguard 的经过验证的工件库中提取，而非原始的公共注册表。

## 智能体不会停下来检查

Cursor 的全球营收与现场业务总裁 [Brian McCarthy](https://www.linkedin.com/in/bkmccarthy/) 告诉 *The New Stack*：“与 Chainguard 合作是 Cursor 实现大规模安全智能体编程的又一举措。最近的供应链攻击展示了恶意分子如何操纵我们历史上依赖的公共工具和注册表来获取开源内容。”

> “随着全球顶尖企业的多数代码由智能体编写，这种能确保代码可信并能进行大规模快速审查与监控的新工具，创造了一个更安全的范式。”

事实上，这一时机反映了一个真实且有记录的威胁模式。针对包括 Trivy、LiteLLM、telnyx 和 axios 在内的项目的供应链攻击表明，受损包极易在开发者生态系统中传播。所谓的 Shai-Hulud 恶意软件活动证明，恶意分子正积极瞄准 [PyPI](https://thenewstack.io/whos-keeping-the-python-ecosystem-safe/)、npm、Maven Central 等注册表，而 AI 智能体越来越多地将这些注册表视为依赖解析的“真理之源”。

[Chainguard](https://c67dcd9a.streak-link.com/C2uzyXrVldVCtIchdgDQ0p2d/https%3A%2F%2Fwww.chainguard.dev%2F) 的资深产品营销经理 [Ross Gordon](https://www.linkedin.com/in/rosscgordon/) 告诉 *The New Stack*：“开发者可以使用自然语言指示 Cursor 将项目迁移到 Chainguard。”

随后，Cursor 会更新项目配置，管理凭据，并将依赖解析路由到 Chainguard 的目录，而非 PyPI、[npm](https://thenewstack.io/18-popular-npm-packages-compromised-in-attack/) 或 Maven Central 等公共注册表。这是在 Cursor 的 IDE 或智能体层面处理的，而不是通过外部网络控制。

正如两家公司所描述的，[智能体开发](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/)的核心问题在于：依赖决策是以机器速度发生的，缺少了历史上作为最后一道防线的手动审查。Chainguard 首席执行官兼联合创始人 [Dan Lorenc](https://www.linkedin.com/in/danlorenc/) 在一份声明中表示：“AI 智能体正在以任何安全团队都无法手动审查的规模和速度做出依赖决策。”

## 威胁模式已初现端倪

这种集成专注于通过确保库和容器镜像来自受信任且可公开验证的来源，从而减轻 AI 生成代码中开源工件漏洞带来的风险。

“[Ross Gordon](https://www.linkedin.com/in/rosscgordon/) 表示：‘这解决了智能体开发中的一个关键风险层：大规模自动化选择外部工件。’‘另一种选择是让开发者审查每一个使用的库，对于某些应用来说，这可能超过 1,000 个。Chainguard 工件并未受到最近针对流行开源工件的供应链攻击的影响，我们的客户一直在持续交付，而无需评估是否受影响或更换凭据。’”

根据合作协议，共同客户可以访问 2,300 多个容器镜像，Chainguard 会持续重新构建这些镜像以包含上游补丁，并在发布时确保零已知 CVE（常见漏洞与披露）。该集成还涵盖了数百万个 [Python 版本](https://thenewstack.io/what-is-python/)、[JavaScript](https://thenewstack.io/introduction-to-javascript/) 和 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 库，这些库完全由可公开验证的源构建，旨在针对近期的攻击载体——带后门的二进制文件和恶意安装脚本。

来源（Provenance）通过签名的构建证明和可重现的构建流水线来处理。Cursor 自动管理凭据配置，因此开发者无需修改现有工具或工作流即可获得覆盖。

## 数小时内重新构建

Chainguard 在上游源代码修复可用时立即重新构建其镜像，持续努力实现零 CVE 状态。

“[Ross Gordon](https://www.linkedin.com/in/rosscgordon/) 说：‘这些重建通常在发布新版本后的几小时内发生，客户可以直接从 Chainguard 的注册表提取新版本，或者镜像到他们的工件管理器以自动化方式提取。容器镜像会频繁重建，并涵盖在我们的补救时间表内，以确保在修复可用时立即并入。’”

这种合作为 Chainguard 在智能体开发工作流中占据了一席之地，而不是将供应链安全视为事后审计步骤——随着 AI 编程工具从助手转向自主智能体，该公司一直在推动这一定位。对于 Cursor 来说，这承认了确保 AI 生成的代码安全不仅需要审查输出，还需要从源头控制智能体引入的内容。

该集成现已面向 Chainguard 和 Cursor 的共同客户开放。