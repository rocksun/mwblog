## 使用人工智能改善糟糕的商业写作

![使用人工智能改善糟糕的商业写作的特色图片](https://cdn.thenewstack.io/media/2024/03/3cd75438-sticker-mule-b6-8hwbrjz4-unsplash-1024x683.jpg)

我曾经教授说明文写作，并且长期以来一直认为软件工具应该能够帮助人们学习如何更清晰、更有效地写作。在 [之前的帖子](https://blog.jonudell.net/2022/08/13/how-to-rewrite-a-press-release-a-step-by-step-guide/) 中，我将核心原则应用于一篇典型的写得很糟糕的新闻稿中——省略不必要的词语、使用主动语态、避免行话和陈词滥调、引用具体示例。该帖子讲述了一个循序渐进的转变过程，在 [配套帖子](https://blog.jonudell.net/2022/08/27/github-for-english-teachers/) 中，我将其转换为一个 GitHub 拉取请求，使学习者能够 [逐步](https://github.com/judell/editing-step-by-step/pull/1/commits/effd1ecb3de10d4c38af9b5f0fe65436898deb00) 进行更改并逐个查看，其中包含带注释的彩色差异，解释了每次更改的原理。

我希望能够让老师们创造出那种类型的指导体验，但是，尽管该帖子的标题充满希望——

*GitHub 适用于英语老师*——但现实是 GitHub 不适用于英语老师，而且我认为当前一代的 LLM 无法弥合这一差距。不过，我认为它们可能有助于我们解决糟糕的商业写作这一祸害，因此为了验证这一假设，我尝试用我的循序渐进的示例 [提示](https://gist.github.com/judell/55923aee9143721e715fd207045d7c62) 提示 ChatGPT、Claude 和 Gemini，并要求它们应用它所阐述的原则。

在最初的试验中，我向三个 LLM 展示了我的原始示例新闻稿。即使它们“知道”答案，因为提示同时包含原始版本和重写版本，并且将后者指定为目标，但所有建议的重写都与我的重写大不相同。LLM 改进了原始版本，但幅度不大。经过反思，这很有道理——它们的训练集肯定包含更多糟糕的示例，而不是好的示例。如果你来自软件背景，从相同的输入中引出如此不同的输出会令人不安，但事实就是这样。这样做有很多好处，但如果你需要确定性的行为，那么这不是适合你的技术。

我以为我已经接受了 LLM 的非确定性，但看到同一 LLM 在不同的聊天会话中结果差异如此之大，仍然有点惊讶。

[与大型语言模型合作的最佳实践](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) 中的规则 4（*要求合唱解释*）适用于 LLM 内部以及 LLM 之间。这些东西包含很多内容；值得尝试多次做同一件事，挑选你最喜欢的结果，并结合几个结果中的元素。

过去，我觉得 Claude 是比 ChatGPT 更好的作家和编辑，但模型一直在变化，这次它们都没有成为明显的赢家。Gemini 也没有。似乎最好的改进和最糟糕的失败都可能发生在任何地方，并且对于 LLM 内部与 LLM 之间的试验，没有明显的差异。当我使用我尚未进行专家重写的另一个示例新闻稿重复试验时，结果也是如此。

## 隐式与显式控制流

我设想中的写作助手是一个会话伙伴，可以帮助作家逐步完成重写工作。因此，提示指示 LLM 一次执行一个步骤，显示更改段落的修改前和修改后版本，说明更改的原理，并询问作者是否继续下一部分或暂停讨论其他措辞。所有三个 LLM 都做得很好，如果你尝试明确地对这种交互进行编码，这令人印象深刻。使用它们的 API 可以做到这一点（你可以使用退出条件构建编程循环），但要达到 LLM 可以自然创建的效果，需要花费更多的时间。

当然，在这个实验中的会话流非常基本。LLM “假设”逐步重写意味着修改标题，然后依次修改每个段落。这不是我的工作示例进行的方式。它完全省略了第一段（因为它只重复标题），并重新组合其他元素以生成一个最终版本，该版本在结构上和逐行基础上都不同于原始版本。局部行编辑可以激发全局重组，反之亦然。我不知道是否可以将 LLM 支持融入到指导体验中，以捕捉现实世界编辑的这种细微差别，但如果是这样，我怀疑它将需要基于 API 的指数级更困难的方法。或者是一组全面的带注释的修改前后示例。或者两者兼而有之！
无论你对逐句对话施加何种程度的控制，在任何时候进行开放式对话的能力都是与 LLM 交互的基础。可汗学院的 Khanmigo 很好的证明了这一点。如果你还没有尝试过，我强烈建议你注册一门课程并尝试一下。选择一些你很久没有学习的东西，就我而言是 AP 生物学，完成一些讲座和阅读，参加一些测验，然后激活 Khanmigo。

护栏令人印象深刻：它了解你的课程背景，并将邀请你参加一些相同的测验，它通过对话而不是多项选择进行测验。如果你问一个随机问题（“那些红袜队怎么样？”），它会告诉你坚持生物学。但你随时可以暂停提问以加深你的理解。有一次，在关于水作为通用溶剂的部分中，LLM 提到了水会溶解油脂等非极性物质。因为我的高中生物学已经非常生疏了，所以我问：“给我举五个极性和非极性物质的例子。”它做到了，并且在我询问时给出了更多示例。稍后，我询问并收到了脱水合成和水解的示例。我希望我能够时光倒流，在高中和大学期间重新获得那种耐心和有益的帮助。

事实上，我是一个高度自觉的学习者，奥黛丽·沃特斯会将我描述为 [漫游自学者](https://medium.com/@audreywatters/roaming-autodidacts-and-entrepreneurial-l-earners-the-stories-we-tell-about-lifelong-learning-6172060539d4)。这种学习方式并不是常态。许多学习者需要——而且大多数教师的目标是提供——一种更有条理的体验。但可汗学院取得了很好的平衡。脚手架一直都在那里：与标准框架相一致的教学大纲、可重复的评估，使学生能够按照自己的节奏掌握知识，以及仔细的进度监控。然而，在任何时候，学习者都可以提问，以便以对他们最有意义的方式重新构建材料。指导者永远不会变得不耐烦，其他同学也永远不会感到不便，这太棒了。

不过，如果你从不费心问这些问题，你将永远不会有那种经历。当我与 [我的助理团队](https://thenewstack.io/elevating-the-conversation-with-llm-assistants/)一起完成重写练习时，我敦促他们遵守他们试图（并且经常失败）展示的原则。这使得结果比他们原本可能达到的要好得多。而且，挑战助理们更好地简化、澄清和激活散文是一件很有意义的事情。在课堂环境中，在老师和同学面前不会这样做的人，更有可能在与耐心和乐于助人的 [学习伙伴](https://thenewstack.io/learning-while-coding-how-llms-teach-you-implicitly/)的私下对话中获得这种体验。如果可能的话，始终需要提供完全指导的体验。但是，当学习者弄清楚为什么以及如何挑战和质疑 LLM 时，他们将更多地控制自己的学习方式。反过来，学习体验提供者可能能够用更少的脚手架覆盖更多领域，而这些脚手架的创建和维护成本很高。

## 展示差异

如果你从 [这里](https://github.com/judell/editing-step-by-step/pull/1/commits/de67cf6b75f0de9da82b821e82ed1d8457fb7562)开始，并使用“下一步”按钮逐步完成更改，你将看到通过比较每次细粒度修订的前后状态而产生的强大效果。我设想中的写作助手将能够做到这一点。尽管我发现 LLM 在生成和转换 HTML 方面非常出色，但没有一个接近该目标。

不可否认，这是一个艰巨的挑战。我再次怀疑，最适合采用基于混合 API 的方法，该方法调用 LLM API 来生成前后对，然后调用传统 API 来比较它们并发出颜色编码的差异。

## 渠道斯特伦克、怀特和奥威尔

尽管我制作了一个 GPT，其中包含我在本练习中使用的提示，但我不会像推荐 [Strunk & White](https://www.amazon.com/Elements-Style-William-Strunk-Jr/dp/020530902X)和 [Orwell](https://www.orwell.ru/library/essays/politics/english/en_polit)那样推荐它。
[Pipeline Test Writer](https://thenewstack.io/creating-a-gpt-assistant-that-writes-pipeline-tests/), which operates in a narrower domain and adheres to Rule 2 ([Never trust, always verify](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)). It’s quick and easy to verify that a workflow pipeline test is producing the expected results. It’s much harder to verify that a business communication rewrite has achieved its goal. If it’s even possible, I suspect it would require a massive corpus of before-and-after example texts, in addition to the kinds of instructions I wrote in the prompt. Still, it’s worth a try! Badly written business communications are a pain point for everyone, and a systematic way to improve them — even incrementally — would be a godsend. In the meantime, I’ll reiterate a few tips that [have proven consistently useful](https://thenewstack.io/should-llms-write-marketing-copy/). I now think of them as Strunk & White variations and George Orwell variations. **Strunk & White**: I’m going to show you a marketing document. Please revise it according to Strunk & White: omit needless words, favor short Anglo-Saxon words over long Latinate ones, use the active voice. **George Orwell**: Please evaluate this marketing document against the writing guidelines that George Orwell set out in his essay “Politics and the English Language.” What passages would make him cringe? Armed with these prompts, my LLM assistant was able to do a pretty good job of stripping vague jargon and turgid phrasing from a poorly written press release, as in this exercise. I recommend them to writers of press releases or any other marketing copy as a first step toward clearer, more effective business communications. [YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) Tech moves fast. Don’t miss a single episode. Subscribe to our YouTube channel to stream all of our podcasts, interviews, demos, and more.