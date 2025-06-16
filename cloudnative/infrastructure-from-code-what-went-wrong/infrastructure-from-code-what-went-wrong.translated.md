# 代码构建基础设施：哪里出了问题

![代码构建基础设施：哪里出了问题 的特色图片](https://cdn.thenewstack.io/media/2025/05/4e5c6ab7-ifc-control-1024x573.png)

[代码构建基础设施](https://thenewstack.io/infrastructure-as-code-is-dead-long-live-infrastructure-from-code/) (IfC) 背后的理念是，你可以简单地用你选择的编程语言写出所有的部署和配置步骤，然后就完成了——不再需要担心你的应用程序如何在云中运行。这是从[基础设施即代码](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/) (IaC) 工具（如 [Terraform](https://thenewstack.io/red-hat-ansible-and-hashicorp-terraform-will-be-coming-together/) 和 [OpenTofu](https://thenewstack.io/opentofu-turns-one-with-opentofu-1-9-0/)）向前迈出的一步。

最棒的是，不需要 [YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)。

“剧透一下：它没有成功，”缓存平台提供商 [Momento](https://www.gomomento.com/company/about/) 的生态系统工程师 Allen Helton 在虚拟 [IaCConf 2025](https://www.linkedin.com/showcase/iac-conf/) 上[发言](https://www.youtube.com/watch?v=10mU9eqN7m4&list=PLocaoeyiLZlU1jkC6Kysu_IyD8h3wE3mL&index=11)，谈到了 IfC 的[短暂趋势](https://thenewstack.io/infrastructure-from-code-gives-ops-needed-freedom/)。

Helton 对 IfC 未能如宣传的那样发挥作用提出了一些想法。在由 [Spacelift](https://spacelift.io/?utm_content=inline+mention) 主办的会议上，其他人也分享了他们在自动化基础设施部署和尽可能保持其可管理性方面的经验教训。

## 上下文切换

Helton 说，云使应用程序开发人员的工作变得复杂。过去的日子一去不复返了，那时你可以点击 F5，将你的代码发送到生产环境中，而无需考虑它将如何运行。他们现在必须担心基础设施。

有了云，“我总是在我的模板文件和我的业务逻辑之间进行上下文切换，这减慢了我的速度，”他回忆道。

IfC 承诺消除所有这些上下文切换。

![Klotho 标志](https://cdn.thenewstack.io/media/2025/05/3bf95233-klotho-150x150.jpg)

Klotho，不复存在。

这似乎是个好主意，因此出现了一批供应商，他们推出了一系列令人印象深刻的支持工具：[Nitric](https://nitric.io?utm_content=inline+mention), [Klotho](https://klo.dev/ifc/), [Encore](https://encore.dev/docs/ts), [Wing](https://thenewstack.io/wing-the-startup-failed-but-the-language-has-potential/), [Shuttle](https://www.shuttle.dev/blog/2022/05/09/ifc), [Dark](https://blog.darklang.com/what-is-dark/) 和 [Ampt](https://www.getampt.com/docs/overview/)。

每家公司都采取了略有不同的方法。Wing 提供了自己的[编程语言](https://thenewstack.io/winglang-cloud-development-programming-for-the-ai-era/)，允许编译器将其转换为运行基础设施的代码。Klotho 使用 JavaScript，并为基础设施调用添加了一组注释。

然而，Helton 回忆说，所有这些方法都难以找到市场吸引力。

## 别担心，一切都不在控制之中

上述许多公司已经倒闭或停止开发——Wing、Klotho——而另一些公司正在转型或进入维护模式。似乎只有 Nitric 和 Encore 仍在蓬勃发展。

Helton 认为，IfC 方法的问题在于开发人员还没有完全准备好放弃控制权。

使用 IfC，供应商控制着开发人员可以使用哪些资源来保持简单。因此，是由供应商决定客户的基础设施将如何配置。

这对大多数开发人员来说是行不通的。

供应商承诺提供开箱即用的最佳实践。但是，供应商的最佳实践很少是客户自己的最佳实践。许多企业可能在 HIPAA 或其他外部或内部授权方面有特殊需求。

简而言之，IfC 为那些愿意放弃一点基础设施控制权的人承诺了巨大的回报。

“随着抽象程度越来越高，这让我们感到不安，因为当你抽象并消除可配置性时，我们就会走出舒适区。”

— Allen Helton, Momento 的生态系统工程师

“这里的潜台词是，‘相信我们，我们会支持你，尤其是在出现问题时’，这意味着当出现问题时，你真的要听从他们的 SLA [服务级别协议] 的摆布。”
如果开发人员和软件工程师不喜欢放弃控制权，那么平台工程师和 [DevOps 人员](https://thenewstack.io/devops/) 也不会热衷于这个想法。事实上，DevOps 工程师和平台工程师的特定工作就是[控制基础设施](https://thenewstack.io/foundational-concepts-in-platform-engineering/)。他们决定使用哪个云提供商以及如何满足各种要求。

换句话说，IfC 从一开始就注定要失败，Helton 说。

“代码即基础设施是一个非常有趣的话题，我很遗憾看到它没有成功，”Helton 说。“在演示中它真的很酷，但我认为在实践中，它并不适合行业的发展方向。”

## 自适应基础设施，另一种 AI

事实证明，管理基础设施比简单地交给供应商并忘记它要动态得多。

基础设施不是一次性的事情。它需要随着业务需求的变化而变化，并且随着应用程序需求的变化而变化，Helton 说。我们真正需要的是自适应基础设施，由 [人工智能](https://thenewstack.io/ai-engineering/) 驱动，它可以查看当前的使用情况并实时提出优化建议。

然后，客户将根据自己的喜好在成本、延迟和容错之间取得平衡：很少在夜间运行的服务可以从容器切换到无服务器以节省资金。

## 铺平的道路还是黄金之路？

如果 IfC 最终是一条死胡同，那么是否有其他方法可以[配置基础设施](https://thenewstack.io/terraform-1-0-reflects-what-hashicorp-has-learned-about-infrastructure-as-code/)，使其具有[自动化](https://thenewstack.io/iac-is-too-complicated-wheres-that-easy-button/)和[无忧无虑的模式](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/)？

在另一次 [IaCConf 演讲](https://www.youtube.com/watch?v=iSK-6INXBYo&t=1347s) 中，[Vega](https://www.vega-alts.com/) 首席工程师 Joe Hutchinson 提供了 IaC 的其他一些可能方向，并从中吸取了 [平台工程](https://thenewstack.io/platform-engineering/) 的经验教训。

使用 [Terraform](https://thenewstack.io/terraform-and-the-tooling-multiverse-in-the-future-of-iac/) 之类的东西来配置 IaC 对于第一个项目来说似乎很棒，但是随着添加更多项目，IaC 看起来越来越混乱且难以管理。

“在某个时候，你会意识到这是一个错综复杂的烂摊子，”他告诉虚拟观众。

“我在职业生涯中遇到的大部分复杂性都来自于结构良好的 IaC 世界试图与公司中未配置为代码的部分进行交互，并且可能结构不太好，”他补充说。

在他的为英国金融科技公司 [Checkout](https://www.checkout.com/) 做的演讲中，Hutchinson 描述了一些正确的方法——或者至少让它变得更好。

首先，你要衡量你已经做的事情，并选择一个指标来改进。

“如果我再做一次，我会衡量工程效率，”他说。

Checkout 拥有三名 DevOps 工程师管理基础设施，以支持 200 名工程师从事各种项目。这家快速发展的公司希望将运营分散到“[Spotify 模型](https://thenewstack.io/platformcon-how-spotify-manages-infrastructure-with-gitops/)”。它建立了一个平台工程团队来“加速团队”。

该公司拥有一个自以为是的平台，该平台由 [headless Backstage deployment](https://thenewstack.io/five-years-in-backstage-is-just-getting-started/) 构建，并由 Terraform 配置以提供一系列工具。产品团队使用这些模块来启用他们需要的工具。

“能够衡量事物并量化收益将会是一个容易得多的旅程，”他说。

*更新 (2025/6/13): IaCConf 2025 的所有演讲现在都已发布在 YouTube 上，所以去看看吧。*

## 加入我们的网络研讨会，获取有关代码即基础设施的最新见解

网络研讨会的主要要点：

- 为什么您的 IaC 策略会适得其反（以及如何解决）。
- 无论您使用哪种 IaC 工具，您的云平台都需要的基本功能。
- 关于 2026 年云运营情况的独家预测性见解。
- 针对 2025 年 IaC 现状调查发现的最大问题的实用解决方案。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。