<!-- 
# 大语言模型如何帮助网站改版
https://cdn.thenewstack.io/media/2023/08/59bd18e5-budgie-g2de6c95ce_1280-1024x682.jpg
Image via Pixabay.
 -->

GPT-4 Code Interpreter 的首次成功应用让人们对 LLM 能帮助普及脚本持有希望。

译自 [How Large Language Models Assisted a Website Makeover](https://thenewstack.io/how-large-language-models-assisted-a-website-makeover/) 。

这几周我的一个重要项目是[网站改版](https://thenewstack.io/using-llm-assisted-coding-to-write-a-custom-template-function/)，将两个现有网站合并成一个，并添加新的营销文献。我利用大型语言模型(LLM)[虚拟助手](https://thenewstack.io/elevating-the-conversation-with-llm-assistants/)团队来帮助编程和写作任务。这次我将讨论编程方面，下次再讨论助手如何帮助写作。

## 统一标题格式

其中一个遗留网站使用标题大小写：大多数单词首字母大写，例外的词有“a”、“an”、“the”等及专有名词。另一个网站使用句子大小写：只有首单词首字母大写。但实际上，两个网站都没有100%严格遵循这些规则。

我们选择了句子大小写。需要考虑 250 个标题，这是一个常见的挑战。手动修改会更快，还是编写脚本来自动转换更快？过去我总认为脚本会节省更多时间，而且老实说，有时这种赌注输了。构建自动化很有意思也很有趣，手动编辑是乏味的苦差事，所以这里存在一种适得其反的偏见。

如今我的工具包里有 LLM 助手，我认为它们可以提高我的胜算。我开始用一个严重不完备的提示，大意是：“这里有一些标题，请将它们改为句子大小写。” LLM 助手总是力求达到预期效果，所以它们立即开始编写脚本，通过对映射结果的肉眼检查就可以轻松验证。可轻松验证已成为一个指导原则：你必须检查结果，如果这个过程缓慢或困难，你就会输掉这个赌注。

经过探索各种 Python 库，包括 [spaCy](https://spacy.io/) (最终放弃了命名实体识别的尝试)，我们终于蹒跚前行，找到了 90% 的解决方案。然后，感觉到收益递减，我用手工完成了剩下的工作。虽然这不是最快的解决方案，但我认为如果没有辅助，结果也不会更快。而且如果我那样做，就无法快速浏览一些可能在其他时间有用的库。

有了映射，我只需要一个脚本遍历文件并应用转换。在编写简单脚本方面，LLM 表现出色，当然，我自己也可以编写，但需要花费时间和注意力，这些我更希望投入到更高阶的任务中。我们一直使用一次性脚本来组合解决方案，我不认为这会(或应该)改变。如果有什么改变的话，我希望 LLM 可以帮助普及编程——同样面临验证结果是否容易、快速和自信的约束。

现在让我们快进到完成练习后我编写的一个更有趣的提示。

```
Here is a sample of document names and titles, stored in a file called titles.txt. The format is:

2015-04-kms-integration.md:title: “Enterprise guardrails for AWS Key Management Service”

Write a script to convert the titles to sentence-case:

– initial cap
– preserve all-uppercase acronyms
– preserve an enumerated set of capitalized phrases

Here are phrases to preserve:

Key Management Service
Quick Actions
Turbot Guardrails

Here are tests it should pass.

(‘2015-03-turbot-initialized.md’, ‘Turbot Initialized’):’ Turbot initialized’
(‘2015-04-kms-integration.md’, ‘Enterprise guardrails for AWS Key Management Service)’: ‘Enterprise guardrails for AWS Key Management Service’
(‘2022-06-guardrails-hipaa-compliance-controls.md’, ‘HIPAA Compliance Controls’): ‘HIPAA compliance controls
(‘2022-08-guardrails-quick-actions.md’, ‘Turbot Guardrails Quick Actions’): ‘Turbot Guardrails Quick Actions’
(‘2016-07-nist-800-53-controls.md’, ‘NIST 800-53 Controls’): ‘NIST 800-53 controls’
(‘2022-02-pipes-for-audit-readiness.md’, ‘Pipes for Audit Readiness’): ‘Pipes for audit readiness’
```

## 招募 GPT-4 Code Interpreter

这对 GPT-4 Code Interpreter 模型的首次试用效果很好，它可以运行所写的代码，并自主迭代来找到解决方案。我的经历与 AI 专家 [Simon Willison](https://simonwillison.net/) 在[这个播客](https://www.latent.space/p/code-interpreter)中的描述一致:

> [01:32:42] 事实上，当它编写代码时，我看到它犯了我也会犯的同样错误，像出现偏差之类的。然后它输出结果时发现自己出错了，需要修正。所以它基本上是以我会编写的完全相同方式编写了代码，只是它的速度非常快，我只需坐回来看它工作就可以了。

下面是 GPT-4 编写的 sentence-case 函数的中间迭代版本。

![使用GPT-4代码解释器](https://cdn.thenewstack.io/media/2023/07/ffeba476-code-interpreter-1-744x1024.png)

我们看到 LLM 注意到了我最初也曾犯过的各种错误。它正在使用自行构建的测试(从我提供的测试数据)来发现这些错误。过去我也试过将测试输出反馈到循环中，但效果不佳。即使使用了大大改进的提示，Cody 和 Copilot 在编写能通过测试的代码方面也很困难。

GPT-4 代码解释器模型仍需要一些提示，但它确实成功了。诚然，只是在一个玩具问题上，但有很多类似的问题会占用时间和注意力。如果我们能快速可靠地解决它们，我们就可以把注意力集中在更大的问题上，在那里，我希望我们也能从生成/测试循环的自动化中受益。

## 一群随机鹦鹉的合唱

虽然我们已经使用了链接检查工具，但我还想再次检查，并好奇我能多快多轻松地在我的团队帮助下组建一个简单的检查器。这个工具组合的很好，在使用过程中，我想知道服务器返回的 header。当我请我的团队解释时，他们提供了各种有趣的解释。

![LLM 解释合唱](https://cdn.thenewstack.io/media/2023/07/d5ef84ca-choral-header-explanations-1024x837.png)

在 [Choral Explanations](https://hapgood.us/2016/05/13/choral-explanations/) 中，Mike Caulfield 描述了 StackExchange 和 Quora 等网站的问答过程如何提供一系列答案，读者可以从中综合理解。

> 这些“Choral Explanations”
>
> 1. 结合起来推动我获得单个解释无法达到的深刻理解，
> 2. 为我提供了多个进入内容的途径

我的随机鹦鹉团队可以产生这样的效果。如果 Copilot 说“任何来源都可访问资源”，我可能会想知道“源”的定义。当 Cody 补充说“来自任何域的跨源请求”时，我可以把“源”与“域”联系起来。GPT-4 则将这些概念与 CORS 联系起来。并不总是需要这种效果，通常你在寻找单一的最佳答案，但当你正在学习一个主题时，一群解释可以非常有帮助。

## 何时让合唱团安静

最后一个任务是找到一组需要重新设计的小图片。我的助手团队帮助我组装了一个基本脚本来扫描源树以查找图像，然后快速迭代几种不同的方法来提取图像尺寸。但用于生成包含那些图像的页面链接的转换证明很麻烦，在这种情况下，合唱更像是喧嚣。

最终，在花费过多时间尝试各种不令人满意的方法后，我让团队停止，自己完成了任务。与所有增强人类智能的技术一样，存在真正的萎缩风险。没有 GPS 的导航正在成为一门失传的艺术，没有 LLM 的编程也正在朝这个方向发展。

理想情况下，我们的助手会将我们从低级细节中释放出来，以便我们可以专注于更高级的推理，这通常就是发生的情况。但是，就像有时关闭手机并依靠死经验进行导航一样重要，知道何时让编程助手合唱团安静也很重要。
