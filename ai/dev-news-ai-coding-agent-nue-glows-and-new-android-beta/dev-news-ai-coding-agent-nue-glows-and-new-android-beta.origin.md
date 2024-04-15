# Dev News: AI Coding Agent, Nue Glows, and New Android Beta
![Featued image for: Dev News: AI Coding Agent, Nue Glows, and New Android Beta](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
[CodiumAI](https://www.codium.ai/) released a new AI coding agent that’s designed to work with code completion tools last week. Along with the agent, CodiumAI also released *its own* code completion tool.
The AI tool is called Codiumate Agent and it’s available for free download for either
[JetBrains IDEs](https://plugins.jetbrains.com/plugin/21206-codiumate--code-test-and-review-with-confidence--by-codiumai) and [Codiumate for VS Code](https://marketplace.visualstudio.com/items?itemName=Codium.codium). It suggests relevant tests, drafts documentation, provides guidance on best practices and identifies code duplicates without prompting.
“This announcement builds upon the recent success of CodiumAI’s
[AlphaCodium research](https://github.com/Codium-ai/AlphaCodium), which proposed a new approach to code generation by LLMs, one built upon a test-based, multi-stage iterative flow to solve code problems,” the company noted in its press release. “AlphaCodium’s performance on the CodeContest’s benchmark showed that its performance improved GPT-4’s accuracy from 19% to 44%.”
## Nue Offers Glow for Syntax Highlighting
The makers of
[Nue.js released Glow](https://nuejs.org/blog/introducing-glow), which Nue creator and frontend developer [Tero Piirainen](https://www.linkedin.com/in/tipiirai/?originalSubdomain=fi) called “a new take on syntax highlighting.”
Glow focuses only on aesthetics — and how your code looks. It makes all languages work with your brand colors by adjusting just a handful of CSS variables. It’s also microscopic in size, Piirainen claims.
“Glow is orders of magnitude smaller than the mainstream alternatives,” he wrote. “We’re talking 5K instead of 5M. It’s by far the smallest implementation available.”
It’s designed to compete with the likes of Shiki.
[Nue](https://thenewstack.io/dev-news-a-nue-frontend-dev-tool-panda-and-bun-updates/), of course, has built-in support for Glow, he added, although Glow can also be used as a standalone library.
## JetBrains Launches Enterprise IDE Services
JetBrains announced a new
[IDE Services suite for enterprises](https://www.jetbrains.com/ide-services/) that combines five products and services available separately or as a bundle. Included are:
- IDE Provisioner, a centralized and streamlined IDE management tool for pushing appropriate versions, settings and IDE plugins to developers across the organization to reduce the risks associated with unapproved or outdated versions;
- AI Enterprise, which provides developers with AI-based productivity features and gives companies control over security, spending, choosing the best-in-class LLM provider, and efficiency measures;
- License Vault, a tool that
[automates the distribution of the JetBrains IDE](https://thenewstack.io/gitpod-brings-automated-environments-to-jetbrains-ides/)licenses for the organization;
- Code With Me Enterprise, which supports real-time collaborative programming for “security‑conscious organizations”; and
- CodeCanvas, a self-hosted remote development environment orchestrator.
![Jetbrains IDE Services dashboard](https://cdn.thenewstack.io/media/2024/04/00bf51e5-jetbrainsideservices.png)
Image courtesy of JetBrains
“JetBrains IDE Services delivers a sleek control panel that simplifies management of developer tools while making it practically invisible to developers,” Ernst Haagsman, head of product in JetBrains IDE Services, said in a prepared statement.
The company anticipates the introduction of a managed cloud platform “in the near future,” Haagsman added.
## Android 15 First Beta Released
Thursday,
[first beta of Android 15](https://developer.android.com/about/versions/15/overview#pixel), opening it up to developers and early adopters in preparation for a consumer release at some point in the future.
Among the updates: Apps are displayed edge-to-edge by default on Android 15 devices, which means developers no longer need to explicitly call
Window.setDecorFitsSystemWindows(false) or
enableEdgeToEdge() to show their content behind the system bars. That said, Google does recommend continuing to call
enableEdgeToEdge() to get the edge-to-edge experience on earlier OS releases. Also, to assist with going edge-to-edge, many of the Material 3
[composables handle insets](https://developer.android.com/develop/ui/compose/layouts/insets#inset-handling) for you, based on how the composables are placed in an app according to the Material specifications, Google noted.
Android 15 includes improvements to streamline performance by including OS-level support for app archiving and unarchiving so that users can free up space on their device from infrequently used apps while maintaining their data. The beta also prioritizes privacy and security by offering an OS-level API for end-to-end encryption for contact keys, so users can securely manage and verify other people’s contact information.
Finally, Android TalkBack will now support Braille displays that use human interface devices over USB and Bluetooth to improve accessibility.
Any Pixel device can download Android 15 and get future Android 15 Beta and feature drop updates over the air, Google added. There’s also an
[Android Emulator](https://developer.android.com/about/versions/15/get) that developers can use to test apps on Android 15.
## Astro 4.6 Releases
[Astro 4.6 released](https://astro.build/blog/astro-460/) Thursday, with a new manual routing strategy for internationalization.
“This new strategy allows you to take total control over the routing of your internationalized Astro website, for cases where the default routing strategy doesn’t quite meet your needs,” the
[Astro](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/) team wrote.
As an alternative, it’s possible to import Astro’s own middleware logic using the new middleware function from astro:i18n to build upon the default routing strategy, they added. Code samples are provided in the post.
The new release also allows
[developers to move](https://thenewstack.io/tips-for-developers-moving-sectors-in-the-software-industry/) the Dev toolbar to different positions at the bottom of the screen. Other changes:
- The release adds experimental partial support for CSRF protection, although that may change in future releases;
- Cookie improvements, in that Astro’s helper for deleting cookies now allows setting more cookie attributes instead of just the path and domain attributes; and
- Deprecated support for older versions of
[Node.js](https://thenewstack.io/dev-news-django-updates-storybook-7-6-and-node-js-20-beta/)lower than 18.17.1, Node.js 19 and versions of Node.js 20 lower than 20.3.0. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)