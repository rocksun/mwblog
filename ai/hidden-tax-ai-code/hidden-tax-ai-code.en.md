AI coding tools haven’t removed bottlenecks. They’ve moved them to the review queue, putting more pressure on senior engineers.

This result isn’t surprising: As teams grow, code generation increases, but review expertise doesn’t scale the same way. If you measure AI adoption by MR (merge request) volume, lines of code, or seat usage, you’re only tracking inputs, not the real bottleneck.

The 2025 DORA (DevOps Research and Assessment) data show that key delivery metrics such as lead time, deployment frequency, change failure rate, and MTTR haven’t improved with increased use of AI tools. Teams with the fewest change failures are also [the least likely to use AI-assisted development tools](https://www.slashdata.co/post/ai-software-performance-dora-metrics-reveal). This doesn’t mean AI tools are harmful, but it’s a reminder not to assume that more MRs mean higher productivity.

## The review queue became the sprint plan

Recently, I worked with a customer’s AI enablement engineering team to review their delivery metrics. Their [AI coding](https://thenewstack.io/ai-generated-code-invisible/) tool rollout showed strong adoption, but segmenting cycle time by reviewer revealed a different picture. It turned out that engineers with the most system knowledge had review queues so large that reviewing became their primary responsibility, limiting their capacity for design and architecture work.

This pattern is consistent across teams: MR volume increases, review times lengthen, and senior engineers have less time for design. The workload concentrates because a small group handles deep system context, security-sensitive areas, and ownership boundaries. Mid-level engineers cannot step in to review critical changes for senior reviewers.

The primary cost is attention fragmentation. Senior engineers face frequent interruptions, leading to predictable declines in quality: superficial approvals due to long queues, or delays when complex MRs wait for available time.

## Passing CI does not mean it is cheap to review

Automated checks can handle more work, but human judgment doesn’t scale the same way. Even if a pipeline passes, reviewers in regulated environments still need to understand the intent, assess the impact, verify authorization boundaries, examine failure behavior, and confirm audit readiness.

> “Automated checks can handle more work, but human judgment doesn’t scale the same way.”

AI-generated code increases the burden of verifying plausible correctness. The code may compile, pass tests, and meet linting standards, but reviewers must still confirm it fulfills the intended purpose, handles data classification properly, and avoids policy violations. This verification often takes longer when [code is generated](https://thenewstack.io/in-a-typescript-world-code-generation-is-key-for-api-sdks/) for syntactic correctness rather than system-level intent. As queues grow, reviewers spend less time per MR, creating pressure on both speed and quality.

## Generation scales, judgment doesn’t

It’s worth acknowledging that AI coding tools do contribute to productivity. They can produce code quickly, accelerate refactoring, and enable teams to address more features per sprint. That is real value for development teams.

However, review capacity is constrained by limited context and personal accountability. When a senior engineer approves a change to an identity service in a regulated environment, they assume organizational risk. That responsibility doesn’t change regardless of how quickly the code was generated.

> “It’s not yet true that AI-assisted review can reliably substitute for the contextual judgment that makes senior review valuable.”

“Just add AI code review” is the obvious next move. But it’s not yet true that AI-assisted review can reliably substitute for the contextual judgment that makes senior review valuable in high-risk codepaths. In practice, accelerating generation without redesigning the review will not solve the problem.

## When AI review actually closed the gap

In one case, AI-assisted review did reduce the workload for senior engineers. The team already had solid CI, clear code ownership, consistent service templates, and review standards written out as checklists. The improvement came from using AI for pre-triage: summarizing intent, flagging policy-related file changes, and matching diffs to known patterns. Senior reviewers focused on high-risk changes, speeding up cycle times without increasing defects.

Conversely, I’ve seen failure when AI coding was broadly implemented without workflow adjustments. In one regulated company, the senior review load increased sharply. Throttling code generation and requiring fewer, larger MRs only created larger batch sizes and harder reviews. The effective solution was workflow redesign: enforcing strict scope rules for small diffs, requiring author summaries and risk declarations, automating policy checks, and rotating trained “risk captains” to handle high-risk triage. Most changes became low-risk by design, with experts focusing on exceptions.

The most important factor wasn’t the tool. It had clear review standards and workflows, managed with ownership, iteration, and feedback. AI strengthened existing workflows. Where standards are loose, AI triage adds noise that reviewers ignore.

## Where the tax compounds: seams, exceptions, and risk ownership

The hardest reviews are about policy and system boundaries: data classification, logging, authorization, and failure handling. At a global bank with more than 4,000 engineers across security, platform, and delivery teams, each group tracked its own metrics. Security cut vulnerabilities, platform improved uptime, engineering sped up deployments, but handoffs between teams caused significant delays. No one owned the full cycle time.

AI-generated volume can worsen this dynamic by increasing boundary-crossing changes unless workflows are designed to contain them. Even adopting smaller MRs as a best practice can hinder flow if each still requires cross-team review, security approval, or compliance documentation.

## Measuring the constraint instead of the output

If you don’t measure reviewer capacity, you may misinterpret how AI is affecting your team. These metrics help distinguish real throughput from congestion:

* MR cycle time segmented by reviewer, not averaged across the org
* Reviewer load per senior engineer: reviews per day, active queue depth, hours spent in review
* Defect escape rate, severity-weighted, and split by AI-assisted versus non-AI-assisted MRs

Distribution matters more than averages. A small number of overloaded experts can delay critical systems even when overall metrics look healthy. The key indicator is senior engineers regaining design time while maintaining quality, not the number of MRs opened.

## Adding structure through workflow design

![Diagram showing adjustments to the review workflow](https://cdn.thenewstack.io/media/2026/04/c232464d-1-1024x648.png)

The solution isn’t to ban AI or rubber-stamp approvals. It’s to introduce structure so that increased AI-generated volume doesn’t automatically increase senior [engineers’ cognitive load](https://thenewstack.io/cyberark-decreases-cognitive-load-with-platform-engineering/). An example framework could be:

* Implement pre-review triage as a core step in the workflow. AI can summarize intent, map affected files to risk areas, and flag missing tests, enabling reviewers to start with a clear risk assessment.
* Establish risk-tiered review paths so that routine changes go to peer review, while changes involving authorization, data handling, or cross-service boundaries are routed to senior reviewers.
* Attach evidence directly to the MR: threat model notes, data-handling annotations, test results, and policy-check outcomes.
* Enforce work-in-progress limits for designated reviewers through CODEOWNERS rules and workflow automation.

## The decision rule for expanding AI usage

A useful leadership test: after AI adoption, did time-in-review for high-risk changes decrease, or did the workload concentrate among fewer senior reviewers? If the latter, code generation is increasing against fixed review capacity.

Treat senior review attention as a governed resource, with explicit limits, routing rules, and escalation procedures. Only expand AI-assisted code generation to new repositories or teams when reviewer workload and defect escape rates remain within acceptable limits.

> “At the start of each week, ask one question: Who are the two people currently limiting the merging of high-risk changes, and what is their current review queue depth?”

At the start of each week, ask one question: Who are the two people currently limiting the merging of high-risk changes, and what is their current review queue depth? If you can’t answer it, the system lacks visibility. If the number grows each week, you’ve found your hidden tax.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/81408769-brianwald.png)

Brian Wald is Head of Global Field CTO org at GitLab. He leads a dynamic team of Field CTOs dedicated to transforming enterprise software development practices.

Read more from Brian Wald](https://thenewstack.io/author/brian-wald/)