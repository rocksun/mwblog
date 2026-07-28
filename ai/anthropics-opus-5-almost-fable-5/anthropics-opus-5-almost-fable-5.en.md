**Anthropic launched Opus 5 on Friday**, the latest version of what used to be the company’s flagship model (before the launch of Fable 5).

Opus 5, Anthropic says, comes close to the performance of Fable 5 in many domains — all at half the price of Fable 5, with the token cost remaining $5/$25 per million input/output tokens, unchanged from Opus 4.8. Unlike Fable 5, users don’t have to opt into a 30-day data retention policy to use Opus 5. It’s now the default model for Claude Max subscribers (and the best model Claude Pro subscribers can access).

## Almost Fable 5

Unsurprisingly, Opus 5 is Anthropic’s most capable Opus model yet, and the company stresses that it can also autonomously perform work for much longer than before, checking its own work and recovering from errors.

Fable 5, though, remains the model to go to for “your most ambitious work” and for projects that need days-long autonomy, Anthropic says. Opus 5, meanwhile, is what Anthropic describes as “designed to be used every day.”

![](https://cdn.thenewstack.io/media/2026/07/1bb4ab5e-screenshot-2026-07-24-at-10.20.02-am-1024x699.png)

It’s probably this ability to work on a project for a very long time that still sets Fable 5 apart, because on virtually every benchmark Anthropic has shared so far, Opus 5 actually outperforms Fable 5.

That leaves Sonnet 5, which launched only a few weeks ago, in a bit of an awkward position between the cheaper, faster but far less capable Haiku 4.5, and the more capable but expensive Opus and Fable family. Sonnet 5, after all, was previously positioned as the “most efficient for everyday tasks.”

## Opus 5 benchmarks

The new Opus model is especially strong when it comes to doing knowledge work and improves on Opus 4.8’s coding abilities. It scores 1861 on the GDPval-AA v2 knowledge work benchmark, ahead of Fable 5 (1747), GPT-5.6 Sol (1736), and Opus 4.8 (1593).

It’s also the top model on Zapier’s [AutomationBench](https://zapier.com/benchmarks), which measures AI agents on end-to-end business workflows (and where Google’s new [Gemini 3.6 Flash](https://thenewstack.io/google-ships-3-new-gemini-models-just-not-the-one-everyones-waiting-for/) spent a very short time at the top earlier this week). Anthropic says Opus 5’s pass rate there is double the next-best model’s at the same cost per task, and that even at its lowest effort setting, the model passes more tasks than any other.

| Benchmark | Opus 5 | Fable 5 | Opus 4.8 | GPT-5.6 Sol |
| --- | --- | --- | --- | --- |
| **Agentic terminal coding** Frontier-Bench v0.1 | **43.3%** | 33.7% | 18.7% | 37.5% |
| **Knowledge work** GDPval-AA v2 | **1861** | 1747 | 1593 | 1736 |
| **Agentic search** BrowseComp | **90.8%** | 87.4% | 84.3% | 90.4% |
| **Multidisciplinary reasoning** Humanity’s Last Exam | 56.3% no tools  **64.7%** with tools | **56.5%** no tools  63.9% with tools | 49.8% no tools  57.9% with tools | —  — |
| **Computer use** OSWorld 2.0 | **70.6%** | 66.1% | 55.7% | 62.6% |
| **Agentic coding** DeepSWE v1.1 | 68.8% | 69.7% | 59.0% | **72.7%** |
| **Agentic coding** FrontierCode v1.1, Main | **53.4%** | 53.5% | 46.5% | 47.5% |
| **Business workflows** AutomationBench | **26.0%** | 17.4% | 17.0% | 18.1% |
| **Legal** Legal Agent Benchmark, Held-out | 11.7% | **13.3%** | 10.4% | 2.5% |
| **Health** HealthBench Professional | 59.8% | Mythos 5 **66.0%** | 57.4% | 60.5% |
| **Biology** BioMysteryBench | **49.4%** hard  **90.1%** human solved | 46.5% hard  Mythos 5 89.0% human solved | 42.4% hard  88.5% human solved | —  — |

Credit: Anthropic

**Anthropic also says Opus 5 is its best and most cost-effective model** so far on DeepSearchQA and Humanity’s Last Exam (with tools), where it even edges out Fable 5 (64.7 percent vs. 63.9 percent). Without giving the models access to tools, Fable 5 stays ahead.

Fable 5 does keep its lead in a few places, though, among them Anthropic’s held-out legal agent benchmark and DeepSWE, while Mythos 5 remains the company’s strongest model on health benchmarks.

As for coding, Anthropic says that on CursorBench 3.2, Opus 5 beats every other model on performance-per-cost at the high, extra high, and max settings; at max effort, the company says, the model lands within 0.5 percent of Fable 5’s peak score at half the cost per task.

In prepared remarks released by Anthropic, Cursor co-founder Sualeh Asif says, “Claude Opus 5 delivers near Fable 5 intelligence at Opus speed and cost. On CursorBench it’s just under Fable 5 and has many of the same behaviors. We are excited to see how developers use it in Cursor.”

As before, users across Anthropic’s products can choose between low, medium, high, extra high, and max settings with their respective boosts in intelligence (and token usage).

## Opus 5 safety

Anthropic also calls Opus 5 its most aligned model to date, based on its automated behavioral audits, and, together with Fable 5, the least susceptible to being tricked into misuse.

The company says it intentionally didn’t train the model on cybersecurity tasks. Opus 5 nevertheless comes close to Mythos 5 at finding vulnerabilities in open-source code, while remaining far behind at actually exploiting them — which is pretty much where Anthropic [wants it to be](https://thenewstack.io/anthropic-fable-ban-lifted/).

![](https://cdn.thenewstack.io/media/2026/07/52c9c9d8-screenshot-2026-07-24-at-7.56.58-am-1024x470.png)

To keep it safely out of any [Fable 5-like trouble](https://thenewstack.io/anthropic-fable-mess-explained/), Opus 5 ships with a set of safety classifiers that screen requests for a narrow range of cyber tasks, including exploit generation and penetration testing. Because they’re scoped more narrowly than Fable 5’s, Anthropic expects them to intervene about 85% less often.

The idea, Anthropic says, is to leave room for defensive work like finding vulnerabilities in source code, while still blocking so-called [“binary-based vulnerability scanning](https://www.binarly.io/blog/introducing-vulhunt-a-high-level-look-at-binary-vulnerability-detection)“, a technique Anthropic says is more likely to be associated with malicious actors.

When a classifier does flag a request in Claude.ai, Claude Code, or Cowork, it falls back to Opus 4.8 by default, and API users can enable the same behavior. Enterprises and researchers in Anthropic’s Cyber Verification Program get access to a version of Opus 5 with fewer of these restrictions.

Like other frontier labs, Anthropic is using this release to highlight the cost-effective nature of its models. At this point, every business is concerned about token cost and every lab is now sensitive to how the price of its models is perceived.

> At this point, every business is concerned about token cost and every lab is now sensitive to how the price of its models is perceived.

Harvey, the legal AI company, saw its biggest gains with Opus 5 in practice areas like corporate governance and arbitration, says Niko Grupen, its head of applied research. “We were also impressed,” Grupen says, “with Opus 5’s ability to maintain quality at lower reasoning levels, achieving similar performance while generating 26% fewer tokens on average compared to Opus 4.8 at max reasoning.”

## Opus 5 fast mode

Like Opus 4.8, Opus 5 will also offer a “fast mode,” both on the Claude Platform for developers and, by drawing down extra usage credits, in Claude Code. It will generate output tokens 2.5x faster and cost 2x more.

There are also two smaller platform updates that launch in beta today. With automatic fallbacks, API requests that Anthropic’s safety classifiers decline on Opus 5 or Fable 5 can automatically route to another model within the same request, instead of returning an error. Developers can also now change which tools Claude can use mid-conversation without invalidating the prompt cache, so each phase of an agent’s work only sees the tools it needs.

Opus 5 is available today on all of Anthropic’s paid plans and on the Claude Platform as `claude-opus-5`.

## Background

While [Opus 4](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) launched in May 2025, it was [Opus 4.5](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/) in November and [Opus 4.6](https://thenewstack.io/claude-sonnet-46-launch/) in February 2026 that cemented the model family’s reputation as one of the best (and, at times, *the* best) models for coding.

For many users, [Opus 4.7](https://thenewstack.io/claude-opus-47-launch/), which launched in April 2026, was a bit of a disappointment, which maybe explains why Anthropic released the well-received [Opus 4.8](https://thenewstack.io/claude-opus-48-release/) only a month-and-a-half later.

With Mythos and Fable, Anthropic more recently created a new tier of flagship models, but the company says it expects Opus 5 to be “the model we’d expect people to reach for every day, especially in the enterprise.”

OpenAI recently launched its [GPT-5.6 Sol, Terra, and Luna family](https://thenewstack.io/openai-gpt-56-live/), with the Sol flagship model slightly more expensive than Opus 5 at $5/$30 per million input/output tokens. In the benchmark table Anthropic shared with this launch, Sol beats Opus 5 on just one of those benchmarks, the agentic coding test DeepSWE v1.1 (72.7 percent vs. 68.8 percent). Everywhere else, Anthropic is ahead, including on knowledge work, computer use, and business workflows.

Google’s Gemini models, meanwhile, don’t appear in Anthropic’s comparison table at all. Apparently, Anthropic didn’t think they rated an extra column.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)