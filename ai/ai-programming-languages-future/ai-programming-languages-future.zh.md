以AI为先的语言会是什么样子？去年，一位西班牙开发者警告称，我们人类友好的语法消耗了“过量”的token——从而增加了成本——并阻止了复杂程序适应现有AI的上下文窗口。“我让Claude发明一种编程语言，其唯一重点是提高LLM的效率，”这位开发者[在Reddit上解释道](https://www.reddit.com/r/ClaudeAI/comments/1lpxaux/i_asked_claude_code_to_invent_an_aifirst/)，“完全不考虑它将如何服务人类开发者。”

他们尝试创建“[AI优先的原生语言](https://github.com/AvitalTamir/sever)”并非最后一次。就在上周，一位开发者[宣布](https://news.ycombinator.com/item?id=47355138)了一项[新语言](https://github.com/hvoetsch/valea)的计划，旨在通过“确定性”语法明确开发者意图，并通过较小的语言表面减少边缘情况，从而满足自主AI代理的需求。

Andrea Griffiths，GitHub的高级开发者倡导者兼时事通讯《*Main Branch*》的撰稿人，已经看到了“AI优先”语言的实验。然而，Griffiths告诉《*The New Stack*》，目前还没有任何语言获得有意义的采用。

“我认为这说明了很多问题，”Griffiths说，“现有生态系统的引力是巨大的——库、工具、社区知识、生产基础设施。一门新语言不仅需要对AI更好。它还需要有充分理由让开发者放弃他们已拥有的一切，而这种转变不会一蹴而就。”

> “一门新语言不仅需要对AI更好。它还需要有充分理由让开发者放弃他们已拥有的一切，而这种转变不会一蹴而就。”

我们是否有一天会开发出一种以牺牲人类可读性为代价的AI优化语言？或者AI编码代理是否会让我们更容易使用现有语言——尤其是那些具有内置安全优势的强类型语言？我们甚至能否想象一个AI优先语言将一切抽象化，生成无需源代码即可编译的模块的世界？

开发者、语言设计师和开发者倡导者现在正开始提出这些问题……

## Chris Lattner的Mojo vs. Rust

在AI时代，编程语言应该是什么样子？答案不止一个。在Scott Hanselman主持的最新一期《*[The Hanselminutes Podcast](https://hanselminutes.com/1037/thats-good-mojo-creating-a-programming-language-for-an-ai-world-with-chris-lattner)*》中，这位微软开发者社区副总裁与AI工具公司[Modular AI](https://www.modular.com/)的联合创始人兼CEO Chris Lattner探讨了这一话题。

Lattner的职业生涯包括创建Swift编程语言和LLVM编译器工具链——但他正专注于*硬件*如何变化，认为在当今的多核和AI优化芯片面前，“我们拥有所有这些疯狂的GPU和计算能力，但没有人知道如何编程！”

> “我们拥有所有这些疯狂的GPU和计算能力，但没有人知道如何编程！”

因此，虽然Lattner的公司为开发者构建AI工具，但它也在开发其新编程语言Mojo，Lattner称其“基本上是LLVM，但适用于AI芯片……一种能够跨所有硅片扩展的编程方式。”

Hanselman的播客将其称为“[AI世界的一种编程语言](https://www.youtube.com/watch?v=pTM2bnFxyf8)。”

但也有人认为AI正在推动程序员使用具有内置内存安全性的*现有*编程语言——其中包括[Datacurve](https://datacurve.ai/)（销售高质量/复杂数据）的创始工程师Peter Jiang。Jiang在本月早些时候在《*Forbes*》杂志上撰文，将Rust描述为“[氛围编程时代意想不到的引擎](https://www.forbes.com/councils/forbestechcouncil/2026/03/03/rust-the-unlikely-engine-of-the-vibe-coding-era/)……当AI编写代码时，Rust的严格性不再是障碍，而是免费的质量保证，”Rust的编译器充当着“强制LLM证明其逻辑正确的护栏。”

GitHub开发者倡导高级总监Cassidy Williams指出，这是一个有吸引力的优势。[今年1月](https://github.blog/ai-and-ml/llms/why-ai-is-pushing-developers-toward-typed-languages/)，Williams引用了一项2025年的学术研究，该研究发现[94%的LLM生成的编译错误是类型检查失败](https://arxiv.org/pdf/2504.09246)。”

## 强类型语言获胜？

有数据表明开发者正在利用这些优势——而不仅仅是通过转向Rust。Williams补充说，截至[2025年8月](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)，TypeScript“现在是GitHub上使用最多的语言，超越了Python和JavaScript，”其中一个因素归功于“AI辅助开发的推动……TypeScript在2025年增加了超过100万贡献者（同比增长66%，25年8月与24年8月相比），总计约有260万开发者。”Williams相信，其他强类型语言也证实了这一趋势，并分享了[GitHub数据](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)中的更多例子：

*   “Luau，Roblox的脚本语言，作为一种渐进式类型语言，同比增长超过194%。”
*   “Typst，常与LaTeX相提并论，但具有函数式设计和强类型，同比增长超过108%。”
*   “即使是Java、C++和C#等较旧的语言，在本年度报告中也实现了前所未有的增长。”

因此，Griffiths说，尽管AI可能会影响编程语言，但这不一定是通过转向新的AI优化语言来实现的。“实际发生的情况更为微妙：那些已经结构化、强类型和显式的语言变得更具吸引力，因为AI工具能更好地与它们配合。TypeScript优于JavaScript。Rust优于C。Python的类型提示正成为标准实践。这种变化不是一种新语言，而是现有语言的胜利。”

> “这种变化不是一种新语言，而是现有语言的胜利。”

Griffiths上个月[在GitHub的博客上](https://github.blog/ai-and-ml/generative-ai/how-ai-is-reshaping-developer-choice-and-octoverse-data-proves-it/)阐明了这一点，他写道，像Rust这样的强类型语言对AI施加了“更清晰的约束”，从而产生“更可靠、上下文更正确的代码。”同时，随着AI处理语法，“选择强大但复杂语言的代价也消失了。”事实上，GitHub在10月发布的最新数据显示，甚至AI生成的项目中*shell脚本*的使用量也跃升了206%，Griffiths指出。“AI消除了让shell脚本痛苦的摩擦。

“所以现在我们可以在没有通常成本的情况下，为任务使用正确的工具。”

## 现有语言——还是根本没有语言？

Stephen Cass，IEEE Spectrum的特别项目编辑，正在密切关注这一切。自2019年以来，他为IEEE Spectrum对编程语言的受欢迎程度进行了排名（这项传统始于2013年）。但是，当今语言的受欢迎程度现在会停滞不前吗？Cass[在9月份问道](https://spectrum.ieee.org/top-programming-languages-2025)。

在一个拥有AI驱动编码工具的世界里，新兴语言是否总是面临劣势，因为LLM在经过多年历史示例的大型代码库上训练时效果最好？Cass想知道AI是否还会以其他方式阻碍新语言的发展——因为“如果AI正在缓解我们对当今语言的不满，那么任何新语言能否达到产生影响所需的临界质量呢？”

但Cass也是那些对专门为AI代理创建新语言的可能性感到好奇的人之一。Cass的文章认为，语言基本上创造了人类友好的抽象（和安全预防措施）——但是“一个足够先进的编码AI真正需要多少抽象和防误结构呢？”Cass大胆提出了关于我们未来的终极问题：“我们能否让AI直接从提示生成可馈送到我们选择的解释器或编译器的中间语言？在那种未来，我们是否还需要高级语言？”

Cass承认了明显的缺点。（“诚然，这将把程序变成难以理解的黑箱，但它们仍然可以被划分为模块化的可测试单元，以进行健全性和质量检查。”）但是“程序员只需调整他们的提示并重新生成软件，而不是试图阅读或维护源代码。”

这导致了一些令人费解的假设，比如“在没有源代码的未来，程序员的角色是什么？”Cass提出了这个问题，并宣布在10月举行“紧急互动会议”，讨论AI是否预示着我们所知的独特编程语言的终结。

## 如果……？

在[那次网络研讨会](https://www.youtube.com/watch?v=53ZX1SCNryQ)上，Cass说他相信未来的程序员仍然会提出接口、选择算法，并做出其他架构设计选择。Cass说，显然生成的代码需要通过测试，并且“必须能够解释它正在做什么。”

但是什么样的抽象可以消失呢？然后“当我们真正让AI摆脱束缚时会发生什么？”Cass问道——当我们“不再费心”让它们用高级语言编程时。（因为毕竟，高级语言“是人类的工具。”）

“如果我们让机器直接创建中间代码呢？”（Cass认为机器语言层面会太底层，“因为你也需要一个编译层来适应不同的架构……”）

这些想法引起了网络研讨会联合主持人Dina Genkina（该网站专注于计算/硬件的副编辑）的怀疑。Genkina同意当今的编程语言为人类提供了“防止做傻事的护栏”。但即使在一个尝试使用AI友好微优化新语言的世界里，“我觉得AI是否需要更多护栏或更少护栏是一个悬而未决的问题……我不是说这不可能，但我目前看不到一条通向那里的路径……从我们现在所处的位置。”

![IEEE Spectrum 网络研讨会 - IEEE Spectrum 网络研讨会 - AI会终结独特的编程语言吗](https://cdn.thenewstack.io/media/2026/03/4148ee18-ieee-spectrum-webinar-ieee-spectrum-webinar-will-ai-end-distinct-programming-languages.png)

因此，无论是否转向更AI友好的语言，Genkina总结道，最终，我们新的机器驱动的结对程序员仍然需要进行代码审查。“肯定有一派人认为，你需要让人类无限期地参与其中……我想如果我们不理解它在做什么，就会加剧这种恐惧……AI的可解释性将变得越来越重要，尤其是在这类事情上。”

Cass笑着指出，我们甚至可能引入“全新的失败”，就像他所说的“无人驾驶汽车困境……这就像是，‘嗯，你知道，也许它会杀死不同的人，但如果它总体上杀死的人更少……’在这样的未来，问题可能变成‘如果你犯的错误更少，但它们是不同类型的错误呢？’”

Cass说他正在关注设计AI语言的研究论文，尽管他同意这不是“明天”的事情——毕竟，我们现在还在消化“氛围编程”。但“我可以看到这成为一个活跃的研究领域。”

尽管他也同意沙盒环境对AI有好处……

## 无代码编程仍是“推测性的”

本周，《*The New Stack*》联系到联合主持人Dina Genkina征求评论，她仍然持怀疑态度，表示：“据我所知，无代码编程仍然是推测性的。”

在MainBranch.dev，高级开发者Andrea Griffiths也仍然不相信。“我们会看到为AI阅读器而非人类维护者优化的语言吗？我对此持反对意见。代码仍然需要人类调试、审计和理解，尤其是在生产中出现问题时。没有任何工程团队会部署他们无法检查的代码。”

但Griffiths认为，一个更可能的结果是，AI“改变了人类需要阅读的内容”的世界。

Griffiths说，我们应该想象的未来是，“你花更少的时间阅读样板代码——花更多的时间审查架构决策、边缘情况和安全边界！”