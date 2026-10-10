**AWS’s new decision model comes with a familiar address.** Released October 1, [Strands Decider 2B](https://thenewstack.io/aws-strands-decider-model/) is an open-weight model built on Alibaba’s Qwen3.5. But run it as a server, and it answers at `/v1/systemone` — the same endpoint startup TypeSafe AI introduced with [Jev](https://thenewstack.io/typesafe-jev-system-one/) just over two weeks earlier.

Within three weeks, decision models went from one startup’s experiment to a category. OpenAI, Upstage, Perplexity and Cloudflare offer hosted decision models, while AWS and independent developers have published open weights on Hugging Face. What’s standardizing fastest is TypeSafe’s schema — the structure of the request and response — even when vendors publish it under their own URLs and endpoints.

LLM developers saw a similar process unfold. OpenAI’s Chat Completions API became the default interface for LLMs because so many providers cloned it. OpenAI later launched Open Responses, an open specification based on its Responses API. That history suggests a possible trajectory rather than a settled outcome.

## What a decision model returns

A decision model takes application state, such as a customer message and the relevant policy, along with a set of typed questions. It returns structured answers with a probability attached to each option, and it never writes prose, code, or explanations of its reasoning. TypeSafe calls Jev a System One model, borrowing a term psychologist Daniel Kahneman popularized for fast, intuitive judgment

The System One API reduces every decision to three question types. A choice question selects one option from a list, and a score question places the input on an ordered rubric. A noul (yes/no) question returns the probability that a yes-or-no condition holds, and developers can mix all three types in one request.

Jev also returns a confidence value, which teams often mistake for the chance that an answer is correct. TypeSafe’s [documentation](https://docs.typesafe.ai/confidence) explains that confidence measures how concentrated the probability distribution is and advises teams to set thresholds based on their own data. Calibration is measured across many decisions, so a high confidence value never guarantees an individual answer is right.

Think of a decision model as the `if` statement of an AI application. An LLM can classify a support ticket, but it generates tokens to do so and reports its certainty loosely. A decision model hands the application a probability it can branch on, in a fraction of the time.

## Three patterns that made Jev useful in agents

A decision model works beside the LLM. The LLM plans, writes, and calls tools, while the decision model handles the many small judgments an agent makes between those steps.

Imagine a support agent processing a refund request. The LLM drafts a plain-language reply to the customer. A single call to the decision model picks the queue, scores the customer’s frustration, and estimates whether the refund policy applies. Three patterns emerged within days of Jev’s launch.

### Routing requests to the right model

[OpenRouter](https://openrouter.ai/typesafe) launched Jev Router on September 25 to choose the model and reasoning effort for each incoming request. The decision model acts as a dispatcher, reserving expensive LLMs for requests that need them.

The [Strands Decider](https://github.com/strands-labs/strands-decider) repository ships an example that hooks into the Strands Agents `before_tool_call` event. It gates a weather-tool call on two yes/no decisions, so the agent asks the user which city instead of guessing. AWS reports that answers at 0.9 confidence or higher were right about 95% of the time on short classification tasks the model had not seen.

### Falling back when the decision model fails

Maxim AI’s Bifrost gateway [routes](https://www.getmaxim.ai/bifrost/blog/typesafe-system-one-models-and-new-v1-decisions-endpoint) decisions to an LLM when Jev is unreachable. It emulates the decision through the provider’s Responses API and returns an answer in the same shape as Jev’s.

Those patterns showed why the abstraction was useful. As competitors copied it, TypeSafe’s API became a shared contract.

## How the System One contract spread

The first group of adopters implements TypeSafe’s endpoint directly. Upstage serves [Solar Decide](https://openrouter.ai/upstage/solar-decide) through the System One schema, and Ollama [added](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) a `/v1/systemone` endpoint in version 0.35, explicitly based on TypeSafe’s API. Strands Decider, Jared Palmer’s Kev, and Zefan Cai’s community-built Open-Jev expose the same interface, as do local runtimes such as Ollaya and SGLang.

The second group keeps the semantics and changes the address. OpenRouter’s native interface for Jev is its own Decisions API. It also provides a TypeSafe-compatible route, so existing SDK clients can switch providers by changing the base URL. Venice reportedly [serves](https://pexon-consulting.de/blog/venice-api-jev-decisions-privacy/) Jev through a beta decisions endpoint of its own. Perplexity’s Decisions API supports the same choice, noul (yes/no), and score question types, though it uses a different path.

OpenAI remains the outlier among the large vendors. It answered Jev at [DevDay with a Decisions API](https://thenewstack.io/openai-decision-api-luna/) built on a specialized version of GPT-6 Luna. The service is still in limited preview with no published schema or pricing.

The practical result is code-level portability. TypeSafe’s SDKs work against any server implementing the System One API once you change the base URL. An application written against the contract can therefore move from hosted Jev to a local Strands Decider without rewriting its decision logic. Servers still differ in option limits, in how they compute confidence, and in answer quality, so a switch still needs testing.

In short, TypeSafe is winning the schema war while the endpoint war remains open.

## What the Chat Completions precedent suggests

OpenAI’s Chat Completions API offers the closest precedent. vLLM, Ollama, OpenRouter, and dozens of other servers cloned it until it became the default way to call an LLM, regardless of who trained the model. OpenAI later moved its own platform to the Responses API. In January 2026, it launched Open Responses, an open specification based on that design, with OpenRouter, Hugging Face, LM Studio, vLLM, Ollama and Vercel as launch partners. Simon Willison [noted](https://simonwillison.net/2026/Jan/15/open-responses/) that he would have preferred a standard based on Chat Completions, precisely because so many products had already cloned it.

The precedent carries two lessons for decision models. First, the semantic shape spreads before any formal governance, as System One is experiencing now. Second, the company that defines the shape eventually has to open it. Otherwise, the ecosystem drifts into compatible variants, such as the decision paths OpenRouter, Venice, and Perplexity already run.

The differences matter as much as the parallels. The Chat Completions standard took years to settle and covered message roles, streaming, and tool calling, all backed by large volumes of application code. System One covers three question types and is less than a month old, making it easy to clone and fork. If TypeSafe publishes System One as an open specification, it can follow the Open Responses path. If OpenAI publishes a different schema, the category will carry two competing contracts.

## Hosted, open-weight and hybrid models

Hosted services offer a managed endpoint with per-token billing, whereas open-weight models run on a team’s own hardware and keep sensitive application state inside the network. Jev remains the reference implementation on the hosted side, though TypeSafe has not disclosed its size or base model. Upstage built Solar Decide on Solar Mini 4, a mixture-of-experts (MoE) model with 35 billion total and 3 billion active parameters.

Perplexity straddles both camps with a hybrid approach. It released pplx-decider on October 1 with Apache 2.0 weights and a hosted API, then shipped version 1.1 on October 6. The new [model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b) reports a Decision Index of 61.56, up from 56.4. Perplexity credits most of the gain to lifting the causal mask and training on more data.

Most of the first decoder-based open implementations use Qwen3.5, including Strands Decider, the smaller Open-Jev models, and the first three Kev sizes. The ecosystem is already spreading beyond that base, with Kev-27B, Open-Jev-27B, and Perplexity’s model built on Qwen3.8 and Laya from Convai Innovations built on the ModernBERT encoder. Palmer [reports](https://aiweekly.co/alerts/jared-palmer-ships-kev-an-apache-20-jev-style-decision-model-family-built-on) that porting Kev to Qwen3.5 cost roughly $95 in H100 time.

Many of the open implementations avoid autoregressive decoding altogether. They replace the language-model head with a small readout that scores the available options in one pass. AWS reports a median of 115 milliseconds per question for the 1.9 billion-parameter Strands Decider on an RTX 3090.

The table below reflects the market as of October 7, 2026.

| Model | Maker | Deployment | Weights | Base model | Size | API | Published evaluation (source) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jev 1.13 | TypeSafe AI | Hosted (TypeSafe, OpenRouter, Venice) | Closed | Undisclosed | Undisclosed | System One (native) | JevBench v1.5.4, third at 72.13 |
| Decisions API | OpenAI | Hosted, limited preview | Closed | GPT-6 Luna | Undisclosed | Own API, schema unpublished | None published |
| Solar Decide | Upstage | Hosted (Upstage, OpenRouter) | Closed | Solar Mini 4 | 35B MoE, 3B active | System One | None published |
| pplx-decider v1.1 | Perplexity | Hosted and self-hosted | Apache 2.0 | Qwen3.8-27B | 26B | Own Decisions API | Hugging Face Decision Index, 61.56 |
| Strands Decider 2B | AWS | Self-hosted | Apache 2.0 | Qwen3.5-2B | 1.9B | System One | AWS run on JevBench public set, 0.723 |
| Kev | Jared Palmer | Self-hosted | Apache 2.0 | Qwen3.5, Qwen3.8 | 0.8B, 4B, 9B, 27B | System One | Author’s test sets, Kev-9B at 0.837 (locked test); Jev 0.857 vs. Kev-9B 0.812 (dev set) |
| Open-Jev | Zefan Cai | Self-hosted | Published adapters and decision heads (MIT code) | Qwen3.5, Qwen3.8 | 2B, 9B, 27B | System One | Author’s run on JevBench public subset, 27B v1.1 at 85.28% (197 of 231) |
| Laya | Convai Innovations | Self-hosted | Apache 2.0 | ModernBERT | 322M to 421M | System One | JevBench v1.5.4, tracked but not yet publicly ranked |

The evaluation column mixes independent benchmarks with vendor and author test sets, so it does not form a single leaderboard. Florian Standhartinger and contributors maintain [JevBench](https://benchlm.ai/decision-models) under the MIT license, and it is the closest thing to a neutral score. Its v1.5.4 leaderboard tracked 112 decision systems and placed Jev third, behind blockbrain’s Cygnet and the open-weight Winnow-12B.

## The reliability question

Decision models act directly on their answers, which raises the stakes for robustness. A University of Southern California researcher [found](https://arxiv.org/pdf/2609.30243) that an optimizer could redirect 61.4% of 508 initially correct Jev decisions. It did so by adding short, natural-looking context that pushed the model toward a chosen wrong answer. The search used up to 64 accepted evaluations per item, and the successful additions had a median length of 31 words.

The figure is an adversarial targeted-flip rate, not the probability that ordinary context will cause Jev to fail. Still, an open Qwen-based model in the same study flipped at 72.6%, suggesting the weakness lies with the category rather than with a single vendor. Platform teams should treat confidence thresholds as one control among several, especially when the application state includes user-supplied text.

## The economics of a shared contract

On OpenRouter, Jev costs $0.042 per million input tokens with no charge for output. Perplexity prices its hosted v1.1 model at $0.02 per million input tokens. That makes a routing or policy check far cheaper than an equivalent LLM call. Self-hosted open-weight models replace per-token API charges with infrastructure and operating costs, a trade that favors pipelines making thousands of decisions an hour.

For enterprises, a shared contract adds a second benefit. Governance and procurement teams can approve one integration pattern, then swap the backend as accuracy, price, and data-residency requirements change. This gives enterprise customers a stronger negotiating position than a market of incompatible endpoints would.

The same contract commoditizes the interface for vendors. TypeSafe now has to win on model quality and calibration, because a developer can replace Jev with Strands Decider or Kev by editing a URL. OpenAI and Perplexity face different pressures, since a proprietary schema requires developers to write integration code that much of the ecosystem no longer needs.

## What next for the decision models?

System One has emerged as the leading interoperability contract for decision models, with wire-compatible implementations from AWS, Upstage, Ollama, and the open-source community. Once published, OpenAI’s schema will decide whether the category consolidates around one contract or splits into two.

Decision models are becoming a portable, inexpensive judgment layer beside the LLM. Whether developers trust it to gate real actions will depend less on API convergence than on calibration and robustness. The safeguards teams build around these probabilities will matter just as much.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)