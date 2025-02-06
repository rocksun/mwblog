# Cross-platform mobile development with Expo
### Expo has quietly become one of the most popular tools for cross-platform development. Why is this, and how does Expo work? A deepdive with the Expo engineering team
React Native and Flutter are by far the most popular cross-platform development technologies, as previously covered in the deepdive, [Cross-platform mobile development](https://newsletter.pragmaticengineer.com/p/cross-platform-mobile-development). React Native (made by Meta) seems more popular in the US and UK, and at mid to large-sized companies, while Flutter (made by Google) powers more apps overall, globally.

But there’s also one other company that consistently comes up in talk about cross-platform mobile technologies: Expo. When the Bluesky team shared their cross-platform tech stack, they [mentioned](https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture) that it was React Native *and* Expo. Meanwhile, the React Native “getting started” guide strongly advises starting development with Expo, and calls it “a production-grade React Native Framework.”

So, what is Expo and why is it so important for cross-platform React Native development?

A year ago, I travelled to California and visited Expo’s offices in Palo Alto, meeting with the team to find out more; a few months later, I got back in touch for extra details on how Expo works, and to learn what makes it popular. This deepdive covers:

**Why is Expo popular?**It played a large role making React Native as widespread as it is today, and its developer focus has been a big factor.**History.**Expo began in dissatisfaction about the clunkiness of developing and shipping mobile apps. Today, a mission to make mobile development as seamless as web dev still motivates the team.**React Native vs a React Native framework.**Expo is a React Native framework, and the*only*production-ready one, to date.**Expo: developer tools.**Overview of tools Expo offers as open source, for free.**Shipping to production with EAS.**Expo generates revenue with its Expo Application Services (EAS): a freemium remote build and submission service. An overview of its wide-ranging capabilities.**Alternatives for shipping cross-platform apps.**Ionic Appflow, Shoebird, Fastlane, Bitrise, Codemagic.
*This deepdive features contributions from Expo’s co-founder and CEO Charlie Cheever, co-founder and CTO James Ide, and engineering manager Brent Vatne. Their input is appreciated!*
*As with every deepdive we publish, The Pragmatic Engineer has no commercial affiliation with the company featured, and was not paid to write about them in this article. More in our ethics statement.*
## 1. Why is Expo popular?
Expo is a startup based in Palo Alto, California, employing 32 people, 29 of whom are developers – a surprisingly high ratio of 90%. The company [lists employees](https://expo.dev/about) on its about page. *The ratio at larger software companies like Meta, Google, or Microsoft is rarely above 30-40%, due to the presence of other teams like sales, support, and many other support functions.*

Today, the open source Expo framework is used in more than 1 million public Github repositories, and has more than 800,000 downloads per week. The project is very active: more than 1,300 developers contribute in total, and there were more than 50,000 members of the Discord channel at time of publication.

**Expo may be the biggest reason why React Native became as popular as Flutter.** These days, when I hear a company develops with React Native, it almost always follows that they use Expo, too. This is because it has developer tools which make even the best cross-platform framework much less clunky to develop on for the iOS and Android native platforms.
For Flutter, similarly solid developer tooling which Google built and maintained has long been a differentiator; the search giant built [sophisticated tools](https://docs.flutter.dev/tools/devtools) to debug, profile and diagnose Flutter applications. However, getting started with Flutter still requires a [multi-step developer environment setup](https://docs.flutter.dev/get-started/install/macos/mobile-ios), while shipping iOS and Android apps is [a pretty involved process](https://docs.flutter.dev/deployment/android), compared with the simplest ways of getting started with React Native and Expo:

Just open the website *snack.expo.dev.*

This is the site called “Expo Snack,” where you can immediately start to do live editing on a React Native application that runs on an Android emulator, an iOS emulator, or a web view:

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86dd398f-6677-47a9-a13c-9e318d760966_1600x1110.png)
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86dd398f-6677-47a9-a13c-9e318d760966_1600x1110.png)
*An app built in two minutes without installing anything, running on a remote iOS simulator. Image:*
[Expo Snack](https://snack.expo.dev/)You can also run the app on your mobile device by scanning a QR code and installing the Expo Go app. I also did this – and the app live updated as I made changes. With such little effort required, this felt magical.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7f6ebe6-59f0-4910-b031-8faa11554cd2_1272x1128.png)
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7f6ebe6-59f0-4910-b031-8faa11554cd2_1272x1128.png)
Being able to live edit an app with zero development tooling feels magical, even in 2025. Developing with no tools installed locally is not possible when doing native iOS or Android development. Google’s cloud development environment, [Project IDX](https://idx.google.com/), comes close, but it’s not as snappy. Meanwhile, Expo Snack is just one of many developer-first features produced by Expo’s small team, that’s on a par with Apple and Google tools. *More below on Expo’s development tooling in the sections, “What is Expo?” and “Shipping to production.”*

Why do companies move to Expo? We asked the Bluesky engineering team, who are heavy React Native users – and whom we previously covered in the deepdive [Inside Bluesky’s engineering culture](https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture). Here’s what Paul Frazee – the dev who built the initial Bluesky’s iOS, Android, and web applications, using a single codebase – told us:

“We were initially manually building the app using Xcode and Android Studio, then uploading the builds.

The reason we first looked at Expo was to help us with deployments. Expo has a really solid cloud-build infrastructure (EAS Build) and over-the-air update system (EAS Update). We looked at the other React Native cloud build services and none of them seemed as well built, so we took a chance with Expo. We found ourselves iteratively adopting expo modules, and then moved fully into their framework. My only regret is that we didn’t start with it. It’s not often that I have such a positive experience.

We started migrating over to Expo around 9 months into app development, around February 2023. This was when we had a pretty mature app. It was an iterative migration that went pretty smoothly.”

## 2. History
As previously mentioned, Expo was founded out of frustration at how long it takes to build a mobile app. In 2012, Charlie Cheever was CTO at Quora and working on an iOS and Android app for the Q&A site. Being a hands-on developer with extensive web experience (he was an early engineer at Facebook), he assumed it would take at most a few weeks to build each native app. However, it actually took months per platform, and included terrible developer experiences on both iOS and Android; at least, compared to the web. From this came the idea for Expo. Charlie sums up the objective:

“The web is a pretty good way of doing development and it’s so powerful.

Let’s take everything that’s good about the web and web developmentand make the mobile development space better.”
He teamed up with James Ide and they started experimenting with ways of using web technologies to build mobile apps, eventually ending up with a framework that wrapped mobile-native components; basically something pretty similar to React Native. They were about to launch when React Native was released, which was created and used by Meta, with around 40 people working on it. In contrast, the as yet-unreleased Expo framework was developed by two people.

**Rather than compete with React Native, Expo decided to embrace it. **Charlie and James understood that *coding* an app was just one of the many parts of shipping a cross-platform app. Every developer using React Native still had other problem areas to solve:
Distribution to the iOS and Android App Stores

Release strategies

CI pipelines

Improving the developer experience

**“Exponent” was the first product the team shipped;** a React Native development tool that sat a level above React Native. The team [announced](https://www.youtube.com/watch?v=HaxZMDP6eDA) it in 2015 at a React conference called React Rally. It took care of things like:
Dealing with Xcode and Android Studio

Provisioning profiles for iOS

Development and deployment certificates

Any Objective-C, Swift and Java-specific things

The Exponent toolset kept evolving, and two years later in 2017, the name changed to Expo because it’s easier to say and remember. From 2017, Expo kept shipping new, major releases to Expo SDK several times per year. Back then, Expo’s SDK was on version 21; today, it’s on version 52. *The company maintains a changelog listing notable changes, and a detailed changelog.*

## 3. React Native vs a React Native Framework
Expo is a framework and set of tools that uses React Native (RN), and simplifies the development of RN applications. It also happens to be the only React Native Framework considered as production-grade, currently. But what is a “React Native Framework?” As React Native builds on top of React, let’s see how things work in the React world.

#### React vs React Frameworks
**React: providing core capabilities. **React is a JavaScript library for building web user interfaces.
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff87f67fb-f5ab-48f9-9fdd-e3363d5ab4be_1600x725.png)
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff87f67fb-f5ab-48f9-9fdd-e3363d5ab4be_1600x725.png)
*React code using the markup called JSX, a JavaScript syntax extension popularized by React which supports HTML-like rendering logic. Source:*
[React](https://react.dev/)React takes care of many things, like:

**High performance**: using a Virtual[DOM](https://en.wikipedia.org/wiki/Document_Object_Model), React creates an in-memory data structure cache of the UI, computes the resulting differences, and updates the browser’s DOM only as needed. This process is called reconciliation and produces better performance**JSX**: support for the JSX syntax extension to allow using HTML-like code within JavaScript**Reusable UI components:**the core of React is reusable components. React specifies how to define components, their lifecycle events, nesting,[communicating](https://react.dev/learn/passing-props-to-a-component)between them, rendering differently based[on different conditions](https://react.dev/learn/conditional-rendering), and[more](https://react.dev/learn/your-first-component)**Handling events**like clicking, hovering, keyboard inputs, swiping,[etc](https://react.dev/learn/responding-to-events).**UI state management:**an opinionated way to manage state. Instead of manipulating individual parts of the UI, React uses a[declarative approach](https://react.dev/learn/reacting-to-input-with-state)**Other features**like[support for TypeScript](https://react.dev/learn/typescript),[React Hooks](https://react.dev/reference/react/hooks)(using React features from components), and support for[server components](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components), among others.
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5cad761-bf99-4e9f-8f3c-ca3d9cbf3063_1600x814.png)
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5cad761-bf99-4e9f-8f3c-ca3d9cbf3063_1600x814.png)
*The simplest React component. The React framework specifies how to create these, and has support for even complex use cases for components. Source:*
[React](http://v)**React Frameworks: providing production-grade capabilities. **You can build web applications only using React. However, the more complex and larger an application gets, the more additional features must be built, like routing between pages, code-splitting between several files, fetching data, moving some rendering to the server, and so on. Here’s what the React team says about frameworks in the [getting started guide](https://react.dev/learn/start-a-new-react-project):
“You can use React without a framework, however we’ve found that most apps and sites eventually build solutions to common problems such as code-splitting, routing, data fetching, and generating HTML. These problems are common to all UI libraries, not just React.

By starting with a framework, you can get started with React quickly, and avoid essentially building your own framework later.”

The React team lists three “production-grade” frameworks, defined by:

Support for all features needed to deploy and scale apps in production

Open source

Can be deployed to a personal server or a hosting provider

React Frameworks which meet these conditions, and are recommended by the React team:

**Next.js:**the Pages Router of Next.js is a full-stack React framework. It’s versatile and lets you create React apps of any size, from a mostly static blog, to a complex dynamic application. Maintained by Vercel.**Remix**: a full-stack React framework with nested routing. It lets you break an app into nested parts that can load data in parallel and refresh in response to user actions. Maintained by Shopify.**Gatsby:**a React framework for fast CMS-backed websites. Its rich plugin ecosystem and GraphQL data layer simplify integrating content, APIs, and services into one website. Maintained by Netlify.
React is funded by Meta, but React frameworks are funded by other companies. Vercel and Netlify are hosting providers and fund the frameworks as it helps drive adoption of their services. Remix was acquired by Shopify, and is being [merged into](https://remix.run/blog/merging-remix-and-react-router#whats-happening-to-remix) React Router.

#### React Native vs a React Native Framework
Considering the differences between React and React Frameworks, it’s likely to be unsurprising that React Native has a similar concept split between “core” React Native features, and production-ready features which frameworks should provide.

**React Native offers core APIs and capabilities to build native apps. **It’s a framework that allows using the React programming paradigm to build native iOS and Android applications, which offers:
A runtime for JavaScript and the React syntax, with the ability to augment it using native iOS and Android extensions

Similar-enough performance to native-only applications

Continual support for modern React features like

[Suspense](https://react.dev/blog/2022/03/29/react-v18#new-suspense-features)(declaratively specifying the loading part of a component tree),[Transitions](https://react.dev/blog/2022/03/29/react-v18#new-feature-transitions)(distinguishing between urgent and non-urgent updates),[automatic batching](https://react.dev/blog/2022/03/29/react-v18#new-feature-automatic-batching)(grouping multiple re-renders into a single re-render for better performance) and othersAPIs

[to invoke](https://reactnative.dev/docs/next/turbo-native-modules-introduction)native iOS or Android APIsHot reloading: during development, see changes made in the code update on the emulator or device in around a second

**React Native frameworks provide production-grade capability: **The React Native team follows an RFC approach for discussions and proposals. In 2024, the team opened an [RFC for React Native frameworks](https://github.com/react-native-community/discussions-and-proposals/blob/main/proposals/0759-react-native-frameworks.md#what-do-we-recommend-to-react-native-library-developers) and arrived at the following definition of a RN framework:
“Shipping native apps to production usually requires a set of tools & libraries that are not provided by default as part of React Native, but are still crucial to hit the ship to production. Examples of such tools are: support for publishing applications to a dedicated store, or support for routing and navigation mechanisms.

When those tools & libraries are collected to form a cohesive framework built on top of React Native, we call this a React Native Framework.

A practical example of bespoke React Native Framework is how Meta uses React Native internally. We do have a collection of libraries, scripts and tools that make the integration of React Native easier with the various apps where it's used.”

**Expo: the only production-grade open source RN framework available today. **At the time of publishing, the React Native team only recommends Expo as a production-grade framework. This is a very strong recommendation, given that the same team also [writes](https://github.com/react-native-community/discussions-and-proposals/blob/main/proposals/0759-react-native-frameworks.md#what-do-we-recommend-to-react-native-library-developers) this about React Native frameworks:
“You’re either using a React Native Framework or you’re building your own React Native Framework”

So how did Meta end up recommending Expo? Charlie explains:

“I’d clarify the recommendation a tiny bit: the Meta team’s guidance about React Native is that you’re going to need to use

someframework with it to build anything real. If you don’t choose an off the shelf one, you’re going to end up having to build one yourself.
Today, Expo is the only very mature React Native framework.However, if tomorrow another team comes along and builds another really good React Native framework, everyone would welcome this.”
Collaboration with Meta started early, as Brent Vatne, engineering manager at Expo, recalls:

“A few of us have been contributors to React Native since the earliest days, the initial preview release at React Conf 2015. We’ve demonstrated through our involvement for nearly 10 years that we are deeply invested in the success of React Native, and can be relied on to collaborate on everything from conference talks to some of the largest initiatives on the open source side of the project.

For example, over the past year we have been working closely with the React Native team at Meta on getting the

[New Architecture for React Native]ready to roll out to open source. We helped prepare the ecosystem by migrating all of our tooling at Expo, using dependency statistics to determine the most impactful third party libraries and helping to migrate them, reporting and/or fixing related issues that we encounter in React Native, educating the community, and many other projects that come out of rolling out such a significant change.”
Expo seems to fill a gap in a way that helps Meta, by making React Native more accessible for external developers. Charlie:

“

Meta’s focus is mostly about making React Native work greatinsideMeta, and ours is to make it work greatoutsideof Meta.Meta doesn’t directly benefit from making React Native open source and most of their team’s focus is on making it work really well for them. So there’s a natural way that we’re able to fit together in a way that everyone wins!”
React Native by itself does not support tools necessary to deploy and scale an app that is production-grade. Meta has its own production-grade React Native framework, which is tailored to its needs and its [vast number of custom internal tools](https://newsletter.pragmaticengineer.com/p/facebook). So it’s a win for Meta to have a company building a more generic production framework to build React Native apps with.

## 4. Expo: collection of developer tools
Expo makes it easier to build production-grade React Native apps by providing additional abstractions (like routing) and tools (like a command line) to make building apps faster. It brings these added features to React Native development, built on top of React Native: