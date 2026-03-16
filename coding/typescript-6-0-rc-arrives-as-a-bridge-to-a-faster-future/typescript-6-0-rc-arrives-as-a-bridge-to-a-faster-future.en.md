TypeScript 6.0 Release Candidate (RC) is here, and in some ways, it’s the most consequential release since the project hit version 1.0 back in 2014. Not because it’s packed with flashy new features — though there are some — but because of what it’s setting up.

Microsoft’s [TypeScript](https://thenewstack.io/what-is-typescript/) team has been working in parallel on a [full rewrite of the compiler in Go](https://thenewstack.io/go-power-microsofts-bold-bet-on-faster-typescript-tools/), a systems programming language built for speed. That rewrite will ship as TypeScript 7.0. Version 6.0 is the bridge: [the last release of the old engine](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/), tuned up and pointed in the right direction before the swap. The team says 7.0 will follow soon after — likely within months.

## What’s actually new

The most practically useful addition is support for the [**Temporal API**](https://www.w3schools.com/js/js_temporal.asp), a long-overdue replacement for JavaScript’s `Date` object. Temporal gives developers proper tools for handling dates, times, and time zones without reaching for a third-party library like `date-fns` or `Luxon`. TypeScript is now built into the type definitions, so developers can start experimenting today.

Also new: types for **Map.getOrInsert** and **RegExp.escape**, two ECMAScript proposals that just reached stage 4 — effectively final. The former eliminates a common pattern of checking whether a Map key exists before setting a default. The latter handles escaping special characters in strings before they’re used in regular expressions, something developers have been doing manually for decades.

On the quality-of-life front, `dom.iterable` is now merged into the core `dom` library, so iterating over DOM collections no longer requires a separate config entry. It just works.

## What’s going away

The more significant part of the 6.0 story is the cleanup. This release deprecates or removes a long list of options that made sense in 2014 but look like ancient artifacts in 2026.

**ES5 output is gone.** Internet Explorer is dead, and TypeScript is recognizing that. Developers who still need ES5 output are pointed to external tools.

**AMD, UMD, and SystemJS module formats are deprecated.** These were the module systems of the pre-bundler era. Modern tools like Webpack, Vite, and esbuild have made them obsolete. ESM is the standard.

`strict` **now defaults to true****.** TypeScript’s strict mode catches a wide class of common bugs, but it used to be opt-in. As of 6.0 RC, it’s on by default. Projects relying on the old lenient defaults will need to explicitly set `"strict": false` — though the team would rather you fix the underlying issues.

`--baseUrl` **is deprecated.** Many configs used this to set up path aliases and avoid deeply nested relative imports. The option is deprecated in 6.0 and gone in 7.0. The fix is to move the mapping into the `paths` setting, which has handled this on its own for a long time.

## The change most likely to break things

One configuration change deserves a separate callout. The `types` field in a TypeScript config used to default to loading every package found in `node_modules/@types` — potentially hundreds of declaration files, most irrelevant to the project at hand.

In TypeScript 6.0, the default is now an empty array. Nothing is auto-loaded. Projects that rely on global types from `@types/node`, `@types/jest`, or similar packages need to declare them explicitly:

`"types": ["node", "jest"]`

The team says this change alone can cut build times by 20 to 50 percent. But developers who hit it without context will see a wall of “Cannot find name” errors and wonder what broke.

## The bottom line

TypeScript 6.0 is a release developers will mostly feel in their configs rather than in their code. The real action — the native [Go](https://thenewstack.io/introduction-to-go-programming-language/) compiler, parallel type checking, dramatically faster builds — comes with 7.0.

For now, the move is to upgrade to 6.0, address the deprecation warnings, and explicitly set your `types` array. Teams that do that work now will have a much smoother landing when 7.0 arrives, Microsoft says.

The TypeScript 6.0 RC is available via npm: `npm install -D typescript@rc`.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)