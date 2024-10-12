
<!--
title: OpenAI 的实时 API 隆重登场
cover: https://cdn.thenewstack.io/media/2024/10/4d9d7da9-openais-realtime-api-takes-a-bow-2.jpg
-->

开发者现在可以将快速语音到语音体验构建到他们的应用程序中。

> 译自 [OpenAI's Realtime API Takes a Bow](https://thenewstack.io/openais-realtime-api-takes-a-bow/)，作者 Chris J Preimesberger。


# OpenAI's Real-Time API Takes a Bow

![OpenAI's Real-Time API Takes a Bow Feature Image](https://cdn.thenewstack.io/media/2024/10/4d9d7da9-openais-realtime-api-takes-a-bow-2-1024x576.jpg)

San Francisco - [OpenAI](https://openai.com/), whose commercial [ChatGPT chatbot](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/) now boasts about 200 million users, is expanding its business in the [enterprise AI space](https://thenewstack.io/cohere-vs-openai-in-the-enterprise-which-will-cios-choose/). The company on Tuesday unveiled four new versions of its application development products, including a brand-new public beta of its [real-time API](https://platform.openai.com/docs/api-reference/streaming), at its [DevDay event](https://openai.com/devday/).

The real-time API allows developers to build applications that can have back-and-forth conversations with AI chatbots.

These new models - [GPT-4o](https://openai.com/index/hello-gpt-4o/), GPT-4o mini, GPT-o1, and GPT-o1 mini - represent various versions of OpenAI's development platform. They all support the building of generative AI-powered voice applications.

Like OpenAI's [ChatGPT advanced voice mode](https://help.openai.com/en/articles/8400625-voice-mode-faq), the new real-time API enables developers to build low-latency multimodal capabilities into applications, supporting natural speech-to-speech conversations using the [six preset voices](https://platform.openai.com/docs/guides/text-to-speech) already supported in the API.

Advanced voice mode takes conversations to a higher quality level by enabling more natural voice interactions. For example, users can interrupt ChatGPT, just as they would in a normal conversation, making the flow more natural.

## How to Overcome Language Barriers

Chief Product Officer [Kevin Weil](https://www.linkedin.com/in/kevinweil/) told a group of tech writers on Monday that he has used GenAI voice technology (the kind that can be built using the ChatGPT real-time API) in real life.

"I was in Seoul and Tokyo in the last few weeks, and I found myself having conversations with people who didn't speak the same language," Weil said. "I used our voice mode. I just said, 'Hey, ChatGPT. When I speak in English, I want you to speak in Korean. When you hear Korean, I want you to speak back in English.' I had full business-level conversations with people I couldn't otherwise talk to. It was pretty magical.

"Think about what that means, not just for business, but for travel, tourism, software development - anywhere you want to go, you don't have to learn a new language. It's pretty cool. The idea of a universal translator used to be completely science fiction, and now it's really becoming a reality."

OpenAI uses this technology heavily in its development packages. Developers simply describe what they want their application to do, and the GPT AI figures out how to make it happen. GPT-4o will find the necessary [language models](https://thenewstack.io/llm/), line them up, and make them work together.

The company also introduced audio input and output in the [Chat Completions API](https://platform.openai.com/docs/guides/text-generation) to support use cases that don't require the low-latency benefits of the real-time API. With this feature, developers can pass any text or audio input to GPT-4o and have the model respond in their choice of text, audio, or both, Weil said.

OpenAI's Chat Completions API enables developers to integrate ChatGPT's conversational capabilities into their own applications, products, or services. GPT's AI helps developers guide code usage and application architecture.

However, the biggest advancement from a developer's perspective is that, with the real-time API - and the upcoming audio capabilities in the Chat Completions API - developers no longer need to stitch together multiple models to achieve results like Weil's Korean conversation. Instead, they can use a single API call to build natural conversational experiences, he said.

## How It Works

Previously, to create a similar voice assistant experience, developers had to use an automatic speech recognition model like [Whisper](https://openai.com/index/whisper/) (launched in 2022) to transcribe audio, pass the text to a text model for reasoning, and then use a text-to-speech model to play back the model's output. This approach often resulted in the loss of emotion, emphasis, and accents; it also took a long time, Weil said.

Now, with the Chat Completions API, developers will be able to handle the entire process using a single API call, he said. The real-time API improves on this by streaming audio input and output directly, enabling a more natural conversational experience. It can also automatically eliminate interruptions, Weil said.
在幕后，实时 API 现在使开发人员能够创建与 GPT-4o 交换消息的持久 [WebSocket](https://thenewstack.io/the-challenge-of-scaling-websockets/) 连接。该 API 支持函数调用（调用或执行命名代码段以执行特定任务的过程），这使得语音助手可以通过触发操作或引入新上下文来响应用户请求。

例如，语音助手可以代表用户下订单或检索相关客户信息以个性化其回复。

##  更多功能的路线图

Weil 表示，OpenAI 计划添加更多功能，包括：

**新模式**: 随着时间的推移，OpenAI 计划添加更多模式，例如视觉和视频。**提高速率限制**: 今天，API 对 5 级开发人员的速率限制约为 100 个同时会话，2 到 4 级开发人员的限制更低。该公司将随着时间的推移提高这些限制以支持更大的部署。**官方 SDK 支持**: OpenAI 将在 [OpenAI Python](https://thenewstack.io/dev-news-w3c-accessibility-openai-python-sdk-and-more/) 和 Node.js SDK 中集成对实时 API 的支持。**提示缓存**: 将添加对 [提示缓存](https://thenewstack.io/developer-tips-in-ai-prompt-engineering/) 的支持，以便可以以折扣价重新处理之前的对话回合。**扩展模型支持**: 实时 API 还将在该模型的后续版本中支持 GPT-4o mini。

##  谁在测试 Beta 版？

OpenAI 一直在与 Healthify（一个营养和健身教练应用程序）和 Speak（一个语言学习应用程序）等用户进行 Beta 测试。

Healthify 使用 OpenAI 的实时 API 来实现与 AI 教练 Ria 的自然对话，并在需要时让人类营养师参与以提供个性化支持。

Speak 使用实时 API 为其沉浸式角色扮演课程提供动力，这些课程感觉就像与专家人类导师练习对话一样。

实时 API 现在已在 [使用层级 2 到 5](https://platform.openai.com/docs/guides/rate-limits/usage-tiers) 上向开发人员公开测试。该链接中包含定价级别。

[YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)