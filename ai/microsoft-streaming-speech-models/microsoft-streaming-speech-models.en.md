“I think you said, ‘representative.’” It’s the fastest way to bypass automated [speech recognition](https://thenewstack.io/meta-muse-voice-transcribe/) chatbots that fail to route human callers to the service they need. Achieving a human handoff to a living, breathing representative still feels like a badge of honor.

Microsoft wants to change that dynamic.

[Naomi Moneypenny](https://www.linkedin.com/in/moneypenny/), senior director of product development at [Microsoft](https://thenewstack.io/enterprise-ai-model-routing/) Foundry Models division, [blogged](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/build-expressive-voice-experiences-with-new-mai-models-in-microsoft-foundry/4524637) on October 1 to introduce three new Microsoft AI (MAI) models in [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry), Redmond’s app and agent model catalog and platform.

“A voice agent has to do more than hear a request and produce a reply. It has to keep the interaction moving while it listens, reasons, uses tools, and speaks. A delay at either end can turn a conversation into a series of awkward pauses,” writes Moneypenny.

Available now in Microsoft Foundry, the latest voice-centric models include MAI-Transcribe-2-Streaming, which turns live speech into text as it is spoken; MAI-Voice-2.1, an expressive multilingual text-to-speech model; and MAI-Voice-2.1-Flash, optimized for responsive, high-volume voice applications.

## Partials drive incremental speech recognition

Instead of waiting for a person to finish speaking before returning text, the technology (which has automatic language detection) produces its first hypotheses (known as [partials](https://microsoft.ai/news/our-first-streaming-transcription-model/), associated with the field of [incremental speech recognition](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/selfridge2011sigdial.pdf)) within the “low hundreds of milliseconds” of receiving audio. The model then refines the partials as more context arrives, before committing to a stable transcript once an utterance ends.

> “A live transcription experience can surface words almost as quickly as they are spoken.”

“That distinction matters when an application needs to act while someone is speaking. A customer-service agent can begin identifying a caller’s request before the sentence is complete. A voice assistant can start reasoning or preparing a tool call sooner. A live transcription experience can surface words almost as quickly as they are spoken,” writes Moneypenny.

MAI-Voice-2.1-Flash is proposed as “a natural fit” for live support agents, voice assistants, and other applications that generate spoken responses. Moneypenny suggests developers can choose MAI-Voice-2.1 when “expressive fidelity” is the priority, or Flash when they need to balance natural speech with responsiveness and cost at scale.

Moneypenny is bullish about the benchmarks thus far. Her post noted that MAI-Transcribe-2-Streaming “debuts at #1 for accuracy” on both partial and final transcripts on the benchmark-based Artificial Analysis leaderboard.

![](https://cdn.thenewstack.io/media/2026/10/1f74cd66-clipboard_image-1-1790785965152-1024x771.png)

## Time for voice to speak up?

All said and done then (pun intended), does this mean that across the spectrum of human-machine input methods, voice is now ready for wider use and adoption? CEO of voice-agent platform company [Phonely](https://www.phonely.ai/), [Will Bodewes](https://www.linkedin.com/in/william-bodewes/), tells *The New Stack* he sees these developments positively.

“Voice AI is ready for prime time, if Microsoft’s entry into the market is any indication,” Bodewes says.

Microsoft is hardly new to speech, though: Azure Speech has been on the market for years, and it ships the new MAI models. “For an AI developer, that’s an opportunity to build on that momentum, so expect more players to follow suit. But the model is only the beginning. Voice agents need to learn from every call and measurably improve over time. For companies to see real results, their voice AI must be ready for prime time in theory and in practice.”

> “In the early days, a speech request to a hosted model could sit behind a thousand others for 30 seconds, which, on a phone call, is a hang-up.”

From an infrastructure-operations perspective, there’s a clear advancement here. Bodewes, whose company builds its own voice-agent LLM, notes that in the early days (and he means back from the mid 2010s onwards in the initial cloud-based speech API era, such as the Google Cloud Speech-to-Text API, Azure Speech Services, Amazon Transcribe, etc.) a speech request to a hosted model could sit behind a thousand others for 30 seconds, which, on a phone call, is a hang-up.

“We built routing infrastructure just to find the least-loaded endpoints. Owning the model meant owning the queue, and that’s how we got to 120-millisecond responses,” explains Bodewes. “Every sentence you add to a prompt adds another chance of failure. So we enforce the critical steps in code. If an agent needs a name, email, and date of birth before it issues a refund, the codebase guarantees it. Leaving that to the LLM is how you ship incidents.”

## The front end (speech) isn’t the hard part

Phonely machine learning researcher [Amit Kiran Rege](https://amitrege.github.io/) tells *The New Stack* he agrees the developments are positive, but warns of deeper nuances (speech pun intended, again) in the wider rollout.

“Microsoft shipped the two ends of the voice agent pipeline, speech in and speech out, which tells you it’s betting on a cascade effect for contact centers, the same as we did. But in our work, we found the ends aren’t the hard part. The hard part is the silence in the middle where the model is deciding whether a caller is done or taking a breath before the next word,” explains Rege.

What surprised Phonely when scaling this type of service to millions of calls is that speeding up the data pipeline makes the agent interrupt callers more.

> “Microsoft shipped the two ends of the voice agent pipeline, speech in and speech out … But in our work, we found the ends aren’t the hard part.”

“Two-thirds of the time our agent decided to jump in too early, and nobody heard it, because the caller resumed before the first syllable and we canceled the reply. Cut your latency in half, and those become audible interruptions. Thus, the lesson is that latency and turn-taking have to improve together,” cautions Rege.

## Talking our way into future interfaces

Microsoft’s position on these technologies states that developers can embrace these same models and toolsets to build customer-service agents, multilingual assistants that recognize a spoken language and reply in a consistent voice, what it defines as “interactive learning experiences that move between languages, speakers, and conversational exercises” and live captions and voice-driven interfaces.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)