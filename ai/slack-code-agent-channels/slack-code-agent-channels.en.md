Slack on Thursday launched [Slack Code](https://slack.com/blog/news/slack-code-channels-for-agents), a new kind of Slack channel that’s built for coding agents and the developers supervising them.

Now, if you mention a supported agent anywhere in Slack and it decides that the request isn’t a good fit for a threat, it will spin up a code channel that carries its plan, the repository and branch it’s working in, code diffs, pull request information, and a live HTML preview of the output.

People in the channel can then request changes or stop the agent. Once the work is done, the agent archives the channel, though it remains searchable and, [Slack says](https://www.salesforce.com/introducing-slack-code/), can function as an audit log.

Interestingly, humans — at least for now — can’t spin up a code channel themselves.

![](https://cdn.thenewstack.io/media/2026/08/4c05bf1b-slack-code-1024x701.gif)

Credit: Slack.

Slack Code is now live for teams using Anthropic’s Claude, Cognition’s Devin, GitHub Copilot, and Vercel, with OpenAI’s ChatGPT coming later. It’s available on any Slack plan, including free workspaces, and Slack isn’t charging extra for it, Katie Steigman, vice president of product at Slack, tells *The New Stack*.

Overall, this seems like a logical move for Slack. Today, most coding agents are single-player experiences that happen in a terminal, an IDE, a desktop app, or a browser session, though the industry has been [pushing them toward team infrastructure](https://thenewstack.io/coding-agents-team-infrastructure/) for months.

Steigman says, “There’s a shift we need to make from sort of siloed, single player kind of AI work, like I’m working in my terminal, I’m doing my thing with whatever agent, to bringing that into a multiplayer environment.”

## Why agents need a different kind of channel

Slack already has threads (and let this serve as your regular reminder to use those!). But Steigman says threads work for the cases where an agent answers in a message or two, not for a coding session that runs long and pulls in more people as it goes.

“You want to bring people in, and now if you do that in a thread, you’re kind of blowing up the channel,” she says. “You’re blowing up the thread, right?”

![](https://cdn.thenewstack.io/media/2026/08/64dfa707-slack-code-1024x667.png)

Credit: Slack.

A conventional channel has the opposite problem, Steigman argues. Slack designed those as durable team spaces, and an agent’s coding session usually ends.

“They’re a little bit too permanent,” Steigman says. “They aren’t quite flexible enough for agents.”

So Slack added a new kind of channel, one with a defined lifespan and no human creator (though Steigman says that could change). For now each code channel inherits the visibility of the conversation it came from, so it’s public or private depending on where the agent was mentioned.

## Bring in the agents

Slack Code isn’t a coding model, a harness, or an agent runtime. Slack built an [API](https://docs.slack.dev/ai/developing-agents/) that lets partner agents create and manage the new channel type, and that’s the extent of it. The integration doesn’t run on [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-mcp/) or [Agent2Agent (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/), Steigman says, though Slack does ship an MCP server for other purposes. Access to the code channel APIs is limited to the launch partners for now, with plans to open it to more coding agents later.

Slack is owned by Salesforce, Salesforce sells Agentforce, and Slack Code hosts Anthropic, OpenAI, GitHub, and Cognition free of charge. Slack is betting it can be the place agent work gets reviewed no matter whose agent did the work. GitHub made a version of the same bet when it [opened Agent HQ](https://thenewstack.io/github-agent-hq/) to Claude and Codex alongside its own Copilot.

## Context and control

Steigman says, “I think it’s because all of your context is there.” A project’s bug reports, screenshots, decisions, and earlier discussion are already sitting in its channels (but then, GitHub, Atlassian, and virtually every other SaaS company says the same about the context they have).

Too much context isn’t a good thing either, so an agent’s reach depends on its configuration. Slack’s internal agent, Spec, can see everything Steigman can see, she says, while customers can scope theirs more narrowly.

Slack says agents inherit its existing permissions and admin controls, and that high-stakes actions still need human sign-off. In a demo, Steigman noted that someone would approve the pull request in GitHub before her sample change could ship.

## The Buzz around agents

Slack, of course, isn’t the only company thinking about how to bring agents into developer conversations, and it isn’t the furthest along.

Anthropic launched [Claude Tag in June](https://thenewstack.io/anthropic-claude-tag-slack/), a shared agent in beta for Claude Team and Enterprise customers that runs under its own workspace identity instead of borrowing the permissions of whoever summoned it. Anthropic is taking a different approach to the same problem, with one Claude working with everyone in a channel.

[Block’s Buzz](https://thenewstack.io/block-buzz-agent-workspace/), the Apache 2.0-licensed collaboration product that very much feels like Slack, pushes this model further. A Buzz project binds to any number of channels and carries the repository, pull requests with inline diffs and comments, issues, continuous integration results, and merge decisions under a single identity system, so the original request and the eventual result stay connected. Buzz is also self-hostable, which Slack Code is not. What it doesn’t have is the installed base, since most companies already run Slack anyway (including Block itself).

## Avoiding “crazy bot land”

Coding may only be the first use case to get its own kind of agent channel. Steigman says Slack is already seeing code channels used for documents, presentations, and incident response, even though the interface is still built around repositories, branches, pull requests, diffs, and previews.

“I think it’s easy to underestimate UX right now because everybody’s into the models,” Steigman says.

Slack’s core product teams are watching how agent-generated messages change human behavior, she says, with the goal of adding more agents without having Slack “blow up with noise and be this crazy bot land.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)