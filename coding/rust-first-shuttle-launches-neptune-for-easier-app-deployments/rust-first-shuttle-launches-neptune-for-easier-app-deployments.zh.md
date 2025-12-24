[Shuttle](https://www.shuttle.dev/) 是一个 Rust 优先的开源基础设施即代码 (IaC) 云平台，用于部署应用程序。本周，该公司推出了 Neptune，一项旨在加速应用程序部署的新产品。

尽管开发人员可以在几分钟内生成整个后端，但部署应用程序仍然需要数天的设置和配置时间。这就是目前处于测试阶段的 Neptune 发挥作用的地方。Neptune 是一个“AI 平台工程师”，它完全不依赖特定语言，可以连接到任何代码仓库或 AI 编程工具。该[博客文章](https://www.neptune.dev/blog/introducing-ai-platform-engineer)将其比作后端基础设施的 Docker。

该公司在博客文章中表示：“它是一个 AI 原生的平台工程师，能够理解您的代码，知道其需求，并安全、可预测、快速地配置完整的云堆栈。”“它从一个部署助手发展成为一个真正的 AI 平台工程师，能够理解您的代码，智能地规划，并自动配置基础设施。”

文章补充说，它与 IDE 副驾驶和代理集成，实现了完全会话式的部署。它还具有云无关性和可扩展性，通过插件模型支持 AWS、GCP 和 Azure。

Neptune 提供了 PaaS 的简洁性，但允许开发人员使用自己的云账户。文章还指出，它提供了 IaC 的灵活性，但消除了维护周期。

团队表示：“由于您的基础设施是确定性规范，它始终与您的代码保持同步——而不是落后于代码。”“这实现了接近零的维护开销，并弥合了代码与云之间的差距。”

文章指出，Neptune 通过将三个组件连接成一个内聚系统来工作：一个确定性规范、一个 Kubernetes 原生控制平面，以及一个基于真实基础设施元数据的 AI 工作流。这三者共同将应用程序意图转化为生产就绪的云架构，且只需最少的配置。

[Neptune 测试版](https://www.neptune.dev/try-it-now)已向早期构建者开放。

## React 服务器组件中发现漏洞

根据 React 博客，本周安全研究人员[又发现了两个](https://thenewstack.io/react-server-components-vulnerability-found/) [React 服务器组件漏洞](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components)，其中一个可能导致拒绝服务攻击。

新问题包括一个高严重性拒绝服务漏洞和一个中严重性源代码泄露问题。[React](https://thenewstack.io/stop-blaming-react-for-your-state-management-hangover/) 团队建议开发人员立即升级。此外，团队警告说，如果您上周已经针对关键安全漏洞进行了更新，则需要再次更新。

团队表示：“如果您更新到 19.0.2、19.1.3 和 19.2.2 版本，这些更新是不完整的，您需要再次更新。”

React 团队补充说，如果您的应用程序的 React 代码不使用服务器，那么该应用程序不受这些漏洞的影响。如果应用程序不使用支持 React 服务器组件的框架、打包器或打包器插件，则也不会受到影响。

受影响的 React 框架和打包器包括：Next.js、React Router、Waku、@parcel/rsc、@vite/rsc-plugin 和 rwsdk。

## 微软公布 TypeScript 7.0 进展更新

TypeScript 的首席产品经理 Daniel Rosenwasser 最近发布了关于该语言将编译器和语言服务移植到原生代码的[进展更新](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)。

他写道，这项被称为 Project Corsa 的工作将有助于利用更好的原始性能、内存使用和并行性。这将是 TypeScript 7 的一个重大改变。他还介绍了该语言即将发布的路线图。

首先，他介绍了编辑器支持和语言服务的重写情况。他解释说，语言服务是驱动编辑器 TypeScript 和 JavaScript 功能的核心。

他表示，虽然团队仍在移植功能和修复小错误，但现有 TypeScript 编辑体验中的大部分功能已经存在并正在运行，其中包括：

*   代码补全（包括自动导入）
*   转到定义
*   转到类型定义
*   转到实现
*   查找所有引用
*   重命名
*   格式化
*   调用层级
*   文档符号

他写道：“您可能会注意到自上次重大更新以来的一些突出之处——自动导入、查找所有引用、重命名等。”“我们知道这些功能是许多开发人员尝试原生预览时所缺失的部分。我们很高兴地宣布，这些功能现已重新实现并可供日常使用！”

他补充说，他们还重新设计了语言服务的一部分，以提高可靠性，同时利用共享内存并行性。

他表示：“新架构更加健壮，应该能够毫无问题地处理大小代码库。”“虽然肯定还有更多的工作要移植和完善，但您的团队可能会发现尝试 TypeScript 的原生预览是值得的。您可以期待更快的加载时间、更少的内存使用量以及整体上更灵敏/响应更快的编辑器。”

编译器在原生移植方面也取得了进展。

他经常遇到的一个问题是，使用 TypeScript 7 验证构建是否安全；也就是说，它是否能可靠地发现 TypeScript 5.9 所发现的相同错误？

Rosenwasser 写道：“答案是肯定的。”“您今天可以放心地使用 TypeScript 7 对您的项目进行类型检查以查找错误。”

他指出，TypeScript 7.0 将不支持现有的 Strada API。Corsa API 仍在开发中，目前没有稳定的工具集成；这意味着任何依赖 Strada API 的工具（例如 linter、格式化程序或 IDE 扩展）都将无法与 Corsa 配合使用。

他表示：“解决其中一些问题的方法可能是将 typescript 和 @typescript/native-preview 包并行安装，并对需要它的工具使用 ≤6.0 API，同时使用 tsgo 进行类型检查。”