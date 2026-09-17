<!--
title: OpenAI拆解语音模型大脑，助力开发者移除两万行代码
cover: https://cdn.thenewstack.io/media/2026/09/91d4b96d-pramod-tiwari-vs7aagx_354-unsplash-scaled.jpg
summary: OpenAI发布GPT-Live-1 API，通过原生全双工语音架构取代复杂的传统级联系统。该方案简化了语音代理开发，帮助开发者大幅削减代码量，提升交互自然度，并支持灵活的模型调用与任务委托。
-->

OpenAI发布GPT-Live-1 API，通过原生全双工语音架构取代复杂的传统级联系统。该方案简化了语音代理开发，帮助开发者大幅削减代码量，提升交互自然度，并支持灵活的模型调用与任务委托。

> 译自：[OpenAI split a voice model's brain. Then one team deleted 23,000 lines of code.](https://thenewstack.io/gpt-live-1-voice-api/)
> 
> 作者：Amanda Caswell

构建一个AI语音助手一直以来都比看起来要笨拙得多。大多数语音助手实际上是一系列串联在一起、来回传递对话的系统。你说的话被转换成文本，以便模型找出如何回应，然后该答案必须再被转换回语音；不难看出为什么交互过程很快就会变得机械化。现在，OpenAI正试图将这一架构整合在一起。

周三，该公司在[API中推出了GPT-Live-1](https://openai.com/index/introducing-gpt-live-1-in-the-api/)，首次将ChatGPT语音模式背后的原生全双工语音架构提供给外部开发者。它不再让开发者管理整个链路，而是希望由一个模型来处理对话，同时将更繁重的思考工作放在别处进行。

> 它不再让开发者管理整个链路，而是希望由一个模型来处理对话，同时将更繁重的思考工作放在别处进行。

## 全双工语音委派

GPT-Live-1作为对话的前沿阵地运行。由于它是原生的全双工架构，它可以在对话发生时跟上节奏，包括在有人中途插话时，而无需开发者协调多个独立的系统。但语音模型不必独自完成所有工作。

当请求需要更多时间或更多处理时，GPT-Live-1可以将任务移交给后台的另一个模型。这可能是[GPT-6 Astra](https://thenewstack.io/openai-gpt6-astra-benchmarks/)、像Luna这样的小型模型，或是来自其他提供商的模型。

等待更大的模型可能会让语音助手变得极其尴尬。问一个难题，你最终可能会在模型进行处理时陷入沉默。GPT-Live-1则可以保持对话进行——填补停顿、确认对方的发言——然后在后端完成后将答案整合进来。

OpenAI表示，GPT-Live-1在全双工基准测试（Full Duplex Bench）中的表现比GPT-Realtime-2.1高出30个百分点。配合中等推理能力的GPT-6 Astra，它还在[𝜏³-benchmark](https://sierra.ai/resources/research/tau-3-bench)中占据了榜首。

## 委派流程解析

OpenAI通过事件驱动的接口提供委派功能。语音会话生成一个`delegation_id`，将上下文发送给处理繁重任务的任何后端系统，并通过名为`session.commentary.append`的事件获取结果。语音模型将该结果融入到正在进行的对话中，而不是大声读出一块文本。开发者仍然可以看到模型听到和说出的内容，并控制它何时发言——他们只是不必再用独立的系统来构建整个对话。OpenAI的[API文档](https://developers.openai.com/api/docs/live)详细介绍了这种模式，包括使用Codex SDK的有效示例。

## 早期客户精简代码

一位早期客户在切换到GPT-Live-1后删除了23,000行代码。

[Tony Stoyanov](https://www.linkedin.com/in/stoyan-tony-stoyanov-07690a53/)是正在测试该API的医疗公司EliseAI的联合创始人兼CTO，他说此举将他的代码库缩小了80%。他的团队可以将节省下来的时间用于改善患者体验——使预约和导诊变得更加容易。

语言学习公司[Speak](https://www.speak.com/)在对话本身感受到了差异。在对其“实时家教课程（Live Tutor Lessons）”的早期测试中，GPT-Live-1中断正在思考停顿的人的几率降低了近80%。对于正在学习新语言的人来说，这多出的几秒钟可能就是能否说出答案与被AI打断之间的区别。

Yelp已经在Yelp Host和Hatch中使用了GPT-Live-1。CTO [Alex Levy](https://www.linkedin.com/in/ahlevy/)表示，公司看到由AI成功处理的通话数量增加了，且来电者倾向于使用更完整、更自然的句子——Levy认为，这是一个信号，表明电话另一端的体验感受到了不同。发布时展示的一个演示视频恰恰解释了原因：即使在背景噪音下，且人们互相交谈时，餐厅预订仍能持续进行。

## 语音层的定价

GPT-Live-1的费用为每分钟0.05美元，即每小时约3美元。此外还有开发者选择在它背后运行的任何程序的费用。如果GPT-Live-1将请求移交给GPT-6 Astra，开发者也要为那次调用付费。代理调用推理模型的次数越多，账单增长得就越快。

随着来自Anthropic、Google和中国实验室的竞争加剧，OpenAI一直在[下调API价格](https://thenewstack.io/gpt-5-6-api-price-cuts/)，但前沿推理仍然不是免费的。

> 代理调用推理模型的次数越多，账单增长得就越快。

权衡之处在于，开发者现在可以有选择地决定将资金花在什么地方。简单的任务（如安排预约）可以交给Luna。更难的问题（如真正需要多步推理或工具调用的问题）可以交给Astra。OpenAI已经展示了[Astra的可调推理设置如何让开发者针对每次调用灵活调整成本](https://thenewstack.io/astra-reasoning-effort-cost/)，而GPT-Live-1为他们提供了一个将这一逻辑应用于语音的地方。

## 平台控制权的权衡

通过旧的级联方法，团队可以为语音栈的每个部分选择不同的提供商，并随时更换组件。GPT-Live-1接管了更多的对话，这也意味着将其更多的控制权交给了OpenAI。

目前的赌注是，如果这意味着语音助手最终能够跟上与之对话的人，开发者会愿意放弃一部分控制权。

> 目前的赌注是，如果这意味着语音助手最终能够跟上与之对话的人，开发者会愿意放弃一部分控制权。