# GitHub 新功能：问题跟踪和往昔回忆

![Featued image for: New GitHub Features for Issues Tracking — and Memories of Its Past](https://cdn.thenewstack.io/media/2024/09/184b0282-github-1024x683.png)

10 月 1 日，GitHub [发布](https://github.blog/changelog/2024-10-01-evolving-github-issues-public-beta/) 了“问题和项目重大演进”的公开测试版，承诺提供高度期待的增强功能，让“在 GitHub 上分解工作、可视化进度、分类和查找合适的问题比以往更容易”。

作为最受欢迎的代码托管网站之一，GitHub（现为 [微软](https://news.microsoft.com/?utm_content=inline+mention) 所有）的任何变化最终都会影响数百万个组织和 [超过 1 亿名开发者](https://github.blog/news-insights/company-news/100-million-developers-and-counting/)。因此，值得一看究竟引入了什么，以及开发者们今天对此有何反应。

同时，也花点时间回忆一下我们走过的路……

## 传统错误跟踪器

GitHub 于 2008 年推出，仅仅 14 个月后，它就推出了第一个问题跟踪器，当时只有 10 万用户，[据 CNBC 报道](https://www.cnbc.com/2018/06/04/chris-wanstrath-co-founded-github-which-microsoft-bought-for-billions.html)。

至少有一位用户对此表示怀疑。“这是一个不错的基础传统问题跟踪器，但至少公开的内容与过去一年人们一直在尝试的基于 git 的有趣问题跟踪器相比，相差甚远，”2009 年 Hacker News 上的一条 [评论](https://news.ycombinator.com/item?id=566290) 如此抱怨。

历史会记住，这引起了 GitHub 首席执行官 Chris Wanstrath 的 [回应](https://news.ycombinator.com/item?id=566341)，他在自己的 Hacker News 账户 *defunkt* 上发布了帖子，称“不错的基础传统”问题跟踪器“正是它应该成为的样子。我们不做构建花哨的错误跟踪器的生意 :)”。

但这仅仅是开始。“我在 2010 年到 2015 年期间在那里，”开发者 Zach Holman 回忆道，他是 GitHub 的第一批工程招聘人员之一，据他的 [网站](https://zachholman.com/about) 所述，“在五年时间里，我帮助构建和发展了他们的产品和文化，从九名员工发展到 250 名员工。”

在接受 The New Stack 的电子邮件采访时，Holman 同意首席执行官 Wanstrath 关于“不错的基础传统”问题跟踪器的承诺“确实概括了我对问题的感受。它是世界上最大的问题跟踪器，因此从 GitHub 的角度来看，你所能做的事情和支持的范围都受到一定程度的限制……我们有很多关于解决问题和进行软件开发的‘正确’方法的想法，但公司在实践中以 *非常多* 的不同 [方式](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/) 进行操作，因此 GitHub 基本上成为了中立、无观点的工具。”

但他仍然见证了很多历史。“我做的最后一次重大发布是 Issues Three，它基本上是 GitHub Issues 的版本，直到一两周前他们开始预览新功能时才真正没有被触碰。”

Holman [分享了他的回忆](https://thenewstack.io/linux-at-30-early-converts-share-memories-of-their-journey/)，因为一个新时代即将开始。

## “问题”是如何演变的

Holman 回忆起 GitHub 最初的 Issues 的第一次升级，“更多的是 Ajax 风格，更……复杂”。因此，在 2014 年处理 [Issues 3](https://markdotto.com/2014/08/04/shipping-the-new-github-issues/) 时，“我的主要方法是将主要焦点放在单列上，而不是之前的三列混乱，并将 [搜索放在顶部](https://github.blog/news-insights/the-library/the-new-github-issues/)。”

GitHub 作为中立、无观点的工具的定位“也有助于许多第三方工具构建在 GitHub Issues（和 pull 请求……）之上。所以，是的——目标有点像……让我们采用更基本的方法，这种方法可以扩展，以便有观点的生态系统能够围绕它发展。”

但多年来，更新工作一直在继续——本月，GitHub 准备推出全新一轮功能。

这一轮新功能的亮点包括：

- 子问题
- 问题类型
- 高级问题搜索选项

GitHub 在公告中表示，他们的目标是保持“快速和熟悉”，因此新功能是在现有问题前端上添加的。还有一些小的改进，比如新的“复制链接”按钮，让 URL 共享更容易。（在查看包含评论和其他事件的长问题时，“选择‘加载更多’现在将获取 150 个事件，而不是 50 个事件。”）

[注册](https://github.com/features/issues/signup) 仅对组织开放——但测试人员已经开始报告他们的体验……

## 子问题！
子问题可能是最大的变化。在新的公开测试版中，“子问题增加了对问题层次结构的支持，”GitHub 的 [问题文档](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) 解释说，并指出您可以创建“多级”子问题。

根据 GitHub 的 [关于该功能的社区讨论](https://github.com/orgs/community/discussions/139932#discussioncomment-10817810)，最多允许八级嵌套子问题——每个父问题最多可以有五十个子问题。

但每个子问题始终在其标题下方包含一个指向其父问题的链接——即使该父问题来自完全不同的存储库。（正在讨论的一项功能：实际上在子问题列表中显示该存储库的名称……）

在公开测试版中，每个 GitHub 问题描述现在都在底部显示一个名为“创建子问题”的按钮，带有一个下拉菜单，允许您将现有问题变成子问题。只需粘贴问题的 URL 即可创建子问题——或者通过搜索找到它。最棒的是，一个切换按钮可以让您折叠（或展开）所有子问题，立即清理您的视图。

GitHub 还在考虑是否允许将拉取请求也添加为子问题——因为，正如一位开发人员 [指出的那样](https://github.com/orgs/community/discussions/139932#discussioncomment-10821434)，“感觉将拉取请求放在关闭它们的问题的旁边/作为子问题非常合适。”

社区讨论还包括一些普遍的 [正面反馈](https://github.com/orgs/community/discussions/139932#discussioncomment-10916234)。
“感谢您推动这项新功能。子问题显然是现代项目管理的必要改进。”

## 问题类型
另一个新的测试版功能是问题类型，其目标是在组织的存储库中实现“共享和一致的语言”。（默认类型是 *task*、*bug* 和 *feature*，但可以由组织管理员自定义。）

不仅类型会显示在问题列表中（以及问题本身）。“您可以 [过滤](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-by-issue-type) 并按问题类型搜索，”该功能的 [文档](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization) 解释说。“我们正在不断改进问题体验，因此我们很乐意听到您的反馈……”

GitHub 高级产品经理 Riley Broughten [在评论中解释说](https://github.com/orgs/community/discussions/139933#discussioncomment-10824654) 它们与标签有何不同。“问题类型在组织级别进行管理，用于对问题进行全局分类，而标签在存储库级别进行管理。这 [确保问题在存储库之间一致地分类](https://thenewstack.io/ensure-consistency-in-hybrid-clouds-with-amazon-web-services-eks-d-and-istio/)……”

或者，正如一位 [评论者](https://github.com/orgs/community/discussions/139933#discussioncomment-10882191) 所说，“我们喜欢组织级别的类型，因为这消除了在多个存储库之间保持标签同步的痛点……”

GitHub 还正在测试 [针对问题的增强搜索](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#building-advanced-filters-for-issues)，添加“AND”和“OR”关键字（以及括号）

这允许用户构建更复杂的过滤器来查找您要查找的确切问题集……

## 反应和 React
本月初，Holman 在 X 上的一条评论中分享了他的反应。

十多年前，我构建了 GitHub Issues 的最后一次重大更新，我当时……有点希望更多。感觉更像是基于复选框的开发，而不是坐下来真正规划长期改进。

[https://t.co/AhazpHFKTH]— Zach Holman (@holman)

[2024 年 10 月 1 日]
“它还有 React，”Holman 补充道。

在我们的电子邮件采访中，Holman 承认“我对最近的 Issues 更改……还可以。”至少在某种程度上，有一种完成的感觉。“他们最终做的一件事是在搜索栏周围添加了更多自动完成和智能功能，这是我在 2015/16 年如果继续留任的话要做的下一个自然扩展。”

Holman 还 [在 X 上发布了他发现的 JavaScript 错误](https://www.twitter.com/holman/status/1842241385912746438)……)

github 从 html 转向 javascript 的进展非常顺利

[pic.twitter.com/6fcvEfTIdF]— Zach Holman (@holman)

[2024 年 10 月 4 日]
这似乎是在提醒我们，我们正生活在一个不同的时代，霍尔曼在我们的电子邮件采访中似乎这样说。“早期版本的 Issues 都是由两人团队构建的，这也是我们大部分产品工作的方式，直到我们扩展到成为一个‘大型’网站。”

现在，霍尔曼看着 GitHub 进行“一项为期多年的努力，将 Issues（以及网站的其他部分）迁移到 React 和 GraphQL，尽管这样做存在用户和性能方面的挑战。”

霍尔曼还告诉 The New Stack，“GitHub 发布 Issues 后，他们再次对 React/GraphQL 实施了禁令，直到他们迁移到他们正在考虑使用的另一个框架。”

“这部分只是生活……GitHub 现在是一个庞大无比的组织，你无法在没有数十甚至数百人参与的情况下推动事情发展。这就是生活。这也是我喜欢在初创公司而不是大公司工作的原因……”

GitHub 发布新 Issues 的公告也获得了 110 个赞 [在 Hacker News 上](https://news.ycombinator.com/item?id=41708174)——以及更多不同的反应：

- “他们已经让它变得过于复杂，这将完成从生产力到‘可读性’的转变……”
- “我喜欢这些新变化，我期待着更多 [问题之间的依赖关系](https://github.com/github/roadmap/issues/956)。” - “他们应该有一些 AI 解决方案来对问题进行分类，并将实际问题/票证与支持请求和其他噪音区分开来。”
- “问题的一大部分在于‘问题’这个名称。许多大型项目都有数十甚至近百个功能请求和其他非问题‘问题’”
- “如果我们不能在标题、评论和标签之间有效地沟通工作优先级，也许我们需要暂时回到电子邮件。”
但这也很像过去的反应。在谈到他们最初的 Issues 系统时，GitHub 在 2011 年 [承认](https://github.blog/news-insights/issues-2-0-the-next-generation/)，“有些人喜欢它，有些人讨厌它”——同时宣布了 Issues 2.0。（新功能包括分配问题的能力……）

几乎在同一时间，另一篇 2011 年的博客文章宣布了 GitHub Issues iPhone 应用程序——尽管该文章的顶部现在提醒读者该应用程序 [不再受支持](https://github.blog/news-insights/the-library/announcing-github-issues-for-iphone/)。然而，仅仅三年后的 2014 年，GitHub 在搜索框下方添加了现在熟悉的下拉菜单，用于按作者、标签、里程碑或打开/关闭状态筛选结果。

这很好地提醒我们，Issue 功能会来来去去——有些流行，有些被遗忘——当我们开始下一轮改进时。在提供自己的批评和建议的同时，至少 [一位 GitHub 用户](https://github.com/orgs/community/discussions/139932#discussioncomment-10879862) 也确保将这条消息传递给 GitHub 的开发人员：“我喜欢更新。

“新功能非常有用……!”

🆕 我们对 GitHub Issues 和 Projects 进行了多项改进，包括子问题、问题类型和高级搜索！🎉

了解更多并注册公开预览。⬇️

[https://t.co/5j3GZgpc8b]— GitHub (@github)

[2024 年 10 月 2 日]
[
YOUTUBE.COM/THENEWSTACK
科技发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)