We were promised elegance. What we got was runtime CSS parsing, unreadable class names, and hydration bugs straight out of hell. CSS-in-JS was supposed to free us from global namespace nightmares and styling spaghetti.

Instead, [it wrapped us in a shiny new layer of chaos](https://thenewstack.io/css-in-js-and-react-server-components-a-developer-guide/) — one that performs worse, reads worse, and somehow costs more CPU cycles to do what a plain stylesheet did perfectly fine two decades ago. This is not evolution; I’d call it over-engineering disguised as progress.

## From Liberation to Performance Lock-In

When CSS-in-JS first appeared, it felt revolutionary. No more global leaks, no more worrying about specificity wars, no more cryptic class collisions. We could co-locate styles with components, making everything modular and “self-contained.”

But the honeymoon ended quickly. Quickly, developers realized that generating styles at runtime [wasn’t a small tradeoff](https://dev.to/srmagura/why-were-breaking-up-wiht-css-in-js-4g9b) — it was a ticking performance bomb. What started as a way to simplify styling turned into one of the most expensive abstractions ever introduced into frontend development.

> By tying CSS generation to JavaScript execution, we effectively welded presentation to logic — the exact thing we were trying to avoid when we invented CSS in the first place.

The idea of dynamically computing CSS on the client side sounds clever, until you’re debugging a hydration mismatch at 3 a.m. because some SSR pass decided to hash class names differently between the server and browser. It’s the kind of issue that feels less like a bug and more like a punishment for trusting marketing copy. CSS-in-JS libraries made [the simple act of styling a button](https://css-tricks.com/a-thorough-analysis-of-css-in-js/) as complex as dependency injection. And let’s not even start on how much bundle size ballooned just to make borders blue.

By tying CSS generation to JavaScript execution, we effectively welded presentation to logic — the exact thing we were trying to avoid when we invented CSS in the first place. The elegance of separation was replaced with inline chaos wrapped in hooks and context providers.

## The Hidden Performance Tax of Convenience

Developers often defend CSS-in-JS with the argument that “the overhead is negligible.” It’s not. Runtime styling introduces measurable performance degradation — from the milliseconds lost parsing strings, to the memory overhead of style recalculations. Anything [involving commerce](http://www.commerce.com/) in digital form is at risk.

Every time a component mounts, the system has to create, inject, and sometimes even deduplicate style tags. Multiply that across hundreds of components, and you’ve turned your render cycle into a bureaucratic mess.

> What was once the web’s biggest advantage — lightweight rendering — is now being sabotaged by overzealous abstraction.

This is not hypothetical. Performance audits consistently show that CSS-in-JS frameworks add both network and runtime costs. You might not notice it on your 16-core dev machine, but your users on low-end devices certainly do. What was once the web’s biggest advantage — lightweight rendering — is now being sabotaged by overzealous abstraction.

The tragedy here is that the browser already has a battle-tested, optimized system for handling styles: CSS. We replaced it with a JavaScript imitation that’s slower, harder to debug, and occasionally decides to vanish on page refresh. CSS-in-JS didn’t make styling faster: it just [made debugging slower](https://stackoverflow.com/questions/56641028/accessing-css-styles-with-javascript-is-too-slow).

And yet, the cycle continues. Framework maintainers build patch after patch, trying to make dynamic styles “feel native.” But you can’t out-optimize the browser’s own styling engine. It’s like rebuilding a wheel inside a wheel — except this one leaks memory and needs an npm update every week.

## The Developer Experience (DX) Mirage

Advocates often claim CSS-in-JS improves developer experience. They’re right — until you actually have to maintain it. At first glance, it feels modern and ergonomic. Styles live in your component file. Scoped classes feel clean. Variables are accessible.

But once the codebase scales, the illusion collapses. You start hunting for missing prop interpolations, juggling context providers and rewriting logic — all because your styles can’t handle simple overrides without rewriting half the component tree.

Debugging CSS-in-JS feels like playing Minesweeper with class hashes. DevTools turns into a cryptic wasteland of obfuscated selectors. Inspect an element and you’ll find something like .css-4kq0lj{margin:0 auto} — not exactly readable. Good luck tracing that back to its source when you have a dozen styled components inheriting from each other like a dysfunctional family tree.

> This obsession with “DX” — developer experience — has become a smokescreen for architectural debt.

Worse, CSS-in-JS encourages overengineering. Why write a simple media query when you can import a hook and toggle the theme context dynamically? Developers who once debated whether to use Flexbox now debate which flavor of runtime styling performs 2% better on hydration. The mental load is immense. The payoff? Marginal at best.

This obsession with “DX” — developer experience — has become a smokescreen for architectural debt. Sure, it [feels nice to import styled-components](https://styled-components.com/docs/basics#extending-styles) and write CSS in backticks. But that dopamine hit fades quickly when your app’s performance tanks and your build times double. Convenience is not craftsmanship. And CSS-in-JS is convenient at the expense of clarity.

## The Return to Sanity: A Post-CSS-in-JS Future

Thankfully, the tide is turning. Even the most die-hard CSS-in-JS proponents are starting to admit it’s unsustainable at scale. Frameworks like Remix, Astro and Next.js 13 are nudging developers back toward simplicity — leveraging traditional CSS, CSS Modules, or static extraction instead of runtime generation. The message is clear: separation of concerns still matters.

The rise of CSS variables and [container queries](https://www.thisdot.co/blog/css-container-queries-what-are-they), as well as scoped styles, means modern CSS now handles most of what CSS-in-JS tried to fix — but natively, efficiently and predictably. No runtime penalties. No hash collisions. No invisible style tags clogging your DOM. Just styles that load instantly and behave consistently.

> CSS is not broken; our discipline is.

We don’t need to reinvent styling. We just need to respect the boundaries that made the web work in the first place. CSS is not broken; our discipline is. The answer isn’t more abstraction — it’s better understanding. The future isn’t about embedding CSS into JavaScript, but about writing maintainable styles that scale naturally with the web’s evolution.

Returning to fundamentals is simply maturity and a normal shift towards practicality. It’s realizing that adding layers of abstraction to solve problems we created ourselves is not innovation. It’s just pure denial.

## Modern CSS Solves the Original Problem

CSS-in-JS was born out of good intentions — modularity, predictability and componentization. But what we got was complexity disguised as progress. The web didn’t need runtime styling engines or cryptic hashes to stay modern. It needed restraint. It needed developers willing to accept that not every problem requires a library.

We’re entering a new chapter where simplicity is sophistication again, where global stylesheets coexist peacefully with scoped rules. Where the browser does the heavy lifting, as it was always meant to, it’s time to stop worshipping abstractions that slow us down and start trusting the platform we’ve spent decades improving. Ready to make the move?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/01/c616d407-alex-williams-2.png)

Alexander Williams is a full stack developer and technical writer with a background working as an independent IT consultant and helping new business owners set up their websites.

Read more from Alexander T. Williams](https://thenewstack.io/author/alextwilliams/)