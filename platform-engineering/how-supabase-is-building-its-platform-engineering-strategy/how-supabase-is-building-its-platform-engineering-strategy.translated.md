# Supabase 平台工程策略构建

![Featued image for: How Supabase Is Building Its Platform Engineering Strategy](https://cdn.thenewstack.io/media/2024/08/44d188b4-wesley-tingey-7paifc4fohk-unsplash-1-1024x683.jpg)

[平台工程](https://thenewstack.io/platform-engineering/) 不是终点，而是一个不断改进、创新和实验的演进过程，旨在为开发团队提供一致、经过测试且高效的应用程序开发工具。这是大多数公司开始其平台工程策略时的计划，也是开源 [PostgreSQL](https://thenewstack.io/benchmarking-postgresql-vs-mongodb-for-genai/) 数据库基础设施应用程序供应商 [Supabase](https://supabase.com/) 的持续工作方式。

Supabase 自称为 [Google 移动和 Web 应用程序开发平台 Firebase 的开源替代方案](https://kinsta.com/blog/firebase-alternatives/)，几年前就开始使用平台工程。该项目始于公司意识到，为其大约 50 名开发人员构建自己的 [内部开发平台 (IDP)](https://thenewstack.io/internal-developer-platform-vs-internal-developer-portal-whats-up/) 将使公司能够整合、标准化和自动化其开发应用程序，从而提高团队的生产力、代码质量和其他优势。Supabase 自 2020 年开始运营。

“它随着时间的推移而不断发展，”Supabase 的平台工程师 [Samuel Rose](https://www.linkedin.com/in/samrose/) 在 2024 年 2 月加入公司后告诉 The New Stack。“他们已经做了一些类似的事情，并且 [开始] 将每个人都在做的事情正式化，将其转变为一个角色，我们可以在整个公司中对此负责。”

“Supabase 一直采用不断发展的平台工程方法，但我被聘用是为了在整个组织中将其正式化并扩展，”Rose 说。“我们将继续每周对其进行改进，并且已经在公司不断发展的平台工程策略中取得了巨大进展。”

Rose 说，公司的平台工程项目源于许多团队的 IT 管理员和开发人员共同努力，为他们的工作创建平台工程方法。“需求越来越大，以至于 Supabase 需要至少聘用一名全职人员来推动它向前发展，”这就是他加入公司的原因。

Rose 解释说，导致这些决定的因素是 Supabase 不断增长的客户群以及在管理构建、测试和发布流程方面不断增长的技术复杂性。他还补充说，公司“希望在我们的内部平台上使用和利用我们的产品，只要它有意义”。

“我在这个行业工作了 20 多年，”Rose 说。“Supabase 四年前成立，在经过四年的工作和扩展之后，这家公司现在成长到满足这些需求是相当自然的。在 Supabase，我们使用自己的产品，并将我们的一些组件作为工具用于我们的内部平台。”

## Supabase 式平台工程

Supabase 并没有从头开始构建和创建其平台工程策略。相反，它从预先构建的平台工程工具推荐开始，这些工具来自 [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) 等组织的示例 [云原生景观](https://landscape.cncf.io/?view-mode=grid) 概述，Rose 补充道。

“我们的平台与那些 [平台工程方法](https://thenewstack.io/platform-engineering-it-is-all-about-the-tooling/) 非常吻合，”他说。“但我们在平台中使用了一些我们自己的产品，包括我们自己的 API 和以 Postgres 为中心的开发，”而不是使用预构建推荐网格中提供的一些现成或软件即服务组件。

这种定制的平台工程方法非常适合 Supabase，使公司能够将内部工具与其他行业标准工具结合起来构建应用程序。

“主要目标是将我们正在使用的现有构建块用于平台工程，并将它们整合、自动化，并为每个人提供更坚实的基础，”Rose 说。“这并不是一种非常传统的平台工程方法，但它非常适合公司。它随着时间的推移而不断发展。”

Rose 表示，为了实现这一目标，Supabase 目前正在围绕某些标准和某些工具进行整合。

“有时人们谈论平台工程时，他们指的是采用整个平台，这实际上就像其他人编写的某种软件，并将所有东西都放在里面，就像一头扎进游泳池的最底部，”Rose 说。“我们并没有真正这样做。我们 [也使用] 我们自己的工具。”
Rose 说，这些平台工程工作是 Supabase 开发工作和流程的自然产物。“所以，他们很容易看到这种需求——在我参与之前，他们就开始着手这项工作。我一直与他们合作，我们……将它变成了现实，就做你所说的平台工程而言，它已经进入生产阶段。它还在进行中。”

## Supabase 内部开发者平台包含什么

为了给开发者提供构建 Supabase 应用所需的工具，该公司的 IT 管理员围绕少量开发应用构建了他们的平台工程平台。

Rose 说：“我们尽量节俭，这样就不会造成 [问题]，因为如果你不断地往篮子里扔工具，你最终就需要管理所有这些工具。”“所以，我们在这方面很谨慎。我们大约有五到七种主要的组件，我们尽量整合和利用尽可能多的现有系统。”

Supabase 的 IDP 中包含的工具包括：

**开发者控制平面**: Supabase 利用内部维基、GitHub、[Terraform](https://thenewstack.io/terraform-isnt-dead/) 和 [Pulumi](https://thenewstack.io/pulumi-rocks-ai-infused-infrastructure-as-code-platform/)。该公司还使用基于 [Docker](https://www.docker.com/?utm_content=inline+mention) 的自定义工具和其他相关工具在本地运行其平台，以及其 SaaS 后端即服务产品，该产品也可以在本地运行。**集成平面**: Supabase 使用 GitHub Actions、Nix 包管理器/Debian 包、Docker、Amazon S3 和自托管的 Nix 二进制缓存。此外，它还使用 Humanitec 的平台编排器和内部自定义应用程序。**安全平面**: Web 应用防火墙 (WAF)、[AWS](https://aws.amazon.com/?utm_content=inline+mention) GuardDuty、[Google](https://cloud.google.com/?utm_content=inline+mention) 云平台入侵检测系统 (IDS)、AWS Secrets Manager、AWS EC2 Instance Connect 和 [其自身工具](https://github.com/supabase/auth)（在某些情况下）。**监控和日志记录平面**: Vector、Sentry、BigQuery、VictoriaMetrics 和其自身的 [Logflare 工具](https://logflare.app/)。**资源平面**: Supabase 主要使用 AWS 和 GCP 平台中内置的工具，以及战略性地使用其自身产品来管理元数据、集群等。

到目前为止，其平台工程工作的结果对 Supabase 来说很有希望。

Rose 说：“其中一件事是，它为我们提供了一种途径来管理为客户提供更好的 Postgres 新版本。”“我们团队内部的人员可以 [创建] 他们所谓的确定性构建，他们可以构建一次，就不需要再构建了。这是我们正在为平台工程创建的新平台的一部分。[你] 可以反复使用它，除非你改变了什么，所以它可以减少构建时间，并有助于确保系统之间可重复。过去，这很难做到。”

Rose 解释说，通过使用 IDP，开发者可以专注于他们的代码，完成他们的工作，然后继续进行下一个项目，而不必花费宝贵的时间来配置、收集和维护他们的开发工具。“我们已经到了很多开发者可以自助服务他们大部分需求的阶段，同时拥有对监控和测试的安全访问权限，并支持生产部署。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)