Most AI systems interact with software through structured pathways — APIs, code repositories, or tightly defined tool integrations. That setup works when systems are designed for automation, but much of the software people rely on every day isn’t. Internal dashboards, legacy tools, and web apps often require manual navigation, with no clean way for AI to plug in.

That limitation is stoking interest in a different approach: letting models operate software through the interface itself. So instead of calling functions, they click, type, and move through applications much like a human would. The approach, often referred to as “computer use,” builds on ideas long used in robotic process automation ([RPA](https://thenewstack.io/true-success-in-process-automation-requires-microservices/)), but with models now handling the decision-making rather than fixed scripts.

Hugging Face is the latest to test that shift with [HoloTab](https://chromewebstore.google.com/detail/holotab/hlaoiikljjgcjdhkakedfngifaopbcop?pli=1), a Chrome extension designed to run an agent directly inside the browser. The tool can navigate websites, perform actions, and repeat tasks without relying on site-specific integrations.

[Announced Wednesday](https://huggingface.co/blog/Hcompany/holotab), HoloTab is built on Hugging Face’s recently released [Holo3-35B-A3B](https://huggingface.co/Hcompany/Holo3-35B-A3B) model, which the company describes as “[breaking the computer use frontier](https://huggingface.co/blog/Hcompany/holo3)” owing to its claimed performance on the [OSWorld-Verified](https://os-world.github.io/) benchmark, a public test of multi-step software interaction tasks.

> “HoloTab is a Chrome extension that navigates the web just like a person would.” — Hugging Face

## Agents without integrations

Most agent-style systems depend on predefined connections. A model might query a database, trigger an API, or generate code to be executed elsewhere. Those approaches rely on predictable inputs and outputs, which makes them easier to manage but limits where they can be applied.

Computer use takes a different route. Rather than waiting for software to expose functionality, it works with whatever is available on screen. That includes clicking through menus, filling out forms, and moving between tabs or applications.

Recent developments at Anthropic point in a similar direction. Its Claude Code system has been [extended to operate across a user’s machine](https://thenewstack.io/claude-computer-use/), controlling mouse and keyboard inputs and carrying out tasks across files and applications. The company has also introduced features that allow those sessions to [persist and be accessed remotely](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/), part of a broader move toward longer-running agents that can continue working beyond a single interaction.

So, for example, a developer might ask Claude to run a mobile app in a simulator, work through a desktop tool that has no command-line access, or carry out a task that only exists behind a graphical interface, with the system handling those interactions directly on the machine while the developer checks in remotely as the task runs.

Anthropic actually [introduced computer use back in 2024](https://www.anthropic.com/news/3-5-models-and-computer-use) as part of its Claude 3.5 updates, where the focus was on giving developers access to a model that could interpret a screen and act through a control loop. That earlier version required more setup and was largely confined to API-based experiments. Its recent efforts shift that into more of a product setting, with desktop apps and the ability to check in on tasks remotely, making the same underlying capability easier to use in day-to-day work.

HoloTab, for what it’s worth, takes a different approach, operating inside the browser rather than across the full desktop, but it builds on the same idea. Instead of requiring integrations, it works directly against live websites, allowing users to hand off tasks such as reviewing and replying to messages, filling out forms, or even researching people online and initiating outreach on platforms like LinkedIn.

![Computer use to network professionally](https://cdn.thenewstack.io/media/2026/04/5f3d8bca-gif1.gif)

***Computer use to network professionally***

## Computer use coming of age?

With Hugging Face pushing further into browser-based agents, Anthropic continuing to expand its desktop-level capabilities, and Google introducing a [computer use model within its Gemini family](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/), it’s clear that AI systems are being designed to operate software directly, without relying on integrations.

Many business processes involve stitching together multiple tools that don’t communicate cleanly. If an agent can operate those tools directly, it opens up a broader range of tasks that can be automated without rebuilding the underlying systems.

That approach sits alongside a separate push to standardise how AI connects to software. Anthropic’s [Model Context Protocol](https://thenewstack.io/model-context-protocol-roadmap-2026/) (MCP), for example, is designed to give models structured access to tools through defined interfaces. Where MCP depends on services exposing those interfaces, computer use sidesteps the requirement altogether by working directly against the UI. The two approaches reflect different bets: one on adapting software for AI, the other on adapting AI to existing software.

For Hugging Face, HoloTab serves as a proving ground for that latter approach, showing how its Holo3 model can be used to navigate live websites and carry out tasks without integrations.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)