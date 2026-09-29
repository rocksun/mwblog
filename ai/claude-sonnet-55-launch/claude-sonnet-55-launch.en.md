**Anthropic on Monday launched Claude Sonnet 5.5**, the latest version of its workhorse model and the second model in the Claude 5.5 family (after [Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/), which launched last week).

A new version of [Claude Haiku](https://thenewstack.io/anthropic-launches-claude-haiku-4-5/), the smallest and most affordable model in the family, is on the roadmap and will launch “in the coming weeks.”

## 30% faster, up to 30% cheaper

The new Sonnet model, Anthropic says, generates output more than 30% faster than its predecessor, [Sonnet 5](https://thenewstack.io/claude-sonnet-5-launch/), while lowering the cost per task by up to 30%. That makes Sonnet 5.5 the company’s fastest Sonnet model yet and, as Anthropic puts it, “a faster, lower-cost complement to Claude Opus 5.5.”

Anthropic argues that the model is “strongest at well-scoped everyday tasks, fixing bugs, and creating polished documents, slides, and spreadsheets.” Early testers also noted that it “adds polish to user interfaces and can follow slide templates to create decks that require minimal editing.”

Like Opus 5.5, Sonnet 5.5 also writes more clearly than Anthropic’s previous generation of models. With Opus 5.5, the company promised a clearer, more natural-sounding voice, and Sonnet 5.5 now shares that trait.

## Close to Opus on most benchmarks

Anthropic says the biggest gains are in coding. On Terminal-Bench 4.0, which tests agents on command-line tasks, Sonnet 5.5 scores 70.6%, up from 10.3% for Sonnet 5 and ahead of Opus 5.5’s 66.4%. (The benchmark’s maintainers noted that Sonnet 5 sometimes ran into timeouts and token limits, which helps explain its low score.)

On CursorBench, which uses tasks from real Cursor coding sessions, Sonnet 5.5 comes within about two points of Opus 5.5. On Cognition’s FrontierCode, which checks whether a code change could be merged without human edits, it scores 52.1% at its second-highest effort setting, compared to 54.4% for Opus 5.5 and 49.3% for OpenAI’s GPT-6 Sol.

![](https://cdn.thenewstack.io/media/2026/09/d8895bd6-screenshot-2026-09-28-at-19.33.05-1024x417.png)

![](https://cdn.thenewstack.io/media/2026/09/81c5cd65-screenshot-2026-09-28-at-19.39.12-1024x370.png)





Claude Sonnet 5.5 benchmarks. Credit: Anthropic.

For knowledge work, Sonnet 5.5 scores 1,844 on Artificial Analysis’ GDPval-AA, which ranks models by Elo score on real-world tasks across 44 occupations. That’s only two points behind Opus 5.5 and about 400 points ahead of Sonnet 5. Sonnet 5.5 also bests GPT-6 Sol’s score of 1,487.

The new model also comes close to Opus 5.5 in computer use and on Humanity’s Last Exam. And in a less formal test of long-horizon work and image understanding, Anthropic says it’s the first Sonnet model to beat *[Pokémon Red](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Red,_Blue,_and_Yellow)* working only from screenshots.

On several benchmarks, Anthropic says, Sonnet 5.5 at low or medium effort beats Sonnet 5’s best score for about a tenth of the cost per task.

Still, the company says Opus 5.5 remains “clearly stronger at complex, open-ended work requiring sustained judgment.”

## Pricing and availability

While Anthropic cut prices for Opus 5.5 (to $4 per million input tokens and $20 per million output tokens), and OpenAI halved prices for its [GPT-6 Sol and Luna models](https://thenewstack.io/openai-gpt-6-sol-luna-release/) on the same day, the pricing for Sonnet 5.5 remains unchanged at $2 per million input tokens and $10 per million output tokens. Cache reads come in at $0.20 per million tokens.

That’s the same list price as GPT-6 Sol, OpenAI’s second-best model after Astra.

Since the new model uses far fewer tokens, though, at least according to the company’s own measurements, running it should be cheaper than running Sonnet 5.

Sonnet 5.5 is now available on the Claude Platform, Amazon Web Services, Google Cloud, and Microsoft Azure. Developers who run Sonnet with thinking turned off will need to switch to a new `between_tools` setting before moving to Sonnet 5.5. Opus 5.5 [already rejects requests](https://thenewstack.io/claude-opus-agent-migration/) that turn thinking off entirely.

## Safeguards

Because Anthropic believes Sonnet 5.5’s cybersecurity capabilities are comparable to Opus 5’s, this is the first Sonnet model to launch with the same kind of cyber safeguards Anthropic also uses for its most capable models.

Routine bug fixing isn’t affected, the company says, but higher-risk cybersecurity requests will fall back to Sonnet 5. It’s also the first Sonnet model with classifiers designed to stop attackers from [extracting its reasoning to train their own models](https://thenewstack.io/moonshot-fable5-distillation-accusations/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)