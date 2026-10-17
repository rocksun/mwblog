<!--
title: 员工正通过氛围编程自建应用，Cloudflare开源Void帮助IT部门进行有效管控
cover: https://cdn.thenewstack.io/media/2026/10/10c0e182-ubaid-e-alyafizi-3ll8bdtzqya-unsplash-scaled.jpg
summary: 随着员工利用AI进行氛围编程日益流行，Cloudflare开源了Void平台，帮助企业IT部门对员工自建应用进行部署、管理和安全管控。
-->

随着员工利用AI进行氛围编程日益流行，Cloudflare开源了Void平台，帮助企业IT部门对员工自建应用进行部署、管理和安全管控。

> 译自：[Employees are vibe-coding their own apps. Cloudflare open-sources Void to give IT a handle on them](https://thenewstack.io/cloudflare-voidzero-void-vibe-coding/)
> 
> 作者：Paul Sawers

许多公司都热衷于让员工利用AI构建自己的应用程序，即使是那些几乎没有或根本没有编程经验的员工也是如此。就在昨天，*The Pragmatic Engineer* 的 Gergely Orosz [highlighted the likes of Ramp and Stripe](https://newsletter.pragmaticengineer.com/p/the-pulse-new-trend-of-building-internal-aeb)，这些公司开发了内部工具，允许非工程师创建供同事使用的软件。

但这这种新获得自由也给IT部门带来了头痛的问题。谁来追踪这些应用程序，它们可以访问哪些公司数据，谁又负责确保它们的安全？在许多方面，[氛围编程应用就是新的影子IT](https://thenewstack.io/vibe-coded-shadow-it/)，员工部署的软件超出了其IT团队的监督范围。

这就是Cloudflare想要为这种局面带来秩序的原因。周四，该公司[宣布](https://blog.cloudflare.com/deploy-with-void/)发布了 [Void](https://void.cloud/)，这是一个包含三个开源工具的集合，其中包括一个自托管平台，企业可以在其中部署和管理员工用AI构建的应用程序。其理念是为员工提供一个发布其作品的地方，同时让管理员控制*谁*可以部署和访问它们。

## Cloudflare不断壮大的JavaScript帝国

在过去的一年里，Cloudflare积累了相当丰富的JavaScript专业知识。就在上周，[该公司宣布收购Deno](https://thenewstack.io/cloudflare-acquires-deno-ryan-dahl/)，这家由Node.js创始人 [Ryan Dahl](https://www.linkedin.com/in/tinyclouds/) 创立的JavaScript运行时公司。早在1月，[它就收到了Astro背后的团队](https://thenewstack.io/cloudflare-acquires-team-behind-open-source-framework-astro/)，这是一个开源Web框架。然后在6月，[它收购了VoidZero](https://thenewstack.io/cloudflare-voidzero-acquisition-vite/)，这是一个由 [Vue.js](https://vuejs.org/) 和 [Vite](https://vite.dev/) 创始人 [Evan You](https://www.linkedin.com/in/evanyou/) 创立的开源工具公司。

这三家公司都在JavaScript生态系统中运营，尽管它们在Web框架、开发工具和服务器端运行时方面拥有不同的专长。

You 于2024年10月[正式公布了VoidZero](https://voidzero.dev/posts/announcing-voidzero-inc)，其创立使命是将开发者编写JavaScript时依赖的分散工具整合在一起。它已经拥有相当深厚的开源背景，其团队为Vite和 [Vitest testing framework](https://vitest.dev/) 等成熟项目做出了贡献，同时还开发了基于Rust的 [Rolldown](https://rolldown.rs/) 打包工具和 [Oxc](https://oxc.rs/)（一组用于处理和分析JavaScript代码的工具）。

2025年10月，VoidZero [宣布推出 Vite+](https://voidzero.dev/posts/announcing-vite-plus)，这是一项旨在将其各种开发工具整合到一个命令行界面（CLI）下的举措。Vite+最初被构想为商业产品，最终于3月在MIT许可证下[发布为开源版本](https://voidzero.dev/posts/announcing-vite-plus-alpha)，而在同月，该公司[还推出了Void](https://www.youtube.com/watch?v=Bp86buftbX8)，这是一个针对Vite应用程序的抢先体验部署服务，他们希望借此为其开源生态系统创造收入渠道。

> “我们在被收购之前就开始开发Void，最初旨在将其打造为商业产品。但现在我们不再需要这样做了，所以我们将其开源了！”

自从[Cloudflare收购案](https://www.cloudflare.com/press/press-releases/2026/cloudflare-aquires-voidzero-to-build-the-future-of-the-ai-native-web/)以来，Vite+继续发展，在夏天进入Beta测试阶段，并在[9月底](https://blog.cloudflare.com/voidzero-update/)发布了稳定的1.0版本。但可以说，最大的变化发生在Void上，Cloudflare的所有权促使人们重新思考如何提供该部署平台。事实上，这次收购减轻了VoidZero寻找自身收入来源的压力，You在周四宣布消息后在X上承认了这一点。

“我们在被收购之前就开始开发Void，最初旨在将其打造为商业产品，”You [写道](https://x.com/evanyou/status/2110747206584267234)。“但现在我们不再需要这样做了，所以我们将其开源了！”

## 进入虚空：通过Vite构建全栈应用

Void包含三个主要组件，每个组件服务于不同的目的。[Void SDK](https://github.com/voidzero-dev/void) 为使用Vite创建全栈应用程序提供了构建块，包括服务器端功能以及与数据库和其他服务的集成。与此同时，[Void CLI](https://void.cloud/reference/cli) 处理部署，自动配置必要的Cloudflare资源，而 [Void Platform](https://void.cloud/guide/self-hosted-platform) 提供了一个共享环境，公司可以在其中托管应用程序并通过管理控制台进行管理。

SDK和CLI此前已经通过npm以MIT许可证分发，但周四发布的版本将包括平台在内的完整源代码与Void 1.0一起公开。

运行 `void deploy` 会启动应用程序构建、配置所需的基础设施，并将完成的应用程序发布到Cloudflare，包括应用任何必要的数据库迁移。

![Deploying a Vite application to Cloudflare via the Void CLI. ](https://cdn.thenewstack.io/media/2026/10/d0b7941a-voiddeploygif.gif)

*通过Void CLI将Vite应用程序部署到Cloudflare。（图片来源：Cloudflare）*

自托管平台标志着对VoidZero最初计划的重大偏离。[Michael Dong](https://x.com/mdong1909) 从VoidZero加入Cloudflare，现在担任公司的策略主管，他表示这次收购促使对该技术进行了重大重构。

> “在Cloudflare收购VoidZero之后，我们从头开始重新构建了该平台，使其成为任何人都可以安装并在Cloudflare上自托管的平台。”

“在Cloudflare收购VoidZero之后，我们从头开始重新构建了该平台，使其成为任何人都可以安装并在Cloudflare上自托管的平台，”Dong告诉 *The New Stack*。

公司可以使用 `void platform install` 命令安装他们自己的实例，该命令会引导管理员完成身份验证、数据库连接和存储的设置。

![Installing a self-hosted Void Platform.](https://cdn.thenewstack.io/media/2026/10/811f1a2a-voidplatformgif.gif)

*安装自托管的Void Platform。（图片来源：Cloudflare）*

与此同时，最初的Void Cloud服务仍在私下运行。[Christoph Nakazawa](https://www.linkedin.com/in/cnakazawa/) 曾是VoidZero的产品主管，现在是Cloudflare的工程总监，他表示访问权限仅限于公司自己的团队和一小群受邀测试人员。

“它从未公开提供过，”Nakazawa告诉 *The New Stack*。

Dong还表示，已有100多名Beta用户通过Void SDK部署了应用程序，尽管他没有明确说明他们使用的是Void Cloud还是直接部署到Cloudflare。

## 管控员工的应用程序

Void Platform赋予管理员确定谁可以部署应用程序以及谁可以访问它们的权力。他们还可以检查部署、审查日志、监控资源消耗并施加使用限制。与身份提供商和Cloudflare Access的集成允许公司将应用程序限制为授权员工。

Void还提供了部署后用于排查应用程序故障的工具。开发人员可以通过CLI检查错误日志，并将有问题的部署回滚到早期版本。

![Inspecting application error logs and rolling back to a previous deployment.](https://cdn.thenewstack.io/media/2026/10/39fffedb-voidlogsgif.gif)

*检查应用程序错误日志并回滚到先前的部署。（图片来源：Cloudflare）*

Dong表示，Cloudflare已经在内部使用Void Platform，企业身份验证提供了一种保护措施，可防止员工无意中暴露公司信息。

“我们在Cloudflare拥有一个Void Platform，只有员工可以访问，默认情况下可防止通过氛围编程应用导致的数据泄漏，”Dong说。

然而，这种保护也是有局限性的。限制对应用程序的访问并不一定能阻止该应用程序检索敏感信息或将其发送到其他地方。此外，Void的[文档](https://void.cloud/guide/platform/administration/zero-trust)确认，管理员可以将新应用程序配置为默认公开，而各个项目所有者随后可以使他们自己的应用程序公开访问。

Void记录的部署流程在应用程序上线之前也没有强制性的IT安全审查。当被问及管理员是否可以在部署前审查或批准应用程序时，Nakazawa指出了该平台现有的访问控制以及公司扩展这些控制的自由度。

> “由于Void是开源的，其他公司可以根据自己的需求调整平台。”

“由于Void is 开源的，其他公司可以根据自己的需求调整平台，”Nakazawa说。

这可能意味着开发额外的批准机制或更具限制性的访问策略，尽管组织必须自己实施这些措施。

这里还有成本问题。自托管Void Platform的公司需要付费的 Cloudflare Workers for Platforms 计划，起价为每月25美元，并根据使用情况收取额外费用。安装还需要R2存储和单独托管的PostgreSQL数据库，从而带来更多潜在费用。

Dong证实，使用Void SDK直接将应用程序部署到Cloudflare的开发人员不需要付费的Cloudflare计划。然而，希望Cloudflare为其运营Void Platform的公司目前则无法如愿，因为目前没有完全托管的版本可供使用。

因此，对Cloudflare而言，将Void开源具有潜在的商业收益。虽然软件本身是免费提供的，但运行自己的Void Platform的公司将消耗Cloudflare的基础设施，并产生所有相关成本。实际上，Cloudflare有望通过为其提供动力的底层服务，从该软件更广泛的采用中获益。

这些基础设施要求引发了另一个问题：Void与Cloudflare的绑定会有多紧密？Cloudflare已承诺保持Vite和VoidZero的其他成熟开发工具保持厂商中立，而Void的自动基础设施配置目前取决于Cloudflare。Nakazawa表示，这反映了该平台的起源，Void从一开始就是围绕Cloudflare的基础设施设计的。

随着开源项目的发展，这种情况可能会改变，尽管Nakazawa并未明确承诺支持竞争对手的云服务提供商。

“既然它是开源的，我们期待与社区合作，为提供相同基准功能的其他提供商提供支持，”Nakazawa说。