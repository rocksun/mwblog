<!--
title: OpenClaw最大安全漏洞，催生Jentic Mini
cover: https://cdn.thenewstack.io/media/2026/03/6aba3b31-beatriz-camaleao-xa_xf9wakom-unsplash-1.jpg
summary: OpenClaw作为通用AI代理迅速走红，但也暴露了凭据泄露等严重安全问题。Jentic Mini为此提供权限防火墙，集中管理凭据，实现细粒度访问控制，旨在为快速发展的代理AI时代构建安全网，并应对SaaS模式的变革。
-->

OpenClaw作为通用AI代理迅速走红，但也暴露了凭据泄露等严重安全问题。Jentic Mini为此提供权限防火墙，集中管理凭据，实现细粒度访问控制，旨在为快速发展的代理AI时代构建安全网，并应对SaaS模式的变革。

> 译自：[OpenClaw's biggest security flaw is why Jentic Mini exists](https://thenewstack.io/openclaw-is-a-security-mess-jentic-wants-to-fix-it/)
> 
> 作者：Darryl K. Taft

[OpenClaw](https://thenewstack.io/openclaw-github-stars-security/) 改变了一切。这个开源[AI代理](https://thenewstack.io/ai-agents-and-their-life-cycle-what-you-should-know/)，在60天内从零GitHub星标跃升至247,000颗，终于兑现了Google和Apple多年来一直悬而未决但从未实现过的通用代理承诺。

都柏林初创公司[Jentic](https://jentic.com/)的首席执行官兼联合创始人Sean Blanchfield告诉《The New Stack》：“Apple曾展示过一个Siri的惊人版本，你可以让它做任何事情。那是一个非常棒的Siri版本，但从未发布。”

“一个开源项目揭开了它的面纱，现在大家都在争先恐后，”Blanchfield说，“Google或Apple本可以更容易做到，但他们没有这个胆量。”

## OpenClaw 留下的安全隐患

Blanchfield补充道：“要实现这一点并没有巨大的技术挑战。更多的是一种意愿。阻止他们的是这件事的风险状况。”

这种风险规避的结果是一个安全混乱。Blanchfield指出，研究人员已在公共互联网上发现超过40,000个暴露的OpenClaw实例。此外，他指出Cisco的AI安全团队记录了野外的数据泄露和提示注入。[一名工程师在不到两小时内劫持了一个代理](https://thenewstack.io/openclaw-moltbot-security-concerns/)。Blanchfield说，根本原因很简单。OpenClaw代理会泄露凭据。

“如果你说，‘你能帮我一下吗？’它就会说，‘好的，我有一个密码——给你，’”Blanchfield说，“如果有人给你发邮件说，‘我能借用你Stripe的密码吗？你再回邮件，’这就会让你无法真正使用这些东西。”

## 代理时代的权限防火墙

这就是Jentic试图通过Jentic Mini解决的问题，这是一款周三推出的免费、开源、自托管产品。Jentic Mini为开发者提供了一种轻量级的方式，可以在自己的环境中运行Jentic，同时为代理访问添加了一个实用的安全和控制层。Jentic为AI代理提供了一个权限防火墙。

Jentic Mini为开发者提供了一种轻量级的方式，可以在自己的环境中运行Jentic，同时为代理访问添加了一个实用的安全和控制层。

Jentic Mini专为运行OpenClaw及其他通用代理的开发者打造，它位于代理与其连接的API之间。该公司表示，它集中存储凭据，因此代理实际上永远看不到它们，强制执行细粒度权限，并提供一个“一键关闭”开关，可以立即关闭所有代理数据访问。

## 基于18个月的企业级工作经验打造

Blanchfield告诉《The New Stack》，该产品借鉴了18个月的企业级工作经验。Jentic的创立前提是，通用代理最终会出现，并需要这种访问控制层。

访问控制层是一个自托管的开源控制层，它位于AI代理（如OpenClaw）和它们调用的API之间，因此您可以赋予代理广泛的服务访问权限，而无需向它们提供您的凭据或无限权限。

因此，在等待通用代理到来的过程中，该公司为其推出代理的企业客户——金融机构、全球咨询公司、制造商——构建了平台，在这些领域，治理和安全是强制性的。然后，当OpenClaw在1月份风靡网络时，Blanchfield说，当人们开始注册Jentic的免费版，寻求安全保障时，他感到惊讶。

“我们意识到发生了什么，所以我们全力以赴，”他说，“我们已进入‘涡轮模式’，努力抓住这个时机。”

此次发布的核心是Jentic的API目录，目前已涵盖超过10,000个API。Blanchfield将其描述为API和工作流领域的[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)。Blanchfield说，这是一个由代理驱动的公共资源，这些代理花了18个月的时间在互联网上搜寻API定义，并内置了反馈循环，以便使用它的代理可以修正不准确的文档并贡献改进。

他说，前400个左右的API质量可靠，但越深入长尾部分，质量越难判断，代理会倾向于绕过缺陷并提交修复。

凭据问题仅仅是个开始。Jentic Mini还解决了Blanchfield所说的“权限鸿沟”——大多数API缺乏细粒度的访问控制。例如，Gmail不允许你授予代理起草邮件的权限，而不同时给予发送权限。Blanchfield解释说，这是一种“全有或全无”的权衡，使得人们根本不愿意连接他们的账户。他指出，Jentic Mini介入其中，强制执行有针对性的权限，这样代理可以起草但不能发送，可以阅读但不能删除。

Blanchfield说，该产品特意定位为补充而非竞争[Nvidia的NemoClaw](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/)等运行时安全工具，后者旨在锁定主机环境。

“有人在保护运行它的东西，有人在保护它如何连接事物，”他说，“我们没有看到其他人这样做。”

对于该公司来说，时机很好。Anthropic周一宣布，[Claude](https://thenewstack.io/claudes-free-plan-can-now-remember-you/)现在可以控制用户的Mac来完成任务。这是对OpenClaw病毒式传播势头的直接回应。[代理AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/)竞赛正在进行，而安全基础设施却落后了。

## SaaS的清算

Blanchfield，其背景包括在[DemonWare](https://www.demonware.net/)为[使命召唤](https://www.callofduty.com/)构建后端基础设施——他联合创立的公司被[动视暴雪收购](https://investor.activision.com/news-releases/news-release-details/activision-set-acquire-demonware)，而动视暴雪则[归微软所有](https://news.microsoft.com/source/2022/01/18/microsoft-to-acquire-activision-blizzard-to-bring-the-joy-and-community-of-gaming-to-everyone-across-every-device/)——表示他认为当前时刻比他几十年来在科技领域遇到的任何事情都更具意义。

他告诉《The New Stack》：“即使我在95-96年第一次接触互联网时，也没有现在这么兴奋。”“下一个软件时代将不再是为人类构建的。它将为代理而生，由代理构建。”

Blanchfield还表示，他看到一场行业尚未完全应对的转变正在到来。他指出，OpenClaw用户已经[取消了SaaS订阅](https://thenewstack.io/dawn-of-a-saaspocalypse/)。这是因为当代理没有合适的工具时，它就会自己构建一个。“我一直在取消各处的SaaS订阅，”他说，“这是一种不同类型的软件。它不是我们将来会再次购买的软件。”

Blanchfield还表示，他相信更直接的问题是，是否有足够的开发者信任这些代理，将它们连接到任何重要的事情上。Blanchfield认为，Jentic Mini的赌注是人们会说“是”——前提是有人先构建好安全网。

Jentic Mini为开发者提供了一种轻量级的方式，可以在自己的环境中运行Jentic，同时为代理访问添加了一个实用的安全和控制层。

Jentic Mini现已在[jentic.com/mini](http://jentic.com/mini)和GitHub上提供。企业产品仍是一个独立的商业产品。