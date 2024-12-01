# Deno Applies to Cancel Oracle's JavaScript Trademark

![Deno Applies to Cancel Oracle's JavaScript Trademark](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)

Deno is petitioning the United States Patent and Trademark Office (USPTO) to cancel [Oracle's JavaScript trademark](https://thenewstack.io/free-javascript-from-legal-clutches-of-oracle-devs-petition/), Deno creator Ryan Dahl [announced Monday](https://deno.com/blog/deno-v-oracle).

“This marks a crucial step toward freeing ‘JavaScript’ from legal entanglement and establishing it as a shared, public resource,” Dahl [wrote](https://github.com/ry).

Deno is an open-source runtime for JavaScript, TypeScript, and WebAssembly. Dahl is well-known in the front-end community for creating Node.js. He notes that if this effort is successful, the community can claim ownership of JavaScript, promoting it in conferences and as a standard, rather than the current “ECMAScript.”

The [application](https://ttabvue.uspto.gov/ttabvue/v?pno=92086835&pty=CAN&eno=1) argues that JavaScript is the generic name for the programming language and that Oracle neither controls nor ever controlled the language's specification or use. It also alleges that Oracle submitted false evidence to the USPTO when renewing the JavaScript trademark in 2019.

“This included screenshots of [Node.js](https://thenewstack.io/node-js-22-release-improves-developer-experience/)—a project I created myself and entirely unrelated to Oracle,” Dahl wrote.  “Presenting Node.js as evidence of Oracle’s ‘commercial use’ violates the integrity of trademark law.”

Finally, Dahl claims Oracle (which acquired the trademark through its 2009 acquisition of Sun Microsystems) has effectively abandoned the trademark through non-use.

“The application demonstrates that Oracle has not offered significant products or services under the name ‘[JavaScript](https://roadmap.sh/javascript)’ for years,” he said. “Obscure products like the JavaScript Extension Toolkit or GraalVM do not constitute genuine commercial use. US law considers a trademark unused for three consecutive years to be abandoned, and Oracle’s inaction clearly meets this standard.”

## Vite 6 Released

In other news, [Vite 6 was released on Tuesday](https://vite.dev/blog/announcing-vite6.html), which the Vite [team](https://thenewstack.io/development-server-vite-gets-independent-team-and-rust-ifies/) calls “the most significant major release since Vite 2.” A quick look at the [GitHub changelog](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#600-2024-11-26) reveals why—it’s an extensive list of breaking changes, features, fixes, and miscellaneous items.

The team reports continued growth in adoption—weekly npm downloads have jumped from 7.5 million to 17 million since the release of Vite 5. They also thank new frameworks that have joined the Vite ecosystem, including [TanStack Start](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/), [One](https://news.ycombinator.com/item?id=41742278), and [Ember](https://emberjs.com/).

Vite 6 supports Node.js 18, 20, and 22+, but has dropped support for Node.js 21 (Vite stops supporting older Node.js versions after their end-of-life).

The team also wrote about its new [Environment API](https://green.sapphi.red/blog/increasing-vites-potential-with-the-environment-api), which is experimental and primarily aimed at framework authors.

“These new APIs will allow framework authors to provide a closer-to-production development experience and allow the ecosystem to share new building blocks,” the blog post notes. “If you are building [SPAs](https://thenewstack.io/secure-single-page-apps-with-cookies-and-token-handlers/), nothing changes; everything remains the same when you use Vite with a single client environment. Even for custom SSR applications, Vite 6 is backward compatible.”

There’s a [migration guide](https://vite.dev/guide/migration.html), but major changes in Vite 6 include:

* [Default value for `resolve.conditions`](https://vite.dev/guide/migration.html#default-value-for-resolve-conditions)
* [JSON stringify](https://vite.dev/guide/migration.html#json-stringify)
* [postcss-load-config](https://vite.dev/guide/migration.html#postcss-load-config)
* [Extended support of asset references in HTML elements](https://vite.dev/guide/migration.html#extended-support-of-asset-references-in-html-elements)
* [Sass now uses modern API by default](https://vite.dev/guide/migration.html#sass-now-uses-modern-api-by-default)
* [Customize CSS output file name in library mode](https://vite.dev/guide/migration.html#customize-css-output-file-name-in-library-mode)

## Tailwind CSS Releases V4.0 Beta 1
上周晚些时候，Tailwind 发布了 4.0 Beta 1 版本。大约八个月前，Tailwind CSS 团队开源了他们的进展，此次发布紧随其后，此外，Tailwind 开发者描述了“数百小时的 bug 修复、令人沮丧的向后兼容性工作以及 Windows CI 故障排除”。

结果，他写道，这是一个“为性能而构建，专为现代网络设计的全新引擎”。据说完整构建速度提高了 5 倍，增量构建速度提高了 100 多倍，以微秒为单位测量。

它还有一个统一的工具链和 CSS 优先配置。它专为现代网络而设计，因为它“建立在原生级联层、广色域颜色之上，并包括对现代 CSS 特性（如容器查询、`@starting-style`、弹出窗口等）的一流支持”。

团队还发布了 beta 文档，以帮助开发者入门。


[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。