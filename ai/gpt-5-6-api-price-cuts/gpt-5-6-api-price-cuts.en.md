**OpenAI has lowered API prices for two GPT-5.6 models** only three weeks after their launch. On Thursday, the company announced that GPT-5.6 Luna is now 80% cheaper and GPT-5.6 Terra is 20% cheaper, while the price for its main reasoning model, GPT-5.6 Sol, stays the same.

“Major price cuts today,” OpenAI CEO Sam Altman writes in a post on X published on Thursday. “We want to offer the best price/intelligence tradeoff at every level.”

> “We want to offer the best price/intelligence tradeoff at every level.”

Luna now costs $0.20 for a million input tokens and $1.20 for a million output tokens, down from $1 and $6. Terra is priced at $2 per million input tokens and $12 per million output tokens, reduced from $2.50 and $15. Sol’s price stays at $5 per million input tokens and $30 per million output tokens.

Developers using Luna do not need to change their processes, but their inference costs will go down. High-volume tasks will now be much cheaper to run, without requiring any code updates or model changes.

**This timing is unusual because AI vendors** usually keep prices steady for several months after launching a new model family. OpenAI cut prices less than a month after [GPT-5.6 became available on July 9](https://thenewstack.io/openai-gpt-56-live/).

> …serving costs can be more important than small differences in benchmark performance between models.

## Infrastructure gains drive savings

The company says these price cuts were possible because of improvements to the infrastructure behind GPT-5.6, which lets the company offer “substantially more intelligence per dollar.”

These infrastructure upgrades were expected, however. A day before the price announcement, OpenAI shared [an engineering overview that explained optimizations across the inference stack](https://thenewstack.io/gpt-5-6-serving-efficiency/) for Codex and ChatGPT Work.

## GPU kernels rewritten for efficiency

OpenAI engineers rewrote the production GPU kernels, cutting serving costs by about 20%. They also redesigned Sol’s speculative decoding system, making token generation over 15% more efficient. The company updated its agent runtime as well, reducing repeated prompt computation by using prompt caching more during multi-step workflows.

## Agents amplify inference costs

Lately, developers are paying more attention to inference costs since agents often make dozens or even hundreds of model calls to finish a single task. For these workloads, [serving costs can be more important than small differences in benchmark performance](https://thenewstack.io/agentic-ai-token-costs/) between models.

The elephant in the room is that the competition has intensified from overseas. Lower-cost open-weight models from Chinese AI companies like [Moonshot](https://thenewstack.io/kimi-k3-inference-bottleneck/) are pushing commercial providers to show not just better performance, but also [better pricing for production use](https://thenewstack.io/kimi-k3-open-weight-coding/). OpenAI and Anthropic know that leaning on performance just isn’t an option anymore, which is pushing them to match Chinese prices.

The issue here is that most of those steps don’t need a model like Sol, and Chinese labs have figured out how to pack better capabilities into efficient models; a helpful option for companies running through billions of tokens a day.

The ability to send the easy tasks to open models and save the pricey APIs for the tough stuff makes a difference; OpenAI is banking on its 80% price cut on Luna to narrow that gap. Suddenly, switching to self-hosted models doesn’t look worth the hassle.

## Competition reshapes model pricing

These pricing changes come as both OpenAI and Anthropic keep adjusting the economics of their newest model families — a dynamic that [played out across three companies in a single week](https://thenewstack.io/openai-spacexai-meta-price-war/) earlier this month. Earlier this week, OpenAI [raised GPT-5.6 Sol usage limits](https://thenewstack.io/sol-usage-limits-reset/) for ChatGPT Work and Codex after finding that long coding sessions used up allowances faster than expected. Anthropic has also [made pricing changes and added premium inference tiers](https://thenewstack.io/opus-5-agentic-coding-cost/) as enterprise customers move bigger agentic workloads into production.

This announcement highlights a trend in the industry for infrastructure. Now, every percentage point of serving efficiency can lead directly to lower API prices, turning cost optimization into a competitive advantage instead of just an engineering goal.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)