# 7 个原则和 10 种策略让你成为 10 倍开发者

在 Shift 会议上，Flightcontrol 的 Brandon Bayer 提出，你可以通过让另外 10 个人提升 10% 的生产力，来成为一个 10 倍开发者。

翻译自 [7 Principles and 10 Tactics to Make You a 10x Developer](https://thenewstack.io/7-principles-and-10-tactics-to-make-you-a-10x-developer/) 。

![](https://cdn.thenewstack.io/media/2023/07/f2da0f7c-shutterstock_1-1024x684.jpg)
*图片来自 Shutterstock*

我们都听说过 10 倍工程师。不管是真是假， 10 倍工程师被认为比普通同行生产力高 10 倍。互联网上充满了如何成为 10 倍工程师的建议，其中大多数包括如何提高你的专业知识或心态的提示。

Flightcontrol 的 Brandon Bayer 在迈阿密 [Shift 会议](https://shift.infobip.com/us/#hero)上发表了“ 10 种改进你交付软件的方式”的演讲，提供了一个有点不同的视角。他的论点是，你可以通过让其他 10 个人的生产力提高 10% 来成为一个 10 倍开发者。

Bayer 分享了 7 个总体原则和 10 种策略来实现这一目标。

这7个原则是：

## 原则 1 ：速度

开发者都痴迷于速度。如果他们找到一个比原来快 10 毫秒的工具，他们都会想重写整个应用来使用它。但是当涉及到部署代码的频率时，他们往往会更加谨慎。他们总是更愿意明天或者下周再部署，这样今天就不用加班去修复可能出现的问题了。  

对于部署来说，速度就是安全，小步快跑就是速度。   

交付速度有巨大的复利效应。如果你的部署花几个小时，你就会非常确保没有 bug ，因为如果你在部署上线后马上发现严重 bug ，然后你又需要等几个小时你的修复才能上线。

软件生命周期的每个部分都要追求速度：

- 快速反馈循环
- 快速构建
- 快速测试
- 快速部署
- 快速修复
- 快速回滚

## 原则 2 ：可靠性

你的系统必须可依赖。不稳定的 CI/CD 问题是这个宇宙中最可怕的事情之一。不惜一切代价避免不稳定性。

## 原则 3 ：可重现性 

为了构建和维护复杂的系统，我们需要知道如果我们做 X ，每次都得到 Y 。如果一次你做 X 得到 Y ，而另一次却得到 Z ，你就会对系统失去全部信心。

使用脚本和代码来控制你所做的一切，而不是手动点击、手动命令等。

## 原则 4 ：平静的轮岗

平静的轮岗很重要，因为人们通常可以在工作日承受压力，但是如果这种压力侵入到他们生活的其他方面，那就是他们开始更新简历的时候了。

## 原则 5 ：易于调试

每个人都会引起 bug 。即使是高级工程师，即使测试覆盖率 100% 。你会把 bug 部署到生产环境，所以你必须准备好修复生产环境的 bug 。如果调试很困难、部署修复很慢，那会拖慢你，因为你会增加冗长的 QA 流程，等你意识到的时候，你的部署频率可能只有每几周一次。

但是即使有大量的 QA ，你仍然会有生产环境的 bug 。生产环境是找到所有 bug 的唯一可靠的方式。所以我们的系统必须易于调试。

## 原则 6 ：自助基础设施和部署

做基础设施和代码部署的传统方式是，你有两个独立的团队，开发和运维。如果开发需要新的数据库，他们会给运维提交工单。如果需要新的服务，也提交工单给运维。需要部署代码?也提交工单给运维。

这种方式往往导致开发者被阻塞并等待运维去处理某个工单，开发者不监控基础设施，也不了解他们的代码是否快或慢，高效或低效。

作为一个行业，我们发现让开发者自己部署和运行自己的代码要好很多。

这更高效，开发者受阻塞更少，沟通开销更小，开发者也从真实世界中得到更多他们代码性能的反馈。

## 原则 7 ：周五部署

健康的工程组织每天部署多次，包括周五。

如果你害怕在周五部署，很可能是因为：

- 你的部署不够可靠。
- 你的部署很慢。  
- 你没有好的监控和报警。
- 你的应用难以调试。
- 你没有测试。

这些都是你必须解决的问题。

Bayer 然后分享了 10 种实用策略，可以用来成为 10 倍开发者：

## 1. 解耦部署和发布

从根本上说，改变生产环境代码有两种可能的操作：部署和发布。发布是指以有意义的方式改变用户体验的过程。部署是指构建、测试和将更改推送到生产软件的过程。传统流程是你在分支上改变代码，当准备好时，合并并部署。一旦部署，用户就会看到新代码。

但是今天的现代工程组织使用[特性标志](https://thenewstack.io/what-are-the-next-steps-for-feature-flags/)。什么是特性标志?它允许你在旧代码旁边编写新代码，然后根据运行时的特性标志，你的应用决定运行旧代码还是新代码。这是巨大的改进。

记住，速度是关键原则之一。将部署与发布分离可以加快两者的速度，因为工程师可以在产品管理准备好发布之前，在代码准备就绪时就部署。

它也加快了发布速度，因为现在你可以立即发布一个特性。并且无需部署就可以立即回滚一个特性。产品经理可以按照自己的时间表进行发布。

然后，更高级的事情也成为可能，比如渐进式发布，其中你为某个百分比的用户启用特性标志。因此，你可以从 5% 开始，如果一切正常，然后增加到 10% 、 20% 等。这是推出更改的最佳方式，因为如果有问题，只有一部分用户会遇到问题，而不是全部用户。

与长期特性分支相比，特性标志要优越得多。你会有更少的合并冲突、更少的陈旧代码、更好的团队动力、更好的团队士气和与真实用户测试东西的更大灵活性。

## 2. 持续部署（CD）

部署是工程组织的心跳。就像人的心脏一样，你希望有稳定的心跳节奏。有了这稳定的部署节奏，你就有了动力。动力对组织来说就是生命。

随着动力的到来，你也具备了将代码尽可能快地在编写后交付到生产的效率。

你想要尽可能频繁地部署，每天多次。每个提交都应该被部署。小的、可理解的更改意味着你拥有可调试和可理解的部署。

编写代码的工程师应该合并自己的拉取请求，然后监控生产中是否有任何意外问题。特性标志是此的先决条件，因为它允许你的团队持续交付小的更改，而不是拥有长期的特性分支。

## 3. 设置通知

确保你为以下内容设置了通知：

- 构建失败
- 部署失败
- 服务停机时间
- 不健康的服务器
- 意外错误
- 不寻常的流量
- 第三方服务状态

许多第三方服务有可以在 Slack 订阅状态页面。

这个好处相对明显，但是它确实需要至少一些努力来设置通知，所以这是许多团队可以快速获益的地方。

而且如果你已经有了通知和报警，你应该审核它们，并问自己这三个问题：

- 它们有用吗?
- 你是否收到太多误报，以至于你开始忽略它们了? 
- 是否应该为某些事项新增报警?

## 4. 优化部署速度

你的目标是让团队拥有 15 分钟或更短的部署时间。

明显长于此会明显痛苦。但是明显快于此可能需要比价值更多的工作，这取决于你的情况。

有几种方法可以提高部署速度：

### a. 跟踪和测量你当前的部署时间

你需要了解起点，以及哪些过程花费了很长时间。这些是你要着力优化的地方。

### b. 加速依赖安装

这个步骤通常是部署中最长的部分之一，所以它可以是一个不错的第一步。

1. 如果使用 JavaScript，切换到 [pnpM](https://pnpm.io/) 。它是 npm 和 Yarn 的直接替代品，具有显著的性能和缓存改进。
2. 缓存整个安装步骤。

使用你的构建系统完全缓存这个步骤，所以如果你的依赖没改变，这个步骤甚至不会运行。

Docker 示例：

![](https://cdn.thenewstack.io/media/2023/07/21b9d601-image1-300x79.png)

Nixpacks 示例：

![](https://cdn.thenewstack.io/media/2023/07/6f2555f2-image2-300x122.png)

### c. 提高构建速度

主要的方法是切换到更快的打包工具。

如果使用 create-react-app 和 webpack ，可以切换到 Vite ，它要快得多。

如果使用 nextjs，升级到最新版本，并确保你没有 `.babelrc` 文件。这会使用 [SWC (Speedy Web Compiler)](https://swc.rs/) 而不是 [Babel](https://babeljs.io/) ，会快很多。

如果你喜欢靠近前沿，可以在 next dev 中传 --turbo 标志使用 [Turbopack](https://turbo.build/pack) ，但它目前只能用于开发，还不能用于生产构建。

### d. 设置构建缓存

如果使用 Docker ，有几件事可以做。

优化构建层。使用多阶段构建。设置远程缓存。

Docker 在本地默认会缓存，而且很快，但在 CI 中你没有永久的机器。所以你需要自己设置缓存。参考 Docker 文档。 

### e. 未来缓存

如果你想要真正冒险，以好坏参半的方式，对 JavaScript 项目，还有另一种风格的缓存可以给你一些重大收益。未来缓存的工作原理是在你的整个团队和 CI 之间共享一个缓存。

这意味着如果你在本地构建了一个提交，然后将该提交推送到 CI 。CI 构建将只是下载你做的缓存构建，并在几秒内完成。

或者，如果你团队中的其他人已经构建了一个提交，然后你在本地运行构建，它同样会下载缓存，在几秒内完成，而不是从头再构建一次。

## 5. 用预览环境替代暂存环境

预览环境是与拉取请求生命周期相关的临时环境。当你打开一个拉取请求时，基础设施可以为该 PR 自动配置环境。

这使利益相关者可以轻松地在类生产环境中查看更改。然后当拉取请求被合并或关闭时，其环境将被自动清理。

它们是特性标志的配套。较大的更改应该使用特性标志，并且通常会有多个 PR 。但是对于小的更改，预览环境通常比为其管理特性标志更简单。

与长期的暂存环境相比，预览环境通常是一个更好的替代，因为暂存环境无论是否需要都一直在运行。而且你必须合并 PR 才能验证更改。

## 6. 基础设施即代码

希望你已经具有了自动化部署，但你可能还没有基础设施自动化。没有[基础设施即代码(IaC)](https://thenewstack.io/infrastructure-as-code-modernizing-for-faster-development/)，你通常通过点击仪表盘来定义你的基础设施配置。

以 IaC 的形式为你的基础设施配置带来自动化，具有巨大的好处：

- 可重复性 / 可重现性
- 一致性和标准化 - 可预测性 
- 版本控制
- 协作和审查

## 7. 平台工程

在很久以前，你需要在数据中心架设自己的服务器。基础设施的抽象级别非常低。然后出现了亚马逊网络服务(AWS)，引入了云和提高了抽象级别。但对于普通开发者来说，它仍然太低了。

这导致了 Heroku 的诞生，全世界的开发者都为此欢呼雀跃。但这种兴奋并不持久，因为运维人员并不高兴。事实证明， Heroku 这样的抽象在大公司是无法扩展的。

所以运维接手，在 AWS 和 Heroku 之间试验了一件新事物，即 IaC 和 Terraform。这非常有效，但开发者又不高兴了。

此外，公司领导层希望提高运营效率，一种方法是为开发者提供自助基础设施，于是我们开始创建内部平台，以提供更好的开发者体验。通过这种方式，业界找到了一种同时让运维和开发双方满意的方法。这就是所谓的平台工程。

现在许多公司都在构建某种内部开发者平台，它可以更像是一个内部 Heroku，也可以只是 Terraform。

三个关键概念是：

- 它部署到你自己的 AWS/GCP 帐户。
- 自助基础设施具有良好的开发者体验。
- 运维可以规定和自定义底层原语。三个主要工具是 Backstage、Humanitec 和 Flightcontrol 。

## 8. 团队协作

- 小团队( 2 至 6 人， 4 人最佳)
- 整个团队一次只在一个项目上协作
- 开工会议(深入讨论如何构建)
- 将项目分解成小任务(通常在开工会议上)
- 并行处理子任务
- 小型 PR ，每天至少一个
- 快速审查/不要成为阻碍
- 自我解除阻塞 - 如果没有人审查，合并你自己的安全 PR

## 9. 基于主线的开发

不要拉取请求，直接提交到主分支。这称为基于主线的开发。

想象它像一个自助餐厅。你的托盘是主分支。当你的汉堡做好时，放到托盘上。薯条准备好时，也放到托盘上。奶昔倒好后，也放到托盘上。一旦托盘装满，就有人叫你的号。

基于主线的开发就是这样工作的。每个特性在准备就绪时直接进入主分支。子任务还是整个项目无关紧要，因为它们都是完全独立工作和可部署的。

如果直接提交到主分支对你来说太激进，那么第二好的做法是短期分支。PR 不应该超过一天。对于一个项目，你应该有许多简短的 PR ，便于他人快速审查并易于合并。这就是如何获得动力。

## 10. 饮食健康并锻炼

我们都需要这个提醒，整天弯腰盯着电脑。一定要照顾好自己。