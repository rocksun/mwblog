AI leader [Andrej Karpathy](https://karpathy.ai/) said [Inception Labs’](https://www.inceptionlabs.ai/) approach to diffusion has the potential to differ in comparison to all the other large language models that lead the field, such as Claude and ChatGPT.

That means something. And when Karpathy encourages people to try it out? That’s a big deal.

Karpathy, who coined the term vibe coding, posted on X in February that most LLMs are trained autoregressively, meaning they predict tokens left to right. Diffusion doesn’t go left to right, but all at once. In his words, you start with noise and gradually denoise it as a token stream.

“All that to say that this model has the potential to be different, and possibly showcase new, unique psychology, or new strengths and weaknesses,” [he wrote on X](https://x.com/karpathy/status/1894923254864978091?s=20). ” I encourage people to try it out!”

Inception Labs is an 18-month-old startup whose founders pioneered diffusion technology and have developed what they say is the ability to build language models faster and more cost-efficiently than traditional autoregressive LLMs. [Kimberly Mok](https://thenewstack.io/author/kimberleymok/) [wrote about Inception](https://thenewstack.io/get-ready-for-faster-text-generation-with-diffusion-llms/) earlier this year for The New Stack.

The company has a few peers in the market, including [Dream7B](https://thenewstack.io/dream-7b-a-powerful-and-open-diffusion-language-model/), [LLaDA](https://thenewstack.io/how-diffusion-based-llm-ai-speeds-up-reasoning/), and [Google](https://deepmind.google/models/gemini-diffusion/), with the experimental diffusion model it offers through Gemini. But Inception is the only commercially available model with its own API.

## What Makes Diffusion Models Different from Autoregressive LLMs?

[Mercury](https://www.inceptionlabs.ai/blog/mercury-refreshed), Inception’s model, generates tokens in parallel, said [Burzin Patel](https://www.linkedin.com/in/burzinpatel/), vice president of product at Inception, in an interview with The New Stack at [AWS re:Invent](https://thenewstack.io/aws-updates-its-nova-models-to-compete-with-google-anthropic-and-openai/). Autoregressive models generate tokens sequentially.

“Per pass through the selection process, you get multiple tokens ejected, because of which it’s like five to 10 times faster,” Patel said about Mercury. A pass means a forward look through the neural network to evaluate and make predictions.

The speed advantage compounds for applications that make multiple sequential calls to an LLM, Patel said. “More and more applications interact with the LLM multiple times — that’s a very big trend in agentic applications,” he said. If an application makes 30 LLM calls and each is two seconds faster, that’s a full minute saved per request.”

Autoregressive architectures have advantages, especially in the user interface. For instance, use a service like Claude, and you see the token output after the first pass. The output for an autoregressive is real time, while the initial output in a diffusion model has some latency, even though the final response may be faster.

## The Speed and Efficiency Advantages of Diffusion Models

But for agentic workflows, the speed of a diffusion model can make a real difference.

With Mercury, Patel said, as part of a block, you can actually change the tokens. If you see a better fifth token, you can go and change the second token.

Diffusion models generally predict all the masked tokens at the same time. Patel said Mercury generates tokens in blocks with varying confidence levels, Patel said. (That’s as far as he’ll go in explaining what’s under the hood: The company, he said, doesn’t disclose detailed architectural choices.)

In Mercury, it’s a matter of having high confidence in the tokens. If a block has 1,000 tokens, 300 might have high confidence. Mercury can continue the breakdown and continue to show the tokens that have high confidence.

“Say your answer required 1,000 tokens,” Patel said. With autoregressive models, you would take a thousand forward passes. With diffusion, you could generate anywhere between five and 10 tokens per forward pass—thousand divided by five or thousand divided by 10. It’s not much more complicated than that.”

## Inception’s Focus on Coding and Voice Use Cases

The diffusion method came out of Stanford University’s AI labs. Patel pointed out how Inception’s co-founders were involved, and their connections to each other: “[Stefano [Ermon]](https://www.linkedin.com/in/ermon/) is the head of AI labs at Stanford. [Aditya Grover](https://www.linkedin.com/in/aditya-grover/) is a Ph.D. professor at UCLA, and [Volodymyr Kuleshov](https://www.linkedin.com/in/volodymyr-kuleshov-6aa83294/) is from Cornell. Aditya and Volodymyr were students of Stefano, and they kind of built this diffusion-based algorithm.”

Patel added, “All [the diffusion algorithms] came from the Stanford labs. No one had figured out how to use this algorithm for text modality. That’s the breakthrough Stefano had, and he’s taken sabbatical from Stanford and started this company.”

Inception is a small company, he said, and is making the most of its resources by focusing on two verticals: coding and voice.

“We can actually cover the full gamut of use cases, but we’re a 25-person startup company, so that’s really not how we go to market,” Patel said.

Why has it decided to focus on coding and voice? “Because those two are most speed-sensitive. When you’re doing coding and you’re doing something like auto-complete, if I can type faster than the auto-complete, it’s kind of useless.”

Voice agents require speed to avoid latency due to their real-time nature.

“We are a text-to-text modality, so we’re not voice-to-voice,” Patel said. “You use an ASR, you get text, you use the model —and the heart of it is the engine, which is our Inception Mercury diffusion model — and then you do text-to-speech. We’ve got a couple of customers doing that at scale.”

Inception, he said, has started to work with coding IDEs who depend on “model people, those from places like Stanford who have spent years researching for their doctorate degrees.

“We are the default LLM for many of the IDE plugins,” Patel said. “If you look at this whole coding and IDE space, these people are really good at building IDEs. They understand the coder environment. They’re not models people. Models people come from Stanford and have Ph.D.s. We’re the models.”

Inception works with [Continue](https://www.continue.dev/), an open source coding agent. The startup also works with such companies as [Proxy AI](https://www.codegpt.ee/), [JetBrains](https://www.jetbrains.com/), [Kilo Code](https://kilo.ai/), and [Cline](https://cline.bot/).

## How the Mercury Model Integrates into Existing Systems

Mercury is API compatible with OpenAI and the standard models. Integration requires single or low double-digit lines of code, the API is lightweight and it follows the same protocols.

In these times, algorithmic efficiency matters more than ever for companies using generative AI.

“Our model price is 25 cents per million input tokens and $1 for a million output tokens,” Patel said. “We’re more cost-efficient. We can serve these models more efficiently, and that’s what keeps our costs down.”

Inception’s deployment models vary, Patel said. For instance, users get 10 million tokens when they create an account. The API documentation helps them start building their programs and developing their model.

Some companies have data sovereignty requirements, and in that case, they can host the model themselves through Amazon Bedrock or Azure Foundry.

“If you look at Bedrock, there are over 20 different model choices you have available to you, including open source,” said [Alvaro Echeverria](https://www.linkedin.com/in/echeverriaalvaro/), director of startups for Latin America at [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), in a discussion at AWS re:Invent.

“We don’t believe there’s one model that will solve every use case, and you can choose and pick which one’s for you,” Echeverria said. “And things like Bedrock will allow you to fine-tune it.”

Currently, Inception only works with Nvidia for GPUs, Patel said.

Diffusion models have considerable upside. Inception is early to the game, and that brings its own advantages. Still, diffusion models’ capabilities in the realm of text don’t compare historically to their autoregressive counterparts.

For a detailed technical analysis comparing autoregressive and diffusion technologies, check out [Greg Robison’s Medium post](https://gregrobison.medium.com/a-comparative-analysis-of-diffusion-and-autoregressive-models-for-text-generation-architectures-99fb24fa390c) on the topic.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/13c3d9d6-cropped-0fe18b69-ef774ac85213a6506cf973dc6380cd57.jpeg)

Alex Williams is founder and publisher of The New Stack. He's a longtime technology journalist who did stints at TechCrunch, SiliconAngle and what is now known as ReadWrite. Alex has been a journalist since the late 1980s, starting at the...

Read more from Alex Williams](https://thenewstack.io/author/alex/)