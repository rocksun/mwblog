Agent builders are finding that sometimes the easiest way for an agent to do its job is to simply give it a few Unix tools and “let it cook.”

A recent project from Vercel found that stripping away loads of metadata and instead giving the model a BASH shell and access to data produced superior results.

And another group of open source developers is finding that a simple BASH while loop and some time alone is all that is needed to execute even complex tasks.

“Models are getting smarter and context windows are getting larger, so maybe the best agent architecture is almost no architecture at all,” wrote [Andrew Qu](https://www.andrewqu.com/), chief of software at [Vercel](https://vercel.com/about). “What if BASH is all you need?”

## Let the LLM Do the Thinking

For its employees, Vercel [built](https://vercel.com/changelog/introducing-bash-tool-for-filesystem-based-context-retrieval) a file agent to derive answers from its [internal data store](https://thenewstack.io/kepler-openais-internal-agent-platform-for-synthesizing-data/). Called d0, it can answer questions that typically get asked of the data team:

![Screenshot](https://cdn.thenewstack.io/media/2026/01/0c3a12dc-vercel-d0-ai.jpg)

Vercel’s d0 at work, answering questions.

To do this, d0 must translate natural language queries into SQL queries against a variety of YAML, Markdown and JSON files.

“When d0 works well, it democratizes data access across the company. When it breaks, people lose trust and go back to pinging analysts in Slack,” Qu wrote in a [December blog post](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) about d0.

When the company started the project, it devoted resources to making sure the agent had all the backup it needed, giving it specialized tools, heavy dollops of prompt engineering, [loads of metadata](https://thenewstack.io/how-canva-keeps-its-image-metadata-fresh/) and plenty of context management.

“It worked … kind of. But it was fragile, slow and required constant maintenance,” Qu wrote.

So, the engineering team tried the opposite approach: Instead of arming the agent to the teeth with context and tools, the agent was stripped to a single functionality, namely the ability to execute [BASH commands](https://thenewstack.io/how-to-create-your-first-linux-bash-script/). It got direct access to the files, which it had the ability to interrogate using `grep`, `cat`, `ls` and other commands.

Instantly, d0 became a lot easier to manage, used fewer resources and had a higher accuracy rate, the company found.

“All by doing less,” Qu wrote.

## The Unix Philosophy

Perhaps what Qu and the team learned was not so counterintuitive after all.

The [Unix philosophy](https://cscie2x.dce.harvard.edu/hw/ch01s06.html) is one of simplicity: The best way to build complex systems is through the modularity of basic components.

Each tool should do one thing and do it well, and tools should be easily composable into larger workflows. And they should all be text-based, as text is the universal interface.

[BASH](https://thenewstack.io/how-to-create-your-first-linux-bash-script/) (Bourne Again SHell) is the interface for this approach, allowing the user to chain together programs using the simple pipeline command to use the output of one program as the input of another.

Through this simple philosophy, Unix (and its offshoot Linux) has been used for decades to manage servers and the complex workloads they run; perhaps it could manage AI work as well.

## Better Results With Less Input

Vercel’s d0v2 removed 80% of the supporting information supposedly needed for the agent.

The BASH engine, called [bash-tool](https://www.npmjs.com/package/bash-tool), runs as an NPM package and was [open sourced](https://vercel.com/changelog/introducing-bash-tool-for-filesystem-based-context-retrieval) earlier this week.

It runs on Claude Opus 4.5 via the [AI SDK](https://ai-sdk.dev/), which is given a [Vercel Sandbox](https://vercel.com/sandbox) for context exploration. Handling and observability are done through [Vercel Gateway](https://vercel.com/ai-gateway) for request handling and observability, and a Next.js API route was built with [Vercel Slack Bolt](https://vercel.com/academy/slack-agents).

The data was indexed into a cube semantic layer, which is middleware software that aggregates the data sources so they are accessible via a single API, or in this case, a SQL query.

The cube fits into the Unix philosophy as well, given that its single job is to do semantic translation across the different data sources.

A lot of additional context was not needed for d0 because the semantic layer already provides much of the data needed, through dimension definitions, measure calculations and join relationships.

“We were building tools to summarize what was already legible. Claude just needed access to read it directly,” Qu wrote.

The following table summarizes the improvements from the old design to the new one:

| Metric | Advanced (Old) | File System (New) | Change |
| --- | --- | --- | --- |
| Avg execution time | 274.8s | 77.4s | 3.5x faster |
| Success rate | 4/5 (80%) | 5/5 (100%) | +20% |
| Avg token usage | ~102k tokens | ~61k tokens | 37% fewer tokens |
| Avg steps | ~12 steps | ~7 steps | 42% fewer steps |

## Retrospective

In retrospect, Qu’s team was over-engineering the agent prompt. They were reinventing the wheel.

“Grep is 50 years old and still does exactly what we need. We were building custom tools for what Unix already solves,” Qu wrote.

Models are smart and [getting smarter all the time](https://thenewstack.io/ignore-prior-instructions-ai-still-befuddled-by-basic-reasoning/). Providing them with more tools can be beneficial, but they can also be limiting. Sometimes models can make better choices. And they are advancing at a rate that your tool selection can’t equal.

“We were constraining reasoning because we didn’t trust the model to reason. With Opus 4.5, that constraint became a liability. The model makes better choices when we stop making choices for it,” Qu wrote.

Vercel CEO [Guillermo Rauch](https://rauchg.com/) [expounded on this lesson on X](https://x.com/rauchg/status/2008962101784830158), formerly known as Twitter, pointing to a return to understanding [Unix fundamentals](https://thenewstack.io/ken-thompson-recalls-unixs-rowdy-lock-picking-origins/) such as file systems, shells, processes and command lines.

“Don’t fight the models, embrace the abstractions they’re tuned for. BASH is all you need,” he wrote.

## ‘Failures Are Data’

One AI company that is apparently aligning with this philosophy is [Anthropic](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/) itself, the maker of the [Claude](https://thenewstack.io/give-claude-ai-full-access-to-your-local-filesystem-with-mcp/) family of AI models.

Recently, the company released a plugin called [“Ralph Wiggum,”](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum) which is basically a BASH script with a single operation: a do/while loop.

The idea is to give the AI agent a single prompt file and have it “iteratively improve its work until completion,” the docs explain.

No adjusting of the prompt is necessary. Instead, all the work is written to files and captured in git history logs. Claude improves the results by reviewing its own past work in files, and keeps revising the work until it hits the stated goals.

Ralph Wiggum was named after a dimwitted child in “The Simpsons,” and the idea was to [eliminate the need](https://venturebeat.com/technology/how-ralph-wiggum-went-from-the-simpsons-to-the-biggest-name-in-ai-right-now?ref=ghuntley.com) for someone to review the work of a large language model (LLM) each time it attempts the task. Rather, have the LLM itself do the work, and learn how to pull itself up from its own bootstraps.

“Failures are data,” [its creator](https://ghuntley.com/ralph/), open source developer [Geoffrey Huntley](https://x.com/GeoffreyHuntley), explained.

![Screenshot](https://cdn.thenewstack.io/media/2026/01/23897145-im-in-danger-ralph-1.gif)

Copyright: The Simpsons.

Despite its simple brute-force approach, Wiggum, in the best Unix fashion, has produced some remarkable results.

In one Hackathon, the Wiggum technique was used to [port a web agent tool](https://github.com/repomirrorhq/repomirror/blob/main/repomirror.md) from Python to TypeScript. Left overnight to run, the researchers returned the next day to over 1,000 commits, six ported codebases and a nearly fully functional program.

In other words, it was able to complete $50,000 of contract work for $297 in API costs, and, over a three-month period, create an [entire programming language](https://x.com/GeoffreyHuntley/status/1944377299425706060), according to Anthropic.

Wiggum works best for certain types of jobs, such as well-defined ones that don’t require human intervention along the way.

As we think about the road ahead with AI, sometimes it’s worth keeping in mind that complexity is not always the way forward, and some of the best tools for a job aren’t shiny news ones, but ones that have long been available.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)