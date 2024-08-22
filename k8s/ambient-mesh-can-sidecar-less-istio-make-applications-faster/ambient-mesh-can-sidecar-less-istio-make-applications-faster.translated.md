# 环境网格：无边车 Istio 能否让应用程序更快？

![环境网格：无边车 Istio 能否让应用程序更快？的特色图片](https://cdn.thenewstack.io/media/2024/08/fed016c6-abstract-1097762_1280-1024x576.jpg)

环境模式是 [Istio](https://thenewstack.io/simplifying-cluster-connectivity-with-istio-service-mesh/) 在 2022 年推出的新型无边车数据平面。当 [环境模式](https://thenewstack.io/ambient-mesh-sidestepping-the-sidecar/) 在今年 5 月达到 [Beta](https://istio.io/latest/blog/2024/ambient-reaches-beta/) 状态时，我观察到用户在将应用程序添加到网格后，对轮胎进行踢打并运行负载测试，以了解性能影响。

受 [Quentin Joly 的博客](https://a-cup-of.coffee/blog/istio/#with-istio-ambient) 关于 Istio 在环境模式下的出色性能以及社区中其他用户的类似反馈的启发，有时应用程序在 [环境模式](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/) 下速度略快，我决定自己验证这些结果。

## 测试环境：

我使用了一个具有 3 个工作节点的 Kubernetes 集群，每个节点具有 256GB 内存和 32 核 CPU。

Istio 使用一些工具来简化一致的基准测试。首先，我们使用一个名为 [Fortio](https://github.com/fortio/fortio) 的负载测试工具，该工具以每秒指定请求数 (RPS) 运行，记录执行时间的直方图并计算百分位数 - 例如，P99，99% 的请求花费的时间少于该数字。

我们还提供了一个名为 [Bookinfo](https://istio.io/latest/docs/examples/bookinfo/) 的示例应用程序，其中包括用 Python、Java、Node.js 和 Ruby 编写的微服务。

每个 Bookinfo 部署都有两个副本，这些副本均匀分布到三个工作节点上。使用 [Pod 反亲和性规则](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)，我确保 Fortio 被放置在与 [details](https://github.com/istio/istio/tree/master/samples/bookinfo/src/details) 服务不同的节点上。

## 初始测试结果

我从 Istio v1.22.3 版本安装了 Bookinfo 应用程序。使用 Fortio 工具将负载驱动到单个 Bookinfo 服务（例如，details）或完整的 Bookinfo 应用程序，我注意到在将所有内容添加到环境网格后，**延迟影响几乎为零**。大多数情况下，它们在平均值或 P90 的 0-5% 范围内。我始终注意到，Istio 环境模式下的 details 服务速度略快，就像 Quentin 在他的博客中报道的那样。

### 负载测试 details 服务

我进行了与 Quentin 相同的测试，通过 10 个连接向 details 服务发送 100 RPS，并收集了无网格和环境的结果。

![](https://cdn.thenewstack.io/media/2024/08/759c0401-image10-1024x381.png)
无网格：向 details 服务发送 100 RPS。

![](https://cdn.thenewstack.io/media/2024/08/bfdfdb1f-image1-1024x382.png)
环境：向 details 服务发送 100 RPS。

就像 Quentin 一样，我不得不运行多次测试来验证环境模式比无网格略好 - 这很难相信！在 Bookinfo details 服务的情况下，添加环境模式平均将延迟提高了 6-11% - 以及添加 mTLS 和 L4 可观察性！

Fortio 到 details |
平均 |
P50 |
P75 |
P90 |
P99 |
差异 |
无网格运行 1 |
0.89ms | 0.64ms | 0.74ms | 0.85ms | 2.67ms | 平均慢 11% 且 P90 慢 5% |
环境运行 1 |
0.80ms | 0.6ms | 0.71ms | 0.81ms | 1.4ms | |
无网格运行 2 |
0.86ms | 0.65ms | 0.75ms | 0.86ms | 1.71ms | 平均慢 6% 且 P90 慢 4% |
环境运行 2 |
0.81ms | 0.61ms | 0.72ms | 0.83ms | 1.56ms | |
无网格运行 3 |
0.90ms | 0.65ms | 0.76ms | 0.88ms | 1.92ms | 平均慢 10% 且 P90 慢 5% |
环境运行 3 |
0.82ms | 0.63ms | 0.72ms | 0.84ms | 1.5ms |
*表 1：Fortio 到 details 服务 100 RPS 10 个连接。*

## 为什么应用程序在环境网格中有时更快？

我们一直被教导服务网格会增加延迟。Quentin 的结果在这里得到了复制，显示了一个工作负载在通过服务网格运行时 *更快* 的情况。发生了什么事？

### 第一个理论


### 翻译者回复

### EDITOR'S RESPONSE
当您的应用程序位于环境网格中时，负载请求首先通过一个名为 [ztunnel](https://istio.io/latest/docs/ambient/overview/#ztunnel) 的轻量级本地节点代理，然后到达目标 ztunnel，最后到达服务。details 服务使用 Ruby 中的 Webrick 库的 HTTP/1.1，我们发现旧版或配置不当的 HTTP 库存在连接管理和保持活动行为不佳的问题。我的第一个假设是，当客户端和服务器位于不同的节点上时，如果应用程序没有使用高效的 HTTP/2 连接，则通过客户端和服务器 ztunnel 进行代理实际上可能更快。Ztunnel 使用连接池和 [HTTP Connect](https://en.wikipedia.org/wiki/HTTP_tunnel) 在节点之间建立安全隧道，以利用并行性和 HTTP/2 流多路复用以应对负载。

但是，这个理论有一些挑战。为什么我只在 details 服务中观察到这种现象，而没有在其他任何 Bookinfo 服务中观察到？

进一步研究后，我发现我们的 Fortio 负载工具 [默认情况下启用了连接保持活动](https://github.com/fortio/fortio/blob/8a7d9112667e637139c788b68cb063f456d20cb4/bincommon/commonflags.go#L55)。对于来自 Fortio 到 details 服务的 10 个连接，以及 details 服务（使用 WEBrick Ruby 库）尊重连接保持活动设置，这些连接可以在没有环境的情况下有效地重复使用。

### 使用连接关闭进行负载测试
接下来，我探索了运行相同的负载测试，并设置了 `Connection: close`
标头。这强制禁用任何 HTTP 连接池，这是测试此假设的好方法。

12 |
curl -v -d '{"metadata": {"url":"http://details:9080/details/0", "c":"10", "qps": "100", "n": "2000", "async":"on", "save":"on"}}' "localhost:8081/fortio/rest/run?jsonPath=.metadata" -H "Connection: close" |
![](https://cdn.thenewstack.io/media/2024/08/521b5db4-image2-1024x397.png)
无网格：Fortio 到 details 服务 100 RPS 10 个连接，连接关闭。

![](https://cdn.thenewstack.io/media/2024/08/793c4a4b-image5-1024x393.png)
环境：Fortio 到 details 服务 100 RPS 10 个连接，连接关闭。

Fortio 到 details |
平均 |
P50 |
P75 |
P90 |
P99 |
差异 |
无网格 |
1.90ms | 1.72ms | 2.28ms | 2.77ms | 3.98ms | |
环境 |
2.06ms | 2.15ms | 2.65ms | 2.94ms | 4ms | 平均值慢 8%，P90 慢 6% |
*表 2：Fortio 到 details 服务 100 RPS 10 个连接，连接关闭。*
与表 1 的结果相比，表 2 的数字响应时间要高得多，这是预期的，因为每个连接在从 details 服务收到每个响应后立即关闭。鉴于 P50、P75、P90 和 P99 在环境运行中都比连接关闭慢，因此似乎可以安全地排除 ztunnel 中的连接池，因为第一个理论可能会使请求更快。

### 第二个理论
我注意到 John Howard 在我们新的 Istio v1.23 版本中对 Bookinfo 应用程序的 details 和 productpage 服务进行了一个 [与性能相关的 PR](https://github.com/istio/istio/pull/51428/files)。对于 details 服务，PR 为 details WEBrick 服务器启用了 [TCP_NODELAY](https://brooker.co.za/blog/2024/05/09/nagle.html) 标志，这将减少 details 服务响应时间的不必要延迟（最多 [40ms](https://vorner.github.io/2020/11/06/40-ms-bug.html)）。对于 productpage 服务，PR 启用了传入请求的保持活动，这将重复使用现有的传入连接，从而提高性能。

使用包含修复程序的最新更新的 details 部署，我重复了相同的测试，通过 10 个连接向 details 服务发送 100 RPS。无网格和环境的结果非常接近，因此我分别运行了三次测试以确保结果一致。以下是每个场景第一次运行的屏幕截图：

![](https://cdn.thenewstack.io/media/2024/08/bb534c52-image13-1024x330.png)
无网格：Fortio 到新的 details 服务 100 RPS 10 个连接。

![](https://cdn.thenewstack.io/media/2024/08/7b1acd40-image4-1024x332.png)
环境：Fortio 到新的 details 服务 100 RPS 10 个连接。

我为每个场景的三次运行构建了一个表格：

Fortio 到 details |
平均 |
P50 |
P75 |
P90 |
P99 |
差异 |
|
1 |
无网格 |
0.76ms | 0.58ms | 0.69ms | 0.81ms | 1.56ms | 平均值慢 5%，P90 慢 5%。P99 慢 25% |
环境 |
0.72ms | 0.57ms | 0.66ms | 0.76ms | 1.24ms | ||
2 |
无网格 |
0.72ms | 0.59ms | 0.7ms | 0.82ms | 1.6ms | P90 慢 3%，P99 慢 18% |
环境 |
0.76ms | 0.59ms | 0.69ms | 0.8ms | 1.37ms | 平均值慢 5% |
|
3 |
无网格 |
0.77ms | 0.58ms | 0.7ms | 0.8ms | 1.49ms | 平均值慢 1%，P99 慢 8% |
环境 |
0.76ms | 0.59ms | 0.69ms | 0.81ms | 1.38ms | P90 慢 1% |
*表 3：Fortio 到新的 details 服务 100 RPS 10 个连接。*
与表 1 中的先前结果相比，表 3 中的无网格数量有了相当大的改进（在较高百分比下比环境数量更显著），现在更接近环境数量。Ztunnel 默认情况下启用了 [TCP_NODELAY](https://github.com/istio/ztunnel/pulls?q=is%3Apr+is%3Aclosed+TCP_NODELAY)，这有助于在表 1 中，当旧的 details 服务未启用 TCP_NODELAY 时，环境性能比无网格性能有所提高。当新的 details 服务启用 TCP_NODELAY 时，它也略微改善了环境响应时间。

表 3 还显示，对于这种类型的负载测试，在启用 TCP_NODELAY 的情况下，对新的 details 服务进行负载测试，无网格和环境运行之间的平均值、P50、P75 和 P90 几乎没有差异。这些运行之间的差异可能是噪声，除了 P99，无网格始终慢 8% 或更多。

### 第三理论
继续查看表 3 中的测试结果，为什么在存在额外的跳跃到 ztunnel pod 以及环境提供的重大优势（例如 Fortio 和 details 服务之间的 mTLS 和 L4 可观察性）的情况下，无网格和环境之间会存在类似的延迟？对于 P99 情况，为什么环境模式下的 details 服务始终更快？

Ztunnel 提供出色的读/写缓冲区管理，并具有 HTTP/2 多路复用功能，这可以有效地最小化甚至消除通过客户端和服务器 ztunnel pod 添加的额外跳跃带来的开销。我决定使用 [strace](https://strace.io/) 从 Fortio 和 details 服务中使用系统调用来测量这一点，方法是进入它们的 Kubernetes 工作节点并使用 strace 附加 pid，同时过滤掉不相关的跟踪：

1 |
strace -fp {pid} -e trace=write,writev,read,recvfrom,sendto,readv |
details 服务的 strace 输出在无网格和环境情况下类似：
123456 |
…read(9, "GET /details/0 HTTP/1.1\r\nHost: d"..., 8192) = 118write(9, "HTTP/1.1 200 OK\r\nContent-Type: a"..., 180) = 180write(9, "{\"id\":0,\"author\":\"William Shakes"..., 178) = 178write(2, "192.168.239.19 - - [13/Aug/2024:"..., 80) = 80… |
*输出 1：无网格或环境 - 将 strace 附加到 details 服务的 PID。*
Fortio 服务的 strace 输出在无网格和环境情况下不同。在无网格情况下，我们看到 Fortio 执行了两个读取操作，一个用于 HTTP 标头，另一个用于正文。

1234567 |
…read(13, "HTTP/1.1 200 OK\r\nContent-Type: a"..., 4096) = 180read(13, "{\"id\":0,\"author\":\"William Shakes"..., 4096) = 178…write(19, "GET /details/0 HTTP/1.1\r\nHost: d"..., 118) = 118… |
*输出 2：无网格 - 将 strace 附加到 Fortio 的 PID。*
在环境情况下，我们始终只看到一个读取操作，用于标头和正文。

12345 |
…read(19, "HTTP/1.1 200 OK\r\nContent-Type: a"..., 4096) = 358…write(19, "GET /details/0 HTTP/1.1\r\nHost: d"..., 118) = 118… |
*输出 3：环境网格 - 将 strace 附加到 Fortio 的 PID。*
为什么会这样？写入调用保持不变是有道理的，因为它们完全基于应用程序行为，在本例中没有改变。环境合并了这些多个应用程序写入，并将它们转换为单个网络写入，并隐含地转换为对等方中的单个读取。

在上面的测试场景中，我观察到启用环境后，Fortio 服务的总系统调用减少了 60%。这**非常**显著，并解释了延迟改进的大部分原因，以及 Fortio pod 在环境启用时峰值时间的 CPU 减少约 25%。系统调用的减少超过了 mTLS 和 ztunnel 其他功能的成本。我预计这种模式在企业中非常普遍，一些 HTTP 库和应用程序在缓冲和刷新方面做得更好，而另一些则没有那么好。这通常与应用程序的年代和它们构建的 SDK 相关。

![](https://cdn.thenewstack.io/media/2024/08/9d4def12-image9-1024x504.png)
无网格和环境运行：Fortio 到 details 服务 100 QPS 10 个连接。

## 整个 Bookinfo 应用程序怎么样？
使用新更新的 details 和 productpage 部署，我开始通过 100 个连接向 Bookinfo 应用程序发送 1000 RPS，并观察到无网格和环境的出色结果。

![](https://cdn.thenewstack.io/media/2024/08/fb60cd42-image3-1024x318.png)
无网格：Fortio 到新的 Bookinfo 应用程序 1000 RPS 100 个连接。

![](https://cdn.thenewstack.io/media/2024/08/1d2099d9-image8-1024x316.png)
无网格：Fortio 到新的 Bookinfo 应用程序 1000 RPS 100 个连接。

Fortio 到 Bookinfo |
平均值 |
P50 |
P75 |
P90 |
P99 |
平均差异 |
无网格 |
1.39ms | 1.32ms | 1.42ms | 1.67ms | 2.19ms | |
环境 |
1.40ms | 1.34ms | 1.48ms | 1.68ms | 2.94ms | 平均值和 P90 慢不到 1% |
*表 4：Fortio 到新的 Bookinfo 应用程序 1000 RPS 100 个连接。*
为了比较，我还对 v1.22.3 中提供的旧 Bookinfo 示例进行了相同的测试，您可以看到新的 Bookinfo 在响应时间方面有了 **5-10 倍** 的改进，无论是无网格还是环境模式！

Fortio 到 Bookinfo | 平均 | P50 | P75 | P90 | P99 | 平均差异 |
------- | -------- | -------- | -------- | -------- | -------- | -------- |
无网格 | 6.35ms | 4.68ms | 7.44ms | 11.4ms | 36.63ms | |
环境 | 6.74ms | 4.9ms | 7.79ms | 12.12ms | 41.14ms | 慢 6% |

*表 5：Fortio 到旧 Bookinfo 应用程序 1000 RPS 100 个连接。*

将负载增加到 4000 RPS，使用 400 个连接，使用新的 Bookinfo 部署：

![](https://cdn.thenewstack.io/media/2024/08/8d5e182e-image6-1024x317.png)

环境：Fortio 到新的 Bookinfo 应用程序 4000 RPS 400 个连接。

![](https://cdn.thenewstack.io/media/2024/08/b14cf82e-image11-1024x315.png)

环境：Fortio 到新的 Bookinfo 应用程序 4000 RPS 400 个连接。

响应时间仍然非常好，远好于旧的 Bookinfo 应用程序，它只有 1000 RPS 和 100 个连接（表 5）：

Fortio 到 Bookinfo | 平均 | P50 | P75 | P90 | P99 | 平均差异 |
------- | -------- | -------- | -------- | -------- | -------- | -------- |
无网格 | 1.54ms | 1.33ms | 1.54ms | 2.25ms | 3.98ms | |
环境 | 1.58ms | 1.37ms | 1.57ms | 2.33ms | 4.9ms | 平均慢 3%，P90 慢 4% |

*表 6：Fortio 到新的 Bookinfo 应用程序 4000 RPS 400 个连接。*

很高兴看到 Bookinfo 可以处理 4000 RPS 且没有任何错误，环境模式比无网格模式慢约 3-4%，但它具有 mTLS 传输加密和 L4 可观测性的所有优势。我记得我只能使用旧的 Bookinfo 应用程序达到 1200 RPS，这已经导致了很小比例的错误。现在我可以将负载增加到 4000 RPS 或更高，而不会出现错误。

## 总结：
L4 处的环境模式对用户应用程序延迟的影响非常小，有时甚至会自动 *改进*！结合通过标记命名空间来注册应用程序到环境模式而无需重新启动任何工作负载的简单 UX，它为用户提供了我们最初将其命名为环境模式时所期望的愉快体验。

我要感谢所有 Istio 维护者构建了如此令人愉快的项目，并感谢 CNCF 为 Istio 项目提供了 [基础设施实验室](https://www.cncf.io/community-infrastructure-lab/) 的访问权限，我在那里进行了测试。我还想感谢 Quentin Joly 和许多用户，他们向我提供了“环境模式有时比无网格模式略快”的反馈，这促使我运行上述基准测试，以亲身体验负载下的改进或微小的延迟影响。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)