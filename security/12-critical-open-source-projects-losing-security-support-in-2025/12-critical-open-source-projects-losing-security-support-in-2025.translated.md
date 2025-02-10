# 2025年12个失去安全支持的关键开源项目

![Featued image for: 12 Critical Open Source Projects Losing Security Support in 2025](https://cdn.thenewstack.io/media/2025/01/769aa84f-vanna-phon-hrxikdxoapo-unsplash-1024x576.jpg)

没有什么是永恒的，这在[开源软件](https://thenewstack.io/open-source/)中尤其如此。即使是最流行的开源技术版本，也终将有一天会达到其生命周期结束（EOL）。

对于主要版本的开源软件包来说，EOL事件不仅仅是错过了只会整合到未来版本中的新功能，它还会为依赖该[开源软件](https://thenewstack.io/the-future-of-open-source-needs-more-give-and-less-take/)的应用程序带来安全风险。

例如，Apache Struts框架最近发现了一个严重漏洞([CVE-2024-53677](https://www.herodevs.com/vulnerability-directory/cve-2024-53677))。虽然该问题是在积极支持的Struts 6版本中发现的，但它也适用于数千个应用程序仍在使用的已弃用、生命周期结束的Struts 2版本。

仍然依赖Struts 2的公司面临风险，除非他们能够立即迁移到Struts 6，但这对于大多数应用程序来说是不现实的。另一种选择是使用来自值得信赖的长期支持提供商的开源库的直接替代品。这些解决方案包括漏洞补丁，它们为潜在的迫在眉睫的灾难提供了一种可行、安全且近乎即时的解决方案——尤其是对于受监管行业的企业——让您有更多时间彻底规划您的迁移。我们在HeroDevs的团队为Struts 2提供了一个类似的解决方案。在CVE-2024-53677被发现后的一周内，人们对我们的Struts解决方案的兴趣增长了20倍，这突显了一个关键的CVE对于不受支持的OSS用户来说是多么大的问题。

通过提前了解您的开源软件的生命周期结束时间，您可以更好地规划您的迁移，这样您就不会将您和您客户的数据置于风险之中。这份包含12个项目的列表代表了我认为在2025年将发生EOL事件的一些最关键的项目。重要的是要注意，此列表并不详尽。我的团队已经确定了2025年近150个主要的开源EOL事件，并且可能还有更多无法预测的事件。

重要的是要注意，生命周期结束事件不仅仅有一种类型，例如完全停止软件包与仅停止对特定版本的支持。AngularJS在2022年1月被完全弃用，因为[Google觉得它不再满足](https://thenewstack.io/herodevs-throws-net-6-users-a-post-deprecation-lifeline/)现代Web领域的需求。与此同时，.NET基金会和微软在2024年11月停止了对.NET 6的支持，以专注于更新的.NET 8和未来版本。大多数将在2025年达到其生命周期结束的项目都是类似于.NET 6的版本EOL。

### 1. Laravel v10 (2025年2月4日)

[Laravel](https://thenewstack.io/introduction-to-laravel-for-ruby-on-rails-or-django-fans/)是一个基于PHP的全栈Web应用程序框架。它对开发者非常友好，被广泛使用，并且拥有强大的社区。它旨在简化和加速Web开发。Laravel v10将于2025年2月4日达到其生命周期结束。

### 2. OpenSSL v3.1 (2025年3月14日)

OpenSSL被广泛用于Web和通信平台上的加密、安全通信。它很可能是此列表中最常用的软件包；任何具有API的东西都可能使用它。OpenSSL v3.1将于2025年3月14日达到其生命周期结束。

### 3. Ruby v3.1 (2025年3月31日)

[Ruby](https://thenewstack.io/why-ruby-on-rails-is-still-worth-your-while-as-a-developer/)是一种编程语言，广泛用于Ruby on Rails Web框架。Ruby on Rails以能够快速开发基于Web的应用程序而闻名。Ruby v3.1将于2025年3月31日达到其生命周期结束。

### 4. Node.js v18 (2025年4月30日)

[Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/)是一个跨平台的JavaScript运行时环境，无需过多介绍。许多公司——包括一些最大的公司——使用它来构建快速且可扩展的应用程序。Node.js v20在V8引擎中引入了权限模型和性能更新。Node.js v18将于2025年4月30日达到其生命周期结束。

### 5. Django v5.0 和 v5.1 (2025年4月30日)

[Django](https://thenewstack.io/what-is-pythons-django/)是一个基于Python的Web应用程序框架，可以快速、轻松和干净地开发程序。它可以很好地处理复杂的数据库，使其适用于数据密集型应用程序、数据科学工具和社交媒体应用程序。Django v5.0和v5.1将于2025年4月30日到期。

### 6. Kafka v3.4 (2025年5月3日) 和 v3.5 (2025年8月25日)
[Kafka](https://thenewstack.io/gitops-for-kafka-at-scale/) 是最可扩展和广泛采用的分布式发布/订阅框架之一，适用于实时数据管道和分析用例。Kafka 以可扩展、容错的方式处理大量数据的能力使其成为许多大型数据架构的基石。v3.4 将于 2025 年 5 月 3 日达到其生命周期终点。v3.5 将于 2025 年 8 月 25 日达到其生命周期终点。

### 7. Drupal v10（2025 年 6 月 16 日）

[Drupal](https://thenewstack.io/drupal-creator-websites-needed-more-than-ever-in-the-ai-era/) 是一个 CMS 和框架，以其灵活性、可扩展性和可扩展性而闻名。它广泛应用于以内容为中心的平台，如网站、社区和社交平台以及媒体公司。Drupal v10.3，Drupal 10 的最后一个受支持版本，将于 2025 年 6 月 16 日结束其支持。

### 8. Kubernetes < v1.32（2025 年 7 月）

[Kubernetes](https://thenewstack.io/kubernetes/) 是使用最广泛的容器编排平台。大多数容器化应用程序都会使用某个版本的 Kubernetes，尤其是那些具有复杂系统且可以从微服务架构中受益的应用程序。与许多开源软件发布计划一样，Kubernetes 发布遵循结构化的时间表，其中每个次要版本在发布后都将获得一年的完整支持，并在其生命周期结束前有 2 个月的维护期。Kubernetes v1.34 于 2024 年 5 月 15 日发布，预计将于 2025 年 5 月达到其完整支持的终点，并于 2025 年 7 月达到其生命周期终点。

### 9. MongoDB 6（2025 年 7 月 31 日）

[MongoDB](https://thenewstack.io/5-reasons-to-run-mongodb-on-kubernetes/) 是一个多功能、可扩展的 NoSQL 数据库，广泛应用于各个行业，并因其对各种数据（完全结构化、半结构化和非结构化）的灵活支持而备受喜爱。MongoDB 7 带来了一些令人兴奋的改进，例如可查询加密，但这也意味着 6 将于 2025 年 7 月 31 日达到其生命周期终点。

### 10. NumPy v1（2025 年 9 月 17 日）

[NumPy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) 起源于 Numerical Python (Numeric) 的一个分支，并融入了 Numarray 的改进。Python 科学计算社区广泛采用它，这对于密集的数值数据处理和计算应用程序来说非常棒。在 2025 年 9 月 17 日，所有 v1 版本都将达到其生命周期终点。

### 11. Postgres v13（2025 年 11 月 13 日）

[PostgreSQL](https://thenewstack.io/modern-postgresql-deployment-3-cloud-native-approaches-you-should-know/) 是一个高度可扩展的关系数据库管理系统，支持 SQL 用于查询和数据管理。它广泛应用于数据分析、业务数据库和 Web 应用程序。V13 将于 2025 年 11 月 13 日达到其生命周期终点。

### 12. Angular v17（2025 年 5 月 15 日）和 v18（2025 年 11 月 19 日）

[Angular](https://thenewstack.io/angular-shares-potential-ideas-for-2025-improvements/) 是 Google 工程师于 2010 年推出的一个综合框架，后来经过重写以取代 2016 年的 AngularJS。它被广泛用于构建可扩展的 Web 应用程序。
Angular v17 将于 2025 年 5 月 15 日结束，v18 将于 2025 年 11 月 19 日结束。

迁移需要大量的时间（和金钱）。迁移的复杂性取决于多种因素，包括开源软件包/框架、代码库的整洁程度、团队规模和应用程序规模。在 HeroDevs，我们花大量时间与组织讨论迁移和补救选项。从前端 AngularJS 迁移（其中 10 万行代码的迁移可能需要 [2.7 years of effort](https://xlts.dev/blog/2021-01-15-the-math-of-migrating-from-angularjs)）到 Spring 5->6 迁移（其中具有许多依赖项的大型项目可能需要 [more than 6 years of effort](https://www.herodevs.com/blog-posts/spring-framework-6-the-full-cost-of-migrating-from-v5-to-v6)），这些 EOL 时刻应该进行规划和预算。

假设您依赖的 OSS 软件包预计在来年发生 EOL 事件。在这种情况下，您应该已经开始您的规划和迁移——特别是如果您所在的行业受到高度监管，例如医疗保健 (HIPAA)、支付 (SOC 2 和 PCI DSS)、教育 (FERPA) 和政府 (FedRAMP)。

如果您需要更多时间，还有其他选择。直接或第三方商业支持可以提供扩展的长期支持，使您可以根据自己的时间表规划迁移并确保数据的安全。

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)