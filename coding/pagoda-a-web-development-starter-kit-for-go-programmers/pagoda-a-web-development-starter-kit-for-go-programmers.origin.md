# Pagoda: A Web Development Starter Kit for Go Programmers
![Featued image for: Pagoda: A Web Development Starter Kit for Go Programmers](https://cdn.thenewstack.io/media/2025/03/ca27c39e-andre-frueh-ldoxcohl7fw-unsplashb-1024x576.jpg)
In 2020, [Mike Stefanello](https://github.com/mikestefanello) fell in love with [Go](https://thenewstack.io/introduction-to-go-programming-language/).

“It’s the first time I ever said that I loved a programming language or even a technology or tool, but it was that kind of reaction — I just really, really fell in love with it,” the software engineer said. “I knew I wanted to work with it.”

Stefanello also did a lot of [web development](https://thenewstack.io/web-development-trends-in-2024-a-shift-back-to-simplicity/) in the form of personal projects and at that time, most web development was [PHP](https://thenewstack.io/why-php-usage-has-declined-by-40-in-just-over-2-years/)-based. One day, he saw a Hacker News post asking developers what their web stack of choice was for personal projects.

“I sat there just thinking, ‘I actually don’t have an answer to that question,’” he said. “I don’t want to go back to all the stuff in PHP that I was using previously. I love Go. I’m very obsessive and I couldn’t not have an answer to that question.”

Out of that frustration and exploration, [Pagoda](https://github.com/mikestefanello/pagoda) was born.

“It was more about the love of Go and the love of web development,” he said. “It wasn’t like I was thinking about which language should I use to get into web — I started in web development.”

## Pagoda: A Starter Kit for Go
Pagoda is not a framework — Stafanello stressed this repeatedly. It’s a starter kit for web development that provides frontend and backend libraries glued together by Go code. The Go generates the [HTML](https://thenewstack.io/why-html-actions-are-suddenly-a-javascript-trend/) server-side to create the web pages.

The starter pack approach may seem strange to frontend developers who are used to a universe of [JavaScript frameworks](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/), but backend developers want to keep it simple if they have to work with the frontend, Stefanello told The New Stack.

“Most of us don’t want to have to switch languages, especially if you’re not using [JavaScript](https://thenewstack.io/three-javascript-proposals-advance-to-stage-4/) in the backend,” he said. “I can understand if you are, then you’re used to that ecosystem. But if you’re not used to it — and I’m really not, I haven’t really gotten hands-on with JavaScript in a very long time — it feels like a bit of a chaotic ecosystem, and it’s really hard to grasp.”

But that left him with the quandary of how to build a modern, sleek web app without [having to open up JavaScript](https://thenewstack.io/web-development-in-2023-javascript-still-rules-ai-emerges/) and commit to big frameworks, such as React and Vue, he said.

“Nothing at all against them,” he added. “They’re all amazing projects, obviously, but it just comes down to personal choice. If you’re a backend developer, you want to be focusing on the frontend as little as possible.”

But why not make Pagoda a Go framework? Because the Go community doesn’t seem interested in that, he said. Whereas in PHP, there’s a mega singular framework — Laravel — there’s not really an equivalent in Go, he said.

![A home page made with Pagoda](https://cdn.thenewstack.io/media/2025/03/9ff64751-pagoda_sample.png)
A sample home page made in Pagoda by Mike Stefanello. The functional website is included in the repo.

“If you’re new to Go, it’s confusing: Why isn’t there one and why don’t people like it?” Stefanello said. “But I think the more you use Go, the more you begin to appreciate that.”

[Pushup is an exception](https://thenewstack.io/pushup-offers-speed-of-go-in-web-development-framework/) in that it’s a Go web development framework. There is also [GoBuffalo](https://gobuffalo.io/), which notes on its site that it could be a framework, but instead describes itself as a “Go web-development ecosystem” that’s “mostly an ecosystem of Go and JavaScript libraries curated to fit together.”
Stefanello made the choice early on not to create a framework because he didn’t like the idea of being bound by a singular, mega framework.

“They tend to be overly bloated,” he said. “They tend to really force patterns where you have to do it.”

Also, developers tend to outgrow frameworks but then are locked in by the framework, he added. And then there’s the risk that the framework authors will stop maintaining it.

By comparison, starter kits let web developers [quickly jumpstart web development](https://thenewstack.io/pushup-offers-speed-of-go-in-web-development-framework/) without the drawbacks of a full framework, he added.

“The nice thing about the starter kit is it solves all those problems,” he said. “There are no strict patterns to follow. I provide some ideas and patterns and I glue things together just to make things easy and kind of get you up and running. But none of that is forced. There’s nothing strict about it.”

Even if he stops maintaining Pagoda, [web developers have what they need](https://thenewstack.io/web3-stack-what-web-2-0-developers-need-to-know/) to continue.

“I’m basically just doing a lot of the work for you, and then you can take over from there,” he said. “You don’t have to worry about if I stop maintaining it because as soon as you copy the starter kit, it’s yours — 100% of it’s yours. ”

## The Pagoda Frontend
Pagoda includes three libraries for the frontend:

- HTMX, which provides access to AJAX, CSS transitions, web sockets, and server events directly in HTML. “The beauty of something like HTMX is that it enables you to have that Ajax-type behavior where you don’t have to do full-page reloads,” he said. “It’s the kind of functionality you expect or you see a lot on the JavaScript-driven
[single-page apps](https://thenewstack.io/secure-single-page-apps-with-cookies-and-token-handlers/). You can use as much or as little as you want but without having to write a line of JavaScript, you can take regular HTML and create really good interactivity on your site.” - Alpine.js, which Stefanello said was much like JQuery, but for the modern web. It’s a minimal tool for composing behavior directly in markup. “What’s really nice about it, too, is that it all works inside of — for the most part — your HTML, so you don’t even have to actually write standalone JavaScript,” he said. “You can just add a bunch of Alpine tags and some declarations and tell the HTML what to do. And it’s really quite remarkable how far you can get with that. It’s a project that I really enjoy using.”
- Bulma, an easy-to-use CSS framework. “It’s just really easy — you just throw some classes and you have a pretty decent-looking UI,” he said.
If you don’t like those libraries, you can switch them out. For instance, Tailwind could replace Bulma, he said, and it can be done in minutes.

## The Backend of Pagoda
On the backend, Pagoda includes:

- Echo: A high-performance, extensible, minimalist Go web framework.
- Ent: A powerful ORM for
[modeling and querying data](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/). [Gomponents](https://www.gomponents.com/): HTML components written in pure Go. They render to HTML 5, and make it easy to build reusable components.
Again, Stefanello stressed that any of these libraries could be replaced — in fact, this month, he replaced Go templates with Gomponents.

“If you ever go through any of the Go communities, whether it’s Reddit or Slack or Discord or whatever, there’s a lot of frustration with the template — especially when it comes to HTML, they do leave a lot to be desired, “ he said.

He enumerated the problems: They aren’t type-safe; if the code has an error, you can’t tell until you run the application; it’s difficult to pass data between different templates; and finally, it’s tricky to get them to compile in a way that’s easy to use within a web application.

Gomponents is a library created by [Markus Wüstenberg](https://github.com/maragudk), and it renders to HTML 5, making it easy to build reusable components.

“That was probably the single biggest code change that I made in the project […] since the project started,” he said. “This was a big fundamental change, to go away from the Go standard library templates to using a third-party solution.”

SQLite provides the primary data storage as well as persistent, background task queues, according to the documentation. However, it can be swapped out if a [developer prefers to use Postgres or Redis](https://thenewstack.io/vercel-offers-postgres-redis-options-for-frontend-developers/).

The project has even been forked to create [GoShip](https://github.com/leomorpho/GoShip), which is a Go plus HTMX boilerplate with all the essentials for SaaS, AI tools or web apps.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)