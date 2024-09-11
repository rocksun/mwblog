# 框架让 React 开发者可以用代码创建视频

![特色图片：框架让 React 开发者可以用代码创建视频](https://cdn.thenewstack.io/media/2024/09/4a1d9a03-pexels-mediocrememories-1117132-1-1024x683.jpg)

React 以其创建前端网页动画和特效的能力而闻名。程序员 Jonny Burger 觉得视频编辑器使用起来很有挑战性，因此他决定利用 React 的动画功能，构建一个使用 [React 代码创建视频](https://github.com/remotion-dev/remotion/blob/main/packages/docs/static/img/fireship-quickgif) 的框架。它被称为 [Remotion](https://www.remotion.dev/)。

> “对于那些想要构建自己的视频编辑器的人来说，视频方面还有很多未解决的问题，”Burger 告诉 The New Stack。“我们的使命是让人们……让个人能够在一个周末构建出自己真正优秀的视频编辑器。”

## 为什么用 React 代码创建视频？

为什么有人想用代码创建视频？首先，Burger 说，使用现有工具以编程方式更改视频很困难。

> “视频编辑器让你点击一个按钮就可以导出视频，并以编程方式与这些程序交互——这很难，因为这不是它们的设计初衷，”他说。

其次，使用 Remotion 不仅仅可以创建视频。事实上，使用 Remotion 主要有三个用例：

*   创建动态图形，为视频添加字幕等操作或缩放等特效；
*   批量制作视频；以及
*   为多个用户创建自己的视频编辑器。

瑞士的一位马拉松组织者使用 Remotion 为跑步者提供了个性化视频，展示他们冲过终点线的情景。组织者使用 Remotion 批量渲染视频，其中融入了他们时间的动画和一位著名马拉松运动员的剪辑问候。

他表示，一些用户甚至在其中加入了人工智能，从而能够使用 Remotion 将人工智能头像与特效动画和字幕结合起来。他补充说，这种方法已经被用于为 YouTube 和 TikTok 创建视频。

[Submagic](https://www.submagic.co/) 就是一家以这种方式 [使用 Remotion 的公司](https://www.remotion.dev/showcase)，允许用户上传长视频，并使用人工智能提取简短片段，这些片段都添加了字幕，并添加了特效，使其更能吸引社交媒体网站的用户。Burger 表示，他们每个月都在使用这种技术创作超过 100,000 个视频。

他补充说，软件开发人员还可以使用 Remotion 创建自己的视频编辑器。

![Remotion 中用于渲染视频的 React 代码。](https://cdn.thenewstack.io/media/2024/09/0535431d-remotion.jpg)

[Remotion 网站](https://www.remotion.dev/) 的屏幕截图。

> “市面上有太多不同的视频、音频格式和编解码器，要处理用户抛出的任何东西实际上非常困难，”他说。“我们的计划是解决很多无聊的问题，这样你就可以创建像你习惯的那样的视频编辑器，但你不需要花费数十年的时间来构建它。”

## Remotion 独特的许可证

Remotion 是开源的，因此代码是可用的，并且有 200 多名开发人员为其做出了贡献。也就是说，Remotion 确实有一种 [不寻常的许可方式](https://github.com/remotion-dev/remotion/tree/main?tab=License-1-ov-file)。个人、非营利组织、评估目的和只有三人的企业可以使用 [免费许可证](https://github.com/remotion-dev/remotion/tree/main?tab=License-1-ov-file#free-license)，而希望将该框架用于商业用途的大型公司则可以使用单独的 [商业许可证](https://github.com/remotion-dev/remotion/tree/main?tab=License-1-ov-file#company-license)。

Burger 说，这种许可证源于一种担心，即该项目会很受欢迎，但他却没有足够的资源来妥善管理它。

> “我通常会将我所有的项目都发布为开源项目，我担心这会像滚雪球一样越滚越大，但开源实际上是免费赠送，”他说。“我还主张其他维护者在 [开源项目](https://thenewstack.io/the-future-of-open-source-needs-more-give-and-less-take/) 之前，应该考虑一下 [可持续性方面](https://thenewstack.io/how-to-build-open-source-sustainability/) 的情况，从资金和时间上来说，他们必须投入才能使项目做大。我希望人们在总体上更多地思考这个问题，并采用类似的许可证。”

他说，由于采用了分层许可证，Remotion 处于收支平衡状态，他可以给自己和 Remotion 的业务经理 Mehmet Ademi 发工资。

## 竞争对手

还有其他用于创建视频的开源选项，例如 [FFmpeg Hi](https://sourceforge.net/projects/ffmpeg-hi/)，但它们并不是“真正可编程的”，没有 if 语句和引入数据的能力，Burger 说。他还补充说，它们也没有显示实时预览。
“我们的视频完全可以通过代码编程，因此您实际上是在编写网站代码。我们使用浏览器作为画布，因为浏览器非常擅长显示各种图形。然后，我们提供了一种将其转换为视频的方法。”

—— Jonny Burger，Remotion 的创建者

Burger 认为，Remotion 是使用代码创建视频的先驱，并补充说，有两个类似但并不完全相同的项目：Framer Revolution（一个 React 动画库）和 [Motion Canvas](https://www.remotion.dev/docs/compare/motion-canvas)。

“我们的视频完全可以通过代码编程，因此您实际上是在编写网站代码。我们使用浏览器作为画布，因为浏览器非常擅长显示各种图形。然后，我们提供了一种将其转换为视频的方法，”他说。

Ademi 补充说，如果计划只制作一个视频，那么传统的视频编辑器可能会满足您的需求。

“如果您具备使用传统视频编辑器的技能，并且只想创建一个视频，那么您宁愿使用那些，”Ademi 说。“我们提供的基本上是一个可扩展视频制作解决方案。因此，充分利用 Remotion 的方式是创建您自己的网络视频编辑器，以便人们可以使用它来创建他们的视频，例如 Adobe After Effects 视频编辑器的简化版本。”

## 视频乐高积木

他表示，展望未来，Remotion 计划添加一些小软件包，以便开发人员只需安装一个软件包即可解决特定的视频问题——就像视频的 [乐高积木](https://thenewstack.io/how-to-build-an-interactive-lego-robot-using-python/)。例如，已经有一个软件包可以自动转录，Burger 计划添加一个软件包，用于在视频中包含 GIF。

“随着时间的推移，我们计划让它越来越像乐高积木，您只需将合适的软件包组合在一起，”他说。

[YOUTUBE.COM/THENEWSTACK

技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等内容。](https://youtube.com/thenewstack?sub_confirmation=1)