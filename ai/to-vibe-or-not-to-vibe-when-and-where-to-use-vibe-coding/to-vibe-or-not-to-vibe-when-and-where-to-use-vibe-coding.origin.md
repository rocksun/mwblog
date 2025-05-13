# To Vibe or Not to Vibe? When and Where To Use Vibe Coding
![Featued image for: To Vibe or Not to Vibe? When and Where To Use Vibe Coding](https://cdn.thenewstack.io/media/2025/05/c2a4c0e7-andrej-lisakov-f5tv-e6v7-0-unsplashb-1024x576.jpg)
Vibe coding, a term coined [by Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383?) in February 2025, is the practice of steering AI models via natural language prompts to generate working code — shifting the developer’s role from typing to guiding and refining AI outputs. This approach massively reduces the need for in-depth coding knowledge and allows for rapid prototyping.

Sounds great, right? No longer will software engineers have to spend hours perfecting code! Instead, they can be conductors, guiding an orchestra of AI tools to create their dream projects. But just how true is that idea?

In this article, I’m going to take a look at the best use cases for vibe coding and examine scenarios where it might not be the best approach, so you’ll know whether to vibe or not to vibe.

## What Is Vibe Coding?
Vibe coding is a [programming process](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/) where, rather than crafting code for projects, developers describe what they’re looking to achieve in plain language, and then specialized large language models (LLMs) generate the corresponding code.

Unlike traditional line-by-line coding, vibe coding shifts the role of engineers and developers from craftspeople or builders to architects: you tell the LLM what you want, test what it produces, and then refine it, either yourself or by prompting the LLM further.

Common tools include [Cursor](https://dolthub.com/blog/2025-03-29-vibin/), [Windsurf](https://www.analyticsvidhya.com/blog/2025/03/vibe-coding-with-windsurf/), [Claude Code](https://www.infoworld.com/article/3853805/vibe-coding-with-claude-code.html), [Replit](https://www.deeplearning.ai/short-courses/vibe-coding-101-with-replit/) and [ChatGPT](https://medium.com/@niall.mcnulty/how-i-vibe-coded-a-micro-app-in-10-minutes-with-chatgpt-87db79fe5b4a).

## Finding Those Sweet Sweet Vibes: When Vibe Coding Works
Vibe coding is being tested in many different scenarios. Thus far, the following seem to be the best use cases for the process:

### Rapid Prototyping and Idea Testing
For founders and engineers racing to market, [vibe coding offers a frictionless way](https://www.businessinsider.com/developers-redefined-builders-ai-windsurf-ceo-varun-mohan-2025-5) to spin up minimum viable products (MVPs) and validate concepts in hours, not weeks. You can produce predominantly AI-generated codebases, built around prompts that allow you to iterate features on the fly. This approach aligns perfectly with [agile business and development principles](https://thenewstack.io/vibe-coding-is-here-how-ai-is-reshaping-the-software-developer-profession/): prompt away, tinker and pivot rapidly. It’s highly effective for hack-day demos, internal prototypes and investor pitches where speed is the priority over perfection.

### Small Projects and Low-Stakes Applications
When a personal website, browser game or one-off automation script is all you need, vibe coding delivers value by [eliminating boilerplate drudgery](https://spectrum.ieee.org/vibe-coding). Tasks such as generating small games, crafting utilities to automate tedious workflows or creating internal dashboards that require minimal oversight are perfect, especially when the worst possible outcome is just spending a few extra minutes manually debugging.

### Learning and Exploration
Coding beginners often face [steep learning curves](https://lifemichael.com/corporate/the-journey-through-the-learning-curve-of-programming/). Vibe coding flattens the curve by allowing learners to quickly see the impact of working code. There are [benefits for seasoned engineers](https://simonwillison.net/2025/Mar/19/vibe-coding/) as well: vibe coding can probe unfamiliar languages or frameworks, scaffold UIs or generate sample algorithms so they can deepen their understanding through exploration.

### Workflow Streamlining and Repetitive Tasks
In mature codebases, there are plenty of time-consuming repetitive tasks: refactoring naming conventions, adding logging, updating license headers, etc. Vibe coding can [automate these chores](https://dev.to/erikch/what-i-learned-vibe-coding-30em) across hundreds of files, saving hours of tedium and freeing engineers for high-impact work.

### Handling Design and UI Tweaks
Product managers and designers can leverage vibe coding to apply swift UI tweaks like adjusting padding, swapping color schemes or generating multiple layout variations — all without hunting through CSS files. This “[prompt-driven development](https://andrewships.substack.com/p/prompt-driven-development)” enables direct experimentation and rapid feedback loops.

### Fixing Bugs and Glitches (Sort Of…)
Pasting error messages into an LLM often yields immediate fixes, but [these can be superficial](https://blankslatedigital.co.uk/blog/artificial-intelligence/what-is-vibe-coding/). While vibe coding can resolve common syntax errors swiftly, deeper logical bugs still require human insight.

## Real-World Examples and Success Stories
There are a lot of people out there exploring use cases and applications for vibe coding. Here are just a few:

### Fly Pieter
Dutch entrepreneur Pieter Levels used Cursor and Claude 3.7 Sonnet to build a [3D browser-based flight simulator](https://avgeekery.com/new-flight-simulator-made-with-ai-earns-creator-5000-per-month/) with skyscrapers in under three hours, reportedly generating over $67,000 per month in revenue through Stripe microtransactions.

### Speech to App
Engineer Riley Brown [created a homepage and login page](https://www.youtube.com/watch?v=08TcHAeTJeU) in minutes by using vibe coding to combine different AI tools in order to create multimodal inputs (voice and image recognition).

### Airbnb Clone in Ten Minutes
Sully Omar, CEO of Cognosys, demonstrated live [how Cursor’s new agent and Whisper voice-to-text](https://x.com/SullyOmarr/status/1893757471799308321) could build a working Airbnb clone (complete with backend, UI and database) entirely through prompts and speech in ten minutes.

There are plenty more examples out there worth exploring!

## When the Vibe’s Just Off: When Vibe Coding Falls Short
But before you rush off and decide coding is just vibes now, let’s pause to discuss the scenarios where experienced developers doing traditional line-by-line coding is still the best way to go.

### Security-Sensitive Applications
Handling user credentials, payment information or personal data demands rigorous [security measures in applications](https://www.imperva.com/learn/application-security/application-security/). AI-generated code often [overlooks best practices](https://qwiet.ai/appsec-resources/risks-in-ai-generated-code-a-security-and-reliability-perspective/) like proper encryption, secure storage of API keys or correct CORS configurations. Blindly deploying vibe-coded authentication or payment flows could expose organizations to breaches and regulatory fines.

### Large-Scale Production Software
Enterprise systems and distributed microservices require carefully architected solutions, robust CI/CD pipelines and exhaustive testing. [Hallucinations and context-window limitations](https://devops.com/ai-generated-code-packages-can-lead-to-slopsquatting-threat/) make deep debugging across extensive codebases impractical. Vibe coding should never replace human-driven design for mission-critical infrastructure, where uptime and reliability are paramount.

### Compliance-Heavy Domains
Industries like finance, healthcare and government operate under strict regulations (HIPAA, GDPR, etc.). AI models can lack an awareness of nuanced legal requirements, making them ill-suited for [generating compliant code](https://www.jit.io/resources/devsecops/ai-generated-code-the-security-blind-spot-your-team-cant-ignore) for anything that requires conforming to strict regulations..

### When Originality or Deep Understanding Is Required
LLMs generate derivatives of existing patterns; they aren’t inventors. Complex algorithms, such as novel optimization routines or proprietary data-processing pipelines, [demand human ingenuity](https://conspicuous.com/conspicuous-blog/ai-vs-human-coders-comparative-analysis/). If your development projects are creating something utterly new, not replicating existing things, then vibe coding can fall short.

### Proprietary or Sensitive Code
You should [never feed private or proprietary resources](https://www.securityjourney.com/post/5-types-of-data-you-should-never-share-with-ai) to unsandboxed AI assistants. Especially code, as it could become part of an LLM’s training data. If you don’t have access to tools with [strict data-isolation guarantees](https://www.regie.ai/blog/generative-ai-data-privacy), then undisciplined vibe coding could be a liability for your IP.

## Best Practices for Effective Vibe Coding (When Appropriate)
It’s worth noting that many of the success stories from vibe coding experiments have come from experienced coders. Not only do they know what they’re looking to create and what’s possible with code, but they’re able to check for inconsistencies and hallucinations in the code. If you’ve never coded or are inexperienced, you can’t expect to immediately see results.

Whether you’re a coding n00b or a coding master, here’s some quick advice on how you can make the most out of experimenting with vibe coding:

**Have a plan:**Make sure you have an idea of what you want to produce, including the required features, rather than going in blindly. Vibe coding isn’t really a sandbox; it’s a path that can take you to an outcome. Outline features in a spec file before prompting your AI.**Provide context:**If you can supply configuration and rules files to guide the model, you’ll reduce the risk of the AI model going off-book and hallucinating.**Work iteratively:**Tackle features one at a time, keeping your prompts narrow and specific.**Test thoroughly:**You can use a combination of automated test generation via AI, along with manual/human verification of critical paths.**Choose popular stacks:**There are many guides online for using popular tools for vibe coding. Until you get more experience, it’s best to stick to these tools until you’re confident.**Review and refactor:**Always audit AI outputs line by line, then refactor for structure.**Monitor for rabbit holes:**AI can get stuck in a loop of generating code that’s ineffective. Don’t be afraid to roll things back and try different prompt approaches.**Try out multimodal inputs:**Screenshots can enhance prompt clarity, while using voice can be a fun experiment once you’re more experienced.**Check the vibe:**Get a seasoned engineer to review everything before sharing your code beyond prototypes.
## Vibing the Future
Over the next few years, vibe coding is poised to evolve from simple text prompts into more intuitive, drag‑and‑drop [“vibe designing” interfaces](https://andrewchen.substack.com/p/predictionsthoughts-on-vibe-coding): visual workflows where you sketch UIs or map data flows, and AI fills in the code behind the scenes.

As AI models grow more specialized and tightly integrated with business domains, we could see end‑to‑end pipelines that translate high‑level requirements into production‑ready applications.

For developers, this means [a fundamental role shift](https://www.nucamp.co/blog/vibe-coding-the-future-of-vibe-coding-how-aidriven-development-could-transform-programming-by-2030): rather than typing every line, they’ll be crafting precise prompts, curating generated outputs and embedding domain expertise to keep systems coherent. AI is projected to automate up to 80% of routine coding tasks by 2030, so engineers will focus on architecture, ethical oversight and cross‑team integration.

We could also see further applications of “vibing,” like [incident vibing](https://thenewstack.io/vibe-coding-is-here-but-are-you-ready-for-incident-vibing/).

## Conclusion
Vibe coding lowers the barrier to software creation. It’s a game-changer for rapid prototyping, personal projects and learning. However, it’s not a silver bullet: Deploying AI-generated code in security-critical, large-scale, or compliance-driven contexts invites significant risk.

The future requires a balanced approach that harnesses AI’s speed where it shines, but applies traditional engineering discipline where rigorous understanding and accountability are non-negotiable. Knowing when to embrace the vibe and when to grab your IDE is the key to thriving in the next phase of software development.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)