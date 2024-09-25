
<!--
title: 人工智能如何改变应用程序的身份验证和授权
cover: https://cdn.thenewstack.io/media/2024/09/005ccb3c-ai-changes-app-authentication-authorization.jpg
-->

人工智能为应用程序体验带来了新的模式，为开发人员在身份验证和授权方面带来了新的益处和挑战。

> 译自 [How AI Changes App Authentication and Authorization](https://thenewstack.io/how-ai-changes-app-authentication-and-authorization/)，作者 Shiv Ramji。

人工智能无处不在。您无法在没有遇到应用程序或增强型在线服务的情况下进行任何操作。根据 IBM 的数据，[76% 的公司](https://connect.comptia.org/blog/artificial-intelligence-statistics-facts#:~:text=Taking%20part%20in%20machine%20learning,new%20AI%20and%20automation%20tools.)正在使用或探索人工智能在其业务中的应用，而 Okta 委托 SD Times 进行的研究发现，[97% 的产品工程团队](https://www.okta.com/sites/default/files/2023-11/how_dev_teams_purchase_SaaS_report_20231103.pdf)预计到 2024 年底将在开发中使用人工智能工具。

[人工智能](https://thenewstack.io/ai/)带来了前所未有的生产力提升。然而，它也导致了新的网络攻击，损害了企业和人们的数据。
随着人工智能越来越深入地融入我们的日常生活，我预测人工智能的未来将是一个智能代理代表我们运作的数字世界。它们为我们预订酒店或航班，购买音乐会门票或出售股票市场股票。由于这些情况需要使用个人数据和信息；人们必须信任人工智能的身份。

标准身份挑战现在将具有新的维度。开发人员需要在为用户提供不同级别的访问和控制以及代表他们运行的人工智能代理之间进行导航。这种[应用程序安全](https://roadmap.sh/cyber-security)的额外复杂性对于内部构建身份解决方案的开发人员来说尤其困难。

## 人工智能给传统应用程序带来了新的威胁

人工智能现在有能力增强传统的应用程序安全威胁。例如，聊天机器人和令人信服的语音深度伪造正在被用于社会工程攻击；攻击者正在使用人工智能来快速检测和利用应用程序中的漏洞。

借助人工智能，不法分子可以更轻松地扩展其运营，而诸如网络钓鱼之类的活动不再是手动、昂贵的任务。研究人员甚至发现，深度学习语言模型可以帮助编写[更有效的网络钓鱼电子邮件](https://www.wired.com/story/ai-phishing-emails/)，比人类更有效。

随着这些基于身份的攻击变得越来越危险，开发人员必须确保其应用程序[授权](https://thenewstack.io/api-security-is-authorization-the-biggest-threat/)和[身份验证](https://thenewstack.io/73-of-organizations-dont-enforce-multifactor-authentication/)是安全的，并且只有合法用户才能成功访问其帐户。

## 开发人员是新的机器人战斗者

面对这些不断变化的应用程序安全威胁，开发人员必须与试图破坏客户身份的不法分子和机器人作斗争。由于机器人占所有互联网流量的近[50%](https://www.imperva.com/resources/resource-library/reports/2024-bad-bot-report/)，开发人员需要在使恶意行为者更难滥用注册和登录以及提供能够提高最终用户采用的数字体验之间取得平衡。

机器人已经变得非常擅长解决简单的基于图像的 CAPTCHA——通常比人类更快、更准确地解决它们。在这种情况下，[人工智能驱动的工具](https://www.okta.com/products/okta-ai/)可以帮助开发人员充当有效的防御机制，分析攻击模式并检测机器人活动，几乎不会给客户带来任何摩擦。这些工具可以分析与应用程序访问活动相关的各种信号，并将它们与历史数据进行比较，以查找常见模式。如果检测到可疑活动，将要求额外的身份验证因素来验证用户的身份。

## 人工智能驱动的应用程序的新漏洞

作为软件开发的新领域，人工智能应用程序面临着与传统应用程序类似的安全问题，例如未经授权访问信息，但恶意行为者使用的是新技术。

对于人工智能驱动的应用程序，应用程序架构的经典构建块，例如前端、后端和数据库，被新的元素所取代，例如[大型语言模型 (LLM)](https://thenewstack.io/llm/)和向量[数据库](https://thenewstack.io/databases/)。这给传统的应用程序安全带来了新的挑战——提示注入、数据中毒和数据泄露等等。
开放式全球应用程序安全项目 (OWASP) 已经编制了一份[基于 LLM 的应用程序的十大漏洞](https://genai.owasp.org/llm-top-10/) 列表。其中许多与身份相关，例如敏感信息泄露（当应用程序由于缺乏适当的授权或过滤过程而泄露敏感信息时）和过度代理（当 AI 代理被委托根据输入提示或 LLM 的输出执行操作时，而没有采取适当的预防措施）。

对于应用程序开发来说，这是一个全新的领域。它为传统的身份挑战带来了新的维度，例如确保只有授权用户才能访问特定资源，以及能够验证 AI 代理的身份以执行敏感操作，这需要仔细的授权过程。

## 有用的创新正在进行中

身份是 AI 时代任何应用程序的基础，但开发人员很容易将时间花在内部构建和维护身份上。幸运的是，针对创新的研究正在进行中，以帮助您构建安全的 AI 应用程序。[Auth0Lab](https://lab.auth0.com/) 团队已经开始尝试通过 AI 和细粒度身份验证 ([FGA](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/)) 以及内容真实性等机会来保护基于 AI 的应用程序。

在 Okta，我们扩展了 Auth0 免费计划并增强了付费层级——免费提供多因素身份验证 (MFA) 和无密码等身份工具——并推出了 [Okta AI](https://www.okta.com/products/okta-ai/)，使身份易于实施和扩展以满足任何用例。
