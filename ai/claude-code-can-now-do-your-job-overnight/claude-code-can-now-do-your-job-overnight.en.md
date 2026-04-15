On Tuesday, Anthropic launched an oft-requested feature for Claude Code: [routines](https://claude.com/blog/introducing-routines-in-claude-code).

The idea here is that you can now run a given prompt on a schedule, or based on GitHub events (using webhooks) and API triggers from your own code.

In an earlier update this year, Anthropic introduced the [`/schedule` command](https://code.claude.com/docs/en/scheduled-tasks) to its command-line tool, which allows developers to run prompts at a set time or interval. This is similar, but different.

“A routine is a Claude Code automation you configure once — including a prompt, repo, and connectors — and then run on a schedule, from an API call, or in response to an event,” Anthropic explains in its announcement.

Routines are essentially the next-gen version of /schedule, and with this update, existing scheduled tasks now automatically become routines. You can set them up from [claude.ai/code](https://claude.ai/code/draft_a3ce30a9-f0bb-4d18-890f-12cc6d6a6375) on the web or as a remote task in the Claude desktop app.

![](https://cdn.thenewstack.io/media/2026/04/3d6c6652-screenshot-2026-04-14-at-11.18.08-am-1024x211.png)

*Credit: Anthropic.*

## Three triggers: schedule, API, and webhooks

Anthropic notes that scheduled routines will be especially useful for triaging new issues every night, scanning for merged pull requests every week, and ensuring that a project’s documentation is still up to date. For routines that fire based on API pings, the company notes that this could be used for continuous deployment workflows, for example, where “Claude runs smoke checks against the new build, scans error logs for regressions, and posts a go/no-go to the release channel.”

> Many teams have been stringing together similar setups with GitHub Actions and Claude in its -p headless mode. Now Anthropic can manage the session lifecycle for them.

For these routines, Claude Code becomes more of a background agent, especially when running GitHub routines with their per-pull-request continuity. Many teams have been stringing together similar setups with GitHub Actions and Claude in its -p headless mode. Now Anthropic can manage the session lifecycle for them.

![](https://cdn.thenewstack.io/media/2026/04/d699775a-screenshot-2026-04-14-at-11.10.09-am-1006x1024.png)

*Credit: Anthropic.*

## Cloud execution, subscription limits

To some degree, this is akin to scheduled tasks in [Cowork](https://thenewstack.io/anthropic-takes-claude-cowork-out-of-preview-and-straight-into-the-enterprise/), Anthropic’s Claude Code variant for knowledge workers.

A major difference, though, in addition to the API and GitHub triggers, is that while scheduled Cowork tasks can only run while your computer is on, Claude Code routines run on Anthropic’s web infrastructure. That’s not cheap, so users on Anthropic’s $20/month Pro accounts can only run 5 routines per day, while Max users (who pay $100 or $200 per month) will get 15 routines per day. Users on Team and Enterprise plans get up to 25 daily routine runs. That’s in addition to the regular token limits Anthropic enforces based on your plan — which are a bit opaque but seem to be getting stricter and stricter by the day.

> While scheduled Cowork tasks can only run while your computer is on, Claude Code routines run on Anthropic’s web infrastructure.

One interesting aspect of these routines running in the cloud is that they run autonomously. As Anthropic notes, “there is no permission-mode picker and no approval prompts during a run.” These routines can run shell commands, access skills (if they are in the repository), and call connectors and MCP servers.

It’s also worth noting that they are not shared across teams, and whatever they do across GitHub, Slack, and other tools is linked to the user’s identity.

## Loops are still an option, too

One option that is still available for running long-lived session-scoped tasks is the [`/loop` command](https://code.claude.com/docs/en/scheduled-tasks). Loops live on your local machine and let you schedule recurring tasks, but they can only live for up to 7 days and do not persist across restarts.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)