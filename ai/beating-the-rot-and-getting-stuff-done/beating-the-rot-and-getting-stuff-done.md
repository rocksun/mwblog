<!--
title: 使用GSD，在Claude Code中战胜上下文腐烂
cover: https://cdn.thenewstack.io/media/2026/01/8c7d1063-eden-constantino-ijg1yzsefqo-unsplash.jpg
summary: GSD扩展助Claude克服LLM“上下文腐烂”，通过产品导向提问智能规划项目，将模糊想法转为具体路线图及执行计划，提升LLM开发效率，摆脱“氛围编程”困境。
-->

GSD扩展助Claude克服LLM“上下文腐烂”，通过产品导向提问智能规划项目，将模糊想法转为具体路线图及执行计划，提升LLM开发效率，摆脱“氛围编程”困境。

> 译自：[Beating context rot in Claude Code with GSD](https://thenewstack.io/beating-the-rot-and-getting-stuff-done/)
> 
> 作者：David Eastman

迄今为止，我通常只在现有项目中使用LLM工具。尽管LLM付出了真诚的努力，但通过像Claude这样的智能体LLM，以“氛围编程”的方式从零开始创建详细项目的尝试往往会失败。它经常忘记信息或在非生产性循环中消耗令牌。

在这篇文章中，我将探讨流行的Claude扩展[GSD](https://github.com/glittercowboy/get-shit-done)，以及它如何应对[上下文腐烂](https://redis.io/blog/context-rot/)。

# **LLM领域的一些腐烂现象**

区分那些对现有模式的真正改进趋势和那些仅仅是为了规避当前限制的趋势是很重要的。处理“上下文腐烂”属于后者，因此它不应被视为仅仅是反映当前LLM技术现状的临时性解决方案。但它确实存在。

如今著名的论文[“Attention is all you need”](https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf)指导研究人员开发了能够理解意义并模拟理解句子结构的LLM。但是[研究](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf)确实表明，无论上下文窗口的大小如何，较早的令牌比后来的令牌获得更多的关注。因此，我们遇到了腐烂问题。

对于通常的短提示，这完全不是问题。但对于更长的任务，研究指出“注意力稀释”，就好像LLM是一个无聊的6岁孩子。对此的一个解决方案是将问题分解为子代理可以处理的任务，同时以某种方式保持整体上下文完整。

### 那么GSD是什么？

[GSD](https://github.com/glittercowboy/get-shit-done)（在本文中我将继续使用这个首字母缩略词）在Claude之上添加了一些元编程（被描述为一个上下文工程层）。我曾研究过早期的规范驱动系统之一[AWS的Kiro](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/)，但这与它不完全相同。

GSD通过提供一个内部任务规划框架来解决上下文腐烂问题，该框架明智地利用了Claude Code中已有的子任务。我将尝试用它来做一个小项目，看看效果如何。

正如我在关于[Claude Cowork](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/)的文章中描述的那样，过于雄心勃勃的项目最终只会变成令牌的篝火。因此，我将坚持我经常要求的功能——一个通过ID查看一组JSON对象的前端，就像它们是数据库一样。如果被问及，我将提供JSON模板。我不会指定特定的前端。

### 安装与规划

我通过npx安装了GSD：

![](https://cdn.thenewstack.io/media/2026/01/8cd46f7d-image-1024x802.png)

然后我从我的Warp终端在该目录中启动了Claude：

![](https://cdn.thenewstack.io/media/2026/01/628dfe65-image-1-1024x450.png)

然后使用了`/gsd:new -project`。（请注意，我使用的是Claude Pro，而不是API计划。）

![](https://cdn.thenewstack.io/media/2026/01/51eebba5-image-2-1024x286.png)

然后在GSD检查其启动条件后，~~审问~~提问开始了：

![](https://cdn.thenewstack.io/media/2026/01/245a06ec-image-3-1024x181.png)

注意底部的绿色百分比进度条，我假设它正朝着完成迈进。GSD启动了一个git仓库——所以我所要做的就是像上面那样定义项目。它很模糊，但足以开始对话。

项目的质量现在显然取决于我对GSD问题的回答质量。它们大体上是正确的问题，但数量很多：

![](https://cdn.thenewstack.io/media/2026/01/9b74131c-image-4-1024x323.png)

首先，它探讨了目标受众——这很像任何产品的发布。然而，在这种情况下，答案恰好是上面的第一个选项。这是为同事准备的。

我没想到下一个问题：

![](https://cdn.thenewstack.io/media/2026/01/0fed1d23-image-5-1024x474.png)

答案是多种多样的，但从技术上讲，它也可以是第一个答案；我想避免同事直接处理JSON文件。同样，下一个问题也很有针对性。我最初刻意的模糊性正在被仔细地揭示出来：

![](https://cdn.thenewstack.io/media/2026/01/922591d5-image-6-1024x476.png)

我没有提到用户是否需要编辑数据。这显然是好的，但可能会大大扩展项目。然而，将其设定为一个期望感觉是合理的。好的。

![](https://cdn.thenewstack.io/media/2026/01/5d25f63a-image-7-1024x27.png)

因此，虽然我从未明确说明该应用程序用于查看（我使用了“搜索”一词），但GSD智能地捕捉到了我的担忧。这就是GSD区分需求、阶段和总体规划的方式。

在描述了对象的类型、大致数量以及搜索如何开始之后，我们来到了目标平台的问题。因为我增加了编辑的总体要求，从而需要处理一组不一致的文件，所以我选择了桌面应用程序。它推荐了一个Web应用程序，如果仅仅用于查看，我肯定会同意。

到目前为止，我所做的只是回答一个明智的设计师会向一个早上醒来有一个自己无法实现的想法的经理提出的相同类型的问题。

第一个多选问题也（间接地）与CRUD有关：

![](https://cdn.thenewstack.io/media/2026/01/77d32bd7-image-8-1024x511.png)

为了易于使用，我还将目标操作系统固定为macOS。

最后一个规划问题让我深感好笑：

![](https://cdn.thenewstack.io/media/2026/01/af069461-image-9.png)

这强调了规划一个具有明确目的产品的重要性。我的同事使用这个应用程序始终是首要考虑。

它创建了一个[PROJECT.md](http://PROJECT.md)文件，并且令牌开始如预期般消耗。那个绿色的百分比行/拨盘似乎仍低于30%，这很有趣。它提交了自己的项目和元文件并继续工作。我让它“YOLO”（即非交互式）工作，并选择了“快速”规划。我还让它并行处理计划。

如果你即将问这个过程是否让我更深入地思考了我真正需要什么，答案是肯定的。“我没有选择研究选项，只是从规划开始实施。我也没有费心进行验证步骤。这些是推荐的，但会消耗更多的令牌。

总之，我们得到了这样的规划配置：

![](https://cdn.thenewstack.io/media/2026/01/dce358b9-image-10-1024x707.png)

然后它创建了一个版本1的计划，我将其定义为仅一个查看器，包含所有预期的基本查看功能。无需编辑。因此，我们达成了一套合理的v1要求：

![](https://cdn.thenewstack.io/media/2026/01/b7baba93-image-11-1024x522.png)

也可以说，如果我自己动手做这件事，现在我已经完成了一大半，但这就是开发者的困境。人类的氛围编程并不比让LLM来做更明智。我记得我最初拒绝了路线图，但我认为GSD忽略了我，还是制作了一个：

![](https://cdn.thenewstack.io/media/2026/01/55eb1507-image-12-1024x559.png)

因此，它创建了一个简单的路线图，包括阶段、目标、要求、标准和验证步骤。进度仍只有三分之一，但我们现在有了更多的文件。

GSD在不同阶段之间分配注意力，根据它从我的回答中收集到的信息创建了一个文档网络。

我们终于进入了执行阶段。

![](https://cdn.thenewstack.io/media/2026/01/0f7d6bb9-image-13-1024x632.png)

它选择了使用SwiftUI，这很好。并且创建了大量文件。但本周我们就到此为止。我从未使用过Swift，但这种编程形式的意义在于我的工作仅限于方向和规划，而非执行。

这是构建好的内容，附带验证步骤。我们下周将对此进行检查。

![](https://cdn.thenewstack.io/media/2026/01/bdc69542-image-14-1024x822.png)

### 结论

我们已经看到，Claude通过GSD能够进行详细的项目规划，从一个模糊的项目中提取出合理的步骤。不同之处在于，这种规划结构直接由GSD管理——它们不是由我定义的。

现在，为了推动这个过程，我确实需要理解规划是如何工作的，但问题显然是以“产品”为中心的。我们都没有直接提及CRUD等设计原则，我也从未明确讨论目标实现平台。

在我的下一篇文章中，我们将查看GSD刚刚开发的SwiftUI应用程序，并了解其性能。