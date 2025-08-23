[React Native 0.81 shipped](https://reactnative.dev/blog/2025/08/12/react-native-0.81) last week with support for Android 16 (API level 36) and experimental support for faster iOS builds using recompilation.

“As previously announced by [Google](https://thenewstack.io/googles-gemini-cli-agent-comes-to-github/), Android 16 requires that apps are displayed edge-to-edge with no support for opting out,” the React Native team wrote. To do that, they have depreciated `SafeAreaView`.

If your app uses it, you will see warnings in React Native DevTools, the team warned.

“It will be removed in a future version of React Native,” they added. “We recommend that you migrate to `react-native-safe-area-context` or a similar library to ensure your app looks its best across all platforms.”

They also added a new Gradle property `edgeToEdgeEnabled` to let developers decide whether to enable edge-to-edge on all supported Android versions beyond 16.

Also, support for JavaScriptCore (JSC) engine will now shift to a community-maintained package that is released separately from React Native itself. So, React Native 0.81 removes the built-in version of JavaScriptCore. Any apps that require JavaScriptCore should now move to the community package in order to upgrade to 0.81, the blog post added.

There’s also a list of breaking changes in this update for developers to review, including that it now requires Node.js version 20.19.4, which is the latest Maintenance LTS version at the time of writing, or higher.

React Native 0.81 also shipped with a variety of other stability improvements and bug fixes.

## FlashList v.2 Rewritten for React Native’s New Architecture

Speaking of React Native, [FlashList](https://shopify.github.io/flash-list/) is a high-performance list component for React Native. It was created to address the performance issues commonly found with the standard FlatList component. Both are for displaying long lists of data. Since its release in 2022, FlashList has become popular in the React Native community with more than 2 million monthly downloads.

Now that React Native has a new architecture, [Shopify has rewritten FlashList v.2](https://shopify.engineering/flashlist-v2?ck_subscriber_id=2264736565) from the ground up to be faster, more precise and easier to use, the team wrote.

The post relays the problems with FlashList that are resolved by the rewrite, including a new scrolling system, a resolution to precision problems and improved horizontal lists. The blog post details all the changes this revamp incorporates.

## Turbopack Builds Now Beta in Next.js 15.5 Release

[Next.js 15.5 was released](https://nextjs.org/blog/next-15-5) on Monday, and it makes production Turbopack builds available as a beta feature. That’s led to faster site builds, the Next.js team wrote in a recent post.

TurboPack now powers Vercel websites, including [Vercel.com](https://vercel.com/), [v0.app](https://v0.app/) and [nextjs.org](https://nextjs.org/), the team added.

“These applications powered by Turbopack have been battle-tested, serving over 1.2 billion requests since the rollout,” the post stated.

Turbopack was designed to take advantage of multiple CPU cores throughout all phases of the build, thus letting developers scale build performance as an application grows. Using Turbopack has led to “consistent improvements in compilation time.” There are several anonymous examples of this, including a large site of 70K modules that’s now five times faster on a 30-core machine.

“When compared with Webpack, our production metrics monitoring shows that sites built with Turbopack serve similar or smaller amounts of JavaScript and CSS across fewer requests, leading to comparable or better FCP, LCP and TTFB metrics,” the team wrote.

The Next.js team is requesting that any problems with Turbopack be reported on [GitHub for Next.js](https://github.com/vercel/next.js/discussions/77721). This release also includes the introduction of Node.js middleware as stable.

Node.js runtime won’t be the default in Next.js 16, but they are considering making it the default in Next.js 17, pending community feedback and usage patterns.

This release also included major Typescript improvements to the App Router and stable typed routes. There’s also a list of deprecation warnings for the Next.js 16 release, including:

* The legacyBehavior prop for next/link;
* AMP support;
* The quality settings for next/image, which will be restricted to 75 by default, and
* Query strings with local image src paths will require explicit configuration in images.localPatterns.

## SvelteKit Now Works in Edge Environments

Earlier this month, the Svelte team released a list of updates for Svelte and SvelteKit. Among the changes: SvelteKit’s read now works in edge environments where `fs.readFile` isn’t available. That includes Cloudflare’s Workers and Netlify and Vercel’s edge functions.

Also, remote functions can now be called anywhere in an application, but always run on the server. That allows developers to safely access server-only modules containing, for instance, environmental variables and database clients.

Finally, [vite-plugin-svelte](https://github.com/sveltejs/vite-plugin-svelte/blob/main/packages/vite-plugin-svelte/CHANGELOG.md) now supports Vite7 and rolldown-vite. There are more changes, as well as a community showcase, learning resources, libraries, tools and component links on the [full post](https://svelte.dev/blog/whats-new-in-svelte-august-2025).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)