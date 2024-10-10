# JavaScript Due for New Time, Date and Set Features Next Year
![Featued image for: JavaScript Due for New Time, Date and Set Features Next Year](https://cdn.thenewstack.io/media/2024/10/f9227aec-allison-saeng-zo9fjlfuokm-unsplash_1280-1024x576.jpg)
The language features that will be included in the next [annual update to JavaScript](https://thenewstack.io/whats-new-for-javascript-developers-in-ecmascript-2024/) will be decided early in the new year, including projects that reach the final stage four milestone by March 2025 (and there are a couple of features that have already gotten that far).

There are others that are on track to be ready in time to make the list — including at least one much-requested project that has been eagerly awaited and appears to be finally in the home straight. Two new features reached stage four just after the ECMAScript 2024 cutoff date: duplicate named capture groups for handling regular expressions and methods for handling sets.

## Setting the Scene for JavaScript Efficiency
Being able to [use the same names in different branches of a regexp](https://github.com/tc39/proposal-duplicate-named-capturing-groups) is a small but useful feature that will simplify writing expressions, where you need to match something that can be expressed in different ways but will only match once (like the year being 2025 or just 25 in a date). Currently, you get an [error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_duplicate_capture_group_name) if you call both of those patterns “year”, so you have to come up with different names. Now you can use the same name as long as it’s in different branches of the expression, separated by a |.

“It’s a strong show of support when the browsers all very quickly produce these [implementations] and that’s what we aspire to as much as possible when pushing any of these proposals forward.”

– Rob Palmer, TC39 co-chair
New methods for working with JavaScript’s Set class have been under discussion for years: This is a feature where the language has lagged behind so many other languages (like Python, Ruby, Swift, Rust and C#), leaving developers to write their own set methods or [use a polyfill](https://github.com/zloirock/core-js?tab=readme-ov-file#set) like Core.js. TC39 co-chair [Rob Palmer](https://www.linkedin.com/in/robpalmer2) described this as “another classic case where people have been writing their own three to four line utility functions to process sets and to offer basic set operations since ES 2015, which is now nine years ago.”

“The reason this proposal took so long was because it hit new ground in the language,” explained [Ashley Claymore](https://www.linkedin.com/in/ashleycutmore/), a Bloomberg software engineer who has worked on multiple TC39 proposals.

Before these new set methods, JavaScript didn’t have a complex type that could be combined with another instance of the same type and return an instance, so there wasn’t an example for how the new functionality ought to work.

“We spent a lot of time talking about, what is a set,” said Claymore. “If I have a set intersect with another set, what could that other set be? Is that other set an iterable? Must it be an actual official set instance that was created with new Set? What happens if you pass a map to a set method?”

“…actually answering what is a set was what we spent a lot of time discussing, and now we’ve got an answer for that.”

– Ashley Claymore, Bloomberg software engineer
It was important to get those technical questions right in a way that doesn’t have unintended consequences.

“Everyone agreed this is useful,” he continued. “Set should do these things, these are methods we should probably have. But actually answering what is a set was what we spent a lot of time discussing, and now we’ve got an answer for that.”

All that discussion made sure that what sounds like basic functionality is implemented in a way that fits properly into the language.

A set is like an array but each value is unique, so you can only add new values that aren’t already in the set. That means you might be interested in working with all the values that are in one set and not in another (difference), in either of two sets as long as they’re not on both (symmetricDifference), or only the values that are in two sets (intersection), or in various other combinations. The seven new methods cover the standard range of what developers need to do with sets: union, intersection, difference, symmetricDifference, isSubsetOf, isSupersetOf, isDisjointFrom.

“I use sets a lot, but you don’t often use them without wanting one or more of these, and you’d think they’d have been in the standard library right away, but they just weren’t.”

– Brian Kardell, Igalia developer advocate
“I use sets a lot, but you don’t often use them without wanting one or more of these, and you’d think they’d have been in the standard library right away, but they just weren’t,” Igalia developer advocate [Brian Kardell](https://www.linkedin.com/in/brian-kardell-08a4264/) told The New Stack**. “**As a developer (and a developer *advocate*), I get really excited about that because I know that I will use those forever — just like my favorite few Array methods.”

Even though developers have been able to do this in JavaScript by writing their own functions, having these in the language saves time and helps with consistency.

“Sets and Array methods are valuable because they’re used a lot,” continued Kardell, “and you don’t need to rewrite them or worry about whether your big program winds up with five implementations of the same thing.”

Because reaching stage four means there are at least two major implementations, developers can consider using both these features straight away. The new Set feature is now supported in all major browsers: it shipped in Firefox and [TypeScript 5.5](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5) as of June 2024, making it [widely enough available](https://thenewstack.io/what-does-it-mean-for-web-browsers-to-have-a-baseline/#:~:text=A%20new%20project%20called%20Baseline%20aims%20to%20clarify%20what%20developers) to become part of [Baseline 2024](https://web.dev/blog/set-methods?hl=en), which Kardell glosses as “when we ship the last implementations of something”.

Palmer views the speed at which the Set methods moved into baseline as a good example of the pipeline from standard to broad availability that the [ECMAScript standardization process](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/) aims to deliver: “It’s a strong show of support when the browsers all very quickly produce these [implementations] and that’s what we aspire to as much as possible when pushing any of these proposals forward. You don’t want people to hold back using them because they’re not available in one browser, even though, obviously, there’s always the solution of using a compiler like Babel or TypeScript.”

Duplicate capture groups is not quite as advanced: it’s supported in all the major desktop browsers and most mobile browsers (it’s still in preview in Samsung’s mobile browser), but not in Node.js or Deno yet.

## The Next Stage: Decorators, JSON Modules, and Promises
The other features that are most likely to be ready in time for ECMAScript 2025 are proposals that have already reached stage three: decorators, JSON modules, Promise.try, and (finally) Temporal.

### Decorators
Decorators add extra functionality to existing code by wrapping it in another piece of code (like adding curtains or a new coat of paint to a room to make it more useful). That can be as simple as changing the appearance of the code to make it more readable without changing the underlying code, or it can provide more flexible ways of structuring code by making it more modular.

With decorators, instead of putting the logic for handling your data store and your templates together in the class you’re writing, which would make it less flexible and harder to reuse for other projects, you can put the dependencies outside the class. Decorators let developers create abstractions for common tasks like logging, dynamic type checking, and other security checks (like validating parameters) and add them to classes when they’re needed.

“We saw that the transition path from existing use of decorators was important, and we want to enable incremental adoption and treat the existing ecosystem well: we’re not designing this in a vacuum.”

– Daniel Ehrenberg, Ecma vice president
This is a pattern that’s widely used in frameworks like React and Angular, and it’s been supported in TypeScript and Babel for many years — although not in exactly the same form as what the ECMAScript proposal has developed into after many years of discussion (which allows decorators to work with private fields and methods).

Although the broader concept of decorators has been widely validated by extensive use in transpilers, it has taken quite some time to agree on the right approach in the JavaScript language itself.

“We went through many iterations of the decorator proposal and we finally arrived at one that we could agree met both the use cases and the transition paths that were needed from previous decorators and the implementability concerns from browsers,” Ecma vice president [Daniel Ehrenberg](https://www.linkedin.com/in/danielehrenberg/) explained. “We were finally able to triangulate all of that. It does mean that there’s some differences, but at the same time, we’ve really tried to make sure that the transition is smooth.”

Part of that is allowing code to use either the existing syntax of TypeScript’s experimental decorators or the new syntax of the proposal. You have to pick one or the other for individual functions, but he explained, “In one particular exported class declaration, the decorators can come either before or after the exported keyword.” It’s a little thing but it avoids developers needing to rewrite existing code.

“We saw that the transition path from existing use of decorators was important, and we want to enable incremental adoption and treat the existing ecosystem well: we’re not designing this in a vacuum,” Ehrenberg noted.

As part of getting decorators into JavaScript, some of the more ambitious ideas about applying decorators to objects, variables and parameters were dropped from the proposal — but those remain as [a possible extension](https://github.com/tc39/proposal-decorators/blob/master/EXTENSIONS.md) using the same syntax.

### JSON Modules
In another simplification, [JSON modules](https://github.com/tc39/proposal-json-modules) were originally part of the Import Attributes proposal, part of the large [Module Harmony effort](https://thenewstack.io/5-ways-javascript-is-improving-modules-for-developers/) to fill in the gaps in [ECMAScript module functionality](https://thenewstack.io/how-javascript-is-finally-improving-the-module-experience/) in JavaScript. It was moved to a separate proposal to avoid holding up the more general concept of being able to include instructions for handling what you’re importing with the specifics of handling JSON files.

Implementations of both Import Attributes and JSON modules are underway, and will probably both move to stage four at the same time later this year.

Being able to mark a JSON or CSS file as text to be read rather than code to be executed is good for security, because it means the file won’t do something a developer isn’t expecting. Although this seems simple, it took some time for the HTML and browser community, along with the ECMAScript committee, to work through the right syntax for integrating this into browsers. Chrome had already shipped the feature with the early version of the syntax (contributed by Microsoft), but that’s now been removed, and implementations of both Import Attributes and JSON modules are underway and will probably both move to stage four at the same time later this year. That doesn’t mean splitting the proposals apart was pointless; it allowed them to both move at their own speed, even if it looks like they will arrive together.

### Promises.try
Another feature that’s been in the works for some time fills in a small gap with using promises.

Promises.try reached stage three in June and there are already implementations in a range of browsers.

Promises in JavaScript handle the eventual success or failure of an asynchronous operation in a structured way: the catch method at the end of a chain of promises is supposed to catch all and any errors and the then method tells your code what to do about the error. But if you’re calling a function or using an API that takes a callback that might or might not be asynchronous, [Promise.try](https://github.com/tc39/proposal-promise-try) wraps the result of the callback in a promise, so if it throws an error, that will get caught and turned into a rejected promise. That way you can be sure you can handle synchronous and asynchronous errors in a single chain of promises. This is another popular feature that’s polyfilled in Core.js (as well as third-party promise libraries that predate the JavaScript implementation, like [Bluebird](http://bluebirdjs.com/docs/why-bluebird.html)).

Promises.try reached stage three in June and there are already implementations in a range of browsers (it’s in Edge and Chrome, has been added to WebKit, is behind a flag in current developer builds of Firefox, and is likely to be included in the November 2024 or January 2025 Firefox release) as well as runtimes like Bun and Cloudflare workers. That’s enough to reach stage four once the ECMAScript committee agrees, which should be comfortably in time for ECMAScript 2025.

## It’s About Time for Temporal
It seems increasingly likely that Temporal (which then TC39 editor [Brian Terlson](https://www.linkedin.com/in/brian-terlson-6822aa61/) memorably [described to us](https://thenewstack.io/javascript-forecast-whats-ahead-for-ecmascript-2022/#:~:text=Temporal,%20for%20Date-Related%20Javascript.%20Temporal,%20which%20Terlson%20refers%20to%20as) as “the replacement for our broken Date object” back in 2021, when it first reached stage three) will also be ready for ECMAScript 2025, because there’s been a lot of progress recently on [dealing with the issues](https://github.com/tc39/proposal-temporal/issues/2628) that have held it up.

When JavaScript was created in 1995, it [copied Java’s date object](https://maggiepint.com/2017/04/09/fixing-javascript-date-getting-started/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform): a rather simplistic implementation that Java replaced in 1997 but that struggles on in JavaScript (or more often is routinely replaced by libraries like Moment.js). Replacing that with Temporal was always expected to be a lot of work, because of the complexity of dates, times, timezones and calendars, but also to be relatively uncontroversial.

Temporal is clearly in demand: as part of the discussions about what would be included in [Interop 2023](https://thenewstack.io/how-interop-2023-will-move-the-web-forward/#:~:text=Interop%20progress%20as%20of%20August%202023.%20Government%20regulation%20on%20competition), Ehrenberg told us, “they did polls about which APIs developers would like and Temporal got a lot of votes”. So why has a popular proposal stayed on the verge of making it into the JavaScript language for five years?

“…the number of spec pages dedicated to Temporal is at roughly the same size as the entirety of ES6.”

– Palmer
One of the things that the proposal has been waiting on is the Internet Engineering Task Force (IETF) work to [standardize the ISO string formats used for calendar and time zone](https://www.rfc-editor.org/rfc/rfc9557.html) annotations. Somewhat delayed by the pandemic, that work was completed as a new RFC in April 2024, but even before it was finished it was clear that it hadn’t been the only thing holding up Temporal.

Dates and times form a large and complex subject with intricate rules (like the missing eleven days in UK history or the one time Toronto had a day that was 23 hours and 30 minutes long). Temporal started out as a really comprehensive approach to the problem: so comprehensive that as the various browsers started implementing it, it became clear that fitting all the code required into a JavaScript engine was going to take a lot of work and maybe more disk and executable memory space than is currently available on, say, an Apple Watch or a low-end Android phone.

Working out how to save space was a lot of work, looking at every single argument and function in Temporal to see how important it was and what would be lost without it, without either redesigning a proposal that’s been worked on for seven years or making it harder for developers to learn.

Although there were some places that the Temporal specification could be optimized, it also had to be cut down in scope — mainly by removing the calendar and timezone objects that were there to allow developers to build custom calendars and timezones. Those were both the most complicated parts of the proposal for web browsers to implement and also where they saw the most bugs.

“We really wanted to focus on making sure that we’re still meeting the important use cases.”

– Ehrenberg
Removing those from the spec was about “reducing the implementation and maintenance burden,” Ehrenberg explained. “We really wanted to focus on making sure that we’re still meeting the important use cases.”

“It’s just what is a more sensible size and scope given that the number of spec pages dedicated to Temporal is at roughly the same size as the entirety of ES6,” Palmer agreed. “It was becoming huge and we might get those things later.”

Partly that’s because new devices will have more storage and memory that makes room for more functions in JavaScript. And the experience of working on Temporal makes it clearer what will and won’t work for custom time zones and calendars, so new designs for those (likely based on [jsCalendar](https://www.rfc-editor.org/rfc/rfc8984.html), intended to replace the ubiquitous iCal format) may well be an improvement on the original approach.

Meanwhile, implementations are progressing in SpiderMonkey, V8, LibJS, JavaScriptCore and Boa, as well as a [polyfill from Fullcalendar.](https://github.com/fullcalendar/temporal-polyfill) When two of those are available, Temporal can finally move to stage four and become an official part of JavaScript. With luck, that will be in ECMAScript 2025.

## Making the Web Really International
Ambitious proposals like Temporal tend to require this kind of iterative design (hard as it is on the people leading the proposals through committee; Temporal has already have multiple “champions” leading the charge).

Another large and significant proposal, for [making it easier to localize websites and apps in multiple languages](https://thenewstack.io/whats-next-for-javascript-new-features-to-look-forward-to/#:~:text=Intl%20MessageFormat%20is%20another%20stage%201%20TC39%20proposal,%20in%20conjunction) by replacing proprietary message formats with a standard in JavaScript, is also making slow progress. Again, [the external ICU standard it relates to has made significant progress](https://www.unicode.org/reports/tr35/tr35-messageFormat.html#introduction), but the ECMAScript committee is [still discussing what the scope of the proposal should be](https://github.com/tc39/notes/blob/main/meetings/2024-04/april-10.md) in JavaScript in a way that has some of those involved rather frustrated by the slow progress.

And again, this is something developers want: almost a third of web localization uses a polyfill with an API very similar to the [Intl.MessageFormat](https://github.com/tc39/proposal-intl-messageformat) proposal (in fact it’s based on a similar proposal from 2013 that used the previous ICU MessageFormat).

“…they [big proposals like Intl.MessageFormat] solve harder problems and they’re also a real common good — improving those things helps encourage us to build a web that is more international.”

– Kardell
Even though the new ICU work was in response to the ECMAScript proposal, the TC39 committee wants to be sure that the approach is useful to organizations who aren’t already involved with MessageFormat 2: that would look like around a dozen new organizations using the new syntax in production. Bloomberg is already working on prototypes, but it looks like it will need more examples for that proposal to reach the stage when we can even speculate on when it will become part of the language.

But these big proposals remain exciting even when progress is slow, Kardell argues. “Things [that] are harder or even impossible — like [Temporal](https://github.com/tc39/proposal-temporal) or [Intl.MessageFormat](https://github.com/tc39/proposal-intl-messageformat) — or even [module bundles/inline modules ideas](https://github.com/tc39/proposal-module-expressions), those might require huge complexity, require build steps, or maybe there are things that are even just totally impossible to do realistically otherwise. I get excited about those for other reasons. Those are huge if we can get them. They won’t just improve performance a bit or something, they solve harder problems and they’re also a real common good — improving those things helps *encourage* us to build a web that is more international.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)