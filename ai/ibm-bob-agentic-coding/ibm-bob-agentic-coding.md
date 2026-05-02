<!--
title: “别开着法拉利去买牛奶”：IBM Neel Sundaresan 谈 AI 代理 Bob 的实战逻辑
cover: https://cdn.thenewstack.io/media/2026/05/c4c2637a-screenshot-2026-05-02-at-08.21.15-1024x683.png
summary: GitHub Copilot 奠基人 Neel Sundaresan 现任 IBM 高管，他推出的 AI 代理 Bob 已在内部拥有 8 万用户。文章探讨了其开发背景，并着重介绍了如何通过智能路由解决 AI 成本浪费问题。
-->

GitHub Copilot 奠基人 Neel Sundaresan 现任 IBM 高管，他推出的 AI 代理 Bob 已在内部拥有 8 万用户。文章探讨了其开发背景，并着重介绍了如何通过智能路由解决 AI 成本浪费问题。

> 译自：["Like taking your Ferrari to buy milk": IBM's Neel Sundaresan on the case for Bob](https://thenewstack.io/ibm-bob-agentic-coding/)
> 
> 作者：Darryl K. Taft

[Neel Sundaresan](https://www.linkedin.com/in/neel-sundaresan-a964a2/) 有三个问题从不回答。其中一个，他带着些许笑意说道，就是为什么 IBM Bob 被命名为 Bob。

这种特别的回避很有深意。Sundaresan —— IBM 软件部自动化与 AI 总经理、[Microsoft GitHub Copilot](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) 的创始工程师，以及此前在 [IBM](https://thenewstack.io/ibm-tackles-shadow-ai-an-enterprise-blind-spot/) 担任的研究员 —— 他不是那种产品营销人员。他是一名从研究员转型的构建者，再转型的管理层，贯穿这三个角色的主线是同一个痴迷点：[如何让软件开发者更高效](https://thenewstack.io/how-google-unlocks-and-measures-developer-productivity/)，而又是什么在阻碍效率？

他自 2000 年起就在研究这个问题，那时还没有 Transformer，没有[大语言模型](https://thenewstack.io/introduction-to-llms/)，当时除了小众研究社区外，没人会把 AI 和开发工具放在同一个句子里。从那时起到 IBM Bob —— [**本周发布且已在 IBM 内部拥有 80,000 名用户**](https://thenewstack.io/ibm-bob-agentic-development/) —— 的发展历程，比发布新闻稿中描述的要漫长得多。

## 在聚光灯亮起之前开始

Sundaresan 为提升开发者生产力构建的第一个系统，与我们今天所认知的 AI 编程工具截然不同。那是一个 API 调用的推荐系统。

“30% 的开发者代码是 API 调用，”他在一次广泛的采访中告诉 *The New Stack*。“如果你输入一个类名加点号，会得到一长串待调用的函数列表，你必须从中挑选。这本身就是一个摩擦点。”

![](https://cdn.thenewstack.io/media/2026/05/428cd83c-screenshot-2026-05-02-at-08.18.19-1024x487.png)

*Sundaresan 站在 IBM Bob 吉祥物旁边。（图片来源：Sundaresan 的 LinkedIn 个人资料）*

当时的目标不是生成代码，而是在正确的时刻呈现正确的函数调用 —— 本质上是将搜索排序问题应用于开发者的自动补全体验。

那个模型不是 Transformer，甚至不是现代意义上的深度学习模型。但他表示，开发者们非常喜欢它。那个早期的信号 —— 即在开发工作流中特定、细微的时刻减少摩擦，能产生巨大的满意度 —— 塑造了 Sundaresan 至今对待这一问题的思考方式。

“编程是一项分析性任务。它与[在线]购物不同，”他说。“如果系统给出了错误的建议，或者给出了干扰我思维过程的建议，那影响就大了。”

他认为，用户体验与底层 AI 正在做的事情是正交的。如果你在交互界面上搞错了，你可能会拥有更好的模型，但产品却更糟糕。

他目睹了模型世界的演变：长短期记忆网络（LSTM）、早期的编码器-解码器架构、[Google 的 Transformer 论文](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)，以及第一个 GPT。在每个阶段，他的团队都已经预见了他们试图解决的问题。只是当时的模型还不够强大。“如果你回头看我们的发表物，我们在所有这些领域都有成果，”Sundaresan 说。“每篇论文都会说，这是针对此问题的模型，那是针对彼问题的模型。”

> “甚至我们的客户也不放心将数据发送到我们自己的云端。他们希望数据留在客户端。因此，我们实际上让模型在笔记本电脑上运行 —— 为了确保它能在笔记本电脑内运行，必须进行大量的工程工作。”

他说，当前沿模型终于具备了足够的能力，让更大的赌注获得回报时，Copilot 应运而生。但到那时，Sundaresan 也花了数年时间观察模型在哪些地方会出错 —— 以及围绕它们的产品设计在哪些地方会出错。训练截止日期导致了言之凿凿的错误信息。人们倾向于为每项任务都动用最强大（也最昂贵）的模型，而不论是否有此必要。在企业实际运行的受限环境中运行高性能模型的困难。

“甚至我们的客户也不放心将数据发送到我们自己的云端，”谈到在 Microsoft 的早期岁月时他说道。“他们希望数据留在客户端。因此，我们实际上让模型在笔记本电脑上运行 —— 为了确保它能在笔记本电脑内运行，必须进行大量的工程工作。”

## 为什么选择 IBM？

当 Sundaresan 描述这段历史时，一个显而易见的问题是，为什么他带着这些积累的知识去了 IBM，而不是更显眼的地方。他直截了当地回答：在 Microsoft 待了十年后，他想寻求改变，而 IBM 提出了一个极具说服力的方案。

但不太明显的答案是，对于他所关注的特定问题，IBM 的劣势实际上是资产。

“在软件部门，我们有近 20,000 人。我们有基础设施，有咨询业务。IBM 内部有大量的用户，”他说。“如果我能创造出一些能让他们获益的东西，那本身就是一个巨大的产品。” 内部部署 —— IBM 称之为“零号客户（client zero）” —— 给了他外部产品发布无法提供的东西：一个庞大、多样化且稳定的用户群，他们愿意接受早期的摩擦，以换取真实的生产力提升。

另一项资产是工作负载的多样性。IBM 的内部开发者群体既编写 [Python](https://thenewstack.io/python/) 和 [Rust](https://thenewstack.io/rust-programming-language-guide/)，也编写 [PL/I](https://www.ibm.com/docs/en/zos-basic-skills?topic=zos-pli)、[COBOL](https://thenewstack.io/cobol-everywhere-will-maintain/)、[大型机 JCL](https://www.ibm.com/docs/da/zos-basic-skills?topic=collection-basic-jcl-concepts)，以及 Sundaresan 描述为“像方言一样的自定义语言”。如果 Bob 能处理这种广度，它就能处理企业客户带来的任何需求。

“在我们去敲客户大门之前，我们已经有了一个可以讲述的故事，”他说。

他也直言不讳地表达了他的构建理念：不是为任何开发者执行任何任务而构建的水平化工具，而是专门为大多数 AI 编程工具视为边缘情况的企业环境优化的系统：遗留代码库、严格的合规要求、混合环境，以及 [AI 生成代码](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/)带来的真实成本 —— 那些看起来已准备好投入生产但实际并非如此的代码。

## 没人谈论的成本问题

在与 Sundaresan 的交谈中，最坦诚的时刻之一是他描述大多数开发者在随心所欲使用 AI 编程工具时的状态。

> “这就像开着你的法拉利去买牛奶。你没必要这么做。”

“人们只会问，‘你想用什么模型？’ 然后人们会选择最新的 Sonnet 4.7 之类的。他们可能只是运行一个简单的提示词，但一百万个 Token 的成本就要 40 美元，”他说。“这就像开着你的法拉利去买牛奶。你没必要这么做。”

Bob 不会将底层模型暴露给用户。它会根据任务的实际需求自动路由任务 —— 路由到 Anthropic Claude、Mistral 开源模型、IBM Granite，或是专为 Bob 环境构建的几种专有微调模型之一。

Sundaresan 认为这种路由智能才是真正的架构工作所在。“这不仅仅是在系统中塞进一个模型，”他说。“而是引入模型、引入体验，同时也引入提供卓越体验的架构。这三者必须结合在一起。模型只是方程的一部分。”

他描述了在 IBM 内部用户群中进行的 A/B 测试 —— 测试不同前沿模型的变体，监控使用模式，并识别哪些地方原本可以使用廉价模型达到同样效果，却使用了昂贵模型。内部部署让这种规模的实验成为可能，这是任何早期阶段产品都负担不起的。

## 代理化市场的真实去向

问及 Sundaresan 关于代理化 AI（agentic AI）的热度周期，他会给出研究员式的回答，而非总经理式的。

“无风不起浪，”他告诉 *The New Stack*。“如果热度是烟，那么某处一定有火。火可能没烟看起来那么大，但火是存在的。”

他的看法是，基于代理的开发是真实的，但并不新鲜。基于服务的开发、基于 API 的开发、基于代理的开发 —— 所有这些以前都存在。改变的是，现在的接口是概率性的和对话式的，而不是确定性的和编程化的。这种转变创造了真实的新能力，但也带来了真实的新风险。

> “我们可以因为恐惧而无所作为，也可以勇敢但系统化地前进。”

“你也可以分散它的注意力，”谈到代理系统时他说道。“你可以问一些不该问的问题，或者泄露它不该泄露的信息。” 他认为，被引用的 91% 的 AI 项目失败率归根结底在于纪律 —— 或者说缺乏纪律。公司认为与前沿模型提供商签署协议就足够了。事实并非如此。“在将它们整合进你的软件产品之前，你需要遵循你原有的纪律，”Sundaresan 说。

他正在关注的方向，也是他认为需要比现在获得更多关注的方向是：代理与代理之间的对话，最终使用人类无法直接阅读的机器原生语言。“如果这些衍生语言中存在错误，错误可能会爆炸式增长，”他说。“未来还有很多事情会发生。我们可以因为恐惧而无所作为，也可以勇敢但系统化地前进。”