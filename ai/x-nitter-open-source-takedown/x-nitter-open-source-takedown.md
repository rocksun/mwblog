<!--
title: X向Nitter发送停止令，并将矛头指向其源代码
cover: https://cdn.thenewstack.io/media/2026/08/2c542495-steve-a-johnson-zcl4fqhg-yg-unsplash-scaled.jpg
summary: Elon Musk旗下的X平台向开源项目Nitter发送律师函，不仅要求其停止服务，还试图封杀其源代码仓库。此举引发了平台控制权与开源代码合法性的争议，类似于此前YouTube-dl遭遇的法律挑战，凸显了大型平台对开源生态施加法律压力的趋势。
-->

Elon Musk旗下的X平台向开源项目Nitter发送律师函，不仅要求其停止服务，还试图封杀其源代码仓库。此举引发了平台控制权与开源代码合法性的争议，类似于此前YouTube-dl遭遇的法律挑战，凸显了大型平台对开源生态施加法律压力的趋势。

> 译自：[X sent Nitter a cease-and-desist. Then it went after the source code.](https://thenewstack.io/x-nitter-open-source-takedown/)
> 
> 作者：Amanda Caswell

**当Elon Musk的X发送停止侵权信件**，要求Nitter（社交媒体平台的一个开源替代前端）永久关闭其实例并移除该项目的源代码仓库时，它实际上是在针对代码本身。

虽然Nitter.net是该项目的主要公共实例，但其他开发者可以运行自己的版本，因为该代码是开源的。因此，让Nitter.net下线并不能真正消除Nitter，因为它的代码可以被分叉（fork）并用于运行独立实例，包括诸如 [XCancel](https://github.com/zedeus/nitter/wiki/Instances) 之类的服务。X对于仓库的需求走得更远。

## 开源与平台控制的碰撞

开源赋予了开发者对Nitter代码的控制权，但并未赋予其对该代码所依赖平台的控制权。X仍然控制着对其服务的访问，其最新举措表明这种控制如何超越了单纯修改API的范畴。

> 开源赋予了开发者对Nitter代码的控制权，但并未赋予其对该代码所依赖平台的控制权。

Nitter过去允许人们在没有账号的情况下阅读X的公共帖子，但在X关闭了该项目所依赖的访客访问权限，导致Nitter.net下线后，这一功能在2024年失效。根据 [该项目的GitHub仓库](https://github.com/zedeus/nitter)，Nitter后来通过使用真实的X账号来访问帖子，从而找到了回归的方法。

这让Nitter重新上线，但也意味着它必须依赖X账号才能保持运行。X控制着这些账号，并可能随时更改围绕它们的规则。这并不一定让单纯下载或分叉Nitter代码的人处于同样的境地，因为仅这样做并不意味着他们已经同意了X的条款。

## X的停止侵权指控

这些变化现在处于X法律诉讼的中心。根据最初由 *TechCrunch* [报道](https://techcrunch.com/2026/08/25/x-sends-cease-and-desist-to-open-source-project-nitter-over-alleged-scraping/) 的停止侵权信件，X称Nitter通过抓取数据以及访问账号和会话令牌违反了其规则，并指控该项目“非法使用和规避”其API。

X的律师还引用了《兰哈姆法案》（Lanham Act）和 [德克萨斯州刑法典第33.02条](https://tcss.legis.texas.gov/resources/PE/htm/PE.33.htm)，该条款涉及在未经所有者“有效同意”的情况下访问计算机系统。但违反平台的规则并不意味着同时也触犯了法律。

> 违反平台的规则并不意味着同时也触犯了法律。

## GitHub的代码移除标准

根据 [《数字千年版权法案》（DMCA）第1201条](https://www.copyright.gov/policy/1201/)，如果软件被用于绕过保护版权材料访问的技术，即使软件本身不包含该材料，也可以成为目标。

仅仅声称软件绕过了技术限制，不足以让仓库从GitHub上被移除。根据 [GitHub关于提交规避声明的指南](https://docs.github.com/en/site-policy/content-removal-policies/submitting-content-removal-requests)，对于第1201条的投诉，公司必须指明受保护的版权材料，并解释代码是如何规避控制对其访问的技术的。

据报道，X称Nitter绕过了其API限制以访问账号和会话令牌。问题在于这些限制是否按照第1201条的要求保护了版权材料。

## YouTube-dl的先例

类似的问题出现在2020年，当时在收到美国唱片业协会（Recording Industry Association of America）根据第1201条提出的投诉后，GitHub移除了开源项目 [YouTube-dl](https://github.blog/news-insights/policy-news-and-insights/standing-up-for-developers-youtube-dl-is-back/)。GitHub后来恢复了该仓库，并改变了处理此类投诉的方式，即在规避声明不明确的情况下，在移除代码前增加技术和法律审查。

目前，该仓库仍保留在GitHub上，已归档且为只读状态。尽管Nitter的开发者已不再维护该项目，但代码仍然可以被查看和分叉。