# OpenAI’s Realtime API Takes a Bow
![Featued image for: OpenAI’s Realtime API Takes a Bow](https://cdn.thenewstack.io/media/2024/10/4d9d7da9-openais-realtime-api-takes-a-bow-2-1024x576.jpg)
SAN FRANCISCO — [OpenAI](https://openai.com/), which at last count serves roughly 200 million users with its commercial [ChatGPT bot](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/), is branching out in the [enterprise AI space](https://thenewstack.io/cohere-vs-openai-in-the-enterprise-which-will-cios-choose/). At its [DevDay event](https://openai.com/devday/) here Tuesday, the company introduced four new versions of its application development product, led by a new public beta of its [Realtime API](https://platform.openai.com/docs/api-reference/streaming).

Realtime API allows developers to build applications that can have a back-and-forth conversation with an AI chatbot.

The new models — [GPT-4o](https://openai.com/index/hello-gpt-4o/) , GPT-4o mini, GPT-o1 and GPT-o1 mini — represent various versions of the OpenAI development platform. They all enable application building for voice, by voice, based on generative AI.

Like OpenAI’s [ChatGPT Advanced Voice Mode](https://help.openai.com/en/articles/8400625-voice-mode-faq), the new Realtime API enables developers to build low-latency, multimodal features in applications, and supports natural speech-to-speech conversations using the [six preset voices](https://platform.openai.com/docs/guides/text-to-speech) already supported in the API.

Advanced Voice Mode takes conversations to a higher-quality level by enabling more natural voice interactions. For example, a user can interrupt ChatGPT, just as one would in a normal conversation, making the flow more natural.

## How Language Barriers Are Being Scaled
Chief Product Officer [Kevin Weil](https://www.linkedin.com/in/kevinweil/) told a gathering of tech writers on Monday about an example of how he’s used GenAI voice technology — the type that can be built using the ChatGPT Realtime API — in a real-world situation.

“I was also in Seoul and in Tokyo the last few weeks, and I found myself having conversations with folks with whom I had no common language,” Weil said. “And I was using our voice mode. I just said, ‘Hey, ChatGPT. When I say something in English, I want you to say it in Korean. And when you hear Korean, I want you to say it back in English.’ And I was having full, business-level conversations with people who I’ve not been able to say a word to. It’s really amazing.

“Think about what that means, not just for business, but for things like travel, tourism, software development — with your willingness to go somewhere, you won’t have to know a new language. It’s cool. The idea of a universal translator was complete science fiction, and now it’s really possible.”

OpenAI is using this in its development package, big time. Developers need only to describe what they want the application to do, and the GPT AI figures out how to do it. GPT-4o finds the [language models](https://thenewstack.io/llm/) needed, lines them up and makes them work together.

The company also introduced audio input and output in the [Chat Completions API](https://platform.openai.com/docs/guides/text-generation) to support use cases that don’t require the low-latency benefits of the Realtime API. With this capability, Weil said, developers can pass any text or audio inputs into GPT-4o and have the model respond with their choice of text, audio or both.

OpenAI Chat Completions API enables developers to integrate ChatGPT’s conversational abilities into their own applications, products or services. GPT’s AI helps direct developers on code usage and application architecture.

The biggest advance from a developer’s point of view, however, is that with the Realtime API — and soon with audio in the Chat Completions API — developers no longer have to stitch together multiple models to enable results like Weil’s Korean conversation. Instead, they can build natural conversational experiences with a single API call, he said.

## How It Works
Previously, Weil said, to create a similar voice-assistant experience, developers had to transcribe audio with an automatic speech recognition model such as [Whisper](https://openai.com/index/whisper/) (introduced in 2022), pass the text to a text model for inference or reasoning, and then play the model’s output using a text-to-speech model. This approach often resulted in loss of emotion, emphasis and accents; it also took a long time, Weil said.

Now, using the Chat Completions API, developers will be able to handle the entire process with a single API call, he said. The Realtime API improves this by streaming audio inputs and outputs directly, enabling more natural conversational experiences. It can also smooth over interruptions automatically, Weil said.

Under the hood, the Realtime API now enables developers to create a persistent [WebSocket](https://thenewstack.io/the-challenge-of-scaling-websockets/) connection to exchange messages with GPT-4o. The API supports function calling (the process of invoking or executing a named section of code to perform a specific task), which makes it possible for voice assistants to respond to user requests by triggering actions or pulling in new context.

For example, a voice assistant could place an order on behalf of the user or retrieve relevant customer information to personalize its responses.

## Roadmap to More Functionality
OpenAI is planning to add more capabilities, Weil said, including:

**New modalities**: Over time, OpenAI plans to add additional modalities, such as vision and video.**Increased rate limits**: Today the API is rate-limited to approximately 100 simultaneous sessions for Tier 5 developers, with lower limits for Tiers 2 to 4. The company will increase these limits over time to support larger deployments.**Official SDK support**: OpenAI will integrate support for Realtime API into the[OpenAI Python](https://thenewstack.io/dev-news-w3c-accessibility-openai-python-sdk-and-more/)and Node.js SDKs.**Prompt caching**: Support for[prompt caching](https://thenewstack.io/developer-tips-in-ai-prompt-engineering/)will be added, so previous conversation turns can be reprocessed at a discount.**Expanded model support**: The Realtime API will also support GPT-4o mini in upcoming versions of that model.
## Who’s Testing the Beta?
OpenAI has been beta testing with users such as Healthify, a nutrition and fitness coaching app, and Speak, a language learning app.

Healthify uses OpenAI’s Realtime API to enable natural conversations with its AI coach Ria, while involving human dietitians when needed for personalized support.

Speak uses Realtime API to power its immersive role-play lessons that feel like practicing conversation with an expert human tutor.

The Realtime API is available now in public beta for developers on [usage Tiers 2 through 5](https://platform.openai.com/docs/guides/rate-limits/usage-tiers). Pricing levels are included in that link.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)