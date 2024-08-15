# Expo vs. Flutter: How to Choose the Right Mobile Framework
![Featued image for: Expo vs. Flutter: How to Choose the Right Mobile Framework](https://cdn.thenewstack.io/media/2024/08/4f1340e6-computer-chip-6054331_1280-1024x576.jpg)
You want to make the right choice for your company’s next mobile project, but it’s hard to find practical information in this debate. Almost every article points to a [Flutter](https://thenewstack.io/flutter-fever-adoption-grows-and-spreads-to-embedded-devices/) or [React Native](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) dev shop trying to convince you that their technology is the best. I promise you, this post is different.

In this article, I’ll ask and answer ten actionable questions that will help you identify the right technology for your specific use case so you can confidently say: *”I chose Expo/Flutter because of X, Y, and Z.”*

First, let’s set a quick baseline of Expo and Flutter, and then we can dive into the ten questions that will help you decide between them.

## What Is Flutter? What Is Expo?
First of all, [Expo is now the recommended framework ](https://reactnative.dev/docs/environment-setup)for [React Native](https://reactnative.dev/). Therefore, we will compare Expo with Flutter, as Expo is the most popular way to build React Native apps.

The simple truth is that Expo and Flutter are both great technologies!

Google introduced [Flutter](https://flutter.dev/) in 2017. It uses the [Dart ](https://dart.dev/)programming language. Flutter is a complete framework that allows you to build mobile, web, and desktop applications from a single codebase. It is known for its high performance and platform-identical design.

[Expo](https://expo.dev/) is a set of tools and services built around React Native, which was created by [Meta](https://www.meta.com/de/en/). Expo allows you to build mobile apps faster by writing JavaScript/TypeScript and JSX. It is known for its full ecosystem of services that help companies ship and iterate faster.
Flutter and React Native are open source technologies with large communities and ecosystems of tools and libraries.

Flutter follows a “write once, run everywhere” approach, while Expo follows a “learn once, write anywhere” approach.

What is the difference between these philosophies?

- For Flutter, this concept implies that your UI code is platform-independent and looks the same on all platforms. Apps can, in theory, run on every platform, such as embedded devices.
- For Expo, this means every developer who knows React can create platform-native apps using React Native without learning a new programming language.
So you see, both look great from the outside, but the devil is in the details.

And that’s why we need to ask the right questions to choose the right technology for your project.

## 10 Questions to Choose Between Expo and Flutter
### 1. Do You Have React/Dart Knowledge?
If you are a web developer with React knowledge, you will feel at home with Expo. Expo uses React Native, which uses React, so you can leverage your existing knowledge to build mobile apps.

This is a significant advantage if you want to get started quickly and avoid learning a new language like Dart or if you already have React packages you want to use in your mobile app.

On the other hand, if you are a Dart developer or have more experience with Flutter than React, you will feel more comfortable with Flutter.

More than answering this question alone is needed to decide, but it can help save time and resources when starting a new project or dealing with challenging requirements.

### 2. Do You Want To Access Native Platform APIs Directly?
Flutter and Expo allow you to build mobile apps without touching native code. However, they have different approaches to accessing and using native platform APIs.

Take the camera, for example.

In Flutter, the overlay with its controls is rendered by the Flutter framework itself rather than the underlying operating system.

In Expo, the camera is abstracted away, and you can use the `expo-camera`
package to render the native iOS and Android camera views.

While it looks like a minor difference, it can affect the critical requirements for some projects. You should ask yourself if you want to access the user experience provided by the Google and Apple teams or if you need the user interface to be identical across platforms.

Beyond using existing libraries, you can also write native [Expo Modules](https://docs.expo.dev/modules/native-module-tutorial/) or [Flutter Plugins ](https://docs.flutter.dev/platform-integration/platform-channels)to access native APIs directly.

However, managing Flutter channels can be more complex than writing Expo modules as you need to set up many files and handlers (which can also get messy) and [Expo modules can be easily bootstrapped using the CLI.](https://docs.expo.dev/modules/native-module-tutorial/)

Flutter’s ecosystem of plugins is also less extensive than the React Native community’s, so you might have a harder time finding a package that works for you.

So, if you expect to use niche native APIs or want access to new platform features as soon as they are released, you might want to choose Expo.

### 3. Do You Want Visually Identical Designs Across Platforms?
Flutter apps look and feel the same across all platforms. This is because Flutter uses its own [rendering engine ](https://docs.flutter.dev/resources/architectural-overview)Skia in the past, now [Impeller](https://docs.flutter.dev/perf/impeller) on iOS and widgets to draw the UI. This can be a good thing if you want a consistent brand look and feel across platforms, but it comes at the cost of not looking and feeling fully native to each platform.

Why?

Because all Flutter components (or widgets) have a specific, pre-defined styling, when Apple updates the iOS version and controls, Flutter components still render the same UI until the Flutter SDK and your app are updated some weeks/months later.

On the other hand, Expo uses the platform’s native components. This means the components are rendered by the platform itself, and your app will be native on each platform. This can be a good thing if you want to embrace each platform’s design guidelines and behavior.

Also, using platform-native components means having built-in accessibility that is out of the box, which is a big plus for Expo. After all, Google and Apple engineers spent years perfecting their components.

If you want the same design across platforms, choose Flutter. If you want adaptive styling that makes your users feel at home wherever they use your app, you should select Expo.

### 4. Do You Want a Web Version of Your App?
While Flutter technically allows targeting the [web,](https://flutter.dev/multi-platform/web) it is less mature than the mobile version.

Your whole app is rendered in a `canvas`
, which presents obstacles for SEO and accessibility because screen readers will have a tough time making sense of all the elements within the canvas.

Also, the web version of your app will not look and feel like an actual web app but more like a mobile app running in a browser. Usually, even [Flutter developers are no fans of this approach](https://www.reddit.com/r/FlutterDev/comments/180h020/why_is_flutter_not_as_popular_for_web_its_a_great/).

On the other hand, Expo can deliver a web version of your app that uses the DOM out of the box. This means you can build a mobile app and have a web version with minimal effort.

Using [Expo Router](https://docs.expo.dev/router/introduction/), you get file-based routing and can use the same components for your mobile and web app, resulting in universal applications.

This means you get the best of both worlds: a mobile app that looks and feels like a native app on each platform and a web app that looks and feels like an actual web app.

If you want a web version of your app, you should choose Expo.

### 5. Do You Want To Prototype Fast?
Flutter’s built-in UI components allow you to build stunning UIs fast. This is especially valuable if you are a solo developer because you can quickly build an MVP that looks like you hired a designer.

The only downside is that using [Material Design components](https://docs.flutter.dev/ui/widgets/material) while building an app that looks like a native iOS app is a bit more challenging (especially with adaptive styling for both platforms).

People also complain about React Native’s lack of missing UI components. If you want to build a custom UI, you have to build it yourself using the [StyleSheet API](https://reactnative.dev/docs/stylesheet) or add libraries like [NativeWind ](https://www.nativewind.dev/)bringing [TailwindCSS](https://tailwindcss.com/) to React Native or [Tamagui](https://tamagui.dev/) to your project.

Overall, you will spend a lot more time figuring out how to build your UI in React Native than in Flutter.

If you need to ship a prototype fast, you should choose Flutter.

### 6. Do You Want To Use Over-the-Air Updates?
The app store review process has friction. It can take days or sometimes even weeks to get your app reviewed and published. This can be a problem if you need to fix a critical bug or want to push a new feature quickly.

With Expo, you can use [EAS Update](https://docs.expo.dev/eas-update/introduction/) to directly send JS updates to your app’s end users. This service allows you to replace non-native pieces (JS, styling code, and assets) in your app without having to submit a new version to the stores.

This is an absolute game changer for major companies with many users. You can fix bugs and push new features quickly without the waiting time and uncertainty of the external review process.

Flutter does not have a built-in over-the-air update feature, given that Flutter apps are compiled into a binary that can’t be easily replaced. However, [Shorebird](https://shorebird.dev/) is a new service that promises the same for Flutter apps in its early days.

Also, the future of other over-the-air update services is unclear since Microsoft announced that the retirement of [App Center ](https://appcenter.ms/)could be more apparent.

If you plan to push updates to your users frequently or want to fix bugs in production quickly, choose Expo for your next project.

### 7. Do You Plan To Have a Team of Developers?
Finding or upskilling one developer is easy, but what if you want to scale your app and need a team to support it?

As React dominates the web, almost every web developer has some experience with React. This means you can easily find developers who can work on your Expo project with minimal learning time.

On the other hand, Flutter is a more niche technology simply because Dart is a niche language, while JavaScript is more universal. Flutter is growing in popularity but is still not as broadly adopted as React because of the language limitations. You will need help finding developers who can work on your Flutter project because Dart is practically only used in Flutter projects.

If you want to build a team of developers to support your app for years, choose Expo.

PS: If you want to learn React Native or upskill your team, check out [Galaxies. Dev for in-depth React Native video courses](https://galaxies.dev/).

### 8. Do You Want the Best Performance?
Almost every article you read tells you Flutter is faster than React Native.

And, sometimes, that’s true. It depends on the app.

Because Flutter uses its rendering engine, it can achieve excellent performance. But they are in the process of migrating from Skia, a mature rendering engine, to Impeller. It’s not clear what the impact on performance will be.

In the past, React Native suffered from the [bridge ](https://reactnative.dev/docs/communication-ios)between JavaScript and native code, which made it slower than Flutter. However, with the introduction of [TurboModules](https://reactnative.dev/blog/2021/09/13/turbomodules) and the [New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page), React Native has become much faster (take a look at these [performance benchmarks](https://github.com/reactwg/react-native-new-architecture/discussions/123) from 2023).

At the time of writing, the new architecture[ in React Native](https://reactnative.dev/docs/the-new-architecture/landing-page) was not yet the standard, and not all libraries were compatible with it.

On top of that, you can now also use[[React Native Skia](https://shopify.github.io/react-native-skia/) to use Skia as the rendering engine in your app, which can bring the performance of Expo on par with Flutter.

One question remains, though: do you need the best performance?

If you build a standard app, the performance difference between Flutter and Expo will not be noticeable to end users. Both technologies are fast enough and deliver a great user experience.

However, you might want to choose Flutter for the best performance when building a complex app with heavy animations like [Wonderous](https://flutter.gskinner.com/wonderous/). That being said, William Candillon – the creator of Skia, recently [demonstrated powerful app animations built with React Native](https://youtu.be/Pu-Zngp0JUU?si=9r_-oPHsH70pNidT).

To decide which technology “wins” performance, we must define how to measure performance. Is it simply speed? Is it the look and feel of scrolling? Crash rate? CPU usage?

Then, you must decide what performance is most important for your use case.

If you Google ” Flutter vs. React Native performance,” you’ll see a bunch of blogs that prefer Flutter. My advice is to be more nuanced and considerate in how you evaluate performance. Without current and objective public benchmarks, it’s impossible to evaluate in a binary way. Make the decision based on your team’s skills and your use case.

### 9. Do You Want an Ecosystem of Tools To Create, Review, and Submit Your App?
Expo is not only the recommended framework for React Native but also comes with various tools for teams and companies to build, test, and deploy their apps.

Iteration speed is critical when building a mobile app. Expo provides tools like [Expo Go](https://expo.dev/go) to test your app on your phone, [Expo CLI](https://docs.expo.dev/more/expo-cli/) to manage your project, and [Expo Orbit](https://expo.dev/orbit) to collaborate with your team using one-click build launches and simulator management.

Beyond that, you can optionally use the Expo Application Services (EAS):

[EAS Build](https://docs.expo.dev/build/introduction/)to build your app in the cloud, so you don’t have to worry about setting up build environments for iOS and Android.[EAS Submit](https://docs.expo.dev/submit/introduction/)to submit your app to the app stores without using Xcode or Android Studio.[EAS Update](https://docs.expo.dev/eas-update/introduction/)to push JS updates to your app directly to your end users.
For Flutter, you can use a service like[[Codemagic](https://codemagic.io/) to build, test, and deploy your app. However, it is less integrated than the Expo ecosystem and requires more setup and configuration.

If you want the best support for building, testing, and deploying your app with powerful automation that integrates with tools like GitHub, you should choose Expo.

### 10. Do You Want a Future-Safe Technology With an Active Community?
Flutter’s development is powered by Google, which has a [reputation](https://killedbygoogle.com/) [ending projects]. However, it’s a good sign that Google has been actively developing and using Flutter in their apps.

This means that Flutter has a clear roadmap and is actively developed by mostly Google engineers. While the Flutter community is growing, it is still not as big as the React Native community.

What would happen if Google decided to stop developing Flutter? Will the community continue to develop and maintain Flutter? These are questions you should ask yourself when choosing Flutter.

On the other hand, React Native is powered by the community. This means that the community drives the development of React Native and adds new features and updates.

While Meta is still actively developing React Native, the community plays a significant role in the development of React Native. Companies like [Microsoft ](https://microsoft.github.io/react-native-windows/)and [Shopify](https://shopify.github.io/flash-list/) are actively contributing to React Native and massive agencies like [Software Mansion](https://swmansion.com/), [Margelo](https://margelo.io/), [Infinite Red](https://infinite.red/), and [Callstack ](https://www.callstack.com/)are building tools and libraries for React Native in combination with the support from [Expo.](https://expo.dev/)

Even if Meta stopped developing React Native, the community would continue to develop and maintain React Native.

Select Expo if you want to choose a future-safe technology with an active community.

## Making Your Choice
Now that you have answered the ten questions, you should better understand which technology to choose for your next project.

Nobody said the choice is easy, right?

If you are still unsure, let me help you with a quick guideline:

**You should choose Expo if you:**
- Already have React experience or code
- Want to build web and mobile with one code base
- Want to use native platform components
- Need to access the latest native platform APIs
- Want code push
- Plan to build a future-proof app with a big team
**You should choose Flutter if you:**
- Have existing Dart developers or knowledge
- Need to prototype an interface very fast
- Want visually identical design across platforms
- Want to create “custom” app experiences closer to games
- Focus on desktop or embedded device apps as well
Remember, both technologies are great, and you can build amazing apps. The most important thing is to choose the technology that best fits your use case, stakeholders, and team.

## The Future of Flutter and Expo
The future of Flutter and Expo is bright. Both technologies are actively developed and maintained by their respective communities and companies, and new features and updates are added regularly.

Flutter is growing in popularity and is used by companies like Google, [Alibaba](https://flutter.dev/showcase/alibaba-group), and [BMW ](https://flutter.dev/showcase/bmw)to build mobile, web, and desktop applications that deliver custom app experiences.

Expo is used by companies like [Meta](https://reactnative.dev/showcase), [Microsoft](https://devblogs.microsoft.com/react-native/), and [Coinbase](https://www.coinbase.com/en-de/blog/optimizing-react-native) to build mobile apps that look and feel like native apps on each platform.

Evan Bacon’s blog also contains an extensive list of [apps built with React Native and Flutter](https://evanbacon.dev/blog/expo-2024)].

Overall, more big companies are choosing Expo over Flutter. The trend I’ve observed is that companies use Flutter to build employee experiences where it makes sense to have a visually identical experience across multiple devices for internal apps, and companies use Expo to build consumer experiences. These obviously aren’t absolutes. There are plenty of consumer-facing Flutter apps and internal Expo apps.

But if you’re building an app that you think could scale to the masses, you are better off with Expo, as you can quickly scale your app and team with [Expo](https://www.youtube.com/@galaxies_dev).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)