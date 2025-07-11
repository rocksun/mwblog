There’s been a lot of buzz about [Remix’s announcement](https://remix.run/blog/wake-up-remix) that it will pursue a different direction, but in that hullabaloo, news about React Router got a little … buried.

[React Router](https://github.com/remix-run/react-router) may now be Shopify’s React framework, but it’s still a router for the [frontend](https://thenewstack.io/introduction-to-frontend-development). The plan is to keep evolving that offering while also managing the new framework “mode.”

The React Router team has been busy with a new governance model and rolling out support for [React Server Components (RSC)](https://thenewstack.io/react-server-components-in-a-nutshell/), which are [React](https://thenewstack.io/react-adds-new-experimental-animation-feature/) components that run on the server instead of the client.

The New Stack spoke with [Brooks Lybrand](https://www.linkedin.com/in/brooks-lybrand/), a developer relations manager for the e-commerce platform Shopify and a member of the steering committee for React Router. We asked Lybrand what becoming a framework means for React Router and what’s next for the open source project.

“On the React Router side, we are still releasing a bunch of new stuff,” he said. “The biggest, most exciting thing is our React Server Component support.”

The team has already released a preview of what that RSC support might look like, and this week, it will release RSC-specific APIs. The goal is to demonstrate how React Router APIs can implement [React Server Components](https://thenewstack.io/react-panel-frontend-should-embrace-react-server-components/), Lybrand said.

“It’s the way for you to actually enable React Server Components in your React Router app,” he said, adding that it will also be unstable at first.

## Remix and React Router Converge: Now What?

React Router and Remix are both the creations of Ryan Florence and Michael Jackson, who now work at Shopify. Last year at the React Conference 2024, the creators announced that Remix and React Router are merging. Remix will no longer be developed separately from React Router.

In effect, the team has rolled up the framework features into a React Router plugin, which is now the framework.

Since then, Jackson and Florence have announced they plan to create a [new framework](https://remix.run/blog/wake-up-remix) that diverges from the React-based Remix. There’s been a lot of speculation about what that means, but the developing duo have written it will be a “reimagining of what a [web framework](https://thenewstack.io/solidjs-creator-on-confronting-web-framework-complexity/) can be — a fresh foundation shaped by decades of experience building for the web.”

“This isn’t just a new version — it’s a new direction. One that’s faster, simpler, and closer to the web itself,” Jackson and Florence wrote in a May blog post. “To do that, we need to own the full stack — without leaning on layers of abstraction we don’t control. That means no critical dependencies, not even React.”

They’re starting with a fork of Preact, which is a mature virtual [DOM (document object model)](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) library already used heavily at Shopify and Google, they added.

Lost in the discussion has been what all this means for React Router, which is 11 years old this year.

> “We’re trying to support all these folks, so […] the framework mode is totally opt-in.”  
> **– Brooks Lybrand, developer relations manager, Shopify**

The convergence of React Router and the Remix framework drew [some Reddit criticism](https://thenewstack.io/why-some-developers-are-unhappy-with-react-router/), but Lybrand said downloads are up.

“We announced that we were [merging React Router to Remix](https://thenewstack.io/remix-react-router-merge-jetbrains-ide-for-test-automation/), and raw React Router usage went way up, at least judging by NPM downloads,” he said. “This wasn’t framework mode users. This was just like regular old React Router, your old router that you know and love, not the framework features.”

He pointed to React Router version 5, which was released five years ago and is still receiving millions of downloads every week.

“We’re trying to support all these folks, so what we’ve done is the framework mode is totally opt-in,” he said. “It’s a [Vite](https://thenewstack.io/development-server-vite-gets-independent-team-and-rust-ifies/) plugin at the end of the day.”

Vite is a frontend build tool and development server that’s become a popular foundation for meta-frameworks, including [SvelteKit](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/), [Nuxt.js 3](https://thenewstack.io/dev-news-react-19-nuxt-3-11-a-python-gui-tabnine-llms/), [Astro](https://thenewstack.io/new-astro-releases-incorporates-sessions-new-astro-actions-tools/) and [SolidStart](https://thenewstack.io/how-js-meta-framework-solidstart-became-router-agnostic/).

Developers can add the framework plugin or they can opt to use React Router as they always have since version 5, Lybrand said. It’s the basically the same API.

“We’ve had to change some minor things as React itself has changed, because we’re always trying to support the latest version of React and build the way that React wants us to build,” he said.

## The Three Modes of React Router

Lybrand described the new React Router as operating with [one of three modes](https://reactrouter.com/home):

1. The declarative mode, which is React Router as it’s been since v5;
2. The Framework mode, which incorporates the Remix features; and
3. The data mode or data routing, which is an API that Shopify needed but decided to share. It allows you to hook the router and data together, but provides freedom from any particular framework, he explained.

“That’s actually the first entry point that we’re trying to give people — here’s all the pieces you need to enable RSC with your bundler of choice or whatever,” he said. “Were going to build on top of these for our own framework mode, but we’re also giving you these Lego pieces.”

Data mode emerged out of support for RSC, he added.

“What happens on your server and then what do you actually send to the client? That conversation has to include the router,” Lybrand explained. “It decides what to show your user but it also decides what to load for your user. So that’s why we have the data mode, because it can actually couple your loading and your actions.”

RSC also cares about the data and what to render to the user, he added.

“That’s really important to React Server Components, because you can use your client directive to say, ‘Well, this little piece, it gets some JavaScript, but the rest of this stuff doesn’t get JavaScript,’” he said. “With all those details, React Router is the coordinator of those kind of pieces — saying, ‘Here’s your React Server Components [and] here’s where we should render these things, here’s all these pieces.’”

In data mode, developers can use Webpack or basically build their own frameworks, which many companies do, he added.

## Support for React Server Components

[React Server Components were introduced](https://dzone.com/articles/react-server-components-rsc-the-future-of-react) officially in 2020, but the first stable version didn’t hit until React 19’s release last year. If you wanted to implement RSC, it meant using Next.js or doing custom work, Lybrand explained.

That’s because [Next.js builds](https://thenewstack.io/how-to-build-a-carbon-aware-website-using-react-and-next-js/) on top of the most current version of React.

“We have never liked that strategy,” Lybrand said. “We’ve always viewed ourselves as, you get to own your dependencies as much as possible.”

React Router has been primarily used to build single-page applications (SPA), which load on the client side. By supporting RSC, it will be able to provide full-stack SSR (server-side rendering) apps. (Developer and educator [Josh Comeau](https://www.linkedin.com/in/joshwcomeau/?originalSubdomain=ca) has a nice explanation of [how RSC does this and how it differs from SSR](https://www.joshwcomeau.com/react/server-components/).)

This week, the React Router team plans to release APIs to show how its support for RSC might work.

“We’re not just giving it to the framework. We’re actually giving it at this data mode so that lots of React Router users can use it,” he said. “You don’t have to be bought into our Vite framework. You don’t have to be bought into how we do file-based routing and all that crap. You can just use it in your data router and enable React Server Components through React Router, which is very exciting.”

There will also be templates to help people get started using React Server Components, he added. (As of publication, it was  a [pull request](https://github.com/remix-run/react-router-templates/pull/139), but he said it will soon be merged.)

## Open Governance

Support for RSC isn’t the only new development for React Router. In May, Jackson announced the shift to an [open governance model](https://github.com/remix-run/react-router/blob/main/GOVERNANCE.md).

“React Router isn’t just mine and Ryan’s baby anymore. It is a mature OSS project with millions of dependents. We want everyone to have a say in how the project moves forward,” [Jackson wrote on X](https://x.com/mjackson/status/1927739177149382991). “To that end, we are introducing an open governance model for React Router. We are hopeful this will help the project continue to flourish and provide a stable foundation for anyone building on React.”

The five-person steering committee are all from the Remix team — for now — and it includes Lybrand. He and developer Matt Brophy, another member of the steering committee, wrote that [the team wants more feedback](https://remix.run/blog/rr-governance) and contributions from the wider React Router community.

“These changes to how React Router is developed are only a slight tweak to how we’ve been working for years, and will ensure React Router continues evolving for years to come,” Lybrand and Brophy wrote.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)