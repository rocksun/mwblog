Late last week, the global cloud platform Cloudflare [acquired the company behind Astro](https://thenewstack.io/cloudflare-acquires-team-behind-open-source-framework-astro/), one of the [leading frontend frameworks](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/). This follows a pattern of popular frameworks coming under the umbrella of platform companies — or at least becoming financially supported by them.

This trend perhaps began in 2021, when [Vercel hired](https://thenewstack.io/vercel-and-svelte-a-perfect-match-for-web-developers/) Svelte creator Rich Harris. That same year, WordPress vendor [Automattic acquired](https://thenewstack.io/frontity-and-the-future-of-wordpress-as-a-dev-platform/) a React framework company called Frontity. In 2022, the global e-commerce company [Shopify acquired Remix](https://shopify.engineering/remix-joins-shopify). In 2023, [Netlify acquired Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/). In 2024, the static site generator Eleventy [joined Font Awesome](https://www.11ty.dev/blog/eleventy-font-awesome/). In 2025, [Vercel purchased NuxtLabs](https://thenewstack.io/creators-of-nuxt-js-and-nitro-join-vercel/), the company behind Nuxt. Also last year, [Figma acquired Payload](https://www.figma.com/blog/payload-joins-figma/), a promising ([if slightly unusual](https://thenewstack.io/introduction-to-payload-a-headless-cms-and-app-framework/)) application framework.

And now we have Cloudflare acquiring The Astro Technology Company, creators of the Astro web framework. So what does Cloudflare want with a frontend framework?

## What Cloudflare wants

In [announcing the Astro acquisition](https://blog.cloudflare.com/astro-joins-cloudflare/), Cloudflare didn’t give much away — it mostly just parroted Astro’s catchphrase, “content-driven websites.”

But it’s not hard to see how this purchase complements Cloudflare’s [mission](https://www.cloudflare.com/en-gb/about-overview/) “to help build a better internet.” Yes, that’s a pretty vague mission statement. But over the past year the company has clearly demonstrated [its support of independent websites](https://thenewstack.io/cloudflares-balancing-act-protect-content-while-pushing-ai/), as online creators the world over struggle with AI companies hoovering up their content for free and (not unrelatedly) [search referral traffic drying up](https://thenewstack.io/google-ai-overviews-and-citations-tips-for-web-publishers/).

Last year, CEO Matthew Prince declared July 1 to be “[Content Independence Day](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)” and demanded that companies like Google, OpenAI and Anthropic compensate website creators for AI crawls. Cloudflare also offers website operators various tools to prevent AI bots from using their content. But Cloudflare isn’t running away from AI, either. It is carefully experimenting with specific AI technologies designed to help website creators — such as launching an implementation of [NLWeb](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/), a nascent protocol that enables publishers to integrate AI chat into their websites in a way that may actually increase traffic, rather than take it away.

> Cloudflare was likely attracted to Astro partly because it gives web developers a viable alternative to React frameworks.

Cloudflare began as a content delivery network (CDN) in 2009, and so it’s always been obsessed with network speed. I don’t think it’s being too simplistic to say that Cloudflare was attracted to Astro partly because it gives web developers [a viable alternative to React frameworks](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/), which are infamous for creating bulky, JavaScript-heavy and (yes) slow websites and apps. Astro, on the other hand, has a “zero JavaScript, by default” policy, which — along with its [“islands” architecture](https://thenewstack.io/how-astro-and-its-server-islands-compare-to-react-frameworks/) — typically results in much faster websites.

Many open web advocates — myself among them — argue that React is not good for the long-term health of the web. So by supporting Astro, Cloudflare is absolutely helping “build a better internet.” (Note that Astro “supports every major UI framework,” so you can use React in Astro; however, there are plenty of better options available).

For his part, Astro founder Fred Schott made it clear in [his announcement post](https://astro.build/blog/joining-cloudflare/) that “Astro will remain free, open source, and MIT-licensed.” He added that Cloudflare’s support will enable his team to stop worrying about building a business and “start focusing 100% on the code, with a shared vision to move the web forward.”

## When framework acquisitions go wrong

The biggest risk of corporations buying frameworks (or, at the very least, employing the people who maintain them) is that the company’s priorities will shift and support tapers off.

Netlify’s purchase of Gastby in February 2023 provides an object lesson here. When Netlify [announced the acquisition](https://www.netlify.com/press/netlify-acquires-gatsby-inc-to-accelerate-adoption-of-composable-web-architectures/), it promised to “keep the power in the hands of developers” and was “committed to being good stewards of the Gatsby open-source project.” But by September that year, co-founders Kyle Mathews and Sam Bhagwat had [both left Netlify](https://blog.xavie.mirmon.co.uk/farewell-gatsby-its-been-one-heck-of-a-ride-cd18b91b0020) and appeared to be no longer contributing to Gatsby.js, the framework.

Since Gatsby.js is open source, you can track the community fallout in the GitHub project. In November 2023, someone asked whether [the project was discontinued](https://github.com/gatsbyjs/gatsby/issues/38696). Netlify CEO Matt Biilmann [replied](https://github.com/gatsbyjs/gatsby/issues/38696#issuecomment-1817064739), saying that “Gatsby is here to stay and we’re not sunsetting it.” He admitted, though, that it was “no secret that Gatsby is no longer the hip new framework on the block.” His message, basically, was that Netlify would keep gatsby.js in maintenance mode.

The rest of that comments thread was full of developers recommending to move to another framework, like Astro or Next.js.

In August 2024, Denver-based developer Justin Carroll opened another GitHub discussion in the project entitled “[Is GatsbyJS Officially Dead?](https://github.com/gatsbyjs/gatsby/discussions/39062)” He noted that there were “’fix’ commits in the repo, but no major dev,” adding that “I’ve LOVED Gatsby, and have built a mini-side-hustle that’s done very well with GatsbyJS, but I feel abandoned, and I want closure.”

Netlify software engineer Philippe Serhal [replied](https://github.com/gatsbyjs/gatsby/discussions/39062#discussioncomment-11337756), pointing to Biilmann’s comment 9 months prior. “Nothing has changed since and we have no plans to change this approach,” he wrote. He added:

“I believe the current level of limited development (security fixes, limited dependency updates, low-hanging-fruit bug fixes, and perf improvements, addressing upcoming third-party API deprecations, etc.) is aligned with what we’ve communicated.”

You have to give points to Netlify for clear communication, albeit buried in a couple of GitHub discussion threads. However, there’s no getting around the fact that the Gatsby framework is no longer a viable option for new development projects. Developers simply no longer care about it.

In the rest of the comments, Astro appeared to get more recommendations as a Gatsby replacement than Next.js — an indication of Astro’s growing popularity at that point.

## The sponsorship route has fewer risks

Although Cloudflare has acquired a company (The Astro Technology Company), sometimes corporations can influence a framework simply by hiring the lead maintainer — who is typically the person who created the framework — or by sponsoring them in some way.

Usually, this happens when there is just a single person controlling the project — as was the case with Harris’ Svelte and Leatherman’s Eleventy.

Sometimes these partnerships between corporation and project maintainer work out; last March, TanStack creator Tanner Linsley entered into [a partnership with Netlify](https://tanstack.com/blog/netlify-partnership), which continues to this day.

But sometimes they don’t work out. Leatherman also worked for Netlify for several years, including being paid just to maintain Eleventy [from February 2022](https://www.zachleat.com/web/eleventy-oss/). But he left Netlify [in mid-2023](https://www.zachleat.com/web/eleventy-side-project/) and, for a while, ran Eleventy independently until moving to Font Awesome in September 2024.

The benefit to the hiring or sponsorship approach, for the community and for the maintainer, is that the person who runs the framework usually retains control of it. So after leaving Netlify, Leatherman moved on with his project on his own terms. Likewise, we can assume Linsley and Harris have that option too.

But what would happen if, for whatever reason, Astro’s lead maintainer, Fred Schott, quit his job at Cloudflare? It’s unclear, because while Astro is still open source, there might now be conflicts between Schott and those maintainers who remain at Cloudflare.

Let’s hope it never comes to that in the Cloudflare-Astro marriage, but it’s an undeniable risk when corporations acquire the companies behind a popular framework. And it’s why an open source community is typically unsettled when this happens.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)