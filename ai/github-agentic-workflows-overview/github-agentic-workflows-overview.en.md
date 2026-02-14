A lot of the hype around agents has been around writing code, but what if you could have an agent watch for events in your GitHub repo and automatically run a set workflow when, for example, a new issue is created? And what if you could just describe the workflow to the agent, and then have it generate the detailed steps for you? That’s the question the GitHub Next team, the same team that also incubated GitHub Copilot, asked itself.

In an interview with *The New Stack*, [Eddie Aftandilian](https://www.linkedin.com/in/eddie-aftandilian-772b267/), a principal researcher at GitHub Next who also worked on Copilot, notes that there are many tasks developers may want to perform as part of the continuous integration process, but that can’t realistically be done with a purely deterministic algorithm. It is not meant to replace existing CI/CD tools but to augment them with what the team calls ‘continuous AI’ capabilities.

“There’s a whole class of these things that are never done that you always want an agent watching the events in the repo, maybe running on a schedule, or running when an issue is created, and then following, basically a list of steps on how to vet that or how to deal with it,” Aftandilian explains.

[GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/), as this new tool is called, is [now available on GitHub](https://github.github.com/gh-aw/)and uses GitHub Actions to provide a sandboxed environment and the infrastructure to run agents across potentially millions of repositories.

## Use cases

The most basic use case is to run a [daily status report](https://github.com/githubnext/agentics/blob/main/workflows/daily-repo-status.md?plain=1) at the end of the day that summarizes recent issues, pull requests, discussions, and more. But it could also mean running a daily agent that identifies where the team may have deviated from best practices and suggests fixes (with Copilot then being manually or automatically tagged to fix them, too).

Here are a few more examples the team provided, but as with all of these projects, developers will surely find even more creative ways to use a tool like this:

While still in preview, Agentic Workflows already supports the top three coding agents: Claude Code, OpenAI Codex, and GitHub’s own Copilot.

## Agentic prompting for workflows

One interesting first step in setting up these workflows is what Microsoft researcher [Peli de Halleux](https://www.microsoft.com/en-us/research/people/jhalleux/) calls ‘agentic authoring’ in the same interview. This means you can simply describe what the agent should do in a few sentences, and the tool will generate a full, step-by-step workflow and suggest tools to use and permission settings (which are set to read-only by default).

“The barrier to entry is basically all the way to almost zero,” explains de Halleux. “The agents are really good at prompting, and we can weave in debugging and optimizing as part of the authoring experience because the agents can also read their logs and reason about what they’ve done in the past.”

The tools then create two files: a Markdown file that describes the agentic workflow and a YAML file for GitHub Actions. The Markdown file includes front matter specifying which tools and MCPs to use and which permissions the agent has, but for the most part, it’s an English-language description of the workflow.

Here is what that looks like in practice:

> `---  
> on:  
> schedule: daily  
> permissions:  
> contents: read  
> issues: read  
> pull-requests: read  
> safe-outputs:  
> create-issue:  
> title-prefix: "[repo status] "  
> labels: [report]  
> tools:  
> github:  
> ---`
>
> `# Daily Repo Status Report  
> Create a daily status report for maintainers.  
> Include  
> - Recent repository activity (issues, PRs, discussions, releases, code changes)  
> - Progress tracking, goal reminders and highlights  
> - Project status and recommendations  
> - Actionable next steps for maintainers  
> Keep it concise and link to the relevant issues/PRs.`

## Safety architecture

The permissions are read-only, and the agent is never allowed to write — it can comment on issues and join discussions, but there is always a validation phase. Write operations are always deferred and run as separate jobs after the agent finishes its task.

“You want the thing that these agents do to be guardrailled, validated, revalidated, so that you get a lot of guarantees and you know about the stability of these things. This is actually very, very important to us, as far as having the confidence that we’re going to use this,” de Halleux explains.

GitHub Actions already includes its own security architecture, but the team then uses what it calls the [SafeOutputs](https://github.github.com/gh-aw/introduction/architecture/) subsystem, a set of trusted components whose outputs are run through deterministic filters so that policies can be enforced at that level.

In addition, the Agent Workflow Firewall can limit what agents have access to.

## Start with code improvements

Still, the team recommends that developers start with low-risk outputs, such as comments, drafts, and reports, before letting agents create pull requests. To start, developers should have agents focus on improving existing code rather than building new features.

Over time, as agents improve and developers gain a better intuition for how to use these agent loops, we’ll likely see more ambitious use cases.

One thing the team is pretty clear about, though: this is not a replacement for existing CI/CD workflows. “This approach extends continuous automation to more subjective, repetitive tasks that traditional CI/CD struggles to express,” the documentation stresses. But it can take a lot of daily toil off a developer’s hands and, ideally, result in better code.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)