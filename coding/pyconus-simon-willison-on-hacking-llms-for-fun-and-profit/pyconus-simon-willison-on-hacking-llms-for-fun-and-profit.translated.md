## PyCon US：Simon Willison 谈论如何黑进 LLM 以获取乐趣和利润

![PyCon US：Simon Willison 谈论如何黑进 LLM 以获取乐趣和利润的特色图片](https://cdn.thenewstack.io/media/2024/05/921d055f-vibes-1024x819.jpg)

![Simon Willison 在 PyCon US 上分享了他对使用大型语言模型的看法。](https://cdn.thenewstack.io/media/2024/05/5207aa71-simon-01-300x199.jpg)

**匹兹堡——**

[Simon Willison](https://simonwillison.net/) 是被广泛使用的 [Python Django 框架](https://thenewstack.io/what-is-pythons-django/) 的联合创建者，他最近将自己的创造力集中在了 [大型语言模型](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) (LLM) 上 [（最近）](https://x.com/simonw)。

他于周六来到 [PyConUS 2024](https://us.pycon.org/2024/)，发表了主题演讲，并鼓励 Pythonista 探索 LLM 的可能性。

当然，LLM 有局限性。它们 [编造东西](https://thenewstack.io/3-ways-llms-can-let-you-down/)，它们的答案 [可能反映出隐藏的偏见](https://thenewstack.io/threads-and-threats-when-computers-think-and-biases-emerge/)，并且 [难以投入生产](https://thenewstack.io/5-lessons-from-linkedins-first-foray-into-genai-development/)。但这并不意味着 LLM 没有巨大的潜力。

Willison 告诉观众：“仅仅因为一个工具有缺陷并不意味着它没有用。”“如果你了解它们的缺陷并知道如何解决这些缺陷，那么你可以用它们做很多有趣的事情。”

## LLM 是否通过了氛围检查？

Willison 已经摆弄 LLM 大约两年了。

Willison 说：“至关重要的是要记住，无论这些东西在与你互动时多么令人信服，它们都不是智能实体。”

LLM 基本上是巨大的自动完成机器。但是，事实证明，随着自动完成的规模扩大，它获得了一些非常有趣的特性。

Willison 说：“它能做的事情很诡异。”

LLM 是从大量抓取的数据（非法获取或其他方式）构建的，这些数据是从网络、维基百科、GitHub、电子书和科学文献库中抓取的。

![](https://cdn.thenewstack.io/media/2024/05/b1043833-llm-size-1024x819.jpg)

Llama 获取所有信息的地方。

尽管有这些大量的数据源，但收集到的所有数据的总和通常只有几个 TB。这是一个很大的集合，但并不笨重，以至于无法放在现代笔记本电脑上。

收集几个 TB 的源材料，花费一百万美元进行计算，你也可以拥有一个 LLM。

Willison 说：“如果你有资源，实际上并不难构建它们。”

“如果你了解它们的缺陷并知道如何解决这些缺陷，那么你可以用 LLM 做很多有趣的事情”

——Simon Willison

因此，现在有很多 LLM。你如何选择使用哪一个？

Willison 用于评估 LLM 的一个网站是 [LMSYS 聊天机器人竞技场](https://chat.lmsys.org/)，这是一个研究网站。在这个网站上，你提供一个问题，然后将该问题提供给两个 LLM。你评估每个 LLM 的答案。

竞技场跟踪 44 个 LLM，这是最后一次计数。一个 [排行榜](https://chat.lmsys.org/?leaderboard) 显示了哪些 LLM 领先于其他 LLM，仅就受欢迎的投票而言。

Willison 说：“这确实是评估这些东西的最有用工具，因为它捕捉到了模型的氛围。”氛围代表了响应可能有多么信息丰富和正常，至少对人类评委而言是这样。

截至周日，排名前三的 LLM 都是 GPT-4 变体；前 10 名主要由大型科技公司或初创公司创建的专有模型占据。但开放许可的模型正在上升，Meta 的 Llama 3 排名第 7。

据 Willison 说，这是一个好消息。

他说：“这不再是一种被防火墙锁定的技术。”我们现在可以在自己的硬件上运行这些东西，并且我们可以从中获得良好的结果。

他发现，例如，开放模型 [Mistral](https://mistral.ai/) 可以在 iPhone 上直接运行，即使没有互联网连接。

## 提示工程：“一大堆愚蠢的技巧”

但是对于初学者来说，使用 LLM 可能看起来令人生畏。

总的来说，LLM 只为用户提供一个命令行进行交互。

Willison 说：“这就像让一个全新的计算机用户进入 Linux，[只] 使用一个终端，然后告诉 [他们]，‘嘿，你自己弄清楚吧。’”

此外，他说，鉴于它们有时不可预测的行为，“使用这些东西实际上非常棘手，很难让它们做你真正想让它们做的事情。”

但是使用 LLM 一段时间后，你会发现 [提示工程](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/)，正如它所称，是一“一大堆愚蠢的技巧”。

以下是 Willison 建议的一些技巧。
## 首先，如果你将你试图解决的问题呈现为一个小剧本，会有所帮助。

你编写一个对话，其中用户询问一些内容——比如，可能的鹈鹕名称列表——然后计算机用一个鹈鹕名称列表进行响应，由 LLM 生成，然后 LLM 会编造出来。

“如果你给它一个小剧本，它会填补空白，”他说。

如果你为 LLM 提供一些补充材料，也会有所帮助。如果你想要关于特定主题的摘要，请在查询中包含你在网络上找到的所有其他关于该主题的内容。

“这些模型擅长做的事情之一就是根据刚给出的文本块回答问题，”他说。

另一个技巧：给他们完成工作所需的工具。奇怪的是，LLM 无法很好地完成两件事，而这两件事恰恰是计算机历来最擅长的：数学和查找内容。

![](https://cdn.thenewstack.io/media/2024/05/98a4da02-prompt-injection-300x240.jpg)

示例提示注入攻击。

因此，如果你有一个问题，即法国人口乘以 352 是多少，你可以使用指向维基百科和计算器应用程序的链接来准备 LLM。然后，指示它在维基百科上找到人口（6800 万），并拥有将该数字乘以 352 的工具。

Willison 承诺，添加第三方应用程序是让 LLM 摆脱束缚的方法，而且非常容易做到：“当人们对代理和类似的时髦术语感到兴奋时，他们谈论的都是这些。”

## 提示注入的工作原理

然而，添加第三方应用程序的缺点是围绕提示注入的安全问题，第三方可以在你的代码前面加上他们自己的恶意代码。

例如，个人聊天助手，一种当今正在构建的基于人工智能的常见应用程序，它可以通过语音命令预订航班或取消午餐会议（Google 最近

[推出了一款](https://assistant.google.com/)）。它很容易被第三方接管，第三方指示它更改密码并从其日志中删除操作。

“事实证明，我们不知道如何防止这种情况发生，”他说，并指出他创造了术语“提示注入”（如 SQL 注入）来描述这种安全攻击。

提示注入不是对 LLM 本身的攻击，而是对我们放在 LLM 之上的所有工具的攻击。虽然许多解决方案确实提供了一些保护，但没有人想出一种完全防止提示注入攻击的方法。但如果有漏洞，攻击者将找到利用它们的方法。

Willison 说：“永远不要让不受信任的文本——来自电子邮件和网络的文本——访问工具和私人信息。” “你必须将这些东西完全分开。”

## 构建以前无法构建的东西

Willison 本人根据他可以用它构建什么来评估任何新技术，而这些是他以前无法做到的。

他说，LLM “比我见过的任何其他东西都做得更好”。

OpenAI 正在其用户界面方面取得进展。Alpha 版本，

[代码解释器](https://365datascience.com/trending/chatgpt-code-interpreter-what-it-is-and-how-it-works/) 为 ChatGPT 提供了编写 Python 代码并将其放在 [Jupyter Notebook.](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) 中的能力。

Willison 用它绘制了阿迪朗达克公园的轮廓，该轮廓在

[GeoJSON 文件](https://geojson.org/) 中映射为一系列线段。他不得不回去两次并重复他的请求，才能在州地图上获得公园的完整轮廓。

使用 LLM，你很少会在第一次尝试时得到你正在寻找的答案。有时你可以添加明确的说明，有时你只需告诉 ChatGPT “做得更好”。

尽管进行了多次迭代，Willison 还是在大约三分钟内完成了该项目。

Willison 说，仅仅是 Willison 可以在几分钟内启动这些项目这一事实就打开了大门……通往许多其他副项目。

他还编写了一个计数器，实时监控他的 Pycon 演讲，统计他提到“AI”或“人工智能”的次数，并在演讲期间实时更新数字（在演讲屏幕的右上角）。

为了构建计数器，他只是询问 ChatGPT 的最新版本，

[ChatGPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/)，作为一名拥有 Mac 的 Python 程序员，他构建此类应用程序有哪些选择。

他要求提供多个选项。他指出，这一点很重要，因为 ChatGPT 通常只会给出一个答案，而该答案可能有效也可能无效。要求提供多个选项将为你提供更多选择。

他说：“它更有可能给你一个你可以使用结果。”
## 使用 ChatGPT 轻松构建 Python 应用程序

使用他之前从未听说过的 Python 音频翻译工具，ChatGPT 返回了一个几乎可用的 Python 脚本——在进行了一些微小的调整后，它确实可用。然后，他要求 ChatGPT 生成将计数器放在计算机屏幕上的代码。

“这三个提示给了我我所需要的，”他说。总共投入的时间？大约六分钟。

如果他要花半天时间对这个功能进行编码，他不会费心。但在不到 10 分钟内就能完成？

他说，这种易用性“促成了我以前从未考虑过的所有这些项目”。

## 不是生成式而是变革性

威利森推测，[生成式 AI](https://thenewstack.io/ai/) 可能不是这些技术的最佳名称。它表明机器可以产生大部分垃圾。他说，一个更好的名称应该是“变革性 AI”。

“最有趣的应用程序是当你向其中输入大量文本，然后使用它来评估和根据它做事情时，这样你就可以进行结构化数据提取，”他说。“诸如此类的事情不太可能产生幻觉。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、采访、演示等。