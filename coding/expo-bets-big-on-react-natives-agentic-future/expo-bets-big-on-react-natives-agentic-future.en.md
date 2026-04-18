As someone who spent more than six years leading [React](https://react.dev/) at Meta, few are as well-placed as [Seth Webster](https://www.linkedin.com/in/swebster) to assess where the framework fits in an era of AI-assisted development.

At Facebook’s parent company, which open-sourced the React JavaScript library for building user interfaces back in the [halcyon days of 2013](https://www.infoq.com/news/2013/06/facebook-react/), Webster helped guide the framework as it grew into one of the most widely used tools in software development.

Since joining in 2019, he led the React organization through a period of rapid growth, and with [Meta moving React to its own foundation](https://thenewstack.io/react-foundation-open-source-governance/) under the Linux Foundation – where he now serves as executive director – Webster quietly left the company around December to join [Expo](https://expo.dev/), an open source platform built on [React Native](https://reactnative.dev/) that aims to simplify mobile app development.

![React Foundation executive director Seth Webster is now developer evangelist for Expo](https://cdn.thenewstack.io/media/2026/04/cc618f67-seth-full-headshot-1024x576.jpg)

*React Foundation executive director Seth Webster is now developer evangelist for Expo (Credit: Expo)*

At Expo, Webster will serve as chief developer evangelist, focusing on growing platform adoption and shaping its direction as AI tools play a larger role in how apps are built and shipped.

To support that push, Expo on Thursday announced a $45 million Series B funding round led by [Georgian](https://georgian.io/), alongside the public beta launch of [Expo Agent](https://agent.expo.dev/), a new system designed to help developers get mobile apps into production using React Native.

In an interview with *The New Stack*, Webster says that while React’s success has made it a central part of modern development, its growing complexity means it is rarely used on its own, with developers instead relying on additional frameworks, often referred to as “meta-frameworks,” to handle things like routing, data fetching, and deployment.

Webster acknowledged a range of long-standing criticisms, from gaps in tooling to inconsistent developer experience across platforms. On the web, he says React has largely been strong in terms of reliability and backward compatibility, while its native counterpart has often moved faster, at times at the expense of reliability – a dynamic that has pushed many developers to rely on additional layers on top of React, rather than using the library on its own.

“When you use a meta-framework, where so much more of that is baked in, then you can focus on the business value you’re creating, or the experience you’re creating,” Webster says. “And that’s why I think the criticisms are entirely justified of React.”

## Agent of change

One of those “layers” is Expo, an open source platform that sits on top of React Native, providing a more complete toolkit for building and deploying mobile applications. The company describes itself as a “full-stack React Native framework,” designed to handle work that the underlying library leaves to developers.

Founded in 2015 by early Facebook engineers and Quora co-founder [Charlie Cheever](https://www.linkedin.com/in/ccheever/), Expo allows developers to bypass the setup and infrastructure typically required to ship apps, including builds, updates, and access to native device features.

Users can write and update code in a development environment while previewing changes instantly on a live mobile interface.

![Expo in action](https://cdn.thenewstack.io/media/2026/04/bd2760f2-generalgif.gif)

***Expo in action (Credit: Expo)***

When React first emerged on the scene more than a decade ago, building software was very much a human-led endeavor. Fast-forward to 2026, and agents are increasingly taking on larger parts of that work, with [tools such as Claude Code](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/) and [Cursor](https://thenewstack.io/cursor-self-hosted-coding-agents/) — alongside a swathe of so-called “vibe coding” platforms — that can build and modify entire applications.

So, does the world need yet another agent? Expo reckons so. The company quietly debuted [Expo Agent in beta in March](https://expo.dev/blog/expo-agent-beta), pitching it as a system designed to help developers move from idea to production-ready mobile apps.

Expo Agent runs in the browser, allowing developers to generate and modify apps from prompts while working directly on a project or repository. It produces native applications for iOS and Android, writing platform-specific code where needed, and ties into Expo’s build system to generate installable binaries and app store submissions.

![Expo Agent in the browser](https://cdn.thenewstack.io/media/2026/04/30b01523-agentexpoz-1024x825.png)

***Expo Agent in the browser (Credit: Expo)***

Rather than stopping at initial code generation, the system is designed to continue through common points of failure, handling configuration, dependencies, and native integrations as they arise. It also keeps developers in a tight feedback loop, where code can be updated and tested on a live app in real-time.

Projects remain standard Expo apps, allowing developers to export the code, connect to version control, or continue development outside the hosted environment.

![Expo Agent in action](https://cdn.thenewstack.io/media/2026/04/eca4f981-gif1.gif)

***Expo Agent in action (Credit: Expo)***

Under the hood, Expo Agent is powered by Claude Code, but tuned around Expo’s own ecosystem, including its build pipeline and platform APIs.

Expo CEO and co-founder Charlie Cheever notes that the main issue with agentic app development today is that “business critical apps are not making it to production.” In a statement issued to *The New Stack*, he added that many tools fall short when it comes to moving beyond initial code generation and into fully deployed applications.

“That is the problem we are positioned to solve at Expo,” Cheever says. “We built the infrastructure for mobile apps, and we can bake that infrastructure into Expo Agent. Our mission is to give every builder — whether they’re a solo founder, an enterprise team, or someone working alongside AI agents — the infrastructure to ship production-grade apps that scale and succeed.”

> “We built the infrastructure for mobile apps and we can bake that infrastructure into Expo Agent.”

## React in real time

The convergence of AI agents and frameworks like React Native raises a broader question: as more of the development process is handed over to machines, where do those underlying frameworks fit?

For Webster, the answer lies in how those systems actually work.

“You still need something for the computers to parse and render,” he explains, adding that large language models (LLMs) are well-suited to declarative systems such as React, where developers describe what an interface should do rather than spelling out every step.

That alignment also has implications for cost. Webster pointed out that maintaining a single codebase across iOS, Android, Windows, and macOS can reduce the work AI systems need to do, particularly as the cost of running them begins to change.

“If you’re having to do five codebases with your agents versus one, I think that you’re going to start feeling that AI for you can be really expensive,” Webster says.

> “If you’re having to do five codebases with your agents versus one, I think that you’re going to start feeling that AI for you can be really expensive.”

While the cost of running large models is currently artificially low, buoyed by heavy venture funding and aggressive pricing from companies competing for market share, he suggests that this dynamic is unlikely to last, making efficiency — and by extension cross-platform approaches like React Native — more relevant over time.

“You can spend fewer tokens – the cost per token is currently in a super-subsidized place,” Webster says.

## A clean break

Webster’s move to Expo, after more than six years at Meta, coincided with React’s move to an independent foundation under the Linux Foundation, a transition he says had been in the works for some time.

“I’ve been working on getting this thing pulled out into a foundation for four years,” he says.

He added that he pushed the powers that be at Meta to complete the transition before leaving, with the company ultimately supportive of the move, allowing him to focus on finalizing the shift in the final months of 2025.

> “We’re at a moment where the React Native ecosystem is expanding faster than ever.”

With that process complete, Webster says he was ready to step away and focus more directly on helping developers turn ideas into working software — something he sees Expo as well positioned to support.

“This has really been my North Star all along, but I wasn’t able to focus on it as much – and that’s helping others bring their ideas to life,” he says.

Expo, for its part, is betting that demand for those tools will continue to grow, and with a fresh $45 million in the bank, the company says it will use the funding to expand its platform and continue developing products such as Expo Agent, as it looks to shorten the path from idea to production-ready apps.  
At the same time, React Native is seeing renewed momentum as AI tools begin to reshape how mobile apps are built.

“We’re at a moment where the React Native ecosystem is expanding faster than ever, fueled by AI-assisted development, new enterprise entrants, and a global community pushing the boundaries of what’s possible on mobile,” Webster says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)