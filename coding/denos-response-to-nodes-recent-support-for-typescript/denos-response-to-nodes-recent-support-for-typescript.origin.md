# Deno’s Response to Node’s Recent Support for TypeScript
![Featued image for: Deno’s Response to Node’s Recent Support for TypeScript](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
[Node now supports TypeScript](https://github.com/nodejs/node/blob/main/doc/api/typescript.md), which will bring it more in line with the alternative runtimes [Deno](https://deno.com/?utm_content=inline+mention) and [Bun](https://thenewstack.io/bun-1-0-ships-as-node-js-and-deno-alternative/), which offer native [TypeScript](https://thenewstack.io/what-is-typescript/) support. TypeScript allows developers to define data types, which supports early error detection and prevents runtime issues that are common in [JavaScript](https://thenewstack.io/three-javascript-proposals-advance-to-stage-4/).
“Basically, TypeScript adds additional syntax to JavaScript to support a tighter integration with your editor,” Node wrote. “[It can] Catch errors early in your editor or in your CI/CD pipeline, and write more maintainable code.”

Native TypeScript support was among the [most requested Node features developers have requested](https://www.infoq.com/news/2025/03/node-23-runs-typescript-natively), according to InfoQ. It was added as [experimental last August](https://nodejs.org/en/blog/release/v22.6.0#experimental-typescript-support-via-strip-types), but has been enabled by default since January.

TypeScript offers other benefits to Node, including static typing, which is when the type of a variable is known and is checked at compile time before the program is executed. Adding types to JavaScript helps structure code as a project grows, according to a [Deno blog post responding to the news](https://deno.com/blog/typescript-in-node-vs-deno). It was written by Deno’s creator [Ryan Dahl](https://github.com/ry) and product marketing manager [Andy Jiang](https://www.linkedin.com/in/andyjiang/).

It primarily handles two tasks, they noted:

- Type checking, to ensure your variables match declared types.
[Type stripping, for transpiling](https://nodejs.org/api/typescript.html#type-stripping). In TypeScript, developers can add type annotations to their code to improve readability and catch potential errors.
Type stripping is the process of removing these type annotations, typically during a build process. It’s often done when converting code from a language with type annotations (like TypeScript) to a language without them (like plain JavaScript). Transpilers take source code written in one programming language and convert it into source code in another programming language.

Deno explained how the [Node](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) integration worked.

“This essentially integrates functionality previously provided by ts-node directly into Node, simplifying TypeScript execution,” they wrote. “Node’s TypeScript support replaces type annotations with whitespace, resulting in valid JavaScript…”

That said, Dahl and Jiang pointed out there are limitations to this approach including:

- No built-in type checking, which means external tools like tsc are still required.
- No JSX or TSX support: “Node handles .ts, .mts, and .cts, but React (.tsx) and JSX projects still require external transpilers or bundlers such as esbuild, Babel, or tsc,” they wrote.
- Manual management of tsconfig.json: “Type checking still relies on external configuration via tsconfig.json,” they added. Node.js ignores tsconfig.json files, according to InfoQ.
They contrasted this with how [Deno](https://thenewstack.io/deno-creates-board-charter-for-javascript-registry-project/) approaches the problem.

“[Deno simplifies web programming](https://thenewstack.io/ryan-dahl-from-node-js-and-deno-to-the-modern-jsr-registry/) by providing a single executable with a fully integrated TypeScript toolchain,” Dahl and Jiang wrote. “This approach offers TypeScript’s benefits with minimal configuration, streamlining testing, formatting, and compilation workflows.”

[Deno’s TypeScript](https://thenewstack.io/how-oop-developers-can-get-to-know-typescript-through-deno/) integration is composed of three main parts:
- Execution:
[Google’s V8](https://thenewstack.io/node-js-v8-gets-long-term-support-plus-commitment-google-v8/)engine executes JavaScript but not TypeScript directly. - Type checking:
[Microsoft’s TypeScript](https://thenewstack.io/typescript-5-5-faster-smarter-and-more-powerful/)compiler, implemented in JavaScript, is internally bundled. - Type stripping: SWC, a high-performance parser built in
[Rust](https://thenewstack.io/rust-programming-language-guide/), efficiently strips types without running JavaScript.
They added that TypeScript is supported across Deno’s toolchain.

## Nuxt.js Adds Lazy Hydration
[Nuxt.js](https://thenewstack.io/how-to-build-a-quiz-app-with-nuxt-and-xata/) version 3.16 adds support for native delayed/lazy hydration support, which lets developers control exactly when components hydrate. Nuxt is an open source web application framework built upon Vue, an open source JavaScript framework used for building user interfaces.
[Lazy hydration can improve initial load performance](https://nuxt.com/blog/v3-16) and time-to-interactive, wrote [Daniel Roe](https://github.com/danielroe), who leads the Nuxt core team.
Nuxt already offers the [Islands architecture](https://www.patterns.dev/vanilla/islands-architecture/#:~:text=Thus%20it%20provides%20built%2Din,on%20when%20they%20become%20visible.&text=It%20also%20supports%20lazy%20hydration,the%20hydration%20of%20the%20component), which defines which parts of the page are static and which are interactive parts. Lazy hydration is about controlling the timing of when those interactive parts become active. The two are often used in conjunction since lazy hydration can optimize the hydration of individual “islands.”

The update also includes other features and performance enhancements.

For instance, Nuxt has simplified starting projects with the framework with create-nuxt, a new tool for starting Nuxt projects.

“It’s a streamlined version of nuxi init — just a sixth of the size and bundled as a single file with all dependencies inlined, to get you going as fast as possible,” Roe wrote.

Now, a new project can be started with:
`npm create nuxt`

The Nuxt team also made a number of performance improvements, such as:

- Using exsolve for module resolution along with the rest of the unjs ecosystem (nitro, c12, pkg-types, and more), which “dramatically” speeds up module resolution, Roe said;
- Smarter module resolution paths, which prioritize direct imports for better efficiency;
- Eliminated duplicated Nitro alias resolution for leaner file handling, and
- Streamlined
`loadNuxt`
by skipping unnecessary resolution steps for faster startups.
“To add some anecdotal evidence, my personal site at [roe.dev](https://thenewstack.io/goodbye-saas-hello-ai-agents/) loads 32% faster with v3.16, and Nuxt.com is 28% faster,” Roe wrote. “I hope you see similar results!”

## Google Rolls Out Gemma 3, New AI Safety Checker
Google introduced [Gemma 3](https://developers.googleblog.com/en/introducing-gemma3/), a collection of lightweight open models, this week. Gemma 3 is built with the same research and technology as the Gemini 2.0 models.

Google’s DeepMind Vice President of Research [Clement Farabet](https://www.linkedin.com/in/clementfarabet/) and Director [Tris Warkentin](https://www.linkedin.com/in/triswarkentin/) [introduced the models in a blog post](https://blog.google/technology/developers/gemma-3/) published Wednesday.

“They are designed to run fast, directly on devices — from phones and laptops to workstations — helping [developers create AI applications](https://thenewstack.io/top-strategies-for-building-scalable-and-secure-ai-applications/), wherever people need them,” Warkentin and Farabet wrote.

The [Gemma models are open sourced](https://thenewstack.io/the-open-source-ai-definition-is-out/) and provided with open weights. Gemma 3 comes in these sizes: 1B, 4B, 12B and 27B.

[Smaller language models are becoming more popular](https://thenewstack.io/why-red-hat-thinks-ais-future-is-small-language-models/) as more organizations start to build out their own AI applications and AI agents.
Google also launched [ShieldGemma2](https://developers.googleblog.com/en/safer-and-multimodal-responsible-ai-with-gemma/), which is a 4B image safety checker built on the Gemma 3 foundation.

“ShieldGemma 2 provides a ready-made solution for image safety, outputting safety labels across three safety categories: dangerous content, sexually explicit and violence,” the post stated. “Developers can further customize ShieldGemma for their safety needs and users.”

Academic researchers may want to take note that Google is also offering the Gemma 3 Academic Program, which allows academic researchers to apply for Google Cloud credits (worth $10,000 per award) to accelerate their Gemma 3-based research. The [application process opened this week](https://ai.google.dev/gemma/), and will remain open for four weeks.

## OpenAI Releases Developer Tools for Building AI Agents
[OpenAI released the “first set of building blocks”](https://openai.com/index/new-tools-for-building-agents/) to help developers build agents more effectively on its platform. AI agents are defined as AI-enabled systems that can independently automate a task.
“Over the past year, we’ve introduced new model capabilities — such as advanced reasoning, multimodal interactions, and new safety techniques — that have laid the foundation for our models to handle the complex, multistep tasks required to build agents,” OpenAI’s team wrote in announcing the news. “However, customers have shared that turning these capabilities into production-ready agents can be challenging, often requiring extensive prompt iteration and custom orchestration logic without sufficient visibility or built-in support.”

To support the development of AI agents, this week the company released a new [Responses API](https://community.openai.com/t/introducing-the-responses-api/1140929), which “combines the simplicity of the Chat Completions API with the tool use capabilities of the [Assistants API](https://platform.openai.com/docs/api-reference/assistants) to enable developers to build the core logic of agents,” OpenAI explained.

Tools built into the API include web search using the same underlying model that powers ChatGPT’s search, file search, and computer use with the same underlying model powering Operator. OpenAI added that this gives AI agents access to the information and tools they need to be useful.

There’s also a new [Agents SDK](https://platform.openai.com/docs/guides/agents-sdk) to orchestrate single-agent and multi-agent workflows, as well as integrated observability tools to trace and inspect agent workflow execution.

For more, developers can check out this [video of a live stream](https://openai.com/live/) with some of the team members who worked on the tools.

## New York Times Migrates from Enzyme into React Testing Library
[The New York Times published a mini-case study](https://open.nytimes.com/how-the-new-york-times-systematically-migrated-from-enzyme-into-react-testing-library-b3ea538d001c#225:%20React%20Router) of its biggest challenge in upgrading its core site’s [React](https://thenewstack.io/a-react-based-open-source-tool-for-creating-data-tables/) library from React 16 to React 18.
It turns out that one of the biggest problems they faced was transforming their codebase from the Enzyme test utility, a JavaScript testing utility specifically designed for React components, to the [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/).

The React Testing Library is a popular JavaScript testing utility that focuses on testing React components from the user’s perspective. The story explains that there are major differences in unit testing between the two libraries. It details the New York Times upgrade process and includes code samples so developers can see the difference between [Enzyme](https://enzymejs.github.io/enzyme/) and the React Testing Library.

## WordPress Plug-In Vulnerability Discovered
[Word Fence discovered a vulnerability](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/all-in-one-wp-migration/all-in-one-wp-migration-789-unauthenticated-php-object-injection) in the All-in-One WP Migration and Backup plugin — a plugin with over 5 million installations, according to [SearchEngine Journal](https://www.searchenginejournal.com/wordpress-backup-plugin-vulnerability-affects-5-million-websites/541952/). The high-severity vulnerability was discovered and patched.
“The way this kind of vulnerability works is that the WordPress plugin processes potentially malicious data during backup restoration without properly verifying it,” reported SearchEngine Journal. “But because there’s a narrow attack opportunity, it makes exploiting it less straightforward.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)