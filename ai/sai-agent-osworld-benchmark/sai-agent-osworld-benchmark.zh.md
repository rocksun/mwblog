**由 [Simular](https://www.simular.ai/) 构建的计算机智能体 [Sai](https://www.sai.work/) 在周四发布的 [OSWorld 2.0](https://osworld-v2.xlang.ai/) 基准更新中取得了 73% 的成功率**。该评分基于包含 108 项任务的基准测试，这些任务评估的是通常需要熟练人类花费超过 1 小时才能完成的日常、冗长的专业工作。

Simular 表示，这种 SOTA（业内领先）的表现“使 Sai 领先于”成功率为 62.57% 的 GPT-5.6 Sol（据 OpenAI 报道）和成功率为 70.57% 的 Opus 5（据 Anthropic 报道），同时“Sai 在达到顶峰”时，成本仅为前两者的大约 2/3。

Sai 的设计和构建旨在 [专注于现实世界的办公任务](https://thenewstack.io/agents-last-exam-benchmark/) 和功能，而非单纯追求行业赞誉下的无限吞吐量。Sai 可在完整的桌面应用程序和网页上运行、[调用 API](https://thenewstack.io/the-state-of-api-management-in-an-age-of-ai-insecurity/) 并编写代码。

该智能体结合了前沿模型与专用模型，通过专用接口感知用户计算机并采取行动，以该公司承诺的“对个人”和企业而言“可负担的成本”执行复杂的现实任务。

## 为常规（但必要）工作构建的计算机智能体

Simular 的联合创始人兼 CTO [Jiachen Yang](https://www.linkedin.com/in/jc-yang/) 告诉 *The New Stack*，他认为为每个人的常规（但必要）工作（例如招聘外联、验证发票、研究最新新闻）而构建的计算机智能体，“不应该让你掏空钱包”，仅仅因为“底层模型被训练去解决地球上未解的[开放数学猜想](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)”，或类似的旨在展示原始工程能力的追求。

“后人会觉得人们现在还在那样构建模型是可笑的，”Yang 说。“Sai 在 OSWorld 2.0 上实现的成本与结果的最佳权衡，是迈向未来的一步，即我们不需要为了完成工作而忍受高昂的价格。”

> “后人会觉得人们现在还在那样构建模型是可笑的。Sai 在 OSWorld 2.0 上实现的成本与结果的最佳权衡，是迈向未来的一步，即我们不需要为了完成工作而忍受高昂的价格。”

Simular 于今年 3 月首次发布了 Sai。这家总部位于帕洛阿尔托的公司称自己为一家“专注于研究的智能体创业公司”，由前 DeepMind 科学家 [Ang Li (CEO)](https://www.linkedin.com/in/angli-ai/) 和 CTO Yang 创立。

该公司采用了[神经符号方法](https://www.simular.ai/articles/the-power-law-of-practice-is-absent-from-agents)，即神经网络灵活的探索能力与符号代码的精确性相结合；这意味着已解决的任务可以（隐喻地和字面上）编码为可重用的代码，每次以相同的方式重放。底线很简单：处理第一百张发票的成本并不像第一张那样高。

## 什么是 OSWorld 2.0 计算机使用智能体基准？

[OSWorld 2.0 于 6 月 26 日推出](https://xlang.ai/)（并随后于 8 月 8 日更新），由香港大学 HKU NLP Group 下属的可执行语言基础（[XLANG](https://xlang.ai/blog/xlang-intro)）实验室开发。据说它已经超越了其第一代中评估简短、简单桌面测试的阶段。Simular 提醒我们，其开源的 Agent S 是去年 12 月在 OSWorld 1.0 上[首个超越人类基准](https://www.simular.ai/articles/simulars-computer-use-agent-outperforms-humans)的智能体。

![](https://cdn.thenewstack.io/media/2026/08/2c691b10-sai-benchmark-1024x576.png)

当被问及为什么 Sai 的结果不像在 OSWorld 1.0 上那样在 OSWorld 2.0 的官方网站上可见时，Simular 表示：“公司或组织首先在其网站上发布基准测试结果并不罕见（参见 [Anthropic](https://www-cdn.anthropic.com/ceaf5c7ff2783855203fde8208ec311252dced5b/Claude%20Opus%205%20System%20Card.pdf) 和 [OpenAI](https://openai.com/index/gpt-5-6/)）。我们正在提交给 OSWorld 2.0 排行榜，并将我们的轨迹上传到 [Hugging Face](https://thenewstack.io/openai-huggingface-sandbox-breach/)。”

与 OSWorld 1.0 基准不同，OSWorld 2.0 的任务是以小时而非分钟来衡量的。它们提出了现实生活中的挑战，例如跨多个数据源查找和推理（例如，散落在电子邮件和费用报告中的收据）、响应动态环境变化（例如，任务进行到一半时收到的消息）、精确遵循教程（例如，报销指南）以及排查信息差异（例如，相互矛盾的数据）。

Simular 团队认为，这是目前业内最稳健的开放基准，最能反映现实世界的任务。

Yang 和团队解释说，Sai 之所以能实现更好的结果与成本权衡，得益于上述的神经符号规划。这意味着 Sai 通过在每回合采取更多动作，平均比纯模型少使用约 1.5 倍的模型调用，使用 [Simulang 代码](https://docs.simular.ai/simulang/simulang-claude-code)（一种用于 macOS 桌面自动化的 Claude Code 技能）作为规划和执行更长子任务的符号语言。

## Sai 是如何为效率而设计的？

为了提高缓存和内存效率，Sai 通过自适应摘要（一种保持模型上下文窗口较小的动态内存管理技术）将输入大小限制在一定范围内，并在摘要前尽可能长时间地保持恒定的提示前缀。通过代码规划，Sai 能够在整个任务执行过程中在运行时内存中维护和访问关键的任务信息。

对于模型编排，Sai 调用专用模型和接口来定位 UI 元素、执行纯推理并进行验证，从而避免在不需要完整任务上下文的步骤中使用昂贵的模型。

Sai、Sol 和 Opus 在 OSWorld 2.0 上通过玩 [Chrome Dino](https://youtu.be/ZKB8e4r1aVk) 进行了测试，这是一款重复的实时游戏，并需要在实时页面上清除分数目标。Sai 将重复的实时游戏视为一个编程问题，而不是一个点击问题。Sai 从原始像素中测量地面线、障碍物速度及其自身的输入延迟，然后编写了一个捕获屏幕、检测障碍物并跳跃的控制循环，并在单次执行调用中在虚拟机上运行它。

这些智能体还被要求在 OSWorld 2.0 上执行任务 28，即所谓的 [疫苗预约](https://www.youtube.com/watch?v=I6d-m2qtoR0)，其中涉及获取关于所需免疫接种的电子邮件、桌面上的扫描疫苗接种记录，以及具有价格、距离和日期约束的预约网站。

## 开发人员如何看待 Sai？

硬核机器学习计算机科学家 [Santiago Valdarrama](https://www.linkedin.com/in/svpino/) 似乎是一位粉丝；他在 [LinkedIn 上写道](https://www.linkedin.com/posts/svpino_the-secret-nobody-tells-you-about-agents-activity-7436846582752432128-eBaw/)：“因为 Sai 在完整的桌面上运行，而不仅仅是浏览器或 API，它可以处理阻止标准自动化的应用程序。这开启了一整类大多数智能体无法触及的任务。”

> “因为 Sai 在完整的桌面上运行，而不仅仅是浏览器或 API，它可以处理阻止标准自动化的应用程序。这开启了一整类大多数智能体无法触及的任务。”

也许更平衡的观点（并在回应 Valdarrama 最初的标记时发布）来自 AI 收入系统专家 [Baljinder Lally](https://www.linkedin.com/in/baljinder-lally-11b93585/)，他指出 Sai 的到来“与我迄今为止构建智能体工作流所看到的情况相符”。但他提醒说：“演示看起来很棒，但可靠性来自于护栏、[可观测性](https://en.wikipedia.org/wiki/Observability)和人在回路中的检查点。”

[AgenticMode AI](https://www.linkedin.com/company/agenticmodeai/) 的创始人 [Jahanzaib A.](https://www.linkedin.com/in/jahanzaibai/) 的观点同样平衡。他说他在语音智能体上也遇到了同样的可靠性问题。“它们在每次演示中都表现出色，然后在生产中的边缘情况下静默失败，没人预料到。[可观测性](https://en.wikipedia.org/wiki/Observability)部分就是一切——没有它，你只是在盲目地调试，”他写道。

## 通用“直线加速赛”中的智能体

Simular 坚持其研究是基于具有经济价值的工作，而不是演示。该公司表示，这意味着它了解“计算机智能体的整个堆栈”，即模型、规划和基础、脚本层、智能体运行的虚拟机以及用户界面。

该公司的底线是“Sai 是为每个人准备的，而不仅仅是一个实验室结果”，这反映了一套新兴的模型是如何被构建以专注于有形的、可交付的办公任务，而不是参与某种计算、吞吐量和分析的通用“直线加速赛”。