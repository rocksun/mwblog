<!--
title: Akamai接管Kernel.org的托管
cover: https://cdn.thenewstack.io/media/2025/03/9883917f-nocc_1-scaled.jpg
summary: 重磅！Akamai接管Kernel.org托管，拥抱开源！推出AI推理服务Akamai Cloud Inference，押注RTX 40系GPU，联手Fermyon发力WebAssembly (WASM)边缘计算。容器平台用Linode Kubernetes Engine (LKE) 和 Akamai App Engine，加速进军云计算！
-->

重磅！Akamai接管Kernel.org托管，拥抱开源！推出AI推理服务Akamai Cloud Inference，押注RTX 40系GPU，联手Fermyon发力WebAssembly (WASM)边缘计算。容器平台用Linode Kubernetes Engine (LKE) 和 Akamai App Engine，加速进军云计算！

> 译自：[Akamai Picks Up Hosting for Kernel.org](https://thenewstack.io/akamai-picks-up-hosting-for-kernel-org/)
> 
> 作者：Frederic Lardinois

[Akamai](https://www.akamai.com/) 将于下周在伦敦举行的 KubeCon EU 大会之前发布一系列公告。在其他新闻中，Akamai 今天推出了一个用于 AI 应用程序的推理服务，并额外支持 [WebAssembly](https://thenewstack.io/what-is-webassembly-wasm/) (WASM) 工作负载，并宣布它现在是 [kernel.org](https://www.kernel.org/) 的基础设施合作伙伴，kernel.org 是 Linux 内核源代码的主要分发系统，并将接管其托管并提供云计算和内容分发网络支持。

Akamai 表示，它已与 Linux 基金会管理的 Linux 内核组织签署了一项多年协议，以“为该项目及其全球开发者群体提供基础设施服务”。

“我们非常致力于开源。我们建立在像 Linux 这样的开源技术之上。我们是内核的重度用户。我们一直非常积极地参与各种不同的标准机构，”Akamai 产品高级副总裁 Jon Alexander 告诉我。“开源对于 Akamai 来说非常重要，我们希望回馈社区，而支持 Linux 内核是我们能做到的一种方式。”

Cloud Native Computing Foundation (CNCF) 的 CTO Chris Aniszczyk 也对此表示赞同。“Akamai 在开源社区中有着深厚的根基，”他说。“作为 CNCF 的重要成员，他们积极为包括 OpenTelemetry、Argo 和 Prometheus 在内的关键项目做出了贡献，并为计算基础设施项目捐赠了 100 万美元的基础设施信用额度。他们为 Linux 内核提供的支持进一步展示了该公司长期以来对开源项目及其人员和软件的管理和承诺。”

至于 AI 工作负载的推理服务，被称为 Akamai Cloud Inference，该公司采取了一种有趣的方法，即押注标准的 RTX 40 系列 GPU，Akamai 表示这使其能够在数据中心提供更好的密度。

“[这些芯片] 已经存在了 18 到 24 个月了，所以相对于 GPU 的发展来说，已经算是比较老的了。但对我们来说，它确实处于成本和性能、功耗以及我们可以在服务器机箱中获得的密度之间的最佳位置。它对我们来说效果很好，”Alexander 说。“我们将推出新一代产品，可能在今年年底或明年年初。我们已经在测试下一代显卡，但我们真正关注的是我们可以打包和并行化工作负载的密度。”

Akamai 正在与 Fermyon 合作，将该公司的无服务器 WebAssembly 平台也引入其 Cloud Inference 平台。

Akamai 表示，这将使开发人员能够直接从运行在其边缘网络上的基于 Wasm 的无服务器应用程序查询 LLM。但 Alexander 指出，也许更重要的是，Fermyon 的技术还允许多个租户以内存安全的方式访问同一个 GPU。

Wasm 在企业中仍处于早期阶段，但 Akamai 希望走在发展趋势的最前沿。

Akamai 最近还与 [VAST Data 合作](https://www.prnewswire.com/news-releases/akamai-and-vast-data-working-to-usher-in-the-era-of-edge-ai-inference-302403897.html)，以便为这些 AI 应用程序提供更好的实时数据访问，并且对于位于整个服务核心的容器平台，Akamai 正在使用 Linode Kubernetes Engine (LKE) 和 Akamai App Engine，这是该公司[最近宣布的](https://www.akamai.com/newsroom/press-release/akamai-launches-cloud-agnostic-ready-to-run-application-platform)应用程序平台。

所有这一切都发生在 Akamai 当前专注于超越其内容分发网络并进入云计算领域的背景下。它在这方面的努力包括为其一些核心客户提供专门的服务（例如，它今天还推出了新的视频编码和解码加速器），但也通过这些新的 AI 服务以及当然还有它在 2022 年收购的 Linode 云来扩大范围。