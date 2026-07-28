**Moonshot AI became the latest AI company to discover** that launching a popular model is only half the battle. Less than two days after releasing [Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/), the company stopped accepting new subscribers after demand exhausted its available GPU capacity. Existing users will keep access while Moonshot expands its infrastructure and reopens subscriptions in batches.

## Inference demand outpaces supply

The incident emphasizes how demand is outpacing available infrastructure. As AI models take on longer, more coding and agentic workloads, companies are finding they need more inference capacity than they anticipated.

“Kimi K3 has received far more love than we expected,” the official Moonshot account writes on X. “Over the past 48 hours, demand has pushed close to the limits of our current capacity. We’re adding capacity as fast as we can and will reopen new subscription spots in batches.”

> “We’re adding capacity as fast as we can and will reopen new subscription spots in batches.”

For infrastructure engineers and developers, the resulting capacity crunch is a bold indication of why companies from OpenAI to Anthropic to Moonshot are [rationing access](https://thenewstack.io/agentic-ai-token-costs/) instead of selling unlimited usage.

## Open weights, closed capacity

At 2.8 trillion parameters, Kimi K3 is one of the largest open-weight models slated for release — Moonshot has scheduled the [public weight drop for July 27](https://aireiter.com/blog/kimi-k3-open-weights). In [Arena.ai’s Frontend Code Arena](https://officechai.com/ai/kimi-k3-beats-fable-5-gpt-5-6-sol-on-frontend-code-arena/), K3 topped both OpenAI’s GPT-5.6 Sol and Anthropic’s Claude Fable 5. On the broader [Artificial Analysis Intelligence Index](https://the-decoder.com/kimis-open-model-k3-nears-gpt-5-6-sol-and-fable-5-while-signaling-the-end-of-super-cheap-chinese-ai/), it trails both, scoring 57 to Fable 5’s 60 and Sol’s 59. That doesn’t make it any easier to run.

Open weights let anyone deploy the model, but whoever hosts it still has to pay the inference bill. Coding activities tend to tie up GPU resources far longer than a typical chatbot interaction, making it harder to keep latency low as more developers pile on.

“Agent tasks are not one-off question answering; they continuously generate, read, and process tokens during ongoing tasks,” wrote [Citigroup semiconductor analyst Peter Lee](https://www.linkedin.com/in/peter-c-lee-55876480/) in a [research note](https://www.binance.com/en/square/post/346652838928769).

Lee argued that as developers build longer agentic workflows, lower inference costs are quickly “re-converted into higher total resource consumption,” shifting the bottleneck from compute to server memory.

Moonshot’s subscription pause is a sign that keeping enough inference capacity online once developers start using it at scale might be just as hard as building the model.

> “Agent tasks are not one-off question answering; they continuously generate, read, and process tokens during ongoing tasks.”

## China’s chip constraints compound crunch

For a company like Moonshot, this general industry bottleneck is compounded by regional infrastructure realities. Unlike traditional software companies, AI developers typically rent much of this computing power from cloud providers such as Alibaba Cloud, Tencent Cloud, and Huawei Cloud rather than owning extensive data-center infrastructure themselves.

The capacity crunch illustrates the mounting challenge facing Chinese AI developers as US export controls continue to restrict access to leading chip provider Nvidia’s most advanced AI chips. As a result, companies such as Moonshot depend on a combination of older chips and domestically produced alternatives. These constraints have forced Chinese developers to concentrate strongly on software tuning and more efficient use of computing resources to narrow the performance gap with US rivals.

## Token economics under pressure

The scramble for computing power has fueled a data-center construction boom across China. Alibaba has committed more than $53 billion to AI and cloud infrastructure over three years, while ByteDance is reportedly considering spending as much as $70 billion this year on AI data centers and related infrastructure.

AI companies typically charge customers based on the number of tokens, or units of text, processed by a model, making token prices a key measure of operating costs.

According to [Bernstein Research](https://finance.yahoo.com/technology/ai/articles/chinas-latest-star-ai-model-081053486.html), Moonshot charges $3 per million input tokens and $15 per million output tokens for Kimi K3. This makes it about 40% cheaper than Anthropic’s Opus 4.8 and roughly 70% cheaper than Claude Fable 5.

“A world where there are only [two to three] dominant frontier labs with 90 percent inference margins is net negative for every other layer while being awesome for those [two to three] labs,” wrote Atreides Management founder [Gavin Baker](https://www.linkedin.com/in/gavinbaker-portfoliomanager/) on [X.](https://x.com/GavinSBaker/status/2078110934740980193?utm_source) Baker argued that models like Kimi K3, Grok 4.5, and Muse 1.1 could shift value away from the model layer and toward chipmakers, cloud providers, and [the software companies building the infrastructure](https://thenewstack.io/future-proof-ai-infrastructure/) that serves AI models.

For developers, Moonshot’s subscription freeze serves as an [architectural warning](https://thenewstack.io/enterprise-ai-model-routing/). The era of assuming infinite, cheap API access is ending.

> “A world where there are only [two to three] dominant frontier labs with 90 percent inference margins is net negative for every other layer while being awesome for those [two to three] labs.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)