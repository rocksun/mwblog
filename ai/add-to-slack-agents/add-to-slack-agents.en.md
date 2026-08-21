Slack on Thursday rolled out [Add to Slack](https://slack.com/blog/news/add-to-slack), which lets users more easily bring the agents they’ve built with ten outside platforms into their workspaces without having to write a custom Slack integration.

A user simply starts the installation (and agent creation) inside a partner tool, Slack says, and the partner then handles OAuth, app configuration, and permission scoping. The runtime itself remains outside Slack, either with the provider or, for tools like NanoClaw, on a user’s machine or cloud account. The respective Slack app can then receive messages and mentions and join channels.

The launch partners for Add to Slack are Hyperagent, LangChain, Lovable, n8n, NanoClaw, OpenAI, Runlayer, Skydive, Superhuman, and Vercel.

That’s quite a wide range of products that spans from point-and-click builders to developer frameworks. But what matters most here is that the installation path is the same — and far easier than the previous approach, where users had to tediously click through various settings, enable permissions, and hope for the best.

Slack says installed agents inherit workspace data boundaries and permission controls. The workspace’s [app-approval policy](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace) still applies. Each app’s OAuth scopes and channel membership determine what it can access. Once installed, they will also appear in Slack’s App browser.

![](https://cdn.thenewstack.io/media/2026/08/15569ebd-lovable_1@2x-1024x1024.png)

Credit: Slack.

## One app per agent

NanoClaw is a good example of how this works in practice. Connecting the [open source framework](https://github.com/nanocoai/nanoclaw) previously required creating a custom Slack app, then working through its configuration, scopes, and authentication. Now, NanoClaw’s Marketplace app becomes the [manager app](https://docs.slack.dev/reference/methods/apps.manifest.create/), with permission to create a separate managed Slack app for each NanoClaw agent.

In a demo for *The New Stack*, NanoClaw creator Gavriel Cohen asked one NanoClaw agent to build a team modeled on characters from *The Office*.

“I say create a team for me of agents, and it creates all these agents and tags them. They all pop in, and then we start chatting over here,” Cohen tells *The New Stack*.

The bots appeared under distinct names. In the demo, Cohen also brought them together in a room with a shared Canvas.

“Each agent has its own bot. So it creates some new things. It means you can tag them natively,” Cohen says.

NanoClaw creates a separate Slack WebSocket connection for each agent, and its host routes messages to the corresponding agent in Slack.

## What about Slack Code?

It’s worth noting that Add to Slack is separate from [Slack Code](https://thenewstack.io/slack-code-agent-channels/), another new AI agent feature the company rolled out Thursday. Slack Code creates temporary project channels where supported coding agents can present plans, diffs, pull request details, and live previews before the channel is archived. Add to Slack installs an app, while Slack Code structures the work of a small group of coding agents from its partners after installation.

*Featured image credit: Ardian Pranomo for Unsplash+.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)