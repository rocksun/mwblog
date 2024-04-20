# New Wasm Project Brings Web Components to Backend Languages
![Featued image for: New Wasm Project Brings Web Components to Backend Languages](https://cdn.thenewstack.io/media/2024/04/f193e4c1-hal-gatewood-werqau9ta-a-unsplash-1-1024x683.jpg)
WebAssembly basically allows non-frontend languages, such as Rust or Python, to run in a web browser. But web developer and
[Enhance](https://enhance.dev/) maintainer [Ryan Bethel](https://github.com/ryanbethel) wondered: Could you reverse that paradigm and use Wasm to run web components in Python or Rust environments?
The answer, it turns out, is yes. With a little tinkering, it is possible. Bethel and the Enhance team worked out the problems with that and on April 8 released
[Enhance Wasm](https://enhance.dev/wasm).
“In order for the
[Wasm ecosystem](https://thenewstack.io/wasmcon-2023-a-conversation-about-the-future-of-webassembly/) to do what it does, Rust and Python and Java and all these other runtimes can also execute Wasm,” explained [Brian LeRoux](https://www.linkedin.com/in/brianleroux/), CEO at [Begin](https://begin.com/), which created Enhance, and a web developer in his own right. “So we can now go the other way. We can take browser code and run it inside of [Java](https://thenewstack.io/why-wasm-wins-where-java-applets-failed/) or [Python](https://thenewstack.io/python-and-webassembly-elevating-performance-for-web-apps/) or [PHP](https://thenewstack.io/php-has-survived-for-26-years-because-it-keeps-evolving/) or [Rust](https://thenewstack.io/rust-gets-security-wasi-0-2-support-productivity-boost/) or whatever. We’re taking the Enhance interpreter, which generates HTML from web component definitions, and we’re compiling it into Wasm.”
The implications range from solving web problems like reusing headlines across digital properties of different languages, to possibly creating a global universal design where buttons, drop downs and other common design elements could be reused as components across languages, LeRoux explained.
## Web Development Goes Back to the Browser
To understand how it works, it helps to
[know about Enhance](https://enhance.dev/why-enhance), an open source full stack HTML framework. And to understand why Enhance matters, it’s helpful to consider the prolific adoption of [JavaScript](https://thenewstack.io/top-5-underutilized-javascript-features/).
Ten years ago, there were around 20 million programmers — now
[GitHub](https://thenewstack.io/github-developer-productivity-at-30-billion-messages-per-day/) puts that number at 100 million developers, LeRoux noted. Most of them have not become coders by learning lower-level programming languages such as Rust, he contended, but from learning HTML, CSS and JavaScript — and particularly JavaScript, which is the most commonly used programming language for 11 years running, according to the [Stack Overflow’s Developer Survey](https://survey.stackoverflow.co/2022/#technology).
“Our hypothesis is [that] the new largest segment of software developers are frontend and a lot of what they’ve learned, frankly, is also about ten years out of date,” LeRoux said. “There [are] a lot of assumptions around how we need to build for the frontend these days that are invalidated by the browser.”
But browsers have only continued to improve, LeRoux noted. Despite this, a lot of the assumptions around frontend today are about transpiling JavaScript so that it can be more modern and have “nicer syntaxes for things like components and modules,” he said.
“Good news: Browsers have both components and modules built in now,” LeRoux continued. “So needing a framework for that is — actually, to coin a cloud term — undifferentiated, heavy lifting.”
## Does React Create too Much Code?
JavaScript, and
[React](https://thenewstack.io/react-panel-frontend-should-embrace-react-server-components/) specifically, bring a whole bunch of code to the party to replicate components the browser can already create. This slows down the experience for users, he said.
“Enhance’s philosophy is to get back to writing for the platform, writing lower-level code for the browser,” he said.”Now. that’s not to say that the browser’s flawless and awesome. It’s got paper cuts all over the place, and there are difficulties in using things like web components at scale, and you hear about those all over the place. This isn’t just FUD. Plenty of ink [has] been spilled of people complaining about the state of the user experience, of the developer experience, for working with the lower level browser primitives; and so Enhance’s overarching goal is to make it fun to build with web components.”
When developers author a web component, they tend to write JavaScript that extends the HTML element, he said. But, most elements on a page are not actually interactive.
“Probably 90% of elements on a given web page don’t listen for JavaScript, don’t submit forms, don’t interpret scroll events or intercepts, form submits or clicks or whatever,” he said. “So we want to server-render web components and we don’t want to necessarily run client JavaScript.”
Enhance gives developers a page full of custom elements, he said. While developers can use JavaScript, they probably don’t need it, LeRoux added.
“In fact, you probably don’t want it because your performance is going to really suffer by doing all this extra work,” he added.
The average website has one or two megabytes of JavaScript. LeRoux pointed to Enhance’s home page, which, despite rich animations, has only four or five kilobytes of JavaScript and relies instead on
[HTML](https://thenewstack.io/html-markup-tips-for-developing-accessible-websites/) and [CSS](https://thenewstack.io/css-frameworks-in-vogue-but-dont-forget-style-fundamentals/).
“Our hypothesis is [that] the new largest segment of software developers are frontend and a lot of what they’ve learned, frankly, is also about ten years out of date.” –Brian LeRoux, web developer and CEO at Begin
This is radical news for people who were taught that React JavaScript is required to build a website. One of the challenges people have with using Enhance is that, for instance, React will allow you to pass complex objects to attributes. HTML does not allow that; attributes are only used to pass styles, not complex objects. This kind of thing often surprises a React developer, he said.
“React papered over how the browser works, and it creates an uncanny valley and this is actually really kind of awful learning for a lot of people,” he said. “If you’re a web developer, and you’ve been building sites with React for a decade, it’s a bit of a cold shower to realize you don’t know how the browser works and it can be disappointing and upsetting. So they go through the full range of emotions, where they start off angry and then they despair, then they accept and move on.”
![Enhance's code](https://cdn.thenewstack.io/media/2024/04/bef3721f-enhance-code.png)
Brian LeRoux, CEO at Begin and a developer, shows code used from the Enhance website.
A lot of reasons to use JavaScript have disappeared as browsers have progressed, he added.
“We can be very productive working with the basics of the web,” LeRoux said. ”We have auto-updating, super backwards compatible web browsers now that can load a website from the ’90s just as good as it [can] load a website from today, and we don’t even have to tell it to update anymore, and we’re not leveraging that anymore as much as we should be.”
Enhance is for those who are super performance-focused and want to build sites that last, he said.
“I feel with the modern
[JavaScript frameworks](https://thenewstack.io/jamstack-panel-multiple-javascript-frameworks-are-a-good-thing/), they break a lot and they’re very brittle and every year there’s a new big conference where they announce all the breaking changes and everyone cheers; and I’m like, well, you’re cheering for unplanned work […] to deliver a webpage,” he said. “So there’s some soul searching to be done by the industry, for sure, on that topic.”
## Creating Enhance Wasm
Bethel read about Shopify’s experiment using
[Qwik.js](https://thenewstack.io/javascript-on-demand-how-qwik-differs-from-react-hydration/), a newer JavaScript runtime that’s designed to be small. Shopify hypothesized that they could take the interpreter, compile it with Wasm, bundle it with some JavaScript, and run that JavaScript in any runtime that supported Wasm. Bethel and the Enhance team wanted to see if they could go the other way and run web components inside other languages.
The team took the Enhance interpreter, which generates HTML from
[web component](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/) definitions, and compiled that into Wasm, he explained. It took about ten prototypes to get a solution that worked well, he said — the secret ingredient came from a startup called [Extism](https://extism.org/), a cross-language framework for building with WebAssembly.
“Extism gave us the ability to really take this code and run with it across all these different platforms quite quickly,” he said. “Wasmtime [a runtime for WebAssembly], we couldn’t get working in Java, and there was another one that we couldn’t get working on PHP unless we did native shelling, but now we have it working everywhere. The idea would be that you write one set of web components, and you can run them in any backend.”
The team introduced
[Enhance in an April 8 blog post](https://begin.com/blog/posts/2024-04-08-introducing-enhance-wasm), calling it a “leapfrog moment for frontend development.”
“
[Server-side rendering](https://thenewstack.io/spas-and-react-you-dont-always-need-server-side-rendering/) is a key requirement for personalized web applications,” the team wrote. “Organizations that prioritize the stability, performance and accessibility of web standards run workloads in a huge variety of backend runtimes. Now we can build browser native web interfaces that cross the runtime chasm.”
Enhance Wasm, which is open source, launched with support for
[Node](https://thenewstack.io/why-viable-uses-next-js-and-node-js-for-ai-applications/), [Deno](https://thenewstack.io/with-additional-funding-deno-sets-out-to-challenge-node-js/), Python, Ruby, PHP, Java, C#, Rust, and [Go](https://thenewstack.io/go-language-riding-high-with-devs-but-has-a-few-challenges/).
## Enhance Wasm Use Cases
Upon release, Enhance saw developers immediately using it to repurpose headline styles across web properties. It’s particularly useful in large companies that have grown through acquisition and may have four or five different technology sections completely divorced from one another, said LeRoux. For instance, his wife works at the large tech firm
[LaunchDarkly, which has multiple systems from acquired startups. It’s a major headache to maintain a design system across them because they have a blog in PHP and a Go app and different technologies implemented across the different digital properties, he said.](https://launchdarkly.com/?utm_content=inline+mention)
“If you have to maintain a design system across the things you’re re-implementing for each one of these runtimes,” he said. “With Enhance Wasm, we could do all these definitions with web components, and run them in all of these properties from one set of definitions, and that’s that’s why this is compelling.”
The team has also spoken with noted designer
[Brad Frost](https://bradfrost.com/), who has the idea of a global design system similar to Google’s Material or Salesforce’s Lightning, but meant to be used by everyone.
The Enhance team has also joined the W3C
[Web Components Working group](https://www.w3.org/community/webcomponents/) and the [Open UI group](https://open-ui.org/).
“The end game would be [to] get a lot of this in the browser itself,” Le Roux said. “We shouldn’t be necessarily sharing these design systems for buttons —that should just be built into the platform by now… Tabs or carousels or accordions or whatever, every website has these things. Being able to have a kind of blessed set of these components that works everywhere, ideally without client JavaScript, would be nice.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)