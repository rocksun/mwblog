The steady buildout of [vibe-coded applications](https://thenewstack.io/how-to-use-vibe-coding-safely-in-the-enterprise/) into production will lead to catastrophic problems for organizations that don’t properly review [AI-developed software](https://thenewstack.io/innovating-software-development-with-ai-and-ml-pros-and-cons/), a software security expert predicts.

[David Mytton](https://www.linkedin.com/in/davidmytton/), founder and CEO of developer security provider [Arcjet](https://arcjet.com/), writes in a [LinkedIn post](https://www.linkedin.com/posts/davidmytton_since-ive-spent-the-last-few-years-building-activity-7419405381766000640-p2Eu?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAFzCWcBM-zZEsHvACfWjv06uhghiLb7jeY): “In 2026, I expect more and more vibe-coded applications hitting production in a big way. That’s going to be great for velocity … but you’ve still got to pay attention. There’s going to be some big explosions coming!”

I asked what he meant by that, and Mytton adds that he expects to see lots of vibe-coded apps in production “everywhere,” which could be problematic.

“Developers are writing more code and deploying it faster without fully understanding what it’s doing,” Mytton tells *The New Stack*. “I agree with [Simon Willison’s prediction](https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/#1-year-a-challenger-disaster-for-coding-agent-security) that at some point we’re going to have ‘a [Challenger’ disaster](https://en.wikipedia.org/wiki/Space_Shuttle_Challenger_disaster). The root cause will be some core component written by AI that wasn’t properly understood or checked.”

[Willison](https://www.linkedin.com/in/simonwillison/) is a British programmer who is the co-creator of the [Django web framework](https://thenewstack.io/what-is-pythons-django/) and co-founder of the social conference directory [Lanyrd](https://en.wikipedia.org/wiki/Lanyrd).

That comparison is perhaps a bit histrionic, but in his post, Willison writes: “I think we’re due a Challenger disaster with respect to coding agent security … I think so many people, myself included, are running these coding agents practically as root, right? We’re letting them do all of this stuff. And every time I do it, my computer doesn’t get wiped. I’m like, ‘Oh, it’s fine.’”

Willison is referring to the Challenger space shuttle disaster of 1986, where the shuttle exploded shortly after takeoff and resulted in the death of all on board. The disaster occurred 40 years ago next week, on January 28, 1986.

## Vibe coding works ‘sometimes’

Meanwhile, Mytton argues that “Vibe coding works. Sometimes. But there’s a distinction most developers miss. The blast radius is different.”

He also explains that there are legitimate cases for vibe coding, such as:

* Throwaway prototypes where you’re testing feasibility and plan to rewrite properly.
* Small edits where it acts as an editor.
* Implementing within constraints where you’ve got tests or validated libraries with predictable behavior (like rate limiting with a known SDK).

However, Mytton notes that you don’t always know what the AI brought into your codebase, and asks: How deeply do you understand what came back? How do you test it? What’s it actually doing?

Responding to that, Mytton tells *The New Stack* that “strongly typed languages are at an advantage with AI coders because the compiler will fail when something is wrong. Even better with languages like [Rust](https://thenewstack.io/rust-programming-language-guide/), the compiler will fail when something is incorrect. This has always been a benefit of the language, but it was at the cost of a steep learning curve. Maybe that doesn’t matter now that AI can write provably correct code?”

Otherwise, you need a comprehensive test suite to ensure that the code changes don’t break functionality. This probably means end-to-end testing, he notes.

## AI should not invent security from scratch

“This matters most for security-critical code. If you can’t properly review it, you’re taking on risk you might not realize,” Mytton writes. “That’s why AI should implement validated components, not invent security from scratch.”

Moreover, in the blog post, Mytton says AI should implement validated components, not invent security from scratch.

In an interview with *The New Stack*, he adds, “You don’t necessarily want to write something from scratch if there is a prebuilt component you can use. The classic one is: don’t write your own crypto. Use a battle-tested library instead. This is the same principle for other security mechanisms, like writing your own bot detection. AI can bring in a component that is known to be secure and leverage its capabilities rather than writing from scratch.”

However, in a [blog post](https://mobb.ai/blog/how-to-seed-a-security-backlog-in-your-agentic-ide) from last year, [Eitan Worcel](https://www.linkedin.com/in/worcel/), founder and CEO of [Mobb](https://mobb.ai/), which offers a vibe coding security solution, wrote, “In the pre-vibe coding world, a security backlog was a list of known issues you might get around to fixing before the next audit. Bad, but relatively contained. Now those unresolved vulnerabilities are actively shaping the code your team writes tomorrow. **Your backlog is no longer static debt; it is an active risk** that influences every new line of code.”

In an interview with *The New Stack*, Worcel says he agrees with Mytton on the need to rely on validating security best practices versus having the AI come up with some made-up approach that the developer may find hard to review and “for sure” was not battle-tested.

Moreover, Worcel says he doesn’t necessarily agree that limiting the AI to adding functionality to existing projects is more secure than having it write code from scratch.

“In fact, from my experience, it is not,” he says. “Most of the production applications that have been around for years — if not decades — carry with them a large to very large security backlog. When you prompt the [large language model] to add a feature, it will first look at the application code, and if it finds a pattern that can be used in the implementation of the requested feature, it will treat it as an ‘approved pattern’ and prefer using that one over its own knowledge, even if that pattern is vulnerable.”

Yet, when you tell an AI, “I’m getting bot traffic, fix it,” it shouldn’t write novel detection logic you can’t verify. It should install a validated library. Write config. Write tests. Run them. Verify blocking works, Mytton says.

Finally, Mytton asks, “So where’s the line? As of Jan 2026:

* Scaffolding around validated components: yes.
* Novel security implementations you can’t verify: no.
* Small reviewable changes to existing code: yes.
* Entire codebases from scratch: only if treating it as disposable.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)