
<!--
title: 开发人员无意中创建的3个API漏洞
cover: https://cdn.thenewstack.io/media/2024/09/df2bc274-usingapissecurely.jpg
-->

根据专业 API 黑客 Katie Paxton-Fear 的说法，攻击 API 很容易，如果你知道该找什么。她分享了她的攻击方法。

> 译自 [3 API Vulnerabilities Developers Accidentally Create](https://thenewstack.io/3-api-vulnerabilities-developers-accidentally-create/)，作者 Loraine Lawson。

[Katie Paxton-Fear](https://www.linkedin.com/in/katiepf/?originalSubdomain=uk) 自己承认，她不是那种会在黑帽大会或 DEF CON 上发表主题演讲的[网络安全](https://roadmap.sh/cyber-security)黑客。但这位道德黑客正是那种可以利用你的应用程序 API 的黑客。她在上周的 [Kong API 峰会 2024](https://thenewstack.io/kong-new-ai-infused-features-for-api-management-dev-tools/) 上承认，这并不难。

“因为我以前[制作 API](https://thenewstack.io/sxsw-2017-make-apis-easy-use-web/)，所以我了解如何破坏它们，”Paxton-Fear 告诉现场和虚拟观众。“[API 黑客攻击](https://thenewstack.io/lessons-learned-from-hacking-the-tesla-api/) 更多地是关于 API 工作原理的逻辑，而不是特定的有效载荷，而开发人员仍然会犯一些小错误，实际上是很多小错误。”

她在演讲中分享了这些错误，这些错误可以被她利用，演讲名为“[前 4 名 API 漏洞赏金发现：避免常见错误和漏洞](https://konghq.com/resources/videos/top-4-api-bug-bounty-finds-avoid-common-mistakes-vulnerabilities)”。

## 最愚蠢的、可能致命的漏洞

![Katie Paxton-Fear gives a talk on why APIs are vulnerable.](https://cdn.thenewstack.io/media/2024/09/0916b73a-apiwhyvulnerable.jpg)

黑客 Katie Paxton-Fear 讨论了为什么 API 很容易受到攻击。

Paxton-Fear 演示了这些漏洞是多么简单，在某些情况下是“愚蠢”。例如，她将“最愚蠢的漏洞”授予了一个机场系统应用程序的 API 漏洞。该应用程序支持请求飞机飞过头顶，这通常用于社区航空表演。

“当我查看它时，我意识到你可以提供一些关于你当地[机场](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/)的信息——再次，这是有道理的，”她说。“飞机需要跑道。你需要关于跑道的信息。你需要关于机场的信息。否则你怎么才能让飞机飞过头顶呢？”

但是，该应用程序不需要密码。它只使用姓氏和电子邮件，这两者都不是私密的。

“它们非常公开，尤其是如果你在一个你了解很多网络活动发生的行业工作，你甚至可能在你的 LinkedIn 个人资料上拥有这些信息，”她说。“当我们查看它并找到姓氏和电子邮件地址时，我们意识到我们可以更改某人的预订。”

从表面上看，这似乎是一个很小的漏洞，但事实并非如此。由于不需要密码，她可以更改跑道长度或设施等内容。

“现在，这是一个大问题，因为飞机需要特定尺寸的跑道是有原因的，这是因为它们有制动距离，”她说。“如果跑道太短，飞机就会一直往前走。”

她可以将着陆带长度更改为表明它可以容纳 747，而实际上它只设计用于小型通勤飞机，这可能导致损坏、坠毁甚至死亡。

“即使这是一个相对简单的漏洞，它也会产生巨大的影响，这就是我开始说 API 黑客攻击更多地是关于应用程序逻辑的原因，”她说。“这是故意设计成没有密码的，因为他们不想处理密码，但这并不一定是安全性的正确选择。”

## 一个令人费解的漏洞

她讨论的第二个漏洞她称之为令人费解，它实际上是她发现的最快的漏洞。Paxton-Fear 正在查看一个移动应用程序，并在她的计算机上使用 Android 模拟器。她能够插入模拟器发送的流量。

“如果你不了解 [Android 开发](https://thenewstack.io/scoring-comparison-android-ios-development/)，许多开发人员必须克服的一个大问题或挑战是优化他们的访问，”她说。“你不能在手机上发出大量请求，因为每次你在手机天线上传输时，都会消耗手机的电池。”

> “我的漏洞是关于理解应用程序的功能，它应该如何工作，以及如何破坏它。这就是大多数 API 黑客攻击。”
>
> — Katie Paxton-Fear，道德 API 黑客

相反，应用程序使用批处理来发送一个包含五个子请求的请求，这可以节省手机电池。然后，服务器或 API 将解开该批处理请求，并将其转换为您请求的五个请求，获取所有输出并再次将其包装起来。

“这意味着我们仍然可以使用相同的 API，”她说。“我们不需要创建专门的移动 API。我们只需要创建之前没有的包装和解包。这在[开发移动应用程序](https://thenewstack.io/the-role-of-the-database-in-mobile-app-development/)方面确实很有帮助，因为你不能一直传输数据。”

在这种情况下，她测试了一个简单的测验应用程序，允许用户通过正确回答问题获得游戏内货币，这些货币可以实时兑换。

“你们中很多人可能在想，我可以进行[API 请求](https://thenewstack.io/api-governance-and-developer-experience-in-a-developer-portal/)，获取所有问题，获取所有问题的答案，并生成一些免费货币，这绝对是你能做到的，”她说。“但这不仅仅是针对这一个测验问题。这是每个问题的设置方式。所以你可以进去，这是问题 ID 1，但你可以把它改成 2、3、4，这是你标准的 RESTful API，你知道的。把它变成游戏内货币真的非常容易。”

她再次强调，这与应用程序的逻辑有关，而不是 API 功能。

“我的漏洞在于理解应用程序的功能，它应该如何工作，以及如何破坏它。这就是大多数 API 黑客的行为，”她说。“API 通常不会受到很多攻击，大多数[API 攻击](https://thenewstack.io/the-economics-of-api-attacks-and-how-developers-can-stop-them/)，更广泛地说，不会针对 API 的基本基础设施。它们针对的是功能本身。”

## 未记录的 API

她说，API 网关可以帮助执行授权标准，但它们在行业中并没有得到广泛使用。然而，她补充说，许多 API 根本没有文档，就好像这样就能保护它们一样。

“许多 API 更注重没有文档。如果你无法访问它，它就不存在，”她说。“仅仅因为某些东西没有文档，并不意味着你就会遇到像我这样的人去窥探。”

她甚至看到开发人员以某种方式混淆他们的 JSON；例如，模糊键名。

“那仍然只是掩盖问题，”她说。“你真的需要坐下来问自己，这真的应该公开吗？”

她补充说，[API 很难自动测试](https://thenewstack.io/reining-in-the-api-wild-west-5-api-testing-best-practices/)，因为它们依赖于你能够理解逻辑。

“我看到很多人谈论 AI 在黑客方面的未来，但我们仍然错过了对 API 进行基本自动化的机会，因为它们太注重逻辑和业务逻辑，”她说。“实际上，我所有的漏洞都属于这两类：身份验证缺失，以及编写方式存在某种业务逻辑问题，从而产生安全影响。”

她还展示了一个 Laravel 路由控制器，它允许你定义端点，展示了易受攻击代码与非易受攻击代码之间的区别：

![易受攻击代码示例。它有三个额外的行可以被利用。](https://cdn.thenewstack.io/media/2024/09/197d6e83-vulnerable-code-api-.jpg)

*Katie Paxton-Fear 演示文稿中的易受攻击代码示例。*

以及非易受攻击代码：

![Katie Paxton-Fear 演示文稿中的非易受攻击代码。](https://cdn.thenewstack.io/media/2024/09/ed8629a3-notvulnerable-code-api.jpg)

*Katie Paxton-Fear 演示文稿中的非易受攻击代码。*

她指出，两者之间唯一的区别是三行代码和那个 if 语句。

“这甚至不是一行代码，而这，你可以绕过身份验证。一旦你添加[中间件](https://thenewstack.io/middleware-in-the-frontend-tool-helps-manage-webhooks-on-vercel/)，你就添加了身份验证，”她建议。“很多时候，我们都在寻找缺失的 if 语句。这是一个[名为 delete 的函数](https://thenewstack.io/learn-react-delete-functionality-and-the-set-state-hook/)，它删除数据库中的所有内容，但它缺少一个 if 语句。”

## API 问题的核心

她补充说，API 的问题不在于它们难以保护，而在于它们数量众多，开发人员将其他任务优先于测试和保护 API。实际上有成百上千个 API 端点，因此出现遗漏并不奇怪。

> “虽然你可以获得一个可以真正帮助你管理它的解决方案，但如果你没有围绕安全的团队合作和文化，它就会失败，就像其他任何东西一样。”
>
> — Paxton-Fear

但这也是一个[IT 文化问题](https://thenewstack.io/say-no-to-ship-it-culture-slow-and-steady-wins-the-race/)，它会导致安全问题。

“归根结底，任何开发人员都会更重视分解产品 Backlog 和冲刺 Backlog，而不是修复漏洞，因为在冲刺中，即使在软件工程的瀑布模型中，功能也集中在完成特性以获得完整的产品上，” Paxton-Fear 说。“修复错误没有得到同等的优先级。这就是事情被遗忘的方式。”

相反，需要进行基本的内部审查，将发现漏洞作为优先事项。安全不能是“拒绝部门”，因为这会导致与开发人员发生冲突，而不是解决安全问题。IT 组织必须停止将速度置于安全之上。

“虽然你可以获得一个真正有助于你管理它的解决方案，但如果你没有围绕安全的团队合作和文化，它就会失败，就像其他任何事情一样，”她说。

相反，专注于改变文化，让开发人员参与到安全中。她建议，一个简单而有效的方法是教开发人员如何破解和测试自己的代码。

“大多数开发人员真的很喜欢它。他们觉得很有趣，” Paxton-Fear 说。
