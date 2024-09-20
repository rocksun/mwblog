# Frontend Schism: Will React Server Components Destroy React?
![Featued image for: Frontend Schism: Will React Server Components Destroy React?](https://cdn.thenewstack.io/media/2024/09/b6631870-react-shatter-1200-1024x576.png)
“One thing that is clear to me is that React Server Components will destroy React,” said [Igor Minar](https://www.linkedin.com/in/igorminar/), one of the creators of the Angular framework and now senior director of engineering at Cloudflare. Others, notably frontend cloud company Vercel, [think that](https://vercel.com/blog/understanding-react-server-components) React Server Components “augment the fundamentals of React.” So who’s right?

To quickly summarize, [React Server Components](https://react.dev/reference/rsc/server-components) (RSCs) are components that run exclusively on the server. As the React team explained in March 2022, when stable support for this “new type of component” was [added in React 18](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023), RSCs “run ahead of time and are excluded from your [client-side] JavaScript bundle.” Next.js (developed by Vercel, which also supports and helps fund React development) was the first major framework to announce support for RSCs, in Next.js 13 [released in October 2022](https://thenewstack.io/next-js-13-debuts-a-faster-rust-based-bundler/). This version of Next.js integrated RSCs as part of its new [App Router architecture](https://nextjs.org/blog/june-2023-update).

## The Pros and Cons of RSC
For Next.js users, RSCs can be useful. YouTuber [Theo Browne](https://www.linkedin.com/in/t3gg/) recently did [a presentation at React Summit 2024](https://gitnation.com/contents/rscs-in-production-1-year-later) and sang the praises of RSC, which the dev tools company he runs has been using for over a year now.

“I couldn’t recommend Server Components highly enough.”

– Theo Browne, YouTuber and CEO Ping Labs
“If you want to learn something new and aren’t scared of it possibly not being the next big thing, I couldn’t recommend Server Components highly enough,” Browne concluded. “Like honestly, I’d be really surprised if these [RSC] aren’t how we end up writing software, going forward.” (It’s worth noting: up until [earlier this month](https://www.youtube.com/watch?v=uv179CTAK-w), Vercel was a sponsor of Browne’s popular YouTube show — a relationship he has always been upfront about.)

Others, however, have found the RSC adjustment more challenging. “The mental overhead of a mixed client/server graph has been my biggest reservation about RSC since it was announced,” said Vue.js creator [Evan You](https://www.linkedin.com/in/evanyou/) on X back [in June](https://x.com/youyuxi/status/1805905884746592752).

There are other adoption challenges for RSC. One of the aspects that make adoption difficult is that applications migrating to this model require supporting infrastructure and — depending on the flavor of React — extended configuration and additional middleware integration that is potentially incompatible with the current application deployment and hosting model that a client-side app may be built on top of.

RSC technology “creates a delayed ambush-by-JS effect.”

– Alex Russell, Partner Product Manager on Microsoft Edge
Although popular with some Next.js users, RSCs have been controversial in the rest of the web development community. At the same time I spoke to Minar, I was also trying to set up a time to talk with Microsoft’s [Alex Russell](https://www.linkedin.com/in/alexrussell/) about his “[HTML-first](https://thenewstack.io/from-react-to-html-first-microsoft-edge-debuts-webui-2-0/)” philosophy. Russell has been a [long-time critic of React](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/), so I asked him about his thoughts on RSC specifically. He emailed back this explanation of why he dislikes them:

“RSC’s *raison d’etre* [reason for being] is to reduce the amount of code that’s necessary to send to the browser up-front because that code is often the source of poor Core Web Vitals outcomes. It does this by running component sub-trees within React Applications on the server up to the point where a developer includes a ‘use client’ directive. At that point, the server sort of nopes out and defines everything in the tree underneath that component as “client-side”, meaning that the server has to then send down all the code that defines every component in the sub-tree, along with any dependencies. This creates a delayed ambush-by-JS effect.”

![Even with App Router, Next.js performs poorly in Core Web Vitals compared to its competition; HTTP Archive Core Web Vitals Technology Report](https://cdn.thenewstack.io/media/2024/09/77706bd8-corewebvitals-technology-report-18sep24a.png)
![Even with App Router, Next.js performs poorly in Core Web Vitals compared to its competition; HTTP Archive Core Web Vitals Technology Report](https://cdn.thenewstack.io/media/2024/09/77706bd8-corewebvitals-technology-report-18sep24a.png)
Even with App Router, Next.js performs poorly in Core Web Vitals compared to its competition; [HTTP Archive Core Web Vitals Technology Report](https://lookerstudio.google.com/u/0/reporting/55bc8fad-44c2-4280-aa0b-5f3f0cd3d2be/page/M6ZPC?params=%7B%22df44%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580Next.js%25EE%2580%2580Nuxt.js%25EE%2580%2580Next.js%2520App%2520Router%25EE%2580%2580Astro%25EE%2580%2580Remix%25EE%2580%2580Qwik%22,%22df46%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580mobile%22%7D)

But again, some developers think RSCs are a useful evolution. In [an April post](https://thenewstack.io/react-server-components-in-a-nutshell/) here on The New Stack, Paul Scanlon wrote that RSCs make “data easily accessible from within a component.” He argued that RSCs “help with understanding what an application is doing because the logic, data, and the resulting user interface elements are neatly co-located in the same file, and when compared to chasing down props and attempting to follow the data journey, the developer experience is often better.”

Better data fetching is one feature of RSCs that Igor Minar likes. “This improved component encapsulation, that in RSCs includes data fetching, is one positive property of RSCs (maybe the only one?) that I do bring up with developers,” he said. “We should try to preserve this feature and make it the norm in the broader web development ecosystem, but without all the downsides that come with RSCs.”

## How It Started
It’s worthwhile revisiting the reason why RSCs were invented by the React team. They were first introduced by the React project way back in [December 2020](https://react.dev/blog/2020/12/21/data-fetching-with-react-server-components), as a proposed data fetching solution for React. The idea was to move relevant React components away from the client and into the server.

“React could and did execute on the server side before, albeit very inefficiently,” Minar noted. “The change with RSCs is that some components execute exclusively on the server side. And that’s new. With RSCs you must run (a portion) of your React application on the server side, while before RSCs, you could run React on the server as an optional optimization, but you were able to opt out of that (and most of the React ecosystem did).”

As React engineer Dan Abramov explained in [a December 2020 video](https://www.youtube.com/watch?v=TQQPAU21ZUw&t=46s), “These are regular React components still, but we’re going to call them Server Components because they execute on the server and on the server only — they’re never shipped to the client.”

The key idea behind React Server Components is that if a component requires data fetching or performs tasks that don’t involve client-side interactivity, it’s often better to handle that component *on the server* rather than as a regular client component.

So far, so logical. After all, this is kind of how browser components used to work back in the 1990s — remember CGI, PHP and ASP? Except now, not everything needs to be done on the server. React itself was invented to make it easier to do more on the client. And now with RSCs, React is enabling developers to decide which parts of the app should run on the server and which should run on the client.

## How It’s Going
So what’s the problem? Well, according to Igor Minar, developers have struggled to implement RSCs.

“React Server Components will cause so much pain in the React community, that developers will start looking for alternatives.”

– Igor Minar, Angular co-creator, Web and OSS enthusiast, now at Cloudflare
“I’m personally convinced that React Server Components will destroy React, because from the technical point of view, it’s a technology that is flawed, that is immature, and that is incompatible with the current React ecosystem,” Minar told me. “It’s a big breaking change for the current React ecosystem, a breaking change that is not even completely thought through and properly implemented, and it’s been pushed down the throats of React developers. So in an interesting way, I think my prediction is that React Server Components will cause so much pain in the React community, that developers will start looking for alternatives.”

Microsoft’s Alex Russell focuses more on site performance in his analysis of RSC.

“The sites that will see performance benefits from RSC are the same sites that already have the sort of [high-management-maturity practices](https://infrequently.org/2022/05/performance-management-maturity/) necessary to keep non-RSC React or Angular in check,” he explained by email (and the link in that quote is from him). “Outside of those orgs, any stray ‘use client’ directive, any point in the component hierarchy, from any dependency, can totally sink site performance.”

Russell is skeptical about the reasons why the React team wanted to introduce RSCs in the first place. “My personal view is that RSC (like fiber/concurrent mode) are an attempt by the React community to minimally adapt to the evolving Core Web Vitals landscape,” he says. “RSC are an attempt to duck below the (very lenient) INP [[Interaction to Next Paint](https://web.dev/articles/inp)] bar, or at least pitch the React community on the idea that they don’t need to leave React in order to deliver minimally decent performance.”

![“Origins having good INP”; HTTP Archive Core Web Vitals Technology Report](https://cdn.thenewstack.io/media/2024/09/161b97cd-corewebvitals-technology-report-18sep24b.png)
![“Origins having good INP”; HTTP Archive Core Web Vitals Technology Report](https://cdn.thenewstack.io/media/2024/09/161b97cd-corewebvitals-technology-report-18sep24b.png)
“Origins having good INP”; [HTTP Archive Core Web Vitals Technology Report](https://lookerstudio.google.com/u/0/reporting/55bc8fad-44c2-4280-aa0b-5f3f0cd3d2be/page/M6ZPC?params=%7B%22df44%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580Next.js%25EE%2580%2580Nuxt.js%25EE%2580%2580Next.js%2520App%2520Router%25EE%2580%2580Astro%25EE%2580%2580SvelteKit%25EE%2580%2580Remix%25EE%2580%2580Qwik%22,%22df46%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580mobile%22%7D)

As for Theo Browne, even he — a fan of RSC — acknowledges that RSC alone isn’t sufficient to implement the technology successfully. Specifically, his company uses the Next.js [App Router](https://nextjs.org/docs/app), which he said in his React Summit presentation is “the only real way to use Server Components safely in production right now.”

According to an FAQ accompanying his React Summit presentation on RSCs, Browne “faced challenges with performance, especially without partial pre-rendering” and “also encountered issues with developer server performance and integration of server and client components in packages.”

But despite these problems implementing RSCs, Browne ultimately endorses them. As he noted in [a recent video](https://www.youtube.com/watch?v=0tvfC9r9lcw) on his YouTube channel (in which he responded to my own recent post on the [React vs. HTML-first](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) debate), Browne said that “Server Components allow you to not have to update things that don’t need to be updated, which helps a lot with the diffing too.” He went on to show some cool functionality that he achieved by using RSC.

## RSC Polarization
“React 19 is near,” wrote Vercel in [a blog post](https://vercel.com/blog/whats-new-in-react-19) earlier this month. RSCs will “act as a foundation for React 19’s new features,” it continued, listing faster initial loads, code portability, and SEO among its perceived benefits.

However, as explained above, current developer experiences with RSCs have been polarizing. RSCs arguably bring some innovative features — such as encapsulated data fetching — but at the cost of difficult adoption and (in Russell’s words) “a delayed ambush-by-JS effect.”

The big question is: will this polarization damage the most valuable thing React has, its ecosystem and community? Given the magnitude of impact that React Server Components will soon have on the React ecosystem, and the early adopters and experts having two very divergent views of it, it will be interesting to monitor how the React community adopts RSCs — and whether RSCs will nudge some web developers to look for better solutions.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)