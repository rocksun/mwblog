**Anthropic built Claude Duet**, an AI assistant that monitors your connected apps and works on tasks in the background, to decide what needs your attention *without* being asked. A week after its October 21 debut, the frontier lab with [an IPO in its sights](https://thenewstack.io/claude-codes-enterprise-20-to-1/) has shared with *The New Stack* how it is testing whether Duet gets those priorities right.

Anthropic has developed internal graders to assess how Duet prioritizes tasks, though urgency can be subjective. The stakes rise when an agent manages work across email, calendars, and B2B apps. Duet can remain within its permissions and still get its priorities wrong.

Powered by [Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/), Duet can prepare work and flag items it thinks need attention without waiting for instructions. Anthropic has been testing that approach with its own employees, using their day-to-day work to see how Duet handles competing priorities.

## Testing Duet’s judgment

“After using Duet for our day-to-day work at Anthropic, we calibrated graders that assess correctness in task prioritization, and we run them offline against cases representative of internal use and early external testing,” a company representative tells *The New Stack*.

Those graders measure whether Duet can distinguish what deserves attention from what can wait, though Anthropic acknowledges the difficulty of evaluating those decisions.

“Urgency is an inherently subjective call, so we found building an eval for it imperfect but quite helpful,” a company representative says.

Duet can spot tasks like an approaching deadline or an email requiring a reply, but it doesn’t always know which task should be a priority, and the company admits the agent can misread conversations or misjudge urgency. Anthropic’s public launch and support materials do not say how often that happens.

## Testing Duet’s safeguards

On October 23, two days after Duet’s debut, Anthropic published a [closer look at its safety, privacy, and security safeguards](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security). Duet team lead Karan Ahuja pointed to the post while addressing feedback received through messages, emails, and public posts.

Anthropic keeps the part of Duet that does the work separate from the part that checks whether the work matches what the user actually asked for.

“A separate, automated check runs alongside each action, built on the auto mode classifier from Claude Code and extended for Claude Duet,” the rep tells *The New Stack*. “It assesses whether the action matches your intent.”

Because that check runs independently of the model performing the task, Anthropic says instructions hidden in a webpage can’t directly steer the classifier’s decision.

Anthropic says an outside firm penetration-tested Duet, but its public materials don’t show how reliably the separate check catches actions outside the user’s intent. Related research illustrates the difficulty of enforcing this agent scope: Researchers found that [removing a prompt section defining authorized and out-of-scope actions](https://thenewstack.io/coding-agents-overstep-scope/) in Claude Code tests increased out-of-scope actions, although that study did not test Duet’s separate classifier.

## Limiting prompt injection

The separation is designed to reduce prompt injection, where malicious instructions embedded in emails, documents, or webpages try to redirect an agent. Researchers have already explored this risk by [leaving hidden messages for rogue agents](https://thenewstack.io/rogue-ai-agent-fleet-tencent/) and observing how they responded. Anthropic’s support materials still tell users to review drafts and approval requests because Duet may encounter prompt injection.

Duet uses the apps already connected to a user’s Claude account. Disconnecting an app stops new access, but information Duet has already stored in memory remains until the user resets it. Anthropic says Duet never sees passwords, browser cookies, or sign-in tokens, and can’t save them to memory.

Duet is designed to seek approval before actions such as making payments or deleting items. Sharing private health or financial information requires consent, though an explicit request to share it can count as that consent, while trading securities, moving money between bank accounts, and accessing someone else’s account remain off-limits entirely.

## Summaries, not surveillance

Users can see what Duet has finished and what’s still underway through its task list, with a separate page for each job. They can also give the agent new instructions while it’s working.

But users can’t see everything happening behind the scenes. During the research preview, users can’t watch Duet work in its cloud browser or take over the browser. Users can review its task activity and approve actions, but they can’t inspect each browser step as it happens. (The public launch and support materials do not describe a way to undo completed actions across connected apps.)

## What background work costs

Duet uses the same allowance as regular Claude conversations, so background work counts against a subscriber’s plan limits. How much it uses depends on the job.

“Larger tasks, like building a financial model or a deck, will require more model turns and background work,” the Anthropic rep tells *The New Stack*.

Even Duet’s routine checks across connected apps count toward the five-hour session and weekly limits.

Those checks happen every few hours rather than continuously, partly to avoid using up a subscriber’s allowance. The downside is that something urgent could arrive between checks and go unnoticed until the next one. Checking more often would use more resources, while checking less often could leave users waiting longer for an alert. (Anthropic’s public launch and support materials do not quantify how much of a typical subscriber’s usage goes toward background activity.)

Duet’s research preview is available by waitlist to U.S. Pro and Max subscribers. Anthropic employees have used it to work through to-do lists while they’re away and talk through workloads on walks, though Anthropic admits the agent isn’t as reliable with consumer tasks like booking tickets.

The company expects to keep adjusting the product as testing continues.

[Cyber Security Expert
Step by step guide to becoming a Cyber Security Expert in 2026

Fundamental IT Skills
CTFs (Capture the Flag)
Operating Systems
Networking Knowledge
Certifications
Security Skills and Knowledge
Cloud Skills and Knowledge
Programming Skills](https://roadmap.sh/cyber-security?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=claude-duet-agent-judgment)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)