[Aspire](https://aspire.dev/), Microsoft’s open source, cloud native development platform, now supports [JavaScript](https://thenewstack.io/introduction-to-javascript/), [TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/), [Python](https://thenewstack.io/what-is-python/), and [Java](https://thenewstack.io/java-developers-get-multiple-paths-to-building-ai-agents/) as first-class citizens.

“With Aspire 13, JavaScript and TypeScript developers get to join the party — and I’m not talking about some half-baked afterthought integration,” wrote Microsoft Senior Software Engineer [David Pine](http://linkedin.com/in/dpine) on [Microsoft’s developer blog](https://devblogs.microsoft.com/aspire/aspire-for-javascript-developers/). “This is first-class, full-featured support for orchestrating your JavaScript apps in distributed systems.”

The tool was previously called .Net Aspire, but .Net has been dropped since Aspire is a polyglot.

The code-first orchestration platform is used to build, debug, and deploy distributed applications, such as cloud native apps or [microservices](https://thenewstack.io/introduction-to-microservices/).

[Aspire provides a set of curated components and tooling](https://thenewstack.io/microsofts-net-aspire-the-spring-boot-of-net-development/), including a developer dashboard. Its goal is to simplify starting, building, and running [cloud native applications](https://thenewstack.io/the-api-gateway-and-the-future-of-cloud-native-applications/).

Pine explains how to run [JavaScript](https://thenewstack.io/introduction-to-javascript/) code in three different scenarios, including [Node](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/) and [Vite](https://thenewstack.io/how-vite-became-the-backbone-of-modern-frontend-frameworks/).

## Rust 1.93.0 upgrades musl C library

Rust released version 1.93.0 this week. The big news here is that it upgrades the version of the musl C library used when building certain Linux apps.

This ”should make portable Linux binaries that do networking more reliable, particularly in the face of large [DNS records](https://www.cloudflare.com/learning/dns/dns-records/) and recursive nameservers,” according to the [Rust blog about version 1.93.0](https://blog.rust-lang.org/2026/01/22/Rust-1.93.0/).

That translates into apps that will be more stable when running in [Kubernetes](https://thenewstack.io/cncf-kubernetes-is-foundational-infrastructure-for-ai/), [Docker](https://thenewstack.io/dockers-sets-free-the-hardened-container-images/), or complex cloud environments where DNS records are large and complex.

If you have a previous version of Rust installed via [rustup](https://rust-lang.org/tools/install/), you can update to 1.93.0 with:

`$ rustup update stable`

## A hackathon for useful applications

Are you working on a side project that’s especially useful and an actual application — not just a demo?

If so, you might want to submit it to the [Proof of Usefulness Hackathon](https://hackernoon.com/proof-of-usefulness-hackathon-win-%24100k-from-bright-data-neo4j-algolia-storyblok-and-hackernoon), which runs each month until June 5. It’s “a global developer competition that rewards one thing and one thing only: Real-world usefulness,” according to HackerNoon.

What’s interesting about this hackathon is that it will offer monthly rewards and recognition for more than 40 winners over the next six months. Every two months, there will be major software prize cycles for top startups. There’s also $1,500 worth of inventory for each participant.

The hackathon is open to individual developers and budding startups. It provides access to free tools that help you build and promote something meaningful.

While any technology is welcome, the bigger prizes will go to AI and [machine learning (ML)](https://thenewstack.io/ditch-python-5-javascript-libraries-for-machine-learning/) projects that use the sponsor technologies. This week, the site explained [how to enter the event](https://hackernoon.com/how-to-enter-the-proof-of-usefulness-pou-hackathon), which is a bit of a process.

The event is sponsored by HackerNoon, [Bright Data](https://brightdata.com/?utm_content=inline+mention), [Neo4j](https://thenewstack.io/try-a-neo4j-graph-database-right-here-right-now/), [Storyblok,](https://thenewstack.io/frontend-or-backend-where-full-stack-devs-spend-their-time/) and [Algolia](https://thenewstack.io/algolia-takes-app-search-new-places/).

## Benchmark AI models your way

[Kaggle](https://thenewstack.io/where-do-data-practitioners-prefer-to-collaborate-github/), a [Google](https://cloud.google.com/?utm_content=inline+mention)-owned online AI developer community, recently launched a new [feature that lets you create custom benchmarks](https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-community-benchmarks/) for evaluating AI models.  
The feature is called [Community Benchmarks](https://www.kaggle.com/benchmarks?type=community) for its Benchmarks platform. It can be used to design, run, and share the custom AI model benchmarks.

Here’s why it matters: AI is evolving so rapidly that it’s become difficult to evaluate model performances, according to a [blog post](https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-community-benchmarks/) by [Michael Aaron](https://www.kaggle.com/develra), a Kaggle software engineer, and [Megan Risdal](https://www.linkedin.com/in/megan-risdal-4617812a/?originalSubdomain=ca), a product lead for Kaggle.

“Not long ago, a single accuracy score on a static dataset was enough to determine model quality,” Aaron and Risdal write. “But today, as LLMs evolve into reasoning agents that collaborate, write code, and use tools, those static metrics and simple evaluations are no longer sufficient.”

Among the features of Community Benchmarks:

* **Custom task construction** lets developers define tasks for code execution, tool use, and multiturn conversations using the new [kaggle-benchmarks SDK](https://github.com/Kaggle/kaggle-benchmarks).
* **State-of-the-art model access** to run custom benchmarks against models from Google, Anthropic, and DeepSeek for free, within a quota.
* **Audit-ready reproducibility** means the framework captures full inputs, outputs, and model interactions, replacing anecdotal testing with verifiable data.
* **Dynamic leaderboards** so developers can group multiple tasks into a single benchmark to generate comparative rankings across a suite of leading models.

The [Kaggle Benchmarks repo](https://github.com/Kaggle/kaggle-benchmarks) has [examples of prebuilt tasks](https://github.com/Kaggle/kaggle-benchmarks/tree/ci/documentation/examples).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)