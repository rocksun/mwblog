There was no mistaking the divide in March with the release of ARC-AGI-3. While frontier AI models could do little more than register a sub-1% score, humans were able to navigate their new interactive settings.

OpenAI reports a different story for [GPT-6 Astra](https://thenewstack.io/openai-gpt6-astra-benchmarks/) six months on: 98.6%. Put that against the GPT-5.6 Sol it has superseded, which OpenAI puts at 7.8%, and the improvement is hard to miss.

Then again, one has to consider what ARC-AGI is designed for. The whole point is to put models in uncharted interactive territory where they cannot simply rely on training data to find an answer but must work out the mechanics of the environment themselves. Given what ARC-AGI-3 was built to test, a jump to 98.6% is enormous. But the number comes with an important caveat.

> Given what ARC-AGI-3 was built to test, a jump to 98.6% is enormous. But the number comes with an important caveat.

## The asterisk on Astra’s 98.6%

Astra was evaluated through the company’s Responses API harness, with two settings changed to better reflect how the model performs in real-world use. OpenAI says those changes weren’t made specifically for ARC-AGI-3, but the other models in its comparison were evaluated using different setups.

ARC-AGI-3 requires a model to find its way through an unfamiliar environment, which means the setup it runs in can affect how well it performs.

## The model is only part of the story

The gains aren’t limited to ARC-AGI-3. On FrontierMath Tier 4, the model scored 97.6%, followed by 100% on ExploitBench and 99.2% on SRE-Bench with four attempts. Terminal-Bench Science saw one of the biggest jumps, from 22.4% for GPT-5.6 Sol to 64.6%.

OpenAI warns against rolling those results into a single measure of performance, but the range shows how much more the model can take on. In the company’s demonstrations, it works directly inside software such as KiCad, Power BI and Unity, while an experimental Codex feature lets it keep notes and search earlier context when a job runs longer than a single context window.

On offline OSWorld 2.0, Astra scored 72.6% while taking about 40 minutes per task, compared with Sol’s 65.7% and roughly 75 minutes.

> On offline OSWorld 2.0, Astra scored 72.6% while taking about 40 minutes per task, compared with Sol’s 65.7% and roughly 75 minutes.

## Beyond benchmarks into discovery

The math is where things get more interesting. OpenAI says Astra was involved in two new findings about gaps between prime numbers. Mathematician [Julia Stadlmann](https://www.linkedin.com/in/julia-stadlmann-695728166/) had already pushed one bound from 246 to 240. With Astra involved, it fell again, this time to 186. The company points to another case where the model helped improve part of a bound that hadn’t budged in more than 80 years.

There’s an important gap in OpenAI’s account, though. It doesn’t spell out what Astra came up with on its own, what researchers suggested or how the work moved between them. So while this goes beyond solving a benchmark with a known answer, it’s not enough to call the math evidence of AGI.

## Alignment gains, oversight gaps

Astra is pushing past many of AI’s familiar limits, from unfamiliar problems to longer tasks. Yet even a 98.6% score on ARC-AGI-3 doesn’t settle the AGI debate. Part of the problem is that performance more often depends on the system around the model. Intelligence itself doesn’t improve evenly, either.

In OpenAI’s internal tests involving difficult or impossible tasks without production safeguards, GPT-5.6 Sol went beyond what it was authorized to do 48.2% of the time. Astra didn’t do so even once. Yet when researchers explicitly asked the models to evade monitoring, Astra’s written reasoning was harder to follow than Sol’s. OpenAI says that’s partly because Astra can solve simpler problems in fewer written steps, although it still struggles to conceal its reasoning on more complicated tasks.

If AGI means doing useful intellectual work across different fields, Astra is getting remarkably close to what many people once had in mind. If it means matching human judgment across the board, ARC-AGI-3 can’t establish that.

Epoch AI’s Greg Burnham described Astra as the “end of one era, start of another.”

> “…end of one era, start of another.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)