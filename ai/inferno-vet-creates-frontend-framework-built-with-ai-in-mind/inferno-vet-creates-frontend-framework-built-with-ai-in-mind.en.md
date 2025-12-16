Ripple, a new [TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/)-based UI framework, might be shrugged off as just another framework if it weren’t created by [Dominic Gannaway](https://github.com/trueadm).

Gannaway created [InfernoJS](https://www.infernojs.org/), a fast UI library similar to React. He also worked on the [React](https://thenewstack.io/why-reacts-boring-maturity-is-actually-its-main-strength/) core team for three of his six years at Meta. He has been a software engineer at [Vercel](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/) and Bloomberg and is now a principal product engineer at [Attio](https://attio.com/), an AI-native Customer Relationship Management (CRM) platform. Oh yes, he also contributed to [Svelte](https://thenewstack.io/svelte-adds-asynchronous-sync-inside-components/) 5.

Ripple is in early development and not yet ready for production, but it’s already creating a buzz in JavaScript circles. The New Stack spoke with Gannaway about the framework and why he chose to create it when [AI is already impinging on frontend development](https://thenewstack.io/how-ai-agents-are-quietly-transforming-frontend-development/).

## Why: Developer Experience for Debugging AI

It turns out, AI and [large language models (LLMs)](https://thenewstack.io/introduction-to-llms/) are partly responsible for the creation of Ripple.

“I wouldn’t even attempt to try this a couple of years ago, but now with AI tooling, it’s actually quite an interesting proposition,” he said. “If we’re going into a world where we’re letting LLMs write a lot of our logic, then we’re going to be doing a lot more reading, and the reading won’t be our code. It will be maintaining and looking at what the AI is generating.”

Most engineers already read and review more code than they write, he added, noting that the situation is unlikely to change as LLMs generate more code.

That’s also why he focused on developer experience instead of speed for this framework. While it is fast, he said, he focused first on creating an “exciting experience when debugging,” with the goal of making it easier to find out why something is happening.

“Ripple will always be very quick, so the main thing we focused on was the developer experience: Having code that is just much simpler, much easier to read and ergonomic, having a reactive system that you don’t fight with, having a very small set of [APIs](https://thenewstack.io/its-time-to-build-apis-for-ai-not-just-for-developers/), that by having fewer of them it means that you can remember them quickly and quicker, and you can then compose them better,” he explained.

## Ripple Is a Language

When it comes to frameworks, Ripple differs in a number of key ways. First, Ripple isn’t just a framework, Gannaway said. It’s a language.

“In order to be its own language, but be familiar enough to people who come from JavaScript to TypeScript, Ripple needed to be a superset of one of them,” he explained.

He opted to make it a superset of TypeScript, because TypeScript incorporates types.

”It’s a big project, because it’s not just a framework; and it sounds weird, but you have to build a language server to make it so that your TypeScript stuff works,” he said. “You have to make it so your syntax highlighting works. You have to make it so Prettier and ESLint and all the sorts of ecosystem tooling.”

> “In order to be its own language but be familiar enough to people who come from JavaScript to TypeScript, Ripple needed to be a superset of one of them.”  
> **– Dominic Gannaway, creator of Ripple**

[Prettier](https://prettier.io/) is an opinionated code formatter used in JavaScript and TypeScript. [ESLint](https://thenewstack.io/poor-password-hygiene-enabled-eslint-supply-chain-attack-on-npm/) is a widely used, open source static code analysis linter.

Ripple also has its own file extension: .ripple.

## Ripple’s Approach to Fine-Grained Rendering

Ripple supports fine-grain rendering, which is a bit like React… but also not, he cautioned. It’s a mix between the React world of top-down rendering, but at a fine-grain level, he said.

“Values need to be associated with the component tree, a bit like React in that new state has to be used within a component, and that enables the connection to be about the component and not about the effect,” he said. “What we do instead is we have this ability for the dependency to know about the version on the signal.”

Every time a signal is changed, its version changes, he added. When Ripple calls an update, it goes through the tree and, rather than re-render, it just checks to see whether an update is needed.

## No Support for SSR, Signals or React Server Components

One thing Ripple does not support at this time is [server-side rendering](https://thenewstack.io/is-server-side-rendering-reacts-holy-grail/) (SSR).

“I wanted to focus on building a really [SPA (single page app](https://thenewstack.io/spas-and-react-you-dont-always-need-server-side-rendering/)) experience and nailing that functionality,” he said. “The reason for doing that is it gives us a good idea about stability, about our APIs and how our design choices are working or not working. But also it allows us to take some time to rethink how we can do hydration and the sorts of things that couple with server-side rendering.”

Another difference between Ripple and other frameworks is that many other frameworks rely on both a [virtual DOM](https://thenewstack.io/javascript-framework-reality-check-whats-actually-working/), which is a memory representation of the UI tree, and a Reactive Graph or [Signals](https://thenewstack.io/did-signals-just-land-in-react/). This dual architecture requires more memory and CPU time for connection, disconnection and cleanup.

“One of the discoveries I had working on Svelte was that we didn’t actually need to do that,” he said. “There is a way of doing that differently.”

By not using Signals, Ripple doesn’t need as much memory and or have as much overhead to clear down the tree or create the tree to begin with, he explained.

Also, Ripple will not support [React Server Components](https://thenewstack.io/react-server-components-in-a-nutshell/). He said this is because Ripple does not support server-side rendering.

## Ripple Can Be Used Inside React and Vice Versa

It’s possible to use Ripple within an existing React application, with the inverse also true: Developers can use React in a Ripple application.

“Ripple has the ability to be compatible, meaning you can incrementally adopt Ripple in an existing application,” Gannaway said.

Ripple will soon release a compatibility adapter for React. In the future, he plans to add [Solid](https://thenewstack.io/solidjs-creator-on-fine-grained-reactivity-as-next-frontier/), Svelte, [Vue](https://thenewstack.io/a-peek-at-whats-next-for-vue/) and other frameworks, so that there’s compatibility with all of them in Ripple.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)