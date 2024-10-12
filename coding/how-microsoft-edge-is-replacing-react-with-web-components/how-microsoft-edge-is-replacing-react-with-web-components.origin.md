# How Microsoft Edge Is Replacing React With Web Components
![Featued image for: How Microsoft Edge Is Replacing React With Web Components](https://cdn.thenewstack.io/media/2024/10/87a6c598-react-kick-1024x576.jpg)
When Microsoft’s Edge browser team [released WebUI 2.0](https://thenewstack.io/from-react-to-html-first-microsoft-edge-debuts-webui-2-0/) in May, a project that aimed to replace React components with native [web components](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/), its primary goal was to make Edge faster for end users. The core idea was that adopting a “markup-first architecture” would reduce JavaScript reliance on its product, which would mean less code to process on the client side — hence a better experience for the user.

To find out how the WebUI 2.0 project is going — including what inspired it and its ultimate goals — I spoke to [Andrew Ritz](https://www.linkedin.com/in/andrewritz/), who leads the Edge Fundamentals team at Microsoft.

But first, let’s quickly clarify what web components are. The community site WebComponents.org [describes them](https://www.webcomponents.org/introduction) as “a set of web platform APIs that allow you to create new custom, reusable, encapsulated HTML tags to use in web pages and web apps.” Ritz puts it this way, when advising his own team how to approach this web development paradigm: “Anytime you want to do a new control [and] you find yourself writing any JavaScript, pause — stop — talk to a senior engineer and ask, how do you solve this with HTML and CSS?”

## Why Did Microsoft Edge Decide to Ditch React?
Ritz says that his team’s aim is to convert around 50% of the existing React-based web UIs in Edge to web components by the end of this year.

But what was the impetus for the project — why did they decide they needed to move away from React in their web interfaces? Ritz explained that it began from looking at the work requests his “web desk” team at Edge was getting — “both external, to help improve the Chromium project, as well as internal requests.”

“…we [Microsoft] had adopted this React framework, and we had used React in probably one of the worst ways possible.”

– Andrew Ritz, Partner GM, Edge Fundamentals at Microsoft
An example of the latter was the Excel web app, which uses the Canvas element. So one of the questions they had to consider was, “How can we make Canvas more performant?” The HTML <canvas> element is used to draw graphics on the fly via scripting — and it’s usually done with JavaScript.

To help the web desk team deal with requests like this, Ritz wanted to adopt a more “opinionated approach” that would also address issues such as slowness in web apps.

“And so what we did is we started looking at, internally, all of the places where we’re using web technology — so all of our internal web UIs — and realized that they were just really unacceptably slow.”

Why were they slow? The answer: React.

“We realized that our performance, especially on low-end machines, was really terrible — and that was because we had adopted this React framework, and we had used React in probably one of the worst ways possible.”

The use of React within Microsoft kept getting compounded over time, as more teams used it for their UIs. So the company ended up with “one just gigantic bundle that everybody was depending upon,” said Ritz. It was a mess of bundle dependencies across web apps.

“It was just this terrible experience, especially on the lower cost, lower-end machines,” said Ritz. “We were seeing multi-second startup times for something that is ostensibly local. It was just, you know, shocking.”

## Edge Web UIs
Within Edge itself, there are between 50 and 100 web UIs, said Ritz, adding that “each of those are like their own little web application.” Around two-thirds of those Edge web UIs were built in React, before the Web UI 2.0 project started. Interestingly, the Edge team had originally used React in order to differentiate itself from Chrome.

“The team, as they were doing the port to Chromium, decided, well, we needed to add some kind of UI differentiation — different from what Chrome had — and so in the process of that, they did this kind of heavy conversion to React.”

So the current Web UI 2.0 project is, in a sense, rewinding much of the original development work done on Edge.

Ritz’s engineering team owned one of those React Web UIs: “browser extensions.” When you’re using Edge, it’s activated by clicking a heart icon in the browser bar, which opens up a sidebar. This then became the testbed to see what performance improvements could be made using web components for that UI, to replace the React components.

## Are Web Components Too Hard?
Recently yet another debate erupted on social media about web components versus framework components. [Ryan Carniato](https://x.com/RyanCarniato), creator of the SolidJS JavaScript framework, wrote a blog post with the provocative title, “[Web Components Are Not the Future](https://dev.to/ryansolid/web-components-are-not-the-future-48bh).” Essentially his argument is that a framework like SolidJS is able to do more than web components in certain scenarios, and is easier to implement. He dismisses web components as “a compromise through and through.”

In reply to Carniato, [Shoelace](https://thenewstack.io/shoelace-web-components-library-that-works-with-any-framework/) creator Cory LaViska argued that [web components offer stability and interoperability](https://www.abeautifulsite.net/posts/web-components-are-not-the-future-they-re-the-present/).

“The people actually shipping software are tired of framework churn,” wrote LaViska. “They’re tired of shit they wrote last month being outdated already. They want stability. They want to know that the stuff they build today will work tomorrow.”

LaViska also pointed out that web components don’t do all the things framework components do “because they’re a lower-level implementation of an interoperable element.”

It’s the kind of developer debate that rages endlessly on social media — it’s disappeared from *the daily feed* now, but you can bet it’ll be back in a month or two. In any case, I asked Andrew Ritz how his engineering team has adapted to web components and whether they’re as difficult to deploy as some critics claim.

“Our approach has been really to say, let’s use as many of the built-in constructs as possible,” he replied. “So as many of the built-in elements that exist within the browser, and it’s not been so bad to do this.”

“…effort to make web components perform well has definitely been an issue.”

– Ritz
Ritz noted that Edge developers have the advantage of using Microsoft’s own [Fluent UI framework](https://developer.microsoft.com/en-us/fluentui#/), which includes both React components and web components (among other types of components — such as mobile-centric ones for iOS and Android). But even using a company-wide framework to implement web components hasn’t been easy, he admits.

“There [have] been cases where [a] built-in control needs a lot of work — you know, it’s pretty heavy with polyfills, or things like that — that we’re just never, ever going to need. So effort to make them perform well has definitely been an issue.”

In terms of what Ritz calls “development agility” around web components (others might call it “[developer experience](https://thenewstack.io/how-do-you-measure-developer-experience/)“), he says that “we’ve actually seen some pretty good improvements.” For instance, being able to focus on HTML and CSS has meant that the developers and designers are aligned better — because they’re talking the same language.

“By us [the developers] focusing on using HTML and CSS, we kind of remove this entire translation layer, where somebody [in the dev team] might have to take, like, a wireframe and convert it to some other thing. […] And so that [was] a huge impediment to developer productivity for us, and we eliminate that entire loop.”

## On Widespread Adoption of Web Components
It’s fair to say that it’s easier for Microsoft’s browser team to implement web components than the average web development team. Apart from having Microsoft’s Fluent UI framework to call on, the Edge team is also building a software product that only needs to cater to one browser: its own. Whereas almost every other web dev team has to make sure their product is usable on a variety of different browsers: from Chrome, to Edge, to Safari, to Firefox, and others.

“We have an easier time, perhaps, because we can say we only depend upon Edge for our local things,” is how Ritz puts it. “That can be like this true expression of [the] modern, latest web. Whereas a website owner — gosh, they might be forced to support Safari, or something, that doesn’t support half of the constructs that we’d like…and that brings complexity.”

“I’d be good proof if we could get some of the bigger non-web component websites within Microsoft to move over.”

– Ritz
That said, Microsoft’s intention is to release some of its WebUI 2.0 packages as open source — as well as a set of “web platform patterns.” However, Ritz notes that many external developers might not want to do things exactly the same way — for example many developers would want to choose a different styling framework than Fluent UI. But at the very least, Ritz’s team will be able to provide “learning patterns” for others.

An intermediary step will likely be trying to convince other Microsoft web products to make the move to web components.

“I don’t know what the rest of Microsoft exactly will do,” said Ritz. “We [the Edge team] kind of want to get our house clean with […] a common library and whatnot. But I think I’d be good proof if we could get some of the bigger non-web component websites within Microsoft to move over.”

But he added that they’re open to external partners, to help lead the way to a [post-React world](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/).

“If we could find someone external that was meaningful, that wanted to partner on this — by all means, we would be delighted.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)