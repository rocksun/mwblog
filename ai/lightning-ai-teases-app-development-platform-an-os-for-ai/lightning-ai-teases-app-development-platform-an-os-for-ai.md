<!--
# Lightning AI应用开发平台概览 - 一种“AI操作系统”
https://cdn.thenewstack.io/media/2023/09/2c004ba8-navi-a_bqw8jnlou-unsplash-1024x683.jpg
 -->

PyTorch Lightning的创造者Will Falcon领导的Lightning AI，正在准备开放他们的AI开发平台。我们与Will Falcon进行了讨论。

译自 [Lightning AI Teases App Development Platform — an ‘OS for AI’](https://thenewstack.io/lightning-ai-teases-app-development-platform-an-os-for-ai/) 。

Will Falcon的履历十分出色。他是热门机器学习框架PyTorch的封装PyTorch Lightning的创造者，也是一家名为Lightning App的风投支持的“AI操作系统”公司的CEO。而且，正如我今天在与Falcon的采访中了解到的，他曾是一名海豹突击队训练兵，10年前才开始学习编程。

尽管他目前最出名的是拥有近25，000 GitHub星的开源项目PyTorch Lightning，但他的公司Lightning AI志在成为领先的AI开发平台。平台的一个特征是Lightning Apps，它被描述为一个使用Python构建组合式、响应式机器学习工作流的“框架”。客户也可以在平台上创建完整的AI应用程序。该平台目前仅对企业开放，但不久将面向所有开发者开放。

## PyTorch Lightning的定位

在进入该公司平台之前，我首先想弄清PyTorch(一个最初由Meta开发的开源机器学习框架)和PyTorch Lightning之间的关系。

Falcon最初将其比作“PyTorch像JavaScript，Lightning像React”。但这个类比让我有点困惑，因为PyTorch本身就是一个框架。然后Falcon改用汽车的比喻。

“PyTorch是一个在Python中构建模型的框架，但它只会提供组件，对吧？它就像一辆汽车[而]它只给你很多零件。Lightning[...]为你预组装好了汽车，然后如果需要，你可以调整汽车。”

由于我们谈话开始时我提到了ChatGPT，所以他补充说，OpenAI就像“法拉利”。

我认为这个类比也不完全准确，但无论如何，意思已经明白：PyTorch是一个提供组件来构建机器学习应用的机器学习框架，PyTorch Lightning做了一些“预组装”，但你仍需构建应用程序，而ChatGPT是一个高端的机器学习应用。

## Lightning App的平台

Falcon解释说，Lightning App是一个用于构建机器学习模型的企业平台。目前，这个AI平台还没有面向独立开发者开放，但他说它将在“几个月内”公开。

他继续描述客户通常在Lightning App平台上所做的事情。

“你可以进行研发，开发模型，试验想法，训练模型，部署模型。所以它就像是一个管理模型开发的操作系统。”

因此，该平台的核心是模型开发，或者正如Falcon所说，是“围绕模型开发的操作”。

我询问他目前的客户使用案例。他回答说:“我们有使用我们平台来训练图像模型的社交媒体公司。” “所以他们做信息流推荐[...]他们的规模像一个大型语言模型，但针对图像。”

他还提到使用该平台训练视频或多模态模型的公司。此外，其他客户正在使用它来训练大型语言模型，例如利用大型语言模型进行药物发现的制药公司。

虽然模型开发和训练是Lightning App的主要功能，但Falcon告诉我，它的用户也可以通过选择第三方AI工具在其平台上创建应用程序(我得到了一些常见AI开发工具的名称，但采访后，我被要求不要透露，因为该平台还未公开)。

他向我展示了一些演示示例，但指出目前在Lightning App中构建的大多数应用程序都是公司的内部应用。因此，是时候做另一个比喻了。

“所以你可以把一个Lightning App想象成一个菜谱，”他说，成分是第三方AI工具。“我可以根据需要安装这些成分[...]我们更像是一个操作系统。”

## 开源AI

Falcon最近在[Twitter上发帖](https://twitter.com/_willfalcon/status/1704900446098534891)说：“作为一个社区，我们必须继续倡导AI保持开源。”这是对Meta首席AI科学家[Yann LeCun](https://twitter.com/ylecun/status/1704883900458176798)的回应，他曾表示“AI系统正在迅速成为一种基础设施”，而且“从历史上看，基础设施最终都会开源”。

众所周知，Meta[一直在](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)开源大型语言模型，最近开源的是[Llama 2](https://ai.meta.com/llama/)。我问Falcon，他是否认为大型语言模型领域的其他领先公司，如OpenAI和谷歌，也会在未来开源它们的模型？

他回答说：“最终事物确实会开放。” “在这方面已经有很多先例。[...]所以IBM有主机，对吧?这是只有它们能做的事。想象一下[...]如果没有个人电脑的出现，你只能去IBM获取一台电脑。这太疯狂了，对吧?因此，没有一项基础技术会永远只被一家公司拥有。这不会发生。所以不管它们是否想要，它终将开源——它将可供更多人使用，对吧?因为事情就是这样发展的。所以，我认为这可能是我能想到的最贴切的类比。”

他承认不知道OpenAI和谷歌是否会开源，但他说它们可能会有“专有版本[的大型语言模型]”。这次，他使用了Windows(专有)与Linux(开源)的类比。

在我看来，Windows和Linux的类比比IBM大型机和个人电脑的类比更恰当。随着时间的推移，开源大型语言模型很可能会变得更强大、更广泛，从而最终能够媲美OpenAI的最新GPT模型等专有大型语言模型。可以说Llama 2已经非常接近GPT-4的质量(Anyscale [8月份声称](https://www.anyscale.com/blog/llama-2-is-about-as-factually-accurate-as-gpt-4-for-summaries-and-is-30x-cheaper)Llama 2在摘要的事实准确性方面与GPT-4相当)。

## 总结

说到开放......由于Lightning App还未完全向公众开放其开发者平台，很难判断它对应用开发的好坏，特别是与提供AI功能的成熟开发者平台([如Vercel](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/)平台)相比。Will Falcon用他的操作系统类比说了不少大话，但很少有软件产品能像操作系统那样基础。不过，在Lightning App平台对所有人开放之前，我们不妨等待观望。

目前，开发者可以用开源大型语言模型做什么，这值得我们深思——特别是随着越来越多AI应用开发平台的出现。
