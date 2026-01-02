The year 2025 proved to be a transformative period for the JavaScript ecosystem, marked by a shift toward performance optimization and “[post-React](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)” exploration. We look back at the stories and trends that dominated the JavaScript community in 2025.

## Challenging React

While React remains a central pillar of development — even LLMs, when left to their own devices, will primarily [push out React code](https://thenewstack.io/why-ai-is-generating-lowest-common-denominator-react-code/) —  in 2025, more developers called for a “web standards first” philosophy that prioritizes simplicity, as developers began to question the necessity of heavy client-side abstractions.

In part, this is because modern browsers have matured enough to handle tasks previously requiring React, including support for the [View Transitions API](https://thenewstack.io/interop-unites-browser-makers-to-smooth-web-inconsistencies/) and [web components](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/). We also saw this with [Remix 3](https://thenewstack.io/remix-3-and-the-end-of-react-centric-architectures), which challenged React-centric architectures by prioritizing web fundamentals with loaders/actions over React-specific state management. It signalled that React should be the view layer, not the foundation.

But it wasn’t all bad news for React: It now has its own foundation. In a major [governance shift for React](https://thenewstack.io/react-foundation-leader-on-whats-next-for-the-framework/), Meta moved the framework’s governance to an independent foundation under the Linux Foundation, with the goal of fostering corporate neutrality and broader ecosystem contribution.

## Framework Trends: MPAs, Signals and Compilers

Frameworks didn’t slow down in 2025. In fact, the year saw new frameworks introduced — including the [microframework Hono](https://thenewstack.io/hono-shows-the-way-for-microframeworks-in-a-post-react-world/), which is used for edge computing.

There was also the [React-based One](https://thenewstack.io/one-lets-frontend-devs-build-once-deploy-web-and-native-apps/), which supports the creation of create both web and native platform applications. The year also saw the release of the [minimalistic Mastro](https://thenewstack.io/minimalist-mastro-framework-offers-modern-take-on-mpas/), which is used for multipage apps. It champions “zero-JS by default” and enables browser-native routing instead of heavy client-side SPAs. Finally, there was [Wasp](https://thenewstack.io/javascripts-missing-link-wasp-offers-full-stack-solution/), which offers a full-stack solution that creates a Ruby on Rails-like experience for the React/Node ecosystem.

When it came to non-React frameworks, Signals became a keystone of reactivity. Signals uses reactivity only for the exact part of the UI that is updated. [Angular](https://thenewstack.io/angular-v21-adds-signal-forms-new-mcp-server/), Vue, Solid and Svelte all now use Signals for state management. There’s even a push to add [Signals to the JavaScript specifications](https://github.com/tc39/proposal-signals).

But moving forward into 2026, Ryan Carniato, creator of SolidJS, predicted that [fine-grained reactivity may be the next frontier](https://thenewstack.io/solidjs-creator-on-fine-grained-reactivity-as-next-frontier/) for non-React frameworks.

“It’s hard to ignore the impact when pretty much every framework other than React has adopted Signals first-class at this point,” he said, adding that “we’re just at the beginning of a much bigger change, and I’m not alone in this thinking.”

We also saw a focus on fine-grained reactivity with [Runes in Svelte 5](https://thenewstack.io/youll-write-less-code-with-svelte-5-0-promises-rich-harris/), which was released in late 2024.

Compilers are also taking on more heavy lifting. [Svelte 5’s Runes](https://svelte.dev/blog/svelte-5-is-alive), which were released as stable at the end of 2024, rely on Svelte’s compiler. The compiler transforms [Runes](https://svelte.dev/blog/runes), which look like functions, into a Signals runtime. The [React Compiler](https://thenewstack.io/meta-releases-open-source-react-compiler/) also was marked as stable this year. React uses the compiler to automate memoization, which is a term for changing how much of the UI re-renders, as opposed to changing how the data updates (which is what the Svelte compiler does).

In both cases, though, the compiler is doing some of the heavy lifting of transforming”human-readable” code into optimized machine code to avoid unnecessary re-renders.

## Tooling: The Battle for a Unified Stack

At the end of 2024, Vite creator [Evan You announced VoidZero](https://thenewstack.io/vite-creator-launches-company-to-build-javascript-toolchain/), a company dedicated to creating a unified Rust-based toolchain for the web development community. This ecosystem of tools would finally address the “fragmentation tax” of JavaScript development — where developers “duct-tape” together dozens of tools.

TNS Senior Editor [Richard MacManus spoke with You](https://thenewstack.io/how-vite-became-the-backbone-of-modern-frontend-frameworks/) about the resulting unified toolchain, Vite+, in October. “Vite+ is a [unified layer](https://thenewstack.io/vites-creator-on-a-unified-javascript-toolchain-and-vite/) that put all these things together under one coherent solution, right? So it is a drop-in superset of Vite itself,” You said.

It bundles several different [open source projects](https://thenewstack.io/does-your-open-source-project-need-foundation-oversight/) You’s company is working on, including:

* Rolldown, a new Rust-based [bundler](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/) for Vite;
* Oxlint, a Rust-powered linter for JavaScript and TypeScript;
* Vitest, a Vite-native testing framework; and
* Oxc, a collection of JavaScript tools written in Rust.

## AI and Frameworks

AI moved from the backend to the frontend in 2025. We saw a host of MCP servers launched to help frameworks connect best practices and standards with AI, including MCP servers from Angular and React, with more planned by frameworks such as TanStack Start.

Framework maintainers like Minko Gechev even experimented with an “[LLM-first” framework](https://blog.mgechev.com/2025/04/19/llm-first-web-framework/) designed specifically to be easily written and debugged by AI agents. TanStack recently released [TanStack AI](https://thenewstack.io/tanstack-adds-framework-agnostic-ai-toolkit/), an alpha release of a new framework-agnostic AI toolkit for developers.

We’ve also seen a shift to using AI within the browser, with [libraries like AsterMind-ELM and TensorFlow.js](https://thenewstack.io/javascript-library-runs-machine-learning-models-in-browser/) allowing developers to train and run machine learning models directly in the browser with microsecond latency, bypassing the need for expensive server-side GPUs. There’s also [Hashbrown](https://thenewstack.io/run-ai-agents-in-the-browser-with-the-hashbrown-framework/), an open source framework that lets AI agents run in the browser.

## Looking Ahead to 2026

The year 2025 led to JavaScript progress in surprising ways, but perhaps leaves more questions than it answered. Will [frameworks finally be pushed to converge](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/)? Will more frameworks be launched in 2026 to address new concerns and needs? What will AI mean for JavaScript and the ecosystem that supports it?

Hopefully, in the coming year, we’ll get answers to those questions.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)