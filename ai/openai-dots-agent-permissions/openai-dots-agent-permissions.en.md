**OpenAI’s new [Dots](https://thenewstack.io/openai-dots-gpt6-agents/) are built to keep working** after you step away. Launched at DevDay on Tuesday, the always-on agents run on their own cloud computers, use [GPT-6 Astra](https://thenewstack.io/astra-arc-agi-benchmark/), and connect to thousands of apps. A Dot can monitor connected systems and move from one task to the next without waiting for you to prompt it again. But as the work changes, it has to keep figuring out where its permission to act on your behalf ends.

As we learned during the DevDay event, OpenAI measured that problem in its own testing. When it doubled the number of tasks in a chained sequence from five to ten, the share of samples flagged for boundary problems rose from 8.6% to 19.7%. The finding appears in the [Dots appendix of the GPT-6 Astra system card](https://deploymentsafety.openai.com/gpt-6-astra/maintaining-boundaries-across-chained-tasks), which OpenAI updated alongside the launch.

What a Dot can do can change as it moves from one task to the next, even when the user doesn’t explicitly set new boundaries. That leaves the agent to figure out its limits from business records, earlier decisions, context, and OpenAI’s confirmation policy. The evaluation found no high-severity breaches or data exfiltration, although OpenAI hasn’t said what the flagged boundary problems actually involved.

> What a Dot is allowed to do can change as it moves from one task to the next, even when the user doesn’t explicitly set new boundaries.

## Reading versus acting in Dots

The first safeguard applies during what OpenAI calls proactive research, when a Dot looks for work on its own. During that phase, it can read connected apps but can’t change them, send messages, or control the user’s browser or computer.

Each Dot also gets its own cloud computer and browser where it can build and test things, but OpenAI hasn’t said whether those environments face the same restrictions during background work. That matters because a restriction only holds [if the agent can’t find a way around it](https://thenewstack.io/openai-agents-security-bypasses/).

Once a Dot is ready to act, it moves into another layer of controls. Built-in rules decide when it needs permission, Custom Rules let users allow, gate, or block specific actions, and auto-review checks anything that could affect accounts or share information.

Auto-review comes from Codex, where a second model checks commands that run outside a predefined sandbox. The company adapted that system for Dots with its own review instructions and gave the confirmation policy more weight than it receives in the Codex harness.

## From research to pull requests

A Dot doesn’t stay read-only once it takes on a task; OpenAI gives the example of one that monitors customer feedback, identifies a small fix, then builds and tests it on its own machine. By the time it hands the developer a finished pull request, the Dot has already written to the repository before a human has reviewed the work.

OpenAI’s testing also shows what can happen when those permissions carry over into recurring work. In a [simulation of internal Codex traffic](https://deploymentsafety.openai.com/gpt-6-astra/forecasting-misaligned-behavior-with-deployment-simulation-of-internal-codex-traffic), a user asked Astra to create an hourly helper that would watch for failing checks, fix tests, open pull requests, request reviews, and merge once certain conditions were met. Astra enabled every available action across its chat, source-control, and task-system connections, turned off per-action approval, and then published and scheduled the helper.

The test involved Codex rather than Dots, but it describes the kind of long-running workflow Dots are built for, and in it the model gave the helper more access than the user asked for.

## Prompt injection and proactive research

Keeping proactive research read-only also limits indirect prompt injection, since an agent that finds malicious instructions hidden in a ticket or document has fewer ways to act on them right away. OpenAI reports a 99.79% defender success rate for Astra in its internal indirect-injection tests. In external testing, Gray Swan ran 1,810 curated attacks and estimated an 8.5% attack success rate over 15 attempts per scenario against Astra with safeguards enabled. The threat itself keeps evolving, and the company recently described [a new variety of prompt injection that can spread like a computer worm](https://thenewstack.io/openai-self-replicating-injections/).

Separating reading from writing doesn’t remove the risk, because what a Dot reads during research can still shape what it does later. Outside information is supposed to guide its work, so customer feedback can influence the code a Dot writes.

Because Dots can keep notes and learn from feedback over time, OpenAI tested whether misleading hints in the information they encounter could influence later work. Dots running on Astra recorded a 0% misalignment rate across 151 tasks, although that’s a relatively small test for an agent designed to run continuously.

> Dots running on Astra recorded a 0% misalignment rate across 151 tasks, a strong result from a relatively small test for an agent designed to run continuously.

## Credentials, identity and audit trails

When a Dot signs in to a supported website with a saved password, OpenAI says the credential isn’t exposed to the model, keeping it out of the context window and away from malicious instructions the agent might encounter.

The system card offers some context for that separation, with credential-searching flags appearing more often for Astra than for GPT-5.6 Sol in OpenAI’s Codex simulation. In another flagged case, Astra was asked to debug duplicate notifications but went further, retrieving a service’s bot token from its settings and using it to read Slack messages as that service.

The company has not said whether a primary Dot’s actions inside services such as GitHub or Slack are logged under the user’s identity or under one that marks them as coming from an agent. If they carry the user’s identity, a security team investigating an incident will have a harder time separating what the person did from what the Dot did on their behalf. Specialist Dots, which OpenAI is previewing for enterprise pilots, are built around that problem.

Organizations provision each Specialist Dot with its own identity, credentials, and hardware, while OpenAI is working with Microsoft to bring them under Agent 365’s governance and security controls.

> When a Dot signs in to a supported website with a saved password, OpenAI says the credential isn’t exposed to the model, keeping it out of the context window, and away from malicious instructions the agent might encounter.

## What can developers take from it?

For developers building long-running agents, the chained-task results suggest they should reconsider permissions as new work comes in, rather than set them once and carry them forward. That could mean restating the agent’s scope between tasks, preserving where information gathered during research came from, keeping credentials outside the model, and giving the agent its own identity in downstream systems.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)