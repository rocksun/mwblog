<!--
title: 科技专家：GenAI安全，责无旁贷
cover: https://cdn.thenewstack.io/media/2025/09/7b34e661-lead-the-charge-2.jpg
summary: 文章探讨了生成式人工智能（GenAI）在版权、数据隐私、安全、环境和社会心理健康方面带来的风险。强调了版权侵权、数据筛选的伦理问题、安全漏洞以及对社会心理健康的潜在危害。呼吁在技术发展的同时，重视安全使用和伦理考量。
-->

文章探讨了生成式人工智能（GenAI）在版权、数据隐私、安全、环境和社会心理健康方面带来的风险。强调了版权侵权、数据筛选的伦理问题、安全漏洞以及对社会心理健康的潜在危害。呼吁在技术发展的同时，重视安全使用和伦理考量。

> 译自：[Why Tech Professionals Must Lead the Charge on GenAI Safety](https://thenewstack.io/why-tech-professionals-must-lead-the-charge-on-genai-safety/)
> 
> 作者：Charles Humble

我最近和我朋友的女儿聊了聊，她一直以来的梦想是成为一名插画家。尽管她非常有才华，但她决定在大学里选择一个不同的方向，她告诉我：“人工智能意味着没有人会付钱给艺术家来创作艺术。”

我并不认为她是正确的。但如果这种模式不断重演，创意产业将会缺乏新鲜血液。

版权旨在保护和规范作品——无论是书籍、绘画、音乐还是软件——可能在短期内保护创意专业人士。然而，关于生成式人工智能的版权状况尚未确定。

侵犯版权只是生成式人工智能可能造成我们未曾预料到的新类型危害的方式之一。合规和[数据隐私](https://thenewstack.io/navigating-generative-ai-data-privacy-and-compliance/)、治理和[安全](https://thenewstack.io/ai-is-changing-cybersecurity-fast-and-most-analysts-arent-ready/)方面潜藏着漏洞。GenAI 系统还对我们本已脆弱的环境和[我们的社会心理健康](https://thenewstack.io/does-chatgpt-encourage-dangerous-delusions/)构成风险。

谁来保护我们免受 GenAI 的负面影响？ 事实是，在我们迅速攀升这项新技术的学习曲线时，我们也必须确保它被安全地使用，即使在我们等待组织和政府赶上它的时候。

## 程序员和其他创作者面临的版权威胁

让我们首先看看版权。随着摄影的出现，关于版权的新辩论出现了，并且可以与当前关于人工智能和版权的辩论进行类比。复制摄影作品是否构成侵权行为，摄影师是否应该能够控制它？（是的。）照片本身是否应该作为受版权保护的作品受到保护？（再次，是的。）

对于生成式人工智能来说，训练[大型语言模型（LLM）](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/)需要大量的材料语料库已不是什么秘密。关于如何获取这些材料，没有知情同意。人工智能公司知道他们摄取了什么，但没有义务分享他们的数据来源。

因此，作为一名作家、艺术家、摄影师、作曲家——或开发者——很难确定你的作品是否已被用于 LLM 训练，尽管如果作品在互联网上发布或出现在 [LibGen](https://libgen.ac) 中，它几乎肯定会被使用。

就像窃贼辩称，如果他们不能闯入你的房子并偷走里面的东西，他们就无法获利一样，人工智能公司选择忽视版权，声称许可这些材料的成本太高或太困难，如果他们必须付费，他们的业务就无法维持。

忽视几个世纪的法律先例的后果是可以预见的。上周五，人工智能公司 [Anthropic](https://thenewstack.io/anthropic-launches-claude-opus-4-and-sonnet-4/) 面临着 [有史以来最大的版权集体诉讼](https://arstechnica.com/tech-policy/2025/08/ai-industry-horrified-to-face-largest-copyright-class-action-ever-certified/)，[同意支付 15 亿美元](https://www.nytimes.com/2025/09/05/technology/anthropic-settlement-copyright-ai.html) 给一群作者和出版商，此前法官裁定该公司非法下载和存储了受版权保护的书籍。

此外，迪士尼和环球影业均已对人工智能图像生成器 Midjourney [提起诉讼](https://www.bbc.co.uk/news/articles/cg5vjqdm1ypo)，指控其盗版。英国广播公司（BBC）也在 [考虑采取法律行动](https://www.bbc.co.uk/news/articles/cy7ndgylzzmo)，原因是其内容未经授权使用。

Anthropic 案件的引人注目之处在于，美国加利福尼亚州北区地方法院的威廉·阿尔苏普法官（Judge William Alsup）在很大程度上站在 Anthropic 一边。

今年 6 月，他发布了一项简易判决，称当该公司合法获取书籍时，将其用于人工智能模型训练是合法的。但阿尔苏普裁定，当它从“影子图书馆”下载图书时，Anthropic 的领导人知道它正在使用盗版书籍。

阿尔苏普也是此前裁定 API 不受版权保护的同一位法官，从而破坏了 [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) 在 2012 年对 [Google](https://cloud.google.com/?utm_content=inline+mention) 的 Android 提起的具有里程碑意义的案件。

在版权的发源地英国，政府削弱版权以支持人工智能公司的企图迄今为止一直受到 [上议院的阻挠](https://www.theguardian.com/technology/2025/jun/04/ministers-offer-concessions-ai-copyright-avoid-fifth-lords-defeat)。但政府的意图是明确的；它选择押注人工智能带来的未来经济增长，而不是英国已经成功的创意产业带来的现有收入和潜在增长。

在美国，联邦“美好未来法案”（Big Beautiful Bill）的早期版本禁止各州在 10 年内监管人工智能技术，以免阻碍人工智能产业的发展。（特朗普总统签署的法案最终版本不包括该条款。）

如果人工智能在创意领域的应用变得常态化，版权问题很可能会变得毫无意义——尤其是在创意产业缺乏技术娴熟的创作者的情况下。

## 人工智能数据筛选的伦理风险

版权也是一个合规问题。如果你不知道训练数据的来源，你不仅会破坏创作者的权益，还会让你的公司面临巨大的供应链风险。

一旦获得，这些数据集必须经过筛选。这是通过一种称为人工反馈强化学习（RLHF）的技术进行的。人工智能公司从社交媒体的剧本中汲取灵感，让肯尼亚等国家的工人以 2 美元/小时的微薄工资接触到无休止的可怕内容。

正如 [Time](https://time.com/6247678/openai-chatgpt-kenya-workers/) 和 [卫报](https://www.theguardian.com/technology/2023/aug/02/ai-chatbot-training-human-toll-content-moderator-meta-openai) 所报道的那样，RLHF 的结果令人震惊。不幸的是，除了这些优秀的媒体报道之外，这个问题并没有受到太多的关注。

“我现在参加了两个小组讨论，有人告诉我 RLHF 工人只是附带损害，”人工智能伦理学家、心理学家以及 IEEE 人工智能伦理教育委员会的联合主席 [Marisa Zalabak](https://www.marisazalabak.com) 告诉 The New Stack。

如果我们继续将这些受到伤害的人类视为“附带损害”，我们就会将剥削行为融入到人工智能供应链本身。

除了不愿分享他们的训练内容外，大型人工智能公司也对其环境影响保持警惕，尽管我们知道训练 LLM 和使用它们进行推理都会造成相当大的环境破坏。我最近在 The New Stack 中探讨了 [大幅减少](https://thenewstack.io/ai-consumes-lots-of-energy-can-it-ever-be-sustainable/) 其中一些环境危害的策略。

自从撰写该文章以来，谷歌已成为第一家发布 [报告](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference?)，说明其 LLM 每次文本查询的影响的大型科技公司，这非常受欢迎。谷歌报告称，过去一年效率大幅提高，并指出其每次查询的能源使用量比 12 个月前高出 33 倍。不幸的是，他们只关注每次人工智能提示的边际能源使用量，而不关注训练、终端用户设备或外部网络使用的能源。

造成特别混乱的一个方面是 [GenAI 的极速增长](https://benjamintodd.substack.com/p/when-people-say-ai-isnt-finding-real) 的副作用，这会将有害影响集中在特定区域。虽然各个社区正在经历人工智能数据中心带来的非常真实的负面环境影响（最值得注意的是，围绕 xAI 的 Colossus 造成的 [环境噩梦](https://www.tomshardware.com/tech-industry/supercomputers/elon-musks-nvidia-powered-colossus-supercomputer-faces-pollution-allegations-from-under-reported-power-generators)），但通过 LLM 运行单个查询的影响相对较小。

## 为什么 GenAI 给治理带来了新的挑战

当我们从训练到运营 LLM 时，生成式人工智能的某些特性会带来伦理挑战，而我们现有的 AI 治理系统无法很好地处理这些挑战。

人工智能的伦理危害通常分为分配性危害和代表性危害：

*   分配性危害是指人工智能系统拒绝了你本应享有的东西，例如贷款。
*   代表性危害是指个人或社区根据他们看待自己的方式，在心理上发生的变化。

我们有良好的机制来应对分配性危害。然而，代表性危害更加模棱两可，更难衡量。

[Ada Lovelace Institute](https://www.adalovelaceinstitute.org) 的主任 [Gaia Marcus](https://www.adalovelaceinstitute.org/person/gaia-marcus/) 告诉 The New Stack，“作为研究人员，我们意识到代表性危害，但它们可能更难量化。”

“我们对 Gen AI 在英国学校中的使用的研究表明，它主要是对 ChatGPT 等通用 AI 产品的非正式使用，而不是更具体的 AI EdTech，”Marcus 说。“如果没有足够的保障措施，这可能会真正引发代表性危害的问题。”

分配性危害和代表性危害确实存在重叠。 [伦敦政治经济学院](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-025-03118-0) 最近的一项 [研究](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-025-03118-0) 发现，当询问谷歌的人工智能信息工具 Gemma 关于健康问题时，它存在明显的性别偏见，并淡化了女性症状。

“如果你是一名个案工作者，根据给出有偏见输出的工具做出决定，结果将是分配性危害，”Marcus 说。“然而，如果你使用一个系统来重现你自己的想法，那可能是代表性的，但随着时间的推移，可能更难追踪和量化它。”

她补充说，“如果聊天机器人成为个人与互联网之间唯一的界面，从而成为他们获取新闻和与世界互动的主要方式，那么代表性危害带来的风险可能会变得非常大。”

## 代码生成的安全风险

GenAI 似乎在编程领域具有早期的产品市场契合度。它感觉像是云原生方法的自然延伸，云原生方法 [允许组织运行更多实验](https://blog.container-solutions.com/why-run-thousands-of-failed-experiments)。

[GadflyAI](https://www.gadfly.ai) 的技术总监兼首席安全合规顾问 [Sal Kimmich](https://www.salkimmich.com) 告诉 The New Stack，“GenAI 非常适合概念验证工作。在相同的时间内，在不取代人类实际所做的事情（即以最小的危害进行创新）的情况下，你从相同的人那里获得了更多的原型和工程能力。”

Kimmich 认为，应该将 20% 的工程精力用于构建 POC 和试验人工智能。但是，在你的组织执行此操作之前，他们建议你公司的每个人都接受一些伦理和数据安全培训。

他们说：“即使你的员工在构建 MVP 时没有受到公司监控，也要非常清楚地说明合规的期望”，或者 [最小可行产品](https://thenewstack.io/building-an-minimum-viable-product-a-founders-guide-to-success/)。“归根结底，诉讼将起诉一个人，你必须确保你已采取一切合规措施，以尽量减少危害。”

生成式人工智能系统是随机的而不是确定性的；给定表面上相同的输入，它们会产生不同的答案。Kimmich 告诉 The New Stack，这种随机性意味着你永远不应该让 AI 靠近生产代码，因为你无法信任它。“它很笨拙，可能存在漏洞问题，并且不会让开发人员参与长期的架构决策。”

代理系统——通过 LLM 相互通信的代理到代理架构——加剧了随机系统的问题，因为它们会在 LLM 链中产生级联。“理解这些级联真的很难，而且你把这些模型放在一起的越多，系统中的可变性就越大，”Kimmich 说。

因此，基于 GenAI 的系统的测量要求很高。Kimmich 提出了批量测试的替代方案——适用于你在 AI 循环中有人类的情况。它基于逗留时间，它描述了系统在转换之前花费在瞬态状态的时间。

“我们希望通过衡量人类随着时间的推移的行为来模拟人类和机器之间的最佳关系，”Kimmich 告诉我们。“通过创建一个半 [马尔可夫链](https://thenewstack.io/a-developers-guide-to-understanding-markov-chains-in-ai/)，它可以预测该个人可能如何响应，你就可以拥有可以充当反击穿机制的东西。”

金融和医疗保健等监管更严格的行业已经以最高的安全级别处理人工智能，一直到物理硬件。不过，根据 Marcus 的说法，存在一个问题。

基于 LLM 的工具通常用于压缩文本，我们看到这些摘要工具用于医疗保健，或者“围绕 LLM 的聊天机器人包装器用于治疗——无论是作为正式工具的一部分还是‘标签外’使用，”她说。“但是，在对通用工具进行充分测试之前不要推出健康产品的预防原则目前不适用于未作为健康产品销售的通用工具。”

Kimmich 认为，监管结构将遵循安全态势的关键质量。“我认为会因为人工智能和大规模数据存储和使用的性质，特别是个人数据的性质，而出现第二套新的、受监管的行业，”他们说。“这是因为唯一性的问题——捕获这些数据库的能力。

“如果我有某人的 Netflix 帐户信息和关于他们的任何其他交叉信息，我可以识别他们。因此，创建受监管的空间以降低个人数据泄露的风险是不可避免的。”

从安全角度来看，GenAI 的许多威胁都基于数据转储。“避免这些威胁以及相关的碳燃烧的一个简单方法是将生成输出限制为典型人类可以阅读它们的速度，”Kimmich 说。“这意味着它会非常缓慢地运转，并且在意识到之前发生危险数据转储的可能性会大大降低。”

## 社会心理危害的可能性

对于 IEEE 的 Zalabak 来说，她对社会心理健康特别感兴趣，人工智能的拟人化是她最关心的问题。 [Meta 最近成为新闻，因为它允许聊天机器人与儿童进行感性对话](https://www.reuters.com/investigates/special-report/meta-ai-chatbot-guidelines/)。“Meta 允许的性语言非常有害，”她指出。据报道，种族主义语言也被允许。

“这些程序旨在模仿情感，这是一种欺骗，”Zalabak 告诉我们。“没有理由让他们假装成一个人，使用人类代词来指代机器。

“这可能会导致精神病发作，例如 [佛罗里达州男孩自杀身亡](https://edition.cnn.com/2024/10/30/tech/teen-suicide-character-ai-lawsuit)，以及德克萨斯州的一名自闭症青少年被告知 [杀死他的父母以回应他们限制他的屏幕时间](https://www.bbc.co.uk/news/articles/cd605e48q1vo)。两人都在使用 Character AI，而且他们不是个例。从心理上讲，我们正在将人们送入一种双重意识状态，他们拥有两个身份，其中一个身份存在于一个虚假的世界中。”

Marcus 建议，与任何新技术一样，重要的是我们要抵制将人们划分为末日论者与助推者的诱惑。

她说：“我们看到许多脱节现象，这在任何未被管理的重大技术变革中都很常见。技术发展速度与监管能力之间的脱节：想要减少繁文缛节的政客与想要更多治理的普通民众之间的脱节。

“很难将变革的步伐与寻找对人口的意外危害的现有机制对齐。”

Marcus 看到嵌套危害的真正潜力。 “负责任地使用人工智能是一项挑战，因为存在许多嵌套问题，”她告诉 TNS。“你有直接向消费者销售的工具，在没有护栏的情况下在专业环境中使用。技术推出的速度基本上意味着我们正在对数百万人同时进行实验，而没有评估或理解总体效果。

“你可能认为 2025 年将是代理商的一年，但我们还没有解决责任问题。因此，很难理解你试图锁定的拼图的一部分及其伦理后果。”

总的来说，Marcus 建议，人工智能供应商正在投入大量研究来解决生存风险，但较少关注更直接的威胁。“生成式人工智能中的许多测量科学都侧重于灾难性潜力，例如生物和化学风险或失控，而不是我们现在看到的危害。”

## “永远不要忘记我们是在与机器对话”

我与之交谈的专家都不反对人工智能。“我热爱科技，”Zalabak 告诉我们。“我观看了登月，从小就看‘杰森一家’。对我来说，人工智能伦理是关于拥抱人工智能的良好潜力，这是非凡的。我们可以使用这些工具做好事并盈利。

“但与此同时，造成了太多的损害。我们不需要看起来像人类的机器人，也不需要人工智能系统中使用人性化的语言。通过对人工智能进行编程，使其更难让我们暂停怀疑，从而可以避免大量危害，这样我们就永远不会忘记我们是在与机器对话。”

在我完成这篇文章时，有消息称 [加利福尼亚州一对夫妇起诉 OpenAI](https://www.bbc.co.uk/news/articles/cgerwp7rdlvo)，原因是他们十几岁的儿子去世，他们声称 ChatGPT 鼓励他自杀。在其网站上 8 月 25 日发布的一篇文章中，[OpenAI 表示](https://openai.com/index/helping-people-when-they-need-it-most/)，“最近人们在严重危机中使用 ChatGPT 的令人心碎的案例对我们造成了沉重的打击。” 该公司承认，“在某些情况下，我们的系统在敏感情况下未能按预期运行。”

作为领域专家，我们有责任确保我们创建的技术得到适当的使用。没有人比我们更适合这样做。