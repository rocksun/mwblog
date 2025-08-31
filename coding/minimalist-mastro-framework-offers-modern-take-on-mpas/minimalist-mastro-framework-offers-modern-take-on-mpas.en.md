There’s not much that can go wrong at 700 lines of code, according to computer scientist and [frontend](https://thenewstack.io/introduction-to-frontend-development) developer [Mauro Bieg](https://github.com/mb21).

“If I’ve learned anything as a software dev, it’s that fewer lines of code are better,” Bieg told The New Stack. “Fewer things that can go wrong, fewer things to maintain.”

That’s why Bieg created [Mastro](https://github.com/mastrojs/mastro/), a modern JavaScript meta-framework designed to build multipage apps (MPAs). Its core is approximately 700 lines of TypeScript, he said. It’s a great framework for beginning developers and veterans who want a streamlined approach to building multipage apps, Bieg said.

## Frontend Development Lessons Learned

Bieg grew up with [PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/) and later [Ruby on Rails](https://thenewstack.io/why-ruby-on-rails-is-still-worth-your-while-as-a-developer/). He remembers when the term “responsive design” was coined and progressive enhancements meant something. He tried Angular, but ultimately embraced [React](https://thenewstack.io/react-compiler-is-coming/) for projects with a lot of interactivity. He still does Ruby on Rails for basic websites.

Then he was offered a frontend team lead position. The organization had an existing [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/) app.

“I figured sure, why not? React is really nice to develop with and if they figure out how to make it do normal websites, that’s cool I suppose. Everybody seemed to be using it, so how bad it can be.”

He found out first-hand, he continued.

“At least for our use case — a newspaper website — 99% of the [JavaScript](https://thenewstack.io/introduction-to-javascript/) payload in the client was a complete waste,” he said. “We had a few interactive widgets — like slideshows, menus, etc. — but 99% of the DOM that React was hydrating was completely static.”

He settled on [Astro with islands](https://thenewstack.io/how-astro-and-its-server-islands-compare-to-react-frameworks/), because it would allow them to incrementally transition their existing React components without a full rewrite. However, he left to be a CTO and sole developer at a startup before the migration.

Astro seemed like a good fit at that job, too. He paired it with [Solid.js](https://thenewstack.io/solid-js-creator-outlines-options-to-reduce-javascript-code/) instead of React. Solid offered the same functionality as React but was more performant, he found.

> How minimal could you actually get away with?

“I still like Astro a lot and admire them for their awesome marketing, bringing MPAs and island architecture back into the mainstream JS discourse,” he said. “But every once in a while, I would run into oddities and rough edges where they’ve sort of designed themselves into a corner and are now stuck there due to backwards-compatibility and inertia.”

That led him to wonder: How minimal could you actually get away with? What would be the simplest, smallest, most low-maintenance MPA framework that you could build that would still allow a developer to do 95% of use cases effortlessly, but just with much less complexity?

“It seemed like if you focused on MPAs, this would allow you to remove the binder for most websites,” he said. “And removing the bundler would remove this whole layer of indirection that you need to debug if things go wrong.”

## An MPA Renaissance?

Next.js, [Nuxt](https://thenewstack.io/creators-of-nuxt-js-and-nitro-join-vercel/), Astro, SolidStart, [SvelteKit](https://thenewstack.io/dev-news-sveltekit-2-0-state-of-rust-survey-and-ai-on-apple/) and [Qwik](https://thenewstack.io/javascript-on-demand-how-qwik-differs-from-react-hydration/) all use a bundler/transpiler such as [Vite](https://thenewstack.io/vites-creator-on-a-unified-javascript-toolchain-and-vite/) or [Webpack](https://thenewstack.io/airbnb-moves-from-webpack-to-metro-enjoys-shorter-build-times/), and with the exception of Astro and Qwik, all of them are SPAs, he wrote in a [blog post last year](https://mb21.github.io/blog/2024/04/13/mpa-no-bundler-javascript-meta-framework-separating-client-server-code.html). *(Editor’s Note: SolidStart and SvelteKit are considered hybrid frameworks. SolidStart can create both SPAs and MPAs, and SvelteKit takes an approach that offers the benefits of both.)*

“I would love to have a modern JS meta-framework that does away with these two conventions, but instead chooses to optimize for simplicity and leveraging browser-built-ins over client-side JavaScript,” he wrote in the post.

This vision guided the creation of Mastro. Mastro is a [static site generator](https://thenewstack.io/get-back-basics-static-website-generators/) and web framework built from [first principles](https://addyosmani.com/blog/first-principles-thinking-software-engineers/). It offers a simple file-based router, a few composable functions to return HTML and standard `Response` objects.

It builds MPAs because, for most use-cases, modern browsers can do client-side routing better than JavaScript, Bieg contended.

“MPAs are (finally) having a Renaissance,” Bieg told The New Stack via an email interview.

> “I would love to have a modern JS meta-framework that does away with these two conventions, but instead chooses to optimize for simplicity and leveraging browser-built-ins over client-side JavaScript.”  
> **– Mauro Bieg, frontend developer and computer scientist**

Bieg put forth the [case for MPAs in a 2023 post](https://mb21.github.io/blog/2023/09/18/building-a-modern-website-ssg-vs-ssr-spa-vs-mpa-svelte-vs-solid.html#single-page-app-spa-vs-multi-page-app-mpa). He noted that with SPAs, the idea is that developers are trading upfront page load time for a better user experience later on.

“You don’t need to reinitialize everything after a page navigation,” he stated. “And arguably, SPAs have better page transitions than browsers used to have.”

All fine and well, but browsers have improved since then and the balance is shifting away from SPAs, he contended.

“Modern browsers have no flash of white between pages anymore, they have back-forward caching and service workers for offline functionality, etc.,” he wrote.

He still sees use cases for SPAs — for instance, playing audio or video during page navigation, or otherwise keeping state in the DOM (like cursor position) that cannot be easily persisted in localStorage.

“My take is that 99% of websites should be MPAs,” he stated. “Unless you’re building the next Figma or Google Docs, it seems to me that you’re better off doing an MPA with some interactive islands, and if you want to polish things, use the CSS view-transitions and make sure you don’t break the browser’s [bfcache](https://developer.mozilla.org/en-US/docs/Glossary/bfcache).”

With MPAs, developers profit from the reduction in JavaScript bundle size.

“Let the browser handle what is was built to do: page navigation, scroll restoration, page caching, streaming in HTML — and an `HTTP GET` that returns HTML is way easier to debug than [RSC’s (React Server Components)](https://thenewstack.io/frontend-schism-will-react-server-components-destroy-react/) stream of [JSX](https://thenewstack.io/beyond-jsx-rethinking-the-component-model-in-frontend/),” [he wrote in a blog post](https://mb21.github.io/blog/2023/09/18/building-a-modern-website-ssg-vs-ssr-spa-vs-mpa-svelte-vs-solid).

## Mastro’s Approach to Data-Fetching, Error Handling

For data fetching, Mastro uses the [standard fetch function](https://github.com/mastrojs/mastro/blob/main/examples/todo-list-server/routes/todo-list.client.ts), which [Deno](https://thenewstack.io/denos-response-to-nodes-recent-support-for-typescript/) and [Node.js](https://thenewstack.io/a-backend-for-frontend-watt-for-node-js-simplifies-operations/) support as well, he said.

It also isn’t opinionated about error handling. He is considering adding a small Rust-like “Result” type and a few helper functions either in the guide, a separate module, or a separate export such as “mastro/result” one day.

“I don’t think there is a need to be opinionated about this in Mastro core,” he said via email. “Some people are okay handling untyped exceptions, which has been the default in the JavaScript world since forever.”

Mastro uses Deno for its [runtime engine](https://www.pcmag.com/encyclopedia/term/runtime-engine).

“I wanted to start with something clean, without the baggage of Node’s 20 years evolution, and rely on that platform as much as I could,” he wrote. “For example Deno comes with ‘Deno.serve,’ which takes a ‘(req: Request) => Response handler,’  which is a great simple API.”

That said, [Bun](https://thenewstack.io/dev-news-react-19-bun-comes-to-angular-and-github-ai-fund/) and Node.js compatibility are on his to-do list.

## Reactive Mastro

Mastro has its own reactive GUI library called Reactive Mastro. While developers can use any client-side library, such as HTMX or even jQuery, together with Mastro, Reactive Mastro is Bieg’s minimal take on a reactive client-lib. It also goes also the other way, he said: Developers can use Reactive Mastro with any HTML-generating tool such as PHP, Ruby on Rails, etc. He explained in the documentation [why he took that approach](https://mastrojs.github.io/reactive/why-reactive-mastro/) and how it compares to other frameworks.

Mastro also uses the maverick-js/signals library to implement signals.

“What Mastro and Reactive Mastro really share is the minimal philosophy (and yes, the html module),” he wrote. “I’m hoping signals will be standardized sooner rather than later (they’re working on it), then I could almost cut the size of Reactive Mastro in half.”

## What Mastro Offers Developers

Bieg listed Mastro’s benefits to [frontend developers](https://roadmap.sh/frontend):

* Fewer things to understand. “The functions compose well together, so you don’t need to learn yet another function to do basically the same thing,” he said. “ For example, unlike other frameworks, Mastro doesn’t care whether you send HTML or JSON over the wire, you just give it a standard `Response` object, and it would be four lines of code to send XML instead. And incidentally, a handler function (req: `Request`)”
* More control. “Mastro really doesn’t do much, so you’re very close to the underlying runtime (e.g. Deno for server-side JavaScript, or the browser for the HTML, CSS and client-side JS),” he stated. “Mastro never auto-injects anything into your page. If you see something weird in your page, it’s probably a browser extension like an ad block.”

If there’s one thing that’s not very simple in implementing Mastro, it’s the file-based router, he wrote.

“I just wanted people to be able to drop an HTML or CSS file in the **‘**routes/ folder’ and have Mastro serve it like in the good old Apache/PHP days,” he stated. “It’s such a great way to start a project.”

Also, because Mastro is so small, it loads quickly on the edge, where developers often have problems with slow cold start if they load too much code, he said,

“Because it’s so small, you can run it easily in the browser as well, like with the Mastro VSCode for Web extension, which is actually a first I think, a static site generator running entirely in the browser,” he wrote. Eleventy is also working on it, but has not delivered that function as of publication.

## Mastro: No Bloat, No VC Money, No Hosting

Mastro could be used to build most projects on the web today, but it’s also great for beginners who are new to JavaScript, he said. In fact, he wrote his documentation as something of a tutorial for beginners, with the option to skip ahead if you’re a web development veteran.

With Mastro, there’s no bundler and no client-side JavaScript by default. There’s also no bloat, no VC money to “prevent eventual enshitification,” the website states, no hosting services to sell you on, and no “update treadmill.”

“We use the platform and [almost no dependencies](https://jsr.io/@mastrojs/mastro/dependencies), which allows us to keep things small and low-maintenance,” the site states. It says “we,” but actually it’s just Bieg for now. At 700 lines of code, he added, it’s not hard to maintain.

But Bieg does want community feedback and suggestions.

“I’d love for some sort of community to form around it, sharing recipes, docs or even libraries that work well with Mastro,” he said. “Currently, I see that happening mostly in GitHub issues, but perhaps it might soon be time to open a Discord or Discourse. Right now, I’m still in the stage of getting the word out and seeing what aspects of Mastro resonate with whom and what crowd it attracts.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)