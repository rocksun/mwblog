**Anthropic on Wednesday launched Claude Haiku 5.5**, the first new version of its smallest and most affordable model in nearly a year.

That’s Anthropic’s third 5.5 model in a month, though what’s still missing is Fable 5.5. That model, however, will likely go through a much longer review process, so it’s no surprise its launch is taking a bit longer.

## How Haiku 5.5 pricing works

Like with previous iterations, the company describes [Haiku 5.5](https://www.anthropic.com/claude/haiku) as its “fastest and most efficient model,” but this time, it is also much cheaper. While Haiku 4.5 cost $1/$5 per million input/output tokens, Anthropic is bringing the price down to $0.10/$0.50 for requests under 100,000 tokens.

> Anthropic describes Haiku 5.5 as its “fastest and most efficient model,” but this time, it is also much cheaper.

For larger requests, the new price is $0.50/$2.50 (Haiku 4.5 costs the same, no matter the number of tokens in a request), but Anthropic notes that about 90% of requests to Haiku 4.5 fell into the lower-priced category (which is likely a function of the kind of work that developers have sent to Haiku in the past).

Those are 90% and 50% cuts to the per-token prices, respectively. Anthropic puts the average savings at around 75%. That accounts for a mix of requests and an updated tokenizer that uses slightly more tokens per task.

This new version is the first Haiku model with effort controls (the default is medium), giving developers control over how many tokens the model uses on a given task.

|  | | Haiku 5.5 | Haiku 4.5 | GPT-6 Luna | Sonnet 5.5 |
| --- | --- | --- | --- | --- | --- |
| Knowledge work *GDPval-AA v2.1* | | 1620 | 735 | 1437 | 1840 |
| Knowledge work *AA-Briefcase v1.1* | | 1578 | 614 | 1336 | 1824 |
| Computer use *OSWorld 2.1 (Offline subset)* | | 72.4% | 15.7% | 48.9% | 83.9% |
| Multidisciplinary reasoning *Humanity’s Last Exam* | No tools | 45.9% | 10.2% | – | 56.9% |
| With tools | 57.4% | 18.7% | – | 64.5% |
| Agentic coding *Terminal-Bench 4.0* | | 39.2% | 0.0% | 16.4% | 70.6% |
| Agentic coding *FrontierCode 1.1 (Main)* | | 46.4% | – | 42.4% | 52.1% (Xhigh) |
| Visual reasoning *Chartography (no tools)* | | 46.4% | 6.4% | 29.1% | 61.6% |

## Small models, new jobs

The use case for these small models has always been to handle high-volume tasks like summarization, classification, and routing.

That, of course, is also where [decision models like Jev](https://thenewstack.io/typesafe-jev-system-one/) are currently making a splash — and at an even lower price.

Going forward, that may not be where these small models like Haiku or OpenAI’s GPT-6 Luna will be most useful, so it’s probably no surprise that Anthropic also notes that the model can handle tasks like compaction and database queries, as well as agentic workloads where speed matters, including live customer support and browser use.

## Haiku 5.5 benchmarks

Anthropic’s own evaluations show a clear improvement over Haiku 4.5. On the offline subset of OSWorld 2.1, which tests computer use, Haiku 5.5 scored 72.4%, up from 15.7% for its predecessor and ahead of GPT-6 Luna’s 48.9%.

On the GDPval-AA v2.1 knowledge-work benchmark, Haiku 5.5 scored 1,620, compared with 735 for Haiku 4.5 and 1,437 for GPT-6 Luna. Unsurprisingly, Sonnet 5.5 remains ahead on both benchmarks.

On Terminal-Bench 4.0, which tests complex, multi-step tasks in a command-line environment, Haiku 5.5 scored 39.2%, compared with 0% for Haiku 4.5, 16.4% for GPT-6 Luna and 70.6% for Sonnet 5.5.

## How Chinese rivals compare

Anthropic is only directly comparing Haiku 5.5 to its own models and OpenAI’s GPT-6 Luna. But when it comes to small models, many developers are also looking at competitors form Z.ai, Alibaba, and others.

Artificial Analysis currently gives Z.ai’s GLM-5.3-Flash a score of 1,647 on [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) and 1,454 on [AA-Briefcase v1.1](https://artificialanalysis.ai/evaluations/aa-briefcase). Anthropic, in comparison, reports 1,620 and 1,578 for Haiku 5.5, respectively.

There are still cheaper options, too. On Alibaba’s international service, Qwen3.7 Flash costs $0.03 per million input tokens and $0.13 per million output tokens for inputs of up to 32,000 tokens. For inputs above 32,000 and up to 256,000 tokens, those rates rise to $0.10 and $0.40, respectively.

Haiku 5.5 is available on the Claude Platform, Amazon Web Services, Google Cloud and Microsoft Azure. Developers using Anthropic’s platform can access it as claude-haiku-5-5. The company is also adding beta support for computer use and browser use to its Python and TypeScript SDKs.

## Also new: Sonnet 5.5 cache price drop, API credits for Max and Team subscriptions

Alongside the launch, Anthropic is cutting Sonnet 5.5’s cache-read price in half, from $0.20 to $0.10 per million tokens. The company says this should make most agentic tasks about 20% cheaper. The cut is rolling out across platforms on Wednesday, though some existing Azure and Google Cloud customers will have to wait a few days.

> Anthropic is cutting Sonnet 5.5’s cache-read price in half

Anthropic is also adding monthly API credits to its Max and Team subscriptions this week. Max 5x subscribers will get $100 per month and Max 20x subscribers will get $200. Team subscribers will receive up to $500, pooled across their users. You can use the credits with any model on the Claude Platform.

Haiku 5.5 also comes with tighter cybersecurity safeguards than Haiku 4.5, although Anthropic says these allow a wider range of defensive work than Sonnet 5.5’s safeguards. They still block penetration testing. Organizations that need broader access for cybersecurity or biology work can apply to Anthropic’s verification programs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)