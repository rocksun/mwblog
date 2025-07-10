Between companies increasingly using [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) in their development process, such as Microsoft [writing up to 30%](https://techcrunch.com/2025/04/29/microsoft-ceo-says-up-to-30-of-the-companys-code-was-written-by-ai) of its codebase using AI, and site reliability engineers (SREs) adopting [incident vibing](https://thenewstack.io/vibe-coding-is-here-but-are-you-ready-for-incident-vibing), it is clear that software practices are evolving.

Despite [model makers](https://www.inc.com/joe-procopio/anthropics-ceo-said-all-code-will-be-ai-generated-in-a-year/91163367?utm_source=chatgpt.com) pushing the narrative that fully autonomous AI development agents are coming very soon, the consensus remains that having a human in the loop is here to stay, at least for some time. So will AI fuel a developer renaissance?

## The Shift to Multi-Agent Workflows

I recently moderated a [Rootly AI Labs](https://labs.rootly.ai/) [panel](https://lu.ma/ki58hev3) on the topic. [Solomon Hykes](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/), CEO of [Dagger](https://dagger.io/) and founder of [Docker](https://www.docker.com/?utm_content=inline+mention), argued that while the industry has been busy figuring out single-agent approaches, multi-agent setups represent the next frontier.

For example, the startup [Factory](https://www.factory.ai/) introduced “Droids,” software agents designed to handle parallel development tasks. One agent could manage code refactoring, while another could conduct a code review, and yet another could handle the task backlog on [Linear](https://thenewstack.io/anti-agile-project-tracker-linear-the-latest-to-take-on-jira/), prioritizing and assigning tickets.

These setups shift a developer’s role from direct technical tasks to managing and verifying the work of these agents, turning [developers into engineering managers](https://thenewstack.io/ai-will-steal-developer-jobs-but-not-how-you-think/).

Anthropic recently released a [blueprint](https://www.anthropic.com/engineering/built-multi-agent-research-system) on building multi-agent systems, based on lessons from its Research feature, which coordinates multiple Claude agents to explore complex topics.

The report highlights that in agentic systems, small issues that would be minor in traditional software can compound and derail workflows entirely, making the gap between prototype and production wider than expected.

Getting multi-agent systems to work reliably turns the “last mile” into most of the journey, and developers are the ones responsible for making it happen.

## Developer Roles Are Expanding

As developers transition into managing teams of AI agents, their roles naturally broaden beyond purely technical tasks. [Malika Aubakirova](https://www.linkedin.com/in/malika-aubakirova-54759984/), partner on the AI infrastructure team at [Andreessen Horowitz](https://a16z.com/), highlighted the rise of nano unicorns; fast-growing, high-revenue startups with small teams, like [Cursor](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/), which reached [$300M ARR with just 20 employees](https://www.fastcompany.com/91322491/ai-coding-tools-could-bring-us-the-one-employee-unicorn).

She noticed consistent patterns across these companies. First, they augment their teams with AI agents across engineering, product development and customer-facing functions. In this model, AI isn’t a side tool; it’s treated as infrastructure and is central to how work gets done.

Second, these startups frequently employ generalists rather than specialists. For example, in such environments, engineers aren’t limited to backend or frontend tasks; they would contribute across the entire application life cycle and even assist with go-to-market initiatives.  This shift is redefining team structures, tooling and what it means to scale a modern software company.

![Panel discussion at AWS Builder Loft on the future of developers in the AI era.](https://cdn.thenewstack.io/media/2025/06/332ff6e2-unnamed-1-1024x683.jpg)

A panel discussion at AWS Builder Loft on the future of developers in the AI era.

This trend isn’t limited to startups; it’s also playing out inside large, established tech companies. A senior engineering leader at [LinkedIn](https://thenewstack.io/5-lessons-from-linkedins-first-foray-into-genai-development/), who asked to remain anonymous, noted that role expectations have significantly expanded. Engineers are now expected to operate across multiple functions, acting not just as developers but also as project managers, data scientists, and SREs, while leveraging AI agents to execute across these domains.

While the actual usefulness of LLMs is still debated, one thing is certain: engineers are being asked to do more with less.

## Challenges for Reliability and SRE Teams

Despite the productivity boosts from AI agents, their adoption poses reliability challenges. [Kevin Van Gundy](https://www.linkedin.com/in/kevinvangundy/), CEO at [Hypermode](http://hypermode.com) and former COO at Vercel, emphasizes that the [non-deterministic nature of LLMs](https://rootly.com/humans-of-reliability/kaspar-von-grunberg#the-limits-of-llms-for-reliability-and-automation), which can produce hallucinations, is causing very unusual incidents. Handling incidents in deterministic systems was already complex; now imagine doing it when the system itself can’t be trusted to behave the same way twice.

Hykes noted that as LLMs become embedded at every stage of the software development life cycle, from authoring application code and creating other agents, to running tests, provisioning infrastructure and handling monitoring, the number of places where things can go wrong is increasing.

SREs, as the last line of defense between sanity and chaos, may need to be concerned about the [volume and complexity of incidents](https://leaddev.com/software-quality/ai-assisted-coding-incident-magnet) heading their way. The good news, however, is that they’ll also become more sought-after talent, and platform teams, more specifically, will hold the keys to providing the infrastructure for these agentic workflows at scale.

## Navigating the AI-Driven Market: Skills for Developers

So, what should engineers do to stay up to date? Van Gundy encourages engineers to keep building using the latest and hottest tools, such as [Replit](https://replit.com/) and [Lovable](https://lovable.dev/). The focus should be on expanding beyond purely technical skills and developing strong product intuition and UX expertise. Rapid development capabilities alone won’t guarantee success without a polished product.

Conversely, [Mike Chambers](https://www.linkedin.com/in/mikegchambers), specialist developer advocate for machine learning at [Amazon Web Services,](https://aws.amazon.com/?utm_content=inline+mention) recommends that developers have a deep understanding of the underlying technology behind LLMs. Learning foundational AI concepts, such as transformers, can significantly improve engineers’ effectiveness when leveraging these tools. Like any other system, LLMs have strengths and weaknesses, and you shouldn’t use a hammer for a screw.

## The Developer Renaissance Is Underway

The panel consensus was that LLMs indeed offer a potential renaissance for developers by significantly expanding their roles. Success in this new era will likely be highly based on blending human oversight with AI capabilities, balancing technical depth with product sensibility.

In the future, engineers’ performance reviews may focus less on individual execution and more on how effectively engineers manage and direct their agent workforce.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d18c6a77-cropped-5b2d8eb1-sylvain-kalache-768x768-1.jpeg)

Sylvain Kalache is a tech entrepreneur and software engineer. As Head of AI Labs at Rootly, he oversees developer relations and AI initiatives. He previously founded a software engineering school whose graduates were hired by organizations such as Apple, Google,...

Read more from Sylvain Kalache](https://thenewstack.io/author/sylvainkalache/)