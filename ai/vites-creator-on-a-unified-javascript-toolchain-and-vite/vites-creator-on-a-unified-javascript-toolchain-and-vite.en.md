There will be advantages to frameworks that roll out as Vite plugins, such as [Remix React Router](https://thenewstack.io/remix-react-router-merge-jetbrains-ide-for-test-automation/), TanStack and Redmond have, said [Ethan You](https://github.com/yyx990803), the creator of [Vite](https://thenewstack.io/how-to-build-a-server-side-react-app-using-vite-and-express/) and the JavaScript framework [Vue](https://thenewstack.io/a-peek-at-whats-next-for-vue/).

You is now creating a new, unified toolchain for the JavaScript ecosystem, and he provided an [update on that project](https://gitnation.com/contents/vite-and-the-future-of-javascript-tooling) during the [JSNation 2025 conference](https://gitnation.com/events/jsnation-2025), which was held in Amsterdam and virtually presented in part on the GitNation platform.

He also introduced the idea of Vite+, which is still under development. Its goal is to do to JavaScript tooling what Cargo does for [Rust](https://thenewstack.io/rust-programming-language-guide/) — [Cargo](https://doc.rust-lang.org/rust-by-example/cargo.html) is the Rust package manager and build system.

“Remix React Router, [TanStack Start](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/), [Redwood SDK](https://rwsdk.com/) are all going towards this direction, this very smart way of leveraging [Vite](https://thenewstack.io/development-server-vite-gets-independent-team-and-rust-ifies/), and the future features in Vite+ as well, because in the future, when you ship your framework as a Vite+ plugin, you’ll be also able to hook into these additional commands,” You said. “The possibility is limitless when you have the full tool chain accessible through the plugin interface.”

A growing number of frontend frameworks are built on or have migrated to the development server Vite — including Angular, Astro Qwik, Redwood, Remix, Solid and SvelteKit. It was ultimately his work on Vite that led You to believe a better toolchain is needed for JavaScript.

”We’ve always been thinking about what we can do to make Vite serve this role better, and we came to the conclusion that Vite is far from perfect in its current state,” he said.

> “If we look into the bundler and look at all the lower level dependencies that a bundler needs, (we) realized that the JS ecosystem actually suffers from fragmentation at every layer.”  
> **– Ethan You, creator of Vite and Vue**

Specifically, You saw that Vite relied on third-party dependencies that had overlapping duties.

“The problem with this is that many of these tools have overlapping duties. They’re written in different languages,” he said. “There’s a lot of efficiency problems when you pass data back and forth between these tools, and they all have slightly different behavior when it comes to bundling or transformation.”

The team decided to build a bundler called Rolldown, with the goal of replacing esbuild and Rollup — which are currently used in Vite as dependencies — with one unified build tool.

But it’s sort of like those, “[If you give a mouse a cookie](https://en.wikipedia.org/wiki/If_You_Give_a_Mouse_a_Cookie)” books, where building a bundler means they also needed to pick and choose what linter to use, which transformer to use, etc.

“When you go down the rabbit hole, you realize the challenge that Vite is facing is really a reflection of the JavaScript ecosystem at large,” he said. “If we look into the bundler and look at all the lower level dependencies that a bundler needs, (we) realized that the JS ecosystem actually suffers from fragmentation at every layer.”

That’s leading to decision fatigue, and it’s overwhelming for the average user who is just starting out in JavaScript development. While the thriving JavaScript ecosystem has allowed developers to create more ambitious applications, as the language has matured, it’s led to a “complexity tax for everyone,” You said.

“I believe it is now a time where JavaScript deserves a unified tool chain,” he said. To that end, he founded [void(0)](https://voidzero.dev/team), pronounced “Void Zero.”

## The Focus for Void(0)

There are four major pieces the Void(0) team is working on:

* **[Vite](https://github.com/vitejs/vite)**
* **[Vitest](https://vitest.dev/guide/why)**, a test runner, which can be used alone in any JavaScript project.
* [**Rolldown**](https://github.com/rolldown/rolldown), a Rust bundler for JavaScript/TypeScript with a Rollup-compatible API. It supports Vite and Vitest internally. It was originally created by Yinan Long but is now led by You. It is currently in 1.0 beta status, according to You. “You can already use it almost as a drop-in replacement of Rollup, and you’ll see great performance improvements,” You said. It comes with built-in Node-compatible resolution so developers won’t need a plugin for that, he added. It also supports 90% of Rollup plugin interface compatibility, so while it is a Rust bundler, it does support JavaScript plugins, he added.
* **[OXC](https://oxc.rs/)**, the JavaScript Oxidation Compiler, is a set of tools that includes a linter, a parser, a resolver, a minifier (currently in alpha status) and a formatter (still under construction).  The [first stable version of Oxlint](https://voidzero.dev/posts/announcing-oxlint-1-stable) was released on June 9, 2025.

Many of the tools are already complete, including the parser, linter, resolver and transformer for OXC.

“Most of these things that we have built are the fastest in its own category, even compared to other solutions also written in native languages,” he said. “The parser, the linker, the resolver, the transformer, are all fastest in category. The minifier is second fastest, but it also has better compression ratio than the fastest solution, so it is still a very decent choice.”

There are plans to improve the compression ratio of the minifier in the future, he added.

## Update on the OXC Toolset

It helps to understand a bit about how all the tools function to understand what You is building.

A parser takes raw JavaScript code and transforms it into a structured, hierarchical representation called an [Abstract Syntax Tree (AST)](https://daily.dev/blog/js-parser-essentials-for-developers#:~:text=So%2C%20to%20sum%20it%20up,them%20into%20a%20tree%20diagram). The AST is a tree-like data structure, where each node represents a [construct in the code](https://nearform.com/insights/what-is-an-abstract-syntax-tree/) — for example, a variable declaration, a function call, or an if statement. It is the grammatical structure and content of a program, without the “superficial” details like whitespace or comments.

The parser is completely and Void(0) [benchmarks](https://github.com/oxc-project/bench-javascript-parser-written-in-rust) have found it is three times faster than the Rust-based compiler Speedy Web Compiler (SWC), which includes a parser.

[![The OXC toolkit created by Evan You's team.](https://cdn.thenewstack.io/media/2025/06/adb6cb51-oxc_toolit.png)](https://cdn.thenewstack.io/media/2025/06/adb6cb51-oxc_toolit.png)

The OXC toolkit created by Evan You’s team.

The AST is the fundamental input required for almost every other JavaScript tool to do its job.

Minifiers use the AST to safely rename variables, remove dead code, and optimize the code structure without altering its functionality. It basically [strips all unnecessary characters from source code](https://wysiwyg-editor.froala.help/hc/en-us/articles/360000185869-What-is-the-difference-between-minified-and-unminified-source-code) without changing its functionality. Tools like Webpack, Rollup, Vite, Terser (a popular JavaScript minifier) and Esbuild all incorporate minification as part of their optimization pipeline.

[Linters](https://owasp.org/www-project-devsecops-guideline/latest/01b-Linting-Code) enforce coding styles, identify potential bugs or highlight suspicious patterns.

[Bundlers](https://career.comarch.com/blog/javascript-bundlers-is-it-worth-switching-from-webpack-to-vite/), such as Webpack, the SWC and Rollup, parse individual modules into ASTs to understand their dependencies and combine them efficiently. For production builds, Vite acts as a bundler, using Rollup to compile and optimize an application’s code into efficient, production-ready bundles. Vite can also be used with the Speedy Web Compiler (SWC), which is a JavaScript and TypeScript compiler written in Rust that can also be used for bundling. Vite is working on its own bundler, called [Rolldown](https://rolldown.rs/).

Code Formatters parse the code into an AST and then print it back out in a consistent style. Void(o) has completed a prototype formatter but it is not yet available for use.

Transpilers take an AST, e.g. modern JavaScript, and transform it into another AST, e.g. older JavaScript, before converting it back to code. Void(o) has built a [Babel](https://babeljs.io/)-compatible transformer that transforms TypeScript to ESNext and React JSX to ESNext. Transformers are a broader category of tools that modify code in various ways and, therefore, include transpilers.

## Coming Soon: Vite+

Vite+ is still in the early development stage, but the idea comes from Cargo, which is Rust’s package manager and build system.

“If you have worked with Rust, you probably know that Cargo is the all-in-one toolkit, tool chain that can serve most of the development workflow needs during a Rust development,” You said. “There’s nothing like that in JavaScript, and Vite+ is exactly what we’re trying to build to fulfill that role.”

Developers will be able to point their package manager to Vite+ and be good to go, he said.

“Everything that works in today’s Vite will continue to work exactly the same way, but the Vite command line just becomes more powerful,” he said. “Now it comes equipped with additional commands like Vite lib that is dedicated for library bundling, Vite test and bench Vite link to format, Vite new for Project scaffolding, Vite task for monorepo task orchestration and build caching.”

It will have a GUI dev tools, Workspace audits and policy enforcement for enterprise users. The team also will likely ship Vite+ with AI integration via a built-in MCP server, he added. There’s also additional support for [monorepos](https://thenewstack.io/the-case-for-and-against-monorepos-on-the-frontend/), he added.

“Vite+ is going to be monorepo aware, which means we will have pipelines, build, orchestration, caching — similar to that of Turborepo — and we’ll have first-class concept workspaces and policy enforcement,” You said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)