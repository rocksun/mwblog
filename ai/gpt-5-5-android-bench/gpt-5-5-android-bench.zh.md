**谷歌希望软件开发者在构建 Android 应用程序时使用最优秀的 AI 模型；** 因此，该公司于 3 月推出了其 [Android Bench](https://developer.android.com/bench) 基准测试门户网站。该服务旨在提供一个持续更新的排行榜，为开发者和模型创建者提供参考。

排行榜上周进行了更新，纳入了[开放权重模型](https://thenewstack.io/ai-hardware-and-open-models-headed-in-the-linux-direction/)，并增加了延迟、[Token](https://thenewstack.io/the-different-token-types-and-formats-explained/)和成本的新数据列。

> “通过为高质量的 Android 开发确立一个清晰、可靠的基准，我们正在帮助模型创建者找出差距并加速改进——这使开发者能够更高效地工作。”   
> —Matthew McCullough，谷歌。

## 模范生

谷歌 Android 开发者部门产品副总裁 [Matthew McCullough](https://www.linkedin.com/in/matthewjmmccullough/) 在 [3 月份的一篇博客文章中写道](https://android-developers.googleblog.com/2026/03/elevating-ai-assisted-androi.html#:~:text=We%20know%20you%20want%20AI,of%20LLMs%20for%20Android%20development.)，谷歌正在积极针对旨在评估这些工具如何构建 Android 应用的测试，对顶尖的 AI 大语言模型（LLM）进行基准测试。

“我们的目标是为模型创建者提供一个基准，以评估用于 Android 开发的大语言模型能力，”McCullough 解释道。“通过为高质量的 Android 开发确立一个清晰、可靠的基准，我们正在帮助模型创建者找出差距并加速改进——这使开发者能够利用更广泛的、有用的 AI 辅助模型更高效地工作，从而最终提高整个 Android 生态系统中的应用质量。”

## GPT 5.5 是目前用于 Android 的最佳 AI 模型

这项新服务似乎没有提供模型随着时间推移而上升或下降的历史记录，但据 [*9to5Google*](https://9to5google.com/2026/05/21/best-ai-android-app-coding-development-google-list/) 报道，上一次的 Android Bench 将 Gemini 3.1 Pro 与 OpenAI 的 GPT 5.4 并列为联合领头羊。

截至 5 月 18 日的更新，GPT 5.5 是目前用于 Android 应用开发最佳的 AI 模型。

谷歌为 Android Bench 提供了[公开可查的操作方法说明](https://developer.android.com/bench/methodology)，解释道：“该服务通过向大语言模型展示来自开源软件项目的真实问题和拉取请求，来评估其生成解决问题代码的能力。这种方法旨在确保这些任务能够代表开发者每天面临的挑战。”

## 为什么谷歌要构建 Android Bench？

谷歌表示，之所以构建 Android Bench，是因为 AI 辅助软件工程领域“已经出现了几种用于衡量大语言模型能力的基准”。该公司进一步指出，Android 开发者“面临着现有基准无法涵盖的特定挑战”，因此它创建了一项排名服务，旨在专注于对高质量 Android 开发进行全面的综合评估。

“[谷歌表示](https://developer.android.com/bench/methodology)：“我们创建了一个与模型无关的基准，以准确评估大语言模型在各种 Android 开发任务上的表现。”该公司进一步将 Android Bench 的目标定义为：鼓励针对 Android 开发的大语言模型改进；使 Android 开发者能够利用一系列用于 AI 辅助的“有用的模型”来提高生产力；并在整个 Android 生态系统中带来更高质量的应用。

## 软件开发基准测试有用吗？

开发者和模型创建者自然会质疑谷歌设立这一基准的做法是否有用。反对者可能会指出[古德哈特定律（Goodhart's Law）](https://en.wikipedia.org/wiki/Goodhart%27s_law#cite_note-Strathern1997-1)，该定律指出：“当一项指标变成目标时，它就不再是一个好指标。”当然，任何奖励系统都会吸引那些为了达到标准化目标而优化其行为的参与者。

谷歌可能已经预料到了这一陷阱，因此基于现实世界中的公共代码仓库建立了 Android Bench。

“我们通过针对一系列常见的 Android 开发领域策划任务集来创建该基准。它由来自公共 GitHub Android 仓库、难度各异的真实挑战组成，”谷歌的 McCullough 写道。

这意味着测试的情景包括解决跨 Android 版本的“破坏性变更”（即由于谷歌将 Android 更新到新版本，导致以前运行良好的代码损坏）、特定领域的任务，例如可穿戴设备的网络连接（在这里，高延迟和频繁断连的阴影始终是个威胁），以及迁移到最新版本的 Jetpack Compose（Android 自己的、使用 Kotlin 语言功能的声明式 UI 工具包）等等。

## 还存在哪些其他 Android 基准测试？

其他 Android 基准测试包括 [Jetpack Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview)，这是一个允许开发者在 Android Studio 内部对他们的 Android 原生代码（无论是用 Kotlin 还是 Java 编写）进行基准测试的库。其姐妹版 Jetpack Macrobenchmark 则用于测试大规模的用户交互，例如应用程序的冷启动时间或用户界面动画的流畅度。

Android 基准测试领域中可用的还有 [Firebase Performance Monitoring](https://firebase.google.com/products/performance)，这是一个生产级别的实地基准，用于监控应用的网络请求和屏幕渲染时间；这更像是一个应用性能监控工具。

在 Android 开发者社区中，[Android Vitals 已经](https://developer.android.com/topic/performance/vitals)提供了一个仪表板，用于跟踪应用质量指标，例如稳定性、性能、电池消耗和权限问题。Apptim 是一款生成式 AI 移动应用分析和测试工具，所以它也是性能基准测试，但与 Android Bench 不太一样。我们还可以提到谷歌自家的 Android Performance Analyzer (APA)，它于今年 5 月 19 日刚刚推出，是一款提供工作流程简化支持的分析和性能分析工具。

> “像 Android Bench 这样的开放式基准非常好，我们希望有更多这样的基准。但需要注意的是数据污染。公共仓库会泄露到训练数据中，我们已经看到，在公开评估中得分相差仅几分的模型，在旨在模仿相同工作负载的私有基准测试中，差距会急剧扩大。”—— Andrew Filev，Zencoder 首席执行官。

代码编排公司 [Zencoder](https://zencoder.ai/) 的创始人兼首席执行官 [Andrew Filev](https://www.linkedin.com/in/filev/) 告诉 *The New Stack*，他是这些系统的粉丝，但持保留意见。

“像 Android Bench 这样的开放式基准非常好，我们希望有更多这样的基准，”Filev 热切地说道。“总的来说，软件开发过于多样化，单一的总体得分无法在所有领域都具有普遍意义——Python 基准测试无法告诉你模型如何处理 Rust、嵌入式系统或移动应用。此外，构建一个开放的 Web 应用、一个仅有几百人使用的内部工具，与一个全球规模的多租户产品之间存在真正的差距，模型在这些领域的表现并不相同。”

因此，他表示，特定领域的基准测试推动了模型开发者去关注其用户实际工作的环境，因此他认为“谷歌在这方面值得表扬”，并希望其他平台也能跟进。

“但需要注意的是数据污染。公共仓库会泄露到训练数据中，我们已经看到，在公开评估中得分相差仅几分的模型，在旨在模仿相同工作负载的私有基准测试中，差距会急剧扩大，”Filev 说道。“在我们自己的研究中，测试用例构建方式的微小改变，将模型的差距从 6 个百分点拉大到了 26 个百分点，并彻底重新打乱了排名。因此，公共基准测试有助于提高大语言模型在跨领域中的表现，而私有评估则有助于评估在你的工作负载上的实际表现。”

## Android Bench 的分数是如何构成的

每个 Android Bench 模型的整体基准得分都是基于谷歌开发的一种包含四个核心指标的计算方法。

置信区间（CI）范围（%）是衡量预期性能范围的指标，反映了结果的统计可靠性（p值，0.05）；平均延迟分数是跨 10 次运行解决 100 个任务所花费的时间；平均总 Token 分数是跨 10 次运行的完整基准测试中 Token 消耗的衡量标准；平均成本是测试时每次基准测试运行的成本，以美元计算。

Android Bench 的测试套件已[在 GitHub 上公开提供](https://github.com/android-bench/android-bench)。