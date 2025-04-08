# Toast 通过 Gradle DPE 加速构建，解决构建缓慢问题

![Toast 通过 Gradle DPE 加速构建，解决构建缓慢问题 的特色图片](https://cdn.thenewstack.io/media/2025/04/79ded7e8-masha-rayt-uwjtxqprswm-unsplash-1024x575.jpg)

当开发者 Aida Issayeva 于 2023 年 3 月加入 Toast 时，该公司在为其流行的餐厅管理和食品订购应用程序的[发布周期](https://thenewstack.io/3-steps-for-automating-software-release-management/)过长问题上遇到了严重的麻烦。由于发布周期过长，Toast 很难快速将新功能添加到应用程序版本中并立即发布给客户。延迟也导致了 Toast 的挫败感和开发积压。

“我们发现了一个问题，对我们来说最大的问题是交付价值的提前期，” Issayeva 告诉 The New Stack，她是 [Toast 销售点生产力团队](https://central.toasttab.com/s/article/Get-Started-with-the-Toast-Now-App)的软件工程师和技术主管。“我们开始研究为什么我们的发布周期更长。我们越是左移，就越发现开发人员花费更多时间构建功能，因为[持续集成](https://thenewstack.io/ci-cd/) (CI) 上的构建时间很慢。”

她说，仔细观察后发现，修复问题需要更多时间，因为 Toast 没有获得高质量的数据来验证构建时间和测试的实际情况。

Toast 已经拥有一个自研的[平台工程平台](https://thenewstack.io/3-key-benefits-of-platform-engineering/)，但漫长的发布周期问题超出了该系统的范围。

## 选择策略来寻找构建时间补救措施

在 Toast 工作了一段时间后，Issayeva 最终发现他们遇到的漫长发布周期与漫长的构建时间相关，这阻碍了开发团队。

考虑到所有这些，Issayeva 开始思考她和她的团队如何通过引入[开发者生产力工程 (DPE)](https://thenewstack.io/metrics-driven-developer-productivity-engineering-at-spotify/) 工具来解决 Toast 的漫长发布周期挑战。她曾在 Twitter 和 DoorDash 的先前工作中与一种这样的工具 [Gradle](https://thenewstack.io/ai-improves-developer-workflow-says-gradle-dev-evangelist/) Enterprise 合作过，因此她开始再次评估它。现在称为 [Gradle Develocity](https://gradle.com/develocity/)，该构建工具致力于加速构建，并在本地和 CI 系统上提供测试，以便开发团队可以了解其代码中发生的情况。她说，使用 Develocity，开发人员可以在构建过程中修复 [Android 应用程序](https://thenewstack.io/dev-news-android-apps-on-rust-astro-db-and-storybook-8/)中出现的问题和瓶颈。

她说：“开发人员会说他们认为事情正在发生，但无法确定”，因为他们在有问题的构建中挣扎。“这是工具和流程的结合。对我们来说，第一步是确定我们缺少的工具。我们都有预感，并且我们知道感觉像是‘这部分错了吗，还是那部分错了吗’，但我们无法量化这种感觉。因此，没有[关于问题的]回溯数据，这就是促使我们进入 DPE 和 Gradle Develocity 的原因。”

Issayeva 说，借助 Develocity，Toast 可以量化有关其构建发生情况的数据，并了解任务花费的时间，同时还可以识别成功和失败的测试。

她说：“如果我们知道 50,000 或 100,000 个测试中的一个测试不稳定，这意味着我们的构建系统 Gradle 需要多次执行该测试。” “多次执行该测试会带来资源成本，并会减慢速度。它会消耗能量，并且不允许您运行需要运行的其他内容。想象一下，如果我们不仅仅有一个测试，而是 80% 的测试都在占用资源，那将是一个主要问题。”

Develocity 通过清楚地向开发团队和领导者展示事情的执行情况以及不稳定测试导致构建的百分比来提供帮助。通过识别罪魁祸首，Issayeva 和她的团队可以进行干预并采取行动来解决问题，她说。“此外，因为我们现在有了历史数据，所以我们可以知道它何时开始出现故障，例如在新代码添加到它之前或之后。我们更容易识别它。”

## 观察构建时间的下降

在引入 Gradle Develocity 之前，Toast 的构建时间增加了多少？

Issayeva 说，在 2022 年，在她到来之前，每次构建时间约为 55 分钟。当她在 2023 年 3 月加入公司时，平均构建时间已增加到 78 分钟。但三个季度后，使用 Develocity，构建时间降至 27 分钟，她说。
Issayeva说：“它为我们提供了关于每个任务的数据。能够在Develocity中看到每个任务、它花费的时间以及它所依赖的内容。这就是为什么我们可以深入到细粒度级别，并实时找出导致我们出现问题的原因。”

Issayeva和她的团队对所有数据进行最终分析，他们负责读取和解读来自Gradle的数据，但她表示，这些分析之所以成为可能，是因为这些工具提供了过去无法访问的详细信息。

她说：“每次构建发生时，无论是本地构建还是远程构建，Gradle都会发布该构建扫描的快照。我们将其加载到我们的数据库中，这是一个包含所有构建扫描的特殊数据库。然后基于这些信息，我们从Gradle Develocity中获得趋势和模式，从而确定我们可以看到的关于构建时间的趋势。我们不是每次都这样做。我们每两周进行一次指标审查，那时我们会查看这些数据。”

对于Issayeva来说，找到并解决像这样的破坏性瓶颈是她在Toast公司担任的重要职责。

她说：“通常，我的工作是找到问题并说，‘嘿，这就是现在的问题，并且在两到三个月内会变得糟糕两到三倍。’然后我将其提交给领导层，以便他们可以看到。当我[确定为什么]我们的构建时间变慢时，那是一个有趣的时刻。”

## 平台工程和开发者生产力工程之间有什么关系？

Gradle的开发者倡导者兼资深[Java](https://thenewstack.io/introduction-to-java-programming-language/)开发者[Brian Demers](https://www.linkedin.com/in/bdemers/)告诉The New Stack，平台工程和DPE是“公司和开发者团队可以用来提高开发者生产力的互补方法”，每种方法都侧重于改进开发者生产力的不同方面。

Demers说：“[平台工程](https://thenewstack.io/platform-engineering/)从组织的角度看待开发者生产力，并侧重于构建和维护[内部开发者平台（IDP）](https://thenewstack.io/internal-developer-platforms-the-heart-of-platform-engineering/)，这些平台为开发者提供自助服务能力。DPE更进一步，侧重于优化构建、测试和故障排除流程——这些事情会影响到每位工程师，无论他们的开发环境如何。”

他说，DPE可以特别帮助那些可能正在与缓慢的构建和测试周期作斗争的公司，以优化和加速他们的构建和测试性能。与此同时，平台工程提供了一个精简高效的环境，开发者可以在其中使用精选的工具构建他们的应用程序。

Demers说：“一个成熟而有效的策略最终将涉及DPE和平台工程。例如，平台工程提供了一个具有自助服务功能的统一环境，而DPE则确保这些工具和流程尽可能高效地运行。”

[YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)