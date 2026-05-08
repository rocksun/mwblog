The [Association for Computing Machinery](https://www.acm.org/)‘s (ACM) Technology Policy Council (TPC) has a message for organizations riding the [vibe coding](https://thenewstack.io/beginners-guide-to-vibe-coding/) wave: The productivity gains are real, but so are the risks — and current platforms are not equipped to manage them.

A new briefing from the group, “AI-Assisted Software Development, or Vibe Coding: Benefits and Risks of AI-Driven Software Development,” takes a systematic look at the practice of using generative AI to write, debug, and increasingly execute code based on natural-language prompts. The verdict is not a condemnation — but *is* a warning.

“I use AI-assisted coding every day for both my personal and professional projects, and it’s transformed how I develop software,” says [Simson Garfinkel](https://www.linkedin.com/in/simsongarfinkel/), chief scientist at [BasisTech](https://www.basistech.com/) and lead author of the TechBrief, in a statement.

> “It’s making developers dramatically more effective, but it’s also introducing security vulnerabilities.”

“It’s making developers dramatically more effective, but it’s also introducing security vulnerabilities, increasing technical debt, and producing code that can be difficult to maintain. To use these tools safely, strong software engineering practices are still required, including clear specifications, meaningful testing, and enforced standards.”

## Productivity with a catch

The TechBrief acknowledges that vibe coding lowers the barrier to software creation, helps experienced developers navigate complex APIs more quickly, and frees up attention for higher-level design work. Many developers report feeling more productive, especially on routine tasks that don’t require much creative judgment.

But the ACM authors are careful to note that those productivity reports are subjective — and may not hold up under empirical scrutiny over time.

The deeper problem is structural, the TechBrief indicates. A foundational principle of software engineering holds that a program’s behavior must be specified before it can be evaluated as correct or incorrect. [AI-generated code](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/) typically arrives without those specifications. And even when developers provide them, most vibe coding platforms have no mechanism to enforce them. This means the code drifts from requirements in ways that may not surface until much later.

## Tests that disappear

One of the more striking findings in the TechBrief is that AI coding platforms have been observed to modify, disable, or outright delete failing tests rather than fix the underlying code. The implication is significant. If you hand a vibe coding system an acceptance test suite, you cannot assume the suite will be intact when the system is done, the TechBrief says.

The result, the authors argue, is code that accumulates technical debt at scale, is over-engineered and redundant, and is increasingly difficult for human developers to review.

> “AI systems do not understand what they’re producing, and they are not capable of reasoning about the consequences.”

In fact, the volume and complexity of AI-generated code can make manual code review impractical, allowing errors to slip into production undetected.

“AI systems do not understand what they’re producing, and they are not capable of reasoning about the consequences,” Garfinkel says. “As a result, we are only beginning to understand the broader impact of this technology, which is evolving rapidly.”

## Agentic features raise the stakes

The risks become more acute as vibe coding platforms add [agentic capabilities](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/) — the ability not just to write code but to run it, often without requiring the developer to review the execution first. The TechBrief flags this as a meaningful escalation of risk.

Agentic platforms can execute code not just on a user’s local machine but on any networked system within reach. That creates exposure for a range of unintended actions, including deleting critical files, sending sensitive data outside enterprise security perimeters, downloading and running arbitrary software, or reconfiguring systems in ways that invite intrusion.

There is also the [prompt injection problem](https://www.ibm.com/think/topics/prompt-injection), the TechBrief notes. When third parties can embed malicious instructions into software that the AI interprets as legitimate developer commands, the attack surface expands considerably.

## The experience gap

One long-term concern revealed in the TechBrief is the impact of vibe coding on the talent pipeline. An internal study from a major — though unnamed — AI provider found that students and early-career programmers using AI coding tools showed a decline in mastery of core programming concepts over time.

The dynamic the authors describe is compounding. The tasks AI automates most readily — simplifying redundant code, porting to new environments, adding routine features — are the tasks junior developers need to do to become senior developers. Strip those out of the learning path, and you don’t just slow skill development; you eliminate the conditions under which it happens, the authors argue.

The TechBrief calls this the “experience gap” — a scenario in which AI simultaneously automates early-career work and erodes the skills of those further along in their careers, ultimately producing a shortage of experienced developers even as the tools promise abundance.

## The results are systematic

The authors conclude that the failures of current vibe coding platforms are not incidental bugs. They are systemic. The authors conclude that the same absence of a rigorous semantic model that prevents AI from reliably validating its own outputs is the same mechanism responsible for AI hallucinations more broadly.

Until that changes, the TechBrief says, organizations need to compensate with stronger governance, formal verification methods, and specialized tooling designed to catch what vibe coding platforms cannot catch themselves.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)