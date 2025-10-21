Today, Anthropic’s [Claude Code](https://www.claude.com/product/claude-code) agentic coding tool is [moving beyond the terminal](https://www.anthropic.com/news/claude-code-on-the-web) and coming to the [web and the company’s mobile app](https://claude.ai/code). This means developers can now kick off Claude Code workflows directly from the Claude.ai web app, with Claude Code then running these coding tasks on Anthropic-managed instances.

This new capability is launching in what the company calls a “research preview,” and is available to users with paid Pro and Max accounts.

## More Time for Coffee

Anthropic believes this new mode of interacting with Claude Code will be handy for developers who want to assign multiple well-defined coding tasks to Claude that can run in parallel.

In practice, this means you’ll be able to point Claude Code at your GitHub repository and tell it what you want it to work on.

[![A screenshot of the new Claude Code interface on the Web](https://cdn.thenewstack.io/media/2025/10/a2913144-claude_code.png)](https://cdn.thenewstack.io/media/2025/10/a2913144-claude_code.png)

Image Credit: Anthropic.

Once connected to GitHub, you can then provide the agents with your current tasks and watch it reason over them and work on the code in the new web interface, with the agent running in the right sidebar and your set of tasks listed on the left.

That means it’s now possible for a developer using Claude Code to start a task on their phone, grab a coffee or attend yet another meeting (sigh!), and come back to pick up where the agent left off.

## Security

Anthropic stresses that each session will run in its own sandboxed environment, and all git interactions flow through a secure proxy service to ensure that Claude Code can only access those repositories it is supposed to have access to.

There are some ways to break out of this sandbox if you want to. When you set up your Claude Code environment at the story, you have to tell Claude Code if you want to give it trusted network access so it can download npm packages from verified sources. You can also restrict all network access, or curate a list of domains the agent will be allowed to access.

Overall, this approach mirrors how Anthropic handles security in the [Claude Agent SDK](https://thenewstack.io/anthropic-launches-claude-haiku-4-5/).

## Real-Time Steering for Enhanced Agent Control

Recently, Claude Code launched a new feature that allows developers to steer the agent while it is working on a problem. This real-time steering is also available on these new platforms, helping developers guide Claude without having to interrupt the work and, potentially, start over.

“Instead of managing individual coding tasks one at a time, developers can now oversee a fleet of Claude Code instances with confidence they’ll finish safely and independently,” Anthropic says. “It’s less about watching Claude work and more about delegating to an entire team — you assign the work, Claude handles the execution, and you review the results when each task completes.”

[![A screenshot of the new Claude Code interface on the Web](https://cdn.thenewstack.io/media/2025/10/013150e9-claude_code_web.png)](https://cdn.thenewstack.io/media/2025/10/013150e9-claude_code_web.png)

Image Credit: Anthropic.

## What About Google’s Jules?

If you’ve been following the development of these asynchronous coding agents, a lot of this will feel familiar and sound quite a bit like [Google’s Jules](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/), for example. Jules, too, will create a clone of your GitHub repository on a new VM and then work on that code for the user.

Where Jules started on the web and then recently made the move to the command line, Claude Code is moving from the command line to the web.

Anthropic itself also already offers a GitHub integration with [Claude Code GitHub Actions](https://docs.claude.com/en/docs/claude-code/github-actions), which allows developers to tag Claude in a pull request if they want the agent to start working on a solution. The compute environment for this is GitHub Actions, though. Many of its competitors also offer similar GitHub integrations.

## Claude and Anthropic’s Bottom Line

Anthropic says 90% of its Claude Code agentic coding tool is now written with the help of Claude Code, which may explain the pace of development lately. Measured by merges per engineer per day, Anthropic says its engineering team has increased its productivity by 67%, even as it doubled the size of its engineering org.

Claude Code’s popularity is also paying off on the business side, with Anthropic [recently saying](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation) that Claude Code now generated over $500 million in run-rate revenue for the company.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)