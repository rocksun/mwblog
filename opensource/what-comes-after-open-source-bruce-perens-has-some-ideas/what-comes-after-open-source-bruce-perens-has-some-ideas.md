
<!--
title: 开源之后是什么？Bruce Perens有一些想法
cover: https://cdn.thenewstack.io/media/2024/11/c1fa6192-bruce-perens-2009-2.jpg
-->

原始开源定义的创建者提出“Post Open”作为支持创建者、维护者及其项目的一种新方法。

> 译自 [What Comes After Open Source? Bruce Perens Has Some Ideas](https://thenewstack.io/what-comes-after-open-source-bruce-perens-has-some-ideas/)，作者 David Cassel。

是否存在比开源软件更好的开发模式？有人这样认为——具有讽刺意味的是，这个人正是1997年撰写[原始开源定义](https://web.archive.org/web/20131004221206/http://ldp.dvo.ru/LDP/LGNET/issue26/perens.html)的那个人。

现在，[Bruce Perens](https://www.linkedin.com/in/bruce-perens/)正在开发一种他称之为“[Post Open](https://postopen.org/)”的替代方案，而且似乎进展顺利。“我们已经开始组建团队，”Perens通过电子邮件告诉The New Stack。周四，Perens甚至在PostOpen.org上[发布](https://postopen.org/2024/11/14/legal-progress-new-code-of-conduct-version/)了一篇新的更新：他与律师讨论了未来组织的结构，以及其拟议的零成本许可证。“它还没有完成，但距离我们在人们使用它之前所需的法律稳固性更近了一步。”

那么，编程世界是否正朝着范式转变——一种纠正当今开发世界中一些[资金短缺](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/)的转变？我们能否为代码的开源许可要求创建一个更强大的执行机制——同时也能使我们的[软件供应链更安全](https://thenewstack.io/2023-the-year-open-source-security-supply-chain-grew-up/)？

Perens相信这一切都是可能的，他正在公开构建这种替代方案。这是一个对未来的充满希望的愿景——但也许它也为我们提供了其他东西：对我们当前现状的启发性观察，以及我们想要解决的一些问题。

## 通往“Post Open”的道路

1998年2月，Perens与[Eric S. Raymond](https://x.com/esrtweet) [共同创立了开源倡议](https://opensource.org/history)。但在2020年初，Perens在对其新的[加密自主许可证](https://opensource.org/license/cal-1-0)的争议中离开了该组织，在OSI邮件列表上[抱怨](https://lists.opensource.org/pipermail/license-review_lists.opensource.org/2020-January/004598.html)他们“相当热情地走向接受一个不尊重自由的许可证”。

Perens已经担心OSI创建了超过100种不同的软件许可证，在[邮件列表](https://lists.opensource.org/pipermail/license-review_lists.opensource.org/2019-September/004412.html)上敦促，“让我们废除巴别塔吧”。

在[2020年发表在Slashdot上的评论](https://news.slashdot.org/story/20/01/05/208249/open-source-initiative-co-founder-bruce-perens-resigns-citing-move-toward-license-that-isnt-freedom-respecting#perens_coherent)中，Perens谴责了一个这样的世界：“每个额外的许可证都不会带来高价值的创新或新功能——至少在支持社区而不是某些公司的方式上是这样”。

接下来发生了什么？OSI继续运作，尽管最近[面临新的批评](https://thenewstack.io/osis-definition-of-open-source-ai-raises-critical-legal-concerns-for-developers-and-businesses/)，关于其[新发布的开源AI定义](https://thenewstack.io/the-open-source-ai-definition-is-out/)。但Perens本周告诉The New Stack：“幸运的是，开源有一个发展途径，而不必关心OSI的问题。”他提醒我们，“我已经研究开源之后的事情几年了。”

然后他将我们引导到[PostOpen.org](https://postopen.org/)，该网站论证了开源的当前问题“已经对每个人都显而易见”。

它的第一个链接指向[一个强调软件即服务问题的页面](https://postopen.org/how-post-open-works/)——在那里，“拥有整个财富500强客户的开发者往往完全没有得到补偿，并且面临严重的经济压力。”在后来写到应该支付给开源开发者的“几乎普遍的资金转移”时，它警告需要“鼓励更多开发者走这条路，否则最终会失去他们和他们的创新。

“Post Open提供了一种支付他们工作的方式。我们相信Post Open可以解决开源问题，并建立一个更健康的社区，以解决这些问题并实现开源今天未能实现的目标。”

## “Post Open”是什么意思？

该网站称，一个重要的目标是“通过去中介化将资金导向开发者”。

正如Perens在我们的采访中所说：“你可以把它想象成‘带牙齿的开源’。它保留了开源对个人和小型公司的自由，也就是我们*应该*帮助的对象……它要求收入超过[每年500万美元](https://postopen.org/how-post-open-works/)的资金雄厚的实体，支付一小部分收入（随着它们的发展，比例会增加到1%）来支持开发者。我们使用工具对git仓库进行检测，以便将这笔款项分配给付费用户正在使用的软件的开发者。”

PostOpen.org建议将一部分资金扣留“用于税收和运营目的”，但Perens对收入最终能够到达开发者手中感到兴奋。“因此，我们将停止运营当今世界最大的企业福利计划，就像开源所做的那样。开发者将能够负担得起维护他们的软件。”

PostOpen.org指出，已经有软件可以扫描git（尽管“我们可能希望开发我们自己的”）。但除此之外，“必须构建一个用于分配的软件基础设施，包括开发者注册他们的git ID和加密身份的方法。”（“有很多服务可以做到这一点，”该网站指出。带有加密密钥设备的成本低至每件14美元，这些设备可以免费提供给开发者。）

但这带来了另一个巨大的好处。通过可靠地识别开发者——使用加密硬件支持的身份验证和安全的软件链式保管——你[显著提高了安全性](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/)，因为“任何不法行为者都可以被追踪和起诉”。（更不用说通过“为开发者提供适当的资金来维护他们的软件”而获得的安全性和质量提升。）当然，可供下载的文件“将进行加密签名，以进一步支持链式保管的完整性”。

最后，软件基础设施将为开发者提供指定支付方式的方法。（该网站指出，“对于受雇于雇主并支付薪水从事Post Open软件工作的程序员，付款将支付给雇主。”）随着款项的到来，还有一些其他有趣的细节。PostOpen.org网站指出，除了开发者之外，还可以支付“文档创建者”的报酬——并补充说，“其他角色的报酬将在稍后制定”。

与此同时，对于那些资金雄厚的实体，许可协议还将要求“对公司使用、嵌入产品和作为服务执行的Post Open软件进行机器可读的会计核算”，以及对“使用程度（例如，包含该软件的产品销售数量）……”的会计核算。合规很简单——每个人每年结算一次。（根据[PostOpen.org](https://postopen.org/how-post-open-works/)，支付要求也适用于“将软件包含在付费产品中的公司”，以及任何“希望将修改保密的公司”。）

但是，为了保护客户软件使用情况和年度收入数据的隐私，“所有合规信息以及来自公司的付款金额都受[保密协议](https://postopen.org/how-post-open-works/)约束，”该网站写道——付款甚至由注册会计师事务所处理，因此“公共组织可以看到总数（程序的使用、收入等），而不是你的私人数据……”

该网站还提到另一种奖励良好行为的方案：资金雄厚的实体将继续支付开发者支持款项，“*除非*他们向Post Open Collection发布足够的贡献，在这种情况下，我们将*向他们付款*”。


## 开发者合规支持

另一个重要目标是简化项目在开源和Post Open许可证下的不可避免的双重许可。“我已经为开源项目加入潮流并开始获得开发者的报酬提供了便利，而无需放弃他们的旧许可证和依赖它们的使用者，”Perens告诉TNS。

但该网站还雄心勃勃地谈到了“Post Open Collection，一个授权给用户的软件库”。它设想了一个官方的（和“规范的”）git仓库，用于“专门的Post Open许可软件”，免费提供给世界各地的开源开发者（该网站指出，他们今天“大多使用营利性git运营商，这些运营商利用他们的工作来训练AI”）。

该网站还写道，它将帮助开发者遵守新的法律，例如欧盟的网络韧性法案。在我们的现有系统下，如果开发者没有足够的资源来遵守规定，它就会给那些食物链上层的有钱中间商一个机会，“从开源开发者那里转移资金，因为他们可以销售开发者软件的符合规定的副本，而开发者却不能”。
因此，Post Open 的部分宣传将包括代表“Post Open 集合中所有开发者”处理所有此类新法律的要求。

在我们的邮件采访中，Perens 強調了 Post Open 世界的最大优势之一：开发者“不必再忍受我们今天猖獗的许可证违规行为。我们将留出一些收入来为他们打官司。”

该网站认为，Post Open 运营协议“将包括授权 Post Open 管理部门代表 Post Open 集合中任何作品的开发者进行执法。”

随着更多资金的收集，它希望解决开发者世界中的另一个漏洞。目前，Linux 基金会是“少数几个能够持续承担游说费用的开源组织之一”。但随着开源集体收入的增加，它可以用来发展“开发者的代表进行游说和其他目的”。

并且，可能影射了 Linux 基金会，Post Open 网站强调其组织的治理“完全由个人软件创建者掌控，这本来就应该是开源的”。具体来说，该计划是作为一个由软件开发者拥有和控制的非营利公司运营。

Post Open 的既定目标之一是“根据付费用户对软件的使用情况以及他们对该软件的贡献大小，向开发者分配报酬”。但它也清楚地说明了其动机：“公平地支付开发者为其工作付出的报酬。”

希望已经很高。“想象一下，开源开发者不再是恳求者，”Perens 在我们的邮件采访中说。“他们不必*乞求*公司履行其应尽的义务。他们不必被大公司以及这些公司创建的组织剥削。

“他们可以待在家里编程，并且整天靠编程谋生，而不必为此经营一家公司……他们的软件将更安全，并且能够更好地应对开源开始面临的所有法律挑战，例如欧盟网络韧性法案。

“我们已经开始组建团队。我认为我们可以做到。”
