**AI coding tools can produce a striking burst of productivity** — but the initial surge may not last. A [Carnegie Mellon study](https://arxiv.org/html/2511.04427v2) of public repositories adopting Cursor found a three- to five-fold increase in lines added during the first month, with the gains dissipating after roughly two months. The study, which used SonarQube (Sonar’s core platform) to measure code quality, also found that static analysis warnings rose by 30% and code complexity by 41%. The short-term velocity boost therefore comes with a persistent increase in technical debt.

[Tom Howlett](https://www.linkedin.com/in/tom-howlett-85ab6716/), [Sonar](https://www.sonar.com)’s Director of AI Engineering Engagement, tells *The New Stack* that while coding has sped up, verification, which many teams still rely on manual code review to do, hasn’t kept pace. If developers generate 50 times more code while relying on the same review process, time spent on code review rises and becomes a bottleneck, Howlett tells *The New Stack*.

There’s another complication. Agents don’t always know how to make the smallest change needed to deliver a feature. Without sufficient context about the codebase, they can make assumptions, generate unnecessary code, and add to technical debt. As Howlett puts it, you end up with more complex, verbose code, which makes the problem worse.

---

***Explore how*** [***SonarQube***](https://www.sonarsource.com/products/sonarqube/) ***can help your organization adopt agentic software development with confidence.***

---

The lesson for engineering leaders is that faster code generation doesn’t necessarily mean greater value. Teams also need confidence that the code delivers the intended outcome and meets their standards. Sonar describes this through its [code confidence formula](https://thenewstack.io/ai-code-confidence-gap/): intent x guiderails x verification x evidence. Howlett adds that the multiplication is deliberate: if any element is missing, confidence breaks down.

Putting that formula into practice requires more than a final review. Teams need to build it into the  three connected loops that make up development today:

* **The agentic loop**, as the code is created
* **The CI verification loop,** as changes are tested and prepared for merge
* **The code maintenance loop**, as the codebase evolves after release

This always-on approach lets teams pursue agentic velocity while preserving the code quality, security, reliability, and governance standards a dependable development workflow requires.

## The missing discipline: verification in the workflow

Having the model that generated the code review its own work, as Howlett describes it, is “like a student grading their own homework.” Coding agents are excellent coders, but their output isn’t guaranteed to be consistent. Because they’re probabilistic, not deterministic, you never know what they’ll miss, Howlett tells *The New Stack*, and AI code review can’t be your only line of defense.

> “…like a student grading their own homework.”

When pull requests become larger and more frequent, manual review alone can’t scale. Developers under delivery pressure can easily rubber-stamp changes they don’t have time to inspect line by line.  
  
[Anirban Chatterjee](https://www.linkedin.com/in/anirbanc/), Sonar’s director of product and solutions marketing, tells *The New Stack* that if you wait until then to verify, the agent might have made the same mistake three, four, or five times. He adds that the goal should be to prevent that bug from making it into the PR and from being repeated.  
  
Automated verification can catch different categories of problems, while human developers remain responsible for quality and focus on high-risk changes.

## Loop one: the agentic loop — improve effectiveness at creation

Sonar’s Agent Centric Development Cycle, or AC/DC, applies this principle by placing guidance, generation, verification, and remediation inside an agentic workflow. The first opportunity to intervene is also the earliest: while the agent is still writing the code. In [**the agentic loop**](https://docs.sonarsource.com/agent-centric-development-cycle/inside-your-agent-the-agentic-loop/agentic-loop), guidance and automated code verification sit alongside code generation: the agent receives the context it needs, makes a change, checks it, and fixes any issues before moving on.  
  
Context matters because an agent doesn’t start with the same deep codebase knowledge as an experienced developer, who already knows the architecture, relevant files, and established coding practices. Without that understanding, an agent can make unnecessary assumptions, touch too many files, or generate more code than the task requires.

Agents must do a lot of discovery up front and search for different files, which can be expensive, and even more so in a more complicated codebase, Chatterjee tells *The New Stack*. Giving the agent exactly what it needs to know, when it needs to know it, from project standards to historical issues, can reduce exploratory work and help produce code that fits the existing system.  
  
AI code verification then takes place as the agent makes each change, instead of waiting for the PR. This gives the agent a chance to address problems while the task is still contained, before the same mistake repeats elsewhere.  
  
The developer community knows that the earlier you find problems, the cheaper they are to fix in code — and the same is true in the agentic world, says Chatterjee. SonarQube’s analysis runs computationally, he adds, so identifying issues doesn’t require asking a generative AI model to review its own output and consume additional tokens. The agent can spend those tokens fixing verified issues, while the developer gets a cleaner change to assess.

## Loop two: the CI verification loop — scale confidence at merge

The agentic loop catches and fixes issues while the code is being written. [**The CI verification loop**](https://docs.sonarsource.com/agent-centric-development-cycle/in-your-pull-requests-the-ci-verification-loop/ci-verification-loop) then evaluates the proposed change as a whole before it enters the shared codebase or moves towards production.  
  
It provides an independent point for consistent checks on quality, security, dependencies, and maintainability, applying the organization’s standards through a clear quality gate. The first loop should mean fewer problems reach the CI, but the second is crucial because it provides another layer of scrutiny outside the agent that generated it.  
  
The aim isn’t to replace human accountability, but to make accountability workable at agentic volume and speed. The human developer is still responsible, Howlett tells *The New Stack*, but they need to focus on decisions and risks that require human judgment. Reviewing every line of code with the same thoroughness as before isn’t realistic, because there’s too much of it, he adds. With automated checks and AI-assisted review narrowing the field, developers can focus on consequential design, business, and risk decisions rather than reviewing every line with equal intensity.

Of course, scrutiny should match the consequences of failure. A low-risk internal application might need a lighter review process, while software supporting a banking system that moves billions a day requires additional verification layers and more human-focused oversight. AI coding tools can highlight areas of concern, but should sit within a zero-trust, multilayered approach. No single check, including the model that generated the code, is enough on its own.  
  
SonarQube performs automated code analysis, identifying bugs, vulnerabilities, architectural, and complexity issues in real time across all code. [Gitar](https://www.sonarsource.com/products/gitar/), which Sonar acquired in May 2026, adds AI-powered review, including pull request comments, summaries, walkthroughs, and diagrams. Together, these multiple layers help teams scale software development at the speed of agents, while instilling confidence in what ships.

## Loop three: the code maintenance loop — protect ROI over time

AI coding tools don’t operate against a static codebase. The code produced today becomes the context future agents learn from and work on, so poor-quality code, inconsistent patterns, and technical debt can become self-reinforcing.

> “The code produced today becomes the context future agents learn from and work on, so poor-quality code, inconsistent patterns, and technical debt can become self-reinforcing.”

That makes codebase readiness a prerequisite for scaling AI. Chatterjee advises organizations starting to use AI at scale to ensure the code is high-quality and free of bugs and vulnerabilities. Make sure your code is healthy and up to date so agents have a better foundation to work with, Chatterjee tells *The New Stack*, and experiment with a few AI tools at once to find the ones that fit your team.

All three loops are required as each one improves conditions for the next. [**The code maintenance loop**](https://docs.sonarsource.com/agent-centric-development-cycle/in-your-long-living-branches-the-code-maintenance-loop/code-maintenance-loop) must be continuous and consistent. Background analysis and remediation can identify legacy issues, security vulnerabilities, and accumulated technical debt before they hinder future development.  
  
Without that work, agents can spend more time navigating complexity, consume more tokens, and struggle to produce changes that are easy to verify. Maintenance protects the conditions for effective code generation and verification.

## Going after AI-enabled velocity

For leaders scaling AI coding tools, start by agreeing on what good software looks like across the organization. From there, teams can build verification into the workflow.

Chatterjee and Howlett’s advice is to:

* **Define intent and set shared standards.** Establish what a change should achieve, along with the quality, security, reliability, and maintainability expectations it must meet.
* **Prepare and maintain the codebase.** Prioritize existing bugs, vulnerabilities, inconsistent practices, and architectural problems so agents have a stronger foundation to work with. Treat this as ongoing work rather than a one-time cleanup.
* **Experiment in a controlled way.** Compare AI tools and workflows against the same independent standards.
* **Verify earlier.** Connect automated code verification to the agentic workflow so you can identify and fix issues while the code is being written.
* **Guide and govern according to risk.** Give agents relevant context, clear constraints, and escalation boundaries. Apply additional verification layers, approvals, and human scrutiny where failure could have serious consequences.

Howlett, who hosts the weekly developer podcast [*The Next Commit*](https://thenextcommit.substack.com/), suggests measuring whether teams complete more manageable pull requests, release more frequently, and reduce cycle time. He warns against using lines of code as a measure. “If that’s going up a lot, then we’ve got a problem.” More output matters only if quality remains stable or improves.

> “If that’s going up a lot, then we’ve got a problem.”

AI coding’s value depends less on how much code agents produce than on how confidently teams can put that code to work. The three verification loops turn raw generation into trustworthy velocity, enabling AI-driven speed without sacrificing quality. SonarQube provides independent verification, applying that discipline across the tools and environments they choose.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/e36dae7b-cropped-6c610b3e-megan-carnegie-square-sizing-600x600.jpg)

Megan is a London-based independent technology journalist with over a decade of experience writing analytical features for publications like WIRED, Fast Company, and the BBC. She specializes in the world of work, covering Big Tech, startups, AI, recruitment trends, and...

Read more from Megan Carnegie](https://thenewstack.io/author/megan-carnegie/)