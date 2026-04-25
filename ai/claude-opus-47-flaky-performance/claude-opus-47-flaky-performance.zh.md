在政治圈，一周的时间很长，但在 AI 开发者高级用户圈，这一周显得更漫长。在 Anthropic [于上周三发布](https://thenewstack.io/claude-opus-47-launch/) Claude Opus 4.7 后，许多人表达了这种感受。尽管该模型承诺作为一款专为处理复杂推理和细微分析而构建的 AI 服务模型，其性能将超越前代。

来自 [Anthropic 的宣传承诺](https://www.anthropic.com/news/claude-opus-4-7)称其具有“严谨且一致地处理复杂、长期任务”的能力，以及专为精准关注指令而设计的功能。该模型甚至会设计验证自身输出的方法，然后再进行汇报。

## 严格来说，这并不是问题所在

正如 *The New Stack* 报道的那样，我们知道 Opus 4.7 更具字面意义的指令遵循能力意味着一些“为早期模型编写的提示词有时会产生意想不到的结果”，这意味着一些 Claude 用户可能需要调整他们的提示词编写风格。

但这并不是让用户恼火的原因；真正的矛盾在于其他地方，而且情况并不乐观。

Reddit 用户兼博士生 JulioMcLaughlin2 在 [r/artificial](https://www.reddit.com/r/artificial/comments/1so16hr/opus_47_is_terrible_and_anthropic_has_completely/) 版块解释了他们如何要求 Claude 4.7（开启自适应思考模式）完成一个详细的证明，结果它却陷入了循环，回复内容读起来像是“哦等等，那行不通，让我再试一次”——在同一个回复中重复了五次。

“是的，有一个变通办法可以显式地告诉它先思考再回答。但是……为什么这是必要的？我每个月付 20 美元。这本该是一个顶尖模型。相反，它在回复中途浪费时间、自我怀疑，而且经常无法在某些问题上得出任何有用的结论，而我相当确定 4.6 在一个月前能更连贯地处理这些问题，”他们哀叹道。

这种不安似乎正从各个渠道散发出来。Opus 4.7 用户、AI 博主和莎士比亚十四行诗的引用者 Upali R. 也正经历着一段艰难的时光。

Upali R. 在 [Medium](https://medium.com/@solaan/anthropic-just-dropped-a-bomb-claude-4-7-opus-changes-everything-dfcabd69dd53) 上写道，他一直在使用 Opus 4.7 开发一个带有几个 API 集成、中量级后端和 [Flutter](https://aws.amazon.com/what-is/flutter/#:~:text=Flutter%20is%20an%20open%20source,mainly%20supported%20mobile%20app%20development.)（Google 的开源跨平台 UI 工具包）前端的 MicroSaaS 生产力应用。他称之为“神话般的单人开发项目”，即一个野心勃勃甚至有些过头的项目。

## 在 Flutter 项目中“拉胯”

“快到第三个小时的时候，出了一些差错，我看着它在我尝试两周完成的 Flutter 项目中表现得非常糟糕。我错误地估计并高估了这些模型的实力，”Upali R. 抱怨道。

他解释说，他一直将 AI 作为一种智能自动补全工具，这很有用，但他发现了一个“天花板教训”，即该工具在最终失败前能够向上延伸的程度。

“仅仅一两次像样的交流，模型就偏离了航线。它削弱了你的功能，破坏了你的架构。原本那个屋顶还好好的，结果现在全乱了，”他写道。

用户的普遍感受是 Anthropic 削减了模型功能的边界。用户发现模型变得更加谨慎，最终智能程度降低，或许是以符合[安全使用标准](https://www.anthropic.com/news/building-safeguards-for-claude)的名义（就这些标准目前存在的程度而言）。Upali R. 本人暗示开发者支付费用的模型“实际上是‘精简版’”，并且“受到了安全护栏的限制”，这些护栏充当了性能的拖累。

## AI 缩减增效（AI shrinkflation）

所有这些关于现实的讨论，导致一位在 [Trading View 上撰文](https://www.tradingview.com/news/forexlive:a33249d3e094b:0-anthropic-releases-opus-4-7-drops-but-the-real-mythos-is-still-behind-the-glass/)的评论员表示，开发者已经开始将这些举动称为“AI 缩减增效”（AI shrinkflation），即相同的模型，下一个版本的迭代，却有着更少的形式和功能。换句话说，真正的故事在于包装盒里*没有*的东西。

这位开发者引用了 Project Glasswing 作为 Anthropic 限制顶级智能以在更严格的安全指南下工作的举措，认为这是一把双刃剑。

“一方面，它构建了‘上帝模型’的噱头，”他们写道。“另一方面，它证实了人们的怀疑，即我们可以付费使用的模型实际上是‘精简版’，受到了作为性能拖累的安全护栏的限制，或者是因为过度使用而导致的某种退化或限流。”

## 机器里的幽灵？

那么问题来了，我们看到的是某种由于过度使用导致的退化或限流，还是机器中某种更深层的幽灵现在表现为 bug？

为了澄清事实，The Futurum Group 的分析师 Guy Currier 告诉 *The New Stack*，我们在 Opus 4.7 中看到的现象绝对不应被定性为 bug。他坚持认为，这是[每一个变革性技术周期](https://thenewstack.io/ai-agents-and-their-life-cycle-what-you-should-know/)第二阶段现实中“令人不快的真相”。

“第一阶段是狂热：把一切都投向生成式 AI，惊叹于它的输出，宣传你对它的使用，”Guy Currier 说。“现在，在第二阶段，我们正在经历失败和沮丧。Anthropic 正试图通过一个质疑自身信心的模型来走在这一趋势的前面，直接解决 AI 权威语气误导用户产生盲目信任的常见投诉。”

他指出这里存在一个更广泛的讽刺，并表示当“自信的自我怀疑变成一个死循环”时，这是一种同义反复的“第 22 条军规”，即用时间换取预期的质量。

“大多数用户仍然缺乏有效引导 AI 的提示词技巧。天下没有免费的午餐。市场，即人类，始终且自然地需要正常的、人类的时间来成熟，学会纪律严明、熟练地使用变革性工具，并开始体验持久的价值，”Guy Currier 补充道。

## 为 OpenAI Codex 敞开大门？

这些发展是否为 OpenAI 的 Codex 蓬勃发展打开了大门？对于开发者来说，在实际使用中，Claude 和 Opus 当然仍然胜出，但对 Anthropic 备受吹捧、即将推出的 Mythos 模型的信任现在可能多少受到了一些损害。

与此同时，OpenAI 正在尽其所能利用市场机会。该机构本月旨在通过发布新的 Codex 版本来对标 Anthropic 的更新，承诺为开发者提供更多他们日常使用的工具和应用。

根据 [OpenAI 上周四的一篇博文](https://openai.com/index/codex-for-almost-everything/)，“Codex 应用现在还包括对开发者工作流的更深层支持，例如审查 PR、查看多个文件和终端、通过 SSH 连接到远程开发机，以及一个应用内浏览器，以加速前端设计、应用和游戏的迭代。”

## 究竟是不是内容腐烂？

为了寻求某种总结性的见解，英国数字产品构建专家 [Applifting](https://applifting.io/) 的联合创始人 Jan Hauser 告诉 *The New Stack*，Opus 4.6 和 4.7 的“感知迟钝”归结为至少两个因素。

“首先是实际上可以在查询上消耗多少‘努力’（即推理代币），”Jan Hauser 说。“从历史上看，4.6 在这方面相当慷慨，因此模型会返回非常好的输出。在 4.7 发布之前，Anthropic 开始限制这一点，人们开始察觉到了。”

他认为，其次是预期——人们很快就会习惯高质量的输出，并且对任何质量下降都相当敏感。

“有人可能会说，这种发展反映了所有 AI 实验室的发展方向：用同样或更多的钱获得更少的智能。大多数[人还指出内容腐烂](https://thenewstack.io/context-rot-enterprise-ai-llms/)是一个促成因素，而 Anthropic 将 100 万上下文版本设为默认值，使得情况变得更糟，”Jan Hauser 补充道。

在探寻这里正在发生的真正问题和议程时，开发者自然会思考：AI 模型巨头们是在试图节省推理成本，还是在部署更强大的安全控制，或者是感受到了内容腐烂的影响，亦或是在绑定线束更新时玩弄其他博弈元素。

最终无可置疑的事实可能是，面对多方面的多模态优化和扩展，交付恒定不变的模型行为一致性是一项极度复杂的任务。