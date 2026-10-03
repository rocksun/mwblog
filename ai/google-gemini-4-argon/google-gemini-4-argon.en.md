**Google on Wednesday announced Gemini 4 Argon**, the company’s long-awaited flagship model, and it looks like it was worth the wait.

Across most benchmarks, Gemini 4 Argon beats OpenAI’s and Anthropic’s top models, sometimes by a wide margin, though where it trails, it can trail by as much as 10 points.

Google notes it is taking a phased approach and has “actively engaged in the U.S. government’s voluntary process for pre-release model access while we gradually expand access.”

> Gemini 4 Argon beats OpenAI’s and Anthropic’s top models by a wide margin.

The announcement comes only a day after Google CEO Sundar Pichai [co-signed a commitment](https://www.cnn.com/2026/09/29/business/amodei-huang-karp-trump) to “self-police” after a meeting with President Donald Trump. Anthropic, Meta, Nvidia, OpenAI, and SpaceX also signed this “commitment,” which doesn’t seem to come with any enforcement mechanism.

| Category | Benchmark | Gemini 4 Argon | GPT-6 Astra | Claude Fable 5.1 | Claude Opus 5.5 |
| --- | --- | --- | --- | --- | --- |
| Knowledge work | Vals Index | **68.9%** | 63.1% | 65.8% | 67.0% |
| Knowledge work | AutomationBench (Score) | **51.3%** | 41.4% | 31.4% | 42.5% |
| Knowledge work | Vals Finance Agent v2 | **65.4%** | 53.5% | 58.9% | 58.6% |
| Knowledge work | Harvey’s Legal Agent Benchmark | **19.6%** | 5.4% | 6.7% | 3.8% |
| Agentic coding | DeepSWE v1.1 | **77.9%** | 74.1% | 67.4% | 74.2% |
| Agentic coding | FrontierSWE v2 | 55.0% | **65.5%** | 56.3% | 62.3% |
| Agentic coding | Vibe Code Bench | **91.9%** | 89.6% | 90.3% | 90.3% |
| Agentic coding | Terminal-bench 4.0 | 57.4% | 58.2% | 57.9% | **66.4%** |
| ML engineering | PostTrainBench | 45.3% | 44.3% | 40.2% | **49.3%** |
| Science and math | Terminal-Bench Science 0.1 | 57.6% | **68.1%** | 52.6% | 63.3% |
| Science and math | RiemannBench | **76.0%** | 72.0% | 65.6% | 69.6% |
| Long context | GraphWalks (Up to 128k, BFS (F1)) | **99.7%** | 98.7% | 91.4% | 90.6% |
| Long context | GraphWalks (256k to 1M, BFS (F1)) | **84.2%** | 71.8% | 65.0% | 66.8% |
| Computer use | Agent’s Last Exam (Pass rate) | **39.5%** | 34.2% | — | 38.2% |
| Computer use | OSWorld-2.0 (Offline subset, Partial reward) | 69.2% | **72.6%** | — | — |
| Multimodal understanding | Chartography | **71.6%** | 71.0% | 46.2% | 66.3% |
| Multimodal understanding | LVBench | **91.7%** | 87.5% | 79.7% | 83.7% |
| Cybersecurity | CWE-bench v1 | **68.0%** | **68.0%** | 58.0% | 67.0% |

Google says it will gather feedback from early testers and iterate on Argon’s guardrails before making the model available outside the Fairwind Program. Once that day comes, paid API customers and AI Ultra subscribers will get to try the new model first, before it’s released to developers, enterprises, and consumers.

Unlike its boring, odorless, and inert namesake, Gemini 4 Argon will likely create a bit of a stir. Google first announced plans for a new Pro model, [Gemini 3.5 Pro](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/), at its I/O developer conference in May — Argon is essentially its replacement. The original plan was to launch the new model in June, but instead, we got a series of Flash models.

## Coding: so-so. Knowledge work: A+

In Google’s benchmarks, which include a wide variety of tasks, Argon takes top billing, outright or tied, in 13 of 18 tests against Anthropic’s Opus 5.5 and Fable 5.1, as well as OpenAI’s GPT-6 Astra.

Yet while Google specifically mentions Argon’s coding abilities, the results are mixed.

Google highlights Argon’s 77.9% on DeepSWE v1.1 as a new state of the art, but Argon also comes last among the competition on both FrontierSWE v2 and Terminal-Bench 4.0, where GPT-6 Astra and Opus 5.5 lead it by 10.5 and nine points, respectively. Its other coding win is on Vibe Code Bench, with 91.9%, but all four models score above 89% here.

But where Argon excels is knowledge work.

Argon scores 51.3% on Zapier’s AutomationBench, almost nine points ahead of Opus 5.5, and 84.2% on the GraphWalks test for inputs between 256K and 1M tokens, more than 12 points ahead of GPT-6 Astra.

> Its 19.6% on Harvey’s Legal Agent Benchmark is nearly triple Fable 5.1’s score, though that means it still fully completes only about one in five tasks.

In other areas, Argon’s wins are narrower. While it leads on the Vals Index, Vibe Code Bench, Agent’s Last Exam, Chartography, and the shorter GraphWalks test, those leads are generally under two points.

On CWE-bench v1, the one cyber benchmark in the post with rival scores, Argon ties GPT-6 Astra and xAI’s Grok 4.7 at 68%, with Opus 5.5 a point behind, but it’s worth noting that the OpenAI and Anthropic models run in their own [agent harnesses](https://blog.collinear.ai/p/cwe-bench-v1) (Codex and Claude Code), so that leaderboard measures each model and its tooling together.

As always, benchmarks never tell the full story, but it looks like Google focused on making this model especially useful for standard office tasks.

Developers will surely want to test the model, too, given the impressive DeepSWE score.

## 1 million output tokens

One interesting new feature in an area where most of the competition isn’t currently pushing the frontier forward is in the model’s output token limits. One million input tokens is now the standard for frontier models, but Gemini 4 Argon can also generate up to one million output tokens, up from 64,000 for previous Gemini models.

“When the model has the headroom to think deeply and generate hundreds of thousands of tokens in a single trajectory, it adds a new level of depth in reasoning to solve tough problems in one go,” Google writes in the announcement.

As for cyber security, Google says it trained Argon to autonomously find, validate, and patch software vulnerabilities, and for Fairwind participants and its own internal teams, it’s releasing the model without cyber guardrails.

Wiz, which Google [acquired for $32 billion](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/wiz-acquisition/) in March, is already using Argon in its Scan for Good initiative, and Google says the model found a critical vulnerability in healthcare software used by hospitals worldwide that earlier frontier models had missed.

Argon scores 85.8% on Google’s internal vulnerability discovery benchmark and 70.9% on Wiz’s penetration testing benchmark, though Google only compares those results with its own Gemini 3.8 Flash Cyber (71.0% and 58.2%, respectively).

## Pricing?

Google [says](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) Argon will cost $2 per million input tokens and $10 per million output tokens during an introductory period, rising to $4 and $20 afterward. That later output rate matches the [$20 per million output tokens](https://www.anthropic.com/claude/opus) Anthropic charges for Opus 5.5, and with Argon

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)