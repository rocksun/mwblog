
<!--
title: Redis转向源代码可用许可证
cover: ./cover.png
-->

云服务提供商托管 Redis 产品将不再被允许免费使用 Redis 源代码，该公司表示。

> 译自 [Redis moves to source-available licenses](https://www.infoworld.com/article/3714743/redis-moves-to-source-available-licenses.html)，作者 Paul Krill。

Redis 宣布，从 Redis 7.4 开始，所有未来版本的 Redis 软件都将在 [Redis 源代码可用许可证 (RSAL 2)](https://redis.com/legal/rsalv2-agreement/) 和 [服务器端公共许可证 (SSLPv1)](https://redis.com/legal/server-side-public-license-sspl/) 下获得双重许可。这款流行的 [NoSQL 数据库](https://www.infoworld.com/article/3240644/what-is-nosql-databases-for-a-cloud-scale-future.html) 将不再在三条款伯克利软件发行 (BSD) 许可证下发行。

该公司在 [3 月 20 日](https://redis.com/blog/redis-adopts-dual-source-available-licensing/) 表示，新的源代码可用许可证将允许 Redis 公司对其源代码提供宽松的使用权限。源代码将继续通过 Redis 社区版免费提供给开发者、客户和合作伙伴。

未来的 Redis 源代码可用许可证将把核心 Redis 与 Redis Stack 统一到一个软件包中，其中包括搜索、JSON、向量、概率和时间序列数据模型。该公司表示，这将允许 Redis 软件用于各种场景，包括键值和文档存储、查询引擎以及为 [生成式 AI](https://www.infoworld.com/article/3689973/what-is-generative-ai-artificial-intelligence-that-creates.html) 应用程序提供支持的低延迟向量数据库。

该公司表示，Redis 遇到了挑战。Redis 软件的大部分商业销售都是通过最大的云服务提供商进行的，这些提供商将 Redis 的投资及其开源社区商品化。该公司表示，尽管努力支持社区主导的治理模式并希望保留 BSD 许可证，但同时交付多个软件发行版与 Redis 成功推动技术的能力背道而驰。

该公司表示，根据新的许可，托管 Redis 产品的云服务提供商将不再被允许免费使用 Redis 源代码。但实际上，对于 Redis 开发者社区来说，没有任何变化，他们仍将在双重许可下获得宽松的许可。所有 Redis 客户端库都将保持开源许可。

RSALv2 是一种宽松的非 copyleft 许可证，允许“使用、复制、分发、提供和准备软件的衍生作品”的权利。该公司表示，RSALv2 只有两个主要的限制：根据 RSALv2，用户不得将软件商业化或作为托管服务提供给其他人；并且用户不得删除或掩盖任何许可、版权或其他声明。
