For eight years, Snapchat has used [Valdi](https://github.com/Snapchat/Valdi), a cross-platform UI framework, in-house. Now, it has open sourced the framework.

Valdi is designed to solve the fundamental problem of cross-platform development: velocity vs. runtime performance, the repo Readme states.

Although it has been used internally for nearly a decade, this is a beta release because the “tools and documentation need more battle testing in the open source world,” according to the repository. The goal is to [improve developer experience](https://thenewstack.io/improve-developer-experience-to-prevent-burnout/) before moving it out of beta.

“Valdi is a cross-platform UI framework that delivers native performance without sacrificing developer velocity,” the repo states. “Write your UI once in declarative TypeScript, and it compiles directly to native views on iOS, Android, and macOS — no web views, no JavaScript bridges.”

It joins a long list of [cross-platform frameworks](https://thenewstack.io/10-cross-platform-options-for-building-native-mobile-and-web/), but what sets it apart according to the repo is its true native performance.

“Unlike frameworks that rely on web views or JavaScript bridges, Valdi compiles declaratively rendered TypeScript components into platform-native views,” the repo adds.

It also offers a number of performance advantages such as:

* Automatic view recycling, which reduces inflation latency;
* Optimized component rendering, which allows components to re-render independently without triggering parent re-renders;
* A C++ layout engine that runs on the main thread with minimal marshalling overhead;
* Viewport-aware rendering, which inflates visible views so that infinite scrolling is performant by default.

It includes automatic code generation so that the [TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/) interfaces are translated into Kotlin, Objective-C, and Swift bindings.

## Nuxt Releases MCP Server

Progressive web framework Nuxt has released an [Model Context Protocol (MCP) server](https://nuxt.com/blog/building-nuxt-mcp) that exposes its documentation, blog posts and deployment guides in a way that AI assistants can understand.

A number of frameworks, including [Angular](https://angular.love/angular-cli-mcp-server-keep-your-ai-up-to-date) and [React](https://github.com/kalivaraprasad-gonapa/react-mcp), have released MCP servers in recent months.

What sets this announcement apart is that team members [Hugo Richard](https://x.com/HugoRCD__) and [Sébastien Chopin](https://www.linkedin.com/in/atinux/?originalSubdomain=fr) don’t just announce Nuxt’s MCP server — they did something objectively cooler. They explain how they built it so that other developers can follow suit to [deploy their own MCP servers](https://thenewstack.io/tutorial-build-a-simple-mcp-server-with-claude-desktop/).

The announcement also explains how to deploy it in Cursor and other AI tools.

## Next.js Easier to Deploy Outside Vercel

[Next.js is easier](https://appwrite.io/blog/post/everything-new-in-nextjs16) to deploy in non-Vercel environments, according to [Matej Bačo](https://github.com/meldiron), an engineering lead from Appwrite, which is an open source alternative to Vercel.

The big change that makes this possible is the [Adapters API](https://nextjs.org/blog/next-16#build-adapters-api-alpha), according to Bačo.

“If you’ve ever had to deploy a Next.js app in an unusual environment, say, outside [Vercel](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/), this one’s for you,” he wrote. “Build Adapters, now in alpha, let you hook into the build process and modify it without forking the framework. It’s especially handy for teams self-hosting or building custom pipelines.”

He added this demonstrates that “Next.js is starting to take flexibility seriously for developers running the framework in different environments.”

He also pointed out other useful changes in the Next.js 16, including the [DevTools MCP](https://github.com/vercel/next-devtools-mcp). It will allow AI tools to understand your project’s context, routing, caching and rendering behavior.

> “These middlewares are not your typical middlewares. You’re at the mercy of any network calls you make in these middlewares, as a single slow network call may block the initial load of your entire webpage, which is not ideal.”  
> **— Matej Bačo, engineering lead from Appwrite**

He also noted what seems like a minor change, but which he said is important for [Next.js developers](https://roadmap.sh/nextjs) — the old middleware.ts file is now called proxy.ts.

“That’s it. Same behaviour, better name,” he wrote.

But the middleware nomenclature caused a lot of confusion about it worked in Next.js, he said.

“These middlewares are not your typical middlewares,” Bačo wrote. “You’re at the mercy of any network calls you make in these middlewares, as a single slow network call may block the initial load of your entire webpage, which is not ideal.”

Middlewares in Next.js are used to do lightweight tasks, he added, such as redirecting users based on the authentication cookies stored. That made the term confusing so the Next.js team renamed it to ‘proxy’ so that the purpose is clearer.

He pointed to other updates, such as improved logs and graduating TurboPack from the beta to the default bundler for all new Next.js projects.

“Build and dev logs now show where time is spent, breaking down compilation, rendering, and optimization steps,” Bačo wrote. “If your build suddenly feels slower, you can immediately tell which parts are to blame.”

He also points to Refined caching APIs, which he said have been cleaned up and made more explicit.

“Next.js 16 isn’t a release that changes how you build,” Bačo wrote. “It’s one that changes how your build feels. Caching is now predictable. Builds are faster. Routing is leaner. Logs are clearer.”

## React Native Adoption Rises in Bitrise Deployments

Bitrise released its first [Mobile Insights report](http://www.bitrise.io/insights), analyzing 10 million plus builds on the cloud-based mobile [DevOps](https://thenewstack.io/go-beyond-devops-with-autonomous-full-stack-optimization/) and [CI/CD platform](https://thenewstack.io/beyond-ci-cd-why-your-infrastructure-is-your-new-bottleneck/).

Within that dataset, it found that cross-platform frameworks are on the rise, with React Native emerging as the leader. React Native deployments grew from 63% across all platforms builds in 2022 to 83% by 2025, according to the report.

It also uncovered an interesting paradox: While mobile CI pipelines have grown 23% more complex, leading teams have reduced build times by 28%.

“Mobile development is getting more complex and demanding,” [Arpad Kun](https://www.linkedin.com/in/arpadkun/), Bitrise vice president of engineering and infrastructure, said in a prepared statement. “These insights give engineering teams the benchmarks they need to understand where they stand and where they should focus to level up.”

## Wiggle UI: Open Source Widgets for the Web

Web developer [Henil Shah](https://henilshah.vercel.app/) has released what he says is the first ever open source collection of widgets for the web.

[![Wiggle UI home page](https://cdn.thenewstack.io/media/2025/11/9f189f23-wiggleui.png)](https://cdn.thenewstack.io/media/2025/11/9f189f23-wiggleui.png)

An open-source library for widgets. Screenshot via [Wiggle UI site](https://wigggle-ui.vercel.app/).

Called [Wiggle UI](https://wigggle-ui.vercel.app/), it includes widgets for calendars, clocks, dashboards, sports, stocks and weather, all available under the MIT license. Developers can also find it on [Github](https://github.com/wigggle-ui/ui).

## Library Makes It Rain… Poop?

In fun news, self-described Indie hacker Alex Enes Zorlu created an open source “lightweight, fun-filled library” designed to bring animated poop emojis to web applications.

Aptly called [Poopetti](https://poopetti.com/), it will do two things: Cause poop emojis to rain or create a large poop emoji that pops when selected, causing it to rain down — you guessed it — poop emojis.

The eight-year-old in us loves it.

“Are you drowning in user incompetence? Poopetti to the Rescue! 💩,” the page boasts. “Why use boring error messages when you can literally shower your users with 💩?”

So far, it has 35 stars and one fork on [GitHub](https://github.com/enszrlu/poopetti).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)