South Korean AI model company [Upstage AI](https://www.upstage.ai/blog/en/solar-pro) officially announced the launch of its [Solar Pro 4](https://www.upstage.ai/blog/en/solar-pro-4) closed commercial LLM [last week](https://www.prnewswire.com/news-releases/upstage-ai-unveils-solar-pro-4-scoring-42-on-artificial-analysis-index-to-rank-among-global-frontier-models-302856434.html?tc=eml_cleartime). Now also headquartered in San Jose as of 2025, the company is aiming to cut into the AI software engineering market with a strong [agent behavioral reliability](https://thenewstack.io/restack-gives-product-teams-the-reins-to-own-ai-agent-behavior/) play.

## How do we define agent reliability?

Bundled with a (perhaps predictable) promise of operations at a fraction of US frontier-model cost, Upstage’s notion of agent reliability is explained as a model optimized for stably performing workflows that can execute long-context reasoning consistently across multiple steps and stages.

Reliability in this context also encompasses document understanding and information extraction, a model’s ability to adhere to corporate policy, and an ability to call and invoke the correct software tools, sub-agents or [datasets](https://thenewstack.io/5-useful-datasets-for-training-multimodal-ai-models/) needed for a given task, delivered in the correct format.

Head of US operations at Upstage AI, [Kasey Roh](https://www.linkedin.com/in/kaseyroh/), tells *The New Stack* that Upstage has built the “plain cut business suit” of the model world; this is the AI worker bee that gets core business functions done without the wasted token burn associated with retries, malformed outputs, and instruction-following failures.

“Save the frontier models for the frontier problems; we built the workhorse,” Roh says. “If you’re building with AI in production, most of what you’re actually shipping is boring, repetitive work, like document extraction, triage, and simple decisions stacked on top. Pointing a frontier model at that is overkill and honestly a liability: you’re eating flagship prices and flagship latency to run the same task, millions of times a day.”

She notes that  Solar Pro 4 is engineered to prevent token burn waste, with instruction-following capabilities that “hold across turns”, tool call structure that stays intact, and agents that act as instructed, within company policy, and within the boundaries of [valid schema](https://thenewstack.io/json-schema-ai-reliability/) for the job in hand.

> **“**Save the frontier models for the frontier problems; we built the workhorse. Talk to anyone actually running agents in production. Their ask is never ‘make it more creative’; it’s ‘make it reliable enough that I’m not re-tuning prompts and burning tokens every turn’ all day.”

“Our workhorse wears a boring business suit precisely so humans don’t have to. Talk to anyone actually running agents in production. Their ask is never ‘make it more creative’; it’s ‘make it reliable enough that I’m not re-tuning prompts and burning tokens every turn’ all day,” Roh adds.

## What do AI developers think of Solar Pro 4?

In terms of market perception and adoption, Roh and say that within a week of [being listed on OpenRouter](https://openrouter.ai/upstage/solar-pro4#apps), Solar Pro 4’s token consumption exceeded 370 billion tokens.

Solar Pro 4 is also integrated into Hermes Agent, the AI agent developed by U.S.-based [Nous Research](https://nousresearch.com/), where it powers multi-step, self-improving AI agents. In effect, that means Upstage is registered as a model provider alongside [OpenAI](https://thenewstack.io/voice-ai-openai-anthropic/), [Anthropic](https://thenewstack.io/anthropics-claude-security-beta/), [Google](https://thenewstack.io/google-gemini-agent-platform/), and [Nvidia](https://thenewstack.io/palantir-nvidia-sovereign-ai/) by some measure. The company also has partnerships with AWS and AMD.

Solar Pro 4’s overall performance, based on the global [AI evaluation body Artificial Analysis](https://artificialanalysis.ai/models/solar-pro4?models=solar-pro4), is 42 points, placing it on par with general-purpose frontier models.

According to Roh and team (and by this yardstick at least), this is an improvement of more than three times compared to Solar Pro 3 and it has “surpassed big tech models” like Nvidia’s Nemotron 3 Ultra (38 points) and Google’s Gemini 3.5 Flash-Light (37 points). It also outperformed competing sovereign models such as [Mistral](https://thenewstack.io/mistral-vibe-cloud-agents/) Medium 3.5 (30 points) and [Cohere](https://thenewstack.io/cohere-sovereign-coding-model-north-mini-code/) Command A+ (23 points).

The ability to handle long and complex documents without failure means that Solar Pro 4 scored 71 points in the long-context comprehension benchmark ([AA-LCR](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning)), which assesses the ability to extract information from large volumes of long documents and infer answers based on that information, showing performance 2.3 times superior to the previous version.

## What happens when long complex reasoning fails?

Upstage has built its core business serving enterprises in regulated and complex industries, such as financial services, insurance, manufacturing, and supply chain, where models must behave predictably in production, but what happens when long complex reasoning fails?

“The classic one is the long tabular document,” recounts Roh. “Let’s say an invoice or a technical spec has hundreds of line items across hundreds of pages.”

She explains that every agentic workflow is built on top of accurate extraction from documents of this kind. In her example scenario, the model handles rows 1 through 200 just fine, then somewhere past that poit it starts skimming: dropping rows, or silently filling a cell by pattern-matching from earlier rows instead of reading the actual value.”

“What’s ugly is that the output is seemingly well-formed, so nothing catches it until someone reconciles it manually at the final stage. That failure mode is precisely what we trained against,” explains Roh.

> “What’s ugly [in a long complex reasoning failure] is that the output is seemingly well-formed, so nothing catches it until someone reconciles it manually at the final stage. That failure mode is precisely what we trained against.”

## How much cost saving is on offer here?

On average, Roh is on the record here and says that Solar Pro 4 costs about “90% less per typical document workflow”, at list price.

“For instance, a document fact-checking agent, where multiple documents in, structured report out, running ~300K input / 15K output tokens per task: that’s roughly $1 per task on premium frontier pricing versus $0.10 on Solar Pro 4. At 50,000 tasks a month, a $50K bill becomes a $5K one. And through September 10 there’s a launch promo at 90% off list, so right now you can run the whole month’s workload for what a frontier model charges you before your first coffee refill on day one,” she details..

The launch of Solar Pro 4 follows Upstage’s release of [Solar Open 2](https://www.linkedin.com/posts/upstageai_solaropen2-upstageai-solarllm-activity-7485853995350011904-c2lF/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAWx2KsBuQ0EY3EdQfRmgxKmjE9qbcllbdU), the company’s open ecosystem for developers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)