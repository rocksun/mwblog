On Tuesday, [OpenAI released GPT-6 Sol and Luna](https://thenewstack.io/openai-gpt-6-sol-luna-release/), an expansion of the GPT-6 line-up that aims to make GPT-6 Astra’s next-level intelligence more efficient, accessible, and affordable.

Though OpenAI says Astra is still “the most intelligent and aligned model in the world,” the new GPT-6 models come impressively close in alignment — at a fraction of the price.

In an internal coding evaluation on coding deception, for example, GPT-6 Astra’s deception rate is 0.5%, while GPT-5.6 Sol stands at 10.4%. The new GPT-6 Sol is only 1.3%.

As for pricing, GPT-6 Astra [costs](https://openai.com/index/gpt-6-astra/) $10 per million input tokens and $50 per million output tokens; GPT-6 Sol and GPT-6 Luna cost $2 and $0.10 per million input tokens and $10 and $0.50 per million output tokens, respectively.

If OpenAI’s new GPT-6 models can achieve near-Astra-level alignment at a fraction of the cost, that’s good news. But it’s still unclear whether or not the new GPT-6 models also mirror Astra’s [observability and monitoring](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "observability and monitoring") problems.

## Closing the alignment gap between Astra and GPT-5.6

OpenAI says it trained the new GPT-6 models with similar methods as it did for GPT-6 Astra, specifically building on the alignment work it began with Astra.

While Astra is still the AI company’s “most aligned model to date,” it looks like GPT-6 Sol and Luna are giving it a run for its money, dramatically closing the gap between OpenAI’s most advanced model and its GPT-5.6 counterparts in key areas like coding deception, failure to disclose a broken search tool, and unauthorized agent interaction. OpenAI notes that these evaluations deliberately test challenging situations and do not measure failure rates in typical use.

![](https://cdn.thenewstack.io/media/2026/09/9b78897a-screenshot-2026-09-22-at-15.12.20.png)





*Credit: OpenAI*

The most progress was made on failure to disclose a broken search tool, where AI agents are given search tasks and a broken search tool; do they just give their best guess or say that the search tool is broken?

The gap between GPT-5.6 Sol’s ability and Astra’s is notably wide: 77.5% and 1.5%, respectively. Per OpenAI’s internal evaluation, GPT-6 Sol is a dramatic improvement, with a non-disclosure rate of 4.9%. Luna also improved, but less impressively, dropping from 78.3% to 28.7%.

> Though OpenAI says Astra is still “the most intelligent and aligned model in the world,” the new GPT-6 models come impressively close in alignment — at a fraction of the price.
>
> ![](https://cdn.thenewstack.io/media/2026/09/b30417b4-screenshot-2026-09-22-at-15.23.53.png)
>
>
>
>
>
> *Credit: OpenAI*

Coding deception, where AI agents are deliberately given tasks that elicit dishonesty, improved as well. In OpenAI’s internal evaluation, deception rate measures the fraction of answers with detected deception. GPT-6 Sol (1.3%) now almost matches GPT-6 Astra’s performance (0.5%), a far cry from GPT-5.6 Sol’s (10.4%).

![](https://cdn.thenewstack.io/media/2026/09/a89c1e32-screenshot-2026-09-22-at-15.25.33.png)





*Credit: OpenAI*

Significant progress was also made on unauthorized agent interactions, where OpenAI evaluates whether models follow unauthorized instructions on a simulated message board. GPT-5.6 Sol went ahead with the unauthorized action in 52% of runs in which it found the board, while GPT-6 Sol did so in only 11% of cases.

GPT-6 Astra and Luna didn’t take any such actions, but OpenAI says Luna “found the board less often.”

## Where the results are less impressive

Though GPT-6 Sol gets close to Astra in several alignment evaluations, there’s still a way to go with warning circumvention.

> GPT-6 Sol attempted to work around restrictions in 64.4% of runs. That’s only a slight improvement from GPT-5.6 Sol’s 68.2% and still quite far off from Astra’s 17.4%.

![](https://cdn.thenewstack.io/media/2026/09/9cce56b0-screenshot-2026-09-22-at-15.26.07.png)





*Credit: OpenAI*

In an internal evaluation where OpenAI tested models’ abilities to respect explicit warnings, like “access denied” messages, GPT-6 Sol attempted to work around restrictions in 64.4% of runs. That’s only a slight improvement from GPT-5.6 Sol’s 68.2% and still quite far off from Astra’s 17.4%.

![](https://cdn.thenewstack.io/media/2026/09/3a907d76-screenshot-2026-09-22-at-15.26.43.png)





*Credit: OpenAI*

Finally, for reviewer bypass attempts, where OpenAI tests whether models try to bypass or respect an automated safety reviewer’s decision to block an unsafe command in Codex, the new GPT-6 models are almost identical to Astra, though the playing field was already pretty even to begin with: GPT-5.6 Sol attempted a bypass in 7.3% of runs and GPT-5.6 Luna in 4.3%, compared with none for Astra and GPT-6 Sol and 0.3% for GPT-6 Luna.

## But if GPT-6 Sol is anything like Astra, we’re not out of the woods yet

GPT-6 Sol and Luna have made marked improvements across alignment evaluations, inching closer to OpenAI’s star child, Astra. But if the new GPT-6 models also follow suit on Astra’s noted observability issues, then developers hoping to catch misalignment via monitoring aren’t out of the woods yet.

Though Astra is substantially more aligned than its predecessor, [its written reasoning is also harder to monitor than GPT-5.6 Sol’s](https://thenewstack.io/openai-gpt6-astra-benchmarks). That’s not great for teams trying to count on monitoring to find misalignment mistakes; [Jakub Pachocki](https://www.linkedin.com/in/jakub-pachocki/), Chief Scientist at OpenAI, writes in his essay, “[An Alien Mind](https://openai.com/index/an-alien-mind/),” that [OpenAI’s methods for keeping models aligned and monitored aren’t keeping pace with model capabilities](https://thenewstack.io/openai-voluntary-slowdown-safety/).

OpenAI knows that Astra’s — and now GPT-6 Sol’s — improved alignment doesn’t mean the AI industry has gotten a handle on the problem yet.

> “We do not believe that the AI industry has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer.”

Just this month, the AI company shared [six reports of “unexpected or concerning model behavior](https://thenewstack.io/openai-model-misalignment-reports/),” including self-generated instructions, information fabrication, unauthorized use of leaked API keys, cross-agent communication, and unsanctioned file-sharing.

At the same time, it released a new [framework for reporting model misalignment](https://openai.com/index/model-misalignment-reporting-framework/), stating: “We do not believe that the AI industry has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer.”

If GPT-6 Sol and Luna are catching up to Astra in alignment evaluations — at a far cheaper rate — that’s good news. But if the new GPT-6 models also come with the same observability and monitoring problems, then cheaper may still come at a cost.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)