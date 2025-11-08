
<!--
title: 前端开发者，是时候告别“暗模式”了！
cover: https://cdn.thenewstack.io/media/2025/11/d7ce4190-selam_moges_deceptive_patterns.jpg
summary: “黑暗模式”通过欺骗操纵用户。亚马逊因其被罚25亿美元，Facebook也受重创。隐藏费用、订阅陷阱是常见手段。苹果以道德设计提升用户信任。开发者应警惕，避免损害声誉。
-->

“黑暗模式”通过欺骗操纵用户。亚马逊因其被罚25亿美元，Facebook也受重创。隐藏费用、订阅陷阱是常见手段。苹果以道德设计提升用户信任。开发者应警惕，避免损害声誉。

> 译自：[Why Frontend Developers Should Ditch Dark Patterns](https://thenewstack.io/why-frontend-developers-should-ditch-dark-patterns/)
> 
> 作者：Loraine Lawson

9月，[亚马逊和解了一项诉讼](https://www.wired.com/story/amazon-ftc-settlement-prime-dark-patterns/)，该诉讼由联邦贸易委员会 (FTC) 提起，指控这家电子商务平台使用黑暗模式，以操纵和欺骗的方式诱导用户注册Prime会员。这导致亚马逊向客户和FTC支付了25亿美元的赔偿金。

根据为外科医生开发技术的Apella公司软件工程师Selam Moges的说法，黑暗或欺骗性模式是[用户体验设计](https://roadmap.sh/ux-design)的一种，它通过欺骗或操纵用户来强制他们执行某种操作。她上个月在Devmio主办的[国际JavaScript大会](https://javascript-conference.com/new-york/)上发表了题为“解构黑暗模式：React开发者的道德设计原则”的演讲。

Moges说：“诚然，大多数开发者早上醒来时并不会决定要欺骗用户，但当我们不惜一切代价优先考虑增长而又不质疑设计时，我们就有可能默认将操纵行为嵌入产品中。”

Moges认为，虽然这看似是一个设计问题，但Web和应用程序开发者应该意识到黑暗模式，并在注意到这些模式时提出担忧。当这些模式对用户或监管机构（或者像亚马逊最近的案例中，两者都有）造成问题时，开发者是必须修复代码的人。

亚马逊的诉讼就是一个典型的例子。Moges说，即使亚马逊赢了，这场诉讼仍然会影响其声誉和品牌，可能导致亚马逊流失客户。显然，败诉意味着巨额赔偿。而25亿美元的金额，和解费用当然不菲。

Moges补充说：“避免可能使其陷入这种棘手情况的欺骗性设计，符合公司的最佳利益。”

## 定义黑暗模式

“黑暗模式”一词最早由独立用户体验设计师、倡导者和[《欺骗性模式》](https://www.deceptive.design/book/contents/get-started)一书的作者Harry Brignull于2010年首次使用。欺骗性模式网站列举了许多这类[有问题的模式](https://www.deceptive.design/types)，其中包括：

**隐藏费用**：用户被低价广告吸引，但在结账时发现意想不到的费用和收费。例如，一个旅行网站可能会在用户未选择的情况下自动添加保险费。

**视觉干扰**：用户期望信息以清晰可预测的方式呈现在页面上，但信息被隐藏、模糊或伪装。例如，“否”按钮是红色，“是”按钮是绿色，这巧妙地阻止人们选择“否”。

**隐藏订阅**：用户在不知情的情况下被注册到定期订阅或支付计划，且未明确披露或未经其明确同意。Moges提到的一个类似模式是**订阅陷阱**，它使订阅变得容易，但取消订阅需要多个步骤。

苹果的取消订阅可能就是一个例子——选择加入很容易，但选择退出需要用户执行一系列不那么直观的步骤，例如进入设备的设置标签页，然后进入他们的苹果账户，再进入订阅，在那里用户（最终）才能找到取消订阅按钮。

当然，这些策略并不新鲜。Moges指出，即使在互联网出现之前，营销行为也可能是不道德的。

她说：“历史内容始于互联网之前，所以早于1983年互联网出现前的销售策略——也就是在网络时代很久之前——操纵性技术就被用于零售和广告中，例如诱饵和转换策略、合同中的细则以及利用紧迫感的电视购物广告。”

但变化发生在2000年代中期，A/B测试热潮开始。她说，一种痴迷于转化率的文化导致用户体验被武器化。增长衡量标准变成了不惜一切代价的网站停留时间、留存率和追加销售。

## 黑暗模式的两个故事

Moges说，与将包容性嵌入产品开发流程本身相比，事后补救包容性也可能代价高昂。

她提到了[Facebook/剑桥分析公司丑闻](https://www.theguardian.com/news/2018/mar/17/cambridge-analytica-facebook-influence-us-election)，其中[Facebook](https://thenewstack.io/a-reason-to-not-hate-facebook-open-source-contributions/)允许第三方应用访问用户数据，影响了大约8700万用户，他们的数据被滥用于政治广告。

她说：“一些用户甚至不知道发生了什么，直到新闻报道真正写到这件事，才揭露了这一丑闻。”

Facebook不得不事后补救隐私控制措施，彻底修改[API](https://thenewstack.io/its-time-to-build-apis-for-ai-not-just-for-developers/)并改变其同意模型。

她说：“这些都是他们必须做的大量工作，而且从财务方面来看，FTC开出了50亿美元的罚款。”

她说，该品牌的声誉和用户信任也遭受了巨大打击。

她说：“最终，这引发了全球范围的审查和监管，[GDPR（通用数据保护条例）](https://www.hrpo.pitt.edu/european-union-eu-general-data-protection-regulation-gdpr#:~:text=The%20General%20Data%20Protection%20Regulation,of%20individuals%20in%20the%20EEA.)的执行，国会听证会等等。”

将其与苹果如何通过[苹果的应用追踪透明度](https://developer.apple.com/documentation/apptrackingtransparency)框架处理黑暗模式进行对比。

她说：“苹果ATT试图解决的核心问题是，应用程序可以在未经明确许可的情况下追踪用户在其他应用和网站上的行为，大多数用户不知道这一点，对移动应用的信任开始受到侵蚀。”

2021年，苹果做出了一项道德设计决策，引入了ATT。她补充说，现在当应用程序首次下载时，会出现一个弹窗，以清晰、非强制和尊重的方式明确询问用户并提示他们。

她说，苹果的行动提升了用户信任。

她说：“首先是用户信任度提升。苹果将自己定位为隐私先行者，赢得了用户信任——即使广告公司对此进行抵制。其次是采用和留存——消费者越来越将苹果视为一个安全的生态系统。”