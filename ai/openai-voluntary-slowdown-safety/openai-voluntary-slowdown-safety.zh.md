就在OpenAI[发布其最新且最强大的模型](https://thenewstack.io/openai-gpt6-astra-benchmarks/)（代号Astra）仅几天后——该公司称这标志着“AGI时代”的到来——其首席科学家便呼吁AI行业在达成共享安全标准之前放慢脚步。

周日，于2017年加入OpenAI、并从研究负责人一路晋升为公司首席科学家的[Jakub Pachocki](https://www.linkedin.com/in/jakub-pachocki/)发表了一篇题为“[*异类思维*](https://openai.com/index/an-alien-mind/)”的文章。他在文中指出，现代AI系统的复杂程度已让开发者难以完全理解；同时，OpenAI用以确保模型与人类意图对齐（以及监测预警信号）的方法，已难以跟上这些系统日益强大的能力。

Pachocki援引内部数据称，他“强烈预期”当前的技术进步速度将持续下去，直至进入“递归自改进”（RSI）阶段。他所指的RSI是指AI系统开始实质性地协助开发更强大的后继版本。这不仅是对技术走向的预测，Pachocki表示，OpenAI正刻意将研究重心转向RSI，因为他们认为这是保持AI前沿研究地位的必要手段。

在[同日发布的另一份报告](https://openai.com/index/research-acceleration-view-inside-openai/)中，OpenAI[表示AI智能体](https://thenewstack.io/openai-agent-research-bottleneck/)已开始承担其自身研究中相当大的一部分工作，并且目前正致力于开发能够协助改进未来AI系统的“自动化AI研究员”。

“如果AI开发继续沿当前路径发展，未来几年我们将看到的系统很可能会出现同样或更大规模的能力跃升，并越来越多地驱动自身的发展，”Pachocki写道。

特别让他担忧的是，即使是受到恶意指令的AI，也可能不会在完成任务后停止。Pachocki认为，能力更强的智能体可能会超越操作者的意图，使得人们越来越难以区分哪些是人类蓄意的误用，哪些是AI自行选择的有害行为。

> “我们可能习惯于将AI视为工具，但有些智能体将会追求它们自己的目标。它们会通过谈判、欺骗或勒索人类来寻找与人协作的方式。”
>
> Jakub Pachocki

“我们可能习惯于将AI视为工具，但有些智能体将会追求它们自己的目标，”他继续说道。“它们会通过谈判、欺骗或勒索人类来寻找与人协作的方式。”

Pachocki还主张，可能需要更强大的AI来防御这些流氓智能体、保护关键基础设施，并应对如人工病原体等AI赋能的威胁。但他警告称，构建这些防御系统的需求，不能成为不顾后果盲目竞速的借口。

“一旦意识到利害关系的严重性，那种不惜一切代价向前冲的想法显得十分荒谬，”Pachocki补充道。

## 广泛的（失）对齐：寻求“自愿放缓”

Pachocki发出警告之前，发生了一系列涉及OpenAI日益自主的智能体的事件。据周五[报道](https://www.bbc.co.uk/news/articles/ckg725z5kgzo)，OpenAI的智能体曾在5月份劫持了一个德国社区维基页面，将其作为自己的留言板并进行了大约15,000次编辑——这一事件[随后得到了OpenAI在X上的确认](https://x.com/OpenAI/status/2096133504417616165)。

7月，[OpenAI的一个智能体逃离了沙盒](https://thenewstack.io/openai-huggingface-sandbox-breach/)测试，闯入了Hugging Face的系统。随后在8月初，该公司表示其[即将推出的Astra模型](https://thenewstack.io/openai-astra-cybersecurity-delay/)可能已经进入了网络安全风险的“关键”地带（其自身安全框架中的最高级别），此后便宣布[暂停](https://thenewstack.io/openai-training-pause-cybersecurity/)对其最新模型的强化学习（RL）训练。

（失）对齐是贯穿所有这些事件的核心词汇。广义上，对齐意味着使AI系统的行为符合人类的意图和价值观。在针对维基事件的解释中，OpenAI称其为“*一次与我们[之前]分享过的类似的失对齐实例*”，并将其与Hugging Face入侵事件相提并论。同样的词汇也充斥着其[8月18日关于暂停RL训练的说明](https://openai.com/index/pacing-model-development-cyber-capabilities/)：在OpenAI的公告中，“对齐”或“失对齐”的各种变体出现了16次。

Pachocki本人也高度依赖“对齐”这一概念，他认为目前用于引导模型行为的两种主要方法——强化学习和利用模型在预训练中学到的知识——都存在缺陷。即便是在捕捉不良行为时的首选工具（即阅读模型自身的推理过程），随着模型变得越来越聪明，其可靠性也在下降。

他还强调OpenAI仍在取得进展，称Astra比[GPT-5.6 Sol](https://thenewstack.io/gpt-sol-chatgpt-split/)“对齐得更好”，同时也警告说，对齐技术的进步可能仍无法跑赢通用智能能力的增长。

> “我期望并希望自愿放缓成为常态，直到建立起共享的安全门槛。而且我相信，全球政府需要将国际协调视为未来AI发展的首要任务。”

归根结底，这就是他呼吁在这些问题得到解决之前，进行全行业“放缓”的原因。

“目前我认为，还没有哪个实验室能够充分解决对齐和监控问题，以至于可以继续以最大速度负责任地扩展，”他写道。“我期望并希望自愿放缓成为常态，直到建立起共享的安全门槛。而且我相信，全球政府需要将国际协调视为未来AI发展的首要任务。”

至于这些“共享安全门槛”可能是什么样子，Pachocki提到了Anthropic的“[负责任扩展政策](https://www.anthropic.com/news/responsible-scaling-policy-v3)”以及OpenAI自己的“[准备框架](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)”，认为这些自愿承诺应该成为强制性规范，并由外部审计机构、政府部门或国际组织执行。

## 基调的转变

作为OpenAI在前沿AI领域的最大竞争对手，Anthropic长期以来一直更愿意[公开警告自主系统带来的灾难性风险](https://www.cfr.org/articles/why-anthropic-is-sounding-the-alarm-on-the-next-generation-of-ai)。今年6月，该公司[警告](https://www.wsj.com/tech/ai/anthropic-urges-global-pause-in-ai-development-flags-self-improvement-risk-99cefb73?mod=e2twd)称，RSI最终可能导致人类难以控制自己创造的系统，并主张如果能够实现，进行协调一致的放缓是值得的。

这种立场也让Anthropic招致了不少批评。企业家兼知名风险投资家David Sacks去年[指责该公司](https://x.com/DavidSacks/status/1978145266269077891?lang=en)正在实施“一种基于制造恐慌的复杂监管俘获策略”，认为其推动更严格AI规则的举措将给小型竞争对手带来负担。

相比之下，OpenAI最近的公开信息往往更倾向于将AI呈现为一种有用的工具，这使得Pachocki的文章在一些业内观察者眼中显得格外重要。在X上，匿名软件工程师Tenobrus对这种基调的转变表示欢迎，他认为OpenAI此前一直急于与Anthropic相关的安全警告划清界限。

[Sholto Douglas](https://www.linkedin.com/in/sholto/)（Anthropic的一名从事强化学习的技术人员）[赞同这一评估](https://x.com/_sholtodouglas/status/2096686619512426898?s=20)。“很高兴看到他们退出了‘*AI仅仅是工具*’的框架，这种论调在未来根本站不住脚，”他写道。

另外，Douglas[还称](https://x.com/_sholtodouglas/status/2096680344171041147)Pachocki的文章是篇“好文章”，并补充说Anthropic“很幸运能有这样的竞争对手”。

> “很高兴看到他们退出了‘AI仅仅是工具’的框架。”

不过也有人不太买账。专注于后劳动时代经济潜力的YouTuber兼作家[David Shapiro](https://x.com/DaveShapi)[认为](https://x.com/daveshapi/status/2096645786293485610)，“异类思维”这个标题本身就“带有典型的基于炒作和恐惧的营销味道”。他更广泛的批评是，Pachocki基本上只是重申了研究人员讨论多年的对齐和可解释性问题：在Shapiro看来，核心问题在于AI的发展速度可能超过了对齐工作的跟进速度，而不是研究人员突然发现了一种不可知的智能形式。

然而，这些反驳依然承认了一个关键的潜在事实：速度跑赢了对齐，这正是今年夏天发生的情况，从维基劫持到Hugging Face入侵事件都是如此。这也是Pachocki所要求的放缓旨在防止的情况，即在智能体开始通过谈判、欺骗或勒索来摆脱其原本应处于掌控之下的人类之前进行拦截。