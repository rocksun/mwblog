The AI model release cycle continues. On Thursday, OpenAI [released](https://openai.com/index/introducing-gpt-5-5/) GPT-5.5 and GPT-5.5 Pro. The new model is, unsurprisingly, its most capable model yet.

GPT-5.5 will be available to all paying OpenAI users in ChatGPT and Codex, while GPT-5.5 Pro will be rolling out to Pro, Business, and Enterprise users in ChatGPT only. It will be available in the API soon (but will also be more pricey than before).

After Anthropic [launched Opus 4.7](https://thenewstack.io/claude-opus-47-launch/) a week ago, it was only a matter of time before OpenAI would follow suit — and, at least according to the benchmarks we’ve seen so far, GPT-5.5 and 5.5 Pro beat Opus 4.7 across many of today’s standard benchmarks. In many benchmarks, though, GPT-5.4 Pro still outperforms the default GPT-5.5.

On a press call ahead of the launch, OpenAI president and co-founder Greg Brockman described GPT-5.5 as “a new class of intelligence. It’s a big step towards more agentic and intuitive computing.”

![](https://cdn.thenewstack.io/media/2026/04/63a3057d-screenshot-2026-04-23-at-10.19.56-1024x483.png)

GPT-5.5 benchmarks. Credit: OpenAI.

According to Brockman, the new model is especially good at working with less guidance. “It’s just like, way more intuitive to use,” he says. “It can look at an unclear problem and figure out just what needs to happen next. It really, to me, feels like it’s setting the foundation for how we’re going to use computers, how we’re going to do computer work, going forward — for how agentic computing at scale will work.”

Yet even with these additional capabilities, the new model is not any slower than its predecessor and uses fewer tokens. “It’s a faster, sharper thinker for fewer tokens, compared to something like [GPT] 5.4, so this means that there’s just more frontier AI available for businesses and for consumers, which is part of our goal,” he says (with maybe a hint of a sideswipe at Anthropic for its recent capacity issues).

Specifically, latency for GPT-5.5 on a per-token basis remains the same as for the previous model, all while also being more efficient about its token use. OpenAI argues that GPT-5.5 is able to deliver state-of-the-art intelligence “at half the cost of competitive frontier coding models.”

## Benchmarks

The model, of course, is also better at coding. OpenAI’s VP of Research [Mia Glaese](https://www.linkedin.com/in/amelia-glaese/) notes that the model is now far better at “senior engineering work in Codex,” for example. One early tester with access to the new model, for example, gave GPT-5.5 a sloppily vibecoded codebase and asked it to turn it into a “nice codebase,” as Glaese describes it. What the model produced was essentially what a senior engineer would have done, Glaese says.

In the benchmarks, including Terminal-Bench 2.0, which tests how the model handles command-line workflows for developers, and SWE-Bench Pro, which tests how the model solves real-world GitHub issues, scores 82.7% and 58.6%, respectively.

We don’t have SWE-Bench Pro scores for Anthropic’s Opus 4.7, but on SWE-Bench Pro, it reached 64.3%, which is one area where Opus still has the upper hand, it seems. But on Terminal-Bench 2.0, GPT 5.5 scores 82.7%, while Opus only reaches 69.4%.

OpenAI did not provide coding benchmarks for GPT-5.5 Pro yet.

Computer use, too, is getting another intelligence bump with this update, as OpenAI’s Chief Research Officer [Mark Chen](https://www.linkedin.com/in/markchen90/) stresses. “With Codex’s computer-use capabilities, we’re really starting to feel like we have a model which approaches computer use with the same kind of dexterity and accuracy as it does with manipulating code,” he says.

![](https://cdn.thenewstack.io/media/2026/04/076461cc-screenshot-2026-04-23-at-10.25.59-1024x691.png)

GPT-5.5 token use comparison. Credit: OpenAI.

In the benchmarks, GPT 5.5 and Opus 4.7 aren’t very far apart, though at 78.7% on the OSWorld-Verified test, which asks the models to perform computer tasks in the operating system, GPT-5.5 is slightly ahead of Opus 4.7’s 78%.

![](https://cdn.thenewstack.io/media/2026/04/7d7c0ba0-gdpval-1024x663.png)

Credit: OpenAI.

One area where Opus — and to some degree even Google’s older Gemini 3.1 Pro — continue to outperform GPT-5.5 is in many academic benchmarks, but GPT-5.5 beats both of them when it comes to the math benchmarks like FrontierMath Tier 1-3 and Tier 4.

![](https://cdn.thenewstack.io/media/2026/04/17976f34-screenshot-2026-04-23-at-10.39.17-1024x386.png)

Credit: OpenAI.

With this update, OpenAI once again stresses that it used the model itself — and Codex — in building this update.

One interesting point Brockman stresses is that, for OpenAI, the model itself is now only one part of a larger product.

“So we at OpenAI, we want to bring agentic capabilities to all people who are trying to get their work done with their computer, not just as software engineers,” he says. “And one thing to understand is that the model itself is no longer the whole product, right? You can think of it as the brain, but also building the body in terms of the applications we ship, the agentic harnesses — that’s something we’re advancing as well.”

## GPT-5.5 in the age of Mythos

Given the recent discussion around Anthropic’s Mythos model and its cybersecurity capabilities, OpenAI also stresses how it is mitigating those risks with this current release.

The company argues that it believes the best path forward for models with advanced cybersecurity capabilities is to “make sure [the models] can be put to use for accelerating cyber defense and strenghtening the ecosystem.”

OpenAI says it is deploying “industry-leading safeguards” and plans to expand access to accelerate cyber defense at every level.

On the CyberGym benchmark, GPT-5.5 scores 81.8%. Mythos, according to Anthropic, scored 83.1%.

![](https://cdn.thenewstack.io/media/2026/04/e3bb59cd-screenshot-2026-04-23-at-10.55.08.png)

Credit: OpenAI.

## Availability and price

GPT-5.5 is comping to all paying ChatGPT users in ChatGPT and Codex, with GPT-5.5 Pro limited to Pro, Business and Enterprise users in ChatGPT. There will also be a GPT-5.5 Thinking mode, which will also be available to all paying users.

For those who need more speed in Codex, where GPT-5.5 will have a 400,000-token context window, OpenAI is also making a Fast mode available. This mode will be 1.5x faster, but also cost 2.5x more.

In the API, GPT-5.5 will cost $5 per 1 million input tokens and $30 per 1 million output tokens and will feature a 1 million token context window. That’s twice the price of what OpenAI charged for GPT-5.4.

GPT-5.4 also had a tiered pricing structure, where shorter prompts under 272,000 tokens were charged at the standard rate while larger prompts cost $5/$22.5 per million input/output tokens.

OpenAI acknowledges the price difference in its blog post: “While GPT-5.5 is priced higher than GPT-5.4, it is both more intelligent and much more token efficient. In Codex, we have carefully tuned the experience so GPT-5.5 delivers better results with fewer tokens than GPT-5.4 for most users, while continuing to offer generous usage across subscription levels.”

For GPT-5.5 Pro, the cost are $30/$180 per million input/output tokens, the same as for GPT-5.4.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)