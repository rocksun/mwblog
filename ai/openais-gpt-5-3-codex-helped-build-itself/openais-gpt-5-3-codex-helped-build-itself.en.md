OpenAI’s new [GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/) model is the company’s most capable agentic coding model yet. However, unlike previous Codex models, it focuses not only on coding.

With this model, which OpenAI made available on Thursday to its paid users across Codex-powered tools and APIs, the company has set a new goal: to create an agent that can write code and do everything else developers or any professional would do on a computer.

OpenAI says that “the model advances both the frontier coding performance of GPT-5.2-Codex and the reasoning and professional knowledge capabilities of GPT-5.2, together in one model, which is also 25% faster.”

There’s another aspect in which building this model differed from previous efforts: according to OpenAI, the model was “instrumental in creating itself.” The team says it used an early version of the model to debug training runs, manage the model’s deployment, and analyze test results and evaluations.

According to OpenAI, building this model was especially challenging because it combines these coding and general agentic capabilities, which made training and deployment difficult.

That’s where Codex itself came in. “The engineering team used Codex to optimize and adapt the harness for GPT-5.3-Codex,” the team writes in the announcement. “When we started seeing strange edge cases impacting users, team members used Codex to identify context rendering bugs and root cause low cache hit rates. GPT-5.3-Codex is continuing to help the team throughout the launch by dynamically scaling GPU clusters to adjust to traffic surges and keeping latency stable.”

That’s only a first step in having these models build and improve themselves. Yet, just as we’ve seen a speed-up in feature launches for agentic coding tools because developers now use those same tools to make them, we’ll likely see more of this from models from frontier labs.

## GPT-5.3-Codex benchmarks

Unsurprisingly, the new model performs well on coding benchmarks, but in today’s announcement, OpenAI rightly downplays them and focuses more on the practical advances these improvements bring. The company notes that the new model can now build complex games and apps from scratch over the course of days. OpenAI also stresses that the model better understands the user’s intent and chooses more sensible defaults when there is ambiguity.

OpenAI is also emphasizing the new model’s ability to handle cybersecurity tasks, in part because it’s the first model the company has directly trained to identify vulnerabilities. But that also means it should be pretty good at exploiting security issues, something OpenAI acknowledges: “While we don’t have definitive evidence it can automate cyber attacks end-to-end, we’re taking a precautionary approach and deploying our most comprehensive cybersecurity safety stack to date. Our mitigations include safety training, automated monitoring, trusted access for advanced capabilities, and enforcement pipelines including threat intelligence.”  
![](https://cdn.thenewstack.io/media/2026/02/1016db44-screenshot-2026-02-05-at-10.09.05-am.png)

To compare models, benchmarks still matter, though, and the new model does quite well there. Across the board, it delivers leading scores, including on TerminalBench 2.0, which tests the models’ agentic coding skills, as well as SWE-bench Verified (which tests the models’ Python skills) and SWE-Bench Pro (which tests across four programming languages).

With scores of 77.3% on TerminalBench 2.0, it easily beats Anthropic’s [just-launched Opus 4.6 model](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/).

![](https://cdn.thenewstack.io/media/2026/02/5c6a3c76-terminal-bench-2.0.png)

But since OpenAI specifically notes that this model isn’t just about coding, it’s especially noteworthy that on the [OSWorld-Verified benchmark](https://os-world.github.io/), which tests agents on open-ended tasks in real computer environments, it scores  64.7% here.

In its announcement, the OpenAI team argues that, “together, these results across coding, frontend, and computer-use and real-world tasks show that GPT‑5.3-Codex isn’t just better at individual tasks, but marks a step change toward a single, general-purpose agent that can reason, build, and execute across the full spectrum of real-world technical work.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)