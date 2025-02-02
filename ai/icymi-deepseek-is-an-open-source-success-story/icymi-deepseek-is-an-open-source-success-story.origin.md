# ICYMI: DeepSeek Is an Open Source Success Story
![Featued image for: ICYMI: DeepSeek Is an Open Source Success Story](https://cdn.thenewstack.io/media/2025/01/31d13318-deepseek-1024x768.png)
Nvidia stockholders have about [$400 billion less](https://x.com/brewmarkets/status/1883887544200499259) in their pockets today thanks to the open source efforts of a Chinese AI startup company called [DeepSeek](https://www.deepseek.com/). And OpenAI, as well as the other commercial AI model providers, might have to rethink their business models.

And the $500 billion in data centers the [U.S. needs to keep its competitive edge for AI](https://thenewstack.io/ai-power-needs-may-strain-us-grid-as-stargate-project-grows/)? Might not be necessary after all.

Kicking off the hysteria last weekend was the release of [DeepSeek’s R1 reasoning model](https://api-docs.deepseek.com/news/news250120), which showed comparable results to OpenAI’s latest release [O1](https://openai.com/o1/), but at [1/50th](https://x.com/_KarenHao/status/1883877988682649931) of the training cost.

Just as importantly, DeepSeek was released as fully open source, under a[ very permissive MIT License](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/), so any other company could replicate the model.

The implication, should DeepSeek’s promises test out, is that companies no longer would be beholden to [OpenAI](https://thenewstack.io/open-source-may-yet-eat-googles-and-openais-ai-lunch/) and other multibillion-dollar commercial services to build their own generative AI apps.

“DeepSeek has provided a massive gift to nearly everyone,” [observed](https://stratechery.com/2025/deepseek-faq/) Anthropic AI engineer [Ben Thompson](https://tbenthompson.com/). “The biggest winners are consumers and businesses who can anticipate a future of effectively free AI products and services.”

## From Crisis Comes Opportunity
DeepSeek came up with this new architecture chiefly because of limitations, namely the U.S. export limits of the [Nvidia H100,](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/) the latest Nvidia GPU.

Worried about maintaining AI superiority, the United States had prohibited sale of Nvidia’s H100 chips to China. In response, Nvidia came up with the stripped-down H800, which DeepSeek engineers optimized their LLM around instead.

Some clever engineering demonstrated that training leading edge models doesn’t necessarily require more interchip memory bandwidth.

“All of the decisions DeepSeek made in the design of this model only make sense if you are constrained to the H800,” Thompson wrote. “If DeepSeek had access to H100s, they probably would have used a larger training cluster with much fewer optimizations specifically focused on overcoming the lack of bandwidth.”

So they HAD to use the slower H800 instead, and do a lot of fiddly AI engineering things to fit its LLM on smaller platforms.

The results were so good, in fact, that it raised a lot of questions around if we actually need $500 billion data center infra or expensive Nvidia chips when DeepSeek could do it at the fraction of the cost.

It showed a way where we don’t need large data centers just to serve up AI.

## Open Source at the Heart
Don’t worry if you haven’t heard of DeepSeek before. It’s one of a[ number of Chinese startups](https://x.com/RnaudBertrand/status/1883456746058129826) competing in the large model market.

The DeepSeek LLM [actually started](https://x.com/0xmetaschool/status/1882721476723536178) as a side project for the company, something to do with its leftover GPUs.

The CEO has made it a point of pride to open source, and publish papers, about its work.

“Open source, publishing papers, in fact, do not cost us anything. For technical talent, having others follow your innovation gives a great sense of accomplishment. In fact, open source is more of a cultural behavior than a commercial one,” DeepSeek CEO [Liang Wenfeng](https://apnews.com/article/deepseek-founder-liang-wenfeng-china-ai-0673d5c39d90108189cc31b88d85b9f8) told [China Talk](https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas).

The company didn’t go this route for the money but did it for recognition and, just as importantly, to attract better talent. And to level the playing field.

“In the face of disruptive technologies, moats created by closed source are temporary. Even OpenAI’s closed source approach can’t prevent others from catching up,” he said.

## The Technical Side
In looking to cut computational costs, the engineering team adapted some [innovative practices](https://stratechery.com/2025/stratechery-updates-deepseek-r1-deepseek-implications/) for the AI space.

Crucial to this success is a technique called distillation, which in a nutshell, queries another LLM for training. This is the area where the DeepSeek’s open source claims get murky, noted [Amanda Brock](https://www.linkedin.com/in/amandabrocktech/), [OpenUK CEO](https://thenewstack.io/the-open-source-license-rug-pull-vent-get-your-fill-at-soo25/), in an upcoming post for TNS. She worries about the legality of the upstream data being used for DeepSeek.

But the model itself is less important than how the model is built.

Another tactic is to switch back to an on older technique, [reinforcement learning](https://thenewstack.io/reinforcement-learning-ready-real-world/), to improve reasoning abilities. Traditional models use reinforcement learning with human feedback to help guide the models toward the correct responses. DeepSeek built the reinforcement learning directly into the model itself. It could work out several responses and then, using self-guided reasoning, choose the one that seemed the most correct.

“You don’t need to teach the AI how to reason, you can just give it enough compute and data, and it will teach itself!” Thompson wrote.

R1 built on a lot of engineering work that come in previous releases, the [V3](https://api-docs.deepseek.com/news/news1226) and [V2](https://api-docs.deepseek.com/news/news1210) models for DeepSeek. V2 introduced the idea of “mixture of experts,” (MOE) meaning that not every part of the model would be fired up for each question, thereby saving memory space (OpenAI’s ChatGPT 4.0 also dove into MOE, though not at the same granularity).

V3 refined the MOE model and also brought further memory savings by reducing the size of the context window (user-supplied data) through a key-value store.

“V3 was [shockingly cheap](https://arxiv.org/html/2412.19437v1) to train. DeepSeek claimed the model training took [~2.7 million] H800 GPU hours, which, at a cost of $2/GPU hour, comes out to a mere $5.576 million,” Thompson wrote.

That’s $5 million, not $100 billion that OpenAI has claimed it needs to train its leading-edge models.

The greater efficiency could also be reflected in the costs of DeepSeek’s [API service](https://api-docs.deepseek.com/guides/reasoning_model), which offered a million tokens at $2.19, compared with $60 per million tokens for [OpenAI O1](https://openai.com/o1/).

You can test DeepSeek via an [app download](https://api-docs.deepseek.com/news/news250115) or by [web chat interface](https://chat.deepseek.com/).

## Lost Value
The implications, should DeepSeek prove to be as cost-effective as promised, could be massive.

It shows, as Thompson points out “OpenAI does not have some sort of special sauce that can’t be replicated.”

Wenfeng’s view was that OpenAI, Nvidia and Oracle were using the large computing requirements as a barrier to entry in the AI market, and some good open source know-how just completely obliterated that moat.

Wait a minute. You mean to say that we don’t need to blanket the earth with data centers and coal & gas plants to maybe arrive at a future where we can wave a magical AGI wand to make all of the consequences of that go away?

Yes. This is a false trade off. Let that sink in. 16/

— Karen Hao (@_KarenHao)

[January 27, 2025]
Companies can build generative AI apps at the fraction of what they would have previously cost, thanks to radically lower inference costs. They would still benefit from speedy Nvidia GPUs, but they wouldn’t necessarily need data centers filled with them.

The previously sky-high stock valuations of GPU provider Nvidia in particular benefitted from the company’s perceived lock-in value: The proprietary [Cuda programming model](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/) and the the ability the lash together multiple GPUs into larger systems, Thompson noted.

“For Nvidia, this is scary. Their entire business model is built on selling super-expensive GPUs with 90% margins. If everyone can suddenly do AI with regular gaming GPUs … well, you see the problem,” [noted](https://x.com/morganb/status/1883686179276788197) Dropbox VP [Morgan Brown](https://www.linkedin.com/in/morganb/).

Likewise, OpenAI is now fully a consumer tech company and faces a larger more commoditized market. According to [The Information](https://www.theinformation.com/articles/meta-scrambles-after-chinese-ai-equals-its-own-upending-silicon-valley), the management of Meta Generative AI is worrying about the [massive costs of building](https://x.com/a_boutorh/status/1882728052238827966) their own LLama 4 model after it tested worse than DeepSeek.

Microsoft CEO Satya Nadella [evoked](https://x.com/satyanadella/status/1883753899255046301) Jevon’s Paradox, in which, “As AI gets more efficient and accessible, we will see its use skyrocket, turning it into a commodity we just can’t get enough of.”

Even U.S. President Donald J. Trump recognized the power of open source in a recent press briefing, even if he didn’t call it out by name. “The release of DeepSeek AI from a Chinese company should be a wake-up call for our industries,” he said.

🚨TRUMP: “The release of DeepSeek AI from a Chinese company should be a wake up call for our industries that we should be laser focused on competing to win. We have the best scientists in the world. This is very unusual. We always have the ideas. We’re always first.”

[pic.twitter.com/fFiRjxMTmZ]— Autism Capital 🧩 (@AutismCapital)

[January 28, 2025]
“Deepseek R1 is one of the most amazing and impressive breakthroughs I’ve ever seen — and as open source, a profound gift to the world,” [Andreessen Horowitz](https://a16z.com/) cofounder Marc Andreesen [commented](https://x.com/pmarca/status/1882719769851474108).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)