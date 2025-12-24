[Shuttle](https://www.shuttle.dev/) is a Rust-first, open source Infrastructure as Code (IaC) cloud platform for deploying apps. This week, the company launched Neptune, a new offering to speed up application deployments.

While developers can generate entire backends in minutes, it still can take days of setup and configuration to deploy the app. This is where Neptune, now in beta, comes into play. Neptune is an “AI platform engineer” that’s fully language-agnostic and connects to any repo or AI coding tool. The [blog post](https://www.neptune.dev/blog/introducing-ai-platform-engineer) compares it to Docker for backend infrastructure.

“It’s an AI-native platform engineer that understands your code, knows what it needs, and provisions the full cloud stack — safely, predictably, and fast,” the company said in a blog post. “It evolves from a deployment helper into a true AI platform engineer that understands your code, plans intelligently, and provisions infrastructure automatically.”

It integrates with IDE copilots and agents for fully conversational deployments, the post adds. It is also cloud-agnostic and extensible, supporting AWS, GCP and Azure through a plugin model.

Neptune provides the simplicity of a PaaS but lets developers bring their own cloud account. It also offers the flexibility of IaC but eliminates the maintenance cycle, the post added.

“Because your infrastructure is a deterministic spec, it’s always up-to-date with your code — not lagging behind it,” the team stated. “This delivers near-zero maintenance overhead and collapses the gap between code and cloud.”

Neptune works by connecting three components into one cohesive system: a deterministic specification, a Kubernetes-native control plane, and an AI workflow grounded in real infrastructure metadata, the post stated. The three together turn application intent into production-ready cloud architecture with minimal configuration.

The [Neptune beta is open](https://www.neptune.dev/try-it-now) to early builders.

## Vulnerabilities Found in React Server Components

[Two more vulnerabilities](https://thenewstack.io/react-server-components-vulnerability-found/) — one that makes it possible to mount a denial of service attack — in [React Server Components were identified](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components) by security researchers this week, according to the React blog.

The new problems include a high-severity denial-of-service vulnerability and a medium-severity source code exposure issue. The [React](https://thenewstack.io/stop-blaming-react-for-your-state-management-hangover/) team recommended developers upgrade immediately. What’s more, if you already updated for the Critical Security Vulnerability last week, you will need to update again, the team warned.

“If you updated to 19.0.2, 19.1.3, and 19.2.2, these are incomplete and you will need to update again,” the team said.

If your app’s React code does not use a server, then the app is not affected by these vulnerabilities, the React team added. Apps are also unaffected if they do not use a framework, bundler, or bundler plugin that supports React Server Components.

The following React frameworks and bundlers are affected: Next.js, React Router, Waku, @parcel/rsc, @vite/rsc-plugin, and rwsdk.

## Microsoft Offers Update on TypeScript 7.0 Progress

Daniel Rosenwasser, the principal product manager for TypeScript, recently posted an [update about the language’s efforts](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/) to port the compiler and language service to native code.

This effort — dubbed Project Corsa — will help it take advantage of better raw performance, memory usage and parallelism, he wrote. It will be a big change for TypeScript 7. He also offered a look at the language’s upcoming roadmap.

First, he offered a look at the rewrite of editor support and the language service. The language service is what powers an editor’s TypeScript and JavaScript features, he explained.

While the team is still porting features and fixing minor bugs, he said much of what makes the existing TypeScript editing experience is already there and working, a few of which include:

* Code Completions (including auto-imports)
* Go-to-Definition
* Go-to-Type-Definition
* Go-to-Implementation
* Find-All-References
* Rename
* Formatting
* Call Hierarchy
* Document Symbols

“You might notice a few things that stand out since our last major update – auto-imports, find-all-references, rename, and more,” he wrote. “We know that these features were the missing pieces that held a lot of developers back from trying out the native previews. We’re happy to say that these are now reimplemented and ready for day-to-day use!”

They also rearchitected parts of the language service to improve reliability while also leveraging shared-memory parallelism, he added.

“The new architecture is more robust, and should be able to handle codebases, both big and small, without issues,” he said. “While there is certainly more to port and polish, your team will likely find that trying out TypeScript’s native previews is worth it. You can expect faster load times, less memory usage, and a more snappy/responsive editor on the whole.”

There has also been progress on the compiler in native port.

One question he frequently gets is whether it is safe to use TypeScript 7 to validate a build; that is, does it reliably find the same errors that TypeScript 5.9 does?

“The answer is a resounding yes,” Rosenwasser wrote. “You can confidently use TypeScript 7 today to type-check your project for errors.”

TypeScript 7.0 will not support the existing Strada API, he noted. The Corsa API is still a work in progress and no stable tooling integration exists for it; which means any tools (such as linters, formatters, or IDE extensions) that rely on the Strada API will not work with Corsa.

“The workaround for some of these issues may be to have the typescript and @typescript/native-preview packages installed side-by-side, and use the ≤6.0 API for tooling that needs it, with tsgo for type-checking,” he stated.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)