<!-- 
# CDE：大机构更喜欢自托管而不是SaaS
Self-Hosted CDEs Preferred to SaaS in Large Orgs， Says Coder
Cloud Development Environments became popular as SaaS products. But Coder insists that enterprise devs are better off with self-hosted CDEs.
https://thenewstack.io/self-hosted-cdes-preferred-to-saas-in-large-orgs-says-coder/
https://cdn.thenewstack.io/media/2023/09/1b1ce81e-generic-ui--1024x684.jpg
Image via Coder
-->

随着云开发环境(CDE)作为 SaaS 产品变得流行，Coder 坚持认为企业开发人员更适合使用自托管 CDE。

译自 [Self-Hosted CDEs Preferred to SaaS in Large Orgs, Says Coder](https://thenewstack.io/self-hosted-cdes-preferred-to-saas-in-large-orgs-says-coder/) 。

Coder 公司的自托管“云开发环境”(CDE)刚刚发布了 2.0 版本，该版本包括新的 Dev Container 支持和与 JFrog 工件存储库的集成。为了讨论 [Coder.com](https://coder.com/) 的最新情况，我与联合创始人兼 CTO [Kyle Carberry](https://www.linkedin.com/in/kylecarbs/) 和新任 CEO [Robert Whiteley](https://www.linkedin.com/in/rwhiteley/) 进行了交谈。

当谈到 CDE 时，像 GitHub Codespaces 这样的 SaaS 产品似乎是这个市场的标准——换句话说，不是自托管的。所以我问了 Coder，为什么开发者会希望走自托管的路线。

Carberry 回答说，Codespaces “规定了某人编写软件的方式”，而 Coder 是一个“企业抽象，其中有最大的灵活性”。他补充说，在 Coder 上，你可以“带来任何你想要的东西，并制造开发环境”，使用你选择的编码工具。

## 为什么自托管 CDE 的愈发流行

我注意到，我最近[报道了 Daytona 的推出](https://thenewstack.io/codeanywhere-founders-take-on-github-codespaces-with-daytona/)，它也是一个自托管 CDE(尽管它选择的首字母缩略词是 SDE，代表“标准化开发环境”)。 Coder 的两位高管都不熟悉 Daytona，因为它太新了。 但 Whiteley 对为什么自托管 CDE(或 SDE)现在正在风靡，特别是在企业市场，有一个有趣的观点。

“我认为我们正在看到云开发环境或 CDE 的第二代。 我们将看到更多自托管或可部署的东西。 所以 Daytona 就是一个好例子，是一个正在兴起的公司。 如果一些仅 SaaS 版本实际上最终改变方向并有一个可部署版本，我也不会感到惊讶。“

这是一个很好的观点; 事实上，在我的 Daytona 文章的结尾，我怀疑 GitHub Codespaces 是否也会提供自托管。

![](https://cdn.thenewstack.io/media/2023/09/aa00d14e-jfrog-severity-banner-scaled.jpg)
*Coder 和 Jfrog*

“客户表达的主要是，看，这是一个早期采用者市场，”Whiteley 谈到 CDE 时说。 “早期采用者倾向于非常老练，他们需要能够控制环境，扭转和调整 nerd 旋钮，可以这么说。 所以我认为 SaaS 会夺走这一点。 顺便说一句，我是一个巨大的 SaaS 粉丝 - 我认为它将在 12-18 个月内成为这个市场的主流部分。“

他这里指的是企业中的 CDE，因为在消费者市场(个人开发者)中，像 GitHub Codespaces 和 Replit 这样的产品已经比 Coder 更受欢迎。 但 Whiteley 的意思是“早期采用者”公司更有兴趣采用自托管 CDE。

## 安全是自托管的第一原因(但有新出现的原因)

这引出了一个问题：目前使用 Coder 的公司是什么类型？对他们在选择自托管 CDE 时，安全是否是首要考虑的因素？

Whiteley 确认安全性“仍然是”最大的因素，尤其是对于大型企业。

“所以云开发环境的价值在于，我本质上已经将开发从本地工作站转移到某种云托管的工作空间。 所以固有地，我的开发现在是'防火墙后面'，我的源代码不在内部或笔记本电脑上。 我可以实施访问控制，我对开发人员的工作有更好的发现能力[...]。“

然而，他指出自托管 CDE 还有其他新兴用例，而不仅仅是安全。

“CDE 的一个问题是，在某些情况下，它们确实需要开发人员改变行为，”他解释说。 “以前是完全远程的。 现在解决方案的一部分可以是远程的，也许你的 IDE 是远程的，但所有实际的编码实践现在都集中在云中。”

他还说，“如果你使用 AI 或 ML，你可能已经在云中编写代码了，因为你需要访问奇异的 GPU 或你有一些大型数据集要训练模型。” 所以，基于 AI 的开发人员用例正在激励公司转向 CDE。

根据 Carberry 的说法，大公司也选择自托管 CDE，因为它更具成本效益。 他举的一个例子是，它的一些客户已经使用 Kubernetes，所以他们可以将 Coder 放入该环境中，Carberry 说这比支付 SaaS 提供商托管 CDE 要便宜得多。

“这也是我们实际上不规定任何基础设施的原因之一，”Carberry 补充道。 “我们的一些客户非常高兴使用虚拟机。 通过 Coder，他们为每个开发者预配一个 VM，当他们不使用它时，它会自动关闭。 我们的一些客户使用 Kubernetes，其中一些人[...]运行 OpenShift，然后可能在其中开发。 所以它有点像杂乱无章，我会说，但最大的教训是我们不能真正规定任何东西[...]特别是对大型企业。”

## 开发容器

从开发者的角度来看，关于 Coder 2.0 最有趣的事情可能是它对开发容器的增强支持，这是微软开发的一个开放标准，“允许你使用容器作为功能齐全的开发环境”。

![](https://cdn.thenewstack.io/media/2023/09/fb826149-dev-containers-scaled.jpg)

Carberry 说，以前 Coder 支持开发容器作为“二等公民”，但是在 2.0 中，该产品为开发容器提供了“Envbuilder”，这是基于微软开发容器规范的 Coder 开源项目。 “Envbuilder 使用户能够控制其开发环境，而不影响基础设施或需要 DevOps 和平台团队的工作，”Coder 在宣布 2.0 版本时表示。

Whiteley补充说，开发容器是一个“新兴规范”，“我们在某种程度上是被客户拉入的 - 我们一些最大的客户正在使用开发容器，希望它成为他们开发标准的一部分。” 但他说，即使开发容器规范最终不起作用，Coder也不依赖它(它只是一个选项)，因此它的产品不会受到影响。