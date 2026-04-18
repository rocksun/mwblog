OpenAI has [openly](https://openai.com/index/next-phase-of-enterprise-ai/) talked about its plans to build a unified AI superapp that combines ChatGPT with its Codex coding agent, Atlas browser, and new agentic AI tools for the enterprise. We’re now seeing the first pieces of this come together with [a major update to the Codex desktop app](https://openai.com/index/codex-for-almost-everything/), which will form the basis of this new superapp.

The company first launched Codex as its software engineering agent in May 2025. What was initially a bit of a slow burn became a major hit for OpenAI in 2026, especially after the launch of the company’s [dedicated Codex models](https://thenewstack.io/openai-releases-new-models-trained-for-developers/) in February.

Codex now has three million weekly users and is adding a million users per month, and that momentum continues to accelerate, Thibault Sottiaux, OpenAI’s Head of Codex, notes in a press briefing ahead of the launch, announced on Wednesday.

“We’re actually doing the sneaky thing where we’re building the superapp out in the open – and evolving it out of Codex,” Sottiaux says.

The Codex desktop app is the logical place for the company to build this superapp, and while OpenAI is framing Wednesday’s updates around coding and developer use cases, many of them could also be used by business and personal users.

## Computer use in the background

Codex can now use your computer — or at least your Mac, since this feature is not available anywhere else yet. With this, Codex can operate desktop apps, whether that’s for testing something you’ve built with the coding agents or for automating any other task.

What’s interesting here is that Codex can actually do all of this in the background, too, without stopping you from using your computer. Other computer use agents often take over the desktop, which is more likely to slow you down than speed you up, given that these agents still tend to be slow.

“You stop feeling like there is a limit to what Codex can do,” Sottiaux says. “It’s getting very, very creative. It keeps you in the flow. And there’s this understanding of your goals, your context, the ability to work across all of the apps that you have, your browser, and just really staying in lockstep. But also the ability to perform all of this work on a regular basis, in the background, and just really coming in and being useful and helpful on everything that matters to you day-to-day, not just as you’re building and developing software.”

> “It’s literally Codex building itself.” — OpenAI’s Thibault Sottiaux

OpenAI is using this feature to perform quality assurance on Codex, where the agent verifies that each feature is implemented in the app. “It’s literally Codex building itself,” he says.

One thing worth noting is that to get started with computer use, you do need to go into the Codex settings and download the plugin.

![](https://cdn.thenewstack.io/media/2026/04/217c7d05-computer-use-tic-tac-toe.gif)

*Credit: OpenAI.*

## A browser inside of Codex

With Atlas, OpenAI built its own browser, which it is now slowly bringing into Codex as well. For now, the rollout is a bit slow, but there are already some obvious use cases that go beyond the current app previews you are building. In this new version of Codex, you can actually comment on anything you see in the browser. OpenAI notes that this is especially useful to give the agent feedback on frontend work.

Coming soon, Codex will get full use of this browser to open pages, step through user flows, and analyze its own work. That’s when the potential of a built-in browser will become even more obvious for developers, but it will also enable more use cases for business users who have to fill in forms or copy and paste data from one web app to another.

Sottiaux is careful to frame this as a preview of where Atlas and Codex are heading. “It’s not the full power of it yet. It’s kind of a sneak peek of what’s to come there,” he says.

![](https://cdn.thenewstack.io/media/2026/04/6afba678-in-app-browser.gif)

*Credit: OpenAI.*

## Image generation inside of Codex

Regarding frontend work, Codex can now also access OpenAI’s gpt-image-1.5 image-generation model. That’s useful if you want to add any visual assets to a site you generate in Codex (or maybe just as placeholders), but the OpenAI team also noted that this could be useful for building mockups or to generate assets for games, for example.

There will be no extra cost for generating images, OpenAI says.

![](https://cdn.thenewstack.io/media/2026/04/9a978c7b-imagegen-burger.gif)

*Credit: OpenAI.*

## Plugins galore

Also new in this release is support for another 90 plugins, OpenAI’s curated bundles of skills, integrations, and MCP servers. Some of the new ones include Atlassian Rovo for managing JIRA, as well as CircleCI, CodeRabbit, GitLab Issues, Microsoft Suite, Neon by Databricks, Remotion, Render, and Superpowers.

As Andrew Ambrosio, who leads the development of the Codex app, notes, “the goal is for Codex to fit in naturally with the way that people work, and not make them change how they work.”

![](https://cdn.thenewstack.io/media/2026/04/4606b13b-automations-x-plugins-proactive-teammate.gif)

*Credit: OpenAI.*

While plugins may not be glamorous by themselves, they do form the backbone of bringing many of the non-coding use cases to Codex, and at this point, this goes well beyond the standard office productivity and email services and includes MyRegistry.com, United Rentals, FINN car subscriptions, Readwise, and various research tools from the likes of Pitchbook, Morningstar, and Scite.

As the OpenAI team notes, those plugins are especially interesting when combined with Codex’s Automations — that is, OpenAI’s ability to run prompts on a schedule (similar to [Routines in Claude Code](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/)).

## Heartbeats and Automations

Those automations, too, are getting a major, OpenClaw-inspired update, with the addition of heartbeats that allow you to automate follow-ups to a thread.

“You can set up a thread that’s designed for a daily brief, or a thread that’s designed to triage Slack or something like that,” Ambrosio says. “Or you can set this up as a personal assistant that every five minutes gets a heartbeat run, similar to an Open Claw, and then goes and does a bunch of stuff with plugins. So this is a really powerful axis of personalization for the types of tasks you need to get done, especially those that are pretty persistent.”

![](https://cdn.thenewstack.io/media/2026/04/d7872c23-automations-1024x373.png)

*Credit: OpenAI.*

The fact that these heartbeats run in the same thread is worth calling out. Similar tools from OpenAI’s competitors often spin up new worktrees for each run, which can cause them to lose context from previous iterations.

Inside OpenAI, heartbeat automations have become a way to deploy near-continuous agents that monitor Slack channels, triage inboxes, or keep tabs on GitHub and Notion. Sottiaux describes running several of them at once, essentially as teammates.

## More proactive help

One thing Codex will now do more regularly, too, is suggest follow-ups, including scheduling automations. “Codex now also proactively proposes useful work to continue where you have left off. Using context from projects, connected plugins, and memory, Codex can now suggest how to start your work day or where to pick up on a previous project,” the team writes in today’s announcement.

Codex may suggest you follow up on unanswered comments in a Google Doc, for example, and pull context from other apps like Slack and Notion to help you do that.

Combined with an improved memory system that now allows Codex to better remember your preferences and context from previous interactions, this may be one of the more impactful changes for day-to-day use of Codex outside the developer workflow. It also shows where OpenAI is likely going with this app in the long run.

While much of the focus here is going beyond coding, at least for the time being, there are plenty of new features and quality-of-life updates for developers as well.

“We are continuing to invest in places that developers already spend time,” Ambrosio says.

For example, it’s now possible to address GitHub review comments right in Codex. Developers can open multiple terminal tabs (yay!), connect to remote dev boxes over SSH (now in alpha), and open files in the sidebar to view PDFs, spreadsheets, slides, or other documents. Also new is a summary pane that lets you track plans, sources, and artifacts.

“Together, these improvements make it faster to move across all the stages of the software development lifecycle between writing code, checking outputs, reviewing changes, and collaborating with the agent in one workspace,” the OpenAI team writes.

![](https://cdn.thenewstack.io/media/2026/04/4f6aff87-remote-ssh.gif)

*Credit: OpenAI.*

## Codex as a teammate

Inside OpenAI, Codex has already moved well past its coding origins, too. More than 80% of the company uses it, the Codex team says, and not just engineers: use cases include writing weekly briefs, synthesizing feedback, drafting product requirements, reviewing contracts, and even sending security-training reminders.

## Availability

The updated Codex app is now available for all Codex users who are signed in with ChatGPT. Some features, including personalization features like context-aware suggestions and memory, will only come to Enterprise, Edu, and users in the EU and UK at a later point. Computer use, too, won’t be available to EU and UK users at launch but will come “soon.”

Sottiaux notes that, over time, we will also see a Codex web app and a mobile app.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)