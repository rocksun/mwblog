
<!--
title: Fly.io 以对象存储从三大云中吸引开发者
cover: https://cdn.thenewstack.io/media/2024/03/162b4c83-white-tailed-eagle-2015098_1280-1.jpg
-->

虽然 Fly.io 一直保持低调，但它正在悄悄逼近 PaaS 提供商和三大巨头，积累了大量的开发者基础并建立了战略合作伙伴关系。

> 译自 [Fly.io Luring Devs from the Big 3 Clouds with Object Storage](https://thenewstack.io/fly-io-luring-devs-from-the-big-3-clouds-with-object-storage/)，作者 Darryl K Taft。

[Fly.io](https://fly.io/) 是当今最热门的地下开发者运动背后的推手，该公司悄然吸引了超过 25 万名开发者，并且现在正在建立关键合作伙伴关系以接触更多开发者。

Fly.io 是一个平台，开发者可以在此轻松地启动和管理全球应用程序。Fly.io 首席执行官兼创始人 [Kurt Mackey](https://www.linkedin.com/in/mrkurt) 说。Fly.io 与平台即服务 (PaaS) 提供商（如 [Heroku](https://thenewstack.io/service-design-couldve-prevented-herokus-free-tier-closure/) 和 [Render](https://thenewstack.io/render-cloud-deployment-with-less-engineering/)）竞争，以获得最初的开发者采用，但最终，Mackey 的目标是与 [AWS](https://aws.amazon.com/?utm_content=inline-mention)、Azure 和 [GCP](https://cloud.withgoogle.com?utm_content=inline-mention) 等主要云提供商竞争。

## 叛军联盟

事实上，Mackey 告诉 The New Stack，他设想云计算的未来将由大约 50 家专门公司组成的“叛军联盟”组成，每家公司都专注于特定的开发者需求。例如，Fly.io 与合作伙伴 [Supabase](https://thenewstack.io/supabase-takes-aim-at-firebase-with-a-scalable-postgres-service/)（用于管理 [Postgres](https://thenewstack.io/from-a-fan-on-the-ascendance-of-postgresql/)）和 [Tigris Data](https://www.tigrisdata.com/)（用于 [对象存储](https://thenewstack.io/the-new-metrics-of-object-storage/)）共同组成了“最小可行云”，开发者可以使用它来构建几乎任何类型的应用程序。

Mackey 指出，AWS、GCP 和 Azure 等传统云提供商正在变得过时，因为它们围绕十年前更相关的运营实践构建。

而 Fly.io、Railway、[Netlify](https://thenewstack.io/netlifys-approach-to-the-frontend-according-to-its-new-cto/) 和 [Vercel](https://thenewstack.io/vercel-and-svelte-a-perfect-match-for-web-developers/) 等较新的托管平台正在兴起，它们提供与现代开发实践更好的契合度、改进的功能和卓越的开发者体验，[Andreessen Horowitz](https://a16z.com/) 的普通合伙人 [Martin Casado](https://www.linkedin.com/in/martincasado) 在 [博客文章](https://a16z.com/announcement/investing-in-tigris/) 中写道，他在那里专注于企业投资。Andreessen Horowitz 已投资 Fly.io 和 Tigris Data。

“这些新平台的好处可能是功能性的——例如，Fly.io 的多区域支持比 AWS 简单得多——但它们也被采用，因为它们对现代应用程序框架和实践有更好的原生支持，并且有更好的开发者体验，”Casado 在文章中写道。

## 在开发者所在的地方与他们会面

此外，Fly.io 使开发者能够使用他们最喜欢的框架构建应用程序。Fly.io CLI 为大多数流行框架生成容器，包括 [Rails](https://thenewstack.io/why-were-sticking-with-ruby-on-rails-at-gitlab/)、Phoenix、[Django](https://thenewstack.io/dev-news-django-updates-storybook-7-6-and-node-js-20-beta/)、Node、[Laravel](https://laravel.com/) 和 [.NET](https://thenewstack.io/net-7-simplifies-route-from-code-to-cloud-for-developers/)，并且 Fly 支持 [Go](https://thenewstack.io/go-1-18-the-programming-languages-biggest-release-yet/) 和 [Rust](https://thenewstack.io/rust-vs-go-why-theyre-better-together/) 编程语言。

Fly.io 将容器转换为微型虚拟机，这些虚拟机在六大洲 30 多个区域的该公司硬件上运行。Fly.io 提供其称之为 Fly Machines 的东西，它们是运行在该公司金属上的完整 Linux 微型虚拟机，由客户自己的容器通过单个命令或 API 调用构建，该公司在其网站上说。

根据该网站，“Fly Machines 是 Fly.io 平台的引擎：快速启动的虚拟机，可以在亚秒级速度启动和停止。使用其快速的 REST API 或 flyctl CLI 控制它们。或使用 [Fly Launch](https://fly.io/docs/reference/fly-launch/) 进行自以为是的应用程序范围配置和部署。”

## Fly.io 运气不错

Fly.io 最初的重点是让开发者能够轻松构建和管理他们自己的 [CDN](https://thenewstack.io/cdn-outages-exploring-ways-to-increase-resilience/)。此后，它已发展为提供高度可控且“无区域”的基础设施平台。

“一开始，我们说，如果我们做得好的话，一个独立的开发者就能构建一个 CDN，这意味着你可以在很多地方运行一段代码，用一个生命周期管理所有代码，并且不必解决非常复杂的多区域问题，”Mackey 说。

由于专注于 CDN，Fly.io 构建了“这种不在乎的云”。它没有区域性，你可以运行所有数据中心，也可以运行其中一个，完全取决于你。目标是接近人们。我们偶然发现的是开发人员希望在基础设施上管理的正确抽象。

## 存储是关键，进入 Tigris

Tigris Data 的联合创始人兼首席执行官 [Ovais Tariq](https://www.linkedin.com/in/ovaistariq/) 表示，存储一直是阻止应用程序完全迁移到这些新云的关键问题，因为构建和操作强大的云存储解决方案很复杂。

上个月，[Tigris 推出了其对象存储服务的公开测试版](https://www.tigrisdata.com/blog/object-storage-public-beta/)，该服务在 Fly.io 之上运行。Tigris 是一项全球分布式对象存储服务，可在世界任何地方提供低延迟，使开发人员能够使用他们在生产中已使用的 [Amazon S3](https://thenewstack.io/amazon-s3-express-one-zone-introduces-near-real-time-object-storage/) 库存储和访问任意数量的数据。

## Uber 入驻

Tariq 和他的 Tigris 联合创始人领导了 Uber 的存储平台团队。他在[博客文章](https://www.tigrisdata.com/blog/object-storage-public-beta/)中说道：“六年多来，我们构建并运营了 Uber 的全球存储基础设施，每天支持 Uber Rides 和 Uber Eats 应用程序的数百万用户。”

“团队中几乎有一半来自 Uber，”Tariq 告诉 The New Stack。

Tigris 团队显然有能力构建和运行全球对象存储服务，利用他们在 [FoundationDB](https://thenewstack.io/foundationdb-a-reliable-key-value-store-with-acid-compliance/) 方面的经验。

## Amazon S3 引领潮流，但开发人员想要更多？

在 3 月 14 日（[S3 的 8 岁生日](https://www.tigrisdata.com/blog/a16z-round-press-release/)，也是 [Pi Day](https://www.piday.org/)）的一篇帖子中，Tariq 赞扬 S3 通过提供简单存储服务 (S3) 引领了改变开发人员使用数据存储方式的潮流。事实上，“S3 重写了存储规则，并将我们推向了云计算的新时代，”Tariq 说。

然而，“随着时间的推移，开发人员[希望使用更新、更精简的云平台，而不是三大‘传统’云平台](https://survey.stackoverflow.co/2023/#section-admired-and-desired-cloud-platforms)（AWS、Azure 和 Google Cloud），”Tariq 在帖子中说。“按照 2006 年的标准，AWS S3 是一项技术奇迹。然而，现在不是 2006 年，而是 2024 年。”

Tariq 说，Tigris 使应用程序能够在任何区域写入和读取，甚至处理多个区域中的冲突更新，从而提供数据的全局一致视图，作为一个真正的全局多主存储平台。

Mackey 说，Tigris 通过在 Fly.io 的区域中运行冗余的 FoundationDB 集群，使用 [NVMe](https://thenewstack.io/why-nvme-is-a-better-choice-for-your-data-center/) 卷进行缓存，并使用队列系统将对象数据分发到多个副本和数据需求所在区域来实现这一点。

“我们使用 Kubernetes 运行我们的工作负载，我们在 Fly 之上构建了 Kubernetes，”Tariq 在一次采访中说。“我们使用它来简化。Fly 从网络角度提供的简化使我们能够轻松构建此多区域全球应用程序。如果使用 AWS，它们会给我带来很多基础设施复杂性。”

此外，Tigris 提供了一个与 S3 兼容的 API，使开发人员可以轻松地与其现有框架和库集成。

## Tigris 合作带来的收益

因此，Fly.io 已与 Tigris 合作，将对象存储作为 Fly.io 平台的一部分提供，允许开发人员使用“fly storage create”命令创建 Tigris 项目，并将所有必要的配置注入应用程序。

对于客户而言，Fly.io 将包括 Tigris 在内的所有服务的账单合并到一张月度账单中，从而简化了开发人员的会计工作。

Fly.io 拥有约 90 名员工，已筹集到 1.1 亿美元的资金，并在全球 37 个区域运营自己的硬件，以向应用程序提供低延迟访问。

Mackey 说，该公司主要吸引那些希望快速交付和迭代而不寻求许可的小型、急躁且智力好奇的开发人员团队。

Mackey 说，此外，Fly.io 在支持从事新兴和变革性用例的开发人员方面看到了巨大的潜力，尤其是在人工智能等领域。

此外，Tigris 的 Tariq 告诉 The New Stack，他也看到了人工智能领域的巨大潜力，通过计算和存储方面的创新，可以解决围绕高效扩展计算和存储的基础设施挑战。
