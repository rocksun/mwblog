At some point, we stopped writing React components and started worshiping them. The mantra of “reusability” turned from a best practice into a full-blown theology.

Every team has that one engineer preaching the gospel of The Ultimate Component — the one that can handle every layout, color scheme and edge case with a dozen optional props and 500 lines of conditionals.

What began as a noble goal of cleaner architecture has metastasized into a codebase where every file imports every other file, and no one dares touch the base component for fear of breaking the entire app. This isn’t code reuse; it’s dependency debt dressed up as virtue.

## The Cult of Component Reuse

Developers love elegance. We crave patterns that make us feel like we’ve transcended the chaos of ad-hoc coding. DRY (Don’t Repeat Yourself) became one of those sacred principles — a simple idea mutated into dogma. Instead of avoiding unnecessary duplication, many teams started avoiding any duplication, no matter the cost. The result? Abstract monstrosities that do a thousand things poorly instead of three things well.

> The obsession with reusability often leads to “prop soup.”

The obsession with reusability often leads to “[prop soup](https://www.geeksforgeeks.org/software-engineering/dont-repeat-yourselfdry-in-software-development/)”: components overloaded with props to handle every possible variation. You’ll see Button components that accept 20 options just to slightly tweak padding or icon alignment. Instead of simplifying development, these components introduce complexity at scale. Debugging becomes archaeology, with developers sifting through layers of abstraction trying to figure out why a button looks wrong in one context but fine in another.

The irony is that this fetishization of reuse actually reduces reuse in practice. When a component becomes so generic and overloaded that no one wants to touch it, developers just clone it anyway.

## When the DRY Principle Leads to Complexity

The DRY principle is beautiful in theory, but brittle in practice. Code duplication isn’t always evil; sometimes it’s just pragmatic. Over-abstracting can strip code of context, making it harder to reason about. A few extra lines of repetition [are often cheaper](https://thenewstack.io/why-quality-code-matters-and-how-to-achieve-it/) than a month spent deciphering a maze of reusable logic. Don’t be slaves to metrics, people. Make them work for you.

Imagine two forms in your app: a login form and a registration form. They share some inputs, but have different validation logic and submission flows. The DRY zealot merges them into a single mega-component with a dozen conditional branches. Now, every small change risks breaking both flows. The original two simple components have merged into a hydra of if-statements.

> The key isn’t to repeat yourself endlessly, but to know when reuse stops being efficient and starts being entanglement.

Good engineering is about balance. DRY should coexist with another, lesser-known principle: WET — Write Everything Twice. Duplication, when done intentionally, preserves clarity. It allows code to evolve independently.

The key isn’t to repeat yourself endlessly, but to know when reuse stops being efficient and starts being entanglement. React’s component model is flexible enough to tolerate some duplication. The problem is that developers treat duplication as sin instead of strategy.

## The Over-Engineered Button: A Case Study

Let’s talk about [Button.jsx](https://reactnative.dev/docs/button), the unofficial mascot of over-engineering. It’s always there, lurking in every React project. It starts simple: a reusable button with a color and a label. Then someone needs an icon. Someone else needs a loading state.

Then it must support links, disabled states, nested components, theming and custom click handlers. Before long, Button.jsx has a dozen props, conditional rendering galore and a propType list longer than the component itself.

> Every new developer is warned: “Don’t touch Button.jsx.” Yet everyone does.

Every new developer is warned: “Don’t touch Button.jsx.” Yet everyone does, because every new feature requires one more tweak. Eventually, the abstraction collapses under its own flexibility. Testing becomes painful because you’re effectively testing 10 different components jammed into one file. Documentation lags behind, and what started as a noble attempt at reuse now throttles productivity.

At that point, teams start breaking off splinters — creating SlightlyDifferentButton.jsx or IconButton.jsx. Ironically, the antidote to over-reuse is duplication. The codebase returns to a state that’s actually more maintainable because each button now does one thing well. The moral: [Reusing should serve clarity](https://react.dev/learn/reusing-logic-with-custom-hooks), not the other way around.

## The Dangers of Premature Abstraction

The myth of reuse stems from a misunderstanding of what makes code maintainable. It’s not how few lines you’ve written and [whether you’ve reduced cloud costs](https://cast.ai/cloud-cost-monitoring/), but how few mental hops it takes to understand what’s happening. Every abstraction adds a layer of indirection, and each layer costs cognitive effort. The problem isn’t that we abstract; it’s that we abstract prematurely — before we truly understand the problem domain.

> Every abstraction adds a layer of indirection, and each layer costs cognitive effort.

Developers often generalize too early because it feels efficient. “We’ll probably need this in another module,” someone says, and suddenly a single-purpose hook becomes a utility with five parameters and two context providers. But abstraction without proven reuse isn’t foresight; it’s speculation. And speculative abstractions are some of the hardest code to delete because they might still be useful someday.

Great abstractions emerge naturally. They’re born from patterns repeated across real-world use cases. When you abstract and [use escape hatches properly](https://thenewstack.io/how-escape-hatches-make-abstraction-more-powerful/), after seeing three or four examples of the same problem, your solution carries wisdom instead of assumptions. Premature abstraction, on the other hand, creates a scaffolding that traps your code into patterns that no longer make sense months later.

## Adopting a Post-Reuse Mindset for React Architecture

We need a cultural reset around what “good” React architecture looks like. The industry’s obsession with DRY, generic components and high-level abstractions has led to brittle systems that look elegant but break easily. True maintainability isn’t about how many lines you can share, it’s about how easy it is to reason about each piece in isolation.

Believe it or not, [embracing duplication](https://medium.com/@gmiejski/code-duplication-is-fine-kiss-the-dry-in-its-b-2880f8b9eaa5) doesn’t mean reverting to chaos. It means respecting boundaries, keeping code closer to its context and accepting that local optimization is often better than global purity. In practice, this might mean having three different form components that look 80% similar but are easy to modify independently. It might mean deleting a “utility” function used only twice. It might even mean deleting your universal Button.jsx and starting over.

> Somewhere along the way, we replaced simplicity with abstraction worship.

React was built on the idea of small, composable parts. Somewhere along the way, we replaced that simplicity with abstraction worship. It’s time to rediscover the joy of simple, readable, context-aware code. The best component isn’t the one you can use everywhere — it’s the one you can understand instantly.

## Simple, Self-Contained Components

The React ecosystem doesn’t need [more reusable components](https://stackoverflow.com/questions/49580983/where-should-i-store-my-react-reusable-components) and techniques to store them. It needs more intentional ones. The pursuit of reuse for its own sake has created a generation of codebases that are theoretically elegant but practically fragile. Every abstraction carries a cost, and the bill always comes due.

Reuse is a tool, not a religion. The next time you’re tempted to refactor three similar components into one “smart” abstraction, ask yourself: Who is this serving, the code or your ego? Because in the end, clarity outlives cleverness.

The healthiest systems aren’t pyramids built on layers of abstraction; they’re gardens of simple, self-contained components that grow independently without choking each other out. Maybe it’s time to stop climbing the pyramid — and start pruning the garden instead.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/01/c616d407-alex-williams-2.png)

Alexander Williams is a full stack developer and technical writer with a background working as an independent IT consultant and helping new business owners set up their websites.

Read more from Alexander T. Williams](https://thenewstack.io/author/alextwilliams/)