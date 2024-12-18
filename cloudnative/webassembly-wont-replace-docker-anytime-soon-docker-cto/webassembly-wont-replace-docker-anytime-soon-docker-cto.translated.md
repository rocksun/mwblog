# WebAssembly 不会很快取代 Docker：Docker 首席技术官

![WebAssembly 不会很快取代 Docker：Docker 首席技术官的专题图片](https://cdn.thenewstack.io/media/2024/11/57d6f08e-justin_cormack-1024x768.jpg)

Docker 是否将 [WebAssembly](https://thenewstack.io/webassembly-and-kubernetes-go-better-together-matt-butcher/) 视为威胁？

[WebAssembly](https://www.thenewstack.io/WebAssembly) 具有潜在价值，尽管它可能不会取代 Docker 环境本身，[Docker](https://www.docker.com/?utm_content=inline+mention) 首席技术官 [Justin Cormack](https://github.com/justincormack)（也是 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 技术监督委员会成员）在上周于盐湖城举行的 [KubeCon + CloudNativeCon](https://thenewstack.io/cncf-sics-developers-on-kubernetes-patent-trolls/) 上抽出时间与 The New Stack 交流时评论道。

它们的用例略有不同，并且每个用例都很有价值。

他评论说，WebAssembly 的很多价值在于代码隔离和代码组件化。Docker 也是如此，尽管粒度级别不同。

WebAssembly 和 WebAssembly 系统接口 (WASI) 承诺提供一个安全的沙箱，可以在其中安全地执行代码，而程序可以使用组件模型 [使用多种语言构建](https://thenewstack.io/why-wasi-preview-2-makes-webassembly-production-ready/)。

当然，Docker 也是如此，它允许开发人员打包他们的应用程序，这样他们就不依赖于主机操作系统。

Cormack 说，使用 WASM，您可以共享“非常小的东西”。这些是“远低于应用程序级别”的库。

这种粒度级别有其自身的价值。

开发人员喜欢使用库，但他们总是知道库中有什么吗？他们可能会下载一个用于计算的 JavaScript 库，却发现它带有一些用于上传用户密码的秘密代码。

WebAssembly 可以通过提供“微隔离”来限制库的操作范围，使其仅限于开发人员指定的那些操作，从而解决这个问题。因此，该库可用于计算，但被阻止访问任何网络。

Cormack 指出，使用组件构建的应用程序可能会使用数千个库。

Cormack 承认，为每个库提供自己的容器并不是隔离所有这些库的最佳方法。

## WebAssembly 与 Docker 的简短历史

WebAssembly 与 Docker 的话题现在每隔几年就会出现一次。但 WebAssembly 仍处于起步阶段，有人说它缺乏 [明确的用例](https://thenewstack.io/true-portability-is-the-killer-use-case-for-webassembly/)，而 Docker 和容器生态系统则是蓬勃发展的生态系统。整个构建过程都以容器为基础。有状态应用程序，例如涉及数据库的应用程序，已经在容器中找到了舒适的家。

2019 年，Solomon Hykes 在 Twitter 上争辩说，如果在他构思 Docker 的时候 WebAssembly 就存在，那么就不需要容器技术了。

> 如果 WASM+WASI 在 2008 年就存在，我们就不需要创建 Docker。它就是这么重要。服务器上的 WebAssembly 是计算的未来。标准化的系统接口是缺失的一环。希望 WASI 能够胜任这项任务！
>
> [https://t.co/wnXQg4kwa4](https://t.co/wnXQg4kwa4) — Solomon Hykes (@solomonstre) [2019 年 3 月 27 日]


这条评论 [引起了轰动](https://news.ycombinator.com/item?id=28109699)，Hykes 后来稍微收回了他的说法，[向 InfoWorld 解释](https://www.infoworld.com/article/3600287/can-wasm-replace-containers.html) 说：

> *我的那条推文被广泛误解了。它被解释为 WebAssembly 将取代 Docker 容器。我当时不认为这会发生，你看，它并没有发生，而且在我看来，永远不会发生。现在 Docker 已经存在并且是一个标准，WebAssembly 和 WASI 虽然很酷，但它们非常不同。它根本不是替代品。它的形状非常不同。*

到目前为止，WebAssembly 已经找到了 [自己的利基市场](https://webassembly.org/docs/use-cases/)，尤其是在 [前端开发](https://thenewstack.io/whos-leading-webassembly-adoption-so-far-vendors/) 方面，以及 [NIST 建议的](https://csrc.nist.gov/news/2024/nist-has-published-nist-ir-8505) 云原生计算环境中的数据保护方面。

## Docker AI 目录

Cormack 还在 KubeCon 上抽出时间讨论了 Docker 的最新举措，[Docker AI 目录](https://hub.docker.com/catalogs/gen-ai?_gl=1*6snjn6*_gcl_au*MTkzNjIzNjg0NS4xNzMxNTIyNDgx*_ga*NTg2NzQ3NjU1LjE3MzE1MjI0ODE.*_ga_XJWPQMJYHQ*MTczMTUyMjQ4MS4xLjEuMTczMTUyMjUyMi4xOS4wLjA.)。
> “我们看到越来越多的人正在从 Docker 使用 AI 工具，因为那是他们获取 AI 资源的地方，”他说道。“很多开发者正在探索 AI，我们一直在研究如何帮助他们，因为这对他们来说是一个全新的领域。”

> Docker AI 目录 [旨在](https://www.docker.com/blog/accelerating-ai-development-with-the-docker-ai-catalog/) 简化将 AI 工具、模型和库集成到应用程序中的过程。每个工件都包含文档和配置指南。[对于发布者](https://www.docker.com/partners/programs/), Docker 提供了一组使用指标，允许他们根据客户需求进一步完善其工具。

> [Tech moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)