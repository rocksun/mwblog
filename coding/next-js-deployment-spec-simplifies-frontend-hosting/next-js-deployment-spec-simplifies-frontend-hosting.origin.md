# Next.js Deployment Spec Simplifies Frontend Hosting
![Featued image for: Next.js Deployment Spec Simplifies Frontend Hosting](https://cdn.thenewstack.io/media/2025/05/bdbe5393-img_0004-1024x576.jpeg)
On the heels of a [callout from web hosting platform Netlify](https://www.netlify.com/blog/how-we-run-nextjs/), Next.js will soon offer a new specification designed to simplify how infrastructure providers deploy the open source framework. The new specification will bring the framework, which was created and is maintained by Vercel, into alignment with other frameworks, such as [Astro](https://thenewstack.io/astro-5-2-brings-tailwind-4-support-and-new-features/), [Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/), [Remix](https://thenewstack.io/why-some-developers-are-unhappy-with-react-router/), [SvelteKit](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/) and [Qwik](https://thenewstack.io/how-to-build-embed-components-with-astro-qwik-and-stackblitz/).

The specification will reduce the work that third-party hosting providers, which includes Vercel competitors [Netlify](https://thenewstack.io/netlify-makes-preview-servers-available/) and [CloudFlare](https://thenewstack.io/cloudflare-for-ai-helps-businesses-safely-use-ai/), must do to fully support the framework. Such specifications are used by hosting services to build an adapter, plugin or presets for frameworks.

Hosting providers need these adapters to provision and configure the infrastructure when hosting applications built with frameworks. Without such an adapter, they must hand-code a tool to ensure the framework functions as it should.

This is done outside the purview of developers, so it’s possible Next.js developers have not brushed up against the problem — depending on their provider. For instance, Netlify has engineered a solution behind the scenes.

## Frameworks and Infrastructure
[Next.js](https://thenewstack.io/build-a-real-time-bidding-system-with-next-js-and-stream/) was created by [Guillermo Rauch](https://www.linkedin.com/in/rauchg), the CEO and founder of Vercel. That has led some developers to wonder if Vercel and Next.js are too tightly coupled.
It’s a fair question, but it should also be noted that Netlify previously employed [Solid’s Ryan Carniato](https://dev.to/ryansolid/when-netlify-asks-you-to-full-time-oss-you-say-yes-5ccf) and [SvelteKit’s Rich Harris](https://news.ycombinator.com/item?id=29189144) is a Vercel employee. Recently, [TanStack announced that Netlify](https://tanstack.com/blog/netlify-partnership) would be its official deployment provider.

A March post by Netlify hesitantly but decisively called out Next.js for its lack of a specification, although it noted Vercel has been working behind the scenes with Netlify to rectify the situation. The issue seems to have been the pace of progress.

Written by [Philippe Serhal](https://ca.linkedin.com/in/philippe-serhal), Netlify’s staff software engineer for frameworks, and [Elad Rosenheim](https://il.linkedin.com/in/eladrosenheim), principal product manager, the post listed a number of issues the hosting service has with Next.js, noting that the framework does not have an adapter, preset or plugin to work with other infrastructure providers.

“… Next.js builds use a private, largely undocumented format that is subject to change,” they wrote. “…providers like Netlify, Cloudflare, [AWS](https://aws.amazon.com/?utm_content=inline+mention) Amplify Hosting, SST, Google Firebase App Hosting, and Microsoft Azure Static Web Apps must instead read the Vercel-tailored, partly-undocumented build output from disk, translate it to their own format, and write this back to disk.”

They specifically cited a recent [Next.js security incident](https://thenewstack.io/researchers-find-next-js-middleware-vulnerability/), including a list of difficulties in supporting the framework and work it had to do behind the scenes to make Next.js function in the way it does with Vercel (while noting that it does not have to do this with other frameworks).

“Many of these — as well as, arguably, the incident response — are related to the closed nature of how Next.js is maintained,” Netlify stated. “But there is now an honest effort by everyone to tackle this problem.”

A major benefit of [open source software](https://thenewstack.io/open-source-development-threatened-in-europe/) is supposed to be the ability to port it to different providers, the post added.

The specification has been in the works for six months behind the scenes, according to [Lee Robinson](https://www.linkedin.com/in/leeerob), vice president of product at Vercel, who also teaches the Next.js framework.

“This started back in October, and during Next.js Ship, we announced a bunch of improvements for [Next.js developers](https://thenewstack.io/introduction-to-vercel-frontend-as-a-service-for-developers/) who are self-hosting,” Robinson told The New Stack. “Since then, we’ve been continuing, working behind the scenes with the infrastructure companies on adding new functionality for this.”

Robinson said “the honest reality” is it’s beneficial to develop an open source tool alongside the infrastructure, because it allows the infrastructure team to understand how things actually are built and deployed in practice.

“The way we like to think about it is a high cohesion, but loose coupling. So high cohesion between the framework and infrastructure, but then ideally, the loose coupling so you can take that framework and put it wherever you want,” he said. “Even though we’ve had the loose coupling, I think things like the documentation gave this perception that actually it was very intrinsically linked together.”

He added that the lack of adapters for Cloudflare and Netlify also made it “a confusing story for folks who wanted to deploy to competitors of Vercel, essentially.”

The Next.js team agreed that the specification was needed and began working with Netlify and Cloudflare on a deployment adapter API, he added. Behind the scenes, Vercel built an adapter to work with the framework as well.

“It’s not a novel idea. If you look at other frameworks in the ecosystem — SvelteKit and others — they’ve landed in a similar spot, where there is a provider-agnostic way of taking the framework and making it work great on any infrastructure platform,” Lee said.

He agreed that the lack of an adapter meant infrastructure companies needed to do “a lot of that work themselves and reverse-engineer some of the pieces,” adding that the Next.js team wanted to make that process easier.

The specification also addresses something developers want: The ability to choose where they host their applications.

“What developers want to know when picking an open source tool is that they are not locked into that tool,” Robinson said. “They’re free to use whatever platform they would like. They’re free to self-host or use a service if they would like, and that they have confidence in the stewardship, maintenance of the project itself.”

The adapter is currently in the “request for comment” period, and the team made that publicly available after the Netlify post. The plan is to have something for infrastructure platforms in the next month, he said.

“We’re still working with Netlify and Cloudflare and others who want to build their own adapters, or essentially transform what they’ve already built and turn it into this new format,” he said. “Eventually, what will happen behind the scenes is that when you deploy Next.js to Netlify, they’ll just automatically install this adapter for you, which is basically what happens today. It’s just [that] adhering to this spec is much easier for them to maintain.”

In addition to addressing this, Robinson said they are cleaning up the documentation, removing language that specifically alluded to Vercel, to make it clear that it will work on other platforms.

*Editor’s Note: Corrected May 7 at 12:30 a.m. to state that Rich Harris works at Vercel, not, as previously stated, Netlify. Also, Ryan Carniato left Netlify in September, 2024, to work at Sentry.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)