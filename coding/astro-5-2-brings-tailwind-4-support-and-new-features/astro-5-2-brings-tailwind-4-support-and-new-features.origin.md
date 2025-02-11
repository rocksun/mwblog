# Astro 5.2 Brings Tailwind 4 Support and New Features
![Featued image for: Astro 5.2 Brings Tailwind 4 Support and New Features](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
Web framework [Astro released version 5.2](https://astro.build/blog/astro-520/) Thursday, with support for Tailwind 4.

The team wrote about the new release, noting that [Tailwind CSS](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/) now offers a @tailwindcss/vite plugin that can be directly added to an Astro project.

“This simplifies the Tailwind experience in Astro and is now the recommended way to use Tailwind 4 in [Astro](https://thenewstack.io/new-astro-releases-incorporates-sessions-new-astro-actions-tools/),” the team wrote. “Astro 5.2 adds native support for this Vite plugin, and the Astro add tailwind command will now add the plugin to your Astro config and create a default CSS file that imports Tailwind styles.”

Astro 5.2 also includes a new way to access config values in pages, better trailing slash handling, and support for external redirects, the team wrote in a blog post introducing the new release.

Also this release introduces the following as experimental:

- astro:config, which provides a single way to read the most useful configuration options from anywhere inside a project; and
- disable React streaming, which disables React streaming, an action that can be useful if a developer is using a library that is not compatible with streaming, such as in many CSS-in-JS libraries.
## Mirai: A Server-Driven UI Framework for Flutter
[Mirai is a new server-driven UI framework for Flutter](https://medium.com/buildmirai/introducing-mirai-a-server-driven-ui-framework-for-flutter-d020fd0c387d) introduced recently by developer [Divyanshu Bhargava](https://www.linkedin.com/in/divyanshub024/?originalSubdomain=ae), who specializes in Flutter development.
Server-driven UI (SDUI) decouples the UI from the codebase and the client, Bhargava wrote. Instead of the UI being hard-coded into the app, the server drives the UI, he explained.

“Think of it like a browser rendering a website,” he wrote. “Your browser doesn’t know ahead of time what content it’s going to display — it just knows how to interpret and render tags. Similarly, in SDUI, the app is equipped to render widgets or components sent by the server, making the UI dynamic, flexible, and completely server-controlled.”

The benefits are that developers can send updates on the fly without delays and approvals, he continued. In server-driven UI, the server defines the app’s UI, typically in a lightweight format like [JSON](https://thenewstack.io/how-to-use-json-in-your-python-code/). The client or app receives these definitions and renders the UI dynamically, he continued. But building Server-Driven UI is hard, he warned, which is where the open source framework [Mirai](https://github.com/BuildMirai/mirai) comes in.

“With Mirai, you can build stunning, cross-platform applications dynamically, using JSON to define your UI in real time,” he wrote. Mirai makes it easier to personalize UIs and simplifies maintenance, he wrote.

It also supports [A/B testing](https://thenewstack.io/a-perfect-match-a-b-testing-and-business-success/), because developers can experiment with multiple UI versions in real-time by serving variant payloads directly from the server, he added.

## Android 16 Beta Available
[Android released the beta for Android 16](https://android-developers.googleblog.com/2025/01/first-beta-android16.html?m=1) last Thursday. It features support for future app adaptivity, live updates, and the Advanced Professional Video format, which is designed to be used for professional-level high-quality video recording and post-production, according to the Android Developer blog.
One interesting change is that Android 16 is phasing out the ability for apps to restrict screen orientation and resizability on large screens.

“This is similar to features OEMs have added over the last several years to large screen devices to allow users to run apps at any window size and aspect ratio,” the blog post stated. “On screens larger than 600dp wide, apps that target [API level 36](https://apilevels.com/) will have app windows that resize; you should check your apps to ensure your existing UIs scale seamlessly, working well across portrait and landscape aspect ratios.”

Manifest attributes and APIs that restrict orientation and resizing will be ignored for apps — but not games — on large screens, they added.

Android provides [frameworks, tooling and libraries](https://developer.android.com/develop/ui/compose/layouts/adaptive) to help with this.

## Vercel Acquires Tremor
Vercel announced last week that [it has acquired Tremor](https://vercel.com/blog/vercel-acquires-tremor), an open source library built on top of [React](https://thenewstack.io/new-york-public-library-on-choosing-react-to-rebuild-website/), Tailwind CSS, and [Radix](https://www.radix-ui.com/). It’s a way for the company to invest in open source React components, according to [Tom Occhino](https://www.linkedin.com/in/tomocchino/), Vercel’s chief product officer.

Tremor includes 35 unique components and 300 blocks that can be copy-pasted to build visually rich and interactive dashboards, wrote Occhino.

Tremor staff and its cofounders, [Severin Landolt](https://www.linkedin.com/in/b6b682ce450f9e1c8717c24cdb1c988a3ac717b6cbe6e1373a177119a742a434/) and [Christopher Kindl](https://www.linkedin.com/in/kindl/?originalSubdomain=ch), will join Vercel’s Design Engineering team, where they will work on UI components for Vercel Dashboard, v0, and other projects.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)