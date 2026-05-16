The most expensive bugs in software aren’t in the code. They’re in the requirements that guide the code’s construction.

That’s what AWS is trying to eliminate with new features in its [Kiro](https://thenewstack.io/aws-kiro-brings-automated-reasoning-to-agentic-development/) [agentic development platform](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/). The primary new feature is [Requirements Analysis](https://kiro.dev/blog/deep-spec-analysis/), which tackles requirement bugs. These are contradictions, ambiguities, and gaps in specifications that get baked into design and code before anyone catches them. By the time they surface in production, tracing them back to a misread requirement can mean weeks of debugging.

[Mike Miller](https://www.linkedin.com/in/camikemiller/), director of AI product management at AWS, tells *The New Stack* that “a bug in a requirement could be things that are contradicting requirements that imply two different things, ambiguities or gaps where a requirement might mean one thing to one developer but something slightly different to another.”

“And so down the path of implementation, code testing, and then in production, maybe something doesn’t work as expected, and you start rewinding,” says Miller, who leads the Requirements Analysis initiative.

The feature works in three stages, Miller explains. First, an LLM rewrites vague, natural-language requirements into precise, testable criteria. Second, that output gets translated into formal mathematical logic — what AWS calls a “formal representation.” Third, an [SMT (satisfiability modulo theories) solver](https://en.wikipedia.org/wiki/Satisfiability_modulo_theories), a type of automated reasoning engine, runs proofs against that logic to identify contradictions, ambiguities, undefined behaviors, and gaps. Findings surface to the developer as plain-language, two-option questions that Miller says can be resolved in about 10 to 15 seconds each.

The term AWS keeps reaching for is *prove*. This is not the LLM flagging a probable issue — it is a formal reasoning engine demonstrating that no possible implementation can simultaneously satisfy two conflicting rules, the company says.

“Automated reasoning allows us to take those requirements, look at them, identify gaps and ambiguities, and kind of address them up front,” Miller says. “The LLM side does what it does best, and automated reasoning does what it does best.”

[Jason Andersen](https://www.linkedin.com/in/jasontandersen/), an analyst with Moor Insights & Strategy, tells *The New Stack* that “AWS has been a pioneer in the idea that LLM model correctness can be evaluated using diverse algorithmic models to improve accuracy.”

“It started with the use of Automated Reasoning in access control products such as IAM,” Andersen continues. “That success has started to spread into other AWS product lines. This is not the only method for judging LLM outputs. The more typical approach is to use additional LLMs to inspect the outputs and determine whether they make sense.”

## The neurosymbolic positioning

The term [neurosymbolic AI](https://thenewstack.io/allegrograph-8-0-incorporates-neuro-symbolic-ai-a-pathway-to-agi/) refers to the combination of neural networks — the statistical, pattern-matching machinery behind LLMs — with symbolic logic, the rule-based, mathematically rigorous branch of AI that has been used for decades in formal verification and model checking, Miller says.

> “Speed without correctness just means you write wrong software faster.”

He uses the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem) as an analogy to explain the difference in approach. An LLM trained on thousands of right triangles might infer the relationship between the sides and the hypotenuse. But it is inferring. It could be wrong. An automated reasoning system, by contrast, uses mathematical symbols to prove the relationship holds across every possible right triangle — not as a probability, but as a certainty, Miller says.

Formal verification techniques built on this kind of symbolic logic have been used in hardware design and safety-critical software since the 1970s — some 50 years before the advent of LLMs.

“It’s not just about velocity,” he notes. “Speed without correctness just means you write wrong software faster.”

Kiro was built around [spec-driven development](https://thenewstack.io/vibe-coding-spec-driven/) from the start, tracing every line of generated code back to a documented requirement, Miller says. Requirements Analysis is meant to make that trace not just documented, but logically sound.

In internal testing across 35 Kiro projects with more than 1,400 acceptance criteria, roughly 60% of first-draft requirements needed refinement before they could be reliably implemented, Miller says. But he said that is to be expected, as a first draft is a starting point.

## Why now

AWS has been doing automated reasoning work quietly for years. The technology already appears in [Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/), where a similar formal-logic pipeline can encode a chatbot’s behavioral policy and validate responses against it mathematically, Miller says. It also appears in the [Bedrock AgentCore policy](https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/), which uses the same reasoning engine to determine when agents can use which tools under which circumstances.

Requirements Analysis represents the first time that capability has been embedded directly in the development workflow, at the moment when specs are being written, Miller claims.

> “We are not seeing many evaluations applied at this point in the dev toolchain, let alone with a more advanced algorithmic technique.”

“My findings with Kiro are that they have been very successful in pushing the envelope of features and getting to market first. In this case,” Andersen says. “I would agree that they are ahead with this level of requirements reviews. We are not seeing many evaluations applied at this point in the dev toolchain, let alone with a more advanced algorithmic technique.”

AWS has found that healthcare, finance, and other sectors where correctness is non-negotiable have been drawn to its automated reasoning capabilities, specifically because they need AI that doesn’t hallucinate in sensitive contexts. The same pattern, AWS says, is emerging with agentic coding tools.

In addition to Requirements Analysis, other new Kiro features include: Parallel Task Execution, which runs independent coding tasks concurrently to cut implementation time for large specs by roughly 75%, and Quick Plan, which generates a full set of requirements, design specs, and task breakdowns in a single pass after asking clarifying questions upfront.

Kiro competes in a market with several popular AI coding tools, including Cursor, Codex, [Claude Code](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/), [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/), and Windsurf, among others.

However, AWS says Kiro is widely used in the industry.

Kiro’s broader customer base already spans industries where getting it right matters as much as getting it done. [Socure](https://www.socure.com/), a digital identity verification and fraud prevention company, used Kiro’s spec-driven development to complete a [Scala](https://thenewstack.io/scala-creator-proposes-lean-scala-for-simpler-code/)-to-[Go](https://thenewstack.io/go/) migration in two days. The project was originally scoped at three weeks.

[Nymbus](https://www.nymbus.com/), a banking technology provider, generates 80% of its [Terraform](https://thenewstack.io/terraform-competitor-formae-expands-to-more-clouds/) code, unit tests, and [Playwright](https://thenewstack.io/a-practical-guide-to-data-driven-tests-with-playwright/) object models with Kiro, cutting testing time on one project from 32 weeks to 7. Delta Air Lines reached its pilot program goals two quarters ahead of schedule. Nielsen saw a 25% increase in test coverage and a 40% decrease in time spent on documentation. Hughes Network Systems says Kiro specs eliminate the need to repeatedly re-establish context throughout the development workflow.

The Kiro adoption list also includes Siemens, Rackspace Technology, Mondelez International, Appian, and Ericsson, alongside Amazon’s own internal teams — Alexa+, Prime Video, Amazon Stores, and Fire TV among them.

## The leadership signal

In addition to the Kiro feature launch, AWS announced that [Shawn Bice](https://www.linkedin.com/in/shawn-bice-9205423/) has joined the company as VP of AI Services within Agentic AI, reporting to [Swami Sivasubramanian](https://www.linkedin.com/in/swaminathansivasubramanian/), VP of Agentic AI at AWS. Bice will lead AWS’s Automated Reasoning Group.

In an internal memo to employees, Sivasubramanian wrote: “We are at an inflection point with Agentic AI, and I can’t stress enough how critical AI and Automated Reasoning need to come together to build reliable and trustworthy agents.”

“To me, whether it’s a better or more precise method is not the question,” Andersen says. “My question is: what’s the impact on the human-in-the-loop? If AWS is better at locating an issue, that’s a good thing, but ultimately it’s going to come back to the developer to figure out what to do at this point. At some future point when we are automating more of the toolchain, any improvement of this type could be very valuable.”

AWS is betting that the next competitive axis in AI-assisted development is not how fast you can generate code, but how much you can trust what gets generated. Requirements Analysis is key to that bet.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)