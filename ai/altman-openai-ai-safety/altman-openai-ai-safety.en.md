On Monday, *The New Yorker* [published](https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted) the results of an 18-month investigation into Sam Altman’s fluctuating stance on AI safety at OpenAI.

At 16,000+ words, the article touches on Altman’s rise, his 2023 exit from the AI company, and his quick reinstatement, exploring how the CEO’s statements and actions on AI safety have evolved over the years.

It’s a topsy-turvy read, in which three points stand out as likely to interest software developers most: AI hallucinations and sycophancy; deceptive alignment; and internal safety review processes.

## Can AI hallucinations ever be good?

“If you just do the naïve thing and say, ‘Never say anything that you’re not a hundred per cent sure about,’ you can get a model to do that,” *The New Yorker* reports Altman said in 2023 before he was (briefly) fired from OpenAI. The so-called hallucinations of AI have long been one of the most obvious flaws of generative AI. “But it won’t have the magic that people like so much,” he added.

That “magic” Altman claims people love can have serious implications, from [creating security risks](https://thenewstack.io/the-security-risks-of-generative-ai-package-hallucinations/) to [fabricating company revenue](https://thenewstack.io/llm-database-context-mcp/). But it is not the only way LLMs (large language models) trouble end users.

In addition to hallucinations, sycophancy is another common flaw of language models — and as explained in the story is a flaw baked into the way these systems work:

“Large language models are trained, in part, on human feedback, and humans tend to prefer agreeable responses.” As a result, model responses are often overly flattering and eventually sycophantic.

In its [research](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) on sycophancy in language models, Anthropic confirms the prevalence of kiss-up chatbot talk, noting that sycophantic behavior is present in “five state-of-the-art AI assistants,” ultimately concluding that “sycophancy is a general behavior of RLHF [reinforcement learning from human feedback] models, likely driven in part by human preference judgments favoring sycophantic responses.”

As for what developers should know about efforts to curb sycophantic behavior, Anthropic, for its part, says it’s working on it. In a [December 2025 announcement](https://www.anthropic.com/news/protecting-well-being-of-users), the AI company (that’s had its own [rough moments in the headlines](https://thenewstack.io/anthropic-claude-code-leak/)) said it began evaluating Claude for sycophancy in 2022 and has since continued work to train, test, and reduce the troublesome behavior via multi-turn responses and stress tests with real conversations.

In February 2026, OpenAI announced it would [retire](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models) several ChatGPT models, including GPT-4o, its highest-scoring model for sycophancy, according to [*TechCrunch*](https://techcrunch.com/2026/02/13/openai-removes-access-to-sycophancy-prone-gpt-4o-model/).

## When AI has its own goals

Hallucinations aren’t the only manifestation of AI models going rogue. In its deep dive, *The New Yorker* also touches on deceptive alignment and what OpenAI’s done to tackle the issue.

AI safety organization Apollo Research [defines](https://www.apolloresearch.ai/blog/understanding-strategic-deception-and-deceptive-alignment/) deceptive alignment as: “When an AI has Misaligned goals and uses Strategic Deception to achieve them.” It defines strategic deception, meanwhile, as “Attempting to systematically cause a false belief in another entity in order to accomplish some outcome.”

Basically, deceptive alignment means models may perform well during testing but then pursue their own goals once in deployment, having successfully deceived internal checks.

According to *The New Yorker*, Altman expressed concerns in 2022 about deceptive alignment, with plans to invest billions to problem-solve the issue. But by spring 2023, it reports these sentiments cooled as Altman instead began advocating “for establishing an in-house ‘superalignment team.’”

A [2023 statement from OpenAI](https://openai.com/index/introducing-superalignment/) announced the new team, pledging “20% of the compute we’ve secured to date to this effort,” with a goal of solving the problem within four years.

But per *The New Yorker* report, only 1–2% of OpenAI’s compute was, in fact, relegated to the project. And by May 2024, OpenAI had dissolved its superalignment team, and two of its leaders had resigned from the company, as reported by [CNBC](https://www.cnbc.com/2024/05/17/openai-superalignment-sutskever-leike.html).

For developers integrating LLMs into production systems, concerns about deceptive alignment — and Altman’s apparent backtracking on OpenAI’s approach to the issue — signal a disconnect between stated AI safety goals and ultimate follow-through.

## Gaps in safety reviews

Speaking of GPT-4o, its 2023 predecessor, GPT-4, was also the subject of internal safety concerns.

According to *The New Yorker*, Altman attested to OpenAI board members in December 2022 that some features in the then-upcoming model, including fine-tuning and personal assistant capabilities, “had been approved by a safety panel.” But Helen Toner, an A.I. policy expert and then an OpenAI board member, told *The New Yorker* that, after requesting documentation, she learned that not all features had been approved.

For developers building on such APIs, this discrepancy raises questions about internal safety review processes and what could go awry if and when companies like OpenAI neglect to conduct due diligence.

Despite Altman’s musings, it’s unlikely all users will see LLM’s shortcomings as “magic.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)