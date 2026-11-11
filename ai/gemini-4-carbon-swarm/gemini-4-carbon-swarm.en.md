![Chat bubble](https://cdn.thenewstack.io/media/2026/11/94b532e0-getty-images-ngci-nquuq-unsplash-1024x677.jpg)

**Google released Gemini 4 Carbon to paying developers Tuesday**, positioning its newest frontier model above Gemini 4 Argon for complex software engineering, cybersecurity, and scientific reasoning.

Argon remains Google’s recommended model for everyday engineering and knowledge work. while Carbon is designed for more demanding tasks, including multi-package migrations, cross-subsystem debugging, and long-horizon agentic workflows.

[Koray Kavukcuoglu](https://www.linkedin.com/in/koray-kavukcuoglu-0439a720/), SVP of Google DeepMind and Google’s chief AI architect, described Carbon in the [launch announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) as the company’s strongest model for complex, multi-step work.

The release also introduces `/swarm`, a preview feature in Google Antigravity that coordinates multiple coding agents from a single prompt.

## Multi-agent coding arrives

Carbon can build, test, and debug full-stack applications, checking both the code and rendered UI. Google says it performs particularly well on multi-package migrations and debugging across subsystems.

What Google hasn’t explained is how `/swarm` shares context between agents, handles conflicting changes, or decides which tasks need Carbon instead of a lighter model.

Google claims Carbon ranks first on CursorBench 4.0, Perplexity’s WANDR and Zapier’s AutomationBench, completing tasks at less than half the cost of the next-best model.

> What Google hasn’t explained is how /swarm shares context between agents, handles conflicting changes, or decides which tasks need Carbon instead of a lighter model.

## Pricing doubles November 30

The company hasn’t provided enough detail to independently verify those cost comparisons. Carbon launches at $2 per million input tokens and $10 per million output tokens, matching Argon, before doubling to $4 and $20 after November 30.

Whether Carbon’s performance offsets those higher costs, including the overhead of multi-agent orchestration and verification, remains to be seen in production.

## Proving Signal’s code

One of the more technically ambitious examples in Google’s announcement involves AlphaProof Code, a new agentic framework for formal verification.

Google researchers used Carbon alongside other models to mathematically prove key security properties of the code underlying Signal’s cryptographic protocol.

The researchers translated security requirements into mathematical theorems and used AlphaProof Code agents to generate millions of lines of [Lean](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/), a language used to express and check mathematical proofs.

Google says the work took weeks, compared with the years that similar verification efforts have historically required from expert teams.

The announcement doesn’t specify the full scope of the verified properties, how much human intervention it required, or whether Google will make the proof artifacts publicly available.

> Google says the work took weeks, compared with the years that similar verification efforts have historically required from expert teams.

## Security that cuts both ways

Google initially made Carbon’s cybersecurity capabilities available to selected defenders through its [Fairwind Program](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) in late October.

The company says Carbon leads on SEC-bench Pro, ExploitGym and CWE-bench v1, benchmarks covering vulnerability discovery, exploitation and patching.

In Project Fortify, Google’s autonomous scanning, triage and remediation system, Carbon achieved 100% scanning recall and 95% triage precision on an internal benchmark. Google also reports a relative improvement of more than 25% over Argon’s recall rate when testing open-source repositories.

Google’s Cloud Vulnerability Research team used Carbon to confirm that two bugs in a popular open-source project could be exploited, prompting maintainers to classify them as critical and release patches. Google says the vulnerabilities were comparable in severity to the recent [PHP2Shell exploit](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/), but hasn’t named the affected project while the disclosure process is still underway.

Separately, Wiz used Carbon through its Scan for Good program to uncover zero-day vulnerabilities in two major SaaS providers in under two hours. The affected organizations worked with the researchers on remediation.

## Cybersecurity’s double edge

The stronger exploitation capabilities also raise misuse concerns. Google says Carbon’s safeguards blocked 99% of attack trajectories attempted by an adaptive red-teaming agent in simulated environments, reducing the per-attempt breach rate to 0.8%, compared with 3.1% for Argon.

The company also reports a 0% attack success rate on Gray Swan’s indirect prompt-injection benchmark, while acknowledging that more sophisticated attacks remain an area for improvement.

These results come from specific evaluation environments and don’t establish that Carbon is resistant to all real-world attacks.

> These results come from specific evaluation environments and don’t establish that Carbon is resistant to all real-world attacks.

## Getting access to Carbon

Gemini 4 Carbon is available through the paid Gemini API tier in Google AI Studio and Android Studio, as well as Google’s enterprise offerings.

Google AI Ultra subscribers can access Carbon through Antigravity, the Gemini app, and AI Mode in Search. The /swarm orchestration feature remains in preview.

Access to Carbon’s advanced cybersecurity tools still requires approval through Fairwind. Google is also giving selected scientists six months of free access to Carbon through Antigravity, with applications open and new researchers added each week.

Google has published an updated [Gemini 4 developer guide](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) covering migration and implementation.

The post [Google says Gemini 4 Carbon proved Signal’s encryption in weeks](https://thenewstack.io/gemini-4-carbon-swarm/) appeared first on [The New Stack](https://thenewstack.io).