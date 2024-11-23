Last updated: November 12, 2024

Server-side rendering (SSR) has been around for a while, but it's worth exploring further. This technique can make your web apps faster and more SEO-friendly.

In this guide, we'll explain SSR, why you might want to use it, and how to implement it without pulling your hair out. We'll cover the basics, compare it to client-side rendering, and discuss some practical examples.

Fundamentally, SSR is about rendering your web pages on the server instead of in the browser. When a user requests a page, the server does all the heavy lifting and sends a fully rendered page to the client. Then, the client-side JavaScript takes over to make it interactive.

The server is doing the prep work in the kitchen, and the browser just has to plate and serve.

Here's a minimal Express.js example:

```
const express = require('express');
const React = require('react');
const ReactDOMServer = require('react-dom/server');
const App = require('./App');
const app = express();
app.get('/', (req, res) => {
const html = ReactDOMServer.renderToString(<App />);
res.send(`
<!DOCTYPE html>
<html>
<body>
<div id="root">${html}</div>
<script src="client.js"></script>
</body>
</html>
`);
});
app.listen(3000, () => console.log('Server running on port 3000'));
```
When we talk about SSR delivering "fully rendered pages," it's important to understand what that actually means. Let's break it down:

A fully rendered page is an HTML document containing all the content users would get when they first load the page. This includes:

- The complete DOM structure
- All text content
- Image placeholders and other media elements
- Initial styles
Here's a basic example:

```
<!DOCTYPE html>
<html>
<head>
<title>My SSR Page</title>
<style>
/* Initial styles */
</style>
</head>
<body>
<header>
<h1>Welcome to My Site</h1>
<nav><!-- Fully populated navigation --></nav>
</header>
<main>
<article>
<h2>Article Title</h2>
<p>This is the full content of the article...</p>
</article>
</main>
<footer><!-- Fully populated footer --></footer>
<script src="hydration.js"></script>
</body>
</html>
```
In contrast, a client-side rendered (CSR) initial HTML might be like this:

```
<!DOCTYPE html>
<html>
<head>
<title>My CSR Page</title>
</head>
<body>
<div id="root"></div>
<script src="bundle.js"></script>
</body>
</html>
```
The CSR page relies entirely on JavaScript to populate the content.

**Faster Initial Paint**: The browser can start rendering content immediately.**Better SEO**: Search engines read all your content without executing JavaScript.**Improved Accessibility**: Screen readers and other assistive technologies can access content immediately.**Resilience**: Basic content is available even if JavaScript fails to load.
After sending the fully rendered HTML, SSR applications typically go through a process called [hydration](https://www.builder.io/blog/hydration-is-pure-overhead):

- The server sends the fully rendered HTML.
- The browser displays this HTML immediately.
- JavaScript loads and
*hydrates*the page, adding interactivity.
```
// Simplified React hydration example
import { hydrateRoot } from 'react-dom/client';
import App from './App';
const domNode = document.getElementById('root');
hydrateRoot(domNode, <App />);
```
This process allows for fast initial loads while still providing the rich interactivity of modern web apps.

Remember, while SSR provides these fully rendered pages, it's not without trade-offs. The server does more work, and you'll need to handle the state carefully between the server and the client. However, for many applications, the benefits of fully rendered pages make SSR a compelling choice.

Client Side Rendering (CSR) and Server Side Rendering (SSR) are two different approaches to rendering web pages. Here's a breakdown of their main differences:

- The server sends a minimal HTML file with a JavaScript bundle.
- The browser downloads and runs the JavaScript.
- JavaScript creates the page content and makes it interactive.
Pros:

- Smooth interactions after the initial load
- Fewer server resources are needed
Cons:

- Slower initial page load
- Potential SEO challenges
- The server creates the full HTML content.
- The browser receives and displays the pre-rendered HTML quickly.
- JavaScript then loads to make the page fully interactive.
Pros:

- Faster initial page load
- Better for SEO
- Works well on slower devices
Cons:

- It can be more complex to set up
- May use more server resources
Here's a simple visual comparison:

In essence, CSR works more in the browser, while SSR does more on the server. The choice between them depends on your project's specific needs, balancing factors like initial load time, SEO requirements, and server resources.

Server-side rendering can have a big impact on how search engines see your site. Let's break it down:

- Faster Indexing
Search engine bots are impatient. They want to see your content NOW. With SSR, your pages are ready to go when the bot comes knocking — no waiting around for JavaScript to load and render.

- Content consistency
SSR ensures that search engines see the same content that users do. With client-side rendering, there's always a risk that the bot might miss some dynamically loaded content.

- Improved Load Times
Search engines love fast sites. SSR can significantly cut down initial load times, which could give you a slight edge in rankings.

```
// Pseudo-code for search engine ranking
function calculateRanking(site) {
let score = site.relevance;
if (site.loadTime < FAST_THRESHOLD) {
score += SPEED_BONUS;
}
return score;
}
```
- Mobile-First Indexing
With Google's mobile-first indexing, SSR's performance benefits on slower mobile connections become even more important.

- Social Media Previews
While not strictly a search engine feature, SSR makes it easier to generate accurate previews when your content is shared on social platforms. This can indirectly boost your SEO by increasing engagement and backlinks.

```
<!-- SSR makes it easier to include accurate meta tags -->
<meta property="og:title" content="Your Dynamic Title Here">
<meta property="og:description" content="Your Dynamic Description Here">
```
SSR is a powerful tool for SEO, but it's not the only factor. Content quality, relevance, and overall user experience are crucial in search engine rankings. SSR simply ensures that search engines can efficiently crawl and index your content, potentially giving you an edge in visibility and performance metrics.

Implementing SSR doesn't have to be complicated. Let's cover at how to do it using Next.js, a popular React framework that makes SSR straightforward:

- Set up a Next.js project.
- Create server-side rendered pages.
- Let Next.js handle serving the fully rendered HTML and client-side hydration.
Here's a simple Next.js example using the [App Router](https://www.builder.io/blog/next-14-app-router):

```
// app/page.js
async function getData() {
const res = await fetch('<https://api.example.com/data>')
if (!res.ok) {
throw new Error('Failed to fetch data')
}
return res.json()
}
export default async function Home() {
const data = await getData()
return <h1>Hello {data.name}</h1>
}
```
In this example:

- The
`Home`
component is an async function, allowing for server-side[data fetching](https://www.builder.io/blog/safe-data-fetching). `getData()`
fetches the data we need.- The component renders the data directly.
Next.js automatically handles the SSR process:

- When a request comes in, Next.js runs this
[component on the server](https://www.builder.io/blog/why-react-server-components). - It waits for the data to be fetched.
- It renders the component with the fetched data.
- The fully rendered HTML is sent to the client.
- Once the JavaScript loads in the browser, the page becomes interactive.
This approach gives you the benefits of SSR without having to manually set up a server or manage the rendering process yourself.

If you don't want to reinvent the wheel, there are several frameworks that handle SSR complexities for you. Here's a rundown of popular options across different ecosystems:

- Angular Universal: The official SSR solution for Angular applications.
[Laravel](https://laravel.com/): Offers SSR capabilities through[Inertia.js](https://inertiajs.com/)or its own[Livewire component](https://livewire.laravel.com/docs/components).
[Ruby on Rails](https://rubyonrails.org/): Supports SSR through tools like[Stimulus Reflex](https://docs.stimulusreflex.com/)or[Hotwire](https://www.hotrails.dev/).
[Django](https://www.djangoproject.com/): Can implement SSR using libraries like[Django-Unicorn](https://www.django-unicorn.com/)or[HTMX](https://www.builder.io/blog/htmx-vs-react).[Flask](https://flask.palletsprojects.com/en/stable/#): Can be configured for SSR, often used with extensions like Flask-SSE.
Each of these frameworks offers its own approach to SSR, often with additional features like static site generation, API routes, and more. The choice depends on your preferred language, ecosystem, and specific project requirements.

When deploying an SSR app:

- Build both client-side and server-side bundles.
- Run the SSR server as a background process.
- Use a process monitor like PM2 or Supervisor to keep your server running.
Here's a basic deployment flow:

Don't forget about caching! Caching server-rendered pages can significantly reduce server load.

Builder.io provides support for server-side rendering (SSR) and static site generation (SSG) across all components and frameworks. This out-of-the-box functionality allows you to leverage the benefits of SSR and SSG without additional setup.

**Framework Agnostic**: Builder.io works with various frameworks that support SSR and SSG.**Automatic Optimization**: Builder optimizes your content for performance, including code splitting and lazy loading of off-screen components.**Dynamic Rendering**: You can render different content based on user attributes or[A/B tests](https://www.builder.io/c/docs/abtesting)while maintaining[SEO benefits](https://www.builder.io/m/explainers/seo-core-web-vitals).**Easy Integration**: Builder provides[SDKs and documentation](https://www.builder.io/c/docs/sdk-comparison)to seamlessly integrate your existing projects.
Here's a basic example of how you might fetch and render content server-side with [Builder and Next.js](https://www.builder.io/c/docs/custom-components-ssr-ssg):

```
import { builder, BuilderComponent } from '@builder.io/react'
builder.init('YOUR_API_KEY')
export async function getStaticProps({ params }) {
const page = await builder
.get('page', {
userAttributes: {
urlPath: '/' + (params?.page?.join('/') || '')
}
})
.toPromise()
return {
props: {
page: page || null,
},
revalidate: 5
}
}
export default function Page({ page }) {
return (
<BuilderComponent
model="page"
content={page}
/>
)
}
```
- Ensure you're using a framework that supports SSR or SSG.
- Follow your framework's guidelines for fetching data server-side when integrating Builder Pages or Sections.
- Refer to the
`getAsyncProps`
README for more information on handling server-side data.
By leveraging Builder for SSR, you can combine the flexibility of a [headless CMS](https://www.builder.io/headless-cms) with the performance benefits of server-side rendering, all while maintaining an easy-to-use [visual editing](https://www.builder.io/m/knowledge-center/visual-editing) experience.

Server-side rendering (SSR) is a powerful approach in web development that can significantly enhance your application's performance, SEO, and user experience. Throughout this article, we've explored what SSR is, how it differs from client-side rendering, its impact on search engines, and practical implementation strategies using popular frameworks like [Next.js](https://www.builder.io/m/nextjs-cms).

We've also discussed the concept of fully rendered pages and examined various SSR solutions across different ecosystems. While SSR offers many benefits, it's important to consider your project's specific needs when deciding whether to implement it.

**Q: How does SSR affect my development workflow? **
A: SSR can make development more complex, as you need to consider both server and client environments. You might need to adjust your build process and be cautious with browser-specific APIs.

**Q: How does SSR impact my site's Time to Interactive (TTI)? **
A: While SSR can improve initial content visibility, it might slightly delay TTI as the browser needs to load and hydrate the JavaScript after receiving the initial HTML.

**Q: Are there any security considerations specific to SSR? **
A: Yes, with SSR, you need to be more careful about exposing sensitive data or APIs on the server side. Always sanitize user inputs and be cautious about what data you include in the initial render.

**Q: How does SSR work with authentication and personalized content? **
A: SSR can work with authentication, but it requires careful handling. You might need to implement techniques like JWT tokens or server-side sessions to manage authenticated SSR requests.