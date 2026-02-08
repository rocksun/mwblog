在AI时代，我们还需要[持续集成](https://thenewstack.io/ci-cd/)（CI）吗？

在一次[QCon AI 大会](https://ai.qconferences.com/schedule/newyork2025)关于AI与工程的专题讨论会上，一位小组成员提出了这个或许是故意挑衅的问题：AI会扼杀CI吗？

尽管许多与会者很快驳斥了AI能走那么远以至于彻底淘汰CI的说法，但这个问题在会议大厅里引起了共鸣。这场会议在曼哈顿上东区的纽约医学科学院的学术环境中举行，最终成为活动中最热门的讨论话题之一。

许多人也认同，在AI时代，[软件开发生命周期](https://thenewstack.io/toward-a-3-stage-software-development-lifecycle/)必须改变。

[Daniel Doubrovkine](https://code.dblock.org/)曾在Shopify、AWS和Artsy.Net担任工程职位，最近在Microsoft担任副总裁，他最初在一个小组讨论中提出了AI是否会彻底扼杀CI的问题。

他最近参观了Meta的运营，并对该公司在将新代码推向生产环境之前实际运行的测试数量之少感到惊讶。此前，开发人员可以在笔记本电脑上本地运行大量测试（“[左移](https://thenewstack.io/golden-paths-start-with-a-shift-left/)”），然后再推送代码。

“我认为AI为我们提供了一个重新思考工作方式的新机会，”他说，并指出这也让我们有机会摆脱一路积累起来的不必要任务。

拉取请求（PR）是CI系统的核心，它在[代码合并到生产环境之前启动一系列软件测试](https://thenewstack.io/how-ai-revolutionizes-software-testing-and-accelerates-product-releases/)。

但“宇宙中没有哪条基本定律规定PR评审或代码评审必须在代码部署之前进行，”[Michael Webster](https://www.linkedin.com/in/mikedwebster/)表示同意，他是[CI/CD](https://thenewstack.io/ci-cd/)服务提供商[CircleCI](https://circleci.com/?utm_content=inline+mention)的首席工程师，在[他自己的演讲中](https://ai.qconferences.com/presentation/newyork2025/ai-works-pull-requests-dont-how-ai-breaking-sdlc-and-what-do-about-it)提到。“有很多合规工具要求这样做，这些也很重要。但这并非软件交付的基本事实。”

![CI图表](https://cdn.thenewstack.io/media/2025/01/d539ad56-circleci-webster-pr-workflow-1024x363.png)

不一定非要这样——CircleCI的Michael Webster（Google Gemini对Webster幻灯片的复刻）。

## AI正在打破软件交付生命周期

我们[将开发生命周期](https://thenewstack.io/a-developers-lifecycle-how-i-shifted-my-thinking-and-coding-left/)视为一系列离散的线性步骤。“你推送代码。你构建，然后测试，然后部署，”Webster说。

“那种模式在AI面前站不住脚，”他说。

Webster在QCon的演讲是关于AI和代理系统如何改变[软件交付生命周期](https://thenewstack.io/ai-has-become-integral-to-the-software-delivery-lifecycle/)的。[CircleCI](https://circleci.com/?utm_content=inline+mention)是一家CI/CD提供商，每年处理超过十亿个客户任务。

![头像](https://cdn.thenewstack.io/media/2025/12/a7e6c590-qcon-webster-circleci-300x225.jpg)

CircleCI的Michael Webster

从CircleCI在自身客户群中观察到的情况来看，软件行业正处于大量使用无头代理的边缘，这些代理可以按计划执行长期任务，或通过[Webhooks](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/)激活。

无头代理在机械翻译方面表现出色，一旦给定一套可靠的规则就能很好地工作。一个结构良好的代码仓库是关键。

CircleCI的一个项目，代理代理在其中发挥作用的是为CI/CD软件引入暗黑模式的项目。设计团队指定了所需的属性，代理完成了检查所有面向用户的组件并进行更改的繁重工作。

“总而言之，我们发现领域专业知识与AI的结合是一种非常强大的组织能力，因为它允许更多人做出贡献，”Webster说。

据Webster估计，通过[Google的GitHub Archive for BigQuery](https://github.com/igrigorik/gharchive.org/blob/master/bigquery/README.md)，GitHub现在每周产生数十万次代理相关活动。它们在做什么？拉取请求。

但由AI驱动的项目可以生成大量的代码，这又会形成自身的瓶颈。

“AI推送的代码量与它们编写的代码量一样多，”Webster说。Circle CI也观察到其客户有这种行为。

## 拉取请求的问题

平均而言，一个代码评审员每小时可以检查500行代码。当一个代理服务每10分钟可以生成1,500行代码时，交通堵塞是必然的。

![](https://cdn.thenewstack.io/media/2025/12/31b0153-qcon-webster-circleci-pr-300x225.jpg)

QCon上的演示。

除了数量问题，拉取请求“普遍效率低下”，Webster说。许多报告显示，PR评审团队评审代码的平均时间从14小时到3小时不等，后者是当一位工程师不懈地推动一个PR通过的情况。

评审PR会让你脱离工作流，并且所提供的信息如果在开发周期的早期出现会更有用。

持续的技术债务累积也是这股PR浪潮带来的一个问题。

自主工作的无头代理可以快速运行，但也可能粗心大意。最近的[DORA调查](https://thenewstack.io/ai-has-won-googles-dora-study-shows-universal-dev-adoption/)报告也发现了同样的情况：速度提高了，但稳定性更差了。

在[一篇论文](https://arxiv.org/abs/2511.04427)中，一组研究人员发现，采用AI服务（如[Cursor](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/)）可以在代码开发上提供暂时的收益，但项目的速度很快会受到“静态分析警告和代码复杂性”的阻碍。

而在他自己的数学计算中，Webster估计，一旦AI的整体速度比人类程序员快75%，通过AI生成[代码](https://thenewstack.io/ai-code-generations-unexpected-costs-for-dev-teams/)所获得的任何收益都将变得毫无用处。

“如果你无法补充加速你的交付，与AI相比，所有这些都将被过程中的所有延迟抵消，”Webster说。

换句话说，“现实是，即使你让AI以你想要的速度运行，你作为一个组织，以及你试图实现的目标，也无法更快地前进，即使你愿意。”

你可以做一些事情，比如优化管道、重写脚本、并行测试以及更好的代码评审，这些都会有所帮助。

![图表](https://cdn.thenewstack.io/media/2025/01/fed223e8-qcon-webster-circleci-pr-2-1024x432.jpg)

CircleCI客户的代理活动。

## AI生成的代码需要更灵活的测试

但也许最好的答案是[重新思考测试](https://thenewstack.io/rethinking-testing-in-production/)和验证过程，让代理尽可能多地完成工作。

“如果你有办法验证AI，你就可以让它尽可能快地运行，”Webster说。

开发一套测试，以断言如果代码通过测试，就应该投入生产。正如其他人指出的，[失败本身就是一个数据集](https://thenewstack.io/the-key-to-agentic-success-let-unix-bash-lead-the-way/)，AI可以利用它来微调自己的过程。

彻底的[单元测试](https://thenewstack.io/unit-tests-are-overrated-rethinking-testing-strategies/)对此很有帮助，尽管其可扩展性有限（约为人类驱动工作量的10倍，Webster估计）。

更好的方法是[测试影响分析](https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-impact-analysis?view=azure-devops)，通过增量验证来加速测试，根据依赖图剪除只所需测试。CircleCI将其应用于自己的单体用户界面应用程序，发现它将测试时间从30分钟缩短到1.5分钟。

这意味着我们可以采用一个AI代理，让它以我们愿意为token支付的费用一样快的速度工作，并给它一个工具来[只运行](https://thenewstack.io/stop-running-tests-with-your-ci-cd-tool/)它需要在所需更改上运行的测试，”Webster说。

这样的操作可以很容易地在容器或笔记本电脑中运行。

选择性关注的原则可以应用于代码评审。“并非所有代码都具有相同的风险水平，”他说。“这里你可以将评审范围缩小到只关注重要的更改，”Webster说。

Circle CI已经构建了自己的代理，名为[Chunk](https://circleci.com/chunk/)，供客户运行以简化自己的测试流程。

## 未来的构建系统将不再是线性的

Webster预测，未来的工程师将不再那么担心代码本身，而更多地关注支持AI不懈地追求生成更多代码。因此，像[修复不稳定测试](https://thenewstack.io/how-to-fix-flaky-tests/)这样的任务将成为首要任务，并且也可以自动化。

取代这种线性过程，我们将需要构建这样的系统：所有必需的测试都在过程的某个地方进行。

“我们不再是线性的‘是/否’，而是将这些事情合并到一个单一的关口，我们所做的就是记录发生了什么，”Webster说。如果测试通过，代码就应该投入生产。“除此之外的一切都是我们在担心其他事情。”

有了AI，“更多的精力很可能会花在测试和评估上，而较少花在考虑我们服务的低级细节的具体设计上。”

*现在可以通过[纯视频通行证](https://ai.qconferences.com/registration/event/newyork2025)获取这些QCon AI演讲以及[其他演讲](https://thenewstack.io/kepler-openais-internal-agent-platform-for-synthesizing-data/)的完整访问权限。*