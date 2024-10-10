# 禅与 API 开发的艺术（和科学）

![禅与 API 开发的艺术（和科学）的特色图片](https://cdn.thenewstack.io/media/2024/09/e8ad8fa8-zen-api-development-1024x576.jpg)

构建、测试和部署自己的代码可能很痛苦，尤其是在时间紧迫且预算有限的情况下。协作和标准化必须成为该过程的一部分，我们需要共同努力，以便开发人员能够在不中断工作流程的情况下更长时间地停留在其内部开发循环中。

但一次又一次，我看到一些工具声称自己是“以开发人员为中心”或专注于开发人员体验，但它们却非常复杂、昂贵、复杂或抽象到需要手把手指导（想想“低代码”软件即服务 [SaaS]）。

API 开发也不例外。我认为 [API](https://thenewstack.io/api-management/) 可能更糟糕，因为它们在崛起成为“[现代应用程序的支柱](https://dev.to/ismailco96/understanding-apis-the-backbone-of-modern-applications-2n0n)”的过程中一直被忽视，而且它们有增殖的趋势。

根据 [apidays API 行业市场状况报告](https://www.apidays.global/industry-reports/)，41% 的公司拥有比应用程序更多的 API。更重要的是，F5 预测到 2030 年，我们将拥有 [20 亿个 API，其有效期为一年](https://www.f5.com/pdf/reports/f5-office-of-the-cto-report-continuous-api-sprawl.pdf)。同时，Salt 表示 [95% 的公司在生产中遇到了 API 漏洞](https://content.salt.security/state-api-report.html)。

## 正确进行 API 开发

为了使 [API 开发](https://roadmap.sh/api-design)（或未来的创新）正确进行，我们必须拥有合适的工具来完成这项工作。你无法通过管理来实现 API 的质量和一致性；你必须开发它。

我们如何使开发富有成效且有益？我们能否恢复一种模式，让开发人员在完成目标时获得满足感，而不是对旅程感到恐惧？我们能否帮助开发人员避免浏览无尽的 cryptic 文档，或对重复相同“简单”操作但不是他们想要的界面感到厌烦？

我（以及许多其他开发人员，我相信）在 20 多岁时怀着满腔热情投入开发工作的原因之一是，我一直喜欢挑战。（我从 8 岁就开始编程；这就是我如此热爱它的原因。）我想解决问题，我想“破解代码”，我经常寻找能够改善体验的酷炫技术和工具。另一方面，我不想做一些过于繁琐、手动和痛苦的事情，以至于它会 [从开发中吸走乐趣](https://thenewstack.io/7-step-plan-to-make-development-fun/)。我需要一个平衡的中间立场，我迫切地 [寻求和谐](https://www.forbes.com/councils/forbestechcouncil/2024/05/30/rethinking-api-management-should-you-unbundle-or-is-there-a-better-approach/)。

在 API 领域工作了几年，亲眼目睹了混乱之后，我意识到了一种 API 开发工具的愿景，它实现了这种平衡。我想要乐趣和挑战，但我也想要速度和敏捷性，以便快速创新和部署。今年，我的团队和我一起踏上了这段冒险之旅，我们创造了一些我认为能够应对这一挑战的东西。

## 介绍 Blackbird

[Blackbird](https://www.getambassador.io/products/blackbird/api-development) 于 2024 年 10 月 2 日正式发布，是一个 API 开发平台，可以帮助开发人员快速而周到地生成高质量的 API。我们设计它来支持开发人员，而不是妨碍他们，过度简化复杂的任务或侮辱他们的智力。
正如 apidays 在其报告中所说，“来自 Ambassador 的 Blackbird 等新工具能够增强 API 设计实践，并加快 API 设计流程中一些更繁琐的任务，并将输出转换为 OpenAPI 定义。”

这些工具利用 AI 和临时的生产环境来降低云支出并提高优化。它们还意味着花费更少的时间进行手动、无聊的工作，而将更多时间用于创新，这些创新让你最初对成为一名开发人员感到兴奋。如果你想看看它是如何工作的，[创建一个帐户并试一试](https://blackbird.a8r.io)。

## 展望 2025 年

展望未来一年，以下是我对将影响未来发展的想法。

### 开发更高的一致性

需要重复的是：你无法通过管理来实现 API 的质量和一致性；你必须开发它。开发 API 从创建规范开始——本质上是不仅描述 API 需要做什么，还需要描述如何对其进行编码以使其按预期工作。API 管理着眼于确保用户能够按预期访问 API，但核心责任在于代码编写和标准化。
一致性不仅体现在标准和文档流程中，还体现在对 API 的 [模拟和测试](https://www.getambassador.io/blog/streamline-development-effective-api-mocking) 方法上，以确保整个 API 生命周期中的质量和安全性。

### 开发的未来是暂时的
佛陀教导说，一切都是暂时的，宇宙中没有什么是本质的。无常一直都是一种趋势，但我认为在开发领域，我们正在看到向 [无服务器架构](https://www.getambassador.io/blog/enhancing-serverless-architecture-production-like-environments) 的更大转变，以及对临时、类似生产环境的启动的渴望。开发人员不再需要打电话给他们的基础设施团队来启动一个新的生产环境，仅仅是为了测试一两个 API。能够启动临时环境意味着你的开发人员很高兴并进行测试，而你的基础设施团队则不受干扰。它还减少了所有公司（无论大小）都必须处理的技术债务。

### 将 AI（温和地）融入您的工具堆栈
AI 是下一场淘金热，每个人都在争先恐后地抢夺自己的那一份。市场上充斥着“AI-this”和“[LLM](https://thenewstack.io/llm/)-that”，但许多工具只是花哨的 ChatGPT 包装器。许多人担心 AI 会取代开发工作，但更重要的是要保持平衡——“AI 可以帮助开发人员改进其 API 设计的中庸之道”，正如 apidays 在其报告中所写。

例如，API 规范生成现在几乎可以完全使用 AI 工具完成。您不再需要编写规范，因为它们已经存在。将节省的规范生成时间用于开发日中更令人兴奋的部分。

## 实现 API 禅
随着新年的迅速临近，技术领导者需要专注于少花钱、多生产（一个古老的二分法），并努力让它变得有趣。当云支出下降，您的开发人员感到赋能而不是沮丧时，每个人都会很高兴。融入正确的技术，拥抱一切的暂时性，并确保您所做的一切的一致性，是实现这一目标的途径。

要了解更多关于我的愿景，请在 11 月的 [API World](https://www.getambassador.io/events/api-world-2024) 与我交谈，我期待评估其他 2025 年 API 趋势。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以收看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)