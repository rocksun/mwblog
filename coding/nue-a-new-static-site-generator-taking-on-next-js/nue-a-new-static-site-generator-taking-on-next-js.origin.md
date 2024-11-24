# Nue: A New Static Site Generator Taking on Next.js
![Featued image for: Nue: A New Static Site Generator Taking on Next.js](https://cdn.thenewstack.io/media/2024/11/fe236261-getty-images-fv_jinocbla-unsplashb-1024x576.jpg)
How goes the war? The war against… bad caching, slow load times, security breaches, scalability problems, SEO, or whatever we are told we have to fight this month when developing for the web. Web development is a treadmill of innovation that you can never really leave if you want to keep up.

Looking at new web technology is similar to remembering the timeline of a war. We had HTML, CSS and Javascript on the client. This was quick but hard to develop with. Then we got [React](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/), which made reusable components manipulating the Document Object Model (DOM) the default. We were told that using Declarative methods was better than Imperative ones. Then we had [Next.js](https://nextjs.org/) (and [Vue.js](https://vuejs.org/)) built with React, which used server-side rendering by default but allowed for a client-side approach for static site generation and the [JAMstack](https://thenewstack.io/jamstack-style-build-a-website-with-netlify-and-publii/). And so it goes.

Now we have [Nue](https://nuejs.org/blog/nue-release-candidate/), which is “a content-first framework optimized for progressive enhancement.” It has hit release [candidate one](https://nuejs.org/blog/nue-release-candidate/), as we reported [last week](https://thenewstack.io/angular-version-19-scheduled-to-release-tuesday/#nue). Where does progressive enhancement fit in? This is an old principle that your site should work with all browsers, with CSS and JavaScript being used only for enhancing features. This ultimately means that your site should be able to work without JavaScript — but I have my doubts whether that is a reasonable expectation today.

Now, the thing that attracted me immediately was that it appeared to be [markdown](https://thenewstack.io/obsidian-and-the-case-for-using-more-markdown/)-first. This does encourage a design-led approach. Nue is “not currently tested or developed under Windows,” which is either fine or non-serious depending on, er, which side you are on. I always start with my MacBook, so this is fine for me.

## Getting Started
OK, so I’m a willing recruit for this new skirmish. Let’s get to [basic training](https://nuejs.org/docs/installation.html).

I had no idea what “Bun” was; apparently it’s a combined bundler and JavaScript runtime, which is recommended by Nue.

So first install Bun. This was quick:

And it politely added itself to my script. So, starting a new [Warp](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) shell, I install Nue itself with Bun:

…and create the template project:

Eventually, it starts a server and whisks me off to the site at [http://localhost:8083/](http://localhost:8083/).

This site is quick and very nicely designed. This template project, a blog, reacts sensibly to size changes:

I looked forward to seeing how [this was composed.](https://nuejs.org/docs/tutorial.html) But let’s look at the project structure first.

If we cut out images, CSS and JavaScript and just look at the blog content directory, we get a feel for the structure:

As is common, we get a *.dist* output development directory that shows that Markdown files (.md) are converted to HTML files. We can also see a few YAML files that will no doubt hold metadata. Also, note the *@global/layout.html.*

Indeed, the *site.yaml* seems to contain quite specific layout options:

12345678910111213141516171819 |
navigation: header: - Emma Bennet: / - Contact: /contact/ footer: - © Emma Bennet: / - image: /img/twitter.svg url: //x.com/tipiirai alt: Twitter (X) profile size: 22 x 22 - image: /img/github.svg url: //github.com/nuejs/nue/ alt: Github Projects size: 22 x 22 - image: /img/linkedin.svg url: //linkedin.com/in/tipiirai alt: LinkedIn profile size: 22 x 22 |
The footer, which I didn’t capture in the above image, starts off looking like this:
I was naturally intrigued to see if I could make a fairly obvious update. After adding the BlueSky svg:

And editing the site.yaml:

This updated the footer immediately:

You’re welcome! This also gives us a clue as to Nue’s Declarative nature.

The headers and footers are arranged via the *@global/layout.html* and `<navi>`
tags:

They read the data in the *site.yaml* and create those footer items from that. You can already see that the HTML and CSS are tucked away under the stairs as slightly second-class citizens. That suits me fine, but it may upset more code-first developers.

Let’s get into more content detail. The Nue docs site seems to have no search, so you will need Google to penetrate it for details.

Nue leads with Markdown files for content; it supports standard Markdown and then extends it quite a lot. This means if you know Markdown (which you should), you only have to spot the odd discrepancies. Let’s look at the front page, *index.md*; note that my Warp shell is happy to open Markdown and renders it side by side:

We see the “front matter” metadata between the three dashes and the “page-list” block tag that will clearly be used as a container. The front matter mentions the “blog” content collection. That maps to the *blog* folder, which contains the blog entries. Let’s look at the latest entry:

The front matter is used to make a little box for the entry in the page list, consisting of the “thumb” image and the title text, which we saw above on the web page. It creates this *index.html* file in the output directory:

12345678910111213 |
... <li> <a href="/blog/class-naming-strategies.html"> <figure> <img src="/blog/img/dashboard-thumb.png" loading="lazy"> <figcaption> <time datetime="2024-03-13T00:00:00.000Z">March 13, 2024</time> <h2>CSS class naming strategies for scaleable dashboard design</h2> </figcaption> </figure> </a> </li></ul> |
You can see the result in the last blog entry in the web page image.
If you click through, the blog entry itself contains a large hero area, as we can see:

This is specified in the re-usable *blog/hero.html*; it has some templating for variables:

12345678 |
<header @name="pagehead"> <h1>{ title }</h1> <p> <pretty-date :date="pubDate"/> • Content by AI • Photo credits: <a href="//dribbble.com/{ credits }">{ credits }</a> </p> <img :src="og" width="1000" height="800" alt="Hero image for { title }"> |
You can see that it has pulled the value of “title” and “credits” from the Markdown front matter. Note that `:date`
and `:src`
are also bindings.
## Islands
Islands are intended as dynamic components sitting in the otherwise static HTML. Nue allows a hybrid server and client mix and can use [web components](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/). These are also recognized as an ideal way to integrate React components, so this is likely the starting point for those wanting to move across from other server-side projects.

## Conclusion
Looking past the slightly bombastic manner in which the docs are written, I do like the Markdown first approach — even if this just means the workhorse files are kept separate. There are plenty of other concepts to dig into, but this design-led approach is probably the only reason why a developer would jump ship. However, for a young project, this already has a fresh take on web development.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)