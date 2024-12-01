# Deno Petitions to Cancel Oracle’s JavaScript Trademark
![Featued image for: Deno Petitions to Cancel Oracle’s JavaScript Trademark](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
Deno is petitioning the United States Patent and Trademark Office ([USPTO](https://www.uspto.gov/)) to cancel [Oracle’s trademark for JavaScript](https://thenewstack.io/free-javascript-from-legal-clutches-of-oracle-devs-petition/), Deno creator Ryan Dahl [announced on Monday](https://deno.com/blog/deno-v-oracle).

“This marks a pivotal step toward freeing “JavaScript” from legal entanglements and recognizing it as a shared public good,” wrote [Dahl](https://github.com/ry).

Deno is an open source runtime for JavaScript, TypeScript, and WebAssembly. Dahl is well known in the frontend community for his creation of Node.js. He pointed out that if the effort succeeds, the community could claim JavaScript, promoting it at conferences and as a specification, as opposed to the current “ECMAScript.”

The [petition](https://ttabvue.uspto.gov/ttabvue/v?pno=92086835&pty=CAN&eno=1) asserts that JavaScript is a generic, universal name for the programming language and Oracle neither controls nor has ever controlled the language’s specifications or usage. It also claims that Oracle submitted fraudulent evidence to the USPTO when it renewed the JavaScript trademark in 2019.

“This included screenshots of [Node.js](https://thenewstack.io/node-js-22-release-improves-developer-experience/)—a project founded by myself and entirely unrelated to Oracle,” Dahl wrote. “Presenting Node.js as evidence of Oracle’s ‘use in commerce’ violates the integrity of trademark law.”

Finally, Dahl claims that Oracle, which acquired the trademark through its 2009 purchase of Sun Microsystems, has effectively abandoned it through non-use.

“The petition demonstrates that Oracle has not offered significant products or services under the name “[JavaScript](https://roadmap.sh/javascript)” in years,” he said. “Obscure offerings like the JavaScript Extension Toolkit or GraalVM, do not constitute genuine use in commerce. U.S. law considers trademarks unused for three consecutive years as abandoned, and Oracle’s inaction clearly meets this threshold.”

## Vite 6 Released
In other news, [Vite 6 released Tuesday](https://vite.dev/blog/announcing-vite6.html), with the [Vite](https://thenewstack.io/development-server-vite-gets-independent-team-and-rust-ifies/) team calling it the “most significant major release since Vite 2.” A quick look at the [GitHub change log](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#600-2024-11-26) shows why — it’s an extensive list of breaking changes, features, fixes and chores.

The team reported that adoption keeps growing — npm downloads per week jumped from 7.5 million to 17 million since the release of Vite 5. They also gave shoutouts to new frameworks that had joined the Vite ecosystem, which included [TanStack Start](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/), [One](https://news.ycombinator.com/item?id=41742278) and [Ember](https://emberjs.com/).

Vite 6 supports Node.js 18, 20, and 22+, but Node.js 21 support has been dropped (Vite drops Node.js support for older versions after their end of life).

The team also wrote about its new [Environment API](https://green.sapphi.red/blog/increasing-vites-potential-with-the-environment-api), which is experimental and primarily aimed at framework authors.

“These new APIs will allow framework authors to offer a dev experience closer to production and for the Ecosystem to share new building blocks,” the blog post noted. “Nothing changes if you’re building a [SPA](https://thenewstack.io/secure-single-page-apps-with-cookies-and-token-handlers/); when you use Vite with a single client environment, everything works as before. And even for custom SSR apps, Vite 6 is backward compatible.”

There is a [migration guide](https://vite.dev/guide/migration.html) but the listed main changes to Vite 6 include:

[Default value for resolve.conditions](https://vite.dev/guide/migration.html#default-value-for-resolve-conditions);[JSON stringify](https://vite.dev/guide/migration.html#json-stringify);[postcss-load-config](https://vite.dev/guide/migration.html#postcss-load-config);[Extended support of asset references in HTML elements](https://vite.dev/guide/migration.html#extended-support-of-asset-references-in-html-elements);[Sass now uses modern API by default](https://vite.dev/guide/migration.html#sass-now-uses-modern-api-by-default); and[Customize CSS output file name](https://vite.dev/guide/migration.html#customize-css-output-file-name-in-library-mode)in library mode.
## Tailwind CSS Releases V4.0 Beta 1
[Tailwind released version 4.0 Beta 1](https://tailwindcss.com/blog/tailwindcss-v4-beta) late last week. About eight months ago, the Tailwind CSS team open-sourced it’s progress and this release comes on the heels of that, plus what Tailwind developer [Adam Wathan](https://github.com/adamwathan) described as “hundreds of hours of fixing bugs, soul-crushing backward compatibility work, and troubleshooting Windows CI failures later.”
The result, he writes, is an “all-new engine built for performance, and designed for the modern web.” It’s said to be 5 times faster on full builds, with incremental builds coming in at over 100 times faster and measured in microseconds.

There’s also a unified toolchain and CSS-first configuration. It’s designed for the modern web in that it’s “built on native cascade layers, wide-gamut colors, and including first-class support for modern CSS features like container queries, @starting-style, popovers, and more,” he wrote.

The team also published [beta documentation](https://tailwindcss.com/docs/v4-beta) to help developers get started.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)