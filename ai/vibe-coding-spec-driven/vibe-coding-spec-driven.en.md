AI is drowning codebases in machine-written output, but without a strategic framework, we aren’t just innovating; we’re automating the creation of legacy mess, one enterprise software leader argues.

With [vibe coding](https://thenewstack.io/why-there-might-be-something-to-vibe-coding-after-all/), a developer only needs to type a few prompts into an [AI coding assistant](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/) to create a functioning app in seconds. But if you repeat that process thousands of times across an engineering organization, all that AI-generated code could mean that today’s productivity gains may become tomorrow’s [technical debt](https://thenewstack.io/technical-debt-vs-architecture-debt-dont-confuse-them/).

[Matthias Steiner](https://www.linkedin.com/in/matthiassteiner/?originalSubdomain=de), vice president of Global Business Innovation at [Syntax](https://www.syntax.com/), an SAP consulting and managed services firm, tells *The New Stack* that productivity without governance is opening the door to problems.

“Nobody gets paid to write code but to create outcomes,” Steiner says. “Coding is only part of the job.”

## AI for every SDLC phase

In an interview, Steiner emphasized the concept of [spec-driven development](https://thenewstack.io/is-spec-driven-development-key-for-infrastructure-automation/), an approach that applies generative AI not just to code generation but across every phase of the software development lifecycle — from market analysis and ideation through requirements engineering, implementation, testing, and DevOps.

The “spec” in question is a functional specification that serves as a single source of truth for AI agents to generate designs, code, tests, and documentation consistently, Steiner says.

“I see spec-driven development as the future maturation of software development in the agentic age,” [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at the Futurum Group, tells *The New Stack*. “In this case, we’re taking older ideas — remember literate coding? — and using them to better define our ‘intent’ for guiding agentic workflows.”

## Step beyond vibe coding

This is the next big step beyond vibe coding, with minimal upfront structure.

“Freestyle code is probably also very dangerous, because it blows the code base,” Steiner says. “If you want to build enterprise-grade software with a life span of 10, 20 years, then you should probably have something that’s a little more modular and something that’s a little bit more governed.”

He is not dismissing vibe coding outright. He sees it as useful early in a product lifecycle, useful for prototyping and exploration. But he draws a line when it comes to enterprise software built for longevity.

Vibe coding is insufficient for the complexity and governance needs of enterprise software.

“A more durable model is emerging with*spec-driven development*, where a structured specification becomes the system’s single source of truth,” Steiner writes in a [blog post](https://www.syntax.com/blog/how-genai-is-transforming-software-engineering-but-not-replacing-it/).

“From that specification, AI can generate designs, create code, write tests, produce documentation, and orchestrate workflows consistently,” he adds.

Steiner further notes that open frameworks such as SpecKit, OpenSpec, and Claude Task Master are enabling this shift, allowing [AI agents](https://www.syntax.com/blog/agentic-ais-transformative-impact-across-industries/) to interpret and execute specifications with far greater reliability.

“This model reduces friction, improves alignment, and strengthens the link between engineering work and business outcomes,” Steiner writes.

## Governance needs

The governance problem, Steiner argues, is the consequence of AI-driven productivity gains. Industry leaders routinely cite figures suggesting AI will write 60% to 90% of production code and do it up to 55% faster than humans.

Despite those gains, Steiner said he sees this as [Jevons’ paradox](https://en.wikipedia.org/wiki/Jevons_paradox): More productivity means more software gets built, which means more software has to be maintained. In this case, Steiner explains that as AI makes software development faster and cheaper, the total amount of software being built will increase dramatically — meaning the overall demand for engineering work (and the governance burden of maintaining all that software) grows.

“With the gain in productivity, the number of applications will grow tremendously,” he says. “And who takes care of all of that?”

His answer is architecture. He insists that great software engineering has always been about componentization, reuse, and modularity. AI changes the speed of construction, not the fundamentals of the craft.

## Venture capital model

At Syntax, Steiner’s team of 30 engineers is currently running 10 product builds in parallel, applying a venture capital-style portfolio model to software development, he says.

The assumption is that half the products won’t achieve market fit and will be abandoned. The shortened ideation-to-market cycle enabled by spec-driven development makes such parallel experimentation economically viable.

“We assume that half of the products we build will not make it, so we just trash them,” Steiner says. “Maybe two or three will be doing good. And maybe there’s one unicorn in there.”

One product already headed to market is [ShiftBook](https://info.syntax.com/hubfs/5843035/Syntax-ShiftBook-Datasheet-EN_V02.pdf), a manufacturing shift handover application that integrates with SAP Manufacturing Cloud. It was Syntax’s first end-to-end spec-driven build, and Steiner says its success is pushing the team to apply the methodology across all new projects.

For tooling, Steiner’s team uses Anthropic’s Claude for coding and uses Task Master for spec-driven workflow management. TypeScript is the team’s primary language, as it strikes a middle ground between typed and untyped languages for the current generation of engineers, he says.

## Software engineering remains relevant

Steiner emphasizes to *The New Stack* that he does not believe software engineering as a discipline is becoming less relevant as AI takes over code generation.

“Don’t call software engineering dead just yet,” he says. “I think that it’s the opposite.”

While AI can handle the micro-decisions of code generation, the macro-decisions—boundary definition, dependency management, pattern governance, and aligning technical choices with business outcomes—still require human judgment, Steiner says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)