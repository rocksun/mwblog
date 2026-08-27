**Shopify CEO [Tobi Lütke](https://www.linkedin.com/in/tobiaslutke/) is considering banning** Claude Code at the company, but not because he thinks Anthropic’s coding agent isn’t good. The problem, he says, is a Markdown file.

“I’m thinking about banning Claude Code at Shopify until they change their mind and read AGENTS.md and .agents/skills etc.,” Lütke posted Tuesday on [X.](https://x.com/tobi/status/2092259436538495186)

> “I’m thinking about banning Claude Code at Shopify until they change their mind and read AGENTS.md and .agents/skills etc.”

And while this might sound like a small disagreement over how an AI coding tool is configured, at a company the size of Shopify, even a small difference can quickly become a much bigger issue.

Shopify has thousands of developers working in a massive monorepo, and because they don’t all use the same AI coding tools, each agent needs to pick up the right instructions for whatever part of the codebase it happens to be working in. If one coding agent doesn’t pick up the same instructions as the others, developers can end up with [agents operating under different rules](https://thenewstack.io/go-language-ai-agents/).

“Agents and Claude files are recursively applied through the tree,” Lütke wrote in a [follow-up post](https://x.com/tobi/status/2092308116524138711). “With thousands of [developers] in a mono repo, it just does happen that one directory is missing one of the two files and this means that a subset of devs work with lobotomy.”

Shopify has built automation to work around the discrepancy, but Lütke’s core objection is that its engineers shouldn’t have to.

“We fix this with automation, but it’s a stupid complexity tax that shouldn’t have to be paid,” he writes.

> “We fix this with automation, but it’s a stupid complexity tax that shouldn’t have to be paid.”

## The files telling AI agents how to work

Now that coding agents are more capable, engineering teams have needed ways to provide persistent instructions for a codebase, which is where files such as AGENTS.md and CLAUDE.md come in.

Developers can put things like build commands, testing requirements, and coding conventions directly into a file in the repository, so the agent has that information as it works, rather than needing to be told every time. The problem is that coding tools haven’t all standardized on the same convention.

OpenAI introduced AGENTS.md in August 2025 to give coding agents instructions specific to a project; by December, OpenAI said it was being used by more than 60,000 open-source projects and agent frameworks, with support from tools including Codex, Cursor, Gemini CLI, GitHub Copilot, Jules and VS Code. OpenAI later handed the format over to the Agentic AI Foundation under the Linux Foundation.

> “Agents and Claude files are recursively applied through the tree… one directory is missing one of the two files and this means that a subset of devs work with lobotomy.”

## Where AGENTS.md and CLAUDE.md diverge

Claude Code does things differently, however. It uses CLAUDE.md for project instructions and can pick up those files from different parts of a repository as it works. What it doesn’t do is read AGENTS.md natively, something developers have been asking Anthropic to change.

Anthropic does provide workarounds, including importing AGENTS.md from a CLAUDE.md file or using symbolic links, but in a large repository, teams still have to make sure those instructions stay in sync across all the places they appear.

## Platform teams bear the cost

In a large codebase, those instructions can live throughout the directory tree, giving an agent different guidance depending on what it’s working on. Claude Code does this with CLAUDE.md, picking up relevant instruction files as it moves through the repository.

That is also why Lütke’s example carries so much weight. If a directory contains instructions for tools reading AGENTS.md but the equivalent instructions aren’t available to Claude Code, developers using Claude can end up working without the same context.

[Developers have been asking Anthropic to support AGENTS.md for nearly a year.](https://github.com/anthropics/claude-code/issues/7060). More recent requests have continued to push for native support, including [one focused on recursive AGENTS.md discovery](https://github.com/anthropics/claude-code/issues/69151), which Anthropic has closed as “not planned.”

And Shopify isn’t alone. A [2026 study of 2,926 GitHub repositories](https://arxiv.org/abs/2602.14690) found that context files are now the most common way developers give coding agents instructions, with AGENTS.md already being used across several different tools.

Shopify has already built automation to deal with the problem, a point Lütke clearly made, stressing that as companies bring more coding agents into the same repositories, keeping those tools on the same page becomes one more job for platform teams.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)