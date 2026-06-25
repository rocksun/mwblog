Anthropic 在 Claude Fable 5 和 [Mythos](https://thenewstack.io/openai-chatgpt-gpt-5-5-security/) 5 上经历的[过山车式旅程](https://thenewstack.io/fable-ban-open-weights/)在今年留下了各种余波，但这并没有阻止独立软件开发人员通过自己的方法和渠道来测试这些模型所宣称的能力。

来自德克萨斯州奥斯汀的软件开发人员 Joe Cooper（又名 swelljoe）表示，他对于 Mythos 在发现真正具有挑战性的安全漏洞和网络弱点方面的能力持怀疑态度。

## 足够丰富的调试混合体——Mythos 能胜任吗？

“我的想法是收集那些专门由 Mythos 发现的漏洞，正如 [Anthropic 自己的](https://red.anthropic.com/2026/cvd/)文档所涵盖的那样，并开始构建一个基准测试服务，” [Cooper 在他的博客中写道](https://swelljoe.com/post/will-it-mythos/)。

“（我想）找到漏洞修复前的提交记录，验证一个顶级模型（在本例中为 [Opus](https://thenewstack.io/claude-opus-48-release/)）在直接指向该漏洞时是否能够识别并理解它，并将其添加到我们的语料库中，以基准测试那些盲目运行的模型是否能够准确检测和描述该漏洞，” Cooper 解释说。

为了向 YouTube 的 [Will It Blend?](https://en.wikipedia.org/wiki/Will_It_Blend%3F#:~:text=Other%20technological%20devices%20were%20blended,shredded%20or%20the%20boxed%20iPad.) 信息娱乐视频系列致敬——该系列作为 Blendtec 搅拌机系列的营销工具，由创始人 Tom Dickson 尝试粉碎从整只鸡到 iPhone 4 的一切物品——Cooper 今年五月的分析文章被幽默地命名为“Will It Mythos?”（Mythos 能胜任吗？）。

他对自己过程的描述指出，他之前构建了一个名为 [Nelson](https://github.com/swelljoe/nelson) 的工具来自动挖掘自己项目中的漏洞。他注意到他“已经发现各种模型之间存在惊人的差异”（Nelson 通过 [Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/)、Gemini CLI 和兼容 OpenAI 的 API 使用各种模型），以及它们在识别漏洞方面的有效性差异。

但他想要确切的数字，所以他主要利用 Claude 来制作一套基准测试套件，该套件借鉴了 Nelson 的部分代码并对 Mythos 进行了测试。

## 每个主流操作系统中的零日漏洞

考虑到他根据“Anthropic 自己的文档”测试漏洞收集的雄心，我们在此要记住，[Anthropic 曾著名地表示](https://www.anthropic.com/research/mythos-preview?utm_source=tldrai)，在测试期间，它发现 Mythos Preview 在用户引导下，有能力识别并利用“每个主流操作系统和每个主流网络浏览器”中的零日漏洞。

> “最困难的漏洞是多文件漏洞。模型可以自由查看所有文件，但通常需要了解上下文才知道给定的用法是否存在问题。这对任何安全审查员（无论是人类还是 AI）来说都是一个难题。”

最终，他想找出盲目运行的模型是否能准确检测和描述漏洞。Cooper 的系统构建方式是让所使用的模型能够查看整个代码仓库并跟踪跨文件的逻辑，但不会被告知要寻找什么。

“最困难的漏洞是多文件漏洞。模型可以自由查看所有文件，但通常需要了解上下文才知道给定的用法是否存在问题。这对任何安全审查员（无论是人类还是 AI）来说都是一个难题，” Cooper 说。

他说他假设 Mythos 拥有更先进的工具，并且可能在调试器中运行软件或执行[模糊测试](https://thenewstack.io/defend-autonomous-vehicle-from-threat-actors-with-fuzz-testing/)。

## 对 Mythos 在此方面表现优异的一些认可

“猜测 Mythos 可能做的所有事情目前超出了本项目目标。但这个语料库中存在一些极其难以发现的漏洞，这使得 Mythos 在此问题上表现特别出色的观点得到了一些认可，” Cooper 承认道。

> “它几乎肯定在原始能力上处于领先地位，因此从这个意义上讲，Mythos 的设计旨在处理广泛的漏洞。但重要的是要认识到，仅仅领先于基准测试，与将所有安全进展都押注在一个模型上是有区别的。” —— Conor Sherman，Sysdig。

## 原始模型能力并不等同于全能安全

随着人们对 Anthropic 新模型能力的看法开始形成，我们将逐渐获得更多关于其工作机制的真实见解。

运行时安全专家 [Sysdig](https://www.sysdig.com/) 的全球 CISO [Conor Sherman](https://www.linkedin.com/in/conordsherman/) 是一个乐观的人，他告诉 *The New Stack*，Mythos 在其他 AI 模型中脱颖而出。

“它几乎肯定在原始能力上处于领先地位，” Sherman 说。“因此，从这个意义上讲，Mythos 的设计旨在‘混合’（处理）广泛的漏洞（尽管可能不是整只鸡或 iPhone），并且它在寻找那些让其他一切都陷入困境的多文件漏洞时，具有表现良好的内在能力，这似乎是它最显著领先的地方。”

但这里有一些警告：Sherman 建议，重要的是要认识到，仅仅领先于基准测试，与将所有安全进展都押注在一个模型上（将其视为某种网络万能药）是有区别的。

“一个功能较弱但成本较低、连接到正确架构的模型可以弥补大部分差距，” Sherman 解释说。“对于防御者而言，真正重要的优势不在于模型与模型在已知漏洞语料库上的对抗。在人工智能驱动威胁的时代，安全需要运行时上下文和实时信号，使团队能够以当今攻击者的速度采取行动。”

AI 原生合成测试公司 [Mozark](https://www.mozark.ai/) 的联合创始人兼联席 CEO [Fabien Renaudineau](https://www.linkedin.com/in/fabienrenaudineau/) 告诉 *The New Stack*，就纯粹能力而言，代理测试和调试工具正在飞速改进，低估它们将是“一个错误”。

“此类系统已经可以帮助工程师通过更大的代码上下文进行推理、识别可能的失败路径并加速补救，” Renaudineau 说。“但无论基准测试、‘混合’（处理）还是训练方式如何……生产可靠性不仅仅由代理能做什么来决定。”

Renaudineau 在此划出了一条界限，并表示调试可靠性只能由工具输出的验证方式，以及我们选择基于什么进行验证来决定——而这里的第一个原则是“代理本身不能成为”其自身可靠性的可信评判者。

“验证必须独立于代理，可重复，并在真实的用例条件下进行测试——而不仅仅是在开发或基准测试代理的受控环境中进行测试，” Renaudineau 补充道。

## **DevSecOps 开发人员下一步应该思考什么**

至于“Mythos 能胜任吗？”（Will it Mythos?）的提出者本人 Joe Cooper 指出，关于 Anthropic 模型是否能识别真正具有挑战性漏洞的核心问题，他的基准测试给出的回答是“一个响亮的，也许吧”。

“也许 Mythos 在发现安全漏洞方面确实比目前其他模型更好，因为它发现了四个本次实验中没有任何其他模型发现的漏洞。但我会继续测试。可能提示词、工具或测试工具的改变可以使目前公开可用的模型产生更好的结果，” Cooper 总结道。“随着时间的推移，我会改进语料库。如果 Anthropic 停止吹嘘特定漏洞，它可能会成为一个更通用的基于 CVE 的基准测试。”

鉴于对 Anthropic 最新一批产品如此热烈的兴趣和期待，以及在诸如 [Project Glasswing](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) 等领域开展的工作如此神秘，软件工程界正在努力提供如此多（希望永远如此）公正的分析，这肯定是一件好事。