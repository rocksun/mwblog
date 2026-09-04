**Meta’s Superintelligence Labs on Tuesday launched Muse Voice Transcribe**, a new real-time speech recognition model that, on some benchmarks, outperforms virtually every other comparable model for real-time speech processing.

Meta’s lab describes the model as its first “real-time audio perception model.” With Muse Spark, the company also recently shipped another speech-to-text capable model, though not one that specializes in this use case.

The model can distinguish among more than 20 speakers, Meta says, and has been trained on over 70 languages (with 25 of them “extensively verified”), including cases where multilingual speakers switch languages in the middle of a conversation. It also supports long conversations of over an hour.

![](https://cdn.thenewstack.io/media/2026/09/b11af22e-aa-wer-streaming-index-vs.-time-to-final-transcription.png)





Credit: Meta.

It’s now available via the Meta Model API, Meta AI for Mac, and in [Muse Code](https://thenewstack.io/muse-code-sdk-pricing/). The API pricing seems reasonable at $3.00 per 1,000 audio minutes (or $0.18 per hour).

Unlike with its Muse Glimmer models, Meta will not make the open weights of this model available, a Meta spokesperson told *The New Stack*.

## Benchmark lead, in English

On Artificial Analysis’s AA-WER Streaming speech-to-text accuracy benchmark, the model’s word error rate is 3.1%, ahead of competitors like Cartesia Ink-2 (3.4%), ElevenLabs’ Scribe v2 Real-time (3.6%), GPT Live Transcribe (3.9%), and Gemini 3.5 Transcribe Live (4%). This benchmark only applies to English speech, though.

When it comes to recognizing distinct speakers, all models still struggle more than most users would like, but here, too, in these real-time use cases, Muse Voice Transcribe leads the pack with a 17.5% error rate across several standard benchmarks.

[](https://cdn.thenewstack.io/media/2026/09/046113ac-dictation-on-meta-ai-mac-app-muse-code.mp4)

Credit: Meta.

## How it all works

Under the hood, Muse Voice Transcribe is an autoregressive multimodal model from the Muse Spark family, Meta says, and the interesting part is how it decides when to talk.

Audio comes in as 80-millisecond chunks (12.5 per second), each compressed into a single soft token. At every chunk, the model makes a choice. It either emits a text token or a special “next audio” placeholder, which the system then replaces with the next chunk of audio.

When the audio stops, an “empty audio” token signals to the model that no more audio is coming, and it flushes any text it’s still holding.

Because the model controls how much audio it hears before committing to a word, it also controls its own latency. Meta calls this “adaptive delay.” The idea here is that difficult words get more context, while easy words get transcribed almost immediately.

That tradeoff is learned during the models’ reinforcement learning phase, where the word error rate reward and the delay reward are multiplied rather than added.

The system uses a similar mechanism for detecting speakers.

Real-time transcription has quietly become one of the most crowded corners of the AI market this summer, with OpenAI, Google, xAI, and Alibaba all shipping streaming models within weeks of each other, on top of the specialists that were already there. A 0.3-point lead on a benchmark won’t hold for long in a competitive field like that.

What Meta has, however, is a built-in reason to keep pushing. Every product it really cares about, from its glasses to the Mac app, needs this to work as well as possible.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)