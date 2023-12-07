<!--
title:Vercel推出Monorepo支持新特性
cover: https://cdn.thenewstack.io/media/2023/12/487192f5-parvana-praveen-36mmes3ckde-unsplash-1-1024x768.jpg
-->

Vercel推出Developer Experience Platform平台新功能，以便更好支持monorepos，如变更审批等。

> 译自 [Vercel Adds New Features Designed to Support Monorepos](https://thenewstack.io/vercel-adds-new-features-designed-to-support-monorepos/)，作者 Loraine Lawson 是一位资深的技术记者，她曾覆盖从数据整合到安全等技术问题 25 年。在加入 The New Stack 之前，她担任银行技术网站 Bank Automation News 的编辑。她拥有......
来自 Loraine Lawson 的更多内容

前端开发公司 Vercel 在周二推出了[开发者体验平台](https://vercel.com/products/dx-platform)的新功能，以更好地支持单 monorepos，包括在代码发生变化时通知代码所有者，以及在问题到达生产环境之前自动检测问题。

[monorepos](https://thenewstack.io/devpod-ubers-monorepo-based-remote-development-platform/)以前是仅仅大型科技公司才采用的方式，但现在越来越多的公司也在采用这种方式。到目前为止，Vercel 的体验是基于多个单独的存储库，而不是monorepos，后者是在一个存储库中包含多个项目。根据 JetBrains 的[一项调查](https://thenewstack.io/jetbrains-developer-survey-tracks-rapid-adoption-of-ai-chatgpt/)，使用微服务的 [20% 的 Web 前端开发者](https://www.jetbrains.com/lp/devecosystem-2023/development/#microservices)采用了monorepos架构。Vercel 产品副总裁 [Lee Robinson](https://www.linkedin.com/in/leeerob/) 表示，最近随着越来越多的公司采用monorepos架构，Vercel 也看到了这种转变。

"monorepos长期以来只在[大公司](https://thenewstack.io/can-companies-really-self-host-at-scale/)如 Meta 和谷歌这类大型公司中流行，因为它们需要大量投资才能让工程团队在存储库中使用它们，" Robinson 在接受 New Stack 的采访时说。“我们还没有真正看到方程式的另一部分，即‘好的，我有monorepos。现在，我该如何设置一些防护栏杆？我该如何为我的monorepos的不同部分设置一些规则和所有权？’我们还没有看到这部分内容真正进入一个可以在大公司之外广泛使用的产品。"

## 在生产前删除错误

他补充说，尽管这[三个新功能](https://vercel.com/blog/introducing-conformance)在monorepos之外也很有用，但它们可以发挥作用。第一个称为符合性，意思是遵循某事物的规则或标准，这正是它的作用：它本质上是一个规则引擎，用于检查代码是否没有遵循某些规则，并向开发者发出关于关键错误和性能问题的警报。

他说："非常常见的是，许多构建软件的团队在影响生产的问题上遇到问题。可以这样理解符合性：总结我们在帮助许多许多团队构建软件项目、使用我们的框架和工具(如 [Next.js](https://thenewstack.io/vercels-next-js-14-introduces-partial-pre-rendering/))的经验，并将其转化为一套可以在代码库上运行的可重复规则。"

![](https://cdn.thenewstack.io/media/2023/12/8f5bffb5-conformance.png)

*符合性现在是 Vercel 开发者体验平台的一部分。*

他说，开发者在进行多次更改后，看到一个错误进入生产并导致客户问题，这并不罕见。然后，开发者必须在热修复和回滚代码之间做出选择，以将其移出生产环境。符合性可以检查代码库以确保其正确性，并防止问题实际上进入生产环境。

"这并不是说那些问题或错误会消失，因为错误会一直存在，" Robinson说。"但是，我们能够在工具箱中添加的更多工具有助于我们在保持整体快速移动的同时减少[错误数量](https://thenewstack.io/5-takeaways-from-smartbears-state-of-software-quality-report/)，这可以改进我们正在创建的软件的质量，并让团队更有信心进行变更。"

他补充说，有时候问题不在于特定错误，而在于大量的编码错误积累并导致性能下降。

他说："在深入调试之前，性能问题的根源并不总是一开始就很明显。随着时间的推移，我们注意到了一些特定的模式。"

例如，一个常见的痛点是调用数据库或内容管理系统获取数据的代码。编写这种代码有更快的方式，也有不那么快的方式，Robinson 指出。符合性可以立即提供反馈来帮助优化代码。

Vercel 的客户初创公司 [Upstart](https://www.upstart.com/) 在正式发布之前使用了该工具，并看到页面加载性能提高了 200 毫秒，Robinson 说。

"这就像他们得到了代码审核。基本上，他们运行了我们的工具，看到了一些可以优化的地方，并能够根据该指导和反馈进行调整，"他说。

## 对monorepos的更多支持

代码所有者是另一项新功能，它允许团队分配谁对代码负责——[包括安全团队中的成员](https://thenewstack.io/the-limits-of-shift-left-whats-next-for-developer-security/)——并确保如果代码发生更改，他们会收到通知，以便可以进行检查。

“通过代码所有者，根据我可能非常大的代码库，并制定了一系列规则，我可以定义谁有权批准和否决规则或对规则做出例外，当与安全相关的代码发生更改时，应通知谁，”Robinson说。

当然，符合性和代码所有者不是开源的，但会与开源工具集成，包括 [Turborepo](https://turbo.build/)，这是一个为 [JavaScript ](https://thenewstack.io/whats-next-for-javascript-new-features-to-look-forward-to/)和 TypeScript 优化的[增量打包和构建系统](https://thenewstack.io/turborepo-speedy-builds-for-javascript-monorepos/)，使用 [Rust](https://thenewstack.io/rust-is-surging-ahead-in-webassembly-for-now/) 编写并由 Vercel 维护。

最后，开发者体验现在有一个新的控制面板，支持代码运行状况的见解和对新团队成员的更好引导。

他补充说，所有这三个都有助于进一步支持monorepos。

“通过符合性和代码所有者，我们真正帮助团队——特别是较大的企业团队——采用monorepos架构，并提供一个控制面板体验，将这两者结合起来，” Robinson说。“现在在 Vercel 上使用此符合性工具以及我们的控制面板的优点是，您可以看到您为monorepos定义的所有者与代码的特定部分、特定软件包及monorepos的关系。因此，您可以在一个快照中对整个代码库的运行状况有一个很好的概览。”

