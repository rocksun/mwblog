
<!--
title: WP Engine推出AI驱动的WordPress网站搜索
cover: https://cdn.thenewstack.io/media/2024/03/9fcdece1-man-7761204_1920.jpg
-->

WP Engine 的一个测试工具允许用户在几毫秒内对使用 WordPress 构建的网站执行语义搜索。

> 译自 [WP Engine Introduces AI-Powered Search for WordPress Sites](https://thenewstack.io/wp-engine-introduces-ai-powered-search-for-wordpress-sites/)，作者 Loraine Lawson。

WP Engine 正在推出 AI 驱动的搜索，该搜索将支持语义搜索，并为使用 WordPress 平台创建的网站提供更快的搜索结果。专有工具在本周的 WP Engine 虚拟 [De{Code} 会议](https://wpengine.co.uk/blog/decode-registration-open/) 中向开发者和其他 WordPress 用户展示。

AI 及其将如何改变网站是此次 De{Code} 的一个重要讨论点，主题演讲专门针对该主题。该公司还推出了其 [智能搜索](https://wpengine.com/smart-search/) 和 [AI 驱动的混合搜索](https://wpengine.com/support/ai-powered-hybrid-search-for-smart-search/)，承诺为使用该平台创建的网站的用户创造更多“类似于 ChatGPT”的体验，WP Engine 的产品经理 [Luke Patterson](https://www.linkedin.com/in/lukepatterson59/) 说。

## 网站搜索作为一项技术挑战

[搜索是一项困难的技术挑战](https://thenewstack.io/how-to-build-site-search-with-astro-qwik-and-fuse-js/)”，Patterson 告诉与会者。“有很多非常聪明的人在任何时候都在研究搜索，但仍然难以做得正确。这意味着，那些能够做得正确的人，真正为他们的客户带来了巨大的好处，而他们的客户又能够将这些好处传递给他们的用户，在这种情况下，用户是访问你的 WordPress 网站的人。”

他补充说，越来越多的用户期望在搜索中获得更类似于 GPT 的体验。而且风险很高：谷歌统计数据显示，82% 的客户会避开他们在其中遇到搜索困难的网站。这出于很多原因而存在问题，其中最主要的原因是使用搜索的用户是“高意向访问者”——他们实际上输入了他们想要的确切内容，Patterson 解释说。

![Luke Patterson 展示 Google 幻灯片的屏幕截图](https://cdn.thenewstack.io/media/2024/03/7d5b5ef4-lukepattersondecode.jpg)

*WP Engine 的产品经理 Luke Patterson 展示了一张关于网站搜索的幻灯片。*

“他们通过将意图逐字逐句地输入搜索栏来传达他们的意图，如果它什么都没有返回，可能是因为拼写错误或 ACF 未被索引，或者无论什么原因，他们都会反弹，他们不会购买，而且他们可能永远不会回来，”他说。

## 利用高级自定义字段进行智能搜索

ACF 代表 [高级自定义字段](https://www.youtube.com/watch?v=eMCOE9x5mCc)，适用于 CMS。有 [解决方案](https://www.advancedcustomfields.com/) 和插件，允许网站创建者定义和添加超出 WordPress 提供的基本字段的自定义字段，但 Patterson 谈论的是默认的 WordPress 搜索，他承认它不能很好地处理这些搜索期望，并且不允许按日期或标签过滤。他补充说，为了创造增强的搜索体验，智能搜索必须与 ACF 很好地配合。就目前而言，索引 ACF 是“WordPress 中搜索出了名的难题”。

“我们所做的是索引和映射你的 ACF 字段，开箱即用，点击一个按钮，无需自定义映射，无需简码，无需任何代码，你只需在智能搜索中默认索引所有 ACF 和所有自定义帖子类型，”他说。“现在，你可以根据需要设置数据格式。它始终会被索引以进行搜索。它始终会实时更新。”

他还说，智能搜索还使网站搜索变得更快，因为它将索引和搜索从 WordPress 卸载到专用搜索服务器，而不是访问你的 WordPress [MySQL 数据库](https://thenewstack.io/a-cheat-sheet-to-database-access-control-mysql/)。

它还支持“模糊性”，这意味着你可以调整参数以容忍术语中一定程度的拼写错误。他演示了在电影网站上搜索 Mandalorian，但将其拼写错误为 Madelorean——与正确拼写相差两个字母。该网站仍然能够找到这部电影。它还支持通过搜索出现在 Mandalorian 中的演员来查找电影。

“那个繁重的搜索索引不仅仅停留在你的 WordPress 服务器上，减慢了它的速度，”他说。“我们实际上看到了这种现象带来的惊人性能提升。”一位客户每月进行大约 1000 万次搜索，他们的平均请求搜索查询响应时间约为 50 毫秒，Patterson 说。

将搜索从 WordPress 数据库中卸载，并自动索引 ACF 字段中的所有自定义帖子类型——我们认为这是我们在此处 […] 独一无二的地方；再次希望以 WordPress 开发人员工作的方式工作，”他说。“这是我们认为自己为 WordPress 生态系统做出贡献的方式之一，通过帮助以我们希望的真正令人愉快的方式解决这个真正棘手的问题。”

## 智能搜索允许推理、语义搜索

他解释说，人工智能驱动的混合搜索获取网站索引并在其上运行机器学习，将索引转换为可使用自然语言进行搜索的向量数据库。

“对于人工智能驱动的搜索，我们对搜索索引所做的事情是，在幕后，我们将运行一个 [机器学习模型](https://thenewstack.io/machine-learning-models-to-predict-the-next-stranger-things/)，并将索引转换为称为 [向量数据库](https://thenewstack.io/vector-databases-where-geometry-meets-machine-learning/) 的东西，”他说。“因此，在不深入了解向量技术的情况下，最终结果是，在运行机器学习并获得向量数据库后，你可以针对该向量数据库运行自然语言搜索。”

![WP Engine 智能搜索演示](https://cdn.thenewstack.io/media/2024/03/31af78bb-wpsmartsearch.png)

*WP Engine 智能搜索演示*

混合搜索不仅支持关键字搜索，还支持语义搜索。然后，它结合结果并使用算法对它们进行排名，他说。这使用户能够使用推理搜索主题，例如财务不当行为，这会显示出 Ozark 和 Schitt’s Creek，或复仇，这会显示出 The Witcher 和 Loki。他补充说，这使体验更接近 [ChatGPT](https://thenewstack.io/improving-chatgpts-ability-to-understand-ambiguous-prompts/)。

帕特森说：“更好的搜索结果意味着为你的访问者带来更好的转化。”“这意味着为他们带来更好的体验。这意味着对你的品牌有更好的认知。因此，技术、人工智能炒作，所有这些东西显然非常、非常酷。但比酷更酷的是什么？转化率的两位数增长，然后你可以将其带回你的老板和客户那里。”

智能搜索目前通常作为 SaaS 搜索产品提供，专门用于 WordPress，但可以索引和搜索来自任何地方的数据。该公司表示，有一个插件可用，既可用作所见即所得体验的 UI 界面，也可用作更高级用户感兴趣的高级定制的 WP Engine API 界面。人工智能驱动的混合搜索处于测试阶段，并且仅适用于高级帐户上的 WP Engine 客户。
