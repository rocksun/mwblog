**A command as ordinary as** `git diff` can become a problem for an AI coding agent once a variable gets involved.

Take `git diff $base`. If `$base` contains a commit hash, the command behaves as expected. But if it resolves to `--output=/some/file`, Git can write the result to the filesystem. LM Studio built Auto Review to catch cases like this before Bionic runs the command, turning to another language model only when it can’t determine whether it’s safe.

In a [blog post](https://lmstudio.ai/blog/how-auto-review-works) published Thursday, LM Studio said this first layer cleared as many as 82% of Bionic’s commands without another model call, although the author described the figure as anecdotal rather than a benchmark.

Bionic does this by turning shell commands into abstract syntax trees (ASTs), following variables and nested commands to see what they could affect. LM Studio has built 11,651 test cases to catch the many ways that analysis can go wrong.

> A command as ordinary as `git diff` can become a problem for an AI coding agent once a variable gets involved.

## Parsing structure, not strings

Searching for dangerous strings only gets you so far because shell commands can change depending on the variables, redirects and other commands inside them.

Bionic’s Shell Judge gets around that by looking at the structure of the command instead. It uses the mvdan/sh parser for Bash, Zsh and SH, while PowerShell uses its own AST support. The Judge then works out what LM Studio calls the command’s “capabilities,” essentially what the command could read or change.

It can also follow a value from one command to the next. If an agent uses `git merge-base` to find a common ancestor commit and feeds the result into `git diff`, for example, the Judge keeps track of that result when it evaluates the second command. If there are several possible values, Bionic follows up to 1,000 of them before it stops trying to account for every possibility.

## 11,651 tests for CLI quirks

Then there’s the fact that command-line tools have their own rules. `ls -la`, for example, treats `-la` as multiple flags bundled together, while LM Studio points out that TypeScript’s `tsc -vh` doesn’t behave the same as running it with `-v` and `-h`.

So parsing the shell syntax only gets Bionic partway there. The Shell Judge also has to understand how the individual tool will interpret what comes after the command.

That helps explain why LM Studio has already built 11,651 test cases, covering malformed commands and the quirks in how individual tools handle their arguments.

## When the reviewer gets swayed

> LM Studio found that by just asking the reviewer whether a command should run didn’t work well because the model sometimes approved risky actions because they seemed necessary to complete the user’s request.

Anything the Shell Judge can’t clear goes to the Shell Reviewer, which is a separate AI agent that evaluates the command in the context of the conversation.

LM Studio found that just asking the reviewer whether a command should run didn’t work well because the model sometimes approved risky actions because they seemed necessary to complete the user’s request.

The reviewer now rates each command for risk, authorization and correctness without knowing what scores are needed to pass.

## Trust assumptions remain open

The Shell Reviewer needs enough of the conversation to know whether the user authorized a command, which creates another opening for prompt injection. LM Studio excludes tool results, so instructions hidden in a webpage or file aren’t passed directly to the reviewer, but it still sees assistant messages. If Bionic has already been compromised, those messages could carry malicious instructions.

> If Bionic has already been compromised, those messages could carry malicious instructions with them.

The Shell Judge has its own blind spots because it assumes executables such as `git` haven’t been compromised and doesn’t account for malicious configuration that could change how a command behaves. A recent [npm supply chain attack](https://thenewstack.io/npm-supply-chain-worm-attack/) showed how legitimate-looking provenance signals can be used to hide malicious payloads.

Those limits become more important as coding agents get more freedom to act. Google’s Gemini coding agent, for example, recently [expanded beyond its IDE boundaries](https://thenewstack.io/google-antigravity-ide-extensions/), giving agents more opportunities to run commands and make changes without a developer doing each step manually.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)