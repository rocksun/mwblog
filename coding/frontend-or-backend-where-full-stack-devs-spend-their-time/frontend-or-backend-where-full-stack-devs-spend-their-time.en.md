Thinking about becoming a full-stack developer? Be forewarned: Full-stack developers are twice as likely to say that a majority of their tasks are on the backend versus the frontend, according to a [new survey](https://devecosystem-2025.jetbrains.com/) by [JetBrains](https://thenewstack.io/exploring-the-jetbrains-ai-assistant-for-visual-studio-code/).

The [State of Developer Experience and Developer Productivity](https://lp.jetbrains.com/stateofdevex/) in 2025 queried more than 6,000 developers and 2,000 tech leads.

Additionally, the survey also found that 85% of developers who handle the frontend also do [backend development](https://roadmap.sh/backend); that contrasts to the 57% of backend developers who do [frontend development](https://thenewstack.io/introduction-to-frontend-development).

The full survey explores how companies measure DevEx and developer productivity, as well as looking at what developers think about AI and standard productivity metrics.

## A New Alpha Release for htmx

[Carson Gross](https://bigsky.software/cv/), creator of [htmx](https://thenewstack.io/htmx-html-approach-to-interactivity-in-a-javascript-world/), promised there would never be an htmx 3. He’s keeping his word, **but** he never said there wouldn’t be an htmx 4.

Gross released a new alpha of htmx this week. [He’s calling it the fetch()ening](https://htmx.org/essays/the-fetchening/).

Htmx is a JavaScript library that allows web developers to use minimal or no client-side JavaScript. Instead, it gives programmers access to modern browser features such as AJAX, WebSockets and Server Sent Events directly from HTML attributes, which enables dynamic web applications.

Gross explained that earlier this year, he created [fixi.js](https://github.com/bigskysoftware/fixi), a hyperminimalist implementation of the ideas in htmx.

“That work gave me a chance to get a lot more familiar with the fetch() and, especially, the async infrastructure available in JavaScript,” he wrote.

While the htmx API is correct, he said, he began to wonder if “maybe there was room for a more dramatic change of the implementation that took advantage of these features in order to simplify the library.” He knew, though, that changing from XMLHttpRequest to fetch() “would be a pretty violent change, guaranteed to break at least some stuff.”

Instead, he started to think about an update to htmx that could add fetch(), and perhaps fix a few of the quirks htmx has picked up.

“So, eventually & reluctantly, I have changed my mind: there will be another major version of htmx,” he wrote. “However, in order to keep my word that there will not be a htmx 3.0, the next release will instead be htmx 4.0.”

The plan is to make three major changes designed to simplify:

1. **The fetch()ening.** Fetch() will replace XMLHttpRequest as the core ajax infrastructure, he wrote. “This won’t actually have a huge effect on most usages of htmx except that the events model will necessarily change due to the differences between fetch() and XMLHttpRequest.”
2. **The Long National Nightmare of Implicit Attribute Inheritance Ends.** This will be the most significant upgrade htmx users will need to deal with, he said. Gross acknowledged his “biggest mistake in htmx 1.0 & 2.0 was making attribute inheritance implicit. I was inspired by CSS in doing this, and the results have been roughly the same as CSS: powerful & maddening,” he wrote. So, he explained, htmx 4.0 attribute inheritance will be explicit rather than implicit, via the :inherited modifier which looks like this:

   <div><button>Like</button>  
   <button>Dislike</button></div>  
   <output id=”output”>Pick a button…</output>

   “Here the hx-target attribute is explicitly declared as inherited on the enclosing div and, if it wasn’t, the button elements would not inherit the target from it,” he wrote.
3. **The Tyranny Of Locally Cached History Ends.** “Another constant source of pain for both us and for htmx users is history support. htmx 2.0 stores history in local cache to make navigation faster,” he wrote. “Unfortunately, snapshotting the DOM is often brittle because of third-party modifications, hidden state, etc. It also creates security issues to store history information in session storage, he added.

In response to this, after the release of htmx 2.0 the team often would recommend people facing history-related issues disable the cache entirely.

“In htmx 4.0, history support will no longer snapshot the DOM and keep it locally,” he wrote. “It will, rather, issue a network request for the restored content. This is the behavior of 2.0 on a history cache-miss, and it works reliably with little effort on behalf of htmx users.”

Instead, there will be an extension that enables history caching, but it will be opt-in, rather than the default, he added.

He goes on to explain what will remain the same, as well as how they will support the multiyear roll out of htmx, which started Nov. 1 with the roll out of the alpha release. The 4.0.0 release should be available sometime next year, with the final release planned for early 2027. You can track the team’s progress in the [four branch on GitHub](https://four.htmx.org).

“All in all, our hope is that htmx 4.0 will feel an awful lot like 2.0, but with better features and, we hope, with fewer bugs,” Gross ended.

## Vercel’s Turborepo Releases Update with Microfrontend Proxy

The [Turborepo](https://thenewstack.io/turborepo-speedy-builds-for-javascript-monorepos/) team has released [Turborepo 2.6](https://turborepo.com/blog/turbo-2-6#microfrontends), which includes improvements to developer experience for the repository.

Turborepo is a build system written in Rust and optimized for JavaScript and TypeScript. It was acquired by the frontend infrastructure company [Vercel](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/) in 2021. This release includes support for:

1. [**Microfrontends**](https://thenewstack.io/the-case-for-microfrontends-and-moving-beyond-one-framework/): Developers can now create many applications on one localhost port;
2. **[Bun](https://thenewstack.io/how-to-build-a-serverless-api-with-bun-and-hono/) package manager to stable**: Granular lockfile analysis and pruning for bun.lock. Bun is a fast, all-in-one JavaScript, TypeScript and JSX toolkit. “This means that, when you use Bun as your package manager, Turborepo will only miss cache for packages that have changes in their dependencies,’” the announcement noted. “If you update a dependency for your web application, your docs application’s tasks will still hit cache.”
3. **Task list search in terminal UI**: Use ‘/’ to focus on tasks faster. This release improved the task search, making it one of the fundamental ways that developers interact with a large Turborepo.

Vertical microfrontends are an architecture where multiple applications are served on one production domain, split into “zones,” the team explained. “Each path for the domain is handled by one of the applications.”

This can create problems for local development since developers must run many applications instead of just one. Each application ends up needing its own development command and port to use, according to Vercel software engineers [Anthony Shew](https://github.com/anthonyshew) and [Tom Knickman](https://github.com/tknickman).

“Today, we’re releasing a microfrontend proxy for local development, so that all of your applications can run on one port, with one command,” Shew and Knickman wrote. “Add a microfrontends.json file to your parent application and Turborepo will automatically proxy localhost:3024 to the ports for your other applications.”

While Turborepo’s native microfrontend proxy is meant for working locally, Turborepo integrates with infrastructure providers to bring microfrontends architecture to production.

“For example, we’ve designed the Turborepo-native microfrontends proxy to work with Vercel’s microfrontends product, which is also releasing to GA today,” the team wrote. “In fact, Vercel’s microfrontends feature provided the research for Turborepo-native microfrontends. We explored how to build microfrontends, locally and in production, with some of the largest customers at Vercel, and are now extracting those learnings from closed-source to open-source.”

When developers install @vercel/microfrontends into a repository, Turborepo will dynamically adjust the local environment to use the proxy provided by the package, deeply integrating with the production infrastructure, they wrote. [Documentation for the microfrontends feature](https://turborepo.com/docs/guides/microfrontends) is available.

“We look forward to working with more providers to integrate seamless microfrontends across your stack. If you are an infrastructure provider looking to integrate, please reach out,” the team wrote.

## From Content to Web: New Partnership Offers One Workflow

[Storyblok](https://www.storyblok.com/), a headless content management system for enterprises, is partnering with web development platform [Netlify](https://thenewstack.io/new-netlify-agents-offer-ai-workflows-for-developers/) with the goal of providing a connected workflow from content creation to web deployment.

What this means for developers is that they can use any frontend framework they want and trigger automatic deploys with every published content update, according to a company statement.

“We’ve seen it over and over again — customers nailing the content side but struggling to get that project out into the world quickly, reliably, and at scale. Their marketers wait days for pages to go live, while their developers spend nights patching servers or untangling deployment scripts,” Dominik Angerer, CEO and co-founder of Storyblok, said in a prepared statement. “With AI upending content strategies, these delays and pain points are simply not tenable; that’s why we’ve partnered with Netlify. It takes care of the heavy lifting behind the scenes: global hosting, edge delivery, caching, scaling, so teams can create and ship amazing projects.”

It will “close the gap” between content management and project deployment, creating faster and more reliable content deployment times at scale, Storyblock stated.

Another goal is also to help companies mitigate the impact of AI on content.

“With consumers increasingly using AI search engines, companies have found that the visibility and accuracy of their brand online is suffering,” Storyblock said in a press release. “Storyblok’s partnership with Netlify is ideally placed to help brands quickly develop, structure and deploy their new content on a performant, AI-ready platform.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)