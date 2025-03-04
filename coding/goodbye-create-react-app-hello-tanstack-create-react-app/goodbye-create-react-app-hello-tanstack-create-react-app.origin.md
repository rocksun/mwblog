# Goodbye Create React App, Hello TanStack Create React App
![Featued image for: Goodbye Create React App, Hello TanStack Create React App](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
[Create React App was deprecated](https://react.dev/blog/2025/02/14/sunsetting-create-react-app) Feb. 14 after nearly a decade of use building React apps. It will continue working in maintenance mode.
“Today, we’re deprecating Create React App for new apps, and encouraging existing apps to migrate to a framework, or to migrate to a build tool like [Vite](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/), [Parcel](https://parceljs.org/), or [Rsbuild](https://rsbuild.dev/),” wrote Meta’s [Matt Carroll](https://x.com/mattcarrollcode) and [Rickey Hanlon](https://bsky.app/profile/ricky.fm).

The Create React App (CRA) library was released in 2016 when there was no clear way to build a new [React](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/) app, the two wrote. It combined several tools into a single recommended configuration to [simplify app development](https://thenewstack.io/datastax-aims-to-simplify-building-ai-apps-with-ragstack/), allowing developers to quickly spin up a React project. It included a basic file structure for the website and a development server to run the website locally for easy development.

“This allowed apps a simple way to upgrade to new tooling features, and allowed the React team to deploy non-trivial tooling changes (Fast Refresh support, React Hooks lint rules) to the broadest possible audience,” they wrote. “This model became so popular that there’s an entire category of tools working this way today.”

So… why end a popular tool?

The blog post outlined CRA’s problems, including that it’s difficult to build high performant production apps. It also noted that Create React App does not offer specific options for routing, data fetching or code splitting.

“In principle, we could solve these problems by essentially evolving it into a framework,” they wrote.

But that raises what may be the biggest challenge for CRA: It has `null`
active maintainers.

So, the team is recommending that developers create new React apps with a framework.

“All the frameworks we recommend support client-side rendering (CSR) and single-page apps (SPA), and can be deployed to a CDN or static hosting service without a server,” they added.

They offer links to migration guides for [Next.js](https://nextjs.org/docs/app/building-your-application/upgrading/from-create-react-app), [React Router](https://reactrouter.com/upgrading/component-routes) and the [Expo web pack to Expo Router](https://docs.expo.dev/router/migrate/from-expo-webpack/).

“If your app has unusual constraints, or you prefer to solve these problems by building your own framework, or you just want to learn how React works from scratch, you can roll your own custom setup with React using [Vite](https://www.robinwieruch.de/vite-create-react-app/), [Parcel](https://parceljs.org/migration/cra/) or [Rsbuild](https://rsbuild.dev/guide/migration/cra),” they added.

The recently released [2024 State of React](https://2024.stateofreact.com/en-US/) ranked CRA as the third most-used tool, behind the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) and [useState](https://react.dev/reference/react/useState). [Eighty-nine percent of the 6,240 developers](https://2024.stateofreact.com/en-US/libraries/) who responded about CRA had used the tool, but from that group nearly 30% reported a negative sentiment about it. Only 15% expressed a positive sentiment. Forty-four percent of frontend developers expressed no sentiment.

## New Create React App for TanStack Router
In related news, TanStack recently added an open source [Create React App for TanStack Router](https://github.com/TanStack/create-tsrouter-app). It’s designed to be a drop-in replacement for [Create React App](https://create-react-app.dev/). This will allow developers to build SPA applications based on their Router.

To help accelerate the migration away from create-react-app, the team has created the create-tsrouter-app CLI, which is a plug-n-play replacement for CRA.

“What you’ll get is a Vite application that uses TanStack Router,” the project notes state. “create-tsrouter-app is everything you loved about CR but implemented with modern tools and best practices, on top of the popular TanStack set of libraries.”

That includes [Tanstack Query](https://tanstack.com/query/latest), an asynchronous state management for TS/JS, React, Solid, Vue, Svelte and Angular, and [Tanstack Router](https://tanstack.com/router/latest) for React and Solid applications.

It’s available under the MIT license.

## Anaconda Offers New Open Source AI Tool
[Anaconda introduced a new open source AI data tool](https://www.anaconda.com/blog/anaconda-launches-lumen-ai) on Wednesday that lets [data science](https://roadmap.sh/ai-data-scientist/vs-computer-science) and development teams explore, transform and visualize data using natural language.
It’s called [Lumen AI ](https://github.com/holoviz/lumen)and it’s an agent-based framework for “chatting with data” and [retrieval augmented generation (RAG)](https://thenewstack.io/solving-the-rag-vs-long-context-model-dilemma/). The goal is to make advanced data workflows more intuitive and scalable, according to a post announcing the news.

“AI-driven, agent-based systems are rapidly changing how businesses operate, but many organizations still struggle with technical barriers, fragmented tools, and slow, manual processes,” Kodie Dower, senior marketing communications manager, wrote. “Lumen eliminates those roadblocks by giving users an AI-powered environment to quickly generate SQL queries, analyze datasets, and build interactive dashboards — all without writing code.”

Dower added that Lumen can:

- Create visualizations such as charts, tables and dashboards without coding;
- Generate SQL queries and transform data across local files, databases, and cloud data lakes;
- Support collaborations with serialized and shared workflows;
- Inspect, validate and edit AI-generated outputs to ensure
[data accuracy and clarity](https://thenewstack.io/from-chaos-to-clarity-master-the-first-mile-of-observability/); - Support custom tools and AI agents.
“The declarative nature of Lumen’s [data model makes it possible for LLMs](https://thenewstack.io/use-your-data-in-llms-with-the-vector-database-you-already-have/) to easily generate entire data transformation pipelines, visualizations and many other types of output,” the repository explained. “Once generated the [data pipelines and visual](https://thenewstack.io/apache-hop-harnesses-metadata-to-create-visual-data-pipelines/) output can be easily serialized, making it possible to share them, to continue the analysis in a notebook and/or build entire dashboards.”

## Vercel Adds Support for React Router v7 Apps
React Router version 7 is a bit different than its previous iterations in that it’s also a [framework after being merged with Remix](https://thenewstack.io/why-some-developers-are-unhappy-with-react-router/). This week, Vercel announced it will support [React Router v7 applications when used as a framework](https://vercel.com/changelog/support-for-eact-router-v7). This includes support for server-rendered React Router applications using [Vercel’s Fluid compute](https://thenewstack.io/vercel-rolls-out-more-cost-effective-infrastructure-model/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)