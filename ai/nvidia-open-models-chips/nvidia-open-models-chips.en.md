*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

Nvidia agreed to pay $12.9 billion for Hugging Face this week, [*The Information* reported](https://www.theinformation.com/articles/nvidia-agrees-buy-open-source-model-repository-hugging-face-12-9-billion). The purchase feels similar to when Microsoft bought GitHub.

Nvidia followed developers. It bought the place they already go for AI models. Meanwhile, Anthropic and OpenAI are selling a premium into a market that’s increasingly treating free as the default.

It’s getting easier to run those open models, too. Earlier this week, Ollama shipped a release that lets Claude Desktop run Qwen, DeepSeek, and Kimi. You open Anthropic’s app, click the model picker, and pick Kimi K3 instead of Opus 5.

Our own Paul Sawers [covered the Ollama release](https://thenewstack.io/ollama-claude-desktop-integration/) for *The New Stack*. Version 0.33.0 launched on August 21 and uses a local proxy to get around Claude Desktop’s block on non-Anthropic model IDs. Flip “Use Ollama models” in the Mac menu bar, and whatever you’re running, locally or on Ollama Cloud, shows up in Anthropic’s model picker. “Open models should be easy to run, easy to build with, and available wherever people need them,” Ollama CEO Jeffrey Morgan said. The company raised a $65 million Series B in July.

The hardware is catching up, too. Apple launched new Mac Mini and Mac Studio configurations this week that seem purpose-built to run larger models locally. Frederic Lardinois [wrote up Alibaba’s Qwen3.8-27B](https://thenewstack.io/qwen38-27b-local-inference/) two weeks ago. The 4-bit build is 16.1GB and runs on a Mac with 32GB of unified memory; Alibaba’s own benchmarks put it at or past Opus 4.6 Max for coding and computer use. Those are Alibaba’s benchmarks, and early users say the model overthinks. It still fits on a laptop.

The cost of switching dropped with it. TNS writer Janakirm MSV started covering this in May, when [OpenCode passed Claude Code on GitHub stars](https://thenewstack.io/anthropic-claudecode-opencode-split/), from 157,000 to about 122,000. The real decision in front of most developers, he writes, is “whether their environment can tolerate a single-vendor harness at all.” Jason Calacanis put the commercial version [on X on Wednesday](https://x.com/Jason/status/2092748113765126313): “Open source is solving 90% of startup use cases right now, so frugal founders aren’t paying for Fable.” Five hundred dollars per employee per month feels fine, he writes, but “when you start hitting five figures, CFOs start clenching.” Founders are the early signal. CFOs are the broader one.

## Nvidia is paying for the place developers get their models

So what does $12.9 billion buy Nvidia? A website with about $150 million in revenue. Nvidia already builds open models of its own and gives them away, so it isn’t short on weights.

Microsoft paid $7.5 billion for GitHub in 2018 because that’s where code lived, and owning it made GitHub the surface for everything Microsoft wanted developers to do next. Hugging Face is that for weights. Every open model release and every fine-tune lands there. It’s the default place developers go to figure out how to run one.

Product analyst Aakash Gupta [did the math](https://x.com/aakashgupta/status/2092810836142354830) to explain the price. Nvidia just reported $96.2 billion in quarterly revenue, so $12.9 billion is about 12 days of sales. And Nvidia’s largest customers are all building escape routes: OpenAI designing chips with Broadcom, Anthropic training on Amazon’s Trainium, Google a decade into its own TPUs.

Open models are the counterweight, because a downloaded model gets fine-tuned and served on Nvidia CUDA by default. As long as developers keep choosing open models, they’re also choosing Nvidia’s software stack. “Nvidia spent 12 days of revenue to make sure the open-source rival to its own customers never dies,” Gupta writes.

It works because open models run on Nvidia hardware. Download Qwen, fine-tune it, and every step runs on CUDA unless you go out of your way. Broadcom and Amazon can build a chip. Neither of them can make ten thousand repos target it.

So the thing you did to get out from under one vendor’s pricing put you further under another’s.

Hugging Face is also the leaderboard, the datasets, and the transformers library a good chunk of the industry uses. Nvidia will soon own all of it. The stalwart venture capitalist Bill Gurley [posted the reason](https://x.com/bgurley/status/2092812868098175408) on Wednesday: “Open-models are the inevitable outcome of high stakes software competition,” he writes. “The more at stake, the more likely open wins. This is water running downhill.”

He [made the longer case](https://www.washingtonpost.com/opinions/2026/07/20/open-model-ai-is-good-competition-anthropic-openai/) in *The Washington Post* in July, under a headline that names the two companies preparing to go public: Open-model AI is good competition for Anthropic and OpenAI.

The obvious objection is that Hugging Face downloads aren’t production traffic, and that most real work still runs against a closed API. It’s fair. But Chinese open models have taken [more than 30% of U.S. token usage on OpenRouter](https://aiweekly.co/alerts/chinese-ai-models-hit-record-58-of-us-openrouter-traffic) every week since February, peaking at 46%. Right now, that’s the corner of the market where switching is cheapest.

The lesson for AI-native developers isn’t to replace Claude with Qwen or stop paying Anthropic. Closed models will still be the right answer for plenty of work. The lesson is to stop assuming today’s default will still be tomorrow’s.

Every AI-native application has defaults: the model, the registry, the harness, the API. Those become dependencies, and dependencies become leverage. Nvidia reportedly agreed to spend $12.9 billion on the place developers already go to find and fine-tune models.

That changes the job for AI-native developers. Five years ago, the best developers learned Kubernetes. Today, they spend their time comparing benchmark scores and arguing about which model is smartest. And that’s becoming the less important skill. The hard one is building systems that survive when the underlying defaults change.

Because it will.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)