GPT-6 Astra has an obvious problem for developers considering an upgrade from GPT-5.6 Sol: its tokens cost 2.5 times as much, yet OpenAI thinks many developers should upgrade anyway — and then turn the reasoning setting down.

OpenAI’s [Thibault Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/), engineering lead for Codex, [posted on X over the weekend](https://x.com/thsottiaux) saying, “To calibrate you all on which reasoning effort to use for Astra, know that GPT-6 Astra on low performs better than GPT-5.6 Sol on high.”  
  
[Artificial Analysis](https://artificialanalysis.ai/models/gpt-6-astra-low) currently scores Astra-low at 49 on its Intelligence Index, narrowly ahead of [Sol-high at 48](https://artificialanalysis.ai/models/gpt-5-6-sol-high). Astra-low also responded much sooner, with the first token arriving in 2.53 seconds, compared to 11.87 seconds for Sol-high.

> “To calibrate you all on which reasoning effort to use for Astra, know that GPT-6 Astra on low performs better than GPT-5.6 Sol on high.”

## Reasoning effort changes cost

Astra costs [$10 per million input tokens and $50 per million output tokens](https://openai.com/index/gpt-6-astra/), compared with $4 and $20 for Sol at current rates. Moving the reasoning dial from high to low doesn’t change those rates, but it can change how much work gets done before the task is finally complete and it’s an argument [OpenAI makes explicitly](https://developers.openai.com/api/docs/guides/latest-model) in its migration guidance. The company says Astra can produce stronger results while using substantially fewer output tokens.

OpenAI uses its own benchmark as proof. The company saw the same pattern in [Terminal-Bench 4.0](https://openai.com/index/gpt-6-astra/), where Astra scored 57.9% to Sol’s 37.3% but still cost about 9% less per task. The gap was even wider on GPQA Diamond: Astra edged out Sol, 94.9% to 94.6%, at an estimated cost 37% lower.

Real-world workloads will vary, but the results suggest that per-token pricing alone does not tell developers what a model will actually cost to run — an idea OpenAI is [already exploring with outcome-based pricing](https://thenewstack.io/openai-outcome-based-pricing/).

## Fewer tokens, cheaper tasks

Developer [Shinpr](https://dev.to/shinpr/switching-from-gpt-56-sol-to-gpt-6-astra-start-with-medium-effort-25ao) ran the comparison on the same codebase, using Sol-high and several Astra reasoning levels, with analysis, implementation, and review.

Astra-medium did better on both time and cost by handling the implementation in 80 requests, less than a third of the 238 Sol-high needed, and processed 11.1 million input tokens instead of 37.8 million. By the end of all three phases, the Astra-medium run had taken about 51 minutes and cost an estimated $25.67; the Sol-high run had taken roughly 75 minutes and cost $31.79.

Turning Astra up to high didn’t help because that run stretched to 77 minutes and $37.23, and Shinpr said its review missed a startup bug that medium caught.

One developer’s test can’t tell us that medium will be the right choice for every workload, but it does indicate that more reasoning wasn’t worth paying for here. Also, that pattern doesn’t hold everywhere. ARC Prize’s testing went in almost the opposite direction.

> Turning Astra up to high didn’t help because that run stretched to 77 minutes and $37.23, and Shinpr said its review missed a startup bug that medium caught.

## More reasoning, lower bills

[ARC Prize’s evaluation of Astra](https://arcprize.org/blog/astra) shows the other side of the equation. More reasoning not only improved Astra’s score on ARC-AGI-3; in some cases, it also reduced costs.

With ARC Prize’s standard harness, Astra scored 17.5% at low reasoning, 38.6% at medium, 54.8% at high, and 62.7% at max. [Astra also has an xhigh setting between high and max](https://thenewstack.io/astra-arc-agi-benchmark/). But the most expensive runs weren’t the ones using the most reasoning. ARC Prize spent $38,166 at low, $48,090 at medium, and $40,705 at high. Max came in at just $26,098.

At max, Astra used more compute on each decision but needed fewer actions to solve the environments. That tradeoff was enough to bring the overall cost down, which can happen with agents. While lower reasoning may look cheaper, a wrong turn quickly means another tool call or another attempt after another, which costs more in reasoning upfront than just fixing the mistakes later.

> While lower reasoning may look cheaper, a wrong turn quickly means another tool call or another attempt after another, which costs more in reasoning upfront than just fixing the mistakes later.

## Dynamic reasoning without cache loss

Those are two extremes that developers don’t need to choose between for their entire workflow, thanks to Astra introducing a [configuration\_update](https://developers.openai.com/api/docs/guides/latest-model) mechanism that lets an application change the reasoning effort between responses without changing the original request-level configuration.

Routine work can remain at a low reasoning level, while a failed test, an unexpected tool response, or a difficult debugging problem can trigger a higher reasoning level for the next turn. Once that’s resolved, the agent can drop back down.

That also helps explain why Shinpr and ARC Prize got such different results. Shinpr found that extra reasoning added time and cost without improving the outcome, while ARC Prize found that more reasoning sometimes cut the number of actions enough to lower the total bill.

For now, `configuration_update` only works with Astra in standard, single-agent requests. But, don’t get hung up on Astra’s 2.5x token price. An expensive model is often the cheaper run if it takes fewer calls to finish the job and fewer attempts to get it right.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)