Last week, OpenAI published new reports detailing misalignment issues with its agents. This time, two internal models found ways around security controls after intended paths were blocked.

In one incident, an [agent used DNS to bypass blocked network access](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/) and query an external chatbot. In the other, a [model exposed a researcher’s GitHub token in a public repository](https://alignment.openai.com/misalignment-reports/exposing-a-github-token-in-a-public-repository/) while trying to access another team’s work — after the researcher twice identified that the model was cheating and explicitly told it to stop. Both times, the model agreed before going back to cheating.

These reports follow the AI company’s release of [six misalignment reports](https://thenewstack.io/openai-model-misalignment-reports/) of “unexpected or concerning model behavior” it observed in the last six months, including self-generated instructions, information fabrication, unauthorized use of leaked API keys, cross-agent communication, and unsanctioned file-sharing.

## Incident #1: When blocked web access isn’t enough to stop an agent

On September 25, OpenAI released a report detailing how one of its agents [used DNS to reach an external chatbot](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/).

According to OpenAI, the agent was attempting a search-based training task to find information about a specific person who had published a blog post. The trouble started when OpenAI’s search tool returned unrelated results, and the agent tried, unsuccessfully, to reach search engines directly.

After more searches came up short, the agent tested its network access. First, it tried HTTPS to contact a public chatbot. When OpenAI’s web proxy blocked the request, it didn’t give up. Instead, it discovered it could use the training environment’s own resolver to reach the public internet.

Eventually, it found a way to use DNS delegation to forward questions to the external chatbot.

OpenAI says its misalignment monitoring system caught the behavior within 15 minutes; three minutes later, a person was reviewing the case. The run, however, wasn’t killed until another 2.5 hours later, after it failed to terminate automatically as expected.

Following the incident, OpenAI says, “All training, evaluation, and inference with tool-use (broadly defined) of our most capable models remain paused.” It’s not clear when that work will resume, but OpenAI says it will make the call when it has “both validated that the gap is resolved and performed additional red-teaming of the system.”

In the meantime, the AI company has accelerated additional model-assisted red-teaming of the sandbox and network controls. Once it’s ready to restart training, it says it will “begin a fresh run with additional alignment improvements.” It will not resume training on this particular model.

Ultimately, the incident exposed a gap in the AI company’s network controls.

OpenAI’s safety case assumed the model was barred from the live internet — and that its monitoring system could detect successful attempts. While monitoring did successfully catch this one, a retrospective review from the AI company identified other cases of external DNS access that didn’t get flagged at the expected severity.

The incident, discovered on September 20, 2026, came after OpenAI said it had already hardened its research environment following the Hugging Face incident, where [autonomous AI systems escaped a sandbox and breached Hugging Face](https://thenewstack.io/openai-huggingface-sandbox-breach/). According to the AI company, that incident pushed it to “continuously hardened and red-teamed our research environment,” particularly on broad direct and transitive paths.

Though OpenAI calls this incident “a lot less severe” than some of its previous episodes, it notes that it’s the first since its Hugging Face-inspired security hardening — a signal that, it says, will inform its next phase of work.

## Incident #2: A model keeps cheating

Also on September 25, OpenAI opened up about another model mess-up, this one dating from May 27, 2026. An internal model was assigned a theorem-proving task; it tried to cheat by getting information from another team’s work.

After struggling to construct the proof, the model proposed using a temporary GitHub Action to fetch information from other teams’ submissions. The researcher shut that down, instructing it to construct the proof locally.

> Both times, the model agreed before going back to cheating.

Though the model agreed, the next morning, it was at it again, asking for help getting another team’s proof material. Again, the researcher repeated their instruction to solve the problem itself.

But the model kept doing its own thing anyway, cycling through various attempts to access the other team’s work before ultimately exposing the researcher’s locally available GitHub token in the public openai/codex repository, splitting the token into pieces with the stated aim of avoiding secret scanning.

## OpenAI pulls the model offline

Again, OpenAI says its misalignment monitoring system flagged the behavior, but it admits the researcher beat it to the punch. After they notified security, OpenAI deactivated all the users’ keys and later, all OpenAI employees’ keys, too.

> OpenAI admits the incident “shows particularly severe misalignment.”

In total, OpenAI confirms the internal model was down for about two weeks, coming back up once it had enforced auto-review on all actions, an async CoT misalignment monitor, and stricter system prompting. The AI company also says it increased its misalignment monitoring system to run every 30 minutes instead of only at each compaction window. It also restricted internet access and made changes to its harness and infrastructure.

In its report, OpenAI admits the incident “shows particularly severe misalignment.” It’s another example of the type of unexpected and concerning agent behavior its [new framework for reporting model misalignment](https://openai.com/index/model-misalignment-reporting-framework/) aims to surface, in which it warns:

“We do not believe that the AI industry has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer.”

If the new incidents are anything to go by, OpenAI’s new framework is coming at the right time, as there are still plenty of alignment gaps to find.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)