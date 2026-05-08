Growing and emerging software toolsets and standards are prone to love-it-or-hate-it reactions. [Bun](https://bun.com/), an all-in-one JavaScript, TypeScript & JSX runtime and toolkit, has divided a few taste buds among developers.

Apparently named after the [bao variant](https://x.com/bunjavascript) rather than the [burger variety](https://theeburgerdude.com/wp-content/uploads/2023/05/Burger-Blog-01-1-1024x1024.jpg), Bun v0.1.0 arrived in July of 2022 and was designed to act as a drop-in replacement for [Node.js](http://node.js), the widely popular cross-platform JavaScript runtime environment.

## Anthropic acquisition

Created by [Jarred Sumner](https://www.linkedin.com/in/jarred-sumner-a8772425/), Anthropic [acquired](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone) Bun in December 2025 to accelerate Claude Code capabilities and act as a combined runtime, package manager, bundler, and test runner. Anthropic has called Bun “essential infrastructure for AI-led software engineering.” It also defines it as a tool that helps developers build and test applications at unprecedented velocity.

As a software developer and CEO of monetization platform [Meteroid](https://www.meteroid.com/), [Gaspard Boursin](https://www.linkedin.com/in/gboursin/) writes in a [dev.to blog post](https://dev.to/meteroid/anthropic-just-bought-bunjs-heres-why-6bh) published on the day of the acquisition, “Claude Code ships as a Bun executable. When you install Claude Code, you’re running Bun. This isn’t a loose partnership, but a dependency.”

## Python slides slower

According to [Boris Cherney](https://www.linkedin.com/in/bcherny/), head of Claude Code at Anthropic, Bun is all about fast startup times that deliver a millisecond advantage to developer-level AI tools.

“When we started Claude Code, we looked at a bunch of options for runtime; Bun was the winner hands down,” Cherney says in a testimonial video on the Bun homepage. It starts in, like, three milliseconds, and Python was, like, 15 times slower. So for a CLI tool, that’s the difference between an awesome user experience and something that feels sluggish.”

On the face of it, then, Bun sounds tasty enough, so what’s the beef with this bread?

> “Bun has grown to be very complex and without these fixes I doubt it will ever gain as much production-grade maturity as Node.js.” – Xtergo.

## Excessive memory usage

Perhaps typical of a tool built to be amazing, but at whatever cost to base-level resources, developers have complained of excessive memory usage with Bun. Although Bun v1.1.13 [was touted as using 5% less memory](https://x.com/bunjavascript/status/2043841758891741506) when it arrived on April 20 last month, not everyone is happy.

[Reddit user Xtergo](https://old.reddit.com/r/bun/comments/1snjxyf/bun_is_not_stable_enough_for_production_nor/) bemoans Bun’s memory leaks and more besides in a post they admittedly labeled as a “crude investigation” into the issue.

“Any runtime that is new will have real maturity problems that will be ironed out with time, but I am concerned that Buns’ development roadmap looks more like adding features on top of features while ignoring stability issues & bug fixes,” writes Xtergo. “Bun has grown to be very complex, and without these fixes, I doubt it will ever gain as much production-grade maturity as Node.js.”

## Open feature issues

Another concern is open issues, i.e., unresolved bugs, open feature requests, or items or tasks in a software codebase’s project tracking system awaiting action.

According to [Wojciech Maj](https://www.linkedin.com/in/wojtekmaj/?locale=en), chief technical officer at Polish digital loyalty software services company Rewardo, Node.js (as the runtime powering practically the entire planet, including your toothbrush, probably) carries about 1.7k open issues.

“Bun, much younger and — while popular — considerably far less adopted, has around 4.7k, [open issues]” [states Maj](https://dev.to/wojtekmaj/why-using-bun-in-production-maybe-isnt-the-best-idea-3deb), in a blog post. “Raw numbers are never telling us the full story, but the imbalance is striking. Node.js shoulders a global workload and yet manages a far leaner backlog. Bun, still in its infancy, is already swamped.

## Bun is embedded in Claude Code

Software developer and head of technical marketing at Redis, [William Johnston](https://www.linkedin.com/in/wwjdev/), [blogs independently](https://wwj.dev/posts/i-am-worried-about-bun/), had this to say last week: He thinks Bun is great software. This is primarily because he finds it fast and practical, and Bun the team ships constantly. For Johnston, TypeScript is “a joy to work with” in small scripts, apps, tests, and tooling.

But he states, “Bun is embedded in Claude Code. Claude Code appears to be \*expletive\*. So now I have to worry that Bun could \*expletive\* too. Not because Bun is bad. Bun is not bad. Bun is excellent. Not because the Bun team stopped caring. I do not believe that.”

The problem for Johnston is that, as Bun and its team get further integrated into Anthropic, so will its policies.

“The same policies that have led to the collapse of Claude Code. Will we see issues start popping up in Bun that make it seem like the team doesn’t even dogfood their own product? I don’t know, but I’m not sure I want to continue using it just in case,” writes Johnston.

## Happy Bun users

While other developers have complained about this technology’s garbage collection capabilities (again, essentially a memory management issue) and Bun’s perceived [lack of Windows support](https://chyshkala.com/blog/the-bun-story), it’s important to remember that there are a whole lot of quite [happy Bun](https://news.ycombinator.com/item?id=47713219) users out there as well.

The emotive debate around Bun likely stems from the importance of AI infrastructure services, the deeply entrenched, almost standardized technologies it aims to usurp, and the fact that it now plays a frontline role at Claude Code alongside Anthropic. If that’s enough to bring out a few naysayers, then nothing is.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)