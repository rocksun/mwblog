<!--
title: IDP让开发者更自由地编码
cover: https://cdn.thenewstack.io/media/2015/07/platform.jpg
-->

Red Hat的Markus Eisele表示，在充斥着人工智能、安全考量和法规的IT世界中，内部开发者平台解放了许多单调乏味的任务。

> 译自 [IDPs Give Developers More Freedom to Write Code](https://thenewstack.io/idps-give-developers-more-freedom-to-write-code/)，作者 Jeffrey Burt 是一名拥有三十多年经验的记者，过去的二十多年专注于科技报道。在过去的 16 多年里，他曾在 eWEEK 工作，并在此后成为一名自由科技记者，涵盖了从数据...

当[Markus Eisele](https://www.linkedin.com/in/markuseisele/)在本世纪初开始时，正值互联网泡沫开始破裂，软件开发者的生活相对简单。

“我很幸运地开始接触应用服务器和一些大部头的书，基本上概述了如何在[Java](https://thenewstack.io/what-do-java-developers-think-of-the-rise-of-genai/)中完成各种任务，”现任红帽（[Red Hat](https://www.openshift.com/try?utm_content=inline-mention)）高级首席技术营销经理的Eisele告诉The New Stack。 “我事实上是在一堆API上构建我的职业生涯，因为技术很少改变。那时候是一个平台，一个应用服务器，可能还有一两个供应商，我们一直在谈论供应商锁定，但那基本上就是全部。”

快进几十年，开发者的世界变得更加复杂。大型团队开始扩大规模，新的方法论如敏捷（[Agile](https://thenewstack.io/principles-of-good-large-scale-agile/)）和极限编程（XP）出现在舞台上，[Kubernetes](https://thenewstack.io/kubernetes/)和[微服务](https://thenewstack.io/microservices/)等技术带来了新的服务、分解和复杂性程度。Eisele称之为“你来构建它，你来运行它”的这种独特人工混合，使开发者对在生产环境中运行某些东西负有责任。

同时，不断增长的法规数量继续因地区或行业而异，比如GDPR、HIPAA和PCI DSS等，以及[拜登政府在2021年颁布的关于网络安全的行政命令14028](https://thenewstack.io/sboms-are-great-for-supply-chain-security-but-buyers-beware/)，其中包括使用[软件清单（SBOMs）](https://thenewstack.io/how-to-create-a-software-bill-of-materials/)的规定。类似的，欧盟数字运营韧性法案（DORA）于2022年底获得批准。

所有这些都预示着随着人工智能（AI）、机器学习和自动化的加速采用以及网络攻击数量和复杂程度的增长，这一切将继续积累。

## 编码时间不够

“人们开始意识到在说‘敏捷’和‘DevOps’之间存在很大的差异，而真正做到敏捷和DevOps是不容易的，”Eisele说道。“这就是我们很多客户所处的位置。基本上他们不是Netflix，不是Facebook，也不是[Amazon](https://aws.amazon.com/?utm_content=inline-mention)。从规模上来说，是的，但从技术上来说，他们无法以那种方式执行，不是因为他们不想，而是因为他们受到了严格的法规限制。”

在开发领域，推动的方向已经变成了弥合已被证明为高效和灵活的方式与日益增长的政府法规和要求之间的差距，他说。开发者是每个现代公司需要做的事情的核心，因为他们正在提供业务价值。

管理复杂和分布式技术环境、保持符合监管要求的负担使开发者心力交瘁，阻碍了他们做他们最喜欢的事情：编写代码和创建软件，Eisele说。

在过去的几年里，诸如内部开发者门户之类的解决方案已经出现 —— 这是存储有关软件开发运营、工作流程和分散发展环境中所有必要知识的[中心化场所](https://thenewstack.io/internal-developer-portal-what-it-is-and-why-you-need-one/#:~:text=A%20well%2Darchitected%20internal%20developer,about%20your%20software%20development%20operation.)。还有黄金路径模板 —— 有时被称为“铺平的道路”或“铺平的路径” —— 为开发者提供了一个高度定义和支持的途径，配备了工具和流程，以更快地构建软件并将其交付到生产环境。

## 进入 IDP

最近，[内部开发者平台（IDP）](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)已经出现，为简化开发流程提供了另一种方式，通过将必要的工具集中在一个地方。内部开发者平台网站称IDP“由平台团队构建，用于构建Golden Paths并实现开发者自服务。”

[根据红帽（Red Hat）](https://www.redhat.com/en/topics/devops/what-is-an-internal-developer-platform)的说法，“通过巩固和简化开发过程的各个要素，IDP的基本目标是使开发团队的日常工作更加可管理、高效和协作。”

它们为所有开发团队提供了标准化的工具和服务，自动化任务，如设置开发环境和配置构建流水线，为开发者提供集中的协作场所，以及遵循最佳实践并符合安全和监管要求的治理框架。

应用开发者是主要使用内部开发者平台（IDP）的人员，运维团队负责初始配置和维护。整个过程始于运维团队“通过设置基准模板来创建IDP，这些模板在视觉上整合了开发过程的各个元素并管理权限。然后，开发者可以调整这些配置并启动完全配置好的环境，”该公司写道。

IDP与内部开发者门户一起工作，后者解决用户体验并充当与平台的界面。

“当你考虑到所有必要的下游技术时，平台方面基本上是不可避免的，”Eisele说。“门户只是着陆的地方。它可能为您提供视图 —— 插件或文档管理或遗留的CCMDB（变更和配置管理数据库）或其他服务注册。”

他补充说，“真正的价值体现在您能够提供一个完全集成的体验，不仅从UI和前端的角度，还包括一直延伸到基础架构。”

IDP供应商[Humanitec在去年的一篇专栏](https://humanitec.com/blog/build-vs-buy-internal-developer-platform-for-enterprise)中指出，McKinsey and Co.概述了平台内的五个架构层面，其中大多数至少包括开发者控制、集成和交付以及资源平面，监控和安全是可以添加的其他层面。

## 一个集中的地方，包罗万象。

推动对内部开发者平台（IDP）不断增长的兴趣的原因之一是将文档、自动化和监控集中在同一位置，Eisele表示。内部开发者平台还使得DevOps团队能够更好地平衡应对不断增长的安全和法规要求以及在竞争激烈的环境中持续创新、迭代和更新的需求。

基本上，开发者不必过多担心确保他们的软件安全且符合规定，可以更多地专注于软件开发的创造性一面，即使人工智能提出了新的挑战。组织需要知道用于训练[大型语言模型（LLMs）](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)的数据是否符合版权和许可规定，这些信息可以通过IDP传递给团队。

目前，人工智能开发和更典型的软件开发实际上是两个分开的生命周期，尽管它们相似但使用了不同的术语。然而，Eisele表示他预计“所有的人工智能炒作最终都会回归到与应用开发非常接近的东西，以便可以轻松地集成在同一平台上。”

将所有这些工具、信息和服务集中起来，能够减轻开发者的很多琐碎任务，这可能解释了为什么IDP越来越受到关注。红帽看到了越来越多的客户首次采用IDP，Eisele预测这一趋势将继续。他还预计这一趋势将继续朝着平台方法而非以门户为重点的倡议方向倾斜。

对于像 Eisele 这样的老派开发者来说，能够更专注于编写代码是内部开发者平台（IDP）带来的巨大优势。

“最终，[IDP] 减少了不必要的日常任务量，” Eisele说。“只需想象一下你平常使用的浏览器打开了 50 个标签。最终，这将减少到一个标签，因为你确切地知道自己需要去哪。... 这在精神负担上是显著减轻，因为你可以确切地知道需要点击哪里来获取某些信息，因为对于你所工作的每个服务，对于你所工作的每个应用程序，这都是相同的。”

“你可以真正回到高效的状态。”
