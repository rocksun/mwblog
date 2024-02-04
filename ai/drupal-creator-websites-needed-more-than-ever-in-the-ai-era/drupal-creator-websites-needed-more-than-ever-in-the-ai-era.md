<!--
title: Drupal创始人：人工智能时代需要更多的网站
cover: https://cdn.thenewstack.io/media/2024/02/fdfec242-rubaitul-azad-cu2nf0jz5pi-unsplash-1024x690.jpg
-->

生成式人工智能对网站构成了一种存在威胁。这引发了一个问题：网站是否仍然具有重要性？Drupal的创始人Dries Buytaert认为是的！

> 译自 [Drupal Creator: Websites Needed More Than Ever in the AI Era](https://thenewstack.io/drupal-creator-websites-needed-more-than-ever-in-the-ai-era/)，作者 Richard MacManus 是The New Stack的高级编辑，撰写关于Web和应用程序开发趋势的文章。此前，他于2003年创办了ReadWriteWeb，并将其建设成为全球最有影响力的科技新闻网站之一。从早期...

在我上次与Drupal创始人[Dries Buytaert](https://dri.es/)交谈的时候，是在2022年10月，我们的焦点是[无头内容管理系统](https://thenewstack.io/how-drupal-fits-into-an-increasingly-headless-cms-world/) —— 当时是Web开发中的一个热门话题。但自那时以来，许多事情发生了变化：JavaScript框架变得[更加复杂](https://thenewstack.io/web-development-in-2023-javascript-still-rules-ai-emerges/)，Jamstack[不再是一个炙手可热的词汇](https://thenewstack.io/netlify-launches-composable-web-platform-for-enterprise-devs/)，当然，[生成式人工智能也应运而生](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/)。这些并不一定对Web是积极的趋势。

实际上，一些人可能会说，网站现在面临的威胁比Web历史上的任何时候都要大。在2010年代，智能手机应用和应用商店似乎可能会击败Web，但到了那个十年的末期，Web开发人员通过使用先进的JavaScript、WebAssembly和Web组件等技术成功反击。而现在，在2020年代初，生成式人工智能迅速成为网站的新存在威胁。这引出了一个问题…

## 网站仍然重要吗？

在他为其基于开源（且基于浏览器的）Drupal软件构建的SaaS平台Acquia[回顾2023年](https://dri.es/acquia-retrospective-2023)的文章中，Buytaert指出了Web前进的危险和机遇。“一方面，信息收集中AI的崛起将减少对传统网站的需求，”他写道。“另一方面，商业社交媒体的衰落和向无cookie的未来的转变表明，网站将继续保持重要性，甚至可能更加重要。”

Buytaert对于网站的命运表示：“我认为这是正面的。” 他然后有些令人惊讶地指出，谷歌计划在2024年底[淘汰第三方Cookie](https://developers.google.com/privacy-sandbox/3pcd/prepare/prepare-for-phaseout)是Web的一个机会。

“这意味着营销团队对用户的信息不再那么详细，”他说。“所以这意味着他们需要自己更多地了解用户。他们不能在Web上追踪用户，因此他们需要将人们引导到他们的网站 —— 自己的数字属性 —— 并真正与他们互动，了解他们的行为、意图和欲望。所以这对开放式网络是有好处的。我认为这对隐私来说是好事，显然，第三方Cookie的消失也意味着营销人员和组织将会更多地投资于他们自己的网站。”

对于ChatGPT和其他生成式人工智能工具的影响，他持有类似的观点。他承认，人工智能可能导致有机网站流量的下降，因为像ChatGPT这样的工具被设计为直接回答搜索查询。但他认为，这只是迫使网站开发人员和所有者使他们的网站更具吸引力的一种方式。

“你必须提供超越ChatGPT能提供的价值，这样人们仍然有动力来访问你的网站。那么你怎么做呢？通过提供更好的内容 —— 更好的内容可能是个性化的内容，或者[…] 也可能是更多的内容被放在… 不一定是付费墙，但是设有一些门槛。你知道，也许你需要注册才能获得内容。”

另一个推动人们重新回归构建Web的因素是中心化社交媒体平台，如Facebook和Twitter，用户体验迅速恶化。这导致了[联邦宇宙（fediverse）的兴起](https://thenewstack.io/the-fediverse-points-to-our-social-media-future-post-musk/)，其中开放式网络是关键基础，主要通过万维网联盟的ActivityPub规范实现。Buytaert指出，Drupal在过去的十年里一直支持独立网络运动，他说这也延伸到了联邦宇宙。

“你只需安装一个模块，我们称之为插件，它将连接你的博客或网站到联邦宇宙，自动拉取内容并推送内容到联邦宇宙 —— 所有这些事情。我们已经有这个功能很长时间了。”

## 关于Web开发复杂性

我注意到最近Web开发者社区对JavaScript框架不断增加的复杂性提出了反对意见。Netlify首席执行官Matt Biilmann，于2016年创造了“Jamstack”，最近[在TheJam.dev虚拟会议上表示](https://thenewstack.io/keep-it-simple-frameworks-netlify-ceo-praises-astro-remix/)，尽管将前端与后端解耦是积极的发展，但现在存在“将一切扭曲成前端的压力 —— [要]在这个前端层重新构建整体”。

我问Buytaert对当前前端复杂性的看法。

“所有这些平台的共同特点是它们从简单开始，然后人们想要用它们来处理更复杂的用例，” 他说。这导致了Buytaert所谓的“缓慢演进”，朝着更复杂的架构发展。他以内容预览为例，指出Jamstack最初并没有这个功能，因为将内容输入Markdown文件然后使用静态站点生成器构建网站更简单。问题在于，网站用户不一定想要用Markdown写作。因此，这促使Jamstack开发者提出了创建自定义预览功能的请求，或者与提供可视化编辑的无头CMS产品集成（当我在2020年初尝试Jamstack时，出于这个原因我使用了一个名为[Forestry](https://tina.io/forestry/)的产品，现在叫做TinaCMS）。

“我认为Jamstack已经在很大程度上演变成了[...] 我称之为传统CMS，” Buytaert说，“它们可以做所有相同的事情 —— 你知道，内容预览就是一个很好的例子。这是我们Drupal已经有了二十年的功能，对吧？而且任何CMS实际上都有，这不仅仅是Drupal的事情。”

然而，他承认Drupal本身也经历了从简单到复杂的演变。如今，Buytaert及其公司Acquia将[Drupal](https://tina.io/forestry/)称为“数字体验平台”（DXP），因此它已经发展得远远超出了在2000年初作为业余爱好者CMS的起点。

“Drupal已经从我宿舍的业余项目发展成为一个企业级内容管理系统，” Buytaert告诉我。“所以我并不一定反对这种演变。它对Drupal来说肯定是有益的，我可以想象它对Jamstack在很多方面也会有好处。但随着你这样做，[...] 你会吸引新用户并淘汰老用户。你失去了业余爱好者，却得到了企业用户。这是你所做的一个选择。”

## Drupal和生成式人工智能

最后，我问Drupal如何适应生成式人工智能的趋势。Buytaert回答说，Acquia已经在其所有产品中，包括Drupal，添加了GenAI功能。他说，约90%的这种功能是“低挂果实”，有助于内容制作。

“我们将其用于诸如总结内容、为内容或帖子提供标题的建议等方面。我们将其用于将内容翻译成不同的语言。我们将其用于生成替代文本，使图像可访问。我们将其用于内容的自动标记和自动分类。我们开始在搜索中看到它的应用。”

但他表示，2024年的目标是超越“这些相对简单的内容创建用例”。计划是将AI用作CMS的用户界面。他描述了类似于我最近介绍的[设计到代码](https://thenewstack.io/locofy-launches-large-design-model-to-turn-designs-to-code/)工具Locofy的东西，该工具使用AI自动生成网站。看起来Drupal也朝着这个方向发展。

“你可以很容易地想象未来你可以这样提示，对吧？你只需输入：‘创建一个两列的着陆页面，在布局的左列中放置一个带有这些字段的注册表单’ 然后开始。它可能不会完美，但它可能轻松消除90%的[工作]，然后你只需通过点击进行微调。”

他补充说，Acquia还致力于“负责任的AI”，其中包括防止数据泄漏并允许其客户使用自己的LLM。
