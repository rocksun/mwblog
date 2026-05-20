Six months after its initial launch, Google is moving [Antigravity](https://antigravity.google/) beyond its origins as a coding environment. The company is repositioning it as a platform for developing and managing teams of [autonomous AI agents](https://thenewstack.io/why-apis-are-the-missing-link-for-truly-autonomous-ai-agents/) — and backing the expansion with a new desktop application, a [CLI](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/), an [SDK](https://thenewstack.io/openai-agents-sdk-sandboxes/), and [enterprise cloud integration](https://thenewstack.io/cloud-native/).

“We are expanding Antigravity beyond a coding environment and turning it into a platform to develop and manage teams of autonomous AI agents,” said [Koray Kavukcuoglu](https://www.linkedin.com/in/koray-kavukcuoglu-0439a720/), CTO of Google DeepMind and Chief AI Architect at Google, during a press briefing this week ahead of [Google I/O 2026](https://io.google/2026/). The company says millions of developers are already building with the platform.

> “We are expanding Antigravity beyond a coding environment and turning it into a platform to develop and manage teams of autonomous AI agents.”

“Google Antigravity is our agent-first development platform for developers to take an idea and turn it into a production-ready app,” writes [Varun Mohan](https://www.linkedin.com/in/varunkmohan/), Director, Software Engineering, Google DeepMind, and [Logan Kilpatrick](https://www.linkedin.com/in/logankilpatrick/), Member of the Technical Staff, Google DeepMind, in a [blog post](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/). “Today, we’re expanding the Antigravity ecosystem to manage and deploy agents that can integrate across key developer surfaces.”

## A platform in three new forms

The centerpiece of the announcement is Antigravity 2.0, a standalone desktop application that serves as a central hub for agent orchestration. Rather than running a single agent on a single task, developers can coordinate multiple agents working simultaneously — one generating code, another producing brand assets, and a third handling product architecture planning.

For developers who prefer to stay in the terminal, Google is introducing the Antigravity CLI, a lightweight interface for spinning up agents without a graphical environment. Existing Gemini CLI users are being encouraged to migrate.

Rounding out the expansion is the Antigravity SDK, which provides developers with programmatic access to the same agent harness that powers Google’s internal products. The SDK is co-optimized for Gemini models, specifically Gemini 3.5 Flash, which Google says was co-developed alongside Antigravity 2.0 as the platform’s primary workhorse model. Google says it outperforms Gemini 3.1 Pro on almost all benchmarks and runs four times faster than competing frontier models.

Managed Agents in the Gemini API extend the platform into the cloud. A single API call can now spin up a full agent that reasons, uses tools, and executes code inside a persistent, isolated [Linux](https://thenewstack.io/introduction-to-linux-operating-system) environment. State and files persist across follow-up calls, enabling multi-turn sessions without re-initialization.

The enterprise angle is addressed through Antigravity’s integration with the Gemini Enterprise Agent Platform, enabling Google Cloud customers to connect directly to their Cloud projects. A new [$100-per-month Google AI Ultra subscription tier](https://thenewstack.io/google-ai-ultra-pricing/) offers 5x higher usage limits in Antigravity than the existing Pro plan, the company says.

![](https://cdn.thenewstack.io/media/2026/05/f1f7885d-52bde528-8ce8-4a0b-b219-9861b032b6a5-1024x768.jpg)

Credit: *The New Stack*

Early enterprise adopters offered validation in the announcements. [Nikunj Shanti](https://app.aviation-festival.com/event/aviation-festival-asia-2025/person/RXZlbnRQZW9wbGVfMzYyODczNjQ=), CTO of AirAsia Next, said more than half of the company’s production-ready code is now generated through Antigravity agentic workflows.

[Faruk Muratovic](https://www.linkedin.com/in/farukmuratovic/), US AI and Engineering Strategy and Services Leader at Deloitte, cited the platform’s ability to run governed, autonomous engineering workflows that meet Deloitte’s enterprise security standards. PwC Advisory CTIO [Vikas Agarwal](https://www.linkedin.com/in/vikas-agarwal-b5528a2/) described the shift as moving “past simple AI code completion to true agent orchestration.”

“WPP has integrated Antigravity into WPP Open, our agentic marketing platform to supplement our product development lifecycle,” said [Callum Anderson](Callum%20Anderson), Head of Engineering, WPP, in a statement. “Leveraging the power of Gemini, it has streamlined workflows, automated repetitive tasks and empowered engineering teams to deliver high-quality solutions for our clients, faster.”

Meanwhile, another key announcement addresses a problem Google itself helped create — as agents write more code, that code needs to be secured at the same speed and scale it’s being produced.

Google added new capabilities to its [CodeMender](https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/) — an [AI code security agent](https://thenewstack.io/ai-security-agents-combat-ai-generated-code-risks/) developed by Google DeepMind that goes beyond finding vulnerabilities to actually patching them.

“CodeMender is an AI code security agent, originally developed by Google DeepMind. Leveraging Agent Platform capabilities and advanced Gemini models, CodeMender autonomously identifies vulnerabilities within your code,” writes [Thomas Kurian](https://www.linkedin.com/in/thomas-kurian-469b6219/), CEO of Google Cloud, in a [blog post](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud).

“It then recommends precise fixes, securely tests them, and can apply patches and necessary changes across dependent systems, with your approval. This entire process automates secure deployment while ensuring your developers retain control.”

Using the advanced reasoning capabilities of Gemini models, it autonomously identifies critical code flaws, recommends precise fixes, tests them in a secure environment, and applies patches across dependent systems — with developer approval at each step.

> “It shows how AI can actually patch code, not just find exploits.”

“It shows how AI can actually patch code, not just find exploits,” Kavukcuoglu said.

CodeMender is being integrated into Google’s Agent Platform as part of its AI Threat Defense offering. A select group of security experts is being invited to test a CodeMender API now, with broader availability to follow.

The tool puts Google in a market segment that has seen considerable startup activity. Autonomous vulnerability remediation — not detection, remediation — has emerged as one of the more contested spaces in enterprise security, with players such as [Aikido Security](https://thenewstack.io/aikido-self-securing-software/) and [Mobb](https://thenewstack.io/ai-coding-tools-create-more-bugs-than-they-fix/) already offering variations on the AI-driven patching model. CodeMender is Google DeepMind’s entry into that field, backed by Gemini’s reasoning capabilities and native integration into the Agent Platform infrastructure.

Google also announced an AI Content Detection API rolling out today on Agent Platform, enabling businesses to identify AI-generated content from both Google and third-party models — an acknowledgment that synthetic media governance is becoming a platform-level concern alongside code security.

## What it means

Taken together, the Antigravity expansion and CodeMender news represent Google’s clearest statement yet about where it sees developer infrastructure heading: away from single-turn prompts and toward persistent, collaborative, always-on agent systems.

“The leap from single-turn prompts to collaborative, always-on agents changes how developers build software,” Kavukcuoglu said.

The company is simultaneously building the tooling for agents to write code at scale and the security infrastructure to govern what those agents produce. That’s a pairing of agentic development with agentic remediation for enterprises.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)