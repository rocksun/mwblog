# 5 Ways JavaScript Is Improving Modules for Developers
![Featued image for: 5 Ways JavaScript Is Improving Modules for Developers](https://cdn.thenewstack.io/media/2024/06/1e95e702-slashio-photography-dzu4mrqlpao-unsplash-1024x768.jpg)
With modern JavaScript applications typically using thousands of modules, improving the performance of modules and making them easier for developers to work with would be a big step forward. That’s the motivation for the [interconnected set of JavaScript proposals known as module harmony](https://thenewstack.io/how-javascript-is-finally-improving-the-module-experience/). These introduce new features in the [JavaScript language](https://thenewstack.io/javascript/) for working with native ECMAScript modules and give them some of the power that was lost with the switch away from CommonJS modules.

“ECMAScript modules are not as powerful and easy to use as the previous system,” [Nicolò Ribaudo](https://www.linkedin.com/in/nicol%C3%B2-ribaudo-bb94b4187/), an Igalia engineer and maintainer of the popular Babel transpiler, told us.

The module harmony proposals aim to make it easier for advanced developers to get the most from modules, so that their tools work better for mainstream developers.

While having these options built into JavaScript will be new, they’re not new ideas; many of them are already being used by the developers who build tools like bundlers or complex JavaScript platforms like the system Bloomberg creates to run its terminals: they either use CommonJS internally or write their own implementations of similar features.

The module harmony proposals aim to improve the performance of modules and make it easier for those advanced developers to get the most from modules, so that their tools work better for the mainstream developers who use them.

But as always, adding new features to JavaScript takes time, because the [standards process](https://thenewstack.io/beyond-browsers-the-longterm-future-of-javascript-standards/) relies on consensus. [JavaScript features](https://thenewstack.io/the-new-javascript-features-coming-in-ecmascript-2023/) have to be supported in multiple browsers, engines, runtimes and tools before they’re considered mature enough to become permanent features of the language. The default is to say no to proposals until everyone involved is convinced they’re worth spending the time to implement, especially if that means changing code that already works.

“Architecture is about finding the right layer and separation of concerns and coupling and all of those things come together in module harmony,” explained [Kris Kowal](https://www.linkedin.com/in/kkowal/), the original creator of CommonJS.

## 1. Combining Module Files With Web Workers
We’ve already looked at some of the [key module harmony proposals](https://thenewstack.io/how-javascript-is-finally-improving-the-module-experience/), including the ones that rely on the different stages of the pipeline for loading modules. Two of the other most promising proposals aim to simplify the file structure for how developers work with modules, starting with combining them with web workers.

Making developers put workers into a separate file turns out to be one of the [biggest blockers](https://github.com/tc39/proposal-js-module-blocks/issues/21) to adoption because you have to deal with resolving the network route to the module and passing that to the worker — which is dynamic and tricky for bundlers to deal with. Also, handling multiple files adds complexity.

With Module Expressions, you will be able to have multiple modules that are inline in the same file.

“Sometimes your worker will be just a couple of lines of code, that maybe imports some other module and then the module. And it might be very logically related to the code that’s going to run, so splitting it into separate files is not always ideal,” Ribaudo told us.

Various libraries allow developers to write workers inline in their other code, but that causes problems with content security policies. With [Module Expressions](https://github.com/tc39/proposal-module-expressions), you will be able to have multiple modules that are inline in the same file. This is particularly useful for multi-threaded code, where developers want to send a module to a worker to be executed later — maybe more than once.

“When you have to do some expensive computation like in a big application, it’s beneficial to move that to a worker, so your main thread that manages the UI can keep doing its thing, and in the background the worker is computing away,” explained Ribaudo. “This gives you some syntax to declare a module inline inside another module and pass it around without forcing you to create a separate file. It’s then easy for a bundler to figure out how to properly split things and you’re sure the bundler can find all your files without you explicitly having to configure it.”

“Being able to be able to write multiworker programs is how we’re going to be able to write high-performance systems in this multicore core world where the clock speed of the CPU is not going up anymore,” noted Kowal.

## 2. Module Declarations
[Module Declarations](https://github.com/tc39/proposal-module-declarations), on the other hand, lets you bundle multiple modules into a single JavaScript file and have them execute against each other without needing to do any other configuration. Even with HTTP2, when you’re loading a lot of small files, performance suffers — and lots of small files can’t be compressed as effectively as one big file, which is one reason developers use bundlers in the first place.
“Real programs use so many modules and you have a cascading dependency problem when you want to prefetch everything,” [Daniel Ehrenberg](https://www.linkedin.com/in/danielehrenberg/), Ecma vice president and Bloomberg software engineer working on several of the proposals, explained.

Module Declarations aren’t intended to replace bundlers, but they will simplify the task of writing them.

Module Declarations aren’t intended to replace bundlers, but they will simplify the task of writing them, removing some of the tedious work and freeing tool developers up to work on more interesting features; it may allow them to finally migrate off CJS internally.

“Bundlers can output code in a single file using the module semantics that are implemented by browsers: they don’t have to reimplement how ESM works,” Ribaudo suggested.

Ehrenberg agreed. “It still makes sense to do the optimizations that bundlers do, which may cross multiple boundaries, so we’re not imagining that bundlers will become trivial, but at least it would be nice if they didn’t have to do their own interpretation of semantics themselves,” he said.

Module Declarations only cover JavaScript modules. Some resource bundles need to include more than JavaScript modules. The Web Incubator Community Group [bundle preloading proposal ](https://github.com/WICG/bundle-preloading)addresses that, but JavaScript modules tend to be where web apps are loading so many small files that it affects performance.

## 3. Import Attributes
Both of these proposals are at stage 2, which means that they’re still drafts that might change as the open issues are worked through with experimental implementations. But another of the earliest module harmony proposals is close to being available.

[Import Attributes](https://github.com/tc39/proposal-import-attributes) creates a syntax that lets module import statements pass along more information about modules — for example, to tell a bundler how to interpret or process a file you’re importing. Rather than relying on the file type, you can specify if an image should be loaded as a bitmap, if you want to load a file as plain text or even tell the bundler to bundle a file and return a URL pointing to it.
“This will let developers set some property about the module they’re importing,” Ribaudo told us. The initial motivation was to support [importing JSON files as they were modules](https://github.com/tc39/proposal-json-modules) while providing security guarantees. “Maybe you think you’re importing a JSON module,” he continued, “so you think you’re safe, but actually you’re importing a JavaScript module from a CDN that has been compromised.”

Use import attributes to specify that you’re expecting a JSON module and the browser will refuse to load it if it turns out to be something else.

“Import attributes will be a massive boon for bundlers, to know how to bundle your program together in an efficient way.”

– Justin Ridgewell, Vercel
“Import attributes will be a massive boon for bundlers, to know how to bundle your program together in an efficient way, giving the user control and how to control that bundling,” added Vercel’s TC39 delegate [Justin Ridgewell](https://github.com/jridgewell) (who works on the [Turbopack ](https://turbo.build/pack)bundler).

Import Attributes is already implemented in TypeScript, bundlers like Webpack, and both Safari and Chromium-based browsers. But there have been some substantial changes to the syntax since the first implementations were created (with the proposal having already gone back from stage 3 to stage 2 to be worked on more, and then reaching stage 3 again).

“After implementing it, we noticed that just asserting properties about the model was not exactly what the web needed: we needed to be able to slightly affect how the module is imported, for example, to pass the current HTTP headers,” Ribaudo explained.

The initial syntax was useful enough to quickly become popular with developers, but browser and tool developers are already working on adopting the new syntax and he suggested “this will be generally available relatively soon”.

## 4. Granular Security With Compartments
Compartments have a much broader scope than the other proposals — from compatibility to blocking software supply chain attacks — and because of that are at a much earlier stage. Stage 1 means that the TC39 committee has agreed that there’s a problem to be solved, but not that a proposal is necessarily the right way to solve it.

Compartments offer virtual environments for modules to run in, but the proposal also provides features that make other module harmony proposals work better. For instance, Module Phase Imports makes it clearer how modules loaded by workers fit into the module graph and lets you have a trusted main thread that can load and audit modules and pass them to a worker thread for execution, while compartments lock down those capabilities by offering granular isolation.

“The idea is to bring the security boundary down to the object level.”

– Kris Kowal, creator of CommonJS
Kowal called this object capability programming: “making it possible to get security boundaries into JavaScript that are finer granularity than an origin, finer granularity even than a worker. The idea is to bring the security boundary down to the object level, so a programmer can reason by construction about what permissions are inherent to giving a powerful object to a third party.”

“You can explicitly endow capabilities and implicitly deny all powerful IO capabilities unless the host explicitly grants them. For that to work you have to be able to execute modules and you need to be able to virtualize the module loader, so [that] the host can control what sources are available to the guest.”

There’s an obvious security angle here, Kowal said, for avoiding [software supply chain attacks](https://thenewstack.io/securing-the-software-supply-chain-with-a-software-bill-of-materials/).

“It’s been a rapidly deteriorating fiction that a webpage consists exclusively of a single party’s interests. Having object-capability programming as an option available to developers makes it possible for them to isolate their third-party dependencies and limit the damage they can do, if they manage to escalate their privileges by getting an object they’re not supposed to have.”

Embedded system developers using JavaScript see compartments and virtualized modules as a way to protect devices. A programmable light bulb might use compartments to have a powerful API for controlling the LEDs, but limit who has access to some features using what’s called attenuation, Kowal explained.

“They can use compartments to take the native light bulb control API and create an attenuation of that for the user program, so they can’t strobe it so quickly that it would cause an epileptic fit or run so much power through the bulb that it burns out.”

## 5. Making Life Easier for Dev Tools Like Jest
Providing a virtualized environment for modules is also the kind of advanced use case writers of developer tools like Jest and Playwright need: Jest is built on the virtualization system in Node.js, which is similar to what Compartments will offer, Fastly engineer [Guy Bedford](https://www.linkedin.com/in/guybedford/) (involved in many of the module harmony proposals) explained.

“We are building up those primitives in standards so that we can have first class support for these features in the native ES module system.”

– Guy Bedford, Fastly
“Say you want to be able to mock an import, you want to change the execution behaviors slightly: Jest controls all of that and injects a lot of instrumentation and behaviors through these virtualization primitives. We are building up those primitives in standards so that we can have first-class support for these features in the native ES module system, because right now there are implementation complexities without having first-class native support for this kind of functionality.”

Observability providers also find it hard to hook into the ES module system to provide instrumentation today: with compartments, “you can wrap exported functions and hook them and see when they’re called, you can wrap the imports either to log or to mock them out and replace them with alternatives and do that in a way that will work across multiple runtimes.”

That’s useful for plugins as well, Ribaudo suggested, where you can run multiple options in parallel in the same code without them interfering with each other. And it may help with code reuse generally. “Most developers don’t think about virtualizing other JavaScript environments, but this means you will be able, for example, in a browser to emulate how Node works, to implement the Node.js module resolution semantics, to provide the Node.js globals in a virtual machine that keeps them separate from the rest of your code.”

Of course, the module harmony proposals we looked at previously that rely on compartments bring their own benefits, like improved performance by making it easier to use workers and allow modules to be passed around, Kowal noted. “You could parse a module once and then share an immutable object between threads, or have a dedicated module loader worker that’s able to hand off work to other threads,” he said.

## Coordinating a Flock of Proposals
Most JavaScript developers won’t use the new module functionality directly, but the ecosystem of tools they rely on will. Progress here may not be particularly visible, and even the Stage 3 proposals will take some time to become part of JavaScript, as the community works through the details and how the changes will affect parts of the JavaScript ecosystem (like TypeScript).

“This set of module harmony proposals has been three and four years in the making and I think it will continue for several more years, because there are implementer concerns, there are API concerns,” cautioned Ridgewell. “I’m trying to solve my bundler use cases: there are a bunch of things that are affected by this set of proposals.”

This is the way the deliberately conservative JavaScript standards process works, to deliver features mature enough to rely on when they become part of the language.

This is the way the deliberately conservative JavaScript standards process works, to deliver features mature enough to rely on when they become part of the language. The slow pace gives everyone — from tool developers to the teams building server-side JavaScript runtimes — a chance to give feedback about the advanced use cases they need.

“Consensus as a process does need a lot of people to feel pretty confident in those foundations: that’s quite slow but it’s worth it being slow,” Bedford pointed out.

Working through the process may involve restructuring the different proposals along the way. That’s already happened with Module Declarations and Module Expressions, which started out as very different proposals, but evolved so that Module Declarations is now built on top of Module Expression.

Several proposals have been renamed as they progressed, to better explain what they offer. [Deferred imports](https://github.com/tc39/proposal-defer-import-eval) got a new name and was slimmed down to initially cover just being able to delay evaluating a module till you actually need to use it. More sophisticated options that were dropped might make a comeback, but while that’s discussed, they’re not slowing down the attempt to [advance the proposal to a new stage](https://docs.google.com/presentation/d/1EjV6QbT4bvcOdWj-gCLwP5fcEWRfewzbrI3vOI11LA8/edit#slide=id.p) this month.

Also, the [Asset References](https://github.com/tc39/proposal-asset-references) proposal we looked at last time kicked off a lot of the thinking about module harmony, but has largely been superseded by other approaches, like Module Declarations.

## Huge Progress Is Being Made
The TC39 committee that standardizes JavaScript hasn’t had a lot of experience with coordinated proposals that interrelate to deliver (mostly) independent pieces of a larger goal the way the module harmony suite does, but the experts championing the set of proposals have put in a lot of work to find the right way to split the features up logically and keep this many projects progressing.

A single, giant proposal with all these features would be harder to understand and having to implement all of it at once might put off browser makers. “It’s easier to chip off these problems piecemeal than trying to be too ambitious all at once and that’s why the overall effort works,” Bedford suggested.

“Each proposal is self-motivated, and each proposal still makes sense, even if the proposals don’t all get approved,” Ribaudo agreed.

There’s a lot of collaboration between the different projects to keep everything in sync, like making sure the new module class (an object for presenting a module that doesn’t currently exist in the JavaScript language) that all the proposals rely on stays consistent as they develop.

“There’s a huge amount of progress being made, even if it’s difficult to see at times.”

– Nicolò Ribaudo, Igalia engineer
Over the last two years, there’s been a presentation at almost every TC39 meeting about one or more module proposals, so “all delegates are now aware of the whole space of the features,” which has resulted in multiple proposals advancing quite quickly through the different stages of standardization.

“If you look at an individual proposal, it may feel like it’s moving very slowly, but if you look at the whole module space, there is always something that’s being worked on and always something that’s moving forward,” Ribaudo pointed out.

Bedford highlighted that overall momentum is on track to deliver important changes that developers will benefit from, without having to rewrite their own code.

“There’s a huge amount of progress being made, even if it’s difficult to see at times,” said Ribaudo.

“Every spec that we work on here is an improvement,” he explained. “These will be tuning changes and platform level changes that are mostly additions as opposed to major breaking changes.”

“We are aiming to solve virtualization, worker transferability and lazy loading, and whether or not we get to every piece, these will be improvements without cost to the code that most users are writing.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)