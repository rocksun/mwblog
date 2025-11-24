
<!--
title: AI正在为资深工程师制造新的代码评审瓶颈吗？
cover: https://cdn.thenewstack.io/media/2025/11/a7296cca-andre-ouellet-6qbk7gk2ji0-unsplash.jpg
summary: Addy Osmani认为AI编程利于原型，但速度优先于正确性。开发者对AI信任度下降，代码审查成瓶颈。建议理解AI代码，加强上下文工程。
-->

Addy Osmani认为AI编程利于原型，但速度优先于正确性。开发者对AI信任度下降，代码审查成瓶颈。建议理解AI代码，加强上下文工程。

> 译自：[Is AI Creating a New Code Review Bottleneck for Senior Engineers?](https://thenewstack.io/is-ai-creating-a-new-code-review-bottleneck-for-senior-engineers/)
> 
> 作者：David Cassel

爱尔兰软件工程师[Addy Osmani](https://addyosmani.com/)并不反对[氛围编程](https://thenewstack.io/vibe-coding-six-months-later-the-honeymoons-over/)。然而，这位[Google Gemini](https://thenewstack.io/google-launches-gemini-3-pro/)开发者（他也在从事Chrome相关工作）对AI的局限性也有着敏锐的洞察。

“我们在Google也使用氛围编程——我发现它非常适合原型、最小可行产品，对学习也很有帮助……”Osmani在11月初的一个播客中说道。“但在大多数情况下，氛围编程优先考虑速度和探索，而不是正确性和可维护性等因素。”

[![Addy Osmani shares Forrest Brazeal comic on Vibe coding vs rodeo cowboys](https://cdn.thenewstack.io/media/2025/11/21c50c0d-addy-osmani-shares-forrest-brazeal-comic-on-vibe-coding-vs-rodeo-cowboys.png)](https://cdn.thenewstack.io/media/2025/11/21c50c0d-addy-osmani-shares-forrest-brazeal-comic-on-vibe-coding-vs-rodeo-cowboys.png)

Osmani当时正在[Zed Industries的播客上发言](https://youtu.be/kvZGJVAZwr0?si=GBRpJBiB-_8GmxiP)（Zed Industries是一家成立于2022年的公司，旨在为程序员构建工具——并让流行的Atom文本编辑器以“Zed”之名复活）。他对AI如何影响编码世界有着独特的视角，这既来自于观察Google对AI工具的采用，也来自于行业内外的报告。

Google CEO Sundar Pichai[在四月](https://abc.xyz/investor/events/event-details/2025/2025-Q1-Earnings-Call/)表示，Google提交的代码中“远超过30%”是“人们接受AI建议的解决方案”。同月，[CNBC报道](https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html)称Microsoft CEO Satya Nadella估计“我们目前代码仓库和一些项目中的代码，可能20%到30%都是由软件编写的”。

但AI是否在制造更多问题，让程序员面临更长的代码审查和一系列新挑战，因为他们试图解决剩余的“70%问题”？

[![Addy Osmani interviewed by Richard Feldman - screenshot from Agentic Engineering (on YouTube)](https://cdn.thenewstack.io/media/2025/11/1d661ed0-addy-osmani-interviewed-by-richard-feldman-screenshot-from-agentic-engineering-on-youtube.png)](https://cdn.thenewstack.io/media/2025/11/1d661ed0-addy-osmani-interviewed-by-richard-feldman-screenshot-from-agentic-engineering-on-youtube.png)

## AI生成代码的欺骗性说服力

简而言之，Osmani在播客中表示，AI可以快速生成应用程序或功能的许多代码，但框架和明显的模式可能像以前一样耗时。这包括如何与生产系统集成等关键细节，以及“你的身份验证、安全性、API密钥……”，以及需要额外调试的边缘情况和问题。

通过几个提示获得用户界面“具有欺骗性的说服力……你可以得到一个看起来功能正常的东西。但你所知道的是，它可能在幕后是用胶带粘起来的。”

这可能反映在最新的开发者调查中。“尽管采用率处于非常好的水平，但信任度却出奇地低，并且正在下降……”Osmani补充道。“有许多研究，包括[Google的][DORA AI报告](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)，显示虽然采用率上升，但信任度确实下降了……对AI编码的良好评价在两年内从70%下降到60%。大约30%的人表示对AI生成代码几乎没有信任。”

“考虑到我们现在对它的依赖程度，这有点令人惊讶……”

[![Addy Osmani O'Reilly book cover - Beyond Vibe Coding (from Amazon)](https://cdn.thenewstack.io/media/2025/11/14fa5f4b-addy-osmani-oreilly-book-cover-beyond-vibe-coding-from-amazon-229x300.jpg)](https://cdn.thenewstack.io/media/2025/11/14fa5f4b-addy-osmani-oreilly-book-cover-beyond-vibe-coding-from-amazon-229x300.jpg)

9月，Osmani出版了一本新书，名为《氛围编程：编程的未来》。

## 解决AI辅助编程中的“70%问题”

那么，开发者应该如何解决最后的70%呢？Osmani说，一个根本的步骤是“花时间回顾并理解生成了什么”。

Osmani建议，也许有一种新流行的软件设计模式——“退两步”模式。（Osmani解释说，在使用你喜欢的工具生成最小可行产品后，“你感觉良好”，然后尝试“再抛出两三个提示”……）这通常会导致这样一种情况：微小的改动——比如修复一个bug——不知何故会让事情变得更糟。

“修复一个问题会破坏另一个东西，你将要求AI修复那个问题，然后它会制造另外两个问题。反复如此。有时是*五个*新问题。”

除了进行变量验证检查和能够回滚到先前状态之外，Osmani认为开发者仍然需要准备好自己修改代码库。“这始于理解生成的代码。”

这最终表明我们的工作流存在一个更大的问题。他还读过一些文章，警告“将AI用作拐杖”——我们可能不只不理解我们当前的全部代码库。 “我们基本的批判性思维能力，我们从错误中学习的能力，正在消失或被侵蚀。”

在九月纽约的[Lead Dev大会](https://leaddev.com/leaddev-new-york/)上，Osmani询问团队是否应该尝试无AI冲刺日，“只是为了保持这些技能的敏锐。”

但另一个想法是创建一个文件，记录一路上的决策和学到的教训，也许可以通过让代理“在每个任务后提炼见解”。对于你的AI代理来说，这形成了一个“复利学习循环”——但这不仅仅是提高下一轮AI提示的质量。它为你变成了一种记忆锚点，“一个你可以回去学习的文件……”

## 更好的上下文工程的重要性

这引出了他的下一个建议，它更直接地解决了“70%问题”。Osmani说：“我确实发现，投入精力充分理解[上下文工程](https://thenewstack.io/context-engineering-the-foundation-for-reliable-ai-agents/)的含义真的非常有用。”如果AI工具被赋予项目所有相关的背景信息，它们就能生成更好的代码。

一份[Anthropic文档](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)指出，上下文包括消息历史，也包括系统指令，以及外部数据和工具如何连接到外部系统。

Osmani说，这意味着“确保你的模型、你的代理、你的工具拥有成功完成任务所需的所有信息。这不仅仅是‘提示和祈祷’，而是尽可能将最多的信息最佳地放入你的上下文窗口中，以增加事情顺利进行的几率……”

“对于如今很多人使用的工具来说，我认为现在能够引入上下文会更容易一些——例如文档、URL、示例、任何可能包含有关问题或你的代码库或你的团队如何工作的额外上下文的Markdown文件。”

“我认为，对于那些试图超越70%瓶颈的人来说，这也是一个值得记住的有用之处。”

Osmani在Lead Dev大会上表示，这意味着编写代码测试变得更加重要，因为它们可以作为AI代理的反馈循环。

尽管如此，这里仍然适用同样的警示：人类需要对AI生成的任何测试有深刻的理解。“测试是一个安全网。它们降低了AI编码的风险。我倾向于认为，如果你足够幸运，你的团队在测试方面已经投入了相当长的时间。”

“如果你没有足够的测试覆盖率，那么有人会说‘好吧，我们可以直接用AI为我们编写测试’，这或许并不令人惊讶。只要有人类参与审查这些测试，那也没关系。”

“因为如果你认为自己可以通过提示来解决问题，我为你感到担忧。”（他笑了。）“我为你，朋友，感到担忧……”

## AI辅助编码真的能节省时间吗？

那么，归根结底，使用AI工具真的能让编码员提高生产力吗？Osmani看到了一些基于自我报告的生产力提升、Google内部调查甚至AI编写代码行数指标的估计——但他认为真正的提升……不到2倍。“这是一个我深感关注的话题，”他说。

当有人在Twitter上报告出奇高的数字时，“如果你仔细观察，通常这些公司都在全新的项目上进行绿地开发。他们没有技术债务，也没有传统软件工程通常伴随的所有包袱，而传统软件工程是在*真实*且已存在一段时间的项目上进行的。如果你是从零开始构建一些东西，那么从一开始你可能就不会遇到那么多固有的复杂性。”

## 代码审查如何成为新的瓶颈

这在现实世界中如何体现呢？“也许他们可以比以前多完成20%的任务。但我们也开始看到一些副作用……使用AI来提高速度意味着有更多的代码被‘扔’过来，而有人必须*审查*它。我们实际上开始看到代码审查正在成为新的瓶颈……这将是一个有趣的挑战，因为我们往往只有有限的高级工程师来审查这些代码。他们拥有有限的时间……我认为代码审查的模式还没有完全适应这个时刻。”

话虽如此，AI在某些方面确实非常有用。代理“作为学习伙伴实际上非常强大”——也许可以在编码休息时与它聊天，寻求新的视角和更好的方法。Osmani在回到旧代码库时也会使用它。“有时你会认为你对系统的工作方式有一个良好的心智模型，但几乎总是会有一些你可能遗漏或其他人随着时间添加的东西……尝试使用AI来形成更多这些连接——更多的节点——我认为作为一种学习辅助工具，它会非常非常强大。”

Osmani说，在与开发工具的不同公司交流后，“即将到来的是我们如何开始提供主动式AI编码建议……”

尽管他认为，这类工具要成熟到我们每天都在使用的程度，还需要一些时间……