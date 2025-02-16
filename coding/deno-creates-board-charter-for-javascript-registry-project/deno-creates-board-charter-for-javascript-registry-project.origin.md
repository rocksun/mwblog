# Deno Creates Board, Charter for JavaScript Registry Project
![Featued image for: Deno Creates Board, Charter for JavaScript Registry Project](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
The [JSR is an open source package registry](https://jsr.io/) for modern JavaScript and TypeScript, [created last year by the Deno team](https://deno.com/blog/jsr_open_beta). But it was never meant to be a Deno project, according to a new post by Ryan Dahl, Luca Casonato and Leo Kettmeir: It’s supposed to be an [openly governed JavaScript/TypeScript community service](https://deno.com/blog/jsr-open-governance-board).

To further that end, they’ve created a new independent governing board of directors, complete with a governance charter.

The new JSR board members include:

[Evan You](https://github.com/yyx990803?),[creator of Vue.js and Vite](https://thenewstack.io/vite-creator-launches-company-to-build-javascript-toolchain/), founder of VoidZero;[Isaac Schlueter](https://www.linkedin.com/in/isaacschlueter/), creator of npm, cofounder of vlt;[James Snell](https://github.com/jasnell), Node.js TSC member, principal system engineer at Cloudflare;[Luca Casonato](https://github.com/lucacasonato), software engineer at Deno, TC39 representative;[Ryan Dahl](https://github.com/ry), creator of Node.js and Deno;
None of whom are *too* busy. Ahem.

The team also added the full charter to the article, for those curious about such things. And to be fair, it’s wise to be curious about [what happens with your favorite open source offerings](https://thenewstack.io/open-source-is-at-a-crossroads/).

The JSR is as somewhat self-explanatory, but it’s worth noting that each package has a quality score that’s determined by a number of factors — such as completeness of documentation and optimal type declarations for fast type-checking.

## CVEs Released on 3 Node.js Versions
In January, [Node released three major Common Vulnerabilities and Exposures](https://nodejs.org/en/blog/vulnerability/upcoming-cve-for-eol-versions) (CVEs):

- Node.js v17.x or prior CVE-2025-23087
- Node.js v19.x CVE-2025-23088
- Node.js v21.x CVE-2025-23089
The blog post explains how to migrate, but, in related news, if you can’t migrate right away, there is help: [HeroDevs](https://www.herodevs.com/) announced this week it will support these three versions of [Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) as part of its [Never-Ending Support](https://docs.herodevs.com/additional-information/consuming-packages) initiative. HeroDevs is the only option listed in [endoflife.date](https://endoflife.date/nodejs#:~:text=for%20Production%20use.-,Node.,HeroDevs%20Never%2DEnding%20Support%20initiative).

HeroDevs is the the founding partner for [The OpenJS Foundation’s Ecosystem Sustainability Program](https://www.linuxfoundation.org/press/the-openjs-foundation-announces-the-ecosystem-sustainability-program-with-herodevs-as-the-first-partner), of which Node.js is a part.

## LinkedIn’s Case Study on Faster AI Prototyping
LinkedIn has been — like most of us — exploring how to use AI in its many products. One challenge the engineering team faced is [how to develop rapid prototypes while still getting feedback](https://www.linkedin.com/blog/engineering/product-design/building-collaborative-prompt-engineering-playgrounds-using-jupyter-notebook) from the non-technical domain experts, according to LinkedIn software engineer [Ajay Prakash](https://www.linkedin.com/in/ajay-prakash-3780b132/) and senior engineering manager [Lukasz Karolewski](https://www.linkedin.com/in/lukaszkarolewski/).

“When performing prompt engineering, it is not enough to test just the prompts in isolation, sometimes we need to test multiple prompts chained together using the orchestration frameworks like [LangChain](https://thenewstack.io/benchmark-llm-application-performance-with-langchain/),” they wrote this week.

Enter [Jupyter Notebooks](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/). Now most of you are probably familiar, but just in case, Jupyter Notebooks are interactive web applications that let users create and share documents that can contain code, equations, visualizations, etc.

“To validate ideas effectively, a very tight feedback loop was necessary to allow for real-time collaboration and iteration,” Prakash and Karolewski wrote. “To achieve this, we adopted a unique prompt engineering process leveraging Notebooks, which broke down barriers between technical and non-technical team members.”

In the article, published Thursday on the site, they explained how Jupyter Notebooks is a reusable solution that “allows engineers to quickly set up custom prompt engineering playgrounds for their use-cases along with test datasets.”

Jupyter Notebooks are also accessible to non-technical users, “making prompt engineering inclusive and user-friendly,” they wrote.

The engineers also noted the challenges LinkedIn faced when trying to deploy large language models in production.

## Tutorial Explores Microfrontends with Angular
[Angular](https://thenewstack.io/angular-documentary-debuts-with-star-studded-cast-of-devs/) does not *officially* support [microfrontends](https://thenewstack.io/4-lessons-learned-from-building-microfrontends/), but this week, Angular developer, trainer and consultant [Manfred Steyer](https://github.com/manfredsteyer) wrote a detailed look at [how to implement them with Angular using Native Federation](https://blog.angular.dev/micro-frontends-with-angular-and-native-federation-7623cfc5f413).
Steyer created Native Federation, a community project built upon web standards that provide close integration with the Angular CLI.

“To fully decouple the idea of Federation from specific bundlers, I started the project Native Federation several years ago,” Steyer explained. “[Native Federation](https://www.npmjs.com/package/@angular-architects/native-federation) wraps any bundler and communicates with them via an adapter.”

The focus is on portability and standards like ECMAScript modules and Import Maps, he added.

He explores [how to use Native Federation with Module Federation](https://www.angulararchitects.io/blog/combining-native-federation-and-module-federation/) to create a “bridging solution” that can used to integrate Micro Frontends built with Angular’s web pack-based builder. [Module Federation](https://module-federation.io/) is a solution that enables lazy loading and dependency sharing, he explained.

“Native Federation builds on these concepts with a focus on standards and portability,” Steyer stated. “It provides a seamless integration into the Angular CLI and its performant esbuild-based ApplicationBuilder, which is also the foundation for advanced features like SSR and hydration.”

ApplicationBuilder was introduced in Angular version 17 and was designed to offer a faster, streamlined build process.

Steyer actually begins the article with useful exploration of the pros and cons of Microfrontends.

“Microfrontends promise significant advantages for enterprise-scale applications, such as enhanced team autonomy and independent deployment,” he wrote. “These benefits make this architectural style particularly appealing in multi-team corporate environments where streamlined communication and rapid development cycles are critical.”

But, he added, there are trade-offs such as an inconsistent UI/UX, increased load times, and complex runtime integrations.

“Furthermore, [frameworks like Angular](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/), designed for compile-time optimization, face limitations in runtime integration scenarios,” he cautioned. “The Angular team, therefore, recommends alternatives such as splitting an application into libraries managed within a monorepo, which aligns better with Angular’s strengths in type safety and efficient compilation.”

*Do you have Developer News or a story idea to share? Drop us a line.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)