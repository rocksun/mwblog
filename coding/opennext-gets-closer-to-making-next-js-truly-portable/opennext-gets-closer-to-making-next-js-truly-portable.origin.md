# OpenNext Gets Closer to Making Next.js Truly Portable
![Featued image for: OpenNext Gets Closer to Making Next.js Truly Portable](https://cdn.thenewstack.io/media/2024/10/6b003ee3-james-wiseman-imgcpfimorw-unsplashb-1024x576.jpg)
Given that Next.js is an open source JavaScript framework for frontend development, seeing an associated project named OpenNext can feel slightly puzzling (or even pointed). The name may have caused a little confusion, but the reason for the project is to deal with some of the trade-offs that come with Next.js being a vertically integrated framework — something that makes more sense when you consider its history.

Now the chief product officer at Vercel and overseeing Next.js, [Tom Occhino](https://www.linkedin.com/in/tomocchino/) “helped create React” as an engineering manager at Facebook. “Next.js started around the same time with the intention of adding features to React that make it work really well outside of Facebook,” he told The New Stack.

“React doesn’t have any opinions about your server; Next.js does.”

– Tom Occhino, chief product officer at Vercel
Part of what the framework adds is server-side rendering and data fetching, which has obvious implications.

“React doesn’t have any opinions about your server,” said Occhino. “Next.js does, so you can do data fetching and server-side rendering and all of these other things.”

Next.js not only relies on server infrastructure but also expects to define that infrastructure for you.

“React doesn’t have opinions about, again, how you orchestrate your servers and do your server-side rendering. Hey, here’s some primitives: figure out how to assemble them however you want. Next.js says, ‘Well, if you author your code this way and you fetch your data this way, and you’re doing your writing this way, we can automatically provision any necessary compute to be able to not just deploy but also scale your application.’”

If that framework-defined infrastructure happens to be Vercel (the creators of Next.js), developers get what Occhino calls “loose coupling but high cohesion.”

That promises simplicity for developers, who — even if they’re responsible for writing server-side JavaScript code as well as the frontend — are likely thinking less about infrastructure deployment, performance and scaling than about the details of the application itself. Next.js hosted on Vercel automatically configures preview environments with a URL for easy collaboration with colleagues and even handles automatic failover. This cohesion also allows Vercel to craft features that take advantage of orchestration between framework and infrastructure.

“When you deploy Next.js on Vercel, these things were obviously designed to work really well together, even though they’re loosely coupled.”

– Occhino
“An upcoming [Next.js] feature is partial prerendering,” said Occhino. “We can prerender the static parts of your page and then dynamically stream in the dynamic parts of your page.”

Applications can be composed of multiple cloud services, like an e-commerce backend on Shopify, Salesforce Commerce Cloud or Adobe Experience Manager, with generated product details pages and search results pages living in Vercel’s frontend cloud.

“You can also connect to your random Kubernetes cluster that your DevOps team deploys themselves, and we can create a secure link between Vercel’s infrastructure and wherever your backend is,” Occhino added.

Occhino compares that to Android running on a Google Pixel, or the difference between running git and using GitHub: “When you deploy Next.js on Vercel, these things were obviously designed to work really well together, even though they’re loosely coupled.”

Developers don’t have to host their Next.js on Vercel, but there are obvious advantages.

“Of course, both of these work separately, but in tandem, they work really well together,” said Occhino.

## Front, Back and Middle
But not everyone using Next.js wants to use Vercel’s platform, particularly if they have data and other resources on a different cloud — whether that’s AWS, Azure or Cloudflare. For compliance and procurement reasons, larger organizations may have policies dictating what cloud services can be used. Small startups want to think about designing their product, not working out if they might get hit by egress charges.

“You can build the fanciest, coolest hosting platform, but you’re not going to make it past procurement teams,” points out [Dax Raad](https://www.linkedin.com/in/thdxr/), a member of the SST team that started the OpenNext project to help support their AWS-using customers. “Once you’re in that world, it’s a thousand times easier just to use more AWS than [to] use a new thing.”

“The coupling of frontend and backend is very much an unsolved issue for web developers, and a contentious one at that.”

– Kate Holterhoff, senior analyst at RedMonk
“The coupling of frontend and backend is very much an unsolved issue for web developers and a contentious one at that,” adds [Kate Holterhoff](https://www.linkedin.com/in/kateholterhoff/), senior analyst at RedMonk. “Developers are actively looking for ways to navigate the server/client two-step through approaches like microfrontends, island architectures, and React Server Components, but although we’ve moved on from the PHP days, integrating apps in a way that is both performant and interactive remains rife with problems.”

Because it’s not just a client-side approach like React, Next.js has a server runtime that automatically configures functionality like cache control and image optimization. In fact, Next.js has two runtimes: a runtime based on Node.js for rendering the application and an Edge runtime that has a limited set of Node.js functionality (designed to run on smaller servers with fewer resources but with lower latency because they’re distributed around the network edge close to major population areas. The Edge runtime handles routing rules like redirects, which Vercel calls “middleware.” The difference between these two runtimes has [caused frustration for some developers](https://github.com/vercel/next.js/discussions/46722#discussioncomment-6715038) wanting to run Next.js apps on other platforms, like AWS Lambda or Cloudflare Workers.

“In practice, it’s some constraints that are enforced on the application when it’s bundled up,” explains Cloudflare director of product [Brendan Irvine-Broque](https://www.linkedin.com/in/brendanirvinebroque/overlay/about-this-profile/). Those constraints make self-hosting Next.js harder than you might expect.

“Yes, you can host it [Next.js] if you’re good at going back to the old world of running everything in the Docker container.”

– Mathias Biilmann, Netlify CEO
The Next.js documentation suggests self-hosting on a Node.js server (which may not scale for your use case and doesn’t give you the advantages of a serverless environment) or in a Docker container. The instructions for the latter are [rather minimal](https://nextjs.org/docs/pages/building-your-application/deploying#docker-image), but Vercel’s [Lee Robinson](https://www.linkedin.com/in/leeerob/) recently posted [a fairly comprehensive YouTube video](https://www.youtube.com/watch?v=sIVL4JMqRfc) with more details.

“Yes, you can host it if you’re good at going back to the old world of running everything in the Docker container,” complains Netlify CEO [Mathias Biilmann](https://www.linkedin.com/in/mathias-biilmann-christensen-a5a3805/).

Plus, for most applications, that will require [multiple containers](https://github.com/vercel/next.js/tree/canary/examples/with-docker-multi-env) for redundancy or scale, adding extra complexity, adds Raad. “As soon as you have two containers, you’re going to have a bunch of cache problems that aren’t really obvious ahead of time, because you have to implement a custom cache handler that synchronizes with a central cache. And the Docker container itself isn’t enough: you need a CDN in front of it, and again you get that same cache control problem.”

The partial prerendering feature (which Raad notes is much more sophisticated than the simpler Astro equivalent, and that Vercel can serve from a single request) might work in a Docker container, “but the way it works in the Docker container makes the feature useless”. Middleware doesn’t work well in some environments, he says, and it’s left to developers to work out how to make features like image optimization work efficiently. Plus, most SST users don’t want to use Docker; they want to use a serverless platform like AWS Lambda with a CDN.

Part of the problem with self-hosting Next.js is that it’s not immediately clear which features will work on which platforms and which won’t.

“There are features that don’t work and there are other things where it’s not that the feature doesn’t work, it’s that you get buggy behaviour,” said Raad.

For example, until recently, cache control headers output by Next.js were non-standard; the cache controllers in Vercel infrastructure would understand the headers, but the AWS equivalents did not.

“[Next.js] is a big, complex framework, so it’s not obvious when stuff isn’t exactly working right.”

– Dax Raad, SST (started the OpenNext project)
This unpredictability is where some confusion about why OpenNext is needed comes from. It’s not that hosting Next.js outside Vercel is impossible; it’s that the results vary widely, and developers need expertise in Next.js to know what’s portable — which they may not realize until they’ve finished developing their app and have come to deploy it, or even once it’s in production.

“What really happens is you deploy it and it looks like it’s working but over the course of months, you’ll realize, oh, this little feature is actually slightly wrong, or this other feature isn’t working exactly as expected,” said Raad. “This is a big, complex framework, so it’s not obvious when stuff isn’t exactly working right.”

In many ways, Raad says OpenNext is as much a documentation project as it is about code to automatically configure infrastructure.

“We’re not really sharing code, we’re sharing information,” he adds. “For anything even semi-serious, there’s a lot of information that you’re going to have to discover.”

Other frontend frameworks that build on React — like Remix, [TanStack ](https://tanstack.com/)and Astro — don’t have the expectation that the frontend code will be so opinionated about the backend. So they fully document options for self-hosting on different platforms, including what works and what doesn’t, and how to write an adaptor to make features run there. The open source codebase for Next.js has lingering [references](https://github.com/vercel/next.js/discussions/29801) to the proprietary code Vercel uses to do that itself, rather than comprehensive information on how to do it yourself.

That’s why Biilmann, whose company Netlify is a direct competitor with Vercel, views Next.js as occupying “a weird middle ground between open source and closed source”. Dealing with that requires a lot of reverse engineering about how it’s supposed to work. “We put in very serious effort to build that adaption layer for Next.js in a very different way than for any other open source framework,” said Biilmann. To the point, he added, that Netlify’s test suite for its adapter occasionally exposes bugs in Next.js itself.

“It’s not that Next.js isn’t open source,” agrees Raad. “It’s how to get every single Next.js feature listed in the Next.js documentation actually running in all kinds of environments — that information is just not open.”

That matters more than it would for other frontend frameworks because so many powerful Next.js features depend on the backend infrastructure. He doesn’t view that as malicious or anticompetitive behavior by Vercel; he thinks it’s just the nature of a vertically integrated framework.

“Next.js isn’t as flexible as other frameworks — and that’s why OpenNext exists.”

– Raad
“When they see a problem, they can solve it either purely in the framework or by pairing the framework with specific infrastructure; and you always get technically better solutions when you pair it with specific infrastructure. If you play that forward over the years, they tend to design features that place specific demands on the infrastructure, and it’s a natural emergent thing. Other frameworks don’t really do this because they don’t have a platform.”

In fact, Raad argues that this close connection is a strength of Next.js. “The benefit of choosing Next.js is that it’s the only vertically integrated framework: they integrate all the way down to the infrastructure, allowing them to do things that other frameworks cannot do. So if you’re picking Next.js, you should be picking it because you like that and you’re buying into that.”

The tradeoff is that Next.js isn’t as flexible as other frameworks — and that’s why OpenNext exists.

“That’s why there has to be this other neutral thing solving that problem,” says Raad.

## Documenting for Portability
OpenNext isn’t the first project to support developers who want to use Next.js outside Vercel. But with fairly minimal tools created by individual developers covering just features they needed to use, AWS Lambda (for example) often found it hard to keep up with new versions of Next.js. So all those smaller projects have been [superseded](https://github.com/sladg/nextjs-lambda) by OpenNext’s more complete approach and active community support.

In fact, that was part of the inspiration for the project; SST had previously relied on one of the existing open source projects to support Next.js 12, but the substantial changes in Next.js 13 (which Raad describes as “effectively a brand new framework”) weren’t something the existing maintainer was able to tackle. “When it’s a one-off effort, they tend to be dependent on a single person.”

One motivation for OpenNext was the number of SST users wanting help getting Next.js to work on AWS Lambda.

– Raad
The other motivation was the sheer number of SST users wanting help getting Next.js to work on AWS Lambda. “For years, people kept coming to us and saying, ‘Hey, what you’re doing is great, but the biggest pain point I have is that I have this Next.js app and it’s not obvious to me how you get some of the features to work on AWS’ and for years we were like ‘Yeah, that sucks!’”

Ironically, none of the team at SST are Next.js developers, but according to Raad, “We have to support it because it’s massively popular. We have no passion for this project: it wouldn’t exist if it didn’t need to.”

Platforms like Google Firebase, Cloudflare Workers, Netlify and even AWS’s own Amplify were all creating their own (sometimes closed source) integrations for Next.js. That’s a lot of duplicated work, especially as the wide range of features in Next.js means that any adapter needs enough users to exercise the full breadth of options and see if they’re working properly.

“It [felt] silly that everyone [was] doing this separately and there [wasn’t] a centralized effort,” said Raad. “We figured we were in a decent position to do that because we could seed that effort with our community, [which] has a bunch of people wanting to use Next.js and AWS.”

OpenNext aims to support 100% of Next.js 14 features.

OpenNext launched in April 2023 with support for about 70% of Next.js features; it now aims to support all Next.js 14 features and is fully community maintained, with test suites covering features in new Next.js releases. It’s in production use at organizations like Nike, and Raad estimates there are thousands of production sites relying on it.

Now Cloudflare and Netlify are working on OpenNext adapters for their platforms. Biilmann views it as “a place to collaborate cross-competitively in a way that feels pretty natural in the open source world, on what does the right infrastructure look like to make it simple to run Next.js across as many frontend platforms as possible”.

In fact, just days after the launch of Next.js 15, Netlify announced it is [moving](https://www.netlify.com/blog/netlify-joins-opennext/) its own [existing, comprehensive open source Next.js adaptor](https://github.com/netlify/next-runtime/) to the OpenNext repo.

Developers could already deploy Next.js apps to Cloudflare Pages using [cloudflare/next-on-pages](https://www.npmjs.com/package/@cloudflare/next-on-pages), but that only supports the Edge runtime. The [OpenNext adapter Cloudflare is building](https://opennext.js.org/cloudflare) transforms the Next.js output to run in either Pages or Workers (or locally using the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/)).

“Really, it’s just about meeting developers where they are,” says Irvine-Broque. “Next.js is one of the most popular frameworks that’s out there. We want to make sure that whatever framework that you’re bringing to the table, you can use the rest of Cloudflare with it.”

That includes support for options like programmatically interacting with platform primitives, such as rate limiting directly from a Worker.

Because these adaptors are now being built as part of an open source project rather than as internal code in the platforms, it opens it up to a wider pool of contributors. One large Cloudflare customer that uses Next.js is already planning to contribute to the OpenNext adaptor, which Irvine-Broque categorizes as “pretty 1.0”. It already supports upcoming features like Incremental Static Regeneration (which lets you mix static and on-demand server rendering for pages that need occasional updates) and work is underway on Middleware and Partial Prerendering.

## From Confusion to Collaboration
The growing momentum behind OpenNext shows the need for the project; and while there’s clearly been frustration on all sides, what’s come out of it is conversations that will end up making it easier for Next.js users and platform owners. Amplify is the only significant project in this space that hasn’t yet joined OpenNext (it’s not clear how many resources AWS is devoting to it) and Vercel is getting involved too.

Vercel has already been in discussion with OpenNext maintainers.

“They’ve been in discussion with our maintainers,” says Raad, “which has been super helpful, because our maintainers historically have had to reverse engineer everything.”

Now if something in Next.js doesn’t work in AWS Lambda, instead of trying to guess what’s supposed to happen, according to Raad “they can just ask the team and they get answers; having that direct line has been massive.”

The Next.js team at Vercel has also fixed some issues in the code that used to require what Raad terms hacks in OpenNext. “And I think they’ll continue to do that,” he added.

He’s hopeful that the collaboration could shrink the scope of OpenNext over time. “Next.js itself is handling some of these things more and they’re talking about moving the information in our docs into theirs so it looks more like other frameworks.” That will likely cover deploying Next.js on AWS, Netlify and Cloudflare, defusing concerns that Next.js is tied too closely to Vercel.

But even with bug fixes and improved documentation in Next.js, it’s likely that OpenNext will continue to be necessary, and he expects it will transition to being part of a foundation.

“Even if they’re talking to us and letting us know about changes ahead of time, there’s always going to be a chasing dynamic where OpenNext is chasing Next.js releases,” Raad warns. “It’s never going to fully close the gap.”

While the OpenNext name might appear provocative, Raad points out that SST frequently recommends prospective users pick Vercel for simplicity if they can, as well as warning existing Vercel customers how much work moving to OpenNext will be.

“We refer people to them all the time: it’s just a lot of companies that only use AWS have rules you cannot use anything else because it increases the compliance and procurement burden, so they have no choice, and we’re stuck trying to figure it out for them.”

Raad also notes that Vercel’s suggested approach of using Docker is probably a significant part of Next.js usage, especially for simpler uses.

Biilmann agrees. “We run some of the largest Next.js properties out there for our enterprise customers,” he said. “There’s a lot of Next.js sites that just run in Docker containers, in a Kubernetes cluster.”

“If we don’t get some real open governance in place around this, it could be the downfall of React.”

– Biilmann
The developers who are happily using that solution may not understand why OpenNext is necessary, but it doesn’t work for everyone and Biilmann says he sees a lot of frustration in the community, which was starting to spill over onto React (where Vercel also makes significant contributions, as the project introduces its own server-side features, like server functions in React 19).

“If we don’t get some real open governance in place around this, it could be the downfall of React,” Biilmann warns. “If that’s the direction, it feels like being able to run that anywhere in an open way is pretty important for the whole ecosystem, and having really clear adapter contracts and so on becomes really important.”

Increased transparency will help Next.js compete with the [Vite.js](https://v2.vitejs.dev/) ecosystem, which offers routers as composable primitives and promises to support code targeting for multiple environments, which is being adopted by frameworks like Angular.

“An environment could be a Netlify function, or it could be a Cloudflare worker, or it could be the browser, or it could be a service worker in the browser,” Biilmann explains. “That’s a different vision of the world than the framework-derived infrastructure vision.”

He’s hopeful that OpenNext could give Next.js more opportunities for new features, as well as make sure it’s not tied to one company’s success rate.

“If we really succeed in this over the next year, and start creating a more healthy open source ecosystem for frontend, we would start seeing a lot of what’s true for the open source ecosystem for infrastructure and backend,” Biilmann said, meaning that vendors who compete in other ways can still collaborate. “There’s no reason we couldn’t invest a lot of the resources we have to invest into just maintaining adapters, into contributing upstream.”

“I do hope that Next.js itself benefits from the idea that it’s being deployed to a lot of other places.”

– Occhino (from Vercel)
Occhino is equally positive about both the immediate and longer-term impact of OpenNext. “At the very minimum, the ecosystem will benefit. More people will have access to Next.js [because] that works in more contexts. But I do hope that Next.js itself benefits from the idea that it’s being deployed to a lot of other places.”

“I do think there will be an opportunity for some of those adapters to influence the framework itself,” Occhino adds. “But also, I’m interested in the collaboration on those adapters and what we learn when we deploy to different types of infrastructure.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)