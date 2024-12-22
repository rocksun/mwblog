# 2024年顶级开发者工具和Web开发者趋势

![2024年顶级开发者工具和Web开发者趋势特色图片](https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1-1024x576.png)

有时，一项技术会吸引人们的注意，同时也为其他事物在蓬勃发展中创造了空间和资源。涌入大型语言模型 (LLM) 领域的额外资金，间接地为其他稍微普通一些，但却必要的软件项目提供了更多喘息空间。虽然没有直接受到冲击，但其他软件项目也受益于这种颠覆。

这篇文章回顾了我2024年报道的一些开发者工具的亮点。虽然我从LLM开始，但我还在人工智能领域之外看到了许多其他有趣的进展。

## 开发者的AI工具

我认为今年LLM的开发变得更加注重局部。多模态AI——能够处理或响应图像、声音和视频的能力——是今年最突出的实际成就。模型扩展了自身的能力，与之前的版本竞争。大型厂商为我们提供了更大（[和更小](https://thenewstack.io/the-rise-of-small-language-models/)）的模型。但还有一些不那么明显的指数级跃升，影响范围更广。Humane AI Pin的发布提醒我们，LLM及其支持者并不完全掌握AI对大多数人意味着什么。自动驾驶汽车项目的预期悄然降低，这正说明了这一点。就在上个月，我指出LLM还没有在[标准组件开发中](https://thenewstack.io/why-llms-within-software-development-may-be-a-dead-end/)找到位置——无论是在代码中，还是在可测试的服务中。

然而，直接为用户托管LLM行为的工具今年表现良好。我们看到[Cursor AI](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)和[Zed AI](https://thenewstack.io/an-introduction-to-zed-ai-and-how-it-compares-to-cursor-ai/)都为用户提供了内联和聊天访问LLM的方式，以改进某些编码方面。[JetBrains AI](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/)也提升了其广受好评的Rider产品。然而，将LLM作为附加组件始终存在风险，即在依赖它们进行改进时，实际上会将您的业务路线图直接交给LLM提供商——在一个案例中，Zoom的首席执行官兼创始人Eric Yuan承认，数字克隆的未来只能通过外部创新[“下层堆栈”](https://www.theverge.com/2024/7/30/24209552/down-the-stack-baby)来实现。

添加AI的IDE制造商最初可能希望更紧密地集成产品，但这些决策存在权衡。Cursor AI选择分叉VS Code以改进其产品的UI，而不是仅仅编写一个插件。但这意味着他们无法直接运行.NET代码，因为Microsoft拒绝了非Microsoft程序集。顺便说一句，今年我转用了VS Code，因为[Visual Studio for Mac已停止维护](https://learn.microsoft.com/en-us/visualstudio/releases/2022/what-happened-to-vs-for-mac)。到目前为止，一切顺利。

有关开发人员AI的更多信息，请查看我们今年对[AI工程趋势的总结](https://thenewstack.io/top-5-ai-engineering-trends-of-2024/)。

## 2024年编程趋势

与此同时，在LLM之外的开发者工具领域也发生了很多事情。

我之前提到了Zed——它[今年在Linux上发布](https://thenewstack.io/zed-ported-its-text-editor-to-linux-and-its-pretty-special/)并受到了好评（但Zed没有进一步迹象表明它会推出Windows版本）。同样在Rust领域，Warp即将登陆Windows。Linux用户[今年也获得了Warp](https://thenewstack.io/warp-is-a-power-users-dream-terminal-for-linux/)，但对于这些用户来说，一个部分闭源、由风投支持、以MacOS为首要平台、并将AI作为核心功能的产品有点令人却步——他们对[Kitty](https://sw.kovidgoyal.net/kitty/)非常满意，谢谢。

今年我们看到许多新语言的发布或重大更新。[Virgil](https://thenewstack.io/introduction-to-virgil-a-new-language-by-wasms-co-creator/)和[Zig](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/)都是具有内置交叉编译器的轻量级高性能系统。[Gleam](https://thenewstack.io/introduction-to-gleam-a-new-functional-programming-language/)是一种新的类型安全函数式语言，而[MoonBit](https://thenewstack.io/moonbit-wasm-optimized-language-creates-less-code-than-rust/)针对WebAssembly (Wasm)进行了优化。事实上，Wasm为网站中的复杂行为提供了另一种选择——我认为今年对于理解Wasm可以提供什么是一个好年头。
对新语言的兴趣，源于现代开发者持续存在的多种语言使用习惯，也源于即使是一人项目，对入门体验理解的巨大提升。如今几乎所有项目都拥有清晰的入门路径，并认识到[playground](https://thenewstack.io/playgrounds-for-developers-uses-and-design-patterns/)的价值。

## 框架和部署工具
去年，我们见证了[云计算反弹](https://techcrunch.com/2023/03/20/the-cloud-backlash-has-begun-why-big-data-is-pulling-compute-back-on-premises/)的开始。今年二月，[David Heinemeier Hansson](https://www.linkedin.com/in/david-heinemeier-hansson-374b18221/)的软件公司发布了本地部署系统[Kamal](https://thenewstack.io/how-to-exit-the-complexity-of-kubernetes-with-kamal/)——或者说是“[容器版的Capistrano](https://thenewstack.io/why-capistrano-got-usurped-by-docker-and-then-kubernetes/)”。

说到DHH，我还研究了[Omakub](https://thenewstack.io/introduction-to-omakub-a-curated-ubuntu-environment-by-dhh/)，这是一个经过精心设计的开发者Ubuntu环境。这通常带有个人偏好，但对于过去几年没有磨练Linux构建技能的Unix开发者来说，这是一个不错的起点。像我一样，你可以在虚拟机上检查它。

看看应用程序框架，无头CMS[Payload](https://thenewstack.io/introduction-to-payload-a-headless-cms-and-app-framework/)今年升级到了3.0版本。我还通过[几篇文章](https://thenewstack.io/getting-up-to-speed-with-eleventy-config-and-collections/)研究了静态网站生成器[Eleventy](https://thenewstack.io/introduction-to-eleventy-a-modern-static-website-generator/)。我最近检查的一个新的静态网站生成器是[Nue](https://thenewstack.io/nue-a-new-static-site-generator-taking-on-next-js/)，它显然借鉴了Vue，并与Next.js竞争。如果术语[Jamstack](https://thenewstack.io/is-jamstack-toast-some-developers-say-yes-netlify-says-no/)的使用正在减少，那只是因为部署到CDN现在已经成为默认设置了。

[Deno](https://thenewstack.io/how-oop-developers-can-get-to-know-typescript-through-deno/)是一个将TypeScript作为一等公民的JavaScript运行时。虽然我研究了TypeScript如何帮助弥合JavaScript和C#或Java等语言之间的编码差距，但Deno也提供了一个类似Heroku的部署方案，看起来不错。

有一些项目不适合任何可识别的细分市场。虽然[Glamorous Toolkit和可塑性开发](https://thenewstack.io/a-developer-guide-to-using-glamorous-toolkit-on-at-protocol/)仍然局限于Smalltalk，但它们提供了一种强大的替代方案来查看和思考代码库，并且正在慢慢地使其更容易访问。在这篇文章中，我研究了使用该工具包检查Bluesky的AT协议（这是在Bluesky作为平台快速发展之前）。

[System Initiative](https://thenewstack.io/how-system-initiative-treats-aws-components-as-digital-twins/)今年上线，它采用数字孪生方法进行基础设施部署。它现在拥有可靠的SaaS产品和本地构建选项。它目前仅适用于AWS，我希望他们能够与其他云提供商集成。这样一来，亚马逊可能会考虑收购System Initiative，以帮助自己提升价值链地位。

[Markwhen](https://thenewstack.io/introduction-to-markwhen-a-markdown-timeline-tool-for-devs/)在年末适时出现，关注时间以及如何在类似Markdown的语言中表示时间。该编辑器可用于显示类似GANT图的项目图表，但时间会证明它是否会被其他项目采用。

## 2024年简述
我认为今年对于开发工具的发布来说是相当活跃的一年，有些工具使用了LLM辅助——但也许多没有。

在编程方面，Wasm的使用有所扩展，人们正在衡量其价值。

今年纯粹的开源项目似乎减少了，这导致团队需要沟通信任——因此出现了更多博客、视频和社交媒体帖子。

我很高兴报道大型项目的持续增长，以及更具创新性的一人项目。期待2025年。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)