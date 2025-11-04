Things are changing over at [Lodash](https://github.com/lodash/lodash) and the [project is starting a new chapter](https://blog.ulisesgascon.com/the-future-of-lodash), according to [Ulises Gascón](https://github.com/ulisesgascon), who is a member of the Express Technical Committee, a [Node.js](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/) core collaborator and releaser, and a TC39 delegate.

Lodash is a popular open source JavaScript utility library that provides helpful, efficient and consistent functions for common programming tasks. It simplifies working with core JavaScript data structures, such as arrays, objects, numbers and strings. More than 9.3 million live websites use it, including a third of the top 10,000 global sites, and npm downloads exceed 2.57 billion per week, according to the [OpenJS Foundation](https://openjsf.org/).

“Lodash has been a cornerstone of JavaScript development since 2012 and has a massive reach,” the OpenJS Foundation, which Lodash is under, stated. “It appears in frontend and backend code, cloud functions, CMS platforms, build tools, and CI pipelines.”

Also, many developers depend on it “indirectly through frameworks like React, webpack, and more, making it a critical digital infrastructure that hasn’t always been actively maintained,” the article notes.

The problem is that it’s been maintained by one person: [John-David Dalton](https://www.linkedin.com/in/john-david-d/). Moving forward, the project will transition to a more sustainable model, Gascón said.

“For Lodash to remain viable over time, we need to distribute the decision-making and maintenance workload,” Gascón wrote.

The first step will be to establish a technical governance structure similar to one with a Technical Steering Committee that shares responsibility and seeks consensus-based decisions, he wrote.

The library will also look at deprecating some of the “variants” of the main library, restoring the continuous integration system and improving the security model.

The library’s team will also “adopt the Foundation’s CNA […] to handle incidents and request CVEs [common vulnerabilities and exposures], improve reporting channels via GitHub Advisory and document the process for security releases in an Incident Response Plan, as other projects already do,” Gasćon said.

Also this month, the [Sovereign Tech Agency has commissioned work](https://openjsf.org/blog/sta-supports-lodash) to support the Lodash transition.

## New Changes To Next.js

When Next.js frontend programmers stop the dev server, all their work gets thrown away, and developers must start from scratch in a new dev session. To address this problem, Next.js has a new file system caching for development in beta.

“It extends the memory task tracking of [Turbopack](https://thenewstack.io/next-js-13-debuts-a-faster-rust-based-bundler/) to full server restarts by leveraging the file system, the good old reliable awesome file system,” [Guillermo Rauch](https://www.linkedin.com/in/rauchg/), Vercel CEO and creator of Next.js, said. “This is going to be particularly awesome for the largest projects in the ecosystem.”

The framework is also preparing to better serve AI agents by open sourcing its Next.js evals. This is a problem that many [frameworks are trying to address](https://thenewstack.io/new-open-source-tool-from-angular-scores-vibe-code-quality/) — how to get large language models (LLMs) to reflect best practices for the framework while correcting common mistakes.

“Next evals is a public benchmark that tracks how well the latest models and coding agents can build with Next.js,” Rauch said. “This is an investment into the ecosystem.”

## TanStack Start Hackathon Underway

[TanStack Start](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/) is offering $140,000 in cash, prizes and credits to the [winners of its hackathon](https://www.convex.dev/hackathons/tanstack).

First place will win $5,000, plus $100,000 in Cloudflare credits; office hours with the creator of TanStack, [Tanner Linsley](https://www.linkedin.com/in/tannerlinsley); TanStack merch and sticker pack; CodeRabbit credits and swag; 3 months free to the FireCrawl growth plan; 6 months Convex Pro; Netlify credits; and Convex swag.

Second place will get $3,000, plus $25,000 in Cloudflare credits; CodeRabbit credits and swag; 3 months free to the FireCrawl growth plan; Netlify credits; and Convex swag.

Finally, third place will be awarded $2,000, plus $5,000 in Cloudflare credits; CodeRabbit credits and swag; 3 months free to the FireCrawl growth plan; Netlify credits; and Convex swag.

You’ll find a list of judges and resources available on the announcement page. The build requirements are pretty straightforward. The app must be started on or after Oct. 29. It must use TanStack Start, Convex, CodeRabbit, Firecrawl and [Cloudflare](https://thenewstack.io/cloudflare-for-ai-helps-businesses-safely-use-ai/).

“Build something that shows what TanStack Start can really do with rich interactivity, live updates, server streaming, collaborative tools, full-stack routing, and RPCs with Convex, CodeRabbit, Firecrawl, Netlify, Autumn, and Cloudflare,” the team wrote on the announcement.

The event started on Thursday and runs through Nov. 17, with application submissions due at 12 p.m. PT. The winners will be announced Nov. 24. [Registration is open](https://luma.com/tanstackstarthackathonv1).

## Deno Deploy Is Rebuilt

Deno Deploy, a serverless cloud platform for building, deploying and scaling modern web applications and edge functions, has gotten a rebuild from scratch, according to [Phil Hawksworth](https://github.com/philhawksworth), who heads developer relations at Denoland. [Deno is a JavaScript runtime](https://thenewstack.io/deno-2-0-angular-updates-anthropic-for-devs-and-more/).

The updated version has undergone an early access program and is ready for use, Hawksworth added.

Among the updates included in the new version:

* Integrated CI/CD, so you can run your builds within Deno Deploy or on your own CI/CD.
* Easy on-ramp for working with data means developers can start with [KV](https://deno.com/kv), then easily graduate to a full database when necessary.
* Postgres. ”We’ve made it simple to link and provision databases from third-party database providers to your applications in ways that make sense for how developers work with code,” Hawksworth wrote. ”Our database integrations do some work behind the scenes to create database instances for each of your development and production contexts. That means that you can provision or allocate a database to one of your applications, and get separate databases for each environment.”
* More metrics, with out-of-the-box support for data and analytics on all apps. It also supports automatic observability with built-in support for OpenTelemetry.

Another goal was to make Deno Deploy easier to try, and to support that, Deploy now automatically applies integrations and presets according to your project code.

## Vercel Releases Workflow Development Kit, Agent Investigations

Last week, Vercel hosted its Next.js conference, with news about how the [Next.js framework is evolving](https://thenewstack.io/how-next-js-got-its-snappy-client-navs-back/).

The frontend infrastructure company also introduced a new [Vercel Workflow Development Kit](https://vercel.com/blog/introducing-workflow), which is a TypeScript framework for building durable, reliable and observable applications and AI agents, the frontend infrastructure company stated. It’s now [available as an open beta](https://vercel.com/changelog/open-source-workflow-dev-kit-is-now-in-public-beta).

It introduces a new execution model for long-running code, Vercel said in its press release. Developers can use two declarative directives inside normal async functions to express where durability should exist:

* “use workflow” ; // defines a durable workflow boundary
* “use step” ; // defines atomic units of work with persistence and retries

“This model gives developers the ability to write code that can survive restarts, deploys, and failures, all without managing queues, schedulers, or databases,” Vercel noted.

WDK eliminates the need to manually configure queues, databases or retries. It’s not a job scheduler or queue library, Vercel clarified, but a “code-level primitive for reliable, resumable execution.”

Its key features are:

* Code-first durability: “Declare how your logic should persist directly in code,” Vercel explained. “Workflows automatically persist progress, retry failures, and resume from the last successful step.”
* Familiar developer experience: The directives integrate into the code a developer has already written, without a YAML file, state machines or orchestration servers.
* Framework-defined infrastructure: When deployed to Vercel, the platform provisions all required infrastructure automatically through framework-defined infrastructure.
* Open source and portable: Workflow can be configured to execute inside different environments.
* Designed for long-running, reliable systems.

The company also launched [Vercel Agents investigations](https://vercel.com/changelog/vercel-agent-investigations-now-in-public-beta), which is a new intelligent monitoring system that automatically detects issues in an application, conducts a root cause analysis and then provides action remediation plans to resolve incidents faster. It’s also available in public beta.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)