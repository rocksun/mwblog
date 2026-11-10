<!--
title: Cursor与谷歌加入OpenAI阵营，赋予编码智能体语音能力
cover: https://cdn.thenewstack.io/media/2026/11/b6289d67-ruliff-andrean-d42u7dk0m9w-unsplash-scaled.jpg
summary: Cursor与谷歌相继推出支持双向语音的编码智能体功能，允许开发者在智能体工作时通过语音实时交流、跟进进度并下达指令，而Anthropic的Claude Code目前仍仅支持语音听写。
-->

Cursor与谷歌相继推出支持双向语音的编码智能体功能，允许开发者在智能体工作时通过语音实时交流、跟进进度并下达指令，而Anthropic的Claude Code目前仍仅支持语音听写。

> 译自：[Cursor and Google join OpenAI in giving coding agents a voice. Claude Code stays silent.](https://thenewstack.io/cursor-antigravity-voice-agents/)
> 
> 作者：Paul Sawers

Cursor和谷歌加入OpenAI的行列，赋予编码智能体声音。Claude Code保持沉默。

AI编码领域两个最大的玩家正押注于开发者希望在工作时与他们的智能体对话，双方都宣布了一项双向语音功能，允许用户提问和给出后续指令，而无需返回键盘。

[周五](https://cursor.com/changelog/voice-chat)，Cursor宣布了[智能体语音聊天](https://cursor.com/docs/agent/voice-chat)，这是一项由[Grok Voice](https://x.ai/news/grok-voice-think-fast-1)驱动的功能，允许开发者呼叫智能体并商讨代码变更。就在同一天，谷歌[宣布了Antigravity中的语音模式](https://antigravity.google/blog/antigravity-voice-mode)，该功能利用[Gemini Live](https://support.google.com/gemini/answer/15274899)将语音对话引入其桌面应用和命令行工具。

在[宣布该功能的博客文章](https://antigravity.google/blog/antigravity-voice-mode)中，谷歌的开发者关系工程师[Nick Van der Auwermeulen](https://www.linkedin.com/in/nickvander/)将人类同事之间的来回互动与使用编码智能体的“节奏”进行了对比。

“一些最出色的工程设计都是大声说出来的，”Van der Auwermeulen写道。“你会和队友大声讨论一个Bug，在白板前大声思考，或者在结对编程进行到一半时说‘*等等，试试另一种方法*’。而与智能体合作的节奏则大不相同：你输入一个Prompt，智能体开始工作，你阅读它做了什么，然后你再次输入。”

> “一些最出色的工程设计都是大声说出来的。”

他补充说，任务运行的时间越长，开发者就需要越频繁地进行检查。一个命令可能正在等待批准，或者开发者可能会发现原始指令遗漏了某个需求。

“每一个这样的时刻都会把你拉回键盘前，让你分心，离开你原本正在关注的东西，”他继续说道。

因此，Antigravity的语音模式在编码智能体工作时保持实时通话开启，这样开发者就可以听到更新或批准命令，而无需去够键盘。

就Cursor而言，它也提出了类似的口号，主张让对话持续进行。

“大声描述一个变更，询问智能体正在做什么，并在工作推进时听到更新，”该公司写道。

> “大声描述一个变更，询问智能体正在做什么，并在工作推进时听到更新。”

## 看看谁在说话

对于初学者来说，[Antigravity](https://antigravity.google/)是谷歌的智能体软件开发平台。它[在去年11月与Gemini 3一同首次亮相](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/)，[2.0版本于5月推出](https://thenewstack.io/google-io-antigravity-codemender-ai-agentic/)，并配备了独立的桌面应用。还有一个终端客户端[Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-cli/)，以及为[想要在编辑器中工作的开发者](https://thenewstack.io/google-antigravity-ide-extensions/)（例如VS Code、JetBrains IDE和Xcode）提供的扩展。

Antigravity现在是谷歌整合其各种编码工具的地方，它在6月[将各个Gemini CLI用户迁移到了Antigravity](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)，同时也在[逐步淘汰Jules](https://x.com/julesagent/status/2115883717705261283)（一个先前推出的后台编码智能体）。

值得注意的是，Antigravity[现有的听写功能](https://antigravity.google/blog/introducing-google-antigravity-2)已经可以将语音转化为书面的Prompt。现在，[要在桌面应用中发起双向通话](https://antigravity.google/docs/voice-mode)，用户只需点击它旁边的波形按钮，并告诉智能体他们想让它做什么。

![开始语音通话](https://cdn.thenewstack.io/media/2026/11/98af36c0-gif1.gif)

*开始语音通话*

Antigravity会大声回复，并在编码智能体工作时保持通话开启，用户可以询问进展情况或给出进一步的指令。你还可以在智能体说话中途打断它，以提出问题或给出另一个指令。

![Antigravity大声回应](https://cdn.thenewstack.io/media/2026/11/5a9db8bf-gif2.gif)

*Antigravity大声回应*

当智能体完成工作后，其书面总结和一个用于审查代码变更的按钮会出现在同一个聊天中。

![通话中审查修复结果](https://cdn.thenewstack.io/media/2026/11/dee44a5e-gif3.gif)

*通话中审查修复结果*

此外，语音模式也适用于Antigravity CLI。用户运行 `/voice live` 命令来发起通话，并在智能体在终端中埋头苦干时听到它的回复。

![开始终端语音通话](https://cdn.thenewstack.io/media/2026/11/ed88c811-cligif.gif)

*开始终端语音通话*

## 编码智能体会回话了

Cursor在8月被埃隆·马斯克的SpaceX以600亿美元[收购](https://cursor.com/blog/joining-spacex)，它也走过了拥抱语音的类似道路。它在[2025年10月添加了听写功能](https://cursor.com/changelog/2-0)，并在上个月的[发行说明](https://prod.cursor.com/docs/release-notes)中表示，它已经更新了现有的语音通话，让智能体能够提供简短的语音进度更新。

Cursor推出该功能的一个不同之处在于你可以从*哪里*进行呼叫。Cursor支持在网页端、iOS以及桌面上进行语音聊天，而谷歌则在Antigravity桌面应用和CLI中提供该功能。Cursor的通话运行在[Grok Voice](https://x.ai/news/grok-voice-think-fast-1)上，xAI[早在4月就通过其API推出了该功能](https://x.ai/news/grok-voice-think-fast-1)。

> “现在的推动方向，似乎是在智能体开始工作后让对话持续进行。”

然而，谷歌和Cursor并不是第一批将双向语音引入编码智能体的AI公司。OpenAI在2月[推出](https://openai.com/index/introducing-the-codex-app/)了一款带有[内置听写功能](https://learn.chatgpt.com/docs/whats-new#february-26-2026)的Codex桌面应用。正如*The New Stack*在[7月报道的那样](https://thenewstack.io/voice-ai-openai-anthropic/)，该公司在ChatGPT桌面应用的Codex中加入了双向语音，让开发者能够通过说话来给出指令和检查任务。Codex CLI[自春季以来](https://github.com/openai/codex/releases/tag/rust-v0.119.0#new-features)就提供实时语音对话，OpenAI在[9月将其设为默认启用](https://github.com/openai/codex/releases/tag/rust-v0.156.0#new-features)。

就Anthropic而言，它拥有一项[语音模式](https://support.claude.com/en/articles/11101966-use-voice-mode)，仅在Claude应用内部提供双向语音功能。具体在Claude Code中，语音仍然仅通过听写实现单向交互——`/voice` 命令将开发者的语音指令[转化为Prompt文本](https://code.claude.com/docs/en/voice-dictation)，而智能体则以文字形式回复。

听写本身对于大声描述Bug或勾勒功能很有用，并且它正在整个AI编程领域普及，从主流AI实验室到资金充足的初创公司[如Replit](https://docs.replit.com/updates/2026/06/19/changelog#voice-mode)都在采用。

现在的推动方向，似乎是在智能体开始工作*之后*让对话持续进行，这样开发者就可以在工作完成之前，就某个决定进行跟进、澄清需求或改变方向。