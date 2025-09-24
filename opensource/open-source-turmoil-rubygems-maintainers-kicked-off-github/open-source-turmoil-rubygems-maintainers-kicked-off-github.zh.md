Jan Lehnardt 在一篇 [Mastodon 帖子](https://sunny.garden/@janl@narrativ.es/115230600679633623)中说得最好：“Ruby 到底怎么了？”

发生的事情是 RubyGems 社区感到不满，因为维护者们在上周末被踢出了 GitHub 仓库。RubyGems 是可重用 Ruby 代码及其他组件的软件包，用于为 Ruby 项目添加功能。它们是 Ruby 语言的标准包管理器。

本月早些时候，Ruby Central 用其开源总监 [Marty Haught](https://github.com/mghaught) 取代了所有维护者。Ruby Central 是一个非营利组织，致力于“自 2001 年以来在 Ruby 编程生态系统中推动创新和建设社区”。它还运营着全球最大的 Ruby 大会 RubyConf 和 RailsConf。

## 社区保障还是恶意接管？

如果目标是建设社区，Ruby Central 可能犯了一个严重的错误。据维护者 [Ellen Dash](https://github.com/duckinator)（又名 [Puppy 或 duckinator](https://bsky.app/profile/duckinator.bsky.social)）称，9 月 9 日，一名匿名 RubyGems 维护者在没有解释的情况下，将 RubyGems 的 GitHub 企业账户重命名为 Ruby Central，将 Ruby Central 的开源总监 Marty Haught 添加为维护者，并移除了 RubyGems 项目的所有其他维护者。

9 月 15 日，匿名维护者表示，在与 Haught 谈话后，他/她恢复了之前的权限。Dash 报告称，Haught 说这次删除是一个“不应该发生”的错误。

Dash 写道：“‘恢复’保留了一个显著的变化：Marty 现在是 GitHub 企业账户的所有者。RubyGems 团队的回应是立即开始制定一项逾期未制定的官方治理政策，灵感来自 [Homebrew](https://github.com/rubygems/rfcs/pull/61)。”

但 Dash 写道，9 月 18 日，Haught 在没有解释的情况下，撤销了 RubyGems、Bundler 和 RubyGems.org 维护者团队所有管理员的 GitHub 组织成员资格。

Dash 在一篇在社交媒体上分享的[告别 RubyGems 的帖子](https://pup-e.com/goodbye-rubygems.pdf)中写道：“通过这样做，他为自己和 Ruby Central 的其他全职员工攫取了控制权。当天晚些时候，在拒绝恢复 GitHub 权限后，Ruby Central 进一步撤销了对 RubyGems.org 上 bundler 和 rubygems-update gem 的访问权限。

“我在这里不拐弯抹角：这是一次恶意接管。”

## Ruby 非营利组织援引信托责任

9 月 19 日，[Ruby Central 发布了一份解释](https://rubycentral.org/news/strengthening-the-stewardship-of-rubygems-and-bundler/)其行动的声明，称安全担忧和相关的信托责任是这一决定的驱动因素。

Ruby Central 的帖子称：“作为这一基础设施的非营利管理者，Ruby Central 负有信托责任，以保护供应链并维护生态系统的长期稳定性。”该帖子未署名任何个人。

它继续说：“在与法律顾问协商并进行最近的安全审计之后，我们正在强化我们的治理流程，正式化运营者协议，并收紧对生产系统的访问。展望未来，只有 Ruby Central 雇佣或签约的工程师才能拥有 RubyGems.org 服务的管理权限。”

Ruby Central 还引用了[软件供应链攻击](https://thenewstack.io/lessons-learned-from-2021-software-supply-chain-attacks/)，称其要求“采取积极措施，端到端地保护 Ruby gem 生态系统。”

Ruby Central 董事会成员兼 Vestmark 首席技术官 [Freedom Dumlao](http://linkedin.com/in/freedomdumlao) 也解释了[为什么安全问题需要采取行动](https://apiguy.substack.com/p/a-board-members-perspective-of-the?r=43k3q&utm_medium=ios&triedRedirect=true)。

他写道：“Ruby Central 长期以来一直负责 RubyGems 和 Bundler。这不是一个新的发展，我老实说对这种困惑感到非常不解。不困惑的是[供应链正遭受攻击](https://thenewstack.io/how-supply-chain-attackers-maximize-their-blast-radius/)。我们可以在最近对 RubyGems 的攻击以及对其他生态系统造成全球新闻头条的重大攻击中看到这一点。依赖 Ruby 的公司指望 Ruby Central 确保它们不处于风险之中。其中一些公司是 Ruby Central 的赞助商，有些不是，但所有公司都有一个合理的需求，要知道它们可以告诉用户他们正在使用的软件是安全的。”

但这一消息并未受到好评，Ruby 开发者纷纷在社交媒体和博客上表达他们对 Ruby Central 此次举动的不满，有时甚至是愤怒。

## 社区对 Ruby Central 行动的回应

芝加哥的开发者 [Sam Stephenson](https://indieweb.social/@sstephenson) [在 Mastodon 上发帖](https://indieweb.social/@sstephenson/115231391147943333)称：“‘信托责任’是‘我们从一个敌对捐助者那里获得了数百万美元，以换取对 RubyGems 基础设施的控制权’的一个绝佳的委婉说法。”他没有说明那个敌对捐助者可能是谁。

[![Sam Stephenson 在 Mastodon 上的评论截图，内容是“‘信托责任’是‘我们从一个敌对捐助者那里获得了数百万美元，以换取对 RubyGems 基础设施的控制权’的一个绝佳的委婉说法。”](https://cdn.thenewstack.io/media/2025/09/5dd99225-samstephensonrubygemscomment.jpg)](https://cdn.thenewstack.io/media/2025/09/5dd99225-samstephensonrubygemscomment.jpg)

截图来自 [Mastodon](https://indieweb.social/@sstephenson/115231391147943333)。

他并非唯一一个谴责的人。[Mike Perham](https://github.com/mperham) 是一个自称的 Ruby 开发者，也是 [@sidekiq](https://github.com/sidekiq/sidekiq)（一个流行、开源的 Ruby 后台作业框架）和 [Faktory](https://github.com/contribsys/faktory)（一个与语言无关的持久化后台作业服务器）的创建者。他也是那些认为 Ruby Central [此次举动为越权](https://www.reddit.com/r/ruby/comments/1nmzqq2/comment/nfoaj3w/)的人之一。

他说：“Ruby Central 不拥有 RubyGems 源代码的版权，该仓库在 Ruby Central 之前就已存在。Ruby Central 的角色是管理 rubygems.org 基础设施并支付 RubyGems 的持续维护费用。RC 不控制谁是维护者以及谁可以加入维护团队。像任何开源项目一样，这始终是一个团队决定。”

他补充说，Ruby Central 需要向社区提供更多信息。

他表示：“在你告诉我们赞助商及其要求之前，我们只能推测实际原因。这一变化需要公开透明。rubygems/rubygems 在 hsbt 单方面、未经讨论地移除了整个现有团队并添加 Marty [Haught] 为管理员之前，并不在 Ruby Central 的控制之下。那是非法夺权。这一行动本应是一个公开流程，而不是幕后交易。”

[![Mike McQuaid 对 Ruby Central 和 RubyGems 维护者之间争议的看法。](https://cdn.thenewstack.io/media/2025/09/f73eee71-mike_mcquaid.jpg)](https://cdn.thenewstack.io/media/2025/09/f73eee71-mike_mcquaid.jpg)

截图来自 [Mastodon](https://sunny.garden/@mikemcquaid@mastodon.social/115246937754924431)。

Dash 在给工程师 [Mike McQuaid](https://github.com/mikemcquaid) 的 [Bluesky 回应](https://bsky.app/profile/duckinator.bsky.social/post/3lz7mwj3lmk2y)中说：“我没有看到阻止情况恶化的方法，所以我辞职并记录了我所看到的一切。”Mike McQuaid 曾尝试 — 但未能 — [促成 Ruby Central 和维护者](https://sunny.garden/@mikemcquaid@mastodon.social/115246934696920846)之间就此问题进行讨论。“我把生命的三分之一都奉献给了那个项目，我不得不解释我失败了。这种痛苦难以言喻。”

## 视频和更多沟通的承诺

周一，Ruby Central 安排了社区问答环节，但当天下午晚些时候宣布由于犹太新年，该环节将改期。与此同时，于 5 月加入该组织的执行董事 Shan Cureton 发布了[一段 YouTube 视频信息](https://www.youtube.com/watch?v=VyCiE3GjQps)。

她为糟糕的沟通以及由此造成的困惑表示歉意。她解释了为什么从 Ruby Central 的角度来看，这是必要的。

她说：“当 Bundler 和 RubyGems 通过与 Ruby together 的合并而由我们负责时，它带来了运营风险、法律责任和实际义务。不幸的是，合并留下了治理责任和运营漏洞，我们现在正在弥补这些漏洞。”

Cureton 指出，最近几周，角色和职责发生了变化，并且[赞助商对供应链](https://thenewstack.io/the-challenges-of-securing-the-open-source-supply-chain/)风险提出了疑问，这清楚地表明：Ruby Central 需要迅速弥补治理和访问漏洞。

她说：“随着主要维护者的离职和安全工程师的变动，围绕 RubyGems bundler 和 rubygems 管理访问权限的问题……变得紧迫起来。我们已经开始与现有维护者讨论如何加强治理和访问控制。我们非常珍视他们的贡献，但很明显，我们无法在我们所面临的时间限制内就解决安全和责任问题所需的步骤达成一致。”

Ruby Central 还引用了[软件供应链](https://thenewstack.io/get-a-handle-on-software-supply-chain-security-with-lfx/)攻击，称其要求“采取积极措施，端到端地保护 rubygem 生态系统。由于这些担忧，Ruby Central 董事会投票决定暂时移除‘某些管理和提交权限，直到协议到位’。”

Cureton 说：“这个决定从未打算永久化。它旨在巩固保护，为我们争取时间制定协议，并对社区和依赖我们的公司负责。”

与此同时，她补充说，正常的发布和安装仍在继续。

> “这个决定从未打算永久化。它旨在巩固保护，为我们争取时间制定协议，并对社区和依赖我们的公司负责。”
> **– Ruby Central 执行董事 Shan Cureton**

她说：“作为 Ruby Central 的执行董事，我的任务是让组织达到真正可持续的状态。这意味着不仅要稳定我们作为一个组织的运作方式，还要加强我们管理和维护开源基础设施的方式。当我们开始审查我们的实践时，很明显，我们需要更强大的安全协议和 RubyGems 和 Bundler 中更清晰的治理。”

她补充说，Ruby Central 最近开始招聘员工，这引发了关于离职交接的新职责和协议，以及对于一个历史上由志愿者和独立承包商运营的组织来说，更强的安全控制。

她补充说，这些步骤不仅仅是为了风险缓解。

她说：“它们是为了确保 Ruby Central 保持可持续性并能够服务 Ruby 社区。”

她明确了两件事：首先，权限只是暂时受限，Ruby Central 正在最终确定运营者和贡献者协议；其次，这是 Ruby Central 首次为维护者制定这些具有法律约束力的协议。

## RubyGems 对 Ruby Central 的问题

Cureton 说：“在大多数[开源项目](https://thenewstack.io/what-to-do-when-critical-open-source-projects-go-end-of-life/)中，如果代码是库或框架，通常不会看到正式的运营者协议。人们根据贡献者许可协议、行为准则或指导委员会的决定进行贡献。但 rubygems.org 不同。它不仅仅是代码。它是一个生产服务。它为 Ruby 生态系统运行关键基础设施，处理数十亿次下载，存储敏感元数据，并受到有合规性要求的公司的依赖。”

据 Cureton 称，由于它是一项服务，Ruby Central 承担法律责任、财务风险和运营风险。

她说：“这就是为什么运营者协议是必要的。它们确保访问与责任和问责挂钩。虽然您可能在 Rails 或 React 等项目中看不到它们，但它们在 npm、pi 或 Docker Hub 等服务中是常态。”

她说：“我想承认，整个过程的进行方式显得非常突然，我们对此感到遗憾。我们的使命始终是保护社区，保护生态系统，并为未来建设更强大的基础。”

YouTube 视频的评论已关闭。