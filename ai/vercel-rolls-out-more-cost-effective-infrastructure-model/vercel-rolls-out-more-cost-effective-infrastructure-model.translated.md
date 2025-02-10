# Vercel 推出更具成本效益的基础设施模型

![Featued image for: Vercel Rolls Out More Cost-Effective Infrastructure Model](https://cdn.thenewstack.io/media/2025/02/4b6a91e4-vercel-introduces-fluid-1024x684.jpg)

前端云托管提供商 Vercel 的 edge worker/runtime 时代已经过去，CEO [Guillermo Rauch](https://www.linkedin.com/in/rauchg/) 昨天早些时候在推特上表示。

他还补充说：“事实上，截至上周，所有 Edge 中间件都在 Vercel 云中的 Fluid 上运行。”

Edge Network 是 Vercel 的一项产品，它既是内容分发网络 (CDN)，也是一个在全球区域运行计算的全球分布式平台。

[Fluid](https://vercel.com/fluid) 是一种新的 Web 应用程序基础设施模型，旨在融合服务器和无服务器的最佳特性，同时提供高效的资源利用率，更重要的是，降低 Vercel 客户的成本。
Fluid 是多区域的，但这并不意味着“数十或数百个 [CDN 边缘](https://thenewstack.io/from-cdn-edge-to-fornax-toward-a-next-gen-edge-cloud-platform/)”，Rauch 写道。

## ‘边缘不适用于应用、API、数据库’

[边缘计算](https://thenewstack.io/edge-computing/what-is-edge-computing/) 最适合路由、静态资产和预渲染，但不适用于应用、API 和数据库，Rauch 在他的推文中表示，并在当天晚些时候与 CTO [Malte Ubl](https://www.linkedin.com/in/malteubl/) 的网络直播中重申了这一点。
“最大的洞察是，你的应用程序，[the] 真正的逻辑，必须靠近数据运行，因为你会来回传递数据，就像数据瀑布一样；这会很慢，”Ubl 说。“边缘计算的梦想，即你突然在所有这 200 个位置都有你的数据，这个梦想根本不是现实。”

此外，绝大多数 Vercel 客户将其数据托管在一个位置，他补充说。

“我喜欢举的例子是，Google 有八个数据中心用于 Google 搜索，”Rauch 补充说。“Google 用八个数据中心做得很好。你不会将 [copy petabytes of data](https://thenewstack.io/linux-low-level-data-copying-with-dd/) 复制到 200 个位置。”

[Mariano Cocirio](https://www.linkedin.com/in/mcocirio/?originalSubdomain=de)，CI/CD 和计算的产品经理，在 [post introducing Fluid](https://vercel.com/blog/introducing-fluid-compute) 中写道，使用 Fluid，计算运行的位置更靠近你的数据已经存在的位置，而不是“试图在每个边缘位置进行不切实际的复制”。

“边缘计算的梦想，即你突然在所有这 200 个位置都有你的数据，这个梦想根本不是现实。”

— Vercel CTO Malte Ubl

“这种方法不是强制进行广泛的数据分发，而是确保你的计算位于与你的数据对齐的区域，从而优化性能和一致性，”他说。“动态请求被路由到最近的健康计算区域（在你的指定位置中），从而确保高效可靠的执行。”

他补充说，对于企业客户，激活 Fluid 时，多区域故障转移是默认设置。

## Fluid 减少冷启动

[Serverless computing](https://thenewstack.io/serverless-computing-in-2024-genai-influence-security-5g/) 可能会受到冷启动的影响，冷启动是指在首次调用函数或不活动后发生的延迟。
Serverless 函数在 [containers](https://thenewstack.io/introduction-to-containers/) 中运行。部署函数时，云提供商将代码和依赖项打包到容器中。当调用函数时，容器需要初始化，这个过程需要时间，因为容器被分配、初始化和加载代码。此外，容器会因不活动而关闭以节省资源。

但是，客户需要为冷启动付费。

![Vercel CTO Malte Ubl introduces Fluid's benefits.](https://cdn.thenewstack.io/media/2025/02/7dc8721e-vercelvideo.png)

Vercel CTO Malte Ubl 解释了 Fluid 的优势。

“如果我打开 Fluid，我刚刚打开了，我将发送另外四个请求，1-2-3-4，它们都击中了同一个实例，”Ubl 说。“你在演示中可以看到的是，它计算了函数存活的总时间，在本例中为 3.4 秒。所以这就是我要支付的全部费用。是的，所以你要为 3.5 秒而不是 12 秒付费 [...] 这就是 Fluid。”

Fluid 通过维护“warm instance”来降低冷启动的频率。Cocirio 表示，它用高性能的迷你服务器代替了单次调用的函数。

Cocirio 写道：“当冷启动确实发生时，具有完整 [Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) 和 [Python](https://thenewstack.io/what-is-python/) 支持的 [Rust-based runtime](https://vercel.com/blog/vercel-functions-are-now-faster-and-powered-by-rust) 加速了初始化。”“[Bytecode caching](https://vercel.com/blog/introducing-bytecode-caching-for-vercel-functions) 通过预编译函数代码进一步加快了调用速度，从而减少了启动开销。”
因此，该模型最大限度地提高了资源效率，并且在早期采用者中，成本降低了高达 85%，他补充说。

Fluid 根据实际计算使用量计费，最大限度地减少了浪费，他强调说。它还优先使用现有资源，然后再创建新实例，Cociro 说：“消除了硬扩展限制，并利用热计算来实现更快、更高效的扩展”，“通过在实例之前扩展函数，Fluid 转向多对一模型，可以处理数万个并发调用。”

## 其他 Fluid 功能

Cicirio 解释说，Fluid 还[降低了失控执行的风险](https://thenewstack.io/mitigating-risks-in-cloud-native-applications/)，而失控执行会推高成本。等待后端响应的函数可以[处理其他请求，而不是浪费](https://thenewstack.io/how-to-identify-your-wasteful-processes/)计算资源。

Fluid 还支持高级任务，例如[流式传输和后响应处理](https://thenewstack.io/real-time-stream-processing-apps-edge-computing-and-kafka/)。它是完全托管的，保留了 serverless 模型的吸引力之一。

尽管如此，Vercel 并未自动将客户切换到 Fluid，它确实要求客户在“项目设置”下的“函数”选项卡中拨动一个开关才能启用它。Rauch 解释说，Vercel 决定不为所有人启用它，因为执行模型略有变化。

“它不需要任何代码更改。我们内置了……缓解措施。它由 [Node](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) 和 Python 提供支持，并且将来会有更多开放运行时，您今天就可以启用它，”Rauch 说。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)