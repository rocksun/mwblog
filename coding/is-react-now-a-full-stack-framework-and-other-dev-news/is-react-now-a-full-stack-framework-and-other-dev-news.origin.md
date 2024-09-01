# Is React Now a Full Stack Framework? And Other Dev News
![Featued image for: Is React Now a Full Stack Framework? And Other Dev News](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
Maybe we’re not so much [living in a post-React world](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) as we are living with a new React paradigm: [React is becoming a full stack framework](https://www.robinwieruch.de/react-full-stack-framework) with the addition of React Server Components and Server Actions, software engineer and freelance developer [Robin Wieruch](https://www.linkedin.com/company/rwieruch/) argued recently.

“This marks just the beginning of full-stack development with React,” Wieruch wrote. “As developers start to access databases directly through Server Components and Server Actions, there will be a learning curve ahead to tame the complexities beyond simple CRUD applications.”

This will allow frontend developers to quickly master implementing backend architectures with layers, design patterns and best practices, Wieruch added.

## Claude Can Now Generate Artifact
[Artifacts give Claude AI users a dedicated window](https://www.anthropic.com/news/artifacts) to see, iterate and build on any work created in Claude. For developers, this provides a separate window to see code or to make architecture diagrams from codebases, according to the Claude team.
“Artifacts turn conversations with Claude into a more creative and collaborative experience,” the Claude blog stated. “With Artifacts, you have a dedicated window to instantly see, iterate, and build on the work you create with Claude.”

![A screenshot of Claude showing the Artifacts interface with Python code.](https://cdn.thenewstack.io/media/2024/08/234c2f0e-artifacts_claude.jpg)
Screenshot via Claude.ai

Artifacts are now available for all [Claude.ai](https://claude.ai/new) users across the platform’s Free, Pro, and Team plans. Artifacts can also be created and viewed on Claude’s iOS and Android models. It can also create:

- Code snippets
- Flowcharts
- SVG graphics
- Websites in single page React or HTML
- Interactive dashboards
- Insert image
The Anthropic post includes a video that describes how this feature was created and explores other use cases outside development, but for a deeper read on how it can be used to build web applications, check out [this post by Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/how-anthropic-built-artifacts), which explores in-depth the capabilities and creation of Artifacts.

“While the feature is small, it feels like it could a leap in using LLMs for collaborative work — as every Artifact can be shared, used by others, and remixed,” explained [Gergely Orosz](https://www.linkedin.com/in/gergelyorosz/?originalSubdomain=nl), who writes Pragmatic Engineer.

## Catching More Bugs With TypeScript
The [release candidate for TypeScript 5.6](https://devblogs.microsoft.com/typescript/announcing-typescript-5-6-rc/) is out, and [Microsoft TypeScript Product Manager Daniel Rosenwasser](https://www.linkedin.com/in/daniel-rosenwasser-b56b7837/) offered a roundup of what’s new, including disallowed nullish and truthy checks for catching more bugs. Rosenwasser lists several examples of code that do not do what the author intended, but are still valid JavaScript code. Previously, TypeScript would just accept these examples, he wrote. No more.

“But with a little bit of experimentation, we found that many many bugs could be caught from flagging down suspicious examples like above,” he wrote. “In TypeScript 5.6, the compiler now errors when it can syntactically determine a truthy or nullish check will always evaluate in a specific way.”

“But with a little bit of experimentation, we found that many many bugs could be caught from flagging down suspicious examples like above.”

— Daniel Rosenwasser, Microsoft TypeScript Product Manager
TypeScript 5.6 also introduces a new type called IteratorObject and the post provides code examples of how it’s defined.

Rosenwasser writes that there is an AsyncIteratorObject type for parity.

“AsyncIterator does not yet exist as a runtime value in JavaScript that brings the same methods for AsyncIterables, but it is an active proposal and this new type prepares for it,” he explained.

## Project IDX Combines Code Editor With Languages and Tools
[Project IDX](https://thenewstack.io/project-idx-googles-new-web-and-mobile-app-development-ide/) is a browser-based development experience built on Google Cloud Workstations and powered by [Codey](https://lablab.ai/tech/google/codey), a foundational AI model trained on code and built on PaLM 2. Its goal is to make it easier to build, manage and deploy full-stack web and multiplatform applications, with popular frameworks and languages.
Project IDX seeks to unify the two main parts of a development environment: The code editor and the languages and tools required to build and run the code, the team noted in a recent [reflection on developing Project IDX over past year](https://idx.dev/blog/article/a-year-of-project-idx).

“At the heart of Project IDX is our conviction that you should be able to develop from anywhere, on any device, with the full fidelity of local development,” The Project IDX team wrote in introducing it last year. “Every Project IDX workspace has the full capabilities of a [Linux-based VM](https://thenewstack.io/deploying-microsofts-new-linux-distribution-as-a-vm-is-not-easy/), paired with the universal access that comes with being hosted in the cloud, in a data center near you.”

This yearly update noted the Project IDX team had three areas of focus:

[Improve developer productivity](https://thenewstack.io/developer-productivity-metrics-drive-continuous-improvement/)with Generative AI tooling backed by Gemini.- Redefine what it means to “get started fast” with project templates and integration.
- Bring
[native mobile app development](https://thenewstack.io/beta-solution-helps-frontend-developers-make-native-mobile-apps/)to the browser with Flutter, React Native, and soon, Android Studio.
The team has integrated generative AI features, provided by Gemini, into the code.

“These provide context-aware code suggestions, unit test generation, comment writing, programming language conversions, and technical question answering — all without ever leaving your workflow,” the post noted. “On the development environment side, we’ve built a robust system based on Nix, allowing for effortless environment configurations. With minimal setup, you can customize your Project IDX workspace with the precise languages, tools, and extensions you need to hit the ground running.”

Nix is a functional package manager that assigns unique identifiers to each dependency, which ultimately means an environment can contain multiple versions of the same dependency, seamlessly, the post added.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)