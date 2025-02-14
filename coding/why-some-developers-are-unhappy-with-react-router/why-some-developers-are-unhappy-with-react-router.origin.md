# Some Devs Turn to TanStack After Remix/React Router Merger
![Featued image for: Some Devs Turn to TanStack After Remix/React Router Merger](https://cdn.thenewstack.io/media/2025/02/e7791ff0-remix-becomes-react-router-1024x683.jpg)
Meta-frameworks like SolidStart, SvelteKit and [Analog](https://thenewstack.io/google-engineer-outlines-whats-next-for-angular/) are so closely aligned with routers, they’re practically one and the same. In the case of Remix, that’s literally true since it merged with [React Router v7](https://remix.run/blog/react-router-v7) in November. That was first release after the team that maintains both Remix and [React Router](https://www.travis-ci.com/blog/react-router-demystified-a-developers-guide-to-efficient-routing/) opted to integrate the router into the framework last spring.

Not everyone is happy with the change, however, as a recent Reddit thread shows. In fact, many developers in the thread said they’re leaving the framework/router to embrace [TanStack router and its framework, TanStack](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/).

## Routers and Frameworks
Meta-frameworks are a tool that sits on top of or alongside a frontend framework such as React, [Vue](https://thenewstack.io/want-out-of-react-complexity-try-vues-progressive-framework/), or Angular, to provide additional features and structure for building complex web applications.

On the frontend, routers manage navigation and URLs within a web application without full page reloads. Generally, they ship as part of the meta-framework.

[Routers are a key part of that packag](https://thenewstack.io/how-js-meta-framework-solidstart-became-router-agnostic/)e, as Ryan Carniato, creator of framework Solid and co-creator of meta-framework SolidStart, previously told The New Stack. SolidStart became the first framework to emerge as router-agnostic last year, in part because of [Vite](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/) and a Vinxi, a wrapper that takes multiple Vite configs and funnels them together to create all the advanced features developers expect, like server components and server actions.
## How Can a Router Be a Meta-Framework?
Vite — which is a modern frontend build tool that serves as both server and bundler — has taken on more of the heavy lifting that builders and frameworks once performed, explained Remix + React Router core team member [Mark Dalgleish](https://github.com/markdalgleish) during a presentation at React Advanced 2024 called, concisely enough, “[How React Router Became a Framework](https://www.youtube.com/watch?v=BKi4YwLaMBI).”

The presentation digs deep into the meta-framework weeds about the transformation, but the long and short of it is that Remix and React Router have long been deeply integrated, which is fairly easy to achieve since the same team supports both. Changes to one often led to changes in the other, he said.

“React Router is a library. That’s not a controversial thing to say,” he told audiences. Remix adds “a bunch of stuff on top, but it means that the core DNA of Remix is really React Router the framework,” he continued.

He explains in detail how this happened, but it owes no small part to Vite’s evolution, particularly the upcoming [Environment API for Vite](https://vite.dev/guide/api-environment).

“Vite is really great tooling for JavaScript developers, but I want to flip it around today and highlight the other side of this, which is that, as a framework maintainer, it’s a really great platform for frameworks, and that’s why we’re seeing so many frameworks today built on top of Vite,” Dalgleish said. “So when we started going down this road, we really wanted to lean into this philosophy of saying that Remix is just a Vite plug-in.”

That plug-in philosophy didn’t quite work out, so what they’ve now switched to is that the open source Remix is “mostly a Vite plug-in,” he added.

“React Router is a library. That’s not a controversial thing to say.”

– Mark Dalgleish, React Router core team member
“What even is Remix at this point if the vast majority of the bundler-specific things are being done by the Vite plug-in, and that … gap between what Remix is and what React Router is continues to shrink?” Dalgleish questioned. “Why not just get rid of the indirection and have consumers import these things from React Router, the underlying library directly?”

Meanwhile, [React Router](https://remix.run/blog/merging-remix-and-react-router) is “managing the entry points to your application, including the commands you have to run,” Dalgleish said. “It gives you the official version now of the route module API that we got with Remix.”

It includes file system routing, server and client rendering conventions, as well as with SPA (single page application) mode and pre-rendering, he continued.

“It’s a pretty full-featured set here, so it’s fair to look at this now and say that React Router is now a framework,” Dalgleish said.

Frontend developer and creator of the Epic Stack Kent Dodds also explored the [connection between Vite and React Router](https://www.youtube.com/watch?v=rPjj6s7VPQM), becoming a framework at ViteConf 2023.

[React Router is open source](https://github.com/remix-run/react-router) and has been owned by Shopify since 2022. Efforts by The New Stack to reach the framework creator and CEO [Michael Jackson](https://x.com/mjackson?lang=en) by X did not receive a response.
## React Router’s Reach
Only 3% of respondents to the [State of JavaScript 2024 survey reported using Remix](https://2024.stateofjs.com/en-US/libraries/front-end-frameworks/). But [Theo Browne](https://github.com/t3dotgg), aka [t3dotgg](https://www.youtube.com/@t3dotgg), a JavaScript community influencer and former Twitch developer, pointed out that most React apps use React Router’s methodology today.

“Awesome to see them acknowledge that and be the path to bring the best things from the new React building to every other code base using React,” he said in his [mostly positive review](https://www.youtube.com/watch?v=5B1LScZtrb4). “I’ll be realistic here. There is no world in which Twitch could have realistically moved to [Next.js](https://thenewstack.io/why-developers-should-give-next-js-app-router-another-chance/) after all of the work that’s gone into the current website. This lets the benefits of [React 19](https://thenewstack.io/react-19-change-angers-some-devs-vector-database-use-jumps/) reach the Twitch code base and other giant ones like it.”

## Some Developers Reject the Paradigm
A Reddit poster who goes by [MustyMustelidae](https://www.reddit.com/user/MustyMustelidae/) in January started off the discussion with a throwdown about the change, revealingly titled, “[React Router v7 has to be a psyop](https://www.reddit.com/r/reactjs/comments/1iatblk/react_router_v7_has_to_be_a_psyop/).”

“I refuse to believe that the Remix team would take all the momentum their framework had and throw it at the wall like this,” MustyMustelidae wrote. “I think the team is made up of very smart people who are well tapped into the zeitgeist of JS (JavaScript) development and I refuse to believe they don’t know better.”

The poster continued to call the change self-sabotage.

“Frameworks don’t do this for incredibly obvious reasons,” MustyMustelidae stated. “It’d be like if [Svelte](https://thenewstack.io/youll-write-less-code-with-svelte-5-0-promises-rich-harris/) flattened their docs with [SvelteKit](https://thenewstack.io/dev-news-sveltekit-2-0-state-of-rust-survey-and-ai-on-apple/) and labeled it as ‘As a Library’/‘As a Framework.’ Or if [TanStack Start](https://tanstack.com/start/latest) became TanStack Router. There is no universe in which this is not strictly worse: for documentation purposes, for branding purposes, for SEO purposes, for support purposes.”

At least one poster said their entire “very large company” had switched to [TanStack Router](https://github.com/TanStack/router).

Several commenters did note that TanStack still has bugs and flaws, although they disagreed over the speed at which those were being addressed. One poster, [Veranova](https://www.reddit.com/user/Veranova/), thought TanStack should triage its issues. But Veranova and others still recommended it over React Router.

“It’s the best designed router we’ve had on the public API so I’m sure it will get there but there are some serious defects under the hood right now,” Veranova wrote.

## TanStack Router Creator Weighs In
[Tanner Linsley](https://www.linkedin.com/in/tannerlinsley/), who created the TanStack, joined the discussion to note that TanStack Start is still in beta and users can expect that it will change a bit. It’s worth noting that TanStack Start does leverage Vite as well. (*Editor’s Note: TNS did confirm with Linsley via Bluesky that it was he who made the remarks*.)
His meta-framework, TanStack Start, is a collection of plugins and runtime for server functions (Remote Procedure Call), server middleware, React Server Components, streaming and serialization, he noted. It’s a “flavor” of [server-side rendering (SSR)](https://thenewstack.io/how-to-build-a-server-side-react-app-using-vite-and-express/) for TanStack Router, he continued.

“Start adds a fill stack build system that is currently its own CLI but will soon just become a Vite plugin or similar,” he wrote. “This uses Nitro to deploy the server stuff basically anywhere and write portable server code that works just about anywhere.”

He also offered a link to a [chart comparing TanStack Router and TanStack Start](https://tanstack.com/router/latest/docs/framework/react/comparison) against Next.js and React Router/Remix.

## Bottom Line
Vite is changing frameworks; that much is clear. Vite’s Environment API was released as experimental in January.

Although it’s designed primarily for framework creators, it will likely lead to more changes in meta-frameworks that are leveraging Vite, which includes Nuxt, TanStack Start, SvelteKit, SolidStart, [Astro](https://thenewstack.io/new-astro-releases-incorporates-sessions-new-astro-actions-tools/) and [Angular’s Analog.js](https://analogjs.org/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)