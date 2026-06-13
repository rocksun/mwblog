On Tuesday, Anthropic launched Fable 5, its first generally available Mythos-class model.

Fable 5 is essentially the highly capable Mythos model the company has been talking about for the last few weeks, but with guardrails in place to ensure that it can’t be misused to build malware or bioweapons, for example.

To complicate matters, the company also launched Mythos 5, an updated version of Mythos without some of these guardrails, but it will initially be available only to [members of Project Glasswing](https://thenewstack.io/anthropic-glasswing-mythos-cybersecurity/).

## Fable 5 availability: the first one is always free

Unlike Mythos, though, you can use Fable 5 today. [Anthropic says](https://www.anthropic.com/news/claude-fable-5-mythos-5) it’s now available in the API (and on Microsoft Foundry, Amazon Bedrock, and the [Claude Platform on AWS](https://thenewstack.io/anthropics-claude-platform-comes-to-aws/)) for $10 per million input tokens and $50 per million output tokens. That’s twice the price of Anthropic’s current Opus model.

> Anthropic says Fable 5 is better at conceptual reasoning, working with documents, and interpreting charts and tables.

For now, Fable 5 is also available to those with Claude Pro, Max, Team, and seat-based enterprise subscriptions, but there’s a catch: it’ll be gone after June 22. Starting June 23, Fable 5 usage will require usage credits.

The reason for this is, as with so many of the things Anthropic currently does, capacity. “After this point — when sufficient capacity allows us to do so — we aim to restore Fable 5 as a standard part of subscription plans. We intend to do this as quickly as we can,” Anthropic explains.

## Benchmarks

What you are getting, however, is a model that excels on virtually every benchmark — and generally by a very healthy margin.

On SWE-Bench Pro, a set of tests that have the model solve problems across a curated set of code repositories, Fable scores 80% (and Mythos 5, without the guardrails, 80.4%). That’s well ahead of Anthropic’s own Opus 4.8 at 69.2%, and of OpenAI’s GPT 5.5 and Google’s Gemini 3.1 Pro at 58.6% and 54.2%, respectively.

![](https://cdn.thenewstack.io/media/2026/06/de807b3d-1e65982497d7d4891219ed0e83141625a291b860-2600x2870-2-928x1024.webp)

The same holds true for virtually every other kind of benchmark, no matter whether their focus is on coding, tool use, computer use, or knowledge work.

Benchmarks only tell part of the story, though, and don’t always reflect how well a model works in real-world usage. Anthropic argues that Fable 5 and Mythos 5 can work autonomously for longer than its other models and handle more complex tasks. Stripe, for example, had Fable 5 modernize a 50-million-line Ruby codebase in one day — something the company says would’ve otherwise taken a team of developers two months.

The reason it can do that is, in part, because, as Anthropic notes, the new models can stay “focused across millions of tokens in long-running tasks and improve its outputs using its own notes.”

![](https://cdn.thenewstack.io/media/2026/06/0587ccfa-d3c3efe0e8ab310856368cee2b2161439db6676a-1920x1080-1-1024x576.webp)

Mario Rodriguez, GitHub’s Chief Product Officer, also argues that this ability to stay focused longer allows Fable 5 to take on more complex programming tasks.

“Fable 5 is a real step forward for the developers GitHub serves,” he says in a quote included in Anthropic’s announcement blog post. “In our early testing, it took on complex, long-horizon coding tasks with a level of autonomy and reliability that exceeded previous benchmarks. But what excites us most is the direction it points: a future where developers can hand increasingly ambitious work to agents and trust the results across the software lifecycle.”

For knowledge work, where this enhanced memory capability also comes into play, Anthropic says Fable 5 is better at conceptual reasoning, working with documents, and interpreting charts and tables.

## Safeguards and refusals

Safeguards are obviously a key feature of Fable 5. One risk here is that the model will reject too many answers if Anthropic tunes it to be overly conservative. According to Anthropic, the original [Mythos model was too dangerous to release](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/), after all, and the company argues that all Mythos-class models “need strong safeguards to prevent misuse, and their coverage needs to be broad. The safeguards themselves have to stand up to sustained and sophisticated attempts to bypass them.”

When the model detects potential misuse, it will not answer those questions directly. Instead, when it detects requests related to “cybersecurity, biology and chemistry, or distillation,” it will hand the job over to Opus 4.8.

> In my own testing, Fable 5 refused to reason over its own model card, likely because it includes quite a few mentions of the very topics the model is supposed to avoid.

Anthropic says this has only happened in fewer than 5% of Fable sessions so far, but chances are those with early access to the model don’t necessarily represent the majority of Claude users.

In my own testing, Fable 5 refused to reason over its own model card, likely because it includes quite a few mentions of the very topics the model is supposed to avoid.

## 30-day data retention

One thing users *can’t* do when they want to use a Mythos-class model is opt out of any data retention. Going forward, using those models means opting in to 30-day data retention — or not using them at all.

Anthropic says it won’t train new models on this data and that it is logging all human access to it. But the company argues that it needs this data to help it “defend against complex and novel attacks (including new jailbreaks and attacks that operate across many requests) as well as help us identify and reduce false positives.”

Some enterprises, however, will still not want to opt in to Anthropic storing their data at all.

## What’s next

Fable 5 is clearly the most capable model on the market right now. That’s pretty much what everybody expected, and anything less would have been a major disappointment.

This means the [early reactions to the release](https://news.ycombinator.com/item?id=48463808) focused less on the capabilities and more on the rollout, with its short usage window for subscribers and the data retention policies.

Now it remains to be seen if the model can live up to the hype in real-world scenarios. And that tends to take a few days.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)