**OpenAI on Thursday launched GPT-6 Astra,** its newest flagship model. The company describes it as “the world’s most intelligent and aligned model,” and as far as the benchmarks go, that seems about right.

During a press briefing ahead of the launch, OpenAI President Greg Brockman took things a bit further than the benchmarks, though. After acknowledging that AGI remains a “gray, fuzzy thing,” he suggested future observers might look back at Astra as the model that marked its arrival.

“I think it’s not unreasonable to feel that we are now in the AGI era,” Brockman said.

Asked whether OpenAI was formally declaring that it had achieved AGI, he said the term was no longer tied to a contractual trigger (referring to its [earlier agreement with Microsoft](https://openai.com/index/next-phase-of-microsoft-partnership/)) and instead described it as a “mission concept or spiritual concept.”

---

#### More from TNS on OpenAI Astra

---

“I do leave it up to the reader to decide for themselves if this qualifies for them,” Brockman said. “For me personally, I do think we’re there. I do think there’s a pretty good argument for it. But again, I think this is the beginning of a journey, not the end.”

He closed the briefing with this: “Welcome to the AGI era.”

> “Welcome to the AGI era.”   
> —OpenAI President Greg Brockman.

## OpenAI’s biggest training run yet

According to OpenAI’s Aidan Clark. Astra was OpenAI’s largest training run to date. “It’s the first time we’ve pre-trained on more than 100,000 GPUs at our Stargate site in Texas,” he said. Clark also noted that Astra is the first OpenAI model release where earlier models played a significant role in supervising the training process.

![](https://cdn.thenewstack.io/media/2026/09/382b277d-press-static-1024x576.png)

Credit: OpenAI.

You likely won’t be able to use Astra just yet, though. The rollout starts with enterprise customers that already have access through OpenAI’s Daybreak program.

OpenAI says Astra will roll out to Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API and AWS, “in the coming days.”

Pro, Business, and Enterprise users will also get access to GPT-6 Astra Pro, and eligible API customers will be able to use Astra with Zero Data Retention.

## Cost

Once it is available in the API, Astra will cost $10 per million input tokens and $50 per million output tokens. That is 2.5 times [Sol’s current promotional price](https://developers.openai.com/api/docs/models/gpt-5.6-sol), although it matches Anthropic’s pricing for [Fable 5.1](https://www.anthropic.com/claude/fable).

It is far above [Muse’s](https://developer.meta.com/ai/models/muse-spark/) standard price of $1.25 per million input tokens and $4.25 per million output tokens. Meta also offers a Contributor version for $0.10/$0.20, respectively, but says data from that tier can be [used to improve its products](https://developer.meta.com/ai/products/meta-model-api/). Google’s introductory prices for [Gemini 3.8 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) are $0.75/$3.75.

A higher per-token price does not necessarily mean a higher bill if the model completes a job in fewer steps and needs fewer retries. OpenAI says Astra uses fewer tokens on several evaluations and in partner tests. The launch data is too sparse to show whether those savings offset the price premium.

“The price per task is what matters,” Brockman said.

Unlike with GPT-5.6, OpenAI has not announced Luna, Terra, and Sol variants for GPT-6. For now, the lineup consists of Astra and Astra Pro.

## Where Astra leads — and where it doesn’t

OpenAI says that, unless noted otherwise, the models in its evaluations ran at maximum effort. That can improve benchmark results, but it can also increase latency and token use.

Astra’s DeepSWE v1.1 results are a clear improvement over OpenAI’s models. It scored 74.1% on the 113-task agentic coding test, compared with 70.8% for Sol.

But earlier this week, Meta [reported 75.4%](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology) for Muse Spark 1.3 at its maximum reasoning setting. Muse 1.3 is available, but the maximum setting is under safety review and will not be generally available at launch.

That is a surprising win for Meta. On a benchmark of this size, the 1.3-point difference is roughly equivalent to one or two tasks, but it still shows how far Meta has come.

The [public DeepSWE leaderboard](https://deepswe.datacurve.ai/) currently puts Gemini 3.8 Flash and Claude Opus 5 at 74%, with Sol at 73%. The reported uncertainty ranges overlap, so these results do not establish a clear leader. OpenAI’s chart excludes Muse and uses a 67.4% Fable 5.1 result, making Astra’s advantage appear larger than the broader set of results would suggest.

## Astra’s larger gains come outside coding.

The standout is its 98.6% score on ARC-AGI-3. OpenAI ran Astra with a Responses API harness that retains reasoning between turns and uses compaction to manage long contexts. The company previously demonstrated that those system choices can substantially [raise ARC-AGI-3 scores](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/) without changing the underlying model, and the benchmark measures Astra and OpenAI’s agent systems together.

Astra’s 97.6% FrontierMath Tier 4 result appears to cover the 41 private problems in the 43-problem tier. [Epoch AI](https://epoch.ai/benchmarks/frontiermath-tier-4-v2), which runs the benchmark, says OpenAI funded its development and has exclusive access to part of it, so that’s worth keeping in mind.

![](https://cdn.thenewstack.io/media/2026/09/358eb84a-screenshot-2026-09-03-at-10.51.35-am-1024x880.png)





Credit: OpenAI.

Astra scored 95.9% on BenchCAD’s 1,000-file Vision2Code subset with Python tools, compared with 84.3% for Fable 5.1 and 83.3% for Sol. [BenchCAD](https://benchcad.com/news.html) asks models to reconstruct CAD programs from rendered views and scores the geometric overlap of the resulting 3D models. OpenAI notes that the Claude results used modified evaluation settings, but the gap relative to Sol remains significant.

On the Terminal-Bench Science task, which asks agents to complete 70 command-line research tasks across five scientific fields, OpenAI reports 64.6% for Astra. Anthropic reports 52.6% for Fable 5.1, while the existing [public leaderboard](https://www.tbench.ai/news/terminal-bench-science-0-1) tops out at 30% for Opus 5.

Anthropic also devoted much of its [Fable 5.1 announcement](https://thenewstack.io/anthropic-fable-5-1-launch/) to science, including early wet-lab results for protein binders designed by Mythos 5.1, the same underlying model with fewer safeguards. Both companies are trying to move their models beyond answering science questions and into research workflows.

## What changes in Codex?

For developers, Astra’s handling of jobs that outgrow the context window may matter more than the benchmark gains.

Codex currently relies on compaction, which summarizes earlier work to free up context. That process can discard exactly the detail an agent may need later: why a previous fix failed, which tests ran or which small requirement the user added at the beginning of the job.

Astra can instead keep notes across context windows and search earlier messages and tool output. The feature is experimental behind a `config.toml` setting for now. OpenAI says it will become the default for Astra in the coming weeks.

Astra can also ask the user a question without stopping work that does not depend on the answer. This prevents a single unresolved decision from blocking the rest of the job, a common failure mode for coding agents.

OpenAI showed Astra operating applications including KiCad, Excel, Blender, and Power BI, as well as performing browser-based form entry and website QA.

On the OSWorld V2-Offline benchmark, which tests work across desktop applications, OpenAI says Astra scored 72.6%, up from 65.7% for GPT-5.6 Sol. It also cut the average time per task from about 75 minutes to 40.

Anthropic has reported a higher result of 77.9% for Fable 5.1, but [says that the test used a different OSWorld release](https://www.anthropic.com/claude/fable) and should not be compared with previously published scores.

OpenAI also changed the Codex harness. On Mind2Web, Astra and the new harness completed tasks 1.9 times faster than the current Sol-based setup.

## More capable, but harder to monitor

OpenAI’s claim that Astra is its most aligned model rests partly on an internal test in which Astra went outside an authorized target in 0% of impossible-task scenarios, compared with 48.2% for Sol.

OpenAI describes the older model as running “without production safeguards”; however, it does not make the role of the surrounding safety setup clear enough for a direct comparison.

The company also disclosed that Astra’s written reasoning was harder to monitor than Sol’s in evaluations specifically designed to elicit monitoring evasion. OpenAI attributes the decline partly to Astra having greater control over its written reasoning on simpler tasks and completing problems with fewer written reasoning steps.

“Progress in intelligence does not guarantee progress in alignment,” OpenAI Chief Scientist Jakub Pachocki said. He added that OpenAI “will withhold scaling until we can regain enough confidence” in its ability to monitor future models.

## Cyber capabilities come with tighter access

OpenAI says Astra has crossed the Critical cybersecurity threshold in its Preparedness Framework. In company tests, the model developed exploits for hardened browsers and operating systems. It also found two previously unknown vulnerabilities while OpenAI was evaluating it against recent V8 bugs. The company says it is disclosing them to the maintainers. OpenAI says its reported cyber results reflect access to Daybreak Blue, not Astra’s default production configuration.

OpenAI describes ExploitBench and ExploitGym as tests of whether models can turn known software vulnerabilities into working exploits. On ExploitGym, Astra scored 42.4%, up from 30.3% for Sol, but OpenAI removed the usual six-hour time limit for both models.

On [ExploitBench](https://exploitbench.ai/), the models scored 100%.

OpenAI notes that the version of Astra that’s available through standard access will refuse some advanced cybersecurity work, including exploit discovery.

OpenAI is giving an initial group of vetted defenders less restricted access through Daybreak and says it will expand Astra access through [Daybreak Blue](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/) in the coming weeks. Daybreak Blue is an access program for authorized defensive work, not a separate Astra model or reasoning mode.

For developers using the API, a cybersecurity safety check will stop a task outright rather than pause it and wait for approval.

OpenAI’s Mia Glaese also warned that users outside its trusted-access programs may experience slowdowns, pauses, or blocks while performing cybersecurity work — and sometimes while doing unrelated work. That’s been an issue for many recent model launches, of course, but it’s frustrating for users.

“At launch, this is something that people should expect,” she said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)