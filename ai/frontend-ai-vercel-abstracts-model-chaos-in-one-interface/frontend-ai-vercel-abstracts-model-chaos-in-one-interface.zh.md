Vercel 推出了一项新服务，允许开发者通过单一界面试验不同的 AI 模型，而无需管理多个 API 密钥、提供商帐户或速率限制。

这家前端 Web 托管平台在周三于纽约市举行的年度用户大会 Vercel Ship 上，以公开 Beta 版的形式推出了 [Vercel AI Gateway](https://vercel.com/blog/ai-gateway)。

Vercel 首席技术官 [Malte Ubl](https://www.linkedin.com/in/malteubl/) 向 The New Stack 解释说，该网关使开发人员可以访问大约 100 个模型，从而抽象出与多个 AI 模型提供商合作的复杂性。

他说：“如果你曾经构建过任何应用程序，那么访问所有这些供应商并获取 API 密钥是非常乏味的。”

他解释说，这项新服务模仿了过去 25 年来开发者使用数据库的方式。它可以与该公司于 2023 年发布的 AI SDK 配合使用。

“我并不是说我要使用 Oracle SQL，我要使用 [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/)，我实际上是在使用这些访问系统，它们抽象了底层数据库，”他说。“你可以将 [AI SDK](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/) 基本上看作是相同的东西，你有一个 API，无论你与 [Gemini](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/) 交谈还是与 [OpenAI](https://thenewstack.io/openais-sam-altman-ai-is-now-ready-for-the-enterprise/) 交谈，都无关紧要。”

它还解决了开发者们的一个主要难题：简化了开发过程中切换模型的过程。他补充说，借助 AI Gateway，开发者可以使用他们的 Vercel 帐户访问大约 100 个模型，而无需额外的工作。

他说，开发者通常从前沿或大型生成式 AI 模型开始，这种模型很容易工作但成本很高，然后找到一个更小型的模型，该模型更精确地满足应用程序的需求，而且成本更低。AI Gateway 为开发者提供了一种简单的方法来试验不同的模型，从而找到适合其应用程序的模型。

他说：“它完全消除了开发过程中[尝试不同模型](https://thenewstack.io/should-you-try-small-language-models-for-ai-app-development/)的摩擦。你基本上只需要更改模型的名称，然后它就可以工作了。”

他说，一旦应用程序部署到生产环境，开发者就可以通过 Vercel 购买所选的模型。

他还补充说，AI Gateway 还有助于管理使用情况，因此如果一个来源出现故障，它将从另一个云提供商处获得相同的服务。

他说：“与你可能习惯的传统计算相比，所有这些供应商在稳定性方面都很糟糕。所以你肯定不是在说 99.9% 的可用性，而是在说大约 99% 的可用性。”

他解释说，基本上，它充当了生产环境的 AI 模型负载均衡器代理服务器。开发者还可以携带他们自己的 API 密钥，Vercel 可以通过 AI Gateway 向你收费。

它在成本方面也是透明的，而且 Vercel 以市场价销售所有产品 —— 没有加价，他补充说。

## Vercel 的 AI 部署沙箱

在另一项 AI 举措中，这家前端 Web 托管公司还推出了 [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox)，允许用户安全地运行不受信任的代码，例如在 Vercel 的基础设施上由 AI 创建的代码。它目前处于 Beta 版。

它基本上是 Vercel 的“基础设施即服务”策略，允许开发者以安全的方式运行由 AI 创建的未经验证的代码。

他解释说，这不适用于开发者提交代码以进行代码审查的情况，而是适用于在生产环境中生成代码的应用程序。

他说，Vercel 采用了自己的沙箱基础设施，并将其作为服务提供。

他说：“你正在为你的客户构建这个应用程序，你的客户提示生成代码 —— 你想运行它。它基本上将我们构建的基础设施变成了一个平台。我们每天进行超过 100 万次构建，因此它非常稳定，是一个可用于生产的基础设施，经过打包以便在这种 AI 环境中易于使用。”

从本质上讲，开发者获得了一个安全的虚拟机，该虚拟机经过优化，可以运行可能不安全的代码。它没有针对规模进行优化，而是运行一次以确保代码安全，或者在出现错误时识别问题所在。他补充说，该沙箱基本上没有任何访问权限，除非开发者授予它权限。

在本周 Ship 的其他新闻中，Vercel 宣布推出 [**滚动发布**](https://vercel.com/changelog/rolling-releases-are-now-generally-available)，这是一项新的平台功能，可将新的部署逐步推广到一部分用户。该公司表示，与自定义推广逻辑不同，它已集成到平台中，并实时监控部署运行状况。

默认情况下，部署从 20% 的流量开始，然后随着时间的推移自动或手动进行转移。

它还降低了不良部署影响 100% 用户的风险，并为团队提供了一个窗口来捕获回归 —— 例如损坏的结帐、后端错误或性能下降 —— 从而避免影响所有流量。

它还宣布了 **[Fluid Compute 的主动 CPU 定价](https://vercel.com/blog/introducing-active-cpu-pricing-for-fluid-compute)**，这将不再对空闲时间收取计算费率，他说。

Fluid Compute 是 [Vercel 的计算模型](https://thenewstack.io/vercel-rolls-out-more-cost-effective-infrastructure-model/)，旨在通过结合无服务器和传统服务器架构来处理现代的动态工作负载，如 AI 和流媒体。

“每个请求都将使用一定数量的 CPU，你需要为此付费，但某些极端情况实际上变得很重要，”Ubl 解释说。

例如，如果开发者有一个应用程序甚至无法填满 CPU，因为没有足够的用户。开发者不会为整个 CPU 付费，而是只为三个用户付费，他解释说。

“这就是我们的主动 CPU 如此出色的原因，因为你只需为 CPU 付费，如果你只有三个用户，那么你就为三个用户付费，”他说。“你无需为整个盒子付费。”

最后，Vercel 宣布 **一流支持 [微前端](https://thenewstack.io/4-lessons-learned-from-building-microfrontends/)**。Ubl 说，Vercel 之前允许使用微前端，但这需要希望部署该架构的组织提供大量的硬编码支持。现在，[Vercel 构建了各种功能](https://vercel.com/docs/microfrontends)，使开发者可以轻松地部署微前端，而无需进行太多的自定义工作。

Ubl 指出，这些举措使 Vercel 更好地支持代理式 AI。

“总体的目标是将 Vercel 变成托管 AI 应用程序，特别是代理式应用程序的首要平台，”Ubl 说。