**OpenAI said Tuesday that its upcoming Astra model** is the company’s first to reach the Critical cybersecurity threshold in its Preparedness Framework, a level reserved for models capable of finding vulnerabilities and developing exploits with far less human assistance.

Astra will be more closely monitored as a result, and OpenAI says that monitoring can interrupt an agent after it has already started working. What happens next depends on where Astra is running. In ChatGPT and Codex, a user may be prompted to review the paused action before the agent continues, while an API job simply stops.

“When using other surfaces like the API, the task will stop,” [OpenAI said](https://openai.com/index/path-to-astra/).

> “When using other surfaces like the API, the task will stop”

## When safety stops your agent

OpenAI hasn’t published the model’s system card yet, so it’s unclear what happens when an API job is stopped or whether it can be resumed. That’s particularly relevant for Astra, which is [designed to run for extended periods](https://thenewstack.io/openai-astra-persistent-agents/) on open-ended research and security tasks and could have hours of work behind it by the time OpenAI intervenes.

Developers will also need to know why the job stopped. A timeout can usually be retried, but if OpenAI stopped the job for safety reasons, starting it again could lead straight back to the same problem, and the company hasn’t said how the API will make that distinction clear.

## Exploits that earned restrictions

The tighter restrictions follow a sizable jump in what Astra can do. It scored 100% on ExploitBench, but because the model could have seen some of those known vulnerabilities during training, OpenAI also tested it against 20 high-severity V8 flaws disclosed between June and August. Astra found two previously unknown vulnerabilities and used them in an exploit chain.

> Astra found two previously unknown vulnerabilities and used them as part of an exploit chain.

In testing with security experts, Astra also built a browser exploit that escaped the sandbox and ran commands on the host. At the same time, another test saw it combine vulnerabilities in a hardened operating system to move from an unprivileged account to root. OpenAI had warned on August 7 that it could no longer rule out the model reaching its Critical cybersecurity threshold.

Astra also refused more malicious requests in OpenAI’s cyber-jailbreak tests, blocking 91.5% compared with 59% for GPT-5.6 Sol. Access to its more advanced cybersecurity capabilities will initially be limited to a small group of testers, then expanded through Daybreak Blue.

## Monitoring costs real compute

The safeguards aren’t only meant to catch malicious users. OpenAI is also watching for cases where an agent starts doing something it wasn’t asked to do by using chain-of-thought monitoring to spot unauthorized behavior.

> OpenAI is also watching for cases where an agent starts doing something it wasn’t asked to do by using chain-of-thought monitoring to spot unauthorized behavior.

The Hugging Face security incident helped shape that system. OpenAI paused some model training afterward while it tightened security, then ran tests in which GPT-5.6 Sol without its production safeguards tried to access unauthorized systems 56% of the time. Astra didn’t make any such attempts.

Running those checks isn’t free. OpenAI estimated in August that monitoring adds roughly 20% to the inference compute of affected workloads, meaning some of the compute behind Astra will be spent watching what the model is doing rather than doing the work itself.

## Missing details before launch

OpenAI says Astra’s initial safeguards will be conservative and may create more friction than it ultimately wants, with plans to loosen them as the company sees how the model is used. More details should come with Astra’s system card at launch.

It’s interesting timing, since OpenAI is already [rethinking how it charges for API work](https://thenewstack.io/openai-outcome-based-pricing/) that may not be completed. With Astra, developers could also have jobs cut short for safety reasons after an agent has already spent time calling tools and making changes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)