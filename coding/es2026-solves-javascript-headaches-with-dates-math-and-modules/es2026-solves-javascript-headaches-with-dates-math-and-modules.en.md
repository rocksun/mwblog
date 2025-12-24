It could be a bumper year for new features in the JavaScript language in [2026](https://tc39.es/ecma262/), with some very large proposals finally maturing and the usual mix of technical improvements and new options to make life easier for developers.

The final list of what’s making it into the language will include all of the ECMAScript projects that reach the [Stage 4 milestone](https://tc39.es/process-document/) by March 2026.

There are already several projects that have made it fully to Stage 4, and another two that are almost there and just awaiting a final signoff (which means they’re already available in some browsers, JavaScript runtimes, or tools). There are also some very promising proposals that are at Stage 3, with so much momentum, it looks very likely they will be approved in time.

## What’s Already Approved for ECMAScript 2026?

Doing anything beyond simple math in JavaScript is notoriously complex. The Math object doesn’t currently have a method for something as common as summing numbers (rather than just adding numbers two at a time). If you write a loop to do that for numbers that can’t be represented precisely in the 64-bit floats that JavaScript uses for numbers, then [the answers may not be exactly what you expect](https://github.com/tc39/proposal-math-sum) because of the floating-point precision of the intermediate results.

[Math.sumPrecise](https://github.com/tc39/proposal-math-sum) gives you more precise results for floating point numbers using a better (but slower) algorithm. Although it doesn’t fix the oddity where JavaScript can’t add 0.1 and 0.2 correctly, that’s because the floating point representations for those aren’t exactly 0.1 and 0.2. The new algorithm “makes some things a lot easier to accomplish than writing your own function,” says Igalia web standards advocate [Eric Meyer](https://www.linkedin.com/in/meyerweb/).

> “As someone who uses base64 stuff from time to time, and might like to move it into and get it out of other value formats, I look forward to playing with this [Math.sumPrecise].”  
> **– Eric Meyer, Igalia web standards advocate**

Similarly, JavaScript currently has arrays for working with binary data, Uint8Array, but no built-in way to encode binary data as [base64](https://github.com/tc39/proposal-arraybuffer-base64/blob/main/base64.md) (say for handling SSH keys or embedding small images on a page), or to make an array from base64 data (or from hex strings). The [Uint8Array to base64 proposal](https://github.com/tc39/proposal-arraybuffer-base64) adds methods to do both.

“As someone who uses base64 stuff from time to time, and might like to move it into and get it out of other value formats, I look forward to playing with this,” said Meyer.

JavaScript does already have a method for converting JSON into a data object you can work with, [JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse), but if you’re working with numbers and dates the conversion is lossy — because JSON has arbitrary precision and JavaScript doesn’t.

If you parse a quintillion (1 followed by 18 zeroes), you get 1000000000000000000 – but you get the same result if you parse 999999999999999999 (one less than a quintillion). Parse a date and time and JavaScript will add an empty number of seconds to the format. JavaScript won’t even let you convert a BigInt to JSON, because you wouldn’t get the same number when you parse it back out of JSON.

The [JSON.parse Source Text](https://github.com/tc39/proposal-json-parse-with-source) proposal lets you retrieve the raw JSON source and convert that as precisely as you want — either into a BigInt, or you can look at what characters were escaped so that you can compose a string exactly the way you want it. This was first suggested back in 2018, and there was a lot of discussion about adding extra functionality, like being able to serialise JavaScript objects into JSON (the reverse of parsing), the same way; that’s not in the proposal that made it to Stage 4, though.

Another proposal that’s been around for a while (since 2015) is [Error.isError](https://github.com/tc39/proposal-is-error). It’s used to check whether a JavaScript value is actually an error object, since you can use throw with just about anything in JavaScript, including numbers. It’s more reliable than using instanceof Error because it works across different execution contexts, like browser extensions and iframes, and isn’t fooled by objects that just look like errors. That’s useful for debugging and is extremely useful for writing polyfills and libraries; plus it’s already broadly available in browsers.

Many other languages already have a built-in way to chain a sequence of iterators together, so that you can call them one after another and get the values from them all at once and in the correct order; currently, you have to do that with generators in JavaScript. The new [Iterator Sequencing](https://github.com/tc39/proposal-iterator-sequencing) proposal makes that simpler with a new Iterator.concat function; it’s already available in Firefox and Safari.

## Improving Internationalization and Localization

What’s the first day of the week? In some places it’s Sunday instead of Monday. In some countries the weekend is Friday and Sunday (and Saturday is a working day), or Thursday and Friday. In other countries, it’s just one day — but that day is Friday, Saturday or Sunday in different locations. If you’re writing a calendar app, you need to know that (and to know which countries have recently changed which days are the official weekend). [Intl Locale](https://github.com/tc39/proposal-intl-locale-info/blob/main/README.md) takes all that information, as well as other details like whether the language for that location needs to be rendered right to left or left to right from the [Unicode locale data](https://unicode.org/reports/tr35/tr35-dates.html#Calendar_Preference_Data), so developers don’t need to work it out themselves.

> ECMAScript 2026 will also include a variants API for Intl.Locale.

It’s not a specific proposal, but ECMAScript 2026 will also include a variants API for Intl.Locale that lets developers use Unicode locale details like the region, the language, the script and numerals used in a specific place — which might have their own styles for date and time, without having an ISO code for the exact combination.

So “ca-Latn-ES-fonipa-valencia-u-nu-roman” represents the Catalan language with the Latin script as spoken in Spain, with the Valencian variant captured with phonetic IPA and using the Roman numerals numbering system (the order of the subtags is always alphabetical). That’s a lot of detail — and exactly what you need to make a web page work exactly the way it should anywhere in the world.

## Finalizing Asynchronous Code and Resource Management

One of the most commonly used Array methods is Array.from, for when you want a copy of a map, set or something that looks like an array; but it only works for synchronous iterables that produce values straight away, not async iterables that wrap values in promises (so you can use them to handle asynchronous requests like network requests, file streams or data coming from events and APIs). For that, you need either a very popular library or [Array.fromAsync](https://github.com/tc39/proposal-array-from-async), which makes the code easier to read (and write) and is [already available](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fromAsync#browser_compatibility) in all browsers and in JavaScript runtimes like Node and Deno. In fact, it has been for long enough to be part of [Baseline 2024](https://thenewstack.io/baseline-newly-available-stay-on-top-of-new-web-features/).

But so far, the details of how it works haven’t been added to the ECMAScript standard, mainly because there was a small bug that was quickly fixed in implementations but not actually written up in the specification, and a change to match behaviour elsewhere in JavaScript that adds a new WPT test that nearly all browsers already pass as well. There’s already agreement that it will reach Stage 4 as soon as the TC39 editors approve the spec changes, which should be in time for ECMAScript 2026.

Similarly, [Explicit Resource Management](https://github.com/tc39/proposal-explicit-resource-management) needs the last few tests to be reviewed and the text of the specification to be approved to hit Stage 4, but it’s already shipping in Chrome, Node, Deno, the [Moddable XS engine](https://www.moddable.com/faq#what-is-xs) for embedded devices, and (behind a flag) Firefox; along with support in Babel, TypeScript and other tools.

Previously, checking that you’re explicitly cleaning up resources like memory has meant a lot of scrolling up and down in your code, explained [Ashley Claymore](https://www.linkedin.com/in/ashleycutmore/) (a Bloomberg software engineer who has worked on multiple TC39 proposals).

“You acquire the resource up here in the try block and you know you have to clean it up regardless of what happens, whether it returns or throws, but you’d have to put it all the way down in the finally block.” But with long code blocks, a developer probably won’t see both on screen at once. “You see that a resource is required and you’re hoping it gets cleaned up, and you scroll and scroll until you find the final block and see, yes, it’s getting cleaned up, so you scroll back up to the top and then carry on. Now you get it for free with the using block.”

> “…this [Explicit Resource Management] now makes it so much more ergonomic, and it standardizes how this is going to be done.”  
> **– Ashley Claymore, Bloomberg software engineer**

Instead of using const, you create a using block and objects can define Symbol.dispose or Symbol.asyncDispose that are automatically called at the end of the code block. This is much more like working in C++, C# or Python.

“Even if your code throws an exception, or if it just returns, you’re guaranteed that the cleanup is going to happen. It’s something you could do before, but this now makes it so much more ergonomic, and it standardizes how this is going to be done.”

Tools like Babel, TypeScript and esbuild already support this, and can help developers get into good habits where resources get cleaned up deterministically, Claymore suggested.

“In the past, what people might have done is use a finalization registry and rely on the garbage collector to clean things up. While it looks really nice in the code, that’s problematic because the garbage collector is very unpredictable. You don’t know when it will run. Say you have a database handle and your database has a hard limit of 256 connections: your garbage collector doesn’t know that. Your garbage collector just knows how much memory you’re using. Waiting for the garbage collector to decide ‘you’re using too much memory, I’m going to start cleaning things up, and I may or may not call your finalization registry handler’ is too risky.”

## The Long-Awaited Temporal API: A Fix for JavaScript’s Date Object

Other projects that were expected to make it into ECMAScript in 2025, like [Decorators](https://github.com/tc39/proposal-decorators) (which is already broadly available through transpilers), are still working through the final steps. But [Temporal](https://github.com/tc39/proposal-temporal), the long-awaited replacement for “[JavaScript’s broken Date object](https://thenewstack.io/javascript-forecast-whats-ahead-for-ecmascript-2022/#:~:text=Temporal,%20for%20Date-Related%20Javascript.%20Temporal,%20which%20Terlson%20refers%20to%20as)“, has already reached an important milestone: It’s now a Stage 3 draft and the first implementations are happening.

“Date hasn’t aged very well. It’s pretty bad, and developers either use it wrongly and have bugs or they just avoid it altogether,” explained [Jason Williams](https://www.linkedin.com/in/jason-williams10/), creator of [Boa](https://github.com/boa-dev/boa) (an embeddable JavaScript engine written in Rust) and one of the Temporal champions at TC39.

The date libraries developers have adopted to work around those problems add a lot of extra code to projects, especially if you need time zone support or internationalization.

> “Temporal is a lot better at helping you avoid mistakes and trying to be more explicit.”  
> **– Jason Williams, creator of Boa**

“If you take any web app and put it into a bundle analyzer, sometimes the biggest square in there is usually [Moment.js](https://momentjs.com/) or something similar,” Williams noted. “It doesn’t make sense for us to keep sending that over the wire when browsers often have that data anyway.”

The new spec is also just better designed: “Temporal is a lot better at helping you avoid mistakes and trying to be more explicit.” It handles time zones, includes a built-in calendar and parses and formats dates and times correctly, creating nice, human-readable versions of time and date strings. That’s something Date is so bad at that Budibase developer [Sam Rose](https://github.com/samwho) was [inspired by his discovery that it treats 0 and “0” differently](https://bsky.app/profile/samwho.dev/post/3ltpdkr3bmk2o) to create [an infuriatingly funny quiz](https://jsdate.wtf/) mocking its idiosyncrasies. (In fact, because much of Date’s behaviour is implementation dependent, the answers to that quiz will be different in Firefox and Chrome.)

Temporal is big, in impact and in code size. Typical JavaScript features might have a couple of hundred tests; Temporal has 4,000 tests and at one point had almost twice as many.

“It was actually bigger than the [tests for] the whole of ES6 combined; that’s how much surface area it covers,” Williams said. “We did bring it down, because we tried to reduce the complexity.”

Agreeing on the specification took time (“we’re now at the long tail with small bugs coming through tidying it up,” Williams added) and implementing it will too. Although Firefox has already shipped an implementation.

The V8 team is collaborating with Boa on a Rust crate called [temporal\_rs](https://lib.rs/crates/temporal_rs) that contains most of the logic for Temporal, that other JavaScript engines can also use – a pattern of open source community work that could reduce adoption costs in browsers for new JavaScript features generally. The [Kiesel](https://kiesel.dev/) and [Yavashark](https://github.com/Sharktheone/yavashark) JavaScript engines are also adopting it.

> “It [Temporal] makes so many things around dates and times so much easier to do, and with a smaller chance of programmer error.”  
> **– Meyer**

The [library](https://github.com/boa-dev/temporal) is now available in v0.1, to allow for any last-minute spec changes — even though it passes all current tests and is ready to use. It’s already [unflagged](https://issues.chromium.org/issues/401065166#comment106) for V8 and is expected to land in [Chromium 144](https://chromestatus.com/feature/5668291307634688)  (which becomes stable on 7th January 2026), while the Safari implementation in the WebKit repo is almost half finished and [two](https://www.npmjs.com/package/@js-temporal/polyfill)[polyfills](https://www.npmjs.com/package/temporal-polyfill) designed for production use are also available. The Ladybird and Graal engines also have mostly complete implementations.

That makes Temporal a strong possibility for ECMAScript 2026 — Williams [predicted](https://boajs.dev/blog/2025/09/24/temporal-release) it would reach [stage 4](https://github.com/tc39/proposal-temporal/milestone/2) in Q1 2026, which might be in time for the February cutoff. This is something that Igalia developer advocate [Brian Kardell](https://www.linkedin.com/in/brian-kardell-08a4264/) is enthusiastic about: “What a huge endeavor, and what a massive amount of code that this can take out of our applications! So good.”

“It makes so many things around dates and times so much easier to do, and with a smaller chance of programmer error,” agrees Meyer. “I was able to write a basic ‘tell me the date halfway between today and some given date, and what date is as far away from a given date as that given date is from today’ tool in a morning, and I was learning the Temporal methods as I wrote it.”

## Optimizing Performance With Deferred Module Imports

Another Stage 3 proposal that is likely to make it into ECMAScript 2026 is one of the ‘[module harmony’](https://thenewstack.io/how-javascript-is-finally-improving-the-module-experience/) improvements to improve performance: [Import defer](https://github.com/tc39/proposal-defer-import-eval).

“Unlike normal loading, which is eager and causes the module to be evaluated before anything in the current one is, instead you get a handle to the namespace,” TC39 co-chair [Rob Palmer](https://www.linkedin.com/in/robpalmer2), who also works for Bloomberg, explained. “The moment you touch the namespace, the moment that you pull off a property — which could happen much, much later — the first time you make use of that module namespace, that’s the point when the module gets loaded. This is really useful in large code bases, where you have deep module graphs that can take hundreds of milliseconds to load, because you can make sure that you’re only paying for what you use.”

> “This [import defer] is really useful in large code bases, where you have deep module graphs that can take hundreds of milliseconds to load…”  
> **– Rob Palmer, TC39 co-chair**

The Bloomberg terminal (written in C++ and JavaScript) already uses this pattern. “We have some huge, complex applications, and it’s difficult to know, even with a compiler, it’s difficult to know what the optimal loading order will be, and so being able to say, ‘let the code run and whatever it hits, we’ll load it in just in time’ turns out to be a very efficient way of working.”

JavaScript already has dynamic import, but that means going back and making a network call to load a module — which might be too slow.

“If you can do dynamic import, you should,” Palmer suggests. But existing code can’t always be converted to use dynamic import. “You need to make sure that your caller and your call are all asynchronous and able to tolerate the async loading, whereas when you’re using the defer keyword, everything is still synchronous, so it’s a lot easier to sprinkle that in as an optimization when you find you need it.”

Postponing module evaluation using import defer is already supported by [various tools](https://github.com/tc39/proposal-defer-import-eval/issues/73) like [TypeScript](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-9.html#support-for-import-defer), Prettier, Babel and [webpack](https://webpack.js.org/guides/lazy-loading/). With implementations underway in [V8](https://issues.chromium.org/issues/398218423) and the WebKit [JavaScriptCore](https://github.com/WebKit/WebKit/pull/40453) engine (and on the backlog for [SpiderMonkey](https://bugzilla.mozilla.org/show_bug.cgi?id=1952263)), Palmer predicts it will be supported in browsers in 2026 and speeding up startup times for large web applications.

Most other languages already let you check a value of ‘it exists’ or ‘insert if it doesn’t’ without writing a conditional test, because it’s a really common database operation; now JavaScript will get that with [Upsert](https://github.com/tc39/proposal-upsert) (a portmanteau of update and insert) for both maps and weak maps. The feature will ship in Chrome 145 in January 2026, Palmer noted, making it likely to reach Stage 4 in March. This is a relatively straightforward feature, so it’s being used to get more people involved in contributing to browsers — with [students from the University of Bergen](https://webengineshackfest.org/slides/cross-engine_contributions_at_scale:_how_newcomers_accelerated_temporal_and_upsert_in_spidermonkey,_v8,_and_boa_by_jonas_haukenes,_mikhail_barash_&_shane_carr.pdf) currently working on the code.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/e2700739-maryb.jpg)

After completing an MSc in Intelligent Knowledge Based Systems in 1990, Mary Branscombe was convinced that promising as the AI techniques she’d been studying were, they weren’t even close to being ready. Since then, she’s been a technology journalist for...

Read more from Mary Branscombe](https://thenewstack.io/author/marybranscombe/)