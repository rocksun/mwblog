# Astro’s Journey from Static Site Generator to Next.js Rival
![Featued image for: Astro’s Journey from Static Site Generator to Next.js Rival](https://cdn.thenewstack.io/media/2024/03/70ae1f09-nasa-gywfpvi2jzm-unsplash-1024x677.jpg)
In Netlify’s most recent developer survey, Astro was the
[fastest growing web framework](https://thenewstack.io/web-development-in-2023-javascript-still-rules-ai-emerges/) in both usage and satisfaction. While it still trails behind Next.js, the current dominant framework, Astro has been [praised for its simpler approach](https://thenewstack.io/keep-it-simple-frameworks-netlify-ceo-praises-astro-remix/) to web development.
Part of the appeal of
[Astro](https://astro.build/) is that it doesn’t claim to be a swiss army knife for web development. On its homepage, Astro humbly declares itself “the web framework for content-driven websites” (although, less humbly, Astro also says it “powers the world’s fastest websites”).
## Less JavaScript
One of the standout features of Astro is that it doesn’t use as much JavaScript as other popular frameworks. It has “zero JS, by default” — which means that Astro components don’t render on the client, but instead “render to HTML either at build-time or on-demand using server-side rendering (SSR).”
Even if you don’t want to entirely ditch JavaScript, many developers are adopting a
*reduced* JavaScript approach to building websites. In [a tutorial for The New Stack](https://thenewstack.io/how-to-use-astro-with-a-sprinkling-of-react/), Paul Scanlon explained how he migrated his personal website from a React framework to Astro “with a sprinkling of JavaScript.” This was made possible by Astro’s “islands” architecture. [Astro’s documentation](https://docs.astro.build/en/concepts/islands/) defines an “island” as “any interactive UI component on the page” and invites developers to think of an island as “an interactive widget floating in a sea of otherwise static, lightweight, server-rendered HTML.”
The key point is that an island does away with the need to, as Astro puts it, “hydrate and render an entire website as one large JavaScript application (also known as a single-page application, or SPA).”
Islands also mean less need for React, the popular but
[often overused](https://thenewstack.io/2023-web-tech-check-in-react-performance-pwas-ios-browsers/) JavaScript library. As Scanlon put it in his post, “React is great, but is it required on every page of your website, or is it only needed in a few “islands” around your site?”
## Astro Now Rivals Any Major Web Framework
What developers love about Astro is the apparent simplicity of its approach, but with every new release, it is adding more power.
[Astro 3.0](https://astro.build/blog/astro-3/), released at the end of August 2023, had image optimizations and support for the View Transitions API. [Astro 4.0](https://astro.build/blog/astro-4/), released in December, featured a new “dev toolbar” and [boasted](https://twitter.com/astrodotbuild/status/1732104305673634140) “80% faster builds.”
In a recent presentation at CFE, James Q Quick, a JavaScript developer who runs a popular
[YouTube channel](https://www.youtube.com/@JamesQQuick), pointed out that most people start using Astro because it’s known as a “static-first” framework — in other words, it is really good at generating static HTML pages (which are, of course, the foundation of a content site). But, said Quick, Astro can do so much more.
“Astro can do almost anything that major frameworks like Next.js and SvelteKit, etc., can do,” he said. “It’s so powerful, it’s so flexible, it’s so simple.”
On
[an episode](https://www.youtube.com/watch?v=2RL21V48Xqg) of the *Modern Web* podcast in January, Quick explained how Astro was kind of a next-generation Gatsby. His personal blog was previously on Gatsby and he’d started to migrate it to Next.js, the framework he spent a lot of his work time using. But along the way he tried out Astro and was soon hooked by the developer experience. So he ditched Next.js and moved his site to Astro instead.
Then as Astro began adding more server functionality, to catch up with what Next.js offered, Quick became even more impressed.
“I’ve loved the transition of them [Astro] kind of moving away from just being static-first, but really nailing that experience first [and] then moving into the server,” he said. “My bet is they’re going to continue to add features and functionality on the server, but they’re going to do it with an amazing developer experience in mind, because they’ve proven that with all the other stuff that they’ve already done.”
Eventually, says Quick, Astro will rival Next.js in functionality.
## Integrations
Another selling point for Astro is its
[integrations](https://docs.astro.build/en/guides/integrations-guide/) with UI frameworks, like React, Vue, Svelte and Solid. This means you can bring across components you’ve already written in other frameworks. Astro also integrates with tools like Tailwind and MDX “with a few lines of code.”
“I don’t know why other frameworks don’t include this; for the things that you’re going to do on a regular basis, Astro has integrations to do that thing,” Quick said in his CFE presentation. He added that “Next.js doesn’t really have this — they just have NPM packages.”
Scanlon used the React integration in Astro in order to make an interactive contact form for his website. But the rest of his site is static-only. “I think this approach of incrementally opting in or out of React offers a nice middle ground,” he wrote, “where it’ll allow you to tackle a migration without getting into the weeds and refactoring every component.”
## Better for SEO?
The beauty of Astro is that it falls somewhere between the static-site generator approach of frameworks like Eleventy and Hugo, and the full-on JavaScript world of Next.js, Vue and others. You can take an HTML and CSS-first approach with Astro, but “sprinkle in” JavaScript (as Scanlon puts it) fairly easily in Astro.
The creator of Astro, Fred K. Schott, also
[suggested recently](https://twitter.com/FredKSchott/status/1744842592905552227) that when Google moves off the “notoriously passable metric (First Input Delay, or FID) with something much more difficult (Interaction to Next Paint, or INP)” that performance will dive for frameworks, [particularly for](https://thenewstack.io/astro-creator-new-web-metric-will-hurt-js-framework-sites/) websites built on Nuxt and Next.js.
At the end of January,
[Google announced](https://developers.google.com/search/blog/2023/05/introducing-inp) that INP “will replace FID as a part of Core Web Vitals on March 12, 2024,” so we will find out as soon as next week how Astro sites fare compared to Next.js.
Regardless, if you’re a developer looking for ways to reduce your reliance on JavaScript, then Astro is well worth checking out.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)