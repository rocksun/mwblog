As [expected](https://thenewstack.io/gpt-5-6-developer-reactions/), OpenAI on Thursday made its family of GPT-5.6 models available to its app and API users globally.

This marks the first time OpenAI is launching three distinct versions of its new model at the same time:

* **Sol** is the flagship model meant to rival Anthropic’s Fable 5
* **Terra** is the mainstream model
* **Luna** is the faster, more affordable, but less capable option

## GPT 5.6 availability and pricing

With this release, OpenAI is gating the models’ capabilities by reasoning efforts, with Pro and Enterprise users getting access to GPT-5.6 Sol Pro “for the highest-quality results on complex tasks,” as OpenAI puts it.

In Codex and the new ChatGPT Work (OpenAI’s new Claude Cowork competitor), Free and Go users get access to the Terra model, while Plus, Pro, Business, and Enterprise users can choose between Sol, Terra, and Luna and set an effort level for each.

Worth noting: In Codex, the Ultra mode is available to Plus and higher plans.

All of the new models will be available in the API, too, of course. Sol will cost $5 per million input tokens and $30 per million output tokens. For Terra, the price is $2.50/$15, and for Luna, $1/$6.

## GPT 5.6 benchmarks

Sol, the new flagship model, is often on par with or beats Anthropic’s class-leading Fable 5 model, but the main argument OpenAI is making for its models this time around focuses more on cost.

“We trained GPT‑5.6 to get more useful work from every token,” the company notes in its announcement. In the benchmarks, that’s maybe reflected most clearly in the Artificial Analysis Intelligence Index, where GPT-5.6 Sol comes within one percentage point of Fable 5, but at half the cost and in just over half the time.

### Professional

| Eval | GPT-5.6 Sol | GPT-5.6 Terra | GPT-5.6 Luna | GPT-5.5 | Claude Fable 5 | Claude Opus 4.8 |
| --- | --- | --- | --- | --- | --- | --- |
| Agents’ Last Exam | 52.7% | 50.4% | 50.3% | 46.9% | 40.5% | 45.2% |
| GDPval-AA v2 | 1,747.8 Elo | 1,593 Elo | 1,591.8 Elo | 1,493.7 Elo | 1,759.6 Elo | 1,600.1 Elo |
| Management Consulting Tasks (Internal) | 43.2% | 37.2% | 35.4% | 31.3% | 35.5% | 31.6% |
| Big Finance Bench | 53% | 51% | 36% | 49% | — | 44% |
| Artificial Analysis Intelligence Index v4.1 | 58.9 Index score | 55 Index score | 51.2 Index score | 54.8 Index score | 59.9 Index score | 55.7 Index score |

### **Coding**

| Eval | GPT-5.6 Sol | GPT-5.6 Sol Ultra | GPT-5.6 Terra | GPT-5.6 Luna | GPT-5.5 | Claude Mythos 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Artificial Analysis Coding Agent Index v1.1 | 80 Index score | — | 77.4 Index score | 74.6 Index score | 76.4 Index score | — |
| SWE-Bench Pro | 64.6% | — | 63.4% | 62.7% | 59.4% | 80.3% |
| DeepSWE v1.1 | 72.7% | — | 69.6% | 67.2% | 67% | — |
| Terminal-Bench 2.1 | 88.8% | 91.9% | 87.4% | 84.7% | 85.6% | 88% |

## GPT 5.6 coding

For agentic workflow, based on the Agents’ Last Exam benchmark, which tests long-horizon agentic tasks, GPT-5.6 Sol beats Fable 5 by 13.1 points.

![](https://cdn.thenewstack.io/media/2026/07/4e58842c-screenshot-2026-07-09-at-10.20.25-am-1024x901.png)

*Credit: OpenAI*

On coding benchmarks, the results are similar, with GPT-5.6 Sol often beating Anthropic’s Fable 5, inching out higher scores at significantly lower cost. That holds true for Terminal-Bench 2.1 and DeepSWE 1.1.

One reason the models do so well here, OpenAI argues, is that they have new built-in capabilities that allow them to perform certain tasks internally.

“GPT‑5.6 can write and run lightweight programs that coordinate tools, process intermediate results, monitor progress, and choose the next action as work unfolds. This lets tool-heavy tasks advance with fewer tokens, fewer model round-trips, and less guidance,” OpenAI writes.

There is also now a new “ultra” mode — comparable to Anthropic’s “ultracode” that dispatches a team of four agents in parallel for when you need even better (and faster) results and are willing to burn more tokens in the process.

![](https://cdn.thenewstack.io/media/2026/07/34e70b4b-screenshot-2026-07-09-at-10.29.57-am-1024x901.png)

*Credit: OpenAI*

“GPT‑5.6 Sol sets a new standard for both intelligence and efficiency, achieving state-of-the-art results across coding, knowledge work, cybersecurity, and science while outperforming previous and competing frontier models with fewer tokens and at lower estimated cost,” writes OpenAI. “The result is stronger performance per dollar: more successful work for the same spend, or comparable results at a lower total cost.

## Knowledge work

For knowledge work, too, GPT-5.6 Sol is typically leading its class, scoring 92.3% on the BrowseComp agentic browsing benchmark and 62.6% on OSWorld 2.0, which assesses long-horizon computer-use tasks.

But what will likely matter more to users than raw benchmark numbers is that the model has improved at creating presentations and documents.

“The improvement is especially pronounced when following templates and reference decks,” OpenAI writes. “GPT‑5.6 can infer a deck’s design system — layouts, typography, spacing, colors, and recurring content patterns, including rules embedded in the Slide Master — and apply those conventions consistently to new material. “

And, as a bonus, GPT-5.6 won’t [talk about goblins](https://openai.com/index/where-the-goblins-came-from/) all that much, the company said in a livestream that accompanied the release.

## Security

Given what happened to Fable 5 and that OpenAI itself held back the new models to await government approval, the company devotes quite a bit of its release materials to its safety stack. OpenAI may be closer to the Trump administration than Anthropic — or at least have a better relationship — but the company surely doesn’t want to see its models pulled either.

> “In cybersecurity, our testing suggests GPT‑5.6 is better at finding and fixing vulnerabilities than at reliably carrying out autonomous, end-to-end attacks against hardened targets” —OpenAI

“The GPT‑5.6 models are more capable than our earlier models in both biology and cybersecurity, but do not cross the Critical threshold in either category,” OpenAI notes. “In cybersecurity, our testing suggests GPT‑5.6 is better at finding and fixing vulnerabilities than at reliably carrying out autonomous, end-to-end attacks against hardened targets — giving defenders an opportunity to strengthen systems before weaknesses are exploited. In biology, our testing suggests GPT‑5.6 can support legitimate research but does not provide the end-to-end capability needed to create, engineer, or synthesize a highly dangerous novel threat.”

What OpenAI doesn’t talk about as much as Anthropic does is how the models will handle refusals. While Anthropic’s Fable 5 downgrades some sensitive requests to the Opus model, OpenAI mostly talks about blocking attacks.

“Compared with previous models, our GPT‑5.6 Sol cyber safeguards block roughly ten times more potentially harmful activity,” the company explains and, like Anthropic, notes that “there is no such thing as perfect security, and our work to secure increasingly capable models continues. New weaknesses will be discovered, as will new jailbreaks that circumvent existing safeguards.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)