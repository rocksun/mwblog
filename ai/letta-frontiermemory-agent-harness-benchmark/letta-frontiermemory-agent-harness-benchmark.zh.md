AI智能体在记住过去对话和早期任务方面正变得越来越好，但记住某些东西并不能保证智能体下次能利用它把工作做得更好。Letta于周三发布的新FrontierMemory基准测试通过衡量智能体能否从经验中学习，而不是仅仅检索存储的信息，来测试这一差距。早期结果显示，各个智能体框架（即管理智能体运作方式的基础设施）的性能存在巨大差异。

[Letta Dream 以 73.3% 的得分名列榜首](https://frontiermemory.com/blog/v1/)，Prime Agent 以 60% 紧随其后。OpenAI Agents SDK 得分为 40%，而 Claude Managed Agents 和 Hermes Agent 则分别以 33.3% 和 26.7% 落后。

## 回忆不等同于学习

Letta 联合创始人兼首席执行官 [Charles Packer](https://www.linkedin.com/in/charles-packer/)[在 X 上](https://x.com/charlespacker/status/2112972810687823985)写道：“现代‘‘记忆’基准测试已经饱和，因为它们衡量的是对事实的回忆。”他表示，在编码框架和 bash 循环时代，回忆问题已经得到解决，而在 Token 空间中的持续学习（即通过智能体保留的上下文进行学习，而不是通过权重更新进行学习）仍然未得到解决。

Letta 的另一位联合创始人 [Sarah Wooders](https://www.linkedin.com/in/wooders/)[也在 X 上指出了另一个问题](https://x.com/sarahwooders/status/2112964548533907613)。大多数编码和知识工作基准测试评估的都是不相关的任务，并且会预先提供所有必要的上下文。但这并不是人们实际工作的方式。Wooders 将其比作开始一份新工作：新员工需要大量的指导，而呆了多年的员工通常只需很少的解释就能完成工作。

> Packer 的前提是，“如果 AI 生成的记忆是好的，它实际上应该改善下游任务的性能。”

FrontierMemory 采取了不同的方法。智能体接收早期工作的记录（包括成功和失败的尝试），然后生成自己的记忆来帮助完成后面的任务。Packer 的前提是，“如果 AI 生成的记忆是好的，它实际上应该改善下游任务的性能。”开发人员已经接受了这一基本理念，他们通过将语言模型与记忆系统和反馈循环配对，构建了[持续学习的智能体](https://thenewstack.io/how-to-build-ai-agents-with-lifelong-learning/)。

Letta 重新设计了现有的编码和知识工作测试，使智能体必须使用从先前任务中学到的知识，而不是一切都为其明言。在审查并修复了原始测试的问题后，Letta 将 FrontierMemory 1.0 缩减为仅 15 个任务。

## 框架优于模型

框架本身可能和运行在其中的模型一样重要。Letta 测试了五个智能体系统，以查看它们从先前工作学习并在新任务中应用这些经验教训的能力。

> 框架本身可能和运行在其中的模型一样重要。

当两者都使用 GPT-6.1 Sol 创建记忆并使用 GPT-6 Sol 完成任务时，Letta Dream 以 60% 对 40% 的优势击败了 OpenAI Agents SDK。使用 Claude Opus 5.5 时，结果差距甚至更大。Dream 得分为 73.3%，Prime Agent 达到 60%，Claude Managed Agents 则为 33.3%。

Packer 表示，智能体处理 AI “做梦（dreaming）”的方式产生了很大的不同。“做梦”是指智能体回顾过去的工作，并将学到的东西转化为稍后可以使用的指令或记忆。他还指出 Prime Agent 表现优于 Hermes Agent，这是这些系统差异有多大的另一个例子。但也有一个缺点：如果不检查保存的内容，智能体就会冒着[学习并重复坏习惯](https://thenewstack.io/anthropic-agent-memory-dreaming/)的风险。

FrontierMemory 还比较了七个前沿模型生成有用记忆的能力。Anthropic 的 Claude Opus 5.5 和 Z.ai 的 GLM-5.3 以 73.3% 并列第一，Kimi K3 以 66.7% 紧随其后，OpenAI 的 GPT-6.1 Sol 和谷歌的 Gemini 4 Argon 均得 60%。Muse Wonder 达到 46.7%，Grok 4.7 以 33.3% 收尾。Packer 表示，Opus 5.5 和 GLM-5.3 在生成有用记忆方面明显优于 GPT-6.1 Sol。

> Packer 表示，Opus 5.5 和 GLM-5.3 在生成有用记忆方面明显优于 GPT-6.1 Sol。

## 记忆更便宜，分数更低

但 OpenAI 具有巨大的价格优势。GPT-6.1 Sol 每个任务的估计成本为 0.77 美元，而 Opus 5.5 为 2.80 美元，GLM-5.3 为 3.58 美元。因此，虽然 OpenAI 得分较低，但运行成本要便宜得多。

Letta 使用其 Dream 框架通过每个模型创建记忆，然后测试这些记忆在 Letta Code 中运行的任务上的工作情况。结果显示了更好的记忆、更强的性能和更低的成本之间的权衡。

## 可以迁移的记忆

Letta 还研究了某些记忆比其他记忆工作得更好的原因。在涉及公司定价数据的一项测试中，Opus 5.5 创建了一个技能，告诉智能体何时使用某些信息。GPT-6.1 Sol 创建了四个单独的技能，但智能体从未找到它需要的那个。

Gemini 4 Argon 犯了另一个错误。它记住了特定的文件大小，当下一个任务涉及不同的文件时，这没有多大帮助。相反，Opus 5.5 告诉智能体检查常规文件和电子邮件以获取信息。即使任务改变，这也管用。Opus 5.5 创建的记忆帮助 GPT-6 Sol 完成了任务，这表明开发人员可以使用更昂贵的模型来建立记忆，并使用更便宜的模型来完成工作。

其他开发人员也注意到了这一点。在 Letta 的 Sarah Wooders [在 X 上发布有关该基准测试的信息后](https://x.com/sarahwooders/status/2112964548533907613)，OpenClaw 账号回应称，希望为其平台看到一个插件。该账号表示，其多人游戏环境将是测试基准测试的有趣场所，这引发了当多个智能体共享同一框架时记忆如何运作的问题。

“是的，当然——很想将 OpenClaw 添加到框架比较中！”Wooders 写道。“扩展到多人游戏记忆也是一个非常有趣的未来方向。”

## 基准测试忽略了什么

FrontierMemory 仍处于早期阶段。只有 15 个任务且每个任务只有一次尝试，单个结果就可以使分数改变约 6.7 个百分点。该基准测试目前侧重于智能体从过去的工作中学习，而不是在进行过程中更新记忆。Packer 表示，下一个版本将添加运行时间更长的任务和在线记忆更新。