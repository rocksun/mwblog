# SolidJS Creator on Confronting Web Framework Complexity
![Featued image for: SolidJS Creator on Confronting Web Framework Complexity](https://cdn.thenewstack.io/media/2025/01/ef80dc2f-reactcode-1024x683.jpg)
Angular and Vue will be the frameworks to watch this year, predicted frontend expert and Solid.js creator [Ryan Carniato](https://github.com/ryansolid) recently.

“Both Vue and Angular are frameworks I’d have my eye on this next year,” [Carniato wrote in a Jan. 6 ](https://dev.to/this-is-learning/javascript-frameworks-heading-into-2025-hkb)blog post. “Not because I expect to be blown away by some innovation here, but because these tools go the extra mile in making developers happy. Sometimes the best tool isn’t the ‘best’ tool.”

Indeed, Google’s Product and DevRel lead, [Minko Gechev, recently](https://www.linkedin.com/in/mgechev/) announced that improving the [developer experience will be a priority for Angular](https://blog.angular.dev/angular-2025-strategy-9ca333dfc334) in 2025.

If you’re not familiar with Carniato, he’s the creator of the [SolidJS framework](https://github.com/solidjs) and the meta-framework [SolidStart](https://thenewstack.io/how-js-meta-framework-solidstart-became-router-agnostic/), which launched in 2024.

Like many framework authors, he’s also a thought leader in the JavaScript space — an honorific that he’s earned by speaking and writing deeply about JavaScript. He is often cited by other framework makers and leaders in the JavaScript sector.

Carniato foresees a quiet year on the frontend framework front — a period of reflection that could be a good thing as the community grapples with the complexity it’s created.

“The quest for simplicity hasn’t resulted in making web development simpler,” Carniato wrote. “We have a lot of complexity to catch up with. A lot of hard decisions to make on what technology is worth our investment and effort.”

While the “raw capabilities for the next generation of solutions exist,” Carniato isn’t sure that there’s the right combination of pieces yet to create a “consumable” solution.

“But at least we are beginning to acknowledge that in our quest for simplicity, we set ourselves on a path to add back that complexity in new ways,” he writes.

In his blog post and a recent [five-hour live stream](https://www.youtube.com/watch?v=D1XN8j77Ntk) (of which we tuned in for two hours), he explained some of the causes creating the complexity.

## Isomorphic SPA vs. Split-Execution MPAs
There’s a divide that’s arisen in JavaScript between [Multi-Page Applications](https://ellow.io/single-page-application-vs-multi-page-application/), which use a split-execution — think about [Islands in Astro](https://thenewstack.io/astro-launches-new-server-islands-and-partners-with-netlify/) or server components — and server-first, [Single Page Apps](https://thenewstack.io/spas-and-react-you-dont-always-need-server-side-rendering/) (SPAs) that are isomorphic in nature, according to Carniato.

![Solid.js creator Ryan Carniato shows a slide depicting the split between isomorphic and split-execution frameworks.](https://cdn.thenewstack.io/media/2025/01/a1c19542-ryancarniatoisomorphicvssplit-2.png)
Ryan Carniato shared a slide on the divide between isomorphic and split-execution frameworks during a recent live stream.

Isomorphic JavaScript, or Universal JavaScript, involves writing applications using JavaScript code that can operate both on the browser (client-side) and server-side.

With Isomorphic JavaScript, “the server generates the initial view of a webpage and sends it over to the client-side almost instantaneously for rendering while simultaneously downloading the full application in the background,” according to [this Sanity.io glossary](https://www.sanity.io/glossary/isomorphic-javascript). “This method reduces server load and significantly enhances user experience by speeding up page load times.”

Frameworks that are isomorphic in their approach include [Next.js](https://thenewstack.io/vercel-makes-changes-to-next-js-to-simplify-self-hosting/), [Nuxt](https://thenewstack.io/dev-news-react-19-nuxt-3-11-a-python-gui-tabnine-llms/) and [Sveltekit](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/).

They allow [developers to “optimize web application performance](https://thenewstack.io/how-to-master-javascript-performance-optimization/) while maintaining compatibility across different environments,” Sanity.io explains. Companies that have used isomorphic JavaScript for large projects include Airbnb, Facebook and Netflix.

Frameworks that rely on split-execution include [Astro](https://thenewstack.io/new-astro-releases-incorporates-sessions-new-astro-actions-tools/), [Fresh](https://thenewstack.io/denos-fresh-uses-server-side-rendering-for-faster-apps/) and [Next.js’ App Directory](https://nextjs.org/docs/app).

The push for server-first over the past five years has led to the rise of server-first meta-frameworks, specifically SelveKit, Astro, [Remix](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/), [SolidStart](https://thenewstack.io/solidstart-launches-next-js-15-releases-with-dx-questions/), [Qwik](https://thenewstack.io/javascript-on-demand-how-qwik-differs-from-react-hydration/), Fresh and [Analog](https://analogjs.org/), wrote Carniato. It also led to “significant upgrades to existing ones like Next and Nuxt,” he added.

“It is an exercise of two opposites trying to approach each other in the middle.”

– Ryan Carniato, creator of JavaScript framework SolidJS
“The last couple of years have seen SPA-influenced [isomorphic](https://thenewstack.io/doordash-building-isomorphic-javascript-libraries/) (same code runs differently on client/server) approaches up against MPA-influenced split-execution (Islands/Server Components) approaches in a search to find a universal solution for all,” Carniato wrote. “It is an exercise of two opposites trying to approach each other in the middle.”

That’s led to routing [developments such as Next App Router](https://thenewstack.io/why-developers-should-give-next-js-app-router-another-chance/) and View Transitions Routing, he wrote. He also cites other developments such as Out-of-Order Streaming, Server Functions, Optimistic Updates, Server Islands and Single-Flight Mutations.

But it’s also created complexity.

“When you assemble all these features, things are not so simple anymore,” he wrote. “If 2021/22 was a reset to a simpler base, a return to our beginnings on the server, 2024 reminded us that simple doesn’t always cut it.”

## Dealing With Complexity via Compilers
One way frameworks have dealt with this complexity is to use compilers, he adds. In 2024, developers saw the release of [React Compiler](https://thenewstack.io/meta-releases-open-source-react-compiler/) and [Svelte 5 Runes](https://svelte.dev/blog/runes). The React compiler is an “an auto-optimizing compiler, that transforms code in a way that reduces unnecessary re-execution without manual intervention,” he noted.

Svelte 5 Runes, on the other hand, “brings a syntactical sugar over a fine-grained Signals renderer,” he writes. To break that down a bit, signals manage application state by acting as reactive variables — they automatically update any part of the UI that depends on them when their value changes.

The compilers take very different approaches, he added.

“React acknowledging that re-renders do matter enough to optimize around,” he said. “Svelte traded away its minimal syntax for a more expressive language with increased capability and a better fundamental basis for performance. Ironically, these stances are both exactly opposite of their initial selling point.”

## Frontend Framework Predictions
Given all that, Carniato makes two predictions about what’s coming in 2025:

**A server-second approach.**“We already have started seeing some of the swing back of the pendulum towards the middle of 2024 with SPA modes in Sveltekit, SolidStart, and Remix.[Remix ported back their non-server functionality](https://thenewstack.io/remix-react-router-merge-jetbrains-ide-for-test-automation/)to React Router,” he wrote. “SolidStart’s additive approach to Server Functions and Single Flight Mutations laid down the eventual foundations for[TanStack Start](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/), a[React](https://thenewstack.io/redwood-framework-all-in-on-react-server-components/)framework built on the same principles.”**Growing pains for**“It is no secret that pretty much all non-React frameworks run off Signals now,” he wrote. “But some time has passed and developers are starting to understand the depths of tradeoffs present.” While he contended that these are minor issues, he said they may lead to a new respect for React.[Signals](https://thenewstack.io/javascript-in-2023-signals-reacts-rsc-and-full-stack-js/).
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)