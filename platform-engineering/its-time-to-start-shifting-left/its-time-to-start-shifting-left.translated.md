# 是时候开始左移了

![Featued image for: It’s Time To Start Shifting Left](https://cdn.thenewstack.io/media/2024/09/5798c9ad-nick-fewings-s7cyjr_3prc-unsplash-1024x683.jpg)

[Nick Fewings](https://unsplash.com/@jannerboy62?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash.](https://unsplash.com/photos/selective-focus-photography-of-white-arrow-signage-S7cyjr_3prc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

想象一座世代相传的房子，每位房主都添加了自己的个人风格。随着时间的推移，原始结构被一层层的翻新所掩盖。墙壁被重建，管道被重新铺设，电气系统被修补。最终，房子变成了一个错综复杂的更新迷宫，简单的维修变成了令人望而生畏的任务——尤其是如果房子一开始就没有建立在坚实的基础上。

这就是当今世界上许多软件的现状。它不像房子那样在我们眼前坍塌——它只是在慢慢地侵蚀。最近像 Crowdstrike 这样的高调宕机事件只是让人们终于注意到这一点。宕机事件也阻止了[人们购买烘焙食品](https://www.bbc.co.uk/news/technology-68628348)，扰乱了[铁路和航空旅行](https://www.theguardian.com/business/article/2024/jul/19/uk-airports-trains-disrupted-microsoft-global-it-outage)，并阻止了[网上银行转账](https://www.bbc.co.uk/news/business-68671228)。

从这些宕机事件中得出的一个[假设](https://thenewstack.io/why-we-shift-testing-left-a-software-dev-cycle-that-doesnt-scale/)是软件工程师没有对他们的代码进行足够的测试。但这并不属实。[平均而言，开发人员每周有 42% 的时间花在维护上](https://stripe.com/files/reports/the-developer-coefficient.pdf)——而不是创新，也不是编写新代码，而是*修复已经存在的东西*。那么为什么还会发生这么多宕机事件呢？

一个经常导致许多宕机事件的根本原因是[开发人员在过于复杂的软件架构中测试代码](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/)。这是一个高耸的积木塔，没有人敢冒险再添加一块，因为害怕倒塌。这还是在一位高级主管要求实施 AI 之前，尽管没有人记得代码最初是如何构建的。

**软件侵蚀是如何发生的**

如今，软件过于复杂。公司必须跟上竞争激烈的市场压力，[要求开发人员在已经臃肿的代码库中添加新功能](https://thenewstack.io/want-killer-features-foster-dev-user-communication/)。这并不奇怪——代码变得更加复杂，更容易出现故障。

[软件侵蚀](https://thenewstack.io/bringing-back-the-joy-of-software-development/)通常是这样的：开发人员被要求添加一个新功能。这个添加不可避免地会使代码库膨胀。开发人员为了满足紧迫的期限而实施了一个捷径，无意中增加了复杂性。后来，当经理要求扩展产品时，开发人员发现之前的捷径破坏了新的更新。开发人员开始修补，这会消耗大量时间。为了加快修复速度，引入了另一个捷径——可能是出于好意，但很快他们又回到了原点，事情又开始崩溃。

**我们需要摆脱（技术）债务**

代码库越大，软件侵蚀就越容易成为一个自我循环的过程，其中微小的更新会引发一系列问题。简单的质量改进变成了一个复杂的操作，充满了破坏跨团队功能的风险。这种脆弱性阻止了开发人员对产品进行创新和迭代，并浪费了宝贵的开发时间。他们不是想出新主意，而是[被技术债务所困扰](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/)，并忙于修复糟糕的代码。当你考虑到会议、反馈环节和咖啡机旁的聊天，开发人员可能每周不到一半的时间花在增值开发上。

修补循环加上重新发明的需求，鼓励开发人员寻找加快工作流程的方法。通过这样做，开发人员不幸地成为了风本身，慢慢地侵蚀着软件。

**打破循环并“左移”**

我们已经听说了“左移”多年，但这个信息还没有完全传达出去。许多公司仍然习惯于用茶匙来救助一艘正在下沉的船。他们给开发人员投入更多测试时间，或者聘请外部 QA 团队。看起来很忙——感觉很忙。但是，如果由于旨在消除错误的“修复”而出现了新的错误，那么这并不是一个很好的时间利用方式。
企业需要从一开始就将质量融入其产品开发流程。在墙壁建成之前修复房屋地基要容易得多（也便宜得多）。这意味着从第一天开始将 QA 整合到您的开发流程中，从设计阶段开始，而不是在代码编写之后。

为了实现这一点，您需要利用多种工具和视角。在编写时运行静态代码分析。定期执行自动功能测试。了解您的代码重复、依赖关系链和组件交互。这样，您就可以清楚地了解问题所在，即使它们无法在一夜之间解决。

如果做不到这一点，可能是时候退一步看看大局了。您的架构是否仍然适合目的？对于许多中小企业来说，彻底改造在短期内可能很痛苦，但它可以拯救他们免受痛苦。对于拥有多年遗留代码的大型组织来说，这更棘手。

不同的团队成员有不同的优先事项。开发人员可能会抵制额外的分析步骤，因为他们认为这些步骤是额外的工作。至关重要的是，要尽早确定谁负责什么以及为什么这些步骤是必要的。尤其是高管需要确信，如果没有这些基本的 QA 流程，他们也可能很快就会面临 Crowdstrike 级别的噩梦。

软件侵蚀不仅仅是开发人员的问题，而是整个公司的问题。随着软件故障越来越多地登上头条新闻并威胁到企业的生存，组织必须优先考虑其软件架构的坚实基础。不幸的是，太多团队正在使用他们不完全理解的系统。但是，通过将新功能与原始设计保持一致并了解其系统的复杂性，您可以减少对变通方法的需求。结果是一个更稳定的系统——每个人都赢了。

## 额外报道
[通过“从左开始”将“左移”方法更进一步](https://thenewstack.io/shift-left-method-further-by-starting-left/)
[为什么我们将测试左移：无法扩展的软件开发周期](https://thenewstack.io/why-we-shift-left-testing-unscalable-software-development-cycles/)
[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)