Open source software developer [Matteo Collina](https://github.com/mcollina), a member of the Node.js Technical Steering Committee, has a question for you: Why aren’t you updating Node.js?

And why, for pity’s sake, are downloads of the unsupported Node 12 growing when Node 20 is already in maintenance mode?

“Node 12 over there, you see the red one is rising this, I have no clue,” said Collina, pointing to a graph that, indeed, showed Node 12 downloads increasing. This drew nervous laughter. “Anyway, you’re not updating Node, are you? Why are you not updating it? … [Node 24](https://nodejs.org/en/blog/release/v24.0.0) is going to be the new Active LTS; please, guys, update.”

Active LTS, or long-term support, means that the version is actively maintained and receives regular updates for a longer period than regular releases.

Collina created the [Fastify framework](https://thenewstack.io/introducing-fastify-speedy-node-js-web-framework/) and is also the co-founder and CTO of [Platformatic.dev](https://platformatic.dev/), a cloud native platform built to simplify Node.js development. He offered a State of Node.js report to update developers about Node.js, a popular cross-platform runtime that lets developers execute JavaScript code outside the browser. He made his remarks at this month’s [JSNation](https://jsnation.com/), a hybrid event held in Amsterdam.

The [Node Package Manager (NPM)](https://www.npmjs.com/) and [Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) are two sides of the same coin, he began. The [NPM](https://thenewstack.io/npm-security-woes-continue-amidst-a-series-of-cdn-attacks/) is the most popular open source registry out there for things to download, he said.

“Modular usage is growing more or less 50% every year, and it doubles every two years,” he said. “You’re downloading a lot of modules, guys, I don’t know. It’s not going down.”

Node.js downloads alone were 271 million in December of 2024 and in May, that number was 375 million downloads for the month, he said.

“I have no clue why, first of all, you’re not updating Node.js,” he said.

Node 18 went out of support in April, but a huge number of people are still using it — in fact, it was downloaded 50 million times in May, he noted.

The data also showed that developers tend to skip a version when they do update.

“This is Node 16, okay, going down — still downloaded, I don’t know, 30 million times per month,” he said. “Sorry guys, I’m flabbergasted. … You see that not a lot of people are jumping from Node 16 to Node 20 straightaway.”

[![Matteo Collina discusses the downloading of older versions of Node.js at this month's JSNation.](https://cdn.thenewstack.io/media/2025/06/bc38eba7-flabberghasted_node.jpg)](https://cdn.thenewstack.io/media/2025/06/bc38eba7-flabberghasted_node.jpg)

Matteo Collina discusses the downloading of older versions of Node.js at this month’s [JSNation](https://jsnation.com/). Screenshot via JSNation presentation.

That lead to his pitch for why you should update Node.js: In a word, [security](https://thenewstack.io/nodejs-interactive-security/).

“The Node project works very hard to keep you all safe and give you a nice security release every quarter. Do you like our security releases? Maybe, probably not,” he said. “Okay, we don’t like them either, but we live in this world.”

[Alpha Omega](https://alpha-omega.dev/), a Linux Foundation project, provides some of the funding for Node.js to maintain its security posture, he said. Previously, those funds were around $300k, but in 2025, the funding was cut in half to $150k, he added.

## Node.js Updates

Node now has `require()` ESM — it works out of the box, so you can load ES Modules in a CommonJS context, thus improving interoperability between CommonJS and ESM in a Node.js application.

Related to that, if you’re using the latest version of Node.js, .mjs is not needed anymore. .mjs was used to explicitly indicate that a JavaScript file should be treated as an ECMAScript Module. Now, developers can just run it and it works without using .mjs.

“Nobody liked that […] script,” he said. “So you can just run it and it just works.”

Another big change: TypeScript now runs out of the box, which Collina attributed to the work of [Marco Ippolito](https://github.com/marco-ippolito), a senior security engineer at HeroDevs and member of the Node.js Technical Steering Committee.

They hope to have that as a flag on Node 22 and stable by Node 24, he added.

There were also changes in V8 that allowed the Node team to improve the performance of open telemetry tracing by roughly 7%, he said. [V8](https://v8.dev/) is Google’s open source, high-performance JavaScript and WebAssembly engine that’s written in [C++](https://thenewstack.io/bjarne-stroustrup-on-how-he-sees-c-evolving/). It’s the engine that powers Node.js.

“It also made a lot of things based on async local storage significantly faster,” Collina said. “There [are] a lot of new things coming thanks to that.”

Last, he talked about using [explicit resource management](https://github.com/tc39/proposal-explicit-resource-management), which is a new feature of the TC39 that provides a [structured way to manage the lifecycle of resources](https://dev.to/zacharylee/explicit-resource-management-in-js-the-using-keyword-d9f#) like file handles or network connections. Resources are automatically deallocated, which means the resources are automatically cleaned up as soon as the code block using them is exited, even if an error occurs.

“You can do, essentially a finalizer or a deallocation when you exit the scope,” he said. “It already works for timers and other APIs on Node 24, but we plan on adding this through all of them. Why is this useful? Because, essentially, you will be able to use a file or use a stream, and those will be automatically deallocated and cleaned up correctly, especially if there is a native resource underneath. And it’s also worth sync and async. So it’s pretty great.”

That addresses a long-standing challenge in JavaScript, which was tricky, especially with asynchronous operations. There was the possibility that an error occurring before the developer explicitly closed the resource might lead to it remaining open, which in turn led to leaks. JavaScript’s automatic garbage collection did not clean up these non-memory “native resources” like file descriptors.

By allowing resources to be automatically deallocated when their scope is exited — whether the code finishes normally or there’s an error — the explicit resource management feature provides a reliable cleanup mechanism for both sync and async operations.

## Watt: A Node.js Application Server

Collina also talked about an [application server for Node.js](https://blog.platformatic.dev/introducing-the-node-application-platform) that he released last year on the Platformatic.dev platform. The server, called Watt, makes applications enterprise-grade out of the box, he said.

“It runs your application in its streamlined multi-threading, running multiple Node.js applications within the same thread, within the same process, using threading and standardizing probe, logs, metrics, open telemetry and so on and so forth,” he said.

This allowed Node.js to do a few good things, he added — like run PHP.

It was possible to run [PHP on Node.js before,](https://medium.com/@MartinMouritzen/how-to-run-php-in-node-js-and-why-you-probably-shouldnt-do-that-fb12abe955b0) but now PHP inside Node.js runs as a native add-on on a separate thread, he said.

“You could essentially create a single process in which you have your Next.js application and your PHP application,” he said. “How does it work? It runs PHP on a separate thread, and in that way, it can block and do all those things.”

The main reason to support PHP is that people want to run PHP and still have [headless mode](https://thenewstack.io/maximizing-headless-architecture-a-guide-for-developer-teams/), he told the audience.

“I was working on such an application in, I think, 2017 with a very popular newspaper using WordPress for editing, and then [they] wanted to use React for their [frontend](https://roadmap.sh/frontend),” he said. “There’s a lot of software built in PHP these days that probably is not going away anytime soon.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)