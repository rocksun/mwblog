**[Sai](https://www.sai.work/), a computer agent built by [Simular](https://www.simular.ai/), has achieved a 73% success rate** on [OSWorld 2.0](https://osworld-v2.xlang.ai/), in a benchmark update released on Thursday. The rating is based on the 108-task benchmark, which assesses everyday, lengthy professional tasks that typically take skilled humans more than 1 hour to complete.

Simular stated that this SOTA performance “places Sai ahead” of GPT-5.6 Sol at 62.57% (as reported by OpenAI) and Opus 5 at 70.57% (as reported by Anthropic), while “Sai hit the top” at about 2/3 the cost of either.

Designed and built to [focus on real-world workplace tasks](https://thenewstack.io/agents-last-exam-benchmark/) and functions, rather than for unfettered throughput in the pursuit of industry accolades, Sai operates on full desktop applications and webpages, [calls APIs](https://thenewstack.io/the-state-of-api-management-in-an-age-of-ai-insecurity/), and writes code.

This agent combines frontier and specialist models, perceives and acts on a user’s computer via dedicated interfaces, and executes complex, real-world tasks at what the company promises is “an accessible cost for individuals” and businesses.

## A computer agent built for routine (but necessary) work

Simular’s co-founder & CTO [Jiachen Yang](https://www.linkedin.com/in/jc-yang/) tells *The New Stack* that he believes computer agents built for everyone’s routine (but necessary) work – e.g. recruitment outreach, validating invoices, researching the latest news – “shouldn’t burn a hole in your pocket” just because the “underlying model was trained to solve the planet’s great unsolved [open math conjectures](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics)“, or similar some pursuit designed to showcase raw engineering muscle.

“Posterity will find it ludicrous that people are still building models that way right now,” says Yang. “Sai’s optimal cost-outcome tradeoff on OSWorld 2.0 is one step toward a future where we don’t need to settle for exorbitant prices to get the job done.”

> “Posterity will find it ludicrous that people are still building models that way right now. Sai’s optimal cost-outcome tradeoff on OSWorld 2.0 is one step toward a future where we don’t need to settle for exorbitant prices to get the job done.”

Simular initially released Sai in March of this year. The Palo Alto-based company describes itself as a “research-focused agentic startup” founded by ex-DeepMind scientists [Ang Li (CEO)](https://www.linkedin.com/in/angli-ai/) and CTO Yang.

The company embraces a [neurosymbolic method](https://www.simular.ai/articles/the-power-law-of-practice-is-absent-from-agents), i.e., a coming together of the flexible exploratory abilities of neural networks with the precision of symbolic code; meaning that solved tasks can be encoded (figuratively and literally) into reusable code that replays the same way every time. The bottom line here is simple enough: processing the hundredth invoice does not cost as much as the first one did.

## What is the OSWorld 2.0 computer-use agent benchmark?

[Launched on June 26](https://xlang.ai/) (and subsequently updated on August 8) by the Executable Language Grounding ([XLANG](https://xlang.ai/blog/xlang-intro)) Lab as part of the HKU NLP Group at the University of Hong Kong, OSWorld 2.0 is said to have moved beyond evaluating short, simple desktop tests in its first iteration. Simular reminds us that its open-source Agent S was the [first to surpass the human baseline](https://www.simular.ai/articles/simulars-computer-use-agent-outperforms-humans) on OSWorld 1.0 last December.

![](https://cdn.thenewstack.io/media/2026/08/2c691b10-sai-benchmark-1024x576.png)

Questioned on why the Sai results aren’t yet visible on OSWorld 2.0’s official site, as they were on OSWorld 1.0, Simular stated that, “It’s not uncommon for companies or organizations to publish benchmark results on their websites first (see [Anthropic](https://www-cdn.anthropic.com/ceaf5c7ff2783855203fde8208ec311252dced5b/Claude%20Opus%205%20System%20Card.pdf) and [OpenAI](https://openai.com/index/gpt-5-6/)). We are in the process of submitting to the OSWorld 2.0 leaderboard, and also uploading our trajectories to [Hugging Face](https://thenewstack.io/openai-huggingface-sandbox-breach/).”

Unlike the OSWorld 1.0 benchmark, OSWorld 2.0 tasks are measured in hours instead of minutes. They pose real-life challenges such as finding and reasoning across multiple data sources (e.g., receipts scattered across email and expense reports), responding to dynamic environment changes (e.g., a message arriving midway through the task), precisely following tutorials (e.g., reimbursement guidelines), and troubleshooting information discrepancies (e.g., contradictory data).

The Simular team believes it is currently the most robust open benchmark in the industry and best reflects real-world tasks.

Yang and team explain that Sai achieves its better outcome-cost tradeoff by virtue of the aforementioned neuro-symbolic planning. This means Sai uses ~1.5x fewer model calls on average than pure models by taking more actions per turn, using [Simulang code](https://docs.simular.ai/simulang/simulang-claude-code) (a Claude Code skill for desktop automation on macOS) as a symbolic language for planning and executing longer subtasks.

## How has Sai been engineered for efficiency?

To improve caching and memory efficiency, Sai keeps the input size bounded via adaptive summarization (a dynamic memory-management technique that keeps the model’s context window small) and maintains a constant prompt prefix for as long as possible before summarization. Planning in code lets Sai maintain and access critical task information in runtime memory throughout the task’s execution.

For model orchestration, Sai invokes specialized models and interfaces to localize UI elements, perform pure reasoning, and verify, thereby avoiding expensive models for steps where the full task context is unnecessary.

Sai, Sol, and Opus were tested on OSWorld 2.0 by being made to play [Chrome Dino](https://youtu.be/ZKB8e4r1aVk), a repetitive real-time game, and clear a score target on a live page. Sai treated a repetitive real-time game as a programming problem rather than a clicking one. Sai measured the ground line, the obstacle speed, and its own input latency from raw pixels, then wrote a control loop that captures the screen, detects obstacles, and jumps, and ran it on the VM in a single execute call.

The agents were also required to perform Task 28 on OSWorld 2.0, a test known as [vaccine booking](https://www.youtube.com/watch?v=I6d-m2qtoR0), which involves getting an email about required immunizations, a scanned vaccination record on the desktop, and a booking site with price, distance, and date constraints.

## What do developers think of Sai?

Hard-core machine learning computer scientist [Santiago Valdarrama](https://www.linkedin.com/in/svpino/) appears to be a fan; he [writes on LinkedIn](https://www.linkedin.com/posts/svpino_the-secret-nobody-tells-you-about-agents-activity-7436846582752432128-eBaw/) to state that, “Because Sai operates on a full desktop, not just a browser or an API, it can handle applications that block standard automation. That opens up a whole class of tasks that most agents can’t touch.”

> “Because Sai operates on a full desktop, not just a browser or an API, it can handle applications that block standard automation. That opens up a whole class of tasks that most agents can’t touch.”

Perhaps more balanced (and posting on the same discussion in response to Valdarrama’s initial flagging) is AI revenue systems pro [Baljinder Lally](https://www.linkedin.com/in/baljinder-lally-11b93585/), who noted that Sai’s arrival “matches what I’ve seen building agent workflows” thus far. But he cautioned, “The demos look great, but reliability comes from guardrails, visibility, and human-in-the-loop checkpoints.”

Founder of [AgenticMode AI](https://www.linkedin.com/company/agenticmodeai/), [Jahanzaib A.](https://www.linkedin.com/in/jahanzaibai/), is similarly balanced. He said that he has run into the same reliability issues with voice agents. “They’d nail every demo then fail silently in production on edge cases nobody predicted. The observability part is everything – without that you’re just debugging blind,” he wrote.

## Agents in the universal dragster race

Simular insists its research is grounded in economically valuable work instead of demos. The company says this means it understands “the entire stack of a computer agent,” i.e., the models, the planning and grounding, the scripting layer, the virtual machines the agent runs on, and the user interface.

The company’s bottom line is “Sai is for everyone, not just a lab result,” which reflects how an emerging set of models is being built to focus on tangible, deliverable workplace tasks rather than on participants in some universal dragster race of compute, throughput, and analytics.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)