Google wants to give developers a comprehensive, functional AI software development toolkit. As such, this month the company has added a new automated review feature to its [Google Conductor AI](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/) extension.

A context-driven development extension currently available in preview for Gemini CLI, Conductor helps create formal specifications alongside a developer’s code in the form of persistent version-controlled markdown files, the lightweight, portable text format much beloved of programmers.

[According to Google](https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/), Conductor allows developers to plan before they build, review plans before code is written, and keep the human developer firmly in the driver’s seat.

The new automated review extension for Conductor has been designed to understand and interpret a codebase’s specifications and guidelines, and subsequently generate post-implementation [code quality and compliance](https://thenewstack.io/checks-by-google-ai-powered-compliance-for-apps-and-code/) reports.

> “The philosophy behind Conductor is simple: control your code.”

Why is Google doing this? Because in a world where even non-technical businesspeople are becoming aware of AI-driven code and its potential to automate decisions without human oversight, Google needs to ram home its central message, which is put plainly in [the blog post](https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/#:~:text=The%20philosophy%20behind%20Conductor%20is%20simple%3A%20control%20your%20code.) about the update: “The philosophy behind Conductor is simple: control your code.”

## Sharper, but safer

With Anthropic also implementing automated review capabilities for Cloud Code to oversee security, logic, and integration, how does the programming community view these new, supposedly sharper but also safer tools in terms of real-world practicality?

Nigel Douglas, head of developer relations at Cloudsmith, explains it with a colorful analogy about a chainsaw.

“An AI coding CLI without automated reviews is like a chainsaw without an ‘off’ button, but, unfortunately, these changes focus only on the code that’s been generated, i.e., completely skipping the upstream components it’s pulling in. If an AI coding assistant suggests a package that doesn’t exist or has already been infected with malware, a [developer will end up shipping vulnerabilities far faster](https://thenewstack.io/think-like-a-developer-to-help-dev-teams-ship-faster/) than anyone can catch them,” Douglas tells *The New Stack*.

> “An AI coding CLI without automated reviews is like a chainsaw without an ‘off’ button…”

Douglas reminds us that peer reviews can’t work the way they’ve always worked when LLMs can generate thousands of lines of functional code in minutes. It’s a computational process that far outstrips human reading ability. He insists that the current state of AI development tools means automated reviews are just one step; as such, he calls for a human in the loop at the pull request stage, to move contributions back from ‘trusted output’ to ‘proposed draft requiring expert verification’.

## A (mere) meaningful milestone

“Google’s continued investment in improving the quality and reliability of AI-generated code is an important step for the industry. The conversation is shifting from whether AI can [generate code to whether it can be trusted](https://thenewstack.io/ai-code-generation-trust-and-verify-always/) to evaluate and improve it… so automated review is a meaningful milestone in that progression,” said Chris du Toit, CMO of Tabnine.

What du Toit says his team is seeing across enterprises is that trust ultimately comes from context, understanding how code fits into real systems, real dependencies, and real operational constraints.

“As AI moves from assisting developers to performing real engineering work, organizations will increasingly need an organizational intelligence layer that gives AI a structured understanding of their environment, enabling automated reviews to operate safely and consistently at scale,” offered du Toit, in response to the new features.

## Brownfield dirty work

While Tabnine analyzes the context of an entire codebase (not just a single line of code) and can suggest actions related to everything from a single variable name to entire functions and test cases, Google Conductor is not without capabilities at this level. Conductor’s context-driven development approach has been put in place to ensure AI services understand a project’s architecture, rules, and history.

Google also makes it clear that Conductor can be applied to brownfield projects already in motion through its workspace-wide scan capability. The cloud giant confirms that Conductor’s scan enables it to identify programming languages, folder structures, and existing patterns to seed Markdown files. This, says the company, allows it to “respect your specific coding style” once applied, even in a massive codebase.

Conor Sherman, CISO in residence at Sysdig, is equally upbeat and cautious about code assistants. He says that one concrete [risk of the agentic coding](https://thenewstack.io/ai-security-agents-combat-ai-generated-code-risks/) system space is the specter of phantom dependencies, also sometimes known as “slopsquatting” by some.

## Slopsquatting shoddiness

“This is where a coding agent invents a believable package or component name that does not exist. A threat actor can then publish a malicious package under that exact hallucinated name. If the agent — or a developer trusting the agent — installs it, you have just pulled attacker code into your build pipeline. From there, it can go into production,” explained Sherman.

Sysdig recommends treating AI agents like highly privileged insiders. This means giving each agent a strongly scoped identity, least-privilege permissions, and hardened boundaries around what it can install, fetch, or execute. Then make the audit trail non-negotiable: if you cannot answer what the agent did, when it did it, and under whose authority, you do not have control of that system.

Separately, Sherman points to Anthropic’s safety report (last November), which has shown that more capable models can be pushed toward harmful, high-agency behavior in certain evaluation settings. That matters because the same general capability that speeds up benign work can also compress offensive timelines at scale.

## Instruction adherence as a metric

Mohith Shrivastava, principal developer advocate at Salesforce, thinks that the question of whether an agentic service like Google’s Conductor is working effectively will now shift from an assessment of its output, onward to a more defined and measurable analysis of ‘instruction adherence’… and that this will become the industry’s new key reliability metric for AI governance.

“Enterprises will demand probabilistic adherence scores — categorized as high, low, or uncertain — to enable developers to refine their instructions accordingly and gain the confidence of CIOs in their agents’ reliability and trustworthiness. This focus on a quantitative measure of compliance will be essential for scaling enterprise agents and avoiding costly errors, setting a new benchmark for safe and reliable AI,” said Shrivastava.

Google’s final words (for now) in this space are belief in context-driven development and treating developer documentation as the source of truth, as a route to higher-quality outcomes for complex projects. Industry-wide, there is consensus on what we need to do next: it’s not about optimizing code generation per se; it’s about doing so in an architecturally compliant, resource-efficient, and secure way.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)