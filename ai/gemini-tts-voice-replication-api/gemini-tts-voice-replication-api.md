<!--
title: OpenAI定制声音需要联系销售，Google直接将其做成了自助服务
cover: https://cdn.thenewstack.io/media/2026/09/fdcb9158-logan-voss-hpfio3dz9pa-unsplash-scaled.jpg
summary: Google通过Gemini API发布了Gemini 3.8 Flash和Flash-Lite TTS，支持开发者通过提示词或录音自助创建和克隆专属AI声音，相比OpenAI需要联系销售的繁琐流程，Google实现了全自助服务。
-->

Google通过Gemini API发布了Gemini 3.8 Flash和Flash-Lite TTS，支持开发者通过提示词或录音自助创建和克隆专属AI声音，相比OpenAI需要联系销售的繁琐流程，Google实现了全自助服务。

> 译自：[OpenAI makes you call sales for a custom voice. Google just made it self-serve.](https://thenewstack.io/gemini-tts-voice-replication-api/)
> 
> 作者：Amanda Caswell

Google今天通过 Gemini API 和 Google AI Studio 发布了 Gemini 3.8 Flash TTS 和 Gemini 3.8 Flash-Lite TTS。长期以来，文字转语音 API 一直让开发者局限于现有的声音，但 Gemini 3.8 改变了这一点，它允许用户自行创造声音。

现在，开发者可以描述他们心目中的声音，或者从现有声音的简短录音开始，然后保存他们创建的声音并在应用程序中重复使用。Google 会从头到尾处理声音配置文件，因此不需要在每个新请求中附带原始录音或描述。

## 将录音转为 Voice ID

声音复制通过一个新的 Voices 端点（POST /v1beta/voices）进行，需要来自同一说话人的两个录音：这些需要是 10 到 30 秒之间的干净样本以及一个单独的同意录音。对于第二个片段，说话人需要宣读一份声明，确认该声音属于他们，并同意让 Google 创建其合成版本。Google 在继续操作之前会确认提供同意的人和参考片段是同一个人。

获批后，Google 会返回一个 voice_… ID，并将其连同使用 Gemini 的声音设计工具创建的任何声音一起，在开发者的项目中保留一年。一个项目总共可容纳多达 200 个声音，开发者可以通过 API 检索、列出或删除它们，就像处理其他存储的资源一样。

声音复制也可以在不将配置文件存储在项目中的情况下使用。设置 `store=False` 会改为返回一个加密的 voicekey_…，它保留在应用程序中，并在需要声音时再次提供。由于该密钥在 7 天后过期，此选项对于生命周期短的任务非常有意义。

在围绕该功能进行构建之前，还有几点值得注意：Google 使用 SynthID 标记由 Gemini 生成的音频，并且复制的声音还带有 C2PA 内容凭证，可用于追踪音频的来源。Google 不在伊利诺伊州、得克萨斯州、欧洲经济区、英国、瑞士或印度通过 AI Studio 提供声音复制功能。

> 一个项目总共可容纳多达 200 个声音，开发者可以通过 API 检索、列出或删除它们，就像处理其他存储的资源一样。

## 通过提示词从头设计声音

声音设计通过对角色、口音和特征的自然语言描述来生成人物角色，Google 表示它适用于 100 多种语言和方言。文档列出了 Flash TTS 支持 130 种语言，Flash-Lite 支持 101 种。Google 的公告还声称拥有超过 2,000 种可用于生产环境的声音库。

开发者文档描述了 30 种预构建的工作室声音，以及扩展库中的数百种其他声音，可以通过 `GET /v1beta/voices` 按语言、口音、音高和用例进行过滤。Google 列出的一项即将推出的功能是使用提示词对库中声音的音色、音高、语速和口音进行混音调整。

该公司建议创建一次声音并重复使用其 ID，而不是在每个请求中都描述相同的人物角色。根据[文档](https://aistudio.google.com/docs/speech-generation)，重复发送长人物角色描述是导致声音漂移的最常见原因。声音创建后，后续请求仅需简短的风格指令（如果有的话）。

Gemini 3.8 将输入文本严格视为逐字稿，对于在 3.1 预览模型的提示词中嵌入舞台指导的任何人来说，这是一个重大变更。对某个回合的持续指导（例如耳语、讽刺或语速快）现在放在 `speech_metadata` 注释中，而诸如 `<sigh>`、`<cough>` 和 `<short pause>` 等短暂声音则内联放在尖括号中。在双人脚本中，用竖线包裹的听众反应（例如 `|mhm|`）会产生副通道和重叠语音，而不会将脚本打断为额外的轮次。

> Gemini 3.8 将输入文本严格视为逐字稿，对于在 3.1 预览模型的提示词中嵌入舞台指导的任何人来说，这是一个重大变更。

## 双人脚本有限制

原生双人生成有一个值得一提的限制。单个请求最多支持使用预构建声音的两名说话人，而设计声音或复制声音之间的对话必须逐轮生成，并从 24 kHz PCM 输出拼接在一起。

一元请求默认返回 WAV，流式请求返回原始 16 位 PCM，μ-law 和 A-law 编码可用于电话管道。Google 表示，Flash TTS 在数小时的连续音频中保持了声音质量和音色，主要针对有声读物和播客制作。

## Flash 追求性能，Flash-Lite 追求吞吐量

这两个模型共享一个 API 架构，因此在它们之间切换只需更改一个参数，并且两者都支持声音设计和复制。

该公司将 Flash TTS 定位为满足高要求的表演工作，包括复杂的对话、大量使用声音标签、困难的发音、地方方言以及长篇旁白。Flash-Lite TTS 是速度更快、成本更低的选项，也是 `gemini-3.1-flash-tts-preview` 的直接替代品，针对批量生产、朗读功能以及将文本模型与单独语音步骤配对的[级联语音代理](https://thenewstack.io/voice-agent-latency-architectures/)进行了调整。

对于这些代理，Google 建议随着 LLM 文本的到达每轮进行一次 TTS 调用，并使用存储的声音在整个对话中保持身份。

## 接入语音代理框架

语音模型只是生产级语音应用程序的一层，实时代理仍然需要传输、[语音识别](https://thenewstack.io/meta-muse-voice-transcribe/)、轮次检测、中断处理和会话状态。Google 向开发者推荐了已经处理这些层的框架，并点名了 Agora、LiveKit、Pipecat 和 Vercel 的 AI Gateway 作为通过 Gemini API 支持 Gemini 语音生成的平台。

这让团队能够将 Gemini 作为语音层嵌入，而无需重建其音频管道，不过任何打算依赖复制声音的人都应该在提交之前确认他们的框架传递了自定义的 voice_… ID。通过 Gemini Enterprise 的 API 访问权限据称即将推出。

## OpenAI 的方法如何对比

OpenAI 也提供自定义声音，但访问权限更严格。客户必须通过销售渠道，每个组织限制为 20 个声音，并且必须提供同意录音以及长达 30 秒的声音样本。生成的声音 ID 适用于其语音端点、Realtime API 和 Chat Completions。

OpenAI 所没有的是 Google 基于提示词的声音设计，它可以根据书面描述创造声音。其 13 种内置声音[可以针对](https://thenewstack.io/openai-api-now-supports-building-voice-agents/)语调或速度进行引导，并且应用程序必须披露该语音是 AI 生成的。

相比之下，Google 的优势在于它在第一行文本到达之前，就为开发者提供了更多创造所需声音的方法。

> Google 的优势在于它在第一行文本到达之前，就为开发者提供了更多创造所需声音的方法。