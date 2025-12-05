Every time a React app misbehaves, the first tweet is some variation of “React sucks.” No, it isn’t (okay, who am I kidding, maybe a little bit) but what’s really breaking is your mental model of state.

Developers keep reaching for new state management libraries the way hungover people reach for greasy food: hoping it’ll fix what’s fundamentally self-inflicted. Zustand, Jotai, Recoil, Valtio — they’re all great tools.

But none of them can save you from chaos if you don’t understand how data moves through your app. React isn’t your scapegoat: your [state architecture](https://medium.com/@skylernelson_64801/state-architecture-patterns-in-react-part-2-the-top-heavy-architecture-flux-and-performance-a388b928ce89) is the main culprit here.

## The Addiction to Shiny State Management Solutions

The React ecosystem [breeds new state management libraries](https://thenewstack.io/frontends-next-evolution-ai-powered-state-management/) and approaches faster than npm can warn you about vulnerabilities. Every few months, a new one trends on X, promising simplicity, performance and an end to boilerplate. Developers rush to install it, convinced this time they’ve found *the one*. The honeymoon lasts until the first prop drilling conflict or synchronization bug. Then it’s back to blaming React — again.

But these libraries don’t solve the root issue: **unclear data flow**. Developers layer global stores, contexts and hooks without ever asking *why* the data lives where it does. They’re duct-taping logic onto the framework instead of designing an architecture. When everything updates everything else, you’ve built a minefield, not a UI.

> You can’t architect clarity by outsourcing thinking to the latest library.

What React gives you is composability. What you do with it determines whether your app feels elegant or brittle. You can’t architect clarity by outsourcing thinking to the latest library. You do it by understanding unidirectional data flow — React’s core principle — and sticking to it.

## Understanding Context Overload and the Provider Pyramid

If your component tree looks like the inside of a Matryoshka doll, you’re not alone. The “Provider Pyramid,” where half your app lives inside overlapping contexts, is the new callback hell. Everyone’s chasing global state convenience, but context isn’t a silver bullet. It’s a scalpel: powerful when used precisely, disastrous when overapplied.

Developers often [wrap everything in context](https://stackoverflow.com/questions/75060633/react-context-performance-and-suggestions) because it feels like shared state nirvana. But each provider introduces complexity. Debugging nested contexts becomes an archeological dig through useContext calls. Performance suffers because re-renders cascade through the hierarchy.

> The truth is, most data doesn’t need to be global.

And no, [switching to Zustand](https://tkdodo.eu/blog/working-with-zustand) won’t magically fix that. You’re still synchronizing state at the wrong granularity. Not to mention, if you’re running instances then [container security is another thing](https://checkmarx.com/product/container-security/) you have to worry about and take seriously. It’s safe to say it’s not the easiest kerfuffle I’ve found myself in.

The truth is, most data doesn’t need to be global. A shopping cart? Sure. Theme preferences? Maybe. But that “currently selected tab” or “temporary filter” state? Keep it local. The moment you globalize everything, you’ve lost control of your mental model. React encourages local reasoning — respect that boundary.

## Why Redux Wasn’t the Villain You Thought It Was

[Redux](https://thenewstack.io/top-10-javascript-libraries-to-use-in-2024/) became the [punching bag of React fatigue](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/); but in hindsight, it wasn’t the villain. It just made your architecture honest. Redux forced developers to think about data flow, action semantics and immutability. That discipline was painful, but it exposed where logic actually lived. The real issue wasn’t Redux; it was how teams abused it.

Many used Redux as a dumping ground for every variable — from authentication to whether a modal was open. The result was a global spaghetti bowl of actions and reducers no one understood. Then came the wave of “Redux is too complex” think pieces, conveniently ignoring that the complexity came from treating Redux like a database, not a coordination layer.

> Modern tools abstract away the boilerplate, but they don’t remove the need for mental discipline.

Modern tools abstract away the boilerplate, but they don’t remove the need for mental discipline. Whether you’re using Zustand, MobX, or React Query, the same principle applies: [state belongs where it’s most meaningful](https://thenewstack.io/the-pros-and-cons-of-using-react-today/). Global state should be the exception, not the default. You don’t need fewer libraries; you need fewer excuses.

## The Mirage of Simplicity in React Hooks

React hooks were supposed to simplify things. Instead, they became a new hiding place for architectural sins. Custom hooks are great for abstraction, but when you start nesting them like Russian dolls, you’re creating invisible coupling. Each use hides [dependencies and timing issues](https://react.dev/reference/react/use) that only surface in production — when your component tree starts acting possessed.

The seductive thing about hooks is that they *feel* composable. But composition without discipline is just chaos in layers. The mental cost of understanding where state changes originate multiplies fast. You end up with a dozen hooks sharing state in slightly different ways — each re-render triggering the others like dominoes.

Simplicity isn’t about fewer lines of code; it’s about predictability. The fewer mental hops between cause and effect, the saner your app will be. Before you write another useGlobalStore, ask if your hook really needs to exist. Most of the time, you can solve it with props and a clear hierarchy.

## How to Scale Your React App Without Losing Your Mind

Every React project starts clean. Then reality hits: more features, more components, more developers. Suddenly, state’s flowing like an unregulated river. That’s when teams panic and bring in a new library. But scaling isn’t about tools — it’s about patterns.

Colocate state with the components that use it. Pass data down deliberately, not reflexively. Use derived state instead of duplicating sources of truth. Split context providers by domain, not convenience. These principles aren’t trendy; they’re timeless. You can scale a React app without turning it into a dependency labyrinth if you [treat architecture as a living system](https://alexkondov.com/full-stack-tao-clean-architecture-react/), not a patchwork.

> Even at scale, most React chaos comes from neglecting fundamentals.

Even at scale, most React chaos comes from neglecting fundamentals. Don’t reach for complexity when clarity will do. The frameworks evolve, the syntax changes, but the laws of clean architecture never go out of style. React doesn’t demand perfection — just consistency.

## The Framework Isn’t the Problem, Your Architecture Is

Blaming React for state headaches is like blaming your car for bad driving: [why not just switch cars and stop complaining](https://thenewstack.io/why-devs-are-ditching-react-for-preacts-simplicity-and-speed/)? The framework does exactly what you tell it to do. If your components are thrashing, your context layers overgrown, or your hooks indistinguishable from black magic, that’s on you.

React is opinionated about one thing: data flows down. Everything else — side effects, synchronization and caching — is your responsibility. That’s not a bug; it’s a feature. It forces you to build with intention. When you abdicate that responsibility to whatever’s trending on GitHub, you trade understanding for temporary relief.

> Frameworks don’t create chaos; developers do.

You don’t need to rewrite your app in Solid, Svelte, or Vue. You need to stop duct-taping abstractions onto architecture you never fully designed. Frameworks don’t create chaos; developers do. Once you accept that, React stops being a pain and starts being a partner.

## Conclusion

React isn’t broken. Your architecture is. The endless cycle of swapping libraries, reinventing patterns and blaming the framework only masks the truth: state management is hard because thinking clearly is hard.

The solution isn’t another hook or global store; it’s humility and discipline. Understand how your data flows, design your state intentionally, and React will stop feeling like an adversary. Stop blaming React for your hangover. You poured the drinks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/01/c616d407-alex-williams-2.png)

Alexander Williams is a full stack developer and technical writer with a background working as an independent IT consultant and helping new business owners set up their websites.

Read more from Alexander T. Williams](https://thenewstack.io/author/alextwilliams/)