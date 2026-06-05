The pitch for most [AI coding tools](https://thenewstack.io/ai-coding-tools-create-more-bugs-than-they-fix/) is speed. Write a prompt, get a draft, iterate. The faster the model, the theory goes, the faster the software.

[Julien Verlaguet](https://www.linkedin.com/in/julien-verlaguet-b5710a20/) tells *The New Stack* he doesn’t buy that.

The founder and CEO of Paris-based [SkipLabs](https://skiplabs.io/) — and the engineer who created [Hack](https://hacklang.org/), the gradually typed programming language that powers Facebook’s core business logic across more than 100 million lines of production code — thinks the industry has been solving the wrong problem.

> “Building correct software has always been an architecture problem disguised as a coding problem.”

“Building correct software has always been an architecture problem disguised as a coding problem,” Verlaguet says in a statement. “AI did not change that; it just made the problem more urgent.”

On Monday, SkipLabs launched [Skipper](https://thenewstack.io/skiplabs-ai-guardrails-skipper/), a closed-loop coding agent designed to take a plain-language description — or an [OpenAPI](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/) spec — and return a complete, running, validated backend service. No review cycle. No iteration. No developer back-and-forth. The company describes it as the substrate sitting between foundation models and shipped software.

## The closed loop

![](https://cdn.thenewstack.io/media/2026/06/1830214e-1537985926303.jpg)

Julien Verlaguet, founder and CEO of Paris-based SkipLabs.

The key phrase in SkipLabs’ positioning is “closed loop,” and Verlaguet is precise about what it means. Tools like [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/), Cursor, or Codex keep the developer in the iteration cycle — prompt, review, refine, repeat. Skipper takes that cycle and runs it internally. The review-and-refine pass happens inside the agent, not between the agent and a human, he notes.

“Closed loop is not a feature,” Verlaguet adds in a statement. “It is a different theory of what an AI coding tool is supposed to do. The current generation makes the developer faster. The next generation makes the developer’s involvement optional. Describe what you want, and Skipper builds it.”

In practice, that means Skipper receives a prompt, generates an OpenAPI specification from it, builds out the full service — routes, data mappers, validators, TypeScript types, unit tests — and runs the whole thing in a Docker container. If the generated code fails type checks, Skipper fixes it, up to eight attempts, before returning a result. The process runs without a developer watching it.

The FAQ Skipper ships with draws the analogy: “You define an input, run Skipper, and get a working service — without worrying about what the generated code looks like.”

## State is where AI breaks

The architectural bet underneath Skipper is that state management and concurrency are where AI-generated code most consistently fails, and that the right fix is structural, not prompting-based.

Verlaguet has been making this argument for a while. In an earlier conversation with *The New Stack*, before the launch, he put it this way: “Every time I look closer at people who claim that they are bringing guardrails to AI, I see more the same. I see more prompting — and I don’t see anybody who is trying to build real guardrails and real tooling from scratch.”

His answer is the reactive runtime underpinning Skipper — drawn from [Skip](https://github.com/skiplang/skip/blob/master/docs/overview/getting_started.md), the programming language Verlaguet developed at Facebook in 2017. In the reactive model, the program is defined as a declarative graph of computation from inputs to outputs. The runtime handles state management, cache invalidation, and concurrency automatically. The AI model generating the service never has to reason about what happens when one part of the state graph changes and another part depends on it.

“I think it’s because it’s a lot of work,” Verlaguet says of why competitors haven’t taken the same approach, “and so it’s much easier to make those big claims that you’re going to do these things when, in the end, you don’t.”

The comparison he draws is to [React](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/) — the same idea applied to a backend service instead of a UI. [JavaScript](https://thenewstack.io/introduction-to-javascript/) handles the computation links between graph nodes; the Skip runtime manages everything below that.

## **What ships Monday**

Monday’s launch delivers the core closed-loop experience: a single prompt becomes a running service. Skipper is multi-model: it routes tasks to different foundation models based on fit, using Claude Opus as its default, with Sonnet and Haiku also in the mix. It is not locked to Anthropic; model selection is an architectural choice, not a product dependency.

“We don’t do any AI here,” Verlaguet told *The New Stack* in earlier discussions. “We treat the models as a commodity. To us, the model is just an API that we call with a context; it comes back with the result.”

Also shipping Monday: external service integration. Skipper-generated services can call outside APIs, fetch live data, and post to other systems, meaning the software it produces isn’t sandboxed to a local environment but wired into a real stack from the start.

Moreover, two capabilities are coming shortly after launch but weren’t ready to ship: a sound, incremental [TypeScript](https://thenewstack.io/typescript-6-0-rc-arrives-as-a-bridge-to-a-faster-future/) implementation Verlaguet calls SKJS, and an incremental update mode that would let builders change a specification and have Skipper modify the running service without a full rebuild. Both were close enough to appear in the product roadmap, but not close enough for SkipLabs to ship them by default.

“We’re not going to make it the default quite yet because we need to iron out a couple of things,” Verlaguet says in a pre-launch briefing, “but we should be able to release the type system [quickly after launch].”

## The infrastructure thesis

Meanwhile, the longer argument that Verlaguet is making with Skipper concerns where the bottleneck in AI-assisted development truly lies. His contention is that the pace of model improvement is already outrunning the tooling that validates the output.

“In the next few years, it’s not going to be okay to wait for CI to take half an hour to an hour to validate a diff,” Verlaguet tells *The New Stack*. “AI is getting faster and faster, and so you will need the tooling to guardrail the AI, and that tooling will need to be incremental.”

That’s the rationale for the sound TypeScript reimplementation, which is incremental by design — it can re-check code when something changes without restarting from scratch, giving the AI fast, reliable feedback mid-generation rather than at the end, he says.

On the financial side, SkipLabs raised an $8 million seed round led by Amplify Partners, which described Verlaguet in its investment memo as “one of the top two to three programming language designers in the world.” Angel investors include [Yann LeCun](https://www.linkedin.com/in/yann-lecun/) — Turing Award winner and former Meta Chief AI Scientist — and Spencer Kimball, co-founder and CEO of Cockroach Labs.

Skipper is available today at skipperai.dev.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)