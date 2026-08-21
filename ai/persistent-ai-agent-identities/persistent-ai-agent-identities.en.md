**Your next AI coworker may look like a chatbot**, but underneath their name, face, and job title will be something more consequential: A persistent identity that uses memory, keeps permissions, and has responsibilities across all the conversations you have with it.

We can already see that model taking shape in Hermes. This month, [Nous Research](https://nousresearch.com/) folded [Bot Mode](https://github.com/NousResearch/Hermes-Bot-Mode) into the [Hermes desktop app](https://hermes-agent.nousresearch.com/docs/user-guide/desktop). The standalone plugin repository is archived; the roster now ships bundled and enabled by default; and v0.20.4 added a tabbed Sessions and Bots sidebar. Each profile shows up as a named bot with its own chat, avatar, personality, schedule, and pinned model.

Hermes tabbing Sessions beside Bots reflects a broader shift. Sessions did not disappear from any of these products; they sit under a durable agent identity that carries memory and permissions across them.

## Hermes and Grok build rosters, Claude joins one

xAI [announced](https://x.ai/news/introducing-grok-bot) Grok Bot on August 11, featuring a sidebar of named Bots, each with a title, a description, and up to 50 routines per account. Hermes now does the same thing on the desktop under an MIT license. [Claude Tag](https://claude.com/product/tag) from Anthropic, announced on June 23, takes the other route. One organization-provisioned Claude joins the human roster in Slack, where anyone in a channel can tag it, and each thread still spins up its own working session.

Three different products and deployment models took the same direction. The reusable object shifted from being the conversation to serving as the worker identity above it.

## A bot is a profile, not a new runtime

Hermes is the easiest to read because its code is open. A bot is a [Hermes Agent](https://github.com/NousResearch/hermes-agent) profile, a separate home directory holding config, keys, a SOUL file, memory, sessions, skills, and cron state. Routines are ordinary cron jobs namespaced per bot. Bot-to-bot handoffs are real command-line interface (CLI) invocations into a canonical bot chat, delivered whenever the receiving bot next runs. The standalone plugin described itself as a user interface over those primitives, with no core patches and no background daemons.

Profiles existed long before Bot Mode, which gave them faces and a sidebar. What has changed now is the unit of reuse, which moved from the prompt to the profile.

Descriptions are carrying real weight in these products. xAI tells operators to encode a bot’s durable responsibilities, sources, and boundaries in its description, and bots can hand off work to one another. The job description is starting to look a lot like a routing table.

## Three products, three identity architectures

Hermes keeps the credentials profile scoped to whichever host runs Hermes, whether that is a laptop or a remote server. Its own documentation makes it clear that profiles are not sandboxes, so the separation concerns state and configuration rather than security. Grok Bot takes the opposite approach, with every Bot sharing one account-scoped computer. That includes files, browser sessions, and app logins, and xAI says those survive the deletion of the Bot that created them. Claude Tag provisions an organization service identity with channel-scoped access to tools.

The diligence belongs here rather than on the feature list. A named bot with a job title reads like a colleague. What actually signs into a production system is a profile directory, a shared machine, or a service account, depending on the vendor.

The counterintuitive part is that persistence here is mostly a configuration issue. Nothing in a profile directory, a shared computer, or a service account keeps an agent coherent across weeks of accumulated work, and none of the three vendors has published evidence that any of them do.

Teams evaluating any of the three should start with the identity architecture because the roster is trivial to copy, but the underlying identity model is not.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)