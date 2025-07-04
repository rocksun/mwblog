After selling his project management startup [Wrike](https://www.wrike.com/) to a private equity firm and then Citrix, the company’s co-founder and CEO, [Andrew Filev](https://www.linkedin.com/in/filev/), stuck around for a few years before leaving in late 2023 to found a new startup: For Good AI. The company’s mission was to combine frontier AI research with hands-on R&D “to create solutions that safely harness AI’s power.” Filev, however, quickly realized that a small startup wasn’t going to compete with the likes of Anthropic, OpenAI and Google on fundamental research.

The company’s inaugural product, AI coding platform Zencoder.ai, however, quickly found a niche in the market for [enterprise-ready AI coding tools](https://thenewstack.io/your-ai-coding-buddy-is-always-available-at-2-am/). Like [so many other coding tools today](http://anthropic.com/partners/powered-by-claude), Filev ended up using Anthropic’s Claude models at the core of its product.

“Two decades ago, my thesis at school was around automated refactoring, but more importantly, as a product guy at heart, I would say only about 5% of my ideas were ever implemented, even when I was running the company as a CEOm so I’ve always wanted to move faster, And that’s still still the case,” Filev told me when I asked him about how Zencoder came to be. “When running that large team, I saw how much of it was routine work. And you cannot say it’s not important work, right? But it is routine work. For example, at Wrike, we had about 30,000 automated tests. And you can imagine that writing the first one is a hard job, writing the 30,001st is a little bit easier.”

[![](https://cdn.thenewstack.io/media/2025/07/b87dda1e-zen-agents-features.png)](https://cdn.thenewstack.io/media/2025/07/b87dda1e-zen-agents-features.png)

Image credit: Zencoder.

In an enterprise setting, he noted, coding is just a small part of the developer’s job, but many of the other day-to-day processes are just as routine and ripe for automation. As he was looking at the space when he was thinking about starting something new, it was still popular among startups to buy their own GPUs and try to “play the frontier model game,” as he put it.

“I thought that there was already Anthropic and other players, so I didn’t feel that that was a good area for me to focus on, but from day one — and ‘agents’ was not as popular word as it is today — it was very obvious that this was where you needed to take the  LLMs,” Filev explained.

What those agents needed, Filev noted, was access to the right context, because every code repository is different, and a feedback loop to verify the results. Verification, he said, is what defines the reliability of the AI. “If, with a flip of a coin, I can solve an issue for you half of the time, that’s unreliable. But if I can solve the issue the same 50% of the time, but I can tell you when I solved it and when I don’t, now I just saved you half of your work,” he explained.

Traditionally, models from the same family weren’t very good at critiquing each other, but Filev noted that with the latest generation of models, and specifically Anthropic’s Claude Sonnet 4 and Opus 4, they’ve gotten much better at this.

With that focus, Zencoder launched a code completion product that used its first [agentic pipelines](https://zencoder.ai/product/agentic-pipeline) to check the syntax of its code. From there, the company started launching more agents that could handle an increasing number of coding tasks like its unit testing agent, code review agent and, most recently, custom agents that development teams can modify to solve their specific problems.

He also noted that in the early days of modern LLMs, many people thought that it would be best to train them to be great at everything.

[![](https://cdn.thenewstack.io/media/2025/07/0fb70efc-unit20testing20-2016_920-20dark-1.webp)](https://cdn.thenewstack.io/media/2025/07/0fb70efc-unit20testing20-2016_920-20dark-1.webp)

Image credit: Zencoder.

“People thought that transformers could offer an all-encompassing understanding of the universe, where, in reality, instead of teaching them to be a calculator, you give them a calculator,” he said.

With the launch of models like Anthropic’s Claude 3.5, tool calling became a real option and then with the launch of the Model Context Protocol, the industry got a de facto standard for doing so. Filev argues that there are still scenarios where developers have to write their own integrations for calling tools, especially when it comes to user interface interactions, but he also believes that the next area of development will be in agent-to-agent interactions. And while some people may argue that calling another agent isn’t all that different from calling another tool, Filev doesn’t buy it because there are different challenges in orchestrating these agent crews.

Filev also noted that model benchmarks have become increasingly removed from the reality of using them. Once they clear a certain benchmark, he said, it’s not about solving abstract math Olympiad questions anymore but about solving real-world problems. A model that may be good at vibe coding and building a simple game in Python may not be able to refactor a messy Java codebase, after all.

Because of this, Zencoder tends to build its own evaluation tools and often partners with customers to benchmark how well new models work for them.

One area where Zencoder sharply diverges from other coding agents is that it is IDE agnostic, while others like Cursor and Windsurf forked the VS Code IDE to build their agents right into the IDE.

“As you move from that kind of second generation of products that are all the rage today, working in the IDE, to the third generation that’s coming, that’s where we started building the lead and more differences. We took those agents that you use every day in your IDE, and the first thing we did was we allowed you to package them and share them across your organization, which is helpful for adoption,” Filev said.

Adoption, he argues, is still in its early days, especially in the enterprise. While some developers may be all-in and may be writing their custom instructions for agents, many employees are barely scratching the surface and mostly think of AI as code completion.

Since Zencoder allows users to build their own agents, the company also launched a directory where developers can share their agents.

[![](https://cdn.thenewstack.io/media/2025/07/0a6d1fa0-img_0962-scaled.jpg)](https://cdn.thenewstack.io/media/2025/07/0a6d1fa0-img_0962-scaled.jpg)

Image credit: The New Stack.

Most recently, Zencoder itself launched [Zentester](https://zencoder.ai/product/zentester), its tool for testing anything from the user interface to a service’s APIs. Again, the company bet on the Claude models here. “Anthropic seeded the market with its computer use model last year, and that was exciting, because it was next-level compared to previous attempts in terms of operating GUI and web interface,” Filev said. And while those models weren’t originally meant to help services like Zencoder test user interfaces, it turns out that they are quite good at that, given their focus on navigating apps.

“That ability to test that code is extremely important, because if we’re going to ship 10 times more code, that means we’re going to test 10 times more code —  and that’s the only way to production code. And so that pairing of coding and testing, I think it’s, it’s awesome: peanut butter and bread.”

For quite a while now, the models have gotten better at coding with every generation. [Alex Albert](https://www.linkedin.com/in/alex-albert/), Anthropic’s head of developer relations, told me that it was around the launch of the Claude 3 models just over a year ago, where he saw Claude beat him on some coding tasks.

“Around [Claude] 3.7, we launched our own products in coding, and we started to see this take off too with our customers, as they were really turning the knob all the way up on the agentic coding side,” Albert said. “I think Zencoder is a great example of this, in that their entire product has abstracted away the IDE to some sense and it’s just really a coding agent. It very much aligns with the way we see coding moving in the future, as you are now kind of more coordinating these  software engineering agents operating on your code base, rather than having to go in and manually edit lines of code yourself.”

As for Anthropic competing with services like Zencoder itself, Filev said that he isn’t worried about that,e even as Anthropic’s [Claude Code](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/) coding agent is getting increasingly popular among developers.

“It’s been a really, really strong partnership, where we kind of enjoy the chances that Anthropic has given us — and of course, definitely the models themselves. One other kind of related consideration is that I feel that the bottom of this market rapidly commoditizes anyway, so the fact that there’s Claude Code doesn’t necessarily change the market dynamics for us,” he said.

Looking ahead, Filev believes that as the models get smarter, services like Zencoder will be able to build increasingly sophisticated agentic pipelines which will allow developers to get a cup of coffee while the agents work on a problem and return code that is verified, tested and reviewed.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)