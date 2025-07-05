<!--
title: 更轻松地构建和部署可扩展的技术架构
cover: https://cdn.thenewstack.io/media/2025/06/ff66e75c-studio-republic-fotkkqwnmq4-unsplash-scaled.jpg
summary: 作者分享了构建可扩展系统的实战经验，包括验证层、事件驱动通信、微前端、领域驱动设计和数据库优化等策略，强调可扩展性是架构设计的核心，而非事后考虑。
-->

作者分享了构建可扩展系统的实战经验，包括验证层、事件驱动通信、微前端、领域驱动设计和数据库优化等策略，强调可扩展性是架构设计的核心，而非事后考虑。

> 译自：[Build and Deploy Scalable Technical Architecture a Bit Easier](https://thenewstack.io/build-and-deploy-scalable-technical-architecture-a-bit-easier/)
> 
> 作者：Stephen Romain

构建能够有效扩展的系统是软件工程中最具挑战性的方面之一。通过指导多个公司的多个项目完成关键的演进，我开发出了一套经过实战检验的方法，用于创建能够承受快速用户增长和日益增长的技术复杂性的架构。

将概念验证系统转变为可用于生产环境的架构时，一个关键的挑战是在快速开发和未来的可扩展性之间取得平衡。在一家组织中，我接手了一个单体 Python 应用程序，该应用程序最初是作为一个潜在客户分配系统构建的。该原型在受控环境中表现良好，但在[处理真实世界的地址数据时遇到了困难](https://thenewstack.io/ai-adoption-why-businesses-struggle-to-move-from-development-to-production/)，这些数据本质上包含不一致和边缘情况。

这种转变需要在系统入口点实施强大的验证层，并引入全面的错误跟踪以及自动重试逻辑。将单体应用程序分解为离散的服务，实现了独立的扩展——这种转变尤其关键，因为原始架构使得团队和组件的扩展几乎不可能。

最重要的架构转变发生在事件驱动的通信模式的实施过程中。通过设计通过异步消息传递进行通信的轻量级服务，每个服务订阅特定的事件流，我们实现了横向扩展，同时隔离了故障，以防止全系统范围的中断。其影响是可衡量的；端到端系统可靠性显著提高，故障率下降了 80% 以上。

我一直坚持实施几种架构模式，这些模式已被证明对于扩展技术系统至关重要。在处理复杂的前端应用程序时，使用 React 和 Next.js 实施微前端架构使团队能够独立地开发、测试和部署。这种方法需要仔细考虑共享状态管理和标准化的设计系统，但它允许团队按照自己的节奏发布功能，同时保持性能问题是孤立的，而不是全系统的。

数据库性能通常会成为扩展系统中的主要瓶颈。[领域驱动设计 (DDD)](https://www.geeksforgeeks.org/best-practices-for-microservices-architecture/) 已被证明对于创建松散耦合的微服务特别有价值，其战略阶段确保设计架构正确地封装了业务能力，而战术阶段允许使用有效的设计模式创建领域模型。

对于数据库优化，我实施了多层方法，包括 PostgreSQL 只读副本以减轻主实例的压力，逻辑分片以跨边界分配负载，以及有针对性的索引创建以提高查询性能。现代数据库扩展技术通常分为[两类](https://www.instaclustr.com/education/postgresql/scaling-postgresql-challenges-tools-and-best-practices/)：垂直扩展（“向上扩展”），它提高了现有硬件的能力，以及水平扩展（“向外扩展”），它将工作负载分布在多个服务器或数据库实例上。

具体来说，对于 PostgreSQL，[优化摄取](https://www.timescale.com/learn/best-practices-for-scaling-postgresql)速率通常涉及将数据分批插入，每次插入 50-100K 行，这利用了 PostgreSQL 在高效处理批量数据方面的优势。根据我的经验，使用 Redis 对经常访问的[数据实施内存缓存，可以持续减少数据库](https://thenewstack.io/how-open-source-and-time-series-data-fit-together/)负载，同时显著缩短响应时间。

在我之前的一个职位中，我们的遗留 API 层是一个单体框架，随着用户数量的快速增长，它变得越来越难以维护和扩展。由于争夺相同资源的团队之间的竞争，我们经历了无法预测的中断和部署延迟。我领导了向微服务架构的过渡，根据领域和[数据访问模式](https://thenewstack.io/kumo-surfaces-structured-data-patterns-generative-ai-misses/)仔细确定了服务边界。

这种方法与[最佳实践](https://microservices.io/patterns/microservices.html)相一致，这些实践将应用程序构建为一组可独立部署、松散耦合的组件。每个服务都维护着特定业务子域的所有权，API 网关充当应用程序的主要入口点。这种模式实现了通过服务协作模式实现的分布式系统[操作](https://thenewstack.io/how-saas-based-global-server-load-balancing-eases-it-burden/)。

这种转变使我们能够根据需求扩展单个服务，而不是扩展整个应用程序。它还使我们能够针对高流量端点实施有针对性的性能优化，并通过明确定义的服务所有权来实现团队自主性。部署频率从每两周一次增加到每天一次，系统可靠性显着提高。

实施适当的测试框架始终会产生出色的长期效果。在有生产事件历史的组织中，我引入了全面的测试策略，包括用于业务逻辑的单元测试、用于关键用户旅程的集成测试以及用于验证服务之间 API 兼容性的契约测试。通过要求在部署之前进行全面的测试覆盖，我们大大[减少了生产事件，同时通过消除手动测试周期来加速开发](https://thenewstack.io/boost-developer-productivity-by-reducing-their-paper-cuts/)。

在实施微服务时，使用诸如[断路器之类的模式来防止系统中一个部分的故障级联到其他部分](https://www.capitalone.com/tech/software-engineering/10-microservices-best-practices/)至关重要。此模式通过在依赖项无响应时使外部调用超时并返回默认响应来帮助维护服务健康。

在我的项目中，数据库优化始终提供了一些最显著的性能改进。在实施任何扩展策略之前，必须通过评估应用程序主要处理事务处理 (OLTP) 还是分析处理 (OLAP) 工作负载来了解关键瓶颈。

在一种情况下，我们的 PostgreSQL 实例在不断增加的负载下苦苦挣扎，一些查询需要几秒钟才能完成。通过仔细分析，我为经常连接的数据实施了[战略性反规范化](https://keyholesoftware.com/best-practices-for-scaling-a-postgresql-database/)，并为复杂的报告查询实施了物化视图。我还引入了[分区技术](https://www.timescale.com/learn/guide-to-postgresql-scaling)，通过基于日期范围等逻辑边界将大表分解为更小、更易于管理的块来提高查询性能。

对于具有数据保留策略的系统，[表分区被证明特别有效](https://onesignal.com/blog/lessons-learned-from-5-years-of-scaling-postgresql/)，它将一个表变成了多个表，同时保持了应用程序的单个表的外观。这使我们能够通过删除整个分区表而不是执行有针对性的删除来简单地实施保留，从而防止数据库膨胀。

这些优化将平均查询时间从几秒减少到几毫秒，从而能够在相同的基础设施上支持更高的用户负载。正如我为一位利益相关者总结的那样：“我们不仅仅使数据库更快——我们从根本上改变了它随着增长的扩展方式。”

从概念验证到企业级系统的旅程需要技术专长和战略眼光。通过专注于弹性架构模式、周到的技术选择和系统的性能优化，团队可以构建随着业务增长而优雅扩展的系统。

这些方法已被证明在多个行业和技术堆栈中有效，但它们具有一个共同的基础：将可扩展性视为一个基本的架构问题，而不是事后才考虑的问题。通过在开发过程的早期采用这种心态，组织可以避免痛苦的重写和服务中断，而这些重写和服务中断通常伴随着增长。