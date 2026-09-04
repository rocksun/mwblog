<!--
title: Meta在实时语音转录领域超越OpenAI与Google
cover: https://cdn.thenewstack.io/media/2026/09/3af10b45-screenshot-2026-09-01-at-10.00.08-am.png
summary: Meta推出的Muse Voice Transcribe模型在实时语音转录基准测试中表现卓越，以3.1%的错误率超越OpenAI和Google的竞品。该模型采用自回归多模态架构，支持70多种语言及多说话人识别，具备自适应延迟控制技术，目前已通过API及Meta生态系统提供服务。
-->

Meta推出的Muse Voice Transcribe模型在实时语音转录基准测试中表现卓越，以3.1%的错误率超越OpenAI和Google的竞品。该模型采用自回归多模态架构，支持70多种语言及多说话人识别，具备自适应延迟控制技术，目前已通过API及Meta生态系统提供服务。

> 译自：[Meta just beat OpenAI and Google at real-time transcription](https://thenewstack.io/meta-muse-voice-transcribe/)
> 
> 作者：Frederic Lardinois

**Meta的Superintelligence Labs周二发布了Muse Voice Transcribe**，这是一款全新的实时语音识别模型。在部分基准测试中，其性能几乎超越了所有其他同类实时语音处理模型。

Meta实验室将该模型描述为公司首个“实时音频感知模型”。随着Muse Spark的推出，该公司最近还发布了另一款具备语音转文本能力模型，尽管它并非专门针对此类用例。

Meta表示，该模型能够区分超过20名说话人，并已在超过70种语言上进行了训练（其中25种语言经过了“广泛验证”），甚至包括多语言说话人在对话中途切换语言的情况。它还支持超过一小时的长对话。

![](https://cdn.thenewstack.io/media/2026/09/b11af22e-aa-wer-streaming-index-vs.-time-to-final-transcription.png)

图片来源：Meta。

目前，该模型已通过Meta Model API、Meta AI for Mac以及[Muse Code](https://thenewstack.io/muse-code-sdk-pricing/)提供使用。其API定价颇为合理，为每1,000音频分钟3.00美元（或每小时0.18美元）。

Meta的一位发言人告诉*The New Stack*，与Muse Glimmer系列模型不同，Meta此次不会公开该模型的权重。

## 英语基准测试领先

在Artificial Analysis的AA-WER流式语音转文本准确性基准测试中，该模型的词错误率为3.1%，领先于Cartesia Ink-2 (3.4%)、ElevenLabs的Scribe v2 Real-time (3.6%)、GPT Live Transcribe (3.9%) 以及Gemini 3.5 Transcribe Live (4%) 等竞争对手。不过，该基准测试仅适用于英语语音。

在区分不同说话人方面，所有模型目前的表现仍难以达到大多数用户的预期，但在这些实时用例中，Muse Voice Transcribe依然以17.5%的错误率在多项标准基准测试中处于领先地位。

![](https://cdn.thenewstack.io/media/2026/09/046113ac-dictation-on-meta-ai-mac-app-muse-code.mp4)

图片来源：Meta。

## 技术原理

Meta表示，Muse Voice Transcribe是Muse Spark家族中的一款自回归多模态模型，有趣之处在于它如何决定何时进行输出。

音频以80毫秒的片段（每秒12.5个）输入，每个片段被压缩成一个单一的软标记（soft token）。在每一个片段上，模型都会做出选择：要么输出一个文本标记，要么输出一个特殊的“下一个音频”占位符，随后系统会用下一个音频片段替换该占位符。

当音频停止时，“空音频”标记会向模型发出信号，提示没有更多音频输入，随后它会清理缓存中残留的任何文本。

由于模型在确定单词输出前可以控制它所听到的音频量，因此它也能够控制自身的延迟。Meta称之为“自适应延迟”（adaptive delay）。其设计理念是：复杂的词汇会获得更多的上下文，而简单的词汇则几乎可以立即被转录。

这种权衡是在模型的强化学习阶段习得的，在该阶段，词错误率奖励和延迟奖励是相乘而非相加的。

系统在检测说话人时使用了类似的机制。

今年夏天，实时转录已悄然成为AI市场竞争最激烈的领域之一。OpenAI、Google、xAI和Alibaba都在几周内相继推出了流式模型，此外还有早先存在的专业公司。在这样一个竞争激烈的领域，0.3个百分点的基准测试领先优势恐怕难以维持太久。

然而，Meta拥有一种内置的持续推动动力：它真正关心的每一款产品，从智能眼镜到Mac应用程序，都需要这项技术达到尽可能完美的效果。