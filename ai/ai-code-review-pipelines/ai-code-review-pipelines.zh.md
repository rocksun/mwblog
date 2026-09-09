**问问两位经验丰富的工程师**，他们是如何处理审查队列中海量的AI生成代码的，你一定会得到两个截然不同的答案。

这场辩论远未平息。在 [9月29日星期二](https://thenewstack.io/webinar/human-review-vs-verified-pipelines-what-catches-bugs-in-the-age-of-ai-code/)，两位行业领袖将参加一场直播活动，共同探讨应对之策。

[Octopus Deploy](https://octopus.com/) 的首席开发者倡导者 [John Bristowe](http://linkedin.com/in/jbristowe?originalSubdomain=au)，将与 *DevOps Toolkit* 背后的平台工程权威 [Viktor Farcic](https://www.linkedin.com/in/viktorfarcic/) 一起，进行这场名为“[人类审查 vs 验证流水线：AI代码时代如何捕获缺陷](https://thenewstack.io/webinar/human-review-vs-verified-pipelines-what-catches-bugs-in-the-age-of-ai-code/)”的直播对话。

立即注册本次网络研讨会

您已成功注册本次网络研讨会。

**事实如下：** 开发者们已经大规模采用了AI。根据 [2026年 DORA 报告](https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development)显示，90%的开发者现在在工作中会使用AI。结果如何？与AI普及前相比，开发者合并的拉取请求（pull requests）增加了98%。

然而，所有这些由AI生成的代码正留下一堆烂摊子。每位开发者的缺陷数量增加了54%，一项针对10,000名开发者的分析发现，每个拉取请求中的事件增加了惊人的243%。[Octopus Deploy 自己的 AI Pulse 报告](https://octopus.com/publications/ai-pulse-report)发现，虽然AI的使用加快了代码编写速度，但它可能会“降低整体性能”，因为编程代理编写的大规模代码更新，人类难以完全理解。

问题的一部分在于，开发者采用自动代码生成的速度，远快于他们采用自动化代码审查的速度，这有效地将人类瓶颈向下游移动，但并没有完全消除它。而AI代码审查可能存在与编程代理相同的缺陷。

John Bristowe 认为，代码审查已经 [悄然变得不过是一场表演](https://octopus.com/blog/code-review-is-theater-now)。没有任何人类评审员能快速审计一个由代理创建的40,000行代码的拉取请求，因为他们并未参与生成这些代码的逻辑过程，也不可能真正理解它可能改变的一切。

John Bristowe 建议如何处理？将质量关卡从人类的办公桌转移到交付流水线本身。这是否意味着更多的AI？不一定。这位开发者倡导者认为，将稳健的“政策即代码”（policy-as-code）规则构建到部署标准中，可以只标记那些违反这些政策的内容。人类可以处理这些例外情况，而不必假装他们正在“审查”整个软件包。

可以预见，Viktor Farcic 将会向 John Bristowe 施压，探讨“政策即代码”设置在多大程度上能真正吸收判断力，以及我们是否只是在软件开发中创造了另一个问责制黑洞。对话还将探讨 [初级工程师](https://thenewstack.io/ai-junior-developer-hiring/) 的困境，他们再也无法期待加入一个由人类编写代码、并由其他人类进行审查和讨论的团队了。

辩论将于 [9月29日星期二下午 2:30（东部时间）/ 上午 11:30（太平洋时间）](https://thenewstack.io/webinar/human-review-vs-verified-pipelines-what-catches-bugs-in-the-age-of-ai-code/) 开始。活动免费参加，与会者将获得一份基于 Octopus Deploy 的 AI Pulse 数据构建的配套资源，直播参与者可立即获取。[*立即注册*](https://thenewstack.io/webinar/human-review-vs-verified-pipelines-what-catches-bugs-in-the-age-of-ai-code/)。

**您将收获：**

* 为什么AI生成的代码打破了代码审查赖以生存的假设，以及为什么增加审查并不是解决之道
* 为什么使用AI来审查AI自己的代码并不能填补漏洞（相同的训练数据，相同的盲点）
* 如何构建一条针对定义好的规则集验证每一次部署的流水线，无论代码是谁或什么所写
* 代码审查在何处仍然有价值，以及在何处需要为流水线让路