What would an AI-first language look like? Last year, a developer in Spain warned that our human-friendly syntax consumed an “excessive” number of tokens — thereby increasing costs — and prevented complex programs from fitting within existing AI context windows. “I asked Claude to invent a programming language where the sole focus is for LLM efficiency,” the developer [explained on Reddit](https://www.reddit.com/r/ClaudeAI/comments/1lpxaux/i_asked_claude_code_to_invent_an_aifirst/), “without any concern for how it would serve human developers.”

And their attempt at an “[AI-first native language](https://github.com/AvitalTamir/sever) wasn’t the last. Just last week, a developer [announced](https://news.ycombinator.com/item?id=47355138) plans for a [new language](https://github.com/hvoetsch/valea) that addressed the needs of autonomous AI agents with “deterministic” syntax that clarified developer intent and a small language surface to reduce edge cases.

[Andrea Griffiths](https://www.linkedin.com/in/acolombiadev/), a senior developer advocate at GitHub and a writer for the newsletter [*Main Branch*](https://mainbranch.dev/), has seen experiments with “AI-first” languages. Still, nothing with meaningful adoption yet, Griffiths tells *The New Stack*.

“And I think that says a lot,” Griffiths says. “The gravitational pull of existing ecosystems is enormous — libraries, tooling, community knowledge, production infrastructure. A new language doesn’t just need to be better for AI. It needs to justify abandoning everything developers already have, and that shift is not gonna happen overnight.”

> “A new language doesn’t just need to be better for AI. It needs to justify abandoning everything developers already have, and that shift is not gonna happen overnight.”

Will we one day develop an AI-optimized language at the expense of human readability? Or will AI coding agents make it easier to use our existing languages — especially typed languages with built-in safety advantages? Could we even imagine a world with AI-first languages that abstract away everything, generating compiler-ready modules without source code?

Developers, language designers, and developer advocates are now beginning to ask those questions…

## Chris Lattner’s Mojo vs. Rust

How should programming languages look in the age of AI? There’s more than one answer. During a recent episode of *[The Hanselminutes Podcast](https://hanselminutes.com/1037/thats-good-mojo-creating-a-programming-language-for-an-ai-world-with-chris-lattner)* hosted by Scott Hanselman, Microsoft’s VP of developer community, Hanselman broached this topic with [Chris Lattner](https://www.linkedin.com/in/chris-lattner-5664498a/), the co-founder and CEO of the AI tools company [Modular AI](https://www.modular.com/).

Lattner’s career includes creating the Swift programming language and the LLVM compiler toolchain — but he’s focusing on how *hardware* is changing, arguing that with today’s multi-core and AI-optimized chips, “We have all these crazy GPUs and all this compute out there that nobody knows how to program!”

> “We have all these crazy GPUs and all this compute out there that nobody knows how to program!”

So while Lattner’s company builds AI tools for developers, it’s also working on its new programming language Mojo, which Lattner suggests is “LLVM but for AI chips, basically… a way to program it that scales across all the silicon.”

Hanselman’s podcast dubbed it “[a programming language for an AI world](https://www.youtube.com/watch?v=pTM2bnFxyf8).”

But others still see AI nudging coders toward *existing* programming languages with built-in memory safety — including [Peter Jiang](https://www.linkedin.com/in/peter-jiang-ca/), the founding engineer of [Datacurve](https://datacurve.ai/) (which sells high-quality/complexity data). Writing earlier this month in *Forbes*, Jiang describes Rust as ” [the unlikely engine of the vibe coding era](https://www.forbes.com/councils/forbestechcouncil/2026/03/03/rust-the-unlikely-engine-of-the-vibe-coding-era/)… When AI writes the code, Rust’s strictness stops being a hurdle and becomes free quality assurance,” with Rust’s compiler acting as “a guardrail that forces the LLM to prove its logic is sound.”

It’s an attractive advantage, notes GitHub’s senior director for developer advocacy, Cassidy Williams. [In January](https://github.blog/ai-and-ml/llms/why-ai-is-pushing-developers-toward-typed-languages/), Williams cited a 2025 academic study that found [94% of LLM-generated compilation errors were type-check failures](https://arxiv.org/pdf/2504.09246).”

## Typed languages for the win?

There’s data suggesting developers are acting on those advantages — and not just by moving to Rust. Williams added that TypeScript “is now the most used language on GitHub, overtaking *both* Python and JavaScript as of [August 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/),” crediting as one factor “a boost from AI-assisted development… TypeScript grew by over 1 million contributors in 2025 (+66% YoY, Aug ’25 vs. Aug ’24) with an estimated 2.6 million developers total.” And other typed languages prove the trend, Williams believes, sharing more examples from [GitHub’s data](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/):

* “Luau, Roblox’s scripting language, saw >194% YoY growth as a gradually typed language.”
* “Typst, often compared to LaTeX, but with functional design and strong typing, saw >108% YoY growth.”
* “Even older languages like Java, C++, and C# saw more growth than ever in this year’s report.”

So while AI may be impacting programming languages, Griffiths says, it’s not necessarily through a move toward new AI-optimized languages. “What actually happens is more subtle: languages that are already structured, strongly typed, and explicit become more attractive because AI tools work better with them. TypeScript over JavaScript. Rust over C. Python’s type hints are becoming standard practice. The change isn’t a new language. It’s a shift in which existing languages win.”

> “The change isn’t a new language. It’s a shift in which existing languages win.”

Griffiths spelled it out last month [on GitHub’s blog](https://github.blog/ai-and-ml/generative-ai/how-ai-is-reshaping-developer-choice-and-octoverse-data-proves-it/), writing that strongly typed languages like Rust impose “clearer constraints” on AI, resulting in “more reliable, contextually correct code.” And at the same time, “the penalty for choosing powerful but complex languages disappears” with AI handling the syntax. In fact, GitHub’s most recent figures, released in October, showed that even *shell scripting* in AI-generated projects leaped by 206%, Griffiths pointed out. “AI absorbed the friction that made shell scripting painful.

“So now we use the right tool for the job without the usual cost.”

## Existing languages — or no language at all?

One person watching all this closely is Stephen Cass, the special projects editor at IEEE Spectrum. Since 2019, he’s ranked programming languages by popularity for IEEE Spectrum (a tradition they began in 2013). But will the popularity of today’s languages now remain frozen in time, Cass [asked in September](https://spectrum.ieee.org/top-programming-languages-2025)?

In a world with AI-powered coding tools, could emerging languages always face a handicap, since LLMs work best when they’re trained on large codebases with years of historical examples? Cass wondered if AI could also stymie the development of new languages in other ways — since “if an AI is soothing our irritations with today’s languages, will any new ones ever reach the kind of critical mass needed to make an impact?”

But Cass is also among those people intrigued by the possibility of a new language created specifically for AI agents. Languages basically create human-friendly abstractions (and safety precautions), Cass’s essay argued — but “how much abstraction and anti-foot-shooting structure will a sufficiently advanced coding AI really need?” Cass dared the ultimate question about our future: “Could we get our AIs to go straight from prompt to an intermediate language that could be fed into the interpreter or compiler of our choice? Do we need high-level languages at all in that future?”

Cass acknowledged the obvious downsides. (“True, this would turn programs into inscrutable black boxes, but they could still be divided into modular testable units for sanity and quality checks.”) But “instead of trying to read or maintain source code, programmers would just tweak their prompts and generate software afresh.”

This leads to some mind-boggling hypotheticals, like “What’s the role of the programmer in a future without source code?” Cass asked the question and announced “an emergency interactive session” in October to discuss whether AI is signaling the end of distinct programming languages as we know them.

## What if…?

In [that webinar](https://www.youtube.com/watch?v=53ZX1SCNryQ), Cass said he believes programmers of the future would still suggest interfaces, select algorithms, and make other architecture design choices. And obviously the resulting code would need to pass tests, Cass said, and “has to be able to explain what it’s doing.”

But what kind of abstractions could go away? And then “What happens when we really let AIs off the hook on this?” Cass asked — when we “stop bothering” to have them code in high-level languages. (Since, after all, high-level languages “are a tool for human beings.”)

“What if we let the machines go directly into creating intermediate code?” (Cass thinks the machine-language level would be too far down the stack, “because you do want a compile layer too for different architecture…”)

These ideas drew skepticism from the webinar’s co-host, Dina Genkina (the site’s associate editor focused on computing/hardware). Genkina agreed that today’s programming languages are offering “guard rails for the human to not do dumb stuff.” But even in a world trying new languages with AI-friendly micro-optimizations, “I feel like it’s an open question whether the AI will need more guard rails or [fewer] guard rails… I’m not saying it’s not possible, but I don’t quite see a path to there… from where we are right now.”

![IEEE Spectrum webinar - IEEE Spectrum Webinar - Will AI End Distinct Programming Languages](https://cdn.thenewstack.io/media/2026/03/4148ee18-ieee-spectrum-webinar-ieee-spectrum-webinar-will-ai-end-distinct-programming-languages.png)

So, regardless of any moves toward a more AI-friendly language, Genkina concluded that, in the end, our new machine-powered pair programmer will still have to undergo code reviews. “There’s definitely a camp of people that believe that you need a human in the loop… indefinitely… I think if we don’t understand what it’s doing, that contributes to the fear… Interpretability of AI is going to become more and more important, especially in things like this.”

With a laugh, Cass noted the possibility that we could even introduce “brand new failings,” like what he sees as “the driverless car dilemma… It’s like, ‘Well, you know, maybe it kills different people, but if it kills [fewer] people overall… In this future, the question might become ‘What if you make fewer mistakes, but they’re different mistakes?'”

Cass said he’s keeping an eye out for research papers on designing languages for AI, although he agreed that it’s not a “tomorrow” thing — since, after all, we’re still digesting “vibe coding” right now. But “I can see this becoming an area of active research.”

Although he also agrees that a sandboxed environment would be good for AI…

## Code-free programming remains “speculative”

Reached for comment this week by *The New Stack*, co-host Dina Genkina remained skeptical, saying, “To my knowledge, code-free programming is still speculative.”

And back at MainBranch.dev, senior developer Andrea Griffiths remains unconvinced as well. “Will we see languages optimized for AI readers, not human maintainers? I’d push back on that. Code still needs to be debugged, audited, and understood by humans, especially when things go wrong in production. No engineering team is going to deploy code they can’t inspect.”

But a more likely outcome, Griffiths suggests, is a world where AI “changes what humans need to read.”

What we should be imagining, Griffiths says, is a future where “You spend less time reading boilerplate — and more time reviewing architecture decisions, edge cases, and security boundaries!”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel is a proud resident of the San Francisco Bay Area, where he's been covering technology news for more than two decades. Over the years his articles have appeared everywhere from CNN, MSNBC, and the Wall Street Journal Interactive...

Read more from David Cassel](https://thenewstack.io/author/destiny/)