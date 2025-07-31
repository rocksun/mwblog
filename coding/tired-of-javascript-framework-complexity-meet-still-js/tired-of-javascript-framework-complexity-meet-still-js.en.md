Developer [Nakassony Bernardo](https://www.linkedin.com/in/nakassony-bernardo-8392879a/) faced a problem common in enterprises, no matter what industry: modernizing a legacy web application. Many of the older web interfaces did not use [JavaScript](https://thenewstack.io/introduction-to-javascript/) frameworks and lacked the capabilities that developers have today.

“It’s really hard for you to migrate those legacy applications, because they are really solving the problem they had back in the day, and to some extent, still usable for some problems they have today,” Bernardo said. “You cannot just say, ‘I’m going to get rid of whatever they used that time to start using a new, modern framework.’ It just doesn’t work, because you have to disrupt whatever is there and you also have to rebuild everything from scratch.”

## The Challenges of Updating Legacy Apps

Having to use [TypeScript](https://thenewstack.io/typescript-5-5-faster-smarter-and-more-powerful/) is a further complication, because it has to be transpiled to JavaScript.

“This is when things become really hard, especially when you’re dealing with those legacy systems,” he said. “Modernizing those applications required for you **not** to use those new JavaScript approaches, which means that you need to stick with pure JavaScript. Yet you need to bring those features that all the new JavaScript tools are providing — like state management, for example.”

For instance, he had one application that dated back to 2003, but it still solved the organization’s problem. For that reason, the company wanted to add some new features without disrupting the core.

Bernardo found the answer in vanilla JavaScript, which he has used in creating a new open source framework called [Still.js](https://github.com/still-js/core) (*Editor’s Note: Still.js was also the name of a React-based [static site generator](https://thenewstack.io/nue-a-new-static-site-generator-taking-on-next-js/), which is now archived.*) The framework allowed him to bring features like those enabled by [React](https://thenewstack.io/remix-3-and-the-end-of-react-centric-architectures/), [Angular](https://thenewstack.io/angular-v20-advances-zoneless-adds-support-for-ai-development/) or [Vue.js](https://thenewstack.io/a-peek-at-whats-next-for-vue/), without rewriting code. Still.js is only about a year old, but it provides a modular and component-based architecture that’s similar to those popular frameworks, he said.

”It offers a lightweight yet powerful approach to structuring applications, allowing for better maintainability and scalability without introducing a complex abstraction layer,” Bernado wrote in a [Medium post about Still.js.](https://medium.com/@sonybernardo/still-js-a-way-to-leverage-vanilla-javascript-for-complex-and-enterprise-level-web-development-34cd1c555061) “With Still.js, you get the flexibility of raw JavaScript while benefiting from an organized and efficient development workflow.”

## Still.js Use Cases

Still.js has other applications. For instance, it can be used to modernize an older React or Angular application, again without disrupting the legacy code.

While you can’t easily combine frameworks like React, Angular and Vue.js, you can integrate them with Still.js. Bernardo explained that this is because Still.js leverages the browser’s native capabilities directly, avoiding the complex tools and abstraction layers that often cause conflicts when mixing other major frameworks.

“If you are using React and try to combine it with Angular, you have to find a way also to combine the tools that they have behind these things to run their applications, but Still.js doesn’t tell you that,” Bernardo said. “You don’t have to use any kind of tool because it’s vanilla JavaScript.”

It can also be combined with other tech stacks, including applications that leverage [Java](https://thenewstack.io/introduction-to-java-programming-language/), classic [ASP](https://dotnet.microsoft.com/en-us/apps/aspnet) or even [PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/), he added.

## Architecture and Other Still.js Details

Still.js uses its own architecture approach called Service, Controller and View, because “it is quite secular [in] the way it handles and process the components, since it does not have a bundle/building process,” according to the [Still.js documentation](https://still-js.github.io/stilljs-site/architecture/).

[![Still.js uses an architecture called Service, Controller and View.](https://cdn.thenewstack.io/media/2025/07/394b5b87-scv-architecture.png)](https://cdn.thenewstack.io/media/2025/07/394b5b87-scv-architecture.png)

Still.js uses an architecture called Service, Controller and View. Image via the [Still.js website](https://still-js.github.io/stilljs-site/).

Service provides data to the view and takes care of transactions such as HTTP requests. The controller serves the view with different behavior and DOM implementation. View displays whatever needs to be shown to the user.

Still.js relies on object-oriented principles, Bernardo told The New Stack. When it comes to state management, it offers local state management and [global state management](https://thenewstack.io/how-to-simplify-global-state-management-in-react-using-jotai/).

“In Still.js, you have those state properties or state variables for your components, which has to do with the component itself, locally, how it will work,” Bernardo explained.

React introduced the virtual DOM as a lightweight, in-memory representation of the actual DOM. It provides a way to update the UI in a reactive way, but Still.js avoids such artificial layers, he said.

“If you start bringing more layers and layers, then to some extent, you are going to impact the performance,” he said. “I’m not saying that they are not addressing the performance issues in React, but what I’m saying is: Is it needed when it comes to updating the user interface reactively? Because it’s not needed, let’s try to avoid those kinds of implementations.”

## Other Ways Still.js Differs

Other frameworks have a building or compilation process, especially if there’s a need to transpile TypeScript to JavaScript.

“They get this processing time to transform everything that you have written to what needs to be rendered by the browser,” he said. “We don’t have that on Still.js, so it’s a runtime rendering approach. Whenever this component is being accessed or requested is when the rendering process starts.”

The framework uses regular expressions to look into templates. 80% of what is in the templates will be vanilla JavaScript, he added. There are some special directives, though, for HTML. The Still.js interpreter translates those into something the browser understands, he explained.

“This is how the render process works, but it’s everything on top of Still.js itself,” he said. “There is no other framework being used for rendering purposes.”

> 80% of what is in the Still.js templates will be vanilla JavaScript.  
> **– Nakassony Bernardo, creator of Still.js**

Still.js also does not require preprocessing, nor does it depend on bundlers like WebPack or Vite, according to Bernardo. This makes it “ideal for teams and developers who prefer direct, no-compromise access to native web technologies in addition to those modern features a web framework provides,” he wrote.

Not surprisingly, given why it was created, Still.js is suitable for enterprise and complex applications.

“Enterprise-grade web applications need more than just rich UI features. They require: modularization, user permission management, component routing, validation, separation of concern, communication management, microfrontend architecture (e.g. frontend embedding and interaction), and more,” he wrote. “Still.js supports all of these features natively without the burden of a bundler increasing build time and potential complexity or even tooling overhead.”

Still.js can also be used, as he mentioned, to create microfrontends in React. The framework allows developers to embed Still.js components in the existing application, but in such a way that the component can be a whole frontend, enabling access to features such as navigation, he wrote in another [Still.js Medium post](https://medium.com/@sonybernardo/rethinking-microfrontend-architecture-combining-still-js-f24862358847). Bernardo also elaborated on [microfrontends in a YouTube instructional video](https://www.youtube.com/watch?v=8dPNkNhpbkc).

## Still.js Vendor Components

Still.js offers a component-based UI and an HTML-based template. It has built-in notations/directives, user permission flow, component State Management, global state management, routing and form validation.

It even offers some things React doesn’t.

“If you bring up routing in React, you don’t get to add those kinds of data transfers when you are routing, you need to depend on the state management,” Bernardo said. “You are going to push this data to, let’s say, some kind of [Redux state management library](https://redux.js.org/), and then a sibling tool needs to go to Redux to check whatever is there and then start processing the data from there.”

Still.js can send the data no matter how big, he added.

It also offers a feature called vendor components, which is when a web developer needs a feature that isn’t part of the framework’s core. So far, there are only a few of these, but vendor components let developers create the capabilities with a new component — and then that component can be made available for reuse.

Still.js also offers a unique approach to built-in annotation by leveraging JSDoc and JavaScript comments, not for documentation but to dynamically add features at runtime, he explained on the [Still.js website](https://still-js.github.io/stilljs-site/). JSDoc is also used for typing and type hinting, enabling most TypeScript features, although he adds that “typing is generally optional, except in specific cases where it’s required.”

In Still.js, developers will find a complete framework, but it is still a young framework, so developers may encounter things that can be improved, Bernardo said, adding that he is open to contributions and suggestions.

“This is a very mature framework, but still it’s a young one, although you can build very big and complex kinds of things,” he said. “We are really open about any idea, any contribution.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)