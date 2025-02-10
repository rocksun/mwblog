# The Vintage Technology That Speeds Up Modern Web Apps
![Featued image for: The Vintage Technology That Speeds Up Modern Web Apps](https://cdn.thenewstack.io/media/2025/01/86f71230-old-school-technology-for-web-development-1024x683.jpg)
Isaac Hagoel has dealt with his [share of problems in commercial apps](https://dev.to/isaachagoel/are-sync-engines-the-future-of-web-applications-1bbi), many of which don’t show up until the web app starts to gain traction.

“A pattern I noticed in dev teams that start working on a new product is to ignore these problems completely, even if the team is aware of them,” he wrote. “The reasoning is usually along the lines of ‘We’ll deal with it when we start actually having these problems.’”

Ignoring the problems, though, makes them difficult to fix later on, he continued.

“The team would then go on to pick some well-established frameworks (pick your favorite), thinking these tools surely offer solutions to any common problem that may arise,” Hagoel wrote. “Months later, when the app hits ten thousand active users, reality sinks in: The team has to introduce partial, patchy solutions that add complexity and make the system even more sluggish and buggy, or rewrite core parts (which no one ever does right after launch). Ouch.”

Sync engines might be the key to heading off these performance problems, Hagoel wrote.

He’s not the only one who thinks so. Increasingly, The New Stack sees [sync engines mentioned as a tool](https://medium.com/@nile.bits/why-sync-engines-might-be-the-future-of-web-applications-41fdab1d650c) for modern web development.

## Sync Engines: Old Tech With New Application
Sync engines are not new. On the contrary, a sync engine is an old solution, according to [Aaron Boodman](https://www.linkedin.com/in/aaron-boodman/), a software engineer who helped build [Google Chrome](https://thenewstack.io/google-genai-comes-to-chrome/). He has worked on sync engines his whole career.

A sync engine is software that’s designed to synchronize data between multiple devices or services, he explained. Hagoel called it a “persistent buffer between the frontend and backend.” Sync engines can be and are written in any language, according to Boodman.

“I usually use Microsoft Outlook as an example of something that was written with sync, which is who knows how old, as old as dirt, but actually it even predates that,” he said. “One of the most famous GUI programs in computing history, Lotus Notes, was a sync-based product.”

“The reason why people keep coming back to it is because it makes really, really high quality user interfaces.”

– Aaron Boodman, CEO of Rocicorp and sync engine developer
Boodman is now the CEO, founder and partner at [Rocicorp](https://rocicorp.dev/), a small partnership building high-quality developer tools — including [Replicache](https://replicache.dev/) and [Zero](https://zero.rocicorp.dev/), both open source sync engines.

More recently, sync engines have been used by [Linear](https://www.youtube.com/live/WxK11RsLqp4?t=2175s), [Figma](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/) and [Trello](https://www.atlassian.com/blog/atlassian-engineering/sync-architecture), according to Hagoel.

[UI developers](https://thenewstack.io/non-browser-ui-platform-for-ai-offers-grants-to-developers/) have tinkered with sync engines for years, Boodman said.
“The reason why people keep coming back to it is because it makes really, really high-quality user interfaces,” he said. “When you look at who’s interested in sync right now, from a technology side, it’s all [UI people](https://roadmap.sh/ux-design). And the reason is because UI developers are motivated by making things really fast.”

## UX Improvements Enabled by Sync
Among the UX improvements that sync enables:

- It allows reads to happen instantly when the user taps on something in the UI. When a user triggers something in the UI, the sync engines moves the data onto the client so the client can display the data right away;
- It allows writes to be instant because the data that you’re changing is local;
- It means no progress bars because the sync is constantly happening in the background.
“Sync engines are really promising, and they have been promising for a long time because, at the core, what they enable is interactions to be instant,” he said.

There’s a lot of machinery that goes away for UI developers using sync engines because sync engines abstract it away. It makes UI development more fun and gratifying, he added, which is why developers frequently come back to sync engines.

## Sync for Web Apps: Why Now
Boodman identified several reasons why sync engines are becoming a popular option for speeding up the frontend, starting with the fact that the majority of software is now web-based. For a long time, the web did not have good storage primitives, so there was not a way to store very much data locally in the web client — something that’s needed in order to sync, he added.

“Actually […] that started to change more than 10 years ago, but the primitives that were available were so bad that it took a long time for developers to figure out how to use them and iterate on them,” he said.

The other factor is there are a number of really high profile apps that are well-respected by developers for their high quality, and these are enabled by sync engines, he said.

“Other developers want to get that same quality of UI, and they know that it’s enabled by sync engines, and so they’re looking for some way to get these benefits themselves,” he said.

Finally, there’s a [new generation of sync engines](https://gist.github.com/pesterhazy/3e039677f2e314cb77ffe3497ebca07b) being built now, Boodman said. His company is working on a new sync engine called [Zero](https://zero.rocicorp.dev/), but there are other new entries, including [Power Sync](https://www.powersync.com/), [Electric SQL](https://electric-sql.com/), [Convex](https://www.convex.dev/sync) and [Jazz Tools](https://jazz.tools/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)