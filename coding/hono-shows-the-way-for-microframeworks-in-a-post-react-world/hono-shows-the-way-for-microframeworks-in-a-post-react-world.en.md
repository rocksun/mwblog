This week, a web framework called Hono [announced](https://x.com/honojs/status/1942207883879530525) on X that it had “finally” reached 25,000 GitHub stars. While 25,000 fans is not exactly under the radar, Hono hasn’t had the attention it deserves either. Given it is built on web standards, rather than (for example) React, Hono seems like an indicator of where frameworks are headed [post-React](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/).

Hono was created in December 2021 by Japanese developer [Yusuke Wada](https://yusu.ke/). According to its GitHub repository, Hono, which means “flame” in Japanese, is “a small, simple, and ultrafast web framework built on Web Standards.” It was originally built for Cloudflare Workers, but now works “on any JavaScript runtime,” including Node.js, Deno, Bun and Vercel (although Node support requires an adapter and Node ≥ 18).

Wada was hired by Cloudflare in 2023, and some of his work time is spent on Hono. He has big ambitions for the project, judging by this statement in [an October 2024 post](https://blog.cloudflare.com/the-story-of-web-framework-hono-from-the-creator-of-hono/) on the Cloudflare blog:

“In contrast to the Next.js framework, which started from the client-side with React, Hono is trying to become a full-stack framework starting from the server-side.”

## Use Cases

So what can you do with Hono? In [an interview](https://www.youtube.com/watch?v=yoqtk85HITM) on the Cloudflare Developers YouTube channel last October, Wada remarked that he’s been surprised at the variety of use cases.

“Some build classic web APIs, others make full-stack apps, some run documentation sites, and I’ve even seen it used to implement an API layer inside Next.js,” he said. “Users keep coming up with use cases I never imagined, and that’s the most exciting part.”

Within Cloudflare itself, Hono is used for three different API servers, according to the project’s [documentation](https://hono.dev/docs/). Two of them (KV & D1) are internal and one (cdnjs) is public.

[![Hono screenshot](https://cdn.thenewstack.io/media/2025/07/dcbce603-hono-screenshot-july2025.png)](https://cdn.thenewstack.io/media/2025/07/dcbce603-hono-screenshot-july2025.png)

Hono homepage

In terms of direct comparisons, Hono is best thought of as a modern replacement for Express, the middleware web framework for Node.js. The main benefit of using Hono is that it doesn’t just run on Node.js; but even on Node.js, Hono often benchmarks a bit faster than Express.

Hono’s differentiation from Express is that it’s built on the Fetch API, a [WHATWG standard](https://fetch.spec.whatwg.org/) that “defines requests, responses, and the process that binds them: fetching.”

So for those developers looking to move on from Node.js and Express, Hono might be a part of the solution.

“I’ve been using Hono + Bun + SQLite for all my personal projects, and I really like it,” said one developer [on Hacker News](https://news.ycombinator.com/item?id=40049320). “Essentially, I’ve replaced Express and Node with it.”

## Comparing to Next.js

When Wada says Hono is building a full-stack framework, he is mainly referring to [HonoX](https://github.com/honojs/honox), a meta-framework on top of Hono that includes file-based routing.

“When you use HonoX, you’re automatically using Hono underneath, which lets you create complete full-stack applications,” he explained. HonoX is also built on Vite, the popular frontend build tool.

The HonoX GitHub project has 2,300 stars at this time of writing and is described as in “alpha stage.” So as a full-stack solution, it’s still very early days for Hono.

Even though Wada compares Hono to Next.js, that’s like comparing a bicycle to a flash car.

Hono is very lightweight and focuses on the server/runtime layer (routing, middleware, responses). It purposely stays UI-agnostic; you can return JSON, stream HTML or bolt on your own templating or JSX/SSR via HonoX.

> As a full-stack solution, it’s early days for Hono.

By contrast, Next.js is a large, opinionated end-to-end React stack. It includes file-based routing, server components, data fetching, bundling with Turbopack, image optimization and much more. It has both UI and backend pieces.

Perhaps Hono’s biggest advantage is its focus on [edge networks](https://thenewstack.io/why-devs-must-rethink-their-role-in-modern-cdns-and-the-edge/). It is designed for all runtimes and is ideally suited for APIs or microservices that need to run on the edge.

[Cloudflare’s documentation](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/hono/) describes Hono as “an ultra-fast, lightweight framework for building web applications.” Cloudflare suggests that Hono combined with Cloudflare Workers is an effective full-stack solution. “With Workers Assets, you can easily combine a Hono API running on Workers with a [React] SPA to create a full-stack app.”

Indeed, if you’re already living in Cloudflare’s ecosystem, then Hono is a good match with Cloudflare products like KV, R2, D1, Durable Objects and Queues.

## Hono’s Place in a Post-React World

While comparing itself to Next.js is a little ambitious (especially given that HonoX is still in alpha mode), Hono does appear to be an indicator of where things are headed. Unlike Next.js or Remix, Hono doesn’t bake in React. You return JSON, stream HTML or layer HonoX for JSX islands only when you need them. That “opt-in UI” is a reflection of the web development ecosystem starting to [move away from all-in-one monoliths](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/).

The era of “super-frameworks” like Next.js is starting to dissipate. Instead, developers are increasingly turning to more modest frameworks that use web standards like [Astro for larger projects](https://thenewstack.io/how-astro-and-its-server-islands-compare-to-react-frameworks/), and now Hono for edge-specific use cases.

Hono is more in the “microframework” camp, so it isn’t really comparable to Next.js — or Astro, for that matter. But it is just as worthy of your attention as those larger frameworks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)