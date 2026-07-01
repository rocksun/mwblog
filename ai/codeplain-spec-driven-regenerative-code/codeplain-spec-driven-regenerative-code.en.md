AI is generating code faster than teams can review it. The answer, a small but growing number of developers argue, isn’t faster code review, but replacing code review with something else entirely.

[Dušan Omerčević](https://www.linkedin.com/in/dusanomercevic/) is CEO and co-founder of [Codeplain](https://www.codeplain.ai/), a company that’s all-in on [spec-driven development](https://thenewstack.io/vibe-coding-spec-driven/) as the foundation for building and maintaining AI-era software. Founded in Ljubljana, Slovenia, in early 2025, Codeplain [launched quietly in September](https://blog.codeplain.ai/p/beyond-vibe-coding) of that year with the promise of “spec-driven, production-ready code generation.”

The basis of this is [Plain](https://plainlang.org/), an open-source specification language that uses structured, human-readable documents as the single source of truth for how software should be built and behave. The idea is that if something breaks or needs changing, you edit the spec, not the code, and Codeplain regenerates the implementation from scratch.

![A Plain specification for a Trello client application (left) and the Python code Codeplain generates from it (right).](https://cdn.thenewstack.io/media/2026/06/ef967213-codegif.gif)

*A Plain specification for a Trello client application (left) and the Python code Codeplain generates from it (right).*

Now, Omerčević is pushing that idea further. In an interview with *The New Stack*, he argues that as AI generates ever-larger volumes of code, the bottleneck has shifted from writing software to reviewing and maintaining it — and that reviewing specs, which encode intent rather than implementation, requires a fraction of the cognitive load of reviewing code.

> “Our thesis is that code should not be maintained – code should be regenerated. Specs should be reviewed, and it’s the specs that you maintain.”

“Our thesis is that code should not be maintained — code should be regenerated,” Omerčević explains. “Specs should be reviewed, and it’s the specs that you maintain.”

To advance that mission, the company is rolling out a new open-source agentic skills framework dubbed [plain-forge](https://github.com/Codeplain-ai/plain-forge), which lets coding agents such as Claude Code, Codex, and OpenCode draft and maintain Plain specs through conversation — effectively automating the part of spec-driven development that previously required the most human effort.

Alongside the launch, Codeplain also announced that it has raised $3M in funding to date from backers including [GapMinder VC](https://gapminder.vc/) and [Silicon Gardens](https://www.silicongardens.com/).

## **The joy of specs: a new development paradigm**

Codeplain is far from alone in its embrace of spec-driven development. Back in July 2025, [Amazon debuted Kiro](https://thenewstack.io/kiro-is-awss-specs-centric-answer-to-windsurf-and-cursor/), an agentic IDE that steers development using structured specifications generated from natural-language prompts. GitHub, meanwhile, [followed with Spec Kit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/), an open-source toolkit designed to make specs executable artifacts that AI agents can act on directly.

The underlying concept, however, predates both. [SpecLang](https://githubnext.com/projects/speclang/) was a GitHub Next research project that began exploring in 2023 whether plain English could serve as a true programming medium — one where AI handles the translation from human intent to working code.

That lineage connects directly to Codeplain, too. [Johan Rosenkilde](https://www.linkedin.com/in/johan-rosenkilde/), one of SpecLang’s creators and a founding member of the GitHub Copilot team, [sits on Codeplain’s board](https://www.linkedin.com/posts/codeplain_codeplain-welcomes-dr-johan-sebastian-activity-7334949185768599552-bsKS/) and was among its earliest investors.

But despite the momentum behind spec-driven development, it seems developers don’t particularly want to write specifications. Through user testing, Omerčević and his team found that while developers resist writing specs, they are generally happy to read them. A well-structured spec, it turns out, is easier to review and reason about than the code it eventually produces.

Plain-forge is Codeplain’s answer to that tension. Rather than asking developers to author specifications from scratch, it puts the coding agent to work — researching the problem, drafting the spec incrementally, and validating it against Codeplain’s renderer before a human ever sees it. Crucially, it doesn’t front-load the process by generating a sprawling specification upfront — an approach Omerčević is openly critical of.

“We don’t throw 200 lines of specs at a developer; we do it iteratively,” he says.

Each small spec generates working software that the developer can immediately check and respond to, building familiarity with the spec one feature at a time rather than confronting a finished document they had no hand in shaping.

“By incrementally adding to the specs, the developer is building relations with the spec.”

“In this way, by incrementally adding to the specs, the developer is building relations with the spec,” Omerčević says. “The specs are the source of truth, and the specs are the feedback to the developer that the AI understood them.”

## **Rise like a phoenix**

Underpinning all of this is a fundamental belief that code should be treated as disposable output rather than a durable asset, and that the spec — not the generated code — is what teams should preserve and maintain. Omerčević says he arrived at this conclusion through his own experience building Codeplain, but found it difficult to articulate to developers whose entire professional identity is built around code.

This is where [Chad Fowler](https://www.linkedin.com/in/fowlerchad/)‘s [*Phoenix Architecture*](https://aicoding.leaflet.pub/) enters the fray. Fowler, a veteran engineer and General Partner at BlueYard Capital, has spent the past six months developing a broader philosophical framework for this approach.

His inaugural post in the series back in December, titled [*Regenerative Software*](https://aicoding.leaflet.pub/3majnyfydzs2y), argues that AI has made code abundant and cheap, inverting decades of assumptions about what in a software system is worth preserving — and that teams clinging to existing implementations are generating technical debt faster than they realize.

It’s a framework that Omerčević says gave him a vocabulary he’d been struggling to find.

> “Spec-driven development was really hard to communicate to regular developers.”

“Spec-driven development was really hard to communicate to regular developers,” Omerčević says. “What Chad did really well is ground the story in code, saying that the only difference is that this code is no longer permanent — it’s ephemeral, and it can always be regenerated from other artifacts.”

The [phoenix](https://en.wikipedia.org/wiki/Phoenix_(mythology)), for the uninitiated, is a creature of Greek myth — a bird that cyclically burns itself and is reborn from the ashes. Fowler’s argument is that software systems should be designed to do the same.

In his March post, “[The Conversation Is the Commit](https://aicoding.leaflet.pub/3mhxvpam4z22z),” Fowler argues that when developers manually edit AI-generated code, they sever something important: the record of why that code exists and what decisions shaped it. The output changes, but the reasoning behind the change is lost.

Over time, that accumulation of lost context is what Fowler calls “*provenance debt*” — and his argument is that most developers have been building it up their entire careers without a name for it.

> “If we don’t move toward finally capturing this rich and important information, we are irresponsible in the face of this wave of innovation in how we build software.”

“It’s just that it was impossible, technologically, to capture provenance without extreme bureaucracy, so as an industry we all decided it wasn’t a trade worth trying to make in almost all cases,” Fowler explains to *The New Stack*. “Now the tooling opens these sorts of things up without heavy process. My argument is that if we don’t move toward finally capturing this rich and important information, we are irresponsible in the face of this wave of innovation in how we build software.”

Put another way, the specs and the reasoning behind them are now the thing worth preserving — not the code they produce.

It’s difficult to overstate how significant a cultural shift this would entail – developers, after all, have built their identities around code. So how do you convince an engineer that deletion and regeneration represent progress?

For Fowler, there are two ways, each reflecting a different kind of persuasion.

“The first is to wait, because they will see that, over time, the old way of doing things has become obsolete and they need to evolve or die,” he says. “The second, and more positive way is to show them that deletion and regeneration define, and are supported by, a new level of rigor that only this new tooling makes possible.”

Codeplain, in Fowler’s view, represents one credible attempt to build that rigor into a working product — though he’s careful to say it’s just one piece of a larger puzzle still being assembled.

“My hope is that many companies and open source developers [build it],” he says. “This is because I think this missing layer can look very different. There’s a lot of room for imagination and innovation here. I don’t want to go with any one person or team’s assumptions of how it should work. The weirder the better, I think. We have to invent a new set of idioms and tools.”

## **Up to spec**

![Codeplain founders Dusan Omercevic (CEO) and Predrag Radenkovic (CTO)](https://cdn.thenewstack.io/media/2026/06/217cfb17-codeplain-dusan-predrag-photo-1024x681.jpg)

*Codeplain founders Predrag Radenkovic (CTO)* and *Dusan Omercevic (CEO)*

Omerčević is no stranger to building and shipping enterprise software — he previously [founded Cleanshelf](https://techcrunch.com/2017/01/24/cleanshelf-teams-up-with-squrb-to-clean-your-saas-clock/), a SaaS management platform [he sold to LeanIX in 2021](https://www.leanix.net/en/company/press/leanix-acquire-saas-management-provider-cleanshelf), which in turn was subsequently [acquired by SAP](https://news.sap.com/2023/11/sap-completes-acquisition-of-leanix/). Codeplain, then, is his next act — and it already has customers putting it to work.

[Incode](https://www.incode.com/), an identity verification service provider, uses Codeplain to build and maintain integrations with external data providers — the kind of work that involves constant API research, rapidly changing external systems, and a high tolerance for things breaking unexpectedly.

It’s that last problem — things breaking — that Omerčević is most animated about. Because specs encode intent rather than implementation detail, when an external API changes and breaks an integration, Codeplain can often fix it by regenerating the code from the exact same spec, unchanged. The spec didn’t break; only the code did.

“You don’t even tweak the specs,” Omerčević says. “You just regenerate code from exactly the same specs, because quite often something small changes and breaks, but specs don’t.”

There are also hard economic arguments behind the approach. Omerčević says that coding agents that generate specs use five to ten times fewer tokens than when generating code directly — and that because specs are cognitively less demanding for the agent, it can handle larger, more complex problems within the same context window. For the code generation step itself, Codeplain uses faster, cheaper models such as Gemini Flash rather than frontier models, keeping costs down.

The analogy Omerčević reaches for is the TypeScript compiler: Claude could generate JavaScript directly from TypeScript, but why would you when a specialized tool does it faster and more cheaply?

“Let the specialized tools do what they are really good at,” he says. “And let Claude do what it is really good at — and that is research.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)