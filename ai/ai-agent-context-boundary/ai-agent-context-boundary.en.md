AI coding agents play a major role in software development and delivery, and for good reason. They can investigate bugs, trace dependencies, refactor services, and propose patches without developers needing to assemble all of the relevant context manually. That capability comes courtesy of agents’ appetite for context. To make informed decisions, agents read source code, configuration files, terminal output, error messages, environment information, and more…much, *much* more.

> “Secure, agentic development depends on a security control many teams still lack: preventing secrets from leaking to AI coding agents and becoming model context.”

From a security standpoint, this becomes problematic when agents, in the search for context, inadvertently reach for secrets.

For years, developers have been taught not to commit API keys, database credentials, and tokens to Git. But agentic workflows have created another route for secrets to escape development environments before a commit, code review, or CI job. Depending on its permissions, configuration, and provider architecture, an AI coding agent may read local files or receive pasted content that is then included in data sent to an AI service, and, in the process, developers may never see their credentials leak.

## The quiet path from local files to external systems

Some forms of secrets leakage are obvious. A developer troubleshooting an authentication failure may paste, for example, a failing API call into a chat window, including the token. However serious, this sort of leak is characteristically *human*.

The more consequential escape pathway is quieter. An agent tasked with understanding a project may inspect files in its working directory, including an overlooked .env file, a cloud credential profile, an SSH configuration, or sensitive application logs. In such instances, nothing has necessarily gone wrong from the agent’s perspective; it is doing exactly what it was designed to do: collect context to solve the task at hand.

> “Agentic workflows have created another route for secrets to escape development environments before a commit, code review, or CI job.”

But once a secret becomes part of that context, it may pass through systems outside an organization’s direct control. Depending on the workflow, it can appear in model provider logs, gateway telemetry, prompt histories, or debugging records. Rotating the credential is essential, but it does not erase copies that may already exist in those systems.

This changes the practical definition of a secret leak. The problem is no longer limited to what lands in a repository, but also includes what an autonomous tool reads and forwards while operating on a developer’s machine.

## Why traditional security gates no longer suffice

Most application security programs are built around durable checkpoints: the commit, pull request, build, and deployment. In the agentic era, these checkpoints remain important as they can detect secrets that reach version control and [prevent a bad change](https://thenewstack.io/protect-sensitive-data-and-prevent-bad-practices-in-apache-kafka/) from merging and deploying.

They cannot, on their own, prevent a secret from being included in an [agent prompt before the code ever reaches](https://thenewstack.io/ai-codebase-maturity-model/) a repository.

This highlights an important timing gap. The [2025 Verizon Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/2025-dbir-data-breach-investigations-report.pdf) reports a median of 94 days to remediate leaked secrets discovered in GitHub repositories. In an agent-driven workflow, detection and response need to happen much earlier, and not after a credential is exposed. Still, at the moment it’s about to cross the boundary from local context to an external model.

Bad actors already understand the value of that porous boundary. Recent supply-chain attack campaigns, including Mini Shai-Hulud, have searched developer and CI environments for credentials and configuration data, including AI coding-tool configuration files. These campaigns show that agent configurations and the local context accessible to an agent are valuable targets. AI coding agents can broaden the local data reachable during a session, making even the agent’s context-collection mechanisms an attractive target.

## Treat agent context as an egress surface.

The secure mental model doesn’t frame AI agents as mere code editors, but rather, automated data-movement systems. Its inputs can include far more than the source files a developer is actively editing, and its outputs may involve external services.

That calls for a zero-trust approach to agent context. Before sending a prompt or adding a file to an agent’s working set, organizations should evaluate it for sensitive material. Controls should be deterministic: identify a likely secret, block or redact it, and provide the developer with a clear path to remediate it.

> “Asking an LLM to decide whether to transmit a credential does not create a reliable security boundary.”

Critically, the control should be independent of the model. Asking an LLM to decide whether to transmit a credential does not create a reliable security boundary. Purpose-built secrets detection can inspect prompts and files against known credential patterns and policies, applying a deterministic policy, such as blocking a prompt or file read when it detects a credential-shaped value. For example, Sonar’s [secrets detection](https://www.sonarsource.com/solutions/secrets-detection/) ships alongside dedicated [agent plugins](https://github.com/SonarSource/sonarqube-agent-plugins) to bring that local check into tools such as Claude Code, GitHub Copilot, Codex, and Cursor, so it can flag a credential before a prompt or file read is transmitted to a model provider.

## Build defense in layers, without disrupting your agentic workflow

A legitimate workflow does not involve forcing developers to choose between secure development and useful automation, but instead places fast controls at several points where secrets can escape:

* **In the editor:** Use IDE-integrated secrets detection to flag credentials while they are being written.
* **Before model submission or agent file access:** Where the agent supports it, scan prompt submissions and file reads locally, and block risky operations according to policy.
* **At the command line:** Check generated snippets and local changes in terminal-driven workflows.
* **In pull requests and CI:** Detect secrets that reach the repository and use review, quality gate, and deployment controls to prevent unsafe changes from progressing.
* **In incident response:** Rotate exposed credentials quickly, investigate downstream logs and access, and reduce recurrence through policy and training.

Building defense at the pre-submission layer is an emerging requirement and requires both security *and* usability. Secrets detection must be fast enough to run in developer workflows; a scanner that introduces lengthy pauses may be bypassed or disabled by developers, and it must also have a manageable false-positive rate, or developers may stop trusting it.

Teams should also make their agent permissions and context rules explicit, as broad agent permissions can increase the amount of sensitive local context reachable during a coding session. Consider the following: which directories can an agent read? Are .env files, credential stores, home-directory configurations, and production logs excluded by default? Does the organization route prompts through an approved gateway? What retention, training, and audit settings apply at the provider level? Document and enforce the answers rather than leaving them to individual developer preference.

## Secrets security must shift left.

Prevent secret leakage without hindering AI-assisted development, ensuring the productivity promise of agentic development doesn’t carry significant security implications.

As agents become more autonomous, security standards must follow agents upstream. It’s critical to stop a secret before it becomes context, while it is still local, visible, and easier to control. In the agentic era, code review and CI-level checks will remain essential safety nets. Still, for agent-centric development, the first line of defense [must shift left](https://thenewstack.io/why-testing-must-shift-left-for-microservices/): to the instant an AI coding tool determines what to read and what to transmit. *That* is the control modern development teams need to implement now.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/08/7bba6f57-cropped-3d190a8f-tns-headshot-600x600.jpg)

Taylor Luttrell-Williams is a Developer Content Engineer at Sonar, where he leverages a background in full stack software development and DevOps, and a passion for teaching, to produce deep, technical content. He connects Sonar’s products to the global developer community,...

Read more from Taylor Luttrell-Williams](https://thenewstack.io/author/taylor-luttrell-williams/)