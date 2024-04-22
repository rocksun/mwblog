
<!--
title: 为何PHP使用率大降40%？
cover: https://cdn.thenewstack.io/media/2024/04/7418de50-getty-images-sff7fr7g7fo-unsplash.jpg
-->

PHP 的受欢迎程度大幅下降，据其联合创始人 Matt Mullenweg 所说，这与 WordPress 成为“JavaScript 优先”相吻合。

> 译自 [Why PHP Usage Has Declined by 40% in Just Over 2 Years](https://thenewstack.io/why-php-usage-has-declined-by-40-in-just-over-2-years/)，作者 Richard MacManus。

[TIOBE 指数](https://www.tiobe.com/tiobe-index/) 的最新月度更新问道，“PHP 是否正在失去其魅力？”在 4 月份，TIOBE 的编程语言指数将 PHP 排在第 17 位，“这是其历史最低排名”。

不仅 TIOBE 显示 PHP 的受欢迎程度正在下降。在年度 Stack Overflow 开发者调查中，PHP 已从 2018 年的 30.7%（即使用 PHP 的受访者百分比）下降到 2023 年的 18.58%。[JetBrains 开发者生态系统调查](https://www.jetbrains.com/lp/devecosystem-2023/languages/#proglang7years__2) 显示了类似的下降，从 2017 年的 30% 下降到 2023 年的 18%。这一点尤其值得注意，因为 JetBrains（以及 WordPress 托管公司 Automattic）是 PHP 的最大赞助商之一，我将在稍后介绍。

![](https://cdn.thenewstack.io/media/2024/04/e749a5be-jetbrains_dev_php24-1024x886.png)

这种下降在 [BuiltWith](https://trends.builtwith.com/framework/PHP) 中表现得最为明显，其中 PHP 的受欢迎程度增长曲线在 2020 年底开始下降。

![](https://cdn.thenewstack.io/media/2024/04/e3e39ac0-builtwith_php24-1024x890.png)

上一次 [我在 2021 年 11 月写 PHP](https://thenewstack.io/php-has-survived-for-26-years-because-it-keeps-evolving/) 时，红线（轮询排名前 100 万的网站）仍高于 30,000。现在，两年零三个月后，它接近 15,000 的标记——尽管 BuiltWith 在我撰写本文时引用的实际数字是 18.19%。18% 的标记与 Stack Overflow 和 JetBrains 调查更一致，因此我们可以自信地说，PHP 在开发者中的受欢迎程度已从约 30% 下降到现在的 18%。**在短短两年内下降了 40%**。

那么是什么原因呢？在过去几年中发生了什么变化，导致 PHP 成为 Web 编程语言中的落后者？

## WordPress 现在“JavaScript 优先”

PHP 衰落的最大原因可能是 WordPress（迄今为止最流行的内容管理系统）正在远离 PHP 转向 JavaScript。WordPress 的联合创始人兼 Automattic 首席执行官 Matt Mullenweg 在上个月在台湾台北举行的 [WordCamp Asia 2024](https://www.youtube.com/watch?v=EOF70YJLC5U) 上表示了这一点。

“我认为 WordPress 中大部分新代码现在都是 JavaScript，而且已经有一段时间了，”他在回答观众提问时说。“因此，从许多方面来说，你可以争辩说，根据大部分活动发生的情况，Gutenberg 已使我们成为一个 JavaScript 优先的项目。”

是的，你没看错：Matt Mullenweg 说 WordPress 现在是一个“JavaScript 优先的项目”。该公司有争议的新基于块的用户界面 Gutenberg 是造成这种情况的主要原因。不过，他承认，从 PHP 转向 JavaScript “并不容易”。

![](https://cdn.thenewstack.io/media/2024/04/b7196c53-wcasia_mullenweg-1024x585.jpg)

这并不是说 WordPress 仍然不严重依赖 PHP。我应该知道，因为我正在将这篇文章输入 WordPress 中，网址以“/wp-admin/post-new.php”结尾。但它显然不再是 WordPress 的未来。

Mullenweg 还谈到了他希望在 WordPress 中看到的进一步改进——令人惊讶的是，他现在至少通过 JavaScript 镜头来查看其中的一些改进。例如，PHP 是一种服务器端脚本语言（这意味着代码通常在 Web 服务器上处理），但 Mullenweg 希望 WordPress 使用 JavaScript 在客户端执行更多操作。

“天哪，我觉得我们应该在客户端执行更多处理，”他沉思道，“甚至可能在编辑某些内容时将其中一些 [处理推送到客户端]。也许在浏览器中使用 JavaScript（现在拥有令人难以置信的虚拟机和真正快速的处理器）比在服务器端执行此操作更快。”

在演讲的最后，有人问 Mullenweg 他对 Gutenberg 项目以及开发人员在为其做出贡献时遇到的困难有何感想。特别是，提出这个问题的开发人员希望“降低 Gutenberg 中的抽象级别”。

“我认为开发，老实说，是你必须学习的东西，”Mullenweg 回答道。“我认为 Gutenberg 进行开发的方式和 JavaScript 优先 [方法] 是大多数 Web 开发的未来。顺便说一句，这对我来说也很陌生——这不是我最初学到的。我们可能会简化一些抽象，但总体而言，我会深入研究它。”

他补充说，Gutenberg——以及大概向 JavaScript 的转变——尚未完成。“当我们启动 Gutenberg 时，我们说这将是一个为期 10 年的项目，”他说，“所以感觉我们已经完成了 60% 到 70% 的工作。”

## 同时，在 PHP 基金会……

因此，WordPress 项目（PHP 仍然在网络上流行的最大原因）正在向 JavaScript 世界迈进。这几乎肯定会阻止年轻开发者采用 PHP，并迫使其他开发者（例如那些致力于 WordPress 客户的开发者）远离 PHP 转向 JavaScript。

然而，仍然有相当多的开发者在使用 PHP——两项大型开发者调查中，18% 的比例并非微不足道。这就是 PHP 基金会发挥作用的地方。

2021 年 11 月，我受邀撰写有关 PHP 的文章，因为当月成立了一个新的[非营利基金会](https://thenewstack.io/php-gets-a-foundation-to-work-on-php-core/)，负责承担 PHP 的看护职责。PHP 基金会由 [JetBrains](https://blog.jetbrains.com/phpstorm/2021/11/the-php-foundation/) 牵头的公司联盟创建，其中包括 Automattic、Zend、Laravel、Acquia（Drupal 的保管人）等。JetBrains 的工程师 [Roman Pronskiy](https://twitter.com/pronskiy) 承担了该项目的责任——他目前在基金会网站上[被列为](https://thephp.foundation/structure/)“运营经理”。

在 [2 月份的 Laravel 会议](https://www.youtube.com/watch?v=XE4g1Tl6RQw) 上，Pronskiy 主要关注技术问题，但他确实承认“解决 PHP 的公众形象”是“PHP 基金会最艰巨的任务”。虽然他没有具体说明是什么导致了公众形象下降，但我请你参考 Matt Mullenweg 关于 WordPress 现在为何“JavaScript 优先”的评论。无论如何，Pronskiy 很快转向了 PHP 项目中正在进行的积极开发，其中包括十名受薪开发者。

![](https://cdn.thenewstack.io/media/2024/04/d6270c3e-who-pays-for-php-1024x581.jpg)

总之，很容易将 2024 年的 PHP 视为网络开发中被遗忘的孩子，而 JavaScript 是班上最受欢迎的孩子。不幸的是，对于 PHP 来说，其使用率的下降不太可能很快停止——为什么会出现这种情况，当 WordPress 开发者忙于适应新的 JavaScript 范例时？但至少 PHP 基金会正在积极开发。
