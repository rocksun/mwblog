**The appeal of an autonomous coding agent is that you hand it a task**, give it access to your repository and tools, and stay out of its way while it works. Google’s latest Gemini CLI release carves out specific moments when the agent now has to stop and wait for you.

[Gemini CLI 0.61.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.61.0), released Wednesday, requires explicit confirmation before the agent edits build configuration files, runs build or test commands after such an edit, or executes shell commands whose arguments appear to come from untrusted external content. The same release separately hardens Gemini CLI’s optional sandbox so that host credentials and configuration stay out of reach of whatever runs inside it.

Giving a coding agent more authority to modify and execute code also gives an attacker more ways to turn that authority against the developer. Gemini CLI 0.61.0 puts a human back in the loop at some of those points.

## Security fixes, in public

Google announced at I/O in May that it would move Gemini CLI’s Pro, Ultra, and free-tier users to its closed-source Antigravity CLI, and since June 18, the open-source tool has served mainly enterprise customers and developers with paid API keys. The company said Gemini CLI would continue to get model updates, bug fixes, and security patches. Those security changes are still developed in public, and the pull requests behind version 0.61.0 show exactly what Google was worried about.

## Build files become attack vectors

A change to package.json, Makefile, pyproject.toml or a Bazel BUILD file can pull in a dependency or trigger a script. Gemini CLI can make those edits using information from [web searches and external tools, then run shell commands](https://thenewstack.io/coding-with-the-gemini-cli-tool/). If documentation fetched while fixing a bug contains hidden instructions to add a postinstall script to package.json, the agent could make the edit, run the project’s test suite, and execute the malicious code without the developer ever typing the command.

> Giving a coding agent more authority to modify and execute code also gives an attacker more ways to turn that authority against the developer.

[Pull request #29250](https://github.com/google-gemini/gemini-cli/pull/29250), titled “prevent indirect prompt injection via build file modifications and untrusted flags,” targets that sequence directly. Edits to recognized build files now require confirmation, and Gemini CLI tracks which build files change during a session so it holds any later build or test command, such as npm run, make, or cargo, for explicit approval. The confirmation dialog also shows full build-file diffs rather than truncating them.

## Untrusted arguments need approval

The second check covers command arguments. Gemini CLI now treats content from web fetches, MCP server responses, Google Docs, and Buganizer, Google’s internal issue tracker, as untrusted context, and it asks before running any shell command whose flags or arguments match tokens from that content. In both cases, the prompt drops the persistent approval options, so a developer can’t grant a standing “always allow” for these actions.

The pull request ties the changes to restricted workspace mode, the safe mode Gemini CLI applies to folders a user hasn’t marked as trusted, and it doesn’t spell out how the checks behave in a trusted folder or under auto-approval.

The argument check matches tokens rather than tracing the provenance of every value, and the pull request’s review history shows how hard that is to get right. Google’s automated reviewer flagged several workarounds in earlier versions, including quoted arguments, environment-variable prefixes, shell redirection targets, and Windows path handling, all of which were addressed before the change merged on September 11.

## Sandbox keeps credentials out

[Pull request #29214](https://github.com/google-gemini/gemini-cli/pull/29214) tightens Gemini CLI’s sandbox. When the sandbox runs through Docker, Podman, LXC, or macOS Seatbelt, the host’s ~/.gemini directory is no longer mounted inside it. Instead, the CLI passes in a sanitized copy of the user’s settings with API keys, hooks, and custom tool commands stripped out. It also blocks the sandbox from launching in sensitive locations such as the home directory, while new Seatbelt rules deny access to OAuth credentials, trusted-folder decisions, and .env files.

Google’s [sandboxing documentation](https://google-gemini.github.io/gemini-cli/docs/cli/sandbox.html) calls the feature a security barrier between AI operations and the host system, while cautioning that it reduces risk without eliminating it. The two pull requests show why both layers are needed. The sandbox limits what a process can reach once it runs, and the confirmation requirements decide whether the agent gets to take a sensitive action in the first place. Build files make the gap concrete: the sandbox mounts the project directory so the agent can edit it, meaning a poisoned package.json written inside the sandbox still sits in the repository when a developer or a CI job later runs the build outside it.

> …a poisoned package.json written inside the sandbox is still sitting in the repository when a developer or a CI job later runs the build outside of it.

Gemini CLI already gives developers ways to decide how much the agent does on its own, from [hooks that run deterministic checks at fixed points in the agent’s workflow](https://thenewstack.io/gemini-cli-gets-its-hooks-into-the-agentic-development-loop/) to an MCP server trust setting that, according to [Google’s documentation](https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html), bypasses all tool call confirmations for that server. Trust granted once can age badly, though, as [tool-poisoning and rug-pull attacks on MCP servers](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/) have shown when a tool approved on one day starts returning attacker-controlled content later.

> Trust granted once can age badly… when a tool approved on one day starts returning attacker-controlled content later.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)