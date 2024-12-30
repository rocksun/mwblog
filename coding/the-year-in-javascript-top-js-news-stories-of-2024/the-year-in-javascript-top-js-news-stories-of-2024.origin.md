# The Year in JavaScript: Top JS News Stories of 2024
![Featued image for: The Year in JavaScript: Top JS News Stories of 2024](https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1-1024x576.png)
The [JavaScript](https://thenewstack.io/5-javascript-libraries-you-should-say-goodbye-to-in-2025/) language will turn 30 next year — but it’s still changing and evolving in new and sometimes unexpected ways.

This year provided a good example of how dynamic the language can be. We saw the release of two new JavaScript meta-frameworks, plans for another JavaScript tool chain by Vue creator [Evan You](https://evanyou.me/), a new, open source [React compiler](https://github.com/facebook/react/tree/main/compiler) and Angular’s introduction of partial hydration — all indicators of a thriving language for [web development](https://roadmap.sh/roadmaps?g=Web+Development).

But 2024 also revealed signs of strain and wear in the language, such as a proposal by Google to split the language into two and complaints about JavaScript’s bloat.

All told, it was a busy year for JavaScript. Here’s a look at The New Stack’s top picks for 2024 JavaScript news stories.

## Signs of a Thriving Language: More Options
There’s a running joke that there’s a new JavaScript framework every month. Heck, one developer recommended [every developer try writing their own](https://thenewstack.io/learn-more-by-building-your-own-custom-javascript-framework/).

Some, however, are more significant than others.

One interesting entry into the meta-framework arena is [TanStack Start, a full-stack React framework](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/) powered by the popular TanStack Router, according to creator Tanner Linsley. The router directly competes with [routers from React](https://thenewstack.io/remix-react-router-merge-jetbrains-ide-for-test-automation/), Next.js and Redwood.

Also JavaScript framework Solid introduced its own [meta-framework this year called SolidStart](https://thenewstack.io/how-js-meta-framework-solidstart-became-router-agnostic/). A meta-framework adds extra features for tasks such as routing, server-side [rendering and build](https://thenewstack.io/slow-jamstack-builds-netlifys-solution-is-distributed-persistent-rendering/) processes, although SolidStart is deliberately decoupled from a specific router.

Ryan Carniato, creator of [Solid](https://thenewstack.io/solid-js-creator-outlines-options-to-reduce-javascript-code/), started work on SolidStart three years ago because he saw that server-side rendering was going to push people into “really wanting a meta-framework,” he told The New Stack.

“It’s expected now that you have some kind of starter that handles it, so I built SolidStart originally for that reason.”

Finally, Evan You, creator of Vite and the JS framework Vue, announced the formation of a new company, VoidZero, Inc., which will be dedicated to building a [unified JavaScript tool chain](https://thenewstack.io/vite-creator-launches-company-to-build-javascript-toolchain/). It came out of You’s work on a new bundler called Rolldown, when he realized the challenges he has with Vite are a reflection of a fragmented JavaScript ecosystem.

“Such a toolchain will not only enhance Vite but also drive significant improvements throughout the JavaScript ecosystem,” Vue wrote in a [blog post about the move](https://voidzero.dev/posts/announcing-voidzero-inc).

## Angular Introduces Incremental Hydration
[Angular conducted a survey of what frameworks](https://thenewstack.io/angular-vs-react-how-to-choose-the-right-framework-for-you/) were offering in terms of partial hydration and found that despite a lot of talk, there wasn’t a lot of actual implementation. The exception was Astro, with its [Island approach to hydration](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/), which it introduced last year. The framework shipped [incremental hydration with Angular 19](https://thenewstack.io/angulars-approach-to-partial-hydration/).
Creating Angular’s incremental hydration took multiple years and started with the shipment of deferrable views in version 15. Deferrable views are [Angular’s native lazy loading](https://thenewstack.io/deferable-views-page-load-improvements-coming-to-angular/) built-in framework primitive for being able to defer load chunks and specify when those load.

Event replay (which shipped in Angular 18) and defer block also play a role. Defer blocks in Angular are used to delay the execution of certain parts of a component’s template until they are needed. Developers can specify what will trigger the interaction.

## Problems JavaScript Encountered in 2024
But all is not perfect in the JavaScript world, and there are signs of strain on the 29-year-old language.

For instance, not everyone is a fan of the many frameworks. Some [advocate for a return to vanilla JavaScript](https://thenewstack.io/frontend-strategies-frameworks-or-pure-javascript/). TNS Senior Editor Richard MacManus explored [whether we’re in a post-React world](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/). As it turned out, this year’s State of JavaScript survey did reveal a slight decline — 2% — in the number of developers reporting that they used React this year. Overall, however, it remains the [top framework among](https://thenewstack.io/javascript-python-and-java-among-tops-in-language-rankings/) survey respondents.

But this year’s survey did show that the [use of TypeScript outpaced JavaScript use](https://2024.stateofjs.com/en-US/usage/). The survey, released this month, found that 67% of respondents stated they write more TypeScript than JavaScript code. TypeScript is JavaScript with syntax for types.

That’s not the only indicator of dissatisfaction with the language, though. In October, [Google proposed splitting the language into two parts](https://app.daily.dev/posts/the-proposal-to-split-javascript-into-two-languages-an-overview-mdlmsjvsq):

- JS0 would contain only essential features but still be implemented directly in the browser.
- JSSugar would offer additional features, extended features and syntax. But it would need to be compiled down to JS0 using tools similar to Webpack.
It could be the answer to the public pushback, given by some noteworthy [developers this year, against JavaScript’s complexity and bloat](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/). But — and we know this may be [shocking](https://www.youtube.com/watch?v=HMIyDf3gBoY) to a few — it also [sparked debate among programmers](https://leaddev.com/technical-direction/should-javascript-really-be-split-in-two), with some raising [concerns about who stands to benefit](https://www.reddit.com/r/programming/comments/1ggaljn/who_stands_to_benefit_from_a_proposed_split_of/), others questioning whether it would ruin the language, and still [others suggesting using WebAssembly](https://medium.com/@phillipgimmi/javascript-vs-jssugar-vs-webassembly-6fd4bd41fe1f) to achieve the same results.

One [developer](https://news.ycombinator.com/user?id=sshine) pointed out that JavaScript is two languages:

- “JavaScript, the original assembly language of the internet, does not need new language features.”
- “JavaScript, the frontend web development language is a fractal of infinitely many sub-languages that transpile back to ES5.”
And speaking of schism, let’s not forget this year brought an actual battle over who should own the name “JavaScript.” In 2024, Deno petitioned to the United States Patent and Trademark Office (USPTO), asking that the [USPTO cancel Oracle’s trademark for JavaScript](https://thenewstack.io/deno-petitions-to-cancel-oracles-javascript-trademark/).

Ultimately, all of this sets up JavaScript for a fascinating, if potentially cantankerous, 30th birthday.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)