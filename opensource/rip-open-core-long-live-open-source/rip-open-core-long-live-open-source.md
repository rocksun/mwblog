
<!--
title: RIP开源核心—开源万岁
cover: https://cdn.thenewstack.io/media/2024/11/8ff0d5c9-markus-spiske-8oykwqgbskq-unsplash-scaled.jpg
-->

开源可能不断变化和转型，但它一如既往地强大——而且很可能在未来几代人中保持这种状态。

> 译自 [RIP Open Core — Long Live Open Source](https://thenewstack.io/rip-open-core-long-live-open-source/)，作者 Or Weis。

开源的重要性从未如此明显。它对于我们今天构建软件至关重要，并且随着时间的推移只会变得越来越突出。问题在于，我们过去将开源引入市场的方式已经不再适用。

2022 年，我写了[“开源的未来，或为什么开放核心已死”](https://thenewstack.io/the-future-of-open-source-or-why-open-core-is-dead/)。从那时起，多家公司已经放弃了开放核心模式，导致了几个重大的失败。我亲眼目睹了围绕开源的混乱和质疑不断加剧，同时也亲眼目睹了开源的巨大影响力。开源项目（比如我正在参与的 OPAL）不断发展壮大，这强化了真正的开源项目的强大影响力和协作精神。

## 与时俱进

为了快速回顾 2022 年的文章，在 *开源的未来，或为什么开放核心已死* 中，我描述了开放核心模式的局限性，以及为什么它经常适得其反。

开放核心最初之所以流行，是因为它允许公司围绕免费产品版本构建社区，同时为更完整、企业级的版本收费。这种模式在 2010 年代蓬勃发展，帮助 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention) 和 Redis 等公司获得了发展。

但时代变了，如今，开放核心模式往往会带来更多问题，而不是增强公司的地位。

软件的采用和构建速度呈指数级增长。依赖开放核心的公司发现自己陷入了困境，而不是促进增长。一旦他们的项目获得关注，他们就很容易成为竞争对手的猎物，竞争对手可以使用免费的开放核心版本来开发竞争服务。

这导致公司不得不与自己的 [开源社区](https://thenewstack.io/how-to-give-and-receive-technical-help-in-open-source-communities/) 竞争，对他们施加限制，甚至完全退出开源产品。

[Elastic 就是一个典型的例子](https://opensourceconnections.com/blog/2021/01/15/is-elasticsearch-no-longer-open-source-software/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)。在构建了一个成功的 OSS 项目后，Elastic 看到多家公司（包括 AWS）直接在其基础上构建服务，削弱了 Elastic 自己的产品。这导致 Elastic 不得不改变 Elasticsearch 的许可证，以阻止竞争对手利用其代码，这引发了社区的批评和困惑。

Docker 也遇到了类似的情况，其开源产品获得了发展势头，但商业版本却举步维艰。试图限制 OSS 版本导致了开源社区的强烈反对和不信任。

## 不断变化的风向

正如我在 2022 年预测的那样，随着越来越多的知名公司放弃开放核心，这种趋势正在加速。

2023 年 8 月，HashiCorp 的 Terraform，一种在基础设施即代码中广泛采用的工具，[改变了其许可证模式，以限制商业竞争对手](https://www.theregister.com/2024/05/24/opinion_column_terraform/)。这种转变导致了社区的强烈反对，并催生了 [OpenTofu](https://opentofu.org/)——一个分支，允许开源社区在没有附加条件的情况下，将 Terraform 的核心功能保持免费，不受限制性许可证的约束。

一年后，Cockroach Labs [宣布将放弃 CockroachDB 的开放核心模式](https://thenewstack.io/cockroach-rescinds-open-core-for-a-free-enterprise-version/)，转而只为自托管用户提供企业版许可证。与之前的情况一样，这种变化旨在防止竞争对手利用 Cockroach 的产品与之竞争，将其作为商业服务提供，而不回馈给 Cockroach Labs。
Sentry 也认识到开放核心方法的弊端，并通过引入功能性源代码许可证 (FSL) 做出回应。该许可证允许用户自由运行和修改 Sentry，但有一个关键的限制：他们不能用它来直接与 Sentry 竞争。此更改旨在保护项目的可持续性，同时确保 Sentry 的努力不会轻易被其他人复制或用于商业利益。

这些例子反映的趋势很明显：公司正在远离开放核心，因为这种模式越来越难以同时维护社区信任和商业安全。

## 新希望 - 回到真正的开源

虽然开放核心和源代码可用模型曾一度流行，但公司开始意识到真正开源价值的重要性，并正在找到回归的道路。这种回归开源是成长的标志，企业正在与 OSS 社区核心（眨眼）的协作精神重新对齐。

越来越多的公司正在采用真正优先考虑社区参与和透明度的模式，而不是将它们用作营销或增长策略。

在三年时间里，Elastic 为了减轻来自未经许可的商业提供商的竞争，采用了源代码可用许可证，最近[将 Elasticsearch 和 Kibana 重新引入 AGPL](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/)，这是一个 OSI 批准的许可证。这一选择重申了 Elastic 对开源社区的承诺，并允许开发人员相信他们的贡献将支持一个完全开放和透明的项目。

Elastic 事实上采用了开放基金会模式（稍后会详细介绍），尤其是在分析和安全领域，这使它能够区分其商业产品，而不会从社区中扣留核心功能。通过培育补充其企业产品的基础项目，Elastic 可以维护免费社区使用和付费企业功能之间的明确界限——这是许多公司在超越开放核心时正在学习的关键教训之一。

这种愈合过程表明了一个更广泛的运动，因为公司认识到，构建真正的开源项目可以培养持久的社区支持，并避免试图限制使用或锁定客户的模式的弊端。

## 前进的道路 - 开放基金会

随着开放核心模式的淡出，我们看到了一种更可持续的方法正在形成：开放基金会模式。这种[模式允许开源产品](https://thenewstack.io/data-unions-offer-a-new-model-for-user-data/)成为商业产品的支柱，而不会损害 OSS 项目的完整性。相反，它加强了它作为一种有价值的独立产品，支持商业产品，而不是与之竞争。

为了使开放基金会发挥作用，OSS 项目必须本身可行，提供真正的价值，而无需付费升级来实现其核心目的。这使得开源版本和商业版本之间有了明确的区分，每个版本都有其独特的价值主张。

对这种模式的一个实际测试很简单：当一家公司考虑添加一项功能时，应该立即清楚它属于 OSS 项目还是商业产品。理想情况下，对 OSS 版本的贡献应该支持和增强商业产品，而不会创建依赖循环。这种一致性维护了开源项目的完整性，同时允许商业版本蓬勃发展。

一些公司有效地体现了开放基金会模式。Vercel 使用这种方法来处理[Next.js 和 Svelte](https://vercel.com/oss) 等项目，为开发人员创建强大的工具，同时通过补充服务获利。在[Permit.io](http://permit.io/)，我们的 OSS 项目，如[OPAL](https://github.com/permitio/opal)，[Cedar-Agent](https://github.com/permitio/cedar-agent) 和[Permit-CLI](https://github.com/permitio/permit-cli) 也利用开放基金会，提供核心工具作为开源，同时围绕扩展功能构建业务。Supabase 采取了类似的路线，为各种[基于 PostgreSQL 的项目](https://supabase.com/open-source) 做出了贡献，这些项目是其商业产品的基石。

Elastic 最近决定将 Elasticsearch 重新引入使用 AGPL 的开源，是开放基金会行动的另一个例子。核心功能是开放的，而高级企业功能支持其在分析和安全方面的付费产品。其他公司，如[使用 React-email 的 Resend](https://github.com/resend/react-email) 和[使用 Backstage 的 Spotify](https://backstage.io/)，使用开放基金会来促进社区协作，利用 OSS 来建立参与度，同时与可持续的商业目标保持一致。
这些例子表明，开放基金会提供了一条有希望的前进道路，强化了开源可以服务于社区和商业利益的理念。

## 现代化罗马混凝土

如果我们问自己将走向何方，我们应该看看像混凝土一样持久的东西。我们经常将罗马混凝土理想化，认为它优于现代版本——一种失传的技术，并感到一种失落感。但事实是，它从未“更好”，也从未真正失传。像混凝土一样，开源是人类文明的基石；它在建造事物方面具有里程碑意义，并将继续存在。从罗马配方（即开放核心）转变为更现代的配方（例如，开放基金会）并不意味着任何东西都会丢失——开源的协作、弹性和社区价值将持续存在，适应新的模型并满足不断变化的景观的需求，而不会失去其本质。

开源可能会发生变化和转型，但它仍然像以前一样强大——并且很可能在未来几代人中保持这种状态。这一切都是关于找到正确的方法来有效地利用它。