<!--
title: Vercel收购Better Auth，为AI智能体赋予独立身份
cover: https://cdn.thenewstack.io/media/2026/07/b2b71cc7-milhad-py4ctdtm55s-unsplash-scaled.jpg
summary: Vercel正式收购开源认证框架Better Auth，旨在解决AI智能体目前普遍存在的身份管理缺陷。通过集成Agent Auth协议，Vercel计划为智能体赋予独立、可控且具备权限隔离的身份，从而提升AI应用的安全性和精细化管理水平。
-->

Vercel正式收购开源认证框架Better Auth，旨在解决AI智能体目前普遍存在的身份管理缺陷。通过集成Agent Auth协议，Vercel计划为智能体赋予独立、可控且具备权限隔离的身份，从而提升AI应用的安全性和精细化管理水平。

> 译自：[Vercel acquires Better Auth to give AI agents their own identity](https://thenewstack.io/vercel-acquires-better-auth/)
> 
> 作者：Paul Sawers

AI智能体正越来越多地代表人类执行任务，例如发起拉取请求、审查代码、创建部署、查询内部系统或更新业务应用程序。然而，目前的现状是，它们在执行这些操作时通常佩戴着与部署它们的人相同的“工牌”——智能体所接触的每一项服务看到的都是该用户，而不是智能体本身。此外，如果没有切断所有人的访问权限，就无法清晰地限制单个智能体的操作权限或将其关闭。

正因如此，Vercel（Next.js Web框架及其相关部署平台的幕后公司）正在收购Better Auth。Better Auth的[开源TypeScript认证框架](https://github.com/better-auth)每周在npm上的下载量约为470万次。

此次交易完成后，Better Auth的创建者Bereket Engida及其核心团队将加入Vercel，继续致力于该框架的开发，并更广泛地研究智能体身份认证。

## 借用登录凭证的智能体

Better Auth以其开源的TypeScript认证框架而闻名，开发人员使用它为跨多个框架的Web应用程序添加登录、会话、用户管理和权限控制功能。然而，在Vercel接洽时，这家初创公司已经开始探索身份认证之外的领域。

事实上，Better Auth已经开始开发[Agent Auth](https://agentauthprotocol.com/)，这是一个旨在赋予AI智能体独立身份的开放协议。该协议具有范围限定、委派和可撤销的权限，这些权限与部署智能体的人员的权限保持独立。

在拥抱智能体身份方面，Better Auth并不孤单。Anthropic[最近推出了Claude Tag](https://thenewstack.io/anthropic-claude-tag-slack/)，使Claude能够在Slack中拥有自己的身份，并使用其关联的账户，而不是通过调用它的人的身份来执行操作。虽然实现方式不同，但核心理念相似：将AI智能体视为具有自身身份的独立主体，而不是所调用用户的延伸。

> “我们是一个小团队；智能体身份问题规模巨大且发展迅速。”

在[周二的博客文章](https://better-auth.com/blog/better-auth-joins-vercel)中解释加入Vercel的决定时，Bereket Engida写道，解决这一问题的难度已经超出了一个小团队单打独斗所能应对的范围。

“我们是一个小团队；智能体身份问题规模巨大且发展迅速，”Bereket Engida指出。“借助Vercel的基础设施、分发能力、社区和产品覆盖面，我们可以将这些想法以比我们单干大得多的规模带给开发者。”

在周二发布的另一篇[博客文章](https://vercel.com/blog/vercel-acquires-better-auth)中，Vercel首席执行官Guillermo Rauch表达了类似的观点，他认为现有的身份系统是为人类而非自主软件构建的。

“当智能体代表你行事时，它会在你的身份和访问权限下运行，因此它接触到的每一个服务看到的都是你，而不是智能体，”Guillermo Rauch写道。“目前没有一种简洁的方法来限制任何单个智能体或子智能体能做什么，或者在不切断其他所有人访问权限的情况下单独关闭某一个智能体。”

这些工作现在将融入[Vercel Connect](https://vercel.com/blog/introducing-vercel-connect)和[Eve](https://thenewstack.io/vercel-launches-eve-an-open-source-framework-that-treats-agents-as-directories/)，这是该公司用于连接AI智能体与外部服务的产品。

> “当智能体代表你行事时，它会在你的身份和访问权限下运行，因此它接触到的每一个服务看到的都是你，而不是智能体。目前没有一种简洁的方法来限制任何单个智能体或子智能体能做什么，或者在不切断其他所有人访问权限的情况下单独关闭某一个智能体。”

## 加入Vercel之路

![Vercel CEO Guillermo Rauch with Better Auth CEO Bereket Engida](https://cdn.thenewstack.io/media/2026/07/3f5b2397-phb_2919-edit-2-1024x683.avif)

*Vercel首席执行官Guillermo Rauch与Better Auth首席执行官Bereket Engida*

Better Auth的诞生源于Bereket Engida在构建一个不相关的开源分析项目时遇到的问题。由于需要支持具有不同权限级别的团队账户，他发现现有的认证库无法满足他的需求，于是花了大约七个月的时间构建了自己的框架无关替代方案，并于2024年9月发布了第一个版本。

该项目发展迅速，Better Auth在经历了Y Combinator (YC) 加速器计划后，于2025年夏季[筹集了500万美元种子轮资金](https://better-auth.com/blog/seed-round)。那年晚些时候，在维护者得出两个项目目标一致的结论后，[它接管了Auth.js](https://better-auth.com/blog/authjs-joins-better-auth)（前身为NextAuth.js）的管理权。

Guillermo Rauch强调，此次收购不会改变该框架未来的开源状态，Better Auth将继续根据MIT许可证免费提供。

“团队将继续以相同的开源贡献模式、社区治理和跨生态系统的框架支持来引领开发，”他写道。