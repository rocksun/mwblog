Solid plans to introduce a new primitive to its reactive architecture, according to a talk by SolidJS creator [Ryan Carniato](https://github.com/ryansolid) at JSNation last week.

There are two reasons why this matters: First, Carnatio, a leader in the framework space, is demonstrating what he sees as the future for all JavaScript frameworks in terms of expanding their capabilities; and second, as Solid goes, others sometimes follow, as we saw with [Signals adoption](https://thenewstack.io/javascript-in-2023-signals-reacts-rsc-and-full-stack-js/) in [Angular](https://thenewstack.io/angular-v21-adds-signal-forms-new-mcp-server/) and [Preact](https://thenewstack.io/why-devs-are-ditching-react-for-preacts-simplicity-and-speed/).

Carniato explained signals as “like a spreadsheet,” where a normal assignment represents a moment in time.

“It means that on completion, variable A reflects the current sum, but if either B or C changes, you have to do the assignment again.” he said.

Signals are just a set of primitives to help represent the synchronization, he added. Signals had been around for the better part of a decade when he open-sourced Solid.js back in 2018, but Signals had fallen out of favor thanks to the React Component Model, he said.

“It’s hard to ignore the impact when pretty much every framework other than React has adopted Signals first-class at this point. So great, right? End of story,” he said. “No, I think this: We’re just at the beginning of a much bigger change, and I’m not alone in this thinking.”

He’s not talking about artificial intelligence, either, but rather the low-level architecture problem of getting the most out of your applications.

“Just having Signals aren’t enough. Signals are a mechanism for change, but how you use them makes all the difference,” he said.

The common thread in what makes Signals powerful is the knowledge of the data graph that powers your application, he said. It enables developers to do “incredible things that we wouldn’t easily be able to do otherwise,” he added.

He explored what Signals empowers in the talk, introducing code examples that reference upcoming features of Solid that may not even been available at this time. That included a new primitive proposal for the framework.

## Signals Does Not Equal Faster Performance

Carniato began with a look at performance, because it’s the easiest to talk about and “arguably the least important,” he said.

“This starts with debunking a common misconception: I’m using Signals so my App framework must be faster,” he said. “Unfortunately, it doesn’t work that way as [Joe Savona](https://conf.react.dev/speaker/90f2d599-df38-40b7-9878-ff82d16ce353) from the React team found out — if you watched his talk from React Conf 2025, where he showed that adding any state management actually lowers the performance ceiling of your framework.”

Carniato added that while the React compiler might allow developers to write more optimal code, it doesn’t have a meaningful impact on the absolute performance.

Adding [MobX](https://mobx.js.org/README.html), [Zustand](https://zustand.docs.pmnd.rs/) or [Signals to React](https://thenewstack.io/did-signals-just-land-in-react/) or even Signals to Preact isn’t guaranteed to improve the performance in all cases, he explained. In fact, on average, it makes them slower. That’s because frameworks are built around the Virtual DOM (VDOM) and every time state updates, the framework has to rerun component functions and diff the VDOM tree, which compares the old virtual tree to the new virtual tree to find changes.

The answer to Signals and better performance is found in fine-grained rendering, he said. To that end, SolidJS eliminates the VDOM and uses the reactive graph to only update the exact, fine-grained DOM nodes that depend on changed data. Solid as well as Svelte and Vue have joined Solid in having a fine-grained rendering tree.

“Picture some application where you need to pull state up high so it’s available at multiple points, like a shopping cart in the header and maybe a buy button deep in your page,” he said. “You update the state, you trigger re-renders down the tree, only the shopping cart really needs to update, but we do all of this extra work.”

> “This starts with debunking a common misconception: I’m using Signals so my App framework must be faster.”  
> **– Ryan Carniato, creator of SolidJS**

Typically, developers are told to memoize, which is caching the result of a function call and returning the cached result when the same inputs occur again, instead of recalculating the result.

SolidJS, Vue and Svelte use reactive primitives such as Signals that are fundamentally memoized. But memoization creates a trade-off between speed and memory.

“You can realize that the data you send down to the buy button isn’t changing, and only run the one path. Generally, this is what the React compiler does. It’s what Svelte 3 did,” he said. “If the cart has changed, there’s no avoiding this: re-running all the components, from the owner of the state down to that change. We can prune branches that didn’t change along the way, but the change has to reach its place in the UI.”

The point in which you use Signals enters the tree and becomes a new route, he said.

“However, with fine-grain rendering, all props just work that way,” he said. “By default you can declare this data in the top your app bottom, pass it through 10 components to the exact same results. It doesn’t need to rerun the whole component or any of its parents, just the parts change.”

That leads to the whole category of “will my component rerun” going away and performance composition becomes a non-issue, he said.

Svelte and Vue have joined Solid on the fine-grained rendering train, he said.

## New Primitive for Solid

Stores are proxies where each property has the potential of being its own Signal. Working with Stores led to Carniato realizing there are problems that require driving granular data and places where you start from a single source but want to fork or split reactivity.

“It’s a waste to check every row when you’re changing the selected class on a table, but it isn’t always practical to include an ‘is selected’ on every row, especially when that data is shared in multiple places,” he said. “Sometimes we just need to project reactive data onto other data without mutating the source. Sometimes, we need to be able to create ephemeral extensions of that data like merge and optimistic changes without committing them.”

He explained two advanced concepts in SolidJS’s reactivity model, both aimed at eliminating the need for complex side effects (like useEffect in React) to manage state synchronization.

The first is **Projections**, which would be a new [primitive](https://primitives.solidjs.community/) for [Solid](https://github.com/solidjs/solid). It’s still in the works. Projections explain and split reactivity back into multiple different sources, Carniato explained. They’re like a specialized filter or lens you place over the main data. They are granular, derived and non-mutating. They also let developers create ephemeral changes like an Optimistic UI update (showing the users their change immediately before the server actually confirms it) without changing the core application data, he explained.

“While you may not use them very often, they represent a space that we’ve never really had a good solution before in front of frameworks — a primitive that is both granular and derived,” he said.

The second is **Async Signals**, which are already part of SolidJs implemented with createResource. Async signals are a solution for integrating slow data directly into the fast, synchronous UI flow based on reads.

> “While you may not use them very often, they represent a space that we’ve never really had a good solution before in front of frameworks — a primitive that is both granular and derived.”  
> **– Carniato**

Traditional models are write-centric, meaning you have to manually tell the framework to update after the slow data arrives, often leading to complex logic inside useEffect or lifecycle methods. But Solid’s approach is read-centric, so it should only pause when it doesn’t have the data to render (a “read” problem).

”What might be interesting to you is because we’re fine-grained and because we can push the reactivity to where the Read is,” he said. “Basically, children become siblings automatically in this model.”

He then demoed how fast the fine-grained reactivity approach loads: It took the whole page two seconds to load because they all run in parallel, he noted.

He also discussed how this can be used to create “self-healing Reactivity” wherein the reactive graph knows all dependencies, allowing the framework to automatically trace errors back to the async source and retry the fetch when a “Reset” button is clicked—without re-running the component functions.

While fine-grained reactivity guarantees speed, the application still faces a consistency problem known as tearing when dealing with non-urgent, asynchronous updates. Carniato noted that SolidJS actually tears by default after initial load — for instance, a counter number might update instantly, but the accompanying slow-fetched phrase briefly shows the old data.

To solve this, SolidJS uses [**Transitions**](https://www.solidjs.com/tutorial/async_transitions), which allows the developer to mark an update as non-urgent. This primitive is essential for enabling the smooth, concurrent rendering of asynchronous data. Transitions also “can tie together mutation and async fetching to remove weird race conditions around your data and pending states,” Carniato explained. Transitions can be used to ensure an app doesn’t suffer from visual “tearing” during slow data changes.

He noted that Solid has had these features since around 2020, giving it experience with the primitive. Transitions are a key mechanism for building a fully functional Optimistic UI.

But the best is still to come as frameworks lean into fine-grained reactivity.

“I think we’re at just the precipice of the next big thing,” Carniato told audiences.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)