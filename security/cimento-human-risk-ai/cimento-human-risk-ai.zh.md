安全行业花费了数十年和数十亿美元构建工具来保护系统。周三结束隐身模式的 [Cimento](https://cimento.ai/) 创始人认为，该行业一直找错了方向。

“人类始终是最薄弱的环节之一，”Cimento 的联合创始人兼 CEO [Zain Rizavi](https://www.linkedin.com/in/zainrizavi/) 告诉 *The New Stack*。“AI 攻击的成本正在渐进式下降。而现有的工具尚未对此做好准备。”

Zain Rizavi 对构建互联网规模的系统颇有心得。在创立 Cimento 之前，他在 [Cloudflare](https://thenewstack.io/cloudflare-mesh-agent-networking/) 的特别项目团队工作，该团队的任务是超越公司视野，确定这家网络基础设施巨头应该构建什么。他从那段经历中汲取并应用于 Cimento 的核心价值，是建立在真实行为数据之上的智能层。

“让 Cloudflare 真正出色的是我们在网络上获得的智能，”他说道。“我们现在正在企业内部围绕人类行为构建同样的智能层。”

听 Zain Rizavi 解释，Cimento 是一个 AI 原生的人为风险管理平台，它为每位员工构建动态的风险画像。该平台与员工已在使用的工具集成，如电子邮件、IDP（身份提供商）、云提供商以及大多数现有安全工具，为安全和合规团队提供统一的风险画像，帮助他们了解个人在组织内的典型工作方式，Zain Rizavi 告诉 *The New Stack*。

Cimento 已从 Bowery Capital、Indie VC 以及来自 Cloudflare、Palo Alto Networks、Nvidia 和 Okta 的天使投资人处筹集了约 300 万美元的种子前融资。它摄取企业现有安全栈（VPN、CrowdStrike 等端点代理、DLP 工具、云数据湖）的信号，并运行贝叶斯模型来构建统一的、针对每个用户的风险评分。

其目标是取代该类别传统的产出物，例如网络钓鱼邮件和两小时的培训课程，转而采用真正反映人们行为方式的方案，Zain Rizavi 说道。

“如果我说，‘Darryl 没有参加两小时的培训’，我不认为这意味着‘零风险’，”Zain Rizavi 说道。“那只意味着没人想参加两小时的培训。”

“我们认为人类层应该通过实时监控、响应和自动修复来管理。而不是询问员工是否完成了培训，”Zain Rizavi 在一篇[博客文章](https://cimento.ai/articles/human-behavior-is-security-s-blind-spot.-we-built-cimento-to-fix-it)中写道，并问道：“这名员工现在被成功攻击的可能性有多大，应该采取什么措施？”

## 多轮网络钓鱼

该产品最独特的特征是 Cimento 所称的“多轮网络钓鱼模拟”。该平台不再发送单一的[网络钓鱼邮件](https://thenewstack.io/using-mql-to-stop-novel-email-phishing-attacks/)（这是行业惯例），而是针对高风险用户群体运行迭代的、多渠道的活动：特定国家的承包商、心怀不满的员工、已提出离职两周但仍拥有生产权限的人，公司表示。

> “真正优秀的攻击者不会只发一封钓鱼邮件就收手。” ——Zain Rizavi

“真正优秀的攻击者不会只发一封钓鱼邮件就收手，”他告诉 *The New Stack*。他引用了安全概念中的“[杀猪盘](https://dfpi.ca.gov/news/insights/pig-butchering-how-to-spot-and-report-the-scam/)”——这种长线作战的方法让攻击者在发起攻击前投入时间建立信任。“你给它时间，效果会好得多。”

在实践中，高风险员工可能会收到一封钓鱼邮件，接着是短信，然后是语音电话，最后是加密的 WhatsApp 消息——每一步的设计都旨在从员工是否参与、报告或忽略上一步中进行学习。“你有五六个接触点可以学习，”Zain Rizavi 说。“到最后，你正在为最高风险用户保护核心商业机密。”

当跨过风险阈值时，Cimento 可以触发自动响应——例如通过 [Okta](https://thenewstack.io/okta-wants-to-secure-your-ai-agents-too/) 或其他身份提供商撤销访问权限——无需安全团队成员手动干预。

“你不需要团队花时间去弄清楚到底发生了什么，”Zain Rizavi 说道。“我们把风险呈现出来，他们只需按一下按钮。”

## 代理问题

更棘手的问题，也是 Zain Rizavi 所看到的 Cimento 长期使命，是将该风险框架扩展到 [AI 代理](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/)。今天，该公司将代理风险映射到操作代理的人身上：一位使用代理化财务工具的 CFO 会继承该 CFO 所携带的任何风险画像。Zain Rizavi 表示，完整的代理模拟已列入路线图，但尚未发布。

对于 AI 基础设施公司、Cimento 早期客户 [Together AI](https://www.together.ai/) 来说，代理风险问题并非理论性的。Together AI 的安全主管 [Derek Chamorro](https://www.linkedin.com/in/derekchamorro/) 告诉 *The New Stack*，现有工具的问题不在于它们不好，而在于它们是为不同的威胁模型构建的。

> “代理是衍生身份。它们继承你的权限，携带隐含的信任，而且没有先天的身份，没有不可篡改的指纹。” ——Derek Chamorro

“我无法通过 [KnowBe4](https://www.knowbe4.com/) 或 [Proofpoint](https://www.proofpoint.com/us) 弥补的差距正是这一点，”Derek Chamorro 说道。“代理是衍生身份。它们继承你的权限，携带隐含的信任，而且没有先天的身份，没有不可篡改的指纹。传统的培训平台教人们识别钓鱼邮件。它们不是为一个代理（你上个月还信任它，它拥有你授予的所有访问权限，而你和你的安全团队都对其行为缺乏真实可见性）的世界而构建的。”

Derek Chamorro 的威胁模型集中在他认为几乎普遍存在的行为模式上：一旦一个人授予了代理访问权限，他们就会停止对其进行审查。

“他们曾经说过‘是’，所以代理从那时起所做的一切都会获得内含的批准，”他说道。“我敢保证这种攻击类型的模拟失败率在 90% 以上——不是因为我们的员工粗心，而是因为在你已经授予访问权限后，隐含信任是人类的自然反应。”

与 Okta 的集成是该架构对 Together AI 产生吸引力的关键原因。“大多数工具只是给你一个仪表盘，”Derek Chamorro 说道。“拥有一条从风险信号到 Okta 的直接路径——在那里你可以真正禁用应用或隔离用户——这才是闭环的方式。”

对于正在将 Cimento 与老牌公司进行评估的安全负责人，Derek Chamorro 谨慎地定位了这种对比。

“老牌公司在它们擅长的领域表现良好。如果你的威胁模型主要还是电子邮件钓鱼和合规性勾选培训，KnowBe4 和 Proofpoint 会很好地为你服务，”他说道。“但如果你的组织正在快速迈向 AI（大多数组织都是如此，无论安全是否跟上），你处理的就是一个根本不同的问题。不要把 Cimento 评估为你现有工具的替代品。要评估它针对那些工具无法看到的风险平面的能力。”

## 大规模个性化

Zain Rizavi 认为，个性化是前几代安全工具错失的核心开启点。“从未有过这种程度的个性化，”他指出，销售人员倾向于点击外向型诱饵，而大公司的工程师则会跳过邮件但点击 Slack 中的链接。“如果说我对学习有任何了解的话，数据总是表明一对一的个性化是模型发挥作用的地方。”

Cimento 这个名字反映了这种精神。Zain Rizavi 说他在从旧金山飞回来的航班上，阅读关于 1600 年代欧洲科学创新的书籍时想到了这个名字。[Accademia del Cimento](https://en.wikipedia.org/wiki/Accademia_del_Cimento)（伽利略的科学学会）是建立在一个核心原则之上的：形成假设、测试、推断、重复。“测试与推断，”Zain Rizavi 说道，“这正是我们正在做的。”

Zain Rizavi 解释说，Cimento 这个名字“在严谨的科学史上有着深厚的渊源。”

“伽利略的弟子们在佛罗伦萨创立了 Accademia Del Cimento，这是世界上最早的科学机构之一。他们的指导原则是 *Provando e riprovando*——测试与再测试。在经过真实条件下的挑战、观察和证明之前，没有任何事物被接受为真理，”Zain Rizavi 在他的文章中写道。“这正是我们认为管理人为风险（和 AI 代理）的方式。不是假设，而是持续测试、衡量和完善。”

该公司目前正与一小部分企业客户合作，目标是受监管行业和 AI 原生公司。Zain Rizavi 表示，愿景是最终能根据行为数据模式，在攻击发生前三个月进行模拟——在威胁具体化之前而非之后对员工进行培训。

“攻击面正在不断扩大，”他说道。“在某种程度上，他们可以将模拟游戏化。但你作为安全团队，需要感知到它的存在，因为它看起来像一条短信。它看起来像 LinkedIn 上试图重新建立联系的前员工。我们将赋予安全团队进行此类模拟的能力。”