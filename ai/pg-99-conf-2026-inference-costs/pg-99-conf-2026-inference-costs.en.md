**Last October, the P99 conference** — the online gathering for developers focused on high-performance, low-latency applications — featured a cracking keynote from Chip Huyen.

The author of the best-selling [*AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166298/), [Huyen](https://huyenchip.com/) opened with simple math: Training a frontier model is a one-off cost, but inference is the same cost paid over and over. That’s great for the frontier model providers, and bad for us token burners. Over the life of a model, Huyen reckons the compute split ratio lands somewhere between 1:10 and 1:100 for training to inference. Reasoning models — which burn even more tokens — push that out even further. We all know the feeling of hitting our weekly session quotas.

Huyen’s point is that if inference is too expensive, then nobody ever recovers the training bill, which might explain why there are so many memes about the “profitability” of frontier models. So, how do we optimize inference?

That’s a topic that Huyen spent months researching for her book. And in the spirit of optimization, Huyen distilled it down to 30 minutes for the conference in October 2025.

Huyen is [returning for P99 CONF 2026](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000qrLWi&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202026-10-21%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack) in a few weeks. Ahead of that moment, watch her full talk – or read the recap below – from last year, then let’s talk about how those ideas aged over the past 11 months.

## What to measure

Chip recommends focusing on a few key latency metrics:

* Time to first token (TTFT): How much time elapses before the user sees anything
* Time per output token (TPOT): The average time between consecutive tokens (aka *inter-token latency*)
* End-to-end latency: Time to first token, plus time per output token, multiplied by the number of output tokens minus one

![](https://cdn.thenewstack.io/media/2026/09/c34e67c5-image-1024x493.png)





(*Click to enlarge graphic.)*

With reasoning models, some of those tokens never reach the user. “The first generated token might not be the same as the first visible token,” Huyen explained. “The model might think for a while, and it will only show the first token of the final output to the user.”

> “The first generated token might not be the same as the first visible token,”  
> — Chip Huyen

Some people also measure Time to Publish for that (i.e., how long until the user sees the first token). The best metric to prioritize depends on what matters most for your users.

Also consider “goodput” alongside throughput. Throughput measures requests processed in a given window. Goodput measures the requests that actually met your targets. Chip’s example: an app targets 200 ms time to first token and 100 ms time per output token, and processes 10 requests per minute, but only three hit both.

![](https://cdn.thenewstack.io/media/2026/09/c34e67c5-image-5-1024x496.png)





(*Click to enlarge graphic.)*

## 3 ways to optimize LLM inference

With inference servers, you can optimize from 3 different angles: the hardware, the model, and the service that manages the requests and responses.

![](https://cdn.thenewstack.io/media/2026/09/c34e67c5-image-3.png)





(*Click to enlarge graphic.)*

Huyen previously worked at Nvidia and opted out of the hardware discussion: “Even though I find it to be an intellectually interesting topic, it’s not relevant to a lot of people because we don’t have the power to change the hardware itself,” Huyen explained. She also didn’t want to spend much time on the obvious solution: replica parallelism, or just adding more machines. It’s costly, and it gets complicated fast – especially if you end up with a mix of 80GB, 48GB and 24GB machines and models of varying sizes to distribute across them.

That leaves the model and the service. Huyen offers these tips on how to decide: “If you want to host the models yourself, or if you have access to the model weights, or if you train a model yourself, or you want to fine-tune or distill a model, then model optimizations might be for you. However, if you want to take a model as-is and make it more efficient on your own inference service, you might want to look into service optimizations.

### Model optimization

The following techniques change the actual weights so that they can change the model outputs.

**Quantization** lowers the precision used to store weights and activations  (e.g., from four bytes per parameter at 32-bit to one byte at 8-bit). Huyen explained, “Reducing the precision not only reduces the memory requirement to run the model, making it cheaper. It can also make the model a lot faster. If you do additions bit by bit and each weight is 32 bits, you have to do it 32 times. If it’s 8 bits, you only have to do it eight times.”

The tradeoff is a small quality hit. Huyen continued: “It’s possible to reduce a lot of the model’s memory footprint with minimal quality degradation, and quantization is pretty generalizable to a wide variety of model architectures and model sizes. That’s why it’s very popular. I rarely see any companies running a model at full precision anymore.”

> “I rarely see any companies running a model at full precision anymore.”  
> — Chip Huyen

**Distillation** involves using a large model to generate training data for a smaller model. For example, say you have a truly large model (the example Huyen used was o1) and want a model that performs like it, but is much smaller. Basically, you collect a large set of prompts, run them through the larger model, then train the smaller model on its responses.

Proceed with caution, though. Huyen warned, “A lot of model providers have the condition that they do not allow their models to be used to train competitive models. So even though it’s a very common technique, you need to check licensing.”

### Service optimization

This set of techniques targets how requests are scheduled, routed, and reused. The actual weights aren’t affected.

**Batching** groups multiple requests so they’re processed together in a single pass through the model – which is much more efficient than dealing with them one at a time. Huyen presented a few batching options:

* **Static batching** waits for the batch to fill. This maximizes compute utilization, but it might increase the latency for the first requests.
* **Dynamic batching** runs on a timer instead (e.g., batching every 15 ms). This is less compute-efficient, but it’s better for latency.
* **Continuous batching** handles the case where requests finish at wildly different times, which is common with LLMs. One request asks for the capital of Vietnam; another kicks off deep research. With static or dynamic batching, the finished request’s slot sits idle until the slowest one completes – and new requests queue up behind it. Continuous batching returns each request as it finishes and fills the spot with another request. That can improve compute resource utilization and latency.

![](https://cdn.thenewstack.io/media/2026/09/c34e67c5-image-1.png)





(*Click to enlarge graphic.)*

**Decoupling prefill and decode** separates the two phases of a request onto different machines. (Prefill processes the input, while decode generates the output.) Huyen said, “Input tokens can be processed in parallel, whereas output tokens need to be generated sequentially. With parallel processing, it’s bounded by compute, the processing power of the chip. With decoding, it’s bounded by memory, because you have to move model weights.”

Because each phase stresses different resources, most services now separate them. To improve *time to first token*, shift machines toward prefill. If you care more about improving *time per output token*, shift them to decode.

![](https://cdn.thenewstack.io/media/2026/09/c34e67c5-image-4.png)





(*Click to enlarge graphic.)*

**Parallelism** splits work across machines. Replica parallelism copies the whole model onto more machines. Tensor parallelism divides a very large matrix, so different machines compute different parts of it. Pipeline parallelism divides the model by layer, so requests move through as a pipeline.

![](https://cdn.thenewstack.io/media/2026/09/c34e67c5-image-2-1024x485.png)





(*Click to enlarge graphic.)*

**Prompt caching** processes shared text once, saving cost and latency. A lot of repetition exists across requests to the same application: the system prompt, the examples, the same code base, the same document behind different questions. You might as well process that shared segment once, cache it, and reuse it.

The technique was relatively rare when Huyen was writing *AI Engineering*. “There was one paper about it, and it was not really known, but it made a lot of sense. So I included prompt caching in the book, and I’m very happy to see that nowadays it’s pretty much everywhere.”

![](https://cdn.thenewstack.io/media/2026/09/c34e67c5-image-3.png)





(*Click to enlarge graphic.)*

The savings scale depending on how much of your prompt gets cached. In Claude Code logs, Huyen’s open-source tool [Sniffly](https://github.com/chiphuyen/sniffly) found cache hit rates of 90% to 97%. Some providers rewrite prompts internally to improve hit rates, but you might as well structure them yourself.

Huyen’s tip: since caching works on shared prefixes, put the stable parts of your prompt first and the variable parts later. “It’s pretty easy to do, and it can improve your application performance significantly,” she noted.

## Evaluating inference providers

Huyen closed with a warning for anyone evaluating inference providers: “There are many inference companies that provide inference optimizations for models you want to use, and a lot of them advertise just cost and latency.

“But pay attention to how many inference optimization techniques also change the model behavior or reduce the model quality. So when evaluating an inference service, it’s important to look not just at cost and latency, but also at model quality. Does this model, provided on this service, also perform similarly on standard benchmarks?”

## What’s changed one year later?

So where do we stand today, one year on from this keynote? Most of it actually aged quite well.

On the economics, I reckon Huyen was bang on… I think, for most of us as users, we don’t have all the cost levers to pull that Huyen outlined. But it’s great to understand what is happening. As a novice local LLM user myself, I found I could relate to her points on parallelism (I don’t have it) and prompt caching/quantization (within my grasp of control).

Prompt caching (which Huyen said was new when Huyen wrote *AI Engineering*) is now priced into every bundle purchase of API tokens. And her Claude Code observation (90% cache hit rates) is probably the reason we mere mortals can still afford agentic coding agents at all.

Some of it aged in ways that were hard to predict at the time. Huyen mentioned how reasoning models make inference even more significant. One year on, I think agents running multi-step loops with tool calls have turned that idea from a footnote into a way to turn Claude’s rate limits (and their infamous 99.x% availability) on their head.

All the metrics Huyen described – time to first token, time to publish, goodput under a latency SLO, etc., are all now part of the lingo and probably need to be reasoned about differently.

That’s one thing I hope she’s talking about this year! Grab a [free conference pass](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000qrLWi&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202026-10-21%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack) and join us online.

***Grab*** [***a complimentary pass***](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000qrLWi&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202026-10-21%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack) ***to PG 99 Conf 2026 and join us on October 21 and 22 to chat with Huyen.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/09/dea56ceb-cropped-523fff7d-tim.jpg)

Tim has had his hands in all forms of engineering for the past couple of decades with a penchant for reliability and security. In 2013 he founded Flood IO; a distributed performance testing platform. After it was acquired, he enjoyed...

Read more from Tim Koopmans](https://thenewstack.io/author/tim-koopmans/)