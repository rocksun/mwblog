Anthropic shipped [Claude Opus 4.8](https://thenewstack.io/claude-opus-48-release/) on May 28, and with it came dynamic workflows in Claude Code. This fully testable research preview feature lets Claude act like a team of developers rather than a one-AI show. Dynamic workflows enable Claude to write its own orchestration scripts, spin up hundreds of parallel subagents in a single session, and verify outputs. To quote [Anthropic](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code): “Work you’d normally plan in quarters now finishes in days.”

What makes dynamic workflows architecturally different from a standard single-agent is where the orchestration instructions reside. In a regular subagent session, Claude decides, turn by turn, what to do next, and every intermediate result is added to its context window. With dynamic workflows, Claude writes a script that handles the orchestration itself, so the context window receives only the final answer.

According to Anthropic’s [documentation](http://code.claude.com/docs/en/workflows), moving the orchestration instructions into a separate script rather than into Claude’s context window makes large parallel runs feasible. [Thariq Shihipar](https://www.linkedin.com/in/thariqshihipar/), who works on Claude Code at Anthropic, posted this superlative on [X](https://x.com/trq212/status/2061907538741006796): “Workflows are the biggest upgrade to Claude Code’s capabilities since skills and subagents.”

> “Before dynamic workflows, you had one AI handyman you had to supervise. Now you have a general contractor who brings a full crew, runs the inspectors, and hands you a finished job.”  
> —Popular AI educator and enthusiast Ole Lehmann

Popular AI educator and enthusiast [Ole Lehmann](https://x.com/itsolelehmann/status/2060420998168809820) argues in a post on [X](https://x.com/itsolelehmann/status/2060420998168809820) that the release of dynamic workflows is “a much bigger deal than the Opus 4.8 release.” He describes dynamic workflows in plain terms: Before dynamic workflows, you had one AI handyman you had to supervise. Now you have a general contractor who brings a full crew, runs the inspectors, and hands you a finished job. Simple enough.

These are all pretty strong claims. But does it work? Let’s find out. I tested dynamic workflows against a single-agent workflow to determine whether they’re a valuable feature or marketing hype.

## The test

Dynamic workflows require Claude Code version 2.1.154 or later and a Max, Team, or Enterprise plan. I have a Max plan. I upgraded from 2.1.131 to 2.1.159 before starting. Opus 4.8 is the default model for version 2.1.159.

I ran the test twice with the same goal. Build a CLI tool called codebase-health that analyzes any local codebase and produces a markdown health report covering code complexity, documentation coverage, dependency auditing, and test coverage mapping. Both sessions started in completely empty folders.

I’ll paste both prompts at the end of this post for anyone interested in replicating my test.

## Dynamic workflows results

In 6 minutes and 59 seconds, Claude planned the work, scaffolded a shared contract so all agents could build against the same interface, and dispatched five parallel agents simultaneously.

Each agent owned one component and worked independently (as specified in the prompt):

* **Agent 1** built the complexity analyzer using Python’s AST module to analyze nesting depth in Python files, with heuristic fallbacks for JavaScript and other languages. Thresholds were configurable: 50 lines for functions, 4 levels of nesting, and 400 lines for files.
* **Agent 2** built the documentation coverage analyzer using ast.get\_docstring, skipping private and dunder methods by design, and using a JavaScript comment heuristic for non-Python files.
* **Agent 3** built the dependency auditor to parse requirements.txt and package.json, with network calls for outdated checks disabled by default and available as an opt-in flag.
* **Agent 4** built the test coverage mapper by convention, looking for test\_ prefixes, \_test suffixes, and tests/ directories, explicitly noting this was file mapping, not line coverage.
* **Agent 5** wired everything together into a CLI with argparse, per-analyzer error isolation, an overall health score, and a README.

The result: 62 passing tests, two working entry points, configurable flags, and a SAMPLE\_REPORT.md generated against its own repo as self-verification. When I asked how many tokens it used, the five subagents reported a combined 109,237 tokens. The orchestration thread cost was unmeasured since `/cost` was not available in the dynamic workflows session. With orchestration overhead, the total cost was estimated at $3-$5.

### But does it work?

In a new terminal window, I ran the tool against the HTTPie codebase, an open-source Python CLI tool. I got a full health report in seconds.

Overall health score: 60/100 (Fair)

* Code complexity scored 93/100 with 35 issues found.
* Documentation scored 17/100 with 926 undocumented public functions.
* Dependencies scored 100/100, but only because the tool could not parse setup.cfg, which is how HTTPie manages its dependencies.
* Test coverage scored 28/100 with only 20 of 72 source files having matching test files.

While thorough in most areas, it’s important to reflect on what happened with dependencies. Giving a perfect score because it couldn’t parse `setup.cfg` is a limitation. This tool was created in under 10 minutes. I wasn’t expecting perfection, but there’s a better way to document this. Null, error, undefined, or any message along those lines would have sufficed.

I have awareness (once again) that I’m testing Claude’s ability to build a CLI tool in one try. This is an impossible ask. About a year ago I would have been absolutely amazed by this result. But we’re in 2026, and AI companies have become so deeply embedded in our workflows that using AI is now table stakes.

That said, this first pass, like many other first pass results I’ve seen from Claude’s tooling, is close but not quite there yet. We still need an expert in the room.

But how did dynamic workflows stack up against the single agent workflow most of us are more familiar with? That’s a different story.

## Single agent results

The single agent built a different tool. It chose JavaScript over Python. Neither prompt included a language preference, and I’m only including it here as a detail, not a flaw.

The result: a working CLI tool in JavaScript with a src/ folder, test/ folder, and bin/cli.js entry point. Unlike the dynamic workflows session, /cost worked here and provided a full breakdown showing Opus 4.8 handling the bulk of the work, with a small amount of Haiku 4.5 for simpler tasks. /cost confirmed a $2.25 session cost, with a wall time of 10 minutes 42 seconds and 1,789 lines of code added.

### But does it work?

Getting the single-agent tool running required an extra step. When I tried to install it with pip3 (the way I had installed the dynamic workflows version), it failed. The single-agent didn’t create a pyproject.toml or a setup.py. It built a Node.js project with a package.json, a src/ folder, a test/ folder, and a bin/cli.js entry point. Running it required node bin/cli.js rather than a pip install.

Running the same tool against HTTPie produced an overall score of 30/100 (Poor). Documentation coverage came in at 21%. Test coverage at 29%. Both numbers roughly match the dynamic workflows findings. Two completely independent tools, built in different languages with different architectures, landed on similar conclusions about the same codebase.

The lower overall score in the single-agent version is partly due to a weighting decision. It weighted documentation at 30% and test coverage at 30%, which dragged the aggregate down. Also, unable to run a dependency audit, the single-agent tool returned `_No package.json or requirements.txt found._`. This is a better way of handling it.

## The comparison

Both tools worked. Both found the same real problems in HTTPie. Both missed the dependency audit because neither could parse setup.cfg. Both made sensible independent engineering decisions about thresholds, edge cases, and error handling.

Dynamic workflows built a more polished result. It included a shared contract architecture, 62 passing tests, configurable flags, and built-in self-verification. But based on what we built here,  it was marginally better for a task this (very small) size.

Now let’s judge based on estimated expenses. I used the rough cost of this seven-minute build to estimate what it would cost to run dynamic workflows for 24 hours. At Opus 4.8, with pricing of $5 per million input tokens and $25 per million output tokens, assuming a rough 70/30 input-to-output split, the subagent cost is roughly $225 to $375. With orchestration overhead, the total cost could be $400 to $600 for a full 24-hour parallel run.

> The single agent came in cheaper, but cheaper only matters if the job gets done. And in the case of a long-running job, it likely can’t.

The estimated cost for a single agent to run for 24 hours came to $300. The single agent came in cheaper, but cheaper only matters if the job gets done. And in the case of a long-running job, it likely can’t. Context window limits would force it to restart or lose track of earlier work.

With all the details factored in, I am happy to report that dynamic workflows do live up to their hype.

## Prompts

***Dynamic workflows prompt:***

*Create a workflow to build a CLI tool called codebase-health that analyzes any local codebase and produces a markdown health report. Spin up parallel agents to build each component simultaneously:*

***Agent 1****: Code complexity analysis — finds long functions, deeply nested logic, and files that are too large*

***Agent 2****: Documentation coverage — identifies functions and classes with no docstrings or comments*

***Agent 3****: Dependency audit — reads package.json or requirements.txt and flags outdated or unused packages*

***Agent 4****: Test coverage map — identifies which files have corresponding test files and which don’t*

*Each agent should build its component independently, explain what it built and how it made its decisions, and include tests. A final agent should wire all four components together into a single working CLI tool.*

***Single agent prompt:***

*Build a CLI tool called codebase-health that analyzes any local codebase and produces a markdown health report covering four areas:*

1. ***Code complexity*** *— finds long functions, deeply nested logic, and files that are too large*
2. ***Documentation coverage*** *— identifies functions and classes with no docstrings or comments*
3. ***Dependency audit*** *— reads package.json or requirements.txt and flags outdated or unused packages*
4. ***Test coverage map*** *— identifies which files have corresponding test files and which don’t*

*The tool should be installable and runnable as `codebase-health /path/to/project`. Include tests and a README.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)