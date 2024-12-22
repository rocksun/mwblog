# Vercel Makes Changes to Next.js To Simplify Self-Hosting
![Featued image for: Vercel Makes Changes to Next.js To Simplify Self-Hosting](https://cdn.thenewstack.io/media/2024/11/c805612f-delba-de-oliveira-at-next.js-conference-1024x629.jpg)
The Next.js team rolled out improvements to the Next.js core and new documentation that will make it easier for [frontend developers to self-host Next.js](https://roadmap.sh/ai/mastering-nextjs---mid-level), said Vercel’s Vice President of Product Lee Robinson during the October Next.js conference in San Francisco.

“We’ve had docs and examples for a while on how to self-host, but they lacked, honestly, a little bit of depth on some of the features like caching and image optimization and how to use Next when you deploy to multicontainer setups,” Robinson said. “ There [were] a lot of things you had to configure.”

Next.js made it easier to configure the default cache handler with Next.js 15, so that developers can take the in-memory caching and define a custom cache handler that uses any adapter the developer wants, he added.

Robinson also announced a new [Next.js GitHub community](https://github.com/nextjs) that would be a place for templates, deployment examples, community adapters and other resources.

See also:[OpenNext Gets Closer to Making Next.js Truly Portable]
The team has improved the documentation about self-hosting, he added. They’ve also made a new video featuring Robinson that [shows developers how to do self-hosting](https://www.youtube.com/watch?v=sIVL4JMqRfc), including deploying it to a virtual private server (in this case, a $4 VPS with [Docker](https://thenewstack.io/docker-overhauls-simplifies-subscription-plans/)) and configuring all of the features. The video also discusses some of the trade-offs and configurations that developers can make, he said.

Robinson and others outlined the changes made to Next.js to support self-hosting and other improvements as part of the keynote presentations made at the conference.

`Use Cache`
, `CacheTag`
and `CacheLife`
`Use cache`
is a new cache API. [Delba de Oliveira](https://www.linkedin.com/in/delbaoliveira?originalSubdomain=uk), a DX Engineer at Vercel, introduced it during the keynote as a way to make web applications faster. “The `use cache`
uses an in-process memory cache,” she said. “What that means is that it starts in-memory, but then later on, you can configure to your own architecture so that in the future, if you want to, you can host a cache anywhere.”
With this mode, “caching is completely opt-in and explicit now,” she added.

Developers can `use cache`
within a data fetching function and as long as the input value here is the same, it will get reused, she added. This makes it “actually very cheap to use cached throughout your application,” she said.

Those who have used the app router are familiar with the `unstable cache`
API, but the `use cache`
API differs.

“You can think of `use cache`
as a successor to unstable cache,” she said. “While unstable cache was really good at caching [JSON data](https://thenewstack.io/working-with-json-data-in-python/), `use cache`
can cache anything that React renders, so anything that’s serializable.”

![Vercel's Vice President of Product Lee Robinson sits along side four other Next.js team mates as he leads a panel at the Next.js conference.](https://cdn.thenewstack.io/media/2024/11/b82d1adf-leerobinson-next.js-leads-panel.jpg)
Left to right: Vercel’s Lee Robinson, Delba de Oliveira, [Sebastian Markbåge](https://www.linkedin.com/in/sebmarkbage/), [Josh Story](https://www.linkedin.com/in/gnoff/) and [Jimmy Lai](https://www.linkedin.com/in/laijimmy0/?locale=en_US) discuss Next.js improvements. Photo by Loraine Lawson.

This allows developers to use it with fetch, your database clients or ends — and even within the component itself, she said.

There are also two new APIs for revalidation, which is a technique used to ensure that the data displayed on a web page is up-to-date and accurate, even when the underlying data source might have changed. `CacheTag`
can be used for on-demand revalidation, whereas cacheLife can be used for time-based revalidation.

Next.js will also have cache profiles that describe caching in plain English of seconds, minutes, hours and days, she said. The cache profiles are integrated across the framework caching layers, “so hopefully, you won’t have to think so much about the different caching layers and network boundaries.” The cache profiles can be customized as well.

“So our goal with this API is to reduce the decision fatigue that comes with revalidation,” de Oliveira said.

Looking at how Next.js functions today, once these APIs are available, there are things that developers will no longer need. She specifically mentioned `unstable cache`
, but also route config options such as dynamics, fetch, cache and revalidate, the fetch extensions like next revalidate and next tags, and the global stale times config option.

“Overall, these APIs hopefully will make sure that you don’t have to carry a lot of information in your brain,” she said. “To summarize what we discussed, we fetch and render data dynamically with async server components for the dynamic paths. We use [Suspense](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) to leverage streaming. If we want to pre-render something, we use cache and then to revalidate and to configure that cache, we use `cacheLive`
in `cacheTag`
. That’s it.”

## Core Improvements to Next.js
There are other improvements to the core of [Next.js that make it easier to self-host](https://nextjs.org/blog/next-15-rc2#improvements-for-self-hosting), said Robinson.

“Previously, Next.js used a WebAssembly-based image optimization library, and while this was faster to install, it unfortunately used a little bit more memory when you deployed on a server when you’re self-hosting,” he said. “We didn’t really like that trade-off.”

Instead, Next.js switched to [Sharp](https://sharp.pixelplumbing.com/), a high-performance [Node.js](https://thenewstack.io/node-js-22-release-improves-developer-experience/) library for processing images.

“The nice thing about Sharp is that it’s both fast install and it’s very memory-efficient,” he said. “So with Next.js 15, we automatically install Sharp for you. For our self-hosted users, you can have the best of both worlds.”

Another improvement was to update the default cache control headers so it’s easier to override the defaults, which he noted was previously hard to do.

The team also made it easier to configure the default cache handler in Next.js 15, Robinson explained, so that developers take the in-memory caching and define the custom cache handler so you can bring your own [Redis](https://thenewstack.io/redis-users-want-a-change/), a popular open source in-memory data store or use any adapter that you want, which should result in faster response times and lower server load.

The enhanced caching features work with both the traditional Pages Router and the new App Router, he said. It supports all the Next.js caching features, such as [ISR (Incremental Static Regeneration](https://nextjs.org/docs/canary/pages/building-your-application/data-fetching/incremental-static-regeneration)) and `use cache`
, he added. While it defaults to in-memory, programmers can change it to persist to storage if they prefer, he said.

Finally, Next.js will also be supporting [Node.js runtime](https://thenewstack.io/node-js-22-release-improves-developer-experience/) for middleware.

“The last bit here is that in your configuration, you can also have some new options here to be able to fully customize your caching for your own setup, your own [CDN structure](https://thenewstack.io/npm-security-woes-continue-amidst-a-series-of-cdn-attacks/), so you can basically configure this however you want,” he added. ”Our goal with Next.js is really to level up the whole ecosystem and share our research back with you all.”

It’s worth noting that Vercel’s CEO, [Guillermo Rauch, has been critical of CDNs](https://x.com/rauchg/status/1836759912711586210).

Robinson acknowledged that Next.js builds features in parallel with dogfooding them on [Vercel](https://thenewstack.io/introduction-to-vercel-frontend-as-a-service-for-developers/)’s infrastructure, which enables a “high cohesion between the framework and infrastructure.” However, he added, they aim for a loose coupling between the two when deploying to the real world.

“Our ambition with Next.js is to be a powerful but approachable framework for the next million or billion [applications](https://thenewstack.io/how-attackers-bypass-commonly-used-web-application-firewalls/) on the web,” he said. “It should be easy to start, flexible enough to adapt to your needs, and also powerful enough to support any level of ambition [for] your app or your business requirements.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)