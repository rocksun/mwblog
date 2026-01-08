After 20 years in software, full-stack developer [Yaniv Soussana](https://www.linkedin.com/in/yaniv-soussana-408a4a137/?originalSubdomain=il) is tired of complexity in React-based JavaScript frameworks. So the creator of the app conversion tool [Wappaa](https://wappaa.com/) did what developers tend to do: He built a new framework, called [Sigment](https://sigment.dev/).

“I wanted to create something better than [React](https://thenewstack.io/web-development-in-2025-ais-react-bias-vs-native-web/) and [Angular](https://thenewstack.io/angular-v21-adds-signal-forms-new-mcp-server/), because I’m already tired of all this — I wanted to create something simple for developers,” he said.

Sigment simplifies by exemption, which means it does *not*:

* Combine HTML with JavaScript;
* Use JSX; or
* Create a virtual DOM.

So when would you use Sigment?

Well, for starters, if you’re [fed up with React-based frameworks](https://sigment.dev/blogs/sigment-vs-react/) or don’t want to learn React, it might be a good option. The [open source framework](https://github.com/sigmentjs) claims to have a maximum runtime performance with minimal overhead, full control over rendering with a API, zero-config development without transpilation, and fine-grained reactivity.

Let’s dig in.

## The Problem With Mixing HTML and JavaScript

React mixes JavaScript with HTML syntax (JSX), and, frankly, Soussana isn’t a fan. Sigment does not mix the two, which he says makes the syntax shorter and easier. This makes the framework more accessible to those who know vanilla JavaScript but don’t want to learn React (which created and uses JSX).

That makes it possible for the framework to do more than build single page applications; it also supports an HTML first-architecture, he said. Plus, Sigment supports dynamic or incremental rendering.

“The developer can create a small website and then when the user starts to move, it will, on time, on the fly, create the new element and everything,” he explained, adding it will also put that element into the cache for better performance.

## Why Sigment Doesn’t Use JSX

JSX stands for JavaScript XML. It’s a syntax extension that allows developers to write HTML-like code directly inside their JavaScript.

For context, React relies on JSX syntax, as do other React-based frameworks. Preact, Qwik and Solid JS also use JSX. With JSX, developers write JavaScript that generates HTML.

The issue with JSX is it requires transpilation, or conversion, of the code, plus additional tooling such as Babel, Webpack or Vite. And while that feels declarative, it adds complexity to the build process, according to Soussana.

Sigment relies on Templates, which means the UI is written in a specialized version of HTML that the framework engine understands. Svelte, by the way, also [rather famously uses this approach](https://svelte.dev/blog/virtual-dom-is-pure-overhead), as do Angular and Vue.

Instead of JSX, Sigment relies on JavaScript tag functions. Instead of writing:

`<div class="container">`,

…a developer might write:`div({ class: 'container' })`.

This results in “lightning-fast” performance and faster iteration because the code is already valid JavaScript, according to Segment’s website. Also, because Sigment doesn’t use JSX, developers can create websites with pure HTML and simple syntax, Soussana told The New Stack. It also means the framework works without creating a virtual DOM, he explained.

## No Virtual DOM

I asked Soussana why he decided not to use a virtual DOM, which is a lightweight, simplified copy of the “real” DOM; i.e., the actual HTML elements on the screen. A virtual DOM acts as a “drafting board” between the developer’s code and the actual browser.

Soussana pointed out that Svelte and SolidJS also do not use the virtual DOM.

“We are in the new generation,” he said. “We don’t need the virtual DOM anymore. It’s just add[ing] more complexity and heaviness, and also, it takes more time to compile.”

Instead, Sigment uses Signals. Angular and Qwik creator [Miško Hevery](https://github.com/mhevery) once explained [Signals as a value you place in a bucket](https://thenewstack.io/angular-qwik-creator-on-how-js-frameworks-handle-reactivity/). He compared this to a traffic cop that tells the framework when there is access. When a Signal is read, the framework sends a message that someone read the value and it then goes on to the next value.

That makes the performance light, Soussana explained, adding that Sigment runs for the first time and then in the runtime, when the user needs something, it will render it and save it to the cache. The next time the user needs something, it can take it from the cache.

No virtual DOM and no JSX means a smaller bundle size as well, Soussana said, adding that this creates better performance and better experiences for the user and developer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)