Frontend developer Sam Selikoff, who recently joined [Vercel](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/) as staff engineer, had a pressing question for the Next.js team: Why couldn’t developers have snappy navigations while using React Server Components (RSC)?

“I love the DX of the app router, and server components were a great addition to React, especially for just fetching data and rendering it on the page,” he told audiences at [the Next.js Conference](https://www.youtube.com/watch?v=myjrQS_7zNk), held Oct. 22. “I just didn’t understand why using RSCs meant we had to give up on the snappy client navigation that we’re so used to in our React apps. Isn’t one of the reasons we love React the ability to run code right in the browser?”

Why, he wondered, couldn’t Next.js use RSCs for the initial page render and still use good old [client-side React](https://thenewstack.io/strategies-to-build-react-apps-in-a-client-side-architecture/) for everything else?”

This is the story of how the framework answered his question.

## The Web Goes Server Side (Again)

Selikoff took his Next.js Conference audience back to 2023, when the app router was first created. A the time, frontend frameworks bundled all of the code on the server then sent it to the browser, which rendered the data fetching and routing — kind of like an iOS app, he said.

But the web is not iOS.

“People want to be able to open up articles and links to tweets instantly, which is exactly why, in 2012, Twitter’s engineering team shared in this post that they cut their initial load times by 80% by moving a lot of their client-side rendering back to the server,” he said. “They also split up their code into smaller bundles so that they could lazy load them as needed.”

That led frameworks to add features such as server-side rendering and dynamic imports.

In 2017, Netflix shared that it had removed all client-side React from its landing page by pushing even more rendering and data fetching to the server and letting pre-rendered HTML do the heavy lifting. Netflix, according to Selikoff, saw a 50% improvement in the performance of this page.

“So again, we saw the trend continue, more APIs doing more work earlier on the server,” he said.

When it came to single page application (SPA) navigations, teams that relied exclusively on client-side code for their routing concerns also ran into performance ceilings, Selikoff said.

“In 2018, the engineers at Square wrote about using a new [Ember](https://thenewstack.io/choose-your-own-adventure-emberjs-co-creator-tom-dale/) feature called engines to break up their dashboards into sections — that could be lazy loading,” he said.

LinkedIn also adopted this feature of the [Ember.js](https://emberjs.com/) engines because the sheer amount of URLs on their site was causing performance problems by loading the entire client, he said. Remix also recently added a feature to help Shopify with the exact same problem, he added.

> “We knew from experience that the client-centric approach was a dead-end. That’s why the app router defaults to rendering data fetching and routing on the server with server components.”  
> **— Sam Selikoff, Vercel**

“I make all these points to say that after a decade of experience building with these rich frontends and the development of the entire framework ecosystem, this was the state of the art,” he said. “We had these hybrid frameworks that were primarily client-first SPAs, but they kept adding server-side features that you could opt into when you inevitably hit the limitations of the client.”

## Enter App Router

The goal of [App Router](https://thenewstack.io/why-developers-should-give-next-js-app-router-another-chance/) was to solve these problems at the foundational level, Selikoff said.

“We knew from experience that the client-centric approach was a dead end,” he said. “That’s why the App Router defaults to rendering data fetching and routing on the server with server components.”

Next.js hoped to bake in all these hard-won lessons into the framework in an effort to never hit these performance ceilings, he said.

Still, Selikoff wanted his snappy client navs; he likes that he can open his iPhone and see pre-rendered screens sitting there waiting.

“Shouldn’t we have this option to pre-render certain screens or pre-fetch upcoming client navigations so we can provide the best user experience?” he asked. “I think we should. And not coincidentally, so does the rest of the team, because that’s exactly what they’ve been working on.”

## Introducing Cache Components

Two years in the making, Cache Components are a new set of opt-in features designed to make caching in Next.js both more explicit and flexible, the team stated. Cache components, Selikoff said, let developers pre-render and pre-fetch the UI, which brings instant navigations to the App Router.

Cache Components leverage a new “use cache” directive, which uses the compiler to automatically generate cache keys when it’s used. It can deploy cache pages, components and functions.

Dynamic code in any page, layout or API route is executed at request time by default with Cache Components. He demonstrated the new functions, showing how it could be used on a football site with real-time scores.

“If you’ve worked on Next before, you know that if you can make a route static, it’s usually pretty good, it usually ends up in an extremely fast user experience, which is great,” Selikoff said. “Except today, when you make a route static in Next, you can’t fetch anything dynamic during the initial request at all. So it’s an all-or-nothing decision. If you pre-render a route today, you have to pre-render the whole thing.”

> “This is what it’s like to work with Next.js Cache Components. It’s truly dynamic by default, so there’s no more implicit caching. We didn’t need to add force dynamic to our page or cache no store to our fetch calls.”  
> — **Selikoff**

But since every page has something dynamic, developers would need to add some client-side data fetching logic or some new library that’s going to complete way after the initial request has already come back. That will start waterfalling back and forth between the client and the server, he said, so developers typically have to set up API endpoints.

“Here we didn’t do any of that: This page isn’t dynamic or static,” he said. “It’s both.”

Instead, it’s partially pre-rendered, so when Cache Components are enabled, developers don’t have to choose between static or dynamic, Selikoff said.

“Every route is partially pre-rendered,” he said. “Most of the page’s content is dynamic. It gets the browser to start booting the app instantly and it doesn’t slow down the dynamic data at all, thanks to [React’s use of server-side](https://thenewstack.io/how-to-build-a-server-side-react-app-using-vite-and-express/) streaming.”

He showed how to use a wrap inside of `suspense` to create a [skeleton screen](https://medium.com/geekculture/what-is-a-skeleton-screen-69e55648891e) for part of the UI.

“Once the fetch calls finish, the data streams in, easy peasy, right?” he said. “This is what it’s like to work with Next.js Cache Components. It’s truly dynamic by default, so there’s no more implicit caching. We didn’t need to add force dynamic to our page or cache no store to our fetch calls.”

“As long as we’re inside a suspense boundary, we can fetch data without any surprises. And those suspense boundaries ensure that every page in our app can serve its static content instantly and prepare the browser for the dynamic content as early as possible.”

## Snappy Navs Are Here Again

That brings us back to Selikoff’s request for snappy navs. He referenced his demo, which was a game page.

“Let’s imagine we just refreshed on here, and we want to go back to the Games page, so we’ll see as soon as we click, we get an instant nav to the pre-rendered page, and then the content fills in. How does this work?” he said. “The answer is pre-fetching. Thanks to partial pre-rendering, links will pre-fetch the static content for the upcoming route by default.”

The new programming model ensures each route has some static content, Selikoff said, so it’s both cheap to fetch and it won’t become stale by the time the user actually clicks the link.

The link tag can just pre-fetch in advance and developers can have their snappy client nav back, he said.

“Even though the server was involved originally, by the time we took the nav, it’s as if you were in the client doing a client-side navigation,” he said. “We’re able to make use of the browser to get those snappy navs without doing any extra work.

“We don’t have to move any of our data fetching code to the client. We don’t need to fork our page component based on whether it’s the initial render or a client-side navigation, and we didn’t need to create any special loading .TSX file. All we had to do was use Suspense and RSCs like normal and Next gave us instant client-side navs for free.”

He also told the audience why the feature is called Cache Components when it doesn’t seem to have anything to do with the use cache directive.

“If you think about our site so far, what is it that actually let us pref-etch the static content for each one of these pages ahead of time?” Selikoff asked. “It’s the fact that we know that this static content can’t be stale. That’s what let us pre-fetch it. … This static content can’t change because it’s based on the code we wrote in our application. It can’t change unless we change the code and redeploy the app. So this static, pre-rendered content is effectively cached content.”

Cache is not “just an update to our static rendering API,” he added.

What if a developer wants to pre-fetch pages that depend on those things once users are clicking around the app? For that, a developer would still use cache, he said.

“Just because the App Router is server first doesn’t mean we have to give up on the kinds of interactions that made us all fall in love with React in the first place,” Selikoff said. “Pre-fetching is a powerful example of how there are many, many more. Now that we have an architecture that avoids the performance cliffs of the past, we know that this new model can take us further than the old one ever could.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)