[Vercel](https://thenewstack.io/creators-of-nuxt-js-and-nitro-join-vercel/) today rolled out a new version of its [v0 AI-driven offering](https://vercel.com/blog/v0-app), changing the name to .app from .dev to reflect its new audience: end users.

“We started v0 with the idea of making the development workflow easier for developers, and we’ve realized over the course of building v0 that, actually, v0 is better suited for everyone,” [Aryaman Khandelwal](https://www.linkedin.com/in/aryamank/), product manager for [Vercel’s v0.app](https://v0.app/), told The New Stack. “The [v0.dev](https://thenewstack.io/frontend-ai-vercel-abstracts-model-chaos-in-one-interface/) to v0.app transition is really our push to make v0 easier to use for people who are nontechnical completely.”

So far, v0 has 3 million users and is producing six and a half apps every second, he told The New Stack — that’s hundreds of thousands of web apps being built in the course of the day.

## Vercel’s Updates To AI Tool

The first change Vercel made was to update the user interface to make it more accessible to people who are not “super developers,” Khandelwal said.

The second change is that v0 can do actions for developers and end users, such as searching the internet or adding integrations, rather than just generating code. It can create a full-stack app, including a reactive UI for the frontend and backend connections such as databases.

“Basically, we think that v0 covers the full set of what you would want to do when you’re building web apps,” he said. “I wouldn’t recommend using v0 for building a pure backend framework that has no UI.”

Although it can do some of that, he added. People have used it to write “really cool APIs” he said, but v0.app’s superpower is really building websites and applications.

The new v0.app can perform:

* **Web search:** It searches the web, handles failures and returns results with citations.
* **File reading:** It reads files and returns their contents.
* **Site inspection:** It inspects live sites, takes screenshots and summarizes findings.
* **Design inspiration:** It generates image concepts with descriptions based on prompts. For example, I just asked it to add a time-themed image to my to-do site and it popped one in. But it also allows the uploading of logos, product information and even brand guidelines, with more features planned in the future to make branding even easier, he said.
* **To-do management:** It tracks tasks, updates plans and outputs technical breakdowns.
* **Work checking:** It spots errors, compares implementations and reasons through results.
* **Integrations:** It supports integration, including the option to add a database from Vercel’s list of hosted options. It can also add other tools, including AI tools such as [Grok](https://grok.com/), which are currently offered by the Vercel marketplace. It also supports third-party API integration so enterprises can connect with their own backend systems if they choose.

## Why Vercel Is Courting Non-Developers

Obviously, this is not a path Vercel originally started on when it rolled out v0.dev, which targeted frontend and [web developers](https://roadmap.sh/roadmaps?g=Web+Development). The first version focused on creating code.

“We know developers. Our market has always been to developers,” Khandelwal said. “We built this to start with as a developer tool. We made it very technical.”

But over the past two years since deployment, he said, what Vercel saw is people around developers — designers, marketers, sales engineers, product managers — were using the tool more than Vercel expected.

The shift largely came from customers, he added.

“We actually found that there were way more users who were coming from those developer-adjacent kind of roles that got a ton of value from v0,” Khandelwal said. “We weren’t really serving them very well, and that’s kind of where the impetus for this came from.”

## From LLM to Agentic AI, or Waterfall to Agile

[Large language models (LLMs)](https://thenewstack.io/introduction-to-llms/) have primarily used a more waterfall approach to development: You put in a command and it makes something with one attempt — or it outright fails. To make v0 more user-friendly, the tool now makes a call to an [AI agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) instead of just one LLM.

This agentic approach enables it to take a more [agile](https://thenewstack.io/ai-in-agile-managing-the-unpredictable-in-iterative-development/) approach, breaking down commands into sub-tasks so it can iterate very quickly on the application. That, Khandelwal said, allows it to be both easier and powerful for nontechnical users.

“It’ll say, ‘Hey I first need to create the UI, then I need to add a database, then I need to add off, and then I need to polish,’ and it turns out that by doing things step by step just like a real person would, we actually lower error rates a lot more,” he said.

It also allows v0 to iterate on whatever web app you’re deploying. I was able to develop a basic to-do list, complete with an image, in just a few tries that took mere seconds to minutes. If you’re curious about a more complex app, check out [Pokémon Awesome!](https://pokemon-awesome.vercel.app/), a v0-deployed app. There are more on [v0.app’s home page](https://v0.app/).

[![A daily planner made with Vercel v0.app](https://cdn.thenewstack.io/media/2025/08/bebe9721-easy_vercel_app.jpg)](https://cdn.thenewstack.io/media/2025/08/bebe9721-easy_vercel_app.jpg)

My daily planner, made with Vercel v0.app.

Most of my working time was actually spent trying to get [GitHub](https://thenewstack.io/github-launches-its-coding-agent/) to save new iterations of my site, which I felt was more of a “me problem” than a Vercel issue. The AI was finally able to identify the problem (or user error) and tell me how to correct it.

“There are two things that happen much better now, which users find on their first or second prompt,” Khandelwal said.

The first, he said, is that v0.app makes fewer errors, especially for very, very complicated prompts. The second, he added, is that it’s actually faster than v0.dev’s code creation approach.

Previously, Vercel had to “gate” the original v0 so that it wouldn’t do too many things at once. It was told to do a minimum set of what the user had asked for so that it wouldn’t break the application.

“Normally, what would happen is v0 would try to do that all in one pass, and the error rate’s higher when it tries to do all of it once,” he said. Now, v0 will automatically break out those smaller steps.

## Under the AI Hood: Let’s Talk Frameworks

I asked Khandelwal what v0.app did under the hood: Does it default to [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/), for example, which is the micro framework developed and deployed by Vercel? If you don’t ask for a particular framework, he acknowledged, it does use Next.js.

“We try to disclose complexity only when necessary,” he said. “So if you don’t ask for a particular tech stack or anything, we will [build you a web app](https://thenewstack.io/web-devs-meet-the-ai-apps-youll-build-next/). It’ll be using Next.js, it’ll be written in [TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/), and it’ll be styled with [Tailwind](https://thenewstack.io/astro-5-2-brings-tailwind-4-support-and-new-features/).”

These are the “most modern technologies” that are available for web development, he added.

“Today, the industry is very much moving towards standardizing on these, and we use the latest versions of every single part of this stack,” he said. “If you don’t ask for anything, you’re a nontechnical person, you don’t really care what it’s built with. We will give you state-of-the-art technology and build it for you.”

But if you’re more technical, you can customize the code. You can ask for vanilla CSS instead of Tailwind, for instance. It can generate static HTML and CSS sites. It can even generate vanilla React, he said.

> “We try to disclose complexity only when necessary. So if you don’t ask for a particular tech stack or anything, we will build you a web app. It’ll be using Next.js, it’ll be written in TypeScript, and it’ll be styled with Tailwind.”
>
> **— Aryaman Khandelwal, Vercel**

The tool also supports other micro frameworks. Recently, Vercel launched improved support for [Svelte](https://thenewstack.io/svelte-adds-asynchronous-sync-inside-components/), allowing vibe coders to generate Svelte apps and use a lot of the tools that typically work for Next.js.

“We are not super focused on improving support for Vue and Angular and some of the other kind of meta JavaScript frameworks, but in general, we can generate code using them,” Khandelwal said. “We try to make it such that we pick really, really good defaults for you, if you don’t know, and you don’t really care. But you always have the ability to customize it more if you’d like.”

The tool also incorporates a code editor tab, so developers can still go in and change or fix the code if needed. It also allows you to send code to your IDE and, as I alluded to earlier, it can sync with a GitHub repository.

“You can always do that push to git and v0 will actually update the app that you’re working on,” he said. “So you actually get access to the full development workflow in your IDE.”

## v0.app Is Changing the Next.js Framework

There’s another interesting dynamic within Vercel: The Next.js team is [updating the framework](https://thenewstack.io/what-developers-told-us-about-vercels-next-js-update/) so that it plays better with LLMs and agentic AI, Khandelwal said.

“We work super closely with the Next.js team,” he said. “In fact, we are very good customers of Next.js — we give them a lot of feedback on good examples or things like, ‘LLMs don’t seem to understand this syntax’ or ‘don’t seem to understand this pattern in the framework.’”

The team will ask for either better documentation or whether the situation can be simplified or changed.

For instance, there are client-side logs and server-side logs. Typically, client-side logs are in the browser console, whereas server-side logs show up in the terminal. But LLMs often only have access to the terminal.

So, the v0 team informed the Next.js team that they needed logs in both places to support agentic AI development.

Said Khandelwal, “It’s actually a very cool, symbiotic relationship we get to have with Vercel and Next.js where we get to give them very good feedback on how do we make these tools better to use and for vibe coding platforms like this.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)