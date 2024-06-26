# TypeScript 5.5: Faster, Smarter and More Powerful
![Featued image for: TypeScript 5.5: Faster, Smarter and More Powerful](https://cdn.thenewstack.io/media/2024/06/8465ea7a-hotwheels-1024x692.png)
[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) recently released [TypeScript](https://thenewstack.io/what-is-typescript/) 5.5 offering a range of features and optimizations to enhance the company’s [JavaScript](https://thenewstack.io/outer-excuses-why-javascript-developers-should-learn-sql/) superset.
This update includes inferred type conditions, improved expression validation and separate declarations, as well as notable performance boosts and enhancements to editor reliability.

## Better Developer Experience
The release focuses on improving developers’ experiences. TypeScript 5.5 aims to provide quicker build processes and stronger tooling assistance.

“Writing types in our code allows us to explain intent and have other tools check our code to catch mistakes like typos, issues with `null`
and `undefined`
, and more,” wrote [Daniel Rosenwasser](https://www.linkedin.com/in/daniel-rosenwasser-b56b7837/), principal product manager for TypeScript at Microsoft, in a [blog post](https://devblogs.microsoft.com/typescript/author/danielrosenwasser). “Types also power TypeScript’s editor tooling like the auto-completion, code navigation, and refactorings that you might see in editors like [Visual Studio](https://thenewstack.io/microsoft-visual-studio-2017-devops-five-star-app/) and [VS Code](https://thenewstack.io/this-week-in-programming-all-hail-visual-studio-code/). In fact, if you write JavaScript in either of those editors, that experience is powered by TypeScript!”

Microsoft has made several changes to the language since the beta and release candidate versions of TypeScript 5.5.

For instance, “since the beta, we [added support for ECMAScript’s new Set methods](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/#support-for-new-set-methods). Additionally, we’ve adjusted the behavior of [TypeScript’s new regular expression checking](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/#regular-expression-syntax-checking) to be slightly more lenient, while still erroring on questionable escapes that are only allowed per [ECMAScript](https://thenewstack.io/the-new-javascript-features-coming-in-ecmascript-2023/)’s Annex B,” the post said

Microsoft also added and documented more [performance optimizations](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/#performance-and-size-optimizations): notably, skipped checking in `transpileModule`
and optimizations in the way TypeScript filters contextual types. These optimizations can lead to faster build and iteration time, the company said.

## Summary of Key New Features
Summarized highlights of key new features and improvements in TypeScript 5.5 include:

- Inferred type predicates: Improves type inference in certain scenarios, especially with arrays and filtering.
- Control flow narrowing for constant indexed accesses: Enhances type narrowing for object property accesses.
- The JSDoc
`@import`
tag: New tag for importing types in JavaScript files without runtime impact. - Regular expression syntax checking: Basic syntax checking for regular expressions to catch common mistakes.
- Support for new ECMAScript
`Set`
methods: Adds declarations for proposed new`Set`
methods. - Isolated declarations: New compiler option to help with faster declaration file generation.
- The
`${configDir}`
template variable: Helps with writing more portable configuration files. - Consulting
`package.json`
dependencies: Improves declaration file generation by considering package dependencies. - Editor and watch-mode reliability improvements: Various fixes to improve editor experience and watch mode.
- Performance and size optimizations: Multiple improvements to compiler speed and package size.
- Easier API consumption from ECMAScript Modules: Better support for using TypeScript’s API in ESM (ECMAScript Modules) environments.
- The
`transpileDeclaration`
API: New API for generating declaration files for single files.
## Keeps Delivering
[Holger Mueller](https://www.linkedin.com/in/holgermueller/), an analyst at Constellation Research, who harkens back to the initial launch of TypeScript said, “Microsoft keeps investing into TypeScript with the release 5.5. – even if the release of the first .5 release may point to a slowdown. But at its core TypeScript has delivered and keeps delivering what it was invented for: Making JavaScript-based applications scale to enterprise grade and size. The release offers new capabilities across the board, with none sticking out, making it a ‘boring’ but effective release for TypeScript developers.”
The release also includes some behavioral changes, such as disabling features deprecated in TypeScript 5.0. The next version, TypeScript 5.6, is planned for early September.

Meanwhile, [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at Omdia, noted, “In short, I’d say that the 5.5 update shows just how far this relatively new language has come in terms of addressing important demands surrounding software stability and scale; it also showcases just how far TypeScript has ventured from its roots in JavaScript. I think it’s fair to say that with new features like syntax checking of regular expressions, which were previously ignored at compile time, TypeScript is starting to look more and more like Java in terms of supporting enterprise-grade deployments.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)