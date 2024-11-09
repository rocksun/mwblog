# Next.js Canary Supports Partial Pre-Rendering for Faster Sites
![Featued image for: Next.js Canary Supports Partial Pre-Rendering for Faster Sites](https://cdn.thenewstack.io/media/2024/11/a4486f24-wyattjohnsonnextjs-1024x629.jpg)
Partial pre-rendering is fun to say, but it was not fun to code — at least, not initially for the Next.js team.
“When we announced it and we started using it ourselves, it was extremely complicated,”
[Tom Occhino](https://www.linkedin.com/in/tomocchino/), Vercel’s vice president of engineering in frameworks, told The New Stack. “You could make it work, but it was very hard to get it up and running.”
It required advanced configuration and it was easy to get wrong, he added. And if that doesn’t really sell it, the partial pre-rendering process was difficult to document and explain.
“As we’re using it ourselves, we knew that we needed a simpler model, and that started [us] on the journey for what today is
[Next.js 15](https://nextjs.org/blog/next-15),” he said. “In v15, we’ve dramatically simplified the developer APIs and the developer experience associated with being able to leverage this stuff.”
It’s also easier to learn, understand and explain, he added.
“You truly do get the best of both worlds for fast, static, initial render with streaming, dynamic content for your page. It’s beautiful in many ways,” Occhino said.
[Next.js 15’s experimental partial pre-rendering](https://thenewstack.io/vercels-next-js-14-introduces-partial-pre-rendering/) capability was featured prominently at the October Next.js Conference in San Francisco. Next.js is owned by Vercel, a frontend cloud platform.
## Partial Pre-rendering: The Point
[Wyatt Johnson](https://www.linkedin.com/in/wyattjoh/?originalSubdomain=ca), a Vercel software engineer, has worked on partial pre-rendering for two years now. During a conference session, he explained partial pre-rendering — which he shortened to PPR — and how Next.js achieves it to audiences.
“PPR is a rendering strategy that combines the benefits of static and dynamic rendering,” Johnson said. “It allows you to pre-render parts of a page that are static while dynamically fetching and rendering other parts.”
![Code showing partial pre-rendering with Suspense.](https://cdn.thenewstack.io/media/2024/11/cc91da5e-partialprerenderingwithsuspense.png)
Code showing partial pre-rendering with Suspense. Photo by Loraine Lawson
Among the benefits this gives frontend developers is that it can improve performance and SEO by reducing initial load times and providing search engines with pre-rendered content, he added. Johnson walked through how partial pre-rendering can impact core web vitals, particularly the Largest Contentful Paint, which measures how long it takes for a website to display its largest content element.
Partial pre-rendering is uniquely designed to solve some of the problems developers encounter with optimizing this metric, he explained.
“It’s measured from the request start as well, but it’s finished when the largest visible element is rendered on the screen,” he said. “This includes any time it takes to unload the current document, set up connections, perform redirects, and of course, time to first byte.”
A “good” LCP score is less than 2.5 seconds, but that’s still a really long time, he said, adding that a better target would be in the realm of a few 100 milliseconds.
## Challenges of Traditional Rendering
In web development, typically there are two different rendering strategies.
**Static rendering** is fast, but lacks request data. It can render the entire page from the edge and thus send it directly to the users as fast as possible, he said. But it lacks the ability to read request data and instead has to retrieve the information using a client-side request, resulting in expensive round trips to the origin, he added.
In Next.js when you want to access request data, you call the request data APIs, such as cookies or headers, he said. These are only available in server components and once called, the entire page is marked as dynamic and is opted out of static rendering.
**Dynamic rendering** includes request data but can be slow due to server response times. Dynamic rendering allows the request data to be accessed and HTML can be [rendered server-side](https://thenewstack.io/spas-and-react-you-dont-always-need-server-side-rendering/). But that means users are left waiting as the network has to reach all the way back to the origin in order to render the first byte of HTML.
## Partial Pre-rendering Available in Canary
Developers usually have to choose the two, between speed and functionality. That’s the challenge partial pre-rendering aims to solve, according to Johnson. Partial pre-rendering enables generating a static shell at build time.
![An IDE shows an ecostore shop with React code beside it that highlights the use of Suspense.](https://cdn.thenewstack.io/media/2024/11/f38c6277-ecostorenext.js-suspense.png)
An ecostore app showing how Suspense supports partial pre-rendering. Photo by Loraine Lawson
“This is served directly from the edge to browsers while a request is sent back to the origin at the exact same time to complete the dynamic render, which is then streamed in on the same response,” he said. “It’s really composed of those two parts: The static stream that contains the shell [and] the dynamic stream that contains all the dynamic data.”
Getting the static shell to users early is really crucial because it allows resources such as JS, CSS and fonts to begin pre-loading as early as possible, he said.
Next.js does this by using
[React](https://roadmap.sh/react), specifically a “little handy pre-render function” during build they called pre-render. It produces two parts: The first part is named a prelude or the static shell. The second part is the postpone state, which uses JSON to describe what is contained inside the static shell.
“When we run the pre-render, what’s actually happening is that we’re outputting a static shell that’s of HTML,” he said. “We’re outputting this postpone state that informs React of what parts are contained inside that static shell so they can resume the render.”
The Resume API is then called, which creates a stream that the coder could attach to the end of the static shell, which is being streamed out at the same time. The timing of this is critical, he said because “at the same time we’ve started to serve the static shell to users, we’re also kicking off the dynamic invocation at the origin, saving precious milliseconds.”
“Thanks to partial pre-renderings’ hybrid rendering approach, we’re able to serve the static shell to users as fast from the edge as we possibly can, minimizing the time to first byte and the First Contentful Paint.”
– Wyatt Johnson, Vercel software engineer
What this means that as the browser is already downloading static resources that were hinted from the static shell via link headers or tags, while the code is already invoking the server at the origin to render the dynamic parts of that page, he continued.
“Thanks to React streaming, these pieces are sent swapped with their suspense fallbacks, meaning that we don’t even have to wait for hydration in order for the page to load all those pieces,” he said. “The difference from traditional rendering methods and this is that with partial-pre-rendering, when it detects the request data being accessed, it doesn’t actually bail out of static rendering entirely. Instead, it just triggers the fallback to the nearest Suspense boundary.”
The problem the team has spent the past year working on is how to detect when you try to access request data. In his talk,
[Johnson went into a deep dive](https://nextjs.org/conf/session/optimizing-lcp-partial-prerendering-deep-dive) on how they accomplished this; but in short, it leverages Promises, the Node.js event loop, and React server components.
“Suspense is our mortar, allowing [us] to create stable boundaries for the dynamic parts of the page to be streamed in,” he said. “Thanks to partial pre-renderings’ hybrid rendering approach, we’re able to serve the static shell to users as fast from the edge as we possibly can, minimizing the time to first byte and the First Contentful Paint.”
Next.js users can try partial pre-rendering by adding the experimental PPR flag to their Next.js config. That enables the pages to be rendered using the new rendering pipeline.
He emphasized that this is experimental right now, and there are not plans to change that for Next.js 15. It does require installing a canary release to use it.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)