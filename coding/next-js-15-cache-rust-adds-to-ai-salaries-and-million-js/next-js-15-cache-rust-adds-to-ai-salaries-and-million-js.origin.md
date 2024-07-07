# Next.js 15 Cache, Rust Adds to AI Salaries, and Million.js
![Featued image for: Next.js 15 Cache, Rust Adds to AI Salaries, and Million.js](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
Developers have had questions about how the release candidate of Next.js, which shipped last month, handles cache. Vercel’s [Lee Robinson](https://www.linkedin.com/in/leeerob/), vice president of product marketing, attempted to address those questions in a recent post about [where Vercel intends to take cache and data in Next.js](https://threadreaderapp.com/thread/1803824227704877236.html).

In the release candidate for [Next.js](https://thenewstack.io/solidstart-launches-next-js-15-releases-with-dx-questions/) 15, many parts are no longer cached by default, he wrote.

“In Next.js 15, if I make a fetch to some API, or make a database query, the result is not cached. This is something dynamic. If you want to cache the data, you can opt-in to this behavior. You need to be explicit.”

“We believe the local dev experience should be as ‘lazy’ as possible.” — Lee Robinson, Vercel’s VP of Product Marketing

First, he explained pre-rendering, which is different from caching [data fetching or database queries](https://thenewstack.io/best-practices-collect-and-query-data-from-multiple-sources/), he wrote. It’s where the framework tries to generate a static HTML page during ‘next build.’” He then answers a series of related questions, such as why pre-rendering is functioning differently in local development than production.

“We believe the local dev experience should be as ‘lazy’ as possible. Pages should compile on demand; you wouldn’t want to wait for every single route to compile before you can get started,” he said. “Prerendering every route on save would be slow, which goes against our ambition to keep improving Fast Refresh times.”

Long story short: They’re adding an icon back that will let you know if the page will get pre-rendered.

In the long term, their goal is to make all async operations opt into dynamic rendering.

“We believe [partial prerendering](https://thenewstack.io/vercels-next-js-14-introduces-partial-pre-rendering/) will become the default way of building Next.js applications. In this world, routes can be both static and dynamic,” Robinson wrote.

Then even if the majority of the app is dynamic, developers would still get a shell of the application in the browser immediately, then the dynamic parts would stream in parallel.

“If you want more of the route to be included in the prerender, you can wrap the dynamic parts of your page in React Suspense to define a fallback state,” he added. “Next.js can then prerender up to that Suspense boundary as part of the build process. When serving the page, the user is immediately shown the prerendered HTML while simultaneously streaming the dynamic parts of the route.”

He ended with a list of what this means for Next.js 15:

`fetch`
requests are no longer cached by default;- Route Handlers are no longer cached by default;
- Client-side navigations will no longer keep a cached version of the last page for 30 seconds when using
`<Link>`
or`useRouter`
.
## Rust + AI = More Money
[Rust](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/) or [Golang](https://thenewstack.io/how-golang-range-simplifies-data-structure-iteration/) can increase pay by as much as $30,000 for a job related to [artificial intelligence](https://thenewstack.io/ai-for-developers-how-can-programmers-use-artificial-intelligence/), according to research from content operations software [StoryChief.io](https://www.storychief.io/).
The company analyzed 12,643 job listings on Glassdoor that mentioned AI and displayed any salary information. It’s a bit convoluted as to how it arrived at the figures, but basically it identified the most common keywords related to skills, education and experience, and then estimated each keyword’s salary value, depending on which state the job is in and other criteria.

Under their calculations, Rust added a salary boost averaging $29,480, and Go added $21,080. [Python](https://thenewstack.io/python-mulls-a-change-in-version-numbering/) would mean an additional $13,100 while [PyTorch](https://thenewstack.io/pytorch-docker-and-ai-openness-highlight-ai_dev-europe/) translated to $7,223. [JavaScript](https://thenewstack.io/javascript-framework-maintainers-on-unification-potential/) added an average of $5,952.

Oddly, R — commonly used in data work — rated a negative $6,000, which does not mean it decreased the salary, but rather indicates that the language tended to have lower-than-average salaries, the company said.

## A Look at Million.js, a Minimalistic JS Compiler
Million.js is an open source JavaScript compiler that takes a minimalistic approach. We haven’t seen a lot about it and creator Aiden Bai has not responded to our requests for an interview. But this week we found an [in-depth review of Million.js](https://blog.logrocket.com/million-js-adoption-guide) by programmer and LogRocket technical writer [Isaac Okoro](https://www.linkedin.com/in/isaacthajunior/).

“It lets you write JSX code like React, but compile your code so you ship a lot less JavaScript to the browser,” wrote Okoro. “Million uses a granular approach when updating the DOM. This works differently from how React handles DOM updates, where it updates the entire DOM tree. Million’s approach reduces memory usage, improves rendering speed and performance without sacrificing flexibility.”

Million.js achieves this by using blocks, which are lightweight and highly performant higher-order components “optimized for rendering speed that you can use as a React component,” he wrote.

Million.js boasts the following strengths, according to Okoro:

- “Blazing” fast speed;
- Low memory usage;
- Easy DX;
[Integration with React and React frameworks like Astro](https://thenewstack.io/how-quiks-astro-integration-beats-both-react-and-vanilla-js/), Gatsby, Next.js;- Documentation.
However, Okoro cites the learning curve, lack of community and ecosystem, and questions about its future as drawbacks.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)