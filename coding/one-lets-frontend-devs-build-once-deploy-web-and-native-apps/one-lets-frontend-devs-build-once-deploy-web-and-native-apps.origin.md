# One Lets Frontend Devs Build Once, Deploy Web and Native Apps
![Featued image for: One Lets Frontend Devs Build Once, Deploy Web and Native Apps](https://cdn.thenewstack.io/media/2025/04/9157e63c-one_framework_react-1024x576.jpg)
A new React framework enables developers to create both web and native platform applications. Called, poetically enough, One, it stands out from other options in that it will generate [single-page applications (SPAs](https://thenewstack.io/secure-single-page-apps-with-cookies-and-token-handlers/)), [static-site generation](https://thenewstack.io/nue-a-new-static-site-generator-taking-on-next-js/) (SSGs) and server-side rendered (SSRs) web pages.

It runs on [Vite](https://thenewstack.io/vites-new-rust-based-javascript-bundler-available-in-beta/) and is the brainchild of [Nate Wienert](https://www.linkedin.com/in/nathan-wienert-89091945/), a software developer who previously worked at Vercel and is now a staff engineer at software development firm Uniswap Labs. Wienert also created the React-based UI library [Tamagui](https://tamagui.dev/) and [Takeout](https://tamagui.dev/takeout), which is a starter-kit for Tamagui.

## A Framework Packaged as a Vite Plugin
One targets web and native with a [single Vite plugin](https://github.com/onejs/one). [Developers](https://roadmap.sh/roadmaps?g=Web+Development) can create with One, which then outputs both [React Native](https://thenewstack.io/cross-platform-ui-framework-lynx-competes-with-react-native/) for mobile and [React](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/) code for the web. It also adds file-system routing, render modes, loaders, middleware, a command line interface (CLI) and [Hono](https://hono.dev/).

“If you do want to build a native app and you want to build a web app, that’s where it really shines,” Wienert told The New Stack. “You can share code, so you can write less code, and you can target both platforms and still get pretty good — pretty great, honestly — user experience and performance.”

That said, developers can also use it as a development tool to create either.

“I do think the fact that we focus so much on making a really nice experience makes it good for both, but the real shining use case is definitely sharing code across both,” he said.

## Developing for Simplicity
Wienert is a programmer who values simplicity. He remembers as a kid how [Ruby on Rails](https://thenewstack.io/dhh-wants-to-make-web-dev-easy-again-with-ruby-on-rails/) made it 10 times easier for him to create.

“As a kid, I was able to go from barely able to make anything to suddenly making all my ideas,” he said. “The big thing that Rails did was: all those annoying things that weren’t really directly related to what you’re trying to build, [it] made them very easy.”

That’s not always the case in development. Sometimes, he said, developers seemed to want to make development interesting in “weird” ways.

“I don’t care to learn your crazy, esoteric, genius solution that you came up with for, like, authentication,” he said. “I just want to make my authentication work as simply as possible, because 99% of authentication systems are all the same.”

During the pandemic, Wienert created Tamagui because he was working on a big app that he wanted to work cross-platform, supporting both web and native.

“The inspiration is more of a Rails-like experience, where it’s just very simple; it’s very clear, you’re not duplicating things.”

— Nate Wiener, creator of One and Tamagui
“In building that, I noticed there was nothing good to share UI between native and web — everything had big problems,” he said. “I built Tamagui to solve those and I think that was quite successful.”

At the time, he thought the best solution was to take a [Next.js app](https://thenewstack.io/build-a-real-time-bidding-system-with-next-js-and-stream/) and an [Expo](https://thenewstack.io/expo-vs-flutter-how-to-choose-the-right-mobile-framework/) app, then glue them together using [Solito](https://github.com/nandorojo/solito), which was a library created by a friend of his, [Fernando Rojo](https://github.com/nandorojo/solito), who is now head of Mobile at Vercel. It worked but proved frustrating.

“We’ve got all these new amazing things, way more powerful, way better experiences that we can build, but the actual [experience of it as a developer](https://thenewstack.io/developer-experience-devs-shouldnt-have-to-figure-it-out/) is just terrible,” he said. “It’s so much more code, so much less elegant and there was nothing better at the time.”

That became his motivation for creating a framework that could unify all of it in a simpler way, while writing once, he said: “The inspiration is more of a Rails-like experience, where it’s just very simple; it’s very clear, you’re not duplicating things.”

## Why Vite Over Metro
One began as an experiment by forking [Expo Router](https://docs.expo.dev/router/introduction/), which is a file-based routing library for React Native and web applications, built on top of [React Navigation ](https://reactnavigation.org/)for navigation. But it uses [Metro as the bundler](https://metrobundler.dev/), which he found to be “kind of a mess” and a pain to use. And the combo was not good at the web.

He preferred Vite, which is good at the Web but doesn’t output React Native-compatible JavaScript bundles. It was easier to make good at Native than to make Metro good at the web, he added.

“We had to spend a lot of time, too, making a lot of different packages work that with the more modern and more like valid syntax,” he said. “Vite is just the best in so many ways. It’s so clean, it’s very beautifully designed.”

While One is a framework, it’s packaged as a Vite plugin, he added. It also, he said, detects [CommonJS](https://www.freecodecamp.org/news/modules-in-javascript/) packages and automatically supports them as well.

Another differentiator for One is that it’s being developed alongside [Zero](https://zero.rocicorp.dev/), which is a [new breed of sync engine](https://thenewstack.io/how-a-new-breed-of-sync-engines-solves-frontend-problems/) that’s currently in public alpha. Wienert is friends with the creator of Zero, [Aaron Boodman](https://github.com/aboodman).

## Ready by Year End
Both One and Zero are a “little early,” Wienert said, but he believes they represent the future of [frontend development](https://thenewstack.io/introduction-to-frontend-development).

“I’m a big believer that that’s the future of — not just Zero — but sync engines in general,” he said. “This style of software, I think, is going to be how most people write most apps and websites in the next 10 years.”

Developers are welcome to experiment with One now, but it’s not quite ready for prime time, he cautioned. There is a [demo app on Test Flight](https://testflight.apple.com/join/aNcDUHZY), but it’s not accepting new testers at this time. The team is also building a complex cross-platform chat application, similar to Discord, so developers can see what it’s capable of. The team plans to add tooling and a way to host, as well.

One should be ready for real-world deployment towards the end of the year, he added.

“Our goal is just to make it stable, reliable and work really well, and then the Zero integration is really important for us to show,” he said. “If there’s anything we’re focusing on, it’s making it as easy, nice and clean as possible.”

See how One stacks up against other cross-platform frameworks:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)