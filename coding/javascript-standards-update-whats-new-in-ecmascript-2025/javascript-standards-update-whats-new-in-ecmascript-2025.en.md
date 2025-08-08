Now that the ECMAScript 2025 [annual update has been approved](https://ecma-international.org/publications-and-standards/standards/ecma-262/), we know exactly which features have made it into the official JavaScript language specification and which ones we’re still waiting for. It includes [some, but not all, of the features we were hoping for](https://thenewstack.io/javascript-due-for-new-time-date-and-set-features-next-year/), and some other new proposals that moved quickly through the approval stages.

Incidentally, the reason the annual update is known as ECMAScript isn’t just because the TC39 committee that works on it is part of Ecma International; it’s because [Oracle continues to hold the JavaScript trademark](https://thenewstack.io/oracle-wont-release-javascript-without-a-fight/). Oracle’s legal response to the [Deno claim](https://deno.com/blog/deno-v-oracle4) — that it should surrender it to the community as a generic term and abandoned trademark because it doesn’t have a relevant product — is due this month.

Meanwhile, the language itself continues to improve with the same momentum we’ve seen for the last decade, since the large ECMAScript 2015 release.

> “It’s another healthy sized release: not too big and not too small.”  
> **— Rob Palmer, TC39 co-chair**

“It’s another healthy-sized release: not too big and not too small,” TC39 co-chair [Rob Palmer](https://www.linkedin.com/in/robpalmer2) told The New Stack. “It’s got a lot of ergonomic features, and these are ones that we really expect to be widely used.”

They aren’t fundamental new capabilities so much as making life easier for web developers — “features that allow developers to express themselves succinctly, ” as Palmer put it.

## Classier Collections

JavaScript has had the concept of iterators for a long time, but they couldn’t do much beyond looping through everything in your collection of values. If developers wanted to transform or even just filter values, they’d have used a third-party library or copied the values into an array to work with, immediately increasing how much memory the code needs. With the [new Iterator helpers](https://github.com/tc39/proposal-iterator-helpers), that’s no longer necessary.

“Now you can stay in iterator land,” which [Ashley Claymore](https://www.linkedin.com/in/ashleycutmore/) (a Bloomberg software engineer who has worked on multiple TC39 proposals) suggested will be both more expressive and often more efficient, because “iterators try to do the least amount of work possible”.

If you want to filter your iterator to just the first three values, you can now do that right in the control loop (the new methods include map, filter, reduce, flatMap, some, find and every — which will be familiar from working with arrays — as well as new drop and take manipulations).

Filtering in the iterator requires much less work, Claymore explained. “If I take all the things and put them into an array, I’ve created a big array, and then I’m processing every single thing in that array, but then I’m only taking the first three. If I say to this iterator, I only want the first three things, as soon as we’ve got three of them, it will stop doing the work and stop asking for more values.”

> “This is the thing I love about JavaScript. We don’t sidestep those things. JavaScript really tries to say this is exactly what you’ll get.”  
> **— Ashley Claymore, Bloomberg software engineer**

This is only for synchronous iterators. Originally, the Iterator helpers proposal included another feature for working with iterators that contain promises; that was split off into [Sync iterators](https://github.com/tc39/proposal-async-iterator-helpers) (a Stage 2 proposal) “because as soon as you introduce async operations into this, the design space explodes”. Another Stage 2 iterator proposal, [Iterator Chunking](https://github.com/tc39/proposal-iterator-chunking), will let developers retrieve multiple values from an iterator to work on together (either chunks or sliding windows of data).

[As expected](https://thenewstack.io/javascript-due-for-new-time-date-and-set-features-next-year/), the new methods for [composing and comparing sets](https://github.com/tc39/proposal-set-methods) — which are common in languages that support sets and that JavaScript has lacked for a very long time — are now part of the language, filling a gap that was too small for a library and tricky for every developer to get right every time. Until now, all you could do was add values to the set or check if a value was in the set or not. “Everyone was writing these small snippets of code again and again,” Palmer noted.

Looking simple but being tricky was one reason the feature took a while to arrive, but as well defined as the outcomes of set methods were (they just need to work the way they do in mathematics and all the other languages), it was also important to get the order of execution right.

“In the abstract sense, a set doesn’t have an order, it’s just like a bag of things; you don’t know which one is the first thing and the last thing,” Claymore explained. “But in JavaScript, you can loop over a set using an iterator so there is an observable ordering, and if you go through everything and log it, you’ll see what was logged first and what was logged last.”

It was important not to have that be something that could give a different result in different implementations. “This is the thing I love about JavaScript,” Claymore added. “We don’t sidestep those things. JavaScript really tries to say this is exactly what you’ll get.”

For example, while it’s easy to say what the intersection of two sets should be, how efficient that is to calculate depends on how you treat sets of different sizes.

“You really want to only loop over the smaller of the two,” said Claymore. “If I have a set with just one item in it and a set with a million things in it, the intersection is only ever going to be zero or one things, so the most efficient thing to do is to base the ordering on the smaller set — but that means the ordering depends on which set was smaller. We had to discuss that: is that okay? Is it going to be surprising for developers, that sometimes you might get 123, and sometimes you might get 231, depending on which one was smaller?”

> Rather than consistency, the ‘dramatic’ performance difference won out.

Rather than consistency, the “dramatic” performance difference won out, but the same decisions about whether the ordering should be intuitive or efficient came up for almost all the methods; and digging through the details to make those decisions took time.

Plus, because much of the appeal of JavaScript is that it’s a dynamic language with a lot of flexibility, the committee needed to decide how strictly to define what counts as a set that you can use these methods with. As Claymore noted, “Is it OK to have the intersection of a set and an array or a set and a map, because they have very similar methods?”

In the end, that came down to three key properties that make a valid set.

“We must be able to know its size,” said Claymore. “You must be able to do .size on it, and that has to return a number we can turn into an integer, and then it must have two methods: has, so we can ask it immediately, do you have this thing? And then a keys method, which gives us an iterator, so we can loop through everything.”

That means you can use the new methods with a map, which has all three, but not an array or a string, because they don’t.

## Moving Ahead on Modules

Work on the [whole suite of proposals](https://thenewstack.io/5-ways-javascript-is-improving-modules-for-developers/) that will give JavaScript modules the full [features of CommonJS modules](https://thenewstack.io/how-javascript-is-finally-improving-the-module-experience/) continues. “I’m to say that at least some of the foundations of that have now landed,” Palmer said.

The [Import attributes](https://github.com/tc39/proposal-import-attributes/) syntax using with (not to be confused with the [deprecated with statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with) that changes scope in JavaScript) to import, say, JSON code and be confident that what you’re getting is JSON code deals with potential security issues.

“You might think you’re importing harmless data, regular JSON, but on the web, a file name is just a file name; it doesn’t guarantee what’s in there, and it might be delivering JavaScript,” Palmer explained.

The original proposal just checked whether the content could be loaded or not, but because you might be using this option for importing styles from CSS and that requires modifying headers (to add “Accept: text/css”), Import attributes can now change how content loads; Palmer suggested this will be particularly useful for build tools.

> “We’ve learned our lessons […] in particular about making sure that the JavaScript committee and other web groups are all talking earlier in the process.”  
> **— Palmer**

Because Chrome had shipped an early version of the feature using the original assert keyword and because Node embeds the V8 engine, the tooling ecosystem had picked that up. Unshipping that meant using telemetry to see how many websites would be affected — because while other browsers hadn’t added the feature, Chrome is big enough for its features to be adopted quickly. While migrating is easier when the adoption has happened in tools rather than website code, that’s still more work for tool authors.

“Like the Indiana Jones film, where he’s replacing the treasure with a bag of sand, we got away with it,” Palmer said, “but obviously, the tooling ecosystem went through the migration pains associated with needing to get people to move over. We’ve learned our lessons from this, in particular about making sure that the JavaScript committee and other web groups are all talking earlier in the process; Stage 2 is where we should be catching these things in future, because once we get to Stage 3 that’s when browsers are entitled to ship.”

People are already building on top of Import attributes. There’s the [JSON modules proposal](https://github.com/tc39/proposal-json-modules) with the specifics of how to import JSON and be sure that’s what you’re getting (that was originally part of Import attributes and reached Stage 4 at the same time). But there’s also a new proposal called [Import Bytes](https://github.com/tc39/proposal-import-bytes), for importing arbitrary bytes from any kind of file — like a photo or a web font that you want to [convert to SVG](https://github.com/vercel/satori) and that relies on it.

> “This is a case of runtimes already saying we want to use this feature…”  
> **— Claymore**

Import Bytes jumped straight from Stage 0 to Stage 2 when it was presented at the latest TC39 meeting, because it’s something multiple tools and runtimes have already started adding as a feature. It’s in Deno, Bun, webpack, esbuild, Parcel and Moddable — but they all use different syntax, so developers have to detect what platform their code is running on and pick the right one.

“This is a case of runtimes already saying we want to use this feature,” Claymore explained. “If we’re all going to do that, let’s put that in the spec and say what happens.”

That much interest means the feature might move through the other stages quickly as well.

## **Regularizing Regular Expressions**

[Duplicate Names Capture Groups](https://github.com/tc39/proposal-duplicate-named-capturing-groups), which lets you use the same name in two parts of a regular expression if only one of them can ever match (so you don’t need to come up with clever synonyms for “year” just because you want to match either 2025 or 25), [only just missed ECMAScript 2024](https://thenewstack.io/javascript-due-for-new-time-date-and-set-features-next-year/), so it easily made the cutoff this year. But it’s not the only improvement to regular expressions.

JavaScript has [long needed](https://simonwillison.net/2006/Jan/20/escape/) a way for matching and escaping characters in a string that have a specific meaning in a regular expression, like $ or “.”,; [Regex Escaping](https://github.com/tc39/proposal-regex-escaping) gives developers “the type of thing you would have imported a library for, or tried to write it yourself and probably got wrong,” Claymore said.

> “Sometimes you want one part of your regular expression to be case sensitive but not another part.”  
> **— Claymore**

JavaScript also gets the same syntax other languages and regular expression engines have for changing flags for case or multiline inside an expression, with [Pattern Modifiers](https://github.com/tc39/proposal-regexp-modifiers).

“Sometimes you want one part of your regular expression to be case sensitive but not another part,” explained Claymore. “In the past, case sensitive or not was a flag for the entire regular expression. Now you can say: I want the entire thing to be case insensitive apart from this section and I want this section to be case sensitive.”

## Neater Catching

Another proposal that’s been on the table for a while got a push over the finish line with the addition of [Promise.try](https://github.com/tc39/proposal-promise-try), for wrapping a function in a promise without needing to know in advance whether that function (which might be in a library) is asynchronous and returns a promise already, or just a value.

“When you’re invoking functions, we’ve got these different possibilities,” Palmer explained. “It’s very, very common that you want to get the outcome of a promise, rather than throwing an exception, because that’s almost a third way that things could go. A promise can be fulfilled in a positive way, [but] it can be rejected: it’s weird to have, then, a third control path where it could throw an exception.”

Promise.try means if the function is synchronous, it can safely run straight away. This saves time, but you don’t have to write extra code (or pull in a library from npm) to make that happen. It’s also easier for TypeScript to infer what’s happening in JavaScript with the new syntax.

“This being simpler, code works much better in TypeScript as well, so you can get another nice ergonomic win,” Claymore added.

One low-level feature that might not be as widely used — the other features in ECMAScript 2025 will be used in almost every codebase, he suggested — but will be very welcome to anyone working with [advanced graphics](https://github.com/w3c/ColorWeb-CG/blob/main/canvas_float.md), WebGPU and WebGL, or machine learning, is the new half-precision Float16 TypedArray. It doesn’t add a new number type to JavaScript, but it means you can choose to only store 16 bits instead of 64 and save some memory.

> “Developers can just express what they want to do, and it will be as fast as it can.”  
> **— Claymore**

“JavaScript already had 8-bit integers, 16-bit integers, 64-bit integers, 64-bit floats, 32-bit floats, but it didn’t have 16-bit floats,” said Claymore, “and in the past few years the value of 16-bit floats has really proven itself. In machine learning, if you can have twice the number of numbers, even if those numbers have half the precision, that’s a really good thing. Machine learning models perform better having more weights, even if those weights themselves have less information.”

More CPUs have hardware support for the 16-bit floats that more APIs want to use and WebGPU can work with them, but there wasn’t a good way to interact with those APIs from JavaScript. “If you try to implement it yourself, you have to do things really inefficiently to get and manipulate the bits,” said Claymore.

Plus, your own code wouldn’t automatically take advantage of new CPUs that add support, so it would stay slow even on new hardware.

“Now you have a Float16 array, so you can natively get your 16-bit floats down to 16 bits,” Claymore said. “Developers can just express what they want to do, and it will be as fast as it can.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

After completing an MSc in Intelligent Knowledge Based Systems in 1990, Mary Branscombe was convinced that promising as the AI techniques she’d been studying were, they weren’t even close to being ready. Since then, she’s been a technology journalist for...

Read more from Mary Branscombe](https://thenewstack.io/author/marybranscombe/)