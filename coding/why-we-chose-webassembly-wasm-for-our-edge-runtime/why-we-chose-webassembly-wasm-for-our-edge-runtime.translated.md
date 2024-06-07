# 我们为何为边缘运行时选择 WebAssembly (Wasm)

![我们的边缘运行时为何选择 WebAssembly (Wasm) 的特色图片](https://cdn.thenewstack.io/media/2024/05/decce164-webassembly-at-the-edge-featured-image.jpg)

边缘计算使组织能够分配工作负载，将其移至更靠近用户的位置，并针对个性化用户体验更精细地定制输出。然而，在边缘部署容器（更不用说虚拟机 (VM) 及其所有操作系统开销）由于资源限制而不可行。

[WebAssembly (Wasm)](https://thenewstack.io/webassembly/) 是一种用于可执行文件的开放二进制格式，它承诺提供一种轻量级且安全的替代方案，更适合边缘的受限环境。在本文中，我将解释我们为何在 Gcore 选择 Wasm 作为我们最新的 [边缘计算](https://thenewstack.io/edge-computing/) 解决方案 FastEdge 的运行时。我还将分享是什么启发了我们最初构建 FastEdge。

## FastEdge：满足对边缘计算的需求

将流量路由进出数据中心会浪费时间和金钱。随着对越来越个性化的网络体验的需求不断增长，我们需要探索一种新的云计算方法。幸运的是，我们已经通过我们的内容分发网络 (CDN) 构建了一个边缘节点网络。向我们的 CDN 节点添加计算能力是合乎逻辑的下一步。

为了构建 FastEdge，我们首先向我们的 CDN 节点添加了一个 Wasm 运行时，并为常见的网络应用程序任务（如图像调整大小、文件上传或内容转换）构建了边缘应用程序。这些应用程序与我们的 CDN 执行的任务密切相关。它们为我们的客户提供了边缘计算的好处，而无需编写代码，并让我们在为自定义应用程序开放之前使用实际用例测试和完善我们的边缘平台。

我们于今年早些时候向公众[发布了 FastEdge](https://gcore.com/fastedge)，允许我们的客户使用我们的软件开发工具包 (SDK) 构建自己的边缘支持应用程序。

## 为何选择 Wasm？

Wasm 是为 FastEdge 提供支持的技术。它是一种用于可执行文件和运行时的开放标准，类似于 Java。然而，正如其名称中的“汇编”方面所暗示的那样，Wasm 是更低级别的，因为它采用二进制编码，不包括垃圾回收，并支持接近本机的性能。Wasm 提供了三个优势，使其特别适合我们通过 FastEdge 提供安全且高性能边缘计算的目标：固有隔离模块、快速模块启动以及易于分发和部署。

### 固有隔离模块

Wasm 使浏览器能够运行对性能要求很高的应用程序，如 3D 游戏。然而，在网络上的每部智能手机和 PC 上运行使用低级编程语言（如 [Rust](https://roadmap.sh/rust) 或 [C/C++](https://roadmap.sh/cpp)）编写的软件具有严重的安全性影响，因为这些语言通常具有对系统资源的直接访问权限。

这就是 Wasm 具有沙盒模块的原因，这些模块必须在加载时定义其函数调用，以便无法动态注入新调用。此外，每个模块都有自己的堆内存，并带有缓冲区溢出保护。

事实证明，隔离模块不仅适用于客户端软件。云提供商经常在其基础设施上运行第三方应用程序，因此提供商还可以受益于隔离，以保护其系统免受恶意代码的侵害。其他直接基于 [JavaScript](https://thenewstack.io/top-5-underutilized-javascript-features/) 运行时（如 [V8](https://thenewstack.io/node-js-22-release-improves-developer-experience/)）的解决方案需要进行定制才能实现此隔离级别。

### 快速模块启动

Wasm 模块可以在一毫秒内启动，这使得 Wasm 成为将现代无服务器计算方法应用于边缘的理想候选者。同样，在浏览器中执行要求苛刻的应用程序与在云环境中运行它们具有类似的要求。用户不想等待几秒钟才能渲染网站，而无服务器应用程序也会遭受长时间的 [冷启动](https://thenewstack.io/how-to-conquer-cold-starts-for-better-performance/) 时间。与基于容器或 VM 的解决方案相比，Wasm 模块的冷启动时间要短得多。

### 易于分发和部署

Wasm 由浏览器加载和执行，而无需重新启动客户端或整个机器。应用程序创建者可以在 Web 服务器上托管 Wasm 文件，而浏览器会处理其余部分。

由于 Wasm 已经允许通过 HTTP 从远程服务器加载模块，我们只需为 FastEdge 重用此部署模型，即可简化模块分发并减轻边缘系统管理员的负担。

## 开放标准，开放运行时
### 与 JVM 和 .NET 等其他运行时标准不同，Wasm 自诞生以来一直是多个组织创建和维护的开放标准。

这种本质上开放的方法允许任何个人或组织为项目贡献功能和错误修复，从而提高项目的整体质量，使 Wasm 成为云应用程序的理想选择。

### 由于 Wasm 是一个开放标准，因此多个组织已经为其实现了运行时。对于 FastEdge，我们选择了 [Wasmtime](https://wasmtime.dev/) 作为我们的运行时；它的创建者 Bytecode Alliance 是多个组织共同努力的结果。为平台选择运行时是一项重大的长期业务投资，我们期望 Wasmtime 的协作方法能够产生高质量的软件。多个组织共同维护该项目并保持高标准——即使单个贡献者或贡献组织离开，也能得到保护，这使得 Wasmtime 成为一个可靠的长期解决方案。

### 最后，[开源方法](https://thenewstack.io/open-source/) 还为浏览器和边缘带来了多种编程语言的优势。可以将 Rust、C/C++、Go、Zig 和其他语言编译为 Wasm，因此从长远来看，FastEdge 有可能支持多种语言。我们目前提供一个 [Rust SDK](https://github.com/G-Core/FastEdge-sdk-rust/)，并计划很快发布一个 JavaScript/TypeScript SDK。

## 将 Wasm 集成到我们现有的边缘网络中

### 选择 Wasmtime 作为我们的 Wasm 运行时使我们能够在短短三个月内为 FastEdge 提供概念验证，因为 Wasmtime 已经提供了隔离和主机通信等功能。不过，Wasmtime 只是一个运行时，因此我们需要进行一些添加才能使其与我们现有的 CDN 节点配合使用。

### 我们为请求数据（如标头和正文）实现了主机函数，以允许 FastEdge 应用程序访问运行时外部的数据。我们计划为 SQL 和 NoSQL 数据库、Redis 等键值存储、队列和流服务添加更多主机函数。

### 选择开源软件加速了我们可观察性堆栈的创建。Prometheus、Grafana 和 OpenSearch 等项目为我们提供的监控系统提供支持，以便开发人员可以检查边缘的日志。此外，我们正在创建一个工具来支持在本地测试边缘应用程序。

### 最后，我们确保 FastEdge 与我们的 CDN 紧密集成，以便边缘应用程序连接到 CDN 生命周期中的每一步。通过这种方式，您可以检查下载授权、提供上传身份验证，或根据图像大小或地理位置等属性修改正文和标头。

## FastEdge 的实际应用

### 我们提供两种方法来构建和部署 FastEdge 应用程序：

- 一种使用 SDK 和工具的传统方法，允许开发人员构建应用程序。
- 一种模板方法，允许非技术人员从模板部署常见应用程序。

### 对于模板方法，我们创建了解决常见网站任务的应用程序，例如 Markdown 到 HTML 转换器和 S3 上传器。

### 我们还在边缘尝试了 AI，并 [构建了一个网站](https://fast-edge-demo.fastedge.gcore.dev/)，使用图像分类作为用例来演示 FastEdge 的功能。下图显示了在 FastEdge 上运行的图像分类器。我们的白皮书详细解释了 [我们在边缘的 AI 愿景](https://gcore.com/library/wp-web-assembly-for-ai-inference)。

![边缘图像分类](https://cdn.thenewstack.io/media/2024/05/6533790f-webassembly-at-the-edge-1-1024x399.png)

### 边缘图像分类。

### 我们还在 FastEdge 上部署了一个低延迟单词预测引擎。

![边缘单词预测](https://cdn.thenewstack.io/media/2024/05/f1bcef20-webassembly-at-the-edge-2-1024x391.png)

### 边缘单词预测。

### 转向传统方法，我们鼓励开发人员使用 [我们的 Rust SDK](https://github.com/G-Core/FastEdge-sdk-rust/) 在 FastEdge 上构建自己的应用程序。以下代码定义了一个简单的匿名代理，它在边缘提取一个 URL 参数并获取一个网站。

```
use fastedge_sdk::http::{Request, Response};
use fastedge_sdk::runtime::{HostFunction, HostFunctionContext};

#[fastedge_sdk::host_function]
fn anonymous_proxy(ctx: &HostFunctionContext, req: &mut Request) -> Result<Response, String> {
    let url = req.query_params().get("url").ok_or("Missing 'url' query parameter")?;

    let mut new_req = Request::get(url);
    new_req.headers_mut().remove("host");
    new_req.headers_mut().remove("referer");

    let resp = ctx.fetch(new_req)?;

    Ok(resp)
}
```

### 此示例说明了如何使用我们的自定义主机函数从客户端访问请求数据，并将您自己的请求发送到 Web 上的任何 API，而无需向该 API 透露客户端信息。在 [GitHub 上找到完整示例](https://github.com/G-Core/FastEdge-sdk-rust/tree/main/examples/backend)。

## 总结

### 虽然最初并非为后端应用程序创建，但许多 Wasm 功能非常适合在边缘使用。与基于容器的解决方案相比，它们可以提供更小、更快的应用程序，并且不受一种编程语言的约束。将 Wasm 用作我们边缘计算平台的核心技术，使我们能够在小团队的情况下快速交付 FastEdge，同时让我们在 FastEdge 的未来方面保持灵活性和适应性。
### Corrected Markdown Text

借助紧密的 CDN 集成和应用程序模板，FastEdge 与其他边缘计算解决方案截然不同。如果您想为全球分布的客户群个性化您的内容或增强您的非技术团队，不妨试一试 FastEdge（https://gcore.com/fastedge）。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。