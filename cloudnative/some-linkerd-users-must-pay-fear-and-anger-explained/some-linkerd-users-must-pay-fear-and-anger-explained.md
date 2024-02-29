<!--
title: Linkerd收费引发用户恐慌与不满
cover: https://cdn.thenewstack.io/media/2024/02/060c3826-towfiqu-barbhuiya-3agz7a97qwa-unsplash-1-1024x683.jpg
-->

对于 Buoyant 决定向拥有 50 个或更多用户以访问其开源服务网格的稳定版本收取费用，有些人对此产生了误解。

> 译自 [Some Linkerd Users Must Pay: Fear and Anger Explained](https://thenewstack.io/some-linkerd-users-must-pay-fear-and-anger-explained/)，作者 B. Cameron Gain。

Buoyant决定向拥有50名或更多用户的组织收费获取其开源[服务网格](https://thenewstack.io/service-mesh/)的稳定版本，这无疑引发了愤怒。这种反应可以理解，因为这种服务网格(包括所有稳定版本)已经免费可用了一段时间，许多用户(包括企业)至少已经习惯于它。

然而，在宣布后的尘埃落定之后，似乎人们对这一举措的实际意义存在一些误解。这也表明开源模型和免费提供的内容正在发生变化。考虑到开源商业模型的演变背景，这种转变可以说是可以理解的。

与此同时，反对的声音仍在继续。

[Linkerd](https://thenewstack.io/linkerd-service-mesh-update-addresses-more-demanding-user-base/)的创造者和[Buoyant](https://buoyant.io/)的创始人兼CEO [William Morgan](https://www.linkedin.com/in/wmorgan/)表示，他理解用户和社区对这一决定的愤怒。他将他们的反应比作Linkerd就像免费的有机食品，现在却要收费。

Morgan告诉The New Stack:"一些组织可能已经建立了他们的整个生活方式围绕这些稳定版本，现在我们说:'对不起，你现在必须为它付费'，我理解他们的立场。"

Buoyant没有做的事情是改变Linkerd的许可计划。许可仍然是[Apache许可证2.0](https://www.apache.org/licenses/LICENSE-2.0)版本。此外，可能许多人不知道，Buoyant没有强迫用户为了获得稳定版本而支付企业版费用。这是因为它已经在2023年发布了企业版本。

HashiCorp在2023年8月透露，它将改变其领先的[基础设施即代码](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)平台[Terraform](https://thenewstack.io/terraform-providers-and-the-rise-of-infrastructure-as-a-service/)的许可条款，之后将其开源的Mozilla公共许可证v2.0(MPL 2.0)替换为业务源代码许可证(BSL)v1.1，这限制了代码在生产中的使用，这很有可能是对Boyant的批评的后果。在Terraform许可证变更之前，MongoDB、Elastic和其他公司已经从提供纯开源许可证的软件转向混合许可。

相反，Buoyant对Linkerd的改变更类似于[Red Hat](https://www.openshift.com/try?utm_content=inline-mention)选择不再提供[RHEL(Red Hat Enterprise Linux)](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/)源代码的时候。

[Codefresh](https://thenewstack.io/codefresh-goes-open-core-with-argo-previews-open-gitops-1-0-release/)联合创始人兼首席开源官[Dan Garfield](https://www.linkedin.com/in/dan-garfield/)说:"我认为人们在Terraform之后变得很紧张。他们听说Buoyant改变了他们的发布模式，并鼓励人们下载企业版本，他们可能会像'哦，这就是HashiCorp做的事情'，但它并不是HashiCorp做的，因为他们没有改变许可证。"

[企业管理协会](https://www.enterprisemanagement.com/)(EMA)的分析师[Torsten Volk](https://www.linkedin.com/in/torstenvolk)对此持不同意见。Volk对The New Stack表示:"虽然Buoyant没有改变许可证，但它仍改变了Linkerd各种用户的经济状况和风险配置。" Volk说:"已经采用免费开源Linkerd的企业已经在部署和操作该平台所需的工程团队上投入资金。" 对他们来说，不得不开始支付额外费用在财务上可能没有意义。

与此同时，Volk表示，"商业化"的开源项目的趋势正在加速。Volk说:"我们自动地想知道开源的未来是什么:是否不可能在开源上建立一个盈利的业务?" Volk说:"'Terraform震撼'是这一新趋势的开始，无论什么规模的软件公司都必须不断向董事会解释，为什么每年都要向开源社区贡献成千上万的开发时间。在风险投资枯竭的今天，这变得更难辩护。"

## Linkerd的定位

开源Linkerd是一个以低功耗和易用性而闻名的流行服务网格，适用于小型和大型组织。Linkerd仍然使用[服务网格边车](https://thenewstack.io/linkerd-enterprise-creators-keep-the-sidecar-mesh/)，这与也被认为更适合大型组织的[Istio](https://thenewstack.io/what-is-istio-and-why-does-kubernetes-need-it/)形成了另一个对比，后者提供了一个无边车的替代方案。正因如此，Morgan表示，通过继续为少于50名用户的组织提供Linkerd稳定版本的免费使用，他寻求帮助小用户。那些拥有50名以上用户的组织必须支付2000美元，而这些条款可能会改变，Morgan说。

Buoyant将继续通过回归测试和其他测试与开发来维护Linkerd版本之间的稳定性。从理论上讲，用户应该能够从GitHub上的最新提交中安装和使用Linkerd，但仍有一些元素将保持试用阶段，供用户和维护者协作以帮助改进代码。改变的是一些组织将不得不为这些稳定版本付费。

"我们使得低于一定门槛的公司可以免费使用，"Morgan说。"因此，作为这个组成部分，我们想:'好的，我们可以建立一个完整的生态系统并做到这一点。让我们拿起这件事，它实际上比过去的稳定版本要好得多，并使它们变得更好。'"

一个项目的治理是一个需要考虑的关键属性。就[Argo CD](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux/)而言，它与[Flux](https://thenewstack.io/gitops-made-simple-with-flux/)一起作为[GitOps](https://thenewstack.io/what-is-gitops-and-why-it-might-be-the-next-big-thing-for-devops/)的平台，与Buoyant相比，由于其治理结构，改变什么是免费的以及什么不是免费的要困难得多。如果你担心某些事情发生变化，你会看我们的治理，你会说:'好吧，在Argo的情况下，这主要由四个主要的公司维护者共享，但同时也有许多社区维护者，他们必须投票同意这种改变。'所以，对于这类事情，治理非常重要，因为它会告诉你需要什么程度的支持才能改变。在Argo的情况下，需要很多人同意改变。"

相反，Linkerd一直主要由Buoyant维护。从治理的角度来看，Buoyant因此对项目的未来有更多的控制权。Garfield说:"人们会说，'我以为如果它是一个开源项目，你应该提供稳定的版本'，我会回答'我不知道谁告诉你的，因为这没有写在任何地方，也没有CNCF毕业标准提到过'，他们一直在为你提供这些稳定版本，但没有人保证这将永远是这种情况。"

## 商业模式

Buoyant一直是Linkerd的最大贡献者，其在生产版本上的投入占了对该项目支持的相当大一部分。与此同时，最近直接基于业务模型的开源项目的开发日益艰难。风险投资的匮乏和其他动态在很大程度上导致了现金不充裕的气候。近期[Weaveworks的倒闭](https://thenewstack.io/end-of-an-era-weaveworks-closes-shop-amid-cloud-native-turbulence/)，它创建了Flux并首先提出了“GitOps”一词，就令人难过地预示着当前的开源业务气候。

“我们周围的行业正在发生变化，因为公司意识到‘我的天，我们需要赚钱。我们需要有一个可行的业务模式，’”Morgan说。“天使投资轻松做到一切的日子已经过去了。将来我们会再次看到它，但就目前而言，它不在那里。”

可以说，在许多情况下，直接建立在开源之上的企业，其成功几乎完全取决于将开源用户转化为支付企业产品的客户。相反，许多公司通过共享将时间和精力投入到开源项目中而取得成功，这些项目间接地支持他们的业务模式。这些项目可能部分依赖于那些帮助维持这些项目的善意人士，而他们的业务模式并不主要依赖于开源项目的成功。

作为迄今为止最著名的开源项目之一，[Kubernetes](https://thenewstack.io/kubernetes/)在很大程度上依赖于谷歌、[微软](https://news.microsoft.com/?utm_content=inline-mention)和[亚马逊](https://aws.amazon.com/?utm_content=inline-mention)的贡献。他们正在为该项目做出贡献并以一些最重要的方式帮助维护它，因为他们在Kubernetes之上建立了核心价值平台，并希望继续投资底层平台，Garfield说。

Kubernetes保持开放，用户可以添加一些扩展和其他功能，而在不同平台上部署Kubernetes的体验相似，足以让用户期望我的Helm Chart在两个平台上都可以工作，Garfield说。 “Kubernetes有一个非常安全的未来。你可以说Kubernetes突然改变其分发模型或许可模型的可能性跟地狱里的雪球一样小，因为治理就在那里，”Garfield说。“激励机制以这样一种方式对齐，使得任何人都很难做到这一点。”

Volk对Buoyant与Kubernetes的业务可行性提供了一个更严峻的看法。Volk说:"超大规模公司将Kubernetes用于销售更多他们高度成瘾的服务，因此他们从投入开发时间中看到直接的回报。由于其贡献的大部分针对的是与自己的云服务的集成，所以尤其如此。然而，Buoyant未能说服开源用户企业支持的价值，因此别无选择，只能走出开源的队伍，直面现有企业用户的愤怒。”
