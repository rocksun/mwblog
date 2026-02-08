Anthropic is extending Cowork with a plugin system that bundles skills, connectors, slash commands, and sub-agents, giving non-developers the kind of extensibility that Claude Code users are already familiar with.

[Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork), which launched only two weeks ago, is Anthropic’s version of Claude Code for knowledge workers who don’t want to write code but want to have a similar agentic tool that helps them create or clean up documents, [organize files](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/), and summarize large numbers of locally stored documents.

To help new users get started with plugins, Anthropic debuted [11 open-source plugins](https://github.com/anthropics/knowledge-work-plugins) on GitHub on Friday, covering a wide range of use cases and showcasing the possibilities of this new feature.

![](https://cdn.thenewstack.io/media/2026/01/fa598ea8-cowork-plugins-1-scaled.png)

Cowork in the Claude desktop app (credit: Anthropic).

These include a productivity plugin for tasks, calendars, and daily workflows. For users in sales and marketing, there are plugins that help them research prospects and prep deals, or draft content and plan campaigns. Users in finance use a plugin to analyze financial data and build forecasting models. There are similar plugins for enterprise search, legal, customer support, product management, and even biology research.

There is a bit of a meta-plugin for creating and customizing other plugins. Given that every company has its own take on certain business processes, this feature is a must, but by making it a separate plugin, Anthropic is also removing the complexity of editing these files directly.

In practice, this means the sales plugin, for example, includes a connector that integrates Claude with a CRM tool and a knowledge base. It also includes slash commands to start prospect research or to finalize call follow-ups.

The Cowork team writes that all of this means that Claude can now become a “cross-functional expert.”

![](https://cdn.thenewstack.io/media/2026/01/21a57ea3-cowork-plugins-2-scaled.png)

Managing Cowork plugins in the Claude desktop app (credit: Anthropic).

Because Cowork is based on the local file system, the same is true for the plugins as well. This should make them very easy to assemble and share.

Claude Code, on which Cowork is based, follows the same process. The contents are slightly different there (mostly skills, agents, and [hooks](https://thenewstack.io/gemini-cli-gets-its-hooks-into-the-agentic-development-loop/)), but the process for setting up a Claude Code plugin is similarly file system-based.

Since Cowork is designed for users who aren’t necessarily familiar with the terminal, plugin installation happens within the app itself, and building plugins uses the Plugin Create plugin — no CLI needed. The Claude desktop app also lets users browse the contents of every plugin bundle.

Plugins for Cowork are now available to all Claude users on Pro and Max plans.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)